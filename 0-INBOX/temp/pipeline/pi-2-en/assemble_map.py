"""Assemble and check the pi-2 Pāli=English keyword map from the per-chapter mapper files.

usage: python -I -X utf8 assemble_map.py [--write]
Checks for every chapter: mapped file present; same IDs and English keywords (same order) as <ch>.keywords.md;
every Pāli value (each " / " part, each word) occurs in that segment's Pāli (substring, as in the sample's check);
no ", " inside a value. Reports values of 4+ words (pi-1 cut those to head words joined by " / ").
Output lines are sorted by block ID in the extractor's natural order (as the pi-1 file).
--write: AI_translation/english/pi-2-keywords-by-reference-pali-english-plain.md
         and AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md (Pāli side only, as pi-1's make_pali_keywords).
"""
import pathlib, re, sys

B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
M = pathlib.Path(__file__).parent / "mapper"
PDIR = B / "AI_translation/pali/pi-2_split_chapters"
OUT_PE = B / "AI_translation/english/pi-2-keywords-by-reference-pali-english-plain.md"
OUT_P = B / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
NDE = "(no direct equivalent)"


# Long spans cut to their head words joined by " / " (as pi-1's finalise_map.py); keyed by exact old value
LONG = {
    "avasesā ca akusalā dhammā": "avasesā / akusalā / dhammā",
    "Avasesā ca akusalā dhammā": "Avasesā / akusalā / dhammā",
    "avasesā ca sāsavā kusalā": "avasesā / kusalā",
    "Avasesā ca sāsavā kusalā": "Avasesā / kusalā",
    "avasesā ca sāsavā kusalā dhammā": "avasesā / kusalā / dhammā",
    "Avasesā ca sāsavā kusalā dhammā": "Avasesā / kusalā / dhammā",
    "sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā": "sukhāya / sampayuttā",
    "sāsavā ca kusalākusalānaṃ dhammānaṃ": "sāsavā / kusalākusalānaṃ / dhammānaṃ",
    "cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ": "cetosamphassajaṃ / dukkhaṃ / vedayitaṃ",
    "cetosamphassajā asātā dukkhā vedanā": "cetosamphassajā / dukkhā / vedanā",
    "kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ": "kāyasamphassajaṃ / dukkhaṃ / vedayitaṃ",
    "kāyasamphassajā asātā dukkhā vedanā": "kāyasamphassajā / dukkhā / vedanā",
    "kāyassa bhedā paraṃ maraṇā": "kāyassa / paraṃ maraṇā",
    "hoti tathāgato paraṃ maraṇā": "hoti / paraṃ maraṇā",
}
NEG_EN = re.compile(r"\b(not|non|no|without|lack|never|un\w+|in\w+|im\w+)\b", re.I)
WORD = re.compile(r"[^\s,.;:?!()\[\]–\"'‘’“”…]+")
fixlog = []


def fix(sid, pv, en, seg_text):
    """long-span cut, then: a single word that occurs in the segment only inside a negated word -> that word"""
    new = LONG.get(pv, pv)
    if new == pv and pv != NDE and " " not in pv and not NEG_EN.search(en):
        cont = [w for w in WORD.findall(seg_text) if pv.lower() in w.lower()]
        if cont and all(re.match(r"^(an?|na|no)" + re.escape(pv.lower()), w.lower()) and w.lower() != pv.lower() for w in cont):
            new = cont[0]
    if new != pv:
        fixlog.append(f"{sid}\t{pv}\t{new}\t{en}")
    return new


def key(i):
    return [(0, int(p), "") if p.isdigit() else (1, 0, p) for p in i.split("-")]


errs, lines, longv, nde, n_kw = [], {}, [], 0, 0
for p in sorted(PDIR.glob("*.md"), key=lambda p: -1 if p.stem == "preamble" else int(p.stem.split("-")[0])):
    ch = p.stem
    seg, buf = {}, []
    for l in p.read_text(encoding="utf-8").splitlines():
        if l.strip():
            buf.append(l)
            if (m := ID.search(l)):
                seg[m.group(1)] = " ".join(buf); buf = []
    mp = M / f"{ch}.mapped.md"
    if not mp.exists():
        errs.append(f"{ch}: no mapped file"); continue
    a = [l.split("] ", 1) for l in (M / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l.split("] ", 1) for l in mp.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    if [x[0] for x in a] != [x[0] for x in b]:
        errs.append(f"{ch}: ID lines differ"); continue
    for (i, x), (_, y) in zip(a, b):
        sid = i[1:]
        pairs = [q.rsplit("=", 1) for q in y.split(", ")]
        if [k.strip() for k in x.split(", ")] != [q[1] for q in pairs if len(q) == 2] or any(len(q) != 2 for q in pairs):
            errs.append(f"{ch} {sid}: English keywords differ"); continue
        pairs = [[fix(sid, pv, en, seg.get(sid, "")), en] for pv, en in pairs]
        y = ", ".join(f"{pv}={en}" for pv, en in pairs)
        for pv, en in pairs:
            n_kw += 1
            if pv == NDE:
                nde += 1; continue
            for part in pv.split(" / "):
                for w in part.split():
                    if w not in seg.get(sid, ""):
                        errs.append(f"{ch} {sid}: '{w}' not in the segment ({pv}={en})")
            if any(len(part.split()) >= 4 for part in pv.split(" / ")):
                longv.append((sid, pv, en))
        lines[sid] = f"{i}] {y}"

print(f"chapters checked; lines {len(lines)}, keywords {n_kw}, no direct equivalent {nde} ({100*nde/max(n_kw,1):.1f}%)")
print(f"coordinator fixes: {len(fixlog)} (long-span cuts and negation slips; log: finalise-log.tsv)")
(pathlib.Path(__file__).parent / "finalise-log.tsv").write_text("sid\told\tnew\tenglish\n" + "\n".join(fixlog) + "\n", encoding="utf-8", newline="\n")
print(f"values of 4+ words: {len(longv)}")
for v in longv[:40]:
    print("   ", v)
if errs:
    print("\n".join(errs[:40])); sys.exit(f"{len(errs)} problems, nothing written")
if "--write" in sys.argv:
    order = sorted(lines, key=key)
    OUT_PE.write_text("\n".join(lines[i] for i in order) + "\n", encoding="utf-8", newline="\n")
    rows, empty = [], []
    for i in order:
        body = lines[i].split("] ", 1)[1]
        seen, keep = set(), []
        for q in body.split(", "):
            for w in q.rsplit("=", 1)[0].split(" / "):
                w = w.strip()
                if w and w != NDE and w not in seen:
                    seen.add(w); keep.append(w)
        if not keep:
            empty.append(i)
        rows.append(f"[{i}] " + ", ".join(keep))
    OUT_P.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT_PE.name, len(order), "lines and", OUT_P.name, len(rows), "lines; lines with no Pāli keyword:", empty)
