"""For a decisions file, print each line's source: binding book (p5 … p1) or mr (Marathi tag), with tag and values.
usage: src_of.py <decisions.txt> [mr|bind|all]"""
import importlib.util, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('g', HERE / 'gen_decisions_my.py'); g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
bind = {k: g.read_senses(p, True) for k, p in g.BIND_FILES.items()}
mode = sys.argv[2] if len(sys.argv) > 2 else 'all'
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.rstrip('\n')
    if not line or line.startswith('#'): continue
    hw, s = g.parse_line(line)
    src = next((k for k in bind if g.lookup(bind[k], hw)), 'mr')
    if hw in g.MANUAL: src = 'MAN:' + src
    if mode == 'all' or (mode == 'mr' and src.endswith('mr')) or (mode == 'bind' and not src.endswith('mr')):
        print(f'{src}\t{hw}\t' + ' ;; '.join(f'{t} => {" / ".join(v)}' for t, v in s))
