# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 2: 2-parihanikatha.md (Parihānikathā).

Imports the approved sample builder (build_sample_vi, read-only) and uses its frames verbatim.
Every repeated formula is a fixed string or helper below, so every repeat is byte-identical.
Run:  python -I -X utf8 build_2_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "2-parihanikatha.md"
Q, q, NANU, AMANTA, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
TENA_VATA, NO_CA_VATA = B.TENA_VATA, B.NO_CA_VATA
VAR, SPELL = B.VAR, B.SPELL

# ================================================================ persons, fruits, the thesis
AR = "bậc A-la-hán"                    # arahā (pi-4)
SO = "bậc vào dòng"                    # sotāpanno (pi-4)
SA = "bậc trở lại một lần"             # sakadāgāmī (pi-4)
AN = "bậc không trở lại"               # anāgāmī (pi-4)
SV = "bậc A-la-hán được giải thoát theo từng thời điểm"         # samayavimutto arahā (samayavimutto pi-4)
ASV = "bậc A-la-hán được giải thoát không theo từng thời điểm"  # asamayavimutto arahā (pi-4)
FRUIT = {AR: "trạng thái A-la-hán",                # arahatta (style rule: the state of an arahant)
         SO: "thành quả vào dòng",                 # sotāpattiphala (pi-4)
         SA: "thành quả trở lại một lần",          # sakadāgāmiphala (pi-4)
         AN: "thành quả không trở lại"}            # anāgāmiphala (pi-4)
FRUIT[SV] = FRUIT[ASV] = FRUIT[AR]
PARIHAYATI = "sa sút khỏi"            # parihāyati + abl. (pi-4 parihāyeyya «sa sút khỏi»)
PARIHANI = "sự suy thoái"             # parihāni / parihāna (pi-2 parihāniya «dẫn đến suy thoái»; approved heading)


def P(x, neg=False):
    """parihāyati X X-phalā / na parihāyati …"""
    return f"{x} {'không ' if neg else ''}{PARIHAYATI} {FRUIT[x]}"


def PAM(x):
    """X X-phalā parihāyamāno"""
    return f"{x}, khi {PARIHAYATI} {FRUIT[x]},"


# ================================================================ vocabulary
R, D, M = "sự tham đắm", "sự sân hận", "sự si mê"            # rāgo, doso, moho (pi-1)
MANA, DI, VI = "sự kiêu mạn", "quan điểm", "sự hoài nghi"     # māno, diṭṭhi, vicikicchā (pi-1 kilesa list)
TH, UD = "sự uể oải", "sự xao động"                           # thinaṃ, uddhaccaṃ (pi-1)
AH, AO = "sự không biết hổ thẹn", "sự không biết ghê sợ tội lỗi"   # ahirikaṃ, anottappaṃ (pi-1)
SK = "quan điểm về tự ngã"                                     # sakkāyadiṭṭhi (pi-1)
SB = "sự hiểu sai lệch về giới hạnh và nghi thức"              # sīlabbataparāmāso (pi-1)
APAYA = "dẫn đến cõi khổ"                                      # apāyagamanīyo (new; apāya «cõi khổ» sample)
AP_R, AP_D, AP_M = f"{R} {APAYA}", f"{D} {APAYA}", f"{M} {APAYA}"
OK = "sự tham đắm dục lạc ở dạng thô"                          # oḷāriko kāmarāgo (oḷārika «ở dạng thô» pi-1)
OB = "ác ý ở dạng thô"                                         # oḷāriko byāpādo (byāpāda «ác ý» pi-1/pi-4)
AK = "sự tham đắm dục lạc ở dạng nhỏ nhiệm"                    # aṇusahagato kāmarāgo (new)
AB = "ác ý ở dạng nhỏ nhiệm"                                   # aṇusahagato byāpādo (new)
ARA_TEN = [D, M, MANA, DI, VI, TH, UD, AH, AO]                 # doso … anottappaṃ (arahato)
PAHINA = "đã được dứt bỏ"                                      # pahīno / pahīnā / pahīnaṃ (pi-2)
DUKKHA, SAMUDAYA, NIRODHA, MAGGA = "khổ đau", "sự phát sinh", "sự chấm dứt", "con đường"   # pi-1
SACCA4 = "bốn sự thật"                                         # cattāri saccāni (pi-3)
SEEN = "đã thấy"                                               # diṭṭhaṃ / diṭṭho / diṭṭhāni
DEV6 = ["các sự thiết lập tỉnh thức", "các nỗ lực đúng đắn", "các nền tảng thần thông", "các năng lực",
        "các sức mạnh", "các chi phần giác ngộ"]               # satipaṭṭhānā … bojjhaṅgā (pi-3 ^3-2)
BHAVITA = "đã tu tập"                                          # bhāvito / bhāvitā (maggaṃ bhāveti «tu tập con đường» pi-1)
BH = {"magga": "sự tu tập con đường"}                          # maggabhāvanā
BH6 = [f"sự tu tập {x}" for x in DEV6]                         # satipaṭṭhānabhāvanā … bojjhaṅgabhāvanā
PAHANAYA = "để dứt bỏ"                                         # -ppahānāya
UC = ("đã bị cắt đứt tận gốc, đã bị làm cho như cây thốt nốt bị chặt ngọn, đã bị làm cho không còn hiện "
      "hữu{v}, có bản chất không nảy sinh trong tương lai")
# ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo (āyatiṃ anuppāda «không nảy sinh trong tương lai» pi-2)
EP = ["đã lìa tham đắm", "đã lìa sân hận", "đã lìa si mê",            # vītarāgo vītadoso vītamoho (pi-2)
      "đã làm xong việc cần làm", "đã đặt gánh nặng xuống", "đã đạt đến mục đích của chính mình",
      "đã diệt tận hoàn toàn xiềng xích của sự hiện hữu", "đã được giải thoát nhờ hiểu biết trọn vẹn một cách đúng đắn",
      "đã nhấc bỏ thanh chắn", "đã lấp hào", "đã nhổ cột trụ", "đã tháo then cửa", "là bậc thánh",
      "đã hạ ngọn cờ", "đã buông bỏ gánh nặng", "đã thoát khỏi trói buộc", "đã chiến thắng trọn vẹn"]
# katakaraṇīyo ohitabhāro anuppattasadattho parikkhīṇabhavasaṃyojano sammadaññāvimutto ukkhittapaligho
# saṅkiṇṇaparikho abbūḷhesiko niraggaḷo ariyo pannaddhajo pannabhāro visaññutto suvijitavijayo
# (= build_3_vi.py ARA_EPI, byte-identical without its «một phần»)
LAST_EP = "điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm"   # sacchikātabbaṃ sacchikataṃ
TR = ("khổ đau đã được người ấy hiểu biết trọn vẹn, sự phát sinh đã được dứt bỏ, sự chấm dứt đã được tự mình "
      "chứng nghiệm, con đường đã được tu tập, điều cần được hiểu biết trực tiếp đã được hiểu biết trực tiếp, "
      "điều cần được hiểu biết trọn vẹn đã được hiểu biết trọn vẹn, điều cần dứt bỏ đã được dứt bỏ, điều cần "
      f"được tu tập đã được tu tập, {LAST_EP}")
# dukkhaṃ tassa pariññātaṃ … sacchikātabbaṃ sacchikataṃ (abhiññeyya … sacchikātabba pi-2 ^2-1030)
EP_SHORT = f"{EP[0]}, {EP[1]}, {EP[2]}… {LAST_EP}"           # vītarāgo vītadoso vītamoho…pe… sacchikātabbaṃ sacchikataṃ
ARA = ["sự ưa thích công việc", "sự ưa thích nói chuyện", "sự ưa thích ngủ nghỉ", "sự ưa thích tụ tập"]  # pi-2 ^2-U63
KR = ("sự tham đắm, sự tham đắm dục lạc, sự ám ảnh của tham đắm dục lạc, xiềng xích tham đắm dục lạc, "
      "dòng lũ dục lạc, ách dục lạc, chướng ngại ý muốn dục lạc")
# rāgo kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmogho kāmayogo kāmacchandanīvaraṇaṃ
ANUSAYA = "các khuynh hướng tiềm ẩn"                         # anusayā (pi-2)
AN7 = ("khuynh hướng tiềm ẩn tham đắm dục lạc, khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, "
       "khuynh hướng tiềm ẩn quan điểm, khuynh hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm hiện hữu, "
       "khuynh hướng tiềm ẩn vô minh")                       # kāmarāgānusayo … avijjānusayo (pi-2 ^2-816)
UPACAYA = "tăng trưởng"                                       # upacayaṃ gacchati (upacaya «sự tăng trưởng» pi-1)
THERA = "trưởng lão"                                          # thero (pi-4)
V_NOVATA = f"[{VAR} (Syā., Pī.): no vata re, cũng vậy ở các chỗ sau]"   # [no vata re (syā. pī.) evamuparipi] (pi-4 label)


def seen(x, items, neg=False):
    """X-ena dukkhaṃ diṭṭhaṃ…pe… cattāri saccāni diṭṭhāni, (na) parihāyati X X-phalā"""
    return f"{x} {chain([f'{SEEN} {i}' for i in items])}, và {P(x, neg)}"


def pah(x, items, neg=False):
    """X-assa A pahīno…pe… Z pahīno, (na) parihāyati X X-phalā"""
    parts = [f"{items[0]} của {x} {PAHINA}"] + [f"{i} {PAHINA}" for i in items[1:]]
    return f"{chain(parts)}, và {P(x, neg)}"


def dev(x, purposes, items):
    """X-assa A-ppahānāya…pe… Z-ppahānāya maggo bhāvito…pe… bojjhaṅgā bhāvitā"""
    return f"{chain([f'{PAHANAYA} {p}' for p in purposes])}, {x} {chain([f'{BHAVITA} {i}' for i in items])}"


def devq(x, purposes, items, neg=False):
    return f"{dev(x, purposes, items)}, và {P(x, neg)}"


def pair(a, b, end=NHP):
    return f"{Q(a)} {AMANTA} {Q(b)} {end}"


def hanci_no(p, qq, variant=""):
    """Hañci P, no ca vata re vattabbe – "Q"ti."""
    frame = NO_CA_VATA.replace("thì này bạn,", f"thì này bạn {variant},", 1) if variant else NO_CA_VATA
    return f"Nếu {p}, {frame} “{qq}”."


def hanci_semi(p, qq, end="."):
    """Hañci P; tena vata re vattabbe – "Q"ti."""
    return f"Nếu {p}; {TENA_VATA} “{qq}”{end}"


def build():
    d = B.Doc()
    d.head(3, B.KATHA.format(x=PARIHANI), "5-2-0")
    # ------------------------------------------------------------ Vādayuttiparihāni
    d.head(4, "Sự suy thoái xét theo lập luận", "5-2-1-0")
    lines = []
    for adv in ("ở mọi nơi", "vào mọi lúc"):                    # sabbattha / sabbadā (sample)
        x = f"{P(AR)} {adv}"
        lines.append(f"{Q(P(AR))} {AMANTA} {Q(x)} {NHP} {q(x)} {AMANTA} "
                     f"{Q(f'{adv} đều có {PARIHANI} của {AR}')} {NHP}")
    allx = f"tất cả các {AR} đều {PARIHAYATI} {FRUIT[AR]}"
    lines.append(f"{Q(P(AR))} {AMANTA} {Q(allx)} {NHP} {q(allx)} {AMANTA} "
                 f"{Q(f'tất cả các {AR} đều có {PARIHANI}')} {NHP}")
    lines.append(f"{Q(P(AR))} {AMANTA} {Q(PAM(AR) + ' thì sa sút khỏi bốn thành quả')} {NHP}")
    setthi = "một phú hộ giữ địa vị phú hộ nhờ có bốn trăm nghìn, khi mất đi một trăm nghìn,"
    lines.append(pair(f"{setthi} thì bị sa sút khỏi địa vị phú hộ", "người ấy bị sa sút khỏi toàn bộ tài sản"))
    lines.append(pair(f"{setthi} thì có khả năng sa sút khỏi toàn bộ tài sản",
                      f"{PAM(AR)} thì có khả năng sa sút khỏi bốn thành quả"))
    d.seg("5-239", *lines)
    # ------------------------------------------------------------ Ariyapuggalasaṃsandanaparihāni
    d.head(4, "Sự suy thoái xét qua đối chiếu các bậc thánh", "5-2-2-0")
    pos = [(AR, SO), (AR, SA), (AR, AN), (AN, SO), (AN, SA), (SA, SO)]
    neg = [(SO, AR), (SA, AR), (AN, AR), (SO, AN), (SA, AN), (SO, SA)]
    d.seg("5-240", *[pair(P(a), P(b)) for a, b in pos], *[pair(P(a, True), P(b, True)) for a, b in neg])
    ST = "đứng vững trong"     # saṇṭhāti + loc. (= build_4_vi.py SANTHATI «đứng vững trong»)
    stops = (f"{PAM(AR)} {ST} {FRUIT[AN]}, {PAM(AN)} {ST} {FRUIT[SA]}, "
             f"{PAM(SA)} {ST} {FRUIT[SO]}")
    puthu = f"{PAM(SO)} {ST} địa vị của người phàm phu"     # puthujjanabhūmiyaṃ saṇṭhāti
    d.seg("5-241",
          f"{Q(P(AR))} {AMANTA} {cap(PAM(AR))} đứng vững ở đâu? Trong {FRUIT[AN]}. {cap(PAM(AN))} đứng vững ở đâu? "
          f"Trong {FRUIT[SA]}. {cap(PAM(SA))} đứng vững ở đâu? Trong {FRUIT[SO]}. {Q(puthu)} {NH}",
          f"{B.AJANAHI['n']} {hanci_semi(stops, puthu)}",
          pair(f"{PAM(AR)} {ST} {FRUIT[SO]}",
               f"ngay sau {FRUIT[SO]}, vị ấy tự mình chứng nghiệm chính {FRUIT[AR]}"))

    def kil(a, b):
        return (f"{pair(P(a), P(b))} phiền não của ai {PAHINA} nhiều hơn, của {a} hay của {b}? Của {a}. "
                f"{hanci_semi(f'phiền não của {a} {PAHINA} nhiều hơn, và {P(a)}', P(b))}")

    d.seg("5-242", *[kil(a, b) for a, b in ((AR, SO), (AR, SA), (AR, AN), (AN, SO))])
    d.seg("5-243", *[kil(a, b) for a, b in ((AN, SA), (SA, SO))])

    def bhav(a, b, what, last, end="."):
        return (f"{pair(P(a), P(b))} {what} của ai vượt trội hơn, của {a} hay của {b}? Của {a}. "
                f"{hanci_semi(f'{last} của {a} vượt trội hơn, và {P(a)}', P(b), end)}")

    mb = chain([BH["magga"], BH6[-1]])
    d.seg("5-244",
          bhav(AR, SO, BH["magga"], BH["magga"]),
          bhav(AR, SO, chain(BH6), BH6[-1]),
          bhav(AR, SA, mb, BH6[-1]),
          bhav(AR, AN, mb, BH6[-1]))
    d.seg("5-245", bhav(AN, SO, mb, BH6[-1]), bhav(AN, SA, mb, BH6[-1]))
    d.seg("5-246", bhav(SA, SO, mb, BH6[-1], end="…"))
    # ------------------------------------------------------------ seen
    D4 = [SAMUDAYA, NIRODHA, MAGGA, SACCA4]
    DS = [DUKKHA, SACCA4]
    lines = [pair(seen(AR, [x]), seen(SO, [x])) for x in [DUKKHA] + D4]
    lines += [pair(seen(AR, [DUKKHA]), seen(SA, [DUKKHA])), pair(seen(AR, D4), seen(SA, [SACCA4])),
              pair(seen(AR, [DUKKHA]), seen(AN, [DUKKHA])), pair(seen(AR, D4), seen(AN, [SACCA4]))]
    d.seg("5-247", *lines)
    d.seg("5-248",
          pair(seen(AN, [DUKKHA]), seen(SO, [DUKKHA])), pair(seen(AN, D4), seen(SO, [SACCA4])),
          pair(seen(AN, [DUKKHA]), seen(SA, [DUKKHA])), pair(seen(AN, D4), seen(SA, [SACCA4])))
    d.seg("5-249", pair(seen(SA, [DUKKHA]), seen(SO, [DUKKHA])), pair(seen(SA, D4), seen(SO, [SACCA4])))
    d.seg("5-250",
          pair(seen(SO, [DUKKHA], True), seen(AR, [DUKKHA], True)),
          pair(seen(SO, D4, True), seen(AR, [SACCA4], True)),
          pair(seen(SA, DS, True), seen(AR, [SACCA4], True)),
          pair(seen(AN, DS, True), seen(AR, [SACCA4], True)),
          f"{Q(seen(SO, DS, True))} {AMANTA}",                  # ^5-250 line 5 ends with Āmantā. (as written)
          f"{Q(seen(AN, DS, True))} {NHP}",
          pair(seen(SA, DS, True), seen(AN, DS, True)),
          pair(seen(SO, DS, True), seen(SA, DS, True)))
    # ------------------------------------------------------------ abandoned
    V_THINA = f"{TH} [{SPELL} (Sī., Syā., Kaṃ., Pī.): thīnaṃ]"
    SO5 = [VI, SB, AP_R, AP_D, AP_M]
    SA4 = [VI, SB, OK, OB]
    AN4 = [VI, SB, AK, AB]

    def pp(a, ia, b, ib, neg=False, end=NHP):
        return pair(pah(a, ia, neg), pah(b, ib, neg), end)

    d.seg("5-251",
          pp(AR, [R], SO, [SK]), pp(AR, [R], SO, SO5),
          pp(AR, [D, M, MANA, DI, VI, V_THINA, UD, AH, AO], SO, [SK]),
          pp(AR, [AO], SO, SO5),
          pp(AR, [R], SA, [SK], end=NH), pp(AR, [R], SA, SA4), pp(AR, [D, AO], SA, [SK, OB], end=NH),
          pp(AR, [R], AN, [SK]), pp(AR, [R], AN, AN4, end=NH), pp(AR, [D, AO], AN, [SK, AB], end=NH))
    d.seg("5-252",
          pp(AN, [SK], SO, [SK], end=NH), pp(AN, [SK], SO, [VI, AP_M], end=NH),
          pp(AN, [VI, AB], SO, [SK, AP_M], end=NH),
          pp(AN, [SK], SA, [SK], end=NH), pp(AN, [SK], SA, SA4, end=NH), pp(AN, [VI, AB], SA, [SK, OB], end=NH))
    d.seg("5-253",
          pp(SA, [SK], SO, [SK], end=NH), pp(SA, [SK], SO, [VI, AP_M], end=NH),
          pp(SA, [VI, OK, OB], SO, [SK, AP_M], end=NH))
    d.seg("5-254",
          pp(SO, [SK], AR, [R], True, NH), pp(SO, [SK], AR, [D, AO], True, NH),
          pp(SO, [VI, AP_M], AR, [R, AO], True, NH))
    d.seg("5-255", pp(SA, [SK], AR, [R, AO], True, NH), pp(SA, [VI, OB], AR, [R, AO], True, NH))
    d.seg("5-256", pp(AN, [SK], AR, [R, AO], True, NH), pp(AN, [VI, AB], AR, [R, AO], True, NH))
    d.seg("5-257", pp(SO, [SK], AN, [SK, AB], True, NH), pp(SO, [VI, AP_M], AN, [SK, AB], True, NH))
    d.seg("5-258", pp(SA, [SK], AN, [SK, AB], True, NH), pp(SA, [VI, OB], AN, [SK, AB], True, NH))
    d.seg("5-259", pp(SO, [SK], SA, [SK, OB], True, NH), pp(SO, [VI, AP_M], SA, [SK, OB], True, NH))
    # ------------------------------------------------------------ Nanu … (^5-260, ^5-261)
    r_pah = f"{R} của {AR} {PAHINA}"
    ten = chain([f"{ARA_TEN[0]} của {AR} {PAHINA}"] + [f"{i} {PAHINA}" for i in ARA_TEN[1:]])
    uc0 = UC.format(v="")
    d1 = dev(AR, [R], ["con đường"])
    d6 = dev(AR, [R], DEV6)
    d6b = dev(AR, [R], [DEV6[-1]])
    dx = dev(AR, [D, AO], ["con đường", DEV6[-1]])
    dxb = dev(AR, [AO], [DEV6[-1]])
    d.seg("5-260",
          f"{Q(P(AR))} {AMANTA} {NANU(r_pah + ', ' + UC.format(v=f' [{SPELL} (Sī.): anabhāvakato]'))} {AMANTA} "
          f"{hanci_no(f'{r_pah}, {uc0}', P(AR), V_NOVATA)}",
          f"{Q(P(AR))} {AMANTA} {NANU(f'{ten}, {uc0}')} {AMANTA} "
          f"{hanci_no(f'{AO} của {AR} {PAHINA}, {uc0}', P(AR))}",
          f"{Q(P(AR))} {AMANTA} {NANU(d1)} {AMANTA} {hanci_no(d1, P(AR))}",
          f"{Q(P(AR))} {AMANTA} {NANU(d6)} {AMANTA} {hanci_no(d6b, P(AR))}",
          f"{Q(P(AR))} {AMANTA} {NANU(dx)} {AMANTA} {hanci_no(dxb, P(AR))}")
    d.seg("5-261",
          f"{Q(P(AR))} {AMANTA} {NANU(f'{AR} ' + ', '.join(EP) + '; ' + TR)} {AMANTA} "
          f"{hanci_no(f'{AR} {EP_SHORT}', P(AR))}")
    # ------------------------------------------------------------ samayavimutta (^5-262, ^5-263)
    mbj = ["con đường", DEV6[-1]]
    d.seg("5-262",
          f"{Q(P(AR))} ( ) [(āmantā) (Ka.)] {cap(P(SV))}, {P(ASV, True)}. {Q(P(SV))} {AMANTA} "
          f"Có phải {P(ASV)} [{VAR} (Ka.): na parihāyatīti] không? {NH}",
          pair(P(ASV, True), P(SV, True), NH),
          pair(pah(SV, [R]), pah(ASV, [R]), NH),
          pair(pah(SV, [D, AO]), pah(ASV, [AO]), NH),
          pair(devq(SV, [R], ["con đường"]), devq(ASV, [R], ["con đường"]), NH),
          pair(devq(SV, [R], DEV6), devq(ASV, [R], [DEV6[0], DEV6[-1]]), NH),
          pair(devq(SV, [D, AO], mbj), devq(ASV, [AO], mbj), NHP),
          pair(f"{SV} " + ", ".join(EP) + ", " + TR + f", và {P(SV)}", f"{ASV} {EP_SHORT}, và {P(ASV)}", NH))
    d.seg("5-263",
          pair(pah(ASV, [R], True), pah(SV, [R], True), NH),
          pair(pah(ASV, [D, AO], True), pah(SV, [AO], True), NH),
          pair(devq(ASV, [R], mbj, True), devq(SV, [R], mbj, True), NH),
          pair(devq(ASV, [D, AO], mbj, True), devq(SV, [AO], mbj, True), NH),
          pair(f"{ASV} {EP_SHORT}, và {P(ASV, True)}", f"{SV} {EP_SHORT}, và {P(SV, True)}", NHP))
    # ------------------------------------------------------------ the great elders (^5-264)
    PT = f"đã {PARIHAYATI} {FRUIT[AR]}"          # parihāyittha arahattā
    NPT = f"đã không {PARIHAYATI} {FRUIT[AR]}"   # na parihāyittha arahattā
    SARI = f"{THERA} Xá-lợi-phất"                # sāriputto thero (Xá-lợi-phất pi-4)
    names = [("Đại Mục-kiền-liên", f" [{SPELL} (Ka.): mahāmoggalāno]"), ("Đại Ca-diếp", ""),
             ("Đại Ca-chiên-diên", f" [{VAR} (Trung Bộ Kinh 1.202 và các chỗ khác): mahākaccāno]"),
             ("Đại Câu-hy-la", f" [{VAR} (Sī., Syā., Kaṃ., Pī.): mahākoṭṭhito]"), ("Đại Bàn-đặc", "")]
    d.seg("5-264",
          f"{Q(P(AR))} {AMANTA} {Q(f'{SARI} {PT}')} {NH} "
          f"Có phải {chain([f'{THERA} {n}{v}' for n, v in names])} {PT} không? {NH}",
          f"{Q(f'{SARI} {NPT}')} {AMANTA} {hanci_no(f'{SARI} {NPT}', P(AR))}",
          f"Có phải {chain([f'{THERA} {n}' for n, _ in names])} {NPT} không? {AMANTA} "
          f"{hanci_no(f'{THERA} {names[-1][0]} {NPT}', P(AR))}",
          "Sự đối chiếu các bậc thánh.")
    # ------------------------------------------------------------ Suttasādhanaparihāni
    d.head(4, "Sự suy thoái xét qua chứng cứ từ kinh", "5-2-3-0")
    CH = "đối với điều đã được cắt đứt, có điều cần phải cắt"   # atthi chinnassa chediyaṃ
    d.seg("5-265",
          f"{Q(P(AR))} {AMANTA} {B.NANU_VUTTAM}",
          f"“Quả thật, các cách thực hành [{SPELL} (Chú giải): paṭipādā] cao và thấp đã được bậc sa-môn công bố;",
          "Người ta không đi đến bờ bên kia hai lần, nhưng điều này cũng không được xem là chỉ một lần” "
          "[Kinh Tập 719, trong Kinh Tập].",
          f"{B.ATTHEVA} {AMANTA} {B.TENA_HI_NA(P(AR))}",
          f"{Q(P(AR))} {AMANTA} {Q(CH)} {NH}",
          f"{Q(CH)} {AMANTA} {B.NANU_VUTTAM}",
          "“Người đã lìa khao khát, không còn nắm giữ, không có việc gì cần làm;",
          "Đối với điều đã được cắt đứt, không có điều cần phải cắt, dòng lũ và cạm bẫy đã được nhổ bỏ”.",
          f"{B.ATTHEVA} {AMANTA} {B.TENA_HI_NA(CH)}")
    KP = "có sự bồi đắp thêm cho điều đã làm"                  # atthi katassa paticayo
    d.seg("5-266",
          f"{Q(P(AR))} {AMANTA} {Q(KP)} {NH}",
          f"{Q(KP)} {AMANTA} {B.NANU_VUTTAM}",
          "“Với vị tỳ-khưu ấy, đã được giải thoát đúng đắn, có tâm an tịnh;",
          "Không có sự bồi đắp thêm cho điều đã làm, không có việc gì cần làm.",
          "“Như tảng đá liền một khối, không bị gió lay động;",
          "Cũng vậy, các hình sắc, các vị, các âm thanh, các mùi và các vật xúc chạm, tất cả trọn vẹn.",
          "“Các hiện tượng đáng mong muốn và không đáng mong muốn, không làm rung động bậc như vậy;",
          "Tâm vị ấy vững vàng, được giải thoát, và vị ấy quán sát sự suy tàn của nó” "
          "[Đại Phẩm 244; Tăng Chi Bộ Kinh 6.55].",
          f"{B.ATTHEVA} {AMANTA} {B.TENA_HI_NA(KP)}")
    SAMAYA_BH = "vị tỳ-khưu được giải thoát theo từng thời điểm"   # samayavimuttassa bhikkhuno
    sutta = (f"Này các tỳ-khưu, có năm hiện tượng này dẫn đến {PARIHANI} của {SAMAYA_BH}. Năm hiện tượng nào? "
             f"{cap(ARA[0])}, {', '.join(ARA[1:])}, và vị ấy không xem xét lại tâm theo như nó đã được giải thoát. "
             f"Này các tỳ-khưu, đây là năm hiện tượng dẫn đến {PARIHANI} của {SAMAYA_BH}")
    d.seg("5-267",
          f"{B.NA_VATTABBAM_Q(P(AR))} {AMANTA} {B.NANU_VUTTAM} “{sutta}” [Tăng Chi Bộ Kinh 5.149]. "
          f"{B.ATTHEVA} {AMANTA} {B.TENA_HI(P(AR))}",
          f"{Q(f'{AR} có {ARA[0]}')} {NH}",
          pair(f"{AR} có {ARA[0]}", f"{AR} có {KR}", NH),
          f"Có phải {AR} có {ARA[1]}, {AR} có {ARA[2]}, {AR} có {ARA[3]} không? {NH}",
          pair(f"{AR} có {ARA[3]}", f"{AR} có {KR}", NH))
    has_an = f"{AR} có {ANUSAYA}"
    src = (f"Sự ám ảnh sinh khởi tùy thuộc vào cái gì? Sinh khởi tùy thuộc vào khuynh hướng tiềm ẩn.")
    # Pariyuṭṭhānaṃ kiṃ paṭicca uppajjatīti? Anusayaṃ paṭicca uppajjatīti. (pariyuṭṭhāna «sự ám ảnh» pi-1/pi-2)
    grow3 = f"{SK} {UPACAYA}, {VI} {UPACAYA}, {SB} {UPACAYA}"
    acts = ["tích lũy", "giảm trừ", "dứt bỏ", "bám víu", "phân tán", "gom tụ", "dập tắt", "nhen nhóm"]
    # ācinati apacinati pajahati upādiyati visineti ussineti vidhūpeti sandhūpeti (ācaya / apacaya pi-1)
    stood = []
    for a, b, done in (("tích lũy", "giảm trừ", "giảm trừ"), ("dứt bỏ", "bám víu", "dứt bỏ"),
                       ("phân tán", "gom tụ", "phân tán"), ("dập tắt", "nhen nhóm", "dập tắt")):
        x = f"{AR} không {a} cũng không {b}, mà đứng vững sau khi đã {done}"
        stood.append(f"{NANU(x)} {AMANTA} {hanci_no(x, P(AR))}")
    d.seg("5-268",
          f"{Q(P(AR))} {AMANTA} {cap(PAM(AR))} bị cái gì ám ảnh mà sa sút? Bị {R} ám ảnh mà sa sút. {src} "
          f"{Q(has_an)} {NH}",
          pair(has_an, f"{AR} có {AN7}", NH),
          f"Bị {D} ám ảnh mà sa sút… bị {M} ám ảnh mà sa sút… {src} {Q(has_an)} {NHP}",
          pair(has_an, f"{AR} có khuynh hướng tiềm ẩn tham đắm dục lạc… khuynh hướng tiềm ẩn vô minh", NH),
          f"{Q(P(AR))} {AMANTA} Đối với {AR} đang {PARIHAYATI} {FRUIT[AR]}, cái gì {UPACAYA}? "
          f"{cap(R)} {UPACAYA}. {Q(grow3)} {NH} {cap(D)} {UPACAYA}… {M} {UPACAYA}, có phải {grow3} không? {NH}",
          f"{Q(P(AR))} {AMANTA} " + " ".join(f"{Q(f'{AR} {a}')} {NH}" for a in acts),
          *stood,
          B.KATHA_END.format(x=PARIHANI))
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS_BOOK = [
    ("sa sút khỏi", 4), ("người được giải thoát theo từng thời điểm", 4),
    ("người được giải thoát không theo từng thời điểm", 4), ("thành quả vào dòng", 4),
    ("thành quả trở lại một lần", 4), ("thành quả không trở lại", 4), ("thành quả A-la-hán", 4),
    ("bậc vào dòng", 4), ("bậc trở lại một lần", 4), ("bậc không trở lại", 4), ("bậc A-la-hán", 4),
    ("bốn thành quả", 2), ("người phàm phu", 4), ("tự mình chứng nghiệm", 4), ("phiền não", 1),
    ("vượt trội", 4), ("tu tập con đường", 1),
    ("bốn sự thật", 3), ("bốn sự thiết lập tỉnh thức; (8) bốn nỗ lực đúng đắn; (9) bốn nền tảng thần thông", 3),
    ("năm năng lực; (13) năm sức mạnh; (14) bảy chi phần giác ngộ", 3),
    ("sự phát sinh", 1), ("sự chấm dứt", 1), ("khổ đau", 1), ("con đường", 1),
    ("sự tham lam, sự sân hận, sự si mê, sự kiêu mạn, quan điểm, sự hoài nghi, sự uể oải, sự xao động, sự "
     "không biết hổ thẹn, sự không biết ghê sợ tội lỗi", 1),
    ("sự tham đắm", 1), ("quan điểm về tự ngã", 1), ("sự hiểu sai lệch về giới hạnh và nghi thức", 1),
    ("ác ý", 1), ("ở dạng thô", 1), ("đã được dứt bỏ", 2), ("dứt bỏ", 1),
    ("đã lìa tham đắm", 2), ("đã lìa sân hận", 2), ("đã lìa si mê", 2),
    ("Sự ưa thích công việc, sự ưa thích nói chuyện, sự ưa thích ngủ nghỉ, sự ưa thích tụ tập", 2),
    ("dẫn đến suy thoái", 2), ("sự tham đắm dục lạc", 1), ("ám ảnh của tham đắm dục lạc", 2),
    ("xiềng xích tham đắm dục lạc", 1), ("chướng ngại ý muốn dục lạc", 1), ("dòng lũ vô minh", 1),
    ("ách vô minh", 1), ("khuynh hướng tiềm ẩn", 2),
    ("khuynh hướng tiềm ẩn tham đắm dục lạc, khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, "
     "khuynh hướng tiềm ẩn quan điểm, khuynh hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm hiện hữu, "
     "khuynh hướng tiềm ẩn vô minh", 2),
    ("sự tăng trưởng", 1), ("sự tích lũy", 1), ("sự giảm trừ", 1),
    ("cần được hiểu biết trực tiếp, cần được hiểu biết trọn vẹn", 2), ("cần được tu tập", 2),
    ("cần được tự mình chứng nghiệm", 2), ("trưởng lão", 4), ("Xá-lợi-phất", 4), ("Mục-kiền-liên", 4),
    ("sa-môn", 2), ("xem xét lại", 1), ("cách thực hành", 1), ("khao khát", 1), ("dòng lũ", 1),
    ("then cài", 1), ("cao quý", 1), ("vị tỳ-khưu", 2), ("quán sát", 2), ("hình sắc", 1),
    ("vật xúc chạm", 2), ("đã đứng vững", 4), ("cũng vậy ở các chỗ sau", 4), ("sinh khởi tùy thuộc vào", 1),
    ("không nảy sinh", 2), ("trong tương lai", 2), ("hiểu biết trọn vẹn", 2), ("xiềng xích", 1),
    ("sự trói buộc", 1), ("ngọn cờ", 1), ("các bậc thánh", 4), ("Tăng Chi Bộ Kinh", 4), ("Trung Bộ Kinh", 4),
    ("được giải thoát", 4), ("hiện tượng", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings found in pi-1..4 rails")


def main():
    check_cross_book()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line-check problems"
    (B.OUT_DIR / NAME).write_bytes(text.encode("utf-8"))
    segs = text.count(" ^")
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines, {segs} IDs; "
          f"odd closing order repaired: {len(repaired)}")
    print("line checks: OK")


if __name__ == "__main__":
    main()
