"""Compare the ordered tense sequence of arise/cease verbs, Pali vs Vietnamese, per line."""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
only = sys.argv[1].split(",") if len(sys.argv) > 1 and sys.argv[1] != "all" else None
show = int(sys.argv[2]) if len(sys.argv) > 2 else 10


def pseq(p):
    out = []
    for m in re.finditer(r"\b(?:n?uppajj|nirujjh|uppann|niruddh|anusay|anusent|nānusent)\w*", p.lower()):
        w = m.group(0)
        if w.startswith("anusay") and not re.match(r"anusayi(ttha|ssa)", w):
            continue
        if re.search(r"itth", w):
            out.append("PAST")
        elif re.search(r"iss", w):
            out.append("FUT")
        elif "mān" in w:
            out.append("PROG")
        elif w.startswith(("uppann", "niruddh")):
            out.append("STATE")
        else:
            out.append("PRES")
    return out


def vseq(v):
    out = []
    for m in re.finditer(r"(sinh khởi|chấm dứt|nằm sẵn)", v):
        pre = v[max(0, m.start() - 30):m.start()]
        if pre.endswith(("khoảnh khắc ", "sự ", "của sự ", "thiền ")):
            continue
        pre = " " + pre.lower()
        while True:
            q = re.sub(r"(?:^|\s)(không|vẫn|cũng|vừa)\s$", " ", pre)
            if q == pre:
                break
            pre = q
        if re.search(r"trạng thái (đã )?$", pre):
            out.append("STATE")
        elif re.search(r"(đã từng|chưa từng|đã|chưa) $", pre):
            out.append("PAST")
        elif re.search(r"sẽ $", pre):
            out.append("FUT")
        elif re.search(r"đang $", pre):
            out.append("PROG")
        else:
            out.append("PRES")
    return out


c = collections.Counter()
k = 0
for f, n, sid, p, v in pairs(only):
    if p.startswith("#"):
        continue
    a, b = pseq(p), vseq(v)
    if a != b:
        c[f] += 1
        if k < show:
            k += 1
            print(f"{f}:{n} {sid}\n  {a}\n  {b}\n  P: {p.strip()[:600]}\n  V: {v.strip()[:800]}")
print(c)
