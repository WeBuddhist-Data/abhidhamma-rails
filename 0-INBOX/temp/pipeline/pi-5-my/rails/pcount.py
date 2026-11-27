"""Inspection helper (read only): count a Pāli regex and a Burmese regex over aligned rails lines; list lines where the
Pāli matches with the Burmese count. usage: pcount.py <pāli regex> <burmese regex> [--zs] [--show]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT = ROOT / ("AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters" if "--zs" in sys.argv else "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters")
N = lambda s: unicodedata.normalize("NFC", s)
rp, rm = re.compile(sys.argv[1]), re.compile(sys.argv[2])
tp = tm = tmall = 0
for p in sorted(PALI.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n")
    ml = N((OUT / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (a, b) in enumerate(zip(pl, ml)):
        np_ = len(rp.findall(a)); nm = len(rm.findall(b))
        tmall += nm
        if np_ or nm:
            tp += np_; tm += nm if np_ else 0
            if "--show" in sys.argv or (np_ != nm):
                print(f"{p.name[:-3]}:{k+1}\tP {np_}\tB {nm}")
print(f"total Pāli {tp}, Burmese on those lines {tm}, Burmese anywhere {tmall}")
