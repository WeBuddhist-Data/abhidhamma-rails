"""Count regex occurrences per file in the backup: python -I -X utf8 rv_count.py PATTERNFILE"""
import pathlib, re, sys

BAK = pathlib.Path(__file__).parent / "backup-pre-fixes"
for pat in [l for l in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").split("\n") if l.strip()]:
    rx = re.compile(pat)
    res = {p.name[:3]: len(rx.findall(p.read_text(encoding="utf-8"))) for p in sorted(BAK.glob("*.md"))}
    print(pat, sum(res.values()), {k: v for k, v in res.items() if v})
