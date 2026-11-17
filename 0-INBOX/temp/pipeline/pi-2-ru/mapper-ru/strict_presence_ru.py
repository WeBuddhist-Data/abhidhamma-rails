"""Strict presence check over all pi-2 maps (coordinator, 2026-11-16): every non-NDE value is checked with present()
against its segment's Russian, with NO exception lists. Misses are grouped by keyword=value with their segments, so
inherited exceptions cannot hide a wrong value. Output: strict-presence.tsv (count, keyword, value, segments).
usage: python -I -X utf8 strict_presence_ru.py
"""
import collections, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map_common_pi2_ru as M  # noqa: E402

NDE = "(no direct equivalent)"
miss = collections.defaultdict(list)
total = 0
for kf in sorted(HERE.glob("*.keywords.md")):
    part = kf.name[: -len(".keywords.md")]
    ru = M.read_russian(part)
    for line in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        sid, body = line[1:].split("] ", 1)
        text = ru.get(sid, "") if isinstance(ru, dict) else ""
        for it in body.split(", "):
            k, v = it.split("=", 1)
            if v == NDE:
                continue
            total += 1
            if not M.present(v, text):
                miss[(k, v)].append(f"{part.split('-')[0]}:{sid}")
rows = sorted(miss.items(), key=lambda x: -len(x[1]))
with open(HERE / "strict-presence.tsv", "w", encoding="utf-8", newline="\n") as f:
    for (k, v), segs in rows:
        f.write(f"{len(segs)}\t{k}\t{v}\t{' '.join(segs[:12])}\n")
print("values checked", total, "| distinct kw=value missing", len(rows), "| occurrences", sum(len(s) for s in miss.values()))
