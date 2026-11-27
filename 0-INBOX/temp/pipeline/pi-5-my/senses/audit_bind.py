"""Audit a decisions / senses file against the binding Burmese senses (pi-4, then pi-3, pi-2, pi-1): every value that
a binding file lists for the headword must sit under a tag that starts with that file's tag for it (the first file in
binding order that lists the value). Lists the violations (TAG_CHANGED headwords are reported as 'changed').
usage: audit_bind.py <decisions-or-senses.md>"""
import importlib.util, pathlib, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('g', HERE / 'gen_decisions_my.py'); g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
bind = collections.OrderedDict((k, g.read_senses(p, True)) for k, p in g.BIND_FILES.items())
bad = 0
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.rstrip('\n')
    if not line or line.startswith('#'): continue
    hw, senses = g.parse_line(line)
    bind_of = {}
    for k in reversed(list(bind)):
        kk = g.lookup(bind[k], hw)
        if kk:
            bind_of.update({v: (t, k) for t, vs in bind[k][kk] for v in vs})
    for t, vs in senses:
        for v in vs:
            if v in bind_of and not t.startswith(bind_of[v][0]):
                bad += 1
                tag = 'changed' if hw in g.TAG_CHANGED else 'VIOLATION'
                print(f'{tag}\t{hw}\t{v}\tbinding {g.BOOK[bind_of[v][1]]}: {bind_of[v][0][:90]!r}\tgot: {t[:90]!r}')
print(f'{bad} value(s) off their binding tag')
