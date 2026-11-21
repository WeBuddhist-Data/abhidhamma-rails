"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 3 (3-brahmacariyakatha.md, ^5-3-0 … ^5-278).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/3-brahmacariyakatha.md from fixed
strings, importing the approved sample builder (read-only) for the frames and checks. Every string marked
(pi-1) … (pi-4) is asserted to occur in that book's approved Vietnamese rails. New recurring strings:
notes-rails-3.md.

usage: python -I -X utf8 -B build_rails_3_vi.py            (build + checks)
       python -I -X utf8 -B build_rails_3_vi.py --lookup   (termbase entries for this chapter's keywords)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

TB = S.ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = S.ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
NAME = "3-brahmacariyakatha.md"

YES, YES_Q, NO, NO_PE, PE = S.YES, S.YES_Q, S.NO, S.NO_PE, S.PE
Q, q, cap = S.Q, S.q, S.cap
PN = S.PN

# ---------------------------------------------------------------------------------------------------------------
# Strings taken unchanged from the approved pi-1 … pi-4 Vietnamese rails (asserted at build time)
# ---------------------------------------------------------------------------------------------------------------
AVARANA_N = ("mang sự ngăn che do nghiệp, mang sự ngăn che do phiền não, mang sự ngăn che do quả của nghiệp, "
             "không có niềm tin, không có ý muốn, kém trí tuệ, không có khả năng bước vào sự cố định, tức sự đúng "
             "đắn trong các hiện tượng thiện")                                                   # (pi-2 ^2-826)
#   kammāvaraṇena samannāgatā … assaddhā acchandikā duppaññā abhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ
AVARANA_P = ("không mang sự ngăn che do nghiệp, không mang sự ngăn che do phiền não, không mang sự ngăn che do quả "
             "của nghiệp, có niềm tin, có ý muốn, có trí tuệ, có khả năng bước vào sự cố định, tức sự đúng đắn "
             "trong các hiện tượng thiện")                                                       # (pi-2 ^2-827)
KP1 = "sát hại sinh mạng, lấy của không được cho, có hành vi sai trái trong các dục lạc, nói dối, nói lời chia rẽ"
KP2 = "nói lời thô ác"
KP3 = "nói lời phù phiếm, có sự thèm muốn, có tâm ác ý, có quan điểm sai lầm"                   # (pi-4 ^4-136)
KAMMAPATHA_N = f"{KP1}, {KP2}, {KP3}"
#   pāṇātipātino adinnādāyino kāmesumicchācārino musāvādino pisuṇavācā pharusāvācā samphappalāpino abhijjhāluno
#   byāpannacittā micchādiṭṭhikā
ABYAPANNA = "có tâm không ác ý, có quan điểm đúng đắn"                                          # (pi-4 ^4-138)
KAMMAPATHA_P = ("không sát hại sinh mạng, không lấy của không được cho, không có hành vi sai trái trong các dục lạc, "
                "không nói dối, không nói lời chia rẽ, không nói lời thô ác, không nói lời phù phiếm, không có sự "
                f"thèm muốn, {ABYAPANNA}")
ORAM = "năm xiềng xích thuộc phần thấp"                                                           # (pi-2)
UDDHAM = "năm xiềng xích thuộc phần cao"                                                          # (pi-2)
ASANNA = "chư thiên Vô Tưởng"                                                                     # (pi-2)
TAVATIMSA = "chư thiên Ba Mươi Ba"                                                                # (pi-2)
ARIYASAVAKA = "vị đệ tử của bậc thánh"                                                            # (pi-2)
APUBBA = "không trước không sau"                                                                  # (pi-2)
BHIKKHU4 = "tỳ-khưu, tỳ-khưu-ni, nam cư sĩ, nữ cư sĩ"                                            # (pi-2)
KASAVA = "y cà-sa"                                                                                # (pi-2)
SAMMASAMBUDDHA = "bậc Tự Giác Ngộ Hoàn Toàn"                                                      # (pi-1)
PACCEKA = "bậc Độc Giác"                                                                          # (pi-4)
TAD = "và các phiền não cùng hiện diện với chúng"                                                 # (pi-1)
#   tadekaṭṭhe ca kilese
TINI = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"           # (pi-1)
SAKKAYA, VICI, SILAB = TINI.split(", ")
RUPARAGA = "sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động"   # (pi-4)
VIHAYA = "người đạt đến đích sau khi rời bỏ cõi này"                                              # (pi-4)
#   idha vihāya niṭṭho
P_SOTA = "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng"                        # (pi-4)
P_SAKA = "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần"                 # (pi-4)
P_ANAG = "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"                   # (pi-4)
P_ARA = "người đang thực hành để tự mình chứng nghiệm trạng thái A-la-hán"
#   arahattasacchikiriyāya paṭipanno (termbase: arahattasacchikiriyāya «tự mình chứng nghiệm trạng thái A-la-hán»)
SATTAKKHATTU = "người tái sinh tối đa bảy lần"                                                    # (pi-4)
KOLANKOLO = "người đi từ gia đình này sang gia đình khác"                                         # (pi-4)
EKABIJI = "người có một hạt giống"                                                                # (pi-4)
ANTARA = "người nhập Niết-bàn trọn vẹn trong khoảng giữa"                                         # (pi-4)
UPAHACCA = "người nhập Niết-bàn trọn vẹn khi gần mạng chung"                                      # (pi-4)
ASANKHARA = "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy"                                   # (pi-4)
SASANKHARA = "người nhập Niết-bàn trọn vẹn có sự thúc đẩy"                                        # (pi-4)
UDDHAMSOTO = "người theo dòng đi lên đến cõi Sắc Cứu Cánh"                                        # (pi-4)
ODARIKA = "ở dạng thô"                                                                            # (pi-1)
UPASAMPAJJA = "chứng nhập và an trú"                                                              # (pi-1)

REUSED = [(AVARANA_N, "2"), (AVARANA_P, "2"), (KP1, "4"), (KP2, "4"), (KP3, "4"), (ABYAPANNA, "4"),
          (ORAM, "2"), (UDDHAM, "2"), (ASANNA, "2"), (TAVATIMSA, "2"), (ARIYASAVAKA, "2"), (APUBBA, "2"),
          (BHIKKHU4, "2"), (KASAVA, "2"), (SAMMASAMBUDDHA, "1"), (PACCEKA, "4"), (TAD, "1"), (TINI, "1"),
          (RUPARAGA, "4"), (VIHAYA, "4"), (P_SOTA, "4"), (P_SAKA, "4"), (P_ANAG, "4"), (SATTAKKHATTU, "4"),
          (KOLANKOLO, "4"), (EKABIJI, "4"), (ANTARA, "4"), (UPAHACCA, "4"), (ASANKHARA, "4"), (SASANKHARA, "4"),
          (UDDHAMSOTO, "4"), (ODARIKA, "1"), (UPASAMPAJJA, "1")]

# ---------------------------------------------------------------------------------------------------------------
# New strings of this chapter (listed in notes-rails-3.md)
# ---------------------------------------------------------------------------------------------------------------
BRAHMA = "đời sống tu hành trong sạch"                  # brahmacariya (kathā name)
BV = f"việc sống {BRAHMA}"                              # brahmacariyavāso
DEVESU = "giữa chư thiên"                               # devesu
MANUSSESU = "giữa loài người"                           # manussesu
BV_DEV = f"{DEVESU} có {BV}"                            # atthi devesu brahmacariyavāso
BV_NO = f"{DEVESU} không có {BV}"                       # natthi devesu brahmacariyavāso
BV_MAN = f"{MANUSSESU} có {BV}"                         # atthi manussesu brahmacariyavāso
SANNASATTA = "chư thiên có tri giác"                    # saññasattā devā
YN = "có nơi có, có nơi không có"                       # atthi yattha atthi, atthi yattha natthi
YN_ANS = "Có nơi có, có nơi không có."                  # Atthi yattha atthi, atthi yattha natthīti.
KATTHA = "Ở đâu có, ở đâu không có?"                   # Kattha atthi, kattha natthīti?
PACC = "ở các xứ biên địa"                              # paccantimesu janapadesu
MAJJH = "ở các xứ trung tâm"                            # majjhimesu janapadesu
MIL = f"giữa những người man di không thông hiểu, nơi không có sự lui tới của {BHIKKHU4}"
#   milakkhesu aviññātāresu yattha natthi gati bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ
ELSE = f"ở nơi khác không có {BV}"                      # natthaññatra / natthi aññatra brahmacariyavāso
CHINH = "chính ở đó"                                    # tattheva
BP = "Đức Phật, Đức Thế Tôn"                            # buddhaṃ bhagavantaṃ / buddhena bhagavatā
ODHI = "dứt bỏ các phiền não từng phần một"             # odhisodhiso kilese jahati
SAVAKAYUGA = "cặp đệ tử chính"                          # sāvakayugaṃ
ARAHA = PN["arahā"]
ANAG = PN["anāgāmī"]                                    # anāgāmī puggalo
SOTA = PN["sotāpanno"]                                  # sotāpanno puggalo
SAKA = PN["sakadāgāmī"]                                 # sakadāgāmī puggalo


def sac(person, a, b):              # X puggalo idha / tattha bhāvitena maggena tattha / idha phalaṃ sacchikaroti
    return f"{person}, nhờ con đường đã tu tập ở {a}, tự mình chứng nghiệm thành quả ở {b}"


def neu_dev(x):                     # Devesu X natthīti, natthi devesu brahmacariyavāsoti?
    return S.neu(f"{DEVESU} {x}", BV_NO)


def yattha(pos, neg):               # Yattha X tattheva brahmacariyavāso, yattha na-X natthi tattha brahmacariyavāso
    return f"nơi nào {pos}, thì {CHINH} có {BV}, nơi nào {neg}, thì ở đó không có {BV}"


def yo(pos, neg):                   # Yo X tasseva brahmacariyavāso, yo na-X natthi tassa brahmacariyavāso
    return f"ai {pos}, thì chính người ấy có {BV}, ai {neg}, thì người ấy không có {BV}"


def four(neg_cause, pos, neg, yo_pos, yo_neg, yes_q=False):
    """The 4-question line on pabbajjā / muṇḍiyaṃ / kāsāvadhāraṇā / pattadhāraṇā."""
    y = yattha(pos, neg)
    return (f"{neu_dev(neg_cause)} {YES} {Q(y)} {NO_PE} {q(y)} {YES_Q if yes_q else YES} {Q(yo(yo_pos, yo_neg))} "
            f"{NO_PE}")


def arise(neg_cause, pos, neg, last):
    y = yattha(pos, neg)
    return f"{neu_dev(neg_cause)} {YES} {Q(y)} {NO_PE} {q(y)} {YES} {Q(last)} {NO_PE}"


# Anāgāmī in the deva world (^5-272)
AN_HEAD = (f"đối với {ANAG}, {ORAM} đã được dứt bỏ, {UDDHAM} chưa được dứt bỏ, khi chết ở đây và tái sinh ở đó")
#   Anāgāmissa puggalassa pañcorambhāgiyāni saṃyojanāni pahīnāni, pañcuddhambhāgiyāni saṃyojanāni appahīnāni,
#   ito cutassa tattha upapannassa
FR = ["thành quả sinh khởi",                            # phaluppatti
      "gánh nặng được gỡ bỏ",                           # bhāroharaṇaṃ
      "khổ đau đã được hiểu biết trọn vẹn",             # dukkhapariññātaṃ
      "có sự dứt bỏ phiền não",                         # kilesappahānaṃ
      "sự chấm dứt được tự mình chứng nghiệm",          # nirodhasacchikiriyā
      "có sự thấu triệt điều không thể bị lay chuyển"]  # akuppapaṭivedho

# Saṃsandana (^5-273)
MAGGO_NA = "con đường được tu tập, nhưng phiền não không được dứt bỏ"   # maggo ca bhāvīyati, na ca kilesā pahīyanti
MAGGO_CA = f"{APUBBA}, con đường được tu tập và phiền não được dứt bỏ"  # apubbaṃ acarimaṃ maggo ca … kilesā ca …
AN_KK = f"{ANAG}, đã làm xong việc cần làm, đã hoàn tất sự tu tập"     # anāgāmī puggalo katakaraṇīyo bhāvitabhāvano
ANOHATA = "chưa gỡ bỏ gánh nặng"                                         # anohaṭabhāro
APARI = ("chưa hiểu biết trọn vẹn khổ đau, chưa dứt bỏ phiền não, chưa tự mình chứng nghiệm sự chấm dứt, "
         "chưa thấu triệt điều không thể bị lay chuyển")
#   apariññātadukkho appahīnakileso asacchikatanirodho appaṭividdhākuppo
AKUPPA_V = "thấu triệt điều không thể bị lay chuyển"                     # akuppapaṭivedhāya
MIGO = "con nai bị trúng mũi tên, dù đã chạy đi xa"                     # migo sallena viddho dūrampi gantvā
SASALLA = "khi vẫn còn mang mũi tên"                                     # sasallova

# Odhiso (^5-274 … ^5-278)
DASS = {"dukkha": "khổ đau", "samudaya": "sự phát sinh", "nirodha": "sự chấm dứt", "magga": "con đường"}
TAD_PART = "và dứt bỏ một phần các phiền não cùng hiện diện với chúng"   # tadekaṭṭhe ca kilese ekadese jahati
TAD_ALL = "và dứt bỏ các phiền não cùng hiện diện với chúng"             # tadekaṭṭhe ca kilese jahati (after a clause)
ATTAINED = ("đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an trú, chạm đến bằng thân rồi "
            "an trú, một phần không chạm đến bằng thân rồi an trú")
#   paṭiladdho adhigato sacchikato upasampajja viharati, kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā viharati
AK_G = "giới hạnh được các bậc thánh yêu quý"                         # ariyakantehi sīlehi
ARIYAKANTA = f"được trang bị {AK_G}"                                     # ariyakantehi sīlehi samannāgato
ARIYAKANTA_YES = f"một phần có {AK_G}"                                   # ekadesaṃ … samannāgato (termbase phrase)
ARIYAKANTA_NO = f"một phần không có {AK_G}"                              # ekadesaṃ … na samannāgato (termbase phrase)
SOTA_TAIL = (f"một phần là {SATTAKKHATTU}, {KOLANKOLO}, {EKABIJI}, được trang bị niềm tin trong sáng không lay "
             f"chuyển nơi Đức Phật, nơi Giáo Pháp{PE} nơi Tăng đoàn{PE} {ARIYAKANTA}, {ARIYAKANTA_NO}")
ANAG_TAIL = (f"một phần là {ANTARA}, {UPAHACCA}, {ASANKHARA}, {SASANKHARA}, {UDDHAMSOTO}, "
             f"một phần không phải là {UDDHAMSOTO}")
ARA_EPI = ("đã lìa tham đắm, đã lìa sân hận, đã lìa si mê, đã làm xong việc cần làm, đã đặt gánh nặng xuống, "
           "đã đạt đến mục đích của mình, đã hoàn toàn diệt tận xiềng xích hiện hữu, được giải thoát nhờ hiểu biết "
           "trọn vẹn đúng đắn, đã nhấc bỏ thanh chắn, đã lấp hào, đã nhổ cột trụ, không còn then cửa, là bậc thánh, "
           "đã hạ ngọn cờ, đã hạ gánh nặng, đã thoát khỏi trói buộc, đã chiến thắng trọn vẹn")          # (ch2 ^5-261)
#   vītarāgo vītadoso vītamoho katakaraṇīyo ohitabhāro anuppattasadattho parikkhīṇabhavasaṃyojano sammadaññāvimutto
#   ukkhittapaligho saṅkiṇṇaparikho abbūḷhesiko niraggaḷo ariyo pannaddhajo pannabhāro visaññutto suvijitavijayo
ARA_DONE = ("khổ đau đã được vị ấy hiểu biết trọn vẹn, sự phát sinh đã được dứt bỏ, sự chấm dứt đã được tự mình "
            "chứng nghiệm, con đường đã được tu tập, điều cần được hiểu biết trực tiếp đã được hiểu biết trực "
            "tiếp, điều cần được hiểu biết trọn vẹn đã được hiểu biết trọn vẹn, điều cần dứt bỏ đã được dứt bỏ, "
            "điều cần được tu tập đã được tu tập, điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm")
#   dukkhaṃ tassa pariññātaṃ … sacchikātabbaṃ sacchikataṃ                                         (ch2 ^5-261)
CH2 = [ARA_EPI, ARA_DONE]          # asserted to occur in the finished chapter 2 (earlier chapter wins on a clash)
SC_YES = "một phần điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm"   # ekadesaṃ sacchikātabbaṃ sacchikataṃ
SC_NO = "một phần điều cần được tự mình chứng nghiệm chưa được tự mình chứng nghiệm"  # … na sacchikataṃ


def kim(how, person=None):          # (X paṭipanno puggalo) Y-dassanena kiṃ jahatīti?
    if person:
        return f"{cap(person)}, bằng việc thấy {DASS[how]}, dứt bỏ cái gì?"
    return f"Bằng việc thấy {DASS[how]}, dứt bỏ cái gì?"


def head_status(x, fruit, v=""):    # Ekadesaṃ X, ekadesaṃ na X, ekadesaṃ X-phalappatto … na kāyena phusitvā viharati
    return f"một phần là {x}, một phần không phải là {x}, một phần đã đạt đến {fruit}{v}, {ATTAINED}"


def short(x, last):                 # Ekadesaṃ X, ekadesaṃ na X…pe… <last>
    return f"một phần là {x}, một phần không phải là {x}{PE} {last}"


def status_q(body):
    return f"Có phải {body} không? {NO_PE}"


# Suttas (^5-271, ^5-278)
JAMBU = ("“Này các tỳ-khưu, loài người ở Diêm-phù-đề vượt trội hơn loài người ở Bắc Câu-lô châu và "
         f"{TAVATIMSA} ở ba phương diện! Ba phương diện nào? Can đảm, có sự tỉnh thức, ở đây có {BV}”")
DHP = ["“Người trí dần dần, từng chút một, từng khoảnh khắc một;",
       f"Như người thợ luyện đối với bạc, nên gột sạch cấu uế của chính mình” "
       f"[{S.CIT['dha. pa.']} 239, trong {S.CIT['dha. pa.']}]."]
RATANA = ["“Ngay khi vị ấy thành tựu sự thấy chân lý,",
          "Ba hiện tượng được dứt bỏ;",
          "Quan điểm về tự ngã và sự hoài nghi,",
          "Hoặc bất cứ giới hạnh và nghi thức nào có;",
          "Và được giải thoát khỏi bốn cõi khổ,",
          f"Không có khả năng{S.var_sp('Sī., Syā.', 'abhabbo')} làm sáu trọng tội” "
          f"[Tiểu Tụng 6.10; {S.CIT['su. ni.']} 233]."]
DHAMMACAKKHU = (f"“Này các tỳ-khưu, vào lúc nào nơi {ARIYASAVAKA}, con mắt Giáo Pháp không bụi bặm, không cấu uế "
                "sinh khởi – ‘bất cứ điều nào có bản chất phát sinh, tất cả điều ấy đều có bản chất chấm dứt’, thì "
                f"này các tỳ-khưu, ngay khi việc thấy chân lý sinh khởi, ba xiềng xích của {ARIYASAVAKA} được dứt "
                f"bỏ – {TINI}” [trong {S.CIT['a. ni.']}]")


def build_ch3():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    # ---- Suddhabrahmacariyakathā ---------------------------------------------------------------------------------
    add("5-3-0", "### " + S.katha(BRAHMA))
    add("5-3-1-0", "#### " + S.katha(f"{BRAHMA} thuần túy"))
    d1n = (f"đần độn, câm điếc{S.var_sp('Syā.', 'eḷamūgā')}, không hiểu biết, giao tiếp bằng cử chỉ tay, không đủ "
           "khả năng hiểu ý nghĩa của lời nói hay và lời nói dở")
    d2n = ("không có lòng tin trong sáng nơi Đức Phật, không có lòng tin trong sáng nơi Giáo Pháp, không có lòng tin "
           f"trong sáng nơi Tăng đoàn, không thân cận {BP}, không đặt câu hỏi với {BP}, không hài lòng khi câu hỏi "
           f"được {BP} trả lời")
    d4n = "là kẻ giết mẹ, kẻ giết cha, kẻ giết bậc A-la-hán, kẻ làm chảy máu, kẻ chia rẽ Tăng đoàn"
    sab = "tất cả chư thiên đều"
    l1 = (f"{Q(BV_NO)} {YES} Có phải {sab} {d1n}, {sab} {d2n}, {sab} {AVARANA_N}, {sab} {d4n}, {sab} "
          f"{KAMMAPATHA_N} không? {NO_PE}")
    d1p = ("không đần độn, không câm điếc, có hiểu biết, không giao tiếp bằng cử chỉ tay, đủ khả năng hiểu ý nghĩa "
           "của lời nói hay và lời nói dở")
    d2a = "có lòng tin trong sáng nơi Đức Phật"
    d2p = (f"{d2a}, có lòng tin trong sáng nơi Giáo Pháp, có lòng tin trong sáng nơi Tăng đoàn, thân cận {BP}, đặt "
           f"câu hỏi với {BP}, hài lòng khi câu hỏi được {BP} trả lời")
    d4p = ("không phải là kẻ giết mẹ, không phải là kẻ giết cha, không phải là kẻ giết bậc A-la-hán, không phải là "
           "kẻ làm chảy máu, không phải là kẻ chia rẽ Tăng đoàn")
    co = "có chư thiên"
    l2 = f"{S.NANU(f'{co} {d1p}, {co} {d2p}, {co} {AVARANA_P}, {co} {d4p}, {co} {KAMMAPATHA_P}')} {YES}"
    l3 = S.hanci_neg(f"{co} {d1p}{PE} {co} {d2a}{PE} có quan điểm đúng đắn", BV_NO)
    add("5-269", l1, l2, l3)

    l1 = (f"{Q(BV_DEV)} {YES} Có phải ở đó có sự xuất gia, sự cạo đầu, sự mặc {KASAVA}, sự mang bình bát, {DEVESU} "
          f"các {SAMMASAMBUDDHA} xuất hiện, các {PACCEKA} xuất hiện, {SAVAKAYUGA} xuất hiện không? {NO_PE}")
    rows = [
        four("không có sự xuất gia", "có sự xuất gia", "không có sự xuất gia", "xuất gia", "không xuất gia"),
        four("không có sự cạo đầu", "có sự cạo đầu", "không có sự cạo đầu", "cạo đầu", "không cạo đầu"),
        four(f"không có sự mặc {KASAVA}", f"có sự mặc {KASAVA}", f"không có sự mặc {KASAVA}", f"mặc {KASAVA}",
             f"không mặc {KASAVA}"),
        four("không có sự mang bình bát", "có sự mang bình bát", "không có sự mang bình bát", "mang bình bát",
             "không mang bình bát", yes_q=True),
        arise(f"các {SAMMASAMBUDDHA} không xuất hiện", f"các {SAMMASAMBUDDHA} xuất hiện",
              f"các {SAMMASAMBUDDHA} không xuất hiện",
              f"Đức Thế Tôn đã sinh ra ở Lâm-tỳ-ni, đã giác ngộ hoàn toàn dưới gốc cây Bồ-đề, bánh xe Giáo Pháp đã "
              f"được Đức Thế Tôn chuyển ở Ba-la-nại; {CHINH} có {BV}, {ELSE}"),
        arise(f"các {PACCEKA} không xuất hiện", f"các {PACCEKA} xuất hiện", f"các {PACCEKA} không xuất hiện",
              f"{MAJJH}, các {PACCEKA} xuất hiện, {CHINH} có {BV}, {ELSE}"),
        arise(f"{SAVAKAYUGA} không xuất hiện", f"{SAVAKAYUGA} xuất hiện", f"{SAVAKAYUGA} không xuất hiện",
              f"{SAVAKAYUGA} đã xuất hiện ở xứ Ma-kiệt-đà, {CHINH} có {BV}, {ELSE}"),
    ]
    add("5-270", l1, *rows)

    mil_v = MIL.replace("người man di", "người man di" + S.var_sp("Syā., Ka.", "milakkhūsu"), 1)
    sv = f"{SANNASATTA}{S.var('Ka.', 'asaññasattesu')}"
    add("5-271",
        f"{Q(BV_DEV)} {YES} {Q(f'giữa tất cả chư thiên đều có {BV}')} {NO_PE}",
        f"{Q(BV_MAN)} {YES} {Q(f'giữa tất cả loài người đều có {BV}')} {NO_PE}",
        f"{Q(BV_DEV)} {YES} {Q(f'giữa {ASANNA} có {BV}')} {NO_PE}",
        f"{Q(BV_MAN)} {YES} Có phải {PACC} có {BV}, {mil_v} không? {NO}",
        f"{Q(BV_DEV)} {YN_ANS} Có phải giữa {ASANNA}, {YN} {BV}, giữa {sv}, {YN} {BV} không? {NO}",
        f"{Q(f'{DEVESU}, {YN} {BV}')} {YES} {KATTHA} Giữa {ASANNA} không có {BV}, giữa {sv} có {BV}. "
        f"{Q(f'giữa {ASANNA} không có {BV}')} {YES} {Q(f'giữa {sv} không có {BV}')} {NO}",
        f"{Q(f'giữa {SANNASATTA} có {BV}')} {YES} {Q(f'giữa {ASANNA} có {BV}')} {NO}",
        f"{Q(BV_MAN)} {YN_ANS} Có phải {PACC}, {YN} {BV}, {MIL}, {MAJJH}, {YN} {BV} không? {NO}",
        f"{Q(f'{MANUSSESU}, {YN} {BV}')} {YES} {KATTHA} {cap(PACC)} không có {BV}, {MIL}, {MAJJH} có {BV}. "
        f"Có phải {PACC} không có {BV}, {MIL} không? {YES} {Q(f'{MAJJH} không có {BV}')} {NO}",
        f"{Q(f'{MAJJH} có {BV}')} {YES} Có phải {PACC} có {BV}, {MIL} không? {NO}",
        f"{Q(BV_DEV)} {YES} {S.NANU_VUTTAM} {JAMBU} [{S.CIT['a. ni.']} 9.21]. {S.ATTHEVA} {YES} {S.tena_hi(BV_NO)}",
        f"Có phải Đức Thế Tôn đã nói ở Xá-vệ – “ở đây có {BV}” không? {YES} "
        f"{Q(f'chính ở Xá-vệ có {BV}, {ELSE}')} {NO}")

    def an_q(xs):
        return f"{cap(AN_HEAD)}, thì " + ", ".join(f"ở đâu {x}" for x in xs) + "?"

    add("5-272",
        f"{an_q(FR[:1])} {cap(CHINH)}. {S.hanci_neg(f'{AN_HEAD}, ở đó {FR[0]}', BV_NO, ';')}",
        f"{an_q(FR[1:])} {cap(CHINH)}. {S.hanci_neg(f'{AN_HEAD}, ở đó {FR[5]}', BV_NO, ';')}",
        f"{cap(AN_HEAD)}, " + ", ".join(f"ở đó {x}" for x in FR) + f"; theo nghĩa nào mà bạn nói – “{BV_NO}”? "
        f"Bởi vì {sac(ANAG, 'đây', 'đó')}{S.var(S.CIT['bahūsu'], 'sacchikaroti')}.")

    # ---- Saṃsandanabrahmacariyakathā --------------------------------------------------------------------------------
    add("5-3-2-0", "#### " + S.katha(f"{BRAHMA} xét theo sự đối chiếu"))
    T_AN = Q(sac(ANAG, "đây", "đó"))
    SAKA_IDHA = f"{SAKA}, người nhập Niết-bàn trọn vẹn ở đây"          # sakadāgāmī puggalo idha parinibbāyipuggalo
    lines = [
        f"{T_AN} {YES} {Q(sac(SOTA, 'đó', 'đây'))} {NO}",
        f"{T_AN} {YES} {Q(sac(SAKA_IDHA + S.var('?', 'idhaparinibbāyī'), 'đó', 'đây'))} {NO}",
        f"{Q(sac(SOTA, 'đây', 'đây'))} {YES} {Q(sac(ANAG, 'đó', 'đó'))} {NO}",
        f"{Q(sac(SAKA_IDHA, 'đây', 'đây'))} {YES} {Q(sac(ANAG, 'đó', 'đó'))} {NO_PE}",
        f"{Q(f'đối với {VIHAYA}, {MAGGO_NA}')} {YES} {Q(f'đối với {P_SOTA}, {MAGGO_NA}')} {NO_PE}",
        f"{Q(f'đối với {VIHAYA}, {MAGGO_NA}')} {YES} Có phải đối với {P_SAKA}{PE} {P_ARA}, {MAGGO_NA} không? "
        f"{NO_PE}",
        f"{Q(f'đối với {P_SOTA}, {MAGGO_CA}')} {YES} {Q(f'đối với {VIHAYA}, {MAGGO_CA}')} {NO}",
        f"Có phải đối với {P_SAKA}{PE} {P_ARA}, {MAGGO_CA} không? {YES} {Q(f'đối với {VIHAYA}, {MAGGO_CA}')} {NO}",
        f"{Q(f'{AN_KK}, tái sinh ở đó')} {YES} {Q(f'{ARAHA} tái sinh')} {NO}",
        f"{Q(f'{ARAHA} tái sinh')} {YES} {Q(f'{ARAHA} có sự hiện hữu mới')} {NO}",
        f"{Q(f'{ARAHA} có sự hiện hữu mới')} {YES} "
        f"{Q(f'{ARAHA} đi từ sự hiện hữu đến sự hiện hữu, đi từ cõi tái sinh đến cõi tái sinh, đi từ vòng luân hồi đến vòng luân hồi, đi từ sự tái sinh đến sự tái sinh')} "
        f"{NO}",
        f"{Q(f'{AN_KK}, {ANOHATA}, tái sinh ở đó')} {YES} {Q('tu tập lại con đường để gỡ bỏ gánh nặng')} {NO}",
        f"{Q(f'{AN_KK}, {APARI}, tái sinh ở đó')} {YES} {Q(f'tu tập lại con đường để {AKUPPA_V}')} {NO}",
        f"{Q(f'{AN_KK}, {ANOHATA}, tái sinh ở đó, nhưng không tu tập lại con đường để gỡ bỏ gánh nặng')} {YES} "
        f"{Q(f'{ANOHATA} mà nhập Niết-bàn trọn vẹn ở đó')} {NO}",
        f"{Q(f'{AN_KK}, {APARI}, tái sinh ở đó, nhưng không tu tập lại con đường để {AKUPPA_V}')} {YES} "
        f"{Q(f'chưa {AKUPPA_V} mà nhập Niết-bàn trọn vẹn ở đó')} {NO} "
        f"Cũng như {MIGO} cũng qua đời, cũng y như vậy, {sac(ANAG, 'đây', 'đó')}.",
        f"{Q(f'cũng như {MIGO} cũng qua đời {SASALLA}, cũng y như vậy, {ANAG}, nhờ con đường đã tu tập ở đây, nhập Niết-bàn trọn vẹn ở đó {SASALLA}')} "
        f"{NO_PE}",
        S.katha_end(BRAHMA),
    ]
    add("5-273", *lines)

    # ---- Odhisokathā -----------------------------------------------------------------------------------------------
    add("5-3-3-0", "#### " + S.katha("từng phần"))
    ONE = "dứt bỏ một phần"
    sota_full = (f"{head_status(SOTA, 'thành quả vào dòng', '{v}')}, {SOTA_TAIL}")
    sota_full_v = sota_full.replace("{v}", S.var("?", "sotāpattiphalaṃ patto"))
    sota_full_n = sota_full.replace("{v}", "")
    sota_short = short(SOTA, f"{ARIYAKANTA_YES}, {ARIYAKANTA_NO}")
    add("5-274",
        f"{Q(ODHI)} {YES} {kim('dukkha', P_SOTA)} {cap(ONE)} {SAKKAYA}, {VICI}, {SILAB}, {TAD}. "
        f"{status_q(sota_full_v)}",
        f"{kim('samudaya')} Dứt bỏ {SAKKAYA}, {ONE} {VICI}, {SILAB}, {TAD}. {status_q(sota_short)}",
        f"{kim('nirodha')} {cap(ONE)} {VICI}, {SILAB}, {TAD}. {status_q(sota_short)}",
        f"{kim('magga')} Dứt bỏ {SILAB}, {TAD}. {status_q(sota_full_n)}")

    kr, by = f"sự tham đắm dục lạc {ODARIKA}", f"ác ý {ODARIKA}"
    saka_v = head_status(SAKA, "thành quả trở lại một lần", S.var("?", "sakadāgāmiphalaṃ patto"))
    saka_n = head_status(SAKA, "thành quả trở lại một lần")
    add("5-275",
        f"{kim('dukkha', P_SAKA)} Dứt bỏ {kr}, {ONE} {by}, {TAD}. {status_q(saka_v)}",
        f"{kim('samudaya')} Dứt bỏ {kr}, {ONE} {by}, {TAD}. {status_q(saka_n)}",
        f"{kim('nirodha')} Dứt bỏ {by}, {TAD_PART}. {status_q(saka_n)}",
        f"{kim('magga')} Dứt bỏ {by}, {TAD_ALL}. {status_q(saka_n)}")

    kr, by = "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "ác ý ở dạng nhỏ nhiệm"
    an_full = f"{head_status(ANAG, 'thành quả không trở lại', '{v}')}, {ANAG_TAIL}"
    an_short = short(ANAG, f"một phần là {UDDHAMSOTO}, một phần không phải là {UDDHAMSOTO}")
    add("5-276",
        f"{kim('dukkha', P_ANAG)} Dứt bỏ {kr}, {ONE} {by}, {TAD}. "
        f"{status_q(an_full.replace('{v}', S.var('?', 'anāgāmiphalaṃ patto')))}",
        f"{kim('samudaya')} Dứt bỏ {kr}, {ONE} {by}, {TAD}. {status_q(an_short)}",
        f"{kim('nirodha')} Dứt bỏ {by}, {TAD_PART}. {status_q(an_short)}",
        f"{kim('magga')} {cap(TAD_ALL)}. {status_q(an_full.replace('{v}', ''))}")

    rr = RUPARAGA.split(", ")                       # rūparāga, arūparāga, māna, uddhacca
    AV = "vô minh"
    ara_head = "đã đạt đến trạng thái A-la-hán"
    ara_base = (f"một phần là {ARAHA}, một phần không phải là {ARAHA}, một phần {ara_head}{{v}}, {ATTAINED}, "
                f"một phần {ARA_EPI}, {ARA_DONE}, ")
    ara_full_v = (ara_base.replace("{v}", S.var("?", "arahattaṃ patto"))
                  + f"({SC_YES},){S.var('?', '( )')} {SC_NO}")
    ara_full_n = ara_base.replace("{v}", "") + f"{SC_YES}, {SC_NO}"
    ara_short = short(ARAHA, f"{SC_YES}, {SC_NO}")
    add("5-277",
        f"{kim('dukkha', P_ARA)} {cap(ONE)} {rr[0]}, {rr[1]}, {rr[2]}, {rr[3]}, {AV}, {TAD}. {status_q(ara_full_v)}",
        f"{kim('samudaya')} Dứt bỏ {rr[0]}, {rr[1]}, {ONE} {rr[2]}, {rr[3]}, {AV}, {TAD}. {status_q(ara_short)}",
        f"{kim('nirodha')} Dứt bỏ {rr[2]}, {ONE} {rr[3]}, {AV}, {TAD}. {status_q(ara_short)}",
        f"{kim('magga')} Dứt bỏ {rr[3]}, {AV}, {TAD}. {status_q(ara_full_n)}")

    TH = S.tena_hi_na(ODHI)
    add("5-278",
        f"{S.na_vattabbam(ODHI)} {YES} {S.NANU_VUTTAM}",
        *DHP,
        f"{S.ATTHEVA} {YES} {TH}",
        f"{Q(ODHI)} {YES} {S.NANU_VUTTAM}",
        *RATANA,
        f"{S.ATTHEVA} {YES} {TH}",
        f"{Q(ODHI)} {YES} {S.NANU_VUTTAM} {DHAMMACAKKHU}. {S.ATTHEVA} {YES} {TH}",
        S.katha_end("từng phần"))
    return segs


# ---------------------------------------------------------------------------------------------------------------
def check_reused():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize(
            "NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))).lower()
    bad = [(v, b) for v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    ch2 = unicodedata.normalize("NFC", (S.OUT_DIR / "2-parihanikatha.md").read_text(encoding="utf-8"))
    bad = [v for v in CH2 if v not in ch2]
    assert not bad, "chapter-2 strings not found in 2-parihanikatha.md: " + repr(bad)


def lookup():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb[ln.split(": {", 1)[0]] = ln
    tbl = {k.lower(): v for k, v in tb.items()}
    seen = set()
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        ok = i.startswith("5-3-") or (re.fullmatch(r"5-\d+", i) and 269 <= int(i[2:]) <= 278)
        if not ok:
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                e = tb.get(kk) or tbl.get(kk.lower())
                print(f"[{i}] {e if e else kk + ': <NOT IN TERMBASE>'}")


def main():
    S.check_reused()
    check_reused()
    segs = build_ch3()
    S.write(NAME, segs)


if __name__ == "__main__":
    if "--lookup" in sys.argv:
        lookup()
    else:
        main()
