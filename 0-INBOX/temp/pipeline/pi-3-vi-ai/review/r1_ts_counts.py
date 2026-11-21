"""r1: compare non-zero counts, our Vietnamese vs reference (digits). Console only: prints IDs and number tuples."""
import re, sys, importlib.util
spec = importlib.util.spec_from_file_location("c", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\review\r1_counts.py")
TS = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md"
IDRE = re.compile(r"\^([\w-]+)\s*$")
src = open(spec.origin, encoding="utf-8").read().split("for ch in sys.argv")[0]
ns = {}
exec(src, ns)
ts, buf = {}, []
for line in open(TS, encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    buf.append(line)
    m = IDRE.search(line)
    if m:
        ts[m.group(1)] = " ".join(l for l in buf if not l.startswith("![["))
        buf = []
U = {"uẩn": "k", "xứ": "a", "giới": "d"}
for ch in sys.argv[1:]:
    vs, vo = ns["segs"](ns["V"] + "\\" + ch)
    for i in vo:
        if i not in ts:
            print(i, "TS MISSING")
            continue
        t = re.sub(r"^\s*\d+\.\s", "", ts[i])
        t = re.sub(r"(?<=\s)\d+\.\s", " ", t)
        tc = [(int(n), U[u]) for n, u in re.findall(r"(\d+)\s*(uẩn|xứ|giới)", t) if int(n) != 0]
        vc = [x for x in ns["vi_counts"](" ".join(vs[i])) if x[0] != 0]
        if tc != vc:
            print(i, "\n   TS", tc, "\n   VI", vc)
