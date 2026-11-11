import pathlib, re, difflib
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
TR = re.compile(r"^\s*!\[\[.*\]\]\s*$")
def load(p):
    t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    fm = re.match(r"---\n.*?\n---\n", t, re.S)
    body = t[fm.end():] if fm else t
    return [l for l in body.split("\n") if l.strip() and not TR.match(l)]
a = load(B / "AI_translation/english/pi-2-english-plain-zeroshot.md")
b = load(B / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-2-english-plain-zeroshot.md")
ia = [m.group(1) if (m := ID.search(l)) else None for l in a]
ib = [m.group(1) if (m := ID.search(l)) else None for l in b]
print("lines AI", len(a), "track", len(b))
print("IDs AI", sum(1 for x in ia if x), "track", sum(1 for x in ib if x))
root = [m.group(1) for l in (B / "1-SOURCES/Text/pi-2.md").read_text(encoding="utf-8").splitlines() if (m := ID.search(l))]
print("track IDs == root:", [x for x in ib if x] == root, "AI IDs == root:", [x for x in ia if x] == root)
strip = lambda l: ID.sub("", l).rstrip()
same_text = sum(1 for x, y in zip(a, b) if strip(x) == strip(y))
print("lines identical apart from ID:", same_text, "of", min(len(a), len(b)))
diffs = [(k, x, y) for k, (x, y) in enumerate(zip(ia, ib)) if x != y]
print("ID differences (line-aligned):", len(diffs), diffs[:10])
txtdiff = [(k, x[:90], y[:90]) for k, (x, y) in enumerate(zip(a, b)) if strip(x) != strip(y)]
print("text differences:", len(txtdiff)); [print("  ", d) for d in txtdiff[:5]]
