"""Per-segment presence of a term: for each headword (case-insensitive) and term, in how many of the segments where the
headword occurs (keyword map) the pi-7 Burmese segment contains the term (« … » = a gap of up to 80 characters).
usage: segcheck.py hw=term [hw=term ...]      or   segcheck.py --tsv file.tsv   (lines hw|i <TAB> term ...; # ignored)
Prints: hw | term | segments with the term / segments of the headword | up to 4 ids without it."""
import re, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
M = B / "AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("---"): buf.append(line)
            m = ID.search(line)
            if m: out[m.group(1)] = " ".join(buf); buf = []
    return out


def rx(term):
    return re.compile(r"\s*.{0,80}?\s*".join(re.escape(x.strip()) for x in term.split("…")))


def main(pairs):
    R = segs(B / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters")
    want = {hw.lower() for hw, _ in pairs}
    ids = collections.defaultdict(list)
    for l in M.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\[([^\]]+)\] (.*)", l)
        if not m: continue
        ks = {p.partition("=")[0].lower() for p in m.group(2).split(", ")}
        for k in ks & want: ids[k].append(m.group(1))
    for hw, t in pairs:
        r = rx(t); ii = ids[hw.lower()]
        miss = [i for i in ii if not r.search(R.get(i, ""))]
        print(f"{hw} | {t} | {len(ii) - len(miss)}/{len(ii)} | {' '.join(miss[:4])}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--tsv":
        pairs = []
        for l in pathlib.Path(a[1]).read_text(encoding="utf-8").splitlines():
            if not l.strip() or l.startswith("#"): continue
            k, t = l.split("\t")[:2]
            pairs.append((k.rsplit("|", 1)[0], t))
    else:
        pairs = [tuple(x.split("=", 1)) for x in a]
    main(pairs)
