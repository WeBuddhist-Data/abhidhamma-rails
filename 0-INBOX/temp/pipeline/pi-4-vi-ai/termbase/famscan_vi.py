"""Family scan for the pi-4 Vietnamese termbase (read-only; prints only).
Groups single-word headwords by a crude stem (inflection endings stripped) and prints groups whose senses
share the first gloss word of the tag but end with different Vietnamese terms (decision or single candidate)."""
import collections, pathlib, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_vi as T

ENDS = sorted("o ā aṃ ena assa āni ānaṃ e ehi esu ī inā ino iṃ iyā ā āya āyo ā aṃ u uṃ unā uno ūnaṃ tā taṃ to ti tiṃ yā yaṃ".split(), key=len, reverse=True)


def stem(hw):
    h = hw.lower()
    for e in ENDS:
        if h.endswith(e) and len(h) - len(e) >= 4:
            return h[: -len(e)]
    return h


def gloss(tag):
    return re.split(r"[ ,(']", tag.strip(), 1)[0].lower()


ss, dec = T.senses(), T.decisions()
groups = collections.defaultdict(list)
for hw, s in ss:
    if " " in hw:
        continue
    for i, (tag, c) in enumerate(s):
        k = f"{hw}|{i}"
        term = dec[k][0] if k in dec else c[0]
        groups[(stem(hw), gloss(tag))].append((k, term, tag[:80]))
n = 0
for (st, g), v in sorted(groups.items()):
    terms = {t for _, t, _ in v}
    if len(v) > 1 and len(terms) > 1:
        n += 1
        print(f"== {st} / {g}")
        for k, t, tag in v:
            print(f"   {k}\t{t}\t{tag}")
print(n, "groups")
