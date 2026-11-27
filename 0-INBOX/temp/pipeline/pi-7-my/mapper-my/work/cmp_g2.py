"""cmp_g2.py: g2 uses whose value equals / differs from a pi-1 … pi-6 value of the same keyword (or base form, R1),
and values that differ from the phase-1 sample mapping of the same keyword (read-only helper; g2)."""
import sys, pathlib, collections, re, importlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
G = importlib.import_module("map_g2")
M = G.mapper()
p1 = set(re.findall(r"^\| ([^|]+) = ", (D / "map-table.md").read_text(encoding="utf-8"), re.M))
sample = collections.defaultdict(collections.Counter)
for ch in R.SAMPLE:
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        for kv in l.split("] ", 1)[1].split(", "):
            k, v = kv.split("=", 1); sample[k][v] += 1
same = new = diff = 0
diffs = collections.defaultdict(collections.Counter); src = {}
sdiff = collections.Counter()
for ch in G.CHAPTERS:
    B, P = R.burmese(ch), R.pali(ch)
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if k in sample and v not in sample[k]:
                sdiff[(k, v, sample[k].most_common(1)[0][0])] += 1
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
                diffs[(k, v)][pv.most_common(1)[0][0]] += 1
                src.setdefault((k, v), M.SRC.get((sid, k)) or "?")
                M.lookup(ch, sid, k, P.get(sid, ""), B.get(sid, ""))
                src[(k, v)] = M.SRC.get((sid, k)) or "?"
print(f"same {same} new {new} diff {diff} pairs {len(diffs)}")
for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
    flag = "P1" if k in p1 else "--"
    print(f"{flag}\t{sum(c.values())}\t{k} = {v}\t| prior: " + "; ".join(f"{p} ({n})" for p, n in c.items()) + f"\t[{src[(k, v)]}]")
print("## differs from sample")
for (k, v, sv), n in sdiff.most_common():
    print(f"{n}\t{k} = {v}\t| sample: {sv}")
