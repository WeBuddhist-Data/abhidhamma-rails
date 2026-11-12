"""Print, per segment of a chapter, the keywords still unresolved / absent under the current tables
(listed presence exceptions skipped), with the Hindi (and Pāli) for context (ch12 mapper helper).

usage: python -I -X utf8 seg_12_hi.py <chapter> <from-index> <to-index> [brief|hi|pi]
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, present, NDE  # noqa
import common_10_12_13_14_hi as C  # noqa

ch, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mode = sys.argv[4] if len(sys.argv) > 4 else "hi"
hi, pi = read_hindi(ch), read_pali(ch)
allowed = C.ALLOWED.get(ch, {})
for i, (bid, kws) in enumerate(read_keywords(ch)):
    if not a <= i < b:
        continue
    bad = []
    for kw in kws:
        try:
            v = C.resolve(ch, bid, kw, kws, hi.get(bid))
        except KeyError:
            bad.append(f"{kw}=?")
            continue
        if (v != NDE and not present(v, hi.get(bid, "")) and (bid, kw) not in allowed
                and not C.inflect_variant(v, hi.get(bid, ""))):
            bad.append(f"{kw}=!{v}")
    if not bad:
        continue
    print(f"=== [{i}] {bid}")
    if mode == "pi":
        print("PI:", pi.get(bid))
    if mode in ("pi", "hi"):
        print("HI:", hi.get(bid))
    print("NEED:", ", ".join(bad))
    print()
