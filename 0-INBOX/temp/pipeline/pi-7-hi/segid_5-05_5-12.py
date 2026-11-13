import re, sys, pathlib
P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
# usage: segid_5-05_5-12.py <file-prefix> "<pali substring>"  -> block ID of the segment containing it
f = next(p for p in P.iterdir() if p.name.startswith(sys.argv[1]))
lines = f.read_text(encoding="utf-8").splitlines()
for i, l in enumerate(lines):
    if sys.argv[2] in l:
        for k in range(i, len(lines)):
            m = re.search(r"\^([0-9A-Za-z-]+)\s*$", lines[k])
            if m:
                print(f.name, "line", i + 1, "segment", m.group(1))
                break
