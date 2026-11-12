"""Report aligned lines where the Hindi has a number word (4 and up, or -ों forms) that the Pāli line lacks."""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-2_split_chapters"
HDIR = ROOT / r"AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
NUM = {
    "चार": r"cat[uū]|catt|catass", "चारों": r"cat[uū]|catt|catass",
    "पाँच": r"pañc", "पाँचों": r"pañc",
    "छह": r"\bcha|chaḷ|cha[ḷa-z]|saḷ|chab", "सात": r"satt", "आठ": r"aṭṭh", "नौ": r"nav", "दस": r"das",
    "ग्यारह": r"ekādas", "बारह": r"dvādas|bārasa", "सोलह": r"soḷas", "सत्रह": r"sattaras",
    "अठारह": r"aṭṭhāras", "बाईस": r"bāvīsat", "तीनों": r"\bti|tay|tīṇ|tiss|tidh|tiv", "दोनों": r"dve|dvi|dvay|ubh|duv|du",
}
HRX = re.compile(r"(?<![\u0900-\u097F])(" + "|".join(sorted(NUM, key=len, reverse=True)) + r")(?![\u0900-\u097F])")
skip_tinon = "--all" not in sys.argv
for hp in sorted(HDIR.glob("*.md")):
    pp = PDIR / hp.name
    P = [l for l in pp.read_text(encoding="utf-8-sig").split("\n") if l.strip()]
    H = [l for l in hp.read_text(encoding="utf-8-sig").split("\n") if l.strip()]
    for i, (p, h) in enumerate(zip(P, H)):
        for m in HRX.finditer(h):
            w = m.group(1)
            if skip_tinon and w in ("तीनों", "दोनों"):
                continue
            if not re.search(NUM[w], p, re.I):
                print(f"{hp.name} L{i+1} {w}: …{h[max(0, m.start()-40):m.end()+40]}… | P: {p[:80]}")
