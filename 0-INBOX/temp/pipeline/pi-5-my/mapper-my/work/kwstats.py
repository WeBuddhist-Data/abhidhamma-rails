import pathlib, collections, re, sys
d = pathlib.Path(__file__).resolve().parent.parent
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
def kws(ch):
    for l in (d / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if m:
            for k in m.group(2).split(", "):
                yield m.group(1), k.strip()
book = collections.Counter(); chs = collections.defaultdict(set)
for f in sorted(d.glob("*.keywords.md")):
    ch = f.name[:-12]
    for sid, k in kws(ch):
        book[k] += 1; chs[k].add(ch)
c1 = collections.Counter(k for _, k in kws("1-puggalakatha"))
c0 = collections.Counter(k for _, k in kws("preamble"))
print("book distinct", len(book), "total", sum(book.values()))
print("ch1 distinct", len(c1), "total", sum(c1.values()))
top = book.most_common(150)
print("top150 in ch1:", sum(1 for k, _ in top if k in c1))
for k, n in top:
    print(n, len(chs[k]), k, c1.get(k, 0))
