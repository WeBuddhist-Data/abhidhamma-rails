"""Inventory for G10b2: subjects / verbs of 10-13 and intro prefixes of 10-09 … 10-12 (prints only)."""
import re
import sys
from collections import Counter

P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
mode = sys.argv[1]
chs = sys.argv[2:]
subj, verbs, other = Counter(), Counter(), Counter()
for ch in chs:
    txt = open(f"{P}\\{ch}", encoding="utf-8").read()
    for line in txt.splitlines():
        line = re.sub(r"\s*\^[\w-]+$", "", line).strip()
        if not line or line.startswith("#"):
            continue
        for s in re.split(r"(?<=[.?])\s+", line):
            if mode == "pr":
                m = re.match(r"^(.*?)\s*\S+indriy\S*", s)
                if m and not s.startswith("("):
                    subj[m.group(1)] += 1
                for v in re.findall(r"\b(?:na |nap?)?\w*(?:jān|jah|bhāv|sacch)\w*", s):
                    verbs[v] += 1
                if not m and not s.startswith("("):
                    other[s] += 1
            else:
                m = re.match(r"^(.*?) (?:tesaṃ|tāsaṃ)(?: tattha)? \S+indriy", s)
                if m:
                    subj[m.group(1)] += 1
                elif not s.startswith("(") and not s.startswith(("Yassa", "Yattha", "Āmantā", "No.")):
                    other[s] += 1
for k, v in subj.most_common():
    print(v, "|", k)
print("----")
for k, v in verbs.most_common():
    print(v, "|", k)
print("----")
for k, v in other.most_common():
    print(v, "|", k)
