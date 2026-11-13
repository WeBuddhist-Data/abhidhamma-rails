"""Inventory of clauses in 3-03..3-08 after gocchaka normalization (no files written).
usage: python -I -B -X utf8 analyze_3-03_3-08.py [--top N] [--grep pattern]"""
import collections
import os
import re
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]

# (S stem, A stem, G stem) per file
NORM = {
    "3-03": [("sāsav", "SG"), ("anāsav", "aSG"), ("āsav", "GG")],
    "3-04": [("saññojaniy", "SG"), ("asaññojaniy", "aSG"), ("saññojan", "GG")],
    "3-05": [("ganthaniy", "SG"), ("aganthaniy", "aSG"), ("ganth", "GG")],
    "3-06": [],
    "3-07": [("nīvaraṇiy", "SG"), ("anīvaraṇiy", "aSG"), ("nīvaraṇ", "GG")],
    "3-08": [("parāmaṭṭh", "SG"), ("aparāmaṭṭh", "aSG"), ("parāmās", "GG")],
}
ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def lower_initials(s):
    return re.sub(r"(?<!\w)([A-ZĀĪŪṄÑṬḌṆḶṂ])", lambda m: m.group(1).lower(), s)


def normalize(key, text):
    text = lower_initials(text)
    for stem, tok in NORM[key]:
        text = re.sub(rf"(?<!\w)(no)?{stem}", lambda m: (m.group(1) or "") + tok, text)
    return text


def clauses(text):
    text = re.sub(r"\([^()]*\)", " ", text)
    for c in re.split(r" – |; |\. |…pe…|…|\.$|, ", text):
        c = c.strip(" .")
        if c:
            yield c


if __name__ == "__main__":
    cnt = collections.Counter()
    notes = collections.Counter()
    where = {}
    for f in FILES:
        key = f[:4]
        for ln in open(os.path.join(PALI, f), encoding="utf-8").read().splitlines():
            if not ln.strip() or ln.startswith("#"):
                continue
            body = ID_RE.sub("", ln)
            body = normalize(key, body)
            for n in re.findall(r"\([^()]*\)", body):
                notes[n] += 1
            for c in clauses(body):
                cnt[c] += 1
                where.setdefault(c, f[:4])
    print("unique clauses", len(cnt), "total", sum(cnt.values()), "unique notes", len(notes))
    if "--notes" in sys.argv:
        for n, k in notes.most_common():
            print(k, n)
    if "--all" in sys.argv:
        for c, k in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
            print(k, where[c], c)
