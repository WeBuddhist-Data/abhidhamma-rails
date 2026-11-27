"""Inspection helper (read only): Burmese regex in context, per segment id (zero-shot; --rails for the rails).
usage: kw.py REGEX [--rails] [--w N]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa
d = "rails" if "--rails" in sys.argv else "zeroshot"
S = A.segments(ROOT / f"AI_translation/burmese/pi-4-burmese-plain-{d}_split_chapters")
w = int(sys.argv[sys.argv.index("--w") + 1]) if "--w" in sys.argv else 40
rx = re.compile(unicodedata.normalize("NFC", sys.argv[1]))
n = 0
for i, t in S.items():
    for m in rx.finditer(t):
        n += 1
        print(f"{i}\t…{t[max(0, m.start() - w):m.end() + w]}…")
print("total", n)
