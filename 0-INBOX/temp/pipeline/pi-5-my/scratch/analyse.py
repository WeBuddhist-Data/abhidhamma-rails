import re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
t = (ROOT/"AI_translation/pali/pi-5_split_chapters/1-puggalakatha.md").read_text(encoding="utf-8")
chars = collections.Counter(c for c in t if not c.isalnum() and c not in " \n")
print(chars)
odd = []
for i, l in enumerate(t.splitlines(), 1):
    if l.count('"') % 2: odd.append(i)
    if l.count('‘') != l.count('’'): print("single unbalanced", i)
print("odd double-quote lines", odd)
print("brackets", len(re.findall(r"\[[^\]]*\]", t)))
for b in sorted(set(re.findall(r"\[[^\]]*\]", t))): print(" ", b)
