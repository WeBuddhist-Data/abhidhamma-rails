"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 7, Ekaccaṃ atthītikathā (^5-7-0 … ^5-300).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/7-ekaccam-atthitikatha.md from the
fixed strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg,
na_vattabbam …). Every string marked (pi-N) is asserted to occur in that book's approved Vietnamese rails;
S.write runs the per-line dash / quote / NFC / id checks against the Pāli.
New recurring strings: notes-rails-7.md.

usage: python -I -X utf8 -B build_rails_7_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "7-ekaccam-atthitikatha.md"
Q, q, NANU, YES, NO_PE = S.Q, S.q, S.NANU, S.YES, S.NO_PE

# ---------------------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------------------
KATHA_NAME = "việc một số tồn tại"                     # Ekaccaṃ atthītikathā (ekaccaṃ «một số», atthi «tồn tại»)
H_KATHA = S.katha(KATHA_NAME)                          # ### Ekaccaṃ atthītikathā
END_KATHA = S.katha_end(KATHA_NAME)                    # Ekaccaṃ atthītikathā niṭṭhitā.
H_ATITA = S.katha("một số trong quá khứ và các mục khác")     # #### Atītādiekaccakathā
H_ANAGATA = S.katha("một số trong tương lai và các mục khác")  # #### Anāgatādiekaccakathā

# ---------------------------------------------------------------------------------------------------------------
# Terms (termbase; pi-N where identical Pāli exists)
# ---------------------------------------------------------------------------------------------------------------
ATITAM = "quá khứ"                                     # Atītaṃ (termbase Atītaṃ atthi «quá khứ tồn tại»)
ANAGATAM = "tương lai"                                 # Anāgataṃ (termbase Anāgataṃ atthi «tương lai tồn tại»)
ATTHI, NATTHI = "tồn tại", "không tồn tại"             # atthi / natthi (existence thesis)
EK = "một số"                                          # ekaccaṃ / ekacce
EK_PAIR = f"{EK} {ATTHI}, {EK} {NATTHI}"               # ekaccaṃ atthi, ekaccaṃ natthi / ekacce atthi, ekacce natthi
TE = "chúng"                                           # te (pronoun, the dhammā)
DH_AT = "các hiện tượng thuộc quá khứ"                 # atītā dhammā (pi-1)
DH_AN = "các hiện tượng thuộc tương lai"               # anāgatā dhammā (pi-3)
DH_PA = "các hiện tượng thuộc hiện tại"                # paccuppannā dhammā (pi-1)
AVP = "có quả chưa chín muồi"                          # avipakkavipākā (pi-1)
VP = "có quả đã chín muồi"                             # vipakkavipākā (termbase)
AV = "không có quả trổ"                                # avipākā (no headword; sibling savipākā «có quả trổ»)
UPP = "sẽ sinh khởi"                                   # uppādino (pi-1)
AUPP = "sẽ không sinh khởi"                            # anuppādino (no headword; sibling uppādino)
NIR = "đã chấm dứt"                                    # niruddhā / niruddhaṃ (termbase)
AJATA = "chưa sinh ra"                                 # ajātā / ajātaṃ (termbase)
VIPACC = "sẽ trổ quả"                                  # vipaccissanti (termbase)
UPPAJJ = "sẽ sinh khởi"                                # uppajjissanti (no headword; uppajjati «sinh khởi» + sẽ)
NIRUJJ = "sẽ chấm dứt"                                 # nirujjhissanti (termbase)
PACC = "thuộc hiện tại"                                # paccuppannā (predicate; termbase Paccuppannā dhammā)
EKADESAM = "một phần"                                  # ekadesaṃ (termbase)

# thesis pairs of line 1 (participles from the termbase; na / a- with a «đã» participle = «chưa», as ajātaṃ)
PAIRS_AT = [("đã chấm dứt", "chưa chấm dứt"),          # niruddhaṃ / na niruddhaṃ
            ("đã mất đi", "chưa mất đi"),              # vigataṃ / avigataṃ
            ("đã biến mất", "chưa biến mất"),          # atthaṅgataṃ / na atthaṅgataṃ
            ("đã biến mất hoàn toàn", "chưa biến mất hoàn toàn")]   # abbhatthaṅgataṃ / na abbhatthaṅgataṃ
PAIRS_AN = [("đã sinh ra", "chưa sinh ra"),            # jātaṃ / ajātaṃ
            ("đã sinh thành", "chưa sinh thành"),      # sañjātaṃ / asañjātaṃ
            ("đã phát sinh", "chưa phát sinh"),        # nibbattaṃ / anibbattaṃ
            ("đã hiện ra", "chưa hiện ra")]            # pātubhūtaṃ / apātubhūtaṃ

REUSED7 = [  # (Pāli, Vietnamese, book)
    ("atītā dhammā", DH_AT, "1"),
    ("anāgatā dhammā", DH_AN, "3"),
    ("paccuppannā dhammā", DH_PA, "1"),
    ("avipakkavipākānaṃ", AVP, "1"),
    ("uppādino dhammā", f"các hiện tượng {UPP}", "1"),
]


def check_reused7():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                          for p in sorted(d.glob("*.md")))).lower()
    bad = [(p, v, b) for p, v, b in REUSED7 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def te(x, neg=False):              # X – te (n)atthi
    return f"{x} – {TE} {NATTHI if neg else ATTHI}"


def katva_nen(x, y):               # Xti katvā Yti? (no «tena ca kāraṇena»)
    return f"Có phải vì cho rằng {x}, nên {y} không?"


def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def thesis(time, pairs):       # X-ṃ atthīti? Ekaccaṃ atthi, ekaccaṃ natthīti. Ekaccaṃ A, ekaccaṃ B; …ti?
        body = "; ".join(f"{EK} {a}, {EK} {b}" for a, b in pairs)
        return f"{Q(f'{time} {ATTHI}')} {S.cap(EK_PAIR)}. {Q(body)} {NO_PE}"

    # ---- ### Ekaccaṃ atthītikathā / #### Atītādiekaccakathā -------------------------------------------------------
    add("5-7-0", f"### {H_KATHA}")
    add("5-7-1-0", f"#### {H_ATITA}")

    T_AT = f"trong {ATITAM}, {EK_PAIR}"                     # Atītaṃ ekaccaṃ atthi, ekaccaṃ natthi

    def among(x):                                           # X dhammā ekacce atthi, ekacce natthi
        return f"trong số {x}, {EK_PAIR}"

    A_AVP, A_VP, A_AV = f"{DH_AT} {AVP}", f"{DH_AT} {VP}", f"{DH_AT} {AV}"
    l1 = thesis(ATITAM, PAIRS_AT)
    l2 = (f"{Q(T_AT)} {YES} {Q(among(A_AVP))} {NO_PE} {q(T_AT)} {YES} {Q(among(A_VP))} {NO_PE} "
          f"{q(T_AT)} {YES} {Q(among(A_AV))} {NO_PE}")
    l3 = (f"{Q(T_AT)} {YES} Điều gì {ATTHI}, điều gì {NATTHI}? {S.cap(te(A_AVP))}; {te(A_VP, True)}. "
          f"{Q(te(A_AVP))} {YES} {Q(te(A_VP))} {NO_PE} {q(te(A_AVP))} {YES} "
          f"Có phải {te(A_AV)}{S.var('Ka.', 'atītā avipakkavipākā dhammā te natthīti')} không? {NO_PE}")
    l4 = f"{Q(te(A_VP, True))} {YES} {Q(te(A_AVP, True))} {NO_PE}"
    V9A = S.var("Syā.", "vipakkavipākā")[:-1] + "; (Ka.): avipakkavipākā]"
    V9B = S.var("Syā.", "avipākā")
    l5 = (f"{Q(te(A_AV + V9A, True))} {YES} {Q(te(A_AVP + V9B, True))} {NO_PE}")
    NIR_AVP = f"{A_AVP} {NIR}"                              # atītā avipakkavipākā dhammā niruddhā
    l6 = (f"{Q(te(A_AVP))} {YES} {NANU(NIR_AVP)} {YES} "
          f"{S.hanci_neg(NIR_AVP, te(A_AVP).replace(f' {TE} ', f' {TE}' + S.var('Syā., Ka.', 'dhammā niruddhā te') + ' '))}")
    N_AVP, N_VP = f"{A_AVP} {NIR}", f"{A_VP} {NIR}"
    N_AV11 = f"{A_AV}{S.var('Sī., Ka.', 'avipakkavipākā')} {NIR}"
    l7 = (f"{Q(te(N_AVP))} {YES} {Q(te(N_VP))} {NO_PE} {q(te(N_AVP))} {YES} {Q(te(N_AV11))} {NO_PE}")
    l8 = f"{Q(te(N_VP, True))} {YES} {Q(te(N_AVP, True))} {NO_PE}"
    l9 = (f"{Q(te(f'{A_AV}{V9A} {NIR}', True))} {YES} {Q(te(f'{A_AVP}{V9B} {NIR}', True))} {NO_PE}")
    MIX = f"{DH_AT} {EKADESAM} {VP}, các hiện tượng {EKADESAM} {AVP}, {NIR}"
    #   atītā ekadesaṃ vipakkavipākā dhammā ekadesaṃ avipakkavipākā dhammā niruddhā
    l10 = (f"{Q(te(N_AVP))} {YES} {Q(te(N_VP, True))} {YES} "
           f"{Q(f'{MIX} – trong số {TE}, {EK_PAIR}')} {NO_PE}")
    l11 = (f"{S.na_vattabbam(te(A_AVP))} {YES} {NANU(f'{A_AVP} {VIPACC}')} {YES} "
           f"{S.hanci(f'{A_AVP} {VIPACC}', te(A_AVP))}")
    k1 = katva_nen(f"{TE} {VIPACC}", f"{TE} {PACC}")      # Vipaccissantīti katvā paccuppannāti?
    l12 = (f"{katva_nen(f'{A_AVP} {VIPACC}', f'{TE} {ATTHI}')} {YES} {k1} {NO_PE} {k1[:1].lower()}{k1[1:]} {YES} "
           f"{katva_nen(f'{DH_PA} {NIRUJJ}', f'{TE} {NATTHI}')} {NO_PE}")
    add("5-299", l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12)

    # ---- #### Anāgatādiekaccakathā --------------------------------------------------------------------------------
    add("5-7-2-0", f"#### {H_ANAGATA}")
    T_AN = f"trong {ANAGATAM}, {EK_PAIR}"
    N_UPP, N_AUPP = f"{DH_AN} {UPP}", f"{DH_AN} {AUPP}"     # anāgatā (an)uppādino dhammā
    m1 = thesis(ANAGATAM, PAIRS_AN)
    m2 = f"{Q(T_AN)} {YES} {Q(among(N_UPP))} {NO_PE} {q(T_AN)} {YES} {Q(among(N_AUPP))} {NO_PE}"
    m3 = (f"{Q(T_AN)} {YES} Điều gì {ATTHI}, điều gì {NATTHI}? {S.cap(te(N_UPP))}; {te(N_AUPP, True)}. "
          f"{Q(te(N_UPP))} {YES} {Q(te(N_AUPP))} {NO_PE} {q(te(N_AUPP, True))} {YES} "
          f"{Q(te(N_UPP, True))} {NO_PE}")
    AJ_UPP, AJ_AUPP = f"{N_UPP} {AJATA}", f"{N_AUPP} {AJATA}"   # anāgatā (an)uppādino dhammā ajātā
    m4 = f"{Q(te(N_UPP))} {YES} {NANU(AJ_UPP)} {YES} {S.hanci_neg(AJ_UPP, te(N_UPP))}"
    m5 = (f"{Q(te(AJ_UPP))} {YES} {Q(te(AJ_AUPP))} {NO_PE} {q(te(AJ_AUPP, True))} {YES} "
          f"{Q(te(AJ_UPP, True))} {NO_PE}")
    UPPJ = f"{N_UPP} thì {UPPAJJ}"                          # anāgatā uppādino dhammā uppajjissanti
    m6 = f"{S.na_vattabbam(te(N_UPP))} {YES} {NANU(UPPJ)} {YES} {S.hanci(UPPJ, te(N_UPP))}"
    k2 = katva_nen(f"{TE} {UPPAJJ}", f"{TE} {PACC}")
    m7 = (f"{katva_nen(UPPJ, f'{TE} {ATTHI}')} {YES} {k2} {NO_PE} {k2[:1].lower()}{k2[1:]} {YES} "
          f"{katva_nen(f'{DH_PA} {NIRUJJ}', f'{TE} {NATTHI}')} {NO_PE}")
    add("5-300", m1, m2, m3, m4, m5, m6, m7, END_KATHA)
    return segs


def main():
    check_reused7()
    S.check_reused()
    S.write(NAME, build())


if __name__ == "__main__":
    main()
