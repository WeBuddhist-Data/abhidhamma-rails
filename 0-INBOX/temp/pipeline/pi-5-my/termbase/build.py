"""Compose decisions-A.tsv from raw-multi.tsv (part 1, split by pi1234-match category) and raw-align.tsv / raw-family.tsv /
raw-textinc.tsv (parts 2-4) plus notes-part5.txt (comments only). Checks: every multi-candidate sense decided once; no
forbidden separators or dash in a term. usage: build.py [--multi-only]"""
import pathlib, sys, collections
H = pathlib.Path(__file__).resolve().parent
B = H.parents[4]
S = B / "AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md"
cands = {}
for line in S.read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    for i, s in enumerate(body[:-1].split("; ")):
        cands[f"{hw}|{i}"] = s.rsplit(": ", 1)[1].split(" / ")
cat = {r.split("\t")[1]: r.split("\t")[0] for r in (H / "pi1234-match.tsv").read_text(encoding="utf-8").splitlines()}
def rows(name):
    p = H / name
    if not p.exists(): return []
    out = []
    for n, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if not l.strip() or l.startswith("#"): continue
        k, t, why = l.split("\t")
        out.append((k, t, why))
    return out
errs = []
multi = rows("raw-multi.tsv")
mk = [k for k, _, _ in multi]
need = [k for k, c in cands.items() if len(c) > 1]
for k in set(need) - set(mk): errs.append(f"undecided {k}")
for k in set(mk) - set(need): errs.append(f"not multi {k}")
for k, n in collections.Counter(mk).items():
    if n > 1: errs.append(f"dup {k}")
groups = collections.OrderedDict([("1a", []), ("1b", []), ("1c", [])])
for k, t, w in multi:
    c = cat.get(k, "")
    g = "1a" if c == "MULTI_IN" else "1b" if c in ("MULTI_OUT", "MULTI_OUT_ABSENT") else "1c"
    groups[g].append((k, t, w))
parts = [("raw-align.tsv", "Part 2: single-candidate senses re-aligned to the LOCKED pi-4 / pi-3 / pi-2 / pi-1 term (same headword, same sense; the locked term occurs in the pi-5 text)"),
         ("raw-family.tsv", "Part 3: family re-alignments of single-candidate senses (one Burmese word per Pāli lemma and sense; family-scan-before.txt) and the synonym-list check"),
         ("raw-textinc.tsv", "Part 4: text inconsistencies of mapper-my/map-harmonise-notes.md §A decided by a term (single-candidate senses re-aligned)")]
if "--multi-only" in sys.argv: parts = []
allk = set(mk)
for f, _ in parts:
    for k, t, w in rows(f):
        if k in allk: errs.append(f"dup across parts {k} ({f})")
        allk.add(k)
        if k not in cands: errs.append(f"unknown {k} ({f})")
for f, _ in [("raw-multi.tsv", "")] + parts:
    for k, t, w in rows(f):
        for bad in (", ", " / ", "; ", "၊", "–", "—", " - "):
            if bad in t: errs.append(f"bad '{bad}' in {k}: {t}")
if errs:
    print("\n".join(errs)); sys.exit(1)
hdr = ["# pi-5 (Kathāvatthu) Pāli→Burmese plain termbase: decisions. hw|sense_index <TAB> term <TAB> reason",
       "# Built only from this book's own Burmese text (zero-shot, harmonise and mapping notes, my5-zeroshot-terms.md, the approved sample) and the LOCKED pi-4 / pi-3 / pi-2 / pi-1 termbases (with their APPROVED change notes). For review by the coordinator; not locked.",
       "# Order of the brief: (a) locked pi-4 / pi-3 / pi-2 / pi-1 term, (b) approved core term (burmese-style.md, my5-zeroshot-terms.md, the approved sample, harmonise), (c) most used form, (d) clearest plain candidate. Match tool: pi1234_match.py (pi1234-match.tsv); counts: multi_view.py (multi-view.txt).",
       "# A locked term is not taken where it never occurs in the pi-5 text (the pi-5 form is kept and reported), where the pi-5 sense tag is wider than the locked tag and the locked word would misread most uses (explained), or where an approved pi-5 sample form binds; every such case says «departs».",
       "#"]
names = {"1a": "Part 1a: multi-candidate senses where a locked termbase has the same headword and sense and its term is a candidate",
         "1b": "Part 1b: multi-candidate senses whose locked term is not among the candidates (or never occurs in the pi-5 text)",
         "1c": "Part 1c: multi-candidate senses without a locked entry for the same sense"}
out = hdr[:]
for g, items in groups.items():
    out.append(f"# {names[g]} ({len(items)})")
    out += [f"{k}\t{t}\t{w}" for k, t, w in items]
    out.append("#")
for f, title in parts:
    r = rows(f)
    out.append(f"# {title} ({len(r)})")
    out += [f"{k}\t{t}\t{w}" for k, t, w in r]
    out.append("#")
n5 = H / "notes-part5.txt"
if n5.exists() and parts:
    out += [l if l.startswith("#") else "# " + l for l in n5.read_text(encoding="utf-8").splitlines()]
(H / "decisions-A.tsv").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("decisions-A.tsv:", {g: len(v) for g, v in groups.items()}, {f: len(rows(f)) for f, _ in parts})
