import re, collections, pathlib
P = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-7_split_chapters")
N = ["4-10-dukatika-sarammanaduka.md", "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
     "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md"]
c = collections.Counter()
for n in N:
    t = re.sub(r"\{[^{}]*\}", "", (P / n).read_text(encoding="utf-8-sig"))
    for m in re.finditer(r"\([^()]*\)", t):
        if not re.fullmatch(r"\(\d+\)", m[0]):
            c[m[0]] += 1
for k, v in sorted(c.items(), key=lambda kv: -kv[1]):
    print(v, k)
print(len(c))
