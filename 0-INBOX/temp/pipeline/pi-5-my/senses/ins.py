"""Insert a block of text into gen_decisions_my.py before a marker line. usage: ins.py <marker-substring> <blockfile>"""
import sys, pathlib
p = pathlib.Path(__file__).resolve().parent / 'gen_decisions_my.py'
s = p.read_text(encoding='utf-8').split('\n')
blk = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8').rstrip('\n').split('\n')
hits = [i for i, l in enumerate(s) if sys.argv[1] in l]
if len(hits) != 1:
    sys.exit(f'marker found {len(hits)} times')
s[hits[0]:hits[0]] = blk
p.write_text('\n'.join(s), encoding='utf-8')
print(f'inserted {len(blk)} lines before line {hits[0] + 1}')
