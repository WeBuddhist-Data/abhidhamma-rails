"""Builder for the Vietnamese rails of pi-3 chapter 8 (Sattamanayo, «Phương pháp thứ bảy», ^3-306 .. ^3-316),
plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/8-sattamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/8-sattamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the approved
formulas (rails/vi-rails-formulas.md: ch8 frame, «Katihi vippayutto?» answer, «kehici vippayutto», «na kehici …
vippayuttā»). All shared strings are imported from build_rails_sample_vi (read-only); the approved strings are
asserted against the formulas file, and the pi-1 / pi-2 names are asserted by S.check_reuse. Elided items
«Xena ye dhammā…» use the ch3 / ch4 / ch5 form «những hiện tượng nào cùng với X…» (identical Pāli).
New strings: notes-rails-8.md.

usage: python -I -X utf8 build_rails_8_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "8-sattamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== frame pieces (approved ch3-15 formulas)
WHICH = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                  # X-ena on an elided item (as ch3 / ch4 / ch5)
THOSE_REF = "các hiện tượng đó"                    # tehi dhammehi
TE = "những hiện tượng ấy"                         # te dhammā
ASSOC = "gắn liền với"                             # sampayuttā (+ instrumental)
DISSOC = "không gắn liền với"                      # vippayuttā (+ instrumental)
SOME = "một số hiện tượng"                         # kehici (termbase)
Q_DIS = f"{DISSOC} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?"


def frame8(x_vi):
    """Xena ye dhammā sampayuttā, tehi dhammehi ye dhammā vippayuttā"""
    return f"{WHICH} {ASSOC} {x_vi}; {WHICH} {DISSOC} {THOSE_REF}"


def counted_dis(nums, subj):
    """te dhammā N khandhehi … vippayuttā (with the subject te dhammā = «những hiện tượng ấy»).
    Zero runs: «không có khối nào, không có lĩnh vực nhận biết nào mà <subj> không gắn liền với» (approved
    pattern, with te dhammā in the place of the pronoun «chúng»)."""
    groups = S._groups(nums)
    parts = []
    for i, (zero, items) in enumerate(groups):
        if zero:
            parts.append(", ".join(f"không có {c} nào" for c, _ in items) + f" mà {subj} {DISSOC}")
        elif i == 0:
            parts.append(f"{subj} {DISSOC} {S.counts_vi(items)}")
        else:
            parts.append(f"{DISSOC} {S.counts_vi(items)}")
    assert groups[0][0] or len(groups) == 1, nums   # «Te dhammā N … (no zero after a count)» only
    return f", {S.BUT} ".join(parts)


KEHICI_P = "; ekenāyatanena ekāya dhātuyā kehici vippayuttā"
KEHICI_VI = f"; {DISSOC} {SOME} thuộc {S.counts_vi([(S.AYATANA, 1), (S.DHATU, 1)])}"

# ================================================================== reference items in the instrumental
INSTR = {  # instrumental Pāli -> nominative key of S.NAMES (formula: names unchanged)
    "vedanākkhandhena": "vedanākkhandho", "saññākkhandhena": "saññākkhandho",
    "saṅkhārakkhandhena": "saṅkhārakkhandho", "viññāṇakkhandhena": "viññāṇakkhandho",
    "manāyatanena": "manāyatanaṃ",
    "cakkhuviññāṇadhātuyā": "cakkhuviññāṇadhātu", "manodhātuyā": "manodhātu",
    "manoviññāṇadhātuyā": "manoviññāṇadhātu",
    "manindriyena": "manindriyaṃ", "upekkhindriyena": "upekkhindriyaṃ",
    "saṅkhārapaccayā viññāṇena": "saṅkhārapaccayā viññāṇaṃ",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "phassapaccayā vedanāya": "phassapaccayā vedanā",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā", "cittena": "cittaṃ",
    "manasikārena": "manasikāro", "adhimokkhena": "adhimokkho",
}
ATTR = {  # X-ehi dhammehi -> key of S.DHAMMA_ATTR («các hiện tượng X», unchanged)
    "adukkhamasukhāya vedanāya sampayuttehi": "adukkhamasukhāya vedanāya sampayuttā",
    "upekkhāsahagatehi": "upekkhāsahagatā", "savitakkasavicārehi": "savitakkasavicārā",
    "cittehi": "cittā", "cetasikehi": "cetasikā", "cittasampayuttehi": "cittasampayuttā",
    "cittasaṃsaṭṭhehi": "cittasaṃsaṭṭhā", "cittasaṃsaṭṭhasamuṭṭhānehi": "cittasaṃsaṭṭhasamuṭṭhānā",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūhi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
    "savitakkehi": "savitakkā", "savicārehi": "savicārā",
}
used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR[k[: -len(' dhammehi')]]]}"
    else:
        v = S.NAMES[INSTR[k]]
    used.append(v)
    return v


# ================================================================== segment grammar
YE = " ye dhammā"
PRED = " ye dhammā sampayuttā, tehi dhammehi ye dhammā vippayuttā"
Q_FULL = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi vippayuttā? Te dhammā "
SEG = re.compile(r"^(?P<subj>.*?)" + re.escape(PRED) + r"(?P<mid>" + re.escape(Q_FULL) + r"|… te dhammā )"
                 + r"(?P<cnt>" + S.CNT + r") vippayuttā(?P<keh>" + re.escape(KEHICI_P) + r")?\.$")


def subject(p):
    items = [x.strip() for x in p.replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        assert it.endswith(YE), it
        parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
    parts.append(frame8(ref_vi(items[-1])))
    return S.cap("… ".join(parts))


def content_line(p):
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    nums = S.parse_counts(m.group("cnt"))
    ans = counted_dis(nums, TE) + (KEHICI_VI if m.group("keh") else "")
    subj = subject(m.group("subj"))
    if m.group("mid") == Q_FULL:
        return f"{subj}, {S.THEN} {TE} {Q_DIS} {S.cap(ans)}."
    return f"{subj}…, {ans}."                       # vippayuttā… te dhammā (abridged question)


# ================================================================== summary verse (uddāna) of ^3-316, lines 2-7
VERSE = {
    "Khandhā caturo āyatanañca mekaṃ;":
        f"Bốn {S.KHANDHA} và một {S.AYATANA};",
    "Dhātūsu satta dvepi ca indriyato.":
        f"Bảy trong các {S.DHATU}, và cũng có hai trong các năng lực.",
    "Tayo paṭicca tathariva phassapañcamā;":
        f"Ba trong sự sinh khởi tùy thuộc vào điều kiện, cũng vậy năm mục bắt đầu bằng {S.NAMES['phasso']};",
    "Adhimuccanā manasi tikesu tīṇi.":
        f"{S.cap(S.NAMES['adhimokkho'])}, {S.NAMES['manasikāro']}, ba trong các {S.low(S.SUB_HEADINGS['Tikaṃ'])}.",
    "Sattantarā dve ca manena yuttā;":
        "Bảy trong các phần xen giữa, và hai điều kết hợp với ý;",
    "Vitakkavicāraṇā upekkhakāya cāti.":
        "Sự hướng tâm và sự duy trì tâm, và điều có sự bình thản.",
}


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
    # ch8 frame (question)
    f = _formula("Xena ye dhammā sampayuttā, tehi dhammehi ye dhammā vippayuttā, te dhammā")
    got = f"{S.cap(frame8('X'))}, {S.THEN} {TE} {Q_DIS}"
    assert got == f, f"ch8 frame differs:\n{got}\n{f}"
    # «Katihi vippayutto? N … vippayutto.» answer predicate
    f = _formula("Katihi vippayutto?")
    assert f.endswith(f"{S.cap(DISSOC)} N {S.KHANDHA}, N {S.AYATANA} và N {S.DHATU}."), f
    assert f.startswith(f"{S.cap(DISSOC)} {S.HOW_MANY}?"), f
    # «; ekenāyatanena ekāya dhātuyā kehici vippayutto.»
    f = _formula("; ekenāyatanena ekāya dhātuyā kehici vippayutto.")
    assert f == KEHICI_VI + ".", f"{f}\n{KEHICI_VI}."
    # «na kehici khandhehi na kehici āyatanehi N dhātūhi vippayuttā» (pronoun «chúng» = te dhammā here)
    f = _formula("na kehici khandhehi na kehici āyatanehi N dhātūhi vippayuttā")
    got = counted_dis((0, 0, 99), "chúng").replace("chín mươi chín", "N")
    assert got == f, f"na kehici differs:\n{got}\n{f}"


S.NUM.setdefault(99, "chín mươi chín")   # placeholder used only by check_formulas (never in the text)


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_formulas()
    txt = render()
    assert "chín mươi chín" not in txt
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    tagged = sorted({v for v in used if S.reuse_tag(v)})
    print(f"{NAME}: {n} segments; {len(set(used))} reference names ({len(tagged)} with pi-1/pi-2 tag); "
          f"{n_reuse} pi-1/pi-2 strings asserted")
