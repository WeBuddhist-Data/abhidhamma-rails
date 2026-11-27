"""Counts for the report: final pi-6 term vs the matched locked term (pi12345-match.tsv, rerun pi1234_match.py first).
usage: stats.py"""
import pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
T3 = {}
for line in (B / "AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    for i, s in enumerate(body[:-1].split("; ")): T3[f"{hw}|{i}"] = s.rsplit(": ", 1)[1]
c = collections.Counter(); diff = []
for r in pathlib.Path(__file__).with_name("pi12345-match.tsv").read_text(encoding="utf-8").splitlines():
    cat, key, cands, lt, how, src, tag = r.split("\t")
    if not src: c["no locked match"] += 1; continue
    book = src.split()[0]
    if T3[key] == lt: c[f"took {book}"] += 1
    else: c[f"differs from {book}"] += 1; diff.append(f"{key}: {T3[key]}  | {book} {lt} ({how})")
print(dict(c), "total", len(T3)); print("\n".join(diff))
