"""List the distinct Hindi sense-organ being phrases (… जन्म लेने वालों में etc.) in 3.x, 4, 10.x."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
ORG = r"(?:आँख|कान|नाक|जीभ|शरीर|भौतिक रूप|मन)"
RX = re.compile(r"(?:बाकी |और |सभी मरने वालों में और )?(?:[^,।?]*?)(?:" + ORG + r" के साथ|बिना " + ORG + r"|" + ORG +
                r"(?: वाले|-रहित| से रहित))[^,।?]*?(?:जन्म लेने वालों में|जन्म लेने वाली स्त्रियों में|जन्म लेने वाले पुरुषों में|लोगों में|मरने वालों में)")
P = re.compile(r"\b(sa|a)(cakkhuk|sotak|ghānak|jivhak|kāyak|rūpak|cittak)")
cnt = collections.defaultdict(collections.Counter)
for part in C.PARTS:
    if not part.startswith(("3-", "4-", "10-")):
        continue
    for p, h in C.pairs(part):
        if not P.search(p):
            continue
        for m in RX.finditer(h):
            s = m.group(0)
            s = re.sub(r"^.*?(में|,) ", "", s) if " में " in s[:-20] else s
            cnt[s.strip()][C.short(part).split(".")[0]] += 1
for k, v in sorted(cnt.items(), key=lambda kv: (sorted(kv[1])[0], kv[0])):
    print(dict(v), "::", k)
