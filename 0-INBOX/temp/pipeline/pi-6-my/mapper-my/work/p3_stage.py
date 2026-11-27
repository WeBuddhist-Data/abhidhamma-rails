"""phase 3 staging: run the four mapping scripts (map_sample, map_g1, map_g2, map_g3, in that order), copy the 44
*.mapped.md into work/stages/<name>/, and list every value that differs from the previous stage (or from a given
stage) as TSV rows: segment, position, keyword, old, new.
usage: p3_stage.py NAME [--prev PREVNAME] [--norun]
  PREVNAME defaults to the last stage in work/stages/order.txt (phase2 = work/phase2-mapped)."""
import sys
import shutil
import pathlib
import subprocess

D = pathlib.Path(__file__).resolve().parent.parent
W = D / "work"
ST = W / "stages"
PY = "/opt/homebrew/Caskroom/miniconda/base/bin/python3"
SCRIPTS = ["map_sample.py", "map_g1.py", "map_g2.py", "map_g3.py"]


def stage_dir(name):
    return W / "phase2-mapped" if name == "phase2" else ST / name


def read(dirp):
    out = {}
    for f in sorted(dirp.glob("*.mapped.md")):
        for l in f.read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for i, kv in enumerate(rest.split(", ")):
                k, v = kv.split("=", 1)
                out[(sid, i)] = (k, v)
    return out


def diff(a, b):
    rows = []
    for key in sorted(b, key=lambda x: (x[0], x[1])):
        if key not in a:
            rows.append((key[0], key[1], b[key][0], "?", b[key][1]))
        elif a[key][1] != b[key][1]:
            rows.append((key[0], key[1], b[key][0], a[key][1], b[key][1]))
    return rows


def main():
    args = sys.argv[1:]
    name = args[0]
    order = (ST / "order.txt").read_text().split() if (ST / "order.txt").exists() else ["phase2"]
    prev = order[-1] if order[-1] != name else (order[-2] if len(order) > 1 else "phase2")
    if "--prev" in args:
        prev = args[args.index("--prev") + 1]
    if "--norun" not in args:
        for s in SCRIPTS:
            r = subprocess.run([PY, "-I", "-X", "utf8", str(D / s)], cwd=str(D), capture_output=True, text=True)
            (W / f"p3_{name}_{s[:-3]}.txt").write_text(r.stdout + r.stderr, encoding="utf-8")
            if r.returncode:
                print("ERROR in", s, r.stderr[-3000:])
                sys.exit(1)
        out = ST / name
        out.mkdir(parents=True, exist_ok=True)
        for f in D.glob("*.mapped.md"):
            shutil.copy(f, out / f.name)
        if name not in order:
            order.append(name)
            ST.mkdir(exist_ok=True)
            (ST / "order.txt").write_text("\n".join(order) + "\n")
    rows = diff(read(stage_dir(prev)), read(stage_dir(name)))
    (W / f"p3_diff_{name}.tsv").write_text("".join("\t".join(map(str, r)) + "\n" for r in rows), encoding="utf-8")
    print(f"stage {name} vs {prev}: {len(rows)} changed values")
    import collections
    c = collections.Counter((r[2], r[3], r[4]) for r in rows)
    for (k, o, n), x in c.most_common():
        print(f"   {x:4d}  {k}: {o}  ->  {n}")
    for s in SCRIPTS:
        t = (W / f"p3_{name}_{s[:-3]}.txt").read_text(encoding="utf-8") if (W / f"p3_{name}_{s[:-3]}.txt").exists() else ""
        bad = [l for l in t.splitlines() if "UNMAPPED" in l or "FAIL" in l or "PUNCT" in l
               or ("presence-fails" in l and "presence-fails 0" not in l) or ("bad [" in l and "bad []" not in l)
               or ("unmapped" in l and "unmapped 0" not in l and not l.startswith("TOTAL"))]
        for l in bad[:30]:
            print("   !!", s, l)


if __name__ == "__main__":
    main()
