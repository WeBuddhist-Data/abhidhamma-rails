"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 6, Atītakkhandhādikathā (^5-6-0 … ^5-298).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/6-atitakkhandhadikatha.md from the
fixed strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU_VUTTAM, na_vattabbam,
tena_hi_na …). Every string marked (pi-N) is asserted to occur in that book's approved Vietnamese rails; S.write
runs the per-line dash / quote / NFC / id checks against the Pāli.
New recurring strings: notes-rails-6.md.

usage: python -I -X utf8 -B build_rails_6_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "6-atitakkhandhadikatha.md"
Q, q, PE, YES, NO_PE = S.Q, S.q, S.PE, S.YES, S.NO_PE

# ---------------------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------------------
KATHA_NAME = "các khối quá khứ và các mục khác"     # Atītakkhandhādikathā (atītakkhandha «khối quá khứ»; -ādi as Ñātakānuyogādi)
H_KATHA = S.katha(KATHA_NAME)                       # ### Atītakkhandhādikathā
END_KATHA = S.katha_end(KATHA_NAME)                 # Atītakkhandhādikathā niṭṭhitā.
H_NASUTTA = "Chứng cứ không từ kinh"                # #### Nasuttasādhanaṃ
H_SUTTA = "Chứng cứ từ kinh"                        # #### Suttasādhanaṃ (ch2 Suttasādhana- «chứng cứ từ kinh»)

# ---------------------------------------------------------------------------------------------------------------
# Terms (termbase)
# ---------------------------------------------------------------------------------------------------------------
PAST, FUT, PRES = "quá khứ", "tương lai", "hiện tại"          # atītaṃ / anāgataṃ / paccuppannaṃ (subject)
TH = {PAST: "thuộc quá khứ", FUT: "thuộc tương lai", PRES: "thuộc hiện tại"}   # atītaṃ rūpaṃ … «vật chất thuộc quá khứ»
K_PL = "các khối"                                   # khandhā
K_SG = "khối"                                       # khandho
AY = "lĩnh vực nhận biết"                           # āyatanaṃ
DH = "yếu tố"                                       # dhātu
KDA = "các khối, yếu tố, lĩnh vực nhận biết"        # khandhā dhātu āyatanaṃ
EX, NEX = "tồn tại", "không tồn tại"                # atthi / natthi
RUPA, VINNANA = S.RUPA, S.VINNANA                   # rūpaṃ / viññāṇaṃ («vật chất» / «thức»)

TH_NATTHI = f"{KDA} thuộc quá khứ và tương lai, và những điều này {NEX}"
#   atītānāgatā khandhā dhātu āyatanaṃ natthi cete (commentary: natthi ca ete dhammā)

# Sutta quotes
NIRUTTI = ("Này các tỳ-khưu, đây là ba phạm vi của cách diễn đạt, phạm vi của tên gọi, sự định danh"
           f"{PE} bởi những người có trí{PE}")
#   tayome, bhikkhave, niruttipathā adhivacanapathā paññatti…pe… viññūhīti…pe…
#   («phạm vi của cách diễn đạt» / «phạm vi của tên gọi»: pi-1; paññatti «sự định danh»: termbase)
KHANDHA_DEF = ("bất cứ vật chất nào, dù thuộc quá khứ, thuộc tương lai hay thuộc hiện tại, ở nơi bản thân hay "
               "ở bên ngoài bản thân, ở dạng thô hay ở dạng vi tế, thấp kém hay ưu việt, ở xa hay ở gần")   # (pi-2)
VUCCATI_RUPA = "đó được gọi là khối vật chất"       # ayaṃ vuccati rūpakkhandho (pi-2)
VUCCATI_VINN = "đó được gọi là khối thức"           # ayaṃ vuccati viññāṇakkhandho (pi-2)
YA_KACI = ["bất cứ cảm giác nào", "bất cứ tri giác nào", "bất cứ sự tạo tác nào"]   # yā kāci vedanā … ye keci saṅkhārā (pi-2)
YAM_VINN = "bất cứ thức nào, dù thuộc quá khứ, thuộc tương lai hay thuộc hiện tại"   # yaṃ kiñci viññāṇaṃ atītānāgatapaccuppannaṃ (pi-2)
SUTTA_KHANDHA = (f"Này các tỳ-khưu, {KHANDHA_DEF}, {VUCCATI_RUPA}. {S.cap(YA_KACI[0])}{PE} {YA_KACI[1]}{PE} "
                 f"{YA_KACI[2]}{PE} {YAM_VINN}{PE} {VUCCATI_VINN}")

REUSED6 = [  # (Pāli, Vietnamese, book)
    ("niruttipathā", "phạm vi của cách diễn đạt", "1"),
    ("adhivacanapathā", "phạm vi của tên gọi", "1"),
    ("yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ … yaṃ dūre santike vā", KHANDHA_DEF, "2"),
    ("ayaṃ vuccati rūpakkhandho", VUCCATI_RUPA, "2"),
    ("ayaṃ vuccati viññāṇakkhandho", VUCCATI_VINN, "2"),
    ("yā kāci vedanā", YA_KACI[0], "2"),
    ("yā kāci saññā", YA_KACI[1], "2"),
    ("ye keci saṅkhārā", YA_KACI[2], "2"),
    ("yaṃ kiñci viññāṇaṃ atītānāgatapaccuppannaṃ", YAM_VINN, "2"),
]


def check_reused6():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                          for p in sorted(d.glob("*.md")))).lower()
    bad = [(p, v, b) for p, v, b in REUSED6 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Frames of the debate
# ---------------------------------------------------------------------------------------------------------------
def is_(s, pred):                   # X khandhā / āyatanaṃ / dhātu
    return f"{s} là {pred}"


def clause(s, pred, ex):            # X khandhā X atthi / natthi
    return f"{s} là {pred}, {s} {ex}"


def simple(s, preds, first_var="", lead=""):
    """X-ṃ khandhāti? Āmantā. X-ṃ atthīti? Na hevaṃ vattabbe…pe… (four times, fully spelled)."""
    out = []
    for k, pred in enumerate(preds):
        qf = "Có phải" if k == 0 else "có phải"
        var = first_var if k == len(preds) - 1 else ""
        out.append(f"{qf} {lead if k == 0 else ''}{is_(s, pred)}{var} không? {YES} {Q(f'{s} {EX}')} {NO_PE}")
    return " ".join(out)


def simple_short(s, k1, lead=""):
    """First pair spelled; then 'X āyatanaṃ…pe… X dhātu…pe… X khandhā dhātu āyatananti? Āmantā. X atthīti? …'."""
    first = f"Có phải {lead}{is_(s, k1)} không? {YES} {Q(f'{s} {EX}')} {NO_PE}"
    rest = (f"có phải {is_(s, AY)}{PE} {is_(s, DH)}{PE} {is_(s, KDA)} không? {YES} {Q(f'{s} {EX}')} {NO_PE}")
    return f"{first} {rest}"


def pair_full(s1, s2, ex):
    """s1 khandhā s1 ex? Āmantā. s2 khandhā s2 ex? Na hevaṃ vattabbe…pe… (four predicates, fully spelled)."""
    out = []
    for k, pred in enumerate((K_PL, AY, DH, KDA)):
        qf = Q if k == 0 else q
        out.append(f"{qf(clause(s1, pred, ex))} {YES} {Q(clause(s2, pred, ex))} {NO_PE}")
    return " ".join(out)


def pair_short(s1, s2, ex, k1=K_SG, lower=False):
    """First pair spelled; then 's1 āyatanaṃ…pe… s1 dhātu…pe… s1 khandhā dhātu āyatanaṃ s1 ex? Āmantā. s2 … ?'."""
    qf = q if lower else Q
    first = f"{qf(clause(s1, k1, ex))} {YES} {Q(clause(s2, k1, ex))} {NO_PE}"
    rest = (f"có phải {is_(s1, AY)}{PE} {is_(s1, DH)}{PE} {clause(s1, KDA, ex)} không? {YES} "
            f"{Q(clause(s2, KDA, ex))} {NO_PE}")
    return f"{first} {rest}"


def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    add("5-6-0", f"### {H_KATHA}")
    add("5-6-1-0", f"#### {H_NASUTTA}")

    preds = (K_PL, AY, DH, KDA)
    l5 = simple(PAST, preds, first_var=S.var_sp("Syā.", "khandhadhātuāyatananti"))
    l6 = simple(FUT, preds)
    l7 = pair_full(PRES, PAST, EX)
    l8 = pair_full(PRES, FUT, EX)
    l9 = pair_full(PAST, PRES, NEX)
    # ^ line 10: first pair spelled, then "anāgataṃ āyatanaṃ…pe… anāgataṃ dhātu…pe… anāgataṃ khandhā dhātu
    #   āyatanaṃ anāgataṃ natthīti? Āmantā. Paccuppannaṃ … natthīti? …"
    l10 = pair_short(FUT, PRES, NEX, k1=K_PL)

    r = {t: f"{RUPA} {TH[t]}" for t in TH}           # atītaṃ / anāgataṃ / paccuppannaṃ rūpaṃ
    l11 = simple(r[PAST], (K_SG, AY, DH, KDA))
    l12 = simple_short(r[FUT], K_SG)
    l13 = pair_short(r[PRES], r[PAST], EX)
    l14 = pair_short(r[PRES], r[FUT], EX)
    l15 = pair_short(r[PAST], r[PRES], NEX)
    l16 = pair_short(r[FUT], r[PRES], NEX)

    v = {t: f"{VINNANA} {TH[t]}" for t in TH}        # atītaṃ / anāgataṃ / paccuppannaṃ viññāṇaṃ
    lead = (f"{S.VEDANA} {TH[PAST]}{PE} {S.SANNA} {TH[PAST]}{PE} {S.SANKHARA} {TH[PAST]}{PE} ")
    #   Atītā vedanā… atītā saññā… atītā saṅkhārā… (atītā saṅkhārā «tạo tác thuộc quá khứ»)
    l17 = simple_short(v[PAST], K_SG, lead=lead)
    l18 = simple_short(v[FUT], K_SG)
    l19 = pair_short(v[PRES], v[PAST], EX)
    l20 = pair_short(v[PRES], v[FUT], EX)
    l21 = f"{pair_short(v[PAST], v[PRES], NEX)} {pair_short(v[FUT], v[PRES], NEX, lower=True)}"
    add("5-297", l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21)

    add("5-6-2-0", f"#### {H_SUTTA}")
    l25 = (f"{S.na_vattabbam(TH_NATTHI)} {YES} {S.NANU_VUTTAM} “{NIRUTTI}”. {S.ATTHEVA} {YES} "
           f"{S.tena_hi_na(TH_NATTHI)}")
    l26 = (f"{Q(TH_NATTHI)} {YES} {S.NANU_VUTTAM} “{SUTTA_KHANDHA}”. {S.ATTHEVA} {YES} "
           f"{S.tena_hi_na(TH_NATTHI)}")
    add("5-298", l25, l26, END_KATHA)
    return segs


def main():
    check_reused6()
    S.write(NAME, build())


if __name__ == "__main__":
    main()
