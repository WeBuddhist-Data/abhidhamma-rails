"""Tally regex matches per file: python -I -X utf8 rv_tally.py PATTERNFILE
PATTERNFILE: one regex per line (UTF-8), avoids shell quoting of curly quotes."""
import collections, pathlib, re, sys

HDIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters")
pats = [l for l in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").split("\n") if l.strip()]
for pat in pats:
    c = collections.Counter()
    rx = re.compile(pat)
    for hp in sorted(HDIR.glob("*.md")):
        for m in rx.finditer(hp.read_text(encoding="utf-8")):
            c[(hp.name[:3], m.group(0))] += 1
    print("##", pat)
    for (f, s), n in sorted(c.items()):
        print(f"{n}\t{f}\t{s}")
