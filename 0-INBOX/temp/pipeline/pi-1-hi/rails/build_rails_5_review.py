"""Print chosen segments of the chapter 5 Hindi and scan the whole file for adjacent word repetition."""
import pathlib, re, sys

P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\5-atthakathakandam.md")
text = P.read_text(encoding="utf-8")
blocks = text.strip().split("\n\n")
want = set(sys.argv[1:])
for b in blocks:
    m = re.search(r"\^([0-9A-Za-z-]+)$", b)
    if m and m.group(1) in want:
        print(b, "\n")

words = re.findall(r"[ऀ-ॿ़-]+", text)
hits = {}
for a, b in zip(words, words[1:]):
    if a == b:
        hits[a] = hits.get(a, 0) + 1
print("adjacent repeats:", hits)
for pat in [r"मन में से मन", r"की की", r"के के", r"और और", r", ,", r"  ", r"न न ", r"होते हैं होते", r"मन की मन की"]:
    print(repr(pat), len(re.findall(pat, text)))
