"""Print, for each REVIEW / UNRESOLVED headword of gen_decisions_my.py output: Marathi ENGLISH tags only,
and the Burmese values with counts and example ids from agg. usage: show_review_my.py agg.tsv gen-out.txt"""
import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gen_decisions_my as g
agg = {}
for l in open(sys.argv[1], encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    agg[c[0]] = c[2]
mr = g.read_mr_tags()
hws = []
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('  '):
        hw = l[2:].split('\t')[0] if '\ttags=' in l else l[2:].rsplit(': ', 1)[0]
        # REVIEW line "  hw: v / v"
        if '\ttags=' not in l:
            hw = l[2:].split(': ')[0]
            # headwords may contain ': '? no
        hws.append(hw)
for hw in hws:
    print('==', hw, '| MR tags:', mr.get(hw))
    for it in agg[hw].split(' | '):
        print('     ', it)
