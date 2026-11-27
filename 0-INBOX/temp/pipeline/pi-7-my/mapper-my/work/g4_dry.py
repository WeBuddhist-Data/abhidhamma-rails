"""g4_dry.py: dry run of the g4 chapters with map_g4's tables; lists unmapped and stem uses (read-only helper)."""
import sys, pathlib, collections, pickle
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g4 as G
M = G.mapper()
out = D / "work" / "g4-dry.txt"
L = []
unm = collections.Counter(); stem = collections.Counter(); ex = {}
for ch in G.CHAPTERS:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    L.append(f"{ch}: lines {len(lines)} problems {len(problems)} unmapped {len(unmapped)} NDE {nne}")
    for sid, k in unmapped:
        unm[(ch, k)] += 1; ex.setdefault((ch, k), sid)
    for p in problems:
        L.append(f"  PROBLEM {p}")
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if M.SRC.get((sid, k)) == "stem":
                stem[(ch, k, v)] += 1; ex.setdefault((ch, k, v), sid)
L.append("== UNMAPPED")
for (ch, k), c in sorted(unm.items()):
    L.append(f"U\t{ch}\t{k}\t{c}\t{ex[(ch,k)]}")
L.append("== STEM")
for (ch, k, v), c in sorted(stem.items()):
    L.append(f"S\t{ch}\t{k}\t{v}\t{c}\t{ex[(ch,k,v)]}")
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L[:12]))
print("unmapped kinds", len(unm), "uses", sum(unm.values()), "stem kinds", len(stem), "uses", sum(stem.values()))
