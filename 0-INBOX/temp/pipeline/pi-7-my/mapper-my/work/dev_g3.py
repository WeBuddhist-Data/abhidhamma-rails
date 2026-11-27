"""dev_g3.py: map the g3 chapters in memory with the map_g3 tables; print unmapped and stem uses with segment text."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map7_rules as R
try:
    import map_g3 as G
    M = G.mapper()
except Exception as e:
    print("no map_g3:", e)
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
CH = ["3-01-hetugocchaka", "3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka",
      "3-05-ganthagocchaka", "3-06-oghayogagocchaka", "3-07-nivaranagocchaka", "3-08-paramasagocchaka"]
chs = [a for a in sys.argv[1:] if not a.startswith("--")] or CH
mode = [a for a in sys.argv[1:] if a.startswith("--")]
for ch in chs:
    my, pa = R.burmese(ch), R.pali(ch)
    lines, problems, unmapped, nne = M.map_chapter(ch)
    stems = [(l[1:].split("] ", 1)[0], kv) for l in lines for kv in l.split("] ", 1)[1].split(", ")
             if M.SRC.get((l[1:].split("] ", 1)[0], kv.split("=", 1)[0])) == "stem"]
    print(f"== {ch} lines {len(lines)} unmapped {len(unmapped)} fails {len(problems)} NDE {nne} stem {len(stems)}")
    if "--u" in mode:
        for sid, kw in unmapped:
            print(f"  U ^{sid} {kw}\n     P: {pa.get(sid,'')[:300]}\n     M: {my[sid][:400]}")
    if "--s" in mode:
        for sid, kv in stems:
            print(f"  S ^{sid} {kv}\n     P: {pa.get(sid,'')[:250]}\n     M: {my[sid][:300]}")
    if "--uc" in mode:
        print("  ", collections.Counter(k for _, k in unmapped).most_common())
    if "--sc" in mode:
        print("  ", collections.Counter(kv for _, kv in stems).most_common())
    for x in problems[:20]:
        print("  FAIL", x)
    if "--nde" in mode:
        for l in lines:
            if R.NONE in l:
                sid = l[1:].split("] ", 1)[0]
                print("  N", [kv for kv in l.split("] ",1)[1].split(", ") if R.NONE in kv], "^"+sid, pa.get(sid,'')[:150])
    if "--pairs" in mode:
        pairs = collections.Counter(); src = {}
        for l in lines:
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1); pairs[(k, v)] += 1; src.setdefault((k, v), M.SRC.get((sid, k), "?"))
        for (k, v), n in sorted(pairs.items(), key=lambda x: R.low(x[0][0])):
            print(f"  {k} = {v}   [{n} {src[(k, v)]}]")
