"""Grep the reviewed Hindi of pi-1/3/4/5 (rails) for a regex and print contexts.
usage: hz_ref.py <regex> [width] [max]"""
import sys, os, re, glob

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi"
rx = re.compile(sys.argv[1])
w = int(sys.argv[2]) if len(sys.argv) > 2 else 60
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 40
n = 0
for b in ("pi-1", "pi-3", "pi-4", "pi-5"):
    for f in sorted(glob.glob(os.path.join(ROOT, f"{b}-hindi-plain-rails_split_chapters", "*.md"))):
        for i, line in enumerate(open(f, encoding="utf-8-sig"), 1):
            for m in rx.finditer(line):
                n += 1
                if n <= mx:
                    print(f"{b}/{os.path.basename(f)}:{i}: …{line[max(0, m.start()-w):m.end()+w].strip()}…")
print("total", n)
