"""Align a Thai Royal-edition book to its root by paragraph-level dynamic programming.

Units: each Thai numbered paragraph [n] (with its continuation paragraphs) is one unit; each
root text block is one block. A banded DP pairs units and blocks in order with moves
1:1, 2:1, 3:1, 1:2 … 1:5, 1:0 and 0:1, scored by a Pāli/Thai consonant-skeleton cosine
(less a small penalty for uneven moves). A unit paired with several blocks is split over
them paragraph by paragraph. Headings are then paired inside the gap between the same two
blocks on both sides; unpaired Thai headings stay as bold lines in the next block.
"Groups of N" (root 'N-vidhena', Thai 'หมวดละ N') are repaired by number.

Usage: align_th3.py <root.md> <draft.md> <map.json> <report.txt> <book>
"""
import bisect
import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, th_path, out_json, out_report, BOOK = sys.argv[1:6]
R = parse_root(root_path)
T = parse_draft(th_path)
report = []
TD = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")

# ------------------------------------------------------------ similarity
TH = {}
for chars, v in (("กขฃคฅฆ", "k"), ("จฉชฌ", "c"), ("ซศษส", "s"), ("ฎฏฐฑฒดตถทธ", "t"),
                 ("งญณนํ", "n"), ("บปผฝพฟภ", "p"), ("ม", "m"), ("ย", "y"), ("รฤ", "r"),
                 ("ลฦฬ", "l"), ("ว", "v"), ("หฮ", "h")):
    for ch in chars:
        TH[ch] = v
PI = {"k": "k", "g": "k", "c": "c", "j": "c", "t": "t", "d": "t", "n": "n", "p": "p", "b": "p",
      "m": "m", "y": "y", "r": "r", "l": "l", "v": "v", "s": "s", "h": "h"}


def skel_th(s):
    return "".join(TH[ch] for i, ch in enumerate(s) if ch in TH and not (i + 1 < len(s) and s[i + 1] == "์"))


def skel_pi(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    out = []
    for ch in s:
        if ch in PI:
            if ch == "h" and out and out[-1] in "kctp":
                continue
            out.append(PI[ch])
    return "".join(out)


def grams(sk, n=3):
    return Counter(sk[i:i + n] for i in range(len(sk) - n + 1))


df = Counter()
for b in R:
    df.update(grams(skel_pi(b["text"])).keys())
NDOC = len(R)
idf = {g: math.log((NDOC + 1) / (c + 1)) + 1 for g, c in df.items()}


def wvec(text, th):
    c = grams(skel_th(text) if th else skel_pi(text))
    return {g: n * idf[g] for g, n in c.items() if g in idf}


def dot(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(g, 0.0) for g, x in a.items())


# ------------------------------------------------------------ front matter
title_idx = 0 if T[0]["kind"] == "h" else None
homage_idx = next((k for k, it in enumerate(T) if it["text"].startswith("ขอนอบน้อม")), None)
mapping = {b["id"]: {"items": [], "heading": None} for b in R}
if homage_idx is not None:  # (a book sharing a volume may have no homage of its own)
    mapping["T-1"]["items"] = [homage_idx]
mapping[f"{BOOK}-0"]["heading"] = title_idx
root_body = next(k for k, b in enumerate(R) if b["id"] == f"{BOOK}-0") + 1
start_t = max([x for x in (title_idx, homage_idx) if x is not None] or [-1]) + 1
pre_items = [k for k in range(0, start_t) if k not in (title_idx, homage_idx)]

# ------------------------------------------------------------ units and blocks
body_items = [k for k in range(start_t, len(T)) if T[k]["kind"] not in ("hr",)]
units, unit_heads = [], []  # unit = list of non-heading items; headings kept separately
after_head = False
SECTION_SUFFIX = re.compile(r"(มาติกา|นิทเทส|วาร|ภาชนีย์|วิภังค์|ปกรณ์|กถา|ปุจฉกะ|นัย|ทุกะ|ติกะ|จำพวก\)|จบ)\s*$")


def _is_list_line(pos):
    """A centred line inside a list: no number label, not a section name, preceded by text and
    not followed by a new numbered paragraph."""
    k = body_items[pos]
    t = T[k]["text"]
    if re.match(r"^(\[[๐-๙]+\]|[๐-๙]+(-[๐-๙]+)?\.)", t) or SECTION_SUFFIX.search(t):
        return False
    prev = body_items[pos - 1] if pos > 0 else None
    if prev is None or T[prev]["kind"] == "h" and not _is_list_line_cache.get(pos - 1, False):
        return False
    if prev is not None and T[prev]["text"].rstrip().endswith(("จบ", "จบ.")):
        return False
    nxt = body_items[pos + 1] if pos + 1 < len(body_items) else None
    return nxt is None or not re.match(r"^\[[๐-๙]+\]", T[nxt]["text"])


_is_list_line_cache = {}
pending_title = False
for pos, k in enumerate(body_items):
    it = T[k]
    if it["kind"] == "h" and units and _is_list_line(pos):
        _is_list_line_cache[pos] = True
        units[-1].append(k)  # list item printed centred: part of the current paragraph
        continue
    if it["kind"] == "h":
        unit_heads.append(k)
        after_head = True
        continue
    # a short numbered title ("๑. ขันธบัญญัติ") directly before a numbered paragraph [n]
    # belongs to that paragraph: it opens the next unit
    nxt_item = body_items[pos + 1] if pos + 1 < len(body_items) else None
    is_title = (re.match(r"^[๐-๙]+\.\s", it["text"]) and len(it["text"]) < 40 and nxt_item is not None
                and re.match(r"^\[[๐-๙]+\]", T[nxt_item]["text"]))
    # a unit starts at a numbered paragraph [n], or at the first paragraph after a heading
    if is_title:
        units.append([k])
        pending_title = True
    elif re.match(r"^(\|\s*)?\[[๐-๙]+\]", it["text"]) and pending_title:
        units[-1].append(k)
        pending_title = False
    elif not units or (after_head and BOOK != "7") or re.match(r"^(\|\s*)?\[[๐-๙]+\]", it["text"]) or (
            it["kind"] == "table" and re.search(r"(?m)^\|\s*\[[๐-๙]+\]", it["text"])):
        units.append([k])
        pending_title = False
    else:
        units[-1].append(k)
    after_head = False
if pre_items:
    units[0] = pre_items + units[0]
blocks = [k for k in range(root_body, len(R)) if R[k]["kind"] == "t"]
UV = []
for u in units:
    d = Counter()
    for k in u:
        d.update(wvec(T[k]["text"], True))
    UV.append(dict(d))
BV = [wvec(R[k]["text"], False) for k in blocks]
nU, nB = len(UV), len(BV)
report.append(f"UNITS Thai {nU} (numbered paragraphs), root text blocks {nB}")

# norms and adjacent dot products for sums of consecutive units / blocks
MAXK = 8
UU = [[dot(UV[i], UV[i + d]) if i + d < nU else 0.0 for d in range(MAXK)] for i in range(nU)]
BB = [[dot(BV[j], BV[j + d]) if j + d < nB else 0.0 for d in range(MAXK)] for j in range(nB)]


def range_norm(tab, i, a):
    s = sum(tab[i + x][0] for x in range(a))
    s += 2 * sum(tab[i + x][y - x] for x in range(a) for y in range(x + 1, a))
    return math.sqrt(s) if s > 0 else 1.0


BAND = 160
DOTC = {}


def ub(i, j):
    key = (i, j)
    if key not in DOTC:
        DOTC[key] = dot(UV[i], BV[j])
    return DOTC[key]


def score(i, a, j, b):
    """cosine between units i..i+a-1 and blocks j..j+b-1"""
    num = sum(ub(i + x, j + y) for x in range(a) for y in range(b))
    return num / (range_norm(UU, i, a) * range_norm(BB, j, b))


MOVES = [(1, 1, 0.0), (2, 1, 0.05), (3, 1, 0.10), (4, 1, 0.15), (5, 1, 0.20),
         (6, 1, 0.25), (7, 1, 0.30), (8, 1, 0.35),
         (1, 2, 0.05), (1, 3, 0.10), (1, 4, 0.15), (1, 5, 0.20)]
SKIP = 0.25
NEG = -1e18
if BOOK == "7":
    # Paṭṭhāna: the Thai omits whole Pāli sections (e.g. the Pucchāvāra). Spreading one Thai
    # paragraph over several dissimilar root blocks must not be cheaper than leaving them
    # stacked, or the alignment drifts into the omitted section.
    MOVES = [(a, b, (0.3 * (b - 1)) if b > 1 else pen) for a, b, pen in MOVES]


def dp_section(u0, u1, b0, b1):
    """Paragraph-level DP on units u0..u1-1 and blocks b0..b1-1; moves in global indexes."""
    nu, nb = u1 - u0, b1 - b0
    if nu == 0 and nb == 0:
        return []
    if nu == 0:
        return [(u0, 0, b0 + y, 1) for y in range(nb)]
    if nb == 0:
        # Thai text between two headings with no root block between them (e.g. a list the
        # Thai prints before its "อุทเทสวาร" heading): it goes forward to the next block
        return [(u0 + x, 1, b0, -1) for x in range(nu)]
    ratio = nb / nu
    best, back = {(0, 0): 0.0}, {}
    for i in range(nu + 1):
        c = int(i * ratio)
        for j in range(max(0, c - BAND), min(nb, c + BAND) + 1):
            if (i, j) == (0, 0):
                continue
            bv, bm = NEG, None
            for a, b, pen in MOVES:
                if i >= a and j >= b and (i - a, j - b) in best:
                    v = best[(i - a, j - b)] + score(u0 + i - a, a, b0 + j - b, b) - pen
                    if v > bv:
                        bv, bm = v, (a, b)
            # no skipping at the very start of a section: its first Thai paragraph and its
            # first root block (both right after the paired heading) go together
            if i >= 1 and j >= 1 and (i - 1, j) in best and best[(i - 1, j)] - SKIP > bv:
                bv, bm = best[(i - 1, j)] - SKIP, (1, 0)
            if j >= 1 and i >= 1 and (i, j - 1) in best and best[(i, j - 1)] - SKIP > bv:
                bv, bm = best[(i, j - 1)] - SKIP, (0, 1)
            if bm:
                best[(i, j)], back[(i, j)] = bv, bm
    i, j, mv = nu, nb, []
    while (i, j) != (0, 0):
        a, b = back[(i, j)]
        mv.append((u0 + i - a, a, b0 + j - b, b))
        i, j = i - a, j - b
    return list(reversed(mv))


# The two editions name the "group of N" sections with different nouns (Pāli Ekakauddeso,
# Thai เอกกมาติกา; Pāli Ekakapuggalapaññatti, Thai เอกกนิทเทส): match on the number word.
NUMW = [("ekādasaka", "เอกาทสก"), ("ekaka", "เอกก"), ("duka", "ทุก"), ("tika", "ติก"), ("catukka", "จตุกก"),
        ("pañcaka", "ปัญจก"), ("chakka", "ฉักก"), ("sattaka", "สัตตก"), ("aṭṭhaka", "อัฏฐก"),
        ("navaka", "นวก"), ("dasaka", "ทสก")]


ORD = ["paṭhama", "dutiya", "tatiya", "catuttha", "pañcama", "chaṭṭha", "sattama", "aṭṭhama", "navama",
       "dasama", "ekādasama", "dvādasama", "terasama", "cuddasama", "pannarasama", "soḷasama",
       "sattarasama", "aṭṭhārasama", "ekūnavīsatima", "vīsatima", "ekavīsatima", "bāvīsatima", "tevīsatima"]


def num_sim(pi_text, th_text):
    p = pi_text.lower().lstrip("(0123456789) ")
    t = re.sub(r"^[๐-๙]+\.\s*", "", th_text.strip())
    # Yamaka: "(Ka) uddeso" <-> "อุทเทสวาร", "(Kha) niddeso" <-> "นิทเทสวาร"
    pp = re.sub(r"^\(?(ka|kha|ga|gha)\)\s*", "", p)
    if pp in ("uddeso", "uddesavāro"):
        return 0.75 if t.startswith("อุทเทส") else 0.0
    if pp in ("niddeso", "niddesavāro"):
        return 0.75 if t.startswith("นิทเทส") else 0.0
    # "Pañcamavaggo" <-> "วรรคที่ ๕"
    mv = re.match(r"^วรรคที่\s*([๐-๙]+)", t)
    if p.endswith("vaggo") and mv:
        n = int(mv.group(1).translate(TD))
        return 0.8 if 0 < n <= len(ORD) and p == ORD[n - 1] + "vaggo" else 0.0
    for pw, tw in NUMW:
        if p.startswith(pw):
            if not t.startswith(tw):
                return 0.0
            # uddeso <-> มาติกา, niddeso / puggalapaññatti <-> นิทเทส
            if ("uddes" in p and "มาติกา" in t) or (("niddes" in p or "paññatti" in p) and "นิทเทส" in t):
                return 0.7
            return 0.4
    return 0.0


# ------------------------------------------------------------ anchor headings (unique names)
# Headings whose name occurs once in the book on each side (chapter names and other unique
# section names) pair with near certainty; they cut the book into sections so that the
# paragraph alignment cannot drift across them.
def _norm_h(s):
    return re.sub(r"[\s\[\]().]|^[๐-๙]+\.\s*", "", s)


root_heads_all = [k for k in range(root_body, len(R)) if R[k]["kind"] == "h"]
rc = Counter(_norm_h(R[k]["text"]) for k in root_heads_all)
tcn = Counter(_norm_h(T[h]["text"]) for h in unit_heads)
# all headings take part; a pair needs similarity >= 0.55 (unique names get a small bonus),
# order is kept by the LCS and the proportion check below rejects far-off pairs
UR = list(root_heads_all)
UT = list(unit_heads)
UNIQ_R = {k for k in UR if rc[_norm_h(R[k]["text"])] == 1}
UNIQ_T = {h for h in UT if tcn[_norm_h(T[h]["text"])] == 1}


def _cos(a, b):
    return dot(a, b) / ((math.sqrt(dot(a, a)) or 1.0) * (math.sqrt(dot(b, b)) or 1.0))


URV = [wvec(R[k]["text"], False) for k in UR]
UTV = [wvec(T[h]["text"], True) for h in UT]
na_, nb_ = len(UR), len(UT)
# banded: only pairs at roughly the same relative position in the book are compared
HBAND = max(150, int(0.08 * max(na_, nb_)))
_SC = {}


def SCf(x, y):
    key = (x, y)
    if key not in _SC:
        _SC[key] = max(_cos(URV[x], UTV[y]), num_sim(R[UR[x]]["text"], T[UT[y]]["text"])) + \
            (0.1 if (UR[x] in UNIQ_R and UT[y] in UNIQ_T) else 0.0)
    return _SC[key]


def yrange(x):
    c = int(x * nb_ / max(na_, 1))
    return max(1, c - HBAND), min(nb_, c + HBAND)


L = {}


def Lg(x, y):
    if x == 0 or y == 0:
        return 0.0
    return L.get((x, y), -1e9)


for x in range(1, na_ + 1):
    lo, hi = yrange(x)
    for y in range(lo, hi + 1):
        s = SCf(x - 1, y - 1) - 0.55
        best_v = max(Lg(x - 1, y), Lg(x, y - 1), (Lg(x - 1, y - 1) + s) if s > 0 else -1e9)
        L[(x, y)] = best_v if best_v > -1e8 else 0.0
x, y, anchor_pairs = na_, nb_, []
while x > 0 and y > 0:
    lo, hi = yrange(x)
    if y > hi:
        y = hi
        continue
    if y < lo:
        x -= 1
        continue
    s = SCf(x - 1, y - 1) - 0.55
    if s > 0 and abs(Lg(x, y) - (Lg(x - 1, y - 1) + s)) < 1e-9:
        anchor_pairs.append((UR[x - 1], UT[y - 1]))
        x, y = x - 1, y - 1
    elif Lg(x, y) == Lg(x - 1, y):
        x -= 1
    else:
        y -= 1
anchor_pairs.reverse()

# Kathā headings ("…kathā" / "…กถา") come in the same order in both editions: pair them in
# order among themselves with a lower similarity floor, and add them to the anchors.
PK = [k for k in root_heads_all if re.search(r"kathā\s*$", R[k]["text"])]
TK = [h for h in unit_heads if re.search(r"กถา(\s*อีกกถาหนึ่ง)?\s*$", T[h]["text"])]
if PK and TK:
    PKV = [wvec(R[k]["text"], False) for k in PK]
    TKV = [wvec(T[h]["text"], True) for h in TK]
    KS = [[_cos(PKV[a], TKV[b]) for b in range(len(TK))] for a in range(len(PK))]
    KL = [[0.0] * (len(TK) + 1) for _ in range(len(PK) + 1)]
    for a in range(1, len(PK) + 1):
        for b in range(1, len(TK) + 1):
            s = KS[a - 1][b - 1] - 0.2
            KL[a][b] = max(KL[a - 1][b], KL[a][b - 1], (KL[a - 1][b - 1] + s) if s > 0 else -1)
    a, b, kp = len(PK), len(TK), []
    while a > 0 and b > 0:
        s = KS[a - 1][b - 1] - 0.2
        if s > 0 and abs(KL[a][b] - (KL[a - 1][b - 1] + s)) < 1e-9:
            kp.append((PK[a - 1], TK[b - 1]))
            a, b = a - 1, b - 1
        elif KL[a][b] == KL[a - 1][b]:
            a -= 1
        else:
            b -= 1
    merged_pairs, last_t = [], -1
    for rk, th in sorted(set(anchor_pairs) | set(kp)):
        if th > last_t and all(rk != q for q, _ in merged_pairs):
            merged_pairs.append((rk, th))
            last_t = th
    report.append(f"KATHĀ heading pairs: {len(kp)} (Pāli {len(PK)}, Thai {len(TK)})")
    anchor_pairs = merged_pairs
    KATHA_PAIRS = set(kp)
else:
    KATHA_PAIRS = set()
first_unit_item = [u[0] for u in units]
cuts = [(0, 0)]
rejected = 0
REJECTED_ANCHORS = []
for rk, th in anchor_pairs:
    bcut = bisect.bisect_left(blocks, rk)
    ucut = bisect.bisect_left(first_unit_item, th)
    du, db = ucut - cuts[-1][0], bcut - cuts[-1][1]
    # the section before the anchor must stay in proportion: a similar-looking heading far
    # away (e.g. a matrix heading paired with the niddesa heading) would strand a whole part
    structural = (rk, th) in KATHA_PAIRS or num_sim(R[rk]["text"], T[th]["text"]) >= 0.75
    ok = du >= 0 and db >= 0 and (structural or max(du, db) <= 5 or (min(du, db) > 0 and 1 / 5 <= du / db <= 5))
    if ok:
        cuts.append((ucut, bcut))
    else:
        rejected += 1
        REJECTED_ANCHORS.append((rk, th))
report.append(f"ANCHOR headings rejected as out of proportion: {rejected}")
if len(sys.argv) > 6 and sys.argv[6].startswith("anchors:"):
    pref = sys.argv[6].split(":", 1)[1]
    for rk, th in anchor_pairs:
        if R[rk]["id"].startswith(pref):
            print("ANCHOR", R[rk]["id"], R[rk]["text"][:24], "<->", th, T[th]["text"][:20], "REJECTED" if (rk, th) in REJECTED_ANCHORS else "")
anchor_pairs = [p for p in anchor_pairs if p not in REJECTED_ANCHORS]
cuts.append((nU, nB))
report.append(f"ANCHOR headings (unique names, similarity >= 0.5): {len(anchor_pairs)} -> {len(cuts) - 1} sections")
moves = []
for (u0, b0), (u1, b1) in zip(cuts, cuts[1:]):
    moves.extend(dp_section(u0, u1, b0, b1))
cnt = Counter((a, b) for _, a, _, b in moves)
report.append("MOVES " + ", ".join(f"{a}:{b}={n}" for (a, b), n in sorted(cnt.items())))


# ------------------------------------------------------------ split one unit over several blocks
def split_unit(items, bl):
    """Monotone partition of a unit's paragraphs over blocks bl (root indexes)."""
    k, L = len(bl), len(items)
    iv = [wvec(T[x]["text"], True) for x in items]
    bvv = [wvec(R[b]["text"], False) for b in bl]
    bn = [math.sqrt(dot(v, v)) or 1.0 for v in bvv]
    best_s = {(0, 0): (0.0, None)}
    for a in range(1, k + 1):
        for e in range(0, L + 1):
            cand = None
            acc, n2, d = {}, 0.0, 0.0
            if (a - 1, e) in best_s:
                cand = (best_s[(a - 1, e)][0] - 0.3, e)
            for s in range(e - 1, -1, -1):
                for g, w in iv[s].items():
                    old = acc.get(g, 0.0)
                    acc[g] = old + w
                    n2 += 2 * old * w + w * w
                    d += w * bvv[a - 1].get(g, 0.0)
                if (a - 1, s) not in best_s:
                    continue
                v = best_s[(a - 1, s)][0] + d / (bn[a - 1] * (math.sqrt(n2) or 1.0))
                if cand is None or v > cand[0]:
                    cand = (v, s)
            if cand:
                best_s[(a, e)] = cand
    out, e = [], L
    for a in range(k, 0, -1):
        s = best_s[(a, e)][1]
        out.append(items[s:e])
        e = s
    return list(reversed(out))


unit_block = {}  # unit index -> block index (first block it went to), for heading gaps
last_block = None
pending_units = []
for ui, a, bj, b in moves:
    if b == -1:  # empty section: carry forward to the next block
        pending_units.extend(ui + x for x in range(a))
        continue
    if b == 0:  # Thai unit with no root block: attach to the previous block (or the next)
        for x in range(a):
            if last_block is not None:
                mapping[R[last_block]["id"]]["items"].extend(units[ui + x])
                unit_block[ui + x] = last_block
            else:
                pending_units.append(ui + x)
        continue
    bl = [blocks[bj + y] for y in range(b)]
    if pending_units:  # text carried forward goes to the first block reached
        mapping[R[bl[0]]["id"]]["items"].extend(x for p in pending_units for x in units[p])
        for p in pending_units:
            unit_block[p] = bl[0]
        pending_units = []
    if a == 0:
        continue  # root block with no Thai: merged (stacked) by the renderer
    if b == 1:
        items = [x for y in range(a) for x in units[ui + y]]
        if pending_units:
            items = [x for p in pending_units for x in units[p]] + items
            for p in pending_units:
                unit_block[p] = bl[0]
            pending_units = []
        mapping[R[bl[0]]["id"]]["items"].extend(items)
        for y in range(a):
            unit_block[ui + y] = bl[0]
    else:
        parts = split_unit(units[ui], bl)
        for blk, part in zip(bl, parts):
            mapping[R[blk]["id"]]["items"].extend(part)
        unit_block[ui] = bl[0]
    last_block = bl[-1]

# ------------------------------------------------------------ headings in gaps
# Thai heading h lies before unit u(h). Its gap is (block of the unit before, block of u(h)).
first_item_unit = {}
for ui, u in enumerate(units):
    for x in u:
        first_item_unit.setdefault(x, ui)
item_unit = {x: ui for ui, u in enumerate(units) for x in u}
# nearest unit before / after each Thai item (one pass each way)
PREV_U, NEXT_U = [None] * len(T), [None] * len(T)
cur_u = None
for x in range(len(T)):
    PREV_U[x] = cur_u
    if x in item_unit:
        cur_u = item_unit[x]
cur_u = None
for x in range(len(T) - 1, -1, -1):
    NEXT_U[x] = cur_u
    if x in item_unit:
        cur_u = item_unit[x]
th_gap = {h: (unit_block.get(PREV_U[h]), unit_block.get(NEXT_U[h])) for h in unit_heads}
# nearest root text block before / after each root index
PREV_B, NEXT_B = [None] * len(R), [None] * len(R)
cur_b = None
for k in range(len(R)):
    PREV_B[k] = cur_b
    if R[k]["kind"] == "t" and k >= root_body:
        cur_b = k
cur_b = None
for k in range(len(R) - 1, -1, -1):
    NEXT_B[k] = cur_b
    if R[k]["kind"] == "t" and k >= root_body:
        cur_b = k
rk_of = {k: idx for idx, k in enumerate(blocks)}
paired = 0
used_t = set()
for rk, th in anchor_pairs:
    mapping[R[rk]["id"]]["heading"] = th
    used_t.add(th)
    paired += 1
root_heads = [k for k in range(root_body, len(R)) if R[k]["kind"] == "h"]
HV = {k: wvec(R[k]["text"], False) for k in root_heads}
TV = {h: wvec(T[h]["text"], True) for h in unit_heads}


def cosv(a, b):
    na, nb = math.sqrt(dot(a, a)) or 1.0, math.sqrt(dot(b, b)) or 1.0
    return dot(a, b) / (na * nb)


# pair root headings with Thai headings in order, each within 2 blocks of where the text
# alignment puts it; the best-matching candidate above a similarity floor wins
last_used = -1
uh_sorted = sorted(unit_heads)
uh_tn = [rk_of[th_gap[h][1]] if th_gap[h][1] is not None else len(blocks) for h in uh_sorted]
p0 = 0
for ri, rh in enumerate(root_heads):
    if mapping[R[rh]["id"]]["heading"] is not None:  # anchor heading, already paired
        last_used = mapping[R[rh]["id"]]["heading"]
        continue
    prev_b = PREV_B[rh]
    next_b = NEXT_B[rh]
    rp = rk_of[prev_b] if prev_b is not None else -1
    rn = rk_of[next_b] if next_b is not None else len(blocks)
    while p0 < len(uh_sorted) and uh_tn[p0] < rn - 2 and uh_sorted[p0] <= last_used:
        p0 += 1
    cands = []
    for h in uh_sorted[p0:]:
        if h in used_t or h <= last_used:
            continue
        pb, nb_ = th_gap[h]
        tp = rk_of[pb] if pb is not None else -1
        tn = rk_of[nb_] if nb_ is not None else len(blocks)
        if tn < rn - 2:
            continue
        if tp > rp + 2:
            break  # Thai headings are in order: the rest lie further on
        cands.append((max(cosv(HV[rh], TV[h]), num_sim(R[rh]["text"], T[h]["text"])), h))
    if len(sys.argv) > 6 and sys.argv[6] == "debugheads" and paired + 1 < 30:
        print("DBG", R[rh]["id"], R[rh]["text"][:20], "gap", rp, rn, "cands",
              [(round(s_, 2), T[h_]["text"][:15], th_gap[h_] and (rk_of.get(th_gap[h_][0]), rk_of.get(th_gap[h_][1]))) for s_, h_ in cands[:5]])
    if cands:
        s, h = max(cands)
        # if a later root heading in the same gap matches this Thai heading better, leave it to that one
        same_gap = []
        for r2 in root_heads[ri + 1:]:
            if NEXT_B[r2] != next_b:
                break
            same_gap.append(r2)
        if any(max(cosv(HV[r2], TV[h]), num_sim(R[r2]["text"], T[h]["text"])) > s for r2 in same_gap):
            continue
        if s > 0.15:
            mapping[R[rh]["id"]]["heading"] = h
            used_t.add(h)
            last_used = h
            paired += 1
# unpaired Thai headings: bold line at the start of the next unit's block
extra = 0
def _is_continuation(text):
    """second line of a two-column matrix row: starts with Thai-script Pāli, no number"""
    toks = text.split()
    numbered = re.match(r"^(\[[๐-๙]+\]|[๐-๙]+(-[๐-๙]+)?\.)", text)
    return bool(toks) and not numbered and ("ฺ" in toks[0] or toks[0].endswith("ํ"))


for h in unit_heads:
    if h in used_t:
        continue
    if _is_continuation(T[h]["text"]):
        # belongs with the text before it
        prv = PREV_U[h]
        blk = unit_block.get(prv) if prv is not None else blocks[0]
        mapping[R[blk]["id"]]["items"].append(h)
        extra += 1
        continue
    nxt = NEXT_U[h]
    blk = unit_block.get(nxt) if nxt is not None else last_block
    if blk is None:
        blk = blocks[0]
    mapping[R[blk]["id"]]["items"].append(h)
    extra += 1
report.append(f"HEADINGS root {len(root_heads)}, Thai {len(unit_heads)}, paired {paired}, Thai-only kept as bold lines {extra}")

# ------------------------------------------------------------ numbered-group repair
PI_NUM = {"eka": 1, "duvi": 2, "tivi": 3, "catubbi": 4, "pañcavi": 5, "chabbi": 6, "sattavi": 7,
          "aṭṭhavi": 8, "navavi": 9, "dasavi": 10, "ekādasavi": 11}


def group_no_pi(text):
    low = text.lower()
    nums = set()
    for w in re.findall(r"(\w+?)(?:v|bb)idhena", low):
        for key, v in PI_NUM.items():
            if (w + "vi").startswith(key) or (w + "bbi").startswith(key):
                nums.add(v)
                break
    if len(nums) != 1:
        return None
    return next(iter(nums))


rpos = {b["id"]: k for k, b in enumerate(R)}
moved = 0
for bid in [R[k]["id"] for k in blocks]:
    for x in [x for x in mapping[bid]["items"] if re.search(r"หมวดละ\s*[๐-๙]+", T[x]["text"][:45])]:
        if x not in mapping[bid]["items"]:
            continue
        n_th = int(re.search(r"หมวดละ\s*([๐-๙]+)", T[x]["text"][:45]).group(1).translate(TD))
        k0 = rpos[bid]
        g0 = group_no_pi(R[k0]["text"])
        if g0 is None or g0 == n_th:
            continue
        cands = [R[k]["id"] for k in range(max(0, k0 - 15), min(len(R), k0 + 16)) if R[k]["kind"] == "t" and group_no_pi(R[k]["text"]) == n_th]
        if not cands:
            continue
        target = min(cands, key=lambda c: abs(rpos[c] - k0))
        cur = sorted(mapping[bid]["items"])
        st = cur.index(x)
        en = next((y for y in range(st + 1, len(cur)) if re.search(r"หมวดละ\s*[๐-๙]+", T[cur[y]]["text"][:45])), len(cur))
        chunk = cur[st:en]
        mapping[bid]["items"] = cur[:st] + cur[en:]
        mapping[target]["items"] = sorted(mapping[target]["items"] + chunk)
        moved += 1
report.append(f"GROUP repair: {moved} moved")

# ------------------------------------------------------------ checks
for v in mapping.values():
    v["items"] = sorted(set(v["items"]))
merged = [R[k]["id"] for k in blocks if not mapping[R[k]["id"]]["items"]]
report.append(f"ROOT text blocks with no Thai text of their own (MERGE): {len(merged)}")
report.append("  " + " ".join("^" + x for x in merged))
par_of, cur = {}, None
for k, it in enumerate(T):
    m = re.match(r"\[([๐-๙]+)\]", it["text"])
    if m:
        cur = int(m.group(1).translate(TD))
    par_of[k] = cur
seq = []
for k in blocks:
    m = re.fullmatch(rf"{BOOK}-(\d+)", R[k]["id"])
    ns = [par_of[x] for x in mapping[R[k]["id"]]["items"] if re.match(r"\[[๐-๙]+\]", T[x]["text"])]
    if m and ns:
        seq.append((int(m.group(1)), min(ns), R[k]["id"]))
back_ = [(a, c) for a, c in zip(seq, seq[1:]) if c[1] < a[1]]
report.append(f"NON-MONOTONIC numbered paragraphs: {len(back_)}")
placed = set()
for v in mapping.values():
    placed.update(v["items"])
    if v["heading"] is not None:
        placed.add(v["heading"])
lost = [k for k, it in enumerate(T) if k not in placed and it["kind"] != "hr"]
report.append(f"Thai items not assigned anywhere: {len(lost)} {lost[:20]}")
unh = [b["id"] for b in R if b["kind"] == "h" and mapping[b["id"]]["heading"] is None and b["id"] != "0"]
report.append(f"ROOT headings with no Thai heading: {len(unh)}")
# low-confidence blocks for human review: the Thai text placed on a block shares little with
# it while a neighbouring block would share more (a likely shift of one or two blocks)
flags = []
bpos = {k: n for n, k in enumerate(blocks)}
for n, k in enumerate(blocks):
    items = [x for x in mapping[R[k]["id"]]["items"] if T[x]["kind"] != "h"]
    if not items:
        continue
    tv = Counter()
    for x in items:
        tv.update(wvec(T[x]["text"], True))
    tv = dict(tv)
    here = _cos(BV[n], tv)
    near = max((_cos(BV[m], tv) for m in (n - 2, n - 1, n + 1, n + 2) if 0 <= m < len(blocks)), default=0.0)
    if near > here + 0.2:
        flags.append(R[k]["id"])
report.append(f"CHECK (Thai text fits a neighbouring block better; review): {len(flags)}")
report.append("  " + " ".join("^" + x for x in flags))
json.dump({"mapping": mapping, "heading_extra": [], "check": flags}, open(out_json, "w", encoding="utf-8"), ensure_ascii=False)
open(out_report, "w", encoding="utf-8").write("\n".join(report) + "\n")
print("\n".join(r if len(r) < 300 else r[:300] + " …" for r in report))
