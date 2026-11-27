"""phase 3 helper: count / show the Burmese of all 75 chapters around a regex. usage: p3_grep.py REGEX [--show N] [--win W]"""
import sys, re, pathlib
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
import map7_rules as R
a = sys.argv[1:]
show = int(a[a.index("--show") + 1]) if "--show" in a else 10
win = int(a[a.index("--win") + 1]) if "--win" in a else 40
pali = "--pali" in a
rx = re.compile(a[0])
n = 0
for ch in R.chapters():
    segs = R.pali(ch) if pali else R.burmese(ch)
    for sid, t in segs.items():
        for m in rx.finditer(t):
            n += 1
            if n <= show:
                print(f"^{sid}: …{t[max(0, m.start() - win):m.end() + win]}…")
print("matches", n)
