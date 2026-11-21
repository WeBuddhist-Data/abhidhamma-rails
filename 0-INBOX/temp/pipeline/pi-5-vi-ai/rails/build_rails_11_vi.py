"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 11, Tatiyavaggo (^5-11-0 … ^5-386), kathās (21)-(32)
with the vagga close (Tatiyavaggo., Tassuddānaṃ –, the uddāna).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/11-tatiyavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, NANU_VUTTAM, na_vattabbam,
hanci, hanci_neg, noce, yam, katha, katha_end, vaggo, var, var_sp …). Every string marked (pi-N) is asserted to
occur in that book's approved Vietnamese rails, (chN) in that finished pi-5 rails chapter; S.write runs the
per-line dash / quote / NFC / id checks against the Pāli.
New recurring strings: notes-rails-11.md.

usage: python -I -X utf8 -B build_rails_11_vi.py          (build + checks)
       python -I -X utf8 -B build_rails_11_vi.py --adh    (also write the byte-identical copy to rails/adh-11/)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "11-tatiyavaggo.md"
ADH = S.ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails/adh-11"
Q, q, NANU, PE, YES, NO, NO_PE, cap = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE, S.cap
YES_PE = YES[:-1] + PE                               # Āmantā…pe….
NO_ANS = "Không có."                                 # Natthi. (answer)
RE = S.RE
BH, bh = "Này các tỳ-khưu", "này các tỳ-khưu"        # bhikkhave (sample)
I = S.I


def nanu(x):                                         # …pe… nanu Xti? (lower case)
    return f"chẳng phải {x} sao?"


def low(s):
    return s[:1].lower() + s[1:]


# ---------------------------------------------------------------------------------------------------------------
# Vagga, headings, kathā names
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(3)                                   # Tatiyavaggo (heading and the repeated sub-headings)
VAGGA_END = VAGGA + "."                              # Tatiyavaggo. (coordinator rule: heading wording + «.»)
TASSUDDANAM = "Tóm tắt của chương này –"             # Tassuddānaṃ – (APPROVED §4; = ch9 builder)
K = {                                                # kathā names (heading, closing line)
    "Bala": "sức mạnh",                                              # bala «sức mạnh»
    "Ariyanti": "việc là cao quý",                                   # ariyaṃ «cao quý» + iti («việc», ch5 / ch7)
    "Vimutti": "sự giải thoát",                                      # Vimuttikathā (termbase)
    "Vimuccamana": "cái đang được giải thoát",                       # vimuccamāna (termbase)
    "Atthamaka": "người thứ tám",                                    # aṭṭhamaka (termbase)
    "AtthamakaIndriya": "các năng lực của người thứ tám",            # aṭṭhamakassa indriya
    "Dibbacakkhu": "thiên nhãn",                                     # dibbacakkhu (termbase)
    "Dibbasota": "tai thuộc cõi trời",                               # dibbasota (termbase, APPROVED §6)
    "Yathakamma": "hiểu biết về việc đi theo nghiệp của mình",       # yathākammūpagata (termbase) + ñāṇa
    "Samvara": "sự thu thúc",                                        # saṃvara (APPROVED §1)
    "Asanna": "sự không có tri giác",                                # Asañña- (termbase sañña «có tri giác»)
    "Nevasanna": "lĩnh vực không phải tri giác cũng không phải không tri giác",   # (pi-1)
}


def head(n, k, key, level=5):                        # ##### (n) k. Xkathā
    return f"{'#' * level} ({n}) {k}. {S.katha(K[key])}"


# ---------------------------------------------------------------------------------------------------------------
# (21) Balakathā
# ---------------------------------------------------------------------------------------------------------------
TB = "sức mạnh Như Lai"                              # tathāgatabalaṃ (pi-2, termbase)
SB = "sức mạnh của đệ tử"                            # sāvakabalaṃ (termbase)
SADH = "là chung cho đệ tử"                          # sāvakasādhāraṇaṃ (termbase)
ASADH = "không chung cho đệ tử"                      # sāvakaasādhāraṇaṃ
SAVAKO = "vị đệ tử"                                  # sāvako / sāvakassa (termbase)
TATHAGATO = "Như Lai"                                # tathāgato (pi-2)
PW = {                                               # the ten powers (pi-2 ñāṇavibhaṅga wording)
    "tt": "điều có thể xảy ra và điều không thể xảy ra",                             # ṭhānāṭhānaṃ / ṭhānāṭhāne
    "kamma": ("quả của các nghiệp đã thực hiện trong quá khứ, tương lai và hiện tại, theo hoàn cảnh, "
              "theo nguyên nhân"),        # atītānāgatapaccuppannānaṃ kammasamādānānaṃ ṭhānaso hetuso vipākaṃ
    "sabbattha": "cách thực hành dẫn đến mọi nơi",                                   # sabbatthagāminiṃ paṭipadaṃ
    "loka": "thế gian có nhiều yếu tố, có các yếu tố khác nhau",                     # anekadhātuṃ nānādhātuṃ lokaṃ
    "adhim": "chí hướng khác nhau của chúng sinh",                                   # sattānaṃ nānādhimuttikataṃ
    "indriya": "mức độ cao thấp của các năng lực",                                   # indriyaparopariyattaṃ
    "jhana": ("sự vẩn đục, sự trong sạch, sự xuất khỏi của các tầng thiền, các sự giải thoát, các định tâm "
              "và các thành tựu thiền"),  # jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ
    "pubbe": "sự nhớ lại các đời sống trước",                                        # pubbenivāsānussati(ṃ)
    "cuti": "sự chết và sự tái sinh của chúng sinh",                                 # sattānaṃ cutūpapātaṃ / -te
    "asava": "sự diệt tận các ô nhiễm",                                              # āsavānaṃ khaye (pi-1)
}


def know(x):                                         # X yathābhūtaṃ ñāṇaṃ
    return f"hiểu biết đúng như thật về {x}"


def bala(k):                                         # X yathābhūtaṃ ñāṇaṃ tathāgatabalaṃ
    return f"{know(PW[k])}, {TB}"


def common(k, neg=False):                            # … tathāgatabalaṃ sāvaka(a)sādhāraṇaṃ
    return f"{bala(k)}, {ASADH if neg else SADH}"


TH_B = Q(f"{TB} {SADH}")                             # Tathāgatabalaṃ sāvakasādhāraṇanti?
PUBBA = ("sự rèn luyện trước đây, sự thực hành trước đây, việc giảng giải Giáo Pháp, việc thuyết giảng Giáo Pháp")
#   pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā
EPI = ("bậc chiến thắng, bậc đạo sư, bậc Tự Giác Ngộ Hoàn Toàn, bậc toàn tri, bậc thấy tất cả, "
       "bậc làm chủ Giáo Pháp, chỗ nương tựa về Giáo Pháp")
#   jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo
MAGGA_EPI = ("người làm sinh khởi con đường chưa sinh khởi, người làm sinh thành con đường chưa sinh thành, "
             "người tuyên thuyết con đường chưa được tuyên thuyết, người biết con đường, người hiểu con đường, "
             "người thông thạo con đường")
#   anuppannassa maggassa uppādetā asañjātassa maggassa sañjanetā anakkhātassa maggassa akkhātā maggaññū
#   maggavidū maggakovido
KHINA = f"các ô nhiễm của {TATHAGATO} cũng đã bị diệt tận, các ô nhiễm của {SAVAKO} cũng đã bị diệt tận"
#   tathāgatassāpi āsavā khīṇā sāvakassāpi āsavā khīṇā
DIFF = (f"bất cứ sự khác biệt nào giữa {TATHAGATO} và {SAVAKO}, giữa sự diệt tận các ô nhiễm và sự diệt tận "
        f"các ô nhiễm, giữa sự giải thoát và sự giải thoát")
#   kiñci nānākaraṇaṃ tathāgatassa vā sāvakassa vā āsavakkhayena vā āsavakkhayaṃ vimuttiyā vā vimutti
NOTE27 = f"[ở đây, đây là sự phủ nhận nhắm vào phương diện chung ({S.TIKA})]"
#   [ayamettha sādhāraṇapakkhaṃ sandhāya paṭikkhepo (ṭīkā oloketabbā)]

# ---------------------------------------------------------------------------------------------------------------
# (22) Ariyantikathā
# ---------------------------------------------------------------------------------------------------------------
ARIYA = "cao quý"                                    # ariyaṃ / ariyā (termbase)
SUNNA = "có đối tượng là sự trống rỗng"              # suññatārammaṇaṃ / -ā
ANIM = "có đối tượng là cái không có dấu hiệu"       # animittārammaṇaṃ / -ā
APPA = "có đối tượng là cái không mong cầu"          # appaṇihitārammaṇaṃ / -ā
SUNNATA, APPANIHITA = "sự trống rỗng", "cái không mong cầu"   # suññataṃ / appaṇihitaṃ (manasi karoti)
THREE_OBJ = f"{SUNNA}{PE} {ANIM}{PE} {APPA}"         # suññatārammaṇaṃ…pe… animittārammaṇaṃ…pe… appaṇihitārammaṇaṃ
MCA = ("con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng, con đường trở lại một lần, "
       "thành quả trở lại một lần, con đường không trở lại, thành quả không trở lại, con đường A-la-hán, "
       "thành quả A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, năng lực, sức mạnh, "
       "chi phần giác ngộ")
#   maggo phalaṃ nibbānaṃ, sotāpattimaggo … arahattaphalaṃ, satipaṭṭhānaṃ sammappadhānaṃ iddhipādo indriyaṃ balaṃ
#   bojjhaṅgo
MCA_SHORT = f"con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng{PE} chi phần giác ngộ"
SP_PL = "các sự thiết lập tỉnh thức"                 # satipaṭṭhānā (ch8)
OTHERS = ["các nỗ lực đúng đắn", "các nền tảng thần thông", "các năng lực", "các sức mạnh", "các chi phần giác ngộ"]
#   sammappadhānā, iddhipādā, indriyā, balā, bojjhaṅgā (ch2, ch8)
BOJJH = OTHERS[-1]
SAMMAPPADHANA = "nỗ lực đúng đắn"                    # sammappadhānaṃ (singular, as written)
DVINNAM = "có sự tụ hợp của hai sự tiếp xúc, hai tâm"   # dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ hoti (ch4 frame)


def manasi(x, y):                                    # Xñca manasi karoti, Yñca manasi karoti
    return f"vừa chú tâm đến {x}, vừa chú tâm đến {y}"


def ar(k, *obj):                                     # X … tathāgatabalaṃ ariyaṃ (Y-ārammaṇaṃ)
    return ", ".join([bala(k), f"là {ARIYA}"] + list(obj))


def ar_pl(subj, *obj):                               # satipaṭṭhānā ariyā (Y-ārammaṇā)
    return ", ".join([f"{subj} là {ARIYA}"] + list(obj))


def nv(subj, x):                                     # X (ariyaṃ) na vattabbaṃ – "Y"nti?
    return f"Có phải đối với {subj}, không nên nói – “{x}” không?"


def bala_ar(k):                                      # … tathāgatabalaṃ ariyaṃ (attributive, before na vattabbaṃ)
    return f"{bala(k)} {ARIYA}"


# ---------------------------------------------------------------------------------------------------------------
# (23) Vimuttikathā, (24) Vimuccamānakathā
# ---------------------------------------------------------------------------------------------------------------
def free(desc):                                      # X cittaṃ vimuccati
    return f"tâm {desc} được giải thoát"


def ubho(x):                                         # X ca cittañca ubho vimuccanti
    return f"cả {x} và tâm đều được giải thoát"


def saha(r):                                         # rāgasahagataṃ … rāgānuparivatti (pi-1 / pi-3 pattern)
    return (f"có {r} đi kèm, cùng sinh với {r}, hòa lẫn với {r}, gắn liền với {r}, cùng tồn tại với {r}, "
            f"vận hành theo {r}")


QUALS = ["là đối tượng của ô nhiễm", "là đối tượng của xiềng xích", "là đối tượng của nút thắt",
         "là đối tượng của dòng lũ", "là đối tượng của ách", "là đối tượng của chướng ngại",
         "bị sự hiểu sai lệch nắm giữ", "là đối tượng của sự bám víu", "là đối tượng của phiền não"]   # (pi-1)
#   sāsavaṃ saṃyojaniyaṃ ganthaniyaṃ oghaniyaṃ yoganiyaṃ nīvaraṇiyaṃ parāmaṭṭhaṃ upādāniyaṃ saṃkilesiyaṃ
AKU = "bất thiện, thuộc thế gian"                    # akusalaṃ lokiyaṃ (pi-1)
AKU_FULL = f"{AKU}, " + ", ".join(QUALS)
AKU_SHORT = f"{AKU}, {QUALS[0]}{PE} {QUALS[-1]}"     # … sāsavaṃ…pe… saṃkilesiyaṃ
KIL = {"raga": ("tham đắm", "sự tham đắm", "có tham đắm"),        # rāga- / rāgo / sarāgaṃ (termbase)
       "dosa": ("sân hận", "sự sân hận", "có sân hận"),
       "moha": ("si mê", "sự si mê", "có si mê")}
PHASSA = "sự tiếp xúc"                               # phasso / saphassaṃ
VITA = "đã lìa tham đắm, đã lìa sân hận, đã lìa si mê"   # vītarāga- vītadosa- vītamoha- (termbase; ch2)
VTH = "cái đã được giải thoát là cái đang được giải thoát"   # vimuttaṃ vimuccamānaṃ
EKA = "một phần đã được giải thoát, một phần chưa được giải thoát"   # ekadesaṃ vimuttaṃ, ekadesaṃ avimuttaṃ

# ch3 Odhiso strings (^5-274 … ^5-277), asserted in 3-brahmacariyakatha.md
ATTAINED = ("đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an trú, chạm đến bằng thân rồi "
            "an trú, một phần không chạm đến bằng thân rồi an trú")
#   paṭiladdho adhigato sacchikato upasampajja viharati, kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā viharati
ATTAINED_POS = "đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an trú, chạm đến bằng thân rồi an trú"
SOTA_TAIL = ("một phần là người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác, người có một "
             f"hạt giống, được trang bị niềm tin trong sáng không lay chuyển nơi Đức Phật, nơi Giáo Pháp{PE} "
             f"nơi Tăng đoàn{PE} được trang bị giới hạnh được các bậc thánh yêu quý, một phần không có giới hạnh "
             "được các bậc thánh yêu quý")
ANAG_TAIL = ("một phần là người nhập Niết-bàn trọn vẹn trong khoảng giữa, người nhập Niết-bàn trọn vẹn khi gần mạng "
             "chung, người nhập Niết-bàn trọn vẹn không có sự thúc đẩy, người nhập Niết-bàn trọn vẹn có sự thúc đẩy, "
             "người theo dòng đi lên đến cõi Sắc Cứu Cánh, một phần không phải là người theo dòng đi lên đến cõi "
             "Sắc Cứu Cánh")
SC_YES = "một phần điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm"
SC_NO = "một phần điều cần được tự mình chứng nghiệm chưa được tự mình chứng nghiệm"
PN = S.PN


def status(x, fruit):                                # Ekadesaṃ X, ekadesaṃ na X, ekadesaṃ X-phalappatto … (ch3)
    return f"một phần là {x}, một phần không phải là {x}, một phần đã đạt đến {fruit}, {ATTAINED}"


SUTTA_KAMA = ("Khi vị ấy biết như vậy, thấy như vậy, tâm được giải thoát khỏi ô nhiễm dục lạc, tâm được giải thoát "
              "khỏi ô nhiễm hiện hữu, tâm được giải thoát khỏi ô nhiễm vô minh")                     # (pi-4)
#   tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, bhavāsavāpi …, avijjāsavāpi cittaṃ vimuccati
SUTTA_SAMAHITE = ("Khi tâm đã an định như vậy, trong sạch, trong sáng, không còn vết nhơ, đã lìa những thứ làm vẩn "
                  "đục, đã trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm đến sự hiểu "
                  "biết về sự diệt tận các ô nhiễm")                                                 # (pi-4)
#   so evaṃ samāhite citte … āneñjappatte āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti
CIT_DN = "Trường Bộ Kinh"                            # dī. ni. (pi-2)
VIM_C = "có tâm đang được giải thoát"                # atthi cittaṃ vimuccamānaṃ
RAJJ = "có tâm đang tham đắm, đang sân hận, đang si mê, đang bị phiền não làm ô nhiễm"
#   atthi cittaṃ rajjamānaṃ dussamānaṃ muyhamānaṃ kilissamānaṃ (termbase)
BOTH = ("vừa đã tham đắm vừa không tham đắm, vừa đã sân hận vừa không sân hận, vừa đã si mê vừa không si mê, "
        "vừa đã được cắt vừa không được cắt, vừa đã bị phá vỡ vừa không bị phá vỡ, vừa đã được làm vừa không "
        "được làm")
#   rattañceva arattañca, duṭṭhañceva aduṭṭhañca, mūḷhañceva amūḷhañca, chinnañceva achinnañca,
#   bhinnañceva abhinnañca, katañceva akatañca

# ---------------------------------------------------------------------------------------------------------------
# (25) Aṭṭhamakakathā, (26) Aṭṭhamakassa indriyakathā
# ---------------------------------------------------------------------------------------------------------------
A8 = "người thứ tám"                                 # aṭṭhamako puggalo / aṭṭhamakassa puggalassa (termbase)
GOTRA = "người chuyển đổi dòng dõi"                  # gotrabhuno puggalassa (pi-4)
DP = "sự ám ảnh của quan điểm"                       # diṭṭhipariyuṭṭhānaṃ (termbase)
VP = "sự ám ảnh của hoài nghi"                       # vicikicchāpariyuṭṭhānaṃ (termbase)
DA = "khuynh hướng tiềm ẩn quan điểm"                # diṭṭhānusayo (termbase)
VA = "khuynh hướng tiềm ẩn hoài nghi"                # vicikicchānusayo (termbase)
SBP = "sự hiểu sai lệch về giới hạnh và nghi thức"   # sīlabbataparāmāso (pi-1)
PAH, APAH = "đã được dứt bỏ", "chưa được dứt bỏ"      # pahīna- / appahīna-
VA_SBP = f"{VA}{PE} {SBP}"                           # vicikicchānusayo… sīlabbataparāmāso
DA_SBP = f"{DA}{PE} {SBP}"


def a8(x, who=A8):                                   # Aṭṭhamakassa puggalassa X pahīnaṃ (ch3 «đối với …»)
    return f"đối với {who}, {x}"


def bh8(x, what, neg=False):                         # aṭṭhamakassa puggalassa X-pahānāya Y bhāvito (ch2 frame)
    return f"{A8}, để dứt bỏ {x}, {'chưa' if neg else 'đã'} tu tập {what}"


AMAGGA = f"đã được dứt bỏ bằng đường sai, thuộc thế gian, {QUALS[0]}{PE} {QUALS[-1]}"
#   amaggena pahīnaṃ lokiyena sāsavena…pe… saṃkilesiyena (amagga «đường sai»: termbase)
WILL_NOT = "sẽ không sinh khởi"                      # nuppajjissati


def kv(x, who=A8):                                   # X nuppajjissatīti katvā pahīnaṃ (ch7 frame «vì cho rằng … nên …»)
    return f"Có phải vì cho rằng đối với {who}, {x} {WILL_NOT}, nên nó {PAH} không?"


I_SAD, I_VIR, I_SAT, I_SAM, I_PAN = (I[k] for k in ("saddhindriya", "vīriyindriya", "satindriya", "samādhindriya",
                                                     "paññindriya"))
I_MAN, I_SOM, I_JIV = I["manindriya"], I["somanassindriya"], I["jīvitindriya"]
SADDHA, VIRIYA, SATI, SAMADHI, PANNA = "niềm tin", "sự tinh tấn", "sự tỉnh thức", "định tâm", "trí tuệ"
MANO, SOM, JIV = "ý", "niềm vui", "sự sống"          # mano / somanassaṃ / jīvitaṃ (termbase)
NIY = "dẫn đến giải thoát"                           # niyyāniko / -ā / -aṃ (pi-2)
P_SOTA = "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng"                    # (pi-4)
P_SAKA = "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần"             # (pi-4)
P_ANAG = "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"               # (pi-4)
P_ARA = "người đang thực hành để tự mình chứng nghiệm trạng thái A-la-hán"                    # (ch3)
FIVE_I = "năm năng lực"                              # pañcindriyāni (pi-2)
BAHIRO = "người ở bên ngoài, đứng vững ở phía người phàm phu"   # bāhiro puthujjanapakkhe ṭhito (termbase; ch4)
MUDU = [P_ARA, PN["anāgāmī"], P_ANAG, PN["sakadāgāmī"], P_SAKA, PN["sotāpanno"], P_SOTA]
SUTTA5 = (f"{BH}, có {FIVE_I} này! Năm năng lực nào? {cap(I_SAD)}, {I_VIR}, {I_SAT}, {I_SAM}, {I_PAN} – {bh}, "
          f"đây là {FIVE_I}. {BH}, do {FIVE_I} này được trọn vẹn, được viên mãn, mà trở thành {PN['arahā']}. "
          + cap(", ".join(f"ở mức yếu hơn thế thì trở thành {x}" for x in MUDU)) + ". "
          f"{BH}, người nào không có {FIVE_I} này theo mọi cách, bằng mọi phương diện, Ta nói rằng người ấy là "
          f"‘{BAHIRO}’")
#   pañcimāni, bhikkhave, indriyāni! … tamahaṃ ‘bāhiro puthujjanapakkhe ṭhito’ti vadāmī


def has(who, *items):                                # X-assa puggalassa atthi / natthi …
    return f"{who} " + ", ".join(items)


# ---------------------------------------------------------------------------------------------------------------
# (27) Dibbacakkhukathā, (28) Dibbasotakathā
# ---------------------------------------------------------------------------------------------------------------
MC, DC, PC = "mắt thịt", "thiên nhãn", "mắt trí tuệ"   # maṃsacakkhu / dibbacakkhu / paññācakkhu (termbase)
MS, DS = "tai thịt", "tai thuộc cõi trời"            # maṃsasota / dibbasota (termbase)
DH = "được hiện tượng hỗ trợ"                        # dhammupatthaddhaṃ (dhamma «hiện tượng», upatthaddha «được … hỗ trợ»)
SCOPE = "phạm vi, uy lực, vùng hoạt động"            # visayo ānubhāvo gocaro


def becomes(a, b):                                   # A dhammupatthaddhaṃ B hoti
    return f"{a}, {DH}, trở thành {b}"


UPA = "là do nghiệp tạo ra rồi trở thành không do nghiệp tạo ra"          # upādiṇṇaṃ hutvā anupādiṇṇaṃ hoti (pi-1)
KAMA = "là thuộc cõi dục lạc rồi trở thành thuộc cõi hình sắc"            # kāmāvacaraṃ hutvā rūpāvacaraṃ hoti
RUPA_T = "là thuộc cõi hình sắc rồi trở thành thuộc cõi không hình sắc"   # rūpāvacaraṃ hutvā arūpāvacaraṃ hoti
PARI = "là nằm trong các cõi tồn tại rồi trở thành không nằm trong các cõi tồn tại"   # pariyāpannaṃ … (pi-1)
TWO = "chỉ có hai loại mắt"                          # dveva cakkhūni
THREE = f"ba loại mắt – {MC}, {DC}, {PC}"            # tīṇi cakkhūni vuttāni bhagavatā – …
ONE = "chỉ có một loại tai"                          # ekaṃyeva / ekaññeva sotaṃ
CIT_ITI = S.CIT["itivu."]
VERSE_EYE = [
    f"“{cap(MC)}, {DC}, {PC} không có điều gì cao hơn;",
    "Ba loại mắt này, bậc tối thượng giữa con người đã giảng.",
    f"“Sự sinh khởi của {MC} là con đường của {DC};",
    f"Và khi hiểu biết sinh khởi, {PC} không có điều gì cao hơn;",
    f"Do có được con mắt ấy, được giải thoát khỏi mọi khổ đau” [{CIT_ITI} 61, trong {CIT_ITI}].",
]

# ---------------------------------------------------------------------------------------------------------------
# (29) Yathākammūpagatañāṇakathā
# ---------------------------------------------------------------------------------------------------------------
YK = "việc đi theo nghiệp của mình"                  # yathākammūpagataṃ (termbase)
YKN = f"hiểu biết về {YK}"                           # yathākammūpagataṃ ñāṇaṃ
TH_Y_BODY = f"{YKN} là {DC}"                         # yathākammūpagataṃ ñāṇaṃ dibbacakkhu
SEE = f"vừa thấy hình sắc bằng {DC}"                 # dibbena cakkhunā rūpaṃ passati
ITEMS = ["Quả thật, những chúng sinh đáng kính này",                       # (pi-4 ^4-184)
         "mang hành vi xấu bằng thân", "mang hành vi xấu bằng lời nói", "mang hành vi xấu bằng ý",
         "phỉ báng các bậc thánh", "có quan điểm sai lầm", "thực hiện nghiệp theo quan điểm sai lầm",
         "khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục",
         "hoặc những chúng sinh đáng kính này",
         "mang hành vi tốt bằng thân", "mang hành vi tốt bằng lời nói", "mang hành vi tốt bằng ý",
         "không phỉ báng các bậc thánh", "có quan điểm đúng đắn", "thực hiện nghiệp theo quan điểm đúng đắn",
         "khi thân tan rã, sau khi chết, họ đã tái sinh vào cõi tốt lành, thế giới cõi trời"]
NOT_DC = f"có ai đó không có {DC}, chưa có được, chưa chứng đắc, chưa tự mình chứng nghiệm {DC}, mà biết {YK}"
#   atthi koci adibbacakkhuko dibbacakkhuṃ appaṭiladdho anadhigato asacchikato yathākammūpagataṃ jānāti
SARI = "tôn giả Xá-lợi-phất"                         # āyasmā sāriputto (termbase)
CIT_THERA = "Trưởng Lão Tăng Kệ"                     # theragā. / theragāthāyaṃ (not in termbase / CIT)
VERSE_SARI = [
    f"“Không hướng đến các đời sống trước, cũng không hướng đến {DC};",
    "Đến sự bao quát tâm, đến thần thông, đến sự thanh tịnh của yếu tố tai;",
    f"Đến sự chết, đến sự tái sinh, tôi không có sự mong cầu” [{CIT_THERA} 996, trong {CIT_THERA}].",
]

# ---------------------------------------------------------------------------------------------------------------
# (30) Saṃvarakathā
# ---------------------------------------------------------------------------------------------------------------
DEV, MAN = "giữa chư thiên", "giữa loài người"       # devesu / manussesu (ch3)
SV, ASV = "sự thu thúc", "sự không thu thúc"         # saṃvaro / asaṃvaro (APPROVED §1)
PV = "sự kiềm chế việc sát hại sinh mạng"            # pāṇātipātā veramaṇī (pi-2)
PA = "việc sát hại sinh mạng"                        # pāṇātipāto (pi-2)
SV2 = "sự kiềm chế việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # (pi-2)
SU = "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # surāmerayamajjapamādaṭṭhānaṃ (pi-2)
KP4 = "sát hại sinh mạng, lấy của không được cho, có hành vi sai trái trong các dục lạc, nói dối"   # (pi-4)
#   pāṇātipātino adinnādāyino kāmesumicchācārino musāvādino
SURA_DRINK = "dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # surāmerayamajjapamādaṭṭhāyino
P_SV = f"{SV} khỏi {ASV} là giới hạnh, {DEV} có {SV}"       # asaṃvarā saṃvaro sīlaṃ, atthi devesu saṃvaro
Q_SV = f"{DEV} có {ASV}, mà {SV} khỏi {ASV} ấy là giới hạnh"   # atthi devesu asaṃvaro, yamhā asaṃvarā saṃvaro sīlaṃ

# ---------------------------------------------------------------------------------------------------------------
# (31) Asaññakathā, (32) Nevasaññānāsaññāyatanakathā
# ---------------------------------------------------------------------------------------------------------------
AS = "giữa các chúng sinh Vô Tưởng"                  # asaññasattesu (termbase sañña «Tưởng» in asaññasatta)
TH_A = f"{AS} có tri giác"                           # asaññasattesu saññā atthi
MN = f"{MAN} có tri giác"                            # manussesu saññā atthi


def blist(q, items=6):                               # (a)saññābhavo (a)saññāgati … (a)saññattabhāvapaṭilābho
    base = ["sự hiện hữu", "cõi tái sinh", "nơi cư trú của chúng sinh", "vòng luân hồi", "cách sinh",
            "sự có được sự tồn tại cá nhân"]
    return ", ".join(f"{b} {q}" if k < items else b for k, b in enumerate(base))


LIST_S = blist("có tri giác")                        # saññābhavo … saññattabhāvapaṭilābho
LIST_A = blist("không có tri giác")                  # asaññabhavo … asaññattabhāvapaṭilābho
LIST_S2 = blist("có tri giác", 2)                    # saññābhavo saññāgati sattāvāso saṃsāro yoni attabhāvapaṭilābho
MOT, BON, NAM = "một", "bốn", "năm"                  # eka- / catu- / pañca-vokāra


def vok(n):                                          # N-vokārabhavo gati sattāvāso saṃsāro yoni attabhāvapaṭilābho
    return (f"sự hiện hữu gồm {n} khối, cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh, "
            f"sự có được sự tồn tại cá nhân")


def vok_pe(n):                                       # N-vokārabhavo gati…pe… attabhāvapaṭilābho
    return f"sự hiện hữu gồm {n} khối, cõi tái sinh{PE} sự có được sự tồn tại cá nhân"


LIST_S_PE = f"sự hiện hữu có tri giác, cõi tái sinh có tri giác{PE} sự có được sự tồn tại cá nhân có tri giác"
LIST_A_PE = f"sự hiện hữu không có tri giác, cõi tái sinh không có tri giác{PE} sự có được sự tồn tại cá nhân không có tri giác"
KAR = "bằng tri giác ấy mà làm việc của tri giác"    # tāya saññāya saññākaraṇīyaṃ karoti (ch5 frame)
KAR_NO = "nhưng bằng tri giác ấy mà không làm việc của tri giác"   # na ca tāya saññāya … karoti
SUTTA_AS = f"{BH}, có chư thiên tên là chúng sinh Vô Tưởng; và do sự sinh khởi của tri giác, chư thiên ấy chết đi khỏi thân ấy"
#   santi, bhikkhave, asaññasattā nāma devā; saññuppādā ca pana te devā tamhā kāyā cavanti
NS = K["Nevasanna"]                                  # nevasaññānāsaññāyatana (pi-1)
AKA = "lĩnh vực không gian vô tận"                   # ākāsānañcāyatana (pi-1)
VIN = "lĩnh vực thức vô tận"                         # viññāṇañcāyatana (pi-1)
AKI = "lĩnh vực không có gì cả"                      # ākiñcaññāyatana (pi-1)
TH_N = f"ở {NS}, không nên nói – «có tri giác»"      # nevasaññānāsaññāyatane na vattabbaṃ – "saññā atthī"ti
TH_NN = f"ở {NS}, không nên nói – «có tri giác» hay «không có»"   # … – "saññā atthī"ti vā "natthī"ti vā


def nvp(place):                                      # X-e na vattabbaṃ – "saññā atthi" (first level)
    return f"{place}, không nên nói – “có tri giác”"


def c4(place):                                       # X catuvokārabhavo
    return f"{place} là sự hiện hữu gồm bốn khối"


UDDANA = [
    "Sức mạnh là chung, là cao quý, tâm có tham đắm được giải thoát;",
    "Cái đã được giải thoát là cái đang được giải thoát, có tâm đang được giải thoát.",
    f"Đối với {A8}, {DP} {PAH};",
    f"Đối với {A8}, không có {FIVE_I}, mắt.",
    f"Tai {DH}, {YKN};",
    f"{SV.capitalize()} {DEV}, tri giác {AS}, cũng vậy, đỉnh cao của sự hiện hữu.",
]

# ---------------------------------------------------------------------------------------------------------------
# Strings reused from finished rails (asserted)
# ---------------------------------------------------------------------------------------------------------------
REUSED11 = [  # (Pāli, Vietnamese, source)
    ("tathāgatabalaṃ", TB, "2"),
    ("ṭhānaṃ / aṭṭhānaṃ (ṭhānañca ṭhānato …)", "điều có thể xảy ra", "2"),
    ("aṭṭhānaṃ", "điều không thể xảy ra", "2"),
] + [(f"power {k}", PW[k], "2") for k in ("kamma", "sabbattha", "loka", "adhim", "indriya", "jhana", "pubbe",
                                          "cuti")] + [
    ("āsavānaṃ khaye ñāṇaṃ", "hiểu biết về sự diệt tận các ô nhiễm", "1"),
    ("yathābhūtaṃ ñāṇaṃ", "hiểu biết đúng như thật", "2"),
    ("tathāgato", TATHAGATO, "2"),
    ("sammāsambuddho", "bậc Tự Giác Ngộ Hoàn Toàn", "1"),
    ("arahattaphalaṃ / arahattamaggo", "thành quả A-la-hán", "2"),
    ("akusalaṃ lokiyaṃ (sabbaṃ rūpaṃ … lokiyaṃ)", "thuộc thế gian", "1"),
] + [(f"qualifier {k}", v, "1") for k, v in enumerate(QUALS)] + [
    ("cittasahabhuno", "cùng tồn tại với tâm", "1"),
    ("cittānuparivatti", "vận hành theo tâm", "3"),
    ("kāmāsavāpi cittaṃ vimuccati …", SUTTA_KAMA, "4"),
    ("so evaṃ samāhite citte … āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti", SUTTA_SAMAHITE, "4"),
    ("gotrabhū", GOTRA, "4"),
    ("sīlabbataparāmāso", SBP, "1"),
    ("assaddho", "là người không có niềm tin", "2"),
    ("kusīto", "lười biếng", "2"),
    ("muṭṭhassati", "mất tỉnh thức", "2"),
    ("asamāhito", "không được định tâm", "2"),
    ("duppañño", "kém trí tuệ", "2"),
    ("pañcindriyāni", FIVE_I, "2"),
    ("sotāpattiphalasacchikiriyāya paṭipanno", P_SOTA, "4"),
    ("sakadāgāmiphalasacchikiriyāya paṭipanno", P_SAKA, "4"),
    ("anāgāmiphalasacchikiriyāya paṭipanno", P_ANAG, "4"),
    ("upādinna", "do nghiệp tạo ra", "1"),
    ("anupādinna", "không do nghiệp tạo ra", "1"),
    ("kāmāvacara", "thuộc cõi dục lạc", "1"),
    ("rūpāvacara", "thuộc cõi hình sắc", "1"),
    ("arūpāvacara", "thuộc cõi không hình sắc", "1"),
    ("pariyāpannā", "nằm trong các cõi tồn tại", "1"),
    ("apariyāpannā", "không nằm trong các cõi tồn tại", "1"),
] + [(f"dibbacakkhu sutta item {k}", v, "4") for k, v in enumerate(ITEMS)] + [
    ("pāṇātipātā veramaṇī", PV, "2"),
    ("surāmerayamajjapamādaṭṭhānā veramaṇī", SV2, "2"),
    ("pāṇātipātino … musāvādino", KP4, "4"),
    ("nevasaññānāsaññāyatana", NS, "1"),
    ("ākāsānañcāyatana", AKA, "1"),
    ("viññāṇañcāyatana", VIN, "1"),
    ("ākiñcaññāyatana", AKI, "1"),
    ("ekavokārabhavo", "sự hiện hữu gồm một khối", "2"),
    ("catuvokārabhavo", "sự hiện hữu gồm bốn khối", "2"),
    ("pañcavokārabhavo", "sự hiện hữu gồm năm khối", "2"),
    ("adukkhamasukhā vedanā", "cảm giác không khó chịu cũng không dễ chịu", "2"),
    ("dī. ni. (citation)", CIT_DN, "2"),
    # finished pi-5 rails chapters
    ("paṭiladdho … ekadesaṃ na kāyena phusitvā viharati", ATTAINED, "ch3"),
    ("ekadesaṃ sattakkhattuparamo … na samannāgato", SOTA_TAIL, "ch3"),
    ("ekadesaṃ antarāparinibbāyī … na uddhaṃsotoakaniṭṭhagāmī", ANAG_TAIL, "ch3"),
    ("ekadesaṃ sacchikātabbaṃ sacchikataṃ", SC_YES, "ch3"),
    ("ekadesaṃ sacchikātabbaṃ na sacchikataṃ", SC_NO, "ch3"),
    ("devesu", DEV, "ch3"),
    ("manussesu", MAN, "ch3"),
    ("arahato X-ppahānāya Y bhāvito", ", để dứt bỏ sự tham đắm, đã tu tập con đường", "ch2"),
    ("bojjhaṅgā bhāvitā", "đã tu tập các chi phần giác ngộ", "ch2"),
    ("satipaṭṭhānā", SP_PL, "ch8"),
    ("Xti katvā Yti?", "Có phải vì cho rằng", "ch7"),
    ("Nanu āyasmā X etadavoca –", "Chẳng phải tôn giả", "ch5"),
]
CH = {"ch2": "2-parihanikatha.md", "ch3": "3-brahmacariyakatha.md", "ch5": "5-sabbamatthitikatha.md",
      "ch7": "7-ekaccam-atthitikatha.md", "ch8": "8-satipatthanakatha.md"}


def check_reused11():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                          for p in sorted(d.glob("*.md")))).lower()
    for k, f in CH.items():
        texts[k] = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8")).lower()
    bad = [(p, v, b) for p, v, b in REUSED11 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def vagga_head(i):
        add(i, f"#### {VAGGA}")

    # ---- (21) Balakathā ---------------------------------------------------------------------------------------
    add("5-11-0", f"### {VAGGA}")
    add("5-11-1-0", head(21, 1, "Bala", level=4))
    add("5-354",
        f"{TH_B} {YES} {Q(f'{TB} là {SB}, {SB} là {TB}')} {NO_PE}",
        f"{TH_B} {YES} {Q(f'chính {TB} ấy là {SB} ấy, chính {SB} ấy là {TB} ấy')} {NO_PE}",
        f"{TH_B} {YES} {Q(f'{TB} như thế nào, thì {SB} cũng như thế ấy, {SB} như thế nào, thì {TB} cũng như thế ấy')} "
        f"{NO_PE}",
        f"{TH_B} {YES} {Q(f'{PUBBA} của {TATHAGATO} như thế nào, thì {PUBBA} của {SAVAKO} cũng như thế ấy')} {NO_PE}",
        f"{TH_B} {YES} {Q(f'{TATHAGATO} là {EPI}')} {YES} {Q(f'{SAVAKO} là {EPI}')} {NO_PE}",
        f"{TH_B} {YES} {Q(f'{TATHAGATO} là {MAGGA_EPI}')} {YES} {Q(f'{SAVAKO} là {MAGGA_EPI}')} {NO_PE}",
        f"{Q(common('indriya'))} {YES} {Q(f'{SAVAKO} là bậc toàn tri, bậc thấy tất cả')} {NO_PE}")

    def knows(k):
        p = f"{SAVAKO} biết {PW[k]}"
        return f"{Q(p)} {YES} {S.hanci(p, common(k))}"

    add("5-355", *[knows(k) for k in ("tt", "kamma", "sabbattha", "loka", "adhim", "jhana", "pubbe", "cuti")],
        f"{NANU(KHINA)} {YES} {Q(f'có {DIFF}')} {NO_ANS} {S.hanci(f'không có {DIFF}', common('asava'))}")

    def pair(a, b, neg=False):
        return f"{Q(common(a, neg))} {YES} {Q(common(b, neg))} {NO_PE}"

    add("5-356", pair("asava", "tt"), pair("asava", "cuti"), pair("tt", "asava", True), pair("cuti", "asava", True),
        f"{Q(common('indriya', True))} {YES} {Q(common('tt', True))} {NO[:-1]} {NOTE27}{PE}",
        f"{Q(common('indriya', True))} {YES_PE} {Q(common('asava', True))} {NO_PE}",
        pair("tt", "indriya"), pair("asava", "indriya"), S.katha_end(K["Bala"]))

    # ---- (22) Ariyantikathā ------------------------------------------------------------------------------------
    vagga_head("5-11-2-0")
    add("5-11-2-1-0", head(22, 2, "Ariyanti"))
    TT, CUTI = PW["tt"], PW["cuti"]
    add("5-357",
        f"{Q(ar('tt'))} {YES} {Q(f'đó là {MCA}')} {NO_PE}",
        f"{Q(ar('tt'))} {YES} {Q(SUNNA)} {NO_PE} {Q(SUNNA)} {YES} {Q(manasi(TT, SUNNATA))} {NO_PE}",
        f"{Q(manasi(TT, SUNNATA))} {YES} {Q(DVINNAM)} {NO_PE} {q(ar('tt'))} {YES} {Q(f'{ANIM}{PE} {APPA}')} "
        f"{NO_PE} {q(APPA)} {YES} {Q(manasi(TT, APPANIHITA))} {NO_PE}",
        f"{Q(manasi(TT, APPANIHITA))} {YES} {Q(DVINNAM)} {NO_PE}")
    add("5-358",
        f"{Q(ar_pl(SP_PL, SUNNA))} {YES} {Q(ar('tt', SUNNA))} {NO_PE}",
        f"{Q(ar_pl(SP_PL, f'{ANIM}{PE} {APPA}'))} {YES} {Q(ar('tt', APPA))} {NO_PE}",
        f"{Q(ar_pl(', '.join(OTHERS), SUNNA))} {YES} {Q(ar('tt', SUNNA))} {NO_PE}",
        f"{Q(ar_pl(BOJJH, f'{ANIM}{PE} {APPA}'))} {YES} {Q(ar('tt', APPA))} {NO_PE}")
    SPA = f"{SP_PL} {ARIYA}"
    add("5-359",
        f"{nv(bala_ar('tt'), SUNNA)} {YES} {nv(SPA, SUNNA)} {NO_PE}",
        f"{nv(bala_ar('tt'), f'{ANIM}{PE} {APPA}')} {YES} {nv(SPA, APPA)} {NO_PE}",
        f"{nv(bala_ar('tt'), THREE_OBJ)} {YES} {nv(f'{SAMMAPPADHANA}{PE} {BOJJH} {ARIYA}', APPA)} {NO_PE}")
    add("5-360",
        f"{Q(ar('cuti'))} {YES} {Q(f'đó là {MCA_SHORT}')} {NO_PE}",
        f"{Q(ar('cuti'))} {YES} {Q(SUNNA)} {NO_PE} {q(SUNNA)} {YES} {Q(manasi(CUTI, SUNNATA))} {NO_PE}",
        f"{Q(manasi(CUTI, SUNNATA))} {YES} {Q(DVINNAM)} {NO_PE}",
        f"{Q(ar('cuti'))} {YES} {Q(f'{ANIM}, {APPA}')} {NO_PE} {q(APPA)} {YES} {Q(manasi(CUTI, APPANIHITA))} {NO_PE}",
        f"{Q(manasi(CUTI, APPANIHITA))} {YES} {Q(DVINNAM)} {NO_PE}")
    add("5-361",
        f"{Q(ar_pl(SP_PL, THREE_OBJ))} {YES} {Q(ar('cuti', APPA))} {NO_PE}",
        f"{Q(ar_pl(f'{SAMMAPPADHANA}{PE} {BOJJH}', THREE_OBJ))} {YES} {Q(ar('cuti', APPA))} {NO_PE}",
        f"{nv(bala_ar('cuti'), THREE_OBJ)} {YES} {nv(SPA, APPA)} {NO_PE}")
    add("5-362",
        f"{nv(bala_ar('cuti'), THREE_OBJ)} {YES} {nv(f'{OTHERS[0]}{PE} {BOJJH} {ARIYA}', APPA)} {NO_PE}",
        f"{Q(ar('asava'))} {YES} {Q(ar('tt'))} {NO_PE}",
        f"{Q(ar('asava'))} {YES} {Q(ar('cuti'))} {NO_PE}",
        f"{nv(bala('tt'), ARIYA)} {YES} {nv(bala('asava'), ARIYA)} {NO_PE}",
        f"{nv(bala('cuti'), ARIYA)} {YES} {nv(bala('asava'), ARIYA)} {NO_PE}",
        f"{Q(ar('asava', SUNNA))} {YES} {Q(ar('tt', SUNNA))} {NO_PE}",
        f"{Q(ar('asava', f'{ANIM}{PE} {APPA}'))} {YES} {Q(ar('tt', APPA))} {NO_PE}",
        f"{Q(ar('asava', THREE_OBJ))} {YES_PE} {Q(ar('cuti', APPA))} {NO_PE}",
        f"{nv(bala_ar('tt'), SUNNA)} {YES} {nv(bala_ar('asava'), SUNNA)} {NO_PE}",
        f"{nv(bala_ar('tt'), f'{ANIM}{PE} {APPA}')} {YES} {nv(bala_ar('asava'), APPA)} {NO_PE}",
        f"{nv(bala_ar('cuti'), THREE_OBJ)} {YES} {nv(bala_ar('asava'), APPA)} {NO_PE}",
        S.katha_end(K["Ariyanti"]))

    # ---- (23) Vimuttikathā -------------------------------------------------------------------------------------
    vagga_head("5-11-3-0")
    add("5-11-3-1-0", head(23, 3, "Vimutti"))

    def vim_block(key, first_short, variant=False, l4_alt=False):
        r, rn, sa = KIL[key]
        l1 = f"{Q(free(sa))} {YES} {Q(free(f'{saha(r)}, {AKU_SHORT if first_short else AKU_FULL}'))} {NO_PE}"
        l2 = (f"{Q(f'{free(f'có {PHASSA}')}, {ubho(PHASSA)}')} {YES} {Q(f'{free(sa)}, {ubho(rn)}')} {NO_PE}")
        v = S.var("Sī., Ka.", "sasaññaṃ") if variant else ""
        l3 = (f"{Q(f'tâm có {S.VEDANA}{PE} có {S.SANNA}{PE} có chủ ý{PE} có {PANNA}{v} được giải thoát, {ubho(PANNA)}')} "
              f"{YES} {Q(f'{free(sa)}, {ubho(rn)}')} {NO_PE}")
        l4b = f"{free(sa)}, {ubho(rn)}" if l4_alt else ubho(rn)
        l4 = f"{Q(f'{free(f'có {PHASSA}, {sa}')}, {ubho(PHASSA)}')} {YES} {Q(l4b)} {NO_PE}"
        l5 = (f"{Q(f'tâm có {S.VEDANA}, {sa}{PE} có {S.SANNA}, {sa}{PE} có chủ ý, {sa}{PE} có {PANNA}, {sa} được giải thoát, {ubho(PANNA)}')} "
              f"{YES} {Q(ubho(rn))} {NO_PE}")
        return [l1, l2, l3, l4, l5]

    add("5-363", *vim_block("raga", False, variant=True))
    add("5-364", *vim_block("dosa", True, l4_alt=True))
    SAMOHA3 = "có tham đắm, có sân hận, có si mê"
    add("5-365", *vim_block("moha", True),
        f"{Q(free(SAMOHA3))} {YES} {Q(free(f'{VITA}, không còn phiền não'))} {NO_PE} "
        f"{low(S.tena_hi_na(free(SAMOHA3)))}",
        S.katha_end(K["Vimutti"]))

    # ---- (24) Vimuccamānakathā ---------------------------------------------------------------------------------
    vagga_head("5-11-4-0")
    add("5-11-4-1-0", head(24, 4, "Vimuccamana"))
    TH_E = f"{Q(EKA)} {YES}"
    add("5-366",
        f"{Q(VTH)} {YES} {Q(EKA)} {NO_PE}",
        f"{TH_E} {Q(status(PN['sotāpanno'], 'thành quả vào dòng') + ', ' + SOTA_TAIL)} {NO_PE}",
        f"{TH_E} {Q(status(PN['sakadāgāmī'], 'thành quả trở lại một lần'))} {NO_PE}",
        f"{TH_E} {Q(status(PN['anāgāmī'], 'thành quả không trở lại') + ', ' + ANAG_TAIL)} {NO_PE}",
        f"{TH_E} {Q(status(PN['arahā'], 'trạng thái A-la-hán') + f', một phần {VITA}{PE} {SC_YES}, {SC_NO}')} {NO_PE}",
        f"{Q(VTH)} {YES} "
        f"{Q('vào khoảnh khắc sinh khởi là cái đã được giải thoát, vào khoảnh khắc tan rã là cái đang được giải thoát')} "
        f"{NO_PE}")
    add("5-367",
        f"{S.na_vattabbam(VTH)} {YES} {S.NANU_VUTTAM} “{SUTTA_KAMA}” [{CIT_DN} 1.248 và các chỗ khác]! "
        f"{S.ATTHEVA} {YES} Vậy thì nên nói [dị bản (Sī., Syā., Kaṃ.): tena hi; (Ka.): tena hi na vattabbaṃ] "
        f"– “{VTH}”.",
        f"{Q(VTH)} {YES} {S.NANU_VUTTAM} “{SUTTA_SAMAHITE}”! {S.ATTHEVA} {YES} {S.tena_hi_na(VTH)}",
        f"{Q(VIM_C)} {YES} {Q(RAJJ)} {NO_PE} {nanu(BOTH)} {YES} {S.hanci_neg(BOTH, VIM_C)}",
        S.katha_end(K["Vimuccamana"]))

    # ---- (25) Aṭṭhamakakathā -----------------------------------------------------------------------------------
    vagga_head("5-11-5-0")
    add("5-11-5-1-0", head(25, 5, "Atthamaka"))

    def a8q(x, lower=False):
        return (q if lower else Q)(a8(x))

    SOTA8 = f"{A8} là {PN['sotāpanno']}, đã đạt đến thành quả vào dòng"
    add("5-368",
        f"{a8q(f'{DP} {PAH}')} {YES} {Q(f'{SOTA8}, {ATTAINED_POS}')} {NO_PE}",
        f"{a8q(f'{VP} {PAH}')} {YES} {Q(f'{SOTA8}{PE} chạm đến bằng thân rồi an trú')} {NO_PE}",
        f"{a8q(f'{DP} {PAH}')} {YES} {a8q(f'{DA} {PAH}')} {NO_PE} {a8q(f'{DP} {PAH}', True)} {YES} "
        f"{a8q(f'{VA_SBP} {PAH}')} {NO_PE}",
        f"{a8q(f'{VP} {PAH}')} {YES} {a8q(f'{VA} {PAH}')} {NO_PE} {a8q(f'{VP} {PAH}', True)} {YES} "
        f"{a8q(f'{DA_SBP} {PAH}')} {NO_PE}",
        f"{a8q(f'{DA} {APAH}')} {YES} {a8q(f'{DP} {APAH}')} {NO_PE} {a8q(f'{DA} {APAH}', True)} {YES} "
        f"{a8q(f'{VP} {APAH}')} {NO_PE}",
        f"{a8q(f'{VA_SBP} {APAH}')} {YES} {a8q(f'{DP} {APAH}')} {NO_PE} {a8q(f'{SBP} {APAH}', True)} {YES} "
        f"{a8q(f'{VP} {APAH}')} {NO_PE}")
    add("5-369",
        f"{a8q(f'{DP} {PAH}')} {YES} {Q(bh8(DP, 'con đường'))} {NO_PE} {a8q(f'{DP} {PAH}', True)} {YES} "
        f"{Q(bh8(DP, f'{SP_PL}{PE} {OTHERS[0]}{PE} đã tu tập {BOJJH}'))} {NO}",
        f"{a8q(f'{VP} {PAH}')} {YES} {Q(bh8(VP, f'con đường{PE} đã tu tập {BOJJH}'))} {NO_PE}",
        f"{Q(bh8(DP, 'con đường', True))} {YES} {Q(AMAGGA)} {NO_PE} {q(bh8(DP, f'{SP_PL}{PE} {BOJJH}', True))} "
        f"{YES} {Q(AMAGGA)} {NO_PE}",
        f"{Q(bh8(VP, f'con đường{PE} {SP_PL}{PE} chưa tu tập {BOJJH}', True))} {YES} {Q(AMAGGA)} {NO_PE}")
    add("5-370",
        f"{S.na_vattabbam(a8(f'{DP} {PAH}'))} {YES} {Q('sẽ sinh khởi')} {cap(WILL_NOT)}. "
        f"{S.hanci(WILL_NOT, a8(f'{DP} {PAH}'))}",
        f"{S.na_vattabbam(a8(f'{VP} {PAH}'))} {YES} {Q('sẽ sinh khởi')} {cap(WILL_NOT)}. "
        f"{S.hanci(WILL_NOT, a8(f'{VP} {PAH}'))}",
        f"{kv(DP)} {YES} {kv(DA)} {NO_PE}",
        f"{kv(DP)} {YES} {kv(VA_SBP)} {NO_PE}",
        f"{kv(VP)} {YES} {kv(VA_SBP)} {NO_PE}",
        f"{kv(DP)} {YES} {kv(DP, GOTRA)} {NO_PE} {low(kv(VP))} {YES} {kv(VP, GOTRA)} {NO_PE}",
        S.katha_end(K["Atthamaka"]))

    # ---- (26) Aṭṭhamakassa indriyakathā ------------------------------------------------------------------------
    vagga_head("5-11-6-0")
    add("5-11-6-1-0", head(26, 6, "AtthamakaIndriya"))
    NO_SAD = Q(has(A8, f"không có {I_SAD}"))
    add("5-371",
        f"{NO_SAD} {YES} {Q(has(A8, f'không có {SADDHA}'))} {NO} "
        f"{Q(f'{A8} không có {I_VIR}{PE} không có {I_SAT}{PE} không có {I_SAM}{PE} không có {I_PAN}')} {YES} "
        f"{Q(has(A8, f'không có {PANNA}'))} {NO_PE}",
        f"{Q(has(A8, f'có {SADDHA}'))} {YES} {Q(has(A8, f'có {I_SAD}'))} {NO_PE} "
        f"{q(f'{A8} có {VIRIYA}{PE} có {SATI}{PE} có {SAMADHI}{PE} có {PANNA}')} {YES} "
        f"{Q(has(A8, f'có {I_PAN}'))} {NO_PE}",
        f"{Q(has(A8, f'có {MANO}', f'có {I_MAN}'))} {YES} {Q(has(A8, f'có {SADDHA}', f'có {I_SAD}'))} {NO_PE} "
        f"{q(has(A8, f'có {MANO}', f'có {I_MAN}'))} {YES} {Q(has(A8, f'có {PANNA}', f'có {I_PAN}'))} {NO_PE}",
        f"{Q(has(A8, f'có {SOM}', f'có {I_SOM}', f'có {JIV}', f'có {I_JIV}'))} {YES} "
        f"{Q(has(A8, f'có {SADDHA}', f'có {I_SAD}'))} {NO_PE} {q(has(A8, f'có {JIV}', f'có {I_JIV}'))} {YES} "
        f"{Q(f'{A8}{PE} có {PANNA}, có {I_PAN}')} {NO_PE}",
        f"{Q(has(A8, f'có {SADDHA}', f'không có {I_SAD}'))} {YES} {Q(has(A8, f'có {MANO}', f'không có {I_MAN}'))} "
        f"{NO_PE}",
        f"{Q(has(A8, f'có {SADDHA}', f'không có {I_SAD}'))} {YES} "
        f"{Q(f'{A8} có {SOM}, không có {I_SOM}{PE} có {JIV}, không có {I_JIV}')} {NO_PE} "
        f"{q(has(A8, f'có {PANNA}', f'không có {I_PAN}'))} {YES} {Q(has(A8, f'có {MANO}', f'không có {I_MAN}'))} "
        f"{Q(f'có {SOM}, không có {I_SOM}')} {Q(f'có {JIV}, không có {I_JIV}')} {NO_PE}",
        f"{NO_SAD} {YES} {Q(f'{A8} là người không có niềm tin')} {NO_PE} "
        f"{q(has(A8, f'không có {I_VIR}'))} {YES} {Q(f'{A8} là người lười biếng, kém tinh tấn')} {NO_PE} "
        f"{q(has(A8, f'không có {I_SAT}'))} {YES} {Q(f'{A8} là người mất tỉnh thức, không hiểu biết rõ ràng')} "
        f"{NO_PE} {q(has(A8, f'không có {I_SAM}'))} {YES} "
        f"{Q(f'{A8} là người không được định tâm, có tâm rối loạn')} {NO_PE} "
        f"{q(has(A8, f'không có {I_PAN}'))} {YES} {Q(f'{A8} là người kém trí tuệ, câm điếc')} {NO_PE}",
        f"{Q(f'{A8} có {SADDHA}, và {SADDHA} ấy {NIY}')} {YES} "
        f"{S.hanci_neg(f'{A8} có {SADDHA}, và {SADDHA} ấy {NIY}', has(A8, f'không có {I_SAD}'))} "
        f"{Q(f'{A8} có {VIRIYA}, và {VIRIYA} ấy {NIY}; có {SATI}, và {SATI} ấy {NIY}; có {SAMADHI}, và {SAMADHI} ấy {NIY}; có {PANNA}, và {PANNA} ấy {NIY}')} "
        f"{YES} {S.hanci_neg(f'{A8} có {PANNA}, và {PANNA} ấy {NIY}', has(A8, f'không có {I_PAN}'))}")

    def two(who, a, b, neg=False):
        return has(who, f"có {a}", f"{'không có' if neg else 'có'} {b}")

    add("5-372",
        f"{Q(two(P_SAKA, SADDHA, I_SAD))} {YES} {Q(two(A8, SADDHA, I_SAD))} {NO_PE} {q(two(P_SAKA, PANNA, I_PAN))} "
        f"{YES} {Q(two(A8, PANNA, I_PAN))} {NO_PE}",
        f"{Q(f'{P_ANAG}{PE} {P_ARA} có {SADDHA}, có {I_SAD}{PE} có {PANNA}, có {I_PAN}')} {YES} "
        f"{Q(two(A8, PANNA, I_PAN))} {NO_PE}",
        f"{Q(two(A8, SADDHA, I_SAD, True))} {YES} {Q(two(P_SAKA, SADDHA, I_SAD, True))} {NO_PE} "
        f"{q(two(A8, PANNA, I_PAN, True))} {YES} {Q(two(P_SAKA, PANNA, I_PAN, True))} {NO_PE}",
        f"{Q(f'{A8} có {SADDHA}, không có {I_SAD}{PE} có {PANNA}, không có {I_PAN}')} {YES} "
        f"{Q(f'{P_ANAG}{PE} {P_ARA} có {PANNA}, không có {I_PAN}')} {NO_PE}",
        f"{Q(f'{A8} không có {FIVE_I}')} {YES} {S.NANU_VUTTAM} “{SUTTA5}” [{S.CIT['saṃ. ni.']} 5.488]. "
        f"{S.ATTHEVA} {YES} {Q(f'{A8} là {BAHIRO}')} {NO_PE} vậy thì {A8} có {FIVE_I}.",
        S.katha_end(K["AtthamakaIndriya"]))

    # ---- (27) Dibbacakkhukathā ---------------------------------------------------------------------------------
    vagga_head("5-11-7-0")
    add("5-11-7-1-0", head(27, 7, "Dibbacakkhu"))

    def organ_373(m, d, gen_d, variant=""):
        th = Q(becomes(m, d))
        return [f"{th} {YES} {Q(f'{m} là {d}, {d} là {m}')} {NO_PE}",
                f"{th} {YES} {Q(f'{m} như thế nào, thì {d} cũng như thế ấy, {d} như thế nào, thì {m} cũng như thế ấy')} "
                f"{NO_PE}",
                f"{th} {YES} {Q(f'chính {m} ấy là {d} ấy, {d} ấy là {m} ấy')} {NO_PE}",
                f"{th} {YES} {Q(f'{SCOPE} của {m} như thế nào, thì {SCOPE} của {gen_d} cũng như thế ấy')} {NO_PE}",
                f"{th} {YES} Có phải là do nghiệp tạo ra{variant} rồi trở thành không do nghiệp tạo ra không? {NO_PE}",
                f"{Q(UPA)} {YES} {Q(KAMA)} {NO_PE}",
                f"{Q(KAMA)} {YES} {Q(RUPA_T)} {NO_PE}",
                f"{Q(RUPA_T)} {YES} {Q(PARI)} {NO_PE}"]

    TH_C = Q(becomes(MC, DC))
    add("5-373", *organ_373(MC, DC, DC, S.var_sp("Syā., Kaṃ.", "upādinnaṃ")))
    add("5-374",
        f"{TH_C} {YES} {Q(becomes(DC, MC))} {NO_PE}",
        f"{TH_C} {YES} {Q(becomes(DC, PC))} {NO_PE}",
        f"{TH_C} {YES} {Q(becomes(DC, MC))} {NO_PE}",
        f"{TH_C} {YES} {Q(TWO)} {NO_PE} {q(TWO)} {YES} Chẳng phải Đức Thế Tôn đã nói đến {THREE} sao? {YES} "
        f"Nếu Đức Thế Tôn đã nói đến {THREE}, thì {RE}, chắc chắn không nên nói – “{TWO}”.",
        f"{Q(TWO)} {YES} {S.NANU_VUTTAM} “{BH}, có ba loại mắt này! Ba loại mắt nào? {cap(MC)}, {DC}, {PC} – {bh}, "
        f"đây là ba loại mắt”.",
        *VERSE_EYE,
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(TWO)}",
        S.katha_end(K["Dibbacakkhu"]))

    # ---- (28) Dibbasotakathā -----------------------------------------------------------------------------------
    vagga_head("5-11-8-0")
    add("5-11-8-1-0", head(28, 8, "Dibbasota"))
    TH_S = Q(becomes(MS, DS))
    add("5-375", *organ_373(MS, DS, DS))
    add("5-376",
        f"{TH_S} {YES} {Q(becomes(DS, MS))} {NO_PE}",
        f"{TH_S} {YES} {Q(ONE)} {NO_PE}",
        f"{Q(ONE)} {YES} Chẳng phải Đức Thế Tôn đã nói đến hai loại tai – “{MS}, {DS}” sao? {YES} "
        f"Nếu Đức Thế Tôn đã nói đến hai loại tai – {MS}, {DS}, thì {RE}, chắc chắn không nên nói – “{ONE}”.",
        S.katha_end(K["Dibbasota"]))

    # ---- (29) Yathākammūpagatañāṇakathā ------------------------------------------------------------------------
    vagga_head("5-11-9-0")
    add("5-11-9-1-0", head(29, 9, "Yathakamma"))
    TH_Y = Q(TH_Y_BODY)
    ATT_YK = f"vừa chú tâm đến {YK}, {SEE}"
    LAST = ITEMS[-1]
    add("5-377",
        f"Có phải {YKN}{S.var_sp('Syā., Kaṃ.', 'yathākammūpagatañāṇaṃ')} là {DC} không? {YES} {Q(ATT_YK)} {NO_PE}",
        f"{Q(ATT_YK)} {YES} {Q(DVINNAM)} {NO_PE}",
        f"{TH_Y} {YES} {Q(', '.join(f'vừa chú tâm đến “{it}”' for it in ITEMS) + ', ' + SEE)} {NO_PE}",
        f"{Q(f'vừa chú tâm đến “{cap(LAST)}”, {SEE}')} {YES} {Q(DVINNAM)} {NO_PE}")
    SK = f"{SARI} biết {YKN}"
    add("5-378",
        f"{TH_Y} {YES} {Q(NOT_DC)} {YES} {S.hanci_neg(NOT_DC, TH_Y_BODY)}",
        f"{TH_Y} {YES} {Q(SK)} {YES} {S.hanci_neg(SK, TH_Y_BODY)}",
        f"{TH_Y} {YES} {Q(SK)} {YES} {Q(f'{SARI} có {DC}')} {NO_PE}",
        f"{Q(f'{SARI} có {DC}')} {YES} Chẳng phải {SARI} đã nói thế này sao –",
        *VERSE_SARI,
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(TH_Y_BODY)}",
        S.katha_end(K["Yathakamma"]))

    # ---- (30) Saṃvarakathā -------------------------------------------------------------------------------------
    vagga_head("5-11-10-0")
    add("5-11-10-1-0", head(30, 10, "Samvara"))
    add("5-379",
        f"{Q(f'{DEV} có {SV}')} {YES} {Q(f'{DEV} có {ASV}')} {NO_PE}",
        f"{Q(f'{DEV} không có {ASV}')} {YES} {Q(f'{DEV} không có {SV}')} {NO_PE}",
        f"{NANU(P_SV)} {YES} {Q(Q_SV)} {NO_PE}",
        f"{S.ADMIT['niggaha']} {S.hanci(P_SV, Q_SV)} {S.yam(P_SV, Q_SV)}",
        f"{S.noce(P_SV, Q_SV)} Điều bạn nói ở đây là sai – “nên nói ‘{P_SV}’, nhưng không nên nói – ‘{Q_SV}’”.",
        f"{Q(f'{MAN} có {SV}, ở đó có {ASV}')} {YES} {Q(f'{DEV} có {SV}, ở đó có {ASV}')} {NO_PE}",
        f"{Q(f'{DEV} có {SV}, ở đó không có {ASV}')} {YES} {Q(f'{MAN} có {SV}, ở đó không có {ASV}')} {NO_PE}")

    def abst(v, a):
        return [f"{Q(f'{DEV} có {v}')} {YES} {Q(f'{DEV} có {a}')} {NO_PE}"]

    add("5-380",
        *abst(PV, PA), *abst(SV2, SU),
        f"{Q(f'{DEV} không có {PA}')} {YES} {Q(f'{DEV} không có {PV}')} {NO_PE}",
        f"{Q(f'{DEV} không có {SU}')} {YES} {Q(f'{DEV} không có {SV2}')} {NO_PE}",
        f"{Q(f'{MAN} có {PV}, ở đó có {PA}')} {YES} {Q(f'{DEV} có {PV}, ở đó có {PA}')} {NO_PE}",
        f"{Q(f'{MAN} có {SV2}, ở đó có {SU}')} {YES} {Q(f'{DEV} có {SV2}, ở đó có {SU}')} {NO_PE}",
        f"{Q(f'{DEV} có {PV}, ở đó không có {PA}')} {YES} {Q(f'{MAN} có {PV}, ở đó không có {PA}')} {NO_PE}",
        f"{Q(f'{DEV} có {SV2}, ở đó không có {SU}')} {YES} {Q(f'{MAN} có {SV2}, ở đó không có {SU}')} {NO_PE}",
        f"{Q(f'{DEV} không có {SV}')} {YES} {Q(f'tất cả chư thiên đều {KP4}, {SURA_DRINK}')} {NO_PE} "
        f"vậy thì {DEV} có {SV}.",
        S.katha_end(K["Samvara"]))

    # ---- (31) Asaññakathā --------------------------------------------------------------------------------------
    vagga_head("5-11-11-0")
    add("5-11-11-1-0", head(31, 11, "Asanna"))
    TH_AQ = Q(TH_A)
    add("5-381",
        f"{TH_AQ} {YES} {Q(f'đó là {LIST_S}')} {NO_PE}",
        f"{NANU(f'đó là {LIST_A}')} {YES} {S.hanci_neg(f'đó là {LIST_A}', TH_A)}",
        f"{TH_AQ} {YES} {Q(f'đó là {vok('năm')}')} {NO_PE}",
        f"{NANU(f'đó là {vok('một')}')} {YES} {S.hanci_neg(f'đó là {vok('một')}', TH_A)}",
        f"{TH_AQ} {YES} {Q(KAR)} {NO_PE}")
    add("5-382",
        f"{Q(f'{MN}, và đó là {LIST_S}')} {YES} {Q(f'{TH_A}, và đó là {LIST_S2}')} {NO_PE}",
        f"{Q(f'{MN}, và đó là {vok('năm')}')} {YES} {Q(f'{TH_A}, và đó là {vok('năm')}')} {NO_PE}",
        f"{Q(f'{MN}, {KAR}')} {YES} {Q(f'{TH_A}, {KAR}')} {NO_PE}",
        f"{Q(f'{TH_A}, và đó là {LIST_A}')} {YES} {Q(f'{MN}, và đó là {LIST_A_PE}')} {NO_PE}",
        f"{Q(f'{TH_A}, và đó là {vok('một')}')} {YES} {Q(f'{MN}, và đó là {vok_pe('một')}')} {NO_PE}",
        f"{Q(f'{TH_A}, {KAR_NO}')} {YES} {Q(f'{MN}, {KAR_NO}')} {NO_PE}")
    SOME = ("có lúc là chúng sinh có tri giác, có lúc là chúng sinh Vô Tưởng, có lúc là sự hiện hữu có tri giác, "
            "có lúc là sự hiện hữu không có tri giác, có lúc là sự hiện hữu gồm năm khối, có lúc là sự hiện hữu "
            "gồm một khối")
    #   kiñci kāle saññasattā kiñci kāle asaññasattā, … kiñci kāle ekavokārabhavo
    WHEN = ("lúc chết, lúc tái sinh là chúng sinh có tri giác, lúc duy trì là chúng sinh Vô Tưởng; lúc chết, "
            "lúc tái sinh là sự hiện hữu có tri giác, lúc duy trì là sự hiện hữu không có tri giác; lúc chết, "
            "lúc tái sinh là sự hiện hữu gồm năm khối, lúc duy trì là sự hiện hữu gồm một khối")
    #   cutikāle upapattikāle saññasattā, ṭhitikāle asaññasattā; …
    add("5-383",
        f"{S.na_vattabbam(TH_A)} {YES} {S.NANU_VUTTAM} “{SUTTA_AS}” [{CIT_DN} 1.68]! {S.ATTHEVA} {YES} "
        f"{S.tena_hi(TH_A)}",
        f"{TH_AQ} Có lúc{S.var('Syā.', 'kañci')} có, có lúc không có. {Q(SOME)} {NO_PE}",
        f"{Q(f'{AS}, có lúc có tri giác, có lúc không có')} {YES} Lúc nào có, lúc nào không có? "
        f"Lúc chết, lúc tái sinh thì có, lúc duy trì thì không có. {Q(WHEN)} {NO_PE}",
        S.katha_end(K["Asanna"]))

    # ---- (32) Nevasaññānāsaññāyatanakathā ----------------------------------------------------------------------
    vagga_head("5-11-12-0")
    add("5-11-12-1-0", head(32, 12, "Nevasanna"))
    TH_NQ = Q(S.rq(TH_N, 0))
    NSP, ASP = nvp(f"ở {NS}"), nvp(AS)
    L_A1, L_N1, L_S4 = f"đó là {LIST_A}", f"đó là {vok_pe(MOT)}", f"đó là {vok_pe(BON)}"
    L_SPE = f"đó là {LIST_S_PE}"
    add("5-384",
        f"{TH_NQ} {YES} {Q(L_A1)} {NO_PE}",
        f"{NANU(L_SPE)} {YES} {S.hanci_neg(L_SPE, TH_N)}",
        f"{TH_NQ} {YES} {Q(L_N1)} {NO_PE}",
        f"{NANU(L_S4)} {YES} {S.hanci_neg(L_S4, TH_N)}")
    add("5-385",
        f"{Q(f'{ASP}, và {L_A1}')} {YES} {Q(f'{NSP}, và {L_A1}')} {NO_PE}",
        f"{Q(f'{ASP}, và {L_N1}')} {YES} {Q(f'{NSP}, và đó là {vok(MOT)}')} {NO_PE}",
        f"{Q(f'{NSP}, và {L_SPE}')} {YES} {Q(f'{ASP}, và {L_SPE}')} {NO_PE}",
        f"{Q(f'{NSP}, và {L_S4}')} {YES} {Q(f'{ASP}, và {L_S4}')} {NO_PE}",
        f"{TH_NQ} {YES} {NANU(c4(NS))} {YES} {S.hanci_neg(c4(NS), TH_N)}")
    TH_NNQ = S.rq(TH_NN, 0)
    THERE = "ở đó có tri giác"                       # atthi tattha saññā
    l283 = f"{Q(f'{c4(AKA)}, {THERE}')} {YES} {Q(f'{c4(NS)}, {THERE}')} {NO_PE}"
    l284 = f"{Q(f'{VIN}{PE} {c4(AKI)}, {THERE}')} {YES} {Q(f'{c4(NS)}, {THERE}')} {NO_PE}"
    AKA_NV, AKI_NV = nvp(f"ở {AKA}"), nvp(f"ở {AKI}")
    AKI_NN = f"ở {AKI}, không nên nói – “có tri giác” hay “không có”"
    ADM = "cảm giác không khó chịu cũng không dễ chịu"   # adukkhamasukhā vedanā (pi-2)
    VAR_ADM = S.var("Sī., Ka.", "adukkhamasukhā vedanā")
    L290B = f"vì cho rằng đó là {ADM}, nên đối với {ADM}{VAR_ADM}, không nên nói – “cảm giác” hay “không phải cảm giác”"
    add("5-386",
        f"{Q(f'{c4(NS)}, {NSP}')} {YES} {Q(f'{c4(AKA)}, {AKA_NV}')} {NO_PE}",
        f"{Q(f'{c4(NS)}, {NSP}')} {YES} {Q(f'{VIN}{PE} {c4(AKI)}, {AKI_NV}')} {NO_PE}",
        l283, l284,
        f"{Q(TH_NNQ)} {YES} {NANU(c4(NS))} {YES} {S.hanci_neg(c4(NS), TH_NN)}",
        f"{Q(f'{c4(NS)}, {TH_NNQ}')} {YES} {Q(f'{AKA}{PE} {VIN}{PE} {c4(AKI)}, {AKI_NN}')} {NO_PE}",
        l283, l284,
        f"Có phải ở {NS}, không nên nói{S.var('?', 'nevasaññānāsaññāyatane vattabbaṃ')} – “có tri giác” hay "
        f"“không có” không? {YES} {NANU(f'đó là {NS}')} {YES} {S.hanci(f'đó là {NS}', TH_NN)}",
        f"{Q(f'vì cho rằng đó là {NS}, nên {TH_NNQ}')} {YES} {Q(L290B)} {NO_PE}",
        S.katha_end(NS),
        VAGGA_END,
        TASSUDDANAM,
        *UDDANA)
    return segs


def main():
    check_reused11()
    segs = build()
    S.write(NAME, segs)
    if "--adh" in sys.argv:
        ADH.mkdir(parents=True, exist_ok=True)
        text = (S.OUT_DIR / NAME).read_bytes()
        (ADH / NAME).write_bytes(text)
        print("wrote", ADH / NAME)


if __name__ == "__main__":
    main()
