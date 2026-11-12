"""Scratch viewer for 6-paticcasamuppadavibhango.

usage: python -I -X utf8 peek_6-paticcasamuppadavibhango_hi.py ids            -> id, #lines, first 160 chars of Pāli
       python -I -X utf8 peek_6-paticcasamuppadavibhango_hi.py seg ID [N]     -> Pāli/Hindi line N (all if omitted) + keywords
       python -I -X utf8 peek_6-paticcasamuppadavibhango_hi.py grep REGEX     -> Hindi lines (id:line#) matching REGEX
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali  # noqa: E402

CH = "6-paticcasamuppadavibhango"
P, H = read_pali(CH), read_hindi(CH)
K = dict(read_keywords(CH))
cmd = sys.argv[1]
if cmd == "ids":
    for bid, kws in read_keywords(CH):
        p = P.get(bid, "")
        print(bid, len(p.splitlines()), len(kws), p[:160].replace("\n", " / "))
elif cmd == "seg":
    bid = sys.argv[2]
    pl, hl = P[bid].splitlines(), H[bid].splitlines()
    rng = [int(sys.argv[3])] if len(sys.argv) > 3 else range(len(pl))
    for i in rng:
        print(f"--- {i}\nPI: {pl[i]}\nHI: {hl[i]}")
    print("KW:", ", ".join(K[bid]))
elif cmd == "grep":
    rx = re.compile(sys.argv[2])
    for bid, t in H.items():
        for i, l in enumerate(t.splitlines()):
            for m in rx.finditer(l):
                print(bid, i, m.group(0))
