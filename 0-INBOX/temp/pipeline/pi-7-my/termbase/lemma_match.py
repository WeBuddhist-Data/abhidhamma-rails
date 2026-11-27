"""Lemma-level comparison with the LOCKED pi-6 … pi-1 termbases (wider than pi123456_match.py, which needs the same
headword): every pi-7 sense whose headword has the same normalised lemma (family_scan.lemma: case endings, -ti / -ñca /
-ñceva / -pi / -yeva removed, the na- / no- polarity kept) as a locked headword, where none of the locked terms of that
lemma equals the pi-7 term. usage: lemma_match.py [> lemma-match.txt]"""
import pathlib, collections, sys
H = pathlib.Path(__file__).resolve().parent
B = H.parents[4]
# lemma() copied from family_scan.py
ENC = ["ñceva", "ñcā", "ñca", "mpi", "pi", "nti", "ti", "yeva", "eva"]
END = sorted(["ānaṃ", "ānañ", "assa", "āya", "ena", "ehi", "esu", "āni", "aṃ", "o", "ā", "e", "a", "ī", "iṃ", "issa",
              "īnaṃ", "inaṃ", "inā", "ino", "ūnaṃ", "uṃ", "u", "ū", "ussa", "uno", "āyaṃ", "iyā", "yā", "i", "ato", "to"],
             key=len, reverse=True)
def lemma(hw):
    h = hw.lower()
    neg = ""
    for p in ("nano", "na", "no"):
        if h.startswith(p) and len(h) > len(p) + 3 and h[len(p):len(p)+1] not in "ṃ":
            neg = p; h2 = h[len(p):]; break
    else:
        h2 = h
    for e in ENC:
        if h2.endswith(e) and len(h2) - len(e) >= 4: h2 = h2[: -len(e)]; break
    for e in END:
        if h2.endswith(e) and len(h2) - len(e) >= 3: h2 = h2[: -len(e)]; break
    return neg, h2

def parse(p):
    d = collections.OrderedDict()
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        hw, body = line.split(": {", 1)
        d[hw] = [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return d
s6 = parse(B / "AI_translation/burmese/pi-7-pali-word-burmese-senses-plain.md")
L = collections.defaultdict(list)
for n in (6, 5, 4, 3, 2, 1):
    for hw, ss in parse(B / f"AI_translation/burmese/pi-{n}-pali-burmese-termbase-plain.md").items():
        for tg, tm in ss:
            L[lemma(hw)].append((f"pi-{n}", hw, tg, tm))
n = 0
for hw, ss in s6.items():
    lk = L.get(lemma(hw), [])
    if not lk: continue
    for i, (tag, c) in enumerate(ss):
        cl = [x.strip() for x in c.split(" / ")]
        if any(tm in cl for _, _, _, tm in lk): continue
        n += 1
        print(f"{hw}|{i}: {c}   [{tag[:80]}]")
        for b, h1, tg, tm in lk[:6]: print(f"      {b} {h1}: {tm}   [{tg[:80]}]")
print(n, "senses whose lemma has locked terms, none equal", file=sys.stderr)
