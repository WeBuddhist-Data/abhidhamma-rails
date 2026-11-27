import re, pathlib, collections
P = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-7_split_chapters")
mine = ["5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]
done = sorted(p.name for p in pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters").glob("*.md"))
corpus = {n: (P / n).read_text(encoding="utf-8").lower() for n in done if (P / n).exists()}
cnt = collections.Counter()
for n in mine:
    for m in re.finditer(r"\(([^()]*)\)", (P / n).read_text(encoding="utf-8")):
        if re.fullmatch(r"\d+", m[1]): continue
        cnt[m[0]] += 1
for k, c in cnt.most_common():
    where = [n[:4] for n, t in corpus.items() if k.lower() in t]
    print(c, k, "->", ",".join(where[:8]) or "NONE")
