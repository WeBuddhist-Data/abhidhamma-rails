# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 10-navamanayo.md (Navamanayo, method 9,
sampayuttena sampayuttaṃ).

usage: python -I -X utf8 build_10_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\10-navamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's and this file's) still occurs
in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Strings for Pāli shared with chapters 4, 6 and 8 are identical to build_4_vi.py / build_6_vi.py / build_8_vi.py.
Formulas new to this chapter are listed in notes-10.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

CH = "10-navamanayo.md"
N = 9  # method number (file 10)

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                  # Xena / Xāya / Xehi dhammehi ye dhammā
REL2_HEAD = "đối với những hiện tượng ấy"                  # tehi dhammehi
REL2_TAIL = ", những hiện tượng nào"                       # ye dhammā (second relative)
ASSOC = "gắn liền với"                                     # sampayuttā
TE = "những hiện tượng đó"                                 # te dhammā
Q_MAIN = f", thì {TE} {ASSOC} bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
KEHICI = "một số hiện tượng trong"                         # kehici (… kehici sampayuttā)
B.pi2("những hiện tượng đó")
B.pi2("Đối với")
B.pi1("những hiện tượng nào")
B.pi1("những hiện tượng ấy")
B.pi1("gắn liền với")

# ---------------------------------------------------------------- members in the instrumental -> B.vi_item key
INSTR = {
    "vedanākkhandhena": "vedanākkhandho", "saññākkhandhena": "saññākkhandho",
    "saṅkhārakkhandhena": "saṅkhārakkhandho", "viññāṇakkhandhena": "viññāṇakkhandho",
    "manāyatanena": "manāyatanaṃ",
    "cakkhuviññāṇadhātuyā": "cakkhuviññāṇadhātu", "manodhātuyā": "manodhātu",
    "manoviññāṇadhātuyā": "manoviññāṇadhātu",
    "samudayasaccena": "samudayasaccaṃ", "maggasaccena": "maggasaccaṃ",
    "manindriyena": "manindriyaṃ",
    "sukhindriyena": "sukhindriyaṃ", "dukkhindriyena": "dukkhindriyaṃ",
    "somanassindriyena": "somanassindriyaṃ", "domanassindriyena": "domanassindriyaṃ",
    "upekkhindriyena": "upekkhindriyaṃ", "saddhindriyena": "saddhindriyaṃ", "vīriyindriyena": "vīriyindriyaṃ",
    "satindriyena": "satindriyaṃ", "samādhindriyena": "samādhindriyaṃ", "paññindriyena": "paññindriyaṃ",
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
    "kammabhavena": "kammabhavo",
    "sokena": "soko", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ", "upāyāsena": "upāyāso",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "iddhipādena": "iddhipādo",
    "jhānena": "jhānaṃ", "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā",
    "cittena": "cittaṃ", "manasikārena": "manasikāro", "adhimokkhena": "adhimokkho",
    # X-ehi dhammehi -> «các hiện tượng <pi-1 matrix predicate>»
    "sukhāya vedanāya sampayuttehi dhammehi": "sukhāya vedanāya sampayuttā dhammā",
    "dukkhāya vedanāya sampayuttehi dhammehi": "dukkhāya vedanāya sampayuttā dhammā",
    "adukkhamasukhāya vedanāya sampayuttehi dhammehi": "adukkhamasukhāya vedanāya sampayuttā dhammā",
    "savitakkasavicārehi dhammehi": "savitakkasavicārā dhammā",
    "avitakkavicāramattehi dhammehi": "avitakkavicāramattā dhammā",
    "pītisahagatehi dhammehi": "pītisahagatā dhammā", "sukhasahagatehi dhammehi": "sukhasahagatā dhammā",
    "upekkhāsahagatehi dhammehi": "upekkhāsahagatā dhammā",
    "hetūhi dhammehi": "hetū dhammā",
    "hetūhi ceva sahetukehi ca dhammehi": "hetū ceva sahetukā ca dhammā",
    "hetūhi ceva hetusampayuttehi ca dhammehi": "hetū ceva hetusampayuttā ca dhammā",
    "sahetukehi ceva na ca hetūhi dhammehi": "sahetukā ceva na ca hetū dhammā",
    "hetusampayuttehi ceva na ca hetūhi dhammehi": "hetusampayuttā ceva na ca hetū dhammā",
    "na hetusahetukehi dhammehi": "na hetū sahetukā dhammā",     # compound spelling of the dyad name (as ch6)
    "āsavehi dhammehi": "āsavā dhammā",
    "āsavehi ceva sāsavehi ca dhammehi": "āsavā ceva sāsavā ca dhammā",
    "āsavehi ceva āsavasampayuttehi ca dhammehi": "āsavā ceva āsavasampayuttā ca dhammā",
    "āsavasampayuttehi ceva no ca āsavehi dhammehi": "āsavasampayuttā ceva no ca āsavā dhammā",
    "parāmāsehi dhammehi": "parāmāsā dhammā",
    "parāmāsehi ceva parāmaṭṭhehi ca dhammehi": "parāmāsā ceva parāmaṭṭhā ca dhammā",
    "parāmāsasampayuttehi dhammehi": "parāmāsasampayuttā dhammā",
    "cittehi dhammehi": "cittā dhammā", "cetasikehi dhammehi": "cetasikā dhammā",
    "cittasampayuttehi dhammehi": "cittasampayuttā dhammā",
    "cittasaṃsaṭṭhehi dhammehi": "cittasaṃsaṭṭhā dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānehi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānā dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūhi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā",
    "upādānehi dhammehi": "upādānā dhammā", "kilesehi dhammehi": "kilesā dhammā",
    "kilesehi ceva saṃkilesikehi ca dhammehi": "kilesā ceva saṃkilesikā ca dhammā",
    "kilesehi ceva saṃkiliṭṭhehi ca dhammehi": "kilesā ceva saṃkiliṭṭhā ca dhammā",
    "kilesehi ceva kilesasampayuttehi ca dhammehi": "kilesā ceva kilesasampayuttā ca dhammā",
    "saṃkiliṭṭhehi ceva no ca kilesehi dhammehi": "saṃkiliṭṭhā ceva no ca kilesā dhammā",
    "kilesasampayuttehi ceva no ca kilesehi dhammehi": "kilesasampayuttā ceva no ca kilesā dhammā",
    "savitakkehi dhammehi": "savitakkā dhammā", "savicārehi dhammehi": "savicārā dhammā",
    "sappītikehi dhammehi": "sappītikā dhammā",
}
# ^3-346: bare plural nouns without «dhammehi ye dhammā» (as written; strings of build_4_vi.py ^3-187)
BARE = {
    "saṃyojanehi": B.pi1("các xiềng xích"),
    "ganthehi": B.pi1("các nút thắt"),
    "oghehi": "các dòng lũ",          # pi-1 words («là dòng lũ», B.MATRIX_PRED oghā)
    "yogehi": "các ách",              # pi-1 words («là ách», B.MATRIX_PRED yogā)
    "nīvaraṇehi": B.pi1("các chướng ngại"),
}
VARIANTS = {   # ^3-343: placed after «tehi dhammehi», as in the Pāli
    "[na hetūhi sahetukehi (bahūsu)]": "[dị bản (nhiều bản): na hetūhi sahetukehi]",
}
PLURAL_END = ("ehi", "īhi", "ūhi")   # instrumental plural of the last member -> «chúng», else «nó»


def member(p):
    p = p.strip()
    p = p[:1].lower() + p[1:]
    if p in BARE:
        return BARE[p]
    return B.vi_item(INSTR[p])


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā… Cena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, …»;
    members without their own «ye dhammā» (^3-346) share the next «đối với …, những hiện tượng nào»
    (as build_4_vi.py). Returns (Vietnamese, pronoun): the pronoun of «gắn liền với nó / chúng» follows
    the Pāli number of the last member, the one next to «sampayuttā»."""
    parts = [x.strip() for x in chain.split("…")]
    assert parts[-1].endswith(" ye dhammā"), chain
    groups, cur = [], []
    for x in parts:
        if x.endswith(" ye dhammā"):
            cur.append(x[:-len(" ye dhammā")])
            groups.append(cur)
            cur = []
        else:
            cur.append(x)
    assert not cur, chain
    out = "… ".join(REL.format(x="… ".join(member(x) for x in g)) for g in groups)
    last = groups[-1][-1]
    pron = B.PRON_PL if last.endswith(PLURAL_END) else B.PRON_SG
    return B.cap(out), pron


_CK = r"(?:ekena khandhena|(?:dvīhi|tīhi|catūhi|pañcahi) khandhehi)"
_CA = r"(?:[a-zāīūṃṅñṭḍṇḷ]+āyatane(?:hi|na))"
_CD = r"(?:ekāya dhātuyā|[a-zāīūṃṅñṭḍṇḷ]+ dhātūhi)"


def counts_vi(s):
    """'tīhi khandhehi ekenāyatanena sattahi dhātūhi' -> 'ba khối, một lĩnh vực nhận biết, bảy yếu tố';
    any of the three may be absent ('tīhi khandhehi' -> 'ba khối')."""
    m = re.fullmatch(rf"(?:({_CK}) ?)?(?:({_CA}) ?)?({_CD})?", s)
    assert m and s, s
    k, a, d = m.groups()
    out = []
    if k:
        out.append(B.count_phrase(B._NK[k.split()[0]], B.KH))
    if a:
        out.append(B.count_phrase(B._NA[a], B.AY))
    if d:
        out.append(B.count_phrase(B._ND[d.split()[0]], B.DH))
    return ", ".join(out)


def answer_vi(ans):
    """'<counts> sampayuttā; <counts> kehici sampayuttā' (either part may stand alone)."""
    out = []
    for part in ans.split("; "):
        mk = re.fullmatch(r"(.+) kehici sampayuttā", part)
        if mk:
            out.append(f"{ASSOC} {KEHICI} {counts_vi(mk.group(1))}")
            continue
        mp = re.fullmatch(r"(.+) sampayuttā", part)
        assert mp, part
        out.append(f"{ASSOC} {counts_vi(mp.group(1))}")
    return "; ".join(out)


_LINE = re.compile(
    r"^(?P<chain>.+?) sampayuttā, tehi dhammehi(?P<var> \[[^\]]+\])? ye dhammā sampayuttā"
    r"(?:(?P<q>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā\? Te dhammā )|(?P<pe>… te dhammā ))"
    r"(?P<ans>.+)\.$")


def segment_vi(line):
    # ^3-320 «…pe…» -> «…»; ^3-323 / ^3-334 stray space before «…»
    line = line.replace("…pe…", "…").replace(" …", "…")
    m = _LINE.match(line)
    assert m, line
    chain, pron = chain_vi(m.group("chain"))
    var = (" " + VARIANTS[m.group("var").strip()]) if m.group("var") else ""
    head = f"{chain} {ASSOC} {pron}, {REL2_HEAD}{var}{REL2_TAIL} {ASSOC} {B.PRON_PL}"
    tail = f"{Q_MAIN} {B.cap(TE)}" if m.group("q") else f"… {TE}"
    return f"{head}{tail} {answer_vi(m.group('ans'))}."


# ---------------------------------------------------------------- closing verse of ^3-352 (uddāna)
ARUPA = B.MATRIX_PRED["arūpino"]                  # «phi vật chất» (pi-1 matrix arūpino)
VINNANADHATU = B.pi2("yếu tố thức")               # viññāṇadhātu (pi-2 ^2-172)
PITTHIDUKA = B.pi1("Bộ đôi cuối").lower()          # Piṭṭhidukaṃ (pi-1 matrix heading)
MAHANTARA = B.pi1("Bộ đôi xen giữa lớn").lower()   # mahantaraduka (pi-1; ch4 «các bộ đôi xen giữa lớn»)
GOCCHAKA = "nhóm"                                  # gocchaka (pi-1 Hetugocchakaṃ «Nhóm về gốc rễ»; ch4)
B.pi1("Nhóm về gốc rễ")
PADA = "mục"                                       # pada in the verses (ch4, ch8)
TIKA = B.SUBHEADINGS["Tikaṃ"].lower()              # «bộ ba» (ch8 «trong các bộ ba»)
NIDDESA_PADA = B.NIDDESA[:-len(" về")].lower()     # padassa niddese = «giải thích đề mục» (B.NIDDESA without «về»)
assert B.NIDDESA.endswith(" về")
VERSE = {
    "Arūpakkhandhā cattāro, manāyatanameva ca;":
        f"{B.cap(B.NUM[4])} {B.KH} {ARUPA}, và cả {B.AYATANA['manāyatanaṃ']};",
    "Viññāṇadhātuyo satta, dve saccā cuddasindriyā.":
        f"{B.cap(B.NUM[7])} {VINNANADHATU}, {B.NUM[2]} sự thật, {B.NUM[14]} năng lực.",
    "Paccaye dvādasa padā, tato upari soḷasa;":
        f"{B.cap(B.NUM[12])} {PADA} trong chuỗi điều kiện, tiếp theo đó là {B.NUM[16]};",
    "Tikesu aṭṭha gocchake, tecattālīsameva ca.":
        f"{B.cap(B.NUM[8])} trong các {TIKA}, và cả bốn mươi ba trong các {GOCCHAKA}.",
    "Mahantaraduke satta, padā piṭṭhi dukesu cha;":
        f"{B.cap(B.NUM[7])} trong các {MAHANTARA}, {B.NUM[6]} {PADA} trong các {PITTHIDUKA};",
    "Navamassa padassete, niddese saṅgahaṃ gatāti.":
        f"Các {PADA} này {B.INCL} phần {NIDDESA_PADA} {B.ORDINAL[N]}.",
}
B.pi2("năng lực")


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
                if title == "Navamanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Sampayuttenasampayuttapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    raise AssertionError(line)
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body == "Sampayuttenasampayuttapadaniddeso navamo.":
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
    assert "là là" not in text and "được được" not in text and " …" not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
