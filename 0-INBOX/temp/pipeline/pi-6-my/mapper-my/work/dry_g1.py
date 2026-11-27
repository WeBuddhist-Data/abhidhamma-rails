"""read-only helper (g1): dry run of the module on the G1 chapters: unmapped keywords, stem values, sources."""
import sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
G1 = ["2-02-khandhayamaka", "3-01-ayatanayamaka", "3-02-ayatanayamaka", "3-03-ayatanayamaka", "3-04-ayatanayamaka",
      "3-05-ayatanayamaka", "3-06-ayatanayamaka", "4-dhatuyamaka", "5-01-saccayamaka", "5-02-saccayamaka",
      "5-03-saccayamaka"]
chs = sys.argv[1:] or G1
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
for ch in chs:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    um = collections.Counter(k for _, k in unmapped)
    st = collections.Counter()
    for sid, kws in R.keyword_rows(ch):
        for k in kws:
            if M.SRC.get((sid, k)) == "stem":
                pass
    stems = collections.Counter()
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if M.SRC.get((sid, k)) == "stem":
                stems[(k, v)] += 1
    print(f"== {ch}: lines {len(lines)} unmapped {len(unmapped)} ({len(um)} kw) problems {len(problems)} stem {sum(stems.values())} NDE {nne}")
    for k, c in um.most_common():
        print("   UNM", k, c)
    for (k, v), c in stems.most_common():
        print("   STEM", k, "=", v, c)
    for p in problems[:20]:
        print("   PROB", p)
