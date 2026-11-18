"""Checks for Vietnamese rails outputs (any book).

usage: python -I -X utf8 verify_rails_vi.py <pali_file> <vietnamese_file> [<pali_file> <vietnamese_file> ...]
Per pair: block IDs equal and in the same order; per-segment non-empty line counts equal; no CR; no double blank
lines; NFC; no em dash; no ":-"; no «chánh niệm»; outside [...] brackets no Pāli letters (ā ī ū ṃ ṅ ñ ṭ ḍ ṇ ḷ)
and no f / j / w / z (not in the Vietnamese alphabet). Prints OK or the problems per pair.
"""
import re
import sys
import unicodedata

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def segs(text):
    out, n = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            out.append((m.group(1), n))
            n = 0
    return out


args = sys.argv[1:]
if not args or len(args) % 2:
    sys.exit(__doc__)
bad_total = 0
for pf, vf in zip(args[::2], args[1::2]):
    p = open(pf, encoding="utf-8-sig").read()
    raw = open(vf, "rb").read()
    v = raw.decode("utf-8-sig")
    probs = []
    sp, sv = segs(p), segs(v)
    if [x[0] for x in sp] != [x[0] for x in sv]:
        probs.append(f"block IDs differ (pali {len(sp)}, vi {len(sv)})")
    else:
        for (i, a), (_, b) in zip(sp, sv):
            if a != b:
                probs.append(f"^{i}: {a} Pāli lines vs {b} Vietnamese lines")
    if b"\r" in raw:
        probs.append("CR found")
    if "\n\n\n" in v:
        probs.append("double blank line")
    if unicodedata.normalize("NFC", v) != v:
        probs.append("not NFC")
    if "—" in v:
        probs.append("em dash")
    if ":-" in v:
        probs.append("':-'")
    if "chánh niệm" in v.lower():
        probs.append("«chánh niệm»")
    for n, line in enumerate(v.splitlines(), 1):
        body = ID.sub("", re.sub(r"\[[^\]]*\]", "", line))
        if FOREIGN.search(body):
            probs.append(f"line {n}: foreign letter outside brackets: {FOREIGN.search(body).group(0)!r}")
            if len(probs) > 30:
                break
    print(vf, "OK" if not probs else "PROBLEMS")
    for x in probs[:30]:
        print("  ", x)
    bad_total += bool(probs)
sys.exit(1 if bad_total else 0)
