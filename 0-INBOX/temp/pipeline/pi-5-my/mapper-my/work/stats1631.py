"""numbers for notes-ch16-31.md: sources, (no direct equivalent), values that differ from pi-1 … pi-4 / ch1."""
import sys, pathlib, importlib.util, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map5_rules as R, map_ch1 as C1
spec = importlib.util.spec_from_file_location("m1631", HERE / "map_ch16-31.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
src = collections.Counter(); same = new = diff = 0; uses = 0
D = collections.defaultdict(lambda: [collections.Counter(), set(), None])
nde = []
for ch in m.CHAPTERS:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    my = R.burmese(ch)
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1); uses += 1
            src[M.SRC.get((sid, k), "?")] += 1
            if v == R.NONE: nde.append((ch, sid, k))
            pv = R.prev_vals(k); c1 = R.table_get(C1.T_CH1, k)
            ref = set(x for x in pv if x != R.NONE)
            if isinstance(c1, str) and not c1.startswith("@") and c1 != R.NONE: ref.add(c1)
            if not ref: new += 1; continue
            if v in ref: same += 1; continue
            diff += 1
            e = D[k]; e[0][v] += 1; e[1].add(ch.split("-")[0])
            present = [x for x in ref if R.presence(x, my[sid])[0]]
            e[2] = (sorted(ref, key=lambda x: -pv.get(x, 0))[:2], bool(present))
print("uses", uses, "same", same, "new", new, "diff", diff, "keywords diff", len(D))
print("sources", src.most_common())
print("NONE", len(nde))
for x in nde: print("  N", *x)
for k, (vals, chs, (ref, pres)) in sorted(D.items(), key=lambda kv: -sum(kv[1][0].values())):
    print(f"D|{k}|{' ; '.join(f'{v} ({n})' for v, n in vals.most_common())}|{' ; '.join(ref)}|{'present' if pres else 'absent'}|{','.join(sorted(chs, key=int))}")
