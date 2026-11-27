import re, sys, collections, pathlib
P = pathlib.Path(sys.argv[1])
for f in sys.argv[2:]:
    t = re.sub(r"\{[^{}]*\}", "", (P / f).read_text(encoding="utf-8-sig"))
    c = collections.Counter(re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", t))
    keys = [w for w in c if re.search(r"(?i)īvaraṇ|arām|pādān|diṭṭh|sīlabbat|attavād|kām|lobh|rāg", w)]
    print("==", f)
    print(" ".join(f"{w}:{c[w]}" for w in sorted(keys, key=lambda w: -c[w])))
