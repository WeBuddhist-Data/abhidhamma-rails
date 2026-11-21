# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 4 (Tatiyanayo, asaṅgahitena saṅgahitaṃ).

usage: python -I -X utf8 build_4_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\4-tatiyanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's and this file's) still occurs
in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

CH = "4-tatiyanayo.md"
N = 3  # method number (file 4)

# ---------------------------------------------------------------- shared frames (coordinator)
REL_HEAD = "đối với"                       # X-ena / X-āya (instrumental of relation)
REL_TAIL = "những hiện tượng nào"           # ye dhammā
BY_KH = "theo cách gộp vào khối"            # khandhasaṅgahena
BY_AY = "theo cách gộp vào lĩnh vực nhận biết"  # āyatanasaṅgahena
BY_DH = "theo cách gộp vào yếu tố"          # dhātusaṅgahena
# khandhasaṅgahena asaṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā
PRED = f"{B.EXCL} {BY_KH}, {B.INCL} {BY_AY}, {B.INCL} {BY_DH}"
TE = "những hiện tượng đó"                  # te dhammā
Q_MAIN = f", thì {TE} được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"

# ---------------------------------------------------------------- members in the instrumental -> B.vi_item key
INSTR = {
    "vedanākkhandhena": "vedanākkhandho", "saññākkhandhena": "saññākkhandho",
    "saṅkhārakkhandhena": "saṅkhārakkhandho",
    "samudayasaccena": "samudayasaccaṃ", "maggasaccena": "maggasaccaṃ", "nirodhasaccena": "nirodhasaccaṃ",
    "jīvitindriyena": "jīvitindriyaṃ", "itthindriyena": "itthindriyaṃ", "purisindriyena": "purisindriyaṃ",
    "sukhindriyena": "sukhindriyaṃ", "dukkhindriyena": "dukkhindriyaṃ",
    "somanassindriyena": "somanassindriyaṃ", "domanassindriyena": "domanassindriyaṃ",
    "upekkhindriyena": "upekkhindriyaṃ", "saddhindriyena": "saddhindriyaṃ", "vīriyindriyena": "vīriyindriyaṃ",
    "satindriyena": "satindriyaṃ", "samādhindriyena": "samādhindriyaṃ", "paññindriyena": "paññindriyaṃ",
    "anaññātaññassāmītindriyena": "anaññātaññassāmītindriyaṃ", "aññindriyena": "aññindriyaṃ",
    "aññātāvindriyena": "aññātāvindriyaṃ",
    "avijjāya": "avijjā",
    # dependent-origination links: the instrumental keeps the link's name (B.PS_Q, quoted as in pi-2)
    "avijjāpaccayā saṅkhārena": "avijjāpaccayā saṅkhārā",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "phassapaccayā vedanāya": "phassapaccayā vedanā",
    "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "kammabhavena": "kammabhavo",
    "jātiyā": "jāti", "jarāya": "jarā", "maraṇena": "maraṇaṃ", "jhānena": "jhānaṃ",
    "sokena": "soko", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ", "upāyāsena": "upāyāso",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā",
    "adhimokkhena": "adhimokkho", "manasikārena": "manasikāro",
    # X-ehi dhammehi -> «các hiện tượng <pi-1 matrix predicate>»
    "hetūhi dhammehi": "hetū dhammā",
    "hetūhi ceva sahetukehi ca dhammehi": "hetū ceva sahetukā ca dhammā",
    "hetūhi ceva hetusampayuttehi ca dhammehi": "hetū ceva hetusampayuttā ca dhammā",
    "appaccayehi dhammehi": "appaccayā dhammā", "asaṅkhatehi dhammehi": "asaṅkhatā dhammā",
    "āsavehi dhammehi": "āsavā dhammā",
    "āsavehi ceva sāsavehi ca dhammehi": "āsavā ceva sāsavā ca dhammā",
    "āsavehi ceva āsavasampayuttehi ca dhammehi": "āsavā ceva āsavasampayuttā ca dhammā",
    "parāmāsehi dhammehi": "parāmāsā dhammā",
    "parāmāsehi ceva parāmaṭṭhehi ca dhammehi": "parāmāsā ceva parāmaṭṭhā ca dhammā",
    "cetasikehi dhammehi": "cetasikā dhammā", "cittasampayuttehi dhammehi": "cittasampayuttā dhammā",
    "cittasaṃsaṭṭhehi dhammehi": "cittasaṃsaṭṭhā dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānehi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānā dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūhi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā",
    "cittasahabhūmi dhammehi": "cittasahabhuno dhammā",   # ^3-189: spelling slip for cittasahabhūhi
    "cittānuparivattīhi dhammehi": "cittānuparivattino dhammā",
    "upādānehi dhammehi": "upādānā dhammā", "kilesehi dhammehi": "kilesā dhammā",
    "kilesehi ceva saṃkilesikehi ca dhammehi": "kilesā ceva saṃkilesikā ca dhammā",
    "kilesehi ceva saṃkiliṭṭhehi ca dhammehi": "kilesā ceva saṃkiliṭṭhā ca dhammā",
    "kilesehi ceva kilesasampayuttehi ca dhammehi": "kilesā ceva kilesasampayuttā ca dhammā",
}
# ^3-187: bare plural nouns without «dhammehi ye dhammā» (translated as written)
BARE = {
    "saṃyojanehi": B.pi1("các xiềng xích"),
    "ganthehi": B.pi1("các nút thắt"),
    "oghehi": "các dòng lũ",          # pi-1 words («là dòng lũ», B.MATRIX_PRED oghā)
    "yogehi": "các ách",              # pi-1 words («là ách», B.MATRIX_PRED yogā)
    "nīvaraṇehi": B.pi1("các chướng ngại"),
}
VARIANTS = {
    "[upādānapaccayā kammabhavena (syā.)]": "[dị bản (Syā.): upādānapaccayā kammabhavena]",
    "[cullantaradukā (sī.)]": "[khác chính tả (Sī.): cullantaradukā]",
}

# ---------------------------------------------------------------- closing verse of ^3-190 (uddāna)
B.pi1("Nhóm về gốc rễ")            # gocchaka = nhóm
B.pi1("Bộ đôi xen giữa nhỏ")       # cūḷantaraduka
B.pi1("Bộ đôi xen giữa lớn")       # mahantaraduka
VERSE = {
    "Tayo khandhā tathā saccā, indriyāni ca soḷasa;":
        "Ba khối, ba sự thật cũng vậy, và mười sáu năng lực;",
    "Padāni paccayākāre, cuddasūpari cuddasa.":
        "Các mục trong chuỗi điều kiện, mười bốn, rồi thêm mười bốn.",
    "Samatiṃsa padā honti, gocchakesu dasasvatha;":
        "Có tròn ba mươi mục, trong mười nhóm;",
    "Duve cūḷantaradukā [cullantaradukā (sī.)], aṭṭha honti mahantarāti.":
        "Rồi hai mục trong các bộ đôi xen giữa nhỏ " + VARIANTS["[cullantaradukā (sī.)]"]
        + ", tám mục trong các bộ đôi xen giữa lớn.",
}


def member(p):
    """One instrumental member (lower-case Vietnamese)."""
    p = p.strip()
    p = p[:1].lower() + p[1:]
    m = re.fullmatch(r"(.*?) (\[[^\]]+\])", p)
    if m:
        return member(m.group(1)) + " " + VARIANTS[m.group(2)]
    if p in BARE:
        return BARE[p]
    return B.vi_item(INSTR[p])


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā… C ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, …»;
    members without their own «ye dhammā» (^3-187) share the next «đối với … , những hiện tượng nào»."""
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
    out = "… ".join(f"{REL_HEAD} " + "… ".join(member(x) for x in g) + f", {REL_TAIL}" for g in groups)
    return B.cap(out)


_LINE = re.compile(
    r"^(?P<chain>.+?) khandhasaṅgahena asaṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā"
    r"(?:(?P<q>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā\? Te dhammā)"
    r"|(?P<pe>…(?:pe…)? te dhammā))"
    rf"(?P<asx> asaṅkhataṃ khandhato ṭhapetvā)? (?P<inc>{B.COUNTS_RX}) saṅgahitā\.$")


def segment_vi(line):
    m = _LINE.match(line)
    assert m, line
    head = f"{chain_vi(m.group('chain'))} {PRED}"
    pred = B.incl(B.parse_counts(m.group("inc")))
    if m.group("q"):
        subj = B.cap(TE)
        tail = f"{Q_MAIN} {subj}"
    else:
        tail = f"… {TE}"
    if m.group("asx"):
        return f"{head}{tail}, {B.ASX}, {pred}."
    return f"{head}{tail} {pred}."


def build():
    out = []
    for seg in B._segments(os.path.join(B.PALI_DIR, CH)):
        vi = []
        for line in seg:
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                if title == "Tatiyanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Asaṅgahitenasaṅgahitapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    raise AssertionError(line)
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body == "Asaṅgahitenasaṅgahitapadaniddeso tatiyo.":
                t = B.niddesa_closing(N)
            else:
                # normalise the stray space before «…» in ^3-187 «Saṃyojanehi … ganthehi»
                t = segment_vi(body.replace(" …", "…"))
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = B.check_sources()
    text = build()
    assert unicodedata.normalize("NFC", text) == text
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text and "pe…" not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
