# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 12 (12-ekadasamanayo.md, Ekādasamanayo, method 11,
saṅgahitena sampayuttaṃ vippayuttaṃ).

usage: python -I -X utf8 build_12_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\12-ekadasamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's and this file's) still occurs
in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Reuses build_sample_vi (B) verbatim: the relative clause and inclusion modifiers as in chapter 5, the association
answers as in chapters 7-9. Formulas settled for this chapter are listed in notes-12.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

CH = "12-ekadasamanayo.md"
N = 11  # method number (file 12)

# ---------------------------------------------------------------- shared frames (coordinator)
REL = "đối với {x}, những hiện tượng nào"                     # Xena / Xāya / Xehi ye dhammā
MOD_INCL = ", ".join(f"{B.INCL} theo cách gộp vào {n}" for n in B.NOUNS)
#   khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā (as chapter 5)
ASSOC = B.pi1("gắn liền với")                                # sampayuttā
DISS = B.pi1("không gắn liền với")                           # vippayuttā
TE = B.pi2("những hiện tượng đó")                            # te dhammā
Q_MAIN = f", thì {TE} {ASSOC} bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
#   , te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā(ti)?
NATTHI = "Không có."                                         # Natthi.
Q_DISS = B.cap(DISS) + " bao nhiêu?"                          # Katihi vippayuttā?
KEHICI = "một số hiện tượng trong"                           # kehici
B.pi1("những hiện tượng nào")
B.pi2("Đối với")

# ---------------------------------------------------------------- members in the instrumental -> B.vi_item key
INSTR = {
    "samudayasaccena": "samudayasaccaṃ", "maggasaccena": "maggasaccaṃ",
    "avijjāya": "avijjā",
    # dependent-origination links: the instrumental keeps the link's name (B.PS_Q, quoted as in pi-2;
    # saṅkhārehi plural = chapter 5's saṅkhārena, the same link)
    "avijjāpaccayā saṅkhārehi": "avijjāpaccayā saṅkhārā",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "kammabhavena": "kammabhavo", "paridevena": "paridevo",
    "sokena": "soko", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ", "upāyāsena": "upāyāso",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "cetanāya": "cetanā", "adhimokkhena": "adhimokkho", "manasikārena": "manasikāro",
    # X-ehi dhammehi -> «các hiện tượng <pi-1 matrix predicate>» (chapters 4, 5)
    "hetūhi dhammehi": "hetū dhammā",
    "hetūhi ceva sahetukehi ca dhammehi": "hetū ceva sahetukā ca dhammā",
    "hetūhi ceva hetusampayuttehi ca dhammehi": "hetū ceva hetusampayuttā ca dhammā",
    "āsavehi dhammehi": "āsavā dhammā",
    "āsavehi ceva sāsavehi ca dhammehi": "āsavā ceva sāsavā ca dhammā",
    "āsavehi ceva āsavasampayuttehi ca dhammehi": "āsavā ceva āsavasampayuttā ca dhammā",
    "saṃyojanehi dhammehi": "saṃyojanā dhammā", "ganthehi dhammehi": "ganthā dhammā",
    "oghehi dhammehi": "oghā dhammā", "yogehi dhammehi": "yogā dhammā",
    "nīvaraṇehi dhammehi": "nīvaraṇā dhammā", "parāmāsehi dhammehi": "parāmāsā dhammā",
    "upādānehi dhammehi": "upādānā dhammā", "kilesehi dhammehi": "kilesā dhammā",
    "kilesehi ceva saṃkilesikehi ca dhammehi": "kilesā ceva saṃkilesikā ca dhammā",
    "kilesehi ceva saṃkiliṭṭhehi ca dhammehi": "kilesā ceva saṃkiliṭṭhā ca dhammā",
    "kilesehi ceva kilesasampayuttehi ca dhammehi": "kilesā ceva kilesasampayuttā ca dhammā",
}
for _k in B.INDRIYA:                                          # itthindriyaṃ -> itthindriyena
    _s = re.sub(r"aṃ$", "ena", unicodedata.normalize("NFC", _k))
    assert _s.endswith("ena"), _k
    INSTR[_s] = _k


def member(p):
    p = p.strip()
    p = p[:1].lower() + p[1:]
    return B.vi_item(INSTR[p])


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, những hiện tượng nào»."""
    parts = [x.strip() for x in chain.split("…")]
    out = []
    for x in parts:
        assert x.endswith(" ye dhammā"), (x, chain)
        out.append(REL.format(x=member(x[:-len(" ye dhammā")])))
    return B.cap("… ".join(out))


# ---------------------------------------------------------------- counts and answer clauses
_SLOT = re.compile(
    r"^(?:(?P<k>ekena khandhena|(?:dvīhi|tīhi|catūhi|pañcahi) khandhehi) )?"
    r"(?:(?P<a>[a-zāīūṃṅñṭḍṇḷ]+āyatane(?:na|hi)) )?"
    r"(?:(?P<d>ekāya dhātuyā|[a-zāīūṃṅñṭḍṇḷ]+ dhātūhi) )?"
    r"(?P<keh>kehici )?(?P<v>sampayuttā|vippayuttā)$")


def clause_vi(c, first):
    """'tīhi khandhehi ekenāyatanena sattahi dhātūhi sampayuttā' -> 'gắn liền với ba khối, một lĩnh vực nhận
    biết, bảy yếu tố'; '… kehici vippayuttā' -> 'không gắn liền với một số hiện tượng trong …'."""
    c = c[:1].lower() + c[1:]
    m = _SLOT.match(c)
    assert m and (m.group("k") or m.group("a") or m.group("d")), c
    slots = []
    if m.group("k"):
        slots.append(B.count_phrase(B._NK[m.group("k").split()[0]], B.KH))
    if m.group("a"):
        slots.append(B.count_phrase(B._NA[m.group("a")], B.AY))
    if m.group("d"):
        slots.append(B.count_phrase(B._ND[m.group("d").split()[0]], B.DH))
    verb = ASSOC if m.group("v") == "sampayuttā" else DISS
    s = verb + " " + (KEHICI + " " if m.group("keh") else "") + ", ".join(slots)
    return B.cap(s) if first else s


def statement_vi(s, first_cap):
    """'A sampayuttā; B kehici sampayuttā.' -> Vietnamese (clauses joined by '; ')."""
    assert s.endswith("."), s
    cl = s[:-1].split("; ")
    return "; ".join(clause_vi(c, first_cap and i == 0) for i, c in enumerate(cl)) + "."


MOD_PALI = " khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā"
Q_PALI = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā"
SLIPS = []  # (block ID, note) of Pāli rendered as meant; reported


def segment_vi(line, bid):
    i = line.index(MOD_PALI)
    chain, rest = line[:i], line[i + len(MOD_PALI):]
    out = chain_vi(chain) + " " + MOD_INCL
    if rest.startswith(Q_PALI + "? Te dhammā "):              # question + full answer
        out += f"{Q_MAIN} {B.cap(TE)} "
        rest = rest[len(Q_PALI + "? Te dhammā "):]
    elif rest.startswith(Q_PALI + "ti? Natthi. "):           # question + «Natthi.»
        out += f"{Q_MAIN} {NATTHI} "
        rest = rest[len(Q_PALI + "ti? Natthi. "):]
    elif rest.startswith(("…pe… te dhammā ", "… te dhammā ")):  # shortened: «… những hiện tượng đó …»
        out += f"… {TE} "
        rest = rest.split(" te dhammā ", 1)[1]
    elif rest.startswith(" te dhammā "):                      # ^3-413: comma missing before «te dhammā»
        out += f", {B.THI} {TE} "
        SLIPS.append((bid, "comma missing before 'te dhammā' (rendered ', thì những hiện tượng đó')"))
        rest = rest[len(" te dhammā "):]
    else:
        raise AssertionError(line)
    sents = re.split(r"(?<=[.?]) ", rest)
    vi = []
    for k, s in enumerate(sents):
        if s == "Katihi vippayuttā?":
            vi.append(Q_DISS)
        else:
            # the statement right after «Những hiện tượng đó» / «… những hiện tượng đó» stays lower-case
            vi.append(statement_vi(s, first_cap=(k > 0)))
    return out + " ".join(vi)


# ---------------------------------------------------------------- summary verse of ^3-416 and closing
GOCCHAKA = "nhóm"                     # gocchaka (pi-1 Hetugocchakaṃ «Nhóm về gốc rễ»), as chapter 5
B.pi1("Nhóm về gốc rễ")
PADA = "đề mục"                       # pada, as chapter 5
B.pi2("sự thật")
B.pi2("năng lực")
FIXED = {
    # identical Pāli in chapter 5 (^3-192): identical Vietnamese
    "Dve saccā pannarasindriyā, ekādasa paṭiccapadā;":
        f"Hai sự thật, {B.NUM[15]} năng lực, {B.NUM[11]} {PADA} về {B.OTHER['paṭiccasamuppādo']};",
    "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti.":
        f"Tiếp theo lại có {B.NUM[11]}, ở đây các {PADA} thuộc các {GOCCHAKA} có ba mươi loại.",
    "Saṅgahitenasampayuttavippayuttapadaniddeso ekādasamo.": B.niddesa_closing(N),
}


# ---------------------------------------------------------------- build
def build():
    out = []
    for seg in B._segments(os.path.join(B.PALI_DIR, CH)):
        bid_seg = B.ID.search(seg[-1]).group(1)
        vi = []
        for i, line in enumerate(seg):
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip() if bid else line.strip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                t = {"Ekādasamanayo": B.CHAPTER_TITLES[N + 1],
                     "Saṅgahitenasampayuttavippayuttapadaniddeso": B.niddesa_heading(N)}[title]
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in FIXED:
                t = FIXED[body]
            else:
                assert i == 0, line
                t = segment_vi(body, bid_seg)
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
    for b, note in SLIPS:
        print(f"as meant: {b}: {note}")


if __name__ == "__main__":
    main()
