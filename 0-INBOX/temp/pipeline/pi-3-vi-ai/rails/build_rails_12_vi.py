"""Builder for the Vietnamese rails of pi-3 chapter 12 (Ekādasamanayo, «Phương pháp thứ mười một», ^3-409 .. ^3-416),
plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/12-ekadasamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/12-ekadasamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the approved
formulas (rails/vi-rails-formulas.md: the ch12 frame). Shared strings come from the sample builder (S) and, for
identical Pāli, from the finished ch5 builder (B5: inclusion relative clause, ^3-192 verse) and ch7 builder (B7:
sampayutta / vippayutta answers, kehici, «Không có.»), all imported read-only (importing writes nothing). The ch12
frame is asserted against the formulas file; pi-1 / pi-2 names are asserted by S.check_reuse.
New strings: notes-rails-12.md.

usage: python -I -X utf8 build_rails_12_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)
import build_rails_5_vi as B5      # noqa: E402  (read-only import; writes nothing)
import build_rails_7_vi as B7      # noqa: E402  (read-only import; writes nothing)

NAME = "12-ekadasamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== frame pieces (approved ch12 frame; ch5 / ch7)
WHICH = B5.WHICH          # ye dhammā = «những hiện tượng nào»
WITH = B5.WITH            # X-ena = «cùng với»
TE = B5.TE                # te dhammā = «những hiện tượng ấy»
BY3 = B5.BY3              # khandhasaṅgahena saṅgahitā āyatana… dhātu… saṅgahitā = «theo cách gộp vào khối, …»
Q12 = f", {S.THEN} {TE} {B7.Q_SAM_FULL}"   # , te dhammā katihi … sampayuttā(ti)?


def rel12(x_vi):
    """Xena ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā"""
    return f"{WHICH} {S.IN} {WITH} {x_vi} {BY3}"


# ================================================================== reference items in the instrumental
INSTR = {  # instrumental Pāli -> nominative key of S.NAMES (formula: names unchanged)
    "samudayasaccena": "samudayasaccaṃ", "maggasaccena": "maggasaccaṃ",
    "itthindriyena": "itthindriyaṃ", "purisindriyena": "purisindriyaṃ",
    "sukhindriyena": "sukhindriyaṃ", "dukkhindriyena": "dukkhindriyaṃ",
    "somanassindriyena": "somanassindriyaṃ", "domanassindriyena": "domanassindriyaṃ",
    "upekkhindriyena": "upekkhindriyaṃ", "saddhindriyena": "saddhindriyaṃ",
    "vīriyindriyena": "vīriyindriyaṃ", "satindriyena": "satindriyaṃ",
    "samādhindriyena": "samādhindriyaṃ", "paññindriyena": "paññindriyaṃ",
    "anaññātaññassāmītindriyena": "anaññātaññassāmītindriyaṃ", "aññindriyena": "aññindriyaṃ",
    "aññātāvindriyena": "aññātāvindriyaṃ",
    "avijjāya": "avijjā",
    "avijjāpaccayā saṅkhārehi": "avijjāpaccayā saṅkhārā",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "paridevena": "paridevo", "sokena": "soko", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ",
    "upāyāsena": "upāyāso",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "cetanāya": "cetanā", "adhimokkhena": "adhimokkho", "manasikārena": "manasikāro",
}
INSTR_VI = {k: S.NAMES[v] for k, v in INSTR.items()}
INSTR_VI["kammabhavena"] = B5.INSTR["kammabhavena"]       # (pi-2), no variant bracket here (as ch5 / ch6 / ch7)
ATTR = {  # X-ehi dhammehi -> key of S.DHAMMA_ATTR («các hiện tượng X», unchanged; as ch4 ATTR)
    "hetūhi": "hetū", "hetūhi ceva sahetukehi ca": "hetū ceva sahetukā ca",
    "hetūhi ceva hetusampayuttehi ca": "hetū ceva hetusampayuttā ca",
    "āsavehi": "āsavā", "āsavehi ceva sāsavehi ca": "āsavā ceva sāsavā ca",
    "āsavehi ceva āsavasampayuttehi ca": "āsavā ceva āsavasampayuttā ca",
    "saṃyojanehi": "saṃyojanā", "ganthehi": "ganthā", "oghehi": "oghā", "yogehi": "yogā",
    "nīvaraṇehi": "nīvaraṇā", "parāmāsehi": "parāmāsā", "upādānehi": "upādānā",
    "kilesehi": "kilesā", "kilesehi ceva saṃkilesikehi ca": "kilesā ceva saṃkilesikā ca",
    "kilesehi ceva saṃkiliṭṭhehi ca": "kilesā ceva saṃkiliṭṭhā ca",
    "kilesehi ceva kilesasampayuttehi ca": "kilesā ceva kilesasampayuttā ca",
}
used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR[k[: -len(' dhammehi')]]]}"
    else:
        v = INSTR_VI[k]
    used.append(v)
    return v


# ================================================================== segment grammar
YE = " ye dhammā"
PRED = " ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā"
HEAD = re.compile(r"^(?P<subj>.*?)" + re.escape(PRED)
                  + r"(?:, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā(?:ti)?\? "
                    r"(?:(?P<natthi>Natthi\.)|Te dhammā (?P<pos1>.+))"
                    r"|(?P<abr>…pe… te dhammā |… te dhammā )(?P<pos2>.+)"
                    r"| te dhammā (?P<pos3>.+))$")
VSPLIT = " Katihi vippayuttā? "


def subject(p):
    items = [x.strip() for x in p.replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        assert it.endswith(YE), it
        parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
    parts.append(rel12(ref_vi(items[-1])))
    return S.cap("… ".join(parts))


def content_line(p):
    head, neg = p.split(VSPLIT)
    m = HEAD.match(head)
    if not m:
        raise ValueError(f"unparsed: {head}")
    subj = subject(m.group("subj"))
    if m.group("natthi"):                                   # …sampayuttāti? Natthi.
        h = f"{subj}{Q12} {B7.NATTHI}"
    elif m.group("pos1"):                                   # …sampayuttā? Te dhammā …
        h = f"{subj}{Q12} {S.cap(TE)} {S.low(B7.answer_vi(m.group('pos1')))}"
    elif m.group("pos2"):                                   # …pe… te dhammā / … te dhammā (abridged, as ch4)
        h = f"{subj}…, {TE} {S.low(B7.answer_vi(m.group('pos2')))}"
    else:                                                   # ^3-413 «saṅgahitā te dhammā» (no question)
        h = f"{subj}, {S.THEN} {TE} {S.low(B7.answer_vi(m.group('pos3')))}"
    return f"{h} {B7.Q_VIP} {B7.answer_vi(neg)}"


# ================================================================== summary verse of ^3-416 (= ch5 ^3-192)
V1 = "Dve saccā pannarasindriyā, ekādasa paṭiccapadā;"
V2_CH5 = "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti [tiṃsavidhanti (pī.)]."
V2 = "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti."   # no variant bracket here
VERSE = {
    V1: B5.UDDANA[V1],
    V2: B5.UDDANA[V2_CH5].replace(" " + S.spell("Pī.", "tiṃsavidhanti"), ""),
}
assert VERSE[V2] == "Tiếp theo rồi lại có mười một, ở đây đề mục thuộc các nhóm gồm ba mươi loại.", VERSE[V2]


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
def check_formulas():
    txt = FORMULAS.read_text(encoding="utf-8")
    line = next(ln for ln in txt.splitlines() if "sampayuttā? (ch12) = " in ln)
    f = line.split(" = ", 1)[1].replace(" (proposed for ch3-15)", "")
    got = f"{S.cap(rel12('X'))}{Q12}"
    assert got == f, f"ch12 frame differs:\n{got}\n{f}"
    for a in ["Không gắn liền với bao nhiêu? Không gắn liền với N khối, N lĩnh vực nhận biết và N yếu tố.",
              "; không gắn liền với một số hiện tượng thuộc một lĩnh vực nhận biết và một yếu tố.",
              "; gắn liền với một số hiện tượng thuộc một khối, một lĩnh vực nhận biết và một yếu tố."]:
        assert f"= {a} (proposed for ch3-15)" in txt, a
    # the first half of the ch12 frame is the first relative clause of the approved ch5 frame
    assert B5.APPROVED_CH5.startswith(S.cap(rel12("X")) + ";"), "ch5 / ch12 relative clause differ"


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    B5.check_reuse5()
    check_formulas()
    txt = render()
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{NAME}: {n} segments; {len(set(used))} reference names; {n_reuse + len(B5.REUSE5)} pi-1/pi-2 strings "
          f"asserted")
