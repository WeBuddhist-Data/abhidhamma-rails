"""g4_prior.py: g4 values against pi-1 … pi-6 (same keyword or base form, R1) and against the phase-1 sample files
(read-only helper)."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g4 as G
keys = {R.low(k) for k in G.G4} | {R.low(k) for t in G.CTX.values() for k in t}
samp = collections.defaultdict(collections.Counter)
for ch in R.SAMPLE:
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        for kv in l.split("] ", 1)[1].split(", "):
            k, v = kv.split("=", 1); samp[k][v] += 1
same = new = diff = 0
diffs = collections.Counter(); sdiff = collections.Counter()
for ch in G.CHAPTERS:
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        for kv in l.split("] ", 1)[1].split(", "):
            k, v = kv.split("=", 1)
            pv = R.prev_vals(k)
            if not pv:
                for b in R.base_forms(k):
                    pv = R.prev_vals(b)
                    if pv:
                        break
            if not pv:
                new += 1
            elif v in pv:
                same += 1
            else:
                diff += 1
                diffs[(k, v, pv.most_common(1)[0][0], R.low(k) in keys)] += 1
            if k in samp and v not in samp[k]:
                sdiff[(k, v, samp[k].most_common(1)[0][0])] += 1
print("same", same, "new", new, "diff", diff, "pairs", len(diffs))
for (k, v, p, t), n in sorted(diffs.items(), key=lambda x: (not x[0][3], -x[1])):
    print(f"{'G4' if t else 'MOD'}\t{k}\t{v}\tprior {p}\t{n}")
print("== against the sample")
for (k, v, p), n in sorted(sdiff.items()):
    print(f"S\t{k}\t{v}\tsample {p}\t{n}")
