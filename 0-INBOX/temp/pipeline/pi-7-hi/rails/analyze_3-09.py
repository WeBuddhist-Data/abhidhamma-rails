"""Analysis helper for 3-09-mahantaraduka.md: split lines into pieces, abstract dyad items, count unique pieces."""
import re
import sys
from collections import Counter, OrderedDict

SRC = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters\3-09-mahantaraduka.md"

DYADS = OrderedDict([
    ("Sārammaṇadukaṃ", ("sārammaṇ", "anārammaṇ")),
    ("Cittadukaṃ", ("citt", "nocitt")),
    ("Cetasikadukaṃ", ("cetasik", "acetasik")),
    ("Cittasampayuttadukaṃ", ("cittasampayutt", "cittavippayutt")),
    ("Cittasaṃsaṭṭhadukaṃ", ("cittasaṃsaṭṭh", "cittavisaṃsaṭṭh")),
    ("Cittasamuṭṭhānadukaṃ", ("cittasamuṭṭhān", "nocittasamuṭṭhān")),
    ("Cittasahabhūdukaṃ", ("cittasahabh", "nocittasahabh")),
    ("Cittānuparivattidukaṃ", ("cittānuparivatt", "nocittānuparivatt")),
    ("Cittasaṃsaṭṭhasamuṭṭhānadukaṃ", ("cittasaṃsaṭṭhasamuṭṭhān", "nocittasaṃsaṭṭhasamuṭṭhān")),
    ("Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", ("cittasaṃsaṭṭhasamuṭṭhānasahabh", "nocittasaṃsaṭṭhasamuṭṭhānasahabh")),
    ("Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ", ("cittasaṃsaṭṭhasamuṭṭhānānuparivatt", "nocittasaṃsaṭṭhasamuṭṭhānānuparivatt")),
    ("Ajjhattikadukaṃ", ("ajjhattik", "bāhir")),
    ("Upādādukaṃ", ("upādā", "noupādā")),
    ("Upādinnadukaṃ", ("upādinn", "anupādinn")),
])

SPLIT = re.compile(r"( – |; |, |\. |…pe…|…|\(|\)|\.$)")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "pieces"
    cur = None
    cnt = Counter()
    first = {}
    for no, ln in enumerate(open(SRC, encoding="utf-8").read().split("\n"), 1):
        if not ln.strip():
            continue
        body = re.sub(r" \^[0-9A-Za-z-]+\s*$", "", ln)
        if ln.startswith("#"):
            m = re.match(r"#+ \*?(.*?)\*?$", body)
            if m.group(1) in DYADS:
                cur = m.group(1)
            continue
        if mode == "lines":
            print(no, body)
            continue
        if mode == "abs" and cur:
            ps, ns = DYADS[cur]
            ends = r"(aṃ|o|ā|e|assa|ānaṃ|añca|ū|uṃ|uno|ussa|ūnaṃ|uñca|u|i|iṃ|ino|issa|īnaṃ|iñca|ī|ādhipati|a)?"
            body = re.sub(rf"(?<!\w){ns}{ends}(?!\w)", lambda m: "NN" + (m.group(1) or ""), body, flags=re.I)
            body = re.sub(rf"(?<!\w){ps}{ends}(?!\w)", lambda m: "PP" + (m.group(1) or ""), body, flags=re.I)
        for p in SPLIT.split(body):
            p = p.strip()
            if not p or SPLIT.fullmatch(" " + p + " ") or p in ("–", ";", ",", ".", "…pe…", "…", "(", ")"):
                continue
            cnt[p] += 1
            first.setdefault(p, no)
    for p, c in sorted(cnt.items(), key=lambda x: first[x[0]]):
        print(f"{first[p]}\t{c}\t{p}")
    print(len(cnt), "unique pieces", file=sys.stderr)


if __name__ == "__main__":
    main()
