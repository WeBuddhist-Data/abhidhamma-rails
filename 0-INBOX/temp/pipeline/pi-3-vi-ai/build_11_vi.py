# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 11-dasamanayo.md (Dasamanayo, method 10,
vippayuttena vippayuttaṃ).

usage: python -I -X utf8 build_11_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\11-dasamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's, ch7's, ch8's and this file's)
still occurs in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Frames are taken verbatim from build_8_vi (E8: relative chain, «… với chúng», answers, kehici) and the
closing verse from build_7_vi (E7.VERSE, the same Pāli verse). Formulas new to this chapter: notes-11.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_7_vi as E7       # noqa: E402  (importing writes nothing)
import build_8_vi as E8       # noqa: E402  (importing writes nothing)

CH = "11-dasamanayo.md"
N = 10  # method number (file 11)

# ---------------------------------------------------------------- shared frames (verbatim from ch8)
REL, REL2, DISS, TE, Q_MAIN = E8.REL, E8.REL2, E8.DISS, E8.TE, E8.Q_MAIN
assert REL == "đối với {x}, những hiện tượng nào"
assert REL2 == "đối với những hiện tượng ấy, những hiện tượng nào"
assert DISS == "không gắn liền với" and TE == "những hiện tượng đó"

# ---------------------------------------------------------------- members in the instrumental
# singular (and non-«dhammehi») members -> B.vi_item key (Pāli nominative)
SING = {
    "rūpakkhandhena": "rūpakkhandho", "vedanākkhandhena": "vedanākkhandho",
    "saññākkhandhena": "saññākkhandho", "saṅkhārakkhandhena": "saṅkhārakkhandho",
    "viññāṇakkhandhena": "viññāṇakkhandho",
    "manāyatanena": "manāyatanaṃ", "cakkhāyatanena": "cakkhāyatanaṃ", "phoṭṭhabbāyatanena": "phoṭṭhabbāyatanaṃ",
    "cakkhudhātuyā": "cakkhudhātu", "phoṭṭhabbadhātuyā": "phoṭṭhabbadhātu",
    "cakkhuviññāṇadhātuyā": "cakkhuviññāṇadhātu", "manoviññāṇadhātuyā": "manoviññāṇadhātu",
    "samudayasaccena": "samudayasaccaṃ", "maggasaccena": "maggasaccaṃ", "nirodhasaccena": "nirodhasaccaṃ",
    "cakkhundriyena": "cakkhundriyaṃ", "kāyindriyena": "kāyindriyaṃ", "itthindriyena": "itthindriyaṃ",
    "purisindriyena": "purisindriyaṃ", "manindriyena": "manindriyaṃ", "sukhindriyena": "sukhindriyaṃ",
    "dukkhindriyena": "dukkhindriyaṃ", "somanassindriyena": "somanassindriyaṃ",
    "domanassindriyena": "domanassindriyaṃ", "upekkhindriyena": "upekkhindriyaṃ",
    "saddhindriyena": "saddhindriyaṃ", "vīriyindriyena": "vīriyindriyaṃ", "satindriyena": "satindriyaṃ",
    "samādhindriyena": "samādhindriyaṃ", "paññindriyena": "paññindriyaṃ",
    "anaññātaññassāmītindriyena": "anaññātaññassāmītindriyaṃ", "aññindriyena": "aññindriyaṃ",
    "aññātāvindriyena": "aññātāvindriyaṃ",
    "avijjāya": "avijjā",
    # dependent-origination links: the instrumental keeps the link's name (B.PS_Q, quoted as in pi-2)
    "avijjāpaccayā saṅkhārehi": "avijjāpaccayā saṅkhārā",
    "saṅkhārapaccayā viññāṇena": "saṅkhārapaccayā viññāṇaṃ",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "phassapaccayā vedanāya": "phassapaccayā vedanā",
    "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "kammabhavena": "kammabhavo", "rūpabhavena": "rūpabhavo", "arūpabhavena": "arūpabhavo",
    "asaññābhavena": "asaññābhavo", "nevasaññānāsaññābhavena": "nevasaññānāsaññābhavo",
    "ekavokārabhavena": "ekavokārabhavo", "catuvokārabhavena": "catuvokārabhavo",
    "sokena": "soko", "paridevena": "paridevo", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ",
    "upāyāsena": "upāyāso",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "iddhipādena": "iddhipādo",
    "jhānena": "jhānaṃ", "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā",
    "cittena": "cittaṃ", "manasikārena": "manasikāro", "adhimokkhena": "adhimokkho",
}
# X-ehi dhammehi -> X-ā dhammā (matrix names); word-level exceptions to the -ehi / -īhi / -ūhi rule
WORD_EXC = {"cittasaṃsaṭṭhasamuṭṭhānasahabhūhi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno"}
FIX = {"na hetusahetukā dhammā": "na hetū sahetukā dhammā"}   # compound spelling, as ch7 ^3-279 (reported)
VARIANTS = {"[anupādiṇṇehi (sī. ka.)]": "[dị bản (Sī., Ka.): anupādiṇṇehi]"}   # ^3-397


def nominative(key):
    """'kusalehi dhammehi' -> 'kusalā dhammā'; 'ācayagāmīhi dhammehi' -> 'ācayagāmino dhammā';
    'hetūhi ceva sahetukehi ca dhammehi' -> 'hetū ceva sahetukā ca dhammā'."""
    assert key.endswith("dhammehi"), key
    out = []
    for w in key.split():
        if w in WORD_EXC:
            out.append(WORD_EXC[w])
        elif w.endswith("ehi"):
            out.append(w[:-3] + "ā")
        elif w.endswith("īhi"):
            out.append(w[:-3] + "ino")
        elif w.endswith("ūhi"):
            out.append(w[:-3] + "ū")
        else:
            out.append(w)          # ceva, ca, na, no, dassanena, bhāvanāya, sukhāya, vedanāya …
    nom = " ".join(out)
    return FIX.get(nom, nom)


def member(p):
    """One instrumental member (lower-case Vietnamese) and whether it is plural."""
    p = p.strip()
    p = p[:1].lower() + p[1:]
    var = ""
    m = re.fullmatch(r"(.+?) (\[[^\]]+\]) (dhammehi)", p)
    if m:
        p, var = f"{m.group(1)} {m.group(3)}", " " + VARIANTS[m.group(2)]
    plural = p.split()[-1].endswith(("ehi", "īhi", "ūhi"))
    v = B.vi_item(SING[p]) if p in SING else B.vi_item(nominative(p))
    return v + var, plural


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā… Cena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, …»;
    the pronoun of «… không gắn liền với nó / chúng» follows the number of the last member (the one the
    predicate stands next to): «chúng» after a plural instrumental (X-ehi dhammehi, saṅkhārehi), else «nó»."""
    parts = [x.strip() for x in chain.split("…")]
    out, last_plural = [], None
    for x in parts:
        assert x.endswith(" ye dhammā"), (x, chain)
        v, last_plural = member(x[:-len(" ye dhammā")])
        out.append(REL.format(x=v))
    return B.cap("… ".join(out)), (B.PRON_PL if last_plural else B.PRON_SG)


_LINE = re.compile(
    r"^(?P<chain>.+?) vippayuttā, tehi dhammehi ye dhammā vippayuttā"
    r"(?:(?P<q>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi vippayuttā\? Te dhammā )|(?P<pe>… te dhammā ))"
    rf"(?P<c>{B.COUNTS_RX}) vippayuttā"
    r"(?:; (?P<ka>ekenāyatanena) (?P<kd>ekāya dhātuyā) kehici vippayuttā)?\.$")


def segment_vi(line):
    line = line.replace("…pe…", "…")
    line = line.replace("ye dhammā.. ", "ye dhammā… ")   # ^3-357 'kāyindriyena ye dhammā..' (punctuation slip)
    m = _LINE.match(line)
    assert m, line
    chain, pron = chain_vi(m.group("chain"))
    head = f"{chain} {DISS} {pron}, {REL2} {DISS} {B.PRON_PL}"
    tail = f"{Q_MAIN} {B.cap(TE)}" if m.group("q") else f"… {TE}"
    ans = E8.dis(B.parse_counts(m.group("c")))
    if m.group("ka"):
        ans += "; " + E8.kehici_vi(m.group("ka"), m.group("kd"))
    return f"{head}{tail} {ans}."


# ---------------------------------------------------------------- closing verse of ^3-408 (= ch7 ^3-305 verse)
VERSE = {k: v for k, v in E7.VERSE.items() if not k.startswith("Sampayogavippayogapadaniddeso")}
assert len(VERSE) == 6


def build():
    out = []
    for seg in B._segments(os.path.join(B.PALI_DIR, CH)):
        vi = []
        for i, line in enumerate(seg):
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip() if bid else line.strip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                if title == "Dasamanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Vippayuttenavippayuttapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    t = B.SUBHEADINGS[title]
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body == "Vippayuttenavippayuttapadaniddeso dasamo.":
                t = B.niddesa_closing(N)
            else:
                assert i == 0, line
                t = segment_vi(body)
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = B.check_sources()
    text = build()
    assert unicodedata.normalize("NFC", text) == text
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text and "pe…" not in text
    assert "là là" not in text and "được được" not in text and ".." not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
