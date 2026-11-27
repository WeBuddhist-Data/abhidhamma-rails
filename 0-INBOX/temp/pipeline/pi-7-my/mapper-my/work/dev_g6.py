"""dev_g6.py: map the g6 chapters in memory (nothing written) with the module alone; dump unmapped / stem / fails."""
import sys, pathlib, collections, time
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map7_rules as R
G6 = [c for c in R.chapters() if c.startswith("5-")]
t0 = time.time()
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
out = open(HERE / "work" / "dev-g6.txt", "w", encoding="utf-8")
for ch in G6:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    pa, my = R.pali(ch), R.burmese(ch)
    stems = [(l[1:].split("] ", 1)[0], kv) for l in lines for kv in l.split("] ", 1)[1].split(", ")]
    stems = [(sid, kv) for sid, kv in stems if M.SRC.get((sid, kv.split("=", 1)[0])) == "stem"]
    print(ch, "lines", len(lines), "unmapped", len(unmapped), "stem", len(stems), "fails", len(problems), "NDE", nne,
          f"{time.time()-t0:.1f}s", file=out, flush=True)
    for sid, k in unmapped:
        print(f"  U\t{ch}\t{sid}\t{k}", file=out)
    for sid, kv in stems:
        print(f"  S\t{ch}\t{sid}\t{kv}", file=out)
    for x in problems:
        print("  F", ch, x, file=out)
print("sources", collections.Counter(v.split(':')[0] if v else v for v in M.SRC.values()).most_common(), file=out)
out.close()
