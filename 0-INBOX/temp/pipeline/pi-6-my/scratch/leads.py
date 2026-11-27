"""Scratch: every answer lead (Pāli before tesaṃ / tāsaṃ / tattha) with its Burmese lead (up to the first «အား»);
prints leads whose identical Pāli has more than one Burmese, and (with -m REGEX) every lead matching REGEX."""
import pathlib, re, sys, collections
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"
MD = ROOT / ("AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters" if "--bk" not in sys.argv else "x")
if "--bk" in sys.argv: MD = HERE / "harmonise-backup/chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def psplit(l):
    l = ID.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00").replace("? ", "?\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?]) (?=\S)", l) if s]
def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]
LEAD = re.compile(r"^(?:\(\w+\) )?(?P<who>.+?) (?P<pro>tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tassa tattha|tassa)(?= )(?! (?:\w+ant[āī]naṃ|cittassa|(?:\S+ )?\S+kkhaṇe|tattha \w+ant[āī]naṃ)\b)")
D = collections.defaultdict(collections.Counter); W = collections.defaultdict(list)
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        ps, bs = psplit(x), bsplit(y)
        if len(ps) != len(bs): continue
        for s, t in zip(ps, bs):
            m = LEAD.match(s)
            if not m or re.match(r"(?i)(yassa|yattha|yo|ya[mṃ]|yā)\b", m["who"]): continue
            mm = re.search("အား(?!လုံး)", t); k = mm.start() if mm else -1
            if k < 0: continue
            who = m["who"]; who = who[0].lower() + who[1:]
            bl = t[:k + 3]
            D[(who, m["pro"])][bl] += 1
            W[(who, m["pro"], bl)].append(f"{p.name[:5]}:{i}")
rx = re.compile(sys.argv[sys.argv.index("-m") + 1]) if "-m" in sys.argv else None
nd = 0
for (who, pro), c in sorted(D.items()):
    if rx and not rx.search(who): continue
    if len(c) > 1 or rx:
        if len(c) > 1: nd += 1
        print(f"{who} | {pro}")
        for bl, n in c.most_common():
            print(f"   {n}x {bl}   {W[(who, pro, bl)][:6]}")
print("distinct leads", len(D), "with >1 Burmese", nd)
