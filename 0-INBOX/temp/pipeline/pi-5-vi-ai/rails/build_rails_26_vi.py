"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 26, Aṭṭhārasamavaggo (^5-26-0 … ^5-827): nine kathās
(177-185) with the repeated "Aṭṭhārasamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/26-attharasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
neu, tena_hi, katha, katha_end, CIT …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED26);
strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-26.md.

usage: python -I -X utf8 -B build_rails_26_vi.py          (writes the chapter and the adherence copy rails\\adh-26\\)
       python -I -X utf8 -B build_rails_26_vi.py find <regex> [max] [maxchars] [ctx]   (finished pi-5 rails lookup)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "26-attharasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, CIT = S.cap, S.CIT
FINISHED = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
            "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
            "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
            "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
            "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md", "19-ekadasamavaggo.md",
            "20-dvadasamavaggo.md", "21-terasamavaggo.md"]
DN = "Trường Bộ Kinh"                                   # dī. ni. (ch8)


def nanu(x):                          # …pe… nanu Xti? (lower case after …pe…)
    return f"chẳng phải {x} sao?"


def pe_end(s):                        # a closing "…ti…pe…." : the final «.» is absorbed by «…»
    assert s.endswith(".")
    return s[:-1] + PE


BUD = "Đức Phật, Đức Thế Tôn"                          # buddho bhagavā / buddhassa bhagavato / buddhena bhagavatā (ch3, ch10)
BH = "Đức Thế Tôn"                                      # bhagavā

# ---------------------------------------------------------------------------------------------------------------
# (177) Manussaloka
# ---------------------------------------------------------------------------------------------------------------
T1 = f"{BUD} đã sống trong thế giới loài người"        # buddho bhagavā manussaloke aṭṭhāsi (aṭṭhāsi «đã sống», termbase)
PLACES = (f"có các bảo tháp, vườn cây, tịnh xá, làng, thị trấn, thành phố, đất nước, xứ nơi Đức Phật đã cư trú")
#   atthi buddhavutthāni cetiyāni ārāmavihāragāmanigamanagarāni raṭṭhāni janapadāni (termbase each; janapada «xứ» ch3)
BIRTH3 = (f"{BH} đã sinh ra ở Lâm-tỳ-ni, đã giác ngộ hoàn toàn dưới gốc cây Bồ-đề, "
          f"bánh xe Giáo Pháp đã được {BH} chuyển ở Ba-la-nại")              # (ch3 line 11, byte-identical)
BIRTH = (f"{BIRTH3}, tạo tác của tuổi thọ đã được buông bỏ tại bảo tháp Ca-pa-la, "
         f"{BH} đã nhập Niết-bàn trọn vẹn ở Câu-thi-na")
#   cāpāle cetiye āyusaṅkhāro ossaṭṭho, kusinārāyaṃ bhagavā parinibbuto (ossaṭṭho «đã được buông bỏ», termbase)
BIRTH_S = f"{BH} đã sinh ra ở Lâm-tỳ-ni{PE} {BH} đã nhập Niết-bàn trọn vẹn ở Câu-thi-na"


def ekam(x):                          # ekamidāhaṃ, bhikkhave, samayaṃ X viharāmi …
    return f"Này các tỳ-khưu, một thời Ta trú ở {x}"   # samayaṃ «thời», viharāmi «trú» (termbase)


SUT_PLACES = (f"“{ekam('Úc-cát-tha, tại rừng Su-bha-ga, dưới gốc cây sa-la chúa')}” [{DN} 2.91]; "
              f"“{ekam('Ưu-lâu-tần-loa, bên cây đa của người chăn dê, khi vừa mới giác ngộ hoàn toàn')}” "
              f"[{CIT['a. ni.']} 4.21]; "
              f"“{ekam('Vương Xá, tại Trúc Lâm, nơi cho sóc ăn')}” [{DN} 2.180]; "
              f"“{ekam('Xá-vệ, tại rừng Kỳ-đà, khu vườn của Cấp Cô Độc')}”; "
              f"“{ekam('Tỳ-xá-ly, tại Đại Lâm, trong giảng đường có mái nhọn')}” [{DN} 3.11]!")
#   ukkaṭṭhāyaṃ … subhagavane sālarājamūle; uruvelāyaṃ … ajapālanigrodhe paṭhamābhisambuddho; rājagahe … veḷuvane
#   kaḷandakanivāpe; sāvatthiyaṃ … jetavane anāthapiṇḍikassa ārāme; vesāliyaṃ … mahāvane kūṭāgārasālāya
WORLD = (f"{BH} đã sinh ra trong thế gian, đã lớn lên trong thế gian, sống vượt lên trên thế gian, "
         f"không bị vấy bẩn bởi thế gian")                 # (ch12 «Không bị vấy bẩn bởi …»)
#   bhagavā loke jāto, loke saṃvaḍḍho, lokaṃ abhibhuyya viharati anupalitto lokena (viharati «sống», termbase)

# ---------------------------------------------------------------------------------------------------------------
# (178) Dhammadesanā
# ---------------------------------------------------------------------------------------------------------------
T2 = f"Giáo Pháp đã được {BUD} thuyết giảng"           # buddhena bhagavatā dhammo desito (termbase dhammo desito)
KENA = "Được ai thuyết giảng?"                          # Kena desitoti?
JINO = ("bậc chiến thắng, bậc đạo sư, bậc Tự Giác Ngộ Hoàn Toàn, bậc toàn tri, bậc thấy tất cả, "
        "bậc làm chủ Giáo Pháp, chỗ nương tựa về Giáo Pháp")             # jino satthā … dhammappaṭisaraṇo (ch11)
SARI = ("“Này Xá-lợi-phất, Ta cũng có thể thuyết giảng Giáo Pháp một cách tóm tắt; "
        "này Xá-lợi-phất, Ta cũng có thể thuyết giảng Giáo Pháp một cách chi tiết; "
        "này Xá-lợi-phất, Ta cũng có thể thuyết giảng Giáo Pháp một cách vừa tóm tắt vừa chi tiết; "
        f"còn những người hiểu được thì khó tìm” [{CIT['a. ni.']} 3.33, trong Kinh Xá-lợi-phất]!")
#   saṃkhittenapi … vitthārenapi … saṃkhittavitthārenapi kho ahaṃ, sāriputta, dhammaṃ deseyyaṃ; aññātāro ca dullabhā
AB = "sau khi đã hiểu biết trực tiếp, không phải khi chưa hiểu biết trực tiếp"   # abhiññāya … no anabhiññāya
#   (termbase abhiññāya dhammaṃ «Giáo Pháp sau khi đã hiểu biết trực tiếp»)
NI = "có căn nguyên, không phải không có căn nguyên"                          # sanidānaṃ … no anidānaṃ
PA = "có sức thuyết phục, không phải không có sức thuyết phục"               # sappāṭihāriyaṃ … no appāṭihāriyaṃ
SUT_DESANA = (f"“‘Này các tỳ-khưu, Ta thuyết giảng Giáo Pháp {AB}; "
              f"này các tỳ-khưu, Ta thuyết giảng Giáo Pháp {NI}; "
              f"này các tỳ-khưu, Ta thuyết giảng Giáo Pháp {PA}; "
              f"đối với Ta{S.var('Sī., Pī., Ka.', 'yañcassa')}, này các tỳ-khưu, người thuyết giảng Giáo Pháp {AB}, "
              f"thuyết giảng Giáo Pháp {NI}, thuyết giảng Giáo Pháp {PA}, thì lời khuyên dạy là điều nên làm, "
              "lời giáo huấn là điều nên làm; và, này các tỳ-khưu, thật đủ để các ông thỏa mãn, đủ để hài lòng, "
              f"đủ để có niềm vui – {BH} là bậc Tự Giác Ngộ Hoàn Toàn, Giáo Pháp được khéo thuyết giảng, "
              "Tăng đoàn thực hành tốt đẹp’. Và khi lời giải đáp này đang được nói ra, mười nghìn thế giới đã rung chuyển” "
              f"[{CIT['a. ni.']} 3.126]!")
#   karaṇīyo ovādo karaṇīyā anusāsanī; alañca pana vo, bhikkhave, tuṭṭhiyā alaṃ attamanatāya alaṃ somanassāya –
#   sammāsambuddho bhagavā, svākkhāto dhammo, suppaṭipanno saṅgho’ti. Imasmiñca pana veyyākaraṇasmiṃ bhaññamāne
#   dasasahassilokadhātu akampitthā (termbase; nidāna: sibling nidānato «căn nguyên»)

# ---------------------------------------------------------------------------------------------------------------
# (179) Karuṇā
# ---------------------------------------------------------------------------------------------------------------
KAR, MET, MUD, UPE = "lòng trắc ẩn", "lòng từ ái", "niềm vui đồng cảm", "sự bình thản"   # (termbase, pi-1)


def bh(x, neg=False):                 # (n)atthi buddhassa bhagavato X  (genitive possessor «có», as ch10 samāpannassa atthi)
    return f"{BUD} {'không ' if neg else ''}có {x}"


T3 = bh(KAR, True)                                      # natthi buddhassa bhagavato karuṇā
KARUNIKO = (f"{BH} là người có lòng trắc ẩn, người mang lại lợi ích cho thế gian, người thương xót thế gian, "
            "người hành động vì lợi ích của thế gian")
#   bhagavā kāruṇiko lokahito lokānukampako lokatthacaro (termbase kāruṇiko, hito, anukampāya, caro, atthāya)
MAHAK = f"{BH} đã nhập thành tựu thiền của lòng trắc ẩn lớn"   # bhagavā mahākaruṇāsamāpattiṃ samāpajji (termbase)

# ---------------------------------------------------------------------------------------------------------------
# (180) Gandhajāti
# ---------------------------------------------------------------------------------------------------------------
UP = f"phân và nước tiểu của {BUD}"                     # buddhassa bhagavato uccārapassāvo (termbase uccāra, passāvo)
T4 = f"{UP} vượt trội hơn hẳn các loại hương thơm khác"   # … ativiya aññe gandhajāte adhiggaṇhāti
ODANA = f"{BH} ăn cơm và cháo"                          # bhagavā odanakummāsaṃ bhuñjati (termbase odana, kummāsaṃ)
KECI = (f"có ai đó tắm bằng {UP}, thoa, xoa lên người{S.var('Sī., Pī., Ka.', 'uccārenti')}, "
        "cất giữ trong giỏ, đặt vào hộp, bày ra ở cửa hàng, "
        "và dùng hương thơm ấy để làm những điều nên làm với hương thơm")
#   atthi keci … nhāyanti vilimpanti ucchādenti [uccārenti (sī. pī. ka.)] peḷāya paṭisāmenti karaṇḍāya nikkhipanti
#   āpaṇe pasārenti, tena ca gandhena gandhakaraṇīyaṃ karonti

# ---------------------------------------------------------------------------------------------------------------
# (181) Ekamagga
# ---------------------------------------------------------------------------------------------------------------
FOUR = "bốn thành quả của đời sống sa-môn"              # cattāri sāmaññaphalāni (ch4 «ba thành quả của đời sống sa-môn»)
T5 = f"tự mình chứng nghiệm {FOUR} bằng một con đường cao quý"   # ekena ariyamaggena … sacchikaroti
CATU = f"có sự tụ hợp của bốn sự tiếp xúc{PE} bốn tri giác"      # Catunnaṃ phassānaṃ…pe… catunnaṃ saññānaṃ (ch4)
KATAMENA = "Bằng con đường nào? Bằng con đường A-la-hán."       # Katamena maggenāti? Arahattamaggenāti. (ch4)
A1 = ("dứt bỏ quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch về giới hạnh và nghi thức "
      "bằng con đường A-la-hán")                                  # (ch12 line 192)
S1 = f"{BH} đã nói rằng sự dứt bỏ ba xiềng xích là thành quả vào dòng"   # (ch12)
A2 = "dứt bỏ sự tham đắm dục lạc ở dạng thô, ác ý ở dạng thô bằng con đường A-la-hán"   # (ch12 line 194)
S2 = f"{BH} đã nói rằng sự suy yếu của sự tham đắm dục lạc và ác ý là thành quả trở lại một lần"   # (ch12)
A3 = "dứt bỏ sự tham đắm dục lạc ở dạng nhỏ nhiệm, ác ý ở dạng nhỏ nhiệm bằng con đường A-la-hán"  # (ch12 line 196)
S3 = (f"{BH} đã nói rằng sự dứt bỏ sự tham đắm dục lạc và ác ý không còn sót lại "
      "là thành quả không trở lại")                                       # (ch12)
SAVAKA = (f"các đệ tử thấy điều mà {BUD} chưa thấy, đạt được điều chưa chứng đắc, "
          "tự mình chứng nghiệm điều chưa tự mình chứng nghiệm")
#   sāvakā buddhassa bhagavato adiṭṭhaṃ dakkhanti anadhigataṃ adhigacchanti asacchikataṃ sacchikaronti
#   (adiṭṭhaṃ «chưa thấy», adhigacchanti «đạt được», asacchikataṃ termbase; anadhigata «chưa chứng đắc» ch11)

# ---------------------------------------------------------------------------------------------------------------
# (182) Jhānasaṅkanti
# ---------------------------------------------------------------------------------------------------------------
ORD = {1: "nhất", 2: "hai", 3: "ba", 4: "tư"}
T6 = "chuyển từ tầng thiền sang tầng thiền"             # jhānā jhānaṃ saṅkamati (saṅkamati «chuyển», termbase)


def jh(n):
    return f"tầng thiền thứ {ORD[n]}"


def sk(a, b):                         # X-ā jhānā Y-ṃ jhānaṃ saṅkamati
    return f"chuyển từ {jh(a)} sang {jh(b)}"


def av(a, b):                         # yā X-assa jhānassa uppādāya āvaṭṭanā…pe… paṇidhi, sāva Y-assa … paṇidhi
    return (f"sự hướng đến{PE} sự mong cầu nào để {jh(a)} sinh khởi, "
            f"thì chính sự hướng đến{PE} sự mong cầu ấy để {jh(b)} sinh khởi")
#   āvaṭṭanā «sự hướng đến», paṇidhi «sự mong cầu» (ch15 / ch16 series), uppādāya / uppajjati «sinh khởi»


def arise(n, neg):                    # X-ṃ jhānaṃ (an)āvaṭṭentassa uppajjati…pe… (ap)paṇidahantassa uppajjati
    k = "không " if neg else ""
    return f"{jh(n)} sinh khởi nơi người {k}hướng đến{PE} sinh khởi nơi người {k}mong cầu"


def danger(n, obj):                   # X-ṃ jhānaṃ OBJ ādīnavato manasikaroto uppajjati
    return f"{jh(n)} sinh khởi nơi người chú tâm đến {obj} như là sự nguy hại"


def same(a, b):                       # taññeva X-ṃ jhānaṃ taṃ Y-ṃ jhānaṃ (ch5 «chính cái … ấy là cái … ấy»)
    return f"chính {jh(a)} ấy là {jh(b)} ấy"


def sank_block(a, b, obj, quality, pe_first):
    """^5-813 (1→2) / ^5-814 (2→3) / ^5-815 (3→4): lines 2-5 of each block (the 1→2 block has a first line more)."""
    l2 = f"{Q(sk(a, b))} {YES} {Q(av(a, b))} {NO_PE}"
    hn = S.hanci_neg(arise(b, False), sk(a, b))
    l3 = (f"{Q(sk(a, b) + ', nhưng không nên nói – “' + av(a, b) + '”')} {YES} {Q(arise(b, True))} {NO_PE} "
          f"{nanu(arise(b, False))} {YES} {pe_end(hn) if pe_first else hn}")
    l4 = f"{Q(sk(a, b))} {YES} {Q(danger(a, obj))} {YES} {Q(danger(b, obj))} {NO_PE}"
    l5 = (f"{Q(jh(a) + ' ' + quality)} {YES} {Q(jh(b) + ' ' + quality)} {NO_PE} {q(sk(a, b))} {YES} "
          f"{Q(same(a, b))} {NO_PE}")
    return [l2, l3, l4, l5]


SUT_JH = (f"“Ở đây, này các tỳ-khưu, vị tỳ-khưu hoàn toàn tách khỏi các dục lạc{PE} "
          f"chứng nhập và an trú tầng thiền thứ tư” [{CIT['a. ni.']} 2.13; 4.163]!")
#   idha, bhikkhave, bhikkhu vivicceva kāmehi…pe… catutthaṃ jhānaṃ upasampajja viharati (ch21 / pi-2 wording)

# ---------------------------------------------------------------------------------------------------------------
# (183) Jhānantarika
# ---------------------------------------------------------------------------------------------------------------
JA = "tầng thiền trung gian"                            # jhānantarikā (termbase)
T7 = f"{JA} tồn tại"                                    # atthi jhānantarikā (atthi «tồn tại», APPROVED; ch9 rule)
NT = f"{JA} không tồn tại"                              # natthi jhānantarikā


def btw(a, b):                        # X-assa ca jhānassa Y-assa ca jhānassa antare
    return f"ở khoảng giữa {jh(a)} và {jh(b)}"


SV = "định tâm có sự hướng tâm và sự duy trì tâm"                   # savitakko savicāro samādhi (ch17)
AV = "định tâm không có sự hướng tâm, chỉ có sự duy trì tâm"        # avitakko vicāramatto samādhi (ch17)
AA = "định tâm không có sự hướng tâm cũng không có sự duy trì tâm"  # avitakko avicāro samādhi (ch17)


def is_ja(x, neg=False):              # X (na) jhānantarikā
    return f"{x} {'không phải là' if neg else 'là'} {JA}"


TWO_PRESENT = "ở khoảng giữa hai tầng thiền thuộc hiện tại"        # dvinnaṃ jhānānaṃ paṭuppannānamantare
VATT = (f"khi {AV} đang diễn ra, tầng thiền thứ nhất đã chấm dứt, tầng thiền thứ hai thuộc hiện tại")
#   avitakke vicāramatte samādhimhi vattamāne paṭhamaṃ jhānaṃ niruddhaṃ dutiyaṃ jhānaṃ paṭuppannaṃ
#   (vattamāne «đang diễn ra», niruddhaṃ «đã chấm dứt»; paṭuppanna: sibling Paṭuppannañāṇakathā «hiện tại»,
#   «thuộc hiện tại» as ch5 paccuppanna)
TAYO = (f"{BH} đã nói đến ba loại định tâm – {SV}, {AV}, {AA}")        # tayo samādhī vuttā bhagavatā – … (ch17)
TAYO_S = f"{BH} đã nói đến ba loại định tâm – định tâm có sự hướng tâm{PE} cũng không có sự duy trì tâm"
#   … savitakko…pe… avicāro samādhi

# ---------------------------------------------------------------------------------------------------------------
# (184) Saddaṃ suṇāti
# ---------------------------------------------------------------------------------------------------------------
SAMP = "người đang nhập thành tựu thiền"                # samāpanno (termbase Samāpanno saddaṃ suṇāti; as ch21)
T8 = f"{SAMP} nghe âm thanh"                            # samāpanno saddaṃ suṇāti (termbase)
SEE = "thấy hình sắc bằng mắt"                          # cakkhunā rūpaṃ passati (ch12)
HEAR = "nghe âm thanh bằng tai"                         # sotena saddaṃ suṇāti (ch12)
SMELL = "ngửi mùi bằng mũi"                             # ghānena gandhaṃ ghāyati (ch12)
TASTE = "nếm vị bằng lưỡi"                              # jivhāya rasaṃ sāyati (ch12)
TOUCH = "chạm vào vật xúc chạm bằng thân"               # kāyena phoṭṭhabbaṃ phusati (ch12)
SENSES = f"{SAMP} {SEE}{PE} bằng tai{PE} bằng mũi{PE} bằng lưỡi{PE} {TOUCH}"
#   samāpanno cakkhunā rūpaṃ passati…pe… sotena…pe… ghānena…pe… jivhāya…pe… kāyena phoṭṭhabbaṃ phusati
SOTA = f"người có được thức qua tai là {SAMP}"           # sotaviññāṇasamaṅgī samāpanno (ch19 «người có được thức qua …»)
MANO = "định tâm thuộc về người có được ý thức"          # samādhi manoviññāṇasamaṅgissa (samaṅgissa «người có được»)
MANO2 = f"{MANO}, người có được thức qua tai nghe âm thanh"   # … , sotaviññāṇasamaṅgī saddaṃ suṇāti
TWO = f"có sự tụ hợp của hai sự tiếp xúc{PE} hai tâm"   # Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ (ch15 / ch21)
GAI1 = f"{BH} đã nói rằng đối với tầng thiền thứ nhất, âm thanh là cái gai"   # (ch10 line 218)
GAI2 = (f"{BH} đã nói rằng đối với tầng thiền thứ hai, sự hướng tâm và sự duy trì tâm là cái gai, "
        "người ấy có sự hướng tâm và sự duy trì tâm")
#   Dutiyassa jhānassa vitakko vicāro kaṇṭako vutto bhagavatā, atthi tassa vitakkavicārā (ch10 wording)
GAI_PARTS = ["đối với tầng thiền thứ tư, hơi thở vào và hơi thở ra là cái gai",
             "đối với người đang nhập lĩnh vực không gian vô tận, tri giác về hình sắc là cái gai",
             "đối với người đang nhập lĩnh vực thức vô tận, tri giác về lĩnh vực không gian vô tận là cái gai",
             "đối với người đang nhập lĩnh vực không có gì cả, tri giác về lĩnh vực thức vô tận là cái gai",
             "đối với người đang nhập lĩnh vực không phải tri giác cũng không phải không tri giác, "
             "tri giác về lĩnh vực không có gì cả là cái gai",
             "đối với người đang nhập sự chấm dứt tri giác và cảm giác, tri giác và cảm giác là cái gai"]   # (ch10 line 219)
GAI3 = (f"{BH} đã nói rằng đối với tầng thiền thứ ba, sự hân hoan là cái gai{PE} "
        + f"{PE} ".join(GAI_PARTS) + ", người ấy có tri giác và cảm giác")
#   Tatiyassa jhānassa pīti kaṇṭako…pe… catutthassa … kaṇṭako … ākāsānañcāyatanaṃ … kaṇṭako… … saññāvedayitanirodhaṃ
#   samāpannassa saññā ca vedanā ca kaṇṭako vutto bhagavatā, atthi tassa saññā ca vedanā ca (spaced " … " as the
#   sample / ch10: «…»)

# ---------------------------------------------------------------------------------------------------------------
# (185) Cakkhunā rūpaṃ passati
# ---------------------------------------------------------------------------------------------------------------
RR = "hình sắc bằng vật chất"                           # rūpena rūpaṃ (termbase phrase)
RMV = "vật chất là ý thức"                              # rūpaṃ manoviññāṇaṃ (Rūpaṃ «vật chất», manoviññāṇaṃ «ý thức»)


def avt(x, neg=False):                # (n)atthi X-assa āvaṭṭanā…pe… paṇidhi
    return f"{x} {'không ' if neg else ''}có sự hướng đến{PE} sự mong cầu"


SUT_SEE = (f"“Ở đây, này các tỳ-khưu, vị tỳ-khưu {SEE}{PE} {TOUCH}” "
           f"[{CIT['ma. ni.']} 1.349; {CIT['a. ni.']} 4.37 (cần xem Chú giải)]!")
#   idha, bhikkhave, bhikkhu cakkhunā rūpaṃ passati…pe… kāyena phoṭṭhabbaṃ phusati [… (aṭṭhakathā passitabbā)] (ch15)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười tám"                           # Aṭṭhārasamavaggo (termbase)
KATHA = {1: "thế giới loài người", 2: "việc thuyết giảng Giáo Pháp", 3: KAR, 4: "các loại hương thơm",
         5: "một con đường", 6: "sự chuyển tầng thiền", 7: JA, 8: "việc nghe âm thanh", 9: f"việc {SEE}"}
#   Manussaloka- (termbase), Dhammadesanā- (desanā «việc thuyết giảng»), Karuṇā-, Gandhajāti- (termbase «loại hương
#   thơm»), Ekamagga- (eka «một»), Jhānasaṅkanti- (saṅkanti «sự chuyển»), Jhānantarika- (termbase), Saddaṃ suṇātīti-,
#   Cakkhunā rūpaṃ passatīti- (-ti thesis «việc», ch17 / ch21)
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)
UDDANA = cap(", ".join([T1, T2, T3, T4, T5, T6, T7, T8, SEE, TOUCH])) + "."
#   Buddho bhagavā manussaloke aṭṭhāsi, … samāpanno saddaṃ suṇāti, cakkhunā rūpaṃ passati kāyena phoṭṭhabbaṃ phusati.
#   (no comma in the Pāli between the last two theses: «, » supplied, reported)

REUSED26 = [  # (Pāli, Vietnamese, book)
    ("karuṇāsahagataṃ", "có lòng trắc ẩn đi kèm", "1"), ("mettāsahagataṃ", "có lòng từ ái đi kèm", "1"),
    ("muditāsahagataṃ", "có niềm vui đồng cảm đi kèm", "1"), ("upekkhāsahagatā", "có sự bình thản đi kèm", "1"),
    ("savitakkaṃ savicāraṃ", "có sự hướng tâm và sự duy trì tâm", "1"),
    ("avitakkavicāramattā", "không có sự hướng tâm, chỉ có sự duy trì tâm", "1"),
    ("avitakko avicāro samādhi", "định tâm không có sự hướng tâm cũng không có sự duy trì tâm", "2"),
    ("sappītikā", "có sự hân hoan", "1"), ("sukhasahagatā", "có hạnh phúc đi kèm", "1"),
    ("vivicceva kāmehi", "hoàn toàn tách khỏi các dục lạc", "2"),
    ("catutthaṃ jhānaṃ upasampajja viharati", "chứng nhập và an trú tầng thiền thứ tư", "2"),
    ("nevasaññānāsaññāyatanaṃ", "lĩnh vực không phải tri giác cũng không phải không tri giác", "2"),
    ("saññāvedayitanirodhaṃ", "sự chấm dứt tri giác và cảm giác", "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Lumbiniyā bhagavā jāto … dhammacakkaṃ pavattitaṃ", BIRTH3, "3-brahmacariyakatha.md"),
    ("buddhena bhagavatā (agent)", f"được {BUD} trả lời", "3-brahmacariyakatha.md"),
    ("janapadesu", "các xứ", "3-brahmacariyakatha.md"),
    ("Buddhassa bhagavato", f"của {BUD}", "10-dutiyavaggo.md"),
    ("Atthi keci", "Có phải có ai đó", "10-dutiyavaggo.md"),
    ("dī. ni. (citation)", DN, "8-satipatthanakatha.md"),
    ("jino satthā … dhammappaṭisaraṇo", JINO, "11-tatiyavaggo.md"),
    ("dasasahassilokadhātuṃ", "mười nghìn thế giới", "10-dutiyavaggo.md"),
    ("sāmaññaphalāni", "thành quả của đời sống sa-môn", "4-jahatikatha.md"),
    ("Tiṇṇaṃ phassānaṃ tissannaṃ vedanānaṃ tissannaṃ saññānaṃ … samodhānaṃ hoti",
     "có sự tụ hợp của ba sự tiếp xúc, ba cảm giác, ba tri giác", "4-jahatikatha.md"),
    ("Sotāpattimaggenāti?", "Có phải bằng con đường vào dòng không?", "4-jahatikatha.md"),
    ("Katamena maggenāti?", "Bằng con đường nào?", "4-jahatikatha.md"),
    ("Arahattamaggena sakkāyadiṭṭhiṃ … pajahati", A1, "12-catutthavaggo.md"),
    ("tiṇṇaṃ saṃyojanānaṃ pahānaṃ sotāpattiphalaṃ vuttaṃ bhagavatā", S1, "12-catutthavaggo.md"),
    ("Arahattamaggena oḷārikaṃ kāmarāgaṃ …", A2, "12-catutthavaggo.md"),
    ("kāmarāgabyāpādānaṃ tanubhāvaṃ sakadāgāmiphalaṃ vuttaṃ bhagavatā", S2, "12-catutthavaggo.md"),
    ("Arahattamaggena aṇusahagataṃ kāmarāgaṃ …", A3, "12-catutthavaggo.md"),
    ("kāmarāgabyāpādānaṃ anavasesappahānaṃ anāgāmiphalaṃ vuttaṃ bhagavatā", S3, "12-catutthavaggo.md"),
    ("sakadāgāmi…pe… anāgāmi…pe… arahattamaggaṃ", f"con đường trở lại một lần{PE} con đường không trở lại",
     "21-terasamavaggo.md"),
    ("sāvakā", "các đệ tử", "10-dutiyavaggo.md"),
    ("anadhigato asacchikato", "chưa chứng đắc, chưa tự mình chứng nghiệm", "11-tatiyavaggo.md"),
    ("bodhiyā mūle", "dưới gốc cây Bồ-đề", "12-catutthavaggo.md"),
    ("anupalitto", "Không bị vấy bẩn bởi", "12-catutthavaggo.md"),
    ("āvaṭṭanā ābhogo … paṇidhi", "sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong ước, sự mong cầu",
     "15-sattamavaggo.md"),
    ("atthi tassa āvaṭṭanā…pe… paṇidhī", f"có sự hướng đến{PE} sự mong cầu", "15-sattamavaggo.md"),
    ("Taññeva anāgataṃ taṃ paccuppannaṃ", "chính cái tương lai ấy là cái hiện tại ấy", "5-sabbamatthitikatha.md"),
    ("paccuppanna", "thuộc hiện tại", "5-sabbamatthitikatha.md"),
    ("sarāgo", "có tham đắm", "5-sabbamatthitikatha.md"),
    ("Nanu tayo samādhī vuttā bhagavatā – …", f"Chẳng phải {TAYO} [{DN} 3.305, 353] sao?", "17-navamavaggo.md"),
    ("Hañci tayo samādhī vuttā bhagavatā – …", f"Nếu {TAYO}, thì này bạn", "17-navamavaggo.md"),
    ("Nanu atthi avitakko vicāramatto samādhīti?", f"Chẳng phải có {AV} sao?", "17-navamavaggo.md"),
    ("Cakkhuviññāṇasamaṅgī samāpanno / sotaviññāṇasamaṅgī", "người có được thức qua tai", "19-ekadasamavaggo.md"),
    ("manoviññāṇasamaṅgissa", "người có được ý thức", "18-dasamavaggo.md"),
    ("Dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti", TWO, "15-sattamavaggo.md"),
    ("Nanu paṭhamassa jhānassa saddo kaṇṭako vutto bhagavatāti?", f"Chẳng phải {GAI1}", "10-dutiyavaggo.md"),
    ("Paṭhamassa jhānassa saddo kaṇṭako vutto bhagavatāti, …ti?", f"Có phải nếu {GAI1}, thì", "10-dutiyavaggo.md"),
    ("Dutiyassa jhānassa vitakkavicārā kaṇṭako", f"{BH} đã nói rằng đối với tầng thiền thứ hai, sự hướng tâm và "
     "sự duy trì tâm là cái gai", "10-dutiyavaggo.md"),
    ("tatiyassa jhānassa pīti kaṇṭako", f"{BH} đã nói rằng đối với tầng thiền thứ ba, sự hân hoan là cái gai",
     "10-dutiyavaggo.md"),
] + [("… kaṇṭako (ch10 series)", g, "10-dutiyavaggo.md") for g in GAI_PARTS] + [
    ("atthi tassa saññā ca vedanā cāti", "người ấy có tri giác và cảm giác không?", "10-dutiyavaggo.md"),
    ("cakkhunā rūpaṃ passati, sotena saddaṃ suṇāti, …",
     f"{SEE}, {HEAR}, {SMELL}, {TASTE}, {TOUCH}", "12-catutthavaggo.md"),
    ("idha, bhikkhave, bhikkhu vivicceva kāmehi", "Ở đây, này các tỳ-khưu, vị tỳ-khưu hoàn toàn tách khỏi các dục lạc",
     "21-terasamavaggo.md"),
    ("(aṭṭhakathā passitabbā)", "(cần xem Chú giải)", "15-sattamavaggo.md"),
    ("Samāpanno assādeti (samāpanno)", SAMP, "21-terasamavaggo.md"),
    ("X-kathā («việc» for a -ti thesis)", "Bàn về việc", "21-terasamavaggo.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED26 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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

    heading("5-26-0", 3, VAGGA)

    # ---- (177) 1. Manussalokakathā ----------------------------------------------------------------------------
    heading("5-26-1-0", 4, f"(177) 1. {S.katha(KATHA[1])}")
    add("5-802",
        f"{S.na_vattabbam(T1)} {YES} {NANU(PLACES)} {YES} {S.hanci(PLACES, T1)}",
        f"{S.na_vattabbam(T1)} {YES} {NANU(BIRTH)} {YES} {S.hanci(BIRTH_S, T1)}",
        f"{S.na_vattabbam(T1)} {YES} {S.NANU_VUTTAM} {SUT_PLACES} {S.ATTHEVA} {YES} {S.tena_hi(T1)}")
    add("5-803",
        f"{Q(T1)} {YES} {NANU(WORLD + ' [' + CIT['a. ni.'] + ' 4.36]')} {YES} {S.hanci_neg(WORLD, T1)}",
        S.katha_end(KATHA[1]))

    # ---- (178) 2. Dhammadesanākathā ---------------------------------------------------------------------------
    heading("5-26-2-0", 4, VAGGA)
    heading("5-26-2-1-0", 5, f"(178) 2. {S.katha(KATHA[2])}")
    add("5-804",
        f"{S.na_vattabbam(T2)} {YES} {KENA} Được hóa thân thuyết giảng. {Q('hóa thân là ' + JINO)} {NO_PE}",
        f"{S.na_vattabbam(T2)} {YES} {KENA} Được tôn giả A-nan thuyết giảng. {Q('tôn giả A-nan là ' + JINO)} {NO_PE}")
    add("5-805",
        f"{S.na_vattabbam(T2)} {YES} {S.NANU_VUTTAM} {SARI} {S.ATTHEVA} {YES} {S.tena_hi(T2)}")
    add("5-806",
        f"{S.na_vattabbam(T2)} {YES} {S.NANU_VUTTAM} {SUT_DESANA} {S.ATTHEVA} {YES} {S.tena_hi(T2)}",
        S.katha_end(KATHA[2]))

    # ---- (179) 3. Karuṇākathā ---------------------------------------------------------------------------------
    heading("5-26-3-0", 4, VAGGA)
    heading("5-26-3-1-0", 5, f"(179) 3. {S.katha(KATHA[3])}")
    add("5-807",
        f"{Q(T3)} {YES} {Q(bh(MET, True))} {NO_PE} {q(T3)} {YES} {Q(bh(f'{MUD}{PE} {UPE}', True))} {NO_PE}",
        f"{Q(bh(MET))} {YES} {Q(bh(KAR))} {NO_PE} {q(bh(f'{MUD}{PE} {UPE}'))} {YES} {Q(bh(KAR))} {NO_PE}",
        f"{Q(T3)} {YES} {Q(BH + ' là người không có lòng trắc ẩn')} {NO_PE} {nanu(KARUNIKO)} {YES} "
        f"{pe_end(S.hanci_neg(KARUNIKO, T3))}",
        f"{Q(T3)} {YES} {NANU(MAHAK)} {YES} {S.hanci_neg(MAHAK, T3)}")
    add("5-808",
        f"{Q(bh(KAR))} {YES} {Q(BH + ' có tham đắm')} {NO} {S.tena_hi(T3)}",
        S.katha_end(KATHA[3]))

    # ---- (180) 4. Gandhajātikathā -----------------------------------------------------------------------------
    heading("5-26-4-0", 4, VAGGA)
    heading("5-26-4-1-0", 5, f"(180) 4. {S.katha(KATHA[4])}")
    add("5-809",
        f"{Q(T4)} {YES} {Q(BH + ' là người ăn hương thơm')} {NO_PE} {nanu(ODANA)} {YES} {S.hanci_neg(ODANA, T4)}",
        f"{Q(T4)} {YES} {Q(KECI)} {NO_PE}",
        S.katha_end(KATHA[4]))

    # ---- (181) 5. Ekamaggakathā -------------------------------------------------------------------------------
    heading("5-26-5-0", 4, VAGGA)
    heading("5-26-5-1-0", 5, f"(181) 5. {S.katha(KATHA[5])}")
    add("5-810",
        f"{Q(T5)} {YES} {Q(CATU)} {NO_PE} {q(T5)} {YES} {Q('bằng con đường vào dòng')} {NO_PE} "
        f"{q(f'bằng con đường trở lại một lần{PE} con đường không trở lại')} {NO_PE}",
        f"{KATAMENA} {Q(A1)} {NO_PE} {q(A1)} {YES} {NANU(S1)} {YES} {S.hanci_neg(S1, A1)}",
        f"{Q(A2)} {NO_PE} {q(A2)} {YES} {NANU(S2)} {YES} {S.hanci_neg(S2, A2)}",
        f"{Q(A3)} {NO_PE} {q(A3)} {YES} {NANU(S3)} {YES} {S.hanci_neg(S3, A3)}")
    add("5-811",
        f"{S.na_vattabbam(T5)} {YES} {Q(f'con đường vào dòng đã được {BH} tu tập')} {YES} "
        f"{Q(BH + ' là bậc vào dòng')} {NO_PE} "
        f"{q(f'con đường trở lại một lần{PE} con đường không trở lại đã được {BH} tu tập')} {YES} "
        f"{Q(BH + ' là bậc không trở lại')} {NO_PE}")
    add("5-812",
        f"{Q(f'{BH} {T5}, các đệ tử tự mình chứng nghiệm {FOUR} bằng bốn con đường cao quý')} {YES} "
        f"{Q(SAVAKA)} {NO_PE}",
        S.katha_end(KATHA[5]))

    # ---- (182) 6. Jhānasaṅkantikathā --------------------------------------------------------------------------
    heading("5-26-6-0", 4, VAGGA)
    heading("5-26-6-1-0", 5, f"(182) 6. {S.katha(KATHA[6])}")
    add("5-813",
        f"{Q(T6)} {YES} {Q(sk(1, 3))} {NO_PE} {q(T6)} {YES} {Q(sk(2, 4))} {NO_PE}",
        *sank_block(1, 2, "các dục lạc", "có sự hướng tâm và sự duy trì tâm", True))
    add("5-814", *sank_block(2, 3, "sự hướng tâm và sự duy trì tâm", "có sự hân hoan", False))
    add("5-815", *sank_block(3, 4, "sự hân hoan", "có hạnh phúc đi kèm", False))
    add("5-816",
        f"{S.na_vattabbam(T6)} {YES} {S.NANU_VUTTAM} {SUT_JH} {S.ATTHEVA} {YES} {S.tena_hi(T6)}",
        S.katha_end(KATHA[6]))

    # ---- (183) 7. Jhānantarikakathā ---------------------------------------------------------------------------
    heading("5-26-7-0", 4, VAGGA)
    heading("5-26-7-1-0", 5, f"(183) 7. {S.katha(KATHA[7])}")
    add("5-817",
        f"{Q(T7)} {YES} {Q(f'sự tiếp xúc trung gian tồn tại{PE} tri giác trung gian tồn tại')} {NO_PE}",
        f"{Q(T7)} {YES} {Q(btw(2, 3) + ', ' + T7)} {NO_PE}",
        f"{Q(T7)} {YES} {Q(btw(3, 4) + ', ' + T7)} {NO_PE}",
        f"{Q(btw(2, 3) + ', ' + NT)} {YES} {S.hanci_neg(btw(2, 3) + ', ' + NT, T7)}",
        f"{Q(btw(3, 4) + ', ' + NT)} {YES} {S.hanci_neg(btw(3, 4) + ', ' + NT, T7)}")
    add("5-818",
        f"{Q(btw(1, 2) + ', ' + T7)} {YES} {Q(btw(2, 3) + ', ' + T7)} {NO_PE}",
        f"{Q(btw(1, 2) + ', ' + T7)} {YES} {Q(btw(3, 4) + ', ' + T7)} {NO_PE}",
        f"{Q(btw(2, 3) + ', ' + NT)} {YES} {Q(btw(1, 2) + ', ' + NT)} {NO_PE}",
        f"{Q(btw(3, 4) + ', ' + NT)} {YES} {Q(btw(1, 2) + ', ' + NT)} {NO_PE}")
    add("5-819",
        f"{Q(is_ja(AV))} {YES} {Q(is_ja(SV))} {NO_PE}",
        f"{Q(is_ja(AV))} {YES} {Q(is_ja(AA))} {NO_PE}",
        f"{Q(is_ja(SV, True))} {YES} {Q(is_ja(AV, True))} {NO_PE}",
        f"{Q(is_ja(AA, True))} {YES} {Q(is_ja(AV, True))} {NO_PE}")
    add("5-820",
        f"{Q(f'{TWO_PRESENT} có {AV}')} {YES} {NANU(VATT)} {YES} "
        f"{S.hanci_neg(VATT, f'{TWO_PRESENT}, {is_ja(AV)}')}")
    add("5-821",
        f"{Q(is_ja(AV, True))} {YES} "
        f"{Q(f'{AV} là tầng thiền thứ nhất{PE} tầng thiền thứ hai{PE} tầng thiền thứ ba{PE} tầng thiền thứ tư')} "
        f"{NO} {S.tena_hi(is_ja(AV))}")
    add("5-822",
        f"{Q(is_ja(AV))} {YES} {NANU(f'{TAYO} [{DN} 3.305, 353]')} {YES} {S.hanci_neg(TAYO_S, is_ja(AV))}",
        S.katha_end(KATHA[7]))

    # ---- (184) 8. Saddaṃ suṇātītikathā ------------------------------------------------------------------------
    heading("5-26-8-0", 4, VAGGA)
    heading("5-26-8-1-0", 5, f"(184) 8. {S.katha(KATHA[8])}")
    add("5-823",
        f"{Q(T8)} {YES} {Q(SENSES)} {NO_PE}",
        f"{Q(T8)} {YES} {Q(SOTA)} {NO} {NANU(MANO)} {YES} {S.hanci_neg(MANO, T8)}",
        f"{Q(MANO2)} {YES} {S.hanci_neg(MANO2, T8)} {Q(MANO2)} {YES} {Q(TWO)} {NO_PE}")
    add("5-824",
        f"{S.na_vattabbam(T8)} {YES} {NANU(GAI1)} {YES} {S.hanci(GAI1, T8)}")
    add("5-825",
        f"{S.neu(GAI1, T8)} {YES} {Q(GAI2)} {NO_PE}",
        f"{S.neu(GAI1, T8)} {YES} {Q(GAI3)} {NO_PE}",
        S.katha_end(KATHA[8]))

    # ---- (185) 9. Cakkhunā rūpaṃ passatītikathā ---------------------------------------------------------------
    heading("5-26-9-0", 4, VAGGA)
    heading("5-26-9-1-0", 5, f"(185) 9. {S.katha(KATHA[9])}")
    add("5-826",
        f"{Q(SEE)} {YES} {Q('thấy ' + RR)} {NO_PE} {q('thấy ' + RR)} {YES} {Q('nhận biết rõ ' + RR)} {NO_PE} "
        f"{q('nhận biết rõ ' + RR)} {YES} {Q(RMV)} {NO_PE} {q(SEE)} {YES} {Q(avt('mắt'))} {NO_PE} "
        f"{nanu(avt('mắt', True))} {YES} {S.hanci_neg(avt('mắt', True), SEE)}",
        f"{Q(f'{HEAR}{PE} {SMELL}{PE} {TASTE}{PE} {TOUCH}')} {YES} {Q('chạm vào ' + RR)} {NO_PE}",
        f"{Q('chạm vào ' + RR)} {YES} {Q('nhận biết rõ ' + RR)} {NO_PE} {q('nhận biết rõ ' + RR)} {YES} "
        f"{Q(RMV)} {NO_PE} {q(TOUCH)} {YES} {Q(avt('thân'))} {NO_PE} {nanu(avt('thân', True))} {YES} "
        f"{pe_end(S.hanci_neg(avt('thân', True), TOUCH))}")
    add("5-827",
        f"Có phải không nên nói – “{SEE}”{PE} “{TOUCH}” không? {YES} {S.NANU_VUTTAM} {SUT_SEE} {S.ATTHEVA} {YES} "
        f"{S.tena_hi(f'{SEE}{PE} {TOUCH}')}",
        S.katha_end(KATHA[9]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Lookup helper (finished pi-5 rails chapters only)
# ---------------------------------------------------------------------------------------------------------------
def _lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def find(pat, maxhits=8, maxc=700, ctx=100):
    rx = re.compile(pat)
    hits = 0
    for name in FINISHED:
        pl, vl = _lines(S.PALI_DIR / name), _lines(S.OUT_DIR / name)
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if not m:
                continue
            s = max(0, m.start() - ctx)
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
    for bad in ("là là", "được được"):
        assert bad not in text, bad
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-26"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "find":
        find(sys.argv[2], *(int(x) for x in sys.argv[3:]))
    else:
        main()
