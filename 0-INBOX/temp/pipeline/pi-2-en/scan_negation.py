"""Read-only scan of the pi-2 maps: a single-word Pāli value that occurs in its segment ONLY inside a negated word
(a-/an-/na-/no- + value), while the English keyword has no negation (not, non, no, without, un-, in-, lack).
"""
import pathlib, re

B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
M = pathlib.Path(__file__).parent / "mapper"
PDIR = B / "AI_translation/pali/pi-2_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
NEG_EN = re.compile(r"\b(not|non|no|without|lack|never|un\w+|in\w+|im\w+)\b", re.I)
WORD = re.compile(r"[^\s,.;:?!()\[\]–\"'‘’“”…]+")
hits = []
for p in PDIR.glob("*.md"):
    seg, buf = {}, []
    for l in p.read_text(encoding="utf-8").splitlines():
        if l.strip():
            buf.append(l)
            if (m := ID.search(l)):
                seg[m.group(1)] = " ".join(buf); buf = []
    mp = M / f"{p.stem}.mapped.md"
    for l in mp.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        i, body = l.split("] ", 1)
        words = WORD.findall(seg.get(i[1:], ""))
        for q in body.split(", "):
            pv, en = q.rsplit("=", 1)
            if pv == "(no direct equivalent)" or " " in pv or NEG_EN.search(en):
                continue
            containing = [w for w in words if pv.lower() in w.lower()]
            if containing and all(re.match(r"^(an?|na|no)" + re.escape(pv.lower()), w.lower()) and w.lower() != pv.lower()
                                  for w in containing):
                hits.append((p.stem[:6], i[1:], pv, en, containing[0]))
print(len(hits))
for h in hits[:60]:
    print("  ", h)
