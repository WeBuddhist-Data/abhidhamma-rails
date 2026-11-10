"""Clause-level scan: group identical Pāli clauses (block IDs, variant brackets stripped) and list the
distinct English renderings. usage: hz_scan.py [out-file]"""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en")
from hz_show import PARTS, pairs

BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR_P = re.compile(r"\s*\[[^\]]*\]")
SPLIT = re.compile(r"(?<=[?.;:])\s+|\s+–\s+|\s+—\s+")


def norm(s):
    s = BID.sub("", s)
    s = VAR_P.sub("", s)
    return s.strip()


def clauses(s):
    return [c.strip() for c in SPLIT.split(norm(s)) if c.strip()]


groups = collections.defaultdict(lambda: collections.defaultdict(list))
for part in PARTS:
    for i, (p, e) in enumerate(pairs(part)):
        if p.startswith("#"):
            groups[norm(p).lstrip("# ")][norm(e).lstrip("# ")].append(f"{part[:4]}:{i}")
            continue
        cp, ce = clauses(p), clauses(e)
        if len(cp) == len(ce):
            for a, b in zip(cp, ce):
                groups[a][b].append(f"{part[:4]}:{i}")
        groups["LINE::" + norm(p)][norm(e)].append(f"{part[:4]}:{i}")

out = []
for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
    if len(v) > 1:
        # ignore pure case/final-punct differences
        keys = {re.sub(r"[.?;:,]$", "", x).lower() for x in v}
        if len(keys) <= 1:
            continue
        out.append(f"### {k}")
        for e, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            files = sorted({l.split(':')[0] for l in locs})
            out.append(f"  [{len(locs)}] {','.join(files)} :: {e}")
open(sys.argv[1] if len(sys.argv) > 1 else "hz_scan_out.txt", "w", encoding="utf-8").write("\n".join(out))
print("groups with variants:", sum(1 for l in out if l.startswith("###")))
