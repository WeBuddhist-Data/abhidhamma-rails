"""Align the Thai Dhammasangani draft to the pi-1 root blocks.

Output: a JSON mapping (root block id -> list of Thai item indexes, plus the Thai heading
used for root headings) and a match-list report for human review.

Method
1. Matrix (Matika): one Thai unit per numbered triad/dyad heading, in order -> ^1-M1-*, ^1-M2-*.
2. Body: anchor alignment on questions (Pali blocks containing '?', Thai paragraphs
   containing 'เป็นไฉน'), by dynamic programming over a Pali/Thai consonant-skeleton
   similarity; then, between consecutive anchors, headings are paired in order and the
   remaining paragraphs are distributed over the root blocks by the same similarity.
"""
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

root_path, th_path, out_json, out_report = sys.argv[1:5]
R = parse_root(root_path)
T = parse_draft(th_path)

# ------------------------------------------------------------ skeletons
TH = {}
for chars, v in (("กขฃคฅฆ", "k"), ("จฉชฌ", "c"), ("ซศษส", "s"), ("ฎฏฐฑฒดตถทธ", "t"),
                 ("งญณนํ", "n"), ("บปผฝพฟภ", "p"), ("ม", "m"), ("ย", "y"), ("รฤ", "r"),
                 ("ลฦฬ", "l"), ("ว", "v"), ("หฮ", "h")):
    for ch in chars:
        TH[ch] = v


def skel_th(s):
    out = []
    for i, ch in enumerate(s):
        if ch in TH:
            if i + 1 < len(s) and s[i + 1] == "์":  # silent consonant (thanthakhat)
                continue
            out.append(TH[ch])
    return "".join(out)


PI = {"k": "k", "g": "k", "c": "c", "j": "c", "t": "t", "d": "t", "n": "n", "p": "p", "b": "p",
      "m": "m", "y": "y", "r": "r", "l": "l", "v": "v", "s": "s", "h": "h"}


def skel_pi(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    out = []
    for ch in s:
        if ch in PI:
            if ch == "h" and out and out[-1] != "h" and s and False:
                pass
            out.append(PI[ch])
    # aspiration: drop h directly after a consonant (kh, gh, th, dh, ph, bh, ch, jh)
    res = []
    for ch in out:
        if ch == "h" and res and res[-1] in "kctp":
            continue
        res.append(ch)
    return "".join(res)


def grams(sk, n=3):
    return Counter(sk[i:i + n] for i in range(len(sk) - n + 1))


# ------------------------------------------------------------ regions
BOOK = sys.argv[5] if len(sys.argv) > 5 else "1"
title_idx = 0 if T[0]["kind"] == "h" else None
homage_idx = next((k for k, it in enumerate(T) if it["text"].startswith("ขอนอบน้อม")),
                  next(k for k, it in enumerate(T) if it["kind"] == "p"))
if BOOK == "1":
    # Dhammasangani: the Matika (matrix) comes first and is aligned by its numbered headings
    last_matrix_table = max(k for k, it in enumerate(T[:next(k for k, it in enumerate(T) if it["kind"] == "p" and "[๑๖]" in it["text"])]) if it["kind"] == "table")
    first_body = next(k for k in range(last_matrix_table + 1, len(T)) if T[k]["kind"] == "h")
    root_m_start = next(k for k, b in enumerate(R) if b["id"] == "1-M-0")
    root_body = next(k for k, b in enumerate(R) if b["id"] == "1-1-0")
else:
    # other books: everything after the title and homage is body
    first_body = homage_idx + 1
    root_body = next(k for k, b in enumerate(R) if b["id"] == f"{BOOK}-0") + 1
    root_m_start = root_body

mapping = {b["id"]: {"items": [], "heading": None, "note": ""} for b in R}
report = []

# ------------------------------------------------------------ front: homage + title
mapping["T-1"]["items"] = [homage_idx]
mapping[f"{BOOK}-0"]["heading"] = title_idx
report.append(f"FRONT  ^T-1 homage -> Thai homage paragraph;  ^0 + ^{BOOK}-0 -> Thai title lines (split by the renderer)")

# ------------------------------------------------------------ matrix
UNIT_H = re.compile(r"^(\[[๐-๙]+\] )?[๐-๙]+(-[๐-๙]+)?\. ")
m_units = []
cur = None
div_headings = []
pending_extra = []
after_div = {}  # index in div_headings -> Thai-only lines printed right after that heading
for k in range(homage_idx + 1, first_body):
    it = T[k]
    if it["kind"] == "h" and UNIT_H.match(it["text"]):
        cur = pending_extra + [k]
        pending_extra = []
        m_units.append(cur)
    elif it["kind"] == "h":
        if re.match(r"^\*?หมวดที่|^อภิธรรมมาติกา", it["text"]):
            # Thai-only lines ("group N has k dyads", "Abhidhamma matrix of 100 dyads"):
            # kept as text at the start of the next unit
            pending_extra.append(k)
            cur = None
        elif cur is not None and not re.search(r"(ติกะ|ทุกะ|มาติกา|โคจฉกะ)", it["text"]):
            cur.append(k)  # wrapped heading fragment inside a unit
        else:
            # Thai-only lines that came before this division heading stay before it:
            # they follow the previous division heading in the output
            if pending_extra:
                after_div[len(div_headings) - 1] = pending_extra
                pending_extra = []
            div_headings.append(k)
            cur = None
        continue
    elif it["kind"] == "hr":
        continue
    else:
        if cur is None:
            # end markers ("... จบ") after a unit belong to the previous unit
            if m_units:
                m_units[-1].append(k)
        else:
            cur.append(k)
root_m_text = [b for b in R[root_m_start:root_body] if b["kind"] == "t"]
root_m_head = [b for b in R[root_m_start:root_body] if b["kind"] == "h"]
report.append(f"MATRIX units: Thai {len(m_units)} vs root {len(root_m_text)};  division headings: Thai {len(div_headings)} vs root {len(root_m_head)}")
for b, u in zip(root_m_text, m_units):
    mapping[b["id"]]["items"] = u
if len(m_units) != len(root_m_text):
    report.append("  !! matrix count mismatch: check the tail of the matrix")
# division headings by order
for n_div, (b, k) in enumerate(zip(root_m_head, div_headings)):
    mapping[b["id"]]["heading"] = k
    if n_div in after_div:
        mapping[b["id"]]["after"] = after_div[n_div]
for b in root_m_head[len(div_headings):]:
    report.append(f"  UNMATCHED heading ^{b['id']} {b['text']}")
for k in div_headings[len(root_m_head):]:
    report.append(f"  EXTRA Thai heading item {k}: {T[k]['text'][:30]}")

# ------------------------------------------------------------ body anchors
rb = R[root_body:]
tb = list(range(first_body, len(T)))
# a question block: has '?', or opens with an interrogative ("Katamā … hoti…pe…" drops the '?')
P_anchor = [k for k, b in enumerate(rb) if b["kind"] == "t" and ("?" in b["text"] or re.search(r"\b(Katam|katam|Kathaṃ)", b["text"][:40]))]
T_anchor = [k for k in tb if T[k]["kind"] in ("p", "li") and "เป็นไฉน" in T[k]["text"]]


def unit_text_root(ai):
    i = P_anchor[ai]
    j = P_anchor[ai + 1] if ai + 1 < len(P_anchor) else len(rb)
    return " ".join(b["text"] for b in rb[i:j] if b["kind"] == "t")


def unit_text_th(ai):
    i = T_anchor[ai]
    j = T_anchor[ai + 1] if ai + 1 < len(T_anchor) else len(T)
    return " ".join(T[k]["text"] for k in range(i, j) if T[k]["kind"] in ("p", "li", "table"))


Pg = [grams(skel_pi(unit_text_root(a))) for a in range(len(P_anchor))]
Tg = [grams(skel_th(unit_text_th(a))) for a in range(len(T_anchor))]
df = Counter()
for g in Pg:
    df.update(g.keys())
N = len(Pg)
idf = {g: math.log((N + 1) / (c + 1)) + 1 for g, c in df.items()}


def vec(c):
    v = {g: n * idf.get(g, 0.0) for g, n in c.items() if g in idf}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return v, norm


PV = [vec(g) for g in Pg]
TV = [vec(g) for g in Tg]


def q_root(ai):
    t = rb[P_anchor[ai]]["text"]
    return re.split(r"\?|…pe…", t)[0]


def q_th(ai):
    t = T[T_anchor[ai]]["text"]
    return t.split("เป็นไฉน")[0]


# similarity of the question subjects alone (e.g. sīlabbataparāmāso / สีลัพพตปรามาส)
PQ = [vec(grams(skel_pi(q_root(a)))) for a in range(len(P_anchor))]
TQ = [vec(grams(skel_th(q_th(a)))) for a in range(len(T_anchor))]


def cos(A, B):
    (a, na), (b, nb) = A, B
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(g, 0.0) for g, x in a.items()) / (na * nb)


def sim(i, j):
    return 0.4 * cos(PV[i], TV[j]) + 0.6 * cos(PQ[i], TQ[j])


n, m = len(P_anchor), len(T_anchor)
BAND, GAP = 120, 0.25
NEG = -1e9
S = {}
back = {}
S[(0, 0)] = 0.0
for i in range(0, n + 1):
    centre = int(i * m / max(n, 1))
    for j in range(max(0, centre - BAND), min(m, centre + BAND) + 1):
        if i == 0 and j == 0:
            continue
        best, arg = NEG, None
        if i > 0 and j > 0 and (i - 1, j - 1) in S:
            v = S[(i - 1, j - 1)] + sim(i - 1, j - 1) - 0.05
            if v > best:
                best, arg = v, "d"
        if i > 0 and (i - 1, j) in S:
            v = S[(i - 1, j)] - GAP
            if v > best:
                best, arg = v, "u"
        if j > 0 and (i, j - 1) in S:
            v = S[(i, j - 1)] - GAP
            if v > best:
                best, arg = v, "l"
        if arg:
            S[(i, j)], back[(i, j)] = best, arg
i, j = n, m
pairs = []
while i > 0 or j > 0:
    a = back[(i, j)]
    if a == "d":
        pairs.append((i - 1, j - 1))
        i, j = i - 1, j - 1
    elif a == "u":
        pairs.append((i - 1, None))
        i -= 1
    else:
        pairs.append((None, j - 1))
        j -= 1
pairs.reverse()
matched = [(p, t) for p, t in pairs if p is not None and t is not None]
sims = [sim(p, t) for p, t in matched]
report.append(f"BODY anchors: root {n}, Thai {m}, matched {len(matched)}, root-only {sum(1 for p, t in pairs if t is None)}, Thai-only {sum(1 for p, t in pairs if p is None)}")
report.append(f"  similarity of matched anchors: median {sorted(sims)[len(sims)//2]:.2f}, low (<0.15): {sum(1 for s in sims if s < 0.15)}")

# ------------------------------------------------------------ per-question anchors (books 2-7)
if BOOK != "1":
    # One root block may hold several questions while the Thai gives each question its own
    # paragraph, so align question by question and then use, for each root block, the Thai
    # paragraph matched to its first question as that block's anchor.
    pq = []  # (root body index, question text)
    for k, b in enumerate(rb):
        if b["kind"] != "t":
            continue
        t = b["text"]
        found = False
        for m in re.finditer(r"[^.?–;]*\?", t):
            pq.append((k, m.group(0)))
            found = True
        if not found and re.search(r"\b(Katam|katam|Kathaṃ)", t[:40]):
            pq.append((k, re.split(r"…pe…", t)[0]))
    tq = [(k, T[k]["text"]) for k in tb if T[k]["kind"] in ("p", "li") and ("เป็นไฉน" in T[k]["text"] or "?" in T[k]["text"])]
    PQv = [vec(grams(skel_pi(q))) for _, q in pq]
    TQv = [vec(grams(skel_th(q.split("เป็นไฉน")[0].split("?")[0]))) for _, q in tq]
    n2, m2 = len(pq), len(tq)
    QPEN, QGAP = 0.15, 0.10
    S2, B2 = {(0, 0): 0.0}, {}
    for i in range(0, n2 + 1):
        centre = int(i * m2 / max(n2, 1))
        for j in range(max(0, centre - BAND), min(m2, centre + BAND) + 1):
            if i == 0 and j == 0:
                continue
            best, arg = NEG, None
            # a weak match costs more than skipping a question on one side, so that questions
            # the Thai spells out (and the Pāli abbreviates) are skipped, not force-matched
            if i > 0 and j > 0 and (i - 1, j - 1) in S2:
                v = S2[(i - 1, j - 1)] + cos(PQv[i - 1], TQv[j - 1]) - QPEN
                if v > best:
                    best, arg = v, "d"
            if i > 0 and (i - 1, j) in S2:
                v = S2[(i - 1, j)] - QGAP
                if v > best:
                    best, arg = v, "u"
            if j > 0 and (i, j - 1) in S2:
                v = S2[(i, j - 1)] - QGAP
                if v > best:
                    best, arg = v, "l"
            if arg:
                S2[(i, j)], B2[(i, j)] = best, arg
    i, j, qpairs = n2, m2, []
    while i > 0 or j > 0:
        a = B2[(i, j)]
        if a == "d":
            qpairs.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif a == "u":
            i -= 1
        else:
            j -= 1
    qpairs.reverse()
    first = {}
    for qi, tj in qpairs:
        first.setdefault(pq[qi][0], tq[tj][0])
    # Consistency filter: the offset between a root block's number and the Thai paragraph
    # number [n] of its anchor follows a smooth local trend. An anchor far off that trend
    # (e.g. a question matched by wording to a similar question many blocks away, where the
    # two editions differ) is dropped; the text around it is then placed by distribution.
    _TD = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
    par_of, cur_n = {}, None
    for x, it in enumerate(T):
        mm = re.match(r"\[([๐-๙]+)\]", it["text"])
        if mm:
            cur_n = int(mm.group(1).translate(_TD))
        par_of[x] = cur_n
    keys = sorted(first)
    offs = []
    for k in keys:
        mnum = re.fullmatch(rf"{BOOK}-(\d+)", rb[k]["id"])
        n_th = par_of.get(first[k])
        offs.append((int(mnum.group(1)) - n_th) if (mnum and n_th is not None) else None)
    dropped = 0
    for idx, k in enumerate(keys):
        if offs[idx] is None:
            continue
        win = [o for o in offs[max(0, idx - 7):idx + 8] if o is not None]
        med = sorted(win)[len(win) // 2]
        if abs(offs[idx] - med) > 8:
            del first[k]
            dropped += 1
    P_anchor = sorted(first)
    T_anchor = [first[k] for k in P_anchor]
    matched = [(x, x) for x in range(len(P_anchor))]
    report.append(f"QUESTIONS root {n2}, Thai {m2}, matched {len(qpairs)}; root blocks anchored {len(P_anchor)}; anchors dropped by the consistency filter {dropped}")

# ------------------------------------------------------------ distribute between anchors
# segment boundaries: (root index range, Thai item range) between consecutive matched anchors
segs = []
prev_r, prev_t = 0, first_body
for p, t in matched:
    r_i, t_i = P_anchor[p], T_anchor[t]
    segs.append((prev_r, r_i, prev_t, t_i))
    prev_r, prev_t = r_i, t_i
segs.append((prev_r, len(rb), prev_t, len(T)))


PI_NUM = {"eka": 1, "duvi": 2, "tivi": 3, "catubbi": 4, "pañcavi": 5, "chabbi": 6, "sattavi": 7,
          "aṭṭhavi": 8, "navavi": 9, "dasavi": 10, "ekādasavi": 11}
TH_NUM = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")


def blk_sim(text_pi, text_th):
    a, na = vec(grams(skel_pi(text_pi)))
    b, nb = vec(grams(skel_th(text_th)))
    s = sum(x * b.get(g, 0.0) for g, x in a.items()) / (na * nb)
    # Rupa matrix: "N-vidhena rūpasaṅgaho" <-> "สงเคราะห์รูปเป็นหมวดละ N"
    low = text_pi.lower()
    for k, v in PI_NUM.items():
        if low.startswith(k) and re.search(r"(v|bb)idhena", low[:20]):
            nums = {int(x.translate(TH_NUM)) for x in re.findall(r"หมวดละ\s*([๐-๙]+)", text_th)}
            if nums == {v}:
                s += 0.5
            elif v in nums:
                s -= 0.2 * (len(nums) - 1)  # this group also holds other groups' numbers
            elif nums:
                s -= 0.3
    return s


def distribute(r_blocks, t_items):
    """Monotone partition of Thai items over root text blocks (empty groups allowed)."""
    k, L = len(r_blocks), len(t_items)
    if k == 0:
        return []
    if k == 1:
        return [t_items]
    best = {(0, 0): (0.0, None)}
    for a in range(1, k + 1):
        for e in range(0, L + 1):
            cand = None
            for s in range(0, e + 1):
                if (a - 1, s) not in best:
                    continue
                grp = t_items[s:e]
                if grp:
                    sc = blk_sim(r_blocks[a - 1]["text"], " ".join(T[x]["text"] for x in grp))
                    # a numbered Thai paragraph ([n]) is the natural start of a root block
                    if re.match(r"\[[๐-๙]+\]", T[grp[0]]["text"]):
                        sc += 0.3
                    # a numbered paragraph inside a group (not at its start) is a likely missed split
                    sc -= 0.2 * sum(1 for x in grp[1:] if re.match(r"\[[๐-๙]+\]", T[x]["text"]))
                else:
                    sc = -0.4
                v = best[(a - 1, s)][0] + sc
                if cand is None or v > cand[0]:
                    cand = (v, s)
            if cand:
                best[(a, e)] = cand
    out, e = [], L
    for a in range(k, 0, -1):
        s = best[(a, e)][1]
        out.append(t_items[s:e])
        e = s
    return list(reversed(out))


heading_extra = []
for r0, r1, t0, t1 in segs:
    r_part = rb[r0:r1]
    t_part = [x for x in range(t0, t1) if T[x]["kind"] != "hr"]
    r_heads = [x for x, b in enumerate(r_part) if b["kind"] == "h"]
    t_heads = [x for x in t_part if T[x]["kind"] == "h"]
    # pair headings in order when counts agree, otherwise by best similarity in order
    pairs_h = []
    if len(r_heads) == len(t_heads):
        pairs_h = list(zip(r_heads, t_heads))
    elif r_heads and t_heads:
        # order-preserving pairing by similarity (weighted LCS); weak pairs are skipped
        a_n, b_n = len(r_heads), len(t_heads)
        W = [[0.0] * (b_n + 1) for _ in range(a_n + 1)]
        for x in range(1, a_n + 1):
            for y in range(1, b_n + 1):
                s = blk_sim(r_part[r_heads[x - 1]]["text"], T[t_heads[y - 1]]["text"]) - 0.15
                W[x][y] = max(W[x - 1][y], W[x][y - 1], W[x - 1][y - 1] + s if s > 0 else -1)
        x, y = a_n, b_n
        while x > 0 and y > 0:
            s = blk_sim(r_part[r_heads[x - 1]]["text"], T[t_heads[y - 1]]["text"]) - 0.15
            if s > 0 and abs(W[x][y] - (W[x - 1][y - 1] + s)) < 1e-9:
                pairs_h.append((r_heads[x - 1], t_heads[y - 1]))
                x, y = x - 1, y - 1
            elif W[x][y] == W[x - 1][y]:
                x -= 1
            else:
                y -= 1
        pairs_h.reverse()
    for rh, th in pairs_h:
        mapping[r_part[rh]["id"]]["heading"] = th
    paired_t = {th for _, th in pairs_h}
    for th in t_heads:
        if th not in paired_t:
            heading_extra.append(th)
    for rh in r_heads:
        if rh not in {x for x, _ in pairs_h}:
            report.append(f"  UNMATCHED heading ^{r_part[rh]['id']} ({r_part[rh]['text']})")
    # split both sides at paired headings and distribute text
    cuts = [(-1, t0 - 1)] + sorted(pairs_h) + [(len(r_part), t1)]
    for (ra, ta), (rb_, tb_) in zip(cuts, cuts[1:]):
        rblocks = [b for b in r_part[ra + 1:rb_] if b["kind"] == "t"]
        titems = [x for x in t_part if ta < x < tb_ and x not in paired_t]
        groups = distribute(rblocks, titems)
        if not rblocks and titems:
            # Thai text with no root block here: attach to the last root text block before it
            prev = [b for b in r_part[:ra + 1] if b["kind"] == "t"]
            target = prev[-1]["id"] if prev else None
            if target:
                mapping[target]["items"].extend(titems)
            continue
        for b, g in zip(rblocks, groups):
            mapping[b["id"]]["items"].extend(g)

# ------------------------------------------------------------ numbered-group repair
# "N-vidhena …" root blocks (groups of 1, 2, 3 … items) and Thai paragraphs that open with
# "… หมวดละ N" ("group of N") are matched by the number N within a few blocks: the Thai
# paragraph and the following ones up to the next group move to that block.
_TD2 = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
rpos2 = {b["id"]: k for k, b in enumerate(R)}


def group_no_pi(text):
    low = text.lower()
    for key, v in PI_NUM.items():
        if low.startswith(key) and re.search(r"(v|bb)idhena", low[:20]):
            return v
    return None


moved = 0
for bid in [b["id"] for b in R if b["kind"] == "t"]:
    items = mapping[bid]["items"]
    cuts = [x for x in items if re.search(r"หมวดละ\s*([๐-๙]+)", T[x]["text"][:45])]
    for x in cuts:
        n_th = int(re.search(r"หมวดละ\s*([๐-๙]+)", T[x]["text"][:45]).group(1).translate(_TD2))
        k0 = rpos2[bid]
        cands = [R[k]["id"] for k in range(max(0, k0 - 15), min(len(R), k0 + 16))
                 if R[k]["kind"] == "t" and group_no_pi(R[k]["text"]) == n_th]
        if not cands or cands[0] == bid or group_no_pi(R[k0]["text"]) == n_th:
            continue
        target = min(cands, key=lambda c: abs(rpos2[c] - k0))
        cur = mapping[bid]["items"]
        start = cur.index(x)
        end = next((j for j in range(start + 1, len(cur)) if re.search(r"หมวดละ\s*[๐-๙]+", T[cur[j]]["text"][:45])), len(cur))
        chunk = cur[start:end]
        mapping[bid]["items"] = cur[:start] + cur[end:]
        mapping[target]["items"] = sorted(mapping[target]["items"] + chunk)
        moved += 1
report.append(f"GROUP repair (หมวดละ N <-> N-vidhena): {moved} Thai paragraphs moved")

# ------------------------------------------------------------ heading rescue pass
# A Thai heading left unpaired, and an unpaired root heading that sits between the same two
# root text blocks as the Thai heading's neighbours, are paired when they are similar enough.
# Nothing moves: the Thai heading already sits between the text of those two blocks.
rpos = {b["id"]: k for k, b in enumerate(R)}
item_block = {}
for bid, v in mapping.items():
    for x in v["items"]:
        item_block[x] = bid
paired_t = {v["heading"] for v in mapping.values() if v["heading"] is not None}
rescued = 0
for th in sorted(x for x in range(first_body, len(T)) if T[x]["kind"] == "h" and x not in paired_t):
    prev_b = next((item_block[x] for x in range(th - 1, -1, -1) if x in item_block and T[x]["kind"] != "h"), None)
    next_b = next((item_block[x] for x in range(th + 1, len(T)) if x in item_block and T[x]["kind"] != "h"), None)
    lo = rpos[prev_b] if prev_b else 0
    hi = rpos[next_b] if next_b else len(R)
    cands = [R[k] for k in range(lo, hi + 1) if k < len(R) and R[k]["kind"] == "h" and mapping[R[k]["id"]]["heading"] is None]
    if not cands:
        continue
    s_best, b_best = max(((blk_sim(c["text"], T[th]["text"]), c["id"]) for c in cands))
    if s_best > 0.15:
        mapping[b_best]["heading"] = th
        for v in mapping.values():
            if th in v["items"]:
                v["items"].remove(th)
        if th in heading_extra:
            heading_extra.remove(th)
        rescued += 1
report.append(f"HEADINGS rescued in a second pass: {rescued}")

# ------------------------------------------------------------ jump check
# For root blocks whose Thai text starts a numbered paragraph [n], the offset (root number - n)
# changes in small steps. A jump of more than 6 across root blocks that got no numbered
# paragraph of their own is a likely local misalignment and is listed for review.
TD = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
seq = []
for b in R:
    m = re.fullmatch(rf"{BOOK}-(\d+)", b["id"])
    if not m or b["kind"] != "t":
        continue
    ns = [int(mm.group(1).translate(TD)) for x in mapping[b["id"]]["items"] for mm in [re.match(r"\[([๐-๙]+)\]", T[x]["text"])] if mm]
    if ns:
        seq.append((int(m.group(1)), min(ns), b["id"]))
jumps = [(a, c) for a, c in zip(seq, seq[1:]) if abs((c[0] - c[1]) - (a[0] - a[1])) > 6]
report.append(f"OFFSET JUMPS (>6) between numbered paragraphs: {len(jumps)}")
for a, c in jumps[:60]:
    report.append(f"  ^{a[2]} [{a[1]}] -> ^{c[2]} [{c[1]}]")

# ------------------------------------------------------------ report
merged = [b["id"] for b in R if b["kind"] == "t" and not mapping[b["id"]]["items"]]
report.append(f"ROOT text blocks with no Thai text of their own (MERGE into neighbour): {len(merged)}")
report.append("  " + " ".join("^" + x for x in merged[:200]))
report.append(f"EXTRA Thai headings kept as bold lines inside the next block: {len(heading_extra)}")
covered = set()
for v in mapping.values():
    covered.update(v["items"])
    if v["heading"] is not None:
        covered.add(v["heading"])
lost = [k for k, it in enumerate(T) if k not in covered and it["kind"] not in ("hr",) and k not in heading_extra]
report.append(f"Thai items not assigned anywhere: {len(lost)}  {lost[:30]}")

json.dump({"mapping": mapping, "heading_extra": heading_extra}, open(out_json, "w", encoding="utf-8"), ensure_ascii=False)
open(out_report, "w", encoding="utf-8").write("\n".join(report) + "\n")
print("\n".join(report[:12]))
