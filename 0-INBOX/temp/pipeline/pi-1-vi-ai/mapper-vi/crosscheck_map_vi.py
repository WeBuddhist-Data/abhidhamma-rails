"""Cross-part checks of the pi-1 Vietnamese keyword map (read-only).

1. structure: same ids, same keywords in order (as the brief's verifier), for all parts;
2. bare function-word values (a preposition/particle alone, e.g. «с», «по»);
3. identical segments (same Pāli AND same Vietnamese) with different values for the same keyword;
4. per keyword: the distinct values across the book (only keywords with >1 value, top N) -> crosscheck-values.tsv
usage: python -I -X utf8 crosscheck_map_vi.py
"""
import pathlib, re, collections, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
D = ROOT / "0-INBOX/temp/pipeline/pi-1-vi-ai/mapper-vi"
PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
RU = ROOT / "AI_translation/vietnamese/pi-1-vietnamese-plain-zeroshot_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
FUNC = {"và", "của", "là", "có", "không", "các", "những", "ở", "trong", "với", "cho", "thì", "mà", "nào", "đã", "đang", "sẽ", "ấy", "này", "được", "bị", "về", "theo", "từ", "đó", "hay", "hoặc", "cũng", "như", "khi", "lúc", "điều"}


def segs(p):
    out, cur = {}, []
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID.search(line)
        if m:
            out[m.group(1)] = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", "\n".join(cur)).strip()
            cur = []
    return out


def parse(p):
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        sid, body = line[1:].split("] ", 1)
        rows.append((sid, body))
    return rows


bad_struct, func_vals, conflicts = [], [], []
by_kw = collections.defaultdict(collections.Counter)
seen = {}
for kf in sorted(D.glob("*.keywords.md")):
    part = kf.name[: -len(".keywords.md")]
    mf = D / f"{part}.mapped.md"
    if not mf.exists():
        bad_struct.append((part, "missing"))
        continue
    a, b = parse(kf), parse(mf)
    if [x[0] for x in a] != [x[0] for x in b]:
        bad_struct.append((part, "ids"))
        continue
    pali, ru = segs(PALI / f"{part}.md"), segs(RU / f"{part}.md")
    for (sid, kws), (_, mapped) in zip(a, b):
        ks = [k.strip() for k in kws.split(", ")]
        pairs = [x.split("=", 1) for x in mapped.split(", ")]
        if ks != [p[0] for p in pairs]:
            bad_struct.append((part, sid))
            continue
        key = (pali.get(sid, ""), ru.get(sid, ""))
        for k, v in pairs:
            by_kw[k][v] += 1
            if v.strip().lower() in FUNC:
                func_vals.append((part, sid, k, v))
            prev = seen.get((key, k))
            if prev is None:
                seen[(key, k)] = (v, part, sid)
            elif prev[0] != v and key[0]:
                conflicts.append((k, prev[0], f"{prev[1]}:{prev[2]}", v, f"{part}:{sid}"))

print("structure problems:", bad_struct or "none")
print("bare function-word values:", len(func_vals))
for x in func_vals[:40]:
    print("  ", *x)
print("identical-segment conflicts:", len(conflicts))
for x in conflicts[:40]:
    print("  ", *x)
multi = sorted(((k, c) for k, c in by_kw.items() if len(c) > 1), key=lambda x: -sum(x[1].values()))
with open(D / "crosscheck-values.tsv", "w", encoding="utf-8", newline="\n") as f:
    for k, c in multi:
        f.write(k + "\t" + " | ".join(f"{v} ({n})" for v, n in c.most_common()) + "\n")
print("keywords with >1 value:", len(multi), "-> crosscheck-values.tsv")
