"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 12, Catutthavaggo (^5-12-0 … ^5-417): ten kathās
(33-42) with the repeated "Catutthavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/12-catutthavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, neu,
na_vattabbam, tena_hi, tena_hi_na, katha, katha_end, vaggo, var …). Strings taken from pi-1 … pi-4 rails are asserted
there (REUSED12); strings shared with the finished pi-5 rails chapters (sample, ch2-ch5, ch8, ch9) are asserted in
those chapter files (SHARED). The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-12.md.

usage: python -I -X utf8 -B build_rails_12_vi.py          (writes the chapter and the adherence copy rails\\adh-12\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "12-catutthavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap = S.cap
CIT = S.CIT

# ---------------------------------------------------------------------------------------------------------------
# Persons, fruits, paths (pi-4 / ch2 / ch3 / ch4)
# ---------------------------------------------------------------------------------------------------------------
AR, SO, SA, AN = S.PN["arahā"], S.PN["sotāpanno"], S.PN["sakadāgāmī"], S.PN["anāgāmī"]      # (pi-4)
ARAHATTA = "trạng thái A-la-hán"                                       # arahattaṃ (termbase; ch2)
FR = {"so": "thành quả vào dòng", "sa": "thành quả trở lại một lần", "an": "thành quả không trở lại"}  # (ch2)
PATH = {"so": "con đường vào dòng", "sa": "con đường trở lại một lần", "an": "con đường không trở lại"}  # (ch4)
NAMES = {"so": SO, "sa": SA, "an": AN}
SO_TYPES = (f"{SO}, người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, "
            f"người có một hạt giống")
#   sotāpanno sattakkhattuparamo, kolaṅkolo, ekabījī (pi-4)
AN_TYPES = (f"{AN}, người nhập Niết-bàn trọn vẹn trong khoảng giữa, người nhập Niết-bàn trọn vẹn khi gần mạng chung, "
            f"người nhập Niết-bàn trọn vẹn không có sự thúc đẩy, người nhập Niết-bàn trọn vẹn có sự thúc đẩy, "
            f"người theo dòng đi lên đến cõi Sắc Cứu Cánh")
#   anāgāmī, antarāparinibbāyī, upahacca-, asaṅkhāra-, sasaṅkhāraparinibbāyī, uddhaṃsoto akaniṭṭhagāmī (pi-4)
PA = "người đang thực hành để tự mình chứng nghiệm trạng thái A-la-hán"           # arahattasacchikiriyāya paṭipanno puggalo (ch3)
PN = "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"       # anāgāmiphala… (pi-4, ch4)
PS = "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần"     # sakadāgāmiphala… (pi-4)
PU = "người phàm phu"                                                  # puthujjano (pi-1, ch4)
SAMG = "được trang bị"                                                 # samannāgato (termbase)
PAHINA = "đã được dứt bỏ"                                              # pahīnaṃ / pahīnā (termbase, ch2)
UCCH = ("đã bị cắt đứt tận gốc, đã bị làm như cây thốt nốt bị chặt ngọn, đã bị làm cho không còn hiện hữu, "
        "có bản chất không sinh khởi trong tương lai")                 # ucchinnamūlaṃ … anuppādadhammaṃ (ch2)
DITTHE = "ngay trong đời này"                                          # diṭṭheva dhamme (pi-4)
DUKKHA_ANTA = "người đi đến tận cùng của khổ đau"                      # dukkhassantakaro (pi-4)
BHEDA = "khi thân tan rã"                                              # kāyassa bhedā (pi-2)
THERAS = ["trưởng lão Đại Mục-kiền-liên", "trưởng lão Đại Ca-diếp", "trưởng lão Đại Ca-chiên-diên",
          "trưởng lão Đại Câu-hi-la", "trưởng lão Đại Bàn-đặc"]       # (ch2)
SARI = "trưởng lão Xá-lợi-phất"                                        # Sāriputto thero (termbase, ch2)
F4 = "hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường"   # (ch5)
F4S = f"hiểu biết trọn vẹn khổ đau{PE} tu tập con đường"              # dukkhaṃ parijānāti…pe… maggaṃ bhāveti
FETTERS3 = "quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức"   # (pi-1, ch4)
OLARIKA = "sự tham đắm dục lạc ở dạng thô, ác ý ở dạng thô"           # oḷārikaṃ kāmarāgaṃ (,) oḷārikaṃ byāpādaṃ (ch4)
ANUSAH = "sự tham đắm dục lạc ở dạng nhỏ nhiệm, ác ý ở dạng nhỏ nhiệm"   # aṇusahagataṃ … (ch2)
APAYA3 = "sự tham đắm dẫn đến cõi khổ, sự sân hận dẫn đến cõi khổ, sự si mê dẫn đến cõi khổ"   # apāyagamanīyaṃ … (ch2)
KIL = {"so": f"{FETTERS3}, {APAYA3}", "so_s": f"quan điểm về tự ngã{PE} sự si mê dẫn đến cõi khổ",
       "sa": OLARIKA, "an": ANUSAH}
VUTTAM_RANG = "Đức Thế Tôn đã nói rằng"                                # … vuttaṃ bhagavatā (no quote; ch4)
POS = ["dẫn đến giải thoát", "dẫn đến sự diệt tận", "dẫn đến sự giác ngộ", "dẫn đến sự giảm trừ",
       "không phải là đối tượng của ô nhiễm", "không phải là đối tượng của phiền não"]   # niyyānikaṃ … (ch4)
NEG = ["không dẫn đến giải thoát", "không dẫn đến sự diệt tận", "không dẫn đến sự giác ngộ",
       "không dẫn đến sự giảm trừ", "là đối tượng của ô nhiễm", "là đối tượng của phiền não"]  # aniyyānikaṃ … (ch4)
ANS = "không phải là đối tượng của ô nhiễm"                            # anāsava (termbase)
SAS = "đối tượng của ô nhiễm"                                          # sāsava (termbase)
PAGG = ("có thể bị nhấc lên và bị đè xuống, có thể bị cắt và bị đập vỡ, là thứ chung cho quạ, kền kền, diều hâu")
#   paggahaniggahupago chedanabhedanupago kākehi gijjhehi kulalehi sādhāraṇo (ch5)
REQ = "đồ ăn khất thực, cho chỗ ở, cho thuốc men và vật dụng chữa bệnh"   # piṇḍapātaṃ deti, senāsanaṃ … (pi-2 items)
FOUR_TRUTHS = {"d": "sự thật cao quý về khổ đau", "s": "sự thật cao quý về sự phát sinh của khổ đau",
               "n": "sự thật cao quý về sự chấm dứt khổ đau",
               "m": "sự thật cao quý về cách thực hành dẫn đến sự chấm dứt khổ đau"}   # (pi-2)
LIST10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
          "sự định tâm", "trí tuệ"]                                     # phassehi … paññāhi (ch4 tiṇṇaṃ phassānaṃ …)
PAST, FUT, PRES = "quá khứ", "tương lai", "hiện tại"                    # atītāya / anāgatāya / paccuppannāya (ch5)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(4)                                                     # Catutthavaggo «Chương thứ tư» (termbase)
GIHI = "người tại gia"                                                 # gihī / Gihissa (termbase)
G = f"{GIHI} có thể là {AR}"                                           # gihissa (= gihi assa) arahā (commentary)
SU = f"là {AR} ngay khi tái sinh"                                      # saha upapattiyā arahā (termbase Saha upapattiyā)
SUN = f"không phải là {AR} ngay khi tái sinh"                          # na saha upapattiyā arahā
T3 = f"tất cả các hiện tượng của {AR} đều {ANS}"                       # arahato sabbe dhammā anāsavā
UP6 = "sáu sự bình thản"                                               # chahi upekkhāhi
BB = "là bậc giác ngộ nhờ sự giác ngộ"                                 # bodhiyā buddho (termbase)
BS, CV = "Bồ-tát", "người làm vua chuyển luân"                         # bodhisatto / cakkavattisatto (termbase)
LS = "người được trang bị các tướng"                                   # lakkhaṇasamannāgato (termbase phrase)
LB = f"{LS} là {BS}"                                                   # lakkhaṇasamannāgato bodhisatto (termbase)
KAS = "Đức Thế Tôn Ca-diếp"                                            # kassapassa bhagavato (termbase)
OKC = "đã bước vào sự cố định, đã sống đời sống tu hành trong sạch"    # okkantaniyāmo caritabrahmacariyo (termbase)
OK = f"{BS} {OKC} trong lời dạy của {KAS}"                             # bodhisatto kassapassa bhagavato pāvacane …
TH10 = "sự dứt bỏ tất cả các xiềng xích là trạng thái A-la-hán"        # sabbasaṃyojanānaṃ pahānaṃ arahattaṃ
KATHA = {1: f"việc {G}", 2: "sự tái sinh", 3: f"những gì {ANS}", 4: "sự được trang bị",
         5: "sự được trang bị sự bình thản", 6: "bậc giác ngộ nhờ sự giác ngộ", 7: "các tướng",
         8: "việc bước vào sự cố định", 10: "sự dứt bỏ tất cả các xiềng xích"}
#   Gihissa arahātikathā, Upapattikathā, Anāsavakathā, Samannāgatakathā, Upekkhāsamannāgatakathā,
#   Bodhiyā buddhotikathā, Lakkhaṇakathā, Niyāmokkantikathā (termbase), Sabbasaṃyojanappahānakathā
H9 = "Bàn thêm về sự được trang bị"                                    # Aparāpi samannāgatakathā
END9 = "Phần bàn thêm về sự được trang bị đã hoàn tất."                # Aparāpi samannāgatakathā niṭṭhitā.
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)
UDDANA = (f"{cap(G)}, {SU}, {T3}, {AR} {SAMG} bốn thành quả, cũng vậy với {UP6}, bậc giác ngộ nhờ sự giác ngộ, "
          f"{LS}, {BS} {OKC}, người đang thực hành {SAMG} thành quả, {TH10}.")
#   Gihissa arahā, saha upapattiyā arahā, … salakkhaṇasamannāgato, bodhisatto okkantaniyāmo caritabrahmacariyo,
#   paṭipannako phalena samannāgato, sabbasaṃyojanānaṃ pahānaṃ arahattanti.

REUSED12 = [  # (Pāli, Vietnamese, book)
    ("sattakkhattuparamo", "người tái sinh tối đa bảy lần", "4"),
    ("kolaṅkolo", "người đi từ gia đình này sang gia đình khác", "4"),
    ("ekabījī", "người có một hạt giống", "4"),
    ("antarāparinibbāyī", "người nhập Niết-bàn trọn vẹn trong khoảng giữa", "4"),
    ("upahaccaparinibbāyī", "người nhập Niết-bàn trọn vẹn khi gần mạng chung", "4"),
    ("asaṅkhāraparinibbāyī", "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy", "4"),
    ("sasaṅkhāraparinibbāyī", "người nhập Niết-bàn trọn vẹn có sự thúc đẩy", "4"),
    ("uddhaṃsoto akaniṭṭhagāmī", "người theo dòng đi lên đến cõi Sắc Cứu Cánh", "4"),
    ("anāgāmiphalasacchikiriyāya paṭipanno", PN, "4"),
    ("sakadāgāmiphalasacchikiriyāya paṭipanno", PS, "4"),
    ("diṭṭheva dhamme", DITTHE, "4"), ("dukkhassantakaro", DUKKHA_ANTA, "4"),
    ("kāyassa bhedā", BHEDA, "2"),
    ("ajeḷaka-", "dê và cừu", "4"), ("kukkuṭasūkara-", "gà và heo", "4"),
    ("hatthigavāssavaḷava-", "voi, bò, ngựa đực và ngựa cái", "4"),
    ("mālāgandhavilepana-", "vòng hoa, hương thơm, dầu thoa", "4"),
    ("jātarūparajata-", "vàng và bạc", "1"),
    ("cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāra",
     "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh", "2"),
    ("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahāna-",
     "sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động và vô minh không còn sót lại",
     "4"),
    ("sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso", FETTERS3, "1"),
    ("puthujjano", PU, "1"),
    ("dukkhaṃ / dukkhasamudayaṃ / dukkhanirodhaṃ ariyasaccaṃ", FOUR_TRUTHS["d"], "2"),
    ("dukkhasamudayaṃ ariyasaccaṃ", FOUR_TRUTHS["s"], "2"), ("dukkhanirodhaṃ ariyasaccaṃ", FOUR_TRUTHS["n"], "2"),
    ("dukkhanirodhagāminī paṭipadā ariyasaccaṃ", FOUR_TRUTHS["m"], "2"),
    ("pubbe ananussutesu dhammesu", "trong những điều chưa từng được nghe trước đây", "4"),
    ("arahaṃ sammāsambuddho", "bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn", "4"),
    ("aññaṃ satthāraṃ uddiseyya", "một vị khác làm bậc đạo sư", "2"),
    ("rājāno cakkavattī", "vua chuyển luân", "2"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Mahāmoggallāno thero…pe… mahāpanthako thero", f"{PE} ".join(THERAS), "2-parihanikatha.md"),
    ("Sāriputto thero", SARI, "2-parihanikatha.md"),
    ("pahīno ucchinnamūlo … anuppādadhammo", UCCH, "2-parihanikatha.md"),
    ("apāyagamanīyo rāgo / doso / moho", "sự si mê dẫn đến cõi khổ", "2-parihanikatha.md"),
    ("aṇusahagato kāmarāgo / byāpādo", "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "2-parihanikatha.md"),
    ("catūhi phalehi", "bốn thành quả", "2-parihanikatha.md"),
    ("sotāpattiphala …", FR["sa"], "2-parihanikatha.md"),
    ("arahattasacchikiriyāya paṭipanno", PA, "3-brahmacariyakatha.md"),
    ("bodhiyā mūle", "dưới gốc cây Bồ-đề", "3-brahmacariyakatha.md"),
    ("arahattappatto", "đã đạt đến trạng thái A-la-hán", "3-brahmacariyakatha.md"),
    ("niyyāniko khayagāmī bodhagāmī apacayagāmī anāsavo", ", ".join(POS[:5]), "4-jahatikatha.md"),
    ("aniyyāniko na khayagāmī na bodhagāmī na apacayagāmī sāsavo", ", ".join(NEG[:5]), "4-jahatikatha.md"),
    ("oḷārikaṃ kāmarāgaṃ oḷārikaṃ byāpādaṃ", OLARIKA, "4-jahatikatha.md"),
    ("Nanu … vuttaṃ bhagavatāti?", f"Chẳng phải {VUTTAM_RANG}", "4-jahatikatha.md"),
    ("tīṇi sāmaññaphalāni", "ba thành quả của đời sống sa-môn", "4-jahatikatha.md"),
    ("natthi dāni punabbhavo", "giờ đây không có sự hiện hữu mới", "4-jahatikatha.md"),
    ("tiṇṇaṃ phassānaṃ … paññānaṃ", "ba sự tiếp xúc, ba cảm giác, ba tri giác, ba chủ ý, ba tâm, ba niềm tin, "
     "ba sự tinh tấn, ba sự tỉnh thức, ba sự định tâm, ba trí tuệ", "4-jahatikatha.md"),
    ("paggahaniggahupago … sādhāraṇo", PAGG, "5-sabbamatthitikatha.md"),
    ("kāye visaṃ kameyya, satthaṃ kameyya, aggi kameyya", "dao kiếm có thể tác động, lửa có thể tác động",
     "5-sabbamatthitikatha.md"),
    ("addubandhanena bandhituṃ …", "bằng sự giam giữ bằng cùm, trói bằng sự giam giữ bằng dây thừng, trói bằng sự "
     "giam giữ bằng xích sắt, trói bằng sự giam giữ trong làng", "5-sabbamatthitikatha.md"),
    ("kaṇṭhapañcamehi bandhanehi bandhituṃ", "trói bằng các dây trói có cổ là thứ năm", "5-sabbamatthitikatha.md"),
    ("dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti", F4,
     "5-sabbamatthitikatha.md"),
    ("tena ñāṇena ñāṇakaraṇīyaṃ karoti", "bằng hiểu biết ấy mà làm việc của hiểu biết", "5-sabbamatthitikatha.md"),
    ("A hutvā B hoti", "là tương lai rồi trở thành hiện tại", "5-sabbamatthitikatha.md"),
    ("Taññeva A taṃ B", "chính cái tương lai ấy là cái hiện tại ấy", "5-sabbamatthitikatha.md"),
    ("satiyā samohitā", "được kết hợp với sự tỉnh thức", "8-satipatthanakatha.md"),
    ("sati paccupaṭṭhitā", "sự tỉnh thức hiện diện", "8-satipatthanakatha.md"),
    ("cakka- … pariṇāyakaratana", "báu vật bánh xe", "8-satipatthanakatha.md"),
    ("pariṇāyakaratana", "báu vật vị cố vấn", "8-satipatthanakatha.md"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Nanu āyasmā ānando bhagavantaṃ etadavoca –", "đã nói với Đức Thế Tôn điều này sao –", "1-puggalakatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED12 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Small frames
# ---------------------------------------------------------------------------------------------------------------
def sam(who, what):                 # X Y-ehi samannāgato
    return f"{who} {SAMG} {what}"


def is_(who, what):                 # X Y (identity question)
    return f"{who} là {what}"


def full10(n):                      # catūhi phassehi … catūhi paññāhi
    return ", ".join(f"{n} {x}" for x in LIST10)


def short10(n):                     # tīhi phassehi…pe… tīhi paññāhi
    return f"{n} {LIST10[0]}{PE} {n} {LIST10[-1]}"


def short10b(n):                    # tīhi phassehi tīhi vedanāhi…pe… tīhi paññāhi
    return f"{n} {LIST10[0]}, {n} {LIST10[1]}{PE} {n} {LIST10[-1]}"


def hut(a, b):                      # A hutvā B hoti (ch5 «là A rồi trở thành B»)
    return f"{a} rồi trở thành {b}"


NA = hut(ANS, SAS)                  # anāsavaṃ hutvā sāsavaṃ hoti
AS = hut(f"là {SAS}", ANS)          # sāsavaṃ hutvā anāsavaṃ hoti
TN = f"chính cái {ANS} ấy là cái {SAS} ấy"          # taññeva anāsavaṃ taṃ sāsavaṃ
TS = f"chính cái {SAS} ấy là cái {ANS} ấy"          # taññeva sāsavaṃ taṃ anāsavaṃ
PATHS7 = (f"thành quả{PE} sự thiết lập tỉnh thức{PE} nỗ lực đúng đắn{PE} nền tảng thần thông{PE} năng lực{PE} "
          f"sức mạnh{PE} chi phần giác ngộ")         # phalaṃ… satipaṭṭhānaṃ… … bojjhaṅgo
MP_FULL = ("là con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng, con đường trở lại một lần, "
           "thành quả trở lại một lần, con đường không trở lại, thành quả không trở lại, con đường A-la-hán, "
           "thành quả A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, năng lực, sức mạnh, "
           "chi phần giác ngộ")      # Maggo phalaṃ nibbānaṃ, sotāpattimaggo … bojjhaṅgo
MP_SHORT = f"là con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng{PE} chi phần giác ngộ"


def band(x, comp=False):            # labbhā X addubandhanena bandhituṃ … kaṇṭhapañcamehi bandhanehi bandhituṃ (ch5)
    places = ["trong làng, thị trấn, thành phố, vùng đất"] if comp else [
        "trong làng", "trong thị trấn", "trong thành phố", "trong vùng đất"]
    items = ["bằng cùm", "bằng dây thừng", "bằng xích sắt"] + places
    parts = [f"trói bằng sự giam giữ {i}" for i in items]
    return (f"có thể trói {x} bằng sự giam giữ {items[0]}, " + ", ".join(parts[1:])
            + ", trói bằng các dây trói có cổ là thứ năm")


def got(who, n, what="thành quả", comma=True, one=False):   # X-ena N phalāni paṭiladdhāni(,) tehi ca aparihīno
    obj = "nó" if one else "chúng"
    return f"{who} đã có được {n} {what}{',' if comma else ''} và không sa sút khỏi {obj}"


def bb(t):                          # atītāya / anāgatāya / paccuppannāya bodhiyā buddho
    return f"là bậc giác ngộ nhờ sự giác ngộ thuộc {t}"


def by(x, neg=False):               # (na ca) tāya bodhiyā X (ch5 «bằng hiểu biết ấy mà …»)
    return f"{'nhưng ' if neg else ''}bằng sự giác ngộ ấy mà {'không ' if neg else ''}{x}"


KAR = "làm việc của sự giác ngộ"    # bodhikaraṇīyaṃ karoti (ch5 «làm việc của hiểu biết»)


def yatha(a, b):                    # Yathā A, evamevaṃ Bti? (sample)
    return f"Có phải cũng như {a}, cũng y như vậy, {b} không? {NO_PE}"


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    heading("5-12-0", 3, VAGGA)

    # ---- (33) 1. Gihissa arahātikathā ---------------------------------------------------------------------------
    heading("5-12-1-0", 4, f"(33) 1. {S.katha(KATHA[1])}")
    GS = "xiềng xích của người tại gia"                       # gihisaṃyojanaṃ (termbase)
    NO_GS = f"{AR} không có {GS}"
    PH = f"{GS} ở {AR} {PAHINA}, {UCCH}"
    A3 = f"{GIHI} nào, khi chưa dứt bỏ {GS}, mà {DITTHE} là {DUKKHA_ANTA}"
    A4 = f"{GIHI} nào, khi chưa dứt bỏ {GS}, mà {BHEDA} là {DUKKHA_ANTA}"
    LIFE = ("hưởng thụ hành vi dâm dục, làm phát sinh sự dâm dục, sống trên chiếc giường chật chội vì con cái, "
            "thụ hưởng gỗ đàn hương xứ Ca-thi, mang vòng hoa, hương thơm, dầu thoa, nhận vàng và bạc, nhận dê và cừu, "
            "nhận gà và heo, nhận voi, bò, ngựa đực và ngựa cái, nhận chim đa đa, chim cút, chim công và chim trĩ"
            + S.var_sp("Syā., Kaṃ., Pī.", "… kapiñjalaṃ") + ", mang búi tóc nhiều màu"
            + S.var("Syā., Kaṃ., Pī.", "pītavaṇṭavālamoḷikaṃ")
            + ", mang những tấm vải trắng có viền dài, suốt đời là người sống đời gia đình")
    YASO = "người con nhà gia giáo Da-xá, gia chủ Út-ti-da, thanh niên Sê-tu"   # yaso kulaputto, uttiyo gahapati, setu māṇavo
    YP = f"{YASO}, đã đạt đến {ARAHATTA} với hình tướng của người tại gia"
    add("5-387",
        f"{Q(G)} {YES} {Q(f'{AR} có {GS}')} {NO_PE} {q(NO_GS)} {YES} {S.hanci_neg(NO_GS, G)}",
        f"{Q(G)} {YES} {NANU(PH)} {YES} {S.hanci_neg(PH, G)}",
        f"{Q(G)} {YES} Có phải có {A3} [{CIT['ma. ni.']} 2.186] không? Không có. {S.hanci_neg(f'không có {A3}', G)}",
        f"{Q(G)} {YES} Chẳng phải du sĩ Vác-cha-gốt-ta đã nói với Đức Thế Tôn điều này sao – "
        f"“Thưa ông Cồ-đàm, có {A4} không”? “Này Vác-cha, không có {A4}”. {S.ATTHEVA} {YES} {S.tena_hi_na(G)}",
        f"{Q(G)} {YES} Có phải {AR} có thể {LIFE} không? {NO_PE}",
        f"{S.na_vattabbam(G)} {YES} {NANU(YP)} {YES} {S.hanci(YP, G)}",
        S.katha_end(KATHA[1]))

    # ---- (34) 2. Upapattikathā ----------------------------------------------------------------------------------
    heading("5-12-2-0", 4, VAGGA)
    heading("5-12-2-1-0", 5, f"(34) 2. {S.katha(KATHA[2])}")

    def tt(x, neg=False):           # saha upapattiyā X (na) hoti
        return f"{'không ' if neg else ''}trở thành {x} ngay khi tái sinh"

    add("5-388", *[f"{Q(SU)} {YES} {Q(tt(x))} {NO_PE}" for x in (SO, SA, AN)],
        *[f"{Q(tt(x, True))} {YES} {S.hanci_neg(tt(x, True), SU)}" for x in (SO, SA, AN)])
    THER = f"{PE} ".join(THERAS)
    add("5-389",
        f"{Q(SU)} {YES} {Q(f'{SARI} {SU}')} {NO} Có phải {THER} {SU} không? {NO_PE}",
        f"{Q(f'{SARI} {SUN}')} {YES} {S.hanci_neg(f'{SARI} {SUN}', SU)}",
        f"Có phải {THER} {SUN} không? {YES} {S.hanci_neg(f'{THERAS[-1]} {SUN}', SU)}")
    UPC = "tâm tìm cầu sự tái sinh"                                # upapattesiyaṃ cittaṃ (termbase)
    POSL = ", ".join(POS[:5]) + f"{PE} " + POS[-1]
    NEGL = ", ".join(NEG[:5]) + f"{PE} " + NEG[-1]
    add("5-390",
        f"{Q(SU)} {YES} Có phải bằng {UPC}, thuộc thế gian, {NEG[4]}{PE} {NEG[5]}, mà tự mình chứng nghiệm "
        f"{ARAHATTA} không? {NO_PE}",
        f"{Q(SU)} {YES} {Q(f'{UPC} {POSL}')} {NO_PE}",
        f"{NANU(f'{UPC} {NEGL}')} {YES} {S.hanci_neg(f'{UPC} {NEGL}', SU)}",
        f"{Q(SU)} {YES} Có phải bằng {UPC} mà dứt bỏ sự tham đắm, dứt bỏ sự sân hận, dứt bỏ sự si mê, "
        f"dứt bỏ sự không biết ghê sợ tội lỗi không? {NO_PE}",
        f"{Q(SU)} {YES} Có phải {UPC} là con đường{PE} sự thiết lập tỉnh thức{PE} nỗ lực đúng đắn{PE} "
        f"nền tảng thần thông{PE} năng lực{PE} sức mạnh{PE} chi phần giác ngộ không? {NO_PE}",
        f"{Q(SU)} {YES} Có phải bằng {UPC} mà {F4} không? {NO_PE} {q(SU)} {YES} "
        f"Có phải tâm lúc chết là tâm con đường, {UPC} là tâm thành quả không? {NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (35) 3. Anāsavakathā -----------------------------------------------------------------------------------
    heading("5-12-3-0", 4, VAGGA)
    heading("5-12-3-1-0", 5, f"(35) 3. {S.katha(KATHA[3])}")
    BODY = f"thân của {AR}"
    add("5-391",
        f"{Q(T3)} {YES} {Q(MP_FULL)} {NO_PE}",
        f"{Q(T3)} {YES} {Q(f'mắt của {AR} {ANS}')} {NO_PE} {Q(f'mắt của {AR} {ANS}')} {YES} {Q(MP_SHORT)} {NO_PE}",
        f"Có phải tai của {AR}{PE} mũi của {AR}{PE} lưỡi của {AR}{PE} {BODY} {ANS} không? {NO_PE} "
        f"{q(f'{BODY} {ANS}')} {YES} {Q(MP_SHORT)} {NO_PE}",
        f"{Q(f'{BODY} {ANS}')} {YES} {Q(f'{BODY} {PAGG}')} {YES} {Q(f'hiện tượng {ANS} {PAGG}')} {NO_PE}",
        f"{Q(f'chất độc có thể tác động lên {BODY}, dao kiếm có thể tác động, lửa có thể tác động')} {YES} "
        f"{Q(f'chất độc có thể tác động lên hiện tượng {ANS}, dao kiếm có thể tác động, lửa có thể tác động')} "
        f"{NO_PE}",
        f"{Q(band(BODY))} {YES} {Q(band(f'hiện tượng {ANS}', comp=True))} {NO_PE}")

    def l392(give, first, then):    # Yadi … deti, A hutvā B hotīti? … Taññeva …  Maggo / Rāgo …
        return (f"{S.neu(give, 'nó ' + first)} {NO_PE} {q('nó ' + first)} {YES} {Q(then[0])} {NO_PE} "
                f"{q(then[0])} {YES} {Q(then[1])} {NO_PE} {q(then[2])} {NO_PE}")

    MAGGA_NA = (TN, f"con đường {NA}", f"{PATHS7} {NA}")
    RAGA_AS = (TS, f"sự tham đắm {AS}", f"sự sân hận{PE} sự si mê{PE} sự không biết ghê sợ tội lỗi {AS}")
    add("5-392",
        l392(f"{AR} cho {PU} y phục", NA, MAGGA_NA),
        l392(f"{AR} cho {PU} {REQ}", NA, MAGGA_NA),
        l392(f"{PU} cho {AR} y phục", AS, RAGA_AS),
        l392(f"{PU} cho {AR} {REQ}", AS, RAGA_AS),
        f"{S.na_vattabbam(T3)} {YES} {NANU(f'{AR} {ANS}')} {YES} {S.hanci(f'{AR} {ANS}', T3)}",
        S.katha_end(KATHA[3]))

    # ---- (36) 4. Samannāgatakathā -------------------------------------------------------------------------------
    heading("5-12-4-0", 4, VAGGA)
    heading("5-12-4-1-0", 5, f"(36) 4. {S.katha(KATHA[4])}")
    add("5-393",
        f"{Q(sam(AR, 'bốn thành quả'))} {YES} {Q(sam(AR, full10('bốn')))} {NO_PE}",
        f"{Q(sam(AN, 'ba thành quả'))} {YES} {Q(sam(AN, short10('ba')))} {NO_PE}",
        f"{Q(sam(SA, 'hai thành quả'))} {YES} {Q(sam(SA, short10('hai')))} {NO_PE}",
        f"{Q(sam(AR, FR['so']))} {YES} {Q(is_(AR, SO_TYPES))} {NO_PE} {q(sam(AR, FR['sa']))} {YES} "
        f"{Q(is_(AR, SA))} {NO_PE} {q(sam(AR, FR['an']))} {YES} {Q(is_(AR, AN_TYPES))} {NO_PE}",
        f"{Q(sam(AN, FR['so']))} {YES} {Q(is_(AN, SO_TYPES))} {NO_PE} {q(sam(AN, FR['sa']))} {YES} "
        f"{Q(is_(AN, SA))} {NO_PE}",
        f"{Q(sam(SA, FR['so']))} {YES} {Q(is_(SA, SO_TYPES))} {NO_PE}")

    def called(who, k, quoted=True):   # X-phalena samannāgato "X"ti vattabbo … Sveva Y, so X?
        name = NAMES[k]
        v = S.vattabbo(name) if quoted else f"nên gọi là {name}"
        return (f"{Q(f'người {SAMG} {FR[k]} {v}')} {YES} {Q(sam(who, FR[k]))} {YES} "
                f"{Q(f'chính {who} ấy là {name} ấy')} {NO_PE}")

    PAIRS = [(AR, "so"), (AR, "sa"), (AR, "an"), (AN, "so"), (AN, "sa"), (SA, "so")]
    add("5-394", *[called(w, k) for w, k in PAIRS])

    def vit(who, k, kil, comma=False):   # Nanu X Y-phalaṃ vītivatto …; X Y-phalaṃ vītivatto(,) tena samannāgato …
        c = "," if comma else ""
        a = f"{who} đã vượt qua {FR[k]}"
        l1 = f"{Q(sam(who, FR[k]))} {YES} {NANU(a)} {YES} {S.hanci_neg(a, sam(who, FR[k]))}"
        l2 = (f"{Q(f'{a}{c} mà {SAMG} cái ấy')} {YES} "
              f"{Q(f'{who} đã vượt qua {PATH[k]}, đã vượt qua {kil}{c} mà {SAMG} cái ấy')} {NO_PE}")
        return [l1, l2]

    add("5-395", *vit(AR, "so", KIL["so"]), *vit(AR, "sa", KIL["sa"]), *vit(AR, "an", KIL["an"]),
        *vit(AN, "so", KIL["so_s"]), *vit(AN, "sa", KIL["sa"]), *vit(SA, "so", KIL["so_s"]))

    def fruits(who, n, n_path, path_comma=False):
        thesis = sam(who, f"{n} thành quả")
        l1 = f"{S.na_vattabbam(thesis)} {YES} {NANU(got(who, n))} {YES} {S.hanci(got(who, n, comma=False), thesis)}"
        l2 = (f"{S.neu(got(who, n, comma=False), thesis)} {YES} "
              f"{S.neu(got(who, n_path, 'con đường', path_comma), sam(who, f'{n_path} con đường'))} {NO_PE}")
        return l1, l2

    f_ar, f_an, f_sa = fruits(AR, "bốn", "bốn"), fruits(AN, "ba", "ba"), fruits(SA, "hai", "hai", True)
    add("5-396", f_ar[0], f_an[0], f_sa[0], f_ar[1], f_an[1], f_sa[1], S.katha_end(KATHA[4]))

    # ---- (37) 5. Upekkhāsamannāgatakathā -----------------------------------------------------------------------
    heading("5-12-5-0", 4, VAGGA)
    heading("5-12-5-1-0", 5, f"(37) 5. {S.katha(KATHA[5])}")
    T5 = sam(AR, UP6)
    SENSES = ("trong khi thấy hình sắc bằng mắt, thì nghe âm thanh bằng tai, ngửi mùi bằng mũi, nếm vị bằng lưỡi, "
              "chạm vào vật xúc chạm bằng thân, nhận biết đối tượng của ý bằng ý"
              f"{PE} trong khi nhận biết đối tượng của ý bằng ý, thì thấy hình sắc bằng mắt, nghe âm thanh bằng tai, "
              "ngửi mùi bằng mũi, nếm vị bằng lưỡi, chạm vào vật xúc chạm bằng thân")
    CH6 = "có sự bình thản sáu chi phần"                           # chaḷaṅgupekkho
    add("5-397",
        f"{Q(T5)} {YES} {Q(sam(AR, f'sáu sự tiếp xúc, sáu cảm giác, sáu tri giác{PE} sáu trí tuệ'))} {NO_PE}",
        f"{Q(T5)} {YES} Có phải {AR}, {SENSES} không? {NO_PE}",
        f"{Q(T5)} {YES} Có phải thường xuyên, liên tục, liền mạch {SAMG} {UP6}, được kết hợp"
        f"{S.var('Syā.', 'samāhito')}, sáu sự bình thản hiện diện không? {NO_PE}",
        f"{S.na_vattabbam(T5)} {YES} {NANU(f'{AR} {CH6}')} {YES} {S.hanci(f'{AR} {CH6}', T5)[:-1]}{PE}",
        S.katha_end(KATHA[5]))

    # ---- (38) 6. Bodhiyā buddhotikathā -------------------------------------------------------------------------
    heading("5-12-6-0", 4, VAGGA)
    heading("5-12-6-1-0", 5, f"(38) 6. {S.katha(KATHA[6])}")

    def pair(t1, x1, t2, x2, neg=False):
        return f"{Q(f'{bb(t1)}, {by(x1, neg)}')} {YES} {Q(f'{bb(t2)}, {by(x2, neg)}')} {NO_PE}"

    add("5-398",
        f"{Q(BB)} {YES} Có phải khi sự giác ngộ đã chấm dứt, đã mất đi, đã an tịnh, thì trở thành người không giác "
        f"ngộ không? {NO_PE}",
        f"{Q(BB)} {YES} {Q(bb(PAST))} {NO_PE} {q(bb(PAST))} {YES} {Q(by(KAR))} {NO_PE}",
        f"{Q(by(KAR))} {YES} {Q(by(F4))} {NO_PE}",
        f"{Q(BB)} {YES} {Q(bb(FUT))} {NO_PE}",
        f"{Q(bb(FUT))} {YES} {Q(by(KAR))} {NO_PE}",
        f"{Q(by(KAR))} {YES} {Q(by(F4S))} {NO_PE}",
        pair(PRES, KAR, PAST, KAR), pair(PRES, F4, PAST, F4S),
        pair(PRES, KAR, FUT, KAR), pair(PRES, F4S, FUT, F4S),
        pair(PAST, KAR, PRES, KAR, True), pair(PAST, F4S, PRES, F4S, True),
        pair(FUT, KAR, PRES, KAR, True), pair(FUT, F4S, PRES, F4S, True))
    B3 = "là bậc giác ngộ nhờ ba sự giác ngộ"                      # tīhi bodhīhi buddho
    BP = "là bậc giác ngộ nhờ có được sự giác ngộ"                 # bodhipaṭilābhā buddho (termbase)
    add("5-399",
        f"{Q(f'{bb(PAST)}, {bb(FUT)}, {bb(PRES)}')} {YES} {Q(B3)} {NO_PE}",
        f"{Q(B3)} {YES} Có phải thường xuyên, liên tục, liền mạch {SAMG} ba sự giác ngộ, được kết hợp, "
        f"ba sự giác ngộ hiện diện không? {NO_PE}",
        f"{S.na_vattabbam(BB)} {YES} {NANU(BP)} {YES} {S.hanci(BP, BB)}",
        f"{S.neu(BP, BB)} {YES} {Q('việc có được sự giác ngộ là sự giác ngộ')} {NO_PE}",
        S.katha_end(KATHA[6]))

    # ---- (39) 7. Lakkhaṇakathā ---------------------------------------------------------------------------------
    heading("5-12-7-0", 4, VAGGA)
    heading("5-12-7-1-0", 5, f"(39) 7. {S.katha(KATHA[7])}")
    CVQ = f"{CV} được trang bị các tướng, {CV} là {BS}"
    PUBBA = "sự rèn luyện trước đây, sự thực hành trước đây, việc giảng giải Giáo Pháp, việc thuyết giảng Giáo Pháp"
    #   pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā
    add("5-400",
        *[f"{Q(LB)} {YES} {Q(f'người được trang bị {p} các tướng là {p} {BS}')} {NO_PE}"
          for p in ("một phần", "một phần ba", "một nửa")],
        f"{Q(LB)} {YES} {Q(CVQ)} {NO_PE}",
        f"{Q(CVQ)} {YES} {Q(f'{PUBBA} của {BS} như thế nào, thì {PUBBA} của {CV} cũng như thế ấy')} {NO_PE}")
    JB, JC = f"khi {BS} đang ra đời", f"khi {CV} đang ra đời"
    CIT1 = f" [Trường Bộ Kinh 2.27; {CIT['ma. ni.']} 3.205, hỏi sau khi thấy điều đã được nói]"
    RECV = "chư thiên đón nhận trước, loài người sau"
    SPEECH = "– “Thưa hoàng hậu, hãy hài lòng! Người con có uy lực lớn của hoàng hậu đã ra đời”"
    FOUR_G = f"bốn vị thiên tử đón nhận vị ấy rồi đặt trước mặt người mẹ {SPEECH}"

    def water(x):
        return (f"hai dòng nước từ không trung xuất hiện – một dòng lạnh, một dòng nóng – nhờ đó việc dùng nước "
                f"được thực hiện cho {x} và cho người mẹ")

    LION = ("“Ta là bậc hàng đầu của thế gian, Ta là bậc lớn nhất của thế gian, Ta là bậc tối thắng của thế gian, "
            "đây là lần sinh cuối cùng, giờ đây không có sự hiện hữu mới”")

    def born(x):
        return (f"{x} vừa mới sinh ra, đứng vững trên đôi bàn chân đặt ngang nhau, hướng mặt về phương bắc, đi bảy "
                f"bước trong khi chiếc lọng trắng được che theo, nhìn quanh tất cả các phương, và nói ra lời nói hùng dũng "
                f"– {LION}")

    LIGHT = "có sự xuất hiện của ánh sáng lớn, của hào quang lớn, của sự rung chuyển mặt đất lớn"
    add("5-401",
        yatha(f"{JB}, {RECV}{CIT1}", f"{JC}, {RECV}"),
        yatha(f"{JB}, {FOUR_G}", f"{JC}, {FOUR_G}"),
        yatha(f"{JB}, {water(BS)}", f"{JC}, {water(CV)}"),
        yatha(born(BS), born(CV)),
        yatha(f"{JB}, {LIGHT}", f"{JC}, {LIGHT}"),
        yatha(f"thân bình thường của {BS} tỏa sáng một sải tay xung quanh",
              f"thân bình thường của {CV} tỏa sáng một sải tay xung quanh"),
        yatha(f"{BS} thấy giấc mộng lớn", f"{CV} thấy giấc mộng lớn"))
    SUT = ("Này các tỳ-khưu, đây là ba mươi hai tướng đại nhân của bậc đại nhân, bậc đại nhân được trang bị những "
           "tướng ấy chỉ có hai hướng đi, không có hướng khác" + S.var_sp("Ka.", "na aññā") + "! Nếu sống đời gia "
           "đình, vị ấy trở thành vua chuyển luân, theo lẽ phải, vị vua của lẽ phải, làm chủ bốn phương, người chiến "
           "thắng, đã đạt đến sự ổn định của vùng đất, được trang bị bảy báu vật. Vị ấy có bảy báu vật này, tức là – "
           "báu vật bánh xe, báu vật voi, báu vật ngựa đực, báu vật ngọc, báu vật người nữ, báu vật gia chủ, và chính "
           "báu vật vị cố vấn là thứ bảy. Vị ấy có hơn một nghìn người con, can đảm, có thân hình của bậc anh hùng, "
           "đánh tan quân địch. Vị ấy chinh phục trái đất này đến tận biển cả, không dùng gậy, không dùng dao kiếm, "
           "bằng lẽ phải, rồi sống ở đó. Còn nếu từ gia đình xuất gia vào đời không gia đình, vị ấy trở thành bậc "
           "A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn, người đã vén bức màn che ở thế gian")
    add("5-402",
        f"{S.na_vattabbam(LB)} {YES} {S.NANU_VUTTAM} “{SUT}” [Trường Bộ Kinh 3.200]. {S.ATTHEVA} {YES} "
        f"{S.tena_hi(LB)}",
        S.katha_end(KATHA[7]))

    # ---- (40) 8. Niyāmokkantikathā -----------------------------------------------------------------------------
    heading("5-12-8-0", 4, VAGGA)
    heading("5-12-8-1-0", 5, f"(40) 8. {S.katha(KATHA[8])}")
    SAV_K = f"{BS} là vị đệ tử của {KAS}"
    SAV_B = "là vị đệ tử rồi trở thành Đức Phật"                    # sāvako hutvā buddho hoti
    ANUS = "là người hiểu biết nhờ nghe từ người khác"              # anussaviyo (termbase)
    SAYAM = "Đức Thế Tôn là bậc tự mình giác ngộ"                   # bhagavā sayambhū (termbase)
    B_3 = "dưới gốc cây Bồ-đề, Đức Thế Tôn đã giác ngộ hoàn toàn chỉ ba thành quả của đời sống sa-môn"
    B_4 = "dưới gốc cây Bồ-đề, Đức Thế Tôn đã giác ngộ hoàn toàn bốn thành quả của đời sống sa-môn"
    add("5-403",
        f"Có phải {OK} [{CIT['ma. ni.']} 2.282, hỏi dựa vào Kinh Ghá-ti-ka-ra] không? {YES} {Q(SAV_K)} {NO_PE}",
        f"{Q(SAV_K)} {YES} {Q(SAV_B)} {NO_PE}",
        f"{Q(SAV_B)} {YES} {Q(ANUS)} {NO_PE}",
        f"{Q(ANUS)} {YES} {NANU(SAYAM)} {YES} {S.hanci_neg(SAYAM, ANUS)}",
        f"{Q(OK)} {YES} {Q(B_3)} {NO_PE}",
        f"{NANU(B_4)} {YES} {S.hanci_neg(B_4, OK)}")
    DS = "người thành tựu về sự thấy"                                # dassanasampanno puggalo (termbase)
    ANAN = f"tôn giả A-nan {OKC} trong lời dạy của Đức Thế Tôn"
    CITTA_N = "gia chủ Chít-ta, Hát-tha-ka người xứ A-la-vi"        # citto gahapati hatthako āḷavako (termbase)
    CITTA = f"{CITTA_N} {OKC} trong lời dạy của Đức Thế Tôn"
    NSK = f"{OK}, nhưng không phải là vị đệ tử của {KAS}"
    NSB = "nhưng không phải là vị đệ tử của Đức Thế Tôn"
    add("5-404",
        f"{Q(OK)} {YES} {Q(f'{BS} đã làm việc khổ hạnh khó làm')} {YES} {Q(f'{DS} có thể làm việc khổ hạnh khó làm')} "
        f"{NO_PE}",
        f"Có phải {BS} đã làm khổ hạnh khác{S.var(CIT['saṃ. ni.'] + ' 1.137', 'amaraṃ tapaṃ')}, đã tôn xưng một vị "
        f"khác làm bậc đạo sư không? {YES} {Q(f'{DS} có thể tôn xưng một vị khác làm bậc đạo sư')} {NO_PE}",
        f"{Q(f'{ANAN}, tôn giả A-nan là vị đệ tử của Đức Thế Tôn')} {YES} {Q(f'{OK}, {SAV_K}')} {NO_PE}",
        f"{Q(f'{CITTA}, {CITTA_N} là vị đệ tử của Đức Thế Tôn')} {YES} {Q(f'{OK}, {SAV_K}')} {NO_PE}",
        f"{Q(NSK)} {YES} {Q(f'{ANAN}, {NSB}')} {NO_PE}",
        f"{Q(NSK)} {YES} {Q(f'{CITTA}, {NSB}')} {NO_PE}",
        f"{Q(NSK)} {YES} {Q('vị đệ tử, khi đã vượt qua lần sinh, trở thành người không phải là vị đệ tử')} {NO_PE}")
    ME = "nơi Ta, này các tỳ-khưu"                                   # me, bhikkhave
    ANS_ = "trong những điều chưa từng được nghe trước đây"          # pubbe ananussutesu dhammesu (pi-4)
    ARISE = (f"{ANS_}, con mắt đã sinh khởi, hiểu biết đã sinh khởi, trí tuệ đã sinh khởi, hiểu biết chân thật đã "
             f"sinh khởi, ánh sáng đã sinh khởi")
    #   cakkhuṃ udapādi, ñāṇaṃ udapādi, paññā udapādi, vijjā udapādi, āloko udapādi
    ARISE_S = f"{ANS_}, con mắt đã sinh khởi{PE} ánh sáng đã sinh khởi"
    VS = FOUR_TRUTHS["s"].replace("khổ đau", "khổ đau" + S.var_sp("Syā., Kaṃ.", "dukkhasamudayo"))
    VN = FOUR_TRUTHS["n"] + S.var_sp("Syā., Kaṃ.", "dukkhanirodho")
    WHEEL = (f"“‘Đây là {FOUR_TRUTHS['d']}’, {ME}, {ARISE}. "
             f"‘{cap(FOUR_TRUTHS['d'])} ấy cần được hiểu biết trọn vẹn’, {ME}{PE} "
             f"đã được hiểu biết trọn vẹn, {ME}, {ARISE_S}. "
             f"‘Đây là {FOUR_TRUTHS['s']}’, {ME}{PE} "
             f"‘{VS} ấy cần dứt bỏ’, {ME}{PE} "
             f"đã được dứt bỏ, {ME}{PE} "
             f"‘đây là {VN}’, {ME}{PE} "
             f"‘{FOUR_TRUTHS['n']} ấy cần được tự mình chứng nghiệm’, {ME}{PE} "
             f"đã được tự mình chứng nghiệm, {ME}{PE} "
             f"‘đây là {FOUR_TRUTHS['m']}’, {ME}{PE} "
             f"‘{FOUR_TRUTHS['m']} ấy cần được tu tập’, {ME}{PE} "
             f"đã được tu tập, {ME}, {ARISE}” [Đại Phẩm 15; {CIT['saṃ. ni.']} 5.1081; Phân Tích Đạo 2.30].")
    add("5-405",
        f"{S.na_vattabbam(OK)} {YES} {S.NANU_VUTTAM} “Này A-nan, nơi {KAS}, Ta đã sống đời sống tu hành trong sạch "
        f"vì sự giác ngộ trọn vẹn trong tương lai”! {S.ATTHEVA} {YES} {S.tena_hi_na(OK)}",
        f"{Q(OK)} {YES} {S.NANU_VUTTAM}",
        "“Ta là bậc chiến thắng tất cả, bậc hiểu biết tất cả,",
        "Không bị vấy bẩn bởi tất cả các hiện tượng;",
        "Đã dứt bỏ tất cả, được giải thoát trong sự diệt tận khao khát,",
        "Tự mình, sau khi hiểu biết trực tiếp, Ta sẽ tôn xưng ai.",
        "“Ta không có thầy, không có người giống như Ta;",
        "Trong thế gian cùng với chư thiên, không có ai sánh ngang với Ta.",
        "“Thật vậy, Ta là bậc A-la-hán ở thế gian, Ta là bậc đạo sư không có ai cao hơn;",
        "Ta là bậc Tự Giác Ngộ Hoàn Toàn duy nhất, Ta đã trở nên mát mẻ, đã lắng dịu.",
        "“Để chuyển bánh xe Giáo Pháp, Ta đi đến thành của xứ Ca-thi;",
        "Trong thế gian đã trở nên mù lòa" + S.var_sp("Sī., Syā., Kaṃ., Pī.", "andhabhūtasmiṃ") + ", Ta sẽ đánh"
        + S.var("Ka.", "āhaññiṃ") + " tiếng trống của điều bất tử”" + S.var_sp("Ka.", "dudrabhinti") + ".",
        "“Này hiền giả, theo như hiền giả tự nhận, hiền giả có xứng đáng là bậc chiến thắng vô biên không”?",
        "“Quả thật, những người như Ta là những bậc chiến thắng, những người đã đạt đến sự diệt tận ô nhiễm;",
        "Các hiện tượng xấu ác đã bị Ta chiến thắng, vì vậy, này U-pa-ka, Ta là bậc chiến thắng” "
        f"[Đại Phẩm 11; {CIT['ma. ni.']} 1.285; 2.341].",
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(OK)}",
        f"{Q(OK)} {YES} {S.NANU_VUTTAM} {WHEEL} {S.ATTHEVA} {YES} {S.tena_hi_na(OK)}",
        S.katha_end(KATHA[8]))

    # ---- (41) 9. Aparāpi samannāgatakathā ----------------------------------------------------------------------
    heading("5-12-9-0", 4, VAGGA)
    heading("5-12-9-1-0", 5, f"(41) 9. {H9}")
    add("5-406",
        f"{Q(sam(PA, 'ba thành quả'))} {YES} {Q(sam(PA, full10('bốn')))} {NO_PE}",
        f"{Q(sam(PN, 'hai thành quả'))} {YES} {Q(sam(PN, short10b('ba')))} {NO_PE}",
        f"{Q(sam(PS, FR['so']))} {YES} {Q(sam(PS, short10b('hai')))} {NO_PE}",
        f"{Q(sam(PA, FR['so']))} {YES} {Q(is_(PA, SO_TYPES))} {NO_PE}",
        f"{Q(sam(PA, FR['sa']))} {YES} {Q(is_(PA, SA))} {NO_PE}",
        f"{Q(sam(PA, FR['an']))} {YES} {Q(is_(PA, AN_TYPES))} {NO_PE}",
        f"{Q(sam(PN, FR['so']))} {YES} {Q(is_(PN, SO_TYPES))} {NO_PE}",
        f"{Q(sam(PN, FR['sa']))} {YES} {Q(is_(PN, SA))} {NO_PE}",
        f"{Q(sam(PS, FR['so']))} {YES} {Q(is_(PS, SO_TYPES))} {NO_PE}")
    PAIRS9 = [(PA, "so"), (PA, "sa"), (PA, "an"), (PN, "so"), (PN, "sa"), (PS, "so")]
    add("5-407", *[called(w, k, quoted=False) for w, k in PAIRS9])
    add("5-408", *vit(PA, "so", KIL["so"], True), *vit(PA, "sa", KIL["sa"], True), *vit(PA, "an", KIL["an"], True))
    add("5-409", *vit(PN, "so", KIL["so_s"], True), *vit(PN, "sa", KIL["sa"], True))
    add("5-410", *vit(PS, "so", KIL["so_s"], True))

    def fruits9(who, n, thesis_obj, n_path, one=False):
        thesis = sam(who, thesis_obj)
        g, g0 = got(who, n, one=one), got(who, n, comma=False, one=one)
        if one:
            g = f"{who} đã có được {FR['so']}, và không sa sút khỏi nó"
            g0 = f"{who} đã có được {FR['so']} và không sa sút khỏi nó"
        l1 = f"{S.na_vattabbam(thesis)} {YES} {NANU(g)} {YES} {S.hanci(g0, thesis)}"
        l2 = (f"{S.neu(g0, thesis)} {YES} "
              f"{S.neu(got(who, n_path, 'con đường', False), sam(who, f'{n_path} con đường'))} {NO_PE}")
        return l1, l2

    g_pa = fruits9(PA, "ba", "ba thành quả", "bốn")
    g_pn = fruits9(PN, "hai", "hai thành quả", "ba")
    g_ps = fruits9(PS, "", FR["so"], "hai", one=True)
    add("5-411", g_pa[0], g_pn[0], g_ps[0])
    add("5-412", g_pa[1], g_pn[1], g_ps[1], END9)

    # ---- (42) 10. Sabbasaṃyojanappahānakathā ------------------------------------------------------------------
    heading("5-12-10-0", 4, VAGGA)
    heading("5-12-10-1-0", 5, f"(42) 10. {S.katha(KATHA[10])}")
    AM = "con đường A-la-hán"                                        # arahattamaggena (termbase)
    ALLP = f"tất cả các xiềng xích được dứt bỏ bằng {AM}"           # arahattamaggena sabbe saṃyojanā pahīyanti

    def pj(x):                      # arahattamaggena X pajahati (ch4 «dứt bỏ X bằng con đường …»)
        return f"dứt bỏ {x} bằng {AM}"

    V1 = f"{VUTTAM_RANG} sự dứt bỏ ba xiềng xích là {FR['so']}"
    #   tiṇṇaṃ saṃyojanānaṃ pahānaṃ sotāpattiphalaṃ vuttaṃ bhagavatā
    V2 = f"{VUTTAM_RANG} sự suy yếu của sự tham đắm dục lạc và ác ý là {FR['sa']}"
    #   kāmarāgabyāpādānaṃ tanubhāvaṃ sakadāgāmiphalaṃ …
    V3 = f"{VUTTAM_RANG} sự dứt bỏ sự tham đắm dục lạc và ác ý không còn sót lại là {FR['an']}"
    #   kāmarāgabyāpādānaṃ anavasesappahānaṃ anāgāmiphalaṃ …
    V4 = (f"{VUTTAM_RANG} sự dứt bỏ sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao "
          f"động và vô minh không còn sót lại là {ARAHATTA}")
    #   rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānaṃ arahattaṃ … (pi-4 list)
    add("5-413",
        f"{Q(TH10)} {YES} {Q(ALLP)} {NO_PE}",
        f"{Q(ALLP)} {YES} {Q(pj(FETTERS3))} {NO_PE}",
        f"{Q(pj(FETTERS3))} {YES} {NANU(V1)} {YES} {S.hanci_neg(V1, ALLP)}")
    add("5-414", f"{Q(ALLP)} {YES} {Q(pj(OLARIKA))} {NO_PE}")
    add("5-415",
        f"{Q(pj(OLARIKA))} {YES} {NANU(V2)} {YES} {S.hanci_neg(V2, ALLP)}",
        f"{Q(ALLP)} {YES} {Q(pj(ANUSAH))} {NO_PE}")
    add("5-416",
        f"{Q(pj(ANUSAH))} {YES} {NANU(V3)} {YES} {S.hanci_neg(V3, ALLP)}",
        f"{Q(ALLP)} {YES} {NANU(V4)} {YES} {S.hanci_neg(V4, ALLP)}")
    ALLH = f"tất cả các xiềng xích của {AR} {PAHINA}"               # arahato sabbe saṃyojanā pahīnā
    add("5-417",
        f"{S.na_vattabbam(TH10)} {YES} {NANU(ALLH)} {YES} {S.hanci(ALLH, TH10)}",
        S.katha_end(KATHA[10]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


def main():
    check_strings()
    S.check_reused()
    segs = build()
    # S.quotes_ok counts a stanza re-opening “ by raw totals, so the NEW quote that opens ^5-405 at «“Này hiền giả»
    # (after the closed four-stanza verse) is miscounted; run the same per-line checks with ^5-405 split there
    # (the flat line list is unchanged), then write as S.write does.
    k = next(i for i, s in enumerate(segs) if s[-1].endswith("^5-405"))
    seg = segs[k]
    cut = next(i for i, ln in enumerate(seg) if ln.startswith("“Này hiền giả"))
    S.check_against_pali(NAME, segs[:k] + [seg[:cut], seg[cut:]] + segs[k + 1:])
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-12"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
