"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 28, Vīsatimavaggo (^5-28-0 … ^5-877): six kathās
(194-199) with the repeated "Vīsatimavaggo" sub-headings, the vagga close, the uddāna and the fourth fifty-group
close (Catuttho paṇṇāsako. / Tassuddānaṃ – / its uddāna; frame set in ch13, the Tassuddānaṃ rule of ch18).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/28-visatimavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, var_sp, var …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED28); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-28.md.

usage: python -I -X utf8 -B build_rails_28_vi.py          (writes the chapter and the adherence copy rails\\adh-28\\)
       python -I -X utf8 -B build_rails_28_vi.py --find <regex> [max] [chars]   (look up finished pi-5 rails chapters)
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "28-visatimavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, RE, CIT = S.cap, S.RE, S.CIT
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
FINISHED = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
            "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
            "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
            "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
            "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md", "19-ekadasamavaggo.md",
            "20-dvadasamavaggo.md", "21-terasamavaggo.md", "22-cuddasamavaggo.md", "23-pannarasamavaggo.md"]


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case; ch15, ch23)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH = "Này các tỳ-khưu"                                                  # bhikkhave (sample)
BHL = "này các tỳ-khưu"
NO_HAVE = "Không có."                                                   # Natthi. (ch12, ch14)
ATTH_L = "có bài kinh như vậy thật không?"                              # "…"ti – attheva suttantoti? (ch14)
ATTH_HANCI = "có bài kinh như vậy thật"                                 # Hañci "…"ti – attheva suttanto, (ch14)
TATHAGATA = "Như Lai"                                                   # tathāgata (ch20)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close, fifty-group close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ hai mươi"                                           # Vīsatimavaggo (termbase)
KATHA = {1: "việc không cố ý", 2: "hiểu biết", 3: "những kẻ canh giữ địa ngục", 4: "loài súc sinh",
         5: "con đường", 6: "hiểu biết"}
#   Asañcicca- (termbase asañcicca «không cố ý»), Ñāṇa- (termbase ñāṇakathā, = ch19), Nirayapālakathā (termbase),
#   Tiracchāna- (termbase tiracchāna / tiracchānagata «loài súc sinh»), Magga- (termbase magga «con đường»)
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9; after the vagga close)
CATUTTHO = "Nhóm năm mươi thứ tư."                                      # Catuttho paṇṇāsako. (ch13 frame)
TASS50 = "Tóm tắt của nhóm này –"                                       # Tassuddānaṃ – after a fifty-group close (ch18)

# ---- 1. Asañcicca ---------------------------------------------------------------------------------------------
AN = "người tạo nghiệp có quả không gián đoạn"                          # ānantariko (termbase)
MOTHER = "tước đoạt mạng sống của mẹ"                                   # mātaraṃ jīvitā voropetvā (termbase, ch20)


def asan(act, who, neg=False, cetana="không cố ý"):     # (A)sañcicca X-tvā Y (na) hoti
    return f"{cetana} {act} thì {'không ' if neg else ''}trở thành {who}"


A_MOTHER = asan(MOTHER, AN)                                             # Asañcicca mātaraṃ … ānantariko hoti
A_MOTHER_N = asan(MOTHER, AN, True)
S_MOTHER = asan(MOTHER, AN, cetana="cố ý")                              # Sañcicca mātaraṃ … ānantariko hoti
KILL = "sát hại sinh mạng"                                              # pāṇaṃ hantvā / pāṇātipātī (termbase, pi-4)
A_KILL = asan(KILL, f"người {KILL}")                                    # Asañcicca pāṇaṃ hantvā pāṇātipātī hoti
A_KILL_N = asan(KILL, f"người {KILL}", True)
THEFT = "không cố ý lấy của không được cho"                             # asañcicca adinnaṃ ādiyitvā (pi-4 adinnādāyī)
LIE = "nói dối thì trở thành người nói dối"                             # musā bhaṇitvā musāvādī hoti (pi-4 musāvādī)
LIE_N = "nói dối thì không trở thành người nói dối"

KILLERS = [("kẻ giết mẹ", "mẹ bị tước đoạt mạng sống"),                # mātughātako / mātā jīvitā voropitā (ch20)
           ("kẻ giết cha", "cha bị tước đoạt mạng sống"),               # pitughātako / pitā … voropito
           ("kẻ giết bậc A-la-hán", "bậc A-la-hán bị tước đoạt mạng sống"),   # arahantaghātako / arahā …
           ("kẻ làm chảy máu", f"máu của {TATHAGATA} bị làm cho chảy")]    # ruhiruppādako / tathāgatassa lohitaṃ uppāditaṃ
SB = "kẻ chia rẽ Tăng đoàn"                                             # saṅghabhedako (termbase, ch10, ch21)
SBS = "những kẻ chia rẽ Tăng đoàn"                                      # saṅghabhedakā
DSB = f"{SB} với tri giác rằng đó là Giáo Pháp"                         # dhammasaññī saṅghabhedako (termbase)
UPALI = "Ưu-ba-li"                                                      # Upāli (not in the termbase; see notes)
KT = "tồn tại suốt một kiếp"                                            # kappaṭṭho (ch21)
UPALI_SUT = (f"“Này {UPALI}, có {SB} thuộc cõi khổ, là chúng sinh địa ngục, {KT}, không thể cứu chữa; "
             f"này {UPALI}, có {SB} không thuộc cõi khổ, không phải là chúng sinh địa ngục, không {KT}, "
             f"không phải là không thể cứu chữa”!")
#   atthupāli, saṅghabhedako āpāyiko nerayiko kappaṭṭho atekiccho; atthupāli, saṅghabhedako na āpāyiko na nerayiko
#   na kappaṭṭho na atekiccho"ti! (termbase Āpāyiko, nerayiko, atekiccho; ch21 verse wording)
VERSE_SB = [f"“{cap(SB)} thuộc cõi khổ, là chúng sinh địa ngục, {KT};",                         # (ch21)
            "Ưa thích bè phái, đứng vững trong điều trái Giáo Pháp, rơi khỏi sự an ổn thoát khỏi các ách;",
            "Sau khi chia rẽ Tăng đoàn đang hòa hợp, bị nung đốt trong địa ngục suốt một kiếp” "
            "[Tiểu Phẩm 354; Tăng Chi Bộ Kinh 10.39; Kinh Phật Thuyết Như Vậy 18]."]

# ---- 2. Ñāṇa (puthujjana) ---------------------------------------------------------------------------------------
PJ = "người phàm phu"                                                   # puthujjano / puthujjanassa (termbase)
NO_NANA = f"{PJ} không có hiểu biết"                                    # natthi puthujjanassa ñāṇaṃ
HAS_NANA = f"{PJ} có hiểu biết"                                         # atthi puthujjanassa ñāṇaṃ
PANNA = ["trí tuệ", "sự hiểu rõ", "sự tìm hiểu", "sự tìm hiểu kỹ", "sự tìm hiểu các hiện tượng", "sự nhận xét",
         "sự nhận diện", "sự nhận diện chính xác"]                      # paññā … paccupalakkhaṇā (pi-1 ^1-16)
PANNA_F = ", ".join(PANNA)
PANNA_PE = f"{PANNA[0]}, {PANNA[1]}, {PANNA[2]}{PE} {PANNA[-1]}"         # paññā pajānanā vicayo…pe… paccupalakkhaṇā
ARUPA = ["lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả",
         "lĩnh vực không phải tri giác cũng không phải không tri giác"]  # ākāsānañcāyatana … (pi-2 ^2-508)
GIFTS = ["y phục", "đồ ăn khất thực", "chỗ ở", "thuốc men và vật dụng chữa bệnh"]   # cīvara … (ch21, pi-2)
FOUR = ("hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng nghiệm sự chấm dứt, tu tập con đường")
#   dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti (ch5)

# ---- 3. Nirayapāla ----------------------------------------------------------------------------------------------
NP = "những kẻ canh giữ địa ngục"                                       # nirayapālā (termbase)
INN = "trong các địa ngục"                                              # nirayesu (termbase)
KK = "các hình phạt"                                                    # kammakāraṇā (termbase)
KAR = "những người thi hành hình phạt"                                  # kāraṇikā (APPROVED split, torture)
MAN = "giữa loài người"                                                 # manussesu (termbase)


def has(where, what, neg=False):    # (n)atthi WHERE WHAT
    return f"{where} {'không ' if neg else ''}có {what}"


def kk_k(where, neg=False):         # atthi WHERE kammakāraṇā, (n)atthi ca kāraṇikā
    return f"{has(where, KK)}, và {'không ' if neg else ''}có {KAR}"


VERSE_N = ["“Không phải Tỳ-xá-phù, cũng không phải vua ngạ quỷ,",
           "Sô-ma, Diêm-ma và vua Tỳ-sa-môn;",
           "Ở đó, chính các nghiệp của mình đánh đập người bị đẩy đi từ đây"
           + S.var_sp("Syā., Ka.", "paṇuṇṇaṃ")[:-1] + "; (Sī.): panunnaṃ], đã đến thế gian khác”."]
#   Na vessabhū nopi ca pettirājā, / Somo yamo vessavaṇo ca rājā; / Sakāni kammāni hananti tattha, ito paṇunnaṃ
#   [paṇuṇṇaṃ (syā. ka.), panunnaṃ (sī.)] paralokapatta"nti. (Soma, Yama: APPROVED names; Vessabhū, Vessavaṇa: notes)
HIM = "người ấy"                                                        # tamenaṃ / so
FIRE = "đang bốc cháy, rực lửa, cháy sáng"                              # ādittāya sampajjalitāya sajotibhūtāya (termbase)
SPIKE = "cây cọc sắt nung đỏ"                                           # tattaṃ ayokhīlaṃ (termbase)
PAIN = f"ở đó, {HIM} cảm nhận những cảm giác khó chịu, dữ dội, cay đắng"  # so tattha dukkhā tibbā kaṭukā vedanā vedeti
UNTIL = f"{HIM} chưa qua đời chừng nào nghiệp xấu ác ấy chưa chấm dứt"   # na ca tāva kālaṃ karoti yāva na taṃ pāpakammaṃ byantīhoti
CIT_DD = f"{CIT['ma. ni.']} 3.250; {CIT['a. ni.']} 3.36"                 # ma. ni. 3.250; a. ni. 3.36
SUT_5 = (f"“{BH}, {NP} bắt {HIM} chịu hình phạt có tên là sự trói buộc năm cách{S.var(CIT_DD, 'karonti')} – "
         f"chúng đóng {SPIKE} vào bàn tay, đóng {SPIKE} vào bàn tay thứ hai, đóng {SPIKE} vào bàn chân, "
         f"đóng {SPIKE} vào bàn chân thứ hai, đóng {SPIKE} vào giữa ngực; {PAIN}; và {UNTIL}” [{CIT_DD}]!")
SUT_HELL = (f"“{BH}, {NP} đặt {HIM} nằm xuống rồi đẽo bằng búa{S.var_sp('Mọi bản', 'kudhārīhi')}{PE} "
            f"{BHL}, {NP} dựng {HIM} chân lên trên, đầu xuống dưới rồi đẽo bằng rìu{PE} "
            f"{BHL}, {NP} buộc {HIM} vào xe rồi bắt chạy tới và chạy lui trên mặt đất {FIRE}"
            f"{S.var_sp('Syā.', 'sañjotibhūtāya')}{PE} "
            f"{BHL}, {NP} bắt {HIM} leo lên và leo xuống một ngọn núi than hồng lớn {FIRE}{PE} "
            f"{BHL}, {NP} nắm {HIM} chân lên trên, đầu xuống dưới rồi ném vào chum đồng nung đỏ {FIRE}. "
            f"Ở đó, {HIM} bị nung đốt sùng sục bọt; ở đó, {HIM} trong khi bị nung đốt sùng sục bọt, có lúc đi lên "
            f"trên, có lúc đi xuống dưới, có lúc đi ngang. {cap(PAIN)}, và {UNTIL}. "
            f"{BH}, {NP} ném {HIM} vào đại địa ngục! {BH}, còn đại địa ngục ấy –")
VERSE_HELL = ["“Có bốn góc, bốn cửa, được phân chia, được đo theo từng phần;",
              "Được bao quanh bằng tường sắt, được che phủ bằng sắt.",
              "“Mặt đất của nó làm bằng sắt, cháy rực, đầy sức nóng;",
              f"Tỏa ra khắp một trăm do-tuần, duy trì vào mọi lúc” [{CIT_DD}; Ngạ Quỷ Sự 71]."]
#   Catukkaṇṇo catudvāro, vibhatto bhāgaso mito; / Ayopākārapariyanto, ayasā paṭikujjito. / "Tassa ayomayā bhūmi,
#   jalitā tejasā yutā; / Samantā yojanasataṃ, pharitvā tiṭṭhati sabbadā"ti (termbase kaṇṇo «góc», dvāro «cửa»,
#   vibhatto, mito, bhāgaso, pariyanto, pākāra, paṭikujjito, bhūmi, tejasā, yojana, pharitvā, tiṭṭhati «duy trì»,
#   Sabbadā «vào mọi lúc»; pe. va. «Ngạ Quỷ Sự» ch15)

# ---- 4. Tiracchāna ----------------------------------------------------------------------------------------------
DEV = "giữa chư thiên"                                                  # devesu (ch3)
TG = "loài súc sinh"                                                    # tiracchānagatā (termbase, ch1)
IN_DEV = has(DEV, TG)                                                   # atthi devesu tiracchānagatā
IN_DEV_N = has(DEV, TG, True)
CREATURES = (f"ở đó có sâu bọ, châu chấu, muỗi, ruồi, rắn, bọ cạp, rết, giun đất"
             f"{S.var_sp('Syā., Kaṃ., Pī.', 'gaṇḍupādāti')}")           # kīṭā … gaṇḍuppādā (termbase)
ERAVANA = "ở đó có con voi chúa có tên là Ê-ra-va-na, là xe cộ cõi trời được thắng một nghìn con"
#   atthi tattha erāvaṇo nāma hatthināgo sahassayuttaṃ dibbaṃ yānaṃ (termbase hatthināgo, Dibbaṃ, yānaṃ, sahassa,
#   yuttaṃ; Erāvaṇa: notes)
KEEPERS = (f"ở đó có người giữ voi, người giữ ngựa đực{S.var('?', 'hatthibhaṇḍā assabhaṇḍā')}, người cung cấp cỏ, "
           f"người huấn luyện, người nấu thức ăn")
#   hatthibandhā assabandhā yāvasikā kāraṇikā bhattakārakā (termbase hatthi, assa «ngựa đực», bandhā «người giữ»,
#   yāvasikā, kāraṇikā «người huấn luyện» (APPROVED split), bhattakārakā)

# ---- 5. Magga ---------------------------------------------------------------------------------------------------
M8 = "con đường gồm tám chi phần"                                       # aṭṭhaṅgiko maggo (termbase)
M5 = "con đường gồm năm chi phần"                                       # pañcaṅgiko maggo (termbase)
AM8 = "con đường gồm tám chi phần cao quý"                              # ariyo aṭṭhaṅgiko maggo (termbase, pi-2 ^2-486)
SAMMA = dict(zip(["diṭṭhi", "saṅkappa", "vācā", "kammanta", "ājīva", "vāyāma", "sati", "samādhi"], S.SAMMA))
MA = "chi phần của con đường"                                           # maggaṅgaṃ (pi-1, ch23)


def ma(x, neg=False):               # X maggaṅgaṃ, sā / so ca (na) maggo
    return f"{x} là {MA}, và nó {'không phải là' if neg else 'là'} con đường"


def pe_join(*keys):                 # X…pe… Y…pe… Z
    return f"{PE} ".join(SAMMA[k] for k in keys)


VERSE_M = ["“Trong các con đường, con đường gồm tám chi phần là bậc tối thắng, trong các sự thật, bốn câu;",
           "Trong các hiện tượng, sự lìa tham là bậc tối thắng, trong loài hai chân, bậc có mắt” "
           "[Kinh Pháp Cú 273, trong Kinh Pháp Cú]."]
#   Maggānaṃ aṭṭhaṅgiko seṭṭho, saccānaṃ caturo padā; / Virāgo seṭṭho dhammānaṃ, dvipadānañca cakkhumā"ti
#   (termbase seṭṭho «bậc tối thắng», kept also of a path / a state, see notes; padā «câu»; Virāgo «sự lìa tham»;
#   dvipadānaṃ «loài hai chân»; cakkhumā «có mắt»; «…, trong Kinh Pháp Cú» ch10)
PUBBE = (f"“Ngay từ trước đây, nghiệp bằng thân, nghiệp bằng lời nói và sinh kế của người ấy đã hoàn toàn thanh tịnh; "
         f"như vậy, {AM8} này của người ấy đi đến sự viên mãn của việc tu tập” [{CIT['ma. ni.']} 3.431]!")
#   pubbeva kho panassa kāyakammaṃ vacīkammaṃ ājīvo suparisuddho hoti; evamassāyaṃ ariyo aṭṭhaṅgiko maggo
#   bhāvanāpāripūriṃ gacchatī"ti (termbase Kāyakammaṃ, vacīkammaṃ, ājīvo, parisuddho, pāripūriṃ, gacchati, bhāvanā)
SUBH = "Tu-bạt-đà-la"                                                   # subhadda (APPROVED)
DV = "trong Giáo Pháp và Giới Luật"                                     # dhammavinaye (ch10)
SAM = ["sa-môn", "sa-môn thứ hai", "sa-môn thứ ba", "sa-môn thứ tư"]    # samaṇo, dutiyo … catuttho samaṇo (termbase)
SUBH_SUT = (f"“Này {SUBH}, {DV} nào mà {AM8} không được tìm thấy, thì ở đó {SAM[0]} cũng không được tìm thấy, "
            + ", ".join(f"ở đó {x} cũng không được tìm thấy" for x in SAM[1:]) + ". "
            f"Và này {SUBH}, {DV} nào mà {AM8} được tìm thấy, thì ở đó {SAM[0]} cũng được tìm thấy, "
            f"{SAM[1]} cũng{PE} {SAM[2]} cũng{PE} ở đó {SAM[3]} cũng được tìm thấy. "
            f"Này {SUBH}, {DV} này, {AM8} được tìm thấy. "
            f"Này {SUBH}, chính ở đây có {SAM[0]}, " + ", ".join(f"ở đây có {x}" for x in SAM[1:]) + ". "
            f"Các học thuyết của người khác trống rỗng, không có sa-môn nào khác” [Trường Bộ Kinh 2.214]!")
#   yasmiṃ kho, subhadda, dhammavinaye … Suññā parappavādā samaṇebhi aññehī"ti (termbase upalabbhati «được tìm
#   thấy», pavādā «học thuyết», para «người khác», Suññā «trống rỗng»)

# ---- 6. Ñāṇa (twelve modes) -------------------------------------------------------------------------------------
D12 = "hiểu biết có mười hai chủ đề là vượt thế gian"                   # dvādasavatthukaṃ ñāṇaṃ lokuttaraṃ (termbase)


def twelve(x):                      # dvādasa X
    return f"có mười hai {x}"


NANA_SUT = ("“‘Đây là sự thật cao quý về khổ đau’, nơi Ta, này các tỳ-khưu, trong những điều chưa từng được nghe "
            "trước đây, con mắt đã sinh khởi, hiểu biết đã sinh khởi, trí tuệ đã sinh khởi, hiểu biết chân thật đã "
            "sinh khởi, ánh sáng đã sinh khởi. ‘Sự thật cao quý về khổ đau ấy cần được hiểu biết trọn vẹn’, nơi Ta, "
            f"này các tỳ-khưu{PE} đã được hiểu biết trọn vẹn, nơi Ta, này các tỳ-khưu{PE} "
            "‘đây là sự thật cao quý về sự phát sinh của khổ đau"
            + S.var_sp("Syā., Kaṃ., Pī.", "dukkhasamudayo") + f"’, nơi Ta, này các tỳ-khưu{PE} "
            f"‘sự thật cao quý về sự phát sinh của khổ đau ấy cần dứt bỏ’, nơi Ta, này các tỳ-khưu{PE} "
            f"đã được dứt bỏ, nơi Ta, này các tỳ-khưu{PE} "
            "‘đây là sự thật cao quý về sự chấm dứt khổ đau"
            + S.var_sp("Syā., Kaṃ., Pī.", "dukkhanirodhā") + f"’, nơi Ta, này các tỳ-khưu{PE} "
            f"‘sự thật cao quý về sự chấm dứt khổ đau ấy cần được tự mình chứng nghiệm’, nơi Ta, này các tỳ-khưu{PE} "
            f"đã được tự mình chứng nghiệm, nơi Ta, này các tỳ-khưu{PE} "
            f"‘đây là sự thật cao quý về cách thực hành dẫn đến sự chấm dứt khổ đau’, nơi Ta, này các tỳ-khưu{PE} "
            "‘sự thật cao quý về cách thực hành dẫn đến sự chấm dứt khổ đau ấy cần được tu tập’, nơi Ta, này các "
            f"tỳ-khưu{PE} đã được tu tập, nơi Ta, này các tỳ-khưu, trong những điều chưa từng được nghe trước đây, "
            f"con mắt đã sinh khởi{PE} ánh sáng đã sinh khởi” "
            "[Đại Phẩm 15; Tương Ưng Bộ Kinh 5.1081; Phân Tích Đạo 2.30]!")
#   ch12 ^5-? (Bodhisatta kathā) wording; the garbled opening "idaṃ dukkhaṃ ariyasacca"nti is given its inner
#   quote as meant (‘…’ as in ch12)

UDDANA = (", ".join(f"{cap(k) if i == 0 else k} là {AN}" for i, (k, _) in enumerate(KILLERS + [(SB, '')]))
          + f", {NO_NANA}, {has(INN, NP, True)}, {IN_DEV}, {M5}, {D12}.")
#   Mātughātako ānantariko … saṅghabhedako ānantariko, natthi puthujjanassa ñāṇaṃ, natthi nirayesu nirayapālā, atthi
#   devesu tiracchānagatā, pañcaṅgiko maggo, dvādasavatthukaṃ ñāṇaṃ lokuttaranti.
UDD50 = "Sự chế ngự, sự tích lũy phước, đã sống, với quá khứ, và kẻ giết mẹ."
#   Niggaho (ch24 Niggahakathā; termbase «sự chế ngự»), puññasañcayo (termbase), aṭṭhāsi (ch26; termbase «đã sống»),
#   atītena ca (ch27; instrumental «với quá khứ»), mātughātako (here); ch23 frame «…, gốc rễ, và …»

REUSED28 = [  # (Pāli, Vietnamese, book)
    ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā", PANNA_F, "1"),
    ("ākāsānañcāyatanaṃ … nevasaññānāsaññāyatanaṃ", "; ".join(
        f"vị ấy chứng nhập và an trú {x}" for x in ARUPA[:1]), "2"),
    ("viññāṇañcāyatanaṃ", ARUPA[1], "2"), ("ākiñcaññāyatanaṃ", ARUPA[2], "2"), ("nevasaññānāsaññāyatanaṃ", ARUPA[3], "2"),
    ("gilānapaccayabhesajjaparikkhāra", "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh", "2"),
    ("Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – sammādiṭṭhi", f"{AM8}, cụ thể là – quan điểm đúng đắn", "2"),
    ("devaloka", "thế giới chư thiên", "2"),
    ("pañca kammāni ānantarikāni", "nghiệp có quả không gián đoạn", "2"),
    ("pāṇātipātī hoti, adinnādāyī hoti", "sát hại sinh mạng, lấy của không được cho", "4"),
    ("musāvādī hoti", "nói dối", "4"),
    ("sammādiṭṭhi … sammāsamādhi", ", ".join(S.SAMMA), "1"),
    ("maggaṅgaṃ", MA, "1"),
    ("cakkhumā puriso", "có mắt", "4"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Tassuddānaṃ – (after Tatiyo paṇṇāsako.)", TASS50, "23-pannarasamavaggo.md"),
    ("Tatiyo paṇṇāsako. (frame)", "Nhóm năm mươi thứ ba.", "23-pannarasamavaggo.md"),
    ("Ñāṇakathā", S.katha("hiểu biết"), "19-ekadasamavaggo.md"),
    ("Ñāṇakathā niṭṭhitā.", S.katha_end("hiểu biết"), "19-ekadasamavaggo.md"),
    ("Āpāyiko nerayiko, kappaṭṭho saṅghabhedako;", VERSE_SB[0], "21-terasamavaggo.md"),
    ("Vaggarato adhammaṭṭho, yogakkhemā padhaṃsati;", VERSE_SB[1], "21-terasamavaggo.md"),
    ("Saṅghaṃ samaggaṃ bhetvāna", "Sau khi chia rẽ Tăng đoàn đang hòa hợp", "21-terasamavaggo.md"),
    ("kappaṃ nirayamhi paccatī\"ti [cūḷava. 354; a. ni. 10.39; itivu. 18]",
     "bị nung đốt trong địa ngục suốt một kiếp” [Tiểu Phẩm 354; Tăng Chi Bộ Kinh 10.39; Kinh Phật Thuyết Như Vậy 18]",
     "21-terasamavaggo.md"),
    ("Kappaṭṭho dānaṃ dadeyya", "có thể thực hiện sự bố thí", "21-terasamavaggo.md"),
    ("cīvaraṃ dadeyya…pe… piṇḍapātaṃ dadeyya…pe… senāsanaṃ dadeyya…pe… gilāna…",
     "cho y phục… cho đồ ăn khất thực… cho chỗ ở… cho thuốc men và vật dụng chữa bệnh", "21-terasamavaggo.md"),
    ("seyyathidaṃ –", "cụ thể là –", "21-terasamavaggo.md"),
    ("Nanu lobho akusalo vutto bhagavatā", "Chẳng phải Đức Thế Tôn đã nói rằng", "21-terasamavaggo.md"),
    ("tena ñāṇena dukkhaṃ parijānāti, … maggaṃ bhāvetīti?", f"bằng hiểu biết ấy mà {FOUR} không?",
     "5-sabbamatthitikatha.md"),
    ("Mātā jīvitā voropitā… pitā … arahā … tathāgatassa lohitaṃ uppāditaṃ",
     "mẹ bị tước đoạt mạng sống… cha bị tước đoạt mạng sống… bậc A-la-hán bị tước đoạt mạng sống… máu của Như Lai "
     "bị làm cho chảy", "20-dvadasamavaggo.md"),
    ("sañcicca mātaraṃ jīvitā voropeyya", f"cố ý {MOTHER}", "20-dvadasamavaggo.md"),
    ("mātughātako… pitughātako… arahantaghātako… ruhiruppādako… saṅghabhedako",
     "kẻ giết mẹ… kẻ giết cha… kẻ giết bậc A-la-hán… kẻ làm chảy máu", "10-dutiyavaggo.md"),
    ("saṅghabhedako", SB, "10-dutiyavaggo.md"),
    ("Arahā … samāpattiṃ samāpajjeyyāti?", "có thể nhập", "13-pancamavaggo.md"),
    ("Hañci \"…\"nti – attheva suttanto, no ca vata re vattabbe – \"…\"",
     f"– {ATTH_HANCI}, thì này bạn, chắc chắn không nên nói – “", "14-chatthavaggo.md"),
    ('"…"nti – attheva suttantoti? Natthi.', f"” – {ATTH_L} {NO_HAVE}", "14-chatthavaggo.md"),
    ("natthi devesu …", DEV, "3-brahmacariyakatha.md"),
    ("tiracchānagato", TG, "1-puggalakatha.md"),
    ("sotāpattimaggo / sotāpattiphalaṃ", "con đường vào dòng, thành quả vào dòng", "23-pannarasamavaggo.md"),
    ("arahattamaggassa / arahattaphalassa", "con đường A-la-hán", "23-pannarasamavaggo.md"),
    ("sakadāgāmimaggo / anāgāmimaggo", "con đường trở lại một lần", "23-pannarasamavaggo.md"),
    ("con đường không trở lại", "con đường không trở lại", "23-pannarasamavaggo.md"),
    ("thành quả A-la-hán", "thành quả A-la-hán", "23-pannarasamavaggo.md"),
    ("lokuttaraṃ", "là vượt thế gian", "23-pannarasamavaggo.md"),
    ("Sammādiṭṭhi maggo, sā ca sārammaṇā", "và nó có đối tượng", "18-dasamavaggo.md"),
    ("Nanu sammāvācā sammākammanto sammāājīvo maggoti?",
     "Chẳng phải lời nói đúng đắn, hành động đúng đắn, sinh kế đúng đắn là con đường sao?", "18-dasamavaggo.md"),
    ("dhammavinaye", "trong Giáo Pháp và Giới Luật", "10-dutiyavaggo.md"),
    ("[dha. pa. 239 dhammapade]", "[Kinh Pháp Cú 239, trong Kinh Pháp Cú]", "10-dutiyavaggo.md"),
    ("pe. va. 19", "Ngạ Quỷ Sự 19", "15-sattamavaggo.md"),
    ("[arūpadhātuyā (sabbattha)]", "(Mọi bản)", "16-atthamavaggo.md"),
    ("[x (sī.), y (syā. pī. ka.)] spelling", "[khác chính tả (Sī.): jānatāhaṃ; (Syā., Pī., Ka.): jānatvāhaṃ]",
     "10-dutiyavaggo.md"),
    ("dī. ni.", "Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("‘idaṃ dukkhaṃ ariyasacca’nti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ udapādi … āloko udapādi.",
     NANA_SUT.split(" ‘Sự thật")[0][1:], "12-catutthavaggo.md"),
    ("‘Taṃ kho panidaṃ dukkhaṃ ariyasaccaṃ pariññeyya’nti me, bhikkhave…pe… pariññātanti me, bhikkhave",
     f"‘Sự thật cao quý về khổ đau ấy cần được hiểu biết trọn vẹn’, nơi Ta, này các tỳ-khưu{PE} đã được hiểu biết "
     f"trọn vẹn, nơi Ta, này các tỳ-khưu", "12-catutthavaggo.md"),
    ("‘taṃ kho panidaṃ dukkhasamudayaṃ … pahātabba’nti me, bhikkhave…pe… pahīnanti me, bhikkhave…pe…",
     f"ấy cần dứt bỏ’, nơi Ta, này các tỳ-khưu{PE} đã được dứt bỏ, nơi Ta, này các tỳ-khưu{PE} ‘đây là sự thật cao "
     "quý về sự chấm dứt khổ đau", "12-catutthavaggo.md"),
    ("‘taṃ kho panidaṃ dukkhanirodhaṃ … sacchikatanti me, bhikkhave…pe… ‘idaṃ dukkhanirodhagāminī … bhāvitanti me",
     f"’, nơi Ta, này các tỳ-khưu{PE} ‘sự thật cao quý về sự chấm dứt khổ đau ấy cần được tự mình chứng nghiệm’, nơi "
     f"Ta, này các tỳ-khưu{PE} đã được tự mình chứng nghiệm, nơi Ta, này các tỳ-khưu{PE} ‘đây là sự thật cao quý về "
     f"cách thực hành dẫn đến sự chấm dứt khổ đau’, nơi Ta, này các tỳ-khưu{PE} ‘sự thật cao quý về cách thực hành "
     f"dẫn đến sự chấm dứt khổ đau ấy cần được tu tập’, nơi Ta, này các tỳ-khưu{PE} đã được tu tập, nơi Ta, này các "
     "tỳ-khưu, trong những điều chưa từng được nghe trước đây, con mắt đã sinh khởi", "12-catutthavaggo.md"),
    ("[mahāva. 15; saṃ. ni. 5.1081; paṭi. ma. 2.30]", "[Đại Phẩm 15; Tương Ưng Bộ Kinh 5.1081; Phân Tích Đạo 2.30]",
     "12-catutthavaggo.md"),
    ("Kappaṭṭha-", KT, "21-terasamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED28 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = [unicodedata.normalize("NFC", x) for x in lines]
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    def sub(k, n):                  # #### Vīsatimavaggo / ##### (n) k. X-kathā
        heading(f"5-28-{k}-0", 4, VAGGA)
        heading(f"5-28-{k}-1-0", 5, f"({n}) {k}. {S.katha(KATHA[k])}")

    heading("5-28-0", 3, VAGGA)

    # ---- (194) 1. Asañciccakathā ----------------------------------------------------------------------------------
    heading("5-28-1-0", 4, f"(194) 1. {S.katha(KATHA[1])}")
    add("5-857",
        f"{Q(A_MOTHER)} {YES} {Q(A_KILL)} {NO_PE} {q(A_MOTHER)} {YES} {Q(f'{THEFT}{PE} {LIE}')} {NO_PE}",
        f"{Q(A_KILL_N)} {YES} {Q(A_MOTHER_N)} {NO_PE} {q(f'{THEFT}{PE} {LIE_N}')} {YES} {Q(A_MOTHER_N)} {NO_PE}")
    add("5-858",
        f"{Q(A_MOTHER)} {YES} “{cap(A_MOTHER)}” – {ATTH_L} {NO_HAVE} “{cap(S_MOTHER)}” – {ATTH_L} {YES} "
        f"Nếu “{S_MOTHER}” – {ATTH_HANCI}, thì {RE}, chắc chắn không nên nói – “{A_MOTHER}”.")
    add("5-859", *[f"{S.na_vattabbam(f'{k} là {AN}')} {YES} {NANU(p)} {YES} {S.hanci(p, f'{k} là {AN}')}"
                   for k, p in KILLERS])
    add("5-860",
        f"{Q(f'{SB} là {AN}')} {YES} {Q(f'tất cả {SBS} đều là {AN}')} {NO_PE} {q(f'tất cả {SBS} đều là {AN}')} {YES} "
        f"{Q(f'{DSB} là {AN}')} {NO_PE}")
    add("5-861",
        f"{Q(f'{DSB} là {AN}')} {YES} {S.NANU_VUTTAM} {UPALI_SUT} {S.ATTHEVA} {YES} {S.tena_hi_na(f'{DSB} là {AN}')}")
    add("5-862",
        f"{S.na_vattabbam(f'{DSB} là {AN}')} {YES} {S.NANU_VUTTAM}",
        *VERSE_SB,
        f"{S.ATTHEVA} {YES} {S.tena_hi(f'{SB} là {AN}')}",
        S.katha_end(KATHA[1]))

    # ---- (195) 2. Ñāṇakathā ---------------------------------------------------------------------------------------
    sub(2, 195)
    add("5-863",
        f"{Q(NO_NANA)} {YES} {Q(f'{PJ} không có {PANNA_F}')} {NO_PE} {nanu_l(f'{PJ} có {PANNA_PE}')} {YES} "
        f"{S.hanci_neg(f'{PJ} có {PANNA_PE}', NO_NANA)}")
    J1 = f"{PJ} có thể nhập tầng thiền thứ nhất"                       # puthujjano paṭhamaṃ jhānaṃ samāpajjeyya
    GIVE = ", ".join(f"cho {x}" for x in GIFTS)
    J2 = (f"{PJ} có thể nhập tầng thiền thứ hai{PE} tầng thiền thứ ba{PE} tầng thiền thứ tư{PE} {ARUPA[0]}, "
          f"có thể nhập {', '.join(ARUPA[1:])}, {PJ} có thể thực hiện sự bố thí {PE} {GIVE}")
    add("5-864",
        f"{Q(NO_NANA)} {YES} {Q(J1)} {YES} {S.hanci_neg(J1, NO_NANA)}",
        f"{Q(J2)} {YES} {S.hanci_neg(f'{PJ} có thể cho {GIFTS[-1]}', NO_NANA)}")
    add("5-865",
        f"{Q(HAS_NANA)} {YES} {Q(f'{PJ} bằng hiểu biết ấy mà {FOUR}')} {NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (196) 3. Nirayapālakathā ---------------------------------------------------------------------------------
    sub(3, 196)
    add("5-866",
        f"{Q(has(INN, NP, True))} {YES} {Q(has(INN, KK, True))} {NO_PE} {q(has(INN, KK))} {YES} {Q(has(INN, NP))} "
        f"{NO_PE}",
        f"{Q(kk_k(MAN))} {YES} {Q(kk_k(INN))} {NO_PE} {q(kk_k(INN, True))} {YES} {Q(kk_k(MAN, True))} {NO_PE}")
    add("5-867",
        f"{Q(has(INN, NP))} {YES} {S.NANU_VUTTAM}",
        *VERSE_N,
        f"{S.ATTHEVA} {YES} {S.tena_hi(has(INN, NP, True))}")
    add("5-868",
        f"{Q(has(INN, NP, True))} {YES} {S.NANU_VUTTAM} {SUT_5} {S.ATTHEVA} {YES} {S.tena_hi(has(INN, NP))}",
        f"{Q(has(INN, NP, True))} {YES} {S.NANU_VUTTAM} {SUT_HELL}",
        *VERSE_HELL,
        f"{S.ATTHEVA} {YES} {S.tena_hi(has(INN, NP))}",
        S.katha_end(KATHA[3]))

    # ---- (197) 4. Tiracchānakathā ---------------------------------------------------------------------------------
    sub(4, 197)
    add("5-869",
        f"{Q(IN_DEV)} {YES} {Q(has('giữa loài súc sinh', 'chư thiên'))} {NO_PE} {q(IN_DEV)} {YES} "
        f"{Q('thế giới chư thiên là cõi súc sinh')} {NO_PE} {q(IN_DEV)} {YES} {Q(CREATURES)} {NO_PE}")
    add("5-870",
        f"{Q(IN_DEV_N)} {YES} {NANU(ERAVANA)} {YES} {S.hanci(ERAVANA, IN_DEV)}")
    add("5-871",
        f"{Q(IN_DEV)} {YES} {Q(KEEPERS)} {NO} {S.tena_hi(IN_DEV_N)}",
        S.katha_end(KATHA[4]))

    # ---- (198) 5. Maggakathā --------------------------------------------------------------------------------------
    sub(5, 198)
    TAUGHT = f"Đức Thế Tôn đã nói rằng {M8}, cụ thể là – {SAMMA['diṭṭhi']}"   # aṭṭhaṅgiko maggo vutto bhagavatā, seyyathidaṃ –
    add("5-872",
        f"{Q(M5)} {YES} Chẳng phải {TAUGHT}{PE} {SAMMA['samādhi']} sao? {YES} "
        f"Nếu {TAUGHT} {PE} {SAMMA['samādhi']}, thì {RE}, chắc chắn không nên nói – “{M5}”.",
        f"{Q(M5)} {YES} {S.NANU_VUTTAM}",
        *VERSE_M,
        f"{S.ATTHEVA} {YES} {S.tena_hi(M8)}")
    add("5-873",
        f"{Q(ma(SAMMA['vācā'], True))} {YES} {Q(ma(SAMMA['diṭṭhi'], True))} {NO_PE} {q(ma(SAMMA['vācā'], True))} {YES} "
        f"Có phải {pe_join('saṅkappa', 'vāyāma', 'sati')}{PE} {ma(SAMMA['samādhi'], True)} không? {NO_PE}",
        f"Có phải {SAMMA['kammanta']}{PE} {ma(SAMMA['ājīva'], True)} không? {YES} "
        f"Có phải {SAMMA['diṭṭhi']}{PE} {ma(SAMMA['samādhi'], True)} không? {NO_PE}",
        f"{Q(ma(SAMMA['diṭṭhi']))} {YES} {Q(ma(SAMMA['vācā']))} {NO_PE} {q(ma(SAMMA['diṭṭhi']))} {YES} "
        f"Có phải {SAMMA['kammanta']}{PE} {ma(SAMMA['ājīva'])} không? {NO_PE}",
        f"Có phải {pe_join('saṅkappa', 'vāyāma', 'sati')}{PE} {ma(SAMMA['samādhi'])} không? {YES} "
        f"Có phải {pe_join('vācā', 'kammanta')}{PE} {ma(SAMMA['ājīva'])} không? {NO_PE}")
    add("5-874",
        f"{Q(AM8)} {YES} {S.NANU_VUTTAM} {PUBBE} {S.ATTHEVA} {YES} {S.tena_hi(M5)}")
    add("5-875",
        f"{Q(M5)} {YES} {S.NANU_VUTTAM} {SUBH_SUT} {S.ATTHEVA} {YES} {S.tena_hi(M8)}",
        S.katha_end(KATHA[5]))

    # ---- (199) 6. Ñāṇakathā ---------------------------------------------------------------------------------------
    sub(6, 199)
    LU12 = twelve("hiểu biết vượt thế gian")                            # dvādasa lokuttarañāṇāni (termbase)
    SM12 = twelve("con đường vào dòng")                                 # dvādasa sotāpattimaggā (termbase)
    AM12 = twelve("con đường A-la-hán")
    add("5-876",
        f"{Q(D12)} {YES} {Q(LU12)} {NO_PE} {q(LU12)} {YES} {Q(SM12)} {NO_PE} {q(SM12)} {YES} "
        f"{Q(twelve('thành quả vào dòng'))} {NO_PE} "
        f"có phải có mười hai con đường trở lại một lần{PE} con đường không trở lại{PE} con đường A-la-hán không? "
        f"{NO_PE} {q(AM12)} {YES} {Q(twelve('thành quả A-la-hán'))} {NO_PE}")
    add("5-877",
        f"{S.na_vattabbam(D12)} {YES} {S.NANU_VUTTAM} {NANA_SUT} {S.ATTHEVA} {YES} {S.tena_hi(D12)}",
        S.katha_end(KATHA[6]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA,
        CATUTTHO,
        TASS50,
        UDD50)
    return segs


def find(pat, mx=4, mc=700):
    pdir = ROOT / "AI_translation/pali/pi-5_split_chapters"
    vdir = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
    rx, h = re.compile(pat), 0
    for n in FINISHED:
        pl = [x for x in (pdir / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        vl = [x for x in (vdir / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if m:
                s = max(0, m.start() - 100)
                print(f"[{n} line {i + 1}]\n  PI: {ln[s:s + 400]}\n  VI: {vl[i][:mc]}")
                h += 1
                if h >= mx:
                    return


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-28"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--find"]:
        a = sys.argv[2:]
        find(a[0], int(a[1]) if len(a) > 1 else 4, int(a[2]) if len(a) > 2 else 700)
    else:
        main()
