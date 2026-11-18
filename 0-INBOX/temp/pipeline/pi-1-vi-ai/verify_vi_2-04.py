"""Checks for the Vietnamese pi-1 zero-shot part 2-04 (copy of verify_vi_2-03.py for this part).

usage: python -I -X utf8 verify_vi_2-04.py
- block IDs and per-segment line counts equal the Pāli part
- no CR, no double blank lines, NFC, no em dash, no ":-", no «chánh niệm»
- per line: same number of "–" and "?" as the Pāli line
- outside variant brackets: no Pāli letters (ā ī ū ṃ ṅ ñ ṭ ḍ ṇ ḷ) and no f / j / w / z (not in the Vietnamese alphabet)
"""
import pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
PARTS = ["2-04-cittuppadakandam.md"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def segs(p):
    out, n = [], 0
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        n += 1
        m = ID.search(l)
        if m:
            out.append((m.group(1), n))
            n = 0
    return out


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


bad = 0
for name in PARTS:
    f = VI / name
    raw = f.read_bytes()
    t = raw.decode("utf-8")
    errs = []
    if segs(PALI / name) != segs(f):
        errs.append("block IDs / segment line counts differ from the Pāli")
    if b"\r" in raw:
        errs.append("CR")
    if "\n\n\n" in t:
        errs.append("double blank line")
    if unicodedata.normalize("NFC", t) != t:
        errs.append("not NFC")
    if "—" in t or ":-" in t:
        errs.append("em dash or :-")
    if "chánh niệm" in t.lower():
        errs.append("chánh niệm")
    if "seed" in t.lower():
        errs.append("forbidden word")
    if "pe…" in t:
        errs.append("untranslated …pe…")
    for n, (p, line) in enumerate(zip(nonempty(PALI / name), nonempty(f)), 1):
        if p.count("–") != line.count("–") or p.count("?") != line.count("?"):
            errs.append(f"line {n}: dash/question-mark count differs")
        body = ID.sub("", re.sub(r"\[[^\]]*\]", "", line))
        m = FOREIGN.search(body)
        if m:
            errs.append(f"line {n}: foreign letter {m.group(0)!r} in {body[max(0, m.start() - 30):m.start() + 30]!r}")
    print(name, len(segs(f)), "segments", "OK" if not errs else errs[:5])
    bad += bool(errs)
print("ALL OK" if not bad else f"{bad} problem(s)")
