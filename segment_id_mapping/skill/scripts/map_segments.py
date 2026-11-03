#!/usr/bin/env python3
"""
map_segments.py

Maps segment IDs from a "to-map" JSON export (content-only segments, in
translation order) to the "id" field in a language-specific id-registry
JSON file, e.g. "tibetan_segments.json" or "chinese_segments.json" (the
source markdown's block/verse segmentation, with start/end offsets and a
"reference" like "7-58"). Pass --segments explicitly on every run -- there
is no default, since the registry is per-language/translation and using
the wrong one would silently produce wrong ids rather than an error.

How it works
------------
1. Parse the translation source markdown (in whichever language matches
   the --segments registry passed in -- e.g. 1-SOURCES/Translations/
   bo-<translator>.md for Tibetan, or a zh-/en- translation for other
   languages) into an ordered list of (reference, text) blocks, using the
   trailing "^<ref>" Obsidian block-ID on each paragraph. Frontmatter and
   embed/transclusion-only lines (``![[...]]``) are skipped.
2. De-duplicate the to-map file by segment_id, keeping first occurrence
   order (one export was found to contain the same handful of segment_ids
   repeated dozens of times back-to-back -- an upstream glitch, not real
   data).
3. Walk the de-duplicated list in order. Because both lists are
   sequential/monotonic in the common case, for each row we scan forward
   from where the previous match left off, normalizing away the "⤵"
   line-break marker and all whitespace so a no-space double-shad
   ("དང་།།") compares equal to a spaced double-shad ("དང་། །") and a
   multi-line verse compares equal to its ⤵-joined counterpart. On top of
   plain forward matching, four fallbacks handle real-world export
   glitches, tried in this order for every row:
     a. exact match, scanning forward from the pointer;
     b. exact match against a concatenation of several *consecutive
        source* blocks (one to-map row that is itself the concatenation
        of, say, 3 short colophon blocks the markdown keeps separate);
     c. exact match in a small backward window (a row that arrived
        slightly out of order upstream -- e.g. verse N+2 appears in the
        file before verse N and N+1);
     d. fuzzy (similarity >= 90%) match within a forward window, to
        tolerate small text drift between the two files (a typo fixed in
        the markdown after the JSON was generated).
   If none of those succeed for a single row, it is held in a small
   pending buffer and merged with the next row(s) and retried -- this
   covers the reverse case, where the markdown keeps a multi-line verse
   as one block but the to-map file split it across two rows.
4. Once a reference is known for a segment_id, look that reference up in
   the --segments registry (matching on "reference") to get its "id", and
   emit {"segment_id", "content", "source_content", "reference", "id"}
   rows -- "content" is the original to-map row's text, "source_content" is
   the markdown block's own text at that reference (so the two can be
   eyeballed side by side), "reference" is the markdown verse/block id
   (e.g. "7-58") the row was matched to, "id" is the corresponding
   registry id. Every segment_id in a matched merge-group gets the
   same reference/id/source_content (they all belong to the same source
   block).
   Anything that still can't be matched (frontmatter-only metadata with no
   body-text counterpart, or a row whose text doesn't appear anywhere in
   the current markdown at all) still gets a row in the output -- with
   "source_content", "reference" and "id" set to null -- so the output file
   always has one row per unique segment_id; it is never guessed at, and is
   also listed in the report for manual review.
5. The report also covers the reverse direction: every source markdown
   block that never got claimed by any to-map row at all (as opposed to a
   to-map row failing to match one) is listed as an
   "unmatched_source_segment" -- this is normal for chapter/section
   headings (which have no to-map counterpart by design) but also surfaces
   verses the to-map file is simply missing.

Usage
-----
    python3 segment_id_mapping/skill/scripts/map_segments.py \
        --source-md "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md" \
        --to-map "segment_id_mapping/segments to be mapped.json" \
        --segments "segment_id_mapping/tibetan_segments.json" \
        --output "segment_id_mapping/output/segment_id_mapping.json" \
        --report "segment_id_mapping/output/segment_id_mapping.report.json"

--source-md, --to-map, --output and --report default to the
segment_id_mapping/, segment_id_mapping/output/ and 1-SOURCES/ locations
shown above (the original Tibetan run), relative to the vault root, so the
script can be run with just --segments from the vault root. --segments has
no default and must always be given explicitly -- the registry is
per-language (tibetan_segments.json, chinese_segments.json, ...), and
defaulting to one would risk silently matching another language's content
against the wrong registry.
"""

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

LINEBREAK_MARK = "⤵"  # ⤵
FUZZY_THRESHOLD = 0.90
FUZZY_WINDOW = 30  # how far ahead of the pointer to look for a near-match
MERGE_BUFFER_CAP = 4  # max consecutive to-map rows to merge for the split-verse fallback
SOURCE_SPAN_CAP = 4  # max consecutive source blocks to merge for the reverse (one row -> many blocks) case
BACKWARD_WINDOW = 15  # how far behind the pointer to look for an out-of-order row


def normalize(text: str) -> str:
    """Collapse whitespace/newlines and the JSON line-break marker so that
    spaced and unspaced double-shad, and multi-line vs ⤵-joined content,
    compare equal."""
    text = text.replace(LINEBREAK_MARK, "")
    return re.sub(r"\s+", "", text)


def parse_source_md(path: Path):
    """Return an ordered list of (reference, raw_text) for every block in
    the source markdown that carries a trailing '^ref' block ID."""
    raw = path.read_text(encoding="utf-8")

    # Strip YAML frontmatter (--- ... ---) at the top of the file, if present.
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            # move past the closing '---' line
            newline_after = raw.find("\n", end + 1)
            raw = raw[newline_after + 1:] if newline_after != -1 else ""

    blocks = re.split(r"\n\s*\n", raw)

    ref_pattern = re.compile(r"^(.*?)\s*\^([A-Za-z0-9\-]+)\s*$")

    segments = []
    for block in blocks:
        lines = [ln for ln in block.split("\n") if ln.strip() != ""]
        if not lines:
            continue
        last = lines[-1].strip()
        m = ref_pattern.match(last)
        if not m:
            # No block ID on this block (e.g. a bare transclusion line like
            # ![[...]] or stray text) -- not a citable segment, skip it.
            continue
        last_text, ref = m.group(1).strip(), m.group(2)

        text_lines = lines[:-1] + ([last_text] if last_text else [])

        # Strip markdown heading markers ("#", "##", ...) from the first
        # line of the assembled text -- done here, after assembly, rather
        # than on lines[0] beforehand, because a single-line block (heading
        # and trailing "^ref" on the very same line) has its whole text come
        # from last_text, not lines[0]; stripping lines[0] alone would be
        # silently discarded in that case and the "#" would leak into text.
        if text_lines:
            text_lines[0] = re.sub(r"^#{1,6}\s*", "", text_lines[0])

        text = "\n".join(text_lines)
        segments.append({"reference": ref, "text": text, "raw_block": block})

    return segments


def load_to_map(to_map_path: Path):
    """Load the "to be mapped" file, accepting either shape seen in
    practice: a flat [{"segment_id", "content"}, ...] list, or the nested
    {"content": {"sections": [{"segments": [...], "sections": [...]}]}}
    shape (recursing into any sub-sections), flattening the latter into
    the same flat [{"segment_id", "content", "segment_number"}, ...] form.
    The flat shape has no segment_number of its own; callers fill in a
    positional fallback (see main())."""
    data = json.loads(to_map_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [
            {"segment_id": it["segment_id"], "content": it["content"], "segment_number": it.get("segment_number")}
            for it in data
        ]

    def walk(secs):
        out = []
        for s in secs:
            for seg in (s.get("segments") or []):
                out.append({
                    "segment_id": seg["segment_id"],
                    "content": seg["content"],
                    "segment_number": seg.get("segment_number"),
                })
            out.extend(walk(s.get("sections") or []))
        return out

    sections = data.get("content", {}).get("sections", [])
    return walk(sections)


def build_reference_id_map(segments_json_path: Path):
    data = json.loads(segments_json_path.read_text(encoding="utf-8"))
    # segments.json may be the raw two-page-concatenated file OR the already
    # combined flat list -- handle both.
    items = data if isinstance(data, list) else data.get("items", [])
    ref_to_id = {}
    id_to_ref = {}
    ref_to_type = {}
    for it in items:
        ref_to_id[it["reference"]] = it["id"]
        id_to_ref[it["id"]] = it["reference"]
        ref_to_type[it["reference"]] = it.get("type")
    return ref_to_id, id_to_ref, ref_to_type


def load_overrides(overrides_path):
    """Load a manual-override file: a list of {"segment_id", "reference"}
    (or {"segment_id", "id"}) entries for rows a human has confirmed by
    hand -- these are applied verbatim and never touch the automatic
    matching pointer, so they can point anywhere (including a reference
    already claimed by another segment_id, e.g. a genuine duplicate
    verse)."""
    if overrides_path is None:
        return {}
    data = json.loads(Path(overrides_path).read_text(encoding="utf-8"))
    return {entry["segment_id"]: entry for entry in data}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source-md", default="1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md")
    ap.add_argument("--to-map", default="segment_id_mapping/segments to be mapped.json")
    ap.add_argument("--segments", required=True,
                     help="the id registry for this run's language -- e.g. "
                          '"segment_id_mapping/tibetan_segments.json" or '
                          '"segment_id_mapping/chinese_segments.json". No '
                          "default: the registry differs per language/translation, "
                          "so it must always be given explicitly rather than assumed, "
                          "to avoid silently matching one language's content against "
                          "another language's id registry.")
    ap.add_argument("--output", default="segment_id_mapping/output/segment_id_mapping.json")
    ap.add_argument("--report", default="segment_id_mapping/output/segment_id_mapping.report.json")
    ap.add_argument("--overrides", default=None,
                     help="optional JSON file of manually-confirmed "
                          '{"segment_id", "reference"} (or {"segment_id", "id"}) '
                          "entries, applied verbatim ahead of automatic matching")
    args = ap.parse_args()

    source_md_path = Path(args.source_md)
    to_map_path = Path(args.to_map)
    segments_path = Path(args.segments)

    source_segments = parse_source_md(source_md_path)
    for seg in source_segments:
        seg["norm"] = normalize(seg["text"])
    ref_to_source_text = {seg["reference"]: seg["text"] for seg in source_segments}
    ref_to_index = {seg["reference"]: i for i, seg in enumerate(source_segments)}

    to_map_raw = load_to_map(to_map_path)
    ref_to_id, id_to_ref, ref_to_type = build_reference_id_map(segments_path)
    overrides = load_overrides(args.overrides)

    # De-duplicate by segment_id, keeping first-occurrence order. The raw
    # file was found to contain a handful of segment_ids repeated dozens of
    # times (an export glitch) -- those repeats carry no new information.
    seen = set()
    to_map = []
    duplicate_rows_dropped = 0
    for item in to_map_raw:
        if item["segment_id"] in seen:
            duplicate_rows_dropped += 1
            continue
        seen.add(item["segment_id"])
        to_map.append(item)

    # The flat to-map shape carries no real segment_number at all -- rather
    # than fabricate one and put it in the output (where it would look like
    # real data instead of an artifact of this script), leave
    # item["segment_number"] as None for those rows and track a separate,
    # internal-only "_order" (position in the original JSON array) purely
    # to keep sorting stable. "_order" is stripped back out before the
    # output/report files are written (see below).
    for idx, item in enumerate(to_map, start=1):
        item["_order"] = item.get("segment_number") if item.get("segment_number") is not None else idx

    unique_segment_ids = len(to_map)

    mapping = []
    unmatched = []
    ambiguous_refs = []
    fuzzy_matches = []
    merged_matches = []
    manual_matches = []

    def null_row(item, reference=None, source_content=None):
        """Full output-shaped row with explicit nulls for whatever
        couldn't be determined -- used for unmatched/ambiguous entries so
        their shape matches a real mapping row."""
        row = {
            "segment_id": item["segment_id"],
            "content": item["content"],
            "segment_number": item["segment_number"],
            "source_content": source_content,
            "reference": reference,
            "id": None,
            "_order": item["_order"],
        }
        # A row from the flat to-map shape has no real segment_number at
        # all (see the "_order" comment above) -- drop the key entirely
        # rather than emit a fabricated or null one.
        if row["segment_number"] is None:
            del row["segment_number"]
        return row

    j = 0
    n = len(source_segments)
    consumed = set()  # source indices already assigned to some segment_id

    # Pull out any rows a human has manually confirmed via --overrides.
    # These are applied verbatim -- they never touch the automatic-matching
    # pointer, so they can legitimately point at a reference some other
    # segment_id has already claimed (a real duplicate verse). The matched
    # source index (when the reference resolves to one) is still marked
    # consumed so unmatched_source_segments doesn't falsely flag it later.
    override_refs_to_consume = []  # resolved references from --overrides; added to
    # `consumed` only AFTER automatic matching runs (see below) so an override
    # pointing at a reference some *other*, not-yet-processed segment_id will
    # also legitimately auto-match (a genuine duplicate verse, e.g. "4-44")
    # doesn't get pre-emptively blocked from making that normal match.
    if overrides:
        remaining = []
        for item in to_map:
            entry = overrides.get(item["segment_id"])
            if entry is None:
                remaining.append(item)
                continue
            mapped_id = entry.get("id")
            if mapped_id is None:
                mapped_id = ref_to_id.get(entry.get("reference"))
            if mapped_id is None:
                bad_ref = entry.get("reference")
                ambiguous_refs.append(null_row(item, reference=bad_ref, source_content=ref_to_source_text.get(bad_ref)))
                continue
            ref = entry.get("reference") or id_to_ref.get(mapped_id)
            row = {
                "segment_id": item["segment_id"],
                "content": item["content"],
                "segment_number": item["segment_number"],
                "source_content": ref_to_source_text.get(ref),
                "reference": ref,
                "id": mapped_id,
                "_order": item["_order"],
            }
            if row["segment_number"] is None:
                del row["segment_number"]
            mapping.append(row)
            manual_matches.append({
                "segment_id": item["segment_id"],
                "reference": ref,
                "id": mapped_id,
                "content": item["content"],
                "source_content": ref_to_source_text.get(ref),
            })
            if ref in ref_to_index:
                override_refs_to_consume.append(ref_to_index[ref])
        to_map = remaining
    buffer = []  # pending (seg_id, content) rows waiting to be merged/matched
    source_merge_matches = []  # one to-map row matched against >1 source block
    out_of_order_matches = []  # row matched behind the current pointer

    def try_match(target_norm, start):
        """Return (indices, is_fuzzy) where `indices` is a sorted list of
        one or more consecutive, not-yet-consumed source indices whose
        (concatenated) normalized text equals target_norm, or
        (None, False) if nothing clears the exact/fuzzy bar. Tries, in
        order: exact single block forward; exact multi-block span forward
        (the rare case where one to-map row is the concatenation of
        several source blocks, e.g. a combined colophon); exact single
        block in a small backward window (the rare case where upstream
        rows are locally out of order); fuzzy single block forward."""
        for k in range(start, n):
            if k in consumed:
                continue
            if source_segments[k]["norm"] == target_norm:
                return [k], False

        # A span doesn't have to start exactly at `start`: a heading or other
        # block with no corresponding to-map row (e.g. a section title) can
        # sit in between, so try a handful of nearby starting points too.
        for span_start in range(start, min(start + 10, n)):
            if span_start in consumed:
                continue
            acc = ""
            span = []
            for k in range(span_start, min(span_start + SOURCE_SPAN_CAP, n)):
                if k in consumed:
                    break
                span.append(k)
                acc += source_segments[k]["norm"]
                if len(span) > 1 and acc == target_norm:
                    return span, False
                if len(acc) > len(target_norm):
                    break

        for k in range(start - 1, max(-1, start - 1 - BACKWARD_WINDOW), -1):
            if k in consumed:
                continue
            if source_segments[k]["norm"] == target_norm:
                return [k], False

        best_idx, best_ratio = None, 0.0
        for k in range(start, min(start + FUZZY_WINDOW, n)):
            if k in consumed:
                continue
            ratio = difflib.SequenceMatcher(None, target_norm, source_segments[k]["norm"]).ratio()
            if ratio > best_ratio:
                best_ratio, best_idx = ratio, k
        if best_idx is not None and best_ratio >= FUZZY_THRESHOLD:
            return [best_idx], True
        return None, False

    def record_match(chunk, indices, is_fuzzy):
        anchor = indices[0]
        ref = source_segments[anchor]["reference"]
        mapped_id = ref_to_id.get(ref)
        # source_content mirrors reference/id: the anchor (first) source
        # block's own text only, even when this row spanned several
        # consecutive source blocks (source-merge case) -- downstream only
        # supports a 1:1 mapping, so we don't want a multi-block concatenation
        # sitting next to a single reference/id that only names the first one.
        source_content = source_segments[anchor]["text"]
        if mapped_id is None:
            for b in chunk:
                ambiguous_refs.append(null_row(b, reference=ref, source_content=source_content))
            return
        for b in chunk:
            row = {
                "segment_id": b["segment_id"],
                "content": b["content"],
                "segment_number": b["segment_number"],
                "source_content": source_content,
                "reference": ref,
                "id": mapped_id,
                "_order": b["_order"],
            }
            if row["segment_number"] is None:
                del row["segment_number"]
            mapping.append(row)
        if is_fuzzy:
            for b in chunk:
                fuzzy_matches.append({
                    "segment_id": b["segment_id"],
                    "reference": ref,
                    "id": mapped_id,
                    "content": b["content"],
                    "source_text": "\n".join(source_segments[i]["text"] for i in indices),
                })
        if len(indices) > 1:
            # "reference" here is the first/anchor source block only (same
            # as "id" above) -- downstream only supports a 1:1 mapping, not
            # 1:many, so we don't report the full spanned-block list.
            source_merge_matches.append({
                "segment_ids": [b["segment_id"] for b in chunk],
                "reference": ref,
                "id": mapped_id,
            })

    for item in to_map:
        buffer.append(item)

        # Try the shortest suffix first (just the newest row alone -- the
        # normal case), then progressively longer suffixes ending at the
        # newest row (the split-verse merge case). Trying shortest-first
        # means a row that was buffered earlier because IT didn't match
        # anything doesn't force every later row to be merged with it too.
        matched = False
        for length in range(1, len(buffer) + 1):
            chunk = buffer[-length:]
            combined_norm = normalize("".join(b["content"] for b in chunk))
            indices, is_fuzzy = try_match(combined_norm, j)
            if indices is not None:
                leftover = buffer[:-length]
                for b in leftover:
                    unmatched.append(null_row(b))
                record_match(chunk, indices, is_fuzzy)
                consumed.update(indices)
                top = max(indices)
                if top >= j:
                    j = top + 1
                else:
                    out_of_order_matches.append({
                        "segment_ids": [b["segment_id"] for b in chunk],
                        "reference": source_segments[indices[0]]["reference"],
                    })
                buffer.clear()
                matched = True
                break

        if not matched and len(buffer) >= MERGE_BUFFER_CAP:
            # The oldest row in the buffer never found a merge partner --
            # give up on it specifically (not the whole buffer) and keep
            # sliding forward.
            oldest = buffer.pop(0)
            unmatched.append(null_row(oldest))

    # Anything still pending at the end of the file never matched.
    for b in buffer:
        unmatched.append(null_row(b))
    buffer.clear()

    # Now that automatic matching has had its full, unobstructed chance to
    # claim source indices (including the natural earlier occurrence of a
    # duplicate verse an override also points at, e.g. "4-44"), fold in the
    # overrides' resolved indices too. A set add is idempotent, so this is
    # safe whether or not automatic matching already consumed the same index.
    consumed.update(override_refs_to_consume)

    # Output is sorted by "_order" ascending -- matching order isn't
    # necessarily insertion order once merges/out-of-order/manual overrides
    # are involved. "_order" is the real segment_number when the to-map
    # file had one, or a positional fallback when it didn't (see above);
    # either way it's an internal sort key only and never written out.
    mapping.sort(key=lambda r: r["_order"])
    unmatched.sort(key=lambda r: r["_order"])
    ambiguous_refs.sort(key=lambda r: r["_order"])

    # merged_matches: group the FINAL mapping (covering every match type --
    # exact, fuzzy, and manual/override alike) by reference, rather than
    # only the rows that happened to be merged together in the same
    # buffer-chunk during the automatic pass. This catches every genuine
    # many-segment_ids-to-one-reference case, e.g. two separate manual
    # overrides landing on the same reference, or a fuzzy match and an
    # override sharing one -- not just same-chunk merges.
    ref_groups = {}
    for row in mapping:
        ref = row.get("reference")
        if not ref:
            continue
        ref_groups.setdefault(ref, []).append(row)
    merged_matches = [
        {
            "segment_ids": [r["segment_id"] for r in rows],
            "reference": ref,
            "id": rows[0]["id"],
            "content": [r["content"] for r in rows],
            "source_content": rows[0]["source_content"],
        }
        for ref, rows in ref_groups.items()
        if len(rows) > 1
    ]
    merged_matches.sort(key=lambda m: min(r["_order"] for r in ref_groups[m["reference"]]))

    # The output file covers every unique segment_id, not just the matched
    # ones -- unmatched/ambiguous rows are included with source_content,
    # reference and id left null (same null_row shape used in the report),
    # so downstream can see the full to-map file accounted for in one place.
    full_output = mapping + unmatched + ambiguous_refs
    full_output.sort(key=lambda r: r["_order"])
    for row in full_output:
        row.pop("_order", None)

    Path(args.output).write_text(
        json.dumps(full_output, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # The reverse direction: source markdown blocks that never got claimed
    # by any to-map row at all (the to-map file is simply missing that
    # verse/segment, rather than a to-map row failing to match).
    unmatched_source_segments = [
        {
            "reference": seg["reference"],
            "id": ref_to_id.get(seg["reference"]),
            "type": ref_to_type.get(seg["reference"]),
            "source_content": seg["text"],
        }
        for i, seg in enumerate(source_segments)
        if i not in consumed
    ]

    report = {
        "total_rows_in_to_map_file": len(to_map_raw),
        "duplicate_rows_dropped": duplicate_rows_dropped,
        "unique_segment_ids": unique_segment_ids,
        "matched": len(mapping),
        "matched_exact": len(mapping) - len(fuzzy_matches) - len(manual_matches),
        "matched_fuzzy": len(fuzzy_matches),
        "matched_manual": len(manual_matches),
        "manual_matches": manual_matches,
        "fuzzy_matches": fuzzy_matches,
        "merged_matches": merged_matches,
        "source_merge_matches": source_merge_matches,
        "out_of_order_matches": out_of_order_matches,
        "unmatched_count": len(unmatched),
        "unmatched": unmatched,
        "reference_not_in_segments_json_count": len(ambiguous_refs),
        "reference_not_in_segments_json": ambiguous_refs,
        "source_segments_total": n,
        "source_segments_consumed": len(consumed),
        "unmatched_source_segments_count": len(unmatched_source_segments),
        "unmatched_source_segments": unmatched_source_segments,
    }
    Path(args.report).write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"{len(to_map_raw)} rows -> {unique_segment_ids} unique segment_ids "
          f"({duplicate_rows_dropped} duplicate rows dropped).")
    print(f"Matched {len(mapping)}/{unique_segment_ids} "
          f"(exact: {len(mapping) - len(fuzzy_matches) - len(manual_matches)}, fuzzy: {len(fuzzy_matches)}, "
          f"manual: {len(manual_matches)}, "
          f"merged-groups: {len(merged_matches)}, source-merge-groups: {len(source_merge_matches)}, "
          f"out-of-order: {len(out_of_order_matches)}). "
          f"Unmatched: {len(unmatched)}. Missing-in-registry: {len(ambiguous_refs)}.")
    if unmatched:
        print("Unmatched segment_ids:", [u["segment_id"] for u in unmatched])
    print(f"Source segments with no matching to-map row: "
          f"{len(unmatched_source_segments)}/{n}.")
    if unmatched_source_segments:
        refs = [s["reference"] for s in unmatched_source_segments]
        shown = refs if len(refs) <= 40 else refs[:40] + [f"... +{len(refs) - 40} more (see report)"]
        print("Unmatched source references:", shown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
