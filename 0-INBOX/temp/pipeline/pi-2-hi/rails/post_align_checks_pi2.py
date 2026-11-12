"""Post-alignment checks: sample prefix (first 77 non-empty lines of ch1) unchanged vs backup and vs sample-1/1-sample.md;
preamble unchanged; no CR, no double blank lines, no «—», no «:-», no Latin words outside [ ] brackets;
blank-line layout identical to the backup (only line contents may change).
usage: python -I -X utf8 post_align_checks_pi2.py"""
import os, re
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
HDIR = ROOT + r"\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
HERE = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(HERE, "backup-pre-align")


def ne(t):
    return [l for l in t.split("\n") if l.strip()]


cur1 = open(os.path.join(HDIR, "1-khandhavibhango.md"), encoding="utf-8").read()
bak1 = open(os.path.join(BAK, "1-khandhavibhango.md"), encoding="utf-8").read()
smp = open(os.path.join(HERE, "sample-1", "1-sample.md"), encoding="utf-8").read()
print("sample prefix == backup:", ne(cur1)[:77] == ne(bak1)[:77])
print("sample prefix == sample-1/1-sample.md:", ne(cur1)[:77] == ne(smp)[:77], f"(sample file has {len(ne(smp))} lines)")
print("preamble unchanged:", open(os.path.join(HDIR, "preamble.md"), encoding="utf-8").read() ==
      open(os.path.join(BAK, "preamble.md"), encoding="utf-8").read())
bad = 0
for f in sorted(os.listdir(HDIR)):
    t = open(os.path.join(HDIR, f), encoding="utf-8", newline="").read()
    b = open(os.path.join(BAK, f), encoding="utf-8", newline="").read()
    probs = []
    if "\r" in t: probs.append("CR")
    if "\n\n\n" in t: probs.append("double blank")
    if "—" in t: probs.append("em dash")
    if ":-" in t: probs.append(":-")
    if [bool(l.strip()) for l in t.split("\n")] != [bool(l.strip()) for l in b.split("\n")]: probs.append("blank layout")
    lat = []
    for l in t.split("\n"):
        s = re.sub(r"\[[^\]]*\]", "", l)
        s = re.sub(r"\^[\w-]+\s*$", "", s)
        lat += re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", s)
    blat = []
    for l in b.split("\n"):
        s = re.sub(r"\[[^\]]*\]", "", l)
        s = re.sub(r"\^[\w-]+\s*$", "", s)
        blat += re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", s)
    if lat: probs.append(f"latin outside brackets: {len(lat)} (backup {len(blat)}) {sorted(set(lat))[:8]}")
    if probs:
        bad += 1
    print(f"{f}: {'; '.join(probs) or 'OK'}")
print("files with problems:", bad)
