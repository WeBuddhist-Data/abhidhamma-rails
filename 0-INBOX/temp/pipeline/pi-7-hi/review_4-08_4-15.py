"""Review helper for 4-08..4-15 Hindi: distinct parentheses, headings, suspicious patterns (read-only)."""
import collections
import pathlib
import re
import sys

HI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters")
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
         "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md",
         "4-15-tikaduka-hetuduka.md"]
mode = sys.argv[1] if len(sys.argv) > 1 else "paren"
c = collections.Counter()
for f in FILES:
    for i, line in enumerate((HI / f).read_text(encoding="utf-8").splitlines(), 1):
        if mode == "paren":
            for m in re.findall(r"\([^()]*\)", line):
                if not re.fullmatch(r"\(\d+\)", m):
                    c[m] += 1
        elif mode == "head":
            if line.startswith("#"):
                c[re.sub(r"\s*\^\S+$", "", line).lstrip("#").strip()] += 1
        elif mode == "sus":
            if line.startswith("#"):
                continue
            for rx in [r"  ", r" ,", r"परिघटना परिघटना", r"\.", r"।।", r"\?\?", r",,", r" ।",
                       r"—", r":-", r"[A-Za-z]{2,}"]:
                if re.search(rx, line):
                    print(f, i, rx, line[:120])
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(v, k)
