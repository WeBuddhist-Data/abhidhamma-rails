import sys, re
from collections import defaultdict, Counter
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
chs = sys.argv[1].split(",")
mode = sys.argv[2] if len(sys.argv) > 2 else "seq"

PA = [("rūpakkhandh", "R"), ("vedanākkhandh", "V"), ("saññākkhandh", "S"),
      ("saṅkhārakkhandh", "K"), ("viññāṇakkhandh", "C")]
RA = [(r"совокупност\w*\s+материальной формы", "R"), (r"совокупност\w*\s+чувств", "V"),
      (r"совокупност\w*\s+восприятия", "S"), (r"совокупност\w*\s+формирующих факторов", "K"),
      (r"совокупност\w*\s+сознания", "C")]

def pali_aggs(s):
    toks = []
    for m in re.finditer(r"\w+", s):
        w = m.group(0).lower()
        for st, c in PA:
            if w.startswith(st):
                toks.append(c)
    return "".join(toks)

def ru_aggs(s):
    hits = []
    for pat, c in RA:
        for m in re.finditer(pat, s, re.I):
            hits.append((m.start(), c))
    return "".join(c for _, c in sorted(hits))

PV = [(r"n?uppajj(ati|atī)", "u0"), (r"n?uppajjitth", "u-"), (r"n?uppajjiss", "u+"),
      (r"nirujjh(ati|atī)", "n0"), (r"nirujjh[ia]tth", "n-"), (r"nirujjhiss", "n+"),
      (r"parijān(āti|ātī|anti)", "p0"), (r"parijānitth", "p-"), (r"parijāniss", "p+")]
RV = [(r"возникает|возникают", "u0"), (r"возникал[аои]?\b", "u-"), (r"возникнет|возникнут", "u+"),
      (r"прекращается|прекращаются", "n0"), (r"прекращал(ся|ась|ось|ись)", "n-"), (r"прекратится|прекратятся", "n+"),
      (r"(полностью )?понима(ет|ют)", "p0"), (r"(полностью )?понимал[аи]?\b", "p-"), (r"(полностью )?(поймёт|поймут)", "p+")]

def pali_verbs(s):
    out = []
    words = re.findall(r"[\w]+", s.lower())
    flip = False
    prev = ""
    for i, w in enumerate(words):
        if w == "no" and i + 1 < len(words) and words[i + 1] == "ca":
            flip = True
        for pat, c in PV:
            if re.match(pat + r"\w*$", w) or re.match(pat, w):
                neg = w.startswith("nupp") or prev == "na"
                if flip:
                    neg = not neg
                    flip = False
                out.append(c + ("N" if neg else "P"))
                break
        prev = w
    return out

def ru_verbs(s):
    hits = []
    for pat, c in RV:
        for m in re.finditer(pat, s):
            before = s[max(0, m.start() - 4):m.start()]
            neg = before.endswith("не ")
            hits.append((m.start(), c + ("N" if neg else "P")))
    return [c for _, c in sorted(hits)]

def collapse(seq):
    out = []
    for x in seq:
        if not out or out[-1] != x:
            out.append(x)
    return out

def ptempl(s):
    t = s
    t = re.sub(r"\^[\d-]+", "", t)
    for st, c in PA:
        t = re.sub(st + r"\w*", "A", t)
    t = re.sub(r"n?uppajj\w+|nirujjh\w+|parijān\w+", "V", t)
    return t.strip()

def rtempl(s):
    t = re.sub(r"\^[\d-]+", "", s)
    for pat, c in RA:
        t = re.sub(pat, "A", t, flags=re.I)
    for pat, c in RV:
        t = re.sub(pat, "V", t)
    return t.strip()

groups = defaultdict(Counter)
first = {}
for ch in chs:
    p = open(base + r"\pali\pi-6_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
    r = open(base + r"\russian\pi-6-russian-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
    for i, (a, b) in enumerate(zip(p, r)):
        if not a.strip():
            continue
        if mode == "seq":
            pa, ra = pali_aggs(a), ru_aggs(b)
            pv, rv = collapse(pali_verbs(a)), collapse(ru_verbs(b))
            up, ur = len(re.findall(r"upapajj", a)), len(re.findall(r"перерожда", b))
            cp, cr = len(re.findall(r"cavant|cavam", a)), len(re.findall(r"умира", b))
            probs = []
            if pa != ra: probs.append(f"AGG {pa} vs {ra}")
            if pv != rv: probs.append(f"VERB {pv} vs {rv}")
            if up != ur: probs.append(f"UPAPAJJ {up} vs {ur}")
            if cp != cr: probs.append(f"CAV {cp} vs {cr}")
            if probs:
                print(f"{ch}:{i+1}: {'; '.join(probs)}\n  P: {a}\n  R: {b}")
        else:
            pt, rt = ptempl(a), rtempl(b)
            groups[pt][rt] += 1
            first.setdefault((pt, rt), f"{ch}:{i+1}")
if mode != "seq":
    n = 0
    for pt, c in groups.items():
        if mode == "incons" and len(c) < 2:
            continue
        n += 1
        print("P:", pt)
        for rt, k in c.most_common():
            print(f"   [{k}] {first[(pt, rt)]} R: {rt}")
    print("groups", n, "of", len(groups))
