"""Termbase adherence for the Burmese pi-2 track (Burmese version of pi-4-mr/rails/adherence_loose.py).

A keyword of a segment passes if, for ANY of its termbase senses, the term occurs in that segment. A term occurs if
each of its content chunks (the space-separated words of the term, «…» and «–» dropped) occurs as a substring of
the segment, after stripping from the end of the chunk the particles the mapping rules strip
(၏ ကို ၌ တွင် နှင့် မှ ဖြင့် အား သို့ သည် က များ တို့) and the attributive / verbal endings
(သော သည် ၍ ခြင်း မှု), repeatedly, as long as at least two code points remain. A chunk that is only a particle
is dropped.
usage: adherence_my.py <keywords-pali.md> <termbase.md> <split_dir> [report]
Writes the report to stdout, or to [report] when given. First line: «checked N; misses M».
"""
import pathlib
import re
import sys
import unicodedata

PARTICLES = ["၏", "ကို", "၌", "တွင်", "နှင့်", "မှ", "ဖြင့်", "အား", "သို့", "သည်", "က", "များ", "တို့"]
ENDINGS = ["သော", "သည်", "၍", "ခြင်း", "မှု"]
STRIP = sorted(set(PARTICLES + ENDINGS), key=len, reverse=True)
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
NFC = lambda s: unicodedata.normalize("NFC", s)


def parse_termbase(path):
    """headword (lower) -> list of Burmese terms (one per sense)."""
    tb = {}
    for l in open(path, encoding="utf-8"):
        m = re.match(r"^(.*?): \{(.*)\}\s*$", l.rstrip("\n"))
        if not m:
            continue
        senses, cur = [], ""
        for part in m.group(2).split("; "):  # a sense is «gloss: term»; a «; » inside a gloss is re-joined
            cur = part if not cur else cur + "; " + part
            if ": " in cur:
                senses.append(NFC(cur.rsplit(": ", 1)[1]).strip())
                cur = ""
        tb[NFC(m.group(1)).lower()] = senses
    return tb


def stem(chunk):
    changed = True
    while changed:
        changed = False
        for s in STRIP:
            if chunk.endswith(s) and len(chunk) - len(s) >= 2:
                chunk = chunk[: -len(s)]
                changed = True
                break
    return chunk


def chunks(term):
    out = []
    for w in re.split(r"[\s၊။…–\-“”‘’()]+", term):
        if not w or w in STRIP:
            continue
        out.append(stem(w))
    return out


def occurs(term, text):
    cs = chunks(term)
    return bool(cs) and all(c in text for c in cs)


def segments(d, chs=()):
    segs = {}
    for p in sorted(pathlib.Path(d).glob("*.md")):
        if chs and p.name not in chs:
            continue
        buf = []
        for l in NFC(p.read_text(encoding="utf-8")).splitlines():
            if not l.strip():
                continue
            buf.append(l)
            m = ID.search(l)
            if m:
                segs[m.group(1)] = " ".join(buf)
                buf = []
    return segs


def run(kw_path, tb_path, d):
    tb, segs = parse_termbase(tb_path), segments(d)
    miss, n = [], 0
    for l in open(kw_path, encoding="utf-8"):
        m = re.match(r"^\[([^\]]+)\] (.*)$", NFC(l.strip()))
        if not m or m.group(1) not in segs:
            continue
        text = segs[m.group(1)]
        for kw in m.group(2).split(", "):
            terms = tb.get(kw.strip().lower())
            if not terms:
                continue
            n += 1
            if not any(occurs(t, text) for t in terms):
                miss.append((m.group(1), kw.strip(), " | ".join(terms)))
    return n, miss


if __name__ == "__main__":
    kw_path, tb_path, d = sys.argv[1:4]
    n, miss = run(kw_path, tb_path, d)
    out = [f"checked {n}; misses {len(miss)}"] + ["   " + "\t".join(x) for x in miss]
    txt = "\n".join(out) + "\n"
    if len(sys.argv) > 4:
        pathlib.Path(sys.argv[4]).write_text(txt, encoding="utf-8")
        print(out[0])
    else:
        sys.stdout.write(txt)
