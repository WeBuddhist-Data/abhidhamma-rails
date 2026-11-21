# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 19: 19-ekadasamavaggo.md (Ekādasamavaggo, ^5-19-0 … ^5-629),
the kathā (106-108) … (115) of the eleventh vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished
chapter builders build_2_vi / build_4_vi / build_9_vi (read-only, importing writes nothing) for the kilesa /
anusaya lists, the puthujjana word and the vagga close, so every repeat is byte-identical with those chapters.
The anusaya / ñāṇa debate strings of ch17 (^5-554 … ^5-558) are rebuilt here from the same pieces and asserted
to occur in the ch17 output. Every string claimed from the pi-1..4 Vietnamese rails is asserted to occur there,
every string taken from a finished pi-5 chapter is asserted to occur in that chapter's output; the sample's
per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli. Every Pāli sentence keeps
its own sentence.

run:  python -I -B -X utf8 build_19_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (kilesa words, kāmarāga list, anusaya list, Hañci … no ca vata)
import build_4_vi as C4      # noqa: E402  (puthujjano)
import build_9_vi as C9      # noqa: E402  (Tassuddānaṃ –)

NAME = "19-ekadasamavaggo.md"
Q, q, NANU, AM, cap = B.Q, B.q, B.NANU, B.AMANTA, B.cap
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA = B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA
HNO = C2.hanci_no                                          # Hañci P, no ca vata re vattabbe – "Q"ti. (ch2)
VAR, SPELL = B.VAR, B.SPELL
VAGGA11 = B.VAGGA[11]                                      # Ekādasamavaggo = «Chương thứ mười một» (terms file)
K, E = B.KATHA.format, B.KATHA_END.format


def tena_hi_lc(x):
    """…pe… tena hi Xti. (lowercase start, ch14 / ch17)"""
    return f"vậy thì {x}."


def heads(n, num, k, title):
    """#### Ekādasamavaggo ^5-19-n-0 / ##### (num) k. <title> ^5-19-n-1-0"""
    return [(4, VAGGA11, f"5-19-{n}-0"), (5, f"({num}) {k}. {K(x=title)}", f"5-19-{n}-1-0")]


# ================================================================ shared terms
AB = "không xác định về mặt đạo đức"                       # abyākata (core, pi-1)
AKU = "là bất thiện"                                      # akusala (predicate; ch13 «và nó là bất thiện»)
AH, SH = "không có gốc rễ", "có gốc rễ"                    # ahetuka / sahetuka (pi-1 ^1-1079/1080)
CV, CS = "không gắn liền với tâm", "gắn liền với tâm"      # cittavippayutta / cittasampayutta (pi-1 ^1-1197/1198)
WITH_CITTA = "gắn liền với tâm ấy"                         # tena cittena sampayutta
WITH_HETU = f"{SH} nhờ gốc rễ ấy"                          # tena hetunā sahetuka
VAB = "cái không xác định về mặt đạo đức thuộc loại quả của nghiệp"   # vipākābyākata (vipāka «quả của nghiệp» pi-1)
KAB = "cái không xác định về mặt đạo đức mang tính chức năng"         # kiriyābyākata (pi-1 «… mang tính chức năng»)
RUPA, NIB = B.RUPA, "Niết-bàn"
RN = f"là {RUPA}, {NIB}, {B.AYATANA[0]}… {B.AYATANA[9]}"   # rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ (ch17)
RN2 = f"là {VAB}, {KAB}, {RUPA}, {NIB}, {B.AYATANA[0]}… {B.AYATANA[9]}"   # vipākābyākatā kiriyābyākatā rūpaṃ …
ANUS = C2.ANUSAYA                                          # anusayā = «các khuynh hướng tiềm ẩn» (pi-2, ch2)
AN7 = C2.AN7.split(", ")                                   # kāmarāgānusayo … avijjānusayo (pi-2, ch2)
KRA, PAT, MAN, DIT, VIC, BHA, AVA = AN7
AN_REST = ", ".join(AN7[1:])                               # paṭighānusayo … avijjānusayo (ch17)
RAGA, DOSA, MOHA = C2.R, C2.D, C2.M                        # rāgo doso moho (pi-1, ch2)
KIL = "phiền não"                                         # kilesa (core)
assert C2.KR.startswith(f"{C2.R}, ")
KR6L = C2.KR[len(f"{C2.R}, "):].split(", ")               # kāmarāgo … kāmacchandanīvaraṇaṃ (ch2, ch17)
KR6 = ", ".join(KR6L)
KR1 = KR6L[0]                                              # kāmarāgo = «sự tham đắm dục lạc»
KR4 = ", ".join([KR6L[0], KR6L[1], KR6L[2], KR6L[5]])     # kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmacchandanīvaraṇaṃ
KR_PE = f"{KR6L[0]}, {KR6L[1]}… {KR6L[5]}"                 # kāmarāgo kāmarāgapariyuṭṭhānaṃ…pe… kāmacchandanīvaraṇaṃ
PAT3 = "sự ác cảm, sự ám ảnh của ác cảm, xiềng xích ác cảm"                  # paṭighaṃ paṭighapariyuṭṭhānaṃ paṭighasaṃyojanaṃ
MAN3 = "sự kiêu mạn, sự ám ảnh của kiêu mạn, xiềng xích kiêu mạn"            # māno mānapariyuṭṭhānaṃ mānasaṃyojanaṃ
DIT5 = "quan điểm, dòng lũ quan điểm, ách quan điểm, sự ám ảnh của quan điểm, xiềng xích quan điểm"
# diṭṭhi diṭṭhogho diṭṭhiyogo diṭṭhipariyuṭṭhānaṃ diṭṭhisaṃyojanaṃ (pi-1 xiềng xích quan điểm; ogha / yoga on the
# ch10 «dòng lũ vô minh, ách vô minh» pattern; pariyuṭṭhāna «sự ám ảnh của …» ch2, ch10)
VIC4 = "sự hoài nghi, sự ám ảnh của hoài nghi, xiềng xích hoài nghi, chướng ngại hoài nghi"   # (ch10)
BHA3 = "sự tham đắm hiện hữu, sự ám ảnh của tham đắm hiện hữu, xiềng xích tham đắm hiện hữu"
# bhavarāgo bhavarāgapariyuṭṭhānaṃ bhavarāgasaṃyojanaṃ (pi-1 «sự tham đắm hiện hữu», «xiềng xích tham đắm hiện hữu»)
AVJ = "vô minh"
AVJ7 = ("vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, xiềng xích vô "
        "minh, chướng ngại vô minh")                     # (ch10, ch17)
AVJ6 = AVJ7.replace("khuynh hướng tiềm ẩn vô minh, ", "")  # avijjā avijjogho avijjāyogo avijjāpariyuṭṭhānaṃ … avijjānīvaraṇaṃ
AVJ4 = "vô minh, dòng lũ vô minh, ách vô minh, chướng ngại vô minh"   # avijjā avijjogho avijjāyogo avijjānīvaraṇaṃ
AVJ_PE = "vô minh, dòng lũ vô minh… chướng ngại vô minh"   # avijjā avijjogho…pe… avijjānīvaraṇaṃ (ch17)
KUS = "khi tâm thiện hay không xác định về mặt đạo đức đang diễn ra"   # kusalābyākate citte vattamāne (pi-1, ch17)
PU = C4.PUTHUJJANA                                        # puthujjano = «người phàm phu» (pi-1, ch4)
SANU = f"{KUS}, {PU} nên gọi là “có khuynh hướng tiềm ẩn”"   # "sānusayo"ti vattabbo ("X"ti vattabbo sample, ch12)
SARA = f"{KUS}, {PU} nên gọi là “có tham đắm”"              # "sarāgo"ti vattabbo (sarāga ch17)
SAMMUKHA = "các hiện tượng thiện và bất thiện đi đến chỗ cùng hiện diện đối mặt nhau"
# kusalākusalā dhammā sammukhībhāvaṃ āgacchanti (ch15 ^5-485)
SKP = "thuộc về khối tạo tác"                             # saṅkhārakkhandhapariyāpanna (ch17)
KATAMA, SKP_ANS = "Thuộc về khối nào?", "Thuộc về khối tạo tác."   # (ch17)
SKK = "khối tạo tác"
VS2 = "khối cảm giác, khối tri giác"                       # vedanākkhandho saññākkhandho (pi-2)


def part(x):
    """X ekadeso cittasampayutto ekadeso cittavippayutto (ch17 «một phần …, một phần …»)"""
    return f"{x} một phần {CS}, một phần {CV}"


# ================================================================ (109)-(110) ñāṇa
NANA, PANNA = "hiểu biết", "trí tuệ"                       # ñāṇa / paññā (pi-1)
NANI, PANNAVA = "người có hiểu biết", "người có trí tuệ"   # ñāṇī / paññavā (pi-2, ch17)
VR, NK_ = C2.EP[0], "không có phiền não"                   # vītarāgo (ch2) / nikkileso (ch11 nikkilesaṃ)


def vig(x):
    """X-e vigate = «khi X đã mất đi» (vigata ch5, ch12)"""
    return f"khi {x} đã mất đi"


AC = f"{vig('sự không biết')}, khi tâm không gắn liền với hiểu biết đang diễn ra"
# aññāṇe vigate ñāṇavippayutte citte vattamāne (aññāṇa pi-1; ñāṇavippayutta «không gắn liền với hiểu biết» pi-1)
DMK = f"{vig(DOSA)}… {vig(MOHA)}… {vig(KIL)}"              # dose vigate… mohe vigate… kilese vigate


def say(cond, x, neg, low=False):
    """cond (na) vattabbaṃ – "x"ti?"""
    return f"{'c' if low else 'C'}ó phải {cond}, thì {'không ' if neg else ''}nên nói – “{x}” không?"


T5 = f"{NANA} {CV}"                                        # ñāṇaṃ cittavippayuttaṃ
PN5 = "trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ, quan điểm đúng đắn, chi phần giác ngộ là sự tìm hiểu các hiện tượng"
# paññā paññindriyaṃ paññābalaṃ sammādiṭṭhi dhammavicayasambojjhaṅgo (pi-1 ^1-292, ch17)
ARAHA_C = "bậc A-la-hán có được thức qua mắt"             # arahā cakkhuviññāṇasamaṅgī (ch17)
NOTE617 = f"[có vẻ là câu hỏi của {B.SAKAVADI}]"            # [sakavādīpucchā viya dissati]

# ================================================================ (111) Idaṃ dukkhaṃ
D_ = "đây là khổ đau"                                     # idaṃ dukkhaṃ (ch10 ‘Idaṃ dukkha’nti «Đây là khổ đau»)
SD_ = "đây là sự phát sinh của khổ đau"                   # ayaṃ dukkhasamudayo (ch10)
ND_ = "đây là sự chấm dứt khổ đau"                        # ayaṃ dukkhanirodho (ch10)
MG_ = "đây là con đường"                                  # ayaṃ maggo (magga «con đường» pi-1)
S_, N_ = "đây là sự phát sinh", "đây là sự chấm dứt"       # ayaṃ samudayo / ayaṃ nirodho
RA, VA = f"{RUPA} là vô thường", "thức là vô thường"       # rūpaṃ aniccaṃ / viññāṇaṃ aniccaṃ
RT, VT = f"{RUPA} không phải là tự ngã", "thức không phải là tự ngã"   # rūpaṃ anattā (anatta pi-2)
VSS = f"{cap(B.VEDANA)}… {B.SANNA}… {B.SANKHARA}"          # Vedanā… saññā… saṅkhārā…
VSS_LC = f"{B.VEDANA}… {B.SANNA}… {B.SANKHARA}"
KX6 = f"việc nói rằng {D_}"                                # Idaṃ dukkhantikathā


def pos(a, b):
    """"a"ti vācaṃ bhāsato "b"ti ñāṇaṃ pavattati"""
    return f"khi nói lời “{a}”, hiểu biết “{b}” khởi lên"


def neg(a, b):
    """"a"ti vācaṃ bhāsato na ca "b"ti ñāṇaṃ pavattati"""
    return f"nói lời “{a}” mà hiểu biết “{b}” không khởi lên"


# ================================================================ (112) Iddhibala
IBK = "sức mạnh thần thông"                                # iddhibala (iddhi «thần thông» pi-1; bala «sức mạnh» ch11)
T7 = f"người được trang bị {IBK} có thể tồn tại suốt một kiếp"
# iddhibalena samannāgato kappaṃ tiṭṭheyya (samannāgata ch12; kappaṃ tiṭṭhati «… suốt một kiếp» ch10;
# tiṭṭhati of a being «tồn tại», terms file Kappaṭṭhakathā)
MAYA = ("tuổi thọ ấy do thần thông tạo ra, cõi tái sinh ấy do thần thông tạo ra, sự có được sự tồn tại cá nhân "
        "ấy do thần thông tạo ra")
# iddhimayiko so āyu, iddhimayikā sā gati, iddhimayiko so attabhāvappaṭilābho (āyu pi-2; gati sample;
# attabhāvapaṭilābha ch11)
LIVE = "có thể tồn tại khi còn sự sống, còn phần còn lại của sự sống"           # sati jīvite jīvitāvasese tiṭṭheyya
DEAD = "có thể tồn tại khi không còn sự sống, không còn phần còn lại của sự sống"   # asati jīvite jīvitāvasese …
DEAD_Q = (f"Có phải nếu {DEAD}, thì người đã chết có thể tồn tại, người đã qua đời có thể tồn tại không?")
# Asati … tiṭṭheyyāti, mato tiṭṭheyya, kālaṅkato tiṭṭheyyāti? (sample «Có phải nếu X, thì Y không?»;
# kālakiriyā «sự qua đời» pi-2)


def hold(x, end="đừng chấm dứt"):
    """X mā nirujjhīti / niccaṃ hotūti / mā jāyiṃsūti labbhā iddhiyā paggahetuṃ"""
    return f"có thể dùng thần thông mà giữ cho {x} {end}"


UPP = "đã sinh khởi"                                       # uppanna (pi-1)
UPP9 = "… ".join(f"{x} {UPP}" for x in (B.VEDANA, B.SANNA, "chủ ý", "tâm", "niềm tin", "sự tinh tấn",
                                         "sự tỉnh thức", "sự định tâm", PANNA))
# uppannā vedanā…pe… … uppannā paññā (ch12 / ch17 list «chủ ý, tâm, niềm tin, sự tinh tấn, sự tỉnh thức, sự định
# tâm, trí tuệ»)
SATTA = "các chúng sinh có bản chất phải {x}"              # jāti- / jarā- / byādhi- / maraṇadhammā sattā (pi-2)
J4 = [("sinh", "đừng sinh ra"), ("lão hóa", "đừng lão hóa"), ("bệnh", "đừng bệnh"), ("chết", "đừng chết")]
NK = ("không có người bảo đảm nào, dù là sa-môn hoặc bà-la-môn hoặc vị trời hoặc Ma vương hoặc Phạm thiên hoặc "
      "bất cứ ai trong thế gian")
# natthi koci pāṭibhogo samaṇo vā brāhmaṇo vā devo vā māro vā brahmā vā koci vā lokasmiṃ («sa-môn hoặc bà-la-môn»
# pi-2; devo «vị trời», Māra «Ma vương» sample; brahmā «Phạm thiên», pāṭibhoga «người bảo đảm» new)
SUTTA_DN = ("Bất cứ ai, này A-nan, có bốn nền tảng thần thông được tu tập, được làm đi làm lại, được biến thành cỗ "
            "xe, được biến thành nền tảng, được thiết lập vững chắc, được làm cho quen thuộc, được khởi sự đúng đắn, "
            "thì người ấy, nếu muốn, có thể tồn tại suốt một kiếp hoặc phần còn lại của kiếp")
# yassa kassaci, ānanda, cattāro iddhipādā bhāvitā bahulīkatā yānīkatā vatthukatā anuṭṭhitā paricitā susamāraddhā,
# so ākaṅkhamāno kappaṃ vā tiṭṭheyya kappāvasesaṃ vā (iddhipāda ch2; «được tu tập, được làm đi làm lại» pi-2)
SUTTA_AN = (f"Này các tỳ-khưu, đối với bốn hiện tượng, {NK}! Đối với bốn hiện tượng nào? Để điều có bản chất phải "
            f"lão hóa “đừng lão hóa”, {NK}. Để điều có bản chất phải bệnh “đừng bệnh”… để điều có bản chất phải chết "
            f"“đừng chết”… còn những nghiệp xấu ác đã làm trước đây, là đối tượng của phiền não, đưa đến sự hiện hữu "
            f"mới [{SPELL} (Sī., Pī.): ponobhavikāni], đầy lo âu [{VAR} (Sī., Pī., Ka.): nissārāni; (Syā.): "
            f"dukkhudrayāni], có kết quả khổ đau, dẫn đến sự sinh, sự lão hóa và sự chết trong tương lai, để quả của "
            f"chúng “đừng phát sinh”, {NK}. Này các tỳ-khưu, đối với bốn hiện tượng này, {NK}")
# catunnaṃ, bhikkhave, dhammānaṃ … Jarādhammo "mā jīrī"ti … saṃkilesikāni («là đối tượng của phiền não» pi-1)
# ponobbhavikāni (punabbhava «sự hiện hữu mới» coordinator) sadarāni dukkhavipākāni («có kết quả khổ đau» ch10)
# āyatiṃ jātijarāmaraṇiyāni (jarāmaraṇa «sự lão hóa và sự chết» pi-2) … "mā nibbattī"ti (nibbatta «phát sinh» ch5).
# The inner quotes are " in the Pāli (not ‘…’): kept as written.

# ================================================================ (113) Samādhi
CSN = "sự liên tục của tâm"                                # cittasantati (santati «sự liên tục» pi-1)
SAMA = "sự định tâm"                                      # samādhi (noun, ch12 / ch17 list)
T8 = f"{CSN} là {SAMA}"
PAST_FUT = "quá khứ đã chấm dứt, tương lai chưa sinh ra"   # atītaṃ niruddhaṃ anāgataṃ ajātaṃ (ch5)
SAMAP = "người đang nhập thành tựu thiền"                  # samāpanno (ch10)
SMG = "người có được"                                     # -samaṅgī (ch13, ch17)
SG = "tâm có {x} đi kèm"                                  # X-sahagataṃ cittaṃ (pi-1 «có niềm vui đi kèm»)
AO = C2.AO                                                # anottappaṃ = «sự không biết ghê sợ tội lỗi» (pi-1)
SUTTA_MN = ("Ta, này các hiền giả Ni-kiền-tử, có thể không lay động thân, không nói ra lời, suốt bảy ngày đêm "
            f"[{SPELL} (Ka.): rattidivāni] sống cảm nhận hạnh phúc thuần nhất")
# ahaṃ kho, āvuso nigaṇṭhā, pahomi aniñjamāno kāyena, abhāsamāno vācaṃ, satta rattindivāni [rattidivāni (ka.)]
# ekantasukhaṃ paṭisaṃvedī viharituṃ (āvuso «này các hiền giả» ch10; «Ta» for the Buddha ch10)

# ================================================================ (114)-(115) ṭhitatā, aniccatā
PN = "được hình thành trọn vẹn"                            # parinipphanna (new)
TT = ("đối với từng cái như vậy, không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt vòng luân chuyển, "
      "không có sự nhập Niết-bàn trọn vẹn không còn bám víu")
# tāya tāyeva / tassa tasseva natthi dukkhassantakiriyā, natthi vaṭṭupacchedo, natthi anupādāparinibbānaṃ
# (ch1 ^5-125 wording; «từng người» there, «từng cái» here: the referent is a thing)
TH = "sự ổn định"                                         # ṭhitatā (ch14 dhammaṭṭhitatā «sự ổn định của các hiện tượng»)
DTH = f"{TH} của các hiện tượng"
ANC, JARA, MAR = "tính vô thường", "sự lão hóa", "sự chết"   # aniccatā (pi-1) / jarā / maraṇa (pi-2)
BHEDO = "sự tan rã"                                       # bhedo (pi-1, pi-2)
ANTA = "sự biến mất"                                      # antaradhānaṃ (pi-1, pi-2)


def regress(x, xx, mid=NHP, end=NHP, low_mid=True):
    """X parinipphannā? Āmantā. XX parinipphannā? Na hevaṃ… XX …? Āmantā. Tāya tāyeva natthi …? Na hevaṃ…"""
    again = q(f"{xx} {PN}") if low_mid else Q(f"{xx} {PN}")
    return f"{Q(f'{x} {PN}')} {AM} {Q(f'{xx} {PN}')} {mid} {again} {AM} {Q(TT)} {end}"


def has(x, what, of):
    """X parinipphannaṃ, X-assa Y atthi"""
    return f"{x} {PN}, có {what} của {of}"


# ================================================================ vagga close (ch9 frame)
TISSO = "cả ba loại khuynh hướng tiềm ẩn"                  # Tissopi anusayakathā (terms file heading)
UDDANA = (f"{cap(ANUS)} {AB}, {AH}, {CV}, {NANI} {vig('sự không biết')}, {T5}, hiểu biết khởi lên nơi âm thanh "
          f"[{VAR} (Sī.): yattha saddo; (?): yathāsaddaṃ], {T7}, {T8}, {DTH}, {ANC}.")
# Anusayā abyākatā, ahetukā, cittavippayuttā, aññāṇe vigate ñāṇī, ñāṇaṃ cittavippayuttaṃ, yattha sadde [yattha
# saddo (sī.), yathāsaddaṃ (?)] ñāṇaṃ pavattati, iddhibalena samannāgato kappaṃ tiṭṭheyya, cittasantati samādhi,
# dhammaṭṭhitatā, aniccatāti.  (uddāna = the thesis phrases as written, ch13 rule)


def build():
    d = B.Doc()
    d.head(3, VAGGA11, "5-19-0")
    # ------------------------------------------------------------ (106-108) anusaya
    d.head(4, f"(106-108) 1-3. {K(x=TISSO)}", "5-19-1-0")
    T1 = f"{ANUS} {AB}"

    def ab_line(an, lst, lst2):
        return (f"{Q(f'{an} {AB}')} {AM} {Q(f'{lst} {AB}')} {NHP} {q(f'{lst2} {AKU}')} {AM} "
                f"{Q(f'{an} {AKU}')} {NHP}")

    d.seg("5-605",
          f"{Q(T1)} {AM} {Q(RN2)} {NHP}",
          ab_line(KRA, KR6, KR_PE),
          ab_line(PAT, PAT3, PAT3),
          ab_line(MAN, MAN3, MAN3),
          ab_line(DIT, DIT5, DIT5),
          ab_line(VIC, VIC4, VIC4),
          ab_line(BHA, BHA3, BHA3),
          ab_line(AVA, AVJ6, AVJ6))
    d.seg("5-606",
          f"{NVQ(T1)} {AM} {Q(SANU)} {AM} {Q(SAMMUKHA)} {NHP} {tena_hi_lc(T1)} {Q(SARA)} {AM} {Q(SAMMUKHA)} {NHP} "
          f"{tena_hi_lc(f'{RAGA} {AB}')}")
    T2 = f"{ANUS} {AH}"
    d.seg("5-607",
          f"{Q(T2)} {AM} {Q(RN)} {NHP}",
          f"{Q(f'{KRA} {AH}')} {AM} {Q(f'{KR4} {AH}')} {NHP} {q(f'{KR_PE} {SH}')} {AM} {Q(f'{KRA} {SH}')} {NHP} "
          f"{q(f'{PAT}… {MAN}… {DIT}… {VIC}… {BHA}… {AVA} {AH}')} {AM} {Q(f'{AVJ6} {AH}')} {NHP} "
          f"{q(f'{AVJ_PE} {SH}')} {AM} {Q(f'{AVA} {SH}')} {NHP}")
    d.seg("5-608",
          f"{NVQ(T2)} {AM} {Q(SANU)} {AM} {Q(f'{ANUS} {WITH_HETU}')} {NHP} {tena_hi_lc(T2)} {Q(SARA)} {AM} "
          f"{Q(f'{RAGA} {WITH_HETU}')} {NHP} {tena_hi_lc(f'{RAGA} {AH}')}")
    T3 = f"{ANUS} {CV}"
    d.seg("5-609",
          f"{Q(T3)} {AM} {Q(RN)} {NHP}",
          f"{Q(f'{KRA} {CV}')} {AM} {Q(f'{KR6} {CV}')} {NHP} {q(f'{KR_PE} {CS}')} {AM} {Q(f'{KRA} {CS}')} {NHP}")

    def block(an, kil, end3=NHP):
        """the four lines Katamakkhandhapariyāpanno … ekadeso cittavippayuttoti? (^5-610 / ^5-612)"""
        return (
            f"{Q(f'{an} {CV}')} {AM} {KATAMA} {SKP_ANS} {Q(f'{SKK} {CV}')} {NH} {Q(f'{SKK} {CV}')} {AM} "
            f"{Q(f'{VS2} {CV}')} {NHP}",
            f"{Q(f'{an} {SKP} {CV}')} {AM} {Q(f'{kil} {SKP} {CV}')} {NHP} {q(f'{kil} {SKP} {CS}')} {AM} "
            f"{Q(f'{an} {SKP} {CS}')} {NHP}",
            f"{Q(f'{an} {SKP} {CV}, {kil} {SKP} {CS}')} {AM} {Q(part(SKK))} {end3}",
            f"{Q(part(SKK))} {AM} {Q(part(VS2))} {NHP}",
        )

    d.seg("5-610", *block(KRA, KR1))
    d.seg("5-611",
          f"{Q(f'{AN_REST} {CV}')} {AM} {Q(f'{AVJ4} {CV}')} {NHP} {q(f'{AVJ4} {CS}')} {AM} {Q(f'{AVA} {CS}')} {NHP}")
    d.seg("5-612", *block(AVA, AVJ, end3=NH))           # ^5-612 l.3: avijjāsaṅkhārakkhandhapariyāpannā (as meant)
    d.seg("5-613",
          f"{NVQ(T3)} {AM} {Q(SANU)} {AM} {Q(f'{ANUS} {WITH_CITTA}')} {NH} {TENA_HI(T3)} {Q(SARA)} {AM} "
          f"{Q(f'{RAGA} {WITH_CITTA}')} {NH} {TENA_HI(f'{RAGA} {CV}')}",
          E(x=TISSO))
    # ------------------------------------------------------------ (109) Ñāṇa
    for lv, t, sid in heads(2, 109, 4, NANA):
        d.head(lv, t, sid)
    d.seg("5-614",
          f"{say(AC, NANI, 1)} {AM} {say(vig(RAGA), VR, 1)} {NHP} {say(AC, NANI, 1, low=True)} {AM} "
          f"{say(DMK, NK_, 1)} {NHP}",
          f"{say(vig(RAGA), VR, 0)} {AM} {say(AC, NANI, 0)} {NHP} {say(DMK, NK_, 0, low=True)} {AM} "
          f"{say(AC, NANI, 0)} {NHP}")
    d.seg("5-615",
          f"{say(AC, NANI, 0)} {AM} "
          f"{Q(f'là {NANI} nhờ {NANA} thuộc quá khứ, là {NANI} nhờ {NANA} đã chấm dứt, đã mất đi, đã an tịnh')} {NHP}",
          E(x=NANA))
    # atītena ñāṇena ñāṇī niruddhena vigatena paṭipassaddhena ñāṇena ñāṇī (ch12 «là bậc giác ngộ nhờ sự giác ngộ»;
    # «đã chấm dứt, đã mất đi, đã an tịnh» ch12)
    # ------------------------------------------------------------ (110) Ñāṇaṃ cittavippayuttaṃ
    for lv, t, sid in heads(3, 110, 5, f"việc cho rằng {T5}"):
        d.head(lv, t, sid)
    d.seg("5-616",
          f"{Q(T5)} {AM} {Q(RN)} {NHP} {q(T5)} {AM} {Q(f'{PN5} {CV}')} {NHP} {q(f'{PN5} {CS}')} {AM} "
          f"{Q(f'{NANA} {CS}')} {NHP}",
          f"{Q(T5)} {AM} {KATAMA} {SKP_ANS} {Q(f'{SKK} {CV}')} {NHP} {q(f'{SKK} {CV}')} {AM} {Q(f'{VS2} {CV}')} {NHP} "
          f"{q(f'{NANA} {SKP} {CV}')} {AM} {Q(f'{PANNA} {SKP} {CV}')} {NHP} {q(f'{PANNA} {SKP} {CS}')} {AM} "
          f"{Q(f'{NANA} {SKP} {CS}')} {NHP} {q(f'{NANA} {SKP} {CV}, {PANNA} {SKP} {CS}')} {AM} {Q(part(SKK))} {NHP} "
          f"{q(part(SKK))} {AM} {Q(part(VS2))} {NHP}")
    d.seg("5-617",
          f"{NVQ(T5)} {AM} {Q(f'{ARAHA_C} nên gọi là “{NANI}”')} {AM} {Q(f'{NANA} {WITH_CITTA}')} {NH} {TENA_HI(T5)}",
          f"Có phải {ARAHA_C} nên gọi là “{PANNAVA}” không {NOTE617}? {AM} {Q(f'{PANNA} {WITH_CITTA}')} {NH} "
          f"{TENA_HI(f'{PANNA} {CV}')}",
          E(x=f"việc cho rằng {T5}"))
    # ------------------------------------------------------------ (111) Idaṃ dukkhaṃ
    for lv, t, sid in heads(4, 111, 6, KX6):
        d.head(lv, t, sid)
    PD = Q(pos(D_, D_))
    d.seg("5-618",
          f"{PD} {AM} {Q(pos(SD_, SD_))} {NHP} {q(pos(D_, D_))} {AM} {Q(pos(ND_, ND_))} {NHP} {q(pos(D_, D_))} {AM} "
          f"{Q(pos(MG_, MG_))} {NHP}",
          f"{Q(neg(S_, S_))} {AM} {Q(neg(D_, D_))} {NHP} có phải nói lời “{N_}”… “{MG_}” mà hiểu biết “{MG_}” không "
          f"khởi lên không? {AM} {Q(neg(D_, D_))} {NHP}")
    d.seg("5-619",
          f"{PD} {AM} {Q(pos(RA, RA))} {NHP} {q(pos(D_, D_))} {AM} {VSS}… {q(pos(VA, VA))} {NHP}",
          f"{PD} {AM} {Q(pos(RT, RT))} {NHP} {q(pos(D_, D_))} {AM} {VSS}… {q(pos(VT, VT))} {NHP}",
          f"{Q(neg(RA, RA))} {AM} {Q(neg(D_, D_))} {NHP} {VSS_LC}… {q(neg(VA, VA))} {AM} {Q(neg(D_, D_))} {NHP}",
          f"{Q(neg(RT, RT))} {AM} {Q(neg(D_, D_))} {NHP} {VSS_LC}… {q(neg(VT, VT))} {AM} "
          f"{Q(neg(D_, 'khổ đau'))} {NHP}")              # last: na ca "dukkha"nti (no idaṃ), as written
    d.seg("5-620",
          f"{PD} {AM} Có phải hiểu biết khởi lên cả về “i” [{SPELL} (Syā., Pī.): īti], cả về “dam”, cả về “du” "
          f"[{SPELL} (Syā., Pī.): dūti], cả về “kham” không? {NHP}",
          E(x=KX6))
    # "I"ti ca "da"nti ca "du"ti ca "kha"nti ca (the syllables of idaṃ dukkhaṃ: i, daṃ, du, khaṃ; written without
    # the niggahīta sign, which is not allowed outside brackets)
    # ------------------------------------------------------------ (112) Iddhibala
    for lv, t, sid in heads(5, 112, 7, IBK):
        d.head(lv, t, sid)
    d.seg("5-621",
          f"{Q(T7)} {AM} {Q(MAYA)} {NHP}",
          f"{Q(T7)} {AM} {Q('có thể tồn tại suốt kiếp thuộc quá khứ, có thể tồn tại suốt kiếp thuộc tương lai')} {NHP} "
          f"{q(T7)} {AM} {Q('có thể tồn tại suốt hai kiếp, có thể tồn tại suốt ba kiếp, có thể tồn tại suốt bốn kiếp')} "
          f"{NHP} {q(T7)} {AM} {cap(LIVE)}, hay {DEAD}? {cap(LIVE)}. {HNO(LIVE, T7)} {DEAD_Q} {NHP}")
    mv = SATTA.format
    d.seg("5-622",
          f"{Q(T7)} {AM} {Q(hold('sự tiếp xúc ' + UPP))} {NHP} {q(hold(UPP9))} {NHP}",
          f"{Q(T7)} {AM} {Q(hold(RUPA, 'thường còn'))} {NHP} "
          f"{q(hold(f'{VSS_LC}… thức', 'thường còn'))} {NHP}",
          f"{Q(T7)} {AM} {Q(hold(mv(x=J4[0][0]), J4[0][1]))} {NHP} "
          f"{q(hold(f'{mv(x=J4[1][0])} {J4[1][1]}… {mv(x=J4[2][0])} {J4[2][1]}… {mv(x=J4[3][0])}', J4[3][1]))} {NHP}")
    d.seg("5-623",
          f"{NVQ(T7)} {AM} {B.NANU_VUTTAM} “{SUTTA_DN}” [Trường Bộ Kinh 2.166; Tương Ưng Bộ Kinh 5.822; Kinh Phật Tự "
          f"Thuyết 51]! {B.ATTHEVA} {AM} {TENA_HI(T7)}")
    d.seg("5-624",
          f"{Q(T7)} {AM} {B.NANU_VUTTAM} “{SUTTA_AN}” [Tăng Chi Bộ Kinh 4.182]. {B.ATTHEVA} {AM} {TENA_HI_NA(T7)}",
          E(x=IBK))
    # ------------------------------------------------------------ (113) Samādhi
    for lv, t, sid in heads(6, 113, 8, SAMA):
        d.head(lv, t, sid)
    d.seg("5-625",
          f"{Q(T8)} {AM} {Q(f'{CSN} thuộc quá khứ là {SAMA}')} {NHP} {q(T8)} {AM} "
          f"{Q(f'{CSN} thuộc tương lai là {SAMA}')} {NHP} {q(T8)} {AM} {NANU(PAST_FUT)} {AM} {HNO(PAST_FUT, T8)}")
    vin = [f"{SMG} thức qua {x}" for x in ("tai", "mũi", "lưỡi", "thân")]
    cit = [f"{SMG} tâm bất thiện"] + [f"{SMG} {SG.format(x=x)}" for x in (RAGA, DOSA, MOHA, AO)]
    d.seg("5-626",
          f"{Q(f'{SAMA} kéo dài trong khoảnh khắc của một tâm')} {AM} {Q(f'{SMG} thức qua mắt là {SAMAP}')} {NHP} "
          f"{q(chain_all(vin + cit) + f' là {SAMAP}')} {NHP}",
          f"{Q(T8)} {AM} {Q(f'sự liên tục của tâm bất thiện là {SAMA}')} {NHP} "
          f"{q(f'sự liên tục của tâm có {RAGA} đi kèm… có {DOSA} đi kèm… có {MOHA} đi kèm… có {AO} đi kèm là {SAMA}')} "
          f"{NHP}",
          f"{NVQ(T8)} {AM} {B.NANU_VUTTAM} “{SUTTA_MN}” [Trung Bộ Kinh 1.180]! {B.ATTHEVA} {AM} {TENA_HI(T8)}",
          E(x=SAMA))
    # ------------------------------------------------------------ (114) Dhammaṭṭhitatā
    for lv, t, sid in heads(7, 114, 9, DTH):
        d.head(lv, t, sid)
    TT2 = f"{TH} của {TH} ấy"                                # tāya ṭhitatā
    d.seg("5-627",
          regress(DTH, TT2),
          regress(f"{TH} của {RUPA}", TT2),
          regress(f"{TH} của {B.VEDANA}… {TH} của {B.SANNA}… {TH} của {B.SANKHARA}… {TH} của thức", TT2),
          E(x=DTH))
    # ------------------------------------------------------------ (115) Aniccatā
    for lv, t, sid in heads(8, 115, 10, ANC):
        d.head(lv, t, sid)
    d.seg("5-628",
          regress(ANC, f"{ANC} của {ANC} ấy", end=NH),
          regress(JARA, f"{JARA} của {JARA} ấy"),
          regress(MAR, f"{MAR} của {MAR} ấy", mid=NH, low_mid=False))
    d.seg("5-629",
          f"{Q(has(RUPA, ANC, RUPA))} {AM} {Q(has(ANC, ANC, ANC))} {NHP} {q(has(RUPA, JARA, RUPA))} {AM} "
          f"{Q(has(JARA, JARA, JARA))} {NHP}",
          f"{Q(f'{has(RUPA, BHEDO, RUPA)}, có {ANTA}')} {AM} {Q(f'{has(MAR, BHEDO, MAR)}, có {ANTA}')} {NHP}",
          f"{Q(has(f'{VSS_LC}… thức', ANC, 'thức'))} {AM} {Q(has(ANC, ANC, ANC))} {NHP} {q(has('thức', JARA, 'thức'))} "
          f"{AM} {Q(has(JARA, JARA, JARA))} {NHP}",
          f"{Q(f'{has(B.VINNANA, BHEDO, B.VINNANA)}, có {ANTA}')} {AM} {Q(f'{has(MAR, BHEDO, MAR)}, có {ANTA}')} "
          f"{NHP}",
          E(x=ANC),
          f"{VAGGA11}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


def chain_all(items):
    return "… ".join(items)


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("không xác định về mặt đạo đức", 1), ("mang tính chức năng", 1), ("Quả của nghiệp", 1),
    ("Những hiện tượng nào có gốc rễ?", 1), ("Những hiện tượng nào không có gốc rễ?", 1),
    ("Những hiện tượng nào gắn liền với tâm?", 1), ("Những hiện tượng nào không gắn liền với tâm?", 1),
    ("không gắn liền với hiểu biết", 1), ("xiềng xích ác cảm", 1), ("xiềng xích kiêu mạn", 1),
    ("xiềng xích quan điểm", 1), ("xiềng xích hoài nghi", 1), ("xiềng xích tham đắm hiện hữu", 1),
    ("sự tham đắm hiện hữu", 1), ("xiềng xích vô minh", 1), ("Bốn dòng lũ", 1), ("Bốn ách", 1),
    ("thiện và không xác định về mặt đạo đức", 1), ("người phàm phu", 1), ("sự không biết", 1),
    ("khối tạo tác", 2), ("khối cảm giác", 2), ("khối tri giác", 2), ("có niềm vui đi kèm", 1),
    ("tính vô thường của vật chất", 1), ("sự liên tục của vật chất", 1), ("sự tan rã", 1), ("sự biến mất", 1),
    ("sự lão hóa", 2), ("sự chết", 2), ("sự lão hóa và sự chết", 2), ("sự qua đời", 2),
    ("những chúng sinh có bản chất phải sinh", 2), ("chúng sinh có bản chất phải lão hóa", 2),
    ("chúng sinh có bản chất phải bệnh", 2), ("chúng sinh có bản chất phải chết", 2),
    ("được tu tập, được làm đi làm lại", 2), ("sa-môn hoặc bà-la-môn", 2), ("là đối tượng của phiền não", 1),
    ("thường còn", 2), ("không phải là tự ngã", 2), ("tuổi thọ", 2), ("đã sinh khởi", 1), ("thần thông", 1),
    ("trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ", 1), ("chi phần giác ngộ là sự tìm hiểu các hiện tượng", 1),
    ("người có trí tuệ", 2), ("thức qua mắt", 2), ("Trường Bộ Kinh", 4), ("Trung Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
CH17_556 = (f"Có phải {KUS}, {PU} nên được gọi là có khuynh hướng tiềm ẩn không?")
PI5 = [
    (C2.KR, "2-parihanikatha.md"), (C2.AN7, "2-parihanikatha.md"), ("đã lìa tham đắm", "2-parihanikatha.md"),
    ("các nền tảng thần thông", "2-parihanikatha.md"),
    (AVJ7, "10-dutiyavaggo.md"), (VIC4, "10-dutiyavaggo.md"), ("‘đây là sự phát sinh của khổ đau’", "10-dutiyavaggo.md"),
    ("‘đây là sự chấm dứt khổ đau’", "10-dutiyavaggo.md"), (SAMAP, "10-dutiyavaggo.md"),
    ("duy trì suốt một kiếp", "10-dutiyavaggo.md"), ("Kinh Phật Tự Thuyết", "10-dutiyavaggo.md"),
    ("có kết quả khổ đau", "10-dutiyavaggo.md"), ("Này các hiền giả", "10-dutiyavaggo.md"),
    ("Bàn về các sức mạnh", "11-tatiyavaggo.md"), ("không có phiền não", "11-tatiyavaggo.md"),
    ("sự có được sự tồn tại cá nhân", "11-tatiyavaggo.md"), ("cõi tái sinh", "11-tatiyavaggo.md"),
    ("đã chấm dứt, đã mất đi, đã an tịnh", "12-catutthavaggo.md"), ("là bậc giác ngộ nhờ sự giác ngộ", "12-catutthavaggo.md"),
    ("nên gọi là “bậc vào dòng”", "12-catutthavaggo.md"), ("được trang bị", "12-catutthavaggo.md"),
    ("chủ ý, bốn tâm, bốn niềm tin, bốn sự tinh tấn, bốn sự tỉnh thức, bốn sự định tâm, bốn trí tuệ",
     "12-catutthavaggo.md"),
    ("và nó là bất thiện", "13-pancamavaggo.md"),
    ("sự ổn định của các hiện tượng", "14-chatthavaggo.md"), ("sự lão hóa và sự chết", "14-chatthavaggo.md"),
    ("đi đến chỗ cùng hiện diện đối mặt nhau", "15-sattamavaggo.md"),
    (f"{Q(RN)} {NHP}", "17-navamavaggo.md"), (PN5, "17-navamavaggo.md"), (ARAHA_C, "17-navamavaggo.md"),
    (f"{KATAMA} {SKP_ANS}", "17-navamavaggo.md"), (CH17_556, "17-navamavaggo.md"),
    (f"Có phải {AN_REST} không có đối tượng không?", "17-navamavaggo.md"), (AVJ_PE, "17-navamavaggo.md"),
    (f"Có phải {KR6} không có đối tượng không?", "17-navamavaggo.md"), ("có tham đắm", "17-navamavaggo.md"),
    (f"Có phải {VS2}, khối thức một phần", "17-navamavaggo.md"),
    ("đã chấm dứt, đã mất đi, đã biến đổi", "5-sabbamatthitikatha.md"), ("chưa sinh ra", "5-sabbamatthitikatha.md"),
    ("không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt vòng luân chuyển, không có sự nhập Niết-bàn trọn "
     "vẹn không còn bám víu không?", "1-puggalakatha.md"),
    ("nên gọi là “người có mắt”", "1-puggalakatha.md"), ("Tóm tắt của chương này –", "9-hevatthikatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    missing += [(st, f) for st, f in PI5 if st not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch19 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
    print(f"wrote {NAME}: {len([ln for ln in text.splitlines() if ln.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
