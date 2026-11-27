"""Print a MANUAL skeleton for headwords: binding senses (pi-5 … pi-1, binding order) with the pi-6 values each
binding file lists, then the unassigned pi-6 values with their ids, then the Marathi pi-6 tags.
usage: skel.py hw [hw ...]"""
import importlib.util, pathlib, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('g', HERE / 'gen_decisions_my.py'); g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
rows = g.read_agg(HERE / 'agg-part1.tsv')
ids = {}
for l in open(HERE / 'agg-part1.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    ids[c[0]] = {m.split('=')[0]: m.split('=', 1)[1] for m in c[2].split(' | ')}
bind = collections.OrderedDict((k, g.read_senses(p, True)) for k, p in g.BIND_FILES.items())
mr = g.read_senses(g.MR_SENSES, False)
for hw in sys.argv[1:]:
    vals = rows[hw]
    print(f"    ('{hw}', [")
    done, seen_tags = set(), []
    for k, d in bind.items():
        kk = g.lookup(d, hw)
        if not kk: continue
        for t, vs in d[kk]:
            if t in seen_tags: continue
            seen_tags.append(t)
            have = [v for v in vs if v in vals and v not in done]
            done |= set(have)
            print(f"        # {k}: {vs}")
            print(f"        ({t!r}, {have!r}),")
    rest = [v for v in vals if v not in done]
    for v in rest:
        print(f"        # UNASSIGNED {v!r} {ids[hw][v]}")
    k3 = g.lookup(mr, hw)
    if k3: print(f"        # mr-6: {mr[k3]}")
    print('    ]),')
