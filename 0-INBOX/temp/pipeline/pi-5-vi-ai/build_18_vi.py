# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 18: 18-dasamavaggo.md (Dasamavaggo, ^5-18-0 … ^5-604),
the eleven kathā (95)-(105) of the tenth vagga, its uddāna and the close of the second fifty-group
(Dutiyo paṇṇāsako. + its uddāna).

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_10_vi / build_11_vi / build_12_vi / build_14_vi / build_15_vi (read-only; importing writes nothing)
for strings shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur
in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run
against the Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_18_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –)
import build_11_vi as C11    # noqa: E402  (dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ)
import build_12_vi as C12    # noqa: E402  (L10 phassa … paññā, ten(), samannāgata, puthujjana)
import build_14_vi as C14    # noqa: E402  (cakkhuñca paṭicca … / attheva suttanto frames)
import build_15_vi as C15    # noqa: E402  (āvaṭṭanā … paṇidhi, kusalākusalā …, suvidūra sutta, latā …)

NAME = "18-dasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA, ATTHEVA, NANU_VUTTAM = (B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA, B.ATTHEVA,
                                                   B.NANU_VUTTAM)
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA10 = B.VAGGA[10]                                     # Dasamavaggo = «Chương thứ mười» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
NUM = B.NUM
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
ATTHEVA_IN = C14.ATTHEVA_IN                               # attheva suttanto (inside a sentence, ch10 / ch14)
ATTHEVA_LC = B.ATTHEVA[0].lower() + B.ATTHEVA[1:]         # "…" – attheva suttantoti? (ch14)
NATTHI = "Không có."                                      # Natthi. (answer, ch11 / ch12 / ch14)
S = B.SAMMA                                               # sammādiṭṭhi … sammāsamādhi (pi-1, pi-2)
AY = B.AYATANA                                            # lĩnh vực mắt … (pi-2)
L10 = C12.L10                                             # phassa … paññā (ch4 / ch12)
L8 = L10[1:4] + L10[5:]                                   # vedanā … paññā without phassa, citta (ch15 L12 order)

# ================================================================ kathā names (headings and closing lines)
KX = {1: "sự chấm dứt",                                   # Nirodhakathā (terms file)
      2: "việc cho rằng vật chất là con đường",           # Rūpaṃ maggotikathā (rūpa «vật chất» pi-2)
      3: "con đường của người có được năm loại thức",     # Pañcaviññāṇasamaṅgissa maggakathā
      4: "việc cho rằng năm loại thức vừa là thiện vừa là bất thiện",   # Pañcaviññāṇā kusalāpi akusalāpītikathā
      5: "việc cho rằng có sự chú hướng",                 # Sābhogātikathā (ābhoga «sự chú hướng» pi-2)
      6: "hai giới hạnh",                                 # Dvīhisīlehikathā (sīla «giới hạnh» pi-1)
      7: "việc cho rằng giới hạnh không phải là yếu tố đồng hành với tâm",   # Sīlaṃ acetasikantikathā (pi-1)
      8: "việc cho rằng giới hạnh không vận hành theo tâm",   # Sīlaṃ na cittānuparivattītikathā (pi-1)
      9: "sự thọ trì làm nguyên nhân",                    # Samādānahetukathā (samādiyati «thọ trì» pi-2)
      10: "việc cho rằng sự biểu lộ là giới hạnh",        # Viññatti sīlantikathā (viññatti «sự biểu lộ» pi-1)
      11: "việc cho rằng sự không biểu lộ là sự phạm giới"}   # Aviññatti dussilyantikathā (dussilya pi-1, pi-4)


def heads(n):
    """#### Dasamavaggo ^5-18-n-0 / ##### (94+n) n. <title> ^5-18-n-1-0"""
    return [(4, VAGGA10, f"5-18-{n}-0"), (5, f"({94 + n}) {n}. {K(x=KX[n])}", f"5-18-{n}-1-0")]


# ================================================================ (95) Nirodha
UPK = "năm khối tìm cầu sự tái sinh"                      # upapattesiye pañcakkhandhe (ch12 upapattesiyaṃ cittaṃ)
KIR = "mang tính chức năng"                               # kiriyā (pi-1 kiriyābyākata «… mang tính chức năng»)
NOT_CEASED = f"khi {UPK} chưa chấm dứt"                   # … aniruddhe
CEASED = f"khi {UPK} đã chấm dứt"                         # … niruddhe
SAMMUKHI = "đi đến chỗ cùng hiện diện đối mặt nhau"       # sammukhībhāvaṃ āgacchanti (ch15; ch5 «cùng hiện diện đối mặt nhau»)
TWO_PE = C15.TWO_PE                                       # dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ (ch15)
MB = "tu tập con đường"                                   # maggaṃ bhāveti (ch3)


def samkh(n):
    """N-annaṃ khandhānaṃ samodhānaṃ hoti, N khandhā sammukhībhāvaṃ āgacchanti"""
    return f"có sự tụ hợp của {NUM[n]} khối, {NUM[n]} khối {SAMMUKHI}"


def nirodha_line(what, n):
    return f"{Q(f'{NOT_CEASED}, {what} sinh khởi')} {AM} {Q(samkh(n))} {NHP} {q(samkh(n))} {AM} {Q(TWO_PE)} {NHP}"


# ================================================================ (96) Rūpaṃ maggo
MS = "người có được con đường"                            # maggasamaṅgī (pi-1 ariyamaggasamaṅgī, ^1-1373)
T96 = f"vật chất của {MS} là con đường"                   # maggasamaṅgissa rūpaṃ maggo
SAR, ANAR = C15.SAR, C15.ANAR                             # sārammaṇa / anārammaṇa (pi-3, ch15)


def sa(neg=False, pe=True):
    """(an)ārammaṇaṃ, (n)atthi tassa āvaṭṭanā…pe… paṇidhi (ch15 att)"""
    return f"{ANAR if neg else SAR}, {C15.att(neg=neg, pe=pe)}"


def mg(x, neg=False):
    """X maggo, sā / so ca (an)ārammaṇā, (n)atthi tāya / tassa āvaṭṭanā…pe… paṇidhi"""
    return f"{x} là con đường, và nó {'không ' if neg else ''}có đối tượng, {C15.att(neg=neg, pe=True)}"


def magga_unit(x, last=None, first_full=False):
    """X maggoti? Āmantā. Sārammaṇo, …? Na hevaṃ…pe… nanu anārammaṇo …? Āmantā. Hañci …; no ca vata re –
    "LAST maggo"ti.  (first_full: the full āvaṭṭanā list as in ^5-573 line 1)"""
    th = f"{x} là con đường"
    end = f"{last or x} là con đường"
    return (f"{Q(th)} {AM} {Q(sa(pe=not first_full))} {NHP} {nanu_l(sa(True))} {AM} "
            f"{hanci_no(sa(True), end, sep=';')}")


# ================================================================ (97)-(99) pañcaviññāṇā
P5 = "năm loại thức"                                      # pañcaviññāṇā (pi-1, pi-2 pañca viññāṇā)
CV, MV = "thức qua mắt", "ý thức"                         # cakkhuviññāṇa / manoviññāṇa (pi-2)
T97 = f"người có được {P5} có sự {MB}"                    # pañcaviññāṇasamaṅgissa atthi maggabhāvanā
T_CV = f"người có được {CV} có sự {MB}"                   # cakkhuviññāṇasamaṅgissa atthi maggabhāvanā
T_MV = f"người có được {MV} có sự {MB}"                   # manoviññāṇasamaṅgissa atthi maggabhāvanā
KA = "vừa là thiện vừa là bất thiện"                      # kusalāpi akusalāpi / kusalampi akusalampi
T98 = f"{P5} {KA}"
ABH, ANABH = "có sự chú hướng", "không có sự chú hướng"   # sābhoga / anābhoga (pi-2 ^Ñāṇavibhaṅga (13))
T99 = f"{P5} {ABH}"
PI2 = ["Có chỗ dựa đã sinh khởi và có đối tượng đã sinh khởi",
       "Có chỗ dựa đã sinh ra trước và có đối tượng đã sinh ra trước",
       "Có chỗ dựa thuộc phần bên trong và có đối tượng thuộc phần bên ngoài",
       "Có chỗ dựa chưa tan rã và có đối tượng chưa tan rã",
       "Có chỗ dựa khác nhau và có đối tượng khác nhau",
       "Không trải nghiệm phạm vi hoạt động của nhau", "Không sinh khởi khi không có sự lưu ý",
       "Không sinh khởi khi không chú tâm", "Không sinh khởi liền mạch", "Không sinh khởi không trước không sau",
       "Không sinh khởi liền sau nhau"]
# pi-2 ^Ñāṇavibhaṅga (2)-(12) uppannavatthukā … na aññamaññassa samanantarā uppajjanti; the pi-2 «và» between the
# vatthu / ārammaṇa pair is not in this Pāli (no ca) and is dropped (coordinator: add no word)
CH = [x[0].lower() + x[1:].replace(" và có ", ", có ") for x in PI2]
U1 = CH[0]                                                # uppannavatthukā uppannārammaṇā
LIST = ", ".join(CH[1:10])                                # purejātavatthukā … na apubbaṃ acarimaṃ uppajjanti
LAST = CH[10]                                             # na aññamaññassa samanantarā uppajjanti
SUN = "sự trống rỗng"                                     # suññataṃ (ch11)
AT = "quá khứ và tương lai"                               # atītānāgataṃ (ch6)
OB = {"phassa": "sự tiếp xúc", "vedana": "cảm giác", "sanna": "tri giác", "cetana": "chủ ý", "citta": "tâm",
      "cakkhu": "mắt", "kaya": "thân", "sadda": "âm thanh", "photth": "vật xúc chạm"}   # (pi-1, pi-2)
EYE_SUN = C14.eye_with(SUN)                               # cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇaṃ
SUTTA_EYE = C14.SUTTA_EYE                                 # cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ (pi-2)


def five_u(th):
    """Nanu pañcaviññāṇā uppannavatthukā uppannārammaṇāti? Āmantā. Hañci …, no ca vata re vattabbe – "TH"ti."""
    return f"{NANU(f'{P5} {U1}')} {AM} {hanci_no(f'{P5} {U1}', th)}"


def five_l(th, last_in_nanu=False):
    """Nanu pañcaviññāṇā purejātavatthukā … , nanu pañcaviññāṇā anābhogā (or: na aññamaññassa samanantarā
    uppajjanti) ti? Āmantā. Hañci …, no ca vata re vattabbe – "TH"ti."""
    if last_in_nanu:
        return (f"Chẳng phải {P5} {LIST}, chẳng phải {P5} {LAST} sao? {AM} {hanci_no(f'{P5} {LAST}', th)}")
    return (f"Chẳng phải {P5} {LIST}, {LAST}, chẳng phải {P5} {ANABH} sao? {AM} "
            f"{hanci_no(f'{P5} {ANABH}', th)}")


def lay(x):
    """X-ṃ ārabbha (pi-1 rūpaṃ ārabbha «lấy hình sắc làm đối tượng»)"""
    return f"lấy {x} làm đối tượng"


def ar(x, who=CV):
    """W X-ṃ ārabbha uppajjati"""
    return f"{who} {lay(x)} mà sinh khởi"


def arl(who, keys):
    """W A-ṃ ārabbha…pe… B-ṃ ārabbha … uppajjati"""
    return f"{who} {chain([lay(OB[k]) for k in keys])} mà sinh khởi"


def eye_tail(open_quote=True, natthi_pe=False):
    """"cakkhuñca paṭicca suññatañca …"nti – attheva suttantoti? Natthi. "cakkhuñca paṭicca rūpe ca …"nti – attheva
    suttantoti? Āmantā. Hañci "…"nti – attheva suttanto, no ca vata re vattabbe – "cakkhuñca … suññatañca …"nti.
    (ch14 frame; open_quote=False: ^5-581 has no opening quote in the Pāli; natthi_pe: ^5-585 Natthi…pe…)"""
    first = f"“{cap(EYE_SUN)}”" if open_quote else f"{cap(EYE_SUN)}”"
    nat = f"{NATTHI[:-1]}… “{SUTTA_EYE}”" if natthi_pe else f"{NATTHI} “{cap(SUTTA_EYE)}”"
    return (f"{first} – {ATTHEVA_IN} không? {nat} – {ATTHEVA_LC} {AM} "
            f"Nếu “{SUTTA_EYE}” – {ATTHEVA_IN}, {B.NO_CA_VATA} “{EYE_SUN}”.")


NOT_G = "không nắm giữ dấu hiệu tổng quát"                # na nimittaggāhī hoti (pi-1 ^1-1354)
NOT_G_FULL = f"{NOT_G}, không nắm giữ các chi tiết"       # na nimittaggāhī hoti nānubyañjanaggāhī (pi-1)
YES_G = "nắm giữ dấu hiệu tổng quát"                      # nimittaggāhī hoti (pi-1 ^1-1352)
MONK = "Này các tỳ-khưu, ở đây, vị tỳ-khưu khi thấy hình sắc bằng mắt thì"   # idha, bhikkhave, bhikkhu cakkhunā rūpaṃ disvā
EAR = "khi nghe âm thanh bằng tai"                        # sotena saddaṃ sutvā (pi-1)
BODY = "khi chạm vật xúc chạm bằng thân thì"              # kāyena phoṭṭhabbaṃ phusitvā (pi-1)
SUTTA_NO = (f"“{MONK} {NOT_G_FULL}… {EAR}… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… {BODY} {NOT_G_FULL}” "
            "[Trung Bộ Kinh 1.349; Tăng Chi Bộ Kinh 4.37]!")
SUTTA_G = f"“{MONK} {YES_G}… {NOT_G}… {EAR}… {BODY} {YES_G}… {NOT_G}”!"   # ^5-583
SUTTA_G2 = f"“{MONK} {YES_G}… {NOT_G}… {BODY} {YES_G}… {NOT_G}”!"         # ^5-586 (no sotena)

# ================================================================ (100) Dvīhi sīlehi
SL = "giới hạnh"                                          # sīla (pi-1 sīlavipatti «sự suy đồi về giới hạnh»)
SAM = C12.SAM                                             # samannāgato «được trang bị» (pi-2, pi-4, ch12)
T100 = f"{MS} {SAM} hai {SL}"                             # maggasamaṅgī dvīhi sīlehi samannāgato
LOK = "thuộc thế gian"                                    # lokiya (pi-1)
LL = "thuộc thế gian và vượt thế gian"                    # lokiya ca lokuttara ca (pi-1)
L10L = [L10[0], L10[1], L10[9]] + L10[3:]                 # phassa vedanā PAÑÑĀ cetanā citta … paññā (as written)
PUTHU = C12.PUTHU                                         # puthujjano «người phàm phu» (pi-1, ch4)
DUS3 = "người phạm giới, có giới hạnh bị sứt mẻ, có giới hạnh bị cắt đứt"   # dussīlo khaṇḍasīlo chinnasīlo


def ms(x):
    return f"{MS} {SAM} {x}"


def lk(items, tag):
    return chain([f"{x} {tag}" for x in items])


# ================================================================ (101)-(102) acetasika / cittānuparivatti
CET = "là yếu tố đồng hành với tâm"                       # cetasika (pi-1, ch15)
ACET = "không phải là yếu tố đồng hành với tâm"           # acetasika (pi-1 ^1-M2-57)
T101 = f"{SL} {ACET}"
CA, NCA = "vận hành theo tâm", "không vận hành theo tâm"  # (no) cittānuparivatti (pi-1 ^1-M2-62)
T102 = f"{SL} {NCA}"
IT = "có kết quả đáng mong muốn"                          # iṭṭhaphala (sample ^5 ch1)
ANIT = "có kết quả không đáng mong muốn"                  # aniṭṭhaphala (sample ch1)
SPV = "có kết quả, có quả trổ"                            # saphalaṃ savipākaṃ (sample ch1)
APV = "không có kết quả, không có quả trổ"                # aphalaṃ avipākaṃ
AVP, SVP = "không có quả trổ", "có quả trổ"               # avipāka / savipāka (sample ch1 savipāka)
DUS_HOTI = f"khi {SL} đã sinh khởi rồi chấm dứt, thì trở thành người phạm giới"   # sīle uppajjitvā niruddhe dussīlo hoti
SANKH4 = f"{S[1]}… {S[5]}… {S[6]}… {S[7]}"                 # sammāsaṅkappo…pe… sammāsamādhi
KA2 = f"{S[3]}… {S[4]}"                                   # sammākammanto…pe… sammāājīvo
OBJ4 = f"là vật chất… Niết-bàn… {AY[0]}… {AY[4]}… {AY[5]}… {AY[9]}"   # rūpaṃ…pe… phoṭṭhabbāyatanaṃ (^5-590)
OBJ2 = f"là vật chất… Niết-bàn… {AY[0]}… {AY[9]}"         # rūpaṃ… nibbānaṃ… cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
LATER5 = chain(L8[4:])                                    # vīriyaṃ…pe… sati…pe… samādhi…pe… paññā

# ================================================================ (103) Samādānahetu
SAMAD = "sự thọ trì"                                      # samādāna (pi-2 samādiyati «thọ trì»)
T103 = f"{SL} có nguyên nhân từ {SAMAD} tăng trưởng"      # samādānahetukaṃ sīlaṃ vaḍḍhati (ch15 vaḍḍhati)
GROW = ", ".join([f"{L10[0]} có nguyên nhân từ {SAMAD} tăng trưởng"] + [f"{x} tăng trưởng" for x in L10[1:]])
LATA = ("Có phải tăng trưởng như dây leo, tăng trưởng như dây quấn, tăng trưởng như cây, tăng trưởng như cỏ, "
        "tăng trưởng như đám cỏ lau không?")              # latā viya vaḍḍhati … (ch15 ^5-483)
VIT3 = ("khởi lên sự hướng tâm đến dục lạc, khởi lên sự hướng tâm đến ác ý, khởi lên sự hướng tâm đến sự hãm hại")
# kāma- / byāpāda- / vihiṃsāvitakkaṃ vitakkentassa (ch15 ^5-485, pi-2)
KSD_A = C15.KSD_A                                         # kusalākusalā … sammukhībhāvaṃ āgacchanti (pi-4, ch15)
FAR = C15.FAR                                             # suvidūravidūra «điều rất xa cách nhau» (ch15)
FAR4 = (f"“Này các tỳ-khưu, có bốn {FAR} này! Bốn điều nào? Này các tỳ-khưu, bầu trời và mặt đất – đây là {FAR} "
        "thứ nhất… vì vậy, giáo pháp của người hiền thiện ở xa kẻ không hiền thiện”.")   # (ch15 ^5-485, abridged)
VERSE = ("“Những người trồng vườn cây, trồng rừng… đứng vững trong Giáo Pháp, thành tựu về giới hạnh, những người "
         "ấy đi đến cõi trời”.")                          # ārāmaropā vanaropā…pe… saggagāmino (ch15 ^5-486, abridged)

# ================================================================ (104)-(105) viññatti / aviññatti
VN, AVN = "sự biểu lộ", "sự không biểu lộ"                # viññatti (pi-1) / aviññatti
DUSS = "sự phạm giới"                                     # dussilya (pi-1 ^1-1368, pi-4 ^4-61)
T104 = f"{VN} là {SL}"
T105 = f"{AVN} là {DUSS}"
BAD = ["việc sát hại sinh mạng", "việc lấy của không được cho", "hành vi sai trái trong các dục lạc",
       "việc nói dối", C15.SURA]                          # pāṇātipāto … surāmerayamajjapamādaṭṭhānaṃ (pi-2)
VER = [f"sự kiềm chế {x}" for x in BAD]                   # pāṇātipātā veramaṇī … (pi-2 ^2-703)
GREET = ["sự đảnh lễ", "sự đứng dậy chào đón", "sự chắp tay", "sự kính cẩn đúng phép", "việc mang đến chỗ ngồi",
         "việc mang đến chỗ nằm", "việc mang đến nước rửa chân", "việc mang đến miếng chà chân",
         "việc chà lưng khi tắm"]
# abhivādanaṃ paccuṭṭhānaṃ añjalikammaṃ sāmīcikammaṃ āsanābhihāro seyyābhihāro pādodakābhihāro
# pādakathalikābhihāro nhāne piṭṭhiparikammaṃ
PAPA = "đã thọ trì nghiệp xấu ác"                         # pāpakammaṃ samādinno āsi (pāpaka «xấu ác» pi-1)
BOTH = "cả phước và điều không phải phước, cả hai đều tăng trưởng"   # puññañca apuññañca ubho vaḍḍhanti (ch11 ubho)
GIVE_PAPA = f"đối với người đã thọ trì nghiệp xấu ác rồi thực hiện sự bố thí, {BOTH}"
# pāpakammaṃ samādiyitvā dānaṃ dadantassa … (dānaṃ deti «thực hiện sự bố thí» ch15)


def neg_list(items, first_cap=True):
    """Xti? Na hevaṃ vattabbe…pe… yti? Na hevaṃ vattabbe…pe… (each «có phải là …»)"""
    return " ".join(f"{(Q if i == 0 and first_cap else q)(f'là {x}')} {NHP}" for i, x in enumerate(items))


# ================================================================ uddāna
UDD = (f"{cap(NOT_CEASED)}, năm khối {KIR} sinh khởi, {T96}, {T97}, {T98}, {T99}, {T100}, {T101}, {T102}, {T103}, "
       f"{T104}, {T105}.")
# Upapattesiye … uppajjanti, maggasamaṅgissa rūpaṃ maggo, …, viññattisīlaṃ aviññatti dussilyanti.
DUTIYO = "Nhóm năm mươi thứ hai."                         # Dutiyo paṇṇāsako. (coordinator, ch13 pattern)
UDD50 = (f"Sự cố định, sự gộp vào, cõi tái sinh, lợi ích, và sự chấm dứt [{VAR} (Sī., Syā., Ka.): niyāma "
         "saṅgahagatānisaṃsatā atthi pañcavokārabhavo nirodho maggasamaṅgissa pañcavokārabhavoti; "
         f"{VAR} (Pī.): niyāma saṅgaha gatānisaṃsatā atthi pañcavokārabhavo maggasamaṅgissa no pañcavokārabhavo].")
# Niyāmasaṅgahagatānisaṃsatā ca nirodhoti: the first kathā of vaggas 6-10 (niyāma ch14, saṅgaha ch15 «sự gộp
# vào», gati «cõi tái sinh» sample / terms (73), ānisaṃsa «lợi ích» terms (84), nirodha)


def build():
    d = B.Doc()
    d.head(3, VAGGA10, "5-18-0")
    # ------------------------------------------------------------ (95) Nirodha
    d.head(4, f"(95) 1. {K(x=KX[1])}", "5-18-1-0")
    d.seg("5-571",
          nirodha_line(f"năm khối {KIR}", 10),
          nirodha_line(f"bốn khối {KIR}", 9),
          nirodha_line(f"hiểu biết {KIR}", 6))
    d.seg("5-572",
          f"{Q(f'{CEASED}, con đường sinh khởi')} {AM} "
          f"{Q(f'người đã chết {MB}, người đã qua đời {MB}')} {NHP}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (96) Rūpaṃ maggo
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-573",
          f"{Q(T96)} {AM} {Q(sa(pe=False))} {NHP} {nanu_l(sa(True))} {AM} {hanci_no(sa(True), T96, sep=';')}",
          magga_unit(S[2]),
          magga_unit(KA2, last=S[4]))
    d.seg("5-574",
          f"{Q(mg(S[0]))} {AM} {Q(mg(S[2]))} {NHP} {q(mg(S[0]))} {AM} {Q(mg(KA2))} {NHP} "
          f"{S[1]}… {S[5]}… {S[6]}…",
          f"{Q(mg(S[7]))} {AM} {Q(mg(S[2]))} {NHP} {q(mg(S[7]))} {AM} {Q(mg(KA2))} {NHP}",
          f"{Q(mg(S[2], True))} {AM} {Q(mg(S[0], True))} {NHP} {q(mg(S[2], True))} {AM} "
          f"{Q(mg(SANKH4, True))} {NHP}",
          f"{Q(mg(KA2, True))} {AM} {Q(mg(f'{S[0]}… {SANKH4}', True))} {NHP}")
    three = f"{S[2]}, {S[3]}, {S[4]} là con đường"
    d.seg("5-575",
          f"{NVQ(T96)} {AM} {NANU(three)} {AM} {hanci_yes(three, T96)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (97) Pañcaviññāṇasamaṅgissa magga
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-576",
          f"{Q(T97)} {AM} {five_u(T97)}",
          five_l(T97))
    d.seg("5-577",
          f"{Q(T_CV)} {AM} {Q(ar(SUN))} {NHP} {q(ar(SUN))} {AM} {Q(EYE_SUN)} {NHP} {q(EYE_SUN)} {AM} {eye_tail()}")
    pv_f = ["phassa", "vedana", "photth"]
    d.seg("5-578",
          f"{Q(T_CV)} {AM} {Q(ar(AT))} {NHP} {q(T_CV)} {AM} "
          f"{Q(arl(CV, ['phassa', 'vedana', 'sanna', 'cetana', 'citta', 'cakkhu', 'kaya', 'sadda', 'photth']))} {NHP}",
          f"{Q(f'{T_MV}, {ar(SUN, MV)}')} {AM} {Q(f'{T_CV}, {ar(SUN)}')} {NHP} "
          f"{q(f'{T_MV}, {ar(AT, MV)}')} {AM} {Q(f'{T_CV}, {ar(AT)}')} {NHP} "
          f"{q(f'{T_MV}, {arl(MV, pv_f)}')} {AM} {Q(f'{T_CV}, {arl(CV, pv_f)}')} {NHP}")
    d.seg("5-579",
          f"{NVQ(T97)} {AM} {NANU_VUTTAM} {SUTTA_NO} {ATTHEVA} {AM} {TENA_HI(T97)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (98) Pañcaviññāṇā kusalāpi akusalāpi
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-580", f"{Q(T98)} {AM} {five_u(T98)} {five_l(T98)}")
    d.seg("5-581",
          f"{Q(f'{CV} là thiện')} {AM} {Q(ar(SUN))} {NHP} {q(ar(SUN))} {AM} {Q(EYE_SUN)} {NH} {Q(EYE_SUN)} {AM} "
          f"{eye_tail(open_quote=False)}")
    cka = f"{CV} {KA}"
    mka = f"{MV} {KA}"
    m_list = arl(MV, ["phassa", "citta", "kaya", "sadda", "photth"])
    c_list = arl(CV, ["phassa", "photth"])
    d.seg("5-582",
          f"{Q(cka)} {AM} {Q(ar(AT))} {NHP} {Q(cka)} {AM} "
          f"{Q(arl(CV, ['phassa', 'citta', 'cakkhu', 'kaya', 'sadda', 'photth']))} {NHP}",
          f"{Q(f'{mka}, {ar(SUN, MV)}')} {AM} {Q(f'{cka}, {ar(SUN)}')} {NHP} "
          f"{q(f'{mka}, {ar(AT, MV)}')} {AM} {Q(f'{cka}, {ar(AT)}')} {NHP} "
          f"{q(f'{mka}, {m_list}')} {AM} {Q(f'{cka}, {c_list}')} {NHP}")
    d.seg("5-583",
          f"{NVQ(T98)} {AM} {NANU_VUTTAM} {SUTTA_G} {ATTHEVA} {AM} {TENA_HI(T98)}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (99) Sābhoga
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-584", f"{Q(T99)} {AM} {five_u(T99)} {five_l(T99, last_in_nanu=True)}")
    cs = f"{CV} {ABH}"
    pf2 = ["phassa", "photth"]
    d.seg("5-585",
          f"{Q(cs)} {AM} {Q(ar(SUN))} {NHP} {q(ar(SUN))} {AM} {Q(EYE_SUN)} {NHP} {q(EYE_SUN)} {AM} "
          f"{eye_tail(natthi_pe=True)}",
          f"{Q(cs)} {AM} {Q(ar(AT))} {NHP} {q(cs)} {AM} {Q(arl(CV, pf2))} {NHP} "
          f"{q(f'{MV} {ABH}, {ar(SUN, MV)}')} {AM} {Q(f'{cs}, {ar(SUN)}')} {NHP} "
          f"{q(f'{MV} {ABH}, {ar(AT, MV)}')} {AM} {Q(f'{cs}, {ar(AT)}')} {NHP} "
          f"{q(f'{MV} {ABH}, {arl(MV, pf2)}')} {AM} {Q(f'{cs}, {arl(CV, pf2)}')} {NHP}")
    d.seg("5-586",
          f"{NVQ(T99)} {AM} {NANU_VUTTAM} {SUTTA_G2} {ATTHEVA} {AM} Vậy thì {T99}…",
          E(x=KX[5]))
    # ------------------------------------------------------------ (100) Dvīhi sīlehi
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    lok10 = ", ".join(f"{x} {LOK}" for x in L10L)
    ll_pe = f"{ms(f'{L10[0]} {LL}')}… {SAM} {L10[9]} {LL}"   # … phassena samannāgato…pe… paññāya samannāgato
    d.seg("5-587",
          f"{Q(T100)} {AM} {Q(ms(C12.ten(2)))} {NHP}",
          f"{Q(ms(f'{SL} {LOK}'))} {AM} {Q(ms(lok10))} {NHP}",
          f"{Q(ms(f'{SL} {LL}'))} {AM} {Q(ll_pe)} {NHP} "
          f"{q(ms(f'{SL} {LOK}'))} {AM} {Q(f'{MS} là {PUTHU}')} {NHP}")
    d.seg("5-588",
          f"{Q(ms(f'{S[2]} {LOK}'))} {AM} {Q(ms(f'{S[0]} {LOK}'))} {NHP} {q(ms(f'{S[2]} {LOK}'))} {AM} "
          f"{Q(ms(lk([S[1], S[5], S[6], S[7]], LOK)))} {NHP} {q(ms(lk([S[3], S[4]], LOK)))} {AM} "
          f"{Q(ms(lk([S[0], S[7]], LOK)))} {NHP}",
          f"{Q(ms(f'{S[2]} {LL}'))} {AM} {Q(ms(f'{S[0]} {LL}'))} {NHP} {q(ms(f'{S[2]} {LL}'))} {AM} "
          f"{Q(ms(lk([S[1], S[5], S[6], S[7]], LL)))} {NHP}",
          f"{Q(ms(f'{S[3]} {LL}… {S[4]}'))} {AM} {Q(ms(f'{S[0]} {LL}'))} {NHP} {q(ms(f'{S[4]} {LL}'))} {AM} "
          f"{Q(ms(lk([S[1], S[7]], LL)))} {NHP}")
    d.seg("5-589",
          f"{NVQ(T100)} {AM} {Q(f'khi {SL} {LOK} đã chấm dứt, con đường sinh khởi')} {AM} "
          f"{Q(f'{DUS3} {MB}')} {NHP} vậy thì {T100}.",
          E(x=KX[6]))
    # ------------------------------------------------------------ (101) Sīlaṃ acetasikaṃ
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-590",
          f"{Q(T101)} {AM} {Q(OBJ4)} {NHP} {q(T101)} {AM} {Q(f'{L10[0]} {ACET}')} {NHP} {q(T101)} {AM} "
          f"{Q(f'{chain(L8)} {ACET}')} {NHP}",
          f"{Q(f'{L10[0]} {CET}')} {AM} {Q(f'{SL} {CET}')} {NHP} {q(f'{chain(L8)} {CET}')} {AM} "
          f"{Q(f'{SL} {CET}')} {NHP}")
    d.seg("5-591",
          f"{Q(T101)} {AM} {Q(ANIT)} {NHP} {nanu_l(IT)} {AM} {hanci_no(IT, T101)}",
          f"{Q(f'{L10[5]} {IT}, {L10[5]} {CET}')} {AM} {Q(f'{SL} {IT}, {SL} {CET}')} {NHP} "
          f"{q(f'{LATER5} {IT}, {L10[9]} {CET}')} {AM} {Q(f'{SL} {IT}, {SL} {CET}')} {NHP}",
          f"{Q(f'{SL} {IT}, {T101}')} {AM} {Q(f'{L10[5]} {IT}, {L10[5]} {ACET}')} {NHP} "
          f"{q(f'{SL} {IT}, {T101}')} {AM} {Q(f'{LATER5} {IT}, {L10[9]} {ACET}')} {NHP}")
    ay4 = chain([AY[1], AY[4], AY[5], AY[9]])            # sotāyatanaṃ…pe… kāyāyatanaṃ … phoṭṭhabbāyatanaṃ
    d.seg("5-592",
          f"{Q(T101)} {AM} {Q(APV)} {NHP} {nanu_l(SPV)} {AM} Nếu {SPV}, {B.NO_CA_VATA} “{T101}”…",
          f"{Q(f'{AY[0]} {ACET}, {AVP}')} {AM} {Q(f'{T101}, {AVP}')} {NHP} {q(f'{ay4} {ACET}, {AVP}')} {AM} "
          f"{Q(f'{T101}, {AVP}')} {NHP}",
          f"{Q(f'{T101}, {SVP}')} {AM} {Q(f'{AY[0]} {ACET}, {SVP}')} {NHP} {q(f'{T101}, {SVP}')} {AM} "
          f"{Q(f'{ay4} {ACET}, {SVP}')} {NHP}")
    d.seg("5-593",
          f"{Q(f'{S[2]} {ACET}')} {AM} {Q(f'{S[0]} {ACET}')} {NHP} {q(f'{S[2]} {ACET}')} {AM} "
          f"{Q(f'{SANKH4} {ACET}')} {NHP} {q(f'{KA2} {ACET}')} {AM} {Q(f'{S[0]} {ACET}')} {NHP} "
          f"{q(f'{S[4]} {ACET}')} {AM} {Q(f'{SANKH4} {ACET}')} {NHP}",
          f"{Q(f'{S[0]} {CET}')} {AM} {Q(f'{S[2]} {CET}')} {NHP} {q(f'{S[0]} {CET}')} {AM} "
          f"{Q(f'{KA2} {CET}')} {NHP} {q(f'{SANKH4} {CET}')} {AM} {Q(f'{S[2]} {CET}')} {NHP} "
          f"{q(f'{S[7]} {CET}')} {AM} {Q(f'{KA2} {CET}')} {NHP}")
    d.seg("5-594",
          f"{NVQ(T101)} {AM} {Q(DUS_HOTI)} {NH} {TENA_HI(T101)}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (102) Sīlaṃ na cittānuparivatti
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    d.seg("5-595",
          f"{Q(T102)} {AM} {Q(OBJ2)} {NHP} {q(T102)} {AM} {Q(f'{L10[0]} {NCA}')} {NHP} {q(T102)} {AM} "
          f"{Q(f'{chain(L8)} {NCA}')} {NHP}",
          f"{Q(f'{L10[0]} {CA}')} {AM} {Q(f'{SL} {CA}')} {NHP} {q(f'{chain(L8)} {CA}')} {AM} "
          f"{Q(f'{SL} {CA}')} {NHP}")
    d.seg("5-596",
          f"{Q(f'{S[2]} {NCA}')} {AM} {Q(f'{S[0]} {NCA}')} {NHP} {q(f'{S[2]} {NCA}')} {AM} "
          f"{Q(f'{SANKH4} {NCA}')} {NHP}",
          f"{Q(f'{KA2} {NCA}')} {AM} {Q(f'{S[0]} {NCA}')} {NHP} {q(f'{S[4]} {NCA}')} {AM} "
          f"{Q(f'{SANKH4} {NCA}')} {NHP}",
          f"{Q(f'{S[0]} {CA}')} {AM} {Q(f'{S[2]} {CA}')} {NHP} {q(f'{S[0]} {CA}')} {AM} {Q(f'{KA2} {CA}')} {NHP}",
          f"{Q(f'{SANKH4} {CA}')} {AM} {Q(f'{S[2]} {CA}')} {NHP} {q(f'{S[7]} {CA}')} {AM} "
          f"{Q(f'{KA2} {CA}')} {NHP}")
    d.seg("5-597",
          f"{NVQ(T102)} {AM} {Q(DUS_HOTI)} {NH} {TENA_HI(T102)}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (103) Samādānahetu
    for lv, t, sid in heads(9):
        d.head(lv, t, sid)
    d.seg("5-598",
          f"{Q(T103)} {AM} {Q(GROW)} {NHP}",
          f"{Q(T103)} {AM} {LATA} {NHP}")
    fourfar = f"{Q(KSD_A)} {AM} {NANU_VUTTAM} {FAR4} {ATTHEVA} {AM} {TENA_HI_NA(KSD_A)}"
    d.seg("5-599",
          f"{Q(T103)} {AM} {Q(f'đối với người đã thọ trì {SL} rồi {VIT3}, {SL} tăng trưởng')} {AM} "
          f"{Q(TWO_PE)} {NHP} {q(TWO_PE)} {AM} {Q(KSD_A)} {NHP}",
          fourfar)
    d.seg("5-600",
          f"{NVQ(T103)} {AM} {NANU_VUTTAM} {VERSE} {ATTHEVA} {AM} {TENA_HI(T103)}",
          E(x=KX[9]))
    # ------------------------------------------------------------ (104) Viññatti sīlaṃ
    for lv, t, sid in heads(10):
        d.head(lv, t, sid)
    d.seg("5-601",
          f"{Q(T104)} {AM} {neg_list(VER)}",
          f"{Q(', '.join(f'{g} là {SL}' for g in GREET))} {AM} {Q(f'là {VER[0]}')} {NHP} {q(f'là {VER[4]}')} {NHP}")
    d.seg("5-602",
          f"{NVQ(T104)} {AM} {Q(f'là {DUSS}')} {NHP} vậy thì {T104}.",
          E(x=KX[10]))
    # ------------------------------------------------------------ (105) Aviññatti dussilyaṃ
    for lv, t, sid in heads(11):
        d.head(lv, t, sid)
    d.seg("5-603",
          f"{Q(T105)} {AM} {neg_list(BAD)}",
          f"{Q(GIVE_PAPA)} {NHP} {q(BOTH)} {AM} {Q(TWO_PE)} {NHP} {q(TWO_PE)} {AM} {Q(KSD_A)} {NHP}",
          fourfar)
    d.seg("5-604",
          f"{NVQ(T105)} {AM} {NANU(PAPA)} {AM} {hanci_yes(PAPA, T105)}",
          E(x=KX[11]),
          f"{VAGGA10}.",
          TASSUDDANAM,
          UDD,
          DUTIYO,
          TASSUDDANAM,
          UDD50)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("người có được con đường", 1), ("mang tính chức năng", 1), (NOT_G_FULL, 1), (f"thì {YES_G}", 1),
    ("khi thấy hình sắc bằng mắt thì", 1),
    ("Khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân", 1),
    ("lấy hình sắc làm đối tượng", 1), ("lấy âm thanh làm đối tượng", 1), ("phạm giới", 1),
    ("Mọi sự phạm giới", 4), ("Các hiện tượng không phải là yếu tố đồng hành với tâm", 1),
    ("Các hiện tượng vận hành theo tâm", 1), ("Các hiện tượng không vận hành theo tâm", 1),
    ("là sự biểu lộ", 1), ("người phàm phu", 1), ("thọ trì", 2), ("giới hạnh", 1), ("xấu ác", 1),
    ("Sự kiềm chế việc sát hại sinh mạng, sự kiềm chế việc lấy của không được cho, sự kiềm chế hành vi sai trái "
     "trong các dục lạc", 2), ("sự kiềm chế việc nói dối", 2), (VER[4], 2),
    ("năm loại thức", 2), ("Năm loại thức không có sự chú hướng", 2), ("thức qua mắt", 2), ("ý thức", 2),
    ("thuộc thế gian", 1), ("vượt thế gian", 1), ("vật xúc chạm", 1), ("Trung Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4),
] + [(x, 2) for x in PI2]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (C11.TWO, "11-tatiyavaggo.md"), (TWO_PE, "15-sattamavaggo.md"), (KSD_A, "15-sattamavaggo.md"),
    (LATA, "15-sattamavaggo.md"), (VIT3, "15-sattamavaggo.md"), (C15.ATT, "15-sattamavaggo.md"),
    (f"{SAR}; {C15.att(pe=True)}", "15-sattamavaggo.md"), (f"{ANAR}; {C15.att(neg=True, pe=True)}", "15-sattamavaggo.md"),
    (f"Này các tỳ-khưu, có bốn {FAR} này! Bốn điều nào? Này các tỳ-khưu, bầu trời và mặt đất – đây là {FAR} thứ nhất",
     "15-sattamavaggo.md"),
    ("giáo pháp của người hiền thiện ở xa kẻ không hiền thiện”", "15-sattamavaggo.md"),
    ("“Những người trồng vườn cây, trồng rừng", "15-sattamavaggo.md"),
    ("ứng vững trong Giáo Pháp, thành tựu về giới hạnh, những người ấy đi đến cõi trời”", "15-sattamavaggo.md"),
    (C15.SURA, "15-sattamavaggo.md"), ("thực hiện sự bố thí", "15-sattamavaggo.md"),
    ("những người đã qua đời", "15-sattamavaggo.md"), ("Sự gộp vào", "15-sattamavaggo.md"),
    (SUTTA_EYE, "14-chatthavaggo.md"), (f"– {ATTHEVA_IN} không? {NATTHI}", "14-chatthavaggo.md"),
    (f"– {ATTHEVA_IN}, {B.NO_CA_VATA}", "14-chatthavaggo.md"), ("sự cố định", "14-chatthavaggo.md"),
    (SPV, "1-puggalakatha.md"), (ANIT, "1-puggalakatha.md"), (IT, "1-puggalakatha.md"),
    ("tâm tìm cầu sự tái sinh", "12-catutthavaggo.md"), (f"{SAM} {C12.ten(4)}", "12-catutthavaggo.md"),
    (SAM, "12-catutthavaggo.md"), (SUN, "11-tatiyavaggo.md"), ("cả hai đều", "11-tatiyavaggo.md"),
    (MB, "3-brahmacariyakatha.md"), (AT, "6-atitakkhandhadikatha.md"), (SAMMUKHI, "15-sattamavaggo.md"),
    ("sự tụ hợp", "4-jahatikatha.md"),
    ("Nhóm năm mươi lớn.", "13-pancamavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    ("[Trung Bộ Kinh", "14-chatthavaggo.md"), ("[Tăng Chi Bộ Kinh", "15-sattamavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    cache = {}
    for s, f in PI5:
        if f not in cache:
            cache[f] = (B.OUT_DIR / f).read_text(encoding="utf-8")
        if s not in cache[f]:
            missing.append((s, f))
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch18 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and "chánh niệm" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
