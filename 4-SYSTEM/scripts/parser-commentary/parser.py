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

import durchen


OUTPUT_DIR = Path(__file__).parent / "output"


def _out_dir(stem):
    """Each source file gets its own folder: output/<stem>/."""
    d = OUTPUT_DIR / stem
    d.mkdir(parents=True, exist_ok=True)
    return d

YAML_PROPS_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
# Headers: ^n, ^n-n, ^n-n-n, ^n-n-n-… (any depth). Content: max ^n-n-n (3 parts).
REF_RE = re.compile(r'(\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\s*$')
VERSE_REF_MAX_PARTS = 3
ROMAN_RE = re.compile(r'^[IVXLCDM]+$')
# Matrix zone (block-id-spec §6): M, or M + run index (M1, M2, …).
MATRIX_ZONE_RE = re.compile(r'^M\d*$')
# Pre-Arabic matrix zones still in the vault: MI, MII.
LEGACY_MATRIX_ZONE_RE = re.compile(r'^M[IVXLCDM]+$')
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


# Characters that look blank but are not whitespace (zero-width space, BOM,
# non-breaking space). A line made only of these is an empty line.
BLANK_CHARS = "\u200b\u200c\u200d\ufeff\xa0"


def _is_blank_line(line):
    return not line.strip().strip(BLANK_CHARS).strip()


def _is_verse_shape(content_lines):
    """True for 2+ consecutive lines with no empty line between them.

    Verse is written one line per pāda, with no gap. An empty line inside a
    block (often an invisible zero-width space) means the block is really two
    paragraphs that were never given their own block IDs.
    """
    if any(_is_blank_line(l) for l in content_lines):
        return False
    return sum(1 for l in content_lines if l.strip()) > 1


# Inline formatting used for interlinear glosses in the sources. The gloss
# text stays in the edition; only the tags are dropped.
INLINE_TAG_RE = re.compile(r"</?small>", re.IGNORECASE)


def _strip_inline_tags(text):
    """Clean a heading title: drop inline gloss tags and footnote markers, turn
    space-like characters (U+00A0 …) into plain spaces and drop invisible ones."""
    return durchen.normalize_spaces(durchen.FOOTNOTE_MARK_RE.sub("", INLINE_TAG_RE.sub("", text)))


# Yigchung (ཡིག་ཆུང་, small-script gloss) is written <small>…</small>. In the
# edition the tags are dropped and each run of text inside them becomes a
# yigchung annotation: a half-open [start, end) span of absolute code-point
# offsets into the edition content.
SMALL_TAG_RE = re.compile(r"<(/?)small>", re.IGNORECASE)
# Everything the edition drops from a line: <small> tags (yigchung) and
# footnote markers [^dN] / [^fN] (durchen / footnote). One pass, so both get
# offsets into the same cleaned text.
INLINE_MARK_RE = re.compile(
    SMALL_TAG_RE.pattern + "|" + durchen.FOOTNOTE_MARK_RE.pattern, re.IGNORECASE
)


def _tag_context(line, m, width=12):
    """A short piece of the line around a tag, for error messages."""
    a, b = max(0, m.start() - width), min(len(line), m.end() + width)
    return ("…" if a else "") + line[a:b] + ("…" if b < len(line) else "")


def _strip_yigchung(line, in_small, error):
    """Drop <small> tags and footnote markers from one line, and find the
    yigchung runs and durchen markers in it.

    in_small says whether a run is already open when the line starts (it
    continues from the previous line of the same block). Returns
    (text, runs, in_small, marks): runs are [start, end) offsets into text,
    in_small says whether a run is still open at the end of the line, and
    marks are (offset, label) for each footnote marker.
    The text is identical to _strip_inline_tags(line).

    A stray tag — </small> with no open run, or <small> inside an open
    run — is passed to error(message); the caller stops the build.
    """
    out, runs, marks = [], [], []
    pos = 0
    run_start = 0 if in_small else None
    last = 0
    for m in INLINE_MARK_RE.finditer(line):
        # normalised piece by piece, so the offsets are into the cleaned text
        piece = durchen.normalize_spaces(line[last:m.start()])
        out.append(piece)
        pos += len(piece)
        last = m.end()
        if m.group(2) is not None:
            marks.append((pos, m.group(2)))
            continue
        closing = bool(m.group(1))
        if not closing:
            if run_start is not None:
                error(f"stray <small> (a <small> run is already open): {_tag_context(line, m)!r}")
                continue
            run_start = pos
        else:
            if run_start is None:
                error(f"stray </small> (no <small> is open): {_tag_context(line, m)!r}")
                continue
            runs.append([run_start, pos])
            run_start = None
    piece = durchen.normalize_spaces(line[last:])
    out.append(piece)
    pos += len(piece)
    if run_start is not None:
        runs.append([run_start, pos])  # carried to the next line, if any
    text = "".join(out)
    return text, runs, run_start is not None, marks


def _heading_level(line):
    """Number of leading '#' characters of a heading line."""
    stripped = line.lstrip()
    return len(stripped) - len(stripped.lstrip('#'))


BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def _clean_heading_title(text, level):
    """Obsidian renders only six heading levels, so a deeper heading (7+ '#')
    is often written in bold to look like one. That bold is display-only:
    drop the ** markers from the TOC title."""
    if level > 6:
        text = BOLD_RE.sub(r"\1", text).strip()
        # Abhidhamma vault: deeper headings are written `####### *Title* ^id`
        # (Markdown stops at six levels); the asterisks are display only.
        if len(text) > 2 and text.startswith("*") and text.endswith("*"):
            text = text[1:-1].strip()
    return text


def _infer_segment_type(ref_no_caret, doc_default):
    if not ref_no_caret:
        return doc_default
    if ref_no_caret[0].upper() == 'T':
        return "top_segment"
    parts = ref_no_caret.split('-')
    # A lowercase-letter part marks a conclusion / colophon: `^1-a` (section
    # conclusion), `^4-M-a` (inside a zone), `^a-1` (a colophon section).
    for part in parts:
        base = re.sub(r'[xX]\d+$', '', part)
        if part and not base.isdigit() and not ROMAN_RE.match(base):
            if re.match(r'^[a-z]+$', base):
                return "back_matter"
    # A matrix zone marks mātikā content. The matrix is text of the work, so
    # it is a verse; the zone only says which numbering run it belongs to.
    for part in parts[:-1]:
        if MATRIX_ZONE_RE.match(part) or LEGACY_MATRIX_ZONE_RE.match(part):
            return "verse"
    # x-suffix / U-leaf stay content; commentaries use paragraph default
    if VERSE_X_RE.search(ref_no_caret):
        return doc_default
    last = parts[-1] if parts else ""
    if re.match(r'^U\d+$', re.sub(r'[xX]\d+$', '', last)):
        return doc_default
    return doc_default


# ---------------------------------------------------------------------------
# Function 1: extract text_input
# ---------------------------------------------------------------------------

def extract_text_input(lint_path, source_stem=None):
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

    stem = lint_path.stem
    if stem.endswith(".lint.errors"):
        stem = stem[: -len(".lint.errors")]
    elif stem.endswith(".lint"):
        stem = stem[:-len(".lint")]
    if source_stem:
        stem = source_stem
    out_path = _out_dir(stem) / f"{stem}.text.json"
    out_path.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Function 2: build edition
# ---------------------------------------------------------------------------

def _block_marks(lines):
    """Labels of the footnote markers in some lines."""
    return [m.group(1) for l in lines for m in durchen.FOOTNOTE_MARK_RE.finditer(l)]


def _warn_lost_marks(block_num, lines, why, dropped):
    labels = [l for l in _block_marks(lines) if durchen.kind(l) is not None]
    if labels:
        dropped.update(labels)
        print(
            f"  WARN block {block_num}: {why}, so nothing is recorded for "
            f"{', '.join(f'[^{l}]' for l in labels)}",
            file=sys.stderr,
        )


def _build_content_and_segmentation(blocks, doc_default, notes=None):
    """Build the edition content and its segments.

    Headings are not part of the edition: they add no segment and no content.
    They are returned separately, with the content offset where they occur,
    for the table of contents.

    notes are the footnote definitions (durchen.split_definitions); each
    [^dN] marker becomes a durchen spanning the lemma before it, and each
    [^fN] marker a footnote at the position where it stood.
    """
    notes = notes or {}
    parts = []
    seg_list = []
    headings = []
    yigchungs = []
    marks = []
    dropped = set()
    tag_errors = []
    pos = 0

    for block_num, block in enumerate(blocks, start=1):
        ref = block["ref"]
        raw_lines = block["lines"]
        is_header = block["is_header"]

        content_lines = [l for l in raw_lines if not TRANSCLUSION_RE.match(l)]
        # Pure transclusion block — silently skip, used for alignment only
        if all(_is_blank(l) for l in content_lines):
            continue

        # Footnote markers left on their own after a block: they mark the end
        # of the text before them.
        if not is_header and not any(
            durchen.FOOTNOTE_MARK_RE.sub("", l).strip() for l in content_lines
        ):
            for label in _block_marks(content_lines):
                marks.append({"label": label, "pos": pos, "where": f"block {block_num}"})
            continue

        if not ref:
            print(f"  WARN block {block_num}: no reference marker — skipped", file=sys.stderr)
            _warn_lost_marks(block_num, content_lines, "block skipped", dropped)
            continue
        ref_no_caret = ref[1:] if ref.startswith("^") else ref

        if is_header:
            def _head_err(msg, _ref=ref, _n=block_num):
                tag_errors.append(f"block {_n} ({_ref}), heading: {msg}")

            _, _, head_open, _ = _strip_yigchung(raw_lines[0], False, _head_err)
            if head_open:
                _head_err("stray <small> (not closed in the heading)")
            if SMALL_TAG_RE.search(raw_lines[0]):
                print(
                    f"  WARN block {block_num}: <small> in heading {ref!r} — headings "
                    f"are not edition content, so no yigchung is recorded for it",
                    file=sys.stderr,
                )
            _warn_lost_marks(
                block_num, raw_lines[:1],
                f"footnote in heading {ref!r} — headings are not edition content", dropped,
            )
            text = _strip_inline_tags(raw_lines[0].strip().lstrip('#').strip())
            ref_idx = text.rfind(ref)
            if ref_idx != -1:
                text = text[:ref_idx].rstrip()
            level = _heading_level(raw_lines[0])
            text = _clean_heading_title(text, level)
            if not text:
                continue
            headings.append({
                "level": level,
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
            _warn_lost_marks(block_num, content_lines, "block skipped", dropped)
            continue

        last_nonempty_idx = -1
        for i in range(len(content_lines) - 1, -1, -1):
            if not _is_blank(content_lines[i]):
                last_nonempty_idx = i
                break
        line_spans = []
        block_yig = []
        in_small = False

        for i, raw_line in enumerate(content_lines):
            def _err(msg, _ref=ref, _n=block_num, _line=i + 1):
                tag_errors.append(f"block {_n} ({_ref}), line {_line}: {msg}")

            text, runs, in_small, line_marks = _strip_yigchung(_rstrip_line(raw_line), in_small, _err)
            if i == last_nonempty_idx:
                ref_idx = text.rfind(ref)
                if ref_idx != -1:
                    text = text[:ref_idx].rstrip()
            start = pos
            for off, label in line_marks:
                # A marker after the text ("…། །[^7] ^1-4") ends at the text's end.
                marks.append({"label": label, "pos": start + min(off, len(text)),
                              "where": f"block {block_num} ({ref})"})
            if not text:
                continue
            parts.append(text)
            pos += len(text)
            line_spans.append({"start": start, "end": start + len(text)})
            for s, e in runs:
                s, e = start + min(s, len(text)), start + min(e, len(text))
                if s >= e:
                    continue  # empty run: the API would store it but never return it
                if block_yig and block_yig[-1]["end"] == s:
                    # One unbroken stretch (a run continuing onto the next
                    # line, or </small><small>): one mark, not two.
                    block_yig[-1]["end"] = e
                else:
                    block_yig.append({"start": s, "end": e, "reference": ref_no_caret})
        if in_small:
            tag_errors.append(
                f"block {block_num} ({ref}): stray <small> (not closed by the end of the block)"
            )
        yigchungs.extend(block_yig)
        if any(_is_blank_line(l) for l in content_lines[1:-1]):
            print(
                f"  WARN block {block_num}: empty line inside the block — kept as one "
                f"segment; the parts may each need their own block ID",
                file=sys.stderr,
            )
        # Verse wins: several lines with no gap is a verse wherever it sits,
        # front matter or colophon included. Otherwise the ID decides.
        if _is_verse_shape(content_lines):
            seg_type = "verse"
        else:
            seg_type = _infer_segment_type(ref_no_caret, doc_default)
        seg_list.append({"lines": line_spans, "type": seg_type, "reference": ref_no_caret})

    if tag_errors:
        # Safety stop: the linter reports stray tags as errors, but the parser
        # also accepts a .lint.errors.json. Broken yigchung markup would put
        # marks on the wrong text, so nothing is written.
        raise ValueError(
            f"{len(tag_errors)} stray <small>/</small> tag(s), first at {tag_errors[0]} — "
            "run the linter for the full list and fix the source; "
            "no edition or yigchung payload written"
        )
    content = "".join(parts)
    durchens, footnotes = _resolve_footnotes(content, marks, notes, dropped)
    return content, seg_list, headings, yigchungs, durchens, footnotes


def _resolve_footnotes(content, marks, notes, dropped):
    """Turn footnote markers into durchens and footnotes. A durchen ([^dN]) is
    the note text over the lemma that ends at the marker (or the syllable
    before it, with a warning). A footnote ([^fN]) is the note text at the
    marker's position: the gap in the content where the marker stood, since
    the markers are already out of the content. Returns (durchens, footnotes)."""
    def warn(msg):
        print(f"  WARN {msg}", file=sys.stderr)

    out, footnotes, seen = [], [], set()
    for mk in marks:
        label, where = mk["label"], mk["where"]
        k = durchen.kind(label)
        if k is None:
            warn(f"{where}: [^{label}] is neither [^dN] (durchen) nor [^fN] (footnote) — not sent")
            continue
        what = "footnote" if k == durchen.FOOTNOTE else "durchen"
        note = notes.get(label)
        if label in seen:
            warn(f"{where}: [^{label}] is marked more than once — one {what} for each")
        seen.add(label)
        if note is None:
            warn(f"{where}: [^{label}] has no definition — no {what}")
            continue
        if not note["text"]:
            warn(f"{where}: [^{label}] has an empty note — no {what}")
            continue
        if k == durchen.FOOTNOTE:
            footnotes.append({"position": mk["pos"], "text": note["text"], "label": label})
            continue
        start, end, how = durchen.locate(content, mk["pos"], note["text"])
        if how is None:
            warn(f"{where}: [^{label}] has no text before it — no durchen")
            continue
        if how == "mismatch":
            warn(
                f"{where}: [^{label}] lemma {durchen.lemma_of(note['text'])!r} does not end at "
                f"the marker — span set to the syllable before it, {content[start:end]!r}"
            )
        elif how == "no-lemma":
            warn(
                f"{where}: [^{label}] note has no ༼…༽ witness, so no lemma — span set to the "
                f"syllable before it, {content[start:end]!r}"
            )
        out.append({"start": start, "end": end, "text": note["text"], "label": label})
    unused = [l for l in notes if l not in seen and l not in dropped and durchen.kind(l) is not None]
    if unused:
        warn(
            f"{len(unused)} footnote definition(s) never marked in the text — not sent: "
            + ", ".join(f"[^{l}]" for l in unused[:10]) + (" …" if len(unused) > 10 else "")
        )
    return out, footnotes


def build_edition(source_path, lint_path):
    fm, body = _read_source(source_path)
    body, notes, note_problems = durchen.split_definitions(body)
    for level, msg in note_problems:
        print(f"  WARN {msg}", file=sys.stderr)
    blocks = _extract_blocks(body, warn=False)  # empty-line warning: see _build_content_and_segmentation

    # Commentaries are paragraph-segmented (not verse)
    doc_default = "paragraph"

    content_str, seg_list, headings, yigchungs, durchens, footnotes = _build_content_and_segmentation(
        blocks, doc_default, notes
    )

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
    yig_path, _ = write_yigchungs(stem, content_str, yigchungs)
    dur_path, _ = write_durchens(stem, content_str, durchens)
    fn_path, _ = write_footnotes(stem, content_str, footnotes)
    return out_path, out, headings, yig_path, yigchungs, dur_path, durchens, fn_path, footnotes


# ---------------------------------------------------------------------------
# Function 2b: yigchung annotations
# ---------------------------------------------------------------------------

def write_yigchungs(stem, content, yigchungs):
    """Write the yigchung payload: one POST body per unbroken run, sorted by
    start. Each item is exactly the body of
    POST /v2/editions/{edition_id}/yigchungs. Not written when there are no
    runs; a file left from an earlier run is removed, so a source that loses
    its <small> markup does not leave a stale payload.
    """
    out_path = _out_dir(stem) / f"{stem}.yigchungs.json"
    if not yigchungs:
        out_path.unlink(missing_ok=True)
        return None, None
    yigchungs = sorted(yigchungs, key=lambda y: (y["start"], y["end"]))
    for y in yigchungs:
        if not (0 <= y["start"] < y["end"] <= len(content)):
            raise ValueError(f"yigchung span out of range: {y}")
    out = {
        "yigchungs": [
            {"span": {"start": y["start"], "end": y["end"]}} for y in yigchungs
        ],
    }
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, out


# ---------------------------------------------------------------------------
# Function 2c: durchen annotations
# ---------------------------------------------------------------------------

def write_durchens(stem, content, durchens):
    """Write the durchen payload: one item per footnote, sorted by span. Each
    item is exactly the body of POST /v2/editions/{edition_id}/durchens (one
    POST per item — the endpoint takes a single object). Written even when
    empty, so a file that loses its footnotes does not leave a stale payload.
    """
    out = {"durchens": durchen.payload(durchens, len(content))}
    out_path = _out_dir(stem) / f"{stem}.durchens.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, out


# ---------------------------------------------------------------------------
# Function 2d: footnotes
# ---------------------------------------------------------------------------

def write_footnotes(stem, content, footnotes):
    """Write the footnote payload: one item per [^fN] marker, sorted by
    position. A footnote has a position, not a span: the gap before
    content[position], 0…len(content). There is no API endpoint for footnotes
    yet, so nothing uploads this file. Not written when the text has no
    footnotes; a file left from an earlier run is removed.
    """
    out_path = _out_dir(stem) / f"{stem}.footnotes.json"
    if not footnotes:
        out_path.unlink(missing_ok=True)
        return None, None
    out = {"footnotes": durchen.footnote_payload(footnotes, len(content))}
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, out


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
    root_body, _, _ = durchen.split_definitions(root_body)
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
    # A transclusion or block ID inside a note is note text, not alignment.
    body, _, _ = durchen.split_definitions(body)
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
        text_out = extract_text_input(lint_path, source_path.stem)
        print(f"OK    {lint_path}  ->  {text_out}")
    except Exception as exc:
        print(f"ERROR text_input: {exc}", file=sys.stderr)
        had_error = True

    edition_result = None
    headings = []
    try:
        (edition_out, edition_result, headings, yig_out, yigchungs,
         dur_out, durchens, fn_out, footnotes) = build_edition(source_path, lint_path)
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
        if yig_out:
            print(f"OK    {source_path}  ->  {yig_out}")
        print(f"  yigchungs        : {len(yigchungs)}" + ("" if yig_out else " (no file written)"))
        print(f"OK    {source_path}  ->  {dur_out}")
        print(f"  durchens         : {len(durchens)}")
        if fn_out:
            print(f"OK    {source_path}  ->  {fn_out}")
        print(f"  footnotes        : {len(footnotes)}" + ("" if fn_out else " (no file written)"))
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
