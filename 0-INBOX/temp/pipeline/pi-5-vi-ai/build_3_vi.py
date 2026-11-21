# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 3: 3-brahmacariyakatha.md.

Imports the approved sample builder (build_sample_vi) for every debate frame. Every repeated phrase is a
module constant, so every repeat is byte-identical. At build time: the sample's cross-book asserts, this
chapter's own cross-book asserts (pi-1..4 rails), and the sample's per-line checks against the Pāli.

run:  python -I -X utf8 build_3_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

from build_sample_vi import (AMANTA, NA_HEVAM, NA_HEVAM_PE, ATTHEVA, NANU_VUTTAM, NO_CA_VATA, Q, q, NANU,  # noqa
                             NA_VATTABBAM_Q, TENA_HI, TENA_HI_NA, KATHA, KATHA_END, VAR, SPELL, cap, Doc)

NAME = "3-brahmacariyakatha.md"

# ================================================================ headings
BV = "đời sống tu hành trong sạch"                       # brahmacariya(vāsa) (pi-1)
H_KATHA = KATHA.format(x=BV)                              # Brahmacariyakathā
H_SUDDHA = f"Bàn thuần túy về {BV}"                       # Suddhabrahmacariyakathā (terms file)
H_SAMSANDANA = f"Bàn về {BV} qua đối chiếu"               # Saṃsandanabrahmacariyakathā (terms file)
ODHISO_X = "sự dứt bỏ từng phần"
H_ODHISO = KATHA.format(x=ODHISO_X)                       # Odhisokathā (terms file)

# ================================================================ beings and places
D = "giữa chư thiên"                     # devesu (devā = chư thiên, pi-2)
D_ALL = "giữa tất cả chư thiên"          # sabbadevesu
D_ASANNA = "giữa chư thiên Vô Tưởng"     # asaññasattesu devesu (pi-2 «chư thiên Vô Tưởng»)
D_SANNA = "giữa chư thiên có tri giác"   # saññasattesu devesu
M = "giữa loài người"                    # manussesu
M_ALL = "giữa tất cả loài người"         # sabbamanussesu
MAJJH = "ở các xứ miền Trung"            # majjhimesu janapadesu
GATI4 = "nơi mà các tỳ-khưu, tỳ-khưu-ni, nam cư sĩ, nữ cư sĩ không lui tới"
# yattha natthi gati bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ (pi-2 list)


def pacc(var=""):
    """paccantimesu janapadesu … milakkhesu aviññātāresu yattha natthi gati …"""
    return f"ở các xứ biên địa, giữa những người man di{var}, những người không thông hiểu, {GATI4}"


NATTHI = f"{D} không có {BV}"            # natthi devesu brahmacariyavāso
ATTHI = f"{D} có {BV}"                   # atthi devesu brahmacariyavāso
YATTHA = "có ở một số nơi, không có ở một số nơi"   # atthi yattha atthi, atthi yattha natthi
KATTHA = "Có ở nơi nào, không có ở nơi nào?"        # Kattha atthi, kattha natthīti?
ONLY = f"chỉ ở đó mới có {BV}, ở nơi khác không có {BV}"   # tattheva brahmacariyavāso, natthaññatra …
IDHA_BV = f"ở đây có {BV}"               # idha brahmacariyavāso
V_SANNA = f" [{VAR} (Ka.): asaññasattesu]"

# ================================================================ ^5-269 the devas
NEG = [
    f"tất cả chư thiên đều đần độn, câm điếc [{SPELL} (Syā.): eḷamūgā], không hiểu biết, giao tiếp bằng cử chỉ tay, "
    "không đủ khả năng hiểu ý nghĩa của lời nói hay và lời nói dở",
    "tất cả chư thiên đều không có lòng tin trong sáng nơi Đức Phật, không có lòng tin trong sáng nơi Giáo Pháp, "
    "không có lòng tin trong sáng nơi Tăng đoàn, không thân cận Đức Phật, Đức Thế Tôn, không đặt câu hỏi với Đức "
    "Phật, Đức Thế Tôn, không hài lòng khi Đức Phật, Đức Thế Tôn trả lời các câu hỏi",
    "tất cả chư thiên đều mang sự ngăn che do nghiệp, mang sự ngăn che do phiền não, mang sự ngăn che do quả của "
    "nghiệp, không có niềm tin, không có ý muốn, kém trí tuệ, không có khả năng bước vào sự cố định, tức sự đúng "
    "đắn trong các hiện tượng thiện",
    "tất cả chư thiên đều là kẻ giết mẹ, kẻ giết cha, kẻ giết bậc A-la-hán, kẻ làm chảy máu Như Lai, kẻ chia rẽ "
    "Tăng đoàn",
    "tất cả chư thiên đều sát hại sinh mạng, lấy của không được cho, có hành vi sai trái trong các dục lạc, nói "
    "dối, nói lời chia rẽ, nói lời thô ác, nói lời phù phiếm, có sự thèm muốn, có tâm ác ý, có quan điểm sai lầm",
]
POS = [
    "có những vị trời không đần độn, không câm điếc, có hiểu biết, không giao tiếp bằng cử chỉ tay, đủ khả năng "
    "hiểu ý nghĩa của lời nói hay và lời nói dở",
    "có những vị trời có lòng tin trong sáng nơi Đức Phật, có lòng tin trong sáng nơi Giáo Pháp, có lòng tin "
    "trong sáng nơi Tăng đoàn, thân cận Đức Phật, Đức Thế Tôn, đặt câu hỏi với Đức Phật, Đức Thế Tôn, hài lòng "
    "khi Đức Phật, Đức Thế Tôn trả lời các câu hỏi",
    "có những vị trời không mang sự ngăn che do nghiệp, không mang sự ngăn che do phiền não, không mang sự ngăn "
    "che do quả của nghiệp, có niềm tin, có ý muốn, có trí tuệ, có khả năng bước vào sự cố định, tức sự đúng đắn "
    "trong các hiện tượng thiện",
    "có những vị trời không phải là kẻ giết mẹ, không phải là kẻ giết cha, không phải là kẻ giết bậc A-la-hán, "
    "không phải là kẻ làm chảy máu Như Lai, không phải là kẻ chia rẽ Tăng đoàn",
    "có những vị trời không sát hại sinh mạng, không lấy của không được cho, không có hành vi sai trái trong các "
    "dục lạc, không nói dối, không nói lời chia rẽ, không nói lời thô ác, không nói lời phù phiếm, không có sự "
    "thèm muốn, có tâm không ác ý, có quan điểm đúng đắn",
]
POS2_HEAD = "có những vị trời có lòng tin trong sáng nơi Đức Phật"   # atthi devā buddhe pasannā…pe…
POS_LAST = "có quan điểm đúng đắn"                                   # … sammādiṭṭhikā


def nanca(p, qq):
    """Hañci P, no ca vata re vattabbe – "Q"ti."""
    return f"Nếu {p}, {NO_CA_VATA} “{qq}”."


# ================================================================ ^5-270 marks of the ordained
MARKS = [  # (abstract noun, who does it, who does not)
    ("sự xuất gia", "người nào xuất gia", "người nào không xuất gia"),
    ("sự cạo đầu", "người nào cạo đầu", "người nào không cạo đầu"),
    ("sự mặc y cà-sa", "người nào mặc y cà-sa", "người nào không mặc y cà-sa"),
    ("sự mang bình bát", "người nào mang bình bát", "người nào không mang bình bát"),
]
SSB = "các bậc Tự Giác Ngộ Hoàn Toàn"   # sammāsambuddhā (pi-1..4 «bậc Tự Giác Ngộ Hoàn Toàn»)
PCB = "các bậc Độc Giác"                # paccekasambuddhā (pi-4 «bậc Độc Giác»)
SVY = "cặp đệ tử chính"                 # sāvakayugaṃ
APPEAR, NOT_APPEAR = "xuất hiện", "không xuất hiện"   # uppajjati / nuppajjati


def where(x_yes, x_no):
    """Yattha X tattheva brahmacariyavāso, yattha non-X natthi tattha brahmacariyavāso"""
    return f"nơi nào {x_yes} thì chỉ ở đó mới có {BV}, nơi nào {x_no} thì ở đó không có {BV}"


def who(w_yes, w_no):
    """Yo X tasseva brahmacariyavāso, yo non-X natthi tassa brahmacariyavāso"""
    return f"{w_yes} thì chỉ người ấy mới có {BV}, {w_no} thì người ấy không có {BV}"


def cond(x):
    """Devesu X natthīti / nuppajjantīti, natthi devesu brahmacariyavāsoti?"""
    return Q(f"nếu {x}, thì {NATTHI}")


# ================================================================ ^5-272 / ^5-273 the non-returner
ANAG = ("đối với bậc không trở lại, năm xiềng xích thuộc phần thấp đã được dứt bỏ, năm xiềng xích thuộc phần cao "
        "chưa được dứt bỏ")
# anāgāmissa puggalassa pañcorambhāgiyāni saṃyojanāni pahīnāni, pañcuddhambhāgiyāni saṃyojanāni appahīnāni (pi-2)
CUTA = "khi người ấy chết từ đây và tái sinh ở đó"   # ito cutassa tattha upapannassa
PHALA = "thành quả sinh khởi"                         # phaluppatti
K5 = ["gánh nặng được gỡ bỏ",                          # bhāroharaṇaṃ
      "khổ đau được hiểu biết trọn vẹn",               # dukkhapariññātaṃ
      "phiền não được dứt bỏ",                         # kilesappahānaṃ
      "sự chấm dứt được tự mình chứng nghiệm",         # nirodhasacchikiriyā
      "điều không thể bị lay chuyển được thấu triệt"]  # akuppapaṭivedho (akuppa as ch4 / pi-4)
TATTHEVA = "Ngay ở đó."                                # Tattheva.
KENATTHENA = "theo nghĩa nào mà bạn nói"               # kenaṭṭhena vadesi
AN = "bậc không trở lại"                               # anāgāmī puggalo
SOTA = "bậc vào dòng"                                  # sotāpanno puggalo
SAKA = "bậc trở lại một lần"                           # sakadāgāmī puggalo
ARAHA = "bậc A-la-hán"                                 # arahā
IDHA_PARI = "người nhập Niết-bàn trọn vẹn ngay ở đây"  # idha parinibbāyipuggalo
HERE, THERE = "ở đây", "ở đó"                          # idha / tattha


def sac(w, a, b):
    """X puggalo <a> bhāvitena maggena <b> phalaṃ sacchikaroti"""
    return f"{w}, nhờ con đường đã tu tập {a}, tự mình chứng nghiệm thành quả {b}"


IV = "đối với người đạt đến đích sau khi rời bỏ cõi này"   # idha vihāya niṭṭhassa puggalassa (pi-4)
PAT = {  # …phalasacchikiriyāya paṭipanna puggala (pi-4); arahatta = trạng thái A-la-hán (style rule)
    "sota": "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng",
    "saka": "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần",
    "ana": "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại",
    "ara": "người đang thực hành để tự mình chứng nghiệm trạng thái A-la-hán",
}
MNA = "con đường được tu tập, nhưng các phiền não không được dứt bỏ"   # maggo ca bhāvīyati, na ca kilesā pahīyanti
APUB = "cùng một lúc, không trước không sau, con đường được tu tập và các phiền não được dứt bỏ"
# apubbaṃ acarimaṃ maggo ca bhāvīyati, kilesā ca pahīyanti («không trước không sau» pi-2; = ch4 apubbaṃ acarimaṃ)
AN_KK = f"{AN}, người đã làm xong việc cần làm, đã hoàn tất sự tu tập"   # anāgāmī … katakaraṇīyo bhāvitabhāvano
UPAP = "tái sinh ở đó"                                                  # tattha upapajjati
ANOHATA = "chưa gỡ bỏ gánh nặng"                                        # anohaṭabhāro
NOT4 = ("chưa hiểu biết trọn vẹn khổ đau, chưa dứt bỏ phiền não, chưa tự mình chứng nghiệm sự chấm dứt, chưa thấu "
        "triệt điều không thể bị lay chuyển")
# apariññātadukkho appahīnakileso asacchikatanirodho appaṭividdhākuppo
AKUPPA_P = "điều không thể bị lay chuyển"
PUNA_BHARA = "tu tập con đường lần nữa để gỡ bỏ gánh nặng"              # bhāroharaṇāya puna maggaṃ bhāveti
PUNA_AKUPPA = f"tu tập con đường lần nữa để thấu triệt {AKUPPA_P}"       # akuppapaṭivedhāya puna maggaṃ bhāveti
ARAHA_UP = f"{ARAHA} tái sinh"                                           # arahā upapajjati
PUNABBHAVA = f"{ARAHA} có sự hiện hữu mới"                               # atthi arahato punabbhavo
MIGA = "giống như con nai bị trúng mũi tên, dù chạy đi xa vẫn chết"      # yathā migo sallena viddho dūrampi …
SASALLA = "khi mũi tên vẫn còn cắm trên mình"                            # sasallova

# ================================================================ ^5-274 … ^5-278 odhiso
ODH = "người ta dứt bỏ các phiền não từng phần một"   # odhisodhiso kilese jahati
DS = {"dukkha": "bằng việc thấy khổ đau", "samudaya": "bằng việc thấy sự phát sinh",
      "nirodha": "bằng việc thấy sự chấm dứt", "magga": "bằng việc thấy con đường"}   # …dassanena
KIM = "người ấy dứt bỏ điều gì?"                      # kiṃ jahatīti?
JA = "Người ấy dứt bỏ"                                # jahati (answer)
TDK = "các phiền não cùng hiện diện với chúng"        # tadekaṭṭhe kilese (pi-1)
S3 = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"   # (pi-1)
KR_O, BY_O = "sự tham đắm dục lạc ở dạng thô", "ác ý ở dạng thô"                 # oḷārika kāmarāga / byāpāda
KR_A, BY_A = "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "ác ý ở dạng nhỏ nhiệm"     # aṇusahagata …
R2 = "sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc"                   # rūparāga arūparāga (pi-1)
R3 = "sự kiêu mạn, sự xao động, vô minh"                                          # māna uddhacca avijjā (pi-1)


def ask(stage, ds):
    """X…phalasacchikiriyāya paṭipanno puggalo <ds> kiṃ jahatīti?"""
    return f"{cap(PAT[stage])}, {ds}, dứt bỏ điều gì?"


def ask2(ds):
    """<ds> kiṃ jahatīti? (later rows)"""
    return f"{cap(ds)}, {KIM}"


def part_a(name):
    """ekadesaṃ X, ekadesaṃ na X"""
    return f"một phần là {name}, một phần không phải là {name}"


def part_b(phala, var=""):
    """ekadesaṃ <phala>ppatto paṭiladdho adhigato sacchikato upasampajja viharati, kāyena phusitvā viharati,
    ekadesaṃ na kāyena phusitvā viharati"""
    return (f"một phần đã đạt đến {phala}{var}, đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an "
            f"trú, chạm đến bằng thân rồi an trú, một phần không chạm đến bằng thân rồi an trú")


SILA = "có các giới hạnh được các bậc thánh yêu quý"           # ariyakantehi sīlehi samannāgato
NA_SILA = "không có các giới hạnh được các bậc thánh yêu quý"
SOTA_X = ("một phần là người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, người có một hạt "
          "giống, có niềm tin trong sáng không lay chuyển nơi Đức Phật, nơi Giáo Pháp… nơi Tăng đoàn… "
          f"{SILA}, một phần {NA_SILA}")
SOTA_END = f"một phần {SILA}, một phần {NA_SILA}"
UDDHAM = "người theo dòng đi lên đến cõi Sắc Cứu Cánh"         # uddhaṃsoto akaniṭṭhagāmī (pi-4)
ANA_X = ("một phần là người nhập Niết-bàn trọn vẹn trong khoảng giữa, người nhập Niết-bàn trọn vẹn khi gần mạng "
         "chung, người nhập Niết-bàn trọn vẹn không có sự thúc đẩy, người nhập Niết-bàn trọn vẹn có sự thúc đẩy, "
         f"{UDDHAM}, một phần không phải là {UDDHAM}")
ANA_END = f"một phần là {UDDHAM}, một phần không phải là {UDDHAM}"
SAC_DONE = "một phần điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm"   # ekadesaṃ sacchikātabbaṃ sacchikataṃ
SAC_NOT = "một phần điều cần được tự mình chứng nghiệm chưa được tự mình chứng nghiệm"  # … na sacchikataṃ
ARA_EPI = ("một phần đã lìa tham đắm, đã lìa sân hận, đã lìa si mê, đã làm xong việc cần làm, đã đặt gánh nặng xuống, "
           "đã đạt đến mục đích của chính mình, đã diệt tận hoàn toàn xiềng xích của sự hiện hữu, đã được giải thoát "
           "nhờ hiểu biết trọn vẹn một cách đúng đắn, đã nhấc bỏ thanh chắn, đã lấp hào, đã nhổ cột trụ, đã tháo then "
           "cửa, là bậc thánh, đã hạ ngọn cờ, đã buông bỏ gánh nặng, đã thoát khỏi trói buộc, đã chiến thắng trọn vẹn, "
           "khổ đau đã được người ấy hiểu biết trọn vẹn, sự phát sinh đã được dứt bỏ, sự chấm dứt đã được tự mình "
           "chứng nghiệm, con đường đã được tu tập, điều cần được hiểu biết trực tiếp đã được hiểu biết trực tiếp, "
           "điều cần được hiểu biết trọn vẹn đã được hiểu biết trọn vẹn, điều cần dứt bỏ đã được dứt bỏ, điều cần "
           "được tu tập đã được tu tập, điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm")
ARA_END = f"{SAC_DONE}, {SAC_NOT}"

# ================================================================ cross-book asserts (this chapter)
CROSS_BOOK_3 = [
    (BV, 1), ("có lòng tin trong sáng", 2), ("chư thiên Vô Tưởng", 2), ("chư thiên Ba Mươi Ba", 2),
    ("mang sự ngăn che do nghiệp, mang sự ngăn che do phiền não, mang sự ngăn che do quả của nghiệp, không có niềm "
     "tin, không có ý muốn, kém trí tuệ, không có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện tượng "
     "thiện", 2),
    ("không mang sự ngăn che do nghiệp, không mang sự ngăn che do phiền não, không mang sự ngăn che do quả của "
     "nghiệp, có niềm tin, có ý muốn, có trí tuệ, có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện "
     "tượng thiện", 2),
    ("sát hại sinh mạng, lấy của không được cho, có hành vi sai trái trong các dục lạc, nói dối", 4),
    ("nói lời chia rẽ", 4), ("nói lời thô ác", 4),
    ("nói lời phù phiếm, có sự thèm muốn, có tâm ác ý, có quan điểm sai lầm", 4),
    ("tâm không ác ý", 2), ("chia rẽ Tăng đoàn", 2), ("Như Lai", 2), ("y cà-sa", 2), ("bình bát", 2),
    ("tỳ-khưu, tỳ-khưu-ni, nam cư sĩ, nữ cư sĩ", 2), ("bậc Tự Giác Ngộ Hoàn Toàn", 4), ("bậc Độc Giác", 4),
    ("năm xiềng xích thuộc phần thấp", 2), ("năm xiềng xích thuộc phần cao", 2),
    ("người đạt đến đích sau khi rời bỏ cõi này", 4),
    (PAT["sota"], 4), (PAT["saka"], 4), (PAT["ana"], 4), ("không trước không sau", 2),
    ("người tái sinh tối đa bảy lần", 4), ("người đi từ gia đình này sang gia đình khác", 4),
    ("người có một hạt giống", 4), ("bằng thân rồi an trú", 4), ("không thể bị lay chuyển", 4),
    ("người nhập Niết-bàn trọn vẹn trong khoảng giữa", 4),
    ("người nhập Niết-bàn trọn vẹn khi gần mạng chung, người nhập Niết-bàn trọn vẹn không có sự thúc đẩy, người "
     "nhập Niết-bàn trọn vẹn có sự thúc đẩy, người theo dòng đi lên đến cõi Sắc Cứu Cánh", 4),
    ("quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức", 1),
    ("các phiền não cùng hiện diện với chúng", 1), (R2 + ", sự kiêu mạn, sự xao động", 1),
    ("sự tham đắm dục lạc và ác ý", 4), ("ở dạng thô", 1), ("chứng nhập và an trú", 1),
    ("cần được hiểu biết trực tiếp", 2), ("cần được hiểu biết trọn vẹn", 2), ("cần dứt bỏ", 2),
    ("cần được tu tập", 2), ("cần được tự mình chứng nghiệm", 2),
    ("đã lìa tham đắm", 2), ("đã lìa sân hận", 2), ("đã lìa si mê", 2), ("diệt tận hoàn toàn", 4),
    ("sự phát sinh của khổ đau", 2), ("sự hiện hữu mới", 2), ("cõi khổ", 2), ("sự thấy chân lý", 1),
    ("Tăng Chi Bộ Kinh", 4), ("đã hoàn tất", 1), ("mũi tên", 2), ("nhập Niết-bàn trọn vẹn", 4),
]


def check_cross_book_3():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))) for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK_3 if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"chapter-3 cross-book asserts: {len(CROSS_BOOK_3)} strings found in pi-1..4 rails")


# ================================================================ chapter builder
def build_ch3():
    d = Doc()
    d.head(3, H_KATHA, "5-3-0")
    d.head(4, H_SUDDHA, "5-3-1-0")
    # ---------------------------------------------------------------- ^5-269
    d.seg("5-269",
          f"{Q(NATTHI)} {AMANTA} {Q('; '.join(NEG))} {NA_HEVAM_PE}",
          f"{NANU('; '.join(POS))} {AMANTA}",
          nanca(f"{POS[0]}… {POS2_HEAD}… {POS_LAST}", NATTHI))
    # ---------------------------------------------------------------- ^5-270
    lines = [f"{Q(ATTHI)} {AMANTA} "
             f"{Q(f'ở đó có sự xuất gia, sự cạo đầu, sự mặc y cà-sa, sự mang bình bát, {D} {SSB} {APPEAR}, {PCB} {APPEAR}, {SVY} {APPEAR}')} "
             f"{NA_HEVAM_PE}"]
    for x, wy, wn in MARKS:
        y = where(f"có {x}", f"không có {x}")
        lines.append(f"{cond(f'{D} không có {x}')} {AMANTA} {Q(y)} {NA_HEVAM_PE} {q(y)} {AMANTA} "
                     f"{Q(who(wy, wn))} {NA_HEVAM_PE}")
    lasts = [
        f"Đức Thế Tôn đã sinh ra tại Lâm-tỳ-ni, đã giác ngộ hoàn toàn dưới gốc cây Bồ-đề, Đức Thế Tôn đã chuyển "
        f"bánh xe Giáo Pháp tại Ba-la-nại; {ONLY}",
        f"{PCB} {APPEAR} {MAJJH}, {ONLY}",
        f"{SVY} đã {APPEAR} ở xứ Ma-kiệt-đà, {ONLY}",
    ]
    for subj, last in zip((SSB, PCB, SVY), lasts):
        y = where(f"{subj} {APPEAR}", f"{subj} {NOT_APPEAR}")
        lines.append(f"{cond(f'{D} {subj} {NOT_APPEAR}')} {AMANTA} {Q(y)} {NA_HEVAM_PE} {q(y)} {AMANTA} "
                     f"{Q(last)} {NA_HEVAM_PE}")
    d.seg("5-270", *lines)
    # ---------------------------------------------------------------- ^5-271
    m_atthi = f"{M} có {BV}"
    d.seg("5-271",
          f"{Q(ATTHI)} {AMANTA} {Q(f'{D_ALL} có {BV}')} {NA_HEVAM_PE}",
          f"{Q(m_atthi)} {AMANTA} {Q(f'{M_ALL} có {BV}')} {NA_HEVAM_PE}",
          f"{Q(ATTHI)} {AMANTA} {Q(f'{D_ASANNA} có {BV}')} {NA_HEVAM_PE}",
          f"{Q(m_atthi)} {AMANTA} {Q(pacc(f' [{SPELL} (Syā., Ka.): milakkhūsu]') + f', có {BV}')} {NA_HEVAM}",
          f"{Q(ATTHI)} {cap(YATTHA)}. "
          f"{Q(f'{D_ASANNA}, {BV} {YATTHA}, {D_SANNA}{V_SANNA}, {BV} {YATTHA}')} {NA_HEVAM}",
          f"{Q(f'{D}, {BV} {YATTHA}')} {AMANTA} {KATTHA} {cap(D_ASANNA)} không có {BV}, {D_SANNA}{V_SANNA} có {BV}. "
          f"{Q(f'{D_ASANNA} không có {BV}')} {AMANTA} {Q(f'{D_SANNA}{V_SANNA} không có {BV}')} {NA_HEVAM}",
          f"{Q(f'{D_SANNA} có {BV}')} {AMANTA} {Q(f'{D_ASANNA} có {BV}')} {NA_HEVAM}",
          f"{Q(m_atthi)} {cap(YATTHA)}. "
          f"{Q(f'{pacc()}, {BV} {YATTHA}, {MAJJH}, {BV} {YATTHA}')} {NA_HEVAM}",
          f"{Q(f'{M}, {BV} {YATTHA}')} {AMANTA} {KATTHA} {cap(pacc())}, không có {BV}, {MAJJH} có {BV}. "
          f"{Q(f'{pacc()}, không có {BV}')} {AMANTA} {Q(f'{MAJJH} không có {BV}')} {NA_HEVAM}",
          f"{Q(f'{MAJJH} có {BV}')} {AMANTA} {Q(f'{pacc()}, có {BV}')} {NA_HEVAM}",
          f"{Q(ATTHI)} {AMANTA} {NANU_VUTTAM} “Này các tỳ-khưu, nhờ ba phương diện, loài người ở Diêm-phù-đề vượt "
          f"trội hơn loài người ở Bắc Câu-lô châu và chư thiên Ba Mươi Ba! Ba phương diện nào? Họ can đảm, có sự "
          f"tỉnh thức, {IDHA_BV}” [Tăng Chi Bộ Kinh 9.21]. {ATTHEVA} {AMANTA} {TENA_HI(NATTHI)}",
          f"Có phải tại Xá-vệ, Đức Thế Tôn đã nói – “{IDHA_BV}” không? {AMANTA} "
          f"{Q(f'chỉ tại Xá-vệ mới có {BV}, ở nơi khác không có {BV}')} {NA_HEVAM}")
    # ---------------------------------------------------------------- ^5-272
    kuhim = ", ".join(f"{x} ở đâu" for x in K5)
    tahim = ", ".join(f"{x} ở đó" for x in [PHALA] + K5)
    d.seg("5-272",
          f"{cap(ANAG)}; {CUTA}, {PHALA} ở đâu? {TATTHEVA} {nanca(f'{ANAG}, {CUTA}, {PHALA} ở đó', NATTHI)}",
          f"{cap(ANAG)}; {CUTA}, {kuhim}? {TATTHEVA} {nanca(f'{ANAG}, {CUTA}, {K5[-1]} ở đó', NATTHI)}",
          f"{cap(ANAG)}; {CUTA}, {tahim}; {KENATTHENA} – “{NATTHI}”? "
          f"Vì {sac(AN, HERE, THERE)} [{VAR} (nhiều bản): sacchikaroti].")
    # ---------------------------------------------------------------- ^5-273
    d.head(4, H_SAMSANDANA, "5-3-2-0")
    an_idha = sac(AN, HERE, THERE)
    saka_idha = f"{SAKA}, {IDHA_PARI}"
    d.seg("5-273",
          f"{Q(an_idha)} {AMANTA} {Q(sac(SOTA, THERE, HERE))} {NA_HEVAM}",
          f"{Q(an_idha)} {AMANTA} {Q(sac(f'{SAKA}, {IDHA_PARI} [{VAR} (?): idhaparinibbāyī]', THERE, HERE))} {NA_HEVAM}",
          f"{Q(sac(SOTA, HERE, HERE))} {AMANTA} {Q(sac(AN, THERE, THERE))} {NA_HEVAM}",
          f"{Q(sac(saka_idha, HERE, HERE))} {AMANTA} {Q(sac(AN, THERE, THERE))} {NA_HEVAM_PE}",
          f"{Q(f'{IV}, {MNA}')} {AMANTA} {Q(f'đối với {PAT_SOTA}, {MNA}')} {NA_HEVAM_PE}",
          f"{Q(f'{IV}, {MNA}')} {AMANTA} Có phải đối với {PAT['saka']}… đối với {PAT['ara']}, {MNA} không? "
          f"{NA_HEVAM_PE}",
          f"{Q(f'đối với {PAT_SOTA}, {APUB}')} {AMANTA} {Q(f'{IV}, {APUB}')} {NA_HEVAM}",
          f"Có phải đối với {PAT['saka']}… đối với {PAT['ara']}, {APUB} không? {AMANTA} {Q(f'{IV}, {APUB}')} "
          f"{NA_HEVAM}",
          f"{Q(f'{AN_KK}, {UPAP}')} {AMANTA} {Q(ARAHA_UP)} {NA_HEVAM}",
          f"{Q(ARAHA_UP)} {AMANTA} {Q(PUNABBHAVA)} {NA_HEVAM}",
          f"{Q(PUNABBHAVA)} {AMANTA} "
          f"{Q(f'{ARAHA} đi từ sự hiện hữu này đến sự hiện hữu khác, đi từ cõi tái sinh này đến cõi tái sinh khác, đi từ vòng luân hồi này đến vòng luân hồi khác, đi từ sự tái sinh này đến sự tái sinh khác')} "
          f"{NA_HEVAM}",
          f"{Q(f'{AN_KK}, {ANOHATA}, {UPAP}')} {AMANTA} {Q(f'người ấy {PUNA_BHARA}')} {NA_HEVAM}",
          f"{Q(f'{AN_KK}, {NOT4}, {UPAP}')} {AMANTA} {Q(f'người ấy {PUNA_AKUPPA}')} {NA_HEVAM}",
          f"{Q(f'{AN_KK}, {ANOHATA}, {UPAP}, nhưng không {PUNA_BHARA}')} {AMANTA} "
          f"{Q(f'người ấy {ANOHATA} mà nhập Niết-bàn trọn vẹn ở đó')} {NA_HEVAM}",
          f"{Q(f'{AN_KK}, {NOT4}, {UPAP}, nhưng không {PUNA_AKUPPA}')} {AMANTA} "
          f"{Q(f'người ấy chưa thấu triệt {AKUPPA_P} mà nhập Niết-bàn trọn vẹn ở đó')} {NA_HEVAM} "
          f"{cap(MIGA)}, cũng vậy, {an_idha}.",
          f"{Q(f'{MIGA} {SASALLA}, cũng vậy, {AN}, nhờ con đường đã tu tập {HERE}, nhập Niết-bàn trọn vẹn {THERE} {SASALLA}')} "
          f"{NA_HEVAM_PE}",
          KATHA_END.format(x=BV))
    # ---------------------------------------------------------------- ^5-274 … ^5-277
    d.head(4, H_ODHISO, "5-3-3-0")
    sp = lambda v: f" [{SPELL} (?): {v}]"  # noqa: E731
    # sotāpatti
    a, b = part_a(SOTA), part_b("thành quả vào dòng")
    d.seg("5-274",
          f"{Q(ODH)} {AMANTA} {ask('sota', DS['dukkha'])} {JA} một phần {S3}, và {TDK}. "
          f"Có phải người ấy {a}, {part_b('thành quả vào dòng', sp('sotāpattiphalaṃ patto'))}, {SOTA_X} không? "
          f"{NA_HEVAM_PE}",
          f"{ask2(DS['samudaya'])} {JA} quan điểm về tự ngã, dứt bỏ một phần sự hoài nghi, sự hiểu sai lệch về giới "
          f"hạnh và nghi thức, và {TDK}. Có phải người ấy {a}… {SOTA_END} không? {NA_HEVAM_PE}",
          f"{ask2(DS['nirodha'])} {JA} một phần sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức, và {TDK}. "
          f"Có phải người ấy {a}… {SOTA_END} không? {NA_HEVAM_PE}",
          f"{ask2(DS['magga'])} {JA} sự hiểu sai lệch về giới hạnh và nghi thức, và {TDK}. "
          f"Có phải người ấy {a}, {b}, {SOTA_X} không? {NA_HEVAM_PE}")
    # sakadāgāmi
    a, b = part_a(SAKA), part_b("thành quả trở lại một lần")
    d.seg("5-275",
          f"{ask('saka', DS['dukkha'])} {JA} {KR_O}, dứt bỏ một phần {BY_O}, và {TDK}. "
          f"Có phải người ấy {a}, {part_b('thành quả trở lại một lần', sp('sakadāgāmiphalaṃ patto'))} không? "
          f"{NA_HEVAM_PE}",
          f"{ask2(DS['samudaya'])} {JA} {KR_O}, dứt bỏ một phần {BY_O}, và {TDK}. Có phải người ấy {a}, {b} không? "
          f"{NA_HEVAM_PE}",
          f"{ask2(DS['nirodha'])} {JA} {BY_O}, và dứt bỏ một phần {TDK}. Có phải người ấy {a}, {b} không? "
          f"{NA_HEVAM_PE}",
          f"{ask2(DS['magga'])} {JA} {BY_O}, và dứt bỏ {TDK}. Có phải người ấy {a}, {b} không? {NA_HEVAM_PE}")
    # anāgāmi
    a, b = part_a(AN), part_b("thành quả không trở lại")
    d.seg("5-276",
          f"{ask('ana', DS['dukkha'])} {JA} {KR_A}, dứt bỏ một phần {BY_A}, và {TDK}. "
          f"Có phải người ấy {a}, {part_b('thành quả không trở lại', sp('anāgāmiphalaṃ patto'))}, {ANA_X} không? "
          f"{NA_HEVAM_PE}",
          f"{ask2(DS['samudaya'])} {JA} {KR_A}, dứt bỏ một phần {BY_A}, và {TDK}. "
          f"Có phải người ấy {a}… {ANA_END} không? {NA_HEVAM_PE}",
          f"{ask2(DS['nirodha'])} {JA} {BY_A}, và dứt bỏ một phần {TDK}. "
          f"Có phải người ấy {a}… {ANA_END} không? {NA_HEVAM_PE}",
          f"{ask2(DS['magga'])} {JA} {TDK}. Có phải người ấy {a}, {b}, {ANA_X} không? {NA_HEVAM_PE}")
    # arahatta
    a, b = part_a(ARAHA), part_b("trạng thái A-la-hán")
    d.seg("5-277",
          f"{ask('ara', DS['dukkha'])} {JA} một phần {R2}, {R3}, và {TDK}. "
          f"Có phải người ấy {a}, {part_b('trạng thái A-la-hán', sp('arahattaṃ patto'))}, {ARA_EPI}, "
          f"({SAC_DONE},) [( ) (?)] {SAC_NOT} không? {NA_HEVAM_PE}",
          f"{ask2(DS['samudaya'])} {JA} {R2}, dứt bỏ một phần {R3}, và {TDK}. "
          f"Có phải người ấy {a}… {ARA_END} không? {NA_HEVAM_PE}",
          f"{ask2(DS['nirodha'])} {JA} sự kiêu mạn, dứt bỏ một phần sự xao động, vô minh, và {TDK}. "
          f"Có phải người ấy {a}… {ARA_END} không? {NA_HEVAM_PE}",
          f"{ask2(DS['magga'])} {JA} sự xao động, vô minh, và {TDK}. "
          f"Có phải người ấy {a}, {b}, {ARA_EPI}, {ARA_END} không? {NA_HEVAM_PE}")
    # ---------------------------------------------------------------- ^5-278 sutta proofs
    conc = f"{ATTHEVA} {AMANTA} {TENA_HI_NA(ODH)}"
    d.seg("5-278",
          f"{NA_VATTABBAM_Q(ODH)} {AMANTA} {NANU_VUTTAM}",
          "“Người trí, dần dần theo thứ tự, từng chút một, trong từng khoảnh khắc;",
          "Như người thợ luyện bạc, hãy gột sạch cấu uế của chính mình” [Kinh Pháp Cú 239, trong Kinh Pháp Cú].",
          conc,
          f"{Q(ODH)} {AMANTA} {NANU_VUTTAM}",
          "“Ngay cùng với sự thành tựu thấy chân lý của người ấy,",
          "Ba hiện tượng được dứt bỏ;",
          "Quan điểm về tự ngã và sự hoài nghi,",
          "Cùng bất cứ giới hạnh và nghi thức nào còn có;",
          "Người ấy được giải thoát khỏi bốn cõi khổ,",
          f"Không thể [{SPELL} (Sī., Syā.): abhabbo] làm sáu trọng tội” [Tiểu Tụng 6.10; Kinh Tập 233].",
          conc,
          f"{Q(ODH)} {AMANTA} {NANU_VUTTAM} “Này các tỳ-khưu, vào lúc mà nơi vị đệ tử cao quý, con mắt Giáo Pháp "
          f"không bụi bặm, không cấu uế sinh khởi – ‘bất cứ điều gì có bản chất phát sinh, tất cả điều ấy đều có bản "
          f"chất chấm dứt’, này các tỳ-khưu, cùng với sự sinh khởi của sự thấy, nơi vị đệ tử cao quý, ba xiềng xích "
          f"được dứt bỏ – {S3}” [trong Tăng Chi Bộ Kinh]. {conc}",
          KATHA_END.format(x=ODHISO_X))
    return d.text()


PAT_SOTA = PAT["sota"]


def main():
    B.check_cross_book()
    check_cross_book_3()
    text = unicodedata.normalize("NFC", build_ch3())
    probs, repaired = B.check_lines((B.PALI_DIR / NAME).read_text(encoding="utf-8"), text, NAME)
    (B.OUT_DIR / NAME).write_bytes(text.encode("utf-8"))
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"Pāli lines with the odd closing order \"’ repaired to ’”: {len(repaired)}")
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
