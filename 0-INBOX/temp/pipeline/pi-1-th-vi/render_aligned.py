"""Render a translation in the root's block structure, with root transclusions.

For every root block, in root order:
    ![[1-SOURCES/Text/pi-1.md#^ID]]

    <translation of that block> ^ID
Root blocks with no translation text of their own are stacked (MERGE) on the next block that
has text; root headings with no translated heading get the transclusion only.
Translation-only headings are kept as bold lines inside the block they precede.

Usage: render_aligned.py <th|vi> <root.md> <draft.md> <map.json> <frontmatter.txt> <out.md> <matchlist.md>
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

lang, root_path, draft, map_path, fm_path, out_path, ml_path = sys.argv[1:8]
R = parse_root(root_path)
D = parse_draft(draft)
J = json.load(open(map_path, encoding="utf-8"))
M = J["mapping"]
extra_titles = J.get("extra_titles", {})
extra_heads = set(J.get("heading_extra", []) or J.get("extra_heads", []))
# every line belongs to a block (no lines printed under a heading): run fix_heading_bounds first
assert not any(v.get("after") for v in M.values()), "map has 'after' lines: run fix_heading_bounds.py"
ROOT = sys.argv[8] if len(sys.argv) > 8 else "1-SOURCES/Text/pi-1.md"


MATRIX_END = next((k for k, it in enumerate(D) if it["kind"] == "p" and "[๑๖]" in it["text"]), len(D))


def item_text(i):
    it = D[i]
    if it["kind"] == "h":
        return f"**{it['text']}**"
    if it["kind"] == "table":
        # The Thai edition prints the matrix in two columns: Pāli (Thai script) | Thai.
        # Tables are not part of the vault structure, and the Pāli is already transcluded
        # from the root, so only the Thai column is kept, one line per row (the raw copy in
        # 0-INBOX/raw-data keeps both columns).
        # Body "tables" (after the matrix) are Thai prose with wide spacing, not Pāli | Thai:
        # there both cells are kept, joined by a space.
        in_matrix = i < MATRIX_END
        rows = []
        for ln in it["text"].splitlines():
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) < 2 or cells[0] in ("Pāli", "") or set(cells[0]) <= set("-"):
                continue
            if in_matrix:
                rows.append(cells[1] if cells[1] else cells[0])
            else:
                rows.append(" ".join(c for c in cells if c))
        return "\n".join(rows)
    return it["text"]


def block_body(b):
    """Return (lines, tables) for a root text block."""
    v = M[b]
    parts = []
    if lang == "vi" and v.get("pieces"):
        # items listed explicitly (matrix, homage) come first, then the split paragraph pieces
        for i in v["items"]:
            parts.append(item_text(i))
        parts.extend(t for _, t in v["pieces"])
    else:
        parts = [item_text(i) for i in v["items"]]
    # extra (translation-only) headings that precede this block's first item
    return parts


# Items the aligner left out (translation-only headings, stray lines before a heading pair) go
# to the start of the block that holds the next placed item, so no translation text is lost.
placed = {}
for b, v in M.items():
    for i in v["items"]:
        placed[i] = b
    for i, _ in v.get("pieces", []):
        placed.setdefault(i, b)
    if v.get("heading") is not None:
        placed[v["heading"]] = None  # used as a heading
    for i in v.get("after", []):
        placed[i] = None  # printed under a heading
orphans = [i for i, it in enumerate(D) if i not in placed and it["kind"] != "hr"]
prefix = {}
for i in orphans:
    nxt = next((j for j in range(i + 1, len(D)) if placed.get(j)), None)
    if nxt is None:
        continue
    b = placed[nxt]
    prefix.setdefault(b, []).append(i)
    placed[i] = b
for b, items in prefix.items():
    if lang == "vi" and M[b].get("pieces"):
        M[b]["items"] = items + M[b]["items"]
    else:
        M[b]["items"] = items + M[b]["items"]

out, ml = [], []
stack = []  # transclusions waiting for text (MERGE)
last_group = None  # index in out of the previous passage's transclusion group
hstack = []  # (root level, output level) of the headings written so far, innermost last
for blk in R:
    bid = blk["id"]
    tl = f"![[{ROOT}#^{bid}]]"
    if blk["kind"] == "h":
        # Headings carry the block ID but no transclusion; a root heading with no heading in
        # the translation is left out (user decision, 2026-11-13).
        h = M[bid]["heading"]
        text = None
        if lang == "th" and bid in ("0", "1-0") and M["1-0"]["heading"] is not None:
            # The Thai title page has one line "พระอภิธรรมปิฎก เล่ม ๑ ธรรมสังคณีปกรณ์":
            # basket + volume -> ^0, book title -> ^1-0
            full = D[M["1-0"]["heading"]]["text"]
            basket, _, book = full.rpartition(" ")
            text = basket if bid == "0" else book
        elif h is not None:
            text = D[h]["text"]
        elif bid in extra_titles and extra_titles[bid]:
            text = extra_titles[bid]
        if stack and last_group is not None:
            # root blocks with no text of their own just before a heading join the passage before them
            out[last_group] += "\n" + "\n".join(stack)
            stack = []
        if text:
            # output level: one below the nearest written ancestor heading, so a root heading
            # left out (no heading in this translation) leaves no gap in the levels
            while hstack and hstack[-1][0] >= blk["level"]:
                hstack.pop()
            lvl = hstack[-1][1] + 1 if hstack else 1
            hstack.append((blk["level"], lvl))
            out.append("#" * lvl + " " + text + f" ^{bid}")
            ml.append(f"^{bid} H  {blk['text'][:40]}  ->  {text[:50]}")
        else:
            ml.append(f"^{bid} H  {blk['text'][:40]}  ->  (no heading in this translation: left out)")
        continue
    parts = block_body(bid)
    if not parts:
        stack.append(tl)
        ml.append(f"^{bid} T  {blk['text'][:40]}  ->  MERGE with the next block")
        continue
    tables = []
    lines = [p for p in parts if p]
    out.append("\n".join(stack + [tl]))
    last_group = len(out) - 1
    stack = []
    if tables:
        chunk = "\n".join(lines)
        segs = ([chunk] if chunk else []) + tables + [f"^{bid}"]
        out.append("\n\n".join(segs))
    else:
        out.append("\n".join(lines) + f" ^{bid}")
    first = re.sub(r"\s+", " ", (lines[0] if lines else tables[0]))[:50]
    ml.append(f"^{bid} T  {blk['text'][:40]!s}  ->  {first}")
if stack:
    if last_group is not None:
        out[last_group] += "\n" + "\n".join(stack)
    else:
        out.append("\n".join(stack))

fm = open(fm_path, encoding="utf-8").read().rstrip() + "\n\n"
body = "\n\n".join(x.replace("\n\n\n", "\n\n") for x in out) + "\n"
open(out_path, "w", encoding="utf-8", newline="\n").write(fm + body)
open(ml_path, "w", encoding="utf-8", newline="\n").write("\n".join(ml) + "\n")

# coverage check: every draft item must appear exactly once
used = []
for b, v in M.items():
    used.extend(v["items"])
    if v.get("heading") is not None:
        used.append(v["heading"])
    used.extend(v.get("after", []))
    used.extend(i for i, _ in v.get("pieces", []))
present = set(used) | set(placed)
missing = [i for i, it in enumerate(D) if i not in present and it["kind"] != "hr"]
ids_out = re.findall(r" \^([\w-]+)$|^\^([\w-]+)$", body, re.M)
print(f"{lang}: root blocks {len(R)}, block IDs written {len(ids_out)}, transclusions {body.count('![[')}, "
      f"draft items not placed {len(missing)} {missing[:20]}")
