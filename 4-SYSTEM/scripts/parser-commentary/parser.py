#!/usr/bin/env python3
"""Parse linter output for commentary files and produce API-ready payloads.

Commentary content segments default to type ``paragraph`` (not verse).
Always builds alignment.json from Obsidian root-text transclusions.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


OUTPUT_DIR = Path(__file__).parent / "output"


def _out_dir(stem):
    """Each source file gets its own folder: output/<stem>/<stem>.<kind>.json."""
    out_dir = OUTPUT_DIR / stem
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir

YAML_PROPS_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
# Headers: ^n, ^n-n, ^n-n-n, ^n-n-n-… (any depth). Content: max ^n-n-n (3 parts).
REF_RE = re.compile(r'(\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\s*$')
VERSE_REF_MAX_PARTS = 3
ROMAN_RE = re.compile(r'^[IVXLCDM]+$')
VERSE_X_RE = re.compile(r'\d+[xX]\d+')
TRANSCLUSION_RE = re.compile(r'^\s*!\[\[.*?#\^.*?\]\]\s*$')
_TRANS_REF_RE = re.compile(r'!\[\[.*?#\^([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\]\]')
_WYLIE_RE = re.compile(r"'[a-zA-Z]")
NBSP = "\u00a0"
ZERO_WIDTH = "\u200b\u200c\u200d\u2060\ufeff"
_SMALL_TAG_RE = re.compile(r"</?small>", re.IGNORECASE)
_BLANK_CHARS = " \t\r" + NBSP + ZERO_WIDTH


def _clean_text(text):
    """Clean the parsed copy of a source file. Source files are never modified.

    Drops <small> tags (the gloss text stays) and turns non-breaking spaces
    into ordinary spaces.
    """
    return _SMALL_TAG_RE.sub("", text).replace(NBSP, " ")


def _is_blank(line):
    """True when a line holds nothing but spacing, including zero-width marks."""
    return not line.strip(_BLANK_CHARS)


def _rstrip_line(line):
    """Trailing spacing off, zero-width marks included."""
    return line.rstrip(_BLANK_CHARS)


def _ref_part_count(ref):
    """Count hyphen-separated parts in a ^ref (caret stripped)."""
    return len(ref.lstrip("^").split("-")) if ref else 0


def _wylie_to_unicode(text, lang_tag):
    if lang_tag != "bo":
        return text
    if not text or any("ༀ" <= c <= "࿿" for c in text):
        return text
    if not _WYLIE_RE.search(text):
        return text
    try:
        import pyewts as _pyewts
        converter = _pyewts.pyewts()
        converted = converter.toUnicode(text)
        if converted and converted.strip():
            return converted
    except ImportError:
        pass
    return text


def _is_empty(value):
    if value is None:
        return True
    if isinstance(value, str) and not value.strip():
        return True
    if isinstance(value, (list, dict)) and not value:
        return True
    return False


def _read_source(path):
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("PyYAML is required: pip install pyyaml") from exc
    text = _clean_text(
        path.read_bytes().replace(b'\x00', b'').decode("utf-8", errors="replace")
    )
    m = YAML_PROPS_RE.match(text)
    if not m:
        raise ValueError("no YAML properties found")
    data = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return data, body


def _resolve_root_text_path(val, source_path):
    val_path = Path(val)
    for base in [source_path.parent, *source_path.parents]:
        candidate = base / val_path
        if candidate.exists():
            return candidate
    name = val_path.name
    for base in source_path.parents:
        matches = list(base.rglob(name))
        if matches:
            return matches[0]
    return None


def _extract_blocks(body, warn=True):
    blocks = []
    for raw in re.split(r'\r?\n[ \t]*\r?\n', body.strip()):
        block = raw.strip()
        if not block:
            continue
        lines = [l.rstrip('\r') for l in block.split('\n')]
        # A line of zero-width characters only looks empty but does not split
        # the block. Keep the block whole and say so.
        if warn and any(_is_blank(l) and l.strip() for l in lines):
            print(
                f"  WARN block {len(blocks) + 1}: a line holds only zero-width characters — "
                "block kept whole; its parts may each need their own block ID",
                file=sys.stderr,
            )
        is_header = lines[0].lstrip().startswith('#')
        ref = None
        for line in reversed(lines):
            stripped = line.rstrip()
            if stripped:
                m = REF_RE.search(stripped)
                if m:
                    ref = m.group(1)
                break
        blocks.append({"ref": ref, "is_header": is_header, "lines": lines, "raw": block})
    return blocks


def _heading_level(line):
    """Number of leading '#' characters of a heading line."""
    stripped = line.lstrip()
    return len(stripped) - len(stripped.lstrip('#'))


def _infer_segment_type(ref_no_caret, doc_default):
    if not ref_no_caret:
        return doc_default
    if ref_no_caret[0].upper() == 'T':
        return "top_segment"
    parts = ref_no_caret.split('-')
    first = parts[0]
    if ROMAN_RE.match(first):
        return "front_matter"
    # Middle (or any) Roman part → front_matter (Abhidhamma book-Roman-N)
    for part in parts:
        base = re.sub(r'[xX]\d+$', '', part)
        if ROMAN_RE.match(base):
            return "front_matter"
    # x-suffix / U-leaf stay content; commentaries use paragraph default
    if VERSE_X_RE.search(ref_no_caret):
        return doc_default
    last = parts[-1] if parts else ""
    if re.match(r'^U\d+$', re.sub(r'[xX]\d+$', '', last)):
        return doc_default
    for part in parts:
        base = re.sub(r'[xX]\d+$', '', part)
        if part and not base.isdigit() and not ROMAN_RE.match(base):
            if re.match(r'^[a-z]+$', base):
                return "back_matter"
    return doc_default


# ---------------------------------------------------------------------------
# Function 1: extract text_input
# ---------------------------------------------------------------------------

def extract_text_input(lint_path, source_path=None):
    data = json.loads(
        lint_path.read_bytes().replace(b'\x00', b'').decode("utf-8", errors="replace")
    )
    text_input = data.get("text_input") or data.get("resolved")
    if text_input is None:
        raise ValueError(f"no text_input found in {lint_path.name}")
    clean = {k: v for k, v in text_input.items() if not _is_empty(v)}

    if "alt_titles" not in clean:
        print("  WARN alt_titles: missing — ignored", file=sys.stderr)

    contribs = clean.get("contributions")
    if contribs is None:
        print("  WARN contributions: author/translator missing — ignored", file=sys.stderr)
    elif isinstance(contribs, list):
        kept = []
        for i, entry in enumerate(contribs):
            if not isinstance(entry, dict):
                print(f"  WARN contributions[{i}]: invalid entry — skipped", file=sys.stderr)
                continue
            role = entry.get("role", "contributor")
            if entry.get("type") == "ai":
                if entry.get("id") or entry.get("ai_id"):
                    kept.append(entry)
                else:
                    print(
                        f"  WARN {role}: AI contributor missing id — skipped",
                        file=sys.stderr,
                    )
                continue
            if entry.get("id") or entry.get("bdrc_id"):
                kept.append(entry)
            else:
                print(
                    f"  WARN {role}: not found (no id) — skipped",
                    file=sys.stderr,
                )
        if kept:
            clean["contributions"] = kept
        else:
            clean.pop("contributions", None)
            if contribs:
                print(
                    "  WARN contributions: none had resolvable ids — omitted",
                    file=sys.stderr,
                )

    # Named after the source file, not the lint file.
    if source_path is not None:
        stem = source_path.stem
    else:
        stem = lint_path.stem
        if stem.endswith(".lint.errors"):
            stem = stem[: -len(".lint.errors")]
        elif stem.endswith(".lint"):
            stem = stem[: -len(".lint")]
    out_path = _out_dir(stem) / f"{stem}.text.json"
    out_path.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Function 2: build edition
# ---------------------------------------------------------------------------

def _build_content_and_segmentation(blocks, doc_default):
    parts = []
    seg_list = []
    headings = []
    pos = 0

    for block_num, block in enumerate(blocks, start=1):
        ref = block["ref"]
        raw_lines = block["lines"]
        is_header = block["is_header"]

        content_lines = [l for l in raw_lines if not TRANSCLUSION_RE.match(l)]
        # Pure transclusion block — silently skip, used for alignment only
        if all(_is_blank(l) for l in content_lines):
            continue

        if not ref:
            print(f"  WARN block {block_num}: no reference marker — skipped", file=sys.stderr)
            continue
        ref_no_caret = ref[1:] if ref.startswith("^") else ref

        if is_header:
            # Headings are not part of the edition: no segment, no text in
            # content. They are recorded only to build the TOC.
            text = raw_lines[0].lstrip().lstrip('#').strip()
            ref_idx = text.rfind(ref)
            if ref_idx != -1:
                text = text[:ref_idx].rstrip()
            if not text:
                continue
            headings.append({
                "level": _heading_level(raw_lines[0]),
                "title": text,
                "reference": ref_no_caret,
                "offset": pos,
            })
            continue

        if _ref_part_count(ref) > VERSE_REF_MAX_PARTS:
            print(
                f"  WARN block {block_num}: reference {ref!r} has {_ref_part_count(ref)} parts; "
                f"content segments allow at most ^n-n-n ({VERSE_REF_MAX_PARTS} parts) — skipped",
                file=sys.stderr,
            )
            continue

        last_nonempty_idx = -1
        for i in range(len(content_lines) - 1, -1, -1):
            if not _is_blank(content_lines[i]):
                last_nonempty_idx = i
                break
        line_spans = []
        for i, raw_line in enumerate(content_lines):
            text = _rstrip_line(raw_line)
            if i == last_nonempty_idx:
                ref_idx = text.rfind(ref)
                if ref_idx != -1:
                    text = text[:ref_idx].rstrip()
            if not text:
                continue
            start = pos
            parts.append(text)
            pos += len(text)
            line_spans.append({"start": start, "end": start + len(text)})
        seg_type = _infer_segment_type(ref_no_caret, doc_default)
        seg_list.append({"lines": line_spans, "type": seg_type, "reference": ref_no_caret})

    return "".join(parts), seg_list, headings


def build_edition(source_path, lint_path):
    fm, body = _read_source(source_path)
    blocks = _extract_blocks(body)

    # Commentaries are paragraph-segmented (not verse)
    doc_default = "paragraph"

    content_str, seg_list, headings = _build_content_and_segmentation(blocks, doc_default)

    edition_type = fm.get("edition_type", "critical")
    source_url = (
        fm.get("source") or fm.get("source_url") or fm.get("gretil_url")
        or fm.get("dsbc_url") or fm.get("suttacentral_id") or ""
    )
    metadata = {"type": edition_type, "source": source_url}

    out = {
        "metadata": metadata,
        "content": content_str,
        "segmentation": {"segments": seg_list},
    }

    stem = source_path.stem
    out_path = _out_dir(stem) / f"{stem}.edition.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, out, headings


# ---------------------------------------------------------------------------
# Function 3: build TOC
# ---------------------------------------------------------------------------

def build_toc(source_path, edition_result, headings):
    """Build the TOC from heading records (headings are not edition segments).

    A section starts at its heading's offset in content and ends at the offset
    of the next heading with level <= its own, else at the end of content. A
    heading followed directly by such a heading gets an empty span.
    """
    fm, _ = _read_source(source_path)
    lang_tag = fm.get("lang_tag") or "en"

    content_len = len(edition_result["content"])

    title_nodes = []
    for heading in headings:
        title = heading["title"]
        if heading["level"] > 6:
            # Obsidian renders six heading levels; deeper ones are often bolded
            # to look like headings. That bold is not part of the title.
            title = title.replace("**", "").strip()
        title_nodes.append({
            "level": heading["level"],
            "span_start": heading["offset"],
            "title": _wylie_to_unicode(title, lang_tag),
            "ref": heading["reference"],
        })

    for i, node in enumerate(title_nodes):
        span_end = content_len
        for j in range(i + 1, len(title_nodes)):
            if title_nodes[j]["level"] <= node["level"]:
                span_end = title_nodes[j]["span_start"]
                break
        node["span_end"] = span_end

    def _nest(nodes, idx, parent_level):
        sections = []
        i = idx
        while i < len(nodes):
            node = nodes[i]
            if node["level"] <= parent_level:
                break
            if node["level"] == parent_level + 1:
                section = {
                    "title": {lang_tag: node["title"]},
                    "span": {"start": node["span_start"], "end": node["span_end"]},
                }
                subsections, i = _nest(nodes, i + 1, node["level"])
                if subsections:
                    section["subsections"] = subsections
                sections.append(section)
            else:
                i += 1
        return sections, i

    top_level = title_nodes[0]["level"] if title_nodes else 1
    sections, _ = _nest(title_nodes, 0, top_level - 1)

    out = {"sections": sections}

    stem = source_path.stem
    out_path = _out_dir(stem) / f"{stem}.toc.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, out


# ---------------------------------------------------------------------------
# Function 4: build alignment (commentary → root text via transclusions)
# ---------------------------------------------------------------------------

def _root_heading_refs(fm, source_path):
    """Return heading IDs (caret stripped) of the file named in ``root_text``.

    Headings are not edition segments, so transclusions pointing at them
    cannot be aligned.
    """
    root_val = fm.get("root_text")
    if not root_val:
        return set()
    resolved = _resolve_root_text_path(str(root_val), source_path)
    if not resolved:
        print(
            f"  WARN alignment: root_text {root_val!r} not found — "
            "heading targets not filtered",
            file=sys.stderr,
        )
        return set()
    try:
        _, root_body = _read_source(resolved)
    except (ValueError, OSError) as exc:
        print(
            f"  WARN alignment: cannot read root_text {root_val!r} ({exc}) — "
            "heading targets not filtered",
            file=sys.stderr,
        )
        return set()
    return {
        b["ref"].lstrip("^")
        for b in _extract_blocks(root_body, warn=False)
        if b["is_header"] and b["ref"]
    }


def _warn_heading_targets(skipped):
    if not skipped:
        return
    uniq = list(dict.fromkeys(skipped))
    print(
        f"  WARN alignment: {len(uniq)} transclusion target(s) are root-text "
        f"headings, not segments — skipped: {', '.join(uniq)}",
        file=sys.stderr,
    )


def build_alignment(source_path):
    fm, body = _read_source(source_path)
    file_type = fm.get("file_type", "")
    if file_type and file_type != "commentary":
        raise ValueError(
            f"parser-commentary expects file_type 'commentary', got {file_type!r}"
        )

    alignments = []
    seen_pairs = set()
    blocks = _extract_blocks(body, warn=False)
    heading_refs = _root_heading_refs(fm, source_path)
    skipped_heading_targets = []
    active_targets = []
    prev_was_transclusion_block = False

    for block in blocks:
        lines = block["lines"]
        # A block of transclusions only. Back-to-back ones form a single
        # group; anything else between them starts a new group.
        is_transclusion_block = all(
            TRANSCLUSION_RE.match(l) for l in lines if not _is_blank(l)
        ) and any(not _is_blank(l) for l in lines)
        raw_refs = [_TRANS_REF_RE.search(l).group(1)
                    for l in lines if _TRANS_REF_RE.search(l)]
        trans_refs = []
        for target_ref in raw_refs:
            if target_ref in heading_refs:
                skipped_heading_targets.append(target_ref)
            else:
                trans_refs.append(target_ref)

        # A heading ends the current scope: commentary after it must carry its
        # own transclusion to be aligned.
        if block["is_header"]:
            active_targets = list(dict.fromkeys(trans_refs)) if trans_refs else []
            prev_was_transclusion_block = False
            continue

        if raw_refs:
            # A transclusion group opens a new scope, replacing any previous
            # one. It stays active for the commentary blocks that follow.
            # (A group made only of heading targets still ends the old scope.)
            if is_transclusion_block and prev_was_transclusion_block:
                # Back-to-back transclusion blocks are one group, so a verse
                # ahead of the blank line keeps its alignment.
                active_targets = list(dict.fromkeys(active_targets + trans_refs))
            else:
                active_targets = list(dict.fromkeys(trans_refs))
        prev_was_transclusion_block = is_transclusion_block

        if block["ref"]:
            source_ref = block["ref"].lstrip("^")
            for target_ref in active_targets:
                pair = (source_ref, target_ref)
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    alignments.append({
                        "source_segment_reference": source_ref,
                        "target_segment_reference": target_ref,
                    })

    _warn_heading_targets(skipped_heading_targets)
    out = {"alignments": alignments}
    stem = source_path.stem
    out_path = _out_dir(stem) / f"{stem}.alignment.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    args = (argv if argv is not None else sys.argv[1:])
    usage = (
        'Usage:\n'
        '  python3 4-SYSTEM\\scripts\\parser-commentary\\parser.py '
        '"<commentary.md>" "<file.lint.json>"'
    )

    if len(args) != 2:
        print(usage)
        sys.exit(0 if not args else 1)

    source_path, lint_path = Path(args[0]), Path(args[1])
    if source_path.suffix != ".md" or ".lint" not in lint_path.name:
        print(usage)
        sys.exit(1)

    had_error = False

    try:
        source_fm, _ = _read_source(source_path)
        source_file_type = source_fm.get("file_type", "")
        if source_file_type and source_file_type != "commentary":
            print(
                f"ERROR {source_path}: expected file_type 'commentary', "
                f"got {source_file_type!r}",
                file=sys.stderr,
            )
            sys.exit(1)
    except Exception as exc:
        print(f"ERROR reading source: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        text_out = extract_text_input(lint_path, source_path)
        print(f"OK    {lint_path}  ->  {text_out}")
    except Exception as exc:
        print(f"ERROR text_input: {exc}", file=sys.stderr)
        had_error = True

    edition_result = None
    headings = []
    try:
        edition_out, edition_result, headings = build_edition(source_path, lint_path)
        segs = edition_result["segmentation"]["segments"]
        content_len = len(edition_result["content"])
        by_type = {}
        for s in segs:
            by_type[s["type"]] = by_type.get(s["type"], 0) + 1
        print(f"OK    {source_path}  ->  {edition_out}")
        print(f"  content length   : {content_len} chars")
        print(f"  segments         : {len(segs)}")
        for t, n in sorted(by_type.items()):
            print(f"    {t}: {n}")
        print(f"  headings (toc)   : {len(headings)}")
    except Exception as exc:
        print(f"ERROR edition: {exc}", file=sys.stderr)
        had_error = True

    if edition_result is not None:
        try:
            toc_out, toc_result = build_toc(source_path, edition_result, headings)
            sections = toc_result["sections"]

            def _toc_stats(nodes, depth=0):
                total = max_depth = 0
                for node in nodes:
                    total += 1
                    max_depth = max(max_depth, depth)
                    if node.get("subsections"):
                        n, d = _toc_stats(node["subsections"], depth + 1)
                        total += n
                        max_depth = max(max_depth, d)
                return total, max_depth

            toc_nodes, toc_depth = _toc_stats(sections)
            print(f"OK    {source_path}  ->  {toc_out}")
            print(f"  top sections     : {len(sections)}")
            print(f"  toc nodes        : {toc_nodes}")
            print(f"  max depth        : {toc_depth}")
        except Exception as exc:
            print(f"ERROR toc: {exc}", file=sys.stderr)
            had_error = True

    try:
        align_out, align_result = build_alignment(source_path)
        n = len(align_result["alignments"])
        print(f"OK    {source_path}  ->  {align_out}")
        print(f"  alignments       : {n}")
    except Exception as exc:
        print(f"ERROR alignment: {exc}", file=sys.stderr)
        had_error = True

    if had_error:
        sys.exit(1)


if __name__ == "__main__":
    main()
