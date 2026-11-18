#!/usr/bin/env python3
"""Scaffold an interlinear gloss file for one (root-text, translation) pair.

Reads two markdown files that share an Obsidian block-ID scheme and writes a
gloss file under ``2-RAILS/Bilingual-Glossaries/Raw/`` with one ``gloss`` code
block per paired block. The format is horizontal: \gla (source), \glb (gloss),
and \ex (translation).

If the output file already exists, existing gloss lines are preserved when
their Pāli token count matches.

Usage:

    python3 scaffold_gloss.py <root-text>.md <translation>.md <output>.md

    python3 scaffold_gloss.py --validate <gloss-file>.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$")
HEADING_RE = re.compile(r"^#{1,6}\s")
FM_FIELD_RE = lambda name: re.compile(rf"^{name}:\s*(.+?)\s*$", re.MULTILINE)

# Tokens we strip from the end of a source token before placing it on gla.
TRAILING_PUNCT = ".,;:!?"
# Tokens we strip from the beginning.
LEADING_PUNCT = "([{"


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    body = text[match.end():]
    fields = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields, body


def parse_blocks(path):
    """Return {block_id: paragraph_text} for ``path``. Skip headings and frontmatter."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    blocks = {}
    order = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph or HEADING_RE.match(paragraph):
            continue
        match = BLOCK_ID_RE.search(paragraph)
        if not match:
            continue
        block_id = match.group(1)
        body = paragraph[: match.start()].rstrip()
        if block_id not in blocks:
            order.append(block_id)
        blocks[block_id] = body
    return blocks, order


def tokenise_source(text):
    """Split source text into gloss tokens, stripping editorial markup."""
    cleaned = re.sub(r"\[[^\]]*\]", "", text)
    cleaned = re.sub(r"\([^)]*\)", "", cleaned)
    cleaned = re.sub(r"^\s*\d+\.\s*", "", cleaned)
    tokens = []
    for raw in cleaned.split():
        token = raw.strip(TRAILING_PUNCT + LEADING_PUNCT + "—–\"\'")
        if not token:
            continue
        if re.fullmatch(r"\d+", token):
            continue
        tokens.append(token)
    return tokens


def normalise_free_translation(text):
    """Collapse internal whitespace and newlines; preserve sentence punctuation."""
    return re.sub(r"\s+", " ", text).strip()


def parse_existing_gloss(text):
    """Return {block_id: [gloss_tokens]}.

    Used when refreshing an existing gloss file to preserve filled lines.
    """
    out = {}
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        
        # Extract \glb line from ```gloss block
        gloss_match = re.search(r"```gloss\s*\n(.*?)\n```", section, re.DOTALL)
        if gloss_match:
            lines = gloss_match.group(1).strip().splitlines()
            for line in lines:
                if line.startswith("\\glb"):
                    glb_tokens = line[4:].strip().split()
                    if glb_tokens:
                        out[block_id] = glb_tokens
                        break
    return out


def build_gloss_block(block_id, gla_tokens, free_translation, existing_glb_tokens):
    """Render the horizontal ```gloss``` block."""
    lines = ["```gloss"]
    
    # gla line
    lines.append(f"\\gla    {'   '.join(gla_tokens)}")
    
    # glb line
    existing = existing_glb_tokens.get(block_id, [])
    if len(existing) == len(gla_tokens):
        glb_line = "   ".join(existing)
    else:
        glb_line = "   ".join(["--"] * len(gla_tokens))
    lines.append(f"\\glb    {glb_line}")
    
    # ex line
    lines.append(f"\\ex     {free_translation}")
    
    lines.append("```")
    return "\n".join(lines)


def scaffold(source_path, target_path, output_path):
    source_fm, _ = parse_frontmatter(source_path.read_text(encoding="utf-8"))
    target_fm, _ = parse_frontmatter(target_path.read_text(encoding="utf-8"))
    source_blocks, order = parse_blocks(source_path)
    target_blocks, _ = parse_blocks(target_path)

    source_lang = source_fm.get("lang_tag", source_fm.get("language", "src"))
    target_lang_tag = target_fm.get("lang_tag", target_fm.get("language", "tgt"))
    target_language = target_fm.get("language", target_lang_tag)
    translator = target_fm.get("translator", "")

    existing = {}
    if output_path.exists():
        try:
            existing = parse_existing_gloss(output_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"warning: could not re-parse existing {output_path}: {exc}", file=sys.stderr)

    blocks_rendered = 0
    skipped_target_missing = 0
    skipped_source_missing = 0

    out_lines = []
    out_lines.append("---")
    out_lines.append(f"source_file: 1-SOURCES/Text/{source_path.name}")
    out_lines.append(f"source_language: {source_lang}")
    # translations sit in language subfolders (1-SOURCES/Translations/<Language>/<file>.md): keep the real vault path
    _tp = target_path.resolve().parts
    target_rel = ("/".join(_tp[_tp.index("1-SOURCES"):]) if "1-SOURCES" in _tp
                  else f"1-SOURCES/Translations/{target_path.name}")
    out_lines.append(f"target_file: {target_rel}")
    out_lines.append(f"target_language: {target_language}")
    out_lines.append(f"target_lang_tag: {target_lang_tag}")
    if translator:
        out_lines.append(f"translator: {translator}")
    out_lines.append("total_verses: __PLACEHOLDER__")
    out_lines.append("status: draft")
    out_lines.append("---")
    out_lines.append("")
    title = f"Interlinear gloss — {source_lang} → {target_language} ({translator})"
    out_lines.append(f"# {title}")
    out_lines.append("")

    for block_id in order:
        source_text = source_blocks.get(block_id, "")
        target_text = target_blocks.get(block_id, "")
        if not source_text:
            skipped_source_missing += 1
            continue
        if not target_text.strip() or target_text.strip() == "-":
            skipped_target_missing += 1
            continue
        gla_tokens = tokenise_source(source_text)
        if not gla_tokens:
            continue
            
        free_t = normalise_free_translation(target_text)
        block = build_gloss_block(block_id, gla_tokens, free_t, existing)
        out_lines.append(f"## ^{block_id}")
        out_lines.append("")
        out_lines.append(block)
        out_lines.append("")
        blocks_rendered += 1

    rendered = "\n".join(out_lines).replace("__PLACEHOLDER__", str(blocks_rendered))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    return {
        "blocks_rendered": blocks_rendered,
        "skipped_target_missing": skipped_target_missing,
        "skipped_source_missing": skipped_source_missing,
    }


def validate(gloss_path):
    text = gloss_path.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    errors = []
    checked = 0
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        gloss_match = re.search(r"```gloss\s*\n(.*?)\n```", section, re.DOTALL)
        if not gloss_match:
            errors.append(f"{block_id}: missing gloss block")
            continue
        checked += 1
        lines = gloss_match.group(1).strip().splitlines()
        gla_count = 0
        glb_count = 0
        for line in lines:
            if line.startswith("\\gla"):
                gla_count = len(line[4:].strip().split())
            elif line.startswith("\\glb"):
                glb_count = len(line[4:].strip().split())
        
        if gla_count != glb_count:
            errors.append(f"{block_id}: column mismatch (gla={gla_count}, glb={glb_count})")
            
    return checked, errors


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", metavar="FILE", help="Validate an existing gloss file")
    parser.add_argument("source", nargs="?", type=Path, help="Root-text markdown file")
    parser.add_argument("target", nargs="?", type=Path, help="Translation markdown file")
    parser.add_argument("output", nargs="?", type=Path, help="Output gloss file")
    args = parser.parse_args(argv[1:])

    # Determine vault root relative to this script's directory
    script_dir = Path(__file__).resolve().parent
    if len(script_dir.parents) >= 4:
        vault_root = script_dir.parents[3]
    else:
        vault_root = Path(".")

    def resolve_path(p: Path) -> Path:
        if p.exists():
            return p
        vp = vault_root / p
        if vp.exists():
            return vp
        return p

    if args.validate:
        validate_path = resolve_path(Path(args.validate))
        checked, errors = validate(validate_path)
        if errors:
            for err in errors:
                print(f"  {err}", file=sys.stderr)
            print(f"FAIL — {len(errors)} errors across {checked} blocks", file=sys.stderr)
            return 1
        print(f"OK — {checked} blocks all valid")
        return 0

    if not (args.source and args.target and args.output):
        parser.print_help(sys.stderr)
        return 2

    source_path = resolve_path(args.source)
    target_path = resolve_path(args.target)
    
    # For output path, resolve relative to vault root if parent doesn't exist locally but exists in vault
    output_path = args.output
    if not output_path.parent.exists():
        vp = vault_root / output_path
        if vp.parent.exists():
            output_path = vp

    print(f"Vault root detected at: {vault_root.resolve()}")
    print(f"Using source: {source_path}")
    print(f"Using target: {target_path}")
    print(f"Using output: {output_path}")

    stats = scaffold(source_path, target_path, output_path)
    print(
        f"Wrote {output_path}: blocks={stats['blocks_rendered']} "
        f"skipped_target_missing={stats['skipped_target_missing']} "
        f"skipped_source_missing={stats['skipped_source_missing']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
