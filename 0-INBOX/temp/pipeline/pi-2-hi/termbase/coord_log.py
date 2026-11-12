"""Coordinator: write coord-log.tsv (key, old term, new term, file, reason) by diffing the current decision files
(decisions-coord.tsv and the part files) against backup-pre-coord/ and the senses-file candidates."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_pi2 as T

HERE = pathlib.Path(__file__).parent


def load(p):
    d = {}
    if p.exists():
        for l in p.read_text(encoding="utf-8-sig").splitlines():
            if l.strip() and not l.startswith("#"):
                x = l.split("\t")
                d[x[0].strip()] = (x[1].strip(), x[2].strip() if len(x) > 2 else "")
    return d


ss = dict(T.senses())
rows = ["key\told term\tnew term\tfile\treason"]
for name in ("decisions-part1.tsv", "decisions-part2.tsv", "decisions-part3.tsv", "decisions-coord.tsv"):
    new, old = load(HERE / name), load(HERE / "backup-pre-coord" / name)
    for k, (t, r) in new.items():
        if k in old and old[k][0] == t:
            continue
        if k in old:
            o = old[k][0]
        else:
            hw, i = k.rsplit("|", 1)
            o = " / ".join(ss[hw][int(i)][1])
        rows.append(f"{k}\t{o}\t{t}\t{name}\t{r}")
(HERE / "coord-log.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print(len(rows) - 1, "changes logged")
