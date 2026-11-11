"""Apply the four term changes the user approved after the bilingual review (2026-11-11).

usage: python -I -X utf8 apply_term_changes.py [--write]
Backup: backup-pre-terms/. Log: term-changes-log.tsv. Writes only if every rule hits its expected count.
"""
import collections, pathlib, re, shutil, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
import hz_common as H

HDIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters")
HERE = pathlib.Path(__file__).parent
WRITE = "--write" in sys.argv

# (name, Pāli-line regex or None, Hindi regex, replacement, expected matches)
RULES = [
    ("saṃkilesika neg", r"saṃkilesik", r"क्लेशों की ओर न ले जाने वाल", "क्लेशों का विषय न बनने वाल", 17),
    ("saṃkilesika", r"saṃkilesik", r"क्लेशों की ओर ले जाने वाल", "क्लेशों का विषय बनने वाल", 38),
    ("kāyena 3rd jhāna", r"kāyena paṭisaṃvedeti", r"शरीर से सुख", "काया से सुख", 1),
    ("lokuttara sammappadhāna", r"sammappadhānaṃ", r"लोकोत्तर सही प्रयास", "लोकोत्तर सही प्रयत्न", 4),
    ("asārāgo", r"asārāgo", r"(?<!प्रबल )राग का अभाव", "प्रबल राग का अभाव", 7),
]

log, cnt, new_text = [], collections.Counter(), {}
for part in H.PARTS:
    p = HDIR / f"{part}.md"
    raw = p.read_text(encoding="utf-8").split("\n")
    pali = H.lines(str(pathlib.Path(H.PDIR) / f"{part}.md"))
    idx = [i for i, l in enumerate(raw) if l.strip()]
    assert len(idx) == len(pali), part
    for n, i in enumerate(idx):
        l = nl = raw[i]
        for name, prx, hrx, rep, _ in RULES:
            if prx and not re.search(prx, pali[n], re.I):
                continue
            nl, k = re.subn(hrx, rep, nl)
            cnt[name] += k
        if nl != l:
            log.append((part, i + 1, l, nl))
            raw[i] = nl
            new_text[p] = "\n".join(raw)

for name, *_, want in RULES:
    print(f"{cnt[name]:5} / {want:<5} {name}")
print("lines changed", len(log), "files", sorted(x.name[:4] for x in new_text))
bad = [name for name, *_, want in RULES if cnt[name] != want]
if bad:
    sys.exit(f"unexpected counts, nothing written: {bad}")
if WRITE:
    bak = HERE / "backup-pre-terms"
    bak.mkdir(exist_ok=True)
    for p, t in new_text.items():
        if not (bak / p.name).exists():
            shutil.copy2(p, bak / p.name)
        p.write_text(t, encoding="utf-8", newline="\n")
    (HERE / "term-changes-log.tsv").write_text("\n".join("\t".join(map(str, r)) for r in log) + "\n", encoding="utf-8", newline="\n")
    print("written")
else:
    print("(dry run; add --write)")
