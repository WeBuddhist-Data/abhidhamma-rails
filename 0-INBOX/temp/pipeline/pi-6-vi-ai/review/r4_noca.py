"""no ca + multi-member clause: how is it rendered (neither vs not-both)?"""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
show = int(sys.argv[1]) if len(sys.argv) > 1 else 3
c = collections.Counter()
ex = collections.defaultdict(list)
for f, n, sid, p, v in pairs():
    pcl = re.findall(r"\bno ca\b[^.;?]*", p)
    vcl = re.findall(r"\bnhưng\b[^.;?]*", v)
    for i, cl in enumerate(pcl):
        members = len(re.findall(r"\w+ ca\b", cl.replace("no ca", "")))
        if members < 2:
            continue
        neg = bool(re.search(r"\bna\b|appahīn|nuppajj", cl))
        vc = vcl[i] if i < len(vcl) else ""
        kind = ("denied" if neg else "plain") + ":" + (
            "neither" if "cũng không có" in vc or "cũng không" in vc else
            ("và" if " và " in vc else "other"))
        c[kind] += 1
        ex[kind].append(f"{f}:{n} {sid}\n  P: {cl}\n  V: {vc}")
for k, x in c.items():
    print(x, k)
for k in ex:
    for e in ex[k][:show]:
        print(k, e)
