# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 8-sattamanayo.md (Sattamanayo, method 7,
sampayuttena vippayuttaṃ).

usage: python -I -X utf8 build_8_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\8-sattamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's and this file's) still occurs
in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Formulas new to this chapter are listed in notes-8.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

CH = "8-sattamanayo.md"
N = 7  # method number (file 8)

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                  # Xena / Xāya ye dhammā
REL2 = "đối với những hiện tượng ấy, những hiện tượng nào"  # tehi dhammehi ye dhammā
ASSOC = "gắn liền với"                                     # sampayuttā
DISS = "không gắn liền với"                                # vippayuttā
TE = "những hiện tượng đó"                                 # te dhammā
Q_MAIN = f", thì {TE} {DISS} bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
KEHICI = "một số hiện tượng trong"                         # kehici (… kehici vippayuttā)
B.pi2("những hiện tượng đó")
B.pi2("Đối với")
B.pi1("những hiện tượng nào")
B.pi1("gắn liền với")
B.pi1("không gắn liền với")

# ---------------------------------------------------------------- members in the instrumental -> B.vi_item key
INSTR = {
    "vedanākkhandhena": "vedanākkhandho", "saññākkhandhena": "saññākkhandho",
    "saṅkhārakkhandhena": "saṅkhārakkhandho", "viññāṇakkhandhena": "viññāṇakkhandho",
    "manāyatanena": "manāyatanaṃ",
    "cakkhuviññāṇadhātuyā": "cakkhuviññāṇadhātu", "manodhātuyā": "manodhātu",
    "manoviññāṇadhātuyā": "manoviññāṇadhātu",
    "manindriyena": "manindriyaṃ", "upekkhindriyena": "upekkhindriyaṃ",
    # dependent-origination links: the instrumental keeps the link's name (B.PS_Q, quoted as in pi-2)
    "saṅkhārapaccayā viññāṇena": "saṅkhārapaccayā viññāṇaṃ",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "phassapaccayā vedanāya": "phassapaccayā vedanā",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā",
    "cittena": "cittaṃ", "manasikārena": "manasikāro", "adhimokkhena": "adhimokkho",
    # X-ehi dhammehi -> «các hiện tượng <pi-1 matrix predicate>»
    "adukkhamasukhāya vedanāya sampayuttehi dhammehi": "adukkhamasukhāya vedanāya sampayuttā dhammā",
    "upekkhāsahagatehi dhammehi": "upekkhāsahagatā dhammā",
    "savitakkasavicārehi dhammehi": "savitakkasavicārā dhammā",
    "cittehi dhammehi": "cittā dhammā", "cetasikehi dhammehi": "cetasikā dhammā",
    "cittasampayuttehi dhammehi": "cittasampayuttā dhammā",
    "cittasaṃsaṭṭhehi dhammehi": "cittasaṃsaṭṭhā dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānehi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānā dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūhi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi dhammehi": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā",
    "savitakkehi dhammehi": "savitakkā dhammā", "savicārehi dhammehi": "savicārā dhammā",
}


def member(p):
    p = p.strip()
    p = p[:1].lower() + p[1:]
    return B.vi_item(INSTR[p])


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā… Cena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, …»;
    returns (Vietnamese, pronoun for «gắn liền với nó / chúng»): «nó» after a singular X, «chúng» after
    X-ehi dhammehi (plural), as the shared frame gives «chúng» for tehi dhammehi."""
    parts = [x.strip() for x in chain.split("…")]
    out, plural = [], set()
    for x in parts:
        assert x.endswith(" ye dhammā"), (x, chain)
        key = x[:-len(" ye dhammā")]
        plural.add(key.endswith("dhammehi"))
        out.append(REL.format(x=member(key)))
    assert len(plural) == 1, chain                # no chain mixes singular and plural members
    return B.cap("… ".join(out)), (B.PRON_PL if plural.pop() else B.PRON_SG)


def dis(counts):
    """Answer predicate of vippayuttā, in the sample's B.excl shape with «không gắn liền với»:
    positive: 'không gắn liền với bốn khối, một lĩnh vực nhận biết, bảy yếu tố'
    na kehici …: 'không có khối nào, không có lĩnh vực nhận biết nào mà chúng không gắn liền với, nhưng …'"""
    parts = []
    for pos, items in B._runs(counts):
        if pos:
            parts.append(DISS + " " + ", ".join(B.count_phrase(n, noun) for n, noun in items))
        else:
            parts.append(", ".join(f"không có {noun} nào" for _, noun in items) + f" mà {B.PRON_PL} {DISS}")
    return ", nhưng ".join(parts)


def kehici_vi(a, d):
    """'ekenāyatanena ekāya dhātuyā kehici vippayuttā' -> 'không gắn liền với một số hiện tượng trong
    một lĩnh vực nhận biết, một yếu tố' (shared frame)."""
    return (f"{DISS} {KEHICI} {B.count_phrase(B._NA[a], B.AY)}, "
            f"{B.count_phrase(B._ND[d.split()[0]], B.DH)}")


_LINE = re.compile(
    r"^(?P<chain>.+?) sampayuttā, tehi dhammehi ye dhammā vippayuttā"
    r"(?:(?P<q>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi vippayuttā\? Te dhammā )|(?P<pe>… te dhammā ))"
    rf"(?P<c>{B.COUNTS_RX}) vippayuttā"
    r"(?:; (?P<ka>ekenāyatanena) (?P<kd>ekāya dhātuyā) kehici vippayuttā)?\.$")


def segment_vi(line):
    line = line.replace("…pe…", "…").replace(" …", "…")   # ^3-307 …pe…; ^3-314 stray space before «…»
    m = _LINE.match(line)
    assert m, line
    chain, pron = chain_vi(m.group("chain"))
    head = f"{chain} {ASSOC} {pron}, {REL2} {DISS} {B.PRON_PL}"
    tail = f"{Q_MAIN} {B.cap(TE)}" if m.group("q") else f"… {TE}"
    ans = dis(B.parse_counts(m.group("c")))
    if m.group("ka"):
        ans += "; " + kehici_vi(m.group("ka"), m.group("kd"))
    return f"{head}{tail} {ans}."


# ---------------------------------------------------------------- closing verse of ^3-316 (uddāna)
ADHIMUCCANA = B.pi2("sự khởi quyết định")       # adhimuccanā (pi-2 ^2 Paṭiccasamuppādavibhaṅga)
VITAKKA = B.pi2("sự hướng tâm")                 # vitakka
VICARA = B.pi2("sự duy trì tâm")                # vicāra / vicāraṇā
UPEKKHAKA = B.pi2("bình thản")                  # upekkhaka (pi-2 ^2-584 «“bình thản”»)
ANTARA = B.pi1("bộ đôi xen giữa")              # antarā (verse) = (các) bộ đôi xen giữa (pi-1 Cūḷantaraduka)
VERSE = {
    "Khandhā caturo āyatanañca mekaṃ;":
        f"{B.cap(B.NUM[4])} {B.KH} và {B.NUM[1]} {B.AY};",
    "Dhātūsu satta dvepi ca indriyato.":
        f"{B.cap(B.NUM[7])} trong các {B.DH}, và {B.NUM[2]} nữa từ các năng lực.",
    "Tayo paṭicca tathariva phassapañcamā;":
        f"{B.cap(B.NUM[3])} từ {B.OTHER['paṭiccasamuppādo']}, "
        f"nhóm {B.NUM[5]} mục bắt đầu bằng {B.OTHER['phasso']} cũng vậy;",
    "Adhimuccanā manasi tikesu tīṇi.":
        f"{B.cap(ADHIMUCCANA)}, {B.OTHER['manasikāro']}, {B.NUM[3]} trong các {B.SUBHEADINGS['Tikaṃ'].lower()}.",
    "Sattantarā dve ca manena yuttā;":
        f"{B.cap(B.NUM[7])} trong các {ANTARA}, và {B.NUM[2]} kết hợp với ý;",
    "Vitakkavicāraṇā upekkhakāya cāti.":
        f"{B.cap(VITAKKA)}, {VICARA} và điều {UPEKKHAKA}.",
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
                if title == "Sattamanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Sampayuttenavippayuttapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    raise AssertionError(line)
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body == "Sampayuttenavippayuttapadaniddeso sattamo.":
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
    assert "là là" not in text and "được được" not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
