import re, pathlib, collections, sys
P = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-7_split_chapters")
STOP = {"paṭicca","uppajjati","uppajjanti","hetupaccayā","paccayo","ca","dhammo","dhammā","dhammaṃ","dhammassa"}
for n in sys.argv[1:]:
    t = (P / n).read_text(encoding="utf-8")
    t = re.sub(r"\^\S+", "", t)
    cnt = collections.Counter()
    for sent in re.split(r"(?<=[.;–])\s|\n", t):
        # phrases ending right before a dhamm word
        for m in re.finditer(r"((?:[^\s.;,()–…]+ ){1,6}?)dhamm\w*", sent):
            words = m[1].split()
            # trim left at stop words
            out = []
            for w in reversed(words):
                if w.lower() in STOP or w.endswith("paccayā") or w.endswith("paccayena") or w.startswith("("): break
                out.append(w)
            cnt[" ".join(reversed(out)).lower()] += 1
    print("==", n, len(cnt))
    for k, c in sorted(cnt.items()):
        print(f"  {c:4d} {k}")
