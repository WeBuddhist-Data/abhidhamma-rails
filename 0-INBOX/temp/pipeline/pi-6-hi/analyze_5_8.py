r"""Survey the 'who/where' prefixes in the Saccayamaka answers (helper for build_5_hi.py)."""
import pathlib, re, sys, collections
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
cnt = collections.Counter()
for f in ["5-01-saccayamaka.md", "5-02-saccayamaka.md", "5-03-saccayamaka.md"]:
    for line in (P / f).read_text(encoding="utf-8").splitlines():
        line = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
        if line.startswith("(") and "?" in line:
            line = line.split("? ", 1)[1] if "? " in line else ""
        for s in re.split(r"(?<=\.) ", line):
            m = re.match(r"(.+?) (tesaṃ tattha|tesaṃ|tattha) \S+sacca", s)
            if m:
                cnt[m.group(1)] += 1
for k, v in sorted(cnt.items()):
    print(v, k)
