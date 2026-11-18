"""Checks for the Vietnamese pi-1 zero-shot sample.

usage: python -I -X utf8 verify_vi.py
- block IDs of ch2-01-sample.md equal those of the Pāli slice, in order
- no CR, no double blank lines, NFC, no em dash, no ":-"
- outside variant brackets: no Pāli letters (ā ī ū ṃ ṅ ñ ṭ ḍ ṇ ḷ) and no f / j / w / z (not in the Vietnamese alphabet)
"""
import pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters"
PALI_SLICE = HERE.parent / "pi-1-ru" / "ref" / "ch2-01-pali-1-122.md"
FILES = [VI / "preamble.md", VI / "1-matika.md", HERE / "ch2-01-sample.md"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def ids(p):
    return [m.group(1) for l in p.read_text(encoding="utf-8").splitlines() if (m := ID.search(l))]


bad = 0
a, b = ids(PALI_SLICE), ids(HERE / "ch2-01-sample.md")
print("sample ids", len(b), "pali ids", len(a), "equal" if a == b else "DIFFER")
bad += a != b
for f in FILES:
    raw = f.read_bytes()
    t = raw.decode("utf-8")
    errs = []
    if b"\r" in raw:
        errs.append("CR")
    if "\n\n\n" in t:
        errs.append("double blank line")
    if unicodedata.normalize("NFC", t) != t:
        errs.append("not NFC")
    if "—" in t or ":-" in t:
        errs.append("em dash or :-")
    for n, line in enumerate(t.splitlines(), 1):
        body = ID.sub("", re.sub(r"\[[^\]]*\]", "", line))
        m = FOREIGN.search(body)
        if m:
            errs.append(f"line {n}: foreign letter {m.group(0)!r} in {body[max(0, m.start() - 30):m.start() + 30]!r}")
    print(f.name, "OK" if not errs else errs[:5])
    bad += bool(errs)
print("ALL OK" if not bad else f"{bad} problem(s)")
