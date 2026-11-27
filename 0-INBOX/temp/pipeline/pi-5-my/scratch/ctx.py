"""scratch: for Pāli regex, print the Burmese sentence(s) of the matching Pāli sentences when the line splits evenly, else the whole Burmese line (cut). usage: ctx.py REGEX [--max N]"""
import pathlib, re, sys, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
PD = ROOT / "AI_translation/pali/pi-5_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def psplit(l):
    l = ID.sub("", l); l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]
def bsplit(l): return [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]
a = sys.argv[1:]; mx = 40
if "--max" in a: i = a.index("--max"); mx = int(a[i+1]); del a[i:i+2]
rx = re.compile(a[0]); cnt = collections.Counter(); where = collections.defaultdict(list)
key = lambda p: (int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)
for p in sorted(PD.glob("*.md"), key=key):
    if p.suffix != ".md": continue
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (MD / p.name).read_text(encoding="utf-8").split("\n")), 1):
        if not rx.search(x): continue
        ps, bs = psplit(x), bsplit(y)
        if len(ps) == len(bs):
            for s, t in zip(ps, bs):
                if rx.search(s): cnt[(s, t)] += 1; where[(s, t)].append(f"{p.name.split('-')[0]}:{i}")
        else:
            cnt[("LINE " + x[:150], y[:400])] += 1; where[("LINE " + x[:150], y[:400])].append(f"{p.name.split('-')[0]}:{i}")
for k, (s, t) in enumerate(sorted(cnt, key=lambda k: where[k][0].split(":")[0].zfill(3))):
    if k >= mx: break
    print(f"[{cnt[(s, t)]}x {' '.join(where[(s, t)][:6])}]\n  P: {s[:300]}\n  M: {t[:500]}")
print(len(cnt), "distinct")
