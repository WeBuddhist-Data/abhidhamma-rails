"""Scratch B5: per aligned sentence, Pāli finite verbs (sg / pl) vs Burmese «ကြ» count; print mismatch classes."""
import pathlib, re, sys, collections
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"
MD = HERE / "harmonise-backup/chapters" if "--bk" in sys.argv else ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def psplit(l):
    l = ID.sub("", l)
    l = re.sub(r"\[[^\]]*\]", "", l)
    return [s for s in re.split(r"(?<=[.?]) (?=\S)", l) if s]
def bsplit(l):
    l = re.sub(r"\[[^\]]*\]", "", l)
    return [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]
ROOTS = r"(?:uppajj|nirujjh|anuse|anusen|pajah|ppajah|parijān|bhāve|bhāvess|bhāvent|sacchikaro|sacchikar|paṭilabh|upapajj|cav|parinibbāy)"
PL = re.compile(rf"\b[Nn]?a?(?:{ROOTS})\w*(?:anti|enti|onti|iṃsu|ssanti|nti|antī|entī|ontī|ssantī)(?:ti)?\b")
SG = re.compile(rf"\b[Nn]?a?(?:{ROOTS})\w*(?:ati|eti|oti|ittha|issati|essati|āti|āsi|ī)(?:ti)?\b")
c = collections.Counter(); ex = collections.defaultdict(list)
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        ps, bs = psplit(x), bsplit(y)
        if len(ps) != len(bs): continue
        for s, t in zip(ps, bs):
            s2 = re.sub(r"\b(?:upapajjitvā|upapajjantānaṃ|upapajjantīnaṃ|cavantānaṃ|cavantīnaṃ|parinibbantānaṃ|parinibbāyissanti|paṭilabhissanti|uppajjamānaṃ|nirujjhamānaṃ|uppajjamānanti|nirujjhamānanti)\b", "", s)
            npl, nsg = len(PL.findall(s2)), len(SG.findall(s2))
            nk = len(re.findall("ကြ(?![\u102B-\u103E]|[\u1000-\u1021]\u103A)", t))
            if npl + nsg == 0: continue
            key = (p.name[:4], "pl" if npl and not nsg else "sg" if nsg and not npl else "mix", npl, nk)
            if nk != npl:
                c[key] += 1; ex[key].append((i, s[:160], t[:200]))
for k, n in sorted(c.items()):
    print(n, k); [print("    ", e) for e in ex[k][:2]]
