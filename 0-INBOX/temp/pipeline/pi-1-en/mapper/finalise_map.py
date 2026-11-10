"""Finalise the pi-1 Pāli=English keyword map (coordinator, 2026-11-10).

1. Long spans (4+ Pāli words) that an English multiword fragment produced are replaced by the Pāli head words
   joined with " / " (the §4 join rule), so no value is a whole clause. Earlier books (pi-3…pi-6) have at most
   one or two values of 4+ words.
2. ñassāmi (a non-word cut from anaññātaññassāmītindriyaṃ) becomes the whole compound (conventions §8).
3. Every replacement must consist of words present in that segment's Pāli (checked).

in:  mapper/assembled-raw.md
out: AI_translation/english/pi-1-keywords-by-reference-pali-english-plain.md
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[4]
SRC = HERE / "assembled-raw.md"
OUT = ROOT / "AI_translation" / "english" / "pi-1-keywords-by-reference-pali-english-plain.md"
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"

# exact old Pāli value -> new value (English side unchanged)
LONG = {
    "kiriyahetu kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā cattāro ñāṇavippayutte cittuppāde ṭhapetvā tīsu bhūmīsu kiriyesu uppajjati": "kiriyahetu / uppajjati",
    "hetu kāmāvacarakusalato cattāro ñāṇavippayutte cittuppāde ṭhapetvā catūsu bhūmīsu kusalesu uppajjati": "hetu / uppajjati",
    "kusalahetu kāmāvacarakusalato cattāro ñāṇavippayutte cittuppāde ṭhapetvā catūsu bhūmīsu kusalesu uppajjati": "kusalahetu / uppajjati",
    "kiriyahetu kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā tīsu bhūmīsu kiriyesu uppajjanti": "kiriyahetu / uppajjanti",
    "hetu catūsu bhūmīsu kusalesu uppajjanti": "hetu / uppajjanti",
    "kusalahetu catūsu bhūmīsu kusalesu uppajjanti": "kusalahetu / uppajjanti",
    "dhammā neva dassanena na bhāvanāya pahātabbahetukā": "dhammā / pahātabbahetukā",
    "dhammā na bhāvanāya pahātabbahetukā": "dhammā / pahātabbahetukā",
    "dhammā na dassanena pahātabbahetukā": "dhammā / pahātabbahetukā",
    "Diṭṭhi catūsu diṭṭhigatasampayuttesu cittuppādesu uppajjati": "Diṭṭhi / uppajjati",
    "Diṭṭhiparāmāso catūsu diṭṭhigatasampayuttesu cittuppādesu uppajjati": "Diṭṭhiparāmāso / uppajjati",
    "avacaraṃ kusalaṃ cittaṃ uppannaṃ hoti": "avacaraṃ / uppannaṃ",
    "ganthavippayuttā kho pana dhammā ganthaniyā": "ganthavippayuttā / ganthaniyā",
    "kilesavippayuttā kho pana dhammā saṃkilesikā": "kilesavippayuttā / saṃkilesikā",
    "nīvaraṇavippayuttā kho pana dhammā nīvaraṇiyā": "nīvaraṇavippayuttā / nīvaraṇiyā",
    "saṃyojanavippayuttā kho pana dhammā saṃyojaniyā": "saṃyojanavippayuttā / saṃyojaniyā",
    "upādānavippayuttā kho pana dhammā upādāniyā": "upādānavippayuttā / upādāniyā",
    "vippayuttā kho pana dhammā": "vippayuttā / dhammā",
    "abhijjhādomanassā pāpakā akusalā dhammā": "abhijjhādomanassā / dhammā",
    "dhamme ārabbha ye uppajjanti": "dhamme / ārabbha / uppajjanti",
    "ganthā ceva dhammā ganthaniyā": "ganthā / ganthaniyā",
    "nīvaraṇā ceva dhammā nīvaraṇiyā": "nīvaraṇā / nīvaraṇiyā",
    "saṃyojanā ceva dhammā saṃyojaniyā": "saṃyojanā / saṃyojaniyā",
    "upādānā ceva dhammā upādāniyā": "upādānā / upādāniyā",
    "mohena hetu ceva hetu": "mohena / hetu",
    "mohena hetu ceva sahetuko": "mohena / hetu",
    "rūpaṃ manasā viññātaṃ rūpaṃ": "rūpaṃ",
    "samaye catūhi vacīduccaritehi ārati": "samaye / ārati",
    "samaye tīhi kāyaduccaritehi ārati": "samaye / ārati",
    "samuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ": "samuṭṭhānaṃ / manokammaṃ",
    "vattabbā sukhāya vedanāya sampayuttā": "vattabbā",
}


def feeling(pali, en):
    """The pleasant/painful feeling strings: keep the contact word, the pleasant/painful word if the English has it,
    and the head noun."""
    w = pali.split()
    if len(w) != 4:
        return None
    contact, _comfort, tone, head = w
    if "pleasant" in en.lower() or "painful" in en.lower():
        return f"{contact} / {tone} / {head}"
    return f"{contact} / {head}"


FEEL = re.compile(r"^(\S*samphassaj[aā]ṃ?) (a?sāt[aā]ṃ?) (\S+) (vedayitaṃ|vedanā)$")


def pali_words(seg_text):
    return set(re.findall(r"[^\s,.;:?!()\[\]–\"'‘’“”]+", seg_text))


# segment texts by id
seg = {}
for p in PALI_DIR.glob("*.md"):
    buf = []
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", line)
        if m:
            seg[m.group(1)] = " ".join(buf)
            buf = []

out, n_long, n_frag, bad = [], 0, 0, []
for line in SRC.read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    sid = i[1:]
    seg_text = seg.get(sid, "")
    pairs = []
    for p in body.split(", "):
        pali, en = p.rsplit("=", 1)
        new = pali
        if pali in LONG:
            new = LONG[pali]
        elif FEEL.match(pali):
            new = feeling(pali, en)
        if new != pali:
            n_long += 1
            for part in new.split(" / "):
                for w in part.split():
                    # substring: compound members cut as the agents did; a word-initial a fused to ā (sandhi) is fine
                    if w not in seg_text and not (w[:1] in "aA" and ("ā" + w[1:]) in seg_text):
                        bad.append((sid, w, new))
        if "ñassāmi" in new.split(" / ") or new == "ñassāmi":
            new = " / ".join("anaññātaññassāmītindriyaṃ" if q == "ñassāmi" else q for q in new.split(" / "))
            n_frag += 1
        pairs.append(f"{new}={en}")
    out.append(f"{i}] " + ", ".join(pairs))

if bad:
    print("replacement words not in the segment's Pāli:", bad[:20])
    sys.exit(1)
left = [(l.split("] ")[0], q) for l in out for p in l.split("] ", 1)[1].split(", ")
        for q in [p.rsplit("=", 1)[0]] if q != "(no direct equivalent)" and any(len(x.split()) >= 4 for x in q.split(" / "))]
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print(f"long spans replaced {n_long}, ñassāmi replaced {n_frag}, values still 4+ words: {len(left)} {left[:5]}")
print("wrote", OUT, len(out), "lines")
