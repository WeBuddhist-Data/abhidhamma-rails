"""[align_vi3: general version for books 2-7: no matrix; usage adds <book> [pairs.json | class-levels JSON]]\nAlign the Vietnamese Dhammasangani draft to the pi-1 root blocks, using the Thai alignment
as a pivot (the Vietnamese was translated from the Thai and keeps its paragraph numbers 1-987).

- Matrix: Vietnamese list items before "Phần B" -> ^1-M1-*, ^1-M2-* in order (164 = 164).
- Body: for each paragraph N, the root blocks that hold Thai paragraph [N] receive the
  Vietnamese paragraph N, split at question sentences in the same proportion as the Thai
  questions; if the question counts differ, the whole paragraph goes to the first block and
  the others are stacked (MERGE), and the case is reported.
- Headings: paired within the gap before the same paragraph number.
"""
import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "th-tools"))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, th_draft, th_map, vi_draft, vi_pdf, out_json, out_report, BOOK = sys.argv[1:9]
ARG_PAIRS = sys.argv[9] if len(sys.argv) > 9 else None
R = parse_root(root_path)
T = parse_draft(th_draft)
TM = json.load(open(th_map, encoding="utf-8"))["mapping"]
V = parse_draft(vi_draft)
ids = [b["id"] for b in R]
pos = {b: k for k, b in enumerate(ids)}
report = []
TD = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")

mapping = {b: {"items": [], "heading": None, "pieces": []} for b in ids}
# pieces: list of (item_index, text) so that a Vietnamese paragraph can be split across blocks

# ---------------------------------------------------------------- title (from the PDF title page)
import pypdf  # noqa: E402

p1 = pypdf.PdfReader(vi_pdf).pages[0].extract_text() or ""
lines = [ln.strip() for ln in p1.splitlines() if ln.strip()]
title_basket = next((ln for ln in lines if ln.startswith("TẠNG VÔ TỶ PHÁP")), None)
kb = lines.index(title_basket) if title_basket else None
if kb is not None and kb + 1 < len(lines) and lines[kb + 1].startswith("("):
    title_basket = title_basket + " " + lines[kb + 1]
# book title: the first "BỘ …" line that is not "BỘ THỨ …" (the book number), with its "(PĀLI)" line
k = next((i for i, ln in enumerate(lines) if ln.startswith("BỘ ") and not ln.startswith("BỘ THỨ")), None)
title_book = (lines[k] + (" " + lines[k + 1] if k + 1 < len(lines) and lines[k + 1].startswith("(") else "")) if k is not None else None
if ARG_PAIRS and os.path.exists(ARG_PAIRS):
    # a volume with two books names both on its title page: the pairs file can give the title
    title_book = json.load(open(ARG_PAIRS, encoding="utf-8")).get("_title_book", title_book)
extra_titles = {"0": title_basket, f"{BOOK}-0": title_book}
report.append(f"TITLE  ^0 <- title page '{title_basket}';  ^{BOOK}-0 <- title page '{title_book}' [Ed: restored from the title page]")

# ---------------------------------------------------------------- front: homage
hom = next((i for i, it in enumerate(V[:40]) if re.match(r"^(NAMO|CUNG K)", it["text"].upper())), None)
if hom is not None:
    mapping["T-1"]["items"] = [hom]
pb = (hom + 1) if hom is not None else 0
BODY0 = pos[f"{BOOK}-0"] + 1

# ---------------------------------------------------------------- Thai paragraph -> root blocks
th_par = {}
cur = None
for i, it in enumerate(T):
    # a paragraph number at the start of an item, or of a row of a two-column table
    m = re.search(r"(?m)^\|?\s*\[([๐-๙]+)\]", it["text"])
    if m and it["kind"] in ("p", "h", "table"):
        cur = int(m.group(1).translate(TD))
    th_par[i] = cur
body_ids = ids[BODY0:]
par_blocks = defaultdict(list)  # N -> [(block_id, n_questions_from_N)]
for b in body_ids:
    if R[pos[b]]["kind"] != "t":
        continue
    cnt = defaultdict(int)
    for i in TM[b]["items"]:
        N = th_par.get(i)
        if N is None:
            continue
        cnt[N] += T[i]["text"].count("เป็นไฉน") if BOOK in ("1", "2", "4") else T[i]["text"].count("?")
        cnt.setdefault(N, cnt[N])
    for N, q in cnt.items():
        par_blocks[N].append((b, q))
for N in par_blocks:
    par_blocks[N].sort(key=lambda bq: pos[bq[0]])

# ---------------------------------------------------------------- Vietnamese paragraphs
v_par_start = {}
for i in range(pb, len(V)):
    m = re.match(r"^(\d{1,4})\.?(?:\s|$)", V[i]["text"])
    if V[i]["kind"] == "p" and m and int(m.group(1)) not in v_par_start:
        n = int(m.group(1))
        # accept only small forward steps: list numbers ("1.", "2.") and misprints ("1008"
        # for 1108) inside the text cannot hijack the paragraph sequence
        top = max(v_par_start) if v_par_start else 0
        if top < n <= top + 6:
            v_par_start[n] = i
starts = sorted(v_par_start.items(), key=lambda kv: kv[1])
report.append(f"BODY Vietnamese numbered paragraphs found: {len(starts)} (first {starts[0][0]}, last {starts[-1][0]})")


def split_units(text):
    """Split a paragraph into units that each start with a question sentence."""
    sents = re.split(r"(?<=[.?!…])\s+", text)
    # a leading paragraph number ("16.") stays with its sentence
    if len(sents) > 1 and re.fullmatch(r"\d{1,4}\.", sents[0]):
        sents = [sents[0] + " " + sents[1]] + sents[2:]
    units, cur_u = [], []
    for s in sents:
        if "?" in s and cur_u:
            units.append(" ".join(cur_u))
            cur_u = []
        cur_u.append(s)
    if cur_u:
        units.append(" ".join(cur_u))
    if BOOK == "4":
        # Puggalapaññatti asks two questions in a row ("Người ưa sân ra sao? Điều kiện sân như
        # thế nào? …" = "Katamo ca puggalo kodhano? Tattha katamo kodho? …"); the Thai counts one
        # "เป็นไฉน" per block: a question with no answer of its own joins the next question
        merged = []
        for u in units:
            if merged and merged[-1].rstrip().endswith("?") and merged[-1].count("?") == 1 and \
                    len(re.split(r"(?<=[.?!…])\s+", merged[-1].strip())) <= 2 and "?" in u:
                merged[-1] = merged[-1] + " " + u
            else:
                merged.append(u)
        units = merged
    return units


mismatch, merged_vi, pali_split, line_split = [], [], [], []
for k, (N, i0) in enumerate(starts):
    i1 = starts[k + 1][1] if k + 1 < len(starts) else len(V)
    items = [i for i in range(i0, i1) if V[i]["kind"] in ("p", "li")]
    units = []  # (item, text)
    for i in items:
        for u in split_units(V[i]["text"]):
            units.append((i, u))
    blocks = par_blocks.get(N, [])
    if not blocks:
        report.append(f"  !! Vietnamese paragraph {N}: no Thai/root blocks found")
        continue
    th_q = sum(q for _, q in blocks)
    vi_q = sum(1 for _, u in units if "?" in u)
    if len(blocks) == 1:
        mapping[blocks[0][0]]["pieces"].extend(units)
        continue
    # the Pāli questions of the blocks come first when they add up to the Vietnamese ones: they
    # are the target structure, and they correct local slips of the Thai pivot (e.g. §659: both
    # questions belong to ^2-572, none to ^2-573)
    pq0 = [(b, len(re.findall(r"\bkatam", R[pos[b]]["text"].lower())) if BOOK in ("1", "2", "4") else R[pos[b]]["text"].count("?"))
           for b, _ in blocks]
    if vi_q > 0 and sum(q for _, q in pq0) == vi_q:
        if th_q != vi_q or [q for _, q in pq0] != [q for _, q in blocks]:
            pali_split.append(N)
        blocks = pq0
        th_q = vi_q
    if th_q == 0 or th_q != vi_q:
        # line-count split: when the Vietnamese lines match the Thai lines of the blocks (or
        # the number of blocks), they go to the blocks line by line (e.g. §59: one list item per
        # "Ekavidhena saññākkhandho …" variant, no questions to cut on)
        lines_vi = [i for i in items if not re.fullmatch(r"\d{1,4}\.?", V[i]["text"].strip())]
        lead = [i for i in items if i not in lines_vi]
        th_cnt = [sum(1 for x in TM[b]["items"] if th_par.get(x) == N and T[x]["kind"] != "h") for b, _ in blocks]
        plan = None
        if lines_vi and sum(th_cnt) == len(lines_vi) and all(c > 0 for c in th_cnt):
            plan = th_cnt
        elif len(lines_vi) == len(blocks):
            plan = [1] * len(blocks)
        if plan:
            k = 0
            for (b, _), c in zip(blocks, plan):
                chunk = lines_vi[k:k + c]
                if k == 0:
                    chunk = lead + chunk
                mapping[b]["pieces"].extend((i, V[i]["text"]) for i in sorted(chunk))
                k += c
            line_split.append(N)
            continue
    if th_q != vi_q:
        # fall back on the Pāli questions of the blocks (katam- … ?), when they add up
        pq = [(b, len(re.findall(r"\bkatam", R[pos[b]]["text"].lower())) if BOOK in ("1", "2", "4") else R[pos[b]]["text"].count("?"))
              for b, _ in blocks]
        if sum(q for _, q in pq) == vi_q and vi_q > 0:
            blocks = pq
            pali_split.append(N)
        else:
            mismatch.append(N)
            mapping[blocks[0][0]]["pieces"].extend(units)
            for b, _ in blocks[1:]:
                merged_vi.append((b, blocks[0][0]))
            continue
    # give each block as many question units as its Thai questions; leading text to the first
    qi = 0
    order = []
    for b, q in blocks:
        order.extend([b] * q)
    owner = blocks[0][0]
    zero_q = [b for b, q in blocks if q == 0]
    for i, u in units:
        if "?" in u:
            owner = order[qi]
            qi += 1
        mapping[owner]["pieces"].append((i, u))
    for b in zero_q:
        if not mapping[b]["pieces"]:
            merged_vi.append((b, None))
report.append(f"  paragraphs split line by line (no questions, or counts differ; lines match): {len(line_split)} {line_split[:40]}")
report.append(f"  paragraphs split by the Pāli questions (Thai count differs): {len(pali_split)} {pali_split[:40]}")
report.append(f"  paragraphs with different question counts (whole paragraph to first block, rest MERGE): {len(mismatch)} {mismatch[:60]}")

# ---------------------------------------------------------------- headings in the body
def gap_key_root(hk):
    # the paragraph number of the first Thai text line (not a heading line) of the next block
    for b in ids[hk + 1:]:
        if R[pos[b]]["kind"] == "t":
            ns = [th_par.get(i) for i in sorted(TM[b]["items"]) if T[i]["kind"] != "h" and th_par.get(i) is not None]
            return ns[0] if ns else None
    return None


root_gap = defaultdict(list)
for hk in range(BODY0, len(ids)):
    if R[hk]["kind"] == "h":
        root_gap[gap_key_root(hk)].append(ids[hk])
vi_gap = defaultdict(list)
for i in range(pb, len(V)):
    if V[i]["kind"] == "h":
        nxt = next((N for N, s in starts if s > i), None)
        vi_gap[nxt].append(i)
# Tịnh Sự numbers his headings by level ("Phần B.", "1)", "a)"); some forms are his own
# groupings with no root heading ("I. PHÁP THIỆN", "1.1) Tâm đại thiện thứ nhứt"). Within a gap,
# a Vietnamese heading pairs with the next root heading of the level its form stands for; deeper
# root headings may be skipped (the Vietnamese lacks them), a shallower one is never crossed.
# Unpaired Vietnamese headings open the next block as bold lines.
def vi_class(t):
    for rx, c in ((r"^PHẦN [IVXL]+(\s*[-–.:]|\s+[A-ZĐÀ-Ỹ]|\s*$)", "PR"), (r"^[A-H]\.\s", "A"), (r"^Phần [A-Z]\.", "P"), (r"^[IVX]+\.\s", "R"),
                  (r"^\d+\.\d+\)", "NN"), (r"^\d+\)", "N"), (r"^[a-zđ]\)", "a")):
        if re.match(rx, t):
            return c
    return "x"


OVERRIDES = None
PAIR_FIX = {}
NAME_MODE = False
CLASS_LEVEL = {"P": 3, "N": 4, "a": 5}
if ARG_PAIRS:
    if os.path.exists(ARG_PAIRS):
        _j = json.load(open(ARG_PAIRS, encoding="utf-8"))
        if _j.get("_pali_names"):
            NAME_MODE = True
            CLASS_LEVEL = {}
            PAIR_FIX = {k: v for k, v in _j.items() if not k.startswith("_")}
        elif "_class_levels" in _j:
            # automatic pairing by heading form -> root level, then reviewed corrections
            CLASS_LEVEL = _j["_class_levels"]
            PAIR_FIX = {k: v for k, v in _j.items() if not k.startswith("_")}
        else:
            OVERRIDES = {k: v for k, v in _j.items() if not k.startswith("_")}
    else:
        CLASS_LEVEL = json.loads(ARG_PAIRS)
extra_vi_heads = []
pair_log = []
if OVERRIDES is not None:
    # reviewed pairs: root heading -> Vietnamese heading text, matched in document order
    import unicodedata

    def _nk(s):  # compare headings NFC-normalised, case-folded, spaces collapsed
        return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip().casefold()

    vh_all = [i for i in range(pb, len(V)) if V[i]["kind"] == "h"]
    used, last = set(), -1
    for b in ids:
        if b not in OVERRIDES:
            continue
        want = _nk(OVERRIDES[b])
        hit = next((i for i in vh_all if i > last and i not in used and _nk(V[i]["text"]).startswith(want)), None)
        if hit is None:
            pair_log.append(f"   !! ^{b}: Vietnamese heading not found after item {last}: {want}")
            continue
        mapping[b]["heading"] = hit
        used.add(hit)
        last = hit
        pair_log.append(f"   ^{b:12} {R[pos[b]]['text'][:30]:30} <- {V[hit]['text'][:50]}")
    extra_vi_heads = [i for i in vh_all if i not in used]
    vi_gap = {}  # skip the automatic pairing below
for key, vh in vi_gap.items():
    rh = root_gap.get(key, [])
    p = 0
    for v_i in vh:
        lvl = CLASS_LEVEL.get(vi_class(V[v_i]["text"]))
        hit = None
        if lvl is not None:
            for q in range(p, len(rh)):
                rl = R[pos[rh[q]]]["level"]
                if rl < lvl:
                    break
                if rl == lvl:
                    hit = q
                    break
        if hit is None:
            extra_vi_heads.append(v_i)
            pair_log.append(f"   [{key}] vi-only  {V[v_i]['text'][:50]}")
            continue
        mapping[rh[hit]]["heading"] = v_i
        pair_log.append(f"   [{key}] ^{rh[hit]:12} {R[pos[rh[hit]]]['text'][:30]:30} <- {V[v_i]['text'][:50]}")
        p = hit + 1
if NAME_MODE:
    # Kathāvatthu: Tịnh Sự gives the Pāli name in brackets ("THA DẪN NGỮ (PARŪPAHĀRAKATHĀ)");
    # match it, in order, with the root headings ("(10) 1. Parūpahārakathā"), ignoring numbering,
    # case and diacritics; "PHẨM THỨ HAI …" is the second vagga ("Dutiyavaggo") and so on.
    import difflib
    import unicodedata as _ud

    def pkey(s):
        s = re.sub(r"^\s*(\(\d+(-\d+)?\)\s*)?(\d+(-\d+)?\.\s*)?", "", s)
        s = "".join(c for c in _ud.normalize("NFD", s.lower()) if not _ud.combining(c))
        return re.sub(r"[^a-z]", "", s)

    ORD_VI = ["NHẤT", "HAI", "BA", "TƯ", "NĂM", "SÁU", "BẢY", "TÁM", "CHÍN", "MƯỜI", "MƯỜI MỘT", "MƯỜI HAI",
              "MƯỜI BA", "MƯỜI BỐN", "MƯỜI LĂM", "MƯỜI SÁU", "MƯỜI BẢY", "MƯỜI TÁM", "MƯỜI CHÍN", "HAI MƯƠI",
              "HAI MƯƠI MỐT", "HAI MƯƠI HAI", "HAI MƯƠI BA"]
    root_vaggas = [b["id"] for b in R[BODY0:] if b["kind"] == "h" and b["level"] == 3 and b["text"].strip().endswith("vaggo")]
    root_heads_b = [k for k in range(BODY0, len(R)) if R[k]["kind"] == "h"]
    vh_all3 = [i for i in range(pb, len(V)) if V[i]["kind"] == "h"]
    last = BODY0 - 1
    for i in vh_all3:
        t = V[i]["text"].strip()
        mv = re.match(r"^(ĐẠI )?PHẨM THỨ (.+)$", t)
        if mv:
            o = ORD_VI.index(mv.group(2).strip()) + 1 if mv.group(2).strip() in ORD_VI else None
            if o and o >= 2 and o - 2 < len(root_vaggas) and pos[root_vaggas[o - 2]] > last:
                b = root_vaggas[o - 2]
                mapping[b]["heading"] = i
                last = pos[b]
                pair_log.append(f"   ^{b:12} {R[pos[b]]['text'][:30]:30} <- {t[:50]}")
            else:
                extra_vi_heads.append(i)
            continue
        groups = [g for g in re.findall(r"\(([^()]*)\)", t) if re.search(r"[A-Za-z]", g)]
        if not groups:
            extra_vi_heads.append(i)
            continue
        key = pkey(groups[-1])
        best, bk, best_raw = -1.0, None, 0.0
        # nearest good candidate first: a small cost per root heading skipped, and no long jumps
        for d, k in enumerate([k for k in root_heads_b if k > last][:40]):
            rk = pkey(R[k]["text"])
            if not rk or not key:
                continue
            s_ = difflib.SequenceMatcher(None, key, rk).ratio()
            if (key in rk or rk in key) and min(len(key), len(rk)) >= 6:
                s_ = max(s_, 0.9)
            if s_ - 0.01 * d > best:
                best, bk, best_raw = s_ - 0.01 * d, k, s_
        best = best_raw
        if bk is not None and best >= 0.85:
            mapping[R[bk]["id"]]["heading"] = i
            last = bk
            pair_log.append(f"   ^{R[bk]['id']:12} {R[bk]['text'][:30]:30} <- {t[:50]}  ({best:.2f})")
        else:
            extra_vi_heads.append(i)
            pair_log.append(f"   vi-only  {t[:60]}  (best {best:.2f})")
    used3 = {mapping[x]["heading"] for x in ids if mapping[x].get("heading") is not None}
    extra_vi_heads = [i for i in vh_all3 if i not in used3]
    pair_log = [ln for ln in pair_log if not re.match(r"^   \[\d+\] vi-only", ln)]
if PAIR_FIX:
    # reviewed corrections on top of the automatic pairs: the Vietnamese heading is searched
    # between the Vietnamese headings of the nearest paired root headings before and after
    import unicodedata

    def _nk2(s):
        return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip().casefold()

    vh_all2 = [i for i in range(pb, len(V)) if V[i]["kind"] == "h"]
    for b in PAIR_FIX:
        mapping[b]["heading"] = None  # clear every corrected heading before placing any
    for b in ids:
        if b not in PAIR_FIX:
            continue
        val = PAIR_FIX[b]
        if val is None:
            pair_log.append(f"   FIX ^{b}: no Vietnamese heading")
            continue
        k0 = pos[b]
        lo = max([mapping[x]["heading"] for x in ids[:k0] if mapping[x].get("heading") is not None and pos[x] >= BODY0] or [pb - 1])
        hi = min([mapping[x]["heading"] for x in ids[k0 + 1:] if mapping[x].get("heading") is not None] or [len(V)])
        cand = [i for i in vh_all2 if lo < i < hi and _nk2(V[i]["text"]).startswith(_nk2(val))]
        if not cand:
            pair_log.append(f"   !! FIX ^{b}: '{val}' not found between items {lo} and {hi}")
            continue
        mapping[b]["heading"] = cand[0]
        pair_log.append(f"   FIX ^{b:12} {R[pos[b]]['text'][:30]:30} <- {V[cand[0]]['text'][:50]}")
    used2 = {mapping[x]["heading"] for x in ids if mapping[x].get("heading") is not None}
    extra_vi_heads = [i for i in vh_all2 if i not in used2]
report.append("HEADING PAIRS (gap = next paragraph number)")
report.extend(pair_log)
unmatched_h = [b for b in ids if R[pos[b]]["kind"] == "h" and mapping[b]["heading"] is None and b not in extra_titles]
report.append(f"UNMATCHED root headings (no Vietnamese heading): {len(unmatched_h)}")
report.append("  " + " ".join("^" + x for x in unmatched_h))
report.append(f"EXTRA Vietnamese headings kept as bold lines inside the next block: {len(extra_vi_heads)}")
no_text = [b for b in ids if R[pos[b]]["kind"] == "t" and not mapping[b]["items"] and not mapping[b]["pieces"]]
report.append(f"ROOT text blocks with no Vietnamese text of their own (MERGE into neighbour): {len(no_text)}")
report.append("  " + " ".join("^" + x for x in no_text))

# ---------------------------------------------------------------- heading boundaries
# Every Vietnamese line (item or split piece) must sit in a root block between the two paired
# headings that surround it in the PDF: a line placed before its heading moves to the start of
# the first block after it, one placed after the next heading moves to the end of the last block
# before it (e.g. a subtitle line "Phân theo bốn bực." printed under a heading but attached to
# the paragraph before; the Rūpakaṇḍa uddesa §502, which the root keeps before "Mātikā").
import bisect  # noqa: E402

body_start = BODY0
kept = sorted((pos[b], mapping[b]["heading"]) for b in ids
              if R[pos[b]]["kind"] == "h" and mapping[b]["heading"] is not None and pos[b] >= body_start)
# keep only pairs in increasing draft order (longest run)
seq_ok, last_v = [], -1
for rp, vh in kept:
    if vh > last_v:
        seq_ok.append((rp, vh))
        last_v = vh
k_root = [x[0] for x in seq_ok]
k_vi = [x[1] for x in seq_ok]
seg_blocks = defaultdict(list)
for b in ids[body_start:]:
    if R[pos[b]]["kind"] == "t":
        seg_blocks[bisect.bisect_left(k_root, pos[b])].append(b)
moved = 0
for b in ids[body_start:]:
    if R[pos[b]]["kind"] != "t":
        continue
    sb = bisect.bisect_left(k_root, pos[b])
    for field in ("items", "pieces"):
        keep_list = []
        for entry in mapping[b][field]:
            i = entry if field == "items" else entry[0]
            si = bisect.bisect_left(k_vi, i)
            tb = seg_blocks.get(si)
            if si == sb or not tb:
                keep_list.append(entry)
                continue
            dest = tb[-1] if si < sb else tb[0]
            mapping[dest][field].append(entry)
            moved += 1
        mapping[b][field] = keep_list
for b in ids:
    mapping[b]["items"].sort()
    mapping[b]["pieces"].sort(key=lambda e: e[0])
report.append(f"BOUNDARIES: {moved} Vietnamese lines moved to the right side of their heading")

json.dump({"mapping": mapping, "extra_titles": extra_titles, "extra_heads": extra_vi_heads},
          open(out_json, "w", encoding="utf-8"), ensure_ascii=False)
open(out_report, "w", encoding="utf-8").write("\n".join(report) + "\n")
print("\n".join(r if len(r) < 300 else r[:300] + " ..." for r in report))
