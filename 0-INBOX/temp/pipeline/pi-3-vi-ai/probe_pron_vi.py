"""Probe: pronoun after an association verb in relative clauses («gắn liền với nó / chúng»).
For each Pāli 'HEAD ye dhammā (sampayuttā|vippayuttā)' (HEAD = the word before 'ye', 'tehi dhammehi' = plural),
expected pronoun: plural if HEAD ends in -ehi/-ūhi/-īhi (instrumental plural), else singular.
Compares with the Vietnamese pronoun sequence on the aligned line.
usage: python -I -X utf8 probe_pron_vi.py [--all]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vi_common import PARTS, segments, short

PREL = re.compile(r"(\S+) ye(?: dhammā)? (sampayuttā|vippayuttā)")
VREL = re.compile(r"(?:không )?gắn liền với (nó|chúng)\b")
stat = collections.Counter()
for part in PARTS:
    for sid, ps, vs in segments(part):
        for p, v in zip(ps, vs):
            heads = PREL.findall(p)
            if not heads:
                continue
            exp = ["chúng" if re.search(r"(ehi|ūhi|īhi)$", h) else "nó" for h, _ in heads]
            got = VREL.findall(v)
            ok = exp == got
            stat[(short(part), ok)] += 1
            if not ok or "--all" in sys.argv:
                print(f"{short(part)} ^{sid}: heads={[h for h, _ in heads]} exp={exp} got={got}")
print(dict(stat))
