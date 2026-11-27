"""List the headwords that take a single Marathi pi-7 tag (no binding line) in a decisions file: hw <TAB> tag <TAB>
values. usage: mrlist.py <decisions.txt> > mr-lines.txt"""
import importlib.util, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('g', HERE / 'gen_decisions_my.py'); g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
bind = [g.read_senses(p, True) for p in g.BIND_FILES.values()]
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.rstrip('\n')
    if not line or line.startswith('#'): continue
    hw, s = g.parse_line(line)
    if hw in g.MANUAL or any(g.lookup(b, hw) for b in bind): continue
    print(f'{hw}\t{s[0][0]}\t{" / ".join(s[0][1])}')
