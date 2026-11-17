"""Render a translation in the root's block structure, with root transclusions.

For every root text block, in root order:
    ![[<root>#^ID]]

    <translation of that block> ^ID
Root headings carry their ID with no transclusion; a root heading with no heading in the
translation is left out. Root text blocks with no translation text of their own are stacked
(MERGE) on the next passage, or, just before a heading, on the passage before them.
Translation-only headings are kept as bold lines when they open a block, plain lines inside it.

Usage: render_aligned.py <th|vi> <root.md> <draft.md> <map.json> <frontmatter.txt> <out.md> <matchlist.md> [<root_rel> <book>]
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
THAI_HEADS = set(J.get("thai_heads", []))
# every line belongs to a block (no lines printed under a heading): run fix_heading_bounds first
assert not any(v.get("after") for v in M.values()), "map has 'after' lines: run fix_heading_bounds.py"
ROOT = sys.argv[8] if len(sys.argv) > 8 else "1-SOURCES/Text/pi-1.md"
BOOK = sys.argv[9] if len(sys.argv) > 9 else "1"
TITLE_IDS = ("0", f"{BOOK}-0")


MATRIX_END = next((k for k, it in enumerate(D) if it["kind"] == "p" and "[๑๖]" in it["text"]), len(D))
LABEL = re.compile(r"^((?:\[[๐-๙]+\]\s*)?(?:[๐-๙]+(?:-[๐-๙]+)?\.\s+)?)(.*)$", re.S)


def is_pali_tok(t):
    return "ฺ" in t or t.endswith("ํ") or t.endswith("ธมฺมา")


def strip_pali_lead(text):
    """'๒. สงฺคหิเตน อสงฺคหิตํ ธรรมที่…' -> '๒. ธรรมที่…': a numbered matrix line printed as
    Thai-script Pāli followed by its Thai; the Pāli is transcluded from the root."""
    m = LABEL.match(text)
    label, rest = m.group(1), m.group(2)
    toks = rest.split()
    # drop everything up to the last Pāli-marked token among the first six (the Pāli column)
    marked = [i for i in range(min(6, len(toks) - 1)) if is_pali_tok(toks[i])]
    if marked:
        return label + " ".join(toks[marked[-1] + 1:])
    # "มนสิกาโร มนสิการ", "เวทนา เวทนา": a Pāli word followed by its Thai loan form
    if len(toks) >= 2 and _sk(toks[0]) and (_sk(toks[0]) == _sk(toks[1]) or _sk(toks[0]).startswith(_sk(toks[1])) and len(_sk(toks[1])) >= 3):
        return label + " ".join(toks[1:])
    # "สภาโค ธรรมที่…": a Pāli nominative in -o (โ + final consonant) before the Thai
    if label and len(toks) >= 2 and re.search(r"โ[ก-ฮ]$", toks[0]):
        return label + " ".join(toks[1:])
    return text


_TH_CONS = set("กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ")


def _sk(tok):
    return "".join(ch for ch in tok if ch in _TH_CONS)


def is_continuation(text):
    """A centred line that continues a two-column matrix row (starts with Pāli, no number)."""
    toks = text.split()
    return bool(toks) and not LABEL.match(text).group(1) and is_pali_tok(toks[0])


def item_text(i, first=True):
    it = D[i]
    if it["kind"] == "h" and not first and not is_continuation(it["text"]):
        # a Thai-only heading line in the middle of a block is a list line: plain text
        return strip_pali_lead(it["text"])
    if it["kind"] == "h":
        if is_continuation(it["text"]):
            # second line of a matrix row: plain text, Pāli column dropped
            toks = it["text"].split()
            k = max(i for i in range(len(toks)) if is_pali_tok(toks[i]) and i < len(toks) - 1) if any(is_pali_tok(t) for t in toks[:-1]) else -1
            return " ".join(toks[k + 1:])
        s = strip_pali_lead(it["text"])
        # a long centred line is a sentence, not a heading: plain text
        return s if len(s) > 45 else f"**{s}**"
    if it["kind"] == "table":
        # The Thai edition prints matrices in two columns: Pāli (Thai script) | Thai.
        # Tables are not part of the vault structure, and the Pāli is already transcluded
        # from the root, so only the Thai column is kept, one line per row (the raw copy in
        # 0-INBOX/raw-data keeps both columns).
        # A row whose left cell is Thai-script Pāli (phinthu, or ending in ธมฺมา) is
        # Pāli | Thai: only the Thai is kept. Otherwise the "table" is Thai prose that the PDF
        # spaced widely, and both cells are kept, joined by a space.
        rows = []
        for ln in it["text"].splitlines():
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) < 2 or cells[0] in ("Pāli", "") or set(cells[0]) <= set("-"):
                continue
            if "ฺ" in cells[0] or cells[0].endswith("ธมฺมา") or "ํ" in cells[0]:
                label = LABEL.match(cells[0]).group(1)  # keep "[๑] ๑." labels printed in the Pāli cell
                rows.append(label + (cells[1] if cells[1] else cells[0]))
            else:
                rows.append(strip_pali_lead(" ".join(c for c in cells if c)))
        return "\n".join(rows)
    return strip_pali_lead(it["text"]) if LABEL.match(it["text"]).group(1) else it["text"]


def block_body(b):
    """Return the translation lines of a root text block."""
    v = M[b]
    parts = []
    if lang == "vi" and v.get("pieces"):
        # items listed explicitly (matrix, homage) come first, then the split paragraph pieces
        for i in v["items"]:
            parts.append(item_text(i))
        parts.extend(t for _, t in v["pieces"])
    else:
        # Thai-only section names moved into this block (fix_heading_bounds) are bold too
        for n, i in enumerate(v["items"]):
            parts.append(item_text(i, first=(n == 0 or i in THAI_HEADS)))
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
    M[b]["items"] = items + M[b]["items"]

out, ml = [], []
stack = []  # transclusions waiting for text (MERGE)
last_group = None  # index in out of the previous passage's transclusion group
hstack = []  # (root level, output level) of the headings written so far, innermost last
CHECK = set(J.get("check", []))
for blk in R:
    bid = blk["id"]
    tl = f"![[{ROOT}#^{bid}]]"
    if blk["kind"] == "h":
        # Headings carry the block ID but no transclusion; a root heading with no heading in
        # the translation is left out (user decision, 2026-11-13).
        h = M[bid]["heading"]
        text = None
        if bid in J.get("title_override", {}):
            # a book sharing a volume: its own name from its end colophon, not the volume title
            text = J["title_override"][bid]
        elif lang == "th" and bid in TITLE_IDS and M[TITLE_IDS[1]]["heading"] is not None:
            # The Thai title page has one line "พระอภิธรรมปิฎก เล่ม N <book>":
            # basket + volume -> ^0, book title -> ^N-0
            full = D[M[TITLE_IDS[1]]["heading"]]["text"]
            mt = re.match(r"^(พระอภิธรรมปิฎก\s+เล่ม\s+[๐-๙]+)\s+(.+)$", full)
            basket, book = (mt.group(1), mt.group(2)) if mt else (full.rpartition(" ")[0], full.rpartition(" ")[2])
            text = basket if bid == "0" else book
        elif h is not None:
            text = D[h]["text"]
        elif bid in extra_titles and extra_titles[bid]:
            text = extra_titles[bid]
        if stack and last_group is not None:
            # root blocks with no Thai text of their own just before a heading: their Thai is
            # in the passage before them, so they join that passage's transclusion group
            out[last_group] += "\n" + "\n".join(stack)
            stack = []
        # (with no previous passage, e.g. a homage the Thai lacks, the stack carries forward)
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
    lines = [p for p in parts if p]
    out.append("\n".join(stack + [tl]))
    last_group = len(out) - 1
    stack = []
    out.append("\n".join(lines) + f" ^{bid}")
    first = re.sub(r"\s+", " ", lines[0])[:50]
    flag = "  [CHECK]" if bid in CHECK else ""
    ml.append(f"^{bid} T  {blk['text'][:40]!s}  ->  {first}{flag}")
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
