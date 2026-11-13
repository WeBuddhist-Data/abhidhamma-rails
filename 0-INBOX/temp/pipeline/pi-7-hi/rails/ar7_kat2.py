"""Lines where the number of Pāli kātabba-/kattabba- tokens differs from the number of Hindi «… चाहिए» verbs
that render them (करना/करने/करनी, also तैयार/शामिल/बना-); shows the other «… चाहिए» verbs on those lines."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
PK = re.compile(r"[kK][aā]t?tabb")
HK = re.compile(r"(?:कर|बना)(?:ना|ने|नी) चाहिए")
ALL = re.compile(r"(\S+ \S+) चाहिए")
cnt = collections.Counter()
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        np_ = len(PK.findall(p))
        if not np_:
            continue
        nh = len(HK.findall(h))
        if nh < np_:
            others = [m.group(1) for m in ALL.finditer(h)]
            for o in others:
                if not HK.search(o + " चाहिए"):
                    cnt[o.split()[-1]] += 1
            if "-v" in sys.argv:
                print(f"{part[:4]}:{i+1} pali={np_} hindi={nh} | {' / '.join(others)[:300]}")
                print("     P:", " | ".join(p[max(0, m.start()-60):m.end()+10] for m in PK.finditer(p))[:400])
print(cnt.most_common())
