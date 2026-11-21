"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 19, Ekādasamavaggo (^5-19-0 … ^5-629): the three
anusaya kathās (106-108) and the kathās 109-115, with the repeated "Ekādasamavaggo" sub-headings, the vagga close
and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/19-ekadasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci_neg, na_vattabbam, tena_hi,
tena_hi_na, neu, vattabbo, katha, katha_end, var_sp, CIT …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED19); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-19.md.

usage: python -I -X utf8 -B build_rails_19_vi.py          (writes the chapter and the adherence copy rails\\adh-19\\)
       python -I -X utf8 -B build_rails_19_vi.py --find <regex> [max]   (finished pi-5 rails: Pāli line + Vietnamese)
       python -I -X utf8 -B build_rails_19_vi.py --kw                  (keywords of this chapter + termbase entry)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "19-ekadasamavaggo.md"
TB = S.ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = S.ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, CIT = S.cap, S.CIT

# ---------------------------------------------------------------------------------------------------------------
# Core words (termbase; pi-1 / pi-2; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
AB = "không xác định về mặt đạo đức"                   # abyākata (core term)
AK = "là bất thiện"                                    # akusalaṃ / akusalo (termbase Kāmarāgānusayo akusalo)
AH, SH = "không có gốc rễ", "có gốc rễ"                 # ahetuka / sahetuka (pi-1; termbase hetukā)
KHG, GL = "không gắn liền với tâm", "gắn liền với tâm"  # cittavippayutta / cittasampayutta (pi-1)
AN = "các khuynh hướng tiềm ẩn"                         # anusayā (ch17)
BASES = f"đó là vật chất, Niết-bàn, {S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}"
#   Rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatananti?  (ch17, «đó là» supplied as ch11)
VK = (f"đó là những gì {AB} thuộc quả của nghiệp, những gì {AB} mang tính chức năng, vật chất, Niết-bàn, "
      f"{S.A['cakkhāyatana']}{PE} {S.A['phoṭṭhabbāyatana']}")
#   Vipākābyākatā kiriyābyākatā rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatananti? (termbase Vipākābyākatā,
#   Kiriyābyākatā; «những gì» supplied for the substantive adjectives)

KRA = "khuynh hướng tiềm ẩn tham đắm dục lạc"           # kāmarāgānusayo (pi-2)
PTA = "khuynh hướng tiềm ẩn ác cảm"                     # paṭighānusayo (pi-2)
MNA = "khuynh hướng tiềm ẩn kiêu mạn"                   # mānānusayo
DTA = "khuynh hướng tiềm ẩn quan điểm"                  # diṭṭhānusayo
VCA = "khuynh hướng tiềm ẩn hoài nghi"                  # vicikicchānusayo
BRA = "khuynh hướng tiềm ẩn tham đắm hiện hữu"          # bhavarāgānusayo
AVA = "khuynh hướng tiềm ẩn vô minh"                    # avijjānusayo
ANU6 = ", ".join([PTA, MNA, DTA, VCA, BRA, AVA])        # paṭighānusayo … avijjānusayo (ch17)
KR = "sự tham đắm dục lạc"                              # kāmarāgo (pi-1)
KR6 = (f"{KR}, sự ám ảnh của tham đắm dục lạc, xiềng xích tham đắm dục lạc, dòng lũ dục lạc, ách dục lạc, "
       f"chướng ngại ý muốn dục lạc")                    # kāmarāgo … kāmacchandanīvaraṇaṃ (ch17)
KR4 = f"{KR}, sự ám ảnh của tham đắm dục lạc, xiềng xích tham đắm dục lạc, chướng ngại ý muốn dục lạc"
#   kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmacchandanīvaraṇaṃ
KR_SH = f"{KR}, sự ám ảnh của tham đắm dục lạc{PE} chướng ngại ý muốn dục lạc"
#   kāmarāgo kāmarāgapariyuṭṭhānaṃ…pe… kāmacchandanīvaraṇaṃ
PT3 = "sự ác cảm, sự ám ảnh của ác cảm, xiềng xích ác cảm"   # paṭighaṃ paṭighapariyuṭṭhānaṃ paṭighasaṃyojanaṃ
MN3 = "sự kiêu mạn, sự ám ảnh của kiêu mạn, xiềng xích kiêu mạn"   # māno mānapariyuṭṭhānaṃ mānasaṃyojanaṃ
DT5 = "quan điểm, dòng lũ quan điểm, ách quan điểm, sự ám ảnh của quan điểm, xiềng xích quan điểm"
#   diṭṭhi diṭṭhogho diṭṭhiyogo diṭṭhipariyuṭṭhānaṃ diṭṭhisaṃyojanaṃ
VC4 = "sự hoài nghi, sự ám ảnh của hoài nghi, xiềng xích hoài nghi, chướng ngại hoài nghi"
#   vicikicchā vicikicchāpariyuṭṭhānaṃ vicikicchāsaṃyojanaṃ vicikicchānīvaraṇaṃ
BR3 = "sự tham đắm hiện hữu, sự ám ảnh của tham đắm hiện hữu, xiềng xích tham đắm hiện hữu"
#   bhavarāgo bhavarāgapariyuṭṭhānaṃ bhavarāgasaṃyojanaṃ
AVJ = "vô minh"                                         # avijjā
AV6 = "vô minh, dòng lũ vô minh, ách vô minh, sự ám ảnh của vô minh, xiềng xích vô minh, chướng ngại vô minh"
#   avijjā avijjogho avijjāyogo avijjāpariyuṭṭhānaṃ avijjāsaṃyojanaṃ avijjānīvaraṇaṃ
AV_SH = f"vô minh, dòng lũ vô minh{PE} chướng ngại vô minh"   # avijjā avijjogho…pe… avijjānīvaraṇaṃ (ch17)
AV4 = "vô minh, dòng lũ vô minh, ách vô minh, chướng ngại vô minh"   # avijjā avijjogho avijjāyogo avijjānīvaraṇaṃ

SK = "khối tạo tác"                                     # saṅkhārakkhandho (pi-2)
V2 = "khối cảm giác, khối tri giác"                     # vedanākkhandho saññākkhandho (pi-1)
IN = "nằm trong khối tạo tác"                           # saṅkhārakkhandhapariyāpanna (ch17)
WHICH = "Nằm trong khối nào? Nằm trong khối tạo tác."   # Katamakkhandhapariyāpanno(-ṃ)ti? … (ch17)
PUTH = "người phàm phu, khi tâm thiện hoặc không xác định về mặt đạo đức đang diễn ra, nên gọi là"   # (ch17)
ARC = "bậc A-la-hán, người có được thức qua mắt, nên gọi là"                                     # (ch17)
SANU, SARA = "“có khuynh hướng tiềm ẩn”", "“có tham đắm”"   # "sānusayo"ti / "sarāgo"ti (ch17 words, quoted)
KUS = "các hiện tượng thiện và bất thiện đi đến chỗ cùng hiện diện đối mặt nhau"
#   Kusalākusalā dhammā sammukhībhāvaṃ āgacchanti (ch15 words)
NANA, PANNA = "hiểu biết", "trí tuệ"                    # ñāṇaṃ / paññā
PANNA5 = (f"{PANNA}, {S.I['paññindriya']}, sức mạnh trí tuệ, quan điểm đúng đắn, "
          f"chi phần giác ngộ là sự tìm hiểu các hiện tượng")   # (ch17; pi-1)
NANI = "người có hiểu biết"                             # ñāṇī (ch17)
PANNAVA = "người có trí tuệ"                            # paññavā (ch17)


def part(x):                          # X ekadeso cittasampayutto ekadeso cittavippayutto
    return f"{x} một phần {GL}, một phần {KHG}"


def inn(x, obj):                      # X saṅkhārakkhandhapariyāpanno citta(vip/sam)payutto
    return f"{x} {IN} thì {obj}"


# ---- Ñāṇakathā ---------------------------------------------------------------------------------------------------
AVN = "khi sự không biết đã mất đi, khi tâm không gắn liền với hiểu biết đang diễn ra"
#   Aññāṇe vigate ñāṇavippayutte citte vattamāne (termbase Aññāṇe, vigate, ñāṇavippayutte citte, citte vattamāne)
VITA = "người đã lìa tham đắm"                          # vītarāgo (termbase «đã lìa tham đắm», ch10; «người» as ñāṇī)
NIKK = "người không còn phiền não"                      # nikkileso (no headword; kilesa «phiền não»)
GONE = {"r": "khi sự tham đắm đã mất đi", "d": "khi sự sân hận đã mất đi", "m": "khi sự si mê đã mất đi",
        "k": "khi phiền não đã mất đi"}                 # Rāge / Dose / mohe / kilese vigate


def nv(cond, x):                      # cond na vattabbaṃ – "X"ti?
    return f"Có phải {cond}, không nên nói – “{x}” không?"


def vv(cond, x):                      # cond vattabbaṃ – "X"ti?
    return f"Có phải {cond}, nên nói – “{x}” không?"


def low(s):
    return s[:1].lower() + s[1:]


# ---- Idaṃ dukkhantikathā -----------------------------------------------------------------------------------------
I_D = "đây là khổ đau"                                  # idaṃ dukkhaṃ (ch10 ‘Đây là khổ đau’)
DS = "đây là sự phát sinh của khổ đau"                  # ayaṃ dukkhasamudayo (ch10)
DN = "đây là sự chấm dứt khổ đau"                       # ayaṃ dukkhanirodho (ch10)
MG = "đây là con đường"                                 # ayaṃ maggo
SMD = "đây là sự phát sinh"                             # ayaṃ samudayo
NRD = "đây là sự chấm dứt"                              # ayaṃ nirodho
RA, VA = "vật chất là vô thường", "thức là vô thường"   # rūpaṃ / viññāṇaṃ aniccaṃ (termbase)
RN, VN = "vật chất không phải là tự ngã", "thức không phải là tự ngã"   # rūpaṃ / viññāṇaṃ anattā (pi-2 anattā)
VSS = f"cảm giác{PE} tri giác{PE} các tạo tác{PE}"      # Vedanā… saññā… saṅkhārā…


def dk(x, y=None, neg=False):         # "X"ti vācaṃ bhāsato (na ca) "Y"ti ñāṇaṃ pavattati
    y = x if y is None else y
    tail = f"nhưng hiểu biết “{y}” không khởi lên" if neg else f"hiểu biết “{y}” khởi lên"
    return f"khi nói lời “{x}”, {tail}"


# ---- Iddhibalakathā ----------------------------------------------------------------------------------------------
TH = "người được trang bị sức mạnh thần thông có thể kéo dài suốt một kiếp"
#   iddhibalena samannāgato kappaṃ tiṭṭheyya (termbase Iddhibalena, samannāgato, kappaṃ, tiṭṭheyya «kéo dài»;
#   «suốt một kiếp» as ch10 kappaṃ tiṭṭhati «duy trì suốt một kiếp»)
KT = "có thể kéo dài"                                   # tiṭṭheyya
ALIVE = "khi có sự sống, có phần còn lại của sự sống"   # sati jīvite jīvitāvasese
DEAD = "khi không có sự sống, không có phần còn lại của sự sống"   # asati jīvite jīvitāvasese
HOLD = "có thể nhờ thần thông mà giữ cho"               # labbhā iddhiyā paggahetuṃ (termbase «thần thông mà giữ cho»)
LIST10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
          "sự định tâm", "trí tuệ"]                     # phasso … paññā (ch4 / ch12 / ch15)
NIRU = "đừng chấm dứt"                                  # mā nirujjhi (termbase mā «đừng», nirujjhi «chấm dứt»)
BEINGS = [("sinh", "sinh ra"), ("lão hóa", "lão hóa"), ("bệnh", "bệnh"), ("chết", "chết")]
#   jāti- / jarā- / byādhi- / maraṇadhammā sattā mā jāyiṃsu / jīriṃsu / byādhiyiṃsu / mīyiṃsu
#   («có bản chất phải …»: pi-2 Saccavibhaṅga)


def being(k):
    n, v = BEINGS[k]
    return f"các chúng sinh có bản chất phải {n} đừng {v}"


SUT_I = (f"“Bất cứ ai, này A-nan, có bốn nền tảng thần thông được tu tập, được làm đi làm lại, được biến thành cỗ "
         f"xe, được làm thành chỗ dựa, được thiết lập vững chắc, được làm cho quen thuộc, được khởi sự trọn vẹn, "
         f"người ấy, nếu muốn, {KT} suốt một kiếp hoặc phần còn sót lại của kiếp”")
#   yassa kassaci, ānanda, cattāro iddhipādā bhāvitā bahulīkatā yānīkatā vatthukatā anuṭṭhitā paricitā
#   susamāraddhā, so ākaṅkhamāno kappaṃ vā tiṭṭheyya kappāvasesaṃ vā (ch10 «các nền tảng thần thông»)
NOONE = ("không có ai là người bảo đảm, dù là sa-môn hoặc bà-la-môn hoặc vị trời hoặc Ma vương hoặc Phạm thiên "
         "hoặc bất kỳ ai trong thế gian")
#   natthi koci pāṭibhogo samaṇo vā brāhmaṇo vā devo vā māro vā brahmā vā koci vā lokasmiṃ
BH, bh = "Này các tỳ-khưu", "này các tỳ-khưu"
SUT_A = (f"“Đối với bốn hiện tượng, {bh}, {NOONE}! Bốn hiện tượng nào? "
         f"Đối với điều có bản chất phải lão hóa, rằng ‘đừng lão hóa’, {NOONE}. "
         f"Đối với điều có bản chất phải bệnh, rằng ‘đừng bệnh’{PE} đối với điều có bản chất phải chết, rằng "
         f"‘đừng chết’{PE} đối với những nghiệp xấu ác đã làm trước đây, là đối tượng của phiền não, đưa đến sự hiện "
         f"hữu mới{S.var_sp('Sī., Pī.', 'ponobhavikāni')}, đầy lo âu "
         f"[dị bản (Sī., Pī., Ka.): nissārāni; dị bản (Syā.): dukkhudrayāni], có quả trổ khó chịu, dẫn đến sự sinh, "
         f"sự lão hóa và sự chết trong tương lai, rằng quả của chúng ‘đừng phát sinh’, {NOONE}. "
         f"{BH}, đối với bốn hiện tượng này, {NOONE}” [{CIT['a. ni.']} 4.182]")
#   catunnaṃ, bhikkhave, dhammānaṃ … lokasmi"nti [a. ni. 4.182]  (the inner "mā jīrī" etc. nested as ‘…’)

# ---- Samādhikathā ------------------------------------------------------------------------------------------------
CS = "sự liên tục của tâm là sự định tâm"               # cittasantati samādhi (termbase)
NAP = "là người đang nhập"                              # samāpanno (APPROVED Samāpanno «người đang nhập»)
SAM = "người có được"                                   # -samaṅgī (termbase)
SUT_N = (f"“Này các hiền giả Ni-kiền-tử, Ta có thể, không lay động thân, không nói ra lời, sống suốt bảy ngày "
         f"đêm{S.var_sp('Ka.', 'rattidivāni')} như người cảm nhận hạnh phúc hoàn toàn” [{CIT['ma. ni.']} 1.180]")
#   ahaṃ kho, āvuso nigaṇṭhā, pahomi aniñjamāno kāyena, abhāsamāno vācaṃ, satta rattindivāni ekantasukhaṃ
#   paṭisaṃvedī viharituṃ (sukha = happiness: APPROVED §2; āvuso «hiền giả» ch10/ch12; Nigaṇṭha: no termbase name)

# ---- Dhammaṭṭhitatā / Aniccatā -----------------------------------------------------------------------------------
PN = "được hình thành trọn vẹn"                         # parinipphanna (termbase)
TAYA = ("đối với từng cái như vậy, không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt vòng luân chuyển, "
        "không có sự nhập Niết-bàn trọn vẹn không còn bám víu")
#   Tāya tāyeva / Tassa tasseva natthi dukkhassantakiriyā, natthi vaṭṭupacchedo, natthi anupādāparinibbānaṃ
#   (termbase Tāya tāyeva «từng cái như vậy»; the rest = S.TASSA_TASSEVA)
assert TAYA.split(", ", 1)[1] == S.TASSA_TASSEVA.split(", ", 1)[1]
TT = f"sự ổn định của sự ổn định ấy {PN}"               # tāya ṭhitatā parinipphannā
AT = "tính vô thường"                                   # aniccatā (termbase)
JR = "sự lão hóa"                                       # jarā
MR = "sự chết"                                          # maraṇaṃ
EX = "tồn tại"                                          # atthi (coordinator rule)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười một"                           # Ekādasamavaggo (termbase)
ANUSAYA_H = f"Cả ba phần bàn về {AN}"                   # Tissopi anusayakathā (heading)
ANUSAYA_E = f"{ANUSAYA_H} đã hoàn tất."                 # Tissopi anusayakathā niṭṭhitā.
KATHA = {4: NANA, 5: f"việc {NANA} {KHG}", 6: f"“{I_D}”", 7: "sức mạnh thần thông", 8: "sự định tâm",
         9: "sự ổn định của các hiện tượng", 10: AT}
#   Ñāṇa- (termbase), Ñāṇaṃ cittavippayuttanti- («việc» for a -ti thesis, ch11 / ch14 / ch17), Idaṃ dukkhanti-
#   (the quoted thesis), Iddhibala-, Samādhi-, Dhammaṭṭhitatā-, Aniccatākathā (termbase)
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)
UDDANA = ", ".join([
    f"{cap(AN)} {AB}", AH, KHG, f"khi sự không biết đã mất đi thì là {NANI}", f"{NANA} {KHG}",
    "nơi có âm thanh [khác chính tả (Sī.): yattha saddo; dị bản (?): yathāsaddaṃ] thì hiểu biết khởi lên",
    TH, CS, "sự ổn định của các hiện tượng", AT]) + "."
#   Anusayā abyākatā, ahetukā, cittavippayuttā, aññāṇe vigate ñāṇī, ñāṇaṃ cittavippayuttaṃ, yattha sadde
#   [yattha saddo (sī.), yathāsaddaṃ (?)] ñāṇaṃ pavattati, iddhibalena samannāgato kappaṃ tiṭṭheyya, cittasantati
#   samādhi, dhammaṭṭhitatā, aniccatāti.

REUSED19 = [  # (Pāli, Vietnamese, book)
    ("cittasampayuttā dhammā", "các hiện tượng gắn liền với tâm", "1"),
    ("cittavippayuttā dhammā", "các hiện tượng không gắn liền với tâm", "1"),
    ("ahetukaṃ (rūpakaṇḍa)", AH, "1"),
    ("Vedanākkhandho, saññākkhandho", V2, "1"),
    ("paṭighasaṃyojanaṃ", "xiềng xích ác cảm", "1"), ("mānasaṃyojanaṃ", "xiềng xích kiêu mạn", "1"),
    ("diṭṭhisaṃyojanaṃ", "xiềng xích quan điểm", "1"), ("vicikicchāsaṃyojanaṃ", "xiềng xích hoài nghi", "1"),
    ("bhavarāgasaṃyojanaṃ", "xiềng xích tham đắm hiện hữu", "1"), ("bhavarāgo", "sự tham đắm hiện hữu", "1"),
    ("diṭṭhi (in a list)", "là quan điểm, sự mắc kẹt", "1"),
    ("paṭighānusayo … avijjānusayo", "khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, khuynh hướng "
     "tiềm ẩn quan điểm, khuynh hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm hiện hữu, khuynh hướng "
     "tiềm ẩn vô minh", "2"),
    ("kāmarāgānusayo", KRA, "2"),
    ("Jātidhammānaṃ sattānaṃ", "chúng sinh có bản chất phải sinh", "2"),
    ("jarādhammānaṃ sattānaṃ", "chúng sinh có bản chất phải lão hóa", "2"),
    ("byādhidhammānaṃ sattānaṃ", "chúng sinh có bản chất phải bệnh", "2"),
    ("maraṇadhammānaṃ sattānaṃ", "chúng sinh có bản chất phải chết", "2"),
    ("anattā", "không phải là tự ngã", "2"),
    ("kiriyābyākata (pi-1 «mang tính chức năng»)", "mang tính chức năng", "1"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatananti?", BASES, "17-navamavaggo.md"),
    ("kāmarāgo … kāmacchandanīvaraṇaṃ", KR6, "17-navamavaggo.md"),
    ("paṭighānusayo … avijjānusayo", ANU6, "17-navamavaggo.md"),
    ("avijjā avijjogho…pe… avijjānīvaraṇaṃ", AV_SH, "17-navamavaggo.md"),
    ("Katamakkhandhapariyāpanno …", WHICH, "17-navamavaggo.md"),
    ("… saṅkhārakkhandhapariyāpanno", f"{IN} thì", "17-navamavaggo.md"),
    ("Puthujjano kusalābyākate citte vattamāne …ti vattabbo", PUTH, "17-navamavaggo.md"),
    ("sānusayo / sarāgo", "nên gọi là có khuynh hướng tiềm ẩn", "17-navamavaggo.md"),
    ("sarāgo", "nên gọi là có tham đắm", "17-navamavaggo.md"),
    ("Arahā cakkhuviññāṇasamaṅgī …ti vattabbo", ARC, "17-navamavaggo.md"),
    ("ñāṇī / paññavā", f"{NANI} không?", "17-navamavaggo.md"),
    ("paññavā", PANNAVA, "17-navamavaggo.md"),
    ("paññā … dhammavicayasambojjhaṅgo", PANNA5, "17-navamavaggo.md"),
    ("ekadeso … ekadeso", "một phần có đối tượng, một phần", "17-navamavaggo.md"),
    ("sammukhībhāvaṃ āgacchanti", "đi đến chỗ cùng hiện diện đối mặt nhau", "15-sattamavaggo.md"),
    ("kusalākusalā … dhammā", "các hiện tượng thiện và bất thiện", "15-sattamavaggo.md"),
    ("kālaṅkatā", "những người đã qua đời", "15-sattamavaggo.md"),
    ("‘Idaṃ dukkha’nti", "‘Đây là khổ đau’", "10-dutiyavaggo.md"),
    ("‘ayaṃ dukkhasamudayo’ti", f"‘{DS}’", "10-dutiyavaggo.md"),
    ("‘ayaṃ dukkhanirodho’ti", f"‘{DN}’", "10-dutiyavaggo.md"),
    ("iddhipādā", "các nền tảng thần thông", "10-dutiyavaggo.md"),
    ("vītarāgo", "đã lìa tham đắm", "10-dutiyavaggo.md"),
    ("kappaṃ tiṭṭhati", "duy trì suốt một kiếp", "10-dutiyavaggo.md"),
    ("udā. (citation)", "Kinh Phật Tự Thuyết", "10-dutiyavaggo.md"),
    ("āvuso", "Này các hiền giả", "10-dutiyavaggo.md"),
    ("aññāṇa", "sự không biết", "10-dutiyavaggo.md"),
    ("niruddhāya vigatāya paṭipassaddhāya", "đã chấm dứt, đã mất đi, đã an tịnh", "12-catutthavaggo.md"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("Tassa tasseva natthi dukkhassa antakiriyā …", S.TASSA_TASSEVA.split(", ", 1)[1], "1-puggalakatha.md"),
    ("Ānanda", "A-nan", "1-puggalakatha.md"),
    ("Xti, Yti?", "Có phải nếu", "1-puggalakatha.md"),
    ("rūpaṃ passati puggalaṃ passatīti? (alternative question)", "thấy hình sắc hay thấy người?",
     "1-puggalakatha.md"),
    ("phasso … paññā (list)", ", ".join(LIST10[1:4]), "15-sattamavaggo.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED19 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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

    heading("5-19-0", 3, VAGGA)

    # ---- (106-108) 1-3. Tissopi anusayakathā -----------------------------------------------------------------
    heading("5-19-1-0", 4, f"(106-108) 1-3. {ANUSAYA_H}")

    def ab_line(xa, full, short=None):    # Xānusayo abyākatoti? … Xānusayo akusaloti? Na hevaṃ vattabbe…pe….
        short = short or full
        return (f"{Q(f'{xa} {AB}')} {YES} {Q(f'{full} {AB}')} {NO_PE} {q(f'{short} {AK}')} {YES} "
                f"{Q(f'{xa} {AK}')} {NO_PE}")

    add("5-605",
        f"{Q(f'{AN} {AB}')} {YES} {Q(VK)} {NO_PE}",
        ab_line(KRA, KR6, KR_SH),
        ab_line(PTA, PT3),
        ab_line(MNA, MN3),
        ab_line(DTA, DT5),
        ab_line(VCA, VC4),
        ab_line(BRA, BR3),
        ab_line(AVA, AV6))

    def because(th, which, end_cap=False):   # Puthujjano … "sānusayo" … tena hi … ti. (5-606 / 608 / 613)
        a_q, r_q, a_end, r_end, no = which
        first = "Vậy thì" if end_cap else "vậy thì"
        return (f"{S.na_vattabbam(f'{AN} {th}')} {YES} {Q(f'{PUTH} {SANU}')} {YES} {Q(a_q)} {no} "
                f"{first} {AN} {th}. {Q(f'{PUTH} {SARA}')} {YES} {Q(r_q)} {no} {first} sự tham đắm {th}.")

    add("5-606", because(AB, (KUS, KUS, None, None, NO_PE)))

    # ^5-607 / ^5-608 (ahetukā)
    add("5-607",
        f"{Q(f'{AN} {AH}')} {YES} {Q(BASES)} {NO_PE}",
        f"{Q(f'{KRA} {AH}')} {YES} {Q(f'{KR4} {AH}')} {NO_PE} {q(f'{KR_SH} {SH}')} {YES} {Q(f'{KRA} {SH}')} "
        f"{NO_PE} có phải {PTA}{PE} {MNA}{PE} {DTA}{PE} {VCA}{PE} {BRA}{PE} {AVA} {AH} không? {YES} "
        f"{Q(f'{AV6} {AH}')} {NO_PE} {q(f'{AV_SH} {SH}')} {YES} {Q(f'{AVA} {SH}')} {NO_PE}")
    add("5-608", because(AH, (f"{AN} {SH} bởi gốc rễ ấy", f"sự tham đắm {SH} bởi gốc rễ ấy", None, None, NO_PE)))
    #   Anusayā / Rāgo tena hetunā sahetukā(-o) (termbase hetunā «gốc rễ»)

    # ^5-609 … ^5-613 (cittavippayuttā)
    add("5-609",
        f"{Q(f'{AN} {KHG}')} {YES} {Q(BASES)} {NO_PE}",
        f"{Q(f'{KRA} {KHG}')} {YES} {Q(f'{KR6} {KHG}')} {NO_PE} {q(f'{KR_SH} {GL}')} {YES} {Q(f'{KRA} {GL}')} "
        f"{NO_PE}")

    def khandha_lines(subj, kin, l3_end=NO_PE):
        l1 = (f"{Q(f'{subj} {KHG}')} {YES} {WHICH} {Q(f'{SK} {KHG}')} {NO} {Q(f'{SK} {KHG}')} {YES} "
              f"{Q(f'{V2} {KHG}')} {NO_PE}")
        l2 = (f"{Q(inn(subj, KHG))} {YES} {Q(inn(kin, KHG))} {NO_PE} {q(inn(kin, GL))} {YES} "
              f"{Q(inn(subj, GL))} {NO_PE}")
        l3 = f"{Q(f'{inn(subj, KHG)}, {inn(kin, GL)}')} {YES} {Q(part(SK))} {l3_end}"
        l4 = f"{Q(part(SK))} {YES} {Q(part(V2))} {NO_PE}"
        return l1, l2, l3, l4

    add("5-610", *khandha_lines(KRA, KR))
    add("5-611",
        f"{Q(f'{ANU6} {KHG}')} {YES} {Q(f'{AV4} {KHG}')} {NO_PE} {q(f'{AV4} {GL}')} {YES} {Q(f'{AVA} {GL}')} "
        f"{NO_PE}")
    add("5-612", *khandha_lines(AVA, AVJ, l3_end=NO))
    add("5-613",
        because(KHG, (f"{AN} gắn liền với tâm ấy", "sự tham đắm gắn liền với tâm ấy", None, None, NO),
                end_cap=True),
        ANUSAYA_E)

    # ---- (109) 4. Ñāṇakathā ----------------------------------------------------------------------------------
    heading("5-19-2-0", 4, VAGGA)
    heading("5-19-2-1-0", 5, f"(109) 4. {S.katha(KATHA[4])}")
    DMK = f"{GONE['d']}{PE} {GONE['m']}{PE} {GONE['k']}"
    add("5-614",
        f"{nv(AVN, NANI)} {YES} {nv(GONE['r'], VITA)} {NO_PE} {low(nv(AVN, NANI))} {YES} {nv(DMK, NIKK)} {NO_PE}",
        f"{vv(GONE['r'], VITA)} {YES} {vv(AVN, NANI)} {NO_PE} {low(vv(DMK, NIKK))} {YES} {vv(AVN, NANI)} {NO_PE}")
    add("5-615",
        f"{vv(AVN, NANI)} {YES} Có phải là {NANI} nhờ {NANA} thuộc quá khứ, là {NANI} nhờ {NANA} đã chấm dứt, "
        f"đã mất đi, đã an tịnh không? {NO_PE}",
        S.katha_end(KATHA[4]))
    #   Atītena ñāṇena ñāṇī niruddhena vigatena paṭipassaddhena ñāṇena ñāṇīti? (ch12 «nhờ», «đã chấm dứt, …»)

    # ---- (110) 5. Ñāṇaṃ cittavippayuttantikathā --------------------------------------------------------------
    heading("5-19-3-0", 4, VAGGA)
    heading("5-19-3-1-0", 5, f"(110) 5. {S.katha(KATHA[5])}")
    NK = f"{NANA} {KHG}"
    add("5-616",
        f"{Q(NK)} {YES} {Q(BASES)} {NO_PE} {q(NK)} {YES} {Q(f'{PANNA5} {KHG}')} {NO_PE} "
        f"{q(f'{PANNA5} {GL}')} {YES} {Q(f'{NANA} {GL}')} {NO_PE}",
        f"{Q(NK)} {YES} {WHICH} {Q(f'{SK} {KHG}')} {NO_PE} {q(f'{SK} {KHG}')} {YES} {Q(f'{V2} {KHG}')} {NO_PE} "
        f"{q(inn(NANA, KHG))} {YES} {Q(inn(PANNA, KHG))} {NO_PE} {q(inn(PANNA, GL))} {YES} "
        f"{Q(inn(NANA, GL))} {NO_PE} {q(f'{inn(NANA, KHG)}, {inn(PANNA, GL)}')} {YES} {Q(part(SK))} {NO_PE} "
        f"{q(part(SK))} {YES} {Q(part(V2))} {NO_PE}")
    NOTE_SV = " [thấy như là câu hỏi của người theo học thuyết của chúng ta]"   # [sakavādīpucchā viya dissati]
    add("5-617",
        f"{S.na_vattabbam(NK)} {YES} {Q(f'{ARC} “{NANI}”')} {YES} {Q(f'{NANA} gắn liền với tâm ấy')} {NO} "
        f"{S.tena_hi(NK)}",
        f"Có phải {ARC} “{PANNAVA}”{NOTE_SV} không? {YES} {Q(f'{PANNA} gắn liền với tâm ấy')} {NO} "
        f"{S.tena_hi(f'{PANNA} {KHG}')}",
        S.katha_end(KATHA[5]))

    # ---- (111) 6. Idaṃ dukkhantikathā -------------------------------------------------------------------------
    heading("5-19-4-0", 4, VAGGA)
    heading("5-19-4-1-0", 5, f"(111) 6. {S.katha(KATHA[6])}")
    add("5-618",
        f"{Q(dk(I_D))} {YES} {Q(dk(DS))} {NO_PE} {q(dk(I_D))} {YES} {Q(dk(DN))} {NO_PE} {q(dk(I_D))} {YES} "
        f"{Q(dk(MG))} {NO_PE}",
        f"{Q(dk(SMD, neg=True))} {YES} {Q(dk(I_D, neg=True))} {NO_PE} có phải “{NRD}”{PE} "
        f"{dk(MG, neg=True)} không? {YES} {Q(dk(I_D, neg=True))} {NO_PE}")

    def four(a, v, neg=False, last_y=None):
        """^5-619 lines: X / idaṃ dukkhaṃ (or reverse) and vedanā… saññā… saṅkhārā… viññāṇaṃ."""
        if not neg:
            return (f"{Q(dk(I_D))} {YES} {Q(dk(a))} {NO_PE} {q(dk(I_D))} {YES} Có phải {VSS} {dk(v)} không? "
                    f"{NO_PE}")
        return (f"{Q(dk(a, neg=True))} {YES} {Q(dk(I_D, neg=True))} {NO_PE} có phải {VSS} {dk(v, neg=True)} "
                f"không? {YES} {Q(dk(I_D, last_y, neg=True))} {NO_PE}")

    add("5-619", four(RA, VA), four(RN, VN), four(RA, VA, neg=True), four(RN, VN, neg=True, last_y="khổ đau"))
    #   last line: "idaṃ dukkha"nti vācaṃ bhāsato na ca "dukkha"nti ñāṇaṃ (as written: «khổ đau»)
    add("5-620",
        f"{Q(dk(I_D))} {YES} Có phải hiểu biết “i”{S.var_sp('Syā., Pī.', 'īti')} và “đam” và "
        f"“đu”{S.var_sp('Syā., Pī.', 'dūti')} và “kham” khởi lên không? {NO_PE}",
        S.katha_end(KATHA[6]))
    #   "I"ti ca "da"nti ca "du"ti ca "kha"nti ca ñāṇaṃ pavattati (syllables in Vietnamese spelling; termbase kha «kham»)

    # ---- (112) 7. Iddhibalakathā ------------------------------------------------------------------------------
    heading("5-19-5-0", 4, VAGGA)
    heading("5-19-5-1-0", 5, f"(112) 7. {S.katha(KATHA[7])}")
    MAY = ", ".join(f"{x} ấy phát sinh từ thần thông" for x in ("tuổi thọ", "cõi tái sinh",
                                                                 "sự có được sự tồn tại cá nhân"))
    #   iddhimayiko so āyu, iddhimayikā sā gati, iddhimayiko so attabhāvappaṭilābho (-maya «phát sinh từ», ch15)
    ALT = f"{cap(KT)} {ALIVE}, hay {KT} {DEAD}? {cap(KT)} {ALIVE}."
    #   Sati jīvite jīvitāvasese tiṭṭheyya, asati … tiṭṭheyyāti? Sati jīvite jīvitāvasese tiṭṭheyyāti.
    add("5-621",
        f"{Q(TH)} {YES} {Q(MAY)} {NO_PE}",
        f"{Q(TH)} {YES} {Q(f'{KT} suốt kiếp thuộc quá khứ, {KT} suốt kiếp thuộc tương lai')} {NO_PE} {q(TH)} "
        f"{YES} {Q(f'{KT} suốt hai kiếp, {KT} suốt ba kiếp, {KT} suốt bốn kiếp')} {NO_PE} {q(TH)} {YES} {ALT} "
        f"{S.hanci_neg(f'{KT} {ALIVE}', TH)} "
        f"{S.neu(f'{KT} {DEAD}', f'người đã chết {KT}, người đã qua đời {KT}')} {NO_PE}")
    UPP = f"{PE} ".join(f"{x} đã sinh khởi" for x in LIST10[1:])
    add("5-622",
        f"{Q(TH)} {YES} {Q(f'{HOLD} {LIST10[0]} đã sinh khởi {NIRU}')} {NO_PE} {q(f'{HOLD} {UPP} {NIRU}')} {NO_PE}",
        f"{Q(TH)} {YES} {Q(f'{HOLD} vật chất thường còn')} {NO_PE} "
        f"{q(f'{HOLD} cảm giác{PE} tri giác{PE} các tạo tác{PE} thức thường còn')} {NO_PE}",
        f"{Q(TH)} {YES} {Q(f'{HOLD} {being(0)}')} {NO_PE} "
        f"{q(f'{HOLD} {being(1)}{PE} {being(2)}{PE} {being(3)}')} {NO_PE}")
    add("5-623",
        f"{S.na_vattabbam(TH)} {YES} {S.NANU_VUTTAM} {SUT_I} [Trường Bộ Kinh 2.166; {CIT['saṃ. ni.']} 5.822; "
        f"Kinh Phật Tự Thuyết 51]! {S.ATTHEVA} {YES} {S.tena_hi(TH)}")
    add("5-624",
        f"{Q(TH)} {YES} {S.NANU_VUTTAM} {SUT_A}. {S.ATTHEVA} {YES} {S.tena_hi_na(TH)}",
        S.katha_end(KATHA[7]))

    # ---- (113) 8. Samādhikathā --------------------------------------------------------------------------------
    heading("5-19-6-0", 4, VAGGA)
    heading("5-19-6-1-0", 5, f"(113) 8. {S.katha(KATHA[8])}")
    GONE2 = "quá khứ đã chấm dứt, tương lai chưa sinh ra"   # atītaṃ niruddhaṃ anāgataṃ ajātaṃ (termbase)
    add("5-625",
        f"{Q(CS)} {YES} {Q('sự liên tục của tâm thuộc quá khứ là sự định tâm')} {NO_PE} {q(CS)} {YES} "
        f"{Q('sự liên tục của tâm thuộc tương lai là sự định tâm')} {NO_PE} {q(CS)} {YES} {NANU(GONE2)} {YES} "
        f"{S.hanci_neg(GONE2, CS)}")
    WHO = ([f"{SAM} thức qua {x}" for x in ("tai", "mũi", "lưỡi", "thân")] + [f"{SAM} tâm bất thiện"]
           + [f"{SAM} tâm có {x} đi kèm" for x in ("sự tham đắm", "sự sân hận", "sự si mê",
                                                  "sự không biết ghê sợ tội lỗi")])
    ACC = f"{PE} ".join(f"có {x} đi kèm" for x in ("sự tham đắm", "sự sân hận", "sự si mê",
                                                   "sự không biết ghê sợ tội lỗi"))
    add("5-626",
        f"{Q('sự định tâm kéo dài trong khoảnh khắc của một tâm')} {YES} {Q(f'{SAM} thức qua mắt {NAP}')} "
        f"{NO_PE} {q(f'{PE} '.join(WHO) + f' {NAP}')} {NO_PE}",
        f"{Q(CS)} {YES} {Q('sự liên tục của tâm bất thiện là sự định tâm')} {NO_PE} "
        f"{q(f'sự liên tục của tâm {ACC} là sự định tâm')} {NO_PE}",
        f"{S.na_vattabbam(CS)} {YES} {S.NANU_VUTTAM} {SUT_N}! {S.ATTHEVA} {YES} {S.tena_hi(CS)}",
        S.katha_end(KATHA[8]))

    # ---- (114) 9. Dhammaṭṭhitatākathā -------------------------------------------------------------------------
    heading("5-19-7-0", 4, VAGGA)
    heading("5-19-7-1-0", 5, f"(114) 9. {S.katha(KATHA[9])}")

    def st(head):
        return f"{head} {YES} {Q(TT)} {NO_PE} {q(TT)} {YES} {Q(TAYA)} {NO_PE}"

    add("5-627",
        st(Q(f"sự ổn định của các hiện tượng {PN}")),
        st(Q(f"sự ổn định của vật chất {PN}")),
        st(f"Có phải sự ổn định của cảm giác{PE} sự ổn định của tri giác{PE} sự ổn định của các tạo tác{PE} "
           f"sự ổn định của thức {PN} không?"),
        S.katha_end(KATHA[9]))

    # ---- (115) 10. Aniccatākathā ------------------------------------------------------------------------------
    heading("5-19-8-0", 4, VAGGA)
    heading("5-19-8-1-0", 5, f"(115) 10. {S.katha(KATHA[10])}")

    def of_(x, end=NO_PE, mid=NO_PE, cap_mid=False):   # X parinipphannā? Tāya X-āya X …
        xx = f"{x} của {x} ấy {PN}"
        mid_q = Q(xx) if cap_mid else q(xx)
        return f"{Q(f'{x} {PN}')} {YES} {Q(xx)} {mid} {mid_q} {YES} {Q(TAYA)} {end}"

    add("5-628",
        of_(AT, end=NO),
        of_(JR),
        of_(MR, mid=NO, cap_mid=True))

    def has(x, attr):
        return f"{x} {PN}, {attr} của {x} {EX}"

    def gone(x):
        return f"{x} {PN}, sự tan rã của {x} {EX}, sự biến mất {EX}"

    AT_AT, JR_JR = has(AT, AT), has(JR, JR)
    VED = f"cảm giác{PE} tri giác{PE} các tạo tác{PE} thức {PN}, {AT} của thức {EX}"
    add("5-629",
        f"{Q(has('vật chất', AT))} {YES} {Q(AT_AT)} {NO_PE} {q(has('vật chất', JR))} {YES} {Q(JR_JR)} {NO_PE}",
        f"{Q(gone('vật chất'))} {YES} {Q(gone(MR))} {NO_PE}",
        f"{Q(VED)} {YES} {Q(AT_AT)} {NO_PE} {q(has('thức', JR))} {YES} {Q(JR_JR)} {NO_PE}",
        f"{Q(gone('thức'))} {YES} {Q(gone(MR))} {NO_PE}",
        S.katha_end(KATHA[10]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Helpers (read only: finished pi-5 rails chapters and the Pāli keyword map / termbase)
# ---------------------------------------------------------------------------------------------------------------
def _lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def find(pat, maxhits=8):
    pat = re.compile(pat)
    hits = 0
    for vf in sorted(S.OUT_DIR.glob("*.md")):
        pf = S.PALI_DIR / vf.name
        if not pf.exists() or vf.name == NAME:
            continue
        pl, vl = _lines(pf), _lines(vf)
        for i, ln in enumerate(pl):
            if not pat.search(ln):
                continue
            print(f"[{vf.name} line {i + 1}]")
            print("  PI:", ln)
            print("  VI:", vl[i] if i < len(vl) else "<missing>")
            hits += 1
            if hits >= maxhits:
                return


def kw():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb.setdefault(ln.split(": {", 1)[0].lower(), ln)
    seen = set()
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip() or "] " not in line:
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        m = re.fullmatch(r"5-(\d+)", i)
        if not (i.startswith("5-19-") or (m and 605 <= int(m.group(1)) <= 629)):
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                print(f"[{i}] {tb.get(kk.lower(), kk + ': <NOT IN TERMBASE>')}")


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-19"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--find"]:
        find(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8)
    elif sys.argv[1:2] == ["--kw"]:
        kw()
    else:
        main()
