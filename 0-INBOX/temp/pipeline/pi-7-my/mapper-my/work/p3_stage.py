"""pi-7 phase 3 staging (model: pi-6-my/mapper-my/work/p3_stage.py, copied, not imported): run the seven mapping
scripts (map_sample, map_g1 … map_g6, in that order), copy the 75 *.mapped.md into work/stages/<name>/, and list every
value that differs from the previous stage (or from a given stage) as TSV rows: segment, position, keyword, old, new.
usage: p3_stage.py NAME [--prev PREVNAME] [--norun] [--only map_gN.py,…]
  PREVNAME defaults to the last stage in work/stages/order.txt (phase2 = work/phase2-mapped)."""
import sys
import shutil
import pathlib
import subprocess
import collections

D = pathlib.Path(__file__).resolve().parent.parent
W = D / "work"
ST = W / "stages"
PY = "/opt/homebrew/Caskroom/miniconda/base/bin/python3"
SCRIPTS = ["map_sample.py", "map_g1.py", "map_g2.py", "map_g3.py", "map_g4.py", "map_g5.py", "map_g6.py"]


def stage_dir(name):
    return W / "phase2-mapped" if name == "phase2" else ST / name


def read(dirp):
    out = {}
    for f in sorted(pathlib.Path(dirp).glob("*.mapped.md")):
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
    scripts = SCRIPTS
    if "--only" in args:
        scripts = args[args.index("--only") + 1].split(",")
    if "--norun" not in args:
        for s in scripts:
            r = subprocess.run([PY, "-I", "-X", "utf8", str(D / s)], cwd=str(D), capture_output=True, text=True)
            (W / f"p3_{name}_{s[:-3]}.txt").write_text(r.stdout + r.stderr, encoding="utf-8")
            if r.returncode:
                print("ERROR in", s, r.stderr[-3000:])
                sys.exit(1)
        out = ST / name
        out.mkdir(parents=True, exist_ok=True)
        for f in sorted(D.glob("*.mapped.md")):
            shutil.copy(f, out / f.name)
        if name not in order:
            order.append(name)
            ST.mkdir(exist_ok=True)
            (ST / "order.txt").write_text("\n".join(order) + "\n")
    rows = diff(read(stage_dir(prev)), read(stage_dir(name)))
    (W / f"p3_diff_{name}.tsv").write_text("".join("\t".join(map(str, r)) + "\n" for r in rows), encoding="utf-8")
    print(f"stage {name} vs {prev}: {len(rows)} changed values")
    c = collections.Counter((r[2], r[3], r[4]) for r in rows)
    for (k, o, n), x in c.most_common():
        print(f"   {x:4d}  {k}: {o}  ->  {n}")
    for s in scripts:
        p = W / f"p3_{name}_{s[:-3]}.txt"
        t = p.read_text(encoding="utf-8") if p.exists() else ""
        bad = [l for l in t.splitlines() if "UNMAPPED" in l or "FAIL" in l or "PUNCT" in l or "Traceback" in l
               or ("presence-fails" in l and "presence-fails 0" not in l)
               or ("presence failures" in l and "presence failures 0" not in l)
               or ("bad [" in l and "bad []" not in l)
               or (" unmapped " in l and "unmapped 0" not in l and not l.startswith(("TOTAL", "total")))]
        for l in bad[:30]:
            print("   !!", s, l)


if __name__ == "__main__":
    main()
