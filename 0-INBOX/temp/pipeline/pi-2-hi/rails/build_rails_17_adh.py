"""Termbase adherence (same matching as hindi_termbase_adherence.py) restricted to chapter 17; lists every miss."""
import collections
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
src = (ROOT / "0-INBOX" / "temp" / "pipeline" / "hindi_termbase_adherence.py").read_text(encoding="utf-8")
ns = {}
# reuse the helpers (stem, found, STOP, ENDS, WORD) without running the script body
exec(src.split("seg = {}")[0].replace("kw_path, tb_path, rails_dir = sys.argv[1:4]", "")
     .replace("report = sys.argv[4] if len(sys.argv) > 4 else None", ""), ns)
ns["tb"] = {}
for line in (ROOT / "AI_translation" / "hindi" / "pi-2-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    ns["tb"][w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
tb = ns["tb"]
tb_ci = {k.lower(): v for k, v in tb.items()}
exec(src[src.index("def found"):src.index("total = miss = 0")], ns)
found, WORD, ID = ns["found"], ns["WORD"], ns["ID"]

seg, buf = {}, []
for line in (ROOT / "AI_translation" / "hindi" / "pi-2-hindi-plain-rails_split_chapters" /
             "17-khuddakavatthuvibhango.md").read_text(encoding="utf-8").splitlines():
    buf.append(line)
    m = ID.search(line)
    if m:
        seg[m.group(1)] = " ".join(buf)
        buf = []
total = miss = 0
by = collections.defaultdict(list)
for line in (ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    words = WORD.findall(seg[i])
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(kk.lower())
            if not terms:
                continue
            total += 1
            if not any(found(t, words) for t in terms):
                miss += 1
                by[(kk, " | ".join(terms))].append(i)
print(f"ch17: {total} keyword occurrences, {miss} misses ({100 * miss / max(total, 1):.1f}%)")
for (k, t), ids in sorted(by.items(), key=lambda x: -len(x[1])):
    print(f"{len(ids):3d} {k} -> {t}  {' '.join(ids[:6])}")
