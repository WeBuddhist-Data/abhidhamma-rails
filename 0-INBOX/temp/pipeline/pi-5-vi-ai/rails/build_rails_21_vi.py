"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 21, Terasamavaggo (^5-21-0 … ^5-685): ten kathās
(126-135) with the repeated "Terasamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/21-terasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, CIT …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED21);
strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-21.md.

usage: python -I -X utf8 -B build_rails_21_vi.py          (writes the chapter and the adherence copy rails\\adh-21\\)
       python -I -X utf8 -B build_rails_21_vi.py find <regex> [max] [maxchars]   (finished pi-5 rails lookup)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "21-terasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, CIT = S.cap, S.CIT
FINISHED = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
            "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
            "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
            "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
            "17-navamavaggo.md"]


def nanu(x):                          # …pe… nanu Xti? (lower case after …pe…)
    return f"chẳng phải {x} sao?"


def pe_end(s):                        # a closing "…ti…pe…." : the final «.» is absorbed by «…»
    assert s.endswith(".")
    return s[:-1] + PE


# ---------------------------------------------------------------------------------------------------------------
# (126) Kappaṭṭha
# ---------------------------------------------------------------------------------------------------------------
KP = "người tồn tại suốt một kiếp"                     # kappaṭṭho (termbase Kappaṭṭho tiṭṭheyya; ṭho «tồn tại»)
KT = f"{KP} có thể kéo dài suốt một kiếp"              # kappaṭṭho kappaṃ tiṭṭheyya (tiṭṭheyya «kéo dài», APPROVED;
#                                                        «suốt … kiếp» as ch10 kappaṃ tiṭṭhati; optative «có thể»)
KK = "nghiệp khiến tồn tại suốt một kiếp"              # kappaṭṭhiyaṃ kammaṃ


def ks(x):                            # Kappo ca saṇṭhāti X ca …
    return f"kiếp hình thành và {x}"                   # saṇṭhāti «hình thành» (termbase)


KS = [ks("Đức Phật sinh khởi ở thế gian"),             # buddho ca loke uppajjati (uppajjati «sinh khởi»)
      ks("Tăng đoàn bị chia rẽ"),                      # saṅgho ca bhijjati (as saṅgho bhinno, termbase / pi-2)
      ks(f"{KP} làm {KK}"),                            # kappaṭṭho ca kappaṭṭhiyaṃ kammaṃ karoti
      ks(f"{KP} qua đời")]                             # kappaṭṭho ca puggalo kālaṃ karoti
FIRE = f"Khi kiếp đang bị thiêu đốt, {KP} đi đến đâu?"   # Kappaṭṭho kappe ḍayhante kattha gacchatīti?
OTHER = "Đi đến thế giới khác."                         # Aññaṃ lokadhātuṃ gacchatīti. (lokadhātu «thế giới», ch10)
DEAD_Q = "Đi đến khi là người đã chết, hay đi đến qua không trung?"   # Mato gacchati, vehāsaṃ gacchatīti?
DEAD_A = "Đi đến khi là người đã chết."                 # Mato gacchatīti.
SKY = "đi đến qua không trung"                          # vehāsaṃ gacchati
NOTE656 = (" [đi đến qua không trung (?): đây chính là lời khẳng định của người theo học thuyết khác, "
           "như ở dòng thứ chín của Các vấn đề tranh luận 621-623]")
#   [vehāsaṃ gacchatīti (?) ayaṃ hi paravādissa paṭiññāyeva, kathā. 621-623 navamapantiyaṃ viya]
IDDHI = ("đã tu tập nền tảng thần thông bằng ý muốn, đã tu tập nền tảng thần thông bằng tinh tấn, "
         "đã tu tập nền tảng thần thông bằng tâm, đã tu tập nền tảng thần thông bằng sự thẩm xét")
#   Kappaṭṭhena chandiddhipādo bhāvito … vīmaṃsiddhipādo bhāvito (pi-2 names; bhāvito «đã tu tập»)
VERSE = [f"“Kẻ chia rẽ Tăng đoàn thuộc cõi khổ, là chúng sinh địa ngục, tồn tại suốt một kiếp;",
         "Ưa thích bè phái, đứng vững trong điều trái Giáo Pháp, rơi khỏi sự an ổn thoát khỏi các ách;",
         f"Sau khi chia rẽ Tăng đoàn đang hòa hợp{S.var('Sī., Ka.', 'bhinditvā')}, bị nung đốt trong địa ngục "
         f"suốt một kiếp” [Tiểu Phẩm 354; {CIT['a. ni.']} 10.39; {CIT['itivu.']} 18]."]
#   Āpāyiko nerayiko, kappaṭṭho saṅghabhedako; / Vaggarato adhammaṭṭho, yogakkhemā padhaṃsati; /
#   Saṅghaṃ samaggaṃ bhetvāna [bhinditvā (sī. ka.)], kappaṃ nirayamhi paccatī"ti [cūḷava. 354; a. ni. 10.39; itivu. 18].

# ---------------------------------------------------------------------------------------------------------------
# (127) Kusalapaṭilābha
# ---------------------------------------------------------------------------------------------------------------
KC = "tâm thiện"                                        # kusalaṃ cittaṃ (termbase)
T2 = f"{KP} không thể có được {KC}"                    # kappaṭṭho kusalaṃ cittaṃ na paṭilabheyya
T2P = f"{KP} có thể có được {KC}"                      # kappaṭṭho kusalaṃ cittaṃ paṭilabheyya
DANA = f"{KP} có thể thực hiện sự bố thí"              # kappaṭṭho dānaṃ dadeyya (ch15 «thực hiện sự bố thí»)
ROUND = "đi nhiễu quanh bảo tháp theo chiều bên phải"  # cetiyaṃ abhidakkhiṇaṃ kareyya (termbase)
GIFTS = (f"{KP} có thể cho y phục{PE} cho đồ ăn khất thực{PE} cho chỗ ở{PE} "
         f"cho thuốc men và vật dụng chữa bệnh {PE} cho món ăn cứng{PE} cho món ăn mềm{PE} cho nước uống{PE} "
         f"đảnh lễ bảo tháp{PE} dâng vòng hoa lên bảo tháp{PE} dâng hương thơm{PE} dâng dầu thoa{PE} "
         f"{ROUND}{S.var('Pī.', 'padakkhiṇaṃ')}")
#   cīvaraṃ dadeyya…pe… piṇḍapātaṃ…pe… senāsanaṃ…pe… gilānapaccayabhesajjaparikkhāraṃ dadeyya … khādanīyaṃ…
#   bhojanīyaṃ… pānīyaṃ… cetiyaṃ vandeyya… cetiye mālaṃ āropeyya… gandhaṃ… vilepanaṃ āropeyya…pe…
#   cetiyaṃ abhidakkhiṇaṃ [padakkhiṇaṃ (pī.)] kareyya   (the Pāli's spaced " … " kept)
VUT = f"có thể có được {KC} của sự xuất khỏi từ đó"    # Tato vuṭṭhānaṃ kusalaṃ cittaṃ paṭilabheyya
HIGH = f"có thể có được {KC} thuộc cõi hình sắc{PE} thuộc cõi không hình sắc{PE} vượt thế gian"
#   Rūpāvacaraṃ…pe… arūpāvacaraṃ…pe… lokuttaraṃ kusalaṃ cittaṃ paṭilabheyya

# ---------------------------------------------------------------------------------------------------------------
# (128) Anantarāpayutta
# ---------------------------------------------------------------------------------------------------------------
AP = "người đã tiến hành nghiệp có quả không gián đoạn"   # anantarāpayutto puggalo (termbase)
SN = "sự cố định theo hướng đúng đắn"                   # sammattaniyāma (ch13 / ch14)
MN = "sự cố định theo hướng sai lầm"                    # micchattaniyāma (ch14)
T3 = f"{AP} có thể bước vào {SN}"                       # … sammattaniyāmaṃ okkameyya
BOTH = f"có thể bước vào cả hai, {MN} và {SN}"          # Micchattaniyāmañca sammattaniyāmañca ubho okkameyya
DONE = "nghiệp ấy đã được tiến hành, sự hối tiếc đã được làm sinh khởi, sự ân hận đã được làm sinh ra"
#   taṃ kammaṃ payuttaṃ kukkuccaṃ uppāditaṃ vippaṭisāriyaṃ janitaṃ (termbase)
ABH = f"{AP} không có khả năng bước vào {SN}"           # … abhabbo sammattaniyāmaṃ okkamituṃ
FIVE = ["mẹ bị tước đoạt mạng sống", "cha bị tước đoạt mạng sống", "bậc A-la-hán bị tước đoạt mạng sống",
        "máu của Như Lai bị làm cho chảy với tâm độc ác", "Tăng đoàn bị chia rẽ"]
#   Mātā jīvitā voropitā… pitā… arahā jīvitā voropito… duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ… saṅgho bhinno
#   (pi-2 ^2-U55 wording, termbase Mātā jīvitā voropitā / saṅgho bhinno)
WITHDRAW = "sau khi rút lại nghiệp ấy, xua tan sự hối tiếc, dẹp bỏ sự ân hận"
#   taṃ kammaṃ paṭisaṃharitvā kukkuccaṃ paṭivinodetvā vippaṭisāriyaṃ paṭivinetvā (termbase)
VAR661 = S.var("Sī., Pī., Ka.", "paṭivinodetvā")


def abh_w(var=""):                    # AP taṃ kammaṃ paṭisaṃharitvā … abhabbo sammattaniyāmaṃ okkamituṃ
    return f"{AP}, {WITHDRAW}{var}, không có khả năng bước vào {SN}"


UNDONE = "nghiệp ấy đã được rút lại, sự hối tiếc đã được xua tan, sự ân hận đã được dẹp bỏ"
#   taṃ kammaṃ paṭisaṃhaṭaṃ kukkuccaṃ paṭivinoditaṃ vippaṭisāriyaṃ paṭivinītaṃ
WAS = "người ấy đã tiến hành nghiệp ấy"                 # taṃ kammaṃ payutto āsi

# ---------------------------------------------------------------------------------------------------------------
# (129) Niyatassa niyāma
# ---------------------------------------------------------------------------------------------------------------
NY = "người cố định"                                    # niyato (termbase)
NI = "sự cố định"                                       # niyāmo (ch12 / ch14)
T4 = f"{NY} bước vào {NI}"                              # niyato niyāmaṃ okkamati (termbase Niyato okkamati)
CROSS = (f"người cố định theo hướng sai lầm bước vào {SN}, người cố định theo hướng đúng đắn bước vào {MN}")
#   Micchattaniyato sammattaniyāmaṃ okkamati, sammattaniyato micchattaniyāmaṃ okkamati


def before(x, y=NI):                  # pubbe X bhāvetvā pacchā Y okkamati
    return f"trước đó tu tập {x} rồi sau đó bước vào {y}"


BODHI = "Bồ-tát có khả năng không thấu hiểu Giáo Pháp trong đời ấy"
#   Bhabbo bodhisatto tāya jātiyā dhammaṃ nābhisametuṃ (as written; jātiyā «đời»)

# ---------------------------------------------------------------------------------------------------------------
# (130) / (131) Nivuta / Sammukhībhūta
# ---------------------------------------------------------------------------------------------------------------
T5 = "người bị ngăn che dứt bỏ chướng ngại"            # nivuto nīvaraṇaṃ jahati (termbase)
T6 = "người đang hiện diện đối mặt dứt bỏ xiềng xích"  # sammukhībhūto saṃyojanaṃ jahati (termbase)
RATTO = ("người đã tham đắm dứt bỏ sự tham đắm, người đã sân hận dứt bỏ sự sân hận, "
         "người đã si mê dứt bỏ sự si mê, người đã bị phiền não làm ô nhiễm dứt bỏ các phiền não")
#   Ratto rāgaṃ jahati, duṭṭho dosaṃ jahati, mūḷho mohaṃ jahati, kiliṭṭho kilese jahati (termbase)
RAGENA = ("bằng sự tham đắm mà dứt bỏ sự tham đắm, bằng sự sân hận mà dứt bỏ sự sân hận, "
          "bằng sự si mê mà dứt bỏ sự si mê, bằng các phiền não mà dứt bỏ các phiền não")
#   rāgena rāgaṃ jahati, … kilesehi kilese jahati («bằng X mà …» as ch13 tena phassena …)
RM = "sự tham đắm gắn liền với tâm, con đường gắn liền với tâm"   # Rāgo cittasampayutto, maggo cittasampayutto
RK = "sự tham đắm là bất thiện, con đường là thiện"               # rāgo akusalo, maggo kusalo
TWO = f"có sự tụ hợp của hai sự tiếp xúc{PE} hai tâm"            # Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ … (ch15)
KUS = ("các hiện tượng thiện và bất thiện, có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong sáng cùng "
       "với các mặt đối lập của chúng đi đến chỗ cùng hiện diện đối mặt nhau")                    # (ch15)
KUS_S = f"các hiện tượng thiện và bất thiện{PE} đi đến chỗ cùng hiện diện đối mặt nhau"
#   Kusalākusalā…pe… sammukhībhāvaṃ āgacchanti («các hiện tượng» kept before the elision: reported)
BH = "Này các tỳ-khưu"
FAR = "điều rất xa cách nhau"                                     # suvidūravidūraṃ (ch15)
SUT_FAR = (f"“{BH}, có bốn {FAR} này! Bốn điều nào? {BH}, bầu trời và mặt đất – đây là {FAR} thứ nhất{PE} "
           f"vì vậy, bản chất của người hiền thiện ở xa kẻ không hiền thiện”.")
#   "cattārimāni, bhikkhave, suvidūravidūrāni! Katamāni cattāri? Nabhañca, bhikkhave, pathavī ca – idaṃ paṭhamaṃ
#   suvidūravidūraṃ…pe… tasmā sataṃ dhammo asabbhi ārakā"ti.   (ch15 ^5-485 wording)
SAMAHITE = "Khi tâm đã an định như vậy"                           # so evaṃ samāhite citte (ch11)
SAMAHITE_FULL = (f"{SAMAHITE}, trong sạch, trong sáng, không còn vết nhơ, đã lìa những thứ làm vẩn đục, "
                 "đã trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm đến sự hiểu biết "
                 "về sự diệt tận các ô nhiễm")                    # (ch11, 11-tatiyavaggo.md line 89)
SAMAHITE_S = f"{SAMAHITE}{PE} vị ấy dẫn tâm đến sự hiểu biết về sự diệt tận các ô nhiễm"
#   so evaṃ samāhite citte…pe… āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti
JANATO = ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc"
          f"{PE} tâm được giải thoát khỏi ô nhiễm vô minh")
#   tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati…pe… avijjāsavāpi cittaṃ vimuccati (ch11)

# ---------------------------------------------------------------------------------------------------------------
# (132) Samāpanno assādeti
# ---------------------------------------------------------------------------------------------------------------
JN = "sự ưa thích tầng thiền"                           # jhānanikanti (termbase)
T7 = f"người đang nhập thành tựu thiền thỏa thích, {JN} có tầng thiền làm đối tượng"
#   samāpanno assādeti, jhānanikanti jhānārammaṇā (termbase Samāpanno assādeti; «có … làm đối tượng» ch17)
JJ = "tầng thiền ấy là đối tượng của tầng thiền ấy"     # taṃ jhānaṃ tassa jhānassa ārammaṇaṃ (as ch13 ñāṇa)
TEN = ("bằng sự tiếp xúc ấy mà chạm vào sự tiếp xúc ấy, bằng cảm giác ấy mà cảm nhận cảm giác ấy, bằng tri giác ấy "
       "mà nhận ra tri giác ấy, bằng chủ ý ấy mà cố ý về chủ ý ấy, bằng tâm ấy mà suy nghĩ về tâm ấy, bằng sự hướng "
       "tâm ấy mà hướng tâm đến sự hướng tâm ấy, bằng sự duy trì tâm ấy mà duy trì tâm nơi sự duy trì tâm ấy, bằng sự "
       "hân hoan ấy mà hân hoan với sự hân hoan ấy, bằng sự tỉnh thức ấy mà ghi nhớ sự tỉnh thức ấy, bằng trí tuệ ấy "
       "mà hiểu rõ trí tuệ ấy")
#   Tena phassena taṃ phassaṃ phusati … tāya paññāya taṃ paññaṃ pajānāti (ch13 ^5-441; "taṃ pīti" read as pītiṃ)
JCS = f"{JN} gắn liền với tâm, tầng thiền gắn liền với tâm"   # Jhānanikanti cittasampayuttā, jhānaṃ cittasampayuttaṃ
JAK = f"{JN} là bất thiện, tầng thiền là thiện"             # Jhānanikanti akusalaṃ, jhānaṃ kusalaṃ
ENJOY = "vị ấy thỏa thích nó, ham muốn nó và nhờ nó đạt đến sự hài lòng"
#   so taṃ assādeti taṃ nikāmeti tena ca vittiṃ āpajjati (termbase assādeti, nikāmeti, vittiṃ, āpajjati)
SUT_JH = (f"Ở đây, này các tỳ-khưu, vị tỳ-khưu hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, "
          f"chứng nhập và an trú tầng thiền thứ nhất, {ENJOY}; nhờ sự hướng tâm và sự duy trì tâm lắng xuống{PE} "
          f"tầng thiền thứ hai{PE} tầng thiền thứ ba{PE} chứng nhập và an trú tầng thiền thứ tư, {ENJOY}")
#   idha, bhikkhave, bhikkhu vivicceva kāmehi … (pi-2 jhāna wording; «ở đây, này các tỳ-khưu» as ch17)

# ---------------------------------------------------------------------------------------------------------------
# (133) Asātarāga
# ---------------------------------------------------------------------------------------------------------------
AR = "sự tham đắm điều không khoan khoái"               # asātarāgo (asāta «điều không khoan khoái», termbase / pi-2)
T8 = f"{AR} tồn tại"                                    # atthi asātarāgo (atthi «tồn tại»)
DK, SK = "sự khó chịu", "sự dễ chịu"                    # dukkhaṃ / sukhaṃ as feelings (APPROVED §2; commentary)


def delight(x):                       # X-ābhinandino sattā, atthi keci X patthenti … , X ajjhosāya tiṭṭhanti
    return (f"chúng sinh hoan hỷ với {x}, có ai đó mong ước, mong mỏi, tìm kiếm, truy tìm, tìm cầu {x}, "
            f"kéo dài sự bám chặt vào {x}")
#   patthenti «mong ước», pihenti «mong mỏi» (new), esanti «tìm kiếm», gavesanti «truy tìm», pariyesanti «tìm cầu»;
#   ajjhosāya «sự bám chặt» (new), tiṭṭhanti «kéo dài» (APPROVED)


DKV, SKV = "cảm giác khó chịu", "cảm giác dễ chịu"      # dukkhāya / sukhāya vedanāya (pi-2)


def lie(a, b):                        # a-vedanāya rāgānusayo anuseti, b-vedanāya paṭighānusayo anuseti
    return f"nơi {a}, khuynh hướng tiềm ẩn tham đắm nằm sẵn, nơi {b}, khuynh hướng tiềm ẩn ác cảm nằm sẵn"


SUT_AR = ("Vị ấy, khi đã rơi vào sự thuận theo và sự chống đối như vậy, cảm nhận bất cứ cảm giác nào, dù dễ chịu, "
          "hoặc khó chịu, hoặc không khó chịu cũng không dễ chịu, vị ấy hoan hỷ với cảm giác ấy, tán thán nó, "
          "duy trì sự bám chặt vào nó")
#   so evaṃ anurodhavirodhaṃ samāpanno yaṃ kiñci vedanaṃ vedayati sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, so taṃ
#   vedanaṃ abhinandati abhivadati ajjhosāya tiṭṭhati (tiṭṭhati «duy trì», APPROVED)
CIT675 = f"[{CIT['ma. ni.']} 3.409, trong Kinh Lớn về Sự Diệt Tận Khao Khát]"   # [ma. ni. 3.409 mahātaṇhāsaṅkhaye]

# ---------------------------------------------------------------------------------------------------------------
# (134) / (135) Dhammataṇhā
# ---------------------------------------------------------------------------------------------------------------
DT = "khao khát đối tượng của ý"                        # dhammataṇhā (termbase, pi-1 wording)
RT = "khao khát hình sắc"                               # rūpataṇhā
SDT, GT, RST, PHT = "khao khát âm thanh", "khao khát mùi", "khao khát vị", "khao khát vật xúc chạm"
LONG4 = f"{SDT}{PE} {GT}{PE} {RST}{PE} {PHT}"           # saddataṇhā…pe… gandhataṇhā…pe… rasataṇhā…pe… phoṭṭhabbataṇhā
SHORT2 = f"{SDT}{PE} {PHT}"                             # saddataṇhā…pe… phoṭṭhabbataṇhā
AB = "không xác định về mặt đạo đức"                    # abyākata
AK = "bất thiện"
SAM = "sự phát sinh của khổ đau"                        # dukkhasamudayo (termbase)
LOBHO = "sự tham lam"                                   # lobho (termbase)


def ab(x):                            # X abyākatā
    return f"{x} là {AB}"


def ak(x):                            # X akusalā
    return f"{x} là {AK}"


def lob(x, y):                        # X lobho Y   («là sự tham lam, là Y»)
    return f"{x} là {LOBHO}, là {y}"


def lob_na(x):                        # X lobho, na dukkhasamudayo
    return f"{x} là {LOBHO}, không phải là {SAM}"


def sam(x):                           # X dukkhasamudayo
    return f"{x} là {SAM}"


def na_sam(x):                        # X na dukkhasamudayo
    return f"{x} không phải là {SAM}"


T9 = ab(DT)                                             # dhammataṇhā abyākatā (termbase heading thesis)
T10 = na_sam(DT)                                        # dhammataṇhā na dukkhasamudayo
VIPAKA = (f"đó là điều {AB} thuộc quả của nghiệp, điều {AB} mang tính chức năng, vật chất, Niết-bàn, "
          f"{S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}")
#   Vipākābyākatā kiriyābyākatā rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ (termbase; «đó là» as ch17)
SAID_T = f"Đức Thế Tôn đã nói rằng khao khát là {AK}"                   # taṇhā akusalā vuttā bhagavatā (termbase)
SAID_L = f"Đức Thế Tôn đã nói rằng {LOBHO} là {AK}, {DT} là {LOBHO}"   # lobho akusalo vutto bhagavatā, dhammataṇhā lobho
SAID_TS = f"Đức Thế Tôn đã nói rằng khao khát là {SAM}"                 # taṇhā dukkhasamudayo vutto bhagavatā
SAID_LS = f"Đức Thế Tôn đã nói rằng {LOBHO} là {SAM}, {DT} là {LOBHO}"
SUT_T = ("“Đó là khao khát dẫn đến sự hiện hữu mới, đi kèm với sự thích thú và tham đắm, tìm vui thích chỗ này chỗ "
         "kia, cụ thể là – khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu”")
#   yāyaṃ taṇhā ponobbhavikā nandīrāgasahagatā tatratatrābhinandinī, seyyathidaṃ – kāmataṇhā, bhavataṇhā,
#   vibhavataṇhā (pi-2 ^ Saccavibhaṅga wording)
SA_DT = f"đó là {DT}"                                   # sā dhammataṇhā

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười ba"                            # Terasamavaggo (termbase)
KATHA = {1: KP, 2: "sự có được điều thiện", 3: AP, 4: f"{NI} của {NY}", 5: "người bị ngăn che",
         6: "người đang hiện diện đối mặt", 7: "việc người đang nhập thành tựu thiền thỏa thích", 8: AR,
         9: f"việc {T9}", 10: f"việc {T10}"}
#   Kappaṭṭha-, Kusalapaṭilābha- (termbase), Anantarāpayutta-, Niyatassa niyāma-, Nivuta-, Sammukhībhūta-,
#   Samāpanno assādeti- (-ti thesis «việc», ch17), Asātarāga-, Dhammataṇhā abyākatāti-, Dhammataṇhā na dukkhasamudayoti-
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)
UDDANA = cap(", ".join([KT, T2, T3, T4, T5, T6, JN, AR, T9, T10])) + "."
#   Kappaṭṭho kappaṃ tiṭṭheyya, kappaṭṭho kusalaṃ cittaṃ na paṭilabheyya, anantarāpayutto puggalo sammattaniyāmaṃ
#   okkameyya, niyato niyāmaṃ okkamati, nivuto nīvaraṇaṃ jahati, sammukhībhūto saṃyojanaṃ jahati, jhānanikanti,
#   asātarāgo, dhammataṇhā abyākatā, dhammataṇhā na dukkhasamudayoti.

REUSED21 = [  # (Pāli, Vietnamese, book)
    ("chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo",
     "nền tảng thần thông bằng ý muốn, nền tảng thần thông bằng tinh tấn, nền tảng thần thông bằng tâm, "
     "nền tảng thần thông bằng sự thẩm xét", "2"),
    ("nerayiko", "chúng sinh địa ngục", "2"),
    ("Mātā jīvitā voropitā hoti, pitā …", "Mẹ bị tước đoạt mạng sống, cha bị tước đoạt mạng sống, "
     "bậc A-la-hán bị tước đoạt mạng sống, máu của Như Lai bị làm cho chảy với tâm độc ác, Tăng đoàn bị chia rẽ", "2"),
    ("saṅgho bhinno", "Tăng đoàn bị chia rẽ", "2"),
    ("tathāgatassa lohitaṃ", "máu của Như Lai", "2"),
    ("micchattaniyatā", "cố định theo hướng sai lầm", "1"),
    ("kiriyābyākatesu dhammesu", f"các hiện tượng {AB} mang tính chức năng", "1"),
    ("rāgānusayo anuseti", "khuynh hướng tiềm ẩn tham đắm của chúng sinh nằm sẵn", "2"),
    ("paṭighānusayo anuseti", "khuynh hướng tiềm ẩn ác cảm của chúng sinh nằm sẵn", "2"),
    ("asātarūpaṃ", "điều không khoan khoái", "2"),
    ("dukkhāya vedanāya / sukhāya vedanāya", "cảm giác khó chịu", "2"), ("sukhā vedanā", "cảm giác dễ chịu", "2"),
    ("sukhaṃ … adukkhamasukhaṃ vā", "dễ chịu, hoặc khó chịu, hoặc không khó chịu cũng không dễ chịu", "2"),
    ("vivicceva kāmehi vivicca akusalehi dhammehi",
     "hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ nhất",
     "2"),
    ("vitakkavicārānaṃ vūpasamā", "nhờ sự hướng tâm và sự duy trì tâm lắng xuống", "2"),
    ("catutthaṃ jhānaṃ upasampajja viharati", "chứng nhập và an trú tầng thiền thứ tư", "2"),
    ("Yāyaṃ taṇhā ponobhavikā", "Đó là khao khát dẫn đến sự hiện hữu mới", "2"),
    ("nandirāgasahagatā … vibhavataṇhā",
     "đi kèm với sự thích thú và tham đắm, tìm vui thích chỗ này chỗ kia, cụ thể là – khao khát dục lạc, "
     "khao khát được hiện hữu, khao khát không còn hiện hữu", "2"),
    ("dhammataṇhā", DT, "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("dve kappe tiṭṭhati", "suốt hai kiếp", "10-dutiyavaggo.md"),
    ("kappaṃ tiṭṭhati", "suốt một kiếp", "10-dutiyavaggo.md"),
    ("dasasahassilokadhātuṃ", "thế giới", "10-dutiyavaggo.md"),
    ("cūḷava. (citation)", "[Tiểu Phẩm", "10-dutiyavaggo.md"), ("mahāva. (citation)", "[Đại Phẩm", "10-dutiyavaggo.md"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("… kaṇṭakasuttaṃ nissāya pucchati (citation note)", "Tăng Chi Bộ Kinh 10.72, câu hỏi dựa vào Kinh Cái Gai",
     "10-dutiyavaggo.md"),
    ("upasaṃhareyyuṃ (optative)", "người khác có thể đưa", "10-dutiyavaggo.md"),
    ("dukkarakāriyaṃ kareyya (optative)", "có thể làm việc khổ hạnh khó làm", "12-catutthavaggo.md"),
    ("dānaṃ deti", "thực hiện sự bố thí", "15-sattamavaggo.md"),
    ("cīvaraṃ / piṇḍapātaṃ / senāsanaṃ / gilāna… dadantassa",
     "người đang cho y phục… người đang cho đồ ăn khất thực… người đang cho chỗ ở… người đang cho thuốc men và vật "
     "dụng chữa bệnh", "13-pancamavaggo.md"),
    ("rūpāvacaraṃ / arūpāvacaraṃ", "thuộc cõi hình sắc", "11-tatiyavaggo.md"),
    ("Lokuttaraṃ", "vượt thế gian", "10-dutiyavaggo.md"),
    ("sammattaniyāmaṃ okkamissati", "bước vào sự cố định theo hướng đúng đắn", "13-pancamavaggo.md"),
    ("Micchattaniyāmo / Sammattaniyāmo", MN, "14-chatthavaggo.md"), ("Sammattaniyāmo", SN, "14-chatthavaggo.md"),
    ("niyato / aniyato", "người cố định", "13-pancamavaggo.md"),
    ("Niyāmokkantikathā", "Bàn về việc bước vào sự cố định", "12-catutthavaggo.md"),
    ("bodhisatto", "Bồ-tát", "12-catutthavaggo.md"),
    ("bhabbo … dhammaṃ abhisametuṃ", "có khả năng thấu hiểu Giáo Pháp", "13-pancamavaggo.md"),
    ("sakadāgāmimaggaṃ", "con đường trở lại một lần", "10-dutiyavaggo.md"),
    ("sotāpattimaggo … arahattamaggo", "con đường vào dòng", "10-dutiyavaggo.md"),
    ("arahattamaggo", "con đường A-la-hán", "10-dutiyavaggo.md"),
    ("anāgāmimaggo", "con đường không trở lại", "10-dutiyavaggo.md"),
    ("satipaṭṭhānaṃ…pe… sammappadhānaṃ… iddhipādo… indriyaṃ… balaṃ… bojjhaṅgo",
     "sự thiết lập tỉnh thức… nỗ lực đúng đắn… nền tảng thần thông… năng lực… sức mạnh… chi phần giác ngộ",
     "12-catutthavaggo.md"),
    ("Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti", TWO, "15-sattamavaggo.md"),
    ("Kusalākusalā … sammukhībhāvaṃ āgacchanti", KUS, "15-sattamavaggo.md"),
    ("cattārimāni, bhikkhave, suvidūravidūrāni! … idaṃ paṭhamaṃ suvidūravidūraṃ",
     f"“{BH}, có bốn {FAR} này! Bốn điều nào? {BH}, bầu trời và mặt đất – đây là {FAR} thứ nhất.",
     "15-sattamavaggo.md"),
    ("Tasmā sataṃ dhammo asabbhi ārakā", "Vì vậy, bản chất của người hiền thiện ở xa kẻ không hiền thiện",
     "15-sattamavaggo.md"),
    ("so evaṃ samāhite citte … abhininnāmeti", SAMAHITE_FULL, "11-tatiyavaggo.md"),
    ("tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati",
     "Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc", "11-tatiyavaggo.md"),
    ("avijjāsavāpi cittaṃ vimuccati", "tâm được giải thoát khỏi ô nhiễm vô minh", "11-tatiyavaggo.md"),
    ("Taṃ ñāṇaṃ tassa ñāṇassa ārammaṇaṃ", "hiểu biết ấy là đối tượng của hiểu biết ấy", "13-pancamavaggo.md"),
    ("Tena phassena taṃ phassaṃ phusati … tāya paññāya taṃ paññaṃ pajānāti", TEN, "13-pancamavaggo.md"),
    ("Rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ",
     f"đó là vật chất, Niết-bàn, {S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}", "17-navamavaggo.md"),
    ("idha, bhikkhave, bhikkhu", "ở đây, này các tỳ-khưu, vị tỳ-khưu", "17-navamavaggo.md"),
    ("X-ārammaṇaṃ (có … làm đối tượng)", "có điều bất tử làm đối tượng", "17-navamavaggo.md"),
    ("Samāpannassa (người đang nhập)", "người đang nhập", "10-dutiyavaggo.md"),
    ("Rūpaṃ sārammaṇantikathā («việc» for a -ti thesis)", "Bàn về việc vật chất có đối tượng", "17-navamavaggo.md"),
    ("atthi / natthi (existence thesis)", "tồn tại", "5-sabbamatthitikatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("dhammaṭṭhā", "Đứng vững trong Giáo Pháp", "15-sattamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED21 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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
        lines = list(lines)
        if i:
            lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    heading("5-21-0", 3, VAGGA)

    # ---- (126) 1. Kappaṭṭhakathā ------------------------------------------------------------------------------
    heading("5-21-1-0", 4, f"(126) 1. {S.katha(KATHA[1])}")
    add("5-654",
        f"{Q(KT)} {YES} {Q(KS[0])} {NO_PE} {Q(KT)} {YES} {Q(KS[1])} {NO_PE} {q(KT)} {YES} {Q(KS[2])} {NO_PE} "
        f"{q(KT)} {YES} {Q(KS[3])} {NO_PE}")
    add("5-655",
        f"{Q(KT)} {YES} {Q('có thể kéo dài suốt kiếp thuộc quá khứ, có thể kéo dài suốt kiếp thuộc tương lai')} "
        f"{NO_PE} {q(KT)} {YES} "
        f"{Q(f'có thể kéo dài suốt hai kiếp{PE} kéo dài suốt ba kiếp{PE} kéo dài suốt bốn kiếp')} {NO_PE}")
    add("5-656",
        f"{Q(KT)} {YES} {FIRE} {OTHER} {DEAD_Q} {DEAD_A} {Q(f'{KK} chín muồi trong các đời kế tiếp')} {NO_PE}"
        f"{NOTE656} {q(SKY)} Đúng vậy{NOTE656}. {Q(f'{KP} có thần thông')} {NO_PE} {q(f'{KP} có thần thông')} "
        f"{YES} {Q(f'{KP} {IDDHI}')} {NO_PE}")
    add("5-657",
        f"{S.na_vattabbam(KT)} {YES} {S.NANU_VUTTAM}",
        *VERSE,
        f"{S.ATTHEVA} {YES} {S.tena_hi(KT)}",
        S.katha_end(KATHA[1]))

    # ---- (127) 2. Kusalapaṭilābhakathā ------------------------------------------------------------------------
    heading("5-21-2-0", 4, VAGGA)
    heading("5-21-2-1-0", 5, f"(127) 2. {S.katha(KATHA[2])}")
    add("5-658",
        f"{Q(T2)} {YES} {Q(DANA)} {YES} {S.hanci_neg(DANA, T2)}",
        f"{Q(T2)} {YES} {Q(GIFTS)} {YES} {pe_end(S.hanci_neg(f'{KP} có thể {ROUND}', T2))}")
    add("5-659",
        f"{Q(T2P)} {YES} {Q(VUT)} {YES} {Q(HIGH)} {NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (128) 3. Anantarāpayuttakathā ------------------------------------------------------------------------
    heading("5-21-3-0", 4, VAGGA)
    heading("5-21-3-1-0", 5, f"(128) 3. {S.katha(KATHA[3])}")
    add("5-660",
        f"{Q(T3)} {YES} {Q(BOTH)} {NO_PE} {q(T3)} {YES} {NANU(DONE)} {YES} {S.hanci_neg(DONE, T3)}")
    add("5-661",
        f"{Q(ABH)} {YES} {Q(f'{PE} '.join(FIVE))} {NO_PE}",
        f"{Q(abh_w(VAR661))} {YES} {Q(f'{FIVE[0]}{PE} {FIVE[1]}{PE} {FIVE[4]}')} {NO_PE}",
        f"{Q(abh_w())} {YES} {NANU(UNDONE)} {YES} {S.hanci_neg(UNDONE, abh_w())}")
    add("5-662",
        f"{Q(T3)} {YES} {NANU(WAS)} {YES} {S.hanci_neg(WAS, T3)}",
        S.katha_end(KATHA[3]))

    # ---- (129) 4. Niyatassa niyāmakathā -----------------------------------------------------------------------
    heading("5-21-4-0", 4, VAGGA)
    heading("5-21-4-1-0", 5, f"(129) 4. {S.katha(KATHA[4])}")
    add("5-663",
        f"{Q(T4)} {YES} {Q(CROSS)} {NO_PE}",
        f"{Q(T4)} {YES} {Q(before('con đường'))} {NO_PE} "
        f"{q(before('con đường vào dòng', 'sự cố định vào dòng'))} {NO_PE} "
        f"{q(before(f'con đường trở lại một lần{PE} con đường không trở lại{PE} con đường A-la-hán', 'sự cố định A-la-hán'))} "
        f"{NO_PE}",
        f"{Q(before(f'sự thiết lập tỉnh thức{PE} nỗ lực đúng đắn{PE} nền tảng thần thông{PE} năng lực{PE} sức mạnh{PE} chi phần giác ngộ'))} "
        f"{NO_PE}")
    add("5-664",
        f"{S.na_vattabbam(T4)} {YES} {Q(BODHI)} {NO} {S.tena_hi(T4)}",
        S.katha_end(KATHA[4]))

    # ---- (130) 5. Nivutakathā / (131) 6. Sammukhībhūtakathā ---------------------------------------------------
    def lines_a(T):                   # ^5-665 / ^5-668
        return (f"{Q(T)} {YES} {Q(RATTO)} {NO_PE} {q(RAGENA)} {NO_PE}",
                f"{Q(RM)} {YES} {Q(TWO)} {NO_PE} {q(RK)} {YES} {Q(KUS)} {NO_PE}")

    def line_far(first):              # Kusalākusalā … āgacchantīti? Āmantā. Nanu vuttaṃ … tena hi na vattabbaṃ …
        return (f"{Q(first)} {YES} {S.NANU_VUTTAM} {SUT_FAR} {S.ATTHEVA} {YES} {S.tena_hi_na(KUS_S)}")

    heading("5-21-5-0", 4, VAGGA)
    heading("5-21-5-1-0", 5, f"(130) 5. {S.katha(KATHA[5])}")
    add("5-665", *lines_a(T5))
    add("5-666",
        line_far(KUS),
        f"{Q(T5)} {YES} {S.NANU_VUTTAM} “{SAMAHITE_FULL}”! {S.ATTHEVA} {YES} {pe_end(S.tena_hi_na(T5))}")
    add("5-667",
        f"{S.na_vattabbam(T5)} {YES} {S.NANU_VUTTAM} “{JANATO}”! {S.ATTHEVA} {YES} {S.tena_hi(T5)}",
        S.katha_end(KATHA[5]))

    heading("5-21-6-0", 4, VAGGA)
    heading("5-21-6-1-0", 5, f"(131) 6. {S.katha(KATHA[6])}")
    add("5-668", *lines_a(T6))
    add("5-669",
        line_far(KUS_S),
        f"{Q(T6)} {YES} {S.NANU_VUTTAM} “{SAMAHITE_S}”! {S.ATTHEVA} {YES} {S.tena_hi_na(T6)}")
    add("5-670",
        f"{S.na_vattabbam(T6)} {YES} {S.NANU_VUTTAM} “{JANATO}”! {S.ATTHEVA} {YES} {S.tena_hi(T6)}",
        S.katha_end(KATHA[6]))

    # ---- (132) 7. Samāpanno assādetikathā ---------------------------------------------------------------------
    heading("5-21-7-0", 4, VAGGA)
    heading("5-21-7-1-0", 5, f"(132) 7. {S.katha(KATHA[7])}")
    add("5-671",
        f"{Q(T7)} {YES} {Q(JJ)} {NO_PE} {q(JJ)} {YES} {Q(TEN)} {NO_PE}",
        f"{Q(JCS)} {YES} {Q(TWO)} {NO_PE}",
        f"{Q(JAK)} {YES} {Q(KUS)} {NO_PE}")
    add("5-672",
        f"{Q(KUS)} {YES} {S.NANU_VUTTAM} {SUT_FAR} {S.ATTHEVA} {YES} {S.tena_hi_na(KUS)}")
    add("5-673",
        f"{S.na_vattabbam(T7)} {YES} {S.NANU_VUTTAM} “{SUT_JH}” [{CIT['a. ni.']} 4.123]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi(T7)}",
        S.katha_end(KATHA[7]))

    # ---- (133) 8. Asātarāgakathā ------------------------------------------------------------------------------
    heading("5-21-8-0", 4, VAGGA)
    heading("5-21-8-1-0", 5, f"(133) 8. {S.katha(KATHA[8])}")
    add("5-674",
        f"{Q(T8)} {YES} {Q(delight(DK))} {NO_PE} {nanu(delight(SK))} {YES} {S.hanci_neg(delight(SK), T8)}",
        f"{Q(T8)} {YES} {Q(lie(DKV, SKV))} {NO_PE} {nanu(lie(SKV, DKV))} {YES} {S.hanci_neg(lie(SKV, DKV), T8)}")
    add("5-675",
        f"{S.na_vattabbam(T8)} {YES} {S.NANU_VUTTAM} “{SUT_AR}” {CIT675}! {S.ATTHEVA} {YES} {S.tena_hi(T8)}",
        S.katha_end(KATHA[8]))

    # ---- (134) 9. Dhammataṇhā abyākatātikathā -----------------------------------------------------------------
    heading("5-21-9-0", 4, VAGGA)
    heading("5-21-9-1-0", 5, f"(134) 9. {S.katha(KATHA[9])}")
    add("5-676",
        f"{Q(T9)} {YES} {Q(VIPAKA)} {NO_PE}",
        f"{Q(T9)} {YES} {Q(ab(RT))} {NO_PE} {q(T9)} {YES} {Q(ab(LONG4))} {NO_PE}",
        f"{Q(ak(RT))} {YES} {Q(ak(DT))} {NO_PE} {q(ak(SHORT2))} {YES} {Q(ak(DT))} {NO_PE}")
    add("5-677",
        f"{Q(T9)} {YES} {NANU(SAID_T)} {YES} {S.hanci_neg(SAID_T, T9)}",
        f"{Q(T9)} {YES} {NANU(SAID_L)} {YES} {S.hanci_neg(SAID_L, T9)}")
    add("5-678",
        f"{Q(lob(DT, AB))} {YES} {Q(lob(RT, AB))} {NO_PE} {q(lob(DT, AB))} {YES} {Q(lob(SHORT2, AB))} {NO_PE}",
        f"{Q(lob(RT, AK))} {YES} {Q(lob(DT, AK))} {NO_PE} {q(lob(SHORT2, AK))} {YES} {Q(lob(DT, AK))} {NO_PE}")
    add("5-679",
        f"{Q(T9)} {YES} {S.NANU_VUTTAM} {SUT_T} [Đại Phẩm 14; Trường Bộ Kinh 2.400]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi_na(T9)}")
    add("5-680",
        f"{S.na_vattabbam(T9)} {YES} {NANU(SA_DT)} {YES} {S.hanci(SA_DT, T9)}",
        S.katha_end(KATHA[9]))

    # ---- (135) 10. Dhammataṇhā na dukkhasamudayotikathā -------------------------------------------------------
    heading("5-21-10-0", 4, VAGGA)
    heading("5-21-10-1-0", 5, f"(135) 10. {S.katha(KATHA[10])}")
    add("5-681",
        f"{Q(T10)} {YES} {Q(na_sam(RT))} {NO_PE} {q(T10)} {YES} {Q(na_sam(LONG4))} {NO_PE}",
        f"{Q(sam(RT))} {YES} {Q(sam(DT))} {NO_PE} {q(sam(LONG4))} {YES} {Q(sam(DT))} {NO_PE}")
    add("5-682",
        f"{Q(T10)} {YES} {NANU(SAID_TS)} {YES} {S.hanci_neg(SAID_TS, T10)} "
        f"{Q(T10)} {YES} {NANU(SAID_LS)} {YES} {S.hanci_neg(SAID_LS, T10)}")
    add("5-683",
        f"{Q(lob_na(DT))} {YES} {Q(lob_na(RT))} {NO_PE} {q(lob_na(DT))} {YES} {Q(lob_na(LONG4))} {NO_PE}",
        f"{Q(lob(RT, SAM))} {YES} {Q(lob(DT, SAM))} {NO_PE} {q(lob(SHORT2, SAM))} {YES} {Q(lob(DT, SAM))} {NO_PE}")
    add("5-684",
        f"{Q(T10)} {YES} {S.NANU_VUTTAM} {SUT_T}! {S.ATTHEVA} {YES} {S.tena_hi_na(T10)}")
    add("5-685",
        f"{S.na_vattabbam(T10)} {YES} {NANU(SA_DT)} {YES} {S.hanci(SA_DT, T10)}",
        S.katha_end(KATHA[10]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Lookup helper (finished pi-5 rails chapters only)
# ---------------------------------------------------------------------------------------------------------------
def _lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def find(pat, maxhits=8, maxc=700):
    rx = re.compile(pat)
    hits = 0
    for name in FINISHED:
        pl, vl = _lines(S.PALI_DIR / name), _lines(S.OUT_DIR / name)
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if not m:
                continue
            s = max(0, m.start() - 100)
            print(f"[{name} line {i + 1}]")
            print("  PI:", ln[s:s + 400])
            print("  VI:", (vl[i] if i < len(vl) else "<missing>")[:maxc])
            hits += 1
            if hits >= maxhits:
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
    adh = S.FORMULAS_MD.parent / "adh-21"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "find":
        find(sys.argv[2], *(int(x) for x in sys.argv[3:]))
    else:
        main()
