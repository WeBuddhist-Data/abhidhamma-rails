"""Scan helper for 4-02..4-07: distinct headings, parentheticals, and lines matching a regex."""
import pathlib, re, sys, collections

PALI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
mode = sys.argv[1]
c = collections.Counter()
for f in FILES:
    for line in (PALI / f).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        line = ID.sub("", line)
        if mode == "head" and line.startswith("#"):
            c[re.sub(r"^#+ ", "", line)] += 1
        elif mode == "paren" and not line.startswith("#"):
            for m in re.finditer(r"\([^()]*\)", line):
                if not re.fullmatch(r"\(\d+\)", m.group(0)):
                    c[m.group(0)] += 1
        elif mode == "grep" and re.search(sys.argv[2], line):
            c[line] += 1
for k, v in sorted(c.items()):
    print(v, k)
