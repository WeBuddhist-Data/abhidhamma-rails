"""Overview for the scan: every keyword with >1 value; per value its uses, first segment, ±W chars of the Burmese
around the value's first chunk and of the Pāli around the keyword.
usage: python3 -I -X utf8 harmonise_overview.py [W] > file"""
import sys, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from harmonise_show import segments, MY, PI  # noqa: E402
W = int(sys.argv[1]) if len(sys.argv) > 1 else 30
uses = collections.defaultdict(list)
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name[:-len(".mapped.md")]
    my = segments(MY / f"{ch}.md"); pa = segments(PI / f"{ch}.md")
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1); sid = sid[1:]
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            uses[k[:1].lower() + k[1:]].append((ch.split("-")[0], sid, k, v, my[sid], pa.get(sid, "")))
for kk in sorted(uses, key=lambda x: (x.lower(), x)):
    vals = collections.Counter(u[3] for u in uses[kk])
    if len(vals) < 2:
        continue
    print(f"== {kk}")
    for v, n in vals.most_common():
        us = [u for u in uses[kk] if u[3] == v]
        chs = sorted({u[0] for u in us}, key=lambda x: (x != 'preamble', int(x) if x.isdigit() else 0))
        ch, sid, k, _, t, p = us[0]
        c = v.split(" … ")[0].split()[0] if v != "(no direct equivalent)" else ""
        c2 = re.sub("(သော|သည်)$", "", c) or c
        i = t.find(c2) if c2 else -1
        j = p.find(k)
        my_ = t[max(0, i - W):i + W + len(c2)] if i >= 0 else "?"
        pa_ = p[max(0, j - W):j + W + len(k)] if j >= 0 else "?"
        print(f"  [{n}; {' '.join(chs)}] {v}  @{sid}  MY…{my_}…  PA…{pa_}…")
