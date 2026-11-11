import pathlib, re
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TR = re.compile(r"^\s*!\[\[.*\]\]\s*$")
def load(p):
    t = p.read_text(encoding="utf-8").replace("\r\n", "\n"); fm = re.match(r"---\n.*?\n---\n", t, re.S)
    return [l for l in (t[fm.end():] if fm else t).split("\n") if l.strip() and not TR.match(l)]
a = load(B / "AI_translation/english/pi-2-english-plain-zeroshot.md")
b = load(B / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-2-english-plain-zeroshot.md")
d = [(x, y) for x, y in zip(a, b) if re.sub(r"^\d+\. ", "", x) != y]
print("differences other than a leading number:", len(d)); [print(" A:", x[:120], "\n T:", y[:120]) for x, y in d[:4]]
