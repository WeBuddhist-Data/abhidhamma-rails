import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *
# Reads the reference translation and prints only counts per segment (no text is written anywhere).
TS = os.path.join(ROOT, r"1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md")
with open(TS, encoding="utf-8") as f:
    tl = f.read().split("\n")
seg = defaultdict(list); cur = None
for l in tl:
    m = re.match(r"!\[\[.*#\^([0-9a-z-]+)\]\]", l.strip())
    if m:
        cur = m.group(1); continue
    if cur and l.strip():
        seg[cur].append(IDRE.sub("", l))
P = defaultdict(list); V = defaultdict(list)
for fn, ln, sid, p, v in pairs():
    P[sid].append(p); V[sid].append(v)

def pc(t):
    return dict(q=t.count("?"), am=len(re.findall(r"Āmantā", t)), no=len(re.findall(r"(?:^|\? )No\.", t)),
                na=len(re.findall(r"Natthi", t)), noca=len(re.findall(r"\bno ca\b", t)))
def tc(t):
    return dict(q=t.count("?"), am=len(re.findall(r"Phải rồi|Đúng vậy|Phải\.", t)),
                no=len(re.findall(r"Không phải\.|Không\.", t)), na=len(re.findall(r"Không có\.|Không có", t)))
ids = [i for i in P if not i.endswith("-0")]
miss = [i for i in ids if i not in seg]
print("segments", len(ids), "missing in TS", len(miss), miss[:20])
for i in ids:
    if i not in seg: continue
    a = pc(" ".join(P[i])); b = tc(" ".join(seg[i]))
    flags = []
    if a["q"] != b["q"]: flags.append("q %d/%d" % (a["q"], b["q"]))
    if a["am"] != b["am"]: flags.append("amanta %d/%d" % (a["am"], b["am"]))
    if a["no"] != b["no"]: flags.append("no %d/%d" % (a["no"], b["no"]))
    if flags: print(i, " | ".join(flags))
