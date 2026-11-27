"""phase 3 S1 review: every stem-fallback value of the three scripts.
usage: stemlist.py OUT.tsv — chapter, segment, keyword, value, the pool keywords of the same stem that carry the
value (with counts), the Pāli word around the keyword"""
import sys, re, pathlib, importlib.util
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
import map5_rules as R
rows = []
for name in ("map_ch1", "map_ch2-15", "map_ch16-31"):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), D / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    M = m.mapper()
    for ch in m.CHAPTERS:
        lines = M.map_chapter(ch)[0]
        for l in lines:
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                if M.SRC.get((sid, k)) == "stem":
                    rows.append((ch, sid, k, v, M.stem.pool if M.stem else {}))
out = []
for ch, sid, k, v, pool in rows:
    src = sorted(((kk, c[v]) for kk, c in pool.items() if v in c and " " not in kk
                  and kk[:max(4, len(k) - 4)] == R.low(k)[:max(4, len(k) - 4)]), key=lambda x: -x[1])[:4]
    pa = R.strip_brackets(R.pali(ch)[sid])
    mm = re.search(r"\S*" + re.escape(R.low(k)[:max(4, len(k) - 3)]) + r"\S*", pa, flags=re.I)
    out.append("\t".join([ch, sid, k, v, " ".join(f"{a}({b})" for a, b in src), mm.group(0) if mm else "-"]))
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n", encoding="utf-8")
print("stem uses", len(out), "unique keyword=value", len({(r.split("\t")[2], r.split("\t")[3]) for r in out}))
