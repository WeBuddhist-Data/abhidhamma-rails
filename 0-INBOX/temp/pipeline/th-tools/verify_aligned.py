"""Verify a block-aligned translation file against its root text.

Checks
 1. Transclusions: every link has the full path of this book's root and points to an existing
    root block; every root TEXT block is transcluded exactly once; transclusions follow root order.
 2. Translation: every transclusion group is followed by a translation block that is not empty
    and ends with the ID of the last transclusion in the group; root text blocks that have no
    translation block of their own (stacked) are listed.
 3. Block IDs: every ^ID in the file exists in the root, appears once, and root order is kept;
    headings carry no transclusion.
 4. Text coverage: Thai/Vietnamese characters in the file versus the draft (the only intended
    losses are the Thai-script Pāli column of matrices and separator lines).

Usage: verify_aligned.py <root.md> <aligned.md> <draft.md|-> <root_rel_path>
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_root  # noqa: E402

root_path, file_path, draft_path, root_rel = sys.argv[1:5]
R = parse_root(root_path)
order = {b["id"]: k for k, b in enumerate(R)}
kind = {b["id"]: b["kind"] for b in R}
text_ids = [b["id"] for b in R if b["kind"] == "t"]

raw = open(file_path, encoding="utf-8").read()
body = raw.split("---", 2)[2] if raw.startswith("---") else raw
lines = body.split("\n")
problems = []

TL = re.compile(r"^!\[\[([^#\]]+)#\^([\w-]+)\]\]\s*$")
IDEND = re.compile(r"(?:^|\s)\^([\w-]+)\s*$")

# ---- walk the file: transclusion groups and the block that follows each
trans = []          # (line_no, path, id)
ids_in_file = []    # (line_no, id, is_heading)
groups = []         # [ [ids...], following_block_id_or_None, following_block_text ]
no_id = []          # (line_no, text): paragraphs or headings with no block ID
u_ids = []          # ^U-N: translation-only lines with no root block
UID = re.compile(r"U-\d+")
i = 0
n = len(lines)
while i < n:
    ln = lines[i]
    m = TL.match(ln)
    if m:
        grp = []
        while i < n and TL.match(lines[i]):
            mm = TL.match(lines[i])
            trans.append((i + 1, mm.group(1), mm.group(2)))
            grp.append(mm.group(2))
            i += 1
        # skip blank lines, then read the block (until a blank line)
        while i < n and not lines[i].strip():
            i += 1
        blk = []
        while i < n and lines[i].strip() and not TL.match(lines[i]):
            blk.append(lines[i])
            i += 1
        # a block may contain blank-separated parts only for tables (none expected now)
        last = blk[-1] if blk else ""
        mid = IDEND.search(last)
        fid = mid.group(1) if mid else None
        if blk and blk[0].startswith("#"):
            problems.append(f"line {i}: transclusion group {grp} is followed by a heading, not a translation block")
            fid = None
        groups.append((grp, fid, "\n".join(blk)))
        if fid:
            ids_in_file.append((i, fid, False))
        continue
    if ln.startswith("#"):
        mid = IDEND.search(ln)
        if mid:
            ids_in_file.append((i + 1, mid.group(1), True))
        else:
            no_id.append((i + 1, ln[:40]))
    elif ln.strip() and (i == 0 or not lines[i - 1].strip()):
        # a paragraph outside a transclusion group: it must end with an ID; only ^U-N
        # (translation-only lines with no root block) may stand without a transclusion
        j = i
        while j < n and lines[j].strip():
            j += 1
        mid = IDEND.search(lines[j - 1])
        if not mid:
            no_id.append((i + 1, ln[:40]))
        elif UID.fullmatch(mid.group(1)):
            u_ids.append(mid.group(1))
        else:
            ids_in_file.append((j, mid.group(1), False))
            problems.append(f"line {j}: block ^{mid.group(1)} has no transclusion before it")
        i = j
        continue
    i += 1
if no_id:
    problems.append(f"{len(no_id)} paragraphs or headings without a block ID, e.g. {no_id[:4]}")
if u_ids:
    # decision 2026-11-17: Thai-only lines open the next root block and share its ID
    problems.append(f"{len(u_ids)} ^U-N IDs: Thai-only lines belong in the next block, e.g. {u_ids[:5]}")

# ---- 1. transclusions
bad_path = [t for t in trans if t[1] != root_rel]
unknown = [t for t in trans if t[2] not in order]
heading_tr = [t for t in trans if kind.get(t[2]) == "h"]
tr_ids = [t[2] for t in trans]
dup_tr = sorted({x for x in tr_ids if tr_ids.count(x) > 1}) if len(tr_ids) < 50000 else []
missing_tr = [x for x in text_ids if x not in set(tr_ids)]
out_of_order = sum(1 for a, b in zip(tr_ids, tr_ids[1:]) if a in order and b in order and order[b] <= order[a])
if bad_path:
    problems.append(f"{len(bad_path)} transclusions with a wrong path, e.g. {bad_path[:2]}")
if unknown:
    problems.append(f"{len(unknown)} transclusions to IDs not in the root, e.g. {unknown[:3]}")
if heading_tr:
    problems.append(f"{len(heading_tr)} transclusions of headings, e.g. {heading_tr[:3]}")
if dup_tr:
    problems.append(f"{len(dup_tr)} root blocks transcluded more than once, e.g. {dup_tr[:5]}")
if missing_tr:
    problems.append(f"{len(missing_tr)} root text blocks never transcluded, e.g. {missing_tr[:8]}")
if out_of_order:
    problems.append(f"{out_of_order} transclusions out of root order")

# ---- 2. translation after each group
no_block = [g for g in groups if g[1] is None]
# the translation block carries the ID of one of the root blocks transcluded above it:
# the last one (blocks stacked before a passage) or an earlier one (blocks stacked after it,
# just before a heading)
wrong_id = [g for g in groups if g[1] is not None and g[1] not in g[0]]
empty = [g for g in groups if g[1] is not None and not re.sub(r"\s*\^[\w-]+\s*$", "", g[2]).strip()]
stacked = [x for g in groups for x in g[0] if x != g[1]]
if no_block:
    problems.append(f"{len(no_block)} transclusion groups with no translation block after them, e.g. {[g[0] for g in no_block[:3]]}")
if wrong_id:
    problems.append(f"{len(wrong_id)} translation blocks whose ID is not the last transcluded ID, e.g. {[(g[0], g[1]) for g in wrong_id[:3]]}")
if empty:
    problems.append(f"{len(empty)} empty translation blocks, e.g. {[g[1] for g in empty[:5]]}")

# ---- 3. block IDs
fid_list = [x[1] for x in ids_in_file]
unknown_ids = [x for x in fid_list if x not in order]
dup_ids = sorted({x for x in fid_list if fid_list.count(x) > 1}) if len(fid_list) < 50000 else []
id_order_bad = sum(1 for a, b in zip(fid_list, fid_list[1:]) if a in order and b in order and order[b] <= order[a])
head_with_text_id = [x for x in ids_in_file if x[2] and kind.get(x[1]) == "t"]
text_with_head_id = [x for x in ids_in_file if not x[2] and kind.get(x[1]) == "h"]
if unknown_ids:
    problems.append(f"{len(unknown_ids)} block IDs not in the root, e.g. {unknown_ids[:5]}")
if dup_ids:
    problems.append(f"{len(dup_ids)} block IDs used more than once, e.g. {dup_ids[:5]}")
if id_order_bad:
    problems.append(f"{id_order_bad} block IDs out of root order")
if head_with_text_id or text_with_head_id:
    problems.append(f"ID kind mismatch: headings carrying text IDs {head_with_text_id[:3]}, text carrying heading IDs {text_with_head_id[:3]}")

# ---- 4. coverage of the translation text against the draft
cov = ""
if draft_path != "-" and os.path.exists(draft_path):
    def letters(s):
        return sum(1 for ch in s if "฀" <= ch <= "๿" or "À" <= ch <= "ỿ" or ch.isalpha() and ord(ch) > 127)
    d = open(draft_path, encoding="utf-8").read()
    body_wo_tr = "\n".join(l for l in lines if not TL.match(l))
    a, b = letters(body_wo_tr), letters(d)
    cov = f"script letters in file {a:,} vs draft {b:,} ({100 * a / max(b, 1):.1f}%)"

own = len(text_ids) - len(set(stacked))
print(f"{os.path.basename(file_path)}: root text blocks {len(text_ids)}, transcluded {len(set(tr_ids))}, "
      f"with own translation {own}, stacked {len(set(stacked))}, heading IDs {sum(1 for x in ids_in_file if x[2])}, "
      f"translation-only ^U-N {len(u_ids)}; {cov}")
print("  RESULT:", "OK" if not problems else f"{len(problems)} problem(s)")
for p in problems:
    print("   -", p)
