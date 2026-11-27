"""read-only helper (g2): unmapped and stem-fallback keywords of a group chapter, with counts and one example sid."""
import sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
import map_g2 as G
M = G.mapper()
for ch in sys.argv[1:]:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    um = collections.Counter(k for _, k in unmapped)
    ex = {}
    for s, k in unmapped:
        ex.setdefault(k, s)
    print(f"== {ch} unmapped {len(unmapped)}")
    for k, c in um.most_common():
        print(f"  U {k} ({c}) ^{ex[k]}")
    sids = {s for s, _ in R.keyword_rows(ch)}
    st = collections.Counter()
    exs = {}
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if M.SRC.get((sid, k)) == "stem":
                st[(k, v)] += 1
                exs.setdefault((k, v), sid)
    print(f"  stem (top-level) {sum(st.values())} uses, {len(st)} pairs")
    for (k, v), c in sorted(st.items()):
        print(f"  S {k} = {v} ({c}) ^{exs[(k, v)]}")
# scattered values: chunks present but not as a phrase
for ch in sys.argv[1:]:
    my = R.burmese(ch)
    seen = collections.Counter(); ex = {}
    for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if v in ("?", R.NONE):
                continue
            if not (R.phrase_ok(v, my[sid]) or R.phrase_ok(v, R.flat(my[sid]))):
                seen[(k, v)] += 1; ex.setdefault((k, v), sid)
    print(f"  scattered {sum(seen.values())}")
    for (k, v), n in seen.most_common():
        print(f"  X {k} = {v} ({n}) ^{ex[(k, v)]} src={M.SRC.get((ex[(k, v)], k))}")
