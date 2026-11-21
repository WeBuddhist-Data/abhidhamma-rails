"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 18, Dasamavaggo (^5-18-0 … ^5-604): eleven kathās
(95-105) with the repeated "Dasamavaggo" sub-headings, the vagga close, the uddāna and the second fifty-group close
(Dutiyo paṇṇāsako. / Tassuddānaṃ – / its uddāna; frame set in ch13).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/18-dasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, vaggo, var …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED18); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-18.md.

usage: python -I -X utf8 -B build_rails_18_vi.py          (writes the chapter and the adherence copy rails\\adh-18\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "18-dasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, RE, CIT, A = S.cap, S.RE, S.CIT, S.A


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case; ch15)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH = "Này các tỳ-khưu"                                                  # bhikkhave (sample)
SD, TU, SV, SK, SA, NL, TT, SM = S.SAMMA                                # sammādiṭṭhi … sammāsamādhi (pi-1)
LIST10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
          "sự định tâm", "trí tuệ"]                                     # phasso … paññā (ch4 / ch12 / ch15)
F8 = LIST10[1:4] + LIST10[5:]                                           # vedanā … paññā without cittaṃ (ch15)
AV7 = ["sự hướng đến", "sự chú hướng", "sự lưu ý", "sự chú tâm", "chủ ý", "sự mong ước", "sự mong cầu"]
#   āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi (ch15)
AVF = ", ".join(AV7)
AVS = f"{AV7[0]}{PE} {AV7[-1]}"                                         # āvaṭṭanā…pe… paṇidhi (ch15)
TWO = f"có sự tụ hợp của hai sự tiếp xúc{PE} hai tâm"                   # Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ (ch15)
KUS = ("các hiện tượng thiện và bất thiện, có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong sáng cùng "
       "với các mặt đối lập của chúng đi đến chỗ cùng hiện diện đối mặt nhau")   # kusalākusalā … āgacchanti (ch15)
FAR = "điều rất xa cách nhau"                                           # suvidūravidūraṃ (ch15)
SUT4_HEAD = f"“{BH}, có bốn {FAR} này! Bốn điều nào? {BH}, bầu trời và mặt đất – đây là {FAR} thứ nhất"
SUT4_TAIL = "vì vậy, bản chất của người hiền thiện ở xa kẻ không hiền thiện”"   # tasmā sataṃ dhammo asabbhi ārakā (ch15)
SUT4 = f"{SUT4_HEAD}{PE} {SUT4_TAIL}."
#   "cattārimāni, bhikkhave, suvidūravidūrāni! … idaṃ paṭhamaṃ suvidūravidūraṃ…pe… tasmā sataṃ dhammo asabbhi ārakā"ti.
ARAMA = ("“Những người trồng vườn cây, trồng rừng" + PE
         + " đứng vững trong Giáo Pháp, thành tựu giới hạnh, những người ấy đi đến cõi trời”")
#   "ārāmaropā vanaropā…pe… dhammaṭṭhā sīlasampannā te janā saggagāmino"ti (ch15 verse lines 1 and 4)
PLANTS = ", ".join(f"tăng trưởng như {x}" for x in ("dây leo", "dây quấn", "cây", "cỏ", "đống cỏ lau"))   # (ch15)
VITAKKA = ("khởi lên sự hướng tâm đến dục lạc, khởi lên sự hướng tâm đến ác ý, khởi lên sự hướng tâm đến sự "
           "hãm hại")                                                   # kāma- / byāpāda- / vihiṃsāvitakkaṃ vitakketi (ch15)
GIVE_D = "thực hiện sự bố thí"                                          # dānaṃ deti (ch15)
PU = "người phàm phu"                                                   # puthujjano (pi-1, ch12)
UP5 = "năm khối tìm cầu sự tái sinh"                                    # upapattesiye pañcakkhandhe (termbase; ch12 UPC)
PV = "sự kiềm chế việc sát hại sinh mạng"                               # pāṇātipātā veramaṇī (pi-2, ch11)
SURA = "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # surāmerayamajjapamādaṭṭhāna (pi-2)
VER = [PV, "sự kiềm chế việc lấy của không được cho", "sự kiềm chế hành vi sai trái trong các dục lạc",
       "sự kiềm chế việc nói dối", f"sự kiềm chế {SURA}"]               # (pi-2 sikkhāpada)
SINS = ["việc sát hại sinh mạng", "việc lấy của không được cho", "hành vi sai trái trong các dục lạc",
        "việc nói dối", SURA]                                           # pāṇātipāto … (pi-2, ch11, ch15)

# ch14 "cakkhuñca paṭicca X-ñca uppajjati cakkhuviññāṇaṃ" frame
EYE_R = "tùy thuộc vào mắt và các hình sắc, sinh khởi thức qua mắt"     # cakkhuñca paṭicca rūpe ca … (pi-2, ch14)
NO_HAVE = "Không có."                                                   # Natthi. (ch12, ch14)
ATTH_L = "có bài kinh như vậy thật không?"                              # "…"nti – attheva suttantoti? (ch14)


def eye(x):                         # cakkhuñca paṭicca X-ñca uppajjati cakkhuviññāṇaṃ (ch14)
    return f"tùy thuộc vào mắt và {x}, sinh khởi thức qua mắt"


def sutta_tail(x, pe=False):        # "Cakkhuñca … X"nti – attheva suttantoti? Natthi. "… rūpe ca …"nti – … (ch14)
    second = f"Không có{PE} “{EYE_R}”" if pe else f"{NO_HAVE} “{cap(EYE_R)}”"
    return (f"“{cap(eye(x))}” – {ATTH_L} {second} – {ATTH_L} {YES} "
            f"Nếu “{EYE_R}” – có bài kinh như vậy thật, thì {RE}, chắc chắn không nên nói – “{eye(x)}”.")


def cease(x):                       # X-e uppajjitvā niruddhe Y hoti (ch14 frame)
    return f"khi {x} đã sinh khởi rồi đã chấm dứt, thì người ta trở thành người phạm giới"


# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, theses, vagga close, fifty-group close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(10)                                                     # Dasamavaggo «Chương thứ mười» (termbase)
MG = "người có được con đường"                                          # maggasamaṅgī / -samaṅgissa (termbase)
T2 = f"vật chất của {MG} là con đường"                                  # maggasamaṅgissa rūpaṃ maggo
P5 = "người có được năm loại thức"                                      # pañcaviññāṇasamaṅgissa (termbase pieces)
MB = "có sự tu tập con đường"                                           # atthi maggabhāvanā (magga + bhāvanā)
T3 = f"{P5} {MB}"                                                       # pañcaviññāṇasamaṅgissa atthi maggabhāvanā
T4 = "năm loại thức vừa là thiện vừa là bất thiện"                      # pañcaviññāṇā kusalāpi akusalāpi (termbase)
T5 = "năm loại thức có sự chú hướng"                                    # pañcaviññāṇā sābhogā (termbase sābhogaṃ)
SAMG = "được trang bị"                                                  # samannāgato (termbase, ch12)
T6 = f"{MG} {SAMG} hai giới hạnh"                                       # maggasamaṅgī dvīhi sīlehi samannāgato
AC = "không phải là yếu tố đồng hành với tâm"                           # acetasika (termbase cetasika)
CE = "là yếu tố đồng hành với tâm"                                      # cetasika (termbase Sīlaṃ cetasikaṃ)
T7 = f"giới hạnh {AC}"                                                  # sīlaṃ acetasikaṃ
NC, C8 = "không vận hành theo tâm", "vận hành theo tâm"                 # (na) cittānuparivatti (termbase)
T8 = f"giới hạnh {NC}"                                                  # sīlaṃ na cittānuparivatti (termbase)
T9 = "giới hạnh có nguyên nhân từ sự thọ trì tăng trưởng"               # samādānahetukaṃ sīlaṃ vaḍḍhati (termbase)
T10 = "sự biểu lộ là giới hạnh"                                         # viññatti sīlaṃ (termbase)
T11 = "sự không biểu lộ là sự phạm giới"                                # aviññatti dussilyaṃ (termbase)
KATHA = {1: "sự chấm dứt", 2: "việc vật chất là con đường", 3: f"con đường của {P5}", 4: f"việc {T4}",
         5: "việc có sự chú hướng", 6: "hai giới hạnh", 7: f"việc {T7}", 8: f"việc {T8}",
         9: "sự thọ trì làm nguyên nhân", 10: f"việc {T10}", 11: f"việc {T11}"}
#   Nirodhakathā (termbase heading), Rūpaṃ maggoti-, Pañcaviññāṇasamaṅgissa magga-, Pañcaviññāṇā kusalāpi
#   akusalāpīti-, Sābhogāti-, Dvīhisīlehi-, Sīlaṃ acetasikanti-, Sīlaṃ na cittānuparivattīti-, Samādānahetu-
#   (termbase samādānahetu), Viññatti sīlanti-, Aviññatti dussilyantikathā
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9; vagga close)
KIR5 = f"khi {UP5} chưa chấm dứt, năm khối mang tính chức năng sinh khởi"   # … aniruddhe kiriyā pañcakkhandhā uppajjanti
UDDANA = (f"{cap(KIR5)}, {T2}, {T3}, {T4}, {T5}, {T6}, {T7}, {T8}, {T9}, {T10}, {T11}.")
#   Upapattesiye pañcakkhandhe aniruddhe kiriyā pañcakkhandhā uppajjanti, maggasamaṅgissa rūpaṃ maggo, … ,
#   samādānahetukaṃ sīlaṃ vaḍḍhatīti, viññattisīlaṃ aviññatti dussilyanti.
DUTIYO = "Nhóm năm mươi thứ hai."                                       # Dutiyo paṇṇāsako. (ch13 frame)
TASS50 = "Tóm tắt của nhóm này –"                                       # Tassuddānaṃ – (here of the fifty-group; ch13
#   «Tóm tắt của nhóm này nữa –» for Tassāpi uddānaṃ –, without «nữa» since the Pāli has no "api"; flagged)
VAR50 = (S.var("Sī., Syā., Ka.", "niyāma saṅgahagatānisaṃsatā atthi pañcavokārabhavo nirodho maggasamaṅgissa "
                                 "pañcavokārabhavoti")[:-1]
         + "; dị bản (Pī.): niyāma saṅgaha gatānisaṃsatā atthi pañcavokārabhavo maggasamaṅgissa no pañcavokārabhavo]")
UDD50 = f"Sự cố định, sự gộp vào, cõi tái sinh, lợi ích, và sự chấm dứt{VAR50}."
#   Niyāmasaṅgahagatānisaṃsatā ca nirodhoti [variants]: Niyāma- (ch14 «sự cố định»), saṅgaha (ch15 «Sự gộp vào»),
#   gati (ch16 Chagatikathā; termbase gati «cõi tái sinh»), ānisaṃsa (ch17 «lợi ích»), nirodho (here)

# pañcaviññāṇā frames (pi-2 Ñāṇavibhaṅga list)
UV = "năm loại thức có chỗ dựa đã sinh khởi và có đối tượng đã sinh khởi"   # uppannavatthukā uppannārammaṇā (pi-2)
L13 = ["có chỗ dựa đã sinh ra trước và có đối tượng đã sinh ra trước",
       "có chỗ dựa thuộc phần bên trong và có đối tượng thuộc phần bên ngoài",
       "có chỗ dựa chưa tan rã và có đối tượng chưa tan rã", "có chỗ dựa khác nhau và có đối tượng khác nhau",
       "không trải nghiệm phạm vi hoạt động của nhau", "không sinh khởi khi không có sự lưu ý",
       "không sinh khởi khi không chú tâm", "không sinh khởi liền mạch", "không sinh khởi không trước không sau",
       "không sinh khởi liền sau nhau"]                                 # purejātavatthukā … samanantarā uppajjanti (pi-2)
ANAB = "năm loại thức không có sự chú hướng"                            # pañcaviññāṇā anābhogā (pi-2)
NOT_SAM = "năm loại thức không sinh khởi liền sau nhau"                 # … na aññamaññassa samanantarā uppajjanti
LONG = "năm loại thức " + ", ".join(L13)
LONG9 = "năm loại thức " + ", ".join(L13[:-1])
EV, MV = "thức qua mắt", "ý thức"                                       # cakkhuviññāṇaṃ / manoviññāṇaṃ (termbase)
SU, AT = "sự trống rỗng", "quá khứ và tương lai"                        # suññataṃ / atītānāgataṃ (termbase)
CS, MS = f"người có được {EV} {MB}", f"người có được {MV} {MB}"         # Cakkhu- / Manoviññāṇasamaṅgissa atthi maggabhāvanā


def ar(x, who=EV):                  # X-viññāṇaṃ Y-ṃ ārabbha uppajjati (termbase «lấy … làm đối tượng mà sinh khởi»)
    return f"{who} lấy {x} làm đối tượng mà sinh khởi"


def chain(who, items):              # X-viññāṇaṃ A-ṃ ārabbha…pe… B-ṃ ārabbha uppajjati
    return f"{who} " + f"{PE} ".join(f"lấy {x} làm đối tượng" for x in items) + " mà sinh khởi"


def pr(lead, who, x):               # Lead, X-viññāṇaṃ Y-ṃ ārabbha uppajjati
    return f"{lead}, {ar(x, who)}"


def prc(lead, who, items):
    return f"{lead}, {chain(who, items)}"


PF = ["sự tiếp xúc", "vật xúc chạm"]                                    # phassaṃ ārabbha…pe… phoṭṭhabbaṃ ārabbha
OBJ9 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "mắt", "thân", "âm thanh", "vật xúc chạm"]
SEEN = "Ở đây, này các tỳ-khưu, vị tỳ-khưu khi thấy hình sắc bằng mắt thì"    # idha, bhikkhave, bhikkhu cakkhunā rūpaṃ disvā
NG, G = "không nắm giữ dấu hiệu tổng quát", "nắm giữ dấu hiệu tổng quát"      # (na) nimittaggāhī hoti (pi-2)
NGA = f"{NG}, không nắm giữ các chi tiết"                               # na nimittaggāhī hoti nānubyañjanaggāhī (pi-2)
SENSES = "khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân"
BODY = "khi chạm vật xúc chạm bằng thân thì"                            # kāyena phoṭṭhabbaṃ phusitvā
SUT_N1 = f"“{SEEN} {NGA}{PE} {SENSES} thì {NGA}”!"
SUT_N2 = f"“{SEEN} {G}{PE} {NG}{PE} khi nghe âm thanh bằng tai{PE} {BODY} {G}{PE} {NG}”!"
SUT_N3 = f"“{SEEN} {G}{PE} {NG}{PE} {BODY} {G}{PE} {NG}”!"


def fa(x, neg=False):               # X maggo, so (sā) ca (an)ārammaṇo, (n)atthi tassa (tāya) āvaṭṭanā…pe… paṇidhi
    n = "không " if neg else ""
    return f"{x} là con đường, và nó {n}có đối tượng, nó {n}có {AVS}"


def pa(items, pred, lower=False):   # A…pe… B pred-ti?
    return f"{'c' if lower else 'C'}ó phải {f'{PE} '.join(items)}{' ' + pred if pred else ''} không?"


LW, LL = "thuộc thế gian", "thuộc thế gian và vượt thế gian"           # lokiya / lokiya ca lokuttara (termbase)


def lw(items, tag=LW, lower=False, last_tag=True):   # maggasamaṅgī lokiyena X-ena…pe… samannāgato
    parts = [f"{x} {tag}" for x in items]
    if not last_tag:
        parts[-1] = items[-1]
    return f"{'c' if lower else 'C'}ó phải {MG} {SAMG} " + f"{PE} ".join(parts) + " không?"


def ip(x, pred):                    # X iṭṭhaphalā, X (a)cetasikā
    return f"{x} có kết quả đáng mong muốn, {x} {pred}"


def av(x, sv=False):                # X acetasikaṃ (sa)vipākaṃ
    return f"{x} {AC}, {'có' if sv else 'không có'} quả trổ"


REUSED18 = [  # (Pāli, Vietnamese, book)
    ("Uppannavatthukā uppannārammaṇā", "Có chỗ dựa đã sinh khởi và có đối tượng đã sinh khởi", "2"),
    *[(f"pañcaviññāṇa list {i}", v, "2") for i, v in enumerate(L13, 3)],
    ("Pañca viññāṇā anābhogā", ANAB, "2"),
    ("cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī",
     f"khi thấy hình sắc bằng mắt thì {NGA}", "2"),
    ("Sotena saddaṃ sutvā…pe… kāyena phoṭṭhabbaṃ phusitvā", SENSES, "2"),
    ("cakkhuñca paṭicca rūpe ca uppajjati", "tùy thuộc vào mắt và các hình sắc, sinh khởi", "2"),
    ("pāṇātipātā veramaṇī …", ", ".join(VER[:3]), "2"),
    ("musāvādā veramaṇī", VER[3], "2"), ("surāmeraya… veramaṇī", VER[4], "2"),
    ("dussīlā", "phạm giới", "1"), ("dussilyaṃ", "sự phạm giới", "1"),
    ("puthujjano", PU, "1"),
    *[("sammādiṭṭhi … sammāsamādhi", v, "1") for v in S.SAMMA],
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("pāṇātipātā veramaṇī", PV, "11-tatiyavaggo.md"),
    ("surāmerayamajjapamādaṭṭhānā veramaṇī", VER[4], "11-tatiyavaggo.md"),
    ("upapattesiyaṃ cittaṃ", "tâm tìm cầu sự tái sinh", "12-catutthavaggo.md"),
    ("puthujjano", PU, "12-catutthavaggo.md"),
    ("samannāgato", SAMG, "12-catutthavaggo.md"),
    ("Mahāpaṇṇāsako. / Tassāpi uddānaṃ –", "Nhóm năm mươi lớn.", "13-pancamavaggo.md"),
    ("Tassāpi uddānaṃ –", "Tóm tắt của nhóm này nữa –", "13-pancamavaggo.md"),
    ("Niyāmakathā", "Bàn về sự cố định", "14-chatthavaggo.md"),
    ("cakkhuñca paṭicca X-ñca … attheva suttantoti? Natthi.", f"” – {ATTH_L} {NO_HAVE} “{cap(EYE_R)}” – {ATTH_L}",
     "14-chatthavaggo.md"),
    ('Hañci "cakkhuñca … rūpe ca …"nti – attheva suttanto, no ca vata re vattabbe –',
     f"Nếu “{EYE_R}” – có bài kinh như vậy thật, thì {RE}, chắc chắn không nên nói – “tùy thuộc vào mắt và",
     "14-chatthavaggo.md"),
    ("X-e uppajja niruddhe … hoti", "đã sinh khởi rồi đã chấm dứt, thì người ta trở thành", "14-chatthavaggo.md"),
    ("Saṅgaho (uddāna)", "Sự gộp vào", "15-sattamavaggo.md"),
    ("āvaṭṭanā … paṇidhi", AVF, "15-sattamavaggo.md"),
    ("Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti", TWO, "15-sattamavaggo.md"),
    ("kusalākusalā … sammukhībhāvaṃ āgacchanti", KUS, "15-sattamavaggo.md"),
    ("cattārimāni, bhikkhave, suvidūravidūrāni! … idaṃ paṭhamaṃ suvidūravidūraṃ", SUT4_HEAD, "15-sattamavaggo.md"),
    ("Tasmā sataṃ dhammo asabbhi ārakā", cap(SUT4_TAIL), "15-sattamavaggo.md"),
    ("Ārāmaropā vanaropā", "“Những người trồng vườn cây, trồng rừng", "15-sattamavaggo.md"),
    ("Dhammaṭṭhā sīlasampannā, te janā saggagāmino",
     "Đứng vững trong Giáo Pháp, thành tựu giới hạnh, những người ấy đi đến cõi trời”", "15-sattamavaggo.md"),
    ("Latā viya vaḍḍhati … muñjapuñjo viya vaḍḍhati", PLANTS, "15-sattamavaggo.md"),
    ("vedanā vaḍḍhati … paññā vaḍḍhati", ", ".join(f"{x} tăng trưởng" for x in LIST10[1:]), "15-sattamavaggo.md"),
    ("kāmavitakkaṃ vitakketi …", VITAKKA, "15-sattamavaggo.md"),
    ("dānaṃ deti", GIVE_D, "15-sattamavaggo.md"),
    ("Ānisaṃsadassāvīkathā", "Bàn về người thấy lợi ích", "17-navamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED18 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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

    def sub(k, n):                  # #### Dasamavaggo / ##### (n) k. X-kathā
        heading(f"5-18-{k}-0", 4, VAGGA)
        heading(f"5-18-{k}-1-0", 5, f"({n}) {k}. {S.katha(KATHA[k])}")

    heading("5-18-0", 3, VAGGA)

    # ---- (95) 1. Nirodhakathā -------------------------------------------------------------------------------------
    heading("5-18-1-0", 4, f"(95) 1. {S.katha(KATHA[1])}")

    def kir(x):                     # Upapattesiye pañcakkhandhe aniruddhe kiriyā X uppajjati
        return f"khi {UP5} chưa chấm dứt, {x} mang tính chức năng sinh khởi"

    def sam(n):                     # N-nnaṃ khandhānaṃ samodhānaṃ hoti, N khandhā sammukhībhāvaṃ āgacchanti
        return f"có sự tụ hợp của {n} khối, {n} khối đi đến chỗ cùng hiện diện đối mặt nhau"

    add("5-571", *[f"{Q(kir(x))} {YES} {Q(sam(n))} {NO_PE} {q(sam(n))} {YES} {Q(TWO)} {NO_PE}"
                   for x, n in (("năm khối", "mười"), ("bốn khối", "chín"), ("hiểu biết", "sáu"))])
    add("5-572",
        f"{Q(f'khi {UP5} đã chấm dứt, con đường sinh khởi')} {YES} "
        f"{Q('người đã chết tu tập con đường, người đã qua đời tu tập con đường')} {NO_PE}",
        S.katha_end(KATHA[1]))

    # ---- (96) 2. Rūpaṃ maggotikathā -------------------------------------------------------------------------------
    sub(2, 96)
    NEG_A = f"nó không có đối tượng, nó không có {AVS}"

    def l573(subj, thesis, full=False):
        pos = f"nó có đối tượng, nó có {AVF if full else AVS}"
        return (f"{Q(subj)} {YES} {Q(pos)} {NO_PE} {nanu_l(NEG_A)} {YES} "
                f"{S.hanci_neg(NEG_A, thesis, sep=';')}")

    add("5-573",
        l573(T2, T2, full=True),
        l573(f"{SV} là con đường", f"{SV} là con đường"),
        f"Có phải {SK}{PE} {SA} là con đường không? {YES} {Q(f'nó có đối tượng, nó có {AVS}')} {NO_PE} "
        f"{nanu_l(NEG_A)} {YES} {S.hanci_neg(NEG_A, f'{SA} là con đường', sep=';')}")
    KA = f"{SK}{PE} {SA}"
    add("5-574",
        f"{Q(fa(SD))} {YES} {Q(fa(SV))} {NO_PE} {q(fa(SD))} {YES} {Q(fa(KA))} {NO_PE} {TU}{PE} {NL}{PE} {TT}{PE}",
        f"{Q(fa(SM))} {YES} {Q(fa(SV))} {NO_PE} {q(fa(SM))} {YES} {Q(fa(KA))} {NO_PE}",
        f"{Q(fa(SV, True))} {YES} {Q(fa(SD, True))} {NO_PE} {q(fa(SV, True))} {YES} "
        f"{Q(fa(f'{TU}{PE} {NL}{PE} {TT}{PE} {SM}', True))} {NO_PE}",
        f"{Q(fa(KA, True))} {YES} {Q(fa(f'{SD}{PE} {TU}{PE} {NL}{PE} {TT}{PE} {SM}', True))} {NO_PE}")
    V3 = f"{SV}, {SK}, {SA} là con đường"
    add("5-575",
        f"{S.na_vattabbam(T2)} {YES} {NANU(V3)} {YES} {S.hanci(V3, T2)}",
        S.katha_end(KATHA[2]))

    # ---- (97) 3. Pañcaviññāṇasamaṅgissa maggakathā ----------------------------------------------------------------
    sub(3, 97)
    add("5-576",
        f"{Q(T3)} {YES} {NANU(UV)} {YES} {S.hanci_neg(UV, T3)}",
        f"Chẳng phải {LONG}, chẳng phải {ANAB} sao? {YES} {S.hanci_neg(ANAB, T3)}")
    add("5-577",
        f"{Q(CS)} {YES} {Q(ar(SU))} {NO_PE} {q(ar(SU))} {YES} {Q(eye(SU))} {NO_PE} {q(eye(SU))} {YES} "
        f"{sutta_tail(SU)}")
    add("5-578",
        f"{Q(CS)} {YES} {Q(ar(AT))} {NO_PE} {q(CS)} {YES} {Q(chain(EV, OBJ9))} {NO_PE}",
        f"{Q(pr(MS, MV, SU))} {YES} {Q(pr(CS, EV, SU))} {NO_PE} {q(pr(MS, MV, AT))} {YES} {Q(pr(CS, EV, AT))} "
        f"{NO_PE} {q(prc(MS, MV, ['sự tiếp xúc', 'cảm giác', 'vật xúc chạm']))} {YES} "
        f"{Q(prc(CS, EV, ['sự tiếp xúc', 'cảm giác', 'vật xúc chạm']))} {NO_PE}")
    add("5-579",
        f"{S.na_vattabbam(T3)} {YES} {S.NANU_VUTTAM} {SUT_N1} [{CIT['ma. ni.']} 1.349; {CIT['a. ni.']} 4.37] "
        f"{S.ATTHEVA} {YES} {S.tena_hi(T3)}",
        S.katha_end(KATHA[3]))

    # ---- (98) 4. Pañcaviññāṇā kusalāpi akusalāpītikathā -----------------------------------------------------------
    sub(4, 98)
    add("5-580",
        f"{Q(T4)} {YES} {NANU(UV)} {YES} {S.hanci_neg(UV, T4)} Chẳng phải {LONG}, chẳng phải {ANAB} sao? {YES} "
        f"{S.hanci_neg(ANAB, T4)}")
    CK = f"{EV} là thiện"                                                # cakkhuviññāṇaṃ kusalaṃ (termbase)
    add("5-581",
        f"{Q(CK)} {YES} {Q(ar(SU))} {NO_PE} {q(ar(SU))} {YES} {Q(eye(SU))} {NO} {Q(eye(SU))} {YES} "
        f"{sutta_tail(SU)}")
    CKA, MKA = f"{EV} vừa là thiện vừa là bất thiện", f"{MV} vừa là thiện vừa là bất thiện"
    add("5-582",
        f"{Q(CKA)} {YES} {Q(ar(AT))} {NO_PE} {Q(CKA)} {YES} "
        f"{Q(chain(EV, ['sự tiếp xúc', 'tâm', 'mắt', 'thân', 'âm thanh', 'vật xúc chạm']))} {NO_PE}",
        f"{Q(pr(MKA, MV, SU))} {YES} {Q(pr(CKA, EV, SU))} {NO_PE} {q(pr(MKA, MV, AT))} {YES} "
        f"{Q(pr(CKA, EV, AT))} {NO_PE} {q(prc(MKA, MV, ['sự tiếp xúc', 'tâm', 'thân', 'âm thanh', 'vật xúc chạm']))} "
        f"{YES} {Q(prc(CKA, EV, PF))} {NO_PE}")
    add("5-583",
        f"{S.na_vattabbam(T4)} {YES} {S.NANU_VUTTAM} {SUT_N2} {S.ATTHEVA} {YES} {S.tena_hi(T4)}",
        S.katha_end(KATHA[4]))

    # ---- (99) 5. Sābhogātikathā -----------------------------------------------------------------------------------
    sub(5, 99)
    add("5-584",
        f"{Q(T5)} {YES} {NANU(UV)} {YES} {S.hanci_neg(UV, T5)} Chẳng phải {LONG9}, chẳng phải {NOT_SAM} sao? {YES} "
        f"{S.hanci_neg(NOT_SAM, T5)}")
    CSB, MSB = f"{EV} có sự chú hướng", f"{MV} có sự chú hướng"          # (termbase Cakkhuviññāṇaṃ sābhogaṃ)
    add("5-585",
        f"{Q(CSB)} {YES} {Q(ar(SU))} {NO_PE} {q(ar(SU))} {YES} {Q(eye(SU))} {NO_PE} {q(eye(SU))} {YES} "
        f"{sutta_tail(SU, pe=True)}",
        f"{Q(CSB)} {YES} {Q(ar(AT))} {NO_PE} {q(CSB)} {YES} {Q(chain(EV, PF))} {NO_PE} "
        f"{q(pr(MSB, MV, SU))} {YES} {Q(pr(CSB, EV, SU))} {NO_PE} {q(pr(MSB, MV, AT))} {YES} {Q(pr(CSB, EV, AT))} "
        f"{NO_PE} {q(prc(MSB, MV, PF))} {YES} {Q(prc(CSB, EV, PF))} {NO_PE}")
    add("5-586",
        f"{S.na_vattabbam(T5)} {YES} {S.NANU_VUTTAM} {SUT_N3} {S.ATTHEVA} {YES} {S.tena_hi(T5)[:-1]}{PE}",
        S.katha_end(KATHA[5]))

    # ---- (100) 6. Dvīhisīlehikathā --------------------------------------------------------------------------------
    sub(6, 100)
    L_LOK = ["sự tiếp xúc", "cảm giác", "trí tuệ", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
             "sự định tâm", "trí tuệ"]                                  # lokiyena phassena … lokiyāya paññāya (as written)
    add("5-587",
        f"{Q(T6)} {YES} {Q(f'{MG} {SAMG} ' + ', '.join(f'hai {x}' for x in LIST10))} {NO_PE}",
        f"{Q(f'{MG} {SAMG} giới hạnh {LW}')} {YES} {Q(f'{MG} {SAMG} ' + ', '.join(f'{x} {LW}' for x in L_LOK))} "
        f"{NO_PE}",
        f"{Q(f'{MG} {SAMG} giới hạnh {LL}')} {YES} Có phải {MG} {SAMG} sự tiếp xúc {LL}{PE} {SAMG} trí tuệ {LL} "
        f"không? {NO_PE} {q(f'{MG} {SAMG} giới hạnh {LW}')} {YES} {Q(f'{MG} là {PU}')} {NO_PE}")
    add("5-588",
        f"{lw([SV])} {YES} {lw([SD])} {NO_PE} {lw([SV], lower=True)} {YES} {lw([TU, NL, TT, SM])} {NO_PE} "
        f"{lw([SK, SA], lower=True)} {YES} {lw([SD, SM])} {NO_PE}",
        f"{lw([SV], LL)} {YES} {lw([SD], LL)} {NO_PE} {lw([SV], LL, lower=True)} {YES} {lw([TU, NL, TT, SM], LL)} "
        f"{NO_PE}",
        f"{lw([SK, SA], LL, last_tag=False)} {YES} {lw([SD], LL)} {NO_PE} {lw([SA], LL, lower=True)} {YES} "
        f"{lw([TU, SM], LL)} {NO_PE}")
    add("5-589",
        f"{S.na_vattabbam(T6)} {YES} {Q(f'khi giới hạnh {LW} đã chấm dứt, con đường sinh khởi')} {YES} "
        f"{Q('người phạm giới, người có giới hạnh bị sứt mẻ, người có giới hạnh bị đứt đoạn tu tập con đường')} "
        f"{NO_PE} vậy thì {T6}.",
        S.katha_end(KATHA[6]))

    # ---- (101) 7. Sīlaṃ acetasikantikathā -------------------------------------------------------------------------
    sub(7, 101)
    OBJ7 = (f"đó là vật chất{PE} Niết-bàn{PE} {A['cakkhāyatana']}{PE} {A['kāyāyatana']}{PE} {A['rūpāyatana']}{PE} "
            f"{A['phoṭṭhabbāyatana']}")
    add("5-590",
        f"{Q(T7)} {YES} {Q(OBJ7)} {NO_PE} {q(T7)} {YES} {Q(f'sự tiếp xúc {AC}')} {NO_PE} {q(T7)} {YES} "
        f"{pa(F8, AC)} {NO_PE}",
        f"{Q(f'sự tiếp xúc {CE}')} {YES} {Q(f'giới hạnh {CE}')} {NO_PE} {pa(F8, CE, True)} {YES} "
        f"{Q(f'giới hạnh {CE}')} {NO_PE}")
    GOOD = "nó có kết quả đáng mong muốn"                               # iṭṭhaphalaṃ
    VSP = ["sự tinh tấn", "sự tỉnh thức", "sự định tâm"]
    add("5-591",
        f"{Q(T7)} {YES} {Q('nó có kết quả không đáng mong muốn')} {NO_PE} {nanu_l(GOOD)} {YES} "
        f"{S.hanci_neg(GOOD, T7)}",
        f"{Q(ip('niềm tin', CE))} {YES} {Q(ip('giới hạnh', CE))} {NO_PE} {pa(VSP + [ip('trí tuệ', CE)], '', True)} "
        f"{YES} {Q(ip('giới hạnh', CE))} {NO_PE}",
        f"{Q(ip('giới hạnh', AC))} {YES} {Q(ip('niềm tin', AC))} {NO_PE} {q(ip('giới hạnh', AC))} {YES} "
        f"{pa(VSP + [ip('trí tuệ', AC)], '')} {NO_PE}")
    FR = "nó có kết quả, có quả trổ"                                    # saphalaṃ savipākaṃ
    A4 = [A["sotāyatana"], A["kāyāyatana"], A["rūpāyatana"]]
    add("5-592",
        f"{Q(T7)} {YES} {Q('nó không có kết quả, không có quả trổ')} {NO_PE} {nanu_l(FR)} {YES} "
        f"{S.hanci_neg(FR, T7)[:-1]}{PE}",
        f"{Q(av(A['cakkhāyatana']))} {YES} {Q(av('giới hạnh'))} {NO_PE} "
        f"{pa(A4 + [av(A['phoṭṭhabbāyatana'])], '', True)} {YES} {Q(av('giới hạnh'))} {NO_PE}",
        f"{Q(av('giới hạnh', True))} {YES} {Q(av(A['cakkhāyatana'], True))} {NO_PE} {q(av('giới hạnh', True))} {YES} "
        f"{pa(A4 + [av(A['phoṭṭhabbāyatana'], True)], '')} {NO_PE}")
    P4 = [TU, NL, TT, SM]
    add("5-593",
        f"{pa([SV], AC)} {YES} {pa([SD], AC)} {NO_PE} {pa([SV], AC, True)} {YES} {pa(P4, AC)} {NO_PE} "
        f"{pa([SK, SA], AC, True)} {YES} {pa([SD], AC)} {NO_PE} {pa([SA], AC, True)} {YES} {pa(P4, AC)} {NO_PE}",
        f"{pa([SD], CE)} {YES} {pa([SV], CE)} {NO_PE} {pa([SD], CE, True)} {YES} {pa([SK, SA], CE)} {NO_PE} "
        f"{pa(P4, CE, True)} {YES} {pa([SV], CE)} {NO_PE} {pa([SM], CE, True)} {YES} {pa([SK, SA], CE)} {NO_PE}")
    add("5-594",
        f"{S.na_vattabbam(T7)} {YES} {Q(cease('giới hạnh'))} {NO} {S.tena_hi(T7)}",
        S.katha_end(KATHA[7]))

    # ---- (102) 8. Sīlaṃ na cittānuparivattītikathā ----------------------------------------------------------------
    sub(8, 102)
    OBJ8 = f"đó là vật chất{PE} Niết-bàn{PE} {A['cakkhāyatana']}{PE} {A['phoṭṭhabbāyatana']}"
    add("5-595",
        f"{Q(T8)} {YES} {Q(OBJ8)} {NO_PE} {q(T8)} {YES} {Q(f'sự tiếp xúc {NC}')} {NO_PE} {q(T8)} {YES} "
        f"{pa(F8, NC)} {NO_PE}",
        f"{Q(f'sự tiếp xúc {C8}')} {YES} {Q(f'giới hạnh {C8}')} {NO_PE} {pa(F8, C8, True)} {YES} "
        f"{Q(f'giới hạnh {C8}')} {NO_PE}")
    add("5-596",
        f"{pa([SV], NC)} {YES} {pa([SD], NC)} {NO_PE} {pa([SV], NC, True)} {YES} {pa(P4, NC)} {NO_PE}",
        f"{pa([SK, SA], NC)} {YES} {pa([SD], NC)} {NO_PE} {pa([SA], NC, True)} {YES} {pa(P4, NC)} {NO_PE}",
        f"{pa([SD], C8)} {YES} {pa([SV], C8)} {NO_PE} {pa([SD], C8, True)} {YES} {pa([SK, SA], C8)} {NO_PE}",
        f"{pa(P4, C8)} {YES} {pa([SV], C8)} {NO_PE} {pa([SM], C8, True)} {YES} {pa([SK, SA], C8)} {NO_PE}")
    add("5-597",
        f"{S.na_vattabbam(T8)} {YES} {Q(cease('giới hạnh'))} {NO} {S.tena_hi(T8)}",
        S.katha_end(KATHA[8]))

    # ---- (103) 9. Samādānahetukathā -------------------------------------------------------------------------------
    sub(9, 103)
    GROW = ("sự tiếp xúc có nguyên nhân từ sự thọ trì tăng trưởng, "
            + ", ".join(f"{x} tăng trưởng" for x in LIST10[1:]))       # samādānahetuko phasso vaḍḍhati, vedanā …
    add("5-598",
        f"{Q(T9)} {YES} {Q(GROW)} {NO_PE}",
        f"{Q(T9)} {YES} {Q(PLANTS)} {NO_PE}")
    VIT9 = f"đối với người đã thọ trì giới hạnh rồi {VITAKKA}, giới hạnh tăng trưởng"
    #   sīlaṃ samādiyitvā kāmavitakkaṃ vitakkentassa … sīlaṃ vaḍḍhati (termbase samādiyitvā «đã thọ trì … rồi»)
    KUS_SUT = f"{Q(KUS)} {YES} {S.NANU_VUTTAM} {SUT4} {S.ATTHEVA} {YES} {S.tena_hi_na(KUS)}"
    add("5-599",
        f"{Q(T9)} {YES} {Q(VIT9)} {YES} {Q(TWO)} {NO_PE} {q(TWO)} {YES} {Q(KUS)} {NO_PE}",
        KUS_SUT)
    add("5-600",
        f"{S.na_vattabbam(T9)} {YES} {S.NANU_VUTTAM} {ARAMA}. {S.ATTHEVA} {YES} {S.tena_hi(T9)}",
        S.katha_end(KATHA[9]))

    # ---- (104) 10. Viññatti sīlantikathā --------------------------------------------------------------------------
    sub(10, 104)
    ETI = ["sự đảnh lễ", "sự đứng dậy chào đón", "sự chắp tay", "việc làm kính cẩn đúng phép",
           "việc mang đến chỗ ngồi", "việc mang đến chỗ nằm", "việc mang đến nước rửa chân",
           "việc mang đến miếng chà chân", "việc chà lưng khi tắm"]
    #   abhivādanaṃ, paccuṭṭhānaṃ, añjalikammaṃ, sāmīcikammaṃ, āsanābhihāro, seyyābhihāro, pādodakābhihāro,
    #   pādakathalikābhihāro, nhāne piṭṭhiparikammaṃ (termbase; piṭṭhi, pādodaka: see notes)
    add("5-601",
        f"{Q(T10)} {YES} " + " ".join(f"{(Q if i == 0 else q)(f'đó là {v}')} {NO_PE}" for i, v in enumerate(VER)),
        f"Có phải {', '.join(f'{x} là giới hạnh' for x in ETI)} không? {YES} {Q(f'đó là {VER[0]}')} {NO_PE} "
        f"{q(f'đó là {VER[-1]}')} {NO_PE}")
    add("5-602",
        f"{S.na_vattabbam(T10)} {YES} {Q('đó là sự phạm giới')} {NO_PE} vậy thì {T10}.",
        S.katha_end(KATHA[10]))

    # ---- (105) 11. Aviññatti dussilyantikathā ---------------------------------------------------------------------
    sub(11, 105)
    BOTH = "cả phước và điều không phải phước đều tăng trưởng"          # puññañca apuññañca ubho vaḍḍhanti
    PAPA = f"đối với người đã thọ trì nghiệp xấu ác rồi {GIVE_D}, {BOTH}"   # pāpakammaṃ samādiyitvā dānaṃ dadantassa …
    add("5-603",
        f"{Q(T11)} {YES} " + " ".join(f"{(Q if i == 0 else q)(f'đó là {v}')} {NO_PE}" for i, v in enumerate(SINS)),
        f"{Q(PAPA)} {NO_PE} {q(BOTH)} {YES} {Q(TWO)} {NO_PE} {q(TWO)} {YES} {Q(KUS)} {NO_PE}",
        KUS_SUT)
    SAMD = "người ấy đã thọ trì nghiệp xấu ác"                          # pāpakammaṃ samādinno āsi
    add("5-604",
        f"{S.na_vattabbam(T11)} {YES} {NANU(SAMD)} {YES} {S.hanci(SAMD, T11)}",
        S.katha_end(KATHA[11]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA,
        DUTIYO,
        TASS50,
        UDD50)
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
    adh = S.FORMULAS_MD.parent / "adh-18"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
