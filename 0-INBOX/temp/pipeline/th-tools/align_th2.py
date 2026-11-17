"""Align a Thai Royal-edition book (pi-2 … pi-7) to its root, top-down.

1. Headings: all body headings of root and Thai are paired in order (weighted LCS on a
   Pali/Thai consonant-skeleton similarity). Paired headings are hard section boundaries.
2. Inside each section: questions are aligned (root questions: '?' or a "katam…" opening;
   Thai: 'เป็นไฉน' or '?'), giving anchors for root blocks; anchors out of step with the
   Thai paragraph numbering are dropped.
3. Between anchors, Thai paragraphs are distributed over the root blocks in order
   (similarity, a bonus for starting at a numbered paragraph [n], a penalty for empty blocks).
4. "N-vidhena" root blocks and Thai "หมวดละ N" paragraphs are matched by N.

Usage: align_th2.py <root.md> <draft.md> <map.json> <report.txt> <book>
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

root_path, th_path, out_json, out_report, BOOK = sys.argv[1:6]
DEBUG = sys.argv[6] if len(sys.argv) > 6 else None  # a root id: print the alignment of its section
R = parse_root(root_path)
T = parse_draft(th_path)
report = []

# ------------------------------------------------------------ skeleton similarity
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
N = len(R)
idf = {g: math.log((N + 1) / (c + 1)) + 1 for g, c in df.items()}


def vec(c):
    v = {g: n * idf.get(g, 0.0) for g, n in c.items() if g in idf}
    return v, (math.sqrt(sum(x * x for x in v.values())) or 1.0)


def cos(A, B):
    (a, na), (b, nb) = A, B
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(g, 0.0) for g, x in a.items()) / (na * nb)


PI_NUM = {"eka": 1, "duvi": 2, "tivi": 3, "catubbi": 4, "pañcavi": 5, "chabbi": 6, "sattavi": 7,
          "aṭṭhavi": 8, "navavi": 9, "dasavi": 10, "ekādasavi": 11}
TD = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")


def group_no_pi(text):
    """N for a root block that holds exactly one 'N-vidhena …' group, else None."""
    low = text.lower()
    nums = set()
    for w in re.findall(r"(\w+?)(?:v|bb)idhena", low):
        for key, v in PI_NUM.items():
            if (w + "vi").startswith(key) or (w + "bbi").startswith(key) or w == key.rstrip("vib"):
                nums.add(v)
                break
    if len(nums) != 1:
        return None  # no group, or several groups in one block
    for key, v in PI_NUM.items():
        if low.startswith(key) and re.search(r"(v|bb)idhena", low[:20]):
            return v
    return None


def blk_sim(text_pi, text_th):
    s = cos(vec(grams(skel_pi(text_pi))), vec(grams(skel_th(text_th))))
    v = group_no_pi(text_pi)
    if v:
        nums = {int(x.translate(TD)) for x in re.findall(r"หมวดละ\s*([๐-๙]+)", text_th)}
        if nums == {v}:
            s += 0.5
        elif v in nums:
            s -= 0.2 * (len(nums) - 1)
        elif nums:
            s -= 0.3
    return s


# ------------------------------------------------------------ front
title_idx = 0 if T[0]["kind"] == "h" else None
homage_idx = next((k for k, it in enumerate(T) if it["text"].startswith("ขอนอบน้อม")),
                  next(k for k, it in enumerate(T) if it["kind"] == "p"))
mapping = {b["id"]: {"items": [], "heading": None} for b in R}
mapping["T-1"]["items"] = [homage_idx]
mapping[f"{BOOK}-0"]["heading"] = title_idx
root_body = next(k for k, b in enumerate(R) if b["id"] == f"{BOOK}-0") + 1
t_body = [k for k in range(len(T)) if k not in (title_idx, homage_idx) and k > min(x for x in (title_idx, homage_idx) if x is not None)]
# Thai items before the homage (other than the title) are kept with the first block
pre = [k for k in range(len(T)) if k not in (title_idx, homage_idx) and k < homage_idx]

# Thai paragraph number of each item
par_of, cur = {}, None
for k, it in enumerate(T):
    m = re.match(r"\[([๐-๙]+)\]", it["text"])
    if m:
        cur = int(m.group(1).translate(TD))
    par_of[k] = cur

# ------------------------------------------------------------ 0. rough position map
# A quick whole-book question alignment gives, for any Thai item, an approximate root index.
# It is only used to stop a heading from pairing with a same-named heading far away.
def _rough_map():
    pq_all, tq_all = [], []
    for k in range(root_body, len(R)):
        if R[k]["kind"] != "t":
            continue
        t = R[k]["text"]
        qs = re.findall(r"[^.?–;]*\?", t) or ([re.split(r"…pe…", t)[0]] if re.search(r"\b(Katam|katam|Kathaṃ)", t[:40]) else [])
        pq_all.extend((k, q) for q in qs)
    tq_all = [(k, T[k]["text"]) for k in t_body if T[k]["kind"] in ("p", "li") and ("เป็นไฉน" in T[k]["text"] or "?" in T[k]["text"])]
    PV = [vec(grams(skel_pi(q))) for _, q in pq_all]
    TV = [vec(grams(skel_th(q.split("เป็นไฉน")[0].split("?")[0]))) for _, q in tq_all]
    n2, m2, band = len(pq_all), len(tq_all), 150
    S, B = {(0, 0): 0.0}, {}
    for i in range(n2 + 1):
        c = int(i * m2 / max(n2, 1))
        for j in range(max(0, c - band), min(m2, c + band) + 1):
            if i == 0 and j == 0:
                continue
            best, arg = -1e9, None
            if i and j and (i - 1, j - 1) in S:
                v = S[(i - 1, j - 1)] + cos(PV[i - 1], TV[j - 1]) - 0.15
                if v > best:
                    best, arg = v, "d"
            if i and (i - 1, j) in S and S[(i - 1, j)] - 0.1 > best:
                best, arg = S[(i - 1, j)] - 0.1, "u"
            if j and (i, j - 1) in S and S[(i, j - 1)] - 0.1 > best:
                best, arg = S[(i, j - 1)] - 0.1, "l"
            if arg:
                S[(i, j)], B[(i, j)] = best, arg
    i, j, pts = n2, m2, []
    while i or j:
        a = B.get((i, j))
        if a is None:
            break
        if a == "d":
            if cos(PV[i - 1], TV[j - 1]) > 0.35:  # confident pairs only
                pts.append((tq_all[j - 1][0], pq_all[i - 1][0]))
            i, j = i - 1, j - 1
        elif a == "u":
            i -= 1
        else:
            j -= 1
    pts.sort()
    return pts


ROUGH = _rough_map()


def approx_root(t_idx):
    """Piecewise-linear estimate of the root index for a Thai item index."""
    if not ROUGH:
        return None
    lo = max((p for p in ROUGH if p[0] <= t_idx), default=ROUGH[0])
    hi = min((p for p in ROUGH if p[0] >= t_idx), default=ROUGH[-1])
    if hi[0] == lo[0]:
        return lo[1]
    return lo[1] + (hi[1] - lo[1]) * (t_idx - lo[0]) / (hi[0] - lo[0])


report.append(f"ROUGH map: {len(ROUGH)} confident question pairs")

# ------------------------------------------------------------ 1. headings, globally
RH = [k for k in range(root_body, len(R)) if R[k]["kind"] == "h"]
TH_ = [k for k in t_body if T[k]["kind"] == "h"]
HR = [vec(grams(skel_pi(R[k]["text"]))) for k in RH]
HT = [vec(grams(skel_th(T[k]["text"]))) for k in TH_]
APX = [approx_root(k) for k in TH_]


def h_score(x, y):
    """Similarity of root heading x and Thai heading y, less a penalty for distance in the text."""
    s = cos(HR[x], HT[y]) - 0.2
    if APX[y] is not None:
        s -= 0.01 * abs(RH[x] - APX[y])
    return s


a_n, b_n = len(RH), len(TH_)
W = [[0.0] * (b_n + 1) for _ in range(a_n + 1)]
for x in range(1, a_n + 1):
    rowp, row = W[x - 1], W[x]
    for y in range(1, b_n + 1):
        s = h_score(x - 1, y - 1)
        row[y] = max(rowp[y], row[y - 1], (rowp[y - 1] + s) if s > 0 else -1)
x, y, hpairs = a_n, b_n, []
while x > 0 and y > 0:
    s = h_score(x - 1, y - 1)
    if s > 0 and abs(W[x][y] - (W[x - 1][y - 1] + s)) < 1e-9:
        hpairs.append((RH[x - 1], TH_[y - 1]))
        x, y = x - 1, y - 1
    elif W[x][y] == W[x - 1][y]:
        x -= 1
    else:
        y -= 1
hpairs.reverse()
for rk, tk in hpairs:
    mapping[R[rk]["id"]]["heading"] = tk
paired_t = {tk for _, tk in hpairs}
report.append(f"HEADINGS root {a_n}, Thai {b_n}, paired {len(hpairs)}")


# ------------------------------------------------------------ helpers for a section
ITEM_V = {}


def item_vec(x):
    if x not in ITEM_V:
        ITEM_V[x] = vec(grams(skel_th(T[x]["text"])))[0]
    return ITEM_V[x]


ROOT_V = {}


def root_vec(bid, text):
    if bid not in ROOT_V:
        ROOT_V[bid] = vec(grams(skel_pi(text)))
    return ROOT_V[bid]


MAXG = 60  # at most this many Thai paragraphs per root block


def distribute(r_blocks, t_items):
    """Monotone partition of Thai items over root blocks. Items are first grouped into units
    (a numbered paragraph [n] with its continuation paragraphs); units are distributed."""
    k = len(r_blocks)
    if k == 0:
        return []
    if k == 1:
        return [t_items]
    units = [[x] for x in t_items]  # one unit per Thai paragraph (a block may take several)
    U = len(units)
    uvec = []
    for u in units:
        d = Counter()
        for x in u:
            d.update(item_vec(x))
        uvec.append(d)
    unum = [re.match(r"\[[๐-๙]+\]", T[u[0]]["text"]) is not None for u in units]
    ugrp = [{int(m.translate(TD)) for x in u for m in re.findall(r"หมวดละ\s*([๐-๙]+)", T[x]["text"])} for u in units]
    NEG = -1e9
    best = [[NEG] * (U + 1) for _ in range(k + 1)]
    arg = [[0] * (U + 1) for _ in range(k + 1)]
    best[0][0] = 0.0
    for a in range(1, k + 1):
        rv, rn = root_vec(r_blocks[a - 1]["id"], r_blocks[a - 1]["text"])
        gno = group_no_pi(r_blocks[a - 1]["text"])
        for e in range(0, U + 1):
            # empty group
            cand, cs = (best[a - 1][e] - 0.15, e) if best[a - 1][e] > NEG else (NEG, e)
            acc, norm2, dot, nums = {}, 0.0, 0.0, set()
            for s in range(e - 1, max(-1, e - 1 - MAXG), -1):
                for g, w in uvec[s].items():
                    old = acc.get(g, 0.0)
                    acc[g] = old + w
                    norm2 += 2 * old * w + w * w
                    dot += w * rv.get(g, 0.0)
                nums |= ugrp[s]
                if best[a - 1][s] <= NEG:
                    continue
                sc = dot / (rn * (math.sqrt(norm2) or 1.0))
                sc += 0.3 if unum[s] else 0.0
                sc -= 0.2 * sum(unum[s + 1:e])
                if gno:
                    if nums == {gno}:
                        sc += 0.5
                    elif gno in nums:
                        sc -= 0.2 * (len(nums) - 1)
                    elif nums:
                        sc -= 0.3
                v = best[a - 1][s] + sc
                if v > cand:
                    cand, cs = v, s
            best[a][e], arg[a][e] = cand, cs
    out, e = [], U
    for a in range(k, 0, -1):
        s = arg[a][e]
        out.append([x for u in units[s:e] for x in u])
        e = s
    return list(reversed(out))


def root_questions(blocks):
    pq = []
    for k in blocks:
        t = R[k]["text"]
        found = False
        for m in re.finditer(r"[^.?–;]*\?", t):
            pq.append((k, m.group(0)))
            found = True
        if not found and re.search(r"\b(Katam|katam|Kathaṃ)", t[:40]):
            pq.append((k, re.split(r"…pe…", t)[0]))
    return pq


def align_questions(pq, tq):
    PQv = [vec(grams(skel_pi(q))) for _, q in pq]
    TQv = [vec(grams(skel_th(q.split("เป็นไฉน")[0].split("?")[0]))) for _, q in tq]
    n2, m2 = len(pq), len(tq)
    S, B = {(0, 0): 0.0}, {}
    for i in range(n2 + 1):
        for j in range(m2 + 1):
            if i == 0 and j == 0:
                continue
            best, arg = -1e9, None
            if i and j:
                v = S[(i - 1, j - 1)] + cos(PQv[i - 1], TQv[j - 1]) - 0.15
                if v > best:
                    best, arg = v, "d"
            if i:
                v = S[(i - 1, j)] - 0.10
                if v > best:
                    best, arg = v, "u"
            if j:
                v = S[(i, j - 1)] - 0.10
                if v > best:
                    best, arg = v, "l"
            S[(i, j)], B[(i, j)] = best, arg
    i, j, pairs = n2, m2, []
    while i or j:
        a = B[(i, j)]
        if a == "d":
            pairs.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif a == "u":
            i -= 1
        else:
            j -= 1
    return list(reversed(pairs))


def align_section(r_idx, t_idx):
    """Assign Thai items t_idx (no paired headings) to root text blocks r_idx (indexes into R)."""
    blocks = [k for k in r_idx if R[k]["kind"] == "t"]
    if not blocks:
        return t_idx  # nothing to receive them here: returned to the caller
    if not t_idx:
        return []
    pq = root_questions(blocks)
    tq = [(k, T[k]["text"]) for k in t_idx if T[k]["kind"] in ("p", "li") and ("เป็นไฉน" in T[k]["text"] or "?" in T[k]["text"])]
    first = {}
    if pq and tq and len(pq) * len(tq) < 4_000_000:
        for qi, tj in align_questions(pq, tq):
            first.setdefault(pq[qi][0], tq[tj][0])
    # consistency filter on the Thai paragraph numbering
    keys = sorted(first)
    offs = []
    for k in keys:
        m = re.fullmatch(rf"{BOOK}-(\d+)", R[k]["id"])
        n_th = par_of.get(first[k])
        offs.append(int(m.group(1)) - n_th if (m and n_th is not None) else None)
    for i, k in enumerate(keys):
        if offs[i] is None:
            continue
        win = [o for o in offs[max(0, i - 7):i + 8] if o is not None]
        if abs(offs[i] - sorted(win)[len(win) // 2]) > 8:
            del first[k]
    # monotonic anchors (block order and Thai order must agree)
    anchors, last_t = [], -1
    for k in sorted(first):
        if first[k] > last_t:
            anchors.append((k, first[k]))
            last_t = first[k]
    if DEBUG and any(R[k]["id"] == DEBUG for k in blocks):
        print(f"DEBUG section ^{R[blocks[0]]['id']}..^{R[blocks[-1]]['id']}: blocks {len(blocks)}, Thai items {len(t_idx)}, "
              f"root questions {len(pq)}, Thai questions {len(tq)}, anchors kept {len(anchors)}: "
              + " ".join(f"^{R[k]['id']}={t}" for k, t in anchors[:30]))
    cuts_r = [blocks[0]] + [k for k, _ in anchors if k != blocks[0]]
    cuts_t = [t_idx[0]] + [t for k, t in anchors if k != blocks[0]]
    for n_seg in range(len(cuts_r)):
        r0 = cuts_r[n_seg]
        r1 = cuts_r[n_seg + 1] if n_seg + 1 < len(cuts_r) else blocks[-1] + 1
        t0 = cuts_t[n_seg]
        t1 = cuts_t[n_seg + 1] if n_seg + 1 < len(cuts_t) else t_idx[-1] + 1
        rb = [R[k] for k in blocks if r0 <= k < r1]
        ti = [x for x in t_idx if t0 <= x < t1]
        for b, g in zip(rb, distribute(rb, ti)):
            mapping[b["id"]]["items"].extend(g)
    return []


# ------------------------------------------------------------ 2-3. sections
cut_r = [root_body] + [rk for rk, _ in hpairs] + [len(R)]
cut_t = [min(t_body)] + [tk for _, tk in hpairs] + [len(T)]
leftover = list(pre)
for s in range(len(cut_r) - 1):
    r_idx = list(range(cut_r[s], cut_r[s + 1]))
    t_idx = [k for k in range(cut_t[s], cut_t[s + 1]) if k not in paired_t and k in set(t_body) and T[k]["kind"] != "hr"]
    t_idx = leftover + t_idx
    leftover = align_section(r_idx, t_idx)
if leftover:
    last = [b for b in R if b["kind"] == "t"][-1]["id"]
    mapping[last]["items"].extend(leftover)

# ------------------------------------------------------------ 4. numbered-group repair
rpos = {b["id"]: k for k, b in enumerate(R)}
moved = 0
for bid in [b["id"] for b in R if b["kind"] == "t"]:
    cuts = [x for x in mapping[bid]["items"] if re.search(r"หมวดละ\s*[๐-๙]+", T[x]["text"][:45])]
    for x in cuts:
        n_th = int(re.search(r"หมวดละ\s*([๐-๙]+)", T[x]["text"][:45]).group(1).translate(TD))
        k0 = rpos[bid]
        if group_no_pi(R[k0]["text"]) is None or group_no_pi(R[k0]["text"]) == n_th:
            continue  # only move between single-group blocks
        cands = [R[k]["id"] for k in range(max(0, k0 - 15), min(len(R), k0 + 16))
                 if R[k]["kind"] == "t" and group_no_pi(R[k]["text"]) == n_th]
        if not cands:
            continue
        target = min(cands, key=lambda c: abs(rpos[c] - k0))
        cur_items = mapping[bid]["items"]
        start = cur_items.index(x)
        end = next((j for j in range(start + 1, len(cur_items)) if re.search(r"หมวดละ\s*[๐-๙]+", T[cur_items[j]]["text"][:45])), len(cur_items))
        chunk = cur_items[start:end]
        mapping[bid]["items"] = cur_items[:start] + cur_items[end:]
        mapping[target]["items"] = sorted(mapping[target]["items"] + chunk)
        moved += 1
report.append(f"GROUP repair (หมวดละ N <-> N-vidhena): {moved} moved")

# ------------------------------------------------------------ checks
for v in mapping.values():
    v["items"] = sorted(set(v["items"]))
merged = [b["id"] for b in R if b["kind"] == "t" and not mapping[b["id"]]["items"]]
report.append(f"ROOT text blocks with no Thai text of their own (MERGE into neighbour): {len(merged)}")
report.append("  " + " ".join("^" + x for x in merged))
seq = []
for b in R:
    m = re.fullmatch(rf"{BOOK}-(\d+)", b["id"])
    if m and b["kind"] == "t":
        ns = [par_of[x] for x in mapping[b["id"]]["items"] if re.match(r"\[[๐-๙]+\]", T[x]["text"])]
        if ns:
            seq.append((int(m.group(1)), min(ns), b["id"]))
back = [(a, c) for a, c in zip(seq, seq[1:]) if c[1] < a[1]]
jumps = [(a, c) for a, c in zip(seq, seq[1:]) if abs((c[0] - c[1]) - (a[0] - a[1])) > 6]
report.append(f"NON-MONOTONIC numbered paragraphs: {len(back)}")
report.append(f"OFFSET JUMPS (>6): {len(jumps)}")
for a, c in jumps[:80]:
    report.append(f"  ^{a[2]} [{a[1]}] -> ^{c[2]} [{c[1]}]")
placed = set()
for v in mapping.values():
    placed.update(v["items"])
    if v["heading"] is not None:
        placed.add(v["heading"])
lost = [k for k, it in enumerate(T) if k not in placed and it["kind"] != "hr"]
report.append(f"Thai items not assigned anywhere: {len(lost)} {lost[:20]}")
unh = [b["id"] for b in R if b["kind"] == "h" and mapping[b["id"]]["heading"] is None and b["id"] not in ("0",)]
report.append(f"ROOT headings with no Thai heading: {len(unh)}")
json.dump({"mapping": mapping, "heading_extra": []}, open(out_json, "w", encoding="utf-8"), ensure_ascii=False)
open(out_report, "w", encoding="utf-8").write("\n".join(report) + "\n")
print("\n".join(r if len(r) < 300 else r[:300] + " …" for r in report if not r.startswith("  ^")))
