# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 11: 11-tatiyavaggo.md (Tatiyavaggo, ^5-11-0 … ^5-386):
twelve kathā (21-32) with the vagga close and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame; the chapter's own
repeated phrases are fixed strings below, so every repeat is byte-identical. Every string claimed from the
pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is
asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign
letters) are run against the Pāli.

run:  python -I -X utf8 build_11_vi.py
"""
import sys
import unicodedata

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "11-tatiyavaggo.md"
Q, q, AM, AMP, cap = B.Q, B.q, B.AMANTA, B.AMANTA_PE, B.cap
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NANU, NANU_VUTTAM, ATTHEVA = B.NANU, B.NANU_VUTTAM, B.ATTHEVA
NO_CA_VATA, TENA_VATA = B.NO_CA_VATA, B.TENA_VATA
VAR, SPELL = B.VAR, B.SPELL
NATTHI_ANS = "Không có."                         # Natthi. (answer)

# ================================================================ headings (kathā wording; vagga per terms file)
VAGGA = B.VAGGA[3]                               # Tatiyavaggo = «Chương thứ ba» (terms file)
NS = "lĩnh vực không phải tri giác cũng không phải không tri giác"   # nevasaññānāsaññāyatana (pi-1, pi-2)
KX = {   # kathā name X: heading «Bàn về X», closing «Phần bàn về X đã hoàn tất.»
    1: "các sức mạnh",                           # Balakathā (terms file)
    2: "việc cho rằng là cao quý",               # Ariyantikathā (ariya «cao quý»; -nti kathā as «việc cho rằng»)
    3: "sự giải thoát",                          # Vimuttikathā (= terms file ch13 «Bàn về sự giải thoát»)
    4: "cái đang được giải thoát",               # Vimuccamānakathā
    5: "người thứ tám",                          # Aṭṭhamakakathā
    6: "các năng lực của người thứ tám",         # Aṭṭhamakassaindriyakathā / Aṭṭhamakassa indriyakathā
    7: "thiên nhãn",                             # Dibbacakkhukathā (dibbena cakkhunā «thiên nhãn» pi-1..4, sample)
    8: "tai thuộc cõi trời",                     # Dibbasotakathā (dibbā sotadhātu «yếu tố tai thuộc cõi trời» sample)
    9: "hiểu biết về việc đi theo nghiệp của mình",   # Yathākammūpagatañāṇakathā (yathākammūpage pi-2, pi-4)
    10: "sự phòng hộ",                           # Saṃvarakathā (saṃvara «sự phòng hộ», terms file ch20)
    11: "sự không có tri giác",                  # Asaññakathā (asañña- «không có tri giác» pi-2)
    12: NS,                                      # Nevasaññānāsaññāyatanakathā
}
NUMS = {n: f"({20 + n}) {n}." for n in KX}       # (21) 1. … (32) 12.


def heading(n):
    return f"{NUMS[n]} {B.KATHA.format(x=KX[n])}"


def end(n):
    return B.KATHA_END.format(x=KX[n])


# ================================================================ 1. Balakathā
TB = "sức mạnh Như Lai"                          # tathāgatabala (pi-2 ^2-830 «sức mạnh Như Lai»)
SV = "đệ tử"                                     # sāvaka (ch4, pi-4)
SVB = "sức mạnh của đệ tử"                       # sāvakabala
SADH = "là chung cho đệ tử"                      # sāvakasādhāraṇaṃ (sādhāraṇa «chung cho» ch5)
ASADH = "không chung cho đệ tử"                  # sāvakaasādhāraṇaṃ
# the objects of the ten powers (pi-2 16-nanavibhango ^2 dasa tathāgatabalāni)
TT = "điều có thể xảy ra và điều không thể xảy ra"      # ṭhānāṭhāna
KAMMA = ("quả của các nghiệp đã thực hiện trong quá khứ, tương lai và hiện tại, theo hoàn cảnh, "
         "theo nguyên nhân")                    # atītānāgatapaccuppannānaṃ kammasamādānānaṃ ṭhānaso hetuso vipākaṃ
SABBA = "cách thực hành dẫn đến mọi nơi"         # sabbatthagāminiṃ paṭipadaṃ
LOKA = "thế gian có nhiều yếu tố, có các yếu tố khác nhau"   # anekadhātuṃ nānādhātuṃ lokaṃ
ADHI = "chí hướng khác nhau của chúng sinh"      # sattānaṃ nānādhimuttikataṃ
JHANA = ("sự vẩn đục, sự trong sạch, sự xuất khỏi của các tầng thiền, các sự giải thoát, các định tâm và các "
         "thành tựu thiền")                     # jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ
PUBBE = "sự nhớ lại các đời sống trước"          # pubbenivāsānussati
CUTU = "sự chết và sự tái sinh của chúng sinh"   # sattānaṃ cutūpapāta
ASAVA = "sự diệt tận các ô nhiễm"                # āsavānaṃ khaya
INDR = "mức độ cao thấp của các năng lực"        # indriyaparopariyatta


def K(x):
    """<x> yathābhūtaṃ ñāṇaṃ tathāgatabalaṃ (apposition, no copula: no doubled «là»)"""
    return f"hiểu biết đúng như thật về {x}, {TB}"


Q0 = Q(f"{TB} {SADH}")                           # Tathāgatabalaṃ sāvakasādhāraṇanti?
PY = ("sự rèn luyện trước đây, sự thực hành trước đây, việc giảng giải Giáo Pháp, việc thuyết giảng Giáo Pháp")
# pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā (dhammadesanā «việc thuyết giảng Giáo Pháp» pi-4)
EPI = ("bậc chiến thắng, bậc đạo sư, bậc Tự Giác Ngộ Hoàn Toàn, bậc toàn tri, bậc thấy tất cả, bậc làm chủ "
       "Giáo Pháp, chỗ nương tựa của Giáo Pháp")
# jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo (satthā, sammāsambuddha pi-4)
MG = ("người làm sinh khởi con đường chưa sinh khởi, người làm sinh thành con đường chưa sinh thành, người tuyên "
      "thuyết con đường chưa được tuyên thuyết, người biết con đường, người hiểu con đường, người thông thạo con "
      "đường")
# anuppannassa maggassa uppādetā asañjātassa maggassa sañjanetā anakkhātassa maggassa akkhātā maggaññū maggavidū
# maggakovido (asañjāta «chưa sinh thành» ch7 / pi-1)
DIFF = ("giữa Như Lai hay đệ tử, về sự diệt tận các ô nhiễm so với sự diệt tận các ô nhiễm, hay về sự giải "
        "thoát so với sự giải thoát")
# tathāgatassa vā sāvakassa vā āsavakkhayena vā āsavakkhayaṃ vimuttiyā vā vimutti(ṃ)
NOTE_27 = f"[ở đây, sự phủ nhận này là nhắm vào phương diện chung ({B.TIKA_NOTE})]"
# [ayamettha sādhāraṇapakkhaṃ sandhāya paṭikkhepo (ṭīkā oloketabbā)]


def sadh(x, neg=False):
    return f"{K(x)}, {ASADH if neg else SADH}"


def pair(a, b, end_=NHP):
    return f"{Q(a)} {AM} {Q(b)} {end_}"


# ================================================================ 2. Ariyantikathā
ARIYA = "là cao quý"                             # ariyaṃ / ariyā (ariya «cao quý» ch4)
SU = "lấy sự trống rỗng làm đối tượng"           # suññatārammaṇa (suññata «trống rỗng» pi-1)
AN = "lấy cái không có dấu hiệu làm đối tượng"   # animittārammaṇa (animitta «không có dấu hiệu» pi-1)
AP = "lấy cái không mong cầu làm đối tượng"      # appaṇihitārammaṇa (appaṇihita «không mong cầu» pi-1)
SUN, APN = "sự trống rỗng", "cái không mong cầu" # suññataṃ / appaṇihitaṃ (manasi karoti)
TWO = "có sự tụ hợp của hai sự tiếp xúc, hai tâm"  # dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ hoti (ch4)
MPN = ("con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng, con đường trở lại một lần, thành "
       "quả trở lại một lần, con đường không trở lại, thành quả không trở lại, con đường A-la-hán, thành quả "
       "A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, năng lực, sức mạnh, chi phần "
       "giác ngộ")
# maggo phalaṃ nibbānaṃ, sotāpattimaggo … arahattaphalaṃ, satipaṭṭhānaṃ … bojjhaṅgo (pi-2, ch2 DEV6 singular)
MPN_PE = "con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng… chi phần giác ngộ"
SPS = "các sự thiết lập tỉnh thức"               # satipaṭṭhānā (ch2 DEV6, pi-3)
REST5 = "các nỗ lực đúng đắn, các nền tảng thần thông, các năng lực, các sức mạnh, các chi phần giác ngộ"
BOJ = "các chi phần giác ngộ"                    # bojjhaṅgā


def ar(x, tail=""):
    """<x> … tathāgatabalaṃ ariyaṃ [<tail>ārammaṇaṃ]"""
    return f"{K(x)}, {ARIYA}" + (f", {tail}" if tail else "")


def man(x, y):
    """<x>ñca manasi karoti, <y>ñca manasi karoti"""
    return f"vừa chú tâm đến {x}, vừa chú tâm đến {y}"


def nv(subj, content):
    """<subj> ariyaṃ / ariyā na vattabbaṃ – <content>"""
    return f"đối với {subj} cao quý, không nên nói – {content}"


def qt(x):
    return f"“{x}”"


ARIYA_NV = qt("cao quý")                         # na vattabbaṃ – "ariya"nti
CHAIN3 = f"{SU}… {AN}… {AP}"                     # suññatārammaṇaṃ…pe… animittārammaṇaṃ…pe… appaṇihitārammaṇaṃ
CHAIN2 = f"{AN}… {AP}"                           # animittārammaṇaṃ…pe… appaṇihitārammaṇaṃ

# ================================================================ 3. Vimuttikathā
VIM = "được giải thoát"                          # vimuccati (pi-4 «tâm được giải thoát khỏi …»)
RAGA, DOSA, MOHA = "sự tham đắm", "sự sân hận", "sự si mê"   # rāga / dosa / moha (pi-1, ch2)
SA = {"raga": "có tham đắm", "dosa": "có sân hận", "moha": "có si mê"}   # sarāga / sadosa / samoha (pi-2)
SA5 = ["có sự tiếp xúc", "có cảm giác", "có tri giác", "có chủ ý", "có trí tuệ"]   # saphassa … sapañña
OBJ = ["là đối tượng của ô nhiễm", "là đối tượng của xiềng xích", "là đối tượng của nút thắt",
       "là đối tượng của dòng lũ", "là đối tượng của ách", "là đối tượng của chướng ngại",
       "bị sự hiểu sai lệch nắm giữ", "là đối tượng của sự bám víu", "là đối tượng của phiền não"]
# sāsava saṃyojaniya ganthaniya oghaniya yoganiya nīvaraṇiya parāmaṭṭha upādāniya saṃkilesiya (pi-1 matrix, ch4)
OBJ_FULL = ", ".join(OBJ)
OBJ_PE = f"{OBJ[0]}… {OBJ[-1]}"                  # sāsavaṃ…pe… saṃkilesiyaṃ
LOKIYA = "bất thiện, thuộc thế gian"             # akusalaṃ lokiyaṃ (pi-1)


def assoc(k):
    """<k>sahagataṃ <k>sahajātaṃ <k>saṃsaṭṭhaṃ <k>sampayuttaṃ <k>sahabhu <k>ānuparivatti
    (pi-2 ^2-567 «đi kèm, cùng sinh, hòa lẫn, gắn liền với»; pi-1 «cùng tồn tại với», «vận hành theo»)"""
    return (f"đi kèm với {k}, cùng sinh với {k}, hòa lẫn với {k}, gắn liền với {k}, cùng tồn tại với {k}, "
            f"vận hành theo {k}")


def both(k):
    """<k> ca cittañca ubho vimuccanti"""
    return f"cả {k} và tâm, cả hai đều {VIM}"


def cit(*adj):
    return f"tâm {', '.join(adj)} {VIM}"


# ================================================================ 4. Vimuccamānakathā
VV = "cái đã được giải thoát là cái đang được giải thoát"     # vimuttaṃ vimuccamānaṃ
ED = "một phần đã được giải thoát, một phần chưa được giải thoát"   # ekadesaṃ vimuttaṃ, ekadesaṃ avimuttaṃ


def part_a(name):
    """ekadesaṃ X, ekadesaṃ na X  (= build_3_vi.py part_a)"""
    return f"một phần là {name}, một phần không phải là {name}"


def part_b(phala):
    """ekadesaṃ <phala>ppatto … ekadesaṃ na kāyena phusitvā viharati  (= build_3_vi.py part_b)"""
    return (f"một phần đã đạt đến {phala}, đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an "
            f"trú, chạm đến bằng thân rồi an trú, một phần không chạm đến bằng thân rồi an trú")


SOTA, SAKA, ANAG, ARAHA = "bậc vào dòng", "bậc trở lại một lần", "bậc không trở lại", "bậc A-la-hán"   # pi-4
SILA_A = "có các giới hạnh được các bậc thánh yêu quý"
SOTA_X = ("một phần là người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, người có một hạt "
          "giống, có niềm tin trong sáng không lay chuyển nơi Đức Phật, nơi Giáo Pháp… nơi Tăng đoàn… "
          f"{SILA_A}, một phần không {SILA_A}")               # (= build_3_vi.py SOTA_X)
UDDHAM = "người theo dòng đi lên đến cõi Sắc Cứu Cánh"
ANA_X = ("một phần là người nhập Niết-bàn trọn vẹn trong khoảng giữa, người nhập Niết-bàn trọn vẹn khi gần mạng "
         "chung, người nhập Niết-bàn trọn vẹn không có sự thúc đẩy, người nhập Niết-bàn trọn vẹn có sự thúc đẩy, "
         f"{UDDHAM}, một phần không phải là {UDDHAM}")         # (= build_3_vi.py ANA_X)
ARA_HEAD = "một phần đã lìa tham đắm, đã lìa sân hận, đã lìa si mê"   # ekadesaṃ vītarāgo vītadoso vītamoho (ch3)
ARA_END = ("một phần điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm, một phần điều cần được tự "
           "mình chứng nghiệm chưa được tự mình chứng nghiệm")   # (= build_3_vi.py ARA_END)
SUTTA_VIM = ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc, tâm được giải thoát "
             "khỏi ô nhiễm hiện hữu, tâm được giải thoát khỏi ô nhiễm vô minh")   # pi-4 ^4 (pañcaka) wording
SUTTA_SO = ("Khi tâm đã an định như vậy, trong sạch, trong sáng, không còn vết nhơ, đã lìa những thứ làm vẩn đục, "
            "đã trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm đến sự hiểu biết về "
            "sự diệt tận các ô nhiễm")                          # pi-4 ^4 (catukka) wording
RATTA = ("là đã tham đắm và không tham đắm, đã sân hận và không sân hận, đã si mê và không si mê, đã bị cắt và "
         "không bị cắt, đã bị phá vỡ và không bị phá vỡ, đã được làm và không được làm")
# rattañceva arattañca, duṭṭhañceva aduṭṭhañca, mūḷhañceva amūḷhañca, chinnañceva achinnañca, bhinnañceva
# abhinnañca, katañceva akatañca
CIT_VM = "có tâm đang được giải thoát"           # atthi cittaṃ vimuccamānaṃ

# ================================================================ 5. Aṭṭhamakakathā
A8 = "người thứ tám"                             # aṭṭhamako puggalo
FOR8 = f"đối với {A8}"                           # aṭṭhamakassa puggalassa (+ pahīna / appahīna)
GOTRA = "đối với người chuyển dòng dõi"          # gotrabhuno puggalassa (dòng dõi pi-4)
DP = "sự ám ảnh của quan điểm"                   # diṭṭhipariyuṭṭhāna (pi-2 ^2-U70)
VP = "sự ám ảnh của hoài nghi"                   # vicikicchāpariyuṭṭhāna (pi-2)
DA = "khuynh hướng tiềm ẩn quan điểm"            # diṭṭhānusaya (pi-2 ^2-949)
VA = "khuynh hướng tiềm ẩn hoài nghi"            # vicikicchānusaya (pi-2)
SB = "sự hiểu sai lệch về giới hạnh và nghi thức"   # sīlabbataparāmāsa (pi-1, ch3)
PAH, APAH = "đã được dứt bỏ", "chưa được dứt bỏ"    # pahīna / appahīna (ch2, ch3)
SOTA_REACH = ("đã đạt đến thành quả vào dòng, đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an "
              "trú, chạm đến bằng thân rồi an trú")
# sotāpattiphalappatto paṭiladdho adhigato sacchikato upasampajja viharati, kāyena phusitvā viharati (ch3)
AMAGGA = f"đã được dứt bỏ bằng cái không phải con đường, thuộc thế gian, {OBJ_PE}"
# amaggena pahīnaṃ lokiyena sāsavena…pe… saṃkilesiyena
WILL = "sẽ sinh khởi"                            # uppajjissati (pi-1)
WONT = "sẽ không sinh khởi"                      # nuppajjissati


def f8(x, st, who=FOR8):
    return f"{who}, {x} {st}"


def kt(x, who=FOR8):
    """Aṭṭhamakassa puggalassa X nuppajjissatīti katvā pahīna(ṃ/o)nti? (ch7 «vì cho rằng»)"""
    return f"Có phải {who}, vì cho rằng {x} {WONT}, nó {PAH} không?"


def dev(x, rest, neg=False):
    """Aṭṭhamakassa puggalassa X-pahānāya <rest> bhāvito / abhāvito (ch2 «để dứt bỏ …, … đã tu tập …»)"""
    return f"để dứt bỏ {x}, {A8} {'chưa tu tập' if neg else 'đã tu tập'} {rest}"


# ================================================================ 6. Aṭṭhamakassa indriyakathā
I5 = ["năng lực niềm tin", "năng lực tinh tấn", "năng lực tỉnh thức", "năng lực định tâm", "năng lực trí tuệ"]
F5 = ["niềm tin", "sự tinh tấn", "sự tỉnh thức", "định tâm", "trí tuệ"]   # saddhā vīriyaṃ sati samādhi paññā
MANO = ("ý", "năng lực ý")                       # mano / manindriya (pi-1)
SOMA = ("niềm vui", "năng lực niềm vui")         # somanassa / somanassindriya (pi-1)
JIVI = ("sự sống", "năng lực sống")              # jīvita / jīvitindriya (pi-1)
PAT = {  # …phalasacchikiriyāya paṭipanna puggala (pi-4; = build_3_vi.py PAT)
    "sota": "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng",
    "saka": "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần",
    "ana": "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại",
    "ara": "người đang thực hành để tự mình chứng nghiệm trạng thái A-la-hán",
}
FIVE = "năm năng lực"                            # pañcindriyāni (pi-1..3)
BAHIRO = "người ở bên ngoài, đứng về phía người phàm phu"   # bāhiro puthujjanapakkhe ṭhito (puthujjana pi-1)
MUDU = "với mức yếu hơn thế"                     # tato mudutarehi
SUTTA_5 = (f"Này các tỳ-khưu, có {FIVE} này! Năm năng lực nào? {cap(', '.join(I5))} – này các tỳ-khưu, đây là "
           f"{FIVE}. Này các tỳ-khưu, do {FIVE} này được trọn vẹn, được viên mãn, nên là {ARAHA}. "
           f"{cap(MUDU)}, là {PAT['ara']}, {MUDU}, là {ANAG}, {MUDU}, là {PAT['ana']}, {MUDU}, là {SAKA}, "
           f"{MUDU}, là {PAT['saka']}, {MUDU}, là {SOTA}, {MUDU}, là {PAT['sota']}. Này các tỳ-khưu, người nào "
           f"không có {FIVE} này theo mọi cách, bằng mọi phương diện, Ta nói người ấy là ‘{BAHIRO}’")
# pañcimāni, bhikkhave, indriyāni! … sabbena sabbaṃ sabbathā sabbaṃ natthi, tamahaṃ ‘bāhiro …’ti vadāmi
# (sabbena sabbaṃ «theo mọi cách» ch5; vadāmi «Ta nói» ch4)


def has(who, *items):
    return f"{who} " + ", ".join(items)


# ================================================================ 7./8. Dibbacakkhu / Dibbasota
MC, DC, PC = "mắt thịt", "thiên nhãn", "mắt trí tuệ"   # maṃsacakkhu / dibbacakkhu / paññācakkhu
MS, DS = "tai thịt", "tai thuộc cõi trời"        # maṃsasota / dibbasota
DH = "được hiện tượng hỗ trợ"                    # dhammupatthaddha (dhamma = hiện tượng, core)
VAG = "phạm vi, uy lực, tầm hoạt động"           # visayo ānubhāvo gocaro
UPA = "là do nghiệp tạo ra rồi trở thành không do nghiệp tạo ra"     # upādiṇṇaṃ hutvā anupādiṇṇaṃ hoti (pi-1)
UPA_V = (f"là do nghiệp tạo ra [{SPELL} (Syā., Kaṃ.): upādinnaṃ] rồi trở thành không do nghiệp tạo ra")
KR = "là thuộc cõi dục lạc rồi trở thành thuộc cõi hình sắc"         # kāmāvacaraṃ hutvā rūpāvacaraṃ hoti (pi-1)
RA = "là thuộc cõi hình sắc rồi trở thành thuộc cõi không hình sắc"  # rūpāvacaraṃ hutvā arūpāvacaraṃ hoti
PA = "là nằm trong các cõi tồn tại rồi trở thành không nằm trong các cõi tồn tại"   # pariyāpannaṃ … (pi-1)
TWO_E = "chỉ có hai mắt"                         # dveva cakkhūni
ONE_S = "chỉ có một tai"                         # ekaṃyeva sotaṃ / ekaññeva sotaṃ
BS = "Đức Thế Tôn đã nói đến"                    # vuttāni bhagavatā
ANUTTARA = "không có điều gì cao hơn"            # anuttara (pi-1)


def becomes(a, b):
    """<a> dhammupatthaddhaṃ <b> hoti"""
    return f"{a} {DH} thì trở thành {b}"


def eye_block(m, d, d_of, upa):
    """the first eight questions of Dibbacakkhu- / Dibbasotakathā (identical frames)"""
    t = Q(becomes(m, d))
    return t, [
        pair(becomes(m, d), f"{m} là {d}, {d} là {m}"),
        pair(becomes(m, d), f"{m} như thế nào thì {d} như thế ấy, {d} như thế nào thì {m} như thế ấy"),
        pair(becomes(m, d), f"chính {m} ấy là {d} ấy, {d} ấy là {m} ấy"),
        pair(becomes(m, d), f"{VAG} của {m} như thế nào thì {VAG} của {d_of} như thế ấy"),
        pair(becomes(m, d), upa),
        pair(UPA, KR),
        pair(KR, RA),
        pair(RA, PA),
    ]


# ================================================================ 9. Yathākammūpagatañāṇakathā
YK = "việc đi theo nghiệp của mình"              # yathākammūpagata (pi-2 «đi theo nghiệp của mình»)
YKN = f"hiểu biết về {YK}"                       # yathākammūpagataṃ ñāṇaṃ
SEE = f"thấy hình sắc bằng {DC}"                 # dibbena cakkhunā rūpaṃ passati (hình sắc pi-1 sense split)
ITEMS = [  # the ime vata bhonto sattā passage, pi-2 ^2-830 / pi-4 wording, one item per "…"ti ca manasi karoti
    "Quả thật, những chúng sinh đáng kính này",
    "mang hành vi xấu bằng thân", "mang hành vi xấu bằng lời nói", "mang hành vi xấu bằng ý",
    "phỉ báng các bậc thánh", "có quan điểm sai lầm", "thực hiện nghiệp theo quan điểm sai lầm",
    "khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục",
    "hoặc những chúng sinh đáng kính này",
    "mang hành vi tốt bằng thân", "mang hành vi tốt bằng lời nói", "mang hành vi tốt bằng ý",
    "không phỉ báng các bậc thánh", "có quan điểm đúng đắn", "thực hiện nghiệp theo quan điểm đúng đắn",
    "khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi tốt lành, thế giới cõi trời",
]
SARI = "tôn giả Xá-lợi-phất"                     # āyasmā sāriputto (āyasmā «tôn giả» ch5; Xá-lợi-phất pi-4)
NO_DC = f"có ai đó không có {DC}, chưa có được, chưa chứng đắc, chưa tự mình chứng nghiệm {DC}, biết {YK}"
# atthi koci adibbacakkhuko dibbacakkhuṃ appaṭiladdho anadhigato asacchikato yathākammūpagataṃ jānāti

# ================================================================ 10. Saṃvarakathā
D, M = "giữa chư thiên", "giữa loài người"       # devesu / manussesu (ch3)
SAM, ASAM = "sự phòng hộ", "sự không phòng hộ"   # saṃvara / asaṃvara (terms file ch20)
SILA = "sự phòng hộ khỏi sự không phòng hộ là giới hạnh"   # asaṃvarā saṃvaro sīlaṃ (sīla «giới hạnh» pi-1)
YAMHA = "mà sự phòng hộ khỏi sự không phòng hộ ấy là giới hạnh"   # yamhā asaṃvarā saṃvaro sīlaṃ
PV, PA_ = "sự kiềm chế việc sát hại sinh mạng", "việc sát hại sinh mạng"   # pāṇātipātā veramaṇī / pāṇātipāto (pi-2)
SURA = "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # surāmerayamajjapamādaṭṭhāna (pi-2)
SV_ = f"sự kiềm chế {SURA}"                      # surāmerayamajjapamādaṭṭhānā veramaṇī (pi-2)
FIVE_COURSES = ("tất cả chư thiên đều sát hại sinh mạng, lấy của không được cho, có hành vi sai trái trong các dục "
                f"lạc, nói dối, dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả")
# sabbe devā pāṇātipātino adinnādāyino kāmesumicchācārino musāvādino surāmerayamajjapamādaṭṭhāyino (ch3, pi-2)

# ================================================================ 11./12. Asañña / Nevasaññānāsaññāyatana
AS = "giữa chúng sinh Vô Tưởng"                  # asaññasattesu (pi-2 «chư thiên Vô Tưởng», ch3)
ATT = f"{AS} có tri giác"                        # asaññasattesu saññā atthi
MA = f"{M} có tri giác"                          # manussesu saññā atthi
S6 = ["sự hiện hữu", "cõi tái sinh", "nơi cư trú của chúng sinh", "vòng luân hồi", "cách thức sinh ra",
      "sự có được sự tồn tại cá nhân"]
# bhavo gati sattāvāso saṃsāro yoni attabhāvapaṭilābho (gati sample; saṃsāra pi-1; attabhāva pi-1)
S6_S = ", ".join(f"{x} có tri giác" for x in S6)            # saññābhavo … saññattabhāvapaṭilābho
S6_A = ", ".join(f"{x} không có tri giác" for x in S6)      # asaññabhavo … asaññattabhāvapaṭilābho
S6_S_PE = f"{S6[0]} có tri giác, {S6[1]} có tri giác… {S6[5]} có tri giác"     # saññābhavo saññāgati…pe…
S6_A_PE = f"{S6[0]} không có tri giác, {S6[1]} không có tri giác… {S6[5]} không có tri giác"
E1, E4, E5 = "sự hiện hữu gồm một khối", "sự hiện hữu gồm bốn khối", "sự hiện hữu gồm năm khối"   # (pi-2)


def bare(head):
    """<head>bhavo gati sattāvāso saṃsāro yoni attabhāvapaṭilābho"""
    return ", ".join([head] + S6[1:])


def bare_pe(head):
    """<head>bhavo gati…pe… attabhāvapaṭilābho"""
    return f"{head}, {S6[1]}… {S6[5]}"


KARANIYA = "nhờ tri giác ấy mà làm được việc của tri giác"   # tāya saññāya saññākaraṇīyaṃ karoti (ch5 frame)
AKASA, VINN, AKIN = "lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả"   # (pi-1, pi-2)
CO_TG = qt("có tri giác")                        # "saññā atthi"
NV_NS = f"trong {NS}, không nên nói – {CO_TG}"   # nevasaññānāsaññāyatane na vattabbaṃ – "saññā atthī"ti
NV_NS_IN = f"trong {NS}, không nên nói – ‘có tri giác’"
OR = f"{CO_TG} hay {qt('không có')}"              # "saññā atthī"ti vā "natthī"ti vā
NV2 = f"trong {NS}, không nên nói – {OR}"
NV2_IN = f"trong {NS}, không nên nói – ‘có tri giác’ hay ‘không có’"
AS_NV = f"{AS}, không nên nói – {CO_TG}"         # asaññasattesu na vattabbaṃ – "saññā atthi"
NS_E4 = f"{NS} là {E4}"                          # nevasaññānāsaññāyatanaṃ catuvokārabhavo

# ================================================================ vagga close
TASSUDDANAM = "Tóm tắt của chương này –"         # Tassuddānaṃ – (ch9, byte for byte)
UDD = [
    "Sức mạnh chung, cao quý, tâm có tham đắm được giải thoát;",
    # Balaṃ sādhāraṇaṃ ariyaṃ, sarāgaṃ cittaṃ vimuccati;
    f"{cap(VV)}, {CIT_VM}.",
    # Vimuttaṃ vimuccamānaṃ, atthi cittaṃ vimuccamānaṃ.
    f"{cap(FOR8)}, {DP} {PAH};",
    # Aṭṭhamakassa puggalassa, diṭṭhipariyuṭṭhānaṃ pahīnaṃ;
    f"{cap(FOR8)}, không có {FIVE}, mắt.",
    # Aṭṭhamakassa puggalassa, natthi pañcindriyāni cakkhuṃ.
    f"Tai {DH}, {YKN};",
    # Sotaṃ dhammupatthaddhaṃ, yathākammūpagataṃ ñāṇaṃ;
    f"{cap(SAM)} {D}, tri giác {AS}, cũng vậy, đỉnh cao của sự hiện hữu.",
    # Devesu saṃvaro asañña-sattesu saññā evameva bhavagganti. (bhavagga «đỉnh cao của sự hiện hữu» pi-2)
]


# ================================================================ chapter builder
def build():
    d = B.Doc()
    d.head(3, VAGGA, "5-11-0")
    # ------------------------------------------------------------ (21) Balakathā
    d.head(4, heading(1), "5-11-1-0")
    d.seg("5-354",
          pair(f"{TB} {SADH}", f"{TB} là {SVB}, {SVB} là {TB}"),
          f"{Q0} {AM} {Q(f'chính {TB} ấy là {SVB} ấy, chính {SVB} ấy là {TB} ấy')} {NHP}",
          f"{Q0} {AM} {Q(f'{TB} như thế nào thì {SVB} như thế ấy, {SVB} như thế nào thì {TB} như thế ấy')} {NHP}",
          f"{Q0} {AM} {Q(f'{PY} của Như Lai như thế nào thì {PY} của {SV} như thế ấy')} {NHP}",
          f"{Q0} {AM} {Q(f'Như Lai là {EPI}')} {AM} {Q(f'{SV} là {EPI}')} {NHP}",
          f"{Q0} {AM} {Q(f'Như Lai là {MG}')} {AM} {Q(f'{SV} là {MG}')} {NHP}",
          pair(sadh(INDR), f"{SV} là bậc toàn tri, bậc thấy tất cả"))
    know = [TT, KAMMA, SABBA, LOKA, ADHI, JHANA, PUBBE, CUTU]
    lines = [f"{Q(f'{SV} biết {x}')} {AM} {B.hanci(f'{SV} biết {x}', sadh(x))}" for x in know]
    lines.append(f"{NANU(f'các ô nhiễm của Như Lai cũng đã bị diệt tận, các ô nhiễm của {SV} cũng đã bị diệt tận')} "
                 f"{AM} {Q(f'có sự khác biệt nào {DIFF}')} {NATTHI_ANS} "
                 f"{B.hanci(f'không có sự khác biệt nào {DIFF}', sadh(ASAVA))}")
    d.seg("5-355", *lines)
    d.seg("5-356",
          pair(sadh(ASAVA), sadh(TT)),
          pair(sadh(ASAVA), sadh(CUTU)),
          pair(sadh(TT, True), sadh(ASAVA, True)),
          pair(sadh(CUTU, True), sadh(ASAVA, True)),
          f"{Q(sadh(INDR, True))} {AM} {Q(sadh(TT, True))} Không nên nói như vậy {NOTE_27} …",
          f"{Q(sadh(INDR, True))} {AMP} {Q(sadh(ASAVA, True))} {NHP}",
          pair(sadh(TT), sadh(INDR)),
          pair(sadh(ASAVA), sadh(INDR)),
          end(1))
    # ------------------------------------------------------------ (22) Ariyantikathā
    d.head(4, VAGGA, "5-11-2-0")
    d.head(5, heading(2), "5-11-2-1-0")
    d.seg("5-357",
          pair(ar(TT), f"là {MPN}"),
          f"{Q(ar(TT))} {AM} {Q(SU)} {NHP} {Q(SU)} {AM} {Q(man(TT, SUN))} {NHP}",
          f"{Q(man(TT, SUN))} {AM} {Q(TWO)} {NHP} {q(ar(TT))} {AM} Có phải {CHAIN2} không? {NHP} {q(AP)} {AM} "
          f"{Q(man(TT, APN))} {NHP}",
          pair(man(TT, APN), TWO))
    d.seg("5-358",
          pair(f"{SPS} {ARIYA}, {SU}", ar(TT, SU)),
          f"Có phải {SPS} {ARIYA}, {CHAIN2} không? {AM} {Q(ar(TT, AP))} {NHP}",
          pair(f"{REST5} {ARIYA}, {SU}", ar(TT, SU)),
          f"Có phải {BOJ} {ARIYA}, {CHAIN2} không? {AM} {Q(ar(TT, AP))} {NHP}")
    d.seg("5-359",
          pair(nv(K(TT), qt(SU)), nv(SPS, qt(SU))),
          f"Có phải {nv(K(TT), CHAIN2)} không? {AM} {Q(nv(SPS, qt(AP)))} {NHP}",
          f"Có phải {nv(K(TT), CHAIN3)} không? {AM} Có phải {nv(f'nỗ lực đúng đắn… {BOJ}', qt(AP))} không? {NHP}")
    d.seg("5-360",
          f"{Q(ar(CUTU))} {AM} Có phải là {MPN_PE} không? {NHP}",
          f"{Q(ar(CUTU))} {AM} {Q(SU)} {NHP} {q(SU)} {AM} {Q(man(CUTU, SUN))} {NHP}",
          pair(man(CUTU, SUN), TWO),
          f"{Q(ar(CUTU))} {AM} {Q(f'{AN}, {AP}')} {NHP} {q(AP)} {AM} {Q(man(CUTU, APN))} {NHP}",
          pair(man(CUTU, APN), TWO))
    d.seg("5-361",
          f"Có phải {SPS} {ARIYA}, {CHAIN3} không? {AM} {Q(ar(CUTU, AP))} {NHP}",
          f"Có phải nỗ lực đúng đắn… {BOJ} {ARIYA}, {CHAIN3} không? {AM} {Q(ar(CUTU, AP))} {NHP}",
          f"Có phải {nv(K(CUTU), CHAIN3)} không? {AM} {Q(nv(SPS, qt(AP)))} {NHP}")
    d.seg("5-362",
          f"Có phải {nv(K(CUTU), CHAIN3)} không? {AM} Có phải {nv(f'các nỗ lực đúng đắn… {BOJ}', qt(AP))} không? "
          f"{NHP}",
          pair(ar(ASAVA), ar(TT)),
          pair(ar(ASAVA), ar(CUTU)),
          pair(f"đối với {K(TT)}, không nên nói – {ARIYA_NV}", f"đối với {K(ASAVA)}, không nên nói – {ARIYA_NV}"),
          pair(f"đối với {K(CUTU)}, không nên nói – {ARIYA_NV}", f"đối với {K(ASAVA)}, không nên nói – {ARIYA_NV}"),
          pair(ar(ASAVA, SU), ar(TT, SU)),
          f"Có phải {ar(ASAVA, CHAIN2)} không? {AM} {Q(ar(TT, AP))} {NHP}",
          f"Có phải {ar(ASAVA, CHAIN3)} không? {AMP} {Q(ar(CUTU, AP))} {NHP}",
          pair(nv(K(TT), qt(SU)), nv(K(ASAVA), qt(SU))),
          f"Có phải {nv(K(TT), CHAIN2)} không? {AM} {Q(nv(K(ASAVA), qt(AP)))} {NHP}",
          f"Có phải {nv(K(CUTU), CHAIN3)} không? {AM} {Q(nv(K(ASAVA), qt(AP)))} {NHP}",
          end(2))
    # ------------------------------------------------------------ (23) Vimuttikathā
    d.head(4, VAGGA, "5-11-3-0")
    d.head(5, heading(3), "5-11-3-1-0")
    sph = SA5[0]
    rest4_pe = "… ".join(SA5[1:])                 # savedanaṃ…pe… sasaññaṃ…pe… sacetanaṃ…pe… sapaññaṃ
    pan = both("trí tuệ")
    for key, k, seg in (("raga", RAGA, "5-363"), ("dosa", DOSA, "5-364"), ("moha", MOHA, "5-365")):
        s = SA[key]
        objs = OBJ_FULL if key == "raga" else OBJ_PE
        mixed = "… ".join(f"{x}, {s}" for x in SA5[1:])   # savedanaṃ sarāgaṃ…pe… sapaññaṃ sarāgaṃ
        l1 = pair(cit(s), f"tâm {assoc(k)}, {LOKIYA}, {objs}, {VIM}")
        l2 = pair(f"{cit(sph)}, {both('sự tiếp xúc')}", f"{cit(s)}, {both(k)}")
        if key == "raga":
            l3 = (f"Có phải tâm {rest4_pe} [{VAR} (Sī., Ka.): sasaññaṃ] {VIM}, {pan} không? {AM} "
                  f"{Q(f'{cit(s)}, {both(k)}')} {NHP}")
        else:
            l3 = f"Có phải tâm {rest4_pe} {VIM}, {pan} không? {AM} {Q(f'{cit(s)}, {both(k)}')} {NHP}"
        tail4 = both(k) if key != "dosa" else f"{cit(s)}, {both(k)}"
        l4 = pair(f"{cit(sph, s)}, {both('sự tiếp xúc')}", tail4)
        l5 = f"Có phải tâm {mixed} {VIM}, {pan} không? {AM} {Q(both(k))} {NHP}"
        if key != "moha":
            d.seg(seg, l1, l2, l3, l4, l5)
        else:
            l6 = (f"{Q(cit(SA['raga'], SA['dosa'], SA['moha']))} {AM} "
                  f"{Q(cit('đã lìa tham đắm', 'đã lìa sân hận', 'đã lìa si mê', 'không có phiền não'))} {NHP} "
                  f"vậy thì không nên nói – {qt(cit(SA['raga'], SA['dosa'], SA['moha']))}.")
            d.seg(seg, l1, l2, l3, l4, l5, l6, end(3))
    # ------------------------------------------------------------ (24) Vimuccamānakathā
    d.head(4, VAGGA, "5-11-4-0")
    d.head(5, heading(4), "5-11-4-1-0")
    d.seg("5-366",
          pair(VV, ED),
          pair(ED, f"{part_a(SOTA)}, {part_b('thành quả vào dòng')}, {SOTA_X}"),
          pair(ED, f"{part_a(SAKA)}, {part_b('thành quả trở lại một lần')}"),
          pair(ED, f"{part_a(ANAG)}, {part_b('thành quả không trở lại')}, {ANA_X}"),
          pair(ED, f"{part_a(ARAHA)}, {part_b('trạng thái A-la-hán')}, {ARA_HEAD}… {ARA_END}"),
          pair(VV, "vào khoảnh khắc sinh khởi thì đã được giải thoát, vào khoảnh khắc tan rã thì đang được giải "
                   "thoát"))
    d.seg("5-367",
          f"{B.NA_VATTABBAM_Q(VV)} {AM} {NANU_VUTTAM} {qt(SUTTA_VIM)} [Trường Bộ Kinh 1.248 và các chỗ khác]! "
          f"{ATTHEVA} {AM} Vậy thì nên nói [{VAR} (Sī., Syā., Kaṃ.): tena hi; (Ka.): tena hi na vattabbaṃ] – {qt(VV)}.",
          f"{Q(VV)} {AM} {NANU_VUTTAM} {qt(SUTTA_SO)}! {ATTHEVA} {AM} {B.TENA_HI_NA(VV)}",
          f"{Q(CIT_VM)} {AM} {Q('có tâm đang tham đắm, đang sân hận, đang si mê, đang bị phiền não làm ô nhiễm')} "
          f"{NHP} chẳng phải {RATTA} sao? {AM} Nếu {RATTA}, {NO_CA_VATA} {qt(CIT_VM)}.",
          end(4))
    # ------------------------------------------------------------ (25) Aṭṭhamakakathā
    d.head(4, VAGGA, "5-11-5-0")
    d.head(5, heading(5), "5-11-5-1-0")
    d.seg("5-368",
          pair(f8(DP, PAH), f"{A8} là {SOTA}, {SOTA_REACH}"),
          f"{Q(f8(VP, PAH))} {AM} Có phải {A8} là {SOTA}, đã đạt đến thành quả vào dòng… chạm đến bằng thân rồi an "
          f"trú không? {NHP}",
          f"{Q(f8(DP, PAH))} {AM} {Q(f8(DA, PAH))} {NHP} {q(f8(DP, PAH))} {AM} Có phải {FOR8}, {VA}… {SB} {PAH} "
          f"không? {NHP}",
          f"{Q(f8(VP, PAH))} {AM} {Q(f8(VA, PAH))} {NHP} {q(f8(VP, PAH))} {AM} Có phải {FOR8}, {DA}… {SB} {PAH} "
          f"không? {NHP}",
          f"{Q(f8(DA, APAH))} {AM} {Q(f8(DP, APAH))} {NHP} {q(f8(DA, APAH))} {AM} {Q(f8(VP, APAH))} {NHP}",
          f"Có phải {FOR8}, {VA}… {SB} {APAH} không? {AM} {Q(f8(DP, APAH))} {NHP} {q(f8(SB, APAH))} {AM} "
          f"{Q(f8(VP, APAH))} {NHP}")
    d.seg("5-369",
          f"{Q(f8(DP, PAH))} {AM} {Q(dev(DP, 'con đường'))} {NHP} {q(f8(DP, PAH))} {AM} "
          f"Có phải {dev(DP, f'{SPS}… các nỗ lực đúng đắn… đã tu tập {BOJ}')} không? {NH}",
          f"{Q(f8(VP, PAH))} {AM} Có phải {dev(VP, f'con đường… đã tu tập {BOJ}')} không? {NHP}",
          f"{Q(dev(DP, 'con đường', True))} {AM} {Q(AMAGGA)} {NHP} {q(dev(DP, f'{SPS}… {BOJ}', True))} {AM} "
          f"{Q(AMAGGA)} {NHP}",
          f"Có phải {dev(VP, f'con đường… {SPS}… chưa tu tập {BOJ}', True)} không? {AM} {Q(AMAGGA)} {NHP}")
    d.seg("5-370",
          f"{B.NA_VATTABBAM_Q(f8(DP, PAH))} {AM} {Q(WILL)} {cap(WONT)}. {B.hanci(WONT, f8(DP, PAH))}",
          f"{B.NA_VATTABBAM_Q(f8(VP, PAH))} {AM} {Q(WILL)} {cap(WONT)}. {B.hanci(WONT, f8(VP, PAH))}",
          f"{kt(DP)} {AM} {kt(DA)} {NHP}",
          f"{kt(DP)} {AM} {kt(f'{VA}… {SB}')} {NHP}",
          f"{kt(VP)} {AM} {kt(f'{VA}… {SB}')} {NHP}",
          f"{kt(DP)} {AM} {kt(DP, GOTRA)} {NHP} {kt(VP)[0].lower()}{kt(VP)[1:]} {AM} {kt(VP, GOTRA)} {NHP}",
          end(5))
    # ------------------------------------------------------------ (26) Aṭṭhamakassa indriyakathā
    d.head(4, VAGGA, "5-11-6-0")
    d.head(5, heading(6), "5-11-6-1-0")
    no_i = [f"không có {x}" for x in I5]
    d.seg("5-371",
          f"{Q(f'{A8} {no_i[0]}')} {AM} {Q(f'{A8} không có {F5[0]}')} {NH} "
          f"Có phải {A8} {'… '.join(no_i[1:])} không? {AM} {Q(f'{A8} không có {F5[4]}')} {NHP}",
          f"{Q(f'{A8} có {F5[0]}')} {AM} {Q(f'{A8} có {I5[0]}')} {NHP} "
          f"có phải {A8} {'… '.join(f'có {x}' for x in F5[1:])} không? {AM} {Q(f'{A8} có {I5[4]}')} {NHP}",
          f"{pair(has(A8, f'có {MANO[0]}', f'có {MANO[1]}'), has(A8, f'có {F5[0]}', f'có {I5[0]}'))} "
          f"{q(has(A8, f'có {MANO[0]}', f'có {MANO[1]}'))} {AM} {Q(has(A8, f'có {F5[4]}', f'có {I5[4]}'))} {NHP}",
          f"{pair(has(A8, f'có {SOMA[0]}', f'có {SOMA[1]}', f'có {JIVI[0]}', f'có {JIVI[1]}'), has(A8, f'có {F5[0]}', f'có {I5[0]}'))} "
          f"{q(has(A8, f'có {JIVI[0]}', f'có {JIVI[1]}'))} {AM} Có phải {A8}… có {F5[4]}, có {I5[4]} không? {NHP}",
          pair(has(A8, f"có {F5[0]}", f"không có {I5[0]}"), has(A8, f"có {MANO[0]}", f"không có {MANO[1]}")),
          f"{Q(has(A8, f'có {F5[0]}', f'không có {I5[0]}'))} {AM} Có phải {A8} có {SOMA[0]}, không có {SOMA[1]}… "
          f"có {JIVI[0]}, không có {JIVI[1]} không? {NHP} {q(has(A8, f'có {F5[4]}', f'không có {I5[4]}'))} {AM} "
          f"{Q(has(A8, f'có {MANO[0]}', f'không có {MANO[1]}'))} {Q(f'có {SOMA[0]}, không có {SOMA[1]}')} "
          f"{Q(f'có {JIVI[0]}, không có {JIVI[1]}')} {NHP}",
          f"{Q(f'{A8} {no_i[0]}')} {AM} {Q(f'{A8} là người không có niềm tin')} {NHP} "
          f"{q(f'{A8} {no_i[1]}')} {AM} {Q(f'{A8} là người lười biếng, kém tinh tấn')} {NHP} "
          f"{q(f'{A8} {no_i[2]}')} {AM} {Q(f'{A8} là người mất tỉnh thức, không hiểu biết rõ ràng')} {NHP} "
          f"{q(f'{A8} {no_i[3]}')} {AM} {Q(f'{A8} là người không được định tâm, có tâm rối loạn')} {NHP} "
          f"{q(f'{A8} {no_i[4]}')} {AM} {Q(f'{A8} là người kém trí tuệ, câm điếc')} {NHP}",
          f"{Q(f'{A8} có {F5[0]}, và {F5[0]} ấy dẫn đến giải thoát')} {AM} "
          f"Nếu {A8} có {F5[0]}, và {F5[0]} ấy dẫn đến giải thoát, {NO_CA_VATA} {qt(f'{A8} {no_i[0]}')}. "
          f"Có phải {A8} {'; '.join(f'có {x}, và {x} ấy dẫn đến giải thoát' for x in F5[1:])} không? {AM} "
          f"Nếu {A8} có {F5[4]}, và {F5[4]} ấy dẫn đến giải thoát, {NO_CA_VATA} {qt(f'{A8} {no_i[4]}')}.")
    sk, an_, ara = PAT["saka"], PAT["ana"], PAT["ara"]
    d.seg("5-372",
          f"{pair(has(sk, f'có {F5[0]}', f'có {I5[0]}'), has(A8, f'có {F5[0]}', f'có {I5[0]}'))} "
          f"{q(has(sk, f'có {F5[4]}', f'có {I5[4]}'))} {AM} {Q(has(A8, f'có {F5[4]}', f'có {I5[4]}'))} {NHP}",
          f"Có phải {an_}… {ara} có {F5[0]}, có {I5[0]}… có {F5[4]}, có {I5[4]} không? {AM} "
          f"{Q(has(A8, f'có {F5[4]}', f'có {I5[4]}'))} {NHP}",
          f"{pair(has(A8, f'có {F5[0]}', f'không có {I5[0]}'), has(sk, f'có {F5[0]}', f'không có {I5[0]}'))} "
          f"{q(has(A8, f'có {F5[4]}', f'không có {I5[4]}'))} {AM} {Q(has(sk, f'có {F5[4]}', f'không có {I5[4]}'))} "
          f"{NHP}",
          f"Có phải {A8} có {F5[0]}, không có {I5[0]}… có {F5[4]}, không có {I5[4]} không? {AM} "
          f"Có phải {an_}… {ara} có {F5[4]}, không có {I5[4]} không? {NHP}",
          f"{Q(f'{A8} không có {FIVE}')} {AM} {NANU_VUTTAM} {qt(SUTTA_5)} [Tương Ưng Bộ Kinh 5.488]. {ATTHEVA} "
          f"{AM} {Q(f'{A8} là {BAHIRO}')} {NHP} vậy thì {A8} có {FIVE}.",
          end(6))
    # ------------------------------------------------------------ (27) Dibbacakkhukathā
    d.head(4, VAGGA, "5-11-7-0")
    d.head(5, heading(7), "5-11-7-1-0")
    t1, eyes = eye_block(MC, DC, DC, UPA_V)
    d.seg("5-373", *eyes)
    three = f"{BS} ba mắt – {MC}, {DC}, {PC}"
    d.seg("5-374",
          pair(becomes(MC, DC), becomes(DC, MC)),
          pair(becomes(MC, DC), becomes(DC, PC)),
          pair(becomes(MC, DC), becomes(DC, MC)),
          f"{t1} {AM} {Q(TWO_E)} {NHP} {q(TWO_E)} {AM} {NANU(three)} {AM} Nếu {three}, {NO_CA_VATA} {qt(TWO_E)}.",
          f"{Q(TWO_E)} {AM} {NANU_VUTTAM} “Này các tỳ-khưu, có ba mắt này! Ba mắt nào? {cap(MC)}, {DC}, {PC} – "
          f"này các tỳ-khưu, đây là ba mắt”.",
          f"“{cap(MC)}, {DC}, {PC} {ANUTTARA};",
          "Ba mắt này, bậc tối thượng trong loài người đã tuyên thuyết.",
          f"“Sự sinh khởi của {MC} là con đường của {DC};",
          f"Và khi hiểu biết đã sinh khởi, {PC} {ANUTTARA};",
          "Nhờ có được mắt ấy, được giải thoát khỏi mọi khổ đau” "
          "[Kinh Phật Thuyết Như Vậy 61, trong Kinh Phật Thuyết Như Vậy].",
          f"{ATTHEVA} {AM} {B.TENA_HI_NA(TWO_E)}",
          end(7))
    # ------------------------------------------------------------ (28) Dibbasotakathā
    d.head(4, VAGGA, "5-11-8-0")
    d.head(5, heading(8), "5-11-8-1-0")
    t2, ears = eye_block(MS, DS, DS, UPA)
    d.seg("5-375", *ears)
    d.seg("5-376",
          pair(becomes(MS, DS), becomes(DS, MS)),
          pair(becomes(MS, DS), ONE_S),
          f"{Q(ONE_S)} {AM} {NANU(f'{BS} hai tai – {qt(f'{MS}, {DS}')}')} {AM} "
          f"Nếu {BS} hai tai – {MS}, {DS}, {NO_CA_VATA} {qt(ONE_S)}.",
          end(8))
    # ------------------------------------------------------------ (29) Yathākammūpagatañāṇakathā
    d.head(4, VAGGA, "5-11-9-0")
    d.head(5, heading(9), "5-11-9-1-0")
    t3 = Q(f"{YKN} là {DC}")
    see_yk = f"vừa chú tâm đến {YK}, vừa {SEE}"
    d.seg("5-377",
          f"Có phải {YKN} [{SPELL} (Syā., Kaṃ.): yathākammūpagatañāṇaṃ] là {DC} không? {AM} {Q(see_yk)} {NHP}",
          pair(see_yk, TWO),
          f"{t3} {AM} Có phải {', '.join(f'vừa chú tâm đến {qt(x)}' for x in ITEMS)}, vừa {SEE} không? {NHP}",
          f"{Q(f'vừa chú tâm đến {qt(ITEMS[-1])}, vừa {SEE}')} {AM} {Q(TWO)} {NHP}")
    yk_dc = qt(f"{YKN} là {DC}")
    d.seg("5-378",
          f"{t3} {AM} {Q(NO_DC)} {AM} Nếu {NO_DC}, {NO_CA_VATA} {yk_dc}.",
          f"{t3} {AM} {Q(f'{SARI} biết đến {YKN}')} {AM} Nếu {SARI} biết đến {YKN}, {NO_CA_VATA} {yk_dc}.",
          f"{t3} {AM} {Q(f'{SARI} biết đến {YKN}')} {AM} {Q(f'{SARI} có {DC}')} {NHP}",
          f"{Q(f'{SARI} có {DC}')} {AM} Chẳng phải {SARI} đã nói thế này sao –",
          f"“Không vì các đời sống trước, cũng không vì {DC};",
          "Vì sự bao quát tâm, vì thần thông, vì sự thanh tịnh của yếu tố tai;",
          "Vì sự chết, vì sự tái sinh, tôi không có sự mong cầu” [Trưởng Lão Tăng Kệ 996, trong Trưởng Lão Tăng Kệ].",
          f"{ATTHEVA} {AM} {B.TENA_HI_NA(f'{YKN} là {DC}')}",
          end(9))
    # ------------------------------------------------------------ (30) Saṃvarakathā
    d.head(4, VAGGA, "5-11-10-0")
    d.head(5, heading(10), "5-11-10-1-0")
    p_ = f"{SILA}, {D} có {SAM}"                    # asaṃvarā saṃvaro sīlaṃ, atthi devesu saṃvaro
    q_ = f"{D} có {ASAM}, {YAMHA}"                  # atthi devesu asaṃvaro, yamhā asaṃvarā saṃvaro sīlaṃ
    d.seg("5-379",
          pair(f"{D} có {SAM}", f"{D} có {ASAM}"),
          pair(f"{D} không có {ASAM}", f"{D} không có {SAM}"),
          f"{NANU(p_)} {AM} {Q(q_)} {NHP}",
          B.line_b("n", p_, q_),
          # vattabbe kho ‘…,’ (no dash after kho in the Pāli: kept as written)
          f"{B.no_ce(q_, p_)} {B.YAM_TATTHA} – “nên nói ‘{p_}’, nhưng không nên nói – ‘{q_}’”.",
          pair(f"{M} có {SAM}, ở đó có {ASAM}", f"{D} có {SAM}, ở đó có {ASAM}"),
          pair(f"{D} có {SAM}, ở đó không có {ASAM}", f"{M} có {SAM}, ở đó không có {ASAM}"))
    lines = [pair(f"{D} có {PV}", f"{D} có {PA_}"), pair(f"{D} có {SV_}", f"{D} có {SURA}"),
             pair(f"{D} không có {PA_}", f"{D} không có {PV}"), pair(f"{D} không có {SURA}", f"{D} không có {SV_}")]
    for v, a in ((PV, PA_), (SV_, SURA)):
        lines.append(pair(f"{M} có {v}, ở đó có {a}", f"{D} có {v}, ở đó có {a}"))
    for v, a in ((PV, PA_), (SV_, SURA)):
        lines.append(pair(f"{D} có {v}, ở đó không có {a}", f"{M} có {v}, ở đó không có {a}"))
    lines.append(f"{Q(f'{D} không có {SAM}')} {AM} {Q(FIVE_COURSES)} {NHP} vậy thì {D} có {SAM}.")
    lines.append(end(10))
    d.seg("5-380", *lines)
    # ------------------------------------------------------------ (31) Asaññakathā
    d.head(4, VAGGA, "5-11-11-0")
    d.head(5, heading(11), "5-11-11-1-0")
    d.seg("5-381",
          pair(ATT, f"là {S6_S}"),
          f"{NANU(f'là {S6_A}')} {AM} Nếu là {S6_A}, {NO_CA_VATA} {qt(ATT)}.",
          pair(ATT, f"là {bare(E5)}"),
          f"{NANU(f'là {bare(E1)}')} {AM} Nếu là {bare(E1)}, {NO_CA_VATA} {qt(ATT)}.",
          pair(ATT, KARANIYA))
    mixed = f"{S6[0]} có tri giác, {S6[1]} có tri giác, " + ", ".join(S6[2:])
    # saññābhavo saññāgati sattāvāso saṃsāro yoni attabhāvapaṭilābho (as written)
    d.seg("5-382",
          pair(f"{MA}, và đó là {S6_S}", f"{ATT}, và đó là {mixed}"),
          pair(f"{MA}, và đó là {bare(E5)}", f"{ATT}, và đó là {bare(E5)}"),
          pair(f"{MA}, {KARANIYA}", f"{ATT}, {KARANIYA}"),
          f"{Q(f'{ATT}, và đó là {S6_A}')} {AM} Có phải {MA}, và đó là {S6[0]} không có tri giác, {S6[1]} không có "
          f"tri giác… {S6[5]} không có tri giác không? {NHP}",
          f"{Q(f'{ATT}, và đó là {bare(E1)}')} {AM} Có phải {MA}, và đó là {bare_pe(E1)} không? {NHP}",
          pair(f"{ATT}, nhưng không {KARANIYA}", f"{MA}, nhưng không {KARANIYA}"))
    CHET = "vào lúc chết, vào lúc tái sinh"        # cutikāle upapattikāle (upapatti «tái sinh», coordinator)
    DUY = "vào lúc duy trì"                         # ṭhitikāle (tiṭṭhati «duy trì», sample)
    d.seg("5-383",
          f"{B.NA_VATTABBAM_Q(ATT)} {AM} {NANU_VUTTAM} “Này các tỳ-khưu, có những vị trời gọi là chúng sinh Vô "
          f"Tưởng; và do sự sinh khởi của tri giác, những vị trời ấy chết đi khỏi thân ấy” [Trường Bộ Kinh 1.68]! "
          f"{ATTHEVA} {AM} {B.TENA_HI(ATT)}",
          f"{Q(ATT)} Có lúc [{VAR} (Syā.): kañci] có, có lúc không có. "
          f"{Q(f'có lúc là chúng sinh có tri giác, có lúc là chúng sinh Vô Tưởng, có lúc là {S6[0]} có tri giác, có lúc là {S6[0]} không có tri giác, có lúc là {E5}, có lúc là {E1}')} "
          f"{NHP}",
          f"{Q(f'{AS}, tri giác có lúc có, có lúc không có')} {AM} Vào lúc nào thì có, vào lúc nào thì không có? "
          f"{cap(CHET)} thì có, {DUY} thì không có. "
          f"{Q(f'{CHET} là chúng sinh có tri giác, {DUY} là chúng sinh Vô Tưởng; {CHET} là {S6[0]} có tri giác, {DUY} là {S6[0]} không có tri giác; {CHET} là {E5}, {DUY} là {E1}')} "
          f"{NHP}",
          end(11))
    # ------------------------------------------------------------ (32) Nevasaññānāsaññāyatanakathā
    d.head(4, VAGGA, "5-11-12-0")
    d.head(5, heading(12), "5-11-12-1-0")
    t4 = Q(NV_NS)
    d.seg("5-384",
          f"{t4} {AM} {Q(f'là {S6_A}')} {NHP}",
          f"{NANU(f'là {S6_S}')} {AM} Nếu là {S6_S_PE}, {NO_CA_VATA} “{NV_NS_IN}”.",
          f"{t4} {AM} Có phải là {bare_pe(E1)} không? {NHP}",
          f"{NANU(f'là {bare_pe(E4)}')} {AM} Nếu là {bare_pe(E4)}, {NO_CA_VATA} “{NV_NS_IN}”.")
    d.seg("5-385",
          pair(f"{AS_NV}, và đó là {S6_A}", f"{NV_NS}, và đó là {S6_A}"),
          f"Có phải {AS_NV}, và đó là {bare_pe(E1)} không? {AM} {Q(f'{NV_NS}, và đó là {bare(E1)}')} {NHP}",
          f"Có phải {NV_NS}, và đó là {S6_S_PE} không? {AM} Có phải {AS_NV}, và đó là {S6_S_PE} không? {NHP}",
          f"Có phải {NV_NS}, và đó là {bare_pe(E4)} không? {AM} Có phải {AS_NV}, và đó là {bare_pe(E4)} không? "
          f"{NHP}",
          f"{t4} {AM} {NANU(NS_E4)} {AM} Nếu {NS_E4}, {NO_CA_VATA} “{NV_NS_IN}”.")
    aka_e4 = f"{AKASA} là {E4}"
    vin_akin_e4 = f"{VINN}… {AKIN} là {E4}"
    d.seg("5-386",
          # ^5-386 l.1 has no comma after catuvokārabhavo (l.2 has one): rendered as meant, same as l.2
          pair(f"{NS_E4}, {NV_NS}", f"{aka_e4}, trong {AKASA}, không nên nói – {CO_TG}"),
          f"{Q(f'{NS_E4}, {NV_NS}')} {AM} Có phải {vin_akin_e4}, trong {AKIN}, không nên nói – {CO_TG} không? {NHP}",
          pair(f"{aka_e4}, ở đó có tri giác", f"{NS_E4}, ở đó có tri giác"),
          f"Có phải {vin_akin_e4}, ở đó có tri giác không? {AM} {Q(f'{NS_E4}, ở đó có tri giác')} {NHP}",
          f"{Q(NV2)} {AM} {NANU(NS_E4)} {AM} Nếu {NS_E4}, {NO_CA_VATA} “{NV2_IN}”.",
          f"{Q(f'{NS_E4}, {NV2}')} {AM} Có phải {AKASA}… {VINN}… {AKIN} là {E4}, trong {AKIN}, không nên nói – "
          f"{OR} không? {NHP}",
          pair(f"{aka_e4}, ở đó có tri giác", f"{NS_E4}, ở đó có tri giác"),
          f"Có phải {vin_akin_e4}, ở đó có tri giác không? {AM} {Q(f'{NS_E4}, ở đó có tri giác')} {NHP}",
          f"Có phải trong {NS}, không nên nói [{VAR} (?): nevasaññānāsaññāyatane vattabbaṃ] – {OR} không? {AM} "
          f"{NANU(f'là {NS}')} {AM} Nếu là {NS}, {TENA_VATA} “{NV2_IN}”.",
          f"Có phải vì cho rằng là {NS}, {NV2} không? {AM} Có phải vì cho rằng là cảm giác không khó chịu cũng không "
          f"dễ chịu, đối với cảm giác không khó chịu cũng không dễ chịu [{VAR} (Sī., Ka.): adukkhamasukhā vedanā] "
          f"không nên nói – {qt('cảm giác')} hay {qt('không phải cảm giác')} không? {NHP}",
          end(12),
          f"{VAGGA}.",
          TASSUDDANAM,
          *UDD)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    (TB, 2), ("điều có thể xảy ra", 2), ("điều không thể xảy ra", 2), (KAMMA, 2), (SABBA, 2), (LOKA, 2), (ADHI, 2),
    (JHANA, 2), (PUBBE, 2), (CUTU, 2), (ASAVA, 2), (INDR, 2), ("hiểu biết đúng như thật", 2), ("mười sức mạnh", 2),
    ("sự toàn tri", 4), ("bậc đạo sư", 4), ("bậc Tự Giác Ngộ Hoàn Toàn", 4), ("việc thuyết giảng Giáo Pháp", 4),
    ("con đường A-la-hán", 2), ("thành quả A-la-hán", 2), ("con đường vào dòng", 2), ("thành quả vào dòng", 2),
    ("con đường trở lại một lần", 2), ("con đường không trở lại", 2), ("thành quả không trở lại", 2),
    ("có tính chất trống rỗng", 1), ("có tính chất không có dấu hiệu", 1), ("có tính chất không mong cầu", 1),
    ("chú tâm đến", 2), ("sự tiếp xúc", 1), ("tâm có tham đắm", 2), ("tâm đã lìa tham đắm", 2), ("có sân hận", 2),
    ("có si mê", 2), ("đã lìa sân hận", 2), ("đã lìa si mê", 2), ("đi kèm, cùng sinh, hòa lẫn, gắn liền với", 2),
    ("cùng tồn tại với tâm", 1), ("vận hành theo tâm", 1), ("thuộc thế gian", 1), ("bất thiện", 1),
    (SUTTA_VIM, 4), (SUTTA_SO, 4), (DP, 2), (VP, 2), (DA, 2), (VA, 2), (SB, 1), (", ".join(I5[:2]), 1),
    ("năng lực tỉnh thức, năng lực định tâm, năng lực trí tuệ", 1), (MANO[1], 1), (SOMA[1], 1), (JIVI[1], 1),
    ("người không có niềm tin", 2), ("là người lười biếng", 2), ("là người kém trí tuệ", 2),
    ("mất tỉnh thức, không hiểu biết rõ ràng, không được định tâm, có tâm rối loạn", 4), ("người phàm phu", 1),
    ("dẫn đến giải thoát", 1), ("dòng dõi", 4), (DC, 2), ("bằng thiên nhãn", 2), ("do nghiệp tạo ra", 1),
    ("không do nghiệp tạo ra", 1), ("thuộc cõi dục lạc", 1), ("thuộc cõi hình sắc", 1),
    ("thuộc cõi không hình sắc", 1), ("nằm trong các cõi tồn tại", 1), ("không nằm trong các cõi tồn tại", 1),
    ("uy lực", 2), ("phạm vi", 1), (ANUTTARA, 1), ("đi theo nghiệp của mình", 2), ("Xá-lợi-phất", 4),
    ("bao quát tâm", 2), ("thần thông", 1), ("yếu tố tai", 1), ("sự mong cầu", 1),
    ("Trường Bộ Kinh", 4), (PAT["sota"], 4), (PAT["saka"], 4), (PAT["ana"], 4),
    ("giới hạnh", 1), ("sự phòng hộ", 4), (PV, 2), (SURA, 2), ("chư thiên Vô Tưởng", 2),
    ("sự hiện hữu có tri giác", 2), ("sự hiện hữu không có tri giác", 2), (E1, 2), (E4, 2), (E5, 2),
    ("sự tồn tại cá nhân", 1), (AKASA, 1), (VINN, 1), (AKIN, 1), (NS, 1),
    ("không khó chịu cũng không dễ chịu", 1), ("đỉnh cao của sự hiện hữu", 2), ("sự tụ hợp", 2),
    ("lấy của không được cho, có hành vi sai trái trong các dục lạc, nói dối", 4), ("sự sống", 1),
    ("đã sinh khởi", 1), ("ô nhiễm vô minh", 4),
] + [(x if x[:4] != "khi " else x[4:], 2) for x in ITEMS[1:8] + ITEMS[9:]] +[("những chúng sinh đáng kính này", 2)] + [(x, 1) for x in OBJ]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
CH3 = "3-brahmacariyakatha.md"
PI5 = [
    (f"{part_a(SOTA)}, {part_b('thành quả vào dòng')}, {SOTA_X}", CH3),
    (f"{part_a(SAKA)}, {part_b('thành quả trở lại một lần')}", CH3),
    (f"{part_a(ANAG)}, {part_b('thành quả không trở lại')}, {ANA_X}", CH3),
    (f"{part_a(ARAHA)}, {part_b('trạng thái A-la-hán')}, {ARA_HEAD}", CH3), (ARA_END, CH3), (SOTA_REACH, CH3),
    (PAT["ara"], CH3), ("đã bị diệt tận", "4-jahatikatha.md"), ("Tương Ưng Bộ Kinh", "1-puggalakatha.md"),
    ("cõi tái sinh", "1-puggalakatha.md"), ("vòng luân hồi", CH3),
    (f"{D} có", CH3), (M, CH3), ("chư thiên Vô Tưởng", CH3), ("chư thiên có tri giác", CH3), ("câm điếc", CH3),
    ("tất cả chư thiên đều sát hại sinh mạng, lấy của không được cho, có hành vi sai trái trong các dục lạc, nói "
     "dối", CH3),
    (f"thì này bạn, chắc chắn không nên nói – “", CH3), ("ở đó", CH3), ("Kinh Pháp Cú 239, trong Kinh Pháp Cú", CH3),
    (SPS, "2-parihanikatha.md"), ("các nỗ lực đúng đắn", "2-parihanikatha.md"), ("để dứt bỏ", "2-parihanikatha.md"),
    ("đã tu tập", "2-parihanikatha.md"), ("và các chỗ khác", "2-parihanikatha.md"),
    (TWO.replace("hai sự tiếp xúc, hai tâm", "ba sự tiếp xúc"), "4-jahatikatha.md"), ("đệ tử", "4-jahatikatha.md"),
    ("là đối tượng của ô nhiễm", "4-jahatikatha.md"), ("Ta nói", "4-jahatikatha.md"),
    ("tôn giả", "5-sabbamatthitikatha.md"), ("theo mọi cách", "5-sabbamatthitikatha.md"),
    ("là thứ chung cho", "5-sabbamatthitikatha.md"), ("làm được việc của hiểu biết", "5-sabbamatthitikatha.md"),
    ("có tham đắm", "5-sabbamatthitikatha.md"), ("chưa sinh thành", "7-ekaccam-atthitikatha.md"),
    ("Có phải vì cho rằng", "7-ekaccam-atthitikatha.md"), (TASSUDDANAM, "9-hevatthikatha.md"),
    ("Kinh Phật Thuyết Như Vậy", "1-puggalakatha.md"), ("Chẳng phải tôn giả A-nan đã nói", "1-puggalakatha.md"),
    ("yếu tố tai thuộc cõi trời", "1-puggalakatha.md"), ("Có phải có ai đó", "1-puggalakatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    missing += [(s, f) for s, f in PI5 if s not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch11 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
