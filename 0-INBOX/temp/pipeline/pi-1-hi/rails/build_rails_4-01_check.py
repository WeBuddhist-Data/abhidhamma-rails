"""Check every question/answer frame of 4-01 against the bare names of 1-matika.md, and basic Hindi slips."""
import pathlib, re
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters")
PH = "परिघटनाएँ"
names = set()
for line in (D / "1-matika.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"\((क|ख|ग)\) (.+?)(?: \^[\w-]+)?$", line)
    if m:
        s = re.sub(r" \[[^\]]*\]", "", m.group(2)).rstrip("।").strip()
        names.add(re.sub(r"\s*परिघटनाएँ$", "", s))
txt = (D / "4-01-nikkhepakandam.md").read_text(encoding="utf-8")
bad = {}
found = 0
for line in txt.splitlines():
    for x in re.findall(r"^([^।?]*?) परिघटनाएँ कौन-सी हैं\?", line) + re.findall(r"ये ([^।?–\n]*?) परिघटनाएँ हैं।", line):
        found += 1
        x = x.strip()
        if x not in names:
            bad[x] = bad.get(x, 0) + 1
print("frames checked", found)
print("frames not in matrix:")
for k, v in bad.items():
    print(v, k)
print("double spaces", txt.count("  "), "काके", txt.count("काके"), "?।", txt.count("?।"), "।।", txt.count("।।"), "{", txt.count("{"))
print("latin outside brackets:", sorted(set(re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{3,}", re.sub(r"\[[^\]]*\]|\^[\w-]+", "", txt))))[:20])
