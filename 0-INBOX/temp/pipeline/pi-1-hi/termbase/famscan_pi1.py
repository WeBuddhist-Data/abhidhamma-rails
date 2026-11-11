"""Whole-book lemma-family scan of the assembled pi-1 Pāli→Hindi plain termbase.

Groups headwords by a rough Pāli base (one-word headwords, common case endings and clitics stripped; letter case merged) and
reports bases whose senses carry more than one Hindi term after a rough Hindi normalisation (final vowel/oblique merged).
Output: famscan.txt (one family per block, with tags); prints the number of families.
"""
import collections, pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md"
OUT = pathlib.Path(__file__).parent / "famscan.txt"
ENDS = ("assāpi", "ānañca", "esuceva", "anti", "assa", "ānaṃ", "ehi", "esu", "āya", "ena", "ato", "smiṃ", "mhi", "ānī", "āni",
        "ṃ", "ā", "o", "e", "ī", "ū", "i", "u", "a")
CLIT = ("meva", "ñceva", "ceva", "ñca", "nti", "ti", "pi", "ca")


def base(hw):
    w = hw.lower()
    changed = True
    while changed:
        changed = False
        for c in CLIT:
            if w.endswith(c) and len(w) - len(c) >= 4:
                w = w[: -len(c)]; changed = True; break
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 3:
            return w[: -len(e)]
    return w


def norm(t):
    t = re.sub(r"(ा|ी|े|ों|एँ|ाएँ)(?=\s|$)", "", t)
    return re.sub(r"\s+", " ", t).strip()


fam = collections.defaultdict(list)
for l in TB.read_text(encoding="utf-8").splitlines():
    hw, body = l.split(": {", 1)
    if " " in hw:
        continue
    for s in body[:-1].split("; "):
        tag, t = s.rsplit(": ", 1)
        fam[base(hw)].append((hw, tag, t))

blocks = []
for b, xs in fam.items():
    if len({norm(t) for _, _, t in xs}) > 1:
        blocks.append((len(xs), b, xs))
blocks.sort(key=lambda x: (-x[0], x[1]))
with OUT.open("w", encoding="utf-8", newline="\n") as f:
    for n, b, xs in blocks:
        f.write(f"== {b} ({n})\n")
        for hw, tag, t in xs:
            f.write(f"  {hw}\t{t}\t{tag}\n")
print(f"families with >1 Hindi term: {len(blocks)} of {len(fam)} -> {OUT.name}")
