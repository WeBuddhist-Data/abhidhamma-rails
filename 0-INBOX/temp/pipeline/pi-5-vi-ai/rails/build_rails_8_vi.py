"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 8, Satipaṭṭhānakathā (^5-8-0 … ^5-303).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/8-satipatthanakatha.md from the
fixed strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, NANU_VUTTAM,
na_vattabbam, hanci …). Every string marked (pi-N) is asserted to occur in that book's approved Vietnamese
rails, (ch2) in the finished 2-parihanikatha.md; S.write runs the per-line dash / quote / NFC / id checks
against the Pāli.
New recurring strings: notes-rails-8.md.

usage: python -I -X utf8 -B build_rails_8_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "8-satipatthanakatha.md"
Q, q, NANU, PE, YES, YES_Q, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.YES_Q, S.NO_PE

# ---------------------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------------------
SP_SG = "sự thiết lập tỉnh thức"                     # satipaṭṭhānaṃ (termbase; «as in Satipaṭṭhānakathā»)
KATHA_NAME = SP_SG                                   # Satipaṭṭhānakathā
H_KATHA = S.katha(KATHA_NAME)                        # ### Satipaṭṭhānakathā
END_KATHA = S.katha_end(KATHA_NAME)                  # Satipaṭṭhānakathā niṭṭhitā.

# ---------------------------------------------------------------------------------------------------------------
# Terms (termbase; pi-N where identical Pāli exists)
# ---------------------------------------------------------------------------------------------------------------
SATI = "sự tỉnh thức"                                # sati
ALL = "tất cả các hiện tượng"                        # sabbe dhammā / sabbe dhamme
EVERY = "mọi hiện tượng"                             # sabbaṃ dhammaṃ (singular)
SP_PL = "các sự thiết lập tỉnh thức"                 # satipaṭṭhānā (pl.)
TH = f"{ALL} là {SP_PL}"                             # sabbe dhammā satipaṭṭhānā (termbase «hiện tượng là các sự thiết lập tỉnh thức»)
BEINGS = "tất cả chúng sinh"                         # sabbe sattā

SATI5 = "sự tỉnh thức, năng lực tỉnh thức, sức mạnh tỉnh thức, tỉnh thức đúng đắn, chi phần giác ngộ là sự tỉnh thức"
#   sati satindriyaṃ satibalaṃ sammāsati satisambojjhaṅgo (pi-1 ^1-290)
EKAYANA = "con đường duy nhất"                       # ekāyanamaggo / ekāyano … maggo (ekāyana «duy nhất»)
QUAL = ["dẫn đến sự diệt tận",                       # khayagāmī          (ch4 list)
        "dẫn đến sự giác ngộ",                       # bodhagāmī
        "dẫn đến sự giảm trừ",                       # apacayagāmī (pi-1)
        "không phải là đối tượng của ô nhiễm",       # anāsavā / anāsavaṃ (pi-2)
        "không phải là đối tượng của xiềng xích",    # asaṃyojaniyā / -yaṃ (pi-2)
        "không phải là đối tượng của nút thắt",      # aganthaniyā (pi-2)
        "không phải là đối tượng của dòng lũ",       # anoghaniyā (pi-2)
        "không phải là đối tượng của ách",           # ayoganiyā
        "không phải là đối tượng của chướng ngại",   # anīvaraṇiyā
        "không bị sự hiểu sai lệch nắm giữ",         # aparāmaṭṭhā (pi-1)
        "không phải là đối tượng của sự bám víu",    # anupādāniyā (pi-1)
        "không phải là đối tượng của phiền não"]     # asaṃkilesikā / -kaṃ (pi-2)
ANUSSATI = ["sự nhớ lại Đức Phật",                   # buddhānussati
            "sự nhớ lại Giáo Pháp",                  # dhammānussati
            "sự nhớ lại Tăng đoàn",                  # saṅghānussati
            "sự nhớ lại giới hạnh",                  # sīlānussati
            "sự nhớ lại sự rộng lượng",              # cāgānussati (cāga «sự rộng lượng»)
            "sự nhớ lại các vị thiên",               # devatānussati (devatā «vị thiên»)
            "sự tỉnh thức về hơi thở vào và hơi thở ra",   # ānāpānassati (ānāpāna)
            "sự nhớ lại sự chết",                    # maraṇānussati
            "sự tỉnh thức hướng về thân",            # kāyagatāsati (termbase)
            "sự nhớ lại sự lắng dịu"]                # upasamānussati (upasama «sự lắng dịu»)

SATI_FULL = f"{SATI5}, {EKAYANA}, " + ", ".join(QUAL)                 # sati … asaṃkilesikā
SATI_SHORT = f"{SATI5}, {EKAYANA}, " + ", ".join(QUAL[:5]) + f"{PE} " + QUAL[-1]   # … asaṃyojaniyaṃ…pe… asaṃkilesikaṃ
AN_FULL = ", ".join(ANUSSATI)

# the ten (āyatana + kilesa) items of ^5-301
AY = [S.A[k] for k in ("sotāyatana", "ghānāyatana", "jivhāyatana", "kāyāyatana", "rūpāyatana", "saddāyatana",
                       "gandhāyatana", "rasāyatana", "phoṭṭhabbāyatana")]
CAKKHU = S.A["cakkhāyatana"]
KILESA = ["sự tham đắm",                             # rāgo (termbase; pi-1 has lobho «sự tham lam»)
          "sự sân hận", "sự si mê", "sự kiêu mạn", "quan điểm", "sự hoài nghi", "sự uể oải", "sự xao động",
          "sự không biết hổ thẹn"]                   # doso … ahirikaṃ (pi-1 ^1-1235)
ANOTTAPPA = "sự không biết ghê sợ tội lỗi"           # anottappaṃ (pi-1)
K = dict(zip(("rāgo", "doso", "moho"), KILESA[:3]))

AND_IS = "và điều ấy là sự tỉnh thức"                # sā ca sati / tañca sati
AND_NOT = "và điều ấy không phải là sự tỉnh thức"    # sā ca na sati / tañca na sati


def is_sp(x):                                        # X satipaṭṭhānaṃ
    return f"{x} là {SP_SG}"


# ^5-302
ARABBHA_ALL = f"lấy {ALL} làm đối tượng mà {SATI} đứng vững"          # sabbe dhamme ārabbha sati santiṭṭhati
def arabbha(x):                                      # sabbaṃ dhammaṃ ārabbha X santiṭṭhati
    return f"lấy {EVERY} làm đối tượng mà {x} đứng vững"


def vi(x, y):                                        # Xti Yti? (no comma, causal "since X, Y?")
    return f"Có phải vì {x}, nên {y} không?"


UPATTHITA = (f"{BEINGS} có sự tỉnh thức được thiết lập, được trang bị sự tỉnh thức, được kết hợp với sự tỉnh thức; "
             f"sự tỉnh thức hiện diện nơi {BEINGS}")
#   sabbe sattā upaṭṭhitasatino satiyā samannāgatā satiyā samohitā; sabbesaṃ sattānaṃ sati paccupaṭṭhitā

# ^5-303 suttas
BH = "Này các tỳ-khưu"                               # bhikkhave
KAYAGATA = ANUSSATI[8]
AMATA = (f"{BH}, những ai không thọ hưởng {KAYAGATA}, những người ấy không thọ hưởng điều bất tử. "
         f"{BH}, những ai thọ hưởng {KAYAGATA}, những người ấy thọ hưởng điều bất tử")
#   amataṃ te, bhikkhave, na paribhuñjanti ye kāyagatāsatiṃ na paribhuñjanti. Amataṃ te … paribhuñjantī
PARIBHUNJ = "thọ hưởng, có được, thực hành, tu tập, làm đi làm lại"   # paribhuñjanti paṭilabhanti āsevanti bhāventi bahulīkaronti («thực hành, tu tập, làm đi làm lại»: pi-2)
CATTARO = "bốn sự thiết lập tỉnh thức"              # cattāro satipaṭṭhānā (pi-2)
EKAYANA_SUTTA = (f"{BH}, đây là {EKAYANA} vì sự thanh tịnh của chúng sinh, để vượt qua sự sầu muộn và sự than khóc, "
                 f"để làm biến mất sự khó chịu và nỗi buồn, để chứng đắc phương pháp đúng đắn, "
                 f"để tự mình chứng nghiệm Niết-bàn, tức là {CATTARO}")
#   ekāyano ayaṃ, bhikkhave, maggo sattānaṃ visuddhiyā sokaparidevānaṃ samatikkamāya dukkhadomanassānaṃ
#   atthaṅgamāya ñāyassa adhigamāya nibbānassa sacchikiriyāya yadidaṃ cattāro satipaṭṭhānā
#   («sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn»: pi-2)
CIT_EKAYANA = (f"[Trường Bộ Kinh 2.373; {S.CIT['ma. ni.']} 1.106; {S.CIT['saṃ. ni.']} 5.367]")   # dī. ni. (pi-2)

KING = "vị vua chuyển luân"                          # rañño cakkavattissa (termbase)
TATHAGATA = "Như Lai, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"   # Tathāgatassa … arahato sammāsambuddhassa (Như Lai: pi-2; arahato sammāsambuddhassa: homage, pi-1)
SEVEN = "Bảy báu vật nào?"                           # Katamesaṃ sattannaṃ?
APPEAR = "có sự xuất hiện của"                       # X-ssa pātubhāvo hoti
R = "báu vật"                                        # ratana
RATANA = ["bánh xe", "voi", "ngựa đực", "ngọc", "người nữ", "gia chủ", "vị cố vấn"]
#   cakka / hatthi / assa («ngựa đực», termbase) / maṇi / itthi / gahapati / pariṇāyaka
BOJJH = ["chi phần giác ngộ là sự tỉnh thức", "chi phần giác ngộ là sự tìm hiểu các hiện tượng",
         "chi phần giác ngộ là sự tinh tấn", "chi phần giác ngộ là sự hân hoan", "chi phần giác ngộ là sự an tịnh",
         "chi phần giác ngộ là định tâm", "chi phần giác ngộ là sự bình thản"]          # (pi-2 ^2-466)
RATANA_SUTTA_1 = (f"{BH}, do sự xuất hiện của {KING}, {APPEAR} bảy {R}. {SEVEN} "
                  f"{S.cap(APPEAR)} {R} {RATANA[0]}, {APPEAR} {R} {RATANA[1]}, của {R} {RATANA[2]}{PE} "
                  f"của {R} {RATANA[3]}{PE} của {R} {RATANA[4]}{PE} của {R} {RATANA[5]}{PE} "
                  f"{APPEAR} {R} {RATANA[6]}. {BH}, do sự xuất hiện của {KING}, {APPEAR} bảy {R} này.")
RATANA_SUTTA_2 = (f"{BH}, do sự xuất hiện của {TATHAGATA}, {APPEAR} bảy {R} chi phần giác ngộ. {SEVEN} "
                  + f"{S.cap(APPEAR)} {R} {BOJJH[0]}, "
                  + ", ".join(f"{APPEAR} {R} {b}" for b in BOJJH[1:])
                  + f". {BH}, do sự xuất hiện của {TATHAGATA}, {APPEAR} bảy {R} chi phần giác ngộ này")
OTHERS = ["các nỗ lực đúng đắn", "các nền tảng thần thông", "các năng lực", "các sức mạnh",
          "các chi phần giác ngộ"]                   # sammappadhānā … bojjhaṅgā (ch2)

REUSED8 = [  # (Pāli, Vietnamese, book)
    ("sati satindriyaṃ satibalaṃ sammāsati satisambojjhaṅgo", SATI5, "1"),
    ("apacayagāmī", QUAL[2], "1"), ("anāsavo", QUAL[3], "2"), ("asaṃyojaniyo", QUAL[4], "2"),
    ("aganthaniyo", QUAL[5], "2"), ("anoghaniyo", QUAL[6], "2"),
    ("yoganiyā", "là đối tượng của ách", "1"), ("nīvaraṇiyā", "là đối tượng của chướng ngại", "1"),
    ("aparāmaṭṭhā", QUAL[9], "1"), ("anupādāniyā", QUAL[10], "1"), ("asaṃkilesiko", QUAL[11], "2"),
    ("doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ",
     ", ".join(KILESA[1:] + [ANOTTAPPA]), "1"),
    ("rāgo", "sự tham đắm", "2"),
    ("āsevati bhāveti bahulīkaroti", "thực hành, tu tập, làm đi làm lại", "2"),
    ("cattāro satipaṭṭhānā", CATTARO, "2"),
    ("cattāro sammappadhānā, cattāro iddhipādā, pañcindriyāni, pañca balāni, satta bojjhaṅgā",
     "bốn nỗ lực đúng đắn, bốn nền tảng thần thông, năm năng lực, năm sức mạnh, bảy chi phần giác ngộ", "2"),
    ("satisambojjhaṅgo … upekkhāsambojjhaṅgo", ", ".join(BOJJH), "2"),
    ("sokaparidevadukkhadomanassa-", "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn", "2"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "2"),
    ("tathāgato", "Như Lai", "2"),
    ("arahato sammāsambuddhassa (homage)", "bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn", "1"),
    ("sati santiṭṭhati", "sự tỉnh thức phù hợp với điều ấy đứng vững", "2"),
    ("cakkavattī", "vua chuyển luân", "2"),
    ("anussati", "sự nhớ lại", "1"),
    ("sammappadhāna- … bojjhaṅga- (pl.)", "các nỗ lực đúng đắn", "ch2"),
    ("iddhipāda- … (pl.)", "các nền tảng thần thông", "ch2"),
    ("bojjhaṅga- (pl.)", "các chi phần giác ngộ", "ch2"),
]


def check_reused8():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                          for p in sorted(d.glob("*.md")))).lower()
    texts["ch2"] = unicodedata.normalize("NFC", (S.OUT_DIR / "2-parihanikatha.md").read_text(encoding="utf-8")).lower()
    bad = [(p, v, b) for p, v, b in REUSED8 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    add("5-8-0", f"### {H_KATHA}")

    # ---- ^5-301 ------------------------------------------------------------------------------------------------
    l3 = f"{Q(TH)} {YES} {Q(f'{ALL} là {SATI_FULL}, {ALL} là {AN_FULL}')} {NO_PE}"
    chain10 = f"{PE} ".join(AY + KILESA + [ANOTTAPPA])       # sotāyatanaṃ… … anottappaṃ
    l4 = (f"{Q(TH)} {YES} {Q(is_sp(CAKKHU))} {NO_PE} {q(is_sp(CAKKHU))} {YES} "
          f"{Q(f'{CAKKHU} là {SATI_SHORT}, {CAKKHU} là {AN_FULL}')} {NO_PE} "
          f"{q(is_sp(chain10))} {NO_PE} {q(is_sp(ANOTTAPPA))} {YES} "
          f"{Q(f'{ANOTTAPPA} là {SATI5.rsplit(chr(44), 1)[0]}{PE} {ANUSSATI[8]}, {ANUSSATI[9]}')} {NO_PE}")
    # ^ "Anottappaṃ sati satindriyaṃ satibalaṃ sammāsati…pe… kāyagatāsati upasamānussatīti?"
    ay_l5 = [S.A[k] for k in ("sotāyatana", "kāyāyatana", "rūpāyatana", "phoṭṭhabbāyatana")]
    chain5 = f"{PE} ".join(ay_l5 + [K["rāgo"], K["doso"], K["moho"], ANOTTAPPA])
    #   Sotāyatanaṃ…pe… kāyāyatanaṃ… rūpāyatanaṃ…pe… phoṭṭhabbāyatanaṃ… rāgo… doso… moho…pe… anottappaṃ
    sati_is = f"{SATI} là {SP_SG}"                           # Sati satipaṭṭhānā (termbase)
    l5 = (f"{Q(f'{sati_is}, {AND_IS}')} {YES} {Q(f'{is_sp(CAKKHU)}, {AND_IS}')} {NO_PE} "
          f"{q(f'{sati_is}, {AND_IS}')} {YES} {Q(f'{is_sp(chain5)}, {AND_IS}')} {NO_PE}")
    l6 = (f"{Q(f'{is_sp(CAKKHU)}, {AND_NOT}')} {YES} {Q(f'{sati_is}, {AND_NOT}')} {NO_PE} "
          f"{q(f'{is_sp(chain5)}, {AND_NOT}')} {YES} {Q(f'{sati_is}, {AND_NOT}')} {NO_PE}")
    add("5-301", l3, l4, l5, l6)

    # ---- ^5-302 ------------------------------------------------------------------------------------------------
    l8 = f"{S.na_vattabbam(TH)} {YES} {NANU(ARABBHA_ALL)} {YES} {S.hanci(ARABBHA_ALL, TH)}"
    base = f"{vi(arabbha(SATI), TH)} {YES}"
    l9 = f"{base} {vi(arabbha('sự tiếp xúc'), f'{ALL} là các sự thiết lập tiếp xúc')} {NO_PE}"
    #   phasso santiṭṭhati … phassapaṭṭhānā
    chain = f"{arabbha(S.VEDANA)}{PE} {S.SANNA} đứng vững{PE} chủ ý đứng vững{PE} tâm đứng vững"
    #   vedanā santiṭṭhati… saññā santiṭṭhati… cetanā santiṭṭhati… cittaṃ santiṭṭhati
    l10 = f"{base} {vi(chain, f'{ALL} là các sự thiết lập tâm')} {NO_PE}"
    l11 = f"{Q(TH)} {YES} {Q(UPATTHITA)} {NO_PE}"
    add("5-302", l8, l9, l10, l11)

    # ---- ^5-303 ------------------------------------------------------------------------------------------------
    l13 = (f"{Q(TH)} {YES} {S.NANU_VUTTAM} “{AMATA}” [{S.CIT['a. ni.']} 1.600]. {S.ATTHEVA} {YES} "
           f"{Q(f'{BEINGS} {PARIBHUNJ} {KAYAGATA}')} {NO_PE}")
    l14 = (f"{Q(TH)} {YES} {S.NANU_VUTTAM} “{EKAYANA_SUTTA}” {CIT_EKAYANA}! {S.ATTHEVA} {YES_Q} "
           f"{Q(f'{ALL} là {EKAYANA}')} {NO_PE}")
    l15 = f"{Q(TH)} {YES} {S.NANU_VUTTAM} “{RATANA_SUTTA_1}"
    q_tath = (f"do sự xuất hiện của {TATHAGATA}, {ALL} thật sự trở thành các {R} {BOJJH[0]}")
    #   Tathāgatassa pātubhāvā arahato sammāsambuddhassa sabbe dhammā satisambojjhaṅgaratanāva honti
    #   (eva «thật», hoti «trở thành»: termbase)
    l16 = (f"“{RATANA_SUTTA_2}” [{S.CIT['saṃ. ni.']} 5.223]. {S.ATTHEVA} {YES} {Q(q_tath)} {NO_PE} "
           f"{q(TH)} {YES} {Q(f'{ALL} là ' + f'{PE} '.join(OTHERS))} {NO_PE}")
    add("5-303", l13, l14, l15, l16, END_KATHA)
    return segs


def main():
    check_reused8()
    S.write(NAME, build())


if __name__ == "__main__":
    main()
