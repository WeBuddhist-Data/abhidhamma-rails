"""phase 3 task 4: the three checks of the phase-1 brief over all 44 chapters: (1) the brief's own preservation
one-liner per chapter (must print bad []), (2) presence (0 failures; every chunk not literal is matched by a named
ending rule), (3) no «, » / «၊» / « / » inside a value."""
import sys
import pathlib
import subprocess
import collections
D = pathlib.Path(__file__).resolve().parent.parent
ROOT = D.parents[4]
sys.path.insert(0, str(D))
import map6_rules as R  # noqa: E402
PY = "/opt/homebrew/Caskroom/miniconda/base/bin/python3"
CMD = ("import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-6-my/mapper-my');ch='CH';a=[l.split('] ',1) for l in "
       "(d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in "
       "(d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];"
       "bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in "
       "y.split(', ')]];print(ch,'lines',len(a),'bad',bad)")
tot = collections.Counter()
rules = collections.Counter()
for ch in R.CHAPTERS:
    out = subprocess.run([PY, "-I", "-X", "utf8", "-c", CMD.replace("CH", ch)], cwd=str(ROOT), capture_output=True,
                         text=True).stdout.strip()
    n, bad, fails, punct, ruled = R.verify_file(ch)
    nde = sum(v == R.NONE for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()
              for v in [kv.split("=", 1)[1] for kv in l.split("] ", 1)[1].split(", ")])
    uses = sum(len(l.split("] ", 1)[1].split(", ")) for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines())
    rules.update(r for *_, r in ruled)
    ok = out.endswith("bad []") and not bad and not fails and not punct
    print(f"{ch}\t{out}\tuses {uses}\tpresence-fails {len(fails)}\tpunct {len(punct)}\tNDE {nde}\tending-rule {len(ruled)}"
          f"\t{'OK' if ok else 'FAIL'}")
    tot.update(lines=n, uses=uses, bad=len(bad), fails=len(fails), punct=len(punct), nde=nde, ruled=len(ruled),
               ok=int(ok))
print("TOTAL", dict(tot))
print("ending rules", dict(rules.most_common()))
