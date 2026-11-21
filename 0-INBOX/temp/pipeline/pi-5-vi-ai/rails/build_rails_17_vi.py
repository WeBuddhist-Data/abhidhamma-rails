"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 17, Navamavaggo (^5-17-0 … ^5-570): eleven kathās
(84-94) with the repeated "Navamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/17-navamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, katha, katha_end, vaggo, CIT …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED17);
strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-17.md.

usage: python -I -X utf8 -B build_rails_17_vi.py          (writes the chapter and the adherence copy rails\\adh-17\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "17-navamavaggo.md"
Q, q, NANU, PE, YES, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO_PE
cap, RE, CIT = S.cap, S.RE, S.CIT


def nanu(x):                          # …pe… nanu Xti? (lower case after …pe…)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Core words (termbase; pi-1 / pi-2; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
NA, SA = "không có đối tượng", "có đối tượng"          # anārammaṇa / sārammaṇa (pi-1, termbase)
R = "vật chất"                                         # rūpaṃ (termbase «vật chất»)
AM = "điều bất tử"                                     # amataṃ (termbase)
NIB = "Niết-bàn"                                       # nibbānaṃ
SKH = "các tạo tác"                                    # saṅkhāre (termbase «tạo tác»; sample)
SK = "khối tạo tác"                                    # saṅkhārakkhandho (pi-2)
V3 = "khối cảm giác, khối tri giác, khối thức"         # vedanā- saññā- viññāṇakkhandho (pi-2)
IN = "nằm trong khối tạo tác"                          # saṅkhārakkhandhapariyāpanna (APPROVED pariyāpanna)
WHICH = "Nằm trong khối nào? Nằm trong khối tạo tác."  # Katamakkhandhapariyāpanno(-ṃ)ti? Saṅkhārakkhandhapariyāpanno(-ṃ)ti.
BASES = f"đó là {R}, {NIB}, {S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}"
#   Rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatananti?  («đó là» supplied, ch11)
TWO = "có sự tụ hợp của hai sự tiếp xúc… hai tâm"     # Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti (ch10/11)


def part(x):                          # X ekadeso sārammaṇo ekadeso anārammaṇo
    return f"{x} một phần {SA}, một phần {NA}"


def inn(x, obj):                      # X saṅkhārakkhandhapariyāpanno (an)ārammaṇo
    return f"{x} {IN} thì {obj}"


# ---- (84) Ānisaṃsadassāvī ---------------------------------------------------------------------------------------
TH1 = "đối với người thấy lợi ích, có sự dứt bỏ các xiềng xích"   # ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ
NIB_SEE = f"là người thấy lợi ích nơi {NIB}"                   # nibbāne ānisaṃsadassāvī hoti
ANICCA_ETC = ["là khổ đau", "là bệnh tật", "là ung nhọt", "là mũi tên", "là điều bất hạnh", "là sự đau ốm",
              "là cái xa lạ", "là cái tan rã", "là tai họa", "là tai ương", "là điều đáng sợ", "là tai nạn",
              "là cái dao động", "là cái dễ vỡ", "là cái không bền vững", "là cái không phải nơi che chở",
              "là cái không phải nơi ẩn náu", "là cái không phải nơi nương tựa",
              "là cái không trở thành nơi nương tựa", "là cái rỗng không", "là cái hư rỗng", "là cái trống rỗng",
              "là cái không phải tự ngã", "là sự nguy hại"]
#   dukkhato rogato gaṇḍato sallato aghato ābādhato parato palokato ītito upaddavato bhayato upasaggato calato
#   pabhaṅguto addhuvato atāṇato aleṇato asaraṇato asaraṇībhūtato rittato tucchato suññato anattato ādīnavato
VIP = "là có bản chất biến đổi"                         # vipariṇāmadhammato (termbase)
ANICCA = "là vô thường"                                 # aniccato (termbase)
LONG = f"{PE} ".join(ANICCA_ETC) + f"{PE} {VIP}"       # dukkhato…pe… rogato… … ādīnavato…pe… vipariṇāmadhammato


def man(x):                           # saṅkhāre X manasikaroto saṃyojanā pahīyanti
    return f"đối với người chú tâm đến {SKH} {x}, các xiềng xích được dứt bỏ"


def both(x):                          # saṅkhāre ca X manasi karoti nibbāne ca ānisaṃsadassāvī hoti (ch11 «vừa … vừa»)
    return f"vừa chú tâm đến {SKH} {x}, vừa {NIB_SEE}"


SUT_A = (f"ở đây, này các tỳ-khưu, vị tỳ-khưu sống quán sát hạnh phúc nơi {NIB}, có tri giác về hạnh phúc, "
         f"là người cảm nhận hạnh phúc, thường xuyên, liên tục, liền mạch, dứt khoát hướng đến bằng tâm, "
         f"đi sâu vào bằng trí tuệ")
#   idha, bhikkhave, bhikkhu nibbāne sukhānupassī viharati sukhasaññī sukhapaṭisaṃvedī, satataṃ samitaṃ
#   abbokiṇṇaṃ cetasā adhimuccamāno paññāya pariyogāhamāno   (sukha here happiness: APPROVED §2)

# ---- (85) Amatārammaṇa ------------------------------------------------------------------------------------------
AMS = f"xiềng xích có {AM} làm đối tượng"              # amatārammaṇaṃ saṃyojanaṃ (termbase «có … làm đối tượng»)
SY = ["là đối tượng của xiềng xích", "là đối tượng của nút thắt", "là đối tượng của dòng lũ",
      "là đối tượng của ách", "là đối tượng của chướng ngại", "bị sự hiểu sai lệch nắm giữ",
      "là đối tượng của sự bám víu", "là đối tượng của phiền não"]          # saṃyojaniyaṃ … saṃkilesiyaṃ (pi-1, ch11)
SY_N = ["không phải là đối tượng của xiềng xích", "không phải là đối tượng của nút thắt",
        "không phải là đối tượng của dòng lũ", "không phải là đối tượng của ách",
        "không phải là đối tượng của chướng ngại", "không bị sự hiểu sai lệch nắm giữ",
        "không phải là đối tượng của sự bám víu", "không phải là đối tượng của phiền não"]   # (pi-1, ch8)
RAGA = ["khơi dậy sự tham đắm", "hấp dẫn", "đáng ham muốn", "làm say đắm", "trói buộc", "làm mê mẩn"]   # (ch10)
RAGA_N = ["không " + x for x in RAGA]                                        # (ch10)
DOSA = ["khơi dậy sự sân hận", "khơi dậy sự phẫn nộ", "khơi dậy ác cảm"]   # dosa- kopa- paṭighaṭṭhāniyaṃ
DOSA_N = ["không " + x for x in DOSA]
MOHA = ["khơi dậy sự si mê", "tạo ra sự không biết", "làm cho không có mắt", "làm chấm dứt trí tuệ",
        "thuộc về phía gây phiền não", "không dẫn đến Niết-bàn"]
#   mohaṭṭhāniyaṃ aññāṇakaraṇaṃ acakkhukaraṇaṃ paññānirodhiyaṃ vighātapakkhiyaṃ anibbānasaṃvattaniyaṃ
MOHA_N = ["không khơi dậy sự si mê", "không tạo ra sự không biết", "không làm cho không có mắt",
          "làm tăng trưởng trí tuệ", "không thuộc về phía gây phiền não", "dẫn đến Niết-bàn"]
#   na mohaṭṭhāniyaṃ na aññāṇakaraṇaṃ na acakkhukaraṇaṃ paññābuddhiyaṃ avighātapakkhiyaṃ nibbānasaṃvattaniyaṃ
FET, RAGO, DOSO, MOHO = "các xiềng xích", "sự tham đắm", "sự sân hận", "sự si mê"


def arise(x, obj=AM):                 # obj ārabbha X uppajjati / uppajjanti
    return f"khi lấy {obj} làm đối tượng, {x} sinh khởi"
#   termbase ārabbha «lấy … làm đối tượng», Rūpaṃ ārabbha «khi lấy vật chất làm đối tượng», rāgo uppajjati «sự tham
#   đắm sinh khởi»; the same «khi lấy … làm đối tượng» as ārabbha paṇidhi in (89)


def full(lst):
    return ", ".join(lst)


def fl(lst, two=False):               # first (two)…pe… last
    head = f"{lst[0]}, {lst[1]}" if two else lst[0]
    return f"{head}{PE} {lst[-1]}"


SUT_M = (f"nhận ra {NIB} là {NIB}, sau khi nhận ra {NIB} là {NIB}, tưởng tượng về {NIB}, tưởng tượng trong {NIB}, "
         f"tưởng tượng từ {NIB}, tưởng tượng rằng {NIB} là của tôi, hoan hỷ với {NIB}")
#   nibbānaṃ nibbānato sañjānāti, … nibbānaṃ meti maññati, nibbānaṃ abhinandati

# ---- (86) Rūpaṃ sārammaṇaṃ --------------------------------------------------------------------------------------
RS = f"{R} {SA}"                                        # rūpaṃ sārammaṇaṃ
AV7 = "sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong ước, sự mong cầu"
#   āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi (pi-2 first four; termbase)
AV3 = f"sự hướng đến, sự chú hướng{PE} sự mong cầu"     # āvaṭṭanā ābhogo…pe… paṇidhi
AV2 = f"sự hướng đến{PE} sự mong cầu"                  # āvaṭṭanā…pe… paṇidhi
PH = "sự tiếp xúc"                                      # phasso
MENT = (f"cảm giác{PE} tri giác, chủ ý, tâm, niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ, sự tham đắm, "
        f"sự sân hận, sự si mê, sự kiêu mạn, quan điểm, sự hoài nghi, sự uể oải, sự xao động, "
        f"sự không biết hổ thẹn{PE} sự không biết ghê sợ tội lỗi")
#   Vedanā…pe… saññā cetanā cittaṃ saddhā vīriyaṃ sati samādhi paññā rāgo doso moho māno diṭṭhi vicikicchā thinaṃ
#   uddhaccaṃ ahirikaṃ…pe… anottappaṃ (ch13 list words)
MENT_S = f"cảm giác{PE} sự không biết ghê sợ tội lỗi"   # Vedanā…pe… anottappaṃ

# ---- (87) / (88) anārammaṇa ---------------------------------------------------------------------------------------
AN = f"các khuynh hướng tiềm ẩn {NA}"                   # anusayā anārammaṇā
KRA = "khuynh hướng tiềm ẩn tham đắm dục lạc"           # kāmarāgānusayo (pi-2)
KR = "sự tham đắm dục lạc"                              # kāmarāgo (pi-1)
KR6 = (f"{KR}, sự ám ảnh của tham đắm dục lạc, xiềng xích tham đắm dục lạc, dòng lũ dục lạc, ách dục lạc, "
       f"chướng ngại ý muốn dục lạc")
#   kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmogho kāmayogo kāmacchandanīvaraṇaṃ (pi-1, termbase)
ANU6 = ("khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, khuynh hướng tiềm ẩn quan điểm, "
        "khuynh hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm hiện hữu, khuynh hướng tiềm ẩn vô minh")
#   paṭighānusayo … avijjānusayo (pi-2)
AVA = "khuynh hướng tiềm ẩn vô minh"                    # avijjānusayo (pi-1, pi-2)
AVJ = "vô minh"                                         # avijjā
AV7L = (f"{AVJ}, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, "
        f"xiềng xích vô minh, chướng ngại vô minh")
#   avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjāsaṃyojanaṃ avijjānīvaraṇaṃ (pi-1)
AV7S = f"{AVJ}, dòng lũ vô minh{PE} chướng ngại vô minh"   # avijjā avijjogho…pe… avijjānīvaraṇaṃ
NAN = f"hiểu biết {NA}"                                 # ñāṇaṃ anārammaṇaṃ
NANA = "hiểu biết"                                      # ñāṇaṃ
PANNA = "trí tuệ"                                       # paññā
PANNA5 = (f"{PANNA}, {S.I['paññindriya']}, sức mạnh trí tuệ, quan điểm đúng đắn, "
          f"chi phần giác ngộ là sự tìm hiểu các hiện tượng")
#   paññā paññindriyaṃ paññābalaṃ sammādiṭṭhi dhammavicayasambojjhaṅgo (pi-1)
PUTH = "người phàm phu, khi tâm thiện hoặc không xác định về mặt đạo đức đang diễn ra, nên gọi là"
#   Puthujjano kusalābyākate citte vattamāne …ti vattabbo
ARC = "bậc A-la-hán, người có được thức qua mắt, nên gọi là"   # Arahā cakkhuviññāṇasamaṅgī …ti vattabbo

# ---- (89) Atītānāgatārammaṇa --------------------------------------------------------------------------------------
T = {"a": "quá khứ", "f": "tương lai", "p": "hiện tại"}  # atīta / anāgata / paccuppanna (termbase, ch5)


def ac(t):                            # X-ārammaṇaṃ cittaṃ (termbase «có đối tượng thuộc X»)
    return f"tâm có đối tượng thuộc {T[t]}"


def adv(t, av=AV2):                   # X-ṃ ārabbha atthi āvaṭṭanā…pe… paṇidhi (termbase «khi lấy … làm đối tượng»)
    return f"khi lấy {T[t]} làm đối tượng, có {av}"


def par(t, obj):                      # X-ṃ ārabbha atthi …, X-ārammaṇaṃ cittaṃ (an)ārammaṇaṃ
    return f"{adv(t)}, {ac(t)} thì {obj}"


ATN = f"tâm có đối tượng thuộc quá khứ và tương lai thì {NA}"   # atītānāgatārammaṇaṃ cittaṃ anārammaṇaṃ

# ---- (90) Vitakkānupatita ---------------------------------------------------------------------------------------
VT = "tất cả tâm đều có sự hướng tâm đi theo"           # sabbaṃ cittaṃ vitakkānupatitaṃ (termbase)
FOLLOW = ["sự duy trì tâm", "sự hân hoan", "sự dễ chịu", "sự khó chịu", "niềm vui", "nỗi buồn", "sự bình thản",
          "niềm tin", "sự tinh tấn", "sự tỉnh thức", "sự định tâm", "trí tuệ", "sự tham đắm", "sự sân hận"]
#   vicāra- pīta- sukha- dukkha- somanassa- domanassa- upekkhā- saddhā- vīriya- sata- samādha- paññā- rāga- dosa-
#   (sukha / dukkha as feelings: APPROVED §2 «sự dễ chịu» / «sự khó chịu»)
SAM0 = "định tâm có sự hướng tâm và sự duy trì tâm"                       # savitakko savicāro samādhi (pi-2)
SAM1 = "định tâm không có sự hướng tâm, chỉ có sự duy trì tâm"           # avitakko vicāramatto samādhi (pi-2)
SAM2 = "định tâm không có sự hướng tâm cũng không có sự duy trì tâm"     # avitakko avicāro samādhi (pi-2)
SAM3 = f"Đức Thế Tôn đã nói đến ba loại định tâm – {SAM0}, {SAM1}, {SAM2}"  # tayo samādhī vuttā bhagavatā – … (ch11)

# ---- (91) Vitakkavipphārasadda ------------------------------------------------------------------------------------
TH8 = "trong mọi trường hợp, khi hướng tâm, duy trì tâm, thì sự lan tỏa của sự hướng tâm là âm thanh"
#   sabbaso vitakkayato vicārayato vitakkavipphāro saddo (termbase phrases)
SEVEN = [("tiếp xúc", "sự tiếp xúc"), ("cảm nhận", "cảm giác"), ("nhận ra", "tri giác"), ("cố ý", "chủ ý"),
         ("suy nghĩ", "tâm"), ("nhớ", "sự tỉnh thức"), ("hiểu rõ", "trí tuệ")]
#   phusayato phassa- / vedayato vedanā- / sañjānato saññā- / cetayato cetanā- / cintayato citta- / sarato sati- /
#   pajānato paññāvipphāro saddo
VS = "âm thanh lan tỏa của sự hướng tâm"               # vitakkavipphāro saddo (subject; kathā name)
EAR = "được nhận biết bằng tai, va chạm vào tai, đi vào tầm của tai"      # (ch10)
EAR_N = "không được nhận biết bằng tai, không va chạm vào tai, không đi vào tầm của tai"

# ---- (92) / (93) Na yathācittassa ----------------------------------------------------------------------------------
NV = "lời nói không tùy theo tâm"                       # na yathācittassa vācā
NK = "nghiệp bằng thân không tùy theo tâm"              # na yathācittassa kāyakammaṃ
V = "lời nói"
K = "nghiệp bằng thân"                                  # kāyakammaṃ (termbase)
HAVE5 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm"]   # (a)phassaka- (a)vedanaka- … (a)cittakassa
VAR = (" [khác chính tả (Pī.): anāvaṭṭantassa; dị bản (Sī., Syā., Ka.): anāvajjantassa; "
       "Các vấn đề tranh luận 484, cần xem]")
#   [anāvaṭṭantassa (pī.), anāvajjantassa (sī. syā. ka.) kathā. 484 passitabbaṃ]


def of(x, who):                       # X-assa vācā / kāyakammaṃ
    return f"{x} của người {who}"


def born(x):                          # X cittasamuṭṭhānā cittena sahajātā cittena saha ekuppādā
    return f"{x} do tâm sinh ra, cùng sinh với tâm, cùng sinh khởi một lúc với tâm"


SPEAK = ["phát biểu", "kể", "trò chuyện", "nói"]        # bhaṇati katheti ālapati voharati (termbase; voharati: report)
WALK = ["đi tới", "đi lui", "nhìn thẳng", "nhìn quanh", "co lại", "duỗi ra"]   # (pi-2, ch14)


def wish_n(vs):                       # na X-tukāmo X-ti, …
    return ", ".join(f"không muốn {v} mà {v}" for v in vs)


def wish(vs):                         # X-tukāmo X-ti, …
    return ", ".join(f"muốn {v} thì {v}" for v in vs)


def other(v, obj="điều này", obj2="điều khác"):   # "aññaṃ X-issāmī"ti aññaṃ X-ti (termbase Aññaṃ «điều này»)
    return f"nghĩ “tôi sẽ {v} {obj}” mà {v} {obj2}"


SAY4 = [other("phát biểu"), other("kể"), other("trò chuyện", "về điều này", "về điều khác"), other("nói")]
GO = "nghĩ “tôi sẽ đi đến chỗ này” mà đi đến nơi khác"  # "aññatra gacchissāmī"ti aññatra gacchati
STRETCH = "nghĩ “tôi sẽ duỗi cái này” mà duỗi ra cái khác"   # "aññaṃ pasāressāmī"ti aññaṃ pasāreti (termbase)

# ---- (94) Atītānāgatasamannāgata -----------------------------------------------------------------------------------
SAMN = "người ta được trang bị"                         # (subjectless) samannāgato (termbase «được trang bị»)
ATS = f"{SAMN} quá khứ và tương lai"                    # atītānāgatehi samannāgato
PAST5 = "đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn"            # (ch5)
FUT6 = "chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra"   # (ch5)
JH = ("có người tu thiền với tám sự giải thoát, đạt được bốn tầng thiền theo ý muốn, "
      "đạt được chín thành tựu thiền an trú tuần tự")
#   atthi aṭṭhavimokkhajhāyī catunnaṃ jhānānaṃ nikāmalābhī navannaṃ anupubbavihārasamāpattīnaṃ lābhī


def three(x):                         # atītena X samannāgato, anāgatena X samannāgato, paccuppannena X samannāgato
    return f"{SAMN} {x} thuộc quá khứ, được trang bị {x} thuộc tương lai, được trang bị {x} thuộc hiện tại"


# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(9)                                     # Navamavaggo «Chương thứ chín» (termbase)
KATHA = {1: "người thấy lợi ích", 2: f"{AM} làm đối tượng", 3: f"việc {RS}", 4: f"việc {AN}", 5: f"việc {NAN}",
         6: "đối tượng thuộc quá khứ và tương lai", 7: "điều có sự hướng tâm đi theo", 8: VS, 9: f"việc {NV}",
         10: f"việc {NK}", 11: "sự được trang bị quá khứ và tương lai"}
#   Ānisaṃsadassāvī-, Amatārammaṇa- (ch13 Cittārammaṇakathā), Rūpaṃ sārammaṇanti-, Anusayā anārammaṇa(ti)-,
#   Ñāṇaṃ anārammaṇanti-, Atītānāgatārammaṇa- (termbase), Vitakkānupatita- (termbase), Vitakkavipphārasadda-,
#   Na yathācittassa vācāti-, Na yathācittassa kāyakammanti-, Atītānāgatasamannāgatakathā (ch12 Samannāgatakathā)
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)
UDDANA = "; ".join([cap(TH1), AMS, RS, AN, f"cũng vậy với {NANA}", "tâm có đối tượng thuộc quá khứ và tương lai",
                    VT, TH8, NV, f"cũng vậy với {K}", ATS]) + "."
#   Ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ, amatārammaṇaṃ saṃyojanaṃ, rūpaṃ sārammaṇaṃ, anusayā anārammaṇā,
#   evamevaṃ ñāṇaṃ, atītānāgatārammaṇaṃ cittaṃ, sabbaṃ cittaṃ vitakkānupatitaṃ, sabbaso vitakkayato vicārayato
#   vitakkavipphāro saddo, na yathācittassa vācā, tatheva kāyakammaṃ atītānāgatehi samannāgatoti.
#   (items separated by «;» because several items carry their own commas: reported)

REUSED17 = [  # (Pāli, Vietnamese, book)
    ("saṃyojaniyaṃ (rūpakaṇḍa list)", "là đối tượng của xiềng xích", "1"),
    ("ganthaniyaṃ", "là đối tượng của nút thắt", "1"), ("oghaniyaṃ", "là đối tượng của dòng lũ", "1"),
    ("yoganiyaṃ", "là đối tượng của ách", "1"), ("nīvaraṇiyaṃ", "là đối tượng của chướng ngại", "1"),
    ("parāmaṭṭhaṃ", "bị sự hiểu sai lệch nắm giữ", "1"), ("upādāniyaṃ", "là đối tượng của sự bám víu", "1"),
    ("aparāmaṭṭhā", "không bị sự hiểu sai lệch nắm giữ", "1"),
    ("anupādāniyā", "không phải là đối tượng của sự bám víu", "1"),
    ("cittasamuṭṭhānā", "do tâm sinh ra", "1"), ("anārammaṇaṃ", "không có đối tượng", "1"),
    ("sappaccayaṃ", "có điều kiện", "1"),
    ("paññābalaṃ", "sức mạnh trí tuệ", "1"),
    ("dhammavicayasambojjhaṅgo", "chi phần giác ngộ là sự tìm hiểu các hiện tượng", "1"),
    ("avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ",
     "vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh", "1"),
    ("kāmarāgasaṃyojanaṃ", "xiềng xích tham đắm dục lạc", "1"), ("avijjāsaṃyojanaṃ", "xiềng xích vô minh", "1"),
    ("kāmacchandanīvaraṇaṃ", "chướng ngại ý muốn dục lạc", "1"), ("avijjānīvaraṇaṃ", "chướng ngại vô minh", "1"),
    ("kāmarāgo", KR, "1"), ("savitakkasavicāra", "có sự hướng tâm và sự duy trì tâm", "1"),
    ("paṭighānusayo … avijjānusayo", ANU6, "2"), ("Kāmarāgānusayo", KRA, "2"),
    ("Tayo samādhī – savitakkasavicāro … avitakkaavicāro samādhi", f"{SAM0}, {SAM1}, {SAM2}", "2"),
    ("savitakko savicāro samādhi / avitakko avicāro samādhi", SAM2, "2"),
    ("navasu anupubbavihārasamāpattīsu", "chín thành tựu thiền an trú tuần tự", "2"),
    ("āvaṭṭanā ābhogo samannāhāro manasikāro", "sự hướng đến, sự chú hướng, sự lưu ý", "2"),
    ("rūpakkhandha … (aggregate names)", "khối cảm giác, khối tri giác, khối tạo tác, khối thức", "2"),
    ("abhikkamati paṭikkamati", "khi đi tới, khi đi lui", "2"), ("āloketi viloketi", "khi nhìn thẳng, khi nhìn quanh", "2"),
    ("aṭṭha vimokkhe", "tám sự giải thoát", "4"), ("nikāmalābhī", "theo ý muốn", "4"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("rāgaṭṭhāniyo rajanīyo kamanīyo madanīyo bandhanīyo mucchanīyo", full(RAGA), "10-dutiyavaggo.md"),
    ("na rāgaṭṭhāniyo … na mucchanīyo", full(RAGA_N), "10-dutiyavaggo.md"),
    ("sotaviññeyyo, sotasmiṃ paṭihaññati, sotassa āpāthaṃ āgacchati", EAR, "10-dutiyavaggo.md"),
    ("Dvinnaṃ phassānaṃ … samodhānaṃ hoti", "có sự tụ hợp của hai sự tiếp xúc", "10-dutiyavaggo.md"),
    ("passitabbaṃ (in a citation bracket)", ", cần xem]", "10-dutiyavaggo.md"),
    ("Xñca manasi karoti, Yñca manasi karoti", "vừa chú tâm đến", "11-tatiyavaggo.md"),
    ("saṃyojaniyaṃ ganthaniyaṃ … saṃkilesiyaṃ", full(SY), "11-tatiyavaggo.md"),
    ("tīṇi cakkhūni vuttāni bhagavatā –", "Đức Thế Tôn đã nói đến ba loại", "11-tatiyavaggo.md"),
    ("asaṃyojaniyaṃ…pe… asaṃkilesikaṃ", "không phải là đối tượng của xiềng xích… không phải là đối tượng của phiền não",
     "8-satipatthanakatha.md"),
    ("niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ", PAST5, "5-sabbamatthitikatha.md"),
    ("ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ", FUT6, "5-sabbamatthitikatha.md"),
    ("…nti micchā", "sai khi nói rằng", "5-sabbamatthitikatha.md"),
    ("Hañci vā pana", "Hoặc nếu", "1-puggalakatha.md"),
    ("Cittārammaṇakathā", "Bàn về tâm làm đối tượng", "13-pancamavaggo.md"),
    ("anottappa (list)", "sự không biết ghê sợ tội lỗi", "13-pancamavaggo.md"),
    ("sabbasaṅkhāre aniccato diṭṭhe", "tất cả các tạo tác được thấy là vô thường", "13-pancamavaggo.md"),
    ("tatheva kāyakammaṃ (uddāna)", f"cũng vậy với {K}", "14-chatthavaggo.md"),
    ("Samannāgatakathā", "Bàn về sự được trang bị", "12-catutthavaggo.md"),
    ("Navamavaggo / … (S.vaggo)", "Chương thứ hai", "10-dutiyavaggo.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED17 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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

    heading("5-17-0", 3, VAGGA)

    # ---- (84) 1. Ānisaṃsadassāvīkathā -------------------------------------------------------------------------
    heading("5-17-1-0", 4, f"(84) 1. {S.katha(KATHA[1])}")
    add("5-547",
        f"{Q(TH1)} {YES} {NANU(man(ANICCA))} {YES} {S.hanci_neg(man(ANICCA), TH1)}",
        f"{NANU(man(LONG))} {YES} {S.hanci_neg(man(VIP), TH1)}",
        f"{Q(both(ANICCA))} {NO_PE} {q(both(ANICCA))} {YES} {Q(TWO)} {NO_PE} "
        f"{q(both(f'là khổ đau{PE} {VIP}'))} {NO_PE} {q(both(VIP))} {YES} {Q(TWO)} {NO_PE}")
    add("5-548",
        f"{S.na_vattabbam(TH1)} {YES} {S.NANU_VUTTAM} “{SUT_A}” [{CIT['a. ni.']} 7.19]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi(TH1)}",
        S.katha_end(KATHA[1]))

    # ---- (85) 2. Amatārammaṇakathā ----------------------------------------------------------------------------
    heading("5-17-2-0", 4, VAGGA)
    heading("5-17-2-1-0", 5, f"(85) 2. {S.katha(KATHA[2])}")
    add("5-549",
        f"{Q(AMS)} {YES} {Q(f'{AM} {full(SY)}')} {NO_PE} {nanu(f'{AM} {fl(SY_N, True)}')} {YES} "
        f"{S.hanci_neg(f'{AM} {fl(SY_N)}', AMS)}",
        f"{Q(arise(RAGO))} {YES} {Q(f'{AM} {full(RAGA)}')} {NO_PE} {nanu(f'{AM} {full(RAGA_N)}')} {YES} "
        f"{S.hanci_neg(f'{AM} {full(RAGA_N)}', arise(RAGO))}",
        f"{Q(arise(DOSO))} {YES} {Q(f'{AM} {full(DOSA)}')} {NO_PE} {nanu(f'{AM} {full(DOSA_N)}')} {YES} "
        f"{S.hanci_neg(f'{AM} {full(DOSA_N)}', arise(DOSO))}",
        f"{Q(arise(MOHO))} {YES} {Q(f'{AM} {full(MOHA)}')} {NO_PE} {nanu(f'{AM} {full(MOHA_N)}')} {YES} "
        f"{S.hanci_neg(f'{AM} {fl(MOHA_N, True)}', arise(MOHO))}")

    def pair(x, lst_r, lst_a, yes_first=R):
        """X ārabbha … uppajjati, X <list>ti? Āmantā. Y ārabbha …, Y <list>ti? Na hevaṃ vattabbe…pe…."""
        other_ = AM if yes_first == R else R
        return (f"{Q(f'{arise(x, yes_first)}, {yes_first} {lst_r}')} {YES} "
                f"{Q(f'{arise(x, other_)}, {other_} {lst_a}')} {NO_PE}")

    add("5-550",
        pair(FET, fl(SY, True), fl(SY)),
        pair(RAGO, full(RAGA), fl(RAGA)),
        pair(DOSO, full(DOSA), full(DOSA)),
        pair(MOHO, fl(MOHA, True), fl(MOHA, True)),
        pair(FET, full(SY_N), fl(SY_N, True), yes_first=AM),
        pair(RAGO, full(RAGA_N), fl(RAGA_N), yes_first=AM),
        pair(DOSO, full(DOSA_N), full(DOSA_N), yes_first=AM),
        pair(MOHO, fl(MOHA_N, True), fl(MOHA_N, True), yes_first=AM))
    add("5-551",
        f"{S.na_vattabbam(AMS)} {YES} {S.NANU_VUTTAM} “{SUT_M}” [{CIT['ma. ni.']} 1.6]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi(AMS)}",
        S.katha_end(KATHA[2]))

    # ---- (86) 3. Rūpaṃ sārammaṇantikathā ----------------------------------------------------------------------
    heading("5-17-3-0", 4, VAGGA)
    heading("5-17-3-1-0", 5, f"(86) 3. {S.katha(KATHA[3])}")
    add("5-552",
        f"{Q(RS)} {YES} {Q(f'nó có {AV7}')} {NO_PE} {nanu(f'nó không có {AV3}')} {YES} "
        f"{S.hanci_neg(f'nó không có {AV3}', RS)}",
        f"{Q(f'{PH} {SA}, nó có {AV3}')} {YES} {Q(f'{RS}, nó có {AV3}')} {NO_PE}",
        f"{Q(f'{MENT} {SA}, nó có {AV3}')} {YES} {Q(f'{RS}, nó có {AV3}')} {NO_PE}",
        f"{Q(f'{RS}, nó không có {AV3}')} {YES} {Q(f'{PH} {SA}, nó không có {AV3}')} {NO_PE}",
        f"{Q(f'{RS}, nó không có {AV3}')} {YES} {Q(f'{MENT_S} {SA}, nó không có {AV3}')} {NO_PE}")
    COND = f"{R} có điều kiện"                                   # rūpaṃ sappaccayaṃ (termbase)
    add("5-553",
        f"{S.na_vattabbam(RS)} {YES} {NANU(COND)} {YES} {S.hanci(COND, RS)}",
        S.katha_end(KATHA[3]))

    # ---- (87) 4. Anusayā anārammaṇakathā ----------------------------------------------------------------------
    heading("5-17-4-0", 4, VAGGA)
    heading("5-17-4-1-0", 5, f"(87) 4. {S.katha(KATHA[4])}")

    def khandha_lines(subj, kin, kin_list_na, kin_list_sa, first=None):
        """The four lines of the anusaya / ñāṇa refutation via the formation aggregate (^5-554 … 555)."""
        l1 = first or (f"{Q(f'{subj} {NA}')} {YES} {Q(f'{kin_list_na} {NA}')} {NO_PE} "
                       f"{q(f'{kin_list_sa} {SA}')} {YES} {Q(f'{subj} {SA}')} {NO_PE}")
        l2 = (f"{Q(f'{subj} {NA}')} {YES} {WHICH} {Q(f'{SK} {NA}')} {NO_PE} {q(f'{SK} {NA}')} {YES} "
              f"{Q(f'{V3} {NA}')} {NO_PE}")
        l3 = (f"{Q(inn(subj, NA))} {YES} {Q(inn(kin, NA))} {NO_PE} {q(inn(kin, SA))} {YES} {Q(inn(subj, SA))} "
              f"{NO_PE}")
        l4 = (f"{Q(f'{inn(subj, NA)}, {inn(kin, SA)}')} {YES} {Q(part(SK))} {NO_PE} {q(part(SK))} {YES} "
              f"{Q(part(V3))} {NO_PE}")
        return l1, l2, l3, l4

    l1, l2, l3, l4 = khandha_lines(KRA, KR, KR6, KR6)
    add("5-554", f"{Q(AN)} {YES} {Q(BASES)} {NO_PE}", l1, l2, l3, l4)
    first = (f"{Q(f'{ANU6} {NA}')} {YES} {Q(f'{AV7L} {NA}')} {NO_PE} {q(f'{AV7S} {SA}')} {YES} "
             f"{Q(f'{AVA} {SA}')} {NO_PE}")
    add("5-555", *khandha_lines(AVA, AVJ, AV7L, AV7S, first=first))
    add("5-556",
        f"{S.na_vattabbam(AN)} {YES} {Q(f'{PUTH} có khuynh hướng tiềm ẩn')} {YES} "
        f"{Q('các khuynh hướng tiềm ẩn ấy có đối tượng')} {NO_PE} vậy thì {AN}. "
        f"{Q(f'{PUTH} có tham đắm')} {YES} {Q('sự tham đắm ấy có đối tượng')} {NO_PE} "
        f"{S.tena_hi(f'sự tham đắm {NA}')}",
        S.katha_end(KATHA[4]))

    # ---- (88) 5. Ñāṇaṃ anārammaṇantikathā ---------------------------------------------------------------------
    heading("5-17-5-0", 4, VAGGA)
    heading("5-17-5-1-0", 5, f"(88) 5. {S.katha(KATHA[5])}")
    _, k2, k3, k4 = khandha_lines(NANA, PANNA, "", "")
    add("5-557",
        f"{Q(NAN)} {YES} {Q(BASES)} {NO_PE} {q(NAN)} {YES} {Q(f'{PANNA5} {NA}')} {NO_PE} "
        f"{q(f'{PANNA5} {SA}')} {YES} {Q(f'{NANA} {SA}')} {NO_PE}",
        f"{k2} {k3[0].lower()}{k3[1:]}",
        k4)
    add("5-558",
        f"{S.na_vattabbam(NAN)} {YES} {Q(f'{ARC} người có hiểu biết')} {YES} {Q('hiểu biết ấy có đối tượng')} "
        f"{NO_PE} vậy thì {NAN}. {Q(f'{ARC} người có trí tuệ')} {YES} {Q('trí tuệ ấy có đối tượng')} {NO_PE} "
        f"{S.tena_hi(f'{PANNA} {NA}')}",
        S.katha_end(KATHA[5]))

    # ---- (89) 6. Atītānāgatārammaṇakathā ----------------------------------------------------------------------
    heading("5-17-6-0", 4, VAGGA)
    heading("5-17-6-1-0", 5, f"(89) 6. {S.katha(KATHA[6])}")

    def obj_lines(t):                 # ^5-559 / ^5-560 first two lines
        th = f"{ac(t)} thì {NA}"
        has = f"nó có đối tượng thuộc {T[t]}"
        l1 = (f"{Q(th)} {YES} {NANU(has)} {YES} {S.hanci_neg(has, th)} Sai khi nói rằng {th}. "
              f"Hoặc nếu nó {NA}, thì {RE}, chắc chắn không nên nói – “có đối tượng thuộc {T[t]}”. "
              f"Sai khi nói rằng cái {NA} thì có đối tượng thuộc {T[t]}.")
        l2 = f"{Q(th)} {YES} {NANU(adv(t))} {YES} {S.hanci_neg(adv(t), th)}"
        return l1, l2

    add("5-559", *obj_lines("a"))
    add("5-560", *obj_lines("f"),
        f"{Q(par('p', SA))} {YES} {Q(par('a', SA))} {NO_PE} {q(par('p', SA))} {YES} {Q(par('f', SA))} {NO_PE}",
        f"{Q(par('a', NA))} {YES} {Q(par('p', NA))} {NO_PE}",
        f"{Q(par('f', NA))} {YES} {Q(par('p', NA))} {NO_PE}")
    NONE = "quá khứ và tương lai không tồn tại"             # atītānāgataṃ natthi (natthi «không tồn tại», ch5-ch9)
    add("5-561",
        f"{S.na_vattabbam(ATN)} {YES} {NANU(NONE)} {YES} {S.hanci(NONE, ATN)[:-1]}{PE}",
        S.katha_end(KATHA[6]))

    # ---- (90) 7. Vitakkānupatitakathā ------------------------------------------------------------------------
    heading("5-17-7-0", 4, VAGGA)
    heading("5-17-7-1-0", 5, f"(90) 7. {S.katha(KATHA[7])}")
    FL = ", ".join(f"có {x} đi theo" for x in FOLLOW) + f"{PE} có sự không biết ghê sợ tội lỗi đi theo"
    add("5-562",
        f"{Q(VT)} {YES} {Q(f'tất cả tâm đều {FL}')} {NO_PE}",
        f"{Q(VT)} {YES} {NANU(f'có {SAM1}')} {YES} {S.hanci_neg(f'có {SAM1}', VT)}",
        f"{Q(VT)} {YES} {NANU(f'có {SAM2}')} {YES} {S.hanci_neg(f'có {SAM2}', VT)} {Q(VT)} {YES} "
        f"Chẳng phải {SAM3} [Trường Bộ Kinh 3.305, 353] sao? {YES} {S.hanci_neg(SAM3, VT)}",
        S.katha_end(KATHA[7]))

    # ---- (91) 8. Vitakkavipphārasaddakathā -------------------------------------------------------------------
    heading("5-17-8-0", 4, VAGGA)
    heading("5-17-8-1-0", 5, f"(91) 8. {S.katha(KATHA[8])}")
    L7 = ", ".join(f"trong mọi trường hợp, khi {v}, thì sự lan tỏa của {n} là âm thanh" for v, n in SEVEN)
    add("5-563",
        f"{Q(TH8)} {YES} {Q(L7)} {NO_PE}",
        f"{Q(TH8)} {YES} {Q(f'{VS} {EAR}')} {NO_PE} {NANU(f'{VS} {EAR_N}')} {YES} "
        f"{S.hanci_neg(f'{VS} {EAR_N}', TH8)}",
        S.katha_end(KATHA[8]))

    # ---- (92) 9. Na yathācittassa vācātikathā ----------------------------------------------------------------
    heading("5-17-9-0", 4, VAGGA)
    heading("5-17-9-1-0", 5, f"(92) 9. {S.katha(KATHA[9])}")
    NEG5 = ", ".join(of(V, f"không có {x}") for x in HAVE5)
    POS5 = ", ".join(of(V, f"có {x}") for x in HAVE5)
    POS5S = f"{of(V, 'có sự tiếp xúc')}{PE} {of(V, 'có tâm')}"
    AVN = f"{of(V, 'không hướng đến')}{VAR}{PE} {of(V, 'không chú hướng')}{PE} {of(V, 'không mong cầu')}"
    AVP = f"{of(V, 'hướng đến')}, {of(V, 'chú hướng')}{PE} {of(V, 'mong cầu')}"
    AVP3 = f"{of(V, 'hướng đến')}, {of(V, 'chú hướng')}, {of(V, 'mong cầu')}"
    add("5-564",
        f"{Q(NV)} {YES} {Q(f'có {NEG5}')} {NO_PE} {nanu(f'có {POS5}')} {YES} {S.hanci_neg(f'có {POS5S}', NV)}",
        f"{Q(NV)} {YES} {Q(f'có {AVN}')} {NO_PE} {nanu(f'có {AVP}')} {YES} {S.hanci_neg(f'có {AVP3}', NV)}",
        f"{Q(NV)} {YES} {NANU(born(V))} {YES} {S.hanci_neg(born(V), NV)}",
        f"{Q(NV)} {YES} {Q(f'người ta {wish_n(SPEAK)}')} {NO_PE} {nanu(f'người ta {wish(SPEAK)}')} {YES} "
        f"{S.hanci_neg(f'người ta {wish(SPEAK)}', NV)}")
    add("5-565",
        f"{S.na_vattabbam(NV)} {YES} {NANU('có ai đó ' + ', '.join(SAY4))} {YES} "
        f"{S.hanci(f'có ai đó {SAY4[0]},{PE} {SAY4[-1]}', NV)}",
        S.katha_end(KATHA[9]))

    # ---- (93) 10. Na yathācittassa kāyakammantikathā ---------------------------------------------------------
    heading("5-17-10-0", 4, VAGGA)
    heading("5-17-10-1-0", 5, f"(93) 10. {S.katha(KATHA[10])}")
    KN = f"có {of(K, 'không có sự tiếp xúc')}{PE} {of(K, 'không có tâm')}"
    KP = f"có {of(K, 'có sự tiếp xúc')}{PE} {of(K, 'có tâm')}"
    KAN = f"có {of(K, 'không hướng đến')}{PE} {of(K, 'không mong cầu')}"
    KAP = f"có {of(K, 'hướng đến')}{PE} {of(K, 'mong cầu')}"
    WP_S = f"người ta muốn {WALK[0]} thì {WALK[0]}{PE} muốn {WALK[-1]} thì {WALK[-1]}"
    add("5-566",
        f"{Q(NK)} {YES} {Q(KN)} {NO_PE} {nanu(KP)} {YES} {S.hanci_neg(KP, NK)}",
        f"{Q(NK)} {YES} {Q(KAN)} {NO_PE} {nanu(KAP)} {YES} {S.hanci_neg(KAP, NK)}",
        f"{Q(NK)} {YES} {NANU(born(K))} {YES} {S.hanci_neg(born(K), NK)}",
        f"{Q(NK)} {YES} {Q(f'người ta {wish_n(WALK)}')} {NO_PE} {NANU(f'người ta {wish(WALK)}')} {YES} "
        f"{S.hanci_neg(WP_S, NK)}")
    GS = f"có ai đó {GO}{PE} {STRETCH}"
    add("5-567",
        f"{S.na_vattabbam(NK)} {YES} {NANU(GS)} {YES} {S.hanci(GS, NK)}",
        S.katha_end(KATHA[10]))

    # ---- (94) 11. Atītānāgatasamannāgatakathā ----------------------------------------------------------------
    heading("5-17-11-0", 4, VAGGA)
    heading("5-17-11-1-0", 5, f"(94) 11. {S.katha(KATHA[11])}")
    PA = f"quá khứ {PAST5}"
    FU = f"tương lai {FUT6}"
    add("5-568",
        f"{Q(f'{SAMN} quá khứ')} {YES} {NANU(PA)} {YES} {S.hanci_neg(PA, f'{SAMN} quá khứ')}",
        f"{Q(f'{SAMN} tương lai')} {YES} {NANU(FU)} {YES} {S.hanci_neg(FU, f'{SAMN} tương lai')}")

    def count(one, three_, all_, n_all, total):
        return (f"{Q(three(one))} {YES} {Q(f'{SAMN} ba {three_}')} {NO_PE} {q(three(f'{n_all} {all_}'))} {YES} "
                f"{Q(f'{SAMN} {total} {all_}')} {NO_PE}")

    add("5-569",
        count("khối vật chất", "khối vật chất", "khối", "năm", "mười lăm"),
        count(S.A["cakkhāyatana"], S.A["cakkhāyatana"], "lĩnh vực nhận biết", "mười hai", "ba mươi sáu"),
        count(S.D["cakkhudhātu"], S.D["cakkhudhātu"], "yếu tố", "mười tám", "năm mươi bốn"),
        count(S.I["cakkhundriya"], S.I["cakkhundriya"], "năng lực", "hai mươi hai", "sáu mươi sáu"))
    add("5-570",
        f"{S.na_vattabbam(ATS)} {YES} {NANU(JH)} {YES} {S.hanci(JH, ATS)}",
        S.katha_end(KATHA[11]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-17"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
