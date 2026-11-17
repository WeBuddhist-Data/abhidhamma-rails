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


DOUBLE = re.compile(r"(.)\1+")


def skel_th(s):
    # "รร" is the Thai spelling of Pāli -amm- / -agg- (ธรรม dhamma, กรรม kamma, วรรค vagga)
    s = s.replace("รร", "")
    k = "".join(TH[ch] for i, ch in enumerate(s) if ch in TH and not (i + 1 < len(s) and s[i + 1] == "์"))
    return DOUBLE.sub(r"\1", k)  # Thai writes Pāli double consonants once (จิต citta)


def skel_pi(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    out = []
    for ch in s:
        if ch in PI:
            if ch == "h" and out and out[-1] in "kctp":
                continue
            out.append(PI[ch])
    return DOUBLE.sub(r"\1", "".join(out))


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
SECTION_SUFFIX = re.compile(r"(มาติกา|นิทเทส|วาร|ภาชนีย์|วิภังค์|ปกรณ์|กถา|ปุจฉกะ|นัย|ทุกะ|ติกะ|จำพวก\)|จบ|วิสัชชนา|วิสัชนา|ปุจฉา)\s*$")


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


# Question counts: a strong structural cue. Vibhaṅga / Dhammasaṅgaṇī / Dhātukathā /
# Puggalapaññatti: Pāli "katamā …?" <-> Thai "… เป็นไฉน"; Yamaka: Pāli "?" <-> Thai "หรือ".
def q_pi(text):
    if BOOK in ("1", "2", "3", "4"):
        return len(re.findall(r"\bkatam", text.lower()))
    if BOOK == "6":
        return text.count("?")
    if BOOK == "7":  # Paṭṭhāna: negated conditions (nahetuyā, naārammaṇe) <-> Thai ที่ไม่ใช่
        return 1 if re.search(r"\bna(?!va\b|vahi|vasu)(?=[a-zāīūṭḍṇñṅ])", text.lower()) else 0
    return 0


def q_th(text):
    if BOOK in ("1", "2", "3", "4"):
        return text.count("ไฉน")
    if BOOK == "6":
        return text.count("หรือ")
    if BOOK == "7":
        return 1 if "ไม่ใช่" in text else 0
    return 0


QU = [sum(q_th(T[k]["text"]) for k in u) for u in units]
QB = [q_pi(R[k]["text"]) for k in blocks]
QU_C = [0]
for v in QU:
    QU_C.append(QU_C[-1] + v)
QB_C = [0]
for v in QB:
    QB_C.append(QB_C[-1] + v)
QW = 0.25 if BOOK in ("1", "2", "3", "4", "6") else 0.15 if BOOK == "7" else 0.0

# Paṭṭhāna, second cue: count sections (Saṅkhyāvāra: "Hetuyā tīṇi, ārammaṇe satta …") <->
# Thai count lines ("ในเหตุปัจจัย มีวาระ ๓", "มี " ๓")
NUMWORDS = re.compile(r"\b(ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa)\b")


def c_pi(text):
    return 1 if len(NUMWORDS.findall(text.lower())) >= 2 else 0


def c_th(text):
    return 1 if ("มีวาระ" in text or 'มี "' in text) else 0


CW = 0.15 if BOOK == "7" else 0.0
CU_C = [0]
CB_C = [0]
if CW:
    for u in units:
        CU_C.append(CU_C[-1] + c_th(" ".join(T[k]["text"] for k in u)))
    for k in blocks:
        CB_C.append(CB_C[-1] + c_pi(R[k]["text"]))


def score(i, a, j, b):
    """cosine between units i..i+a-1 and blocks j..j+b-1, plus the question-count cue"""
    num = sum(ub(i + x, j + y) for x in range(a) for y in range(b))
    s = num / (range_norm(UU, i, a) * range_norm(BB, j, b))
    if QW:
        qa, qb = QU_C[i + a] - QU_C[i], QB_C[j + b] - QB_C[j]
        if qa or qb:
            s += QW if qa == qb else -QW * min(1.0, abs(qa - qb) / max(qa, qb))
    if CW:
        ca, cb = CU_C[i + a] - CU_C[i], CB_C[j + b] - CB_C[j]
        if ca or cb:
            s += CW if (ca > 0) == (cb > 0) else -CW
    return s


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


# Thai heading candidates: section names only. Count lines ("ในอวิคตปัจจัย มี " ๙"), instructions
# ("พึงนับ…", "…เหมือนกับ…"), elisions and end lines ("… จบ") are not section names.
NOT_NAME = re.compile(r'"|\sมี\s|^ใน|^พึง|ผู้มีปัญญา|เหมือน|ฯลฯ|จบ(บริบูรณ์)?\.?\s*$|^บท|^หัวข้อ')
UT = []
for pos_, h in enumerate(unit_heads):
    t = T[h]["text"].strip()
    if len(t) > 60 or NOT_NAME.search(t):
        continue
    # the same name printed again right before another heading closes its section: an end line
    nxt = h + 1 if h + 1 < len(T) else None
    if nxt is not None and T[nxt]["kind"] == "h" and any(
            _norm_h(T[q]["text"]) == _norm_h(t) for q in unit_heads[max(0, pos_ - 40):pos_]):
        continue
    UT.append(h)
UNIQ_T = {h for h in UT if tcn[_norm_h(T[h]["text"])] == 1}
URV = [wvec(R[k]["text"], False) for k in UR]
UTV = [wvec(T[h]["text"], True) for h in UT]
na_, nb_ = len(UR), len(UT)

# position in the text (share of characters before the heading) on each side
_rc, _acc = [0] * len(R), 0
for k, b in enumerate(R):
    _rc[k] = _acc
    if b["kind"] == "t":
        _acc += len(b["text"])
R_TOT = max(_acc, 1)
_tc, _acc = [0] * len(T), 0
for k, it in enumerate(T):
    _tc[k] = _acc
    if it["kind"] != "h":
        _acc += len(it["text"])
T_TOT = max(_acc, 1)
RF = [_rc[k] / R_TOT for k in UR]
TF = [_tc[h] / T_TOT for h in UT]
BANDF = 0.12


def _head_skel(x, y):
    ps = re.sub(r"^[\d\-\.\s()*]+|[*]|^\((ka|kha|ga|gha|ṅa)\)\s*", "", R[UR[x]]["text"].strip(), flags=re.I)
    ts = re.sub(r"^[๐-๙,\.\s]+|^\[|\]$", "", T[UT[y]]["text"].strip())
    # a vowel-initial name (Akusala-, Abhidhamma-, Uddeso, Ekaka-) is written with อ in Thai
    p = ("@" if ps[:1].lower() in "aāiīuūeo" else "") + skel_pi(ps)
    t = ("@" if ts.lstrip("เแโใไ")[:1] == "อ" else "") + skel_th(ts)
    return p, t


def SCf(x, y):
    s = _cos(URV[x], UTV[y])
    # Abhidhamma section names differ in their first element (Kāyānupassanā- / Cittānupassanā-,
    # Kusala- / Akusala-): names that start differently are a weak match
    p, t = _head_skel(x, y)
    if p[:2] != t[:2]:
        s *= 0.75
    # one name much longer than the other ("Kusalā dhammā" vs "กุศลธรรมนิทเทส"): a weak match
    if max(len(p), len(t)) > 1.4 * max(1, min(len(p), len(t))):
        s *= 0.8
    s = max(s, num_sim(R[UR[x]]["text"], T[UT[y]]["text"]))
    s += 0.1 if (UR[x] in UNIQ_R and UT[y] in UNIQ_T) else 0.0
    return s - 1.0 * abs(RF[x] - TF[y])  # small cost for distance from the expected position


# candidate pairs: within the band, sharing a trigram (or a number-word match)
inv = {}
for y, v in enumerate(UTV):
    for g in v:
        inv.setdefault(g, []).append(y)
points = []  # (x, y, score)
for x in range(na_):
    # a very short name ("Tikaṃ", "Dukaṃ": skeleton "tk") cannot tell ติก- from ทุก-: no anchor
    if len(skel_pi(re.sub(r"[\d\-\.\s()*]|ṃ$", "", R[UR[x]]["text"].strip("* ")))) < 4:
        continue
    lo = bisect.bisect_left(TF, RF[x] - BANDF)
    hi = bisect.bisect_right(TF, RF[x] + BANDF)
    cand = set()
    for g in URV[x]:
        for y in inv.get(g, ()):
            if lo <= y < hi:
                cand.add(y)
    if num_sim(R[UR[x]]["text"], "เอกก") or re.search(r"(uddes|niddes|vaggo)", R[UR[x]]["text"].lower()):
        cand.update(range(lo, hi))
    for y in cand:
        s = SCf(x, y) - 0.55
        if s > 0:
            points.append((x, y, s))
# heaviest chain increasing in both x and y (Fenwick tree over y for the prefix maximum)
FT = [(0.0, -1)] * (nb_ + 1)


def ft_query(i):  # max over y' < i
    best = (0.0, -1)
    while i > 0:
        if FT[i][0] > best[0]:
            best = FT[i]
        i -= i & -i
    return best


def ft_update(i, val):
    i += 1
    while i <= nb_:
        if val[0] > FT[i][0]:
            FT[i] = val
        i += i & -i


points.sort()
prev_pt, val_pt = [-1] * len(points), [0.0] * len(points)
k = 0
while k < len(points):
    k2 = k
    while k2 < len(points) and points[k2][0] == points[k][0]:
        k2 += 1
    row = []
    for p in range(k, k2):
        x, y, s = points[p]
        bv, bp = ft_query(y)
        val_pt[p], prev_pt[p] = bv + s, bp
        row.append(p)
    for p in row:  # update after the whole row: one Thai heading per root heading
        ft_update(points[p][1], (val_pt[p], p))
    k = k2
best_end = max(range(len(points)), key=lambda p: val_pt[p]) if points else -1
anchor_pairs = []
p = best_end
while p != -1:
    anchor_pairs.append((UR[points[p][0]], UT[points[p][1]]))
    p = prev_pt[p]
anchor_pairs.reverse()
ANCHOR_SIM = {(UR[x], UT[y]): s + 0.55 for x, y, s in points}
report.append(f"ANCHOR candidates: root headings {na_}, Thai section-name headings {nb_}, candidate pairs {len(points)}, chain {len(anchor_pairs)}")

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
    # a strong name match (e.g. a tika/duka name) holds even where the Thai omits whole sections
    structural = (rk, th) in KATHA_PAIRS or num_sim(R[rk]["text"], T[th]["text"]) >= 0.75 or \
        ANCHOR_SIM.get((rk, th), 0.0) >= 0.75
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
    # question lines first: when each block holds one question and the Thai has as many
    # question lines, cut at them (text before the first question goes with the first block)
    qb_ = [q_pi(R[b]["text"]) for b in bl]
    if QW and BOOK != "7" and all(q >= 1 for q in qb_):
        qi = [x for x in range(L) if q_th(T[items[x]]["text"]) >= 1]
        if len(qi) == sum(qb_) and all(q_th(T[items[x]]["text"]) == 1 for x in qi):
            # block y starts at its first question line (Yamaka: Ka and Kha, two per block)
            starts, acc = [], 0
            for q in qb_:
                starts.append(qi[acc])
                acc += q
            cuts_ = [0] + starts[1:] + [L]
            return [items[cuts_[y]:cuts_[y + 1]] for y in range(k)]
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


def pref_sim(rh, h):
    """'Dukaṃ' <-> 'ทุกมาติกาวิสัชชนา': the root name opens the Thai name."""
    p = skel_pi(re.sub(r"^[\d\-\.\s()*]+|[*]", "", R[rh]["text"]))
    t = skel_th(re.sub(r"^[๐-๙\.\s]+", "", T[h]["text"]))
    if p.endswith("m"):
        p = p[:-1]  # -aṃ ending
    return 0.6 if len(p) >= 3 and len(p) >= 0.2 * len(t) and t.startswith(p) else 0.0


# pair root headings with Thai headings in order, each within 2 blocks of where the text
# alignment puts it; the best-matching candidate above a similarity floor wins
last_used = -1
uh_sorted = sorted(unit_heads)
uh_tn = [rk_of[th_gap[h][1]] if th_gap[h][1] is not None else len(blocks) for h in uh_sorted]
p0 = 0
# the Thai heading of the next anchored root heading: a secondary pair must lie before it
next_anchor_t = {}
_nt = len(T)
for rh in reversed(root_heads):
    next_anchor_t[rh] = _nt
    if mapping[R[rh]["id"]]["heading"] is not None:
        _nt = mapping[R[rh]["id"]]["heading"]
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
        if h >= next_anchor_t[rh]:
            break
        if h in used_t or h <= last_used or NOT_NAME.search(T[h]["text"].strip()):
            continue
        pb, nb_ = th_gap[h]
        tp = rk_of[pb] if pb is not None else -1
        tn = rk_of[nb_] if nb_ is not None else len(blocks)
        if tn < rn - 2:
            continue
        if tp > rp + 2:
            break  # Thai headings are in order: the rest lie further on
        cands.append((max(cosv(HV[rh], TV[h]), num_sim(R[rh]["text"], T[h]["text"]), pref_sim(rh, h)), h))
    if len(sys.argv) > 6 and sys.argv[6] == "debugheads" and paired + 1 < 30:
        print("DBG", R[rh]["id"], R[rh]["text"][:20], "gap", rp, rn, "cands",
              [(round(s_, 2), T[h_]["text"][:15], th_gap[h_] and (rk_of.get(th_gap[h_][0]), rk_of.get(th_gap[h_][1]))) for s_, h_ in cands[:5]])
    if len(sys.argv) > 6 and sys.argv[6] == "debugid:" + R[rh]["id"]:
        print("DEBUG", R[rh]["id"], "gap", rp, rn, "last_used", last_used, "next_anchor_t", next_anchor_t[rh], "p0", p0,
              "cands", [(round(s_, 2), h_, T[h_]["text"][:20]) for s_, h_ in cands])
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
        if s > 0.3:
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
