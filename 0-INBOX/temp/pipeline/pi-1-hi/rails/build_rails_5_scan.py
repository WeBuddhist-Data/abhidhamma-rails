"""Scan the chapter 5 Hindi for awkward repetition: X X and X Y X word patterns, by frequency."""
import collections, pathlib, re

P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\5-atthakathakandam.md")
text = P.read_text(encoding="utf-8")
words = re.findall(r"[ऀ-ॿ़]+(?:-[ऀ-ॿ़]+)*", text)
adj = collections.Counter(a for a, b in zip(words, words[1:]) if a == b)
skip = collections.Counter(f"{a} {b} {c}" for a, b, c in zip(words, words[1:], words[2:]) if a == c and len(a) > 2)
print("X X:", adj.most_common(20))
print("X Y X:")
for k, n in skip.most_common(40):
    print(n, k)
for pat in [r"(?<![ऀ-ॿ])न न ", r" के के "]:
    print(pat, len(re.findall(pat, text)))
