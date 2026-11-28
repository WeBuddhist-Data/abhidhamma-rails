"""G3 inventory: distinct person intros (before «tesaṃ») and place intros (before «tattha») in 3-01 … 3-06."""
import collections
import pathlib
import re

P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters")
intro, place = collections.Counter(), collections.Counter()
for i in range(1, 7):
    t = (P / f"3-0{i}-ayatanayamaka.md").read_text(encoding="utf-8")
    t = re.sub(r"\^[0-9-]+", "", t)
    for s in re.split(r"(?<=[.?])\s+|\n", t):
        s = s.strip()
        m = re.match(r"^(.*?) tesaṃ ", s)
        if m and not s.startswith("("):
            intro[m.group(1).lower()] += 1
        m = re.match(r"^(.*?) tattha ", s)
        if m and not s.startswith("(") and " tesaṃ" not in m.group(1) and not s.lower().startswith(("yattha", "yassa")):
            place[m.group(1).lower()] += 1
for k, v in sorted(intro.items()):
    print("I", v, k)
for k, v in sorted(place.items()):
    print("P", v, k)
