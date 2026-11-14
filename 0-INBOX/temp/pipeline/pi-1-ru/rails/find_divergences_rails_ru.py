"""Identical Pāli -> identical Russian check across the pi-1 Russian rails chapters (read-only).
Groups segments by normalised Pāli (block id and variant brackets stripped, spaces collapsed) and lists groups
whose Russian differs (block id stripped). Also counts the bare «X, – это» punctuation pattern per chapter.
usage: python -I -X utf8 find_divergences_rails_ru.py
"""
import collections, pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
RU = ROOT / "AI_translation/russian/pi-1-russian-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(p):
    out, cur = [], []
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), "\n".join(cur)))
            cur = []
    return out


def norm(t):
    t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", t)
    t = re.sub(r"\[[^\]]*\]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r" ([,.;:?])", r"\1", t)


groups = collections.defaultdict(list)
bare = collections.Counter()
for p in sorted(PALI.glob("*.md")):
    pa, ru = segs(p), segs(RU / p.name)
    assert [a for a, _ in pa] == [b for b, _ in ru], p.name
    for (sid, pt), (_, rt) in zip(pa, ru):
        if pt.lstrip().startswith("#"):
            continue
        groups[norm(pt)].append((p.stem, sid, norm(rt)))
    for line in (RU / p.name).read_text(encoding="utf-8").splitlines():
        if re.search(r"(^|\? )[^,?.]+, – это", line):
            bare[p.stem] += 1

div = [(k, v) for k, v in groups.items() if len(v) > 1 and len({r for _, _, r in v}) > 1]
print("segment groups with identical Pāli:", sum(1 for v in groups.values() if len(v) > 1), "| diverging:", len(div))
for k, v in div[:30]:
    print("  PĀLI:", k[:120])
    for part, sid, r in v:
        print(f"    {part} ^{sid}: {r[:150]}")
print("bare «X, – это» lines per chapter:", dict(bare))
