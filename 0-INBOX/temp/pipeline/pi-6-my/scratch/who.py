"""scratch: list the person / place groups before tesaṃ / tattha in the pavatti answers."""
import re, pathlib, collections
p = pathlib.Path(__file__).resolve().parents[5] / "AI_translation/pali/pi-6_split_chapters/2-01-khandhayamaka.md"
c = collections.Counter()
for line in p.read_text(encoding="utf-8").splitlines():
    line = re.sub(r" \^\S+$", "", line)
    line = re.sub(r" \[[^\]]*\]", "", line)
    for s in re.split(r"(?<=\.) (?=[A-Z])", line):
        m = re.match(r"^(.+?) (tesaṃ|tattha) ", s)
        if m and not s.startswith("("):
            c[m.group(1)] += 1
for k, v in sorted(c.items()):
    print(v, k)
