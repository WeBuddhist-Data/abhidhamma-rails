"""Builder for the Vietnamese rails of pi-3 chapter 10 (Navamanayo, «Phương pháp thứ chín», ^3-319 .. ^3-352),
plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/10-navamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/10-navamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the approved
formulas (rails/vi-rails-formulas.md: ch10 frame, «X tīhi khandhehi … sampayutto.», «; ekena khandhena … kehici
sampayutto.»). All shared strings are imported from build_rails_sample_vi (read-only); the approved strings are
asserted against the formulas file and the pi-1 / pi-2 strings against those rails. Elided items «Xena ye dhammā…»
use the ch3-ch8 form «những hiện tượng nào cùng với X…»; bare cluster nouns (Saṃyojanehi… ganthehi…) use the ch5
form «cùng với các xiềng xích…»; answer parts follow ch7 (sampayutta answers, kehici); the abridged
«sampayuttā… te dhammā» follows ch8. New strings: notes-rails-10.md.

usage: python -I -X utf8 build_rails_10_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "10-navamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== frame pieces (approved ch3-15 formulas)
WHICH = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                  # X-ena on an elided item (as ch3-ch8)
THOSE_REF = "các hiện tượng đó"                    # tehi dhammehi
TE = "những hiện tượng ấy"                         # te dhammā
ASSOC = "gắn liền với"                             # sampayuttā (+ instrumental)
SOME = "một số hiện tượng thuộc"                   # kehici (termbase «một số hiện tượng»; as ch7 / ch8)
Q_ASSOC = f"{ASSOC} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?"


def frame10(x_vi, variant=""):
    """Xena ye dhammā sampayuttā, tehi dhammehi [variant] ye dhammā sampayuttā"""
    return f"{WHICH} {ASSOC} {x_vi}; {WHICH} {ASSOC} {THOSE_REF}{variant}"


# variant note placed after «tehi dhammehi» in ^3-343 (kept at the same spot; sigla as pi-1 «(nhiều ấn bản)»;
# «dị bản» as ch6 for the identical reading «na hetūhi sahetukehi»)
VARIANTS = {"[na hetūhi sahetukehi (bahūsu)]": " " + S.reading("nhiều ấn bản", "na hetūhi sahetukehi")}

# ================================================================== reference items in the instrumental
N = S.NAMES
INSTR = {  # instrumental Pāli -> Vietnamese name (S.NAMES, unchanged)
    "vedanākkhandhena": N["vedanākkhandho"], "saññākkhandhena": N["saññākkhandho"],
    "saṅkhārakkhandhena": N["saṅkhārakkhandho"], "viññāṇakkhandhena": N["viññāṇakkhandho"],
    "manāyatanena": N["manāyatanaṃ"],
    "cakkhuviññāṇadhātuyā": N["cakkhuviññāṇadhātu"], "manodhātuyā": N["manodhātu"],
    "manoviññāṇadhātuyā": N["manoviññāṇadhātu"],
    "samudayasaccena": N["samudayasaccaṃ"], "maggasaccena": N["maggasaccaṃ"],
    "manindriyena": N["manindriyaṃ"], "sukhindriyena": N["sukhindriyaṃ"], "dukkhindriyena": N["dukkhindriyaṃ"],
    "somanassindriyena": N["somanassindriyaṃ"], "domanassindriyena": N["domanassindriyaṃ"],
    "upekkhindriyena": N["upekkhindriyaṃ"], "saddhindriyena": N["saddhindriyaṃ"],
    "vīriyindriyena": N["vīriyindriyaṃ"], "satindriyena": N["satindriyaṃ"],
    "samādhindriyena": N["samādhindriyaṃ"], "paññindriyena": N["paññindriyaṃ"],
    "anaññātaññassāmītindriyena": N["anaññātaññassāmītindriyaṃ"], "aññindriyena": N["aññindriyaṃ"],
    "aññātāvindriyena": N["aññātāvindriyaṃ"],
    "avijjāya": N["avijjā"],
    "avijjāpaccayā saṅkhārehi": N["avijjāpaccayā saṅkhārā"],
    "saṅkhārapaccayā viññāṇena": N["saṅkhārapaccayā viññāṇaṃ"],
    "saḷāyatanapaccayā phassena": N["saḷāyatanapaccayā phasso"],
    "phassapaccayā vedanāya": N["phassapaccayā vedanā"],
    "vedanāpaccayā taṇhāya": N["vedanāpaccayā taṇhā"],
    "taṇhāpaccayā upādānena": N["taṇhāpaccayā upādānaṃ"],
    "kammabhavena": "sự hiện hữu dưới dạng nghiệp",       # (pi-2), without the ch2 variant bracket (as ch5 / ch6)
    "sokena": N["soko"], "dukkhena": N["dukkhaṃ"], "domanassena": N["domanassaṃ"], "upāyāsena": N["upāyāso"],
    "satipaṭṭhānena": N["satipaṭṭhānaṃ"], "sammappadhānena": N["sammappadhānaṃ"],
    "iddhipādena": N["iddhipādo"], "jhānena": N["jhānaṃ"], "appamaññāya": N["appamaññā"],
    "pañcahi indriyehi": N["pañcindriyāni"], "pañcahi balehi": N["pañca balāni"],
    "sattahi bojjhaṅgehi": N["satta bojjhaṅgā"], "ariyena aṭṭhaṅgikena maggena": N["ariyo aṭṭhaṅgiko maggo"],
    "phassena": N["phasso"], "cetanāya": N["cetanā"], "manasikārena": N["manasikāro"],
    "vedanāya": N["vedanā"], "saññāya": N["saññā"], "cittena": N["cittaṃ"], "adhimokkhena": N["adhimokkho"],
}
ATTR = {  # X-ehi dhammehi -> key of S.DHAMMA_ATTR («các hiện tượng X», unchanged)
    "sukhāya vedanāya sampayuttehi": "sukhāya vedanāya sampayuttā",
    "dukkhāya vedanāya sampayuttehi": "dukkhāya vedanāya sampayuttā",
    "adukkhamasukhāya vedanāya sampayuttehi": "adukkhamasukhāya vedanāya sampayuttā",
    "savitakkasavicārehi": "savitakkasavicārā", "avitakkavicāramattehi": "avitakkavicāramattā",
    "pītisahagatehi": "pītisahagatā", "sukhasahagatehi": "sukhasahagatā", "upekkhāsahagatehi": "upekkhāsahagatā",
    "hetūhi": "hetū", "hetūhi ceva sahetukehi ca": "hetū ceva sahetukā ca",
    "hetūhi ceva hetusampayuttehi ca": "hetū ceva hetusampayuttā ca",
    "sahetukehi ceva na ca hetūhi": "sahetukā ceva na ca hetū",
    "hetusampayuttehi ceva na ca hetūhi": "hetusampayuttā ceva na ca hetū",
    "na hetusahetukehi": "na hetū sahetukā",            # compound spelling, rendered as meant (as ch6 / ch7)
    "āsavehi": "āsavā", "āsavehi ceva sāsavehi ca": "āsavā ceva sāsavā ca",
    "āsavehi ceva āsavasampayuttehi ca": "āsavā ceva āsavasampayuttā ca",
    "āsavasampayuttehi ceva no ca āsavehi": "āsavasampayuttā ceva no ca āsavā",
    "parāmāsehi": "parāmāsā", "parāmāsehi ceva parāmaṭṭhehi ca": "parāmāsā ceva parāmaṭṭhā ca",
    "parāmāsasampayuttehi": "parāmāsasampayuttā",
    "cittehi": "cittā", "cetasikehi": "cetasikā", "cittasampayuttehi": "cittasampayuttā",
    "cittasaṃsaṭṭhehi": "cittasaṃsaṭṭhā", "cittasaṃsaṭṭhasamuṭṭhānehi": "cittasaṃsaṭṭhasamuṭṭhānā",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūhi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
    "upādānehi": "upādānā", "kilesehi": "kilesā",
    "kilesehi ceva saṃkilesikehi ca": "kilesā ceva saṃkilesikā ca",
    "kilesehi ceva saṃkiliṭṭhehi ca": "kilesā ceva saṃkiliṭṭhā ca",
    "kilesehi ceva kilesasampayuttehi ca": "kilesā ceva kilesasampayuttā ca",
    "saṃkiliṭṭhehi ceva no ca kilesehi": "saṃkiliṭṭhā ceva no ca kilesā",
    "kilesasampayuttehi ceva no ca kilesehi": "kilesasampayuttā ceva no ca kilesā",
    "savitakkehi": "savitakkā", "savicārehi": "savicārā", "sappītikehi": "sappītikā",
}
# bare instrumental cluster nouns (no «dhammehi», no «ye dhammā»): identical to build_rails_5_vi.py BARE
BARE = {"saṃyojanehi": "các xiềng xích", "ganthehi": "các nút thắt", "oghehi": "các dòng lũ",
        "yogehi": "các ách", "nīvaraṇehi": "các chướng ngại"}
used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR[k[: -len(' dhammehi')]]]}"
    else:
        v = INSTR[k]
    used.append(v)
    return v


# ================================================================== answer parts (as ch7, sampayutta only)
PART = re.compile(r"^(?:(?P<k>ekena khandhena|\S+ khandhehi) ?)?"
                  r"(?:(?P<a>\S+āyatanena|\S+āyatanehi) ?)?"
                  r"(?:(?P<d>ekāya dhātuyā|\S+ dhātūhi) ?)?"
                  r"(?P<keh>kehici )?sampayuttā$")


def _num(cat, s):
    if cat == S.KHANDHA:
        return S.K_NUM[s.split()[0]]
    if cat == S.AYATANA:
        return S.A_NUM[re.sub(r"āyatane(?:hi|na)$", "", s)]
    return S.D_NUM[s.split()[0]]


def part_vi(p):
    p = p[0].lower() + p[1:]
    m = PART.match(p)
    assert m, p
    nums = [(c, _num(c, m.group(g))) for c, g in zip(S.CATS, "kad") if m.group(g)]
    assert nums, p
    if m.group("keh"):
        return f"{ASSOC} {SOME} {S.counts_vi(nums)}"
    return f"{ASSOC} {S.counts_vi(nums)}"


def answer_vi(a):
    """'tīhi khandhehi … sampayuttā; ekenāyatanena ekāya dhātuyā kehici sampayuttā' -> «gắn liền với …; …»"""
    return "; ".join(part_vi(x) for x in a.split("; "))


# ================================================================== segment grammar
YE = " ye dhammā"
SEG = re.compile(r"^(?P<subj>.*?) ye dhammā sampayuttā, tehi dhammehi(?P<var> \[[^\]]+\])? ye dhammā sampayuttā"
                 r"(?P<mid>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā\? Te dhammā "
                 r"|…pe… te dhammā |… te dhammā )(?P<ans>.+)\.$")


def subject(p, variant):
    items = [x.strip() for x in p.replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        if it.endswith(YE):
            parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
        else:
            parts.append(f"{WITH} {BARE[it[0].lower() + it[1:]]}")
    parts.append(frame10(ref_vi(items[-1]), variant))
    return S.cap("… ".join(parts))


def content_line(p):
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    var = VARIANTS[m.group("var").strip()] if m.group("var") else ""
    subj = subject(m.group("subj"), var)
    ans = answer_vi(m.group("ans"))
    if m.group("mid").startswith(", te dhammā katihi"):
        return f"{subj}, {S.THEN} {TE} {Q_ASSOC} {S.cap(TE)} {ans}."
    return f"{subj}…, {TE} {ans}."                    # sampayuttā…(pe…) te dhammā (abridged question)


# ================================================================== summary verse (uddāna) of ^3-352, lines 2-7
PADA = "đề mục"                                        # padā / padassa (verse), as ch4 / ch5 / ch7
VERSE = {
    "Arūpakkhandhā cattāro, manāyatanameva ca;":
        f"Bốn {S.KHANDHA} phi vật chất, và cũng có {N['manāyatanaṃ']};",
    "Viññāṇadhātuyo satta, dve saccā cuddasindriyā.":
        f"Bảy {S.DHATU} thức, hai sự thật, mười bốn năng lực.",
    "Paccaye dvādasa padā, tato upari soḷasa;":
        f"Trong phần điều kiện có mười hai {PADA}, tiếp theo đó có mười sáu;",
    "Tikesu aṭṭha gocchake, tecattālīsameva ca.":
        f"Trong các {S.low(S.SUB_HEADINGS['Tikaṃ'])} có tám, và trong các nhóm cũng có bốn mươi ba.",
    "Mahantaraduke satta, padā piṭṭhi dukesu cha;":
        f"Trong các bộ đôi xen giữa lớn có bảy, trong các bộ đôi cuối có sáu {PADA};",
    "Navamassa padassete, niddese saṅgahaṃ gatāti.":
        f"Những điều này đã được gộp vào trong phần giải thích {PADA} thứ chín.",
}
REUSE10 = [  # (Pāli, Vietnamese as reused, book)
    ("Piṭṭhidukaṃ (heading)", "bộ đôi cuối", 1),
    ("Mahantaradukaṃ", "bộ đôi xen giữa lớn", 1),
    ("Dve saccā", "hai sự thật", 2),
    ("(bahūsu)", "(nhiều ấn bản)", 1),
]


def translate_segment(lines):
    out = []
    for ln in lines:
        if ln.startswith("#"):
            out.append(S.heading_vi(ln))
        elif ln in S.CLOSINGS:
            out.append(S.CLOSINGS[ln])
        elif ln in VERSE:
            out.append(VERSE[ln])
        else:
            out.append(content_line(ln))
    return out


def render():
    blocks = []
    for lines, bid in S.pali_segments(S.PALI / NAME):
        vi = translate_segment(lines)
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


# ================================================================== checks against the approved formulas
def _formula(key):
    txt = FORMULAS.read_text(encoding="utf-8")
    line = next(ln for ln in txt.splitlines() if ln.startswith(key))
    return line.split(" = ", 1)[1].replace(" (proposed for ch3-15)", "")


def check_formulas():
    # ch10 frame (question)
    f = _formula("Xena ye dhammā sampayuttā, tehi dhammehi ye dhammā sampayuttā, te dhammā")
    got = f"{S.cap(frame10('X'))}, {S.THEN} {TE} {Q_ASSOC}"
    assert got == f, f"ch10 frame differs:\n{got}\n{f}"
    # «; ekena khandhena ekenāyatanena ekāya dhātuyā kehici sampayutto.»
    f = _formula("; ekena khandhena ekenāyatanena ekāya dhātuyā kehici sampayutto.")
    got = "; " + part_vi("ekena khandhena ekenāyatanena ekāya dhātuyā kehici sampayuttā") + "."
    assert got == f, f"{got}\n{f}"
    # «X tīhi khandhehi … sampayutto.»
    f = _formula("X tīhi khandhehi … sampayutto.")
    assert f == f"X {part_vi('tīhi khandhehi sampayuttā')}, ….", f
    # ch7 notes: «; ekenāyatanena ekāya dhātuyā kehici sampayutto.»
    assert part_vi("ekenāyatanena ekāya dhātuyā kehici sampayuttā") == \
        "gắn liền với một số hiện tượng thuộc một lĩnh vực nhận biết và một yếu tố."[:-1]


def check_reuse10():
    t = {1: "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_DIR.glob("*.md"))).lower(),
         2: "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI2_DIR.glob("*.md"))).lower()}
    missing = [f"(pi-{b}) {p} = {v}" for p, v, b in REUSE10 if v.lower() not in t[b]]
    assert not missing, missing


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_reuse10()
    check_formulas()
    txt = render()
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    tagged = sorted({v for v in used if S.reuse_tag(v)})
    print(f"{NAME}: {n} segments; {len(set(used))} reference names ({len(tagged)} with pi-1/pi-2 tag); "
          f"{n_reuse + len(REUSE10)} pi-1/pi-2 strings asserted")
