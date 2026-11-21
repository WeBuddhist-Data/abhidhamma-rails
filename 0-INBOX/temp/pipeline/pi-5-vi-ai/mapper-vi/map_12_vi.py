"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 12: 12-catutthavaggo.

usage: python -I -X utf8 -B map_12_vi.py                  (writes 12-catutthavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_12_vi.py show lo hi        (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T12, text) of map_sample_vi (T12 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-12.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "12-catutthavaggo"

_ARA = "bậc A-la-hán"
_ANA = "bậc không trở lại"
_SAK = "bậc trở lại một lần"
_SOT = "bậc vào dòng"
_KA = "không phải là đối tượng của ô nhiễm"       # anāsava (pi-1 MATRIX anāsavā)
_SA = "đối tượng của ô nhiễm"                      # sāsava (bare adjective: leading «là» dropped, pi-1)
_TB = "được trang bị"                              # samannāgato (pi-4)
_GN = "bậc giác ngộ"                               # buddho (Bodhiyā buddho «là bậc giác ngộ nhờ sự giác ngộ»)
_SG = "sự giác ngộ"                                # bodhi
_BT = "Bồ-tát"
_CĐ = "đã bước vào sự cố định"                     # okkantaniyāmo
_TH = "đã sống đời sống tu hành trong sạch"        # caritabrahmacariyo
_TTA = "tự mình chứng nghiệm trạng thái A-la-hán"  # arahattasacchikiriyāya (notes-map-3)
_TQA = "tự mình chứng nghiệm thành quả không trở lại"
_TQS = "tự mình chứng nghiệm thành quả trở lại một lần"
_NT = "người đang thực hành"                       # paṭipanno puggalo (pi-4)
_VK = "chuyển luân"

T12 = {
    # ---- headings «Chương thứ tư», «Bàn về …»; closers «Phần bàn về … đã hoàn tất.»; «Chương thứ tư.»
    "catutthavaggo": "Chương thứ tư",              # line-initial capital kept (notes-map-9 Upalabbho)
    "gihissa": "người tại gia",                    # Gihissa arahā «người tại gia là bậc A-la-hán»
    "gihi": "người tại gia",                       # gihisaṃyojanaṃ / gihibyañjanena (member)
    "upapatti": "sự tái sinh",                     # Upapattikathā «Bàn về sự tái sinh» (the text's «sự»)
    "anāsava": _KA,                                # Anāsavakathā «Bàn về những gì không phải là đối tượng của ô nhiễm»
    "samannāgata": "sự được trang bị",             # Samannāgatakathā «Bàn về sự được trang bị»
    "bodhiyā": _SG, "bodhīhi": _SG,                # «nhờ sự giác ngộ», «nhờ ba sự giác ngộ» (5-403 «cây Bồ-đề»: override)
    "buddho": _GN,                                 # (5-403 «trở thành Đức Phật»: override)
    "bodhiyā buddho": _GN + " nhờ " + _SG,         # Vietnamese order, inner «nhờ» kept (pi-4 «… để …»)
    "lakkhaṇa": "tướng",                           # Lakkhaṇakathā «Bàn về các tướng» («các» dropped; not KV «đặc tính»)
    "lakkhaṇāni": "tướng",                         # mahāpurisalakkhaṇāni «tướng đại nhân»
    "niyāma": "sự cố định", "niyāmo": "sự cố định",
    "okkanti": "việc bước vào", "niyāmokkanti": "việc bước vào sự cố định",
    "niyāmokkantikathā": "Bàn về việc bước vào sự cố định",   # whole heading (sample paṭivedhānuyogo)
    "pahāna": "sự dứt bỏ",                         # Sabbasaṃyojanappahānakathā «Bàn về sự dứt bỏ tất cả các xiềng xích»
    # ---- 5-387 Gihissa arahā
    "pahīnaṃ": "đã được dứt bỏ",                   # notes-map-2 pahīno / pahīnā
    "pahāya": "dứt bỏ",                            # of appahāya «chưa dứt bỏ» (positive part)
    "uppāda": "nảy sinh",                          # anuppādadhammaṃ «có bản chất không nảy sinh» (notes-map-2)
    "anabhāvaṅkataṃ": "đã bị làm cho không còn hiện hữu",   # notes-map-2 anabhāvaṅkato
    "tāla": "cây thốt nốt", "vatthu": "ngọn", "mūlaṃ": "gốc",   # notes-map-2 (tālāvatthukataṃ, ucchinnamūlaṃ)
    "gihisaṃyojanaṃ": "xiềng xích của người tại gia",   # head noun before its genitive
    "dhamme": "đời",                               # diṭṭheva dhamme «ngay trong đời này»
    "dukkhassantakaro": "người đi đến tận cùng của khổ đau",   # notes-map-4 karo
    "antakaro": "người đi đến tận cùng",
    "vacchagotto": "Vác-cha-gốt-ta", "vaccha": "Vác-cha", "paribbājako": "du sĩ",
    "bho": "Thưa ông", "gotama": "Cồ-đàm",         # bho gotama «Thưa ông Cồ-đàm»
    "kāyassa": "thân", "bhedā": "tan rã",          # kāyassa bhedā «khi thân tan rã»
    # optatives: the verb as written («có thể» = the mood frame, as pi-4 jāneyya «biết»)
    "methunaṃ dhammaṃ": "hành vi dâm dục", "methunaṃ": "dâm dục",   # first; CROSSCHECK «sự giao hợp»
    "paṭiseveyya": "hưởng thụ", "uppādeyya": "làm phát sinh",
    "putta": "con cái", "sambādha": "chật chội", "sayanaṃ": "chiếc giường",   # «chiếc giường chật chội vì con cái»
    "ajjhāvaseyya": "sống",
    "kāsikacandanaṃ": "gỗ đàn hương xứ Ca-thi", "candanaṃ": "gỗ đàn hương", "paccanubhaveyya": "thụ hưởng",
    "mālā": "vòng hoa", "gandha": "hương thơm", "vilepanaṃ": "dầu thoa",
    "dhāreyya": "mang",                            # first («có thể mang vòng hoa»); CROSSCHECK «mặc»
    "rajataṃ": "bạc", "aja": "dê", "eḷakaṃ": "cừu", "kukkuṭa": "gà", "sūkaraṃ": "heo",
    "paṭiggaṇheyya": "nhận",
    "hatthi": "voi", "gava": "bò", "assa": "ngựa đực", "vaḷavaṃ": "ngựa cái",   # (5-402 assaratanaṃ: override)
    "tittira": "chim đa đa", "vaṭṭaka": "chim cút", "mora": "chim công", "kapiñjaraṃ": "chim trĩ",
    "tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya": "nhận chim đa đa chim cút chim công và chim trĩ",   # commas
                                                   # dropped (pi-1)
    "citta": "nhiều màu", "vāla": "tóc", "moḷiṃ": "búi tóc",   # cittavaṇḍavālamoḷiṃ «búi tóc có trang sức nhiều
                                                   # màu» (vāla 'hair' = the «tóc» of «búi tóc»; unclear)
    "odātāni": "trắng", "vatthāni": "tấm vải", "dasāni": "viền",   # «những tấm vải trắng có viền dài»
    "yāvajīvaṃ": "suốt đời",
    "yaso": "Da-xá", "kula": "nhà gia giáo", "putto": "người con",   # kulaputto «người con nhà gia giáo»
    "uttiyo": "Út-ti-da", "setu": "Sê-tu", "māṇavo": "thanh niên",
    "byañjanena": "hình tướng",                    # gihibyañjanena «với hình tướng người tại gia»
    "arahattaṃ": "trạng thái A-la-hán",
    "patto": "đã đạt đến",                         # «đã đạt đến trạng thái A-la-hán» (notes-map-3 arahattappatto)
    # ---- 5-388 … 5-390 Upapattikathā «là bậc A-la-hán ngay khi tái sinh»
    "saha": "ngay khi", "upapattiyā": "tái sinh", "saha upapattiyā": "ngay khi tái sinh",
    "sotāpanno": _SOT, "sakadāgāmī": _SAK, "anāgāmī": _ANA, "arahā": _ARA,
    "thero": "trưởng lão",                         # map_2_vi
    "sāriputto thero": "trưởng lão Xá-lợi-phất", "mahāpanthako thero": "trưởng lão Đại Bàn-đặc",
    "upapattesiyena": "tìm cầu sự tái sinh", "upapattesiyena cittena": "tâm tìm cầu sự tái sinh",
    "cittena": "tâm",
    "lokiyena": "thuộc thế gian", "sāsavena": _SA, "saṃkilesiyena": "đối tượng của phiền não",
    "āsavena": "ô nhiễm",                          # member of sāsavena
    "niyyānikaṃ": "dẫn đến giải thoát",
    "khaya": "sự diệt tận", "bodha": "sự giác ngộ", "apacaya": "sự giảm trừ",   # notes-map-4 (…gāmī «dẫn đến sự …»)
    "anāsavaṃ": _KA, "anāsavā": _KA, "anāsavo": _KA, "sāsavaṃ": _SA,
    "rāgaṃ": "sự tham đắm", "dosaṃ": "sự sân hận", "mohaṃ": "sự si mê",
    "anottappaṃ": "sự không biết ghê sợ tội lỗi", "ottappaṃ": "biết ghê sợ tội lỗi",   # notes-map-2
    "pajahati": "dứt bỏ", "rāgaṃ pajahati": "dứt bỏ sự tham đắm",
    "maggo": "con đường",
    "satipaṭṭhānaṃ": "sự thiết lập tỉnh thức", "paṭṭhānaṃ": "sự thiết lập", "sati": "tỉnh thức",   # notes-map-8
    "padhānaṃ": "nỗ lực",                          # sammappadhānaṃ «nỗ lực đúng đắn» (sammā: context5)
    "iddhi": "thần thông", "indriyaṃ": "năng lực", "balaṃ": "sức mạnh",
    "bojjhaṅgo": "chi phần giác ngộ", "bojjha": "giác ngộ", "aṅgo": "chi phần",
    "parijānāti": "hiểu biết trọn vẹn", "dukkhaṃ parijānāti": "hiểu biết trọn vẹn khổ đau",
    "samudayaṃ": "sự phát sinh", "nirodhaṃ": "sự chấm dứt", "sacchikaroti": "tự mình chứng nghiệm",
    "bhāveti": "tu tập", "maggaṃ bhāveti": "tu tập con đường", "maggaṃ": "con đường",
    "cuti": "lúc chết",                            # cuticittaṃ «tâm lúc chết»
    "phala": "thành quả",                          # phalacittaṃ «tâm thành quả»; anāgāmiphalasacchikiriyāya
    # ---- 5-391 … 5-392 Anāsavakathā
    "arahato": _ARA, "arahato anāsavā": _ARA + " " + _KA,
    "kāyo": "thân", "kāyo anāsavo": "thân" + GAP + _KA,
    "arahatta": "trạng thái A-la-hán",             # context: «A-la-hán» in arahattamaggo / -phalaṃ (resolver)
    "arahattamaggo": "con đường A-la-hán", "arahattaphalaṃ": "thành quả A-la-hán",
    "arahattamaggena": "con đường A-la-hán", "maggena": "con đường",
    "anāgāmimaggo": "con đường không trở lại", "sakadāgāmimaggo": "con đường trở lại một lần",
    "sotāpattimaggo": "con đường vào dòng",
    "anāgāmimaggaṃ": "con đường không trở lại", "sakadāgāmimaggaṃ": "con đường trở lại một lần",
    "sotāpattimaggaṃ": "con đường vào dòng",
    "phalaṃ": "thành quả", "phalāni": "thành quả", "phalena": "thành quả", "phalehi": "thành quả",
    "anāgāmiphalaṃ": "thành quả không trở lại", "sakadāgāmiphalaṃ": "thành quả trở lại một lần",
    "sotāpattiphalaṃ": "thành quả vào dòng",
    "anāgāmiphalena": "thành quả không trở lại", "sakadāgāmiphalena": "thành quả trở lại một lần",
    "sotāpattiphalena": "thành quả vào dòng",
    "anāgāmiphala": "thành quả không trở lại", "sakadāgāmiphala": "thành quả trở lại một lần",
    "anāgāmi": "không trở lại", "sakadāgāmi": "trở lại một lần", "sotāpatti": "vào dòng",   # members
    "cakkhuṃ": "mắt", "sotaṃ": "tai", "ghānaṃ": "mũi", "jivhā": "lưỡi",   # (5-405 «con mắt»: override)
    "dhammā": "hiện tượng",
    # 5-391 body string (map_5_vi T5)
    "chedana": "bị cắt", "bhedana": "bị đập vỡ", "sādhāraṇo": "thứ chung",
    "kākehi": "quạ", "gijjhehi": "kền kền", "kulalehi": "diều hâu",
    "kameyya": "tác động",                         # «có thể tác động» (optative: «có thể» = the mood frame)
    "visaṃ": "chất độc", "satthaṃ": "dao kiếm", "aggi": "lửa",
    "bandhituṃ": "trói", "bandhanena": "sự giam giữ", "bandhanehi": "dây trói",
    "addu": "cùm", "rajju": "dây thừng", "saṅkhalika": "xích sắt",
    "gāma": "làng", "nigama": "thị trấn", "nagara": "thành phố", "kaṇṭha": "cổ", "pañcamehi": "thứ năm",
    # 5-392 «nếu bậc A-la-hán cho người phàm phu y phục … đồ ăn khất thực, … chỗ ở, … thuốc men và vật dụng chữa
    # bệnh, thì không phải là đối tượng của ô nhiễm rồi trở thành đối tượng của ô nhiễm … chính cái ấy …»
    "deti": "cho", "cīvaraṃ": "y phục", "piṇḍapātaṃ": "đồ ăn khất thực", "senāsanaṃ": "chỗ ở",
    "gilāna": "bệnh", "bhesajja": "thuốc men", "parikkhāraṃ": "vật dụng",
    "puthu": "phàm phu", "janassa": "người", "puthujjanassa": "người phàm phu",   # notes-map-4
    "puthujjano deti": "người phàm phu cho",
    "āsavaṃ": "ô nhiễm",                           # member of sāsavaṃ / anāsavaṃ
    "taññeva": "chính cái ấy",
    "anāsavaṃ taṃ sāsavaṃ": _KA + " cái ấy là " + _SA,   # comma dropped, inner «là» kept
    "sāsavaṃ taṃ anāsavaṃ": _SA + " cái ấy " + _KA,
    "rāgo": "sự tham đắm", "doso": "sự sân hận", "moho": "sự si mê",
    "arahā anāsavo": _ARA + " " + _KA,
    # ---- 5-393 … 5-397 Samannāgatakathā / Upekkhāsamannāgatakathā «bậc A-la-hán được trang bị bốn thành quả»
    "samannāgato": _TB,
    "arahā samannāgato": _ARA + " " + _TB, "anāgāmī samannāgato": _ANA + " " + _TB,
    "sakadāgāmī samannāgato": _SAK + " " + _TB,
    "phassehi": "sự tiếp xúc", "vedanāhi": "cảm giác", "saññāhi": "tri giác", "cetanāhi": "chủ ý",
    "cittehi": "tâm", "saddhāhi": "niềm tin", "satīhi": "sự tỉnh thức", "samādhīhi": "sự định tâm",
    "paññāhi": "trí tuệ", "upekkhāhi": "sự bình thản",
    "kolaṅkolo": "người đi từ gia đình này sang gia đình khác",
    "ekabījī": "người có một hạt giống", "eka": "một", "bījī": "hạt giống",
    "parinibbāyī": "nhập Niết-bàn trọn vẹn",       # member (notes-map-3 parinibbāyi)
    "upahacca": "khi gần mạng chung",              # pi-4
    "saṅkhāra": "sự thúc đẩy", "uddhaṃsoto": "người theo dòng đi lên", "gāmī": "đến",   # notes-map-3
    "akaniṭṭha": "cõi Sắc Cứu Cánh",               # pi-4
    "vītivatto": "đã vượt qua",
    "sakkāyadiṭṭhiṃ": "quan điểm về tự ngã", "sakkāya": "tự ngã", "diṭṭhiṃ": "quan điểm",
    "vicikicchaṃ": "sự hoài nghi", "parāmāsaṃ": "sự hiểu sai lệch",
    "sīlabbataparāmāsaṃ": "sự hiểu sai lệch về giới hạnh và nghi thức",
    "sīla": "giới hạnh", "sīlabbata": "giới hạnh và nghi thức",
    "apāya": "cõi khổ", "gamanīyaṃ": "dẫn đến",    # map_2_vi
    "oḷārikaṃ": "ở dạng thô", "oḷārikaṃ byāpādaṃ": "ác ý ở dạng thô", "byāpādaṃ": "ác ý", "aṇu": "nhỏ nhiệm",
    "kāma": "dục lạc", "kāmarāgaṃ": "sự tham đắm dục lạc",
    "parihīno": "sa sút",                          # of aparihīno «không sa sút» (positive part)
    "paṭiladdhāni": "đã có được", "paṭiladdhaṃ": "đã có được",
    "tīṇi phalāni paṭiladdhāni": "đã có được ba thành quả",   # keyword with its numeral keeps it (pi-3)
    "dve phalāni paṭiladdhāni": "đã có được hai thành quả",
    "sotāpattiphalaṃ paṭiladdhaṃ": "đã có được thành quả vào dòng",
    "maggā": "con đường",
    "satataṃ": "thường xuyên", "samitaṃ": "liên tục", "abbokiṇṇaṃ": "liền mạch", "samohito": "được kết hợp",
    "cakkhunā": "mắt",                             # «bằng mắt» (sample «nhãn» only in dibbena cakkhunā)
    "sotena": "tai", "ghānena": "mũi", "jivhāya": "lưỡi", "kāyena": "thân", "manasā": "ý",
    "rūpaṃ": "hình sắc", "saddaṃ": "âm thanh", "phoṭṭhabbaṃ": "vật xúc chạm", "dhammaṃ": "đối tượng của ý",
    "passanto": "trong khi thấy", "vijānanto": "trong khi nhận biết",   # participles keep «trong khi» (map 4)
    "suṇāti": "nghe", "ghāyati": "ngửi", "sāyati": "nếm", "phusati": "chạm", "vijānāti": "nhận biết",
    "upekkho": "có sự bình thản", "aṅga": "phương diện",   # chaḷaṅgupekkho «có sự bình thản ở sáu phương diện»
    # ---- 5-398 / 5-399 Bodhiyā buddho
    "niruddhāya": "đã chấm dứt", "vigatāya": "đã mất đi", "paṭipassaddhāya": "đã an tịnh",
    "atītāya bodhiyā": _SG + " thuộc quá khứ", "anāgatāya bodhiyā": _SG + " thuộc tương lai",
    "paccuppannāya bodhiyā": _SG + " thuộc hiện tại",
    "atītāya buddho": _GN + GAP + "thuộc quá khứ", "anāgatāya buddho": _GN + GAP + "thuộc tương lai",
    "paccuppannāya buddho": _GN + GAP + "thuộc hiện tại",
    "bodhiyā bodhikaraṇīyaṃ": _SG + GAP + "việc của " + _SG,   # as map_5_vi ñāṇena ñāṇakaraṇīyaṃ
    "dukkhaṃ": "khổ đau",
    "bodhiyo paccupaṭṭhitā": _SG + " hiện diện",
    "paṭilābhā": "có được", "bodhipaṭilābhā": "có được " + _SG,
    "bodhipaṭilābhā buddho": _GN + " nhờ có được " + _SG,
    # ---- 5-400 … 5-402 Lakkhaṇakathā «người được trang bị các tướng là Bồ-tát»
    "bodhisatto": _BT, "bodhisattassa": _BT,
    "lakkhaṇasamannāgato bodhisatto": "người được trang bị các tướng là " + _BT,   # inner «các» / «là» kept
    "padesa": "một phần",
    "cakkavattisatto": "người làm vua " + _VK, "cakkavattisattassa": "người làm vua " + _VK,
    "cakkavatti": "vua " + _VK,
    "cakkavattī": "vị vua " + _VK,                 # rājā hoti cakkavattī «trở thành vua, vị vua chuyển luân»
    "pubba": "trước đây", "yogo": "sự tu tập", "cariyā": "hạnh kiểm",
    "dhamma": "Giáo Pháp", "akkhānaṃ": "việc giảng nói", "desanā": "việc thuyết giảng",   # (5-402: override)
    # 5-401 the birth wonders
    "jāyamānassa": "khi" + GAP + "đang ra đời",    # participle keeps «khi»
    "devā": "chư thiên", "paṭiggaṇhanti": "đón nhận", "pacchā": "sau", "manussā": "loài người",
    "dissāya": "sau khi thấy", "pucchati": "hỏi",  # editorial «[…, hỏi sau khi thấy điều đã được nói]»
    "devaputtā": "vị thiên tử", "mātu": "người mẹ", "devi": "hoàng hậu",   # «Thưa» = the vocative frame
    "attamanā": "hài lòng", "mahesakkho": "có uy lực lớn",
    "udakassa": "nước", "dhārā": "dòng", "antalikkhā": "không trung", "pātubhavanti": "hiện ra",
    "sītassa": "lạnh", "uṇhassa": "nóng", "udakakiccaṃ": "việc dùng nước",
    "sampati": "vừa mới", "pādehi": "bàn chân", "patiṭṭhahitvā": "đứng vững",   # no «sau khi» in the text
    "abhimukho": "hướng mặt về", "pada": "bước", "gacchati": "bước đi",
    "setamhi": "trắng", "chatte": "chiếc lọng", "disā": "phương", "viloketi": "nhìn khắp",
    "āsabhiṃ": "hùng dũng", "vācaṃ": "lời nói", "bhāsati": "nói lên",
    "aggo": "bậc cao nhất", "jeṭṭho": "bậc lớn nhất", "seṭṭho": "bậc tối thắng",
    "jāti": "lần sinh", "puna": "mới", "bhavo": "sự hiện hữu",   # punabbhavo «sự hiện hữu mới» (ch4)
    "ālokassa": "ánh sáng", "obhāsassa": "hào quang", "bhūmi": "mặt đất", "cālassa": "sự rung chuyển",
    "pakati": "bình thường", "byāmaṃ": "sải tay", "obhāsati": "tỏa sáng", "supinaṃ": "giấc mộng",
    # 5-402 the sutta of the 32 marks
    "dvattiṃsa": "ba mươi hai", "purisassa": "bậc đại nhân",   # mahāpurisassa «của bậc đại nhân»
    "gatiyo": "hướng đi", "agāraṃ": "gia đình", "ajjhāvasati": "sống",   # first; CROSSCHECK «cai quản»
    "rājā": "vua", "dhammiko": "theo lẽ phải", "dhammarājā": "vị vua của lẽ phải", "anto": "phương",
    "vijitāvī": "người chiến thắng", "thāvariya": "sự ổn định",   # patto «đã đạt được»: override
    "ratanaṃ": "báu vật", "ratanāni": "báu vật", "sattamaṃ": "thứ bảy",
    "cakka": "bánh xe", "maṇi": "ngọc", "itthi": "người nữ", "gahapati": "gia chủ",
    "pariṇāyaka": "vị cố vấn",                     # notes-map-8
    "sahassaṃ": "nghìn", "puttā": "người con", "sūrā": "can đảm", "vīra": "bậc anh hùng", "rūpā": "thân hình",
    "sena": "quân", "para": "địch", "pamaddanā": "đánh tan",   # parasenappamaddanā «đánh tan quân địch»
    "pathaviṃ": "trái đất", "sāgara": "biển cả", "pariyantaṃ": "đến tận",
    "daṇḍena": "gậy", "satthena": "dao kiếm",      # of adaṇḍena / asatthena «không dùng gậy / dao kiếm» (positive part)
    "dhammena": "lẽ phải", "abhivijiya": "chinh phục",
    "anagāriyaṃ": "đời không gia đình", "pabbajati": "xuất gia",   # notes-map-3
    "arahaṃ": _ARA, "sambuddho": "bậc Tự Giác Ngộ",
    "vivaṭṭa": "đã vén", "chado": "bức màn che",   # vivaṭṭacchado «đã vén bức màn che»
    # ---- 5-403 … 5-405 Niyāmokkantikathā «Bồ-tát, trong lời dạy của Đức Thế Tôn Ca-diếp, đã bước vào sự cố định,
    # đã sống đời sống tu hành trong sạch»
    "bhagavato": "Đức Thế Tôn",                    # pi-1 (KV «Thế Tôn» only in «Đức Phật Thế Tôn»)
    "kassapassa": "Ca-diếp", "kassapassa bhagavato": "Đức Thế Tôn Ca-diếp",
    "pāvacane": "lời dạy",
    "okkanta": "đã bước vào", "okkantaniyāmo": _CĐ,   # bodhisatto okkantaniyāmo: context12
    "carita": "đã sống", "cariyo": "đời sống tu hành", "brahma": "trong sạch",   # notes-map-3
    "brahmacariyo": "đời sống tu hành trong sạch", "caritabrahmacariyo": _TH,
    "suttaṃ": "Kinh",                              # ghaṭikārasuttaṃ «Kinh Ga-ti-ka-ra»
    "sāvako": "đệ tử", "bodhisatto sāvako": _BT + " là đệ tử",   # inner «là» kept
    "anussaviyo": "người hiểu biết nhờ nghe từ người khác",
    "sayambhū": "bậc tự mình giác ngộ", "bhagavā sayambhū": "Đức Thế Tôn là bậc tự mình giác ngộ",
    "mūle": "gốc",                                 # bodhiyā mūle «dưới gốc cây Bồ-đề» (map_3_vi)
    "sāmañña": "đời sống sa-môn", "abhisambuddhāni": "đã giác ngộ hoàn toàn",
    "bhagavatā abhisambuddhāni": "Đức Thế Tôn" + GAP + "đã giác ngộ hoàn toàn",
    # 5-404
    "akāsi": "đã làm", "bodhisatto akāsi": _BT + " đã làm",
    "dukkara": "khó làm", "kāriyaṃ": "việc khổ hạnh", "dukkarakāriyaṃ": "việc khổ hạnh khó làm",
    "dassana": "sự thấy", "sampanno": "thành tựu", "puggalo": "người",
    "dassanasampanno puggalo": "người thành tựu về sự thấy",   # inner «về» kept
    "tapaṃ": "khổ hạnh", "satthāraṃ": "bậc đạo sư", "uddisi": "đã tôn xưng",
    "āyasmā": "tôn giả", "āyasmā ānando": "tôn giả A-nan",
    "ānando okkantaniyāmo": "A-nan" + GAP + _CĐ,
    "citto": "Chít-ta", "hatthako": "Hát-tha-ka",  # names (not KV hatthako «bàn tay»)
    "hatthako āḷavako": "Hát-tha-ka người xứ A-la-vi",
    "āḷavako okkantaniyāmo": "người xứ A-la-vi" + GAP + _CĐ,
    "jātiṃ": "lần sinh",
    # 5-405 «Này A-nan, Ta đã sống đời sống tu hành trong sạch nơi Đức Thế Tôn Ca-diếp vì sự giác ngộ trọn vẹn trong
    # tương lai»; the verses to Upaka; the Dhammacakka quote
    "sambodhāya": "sự giác ngộ trọn vẹn",
    "abhibhū": "bậc chiến thắng", "vidū": "bậc biết",   # sabbābhibhū «bậc chiến thắng tất cả», sabbavidū «bậc biết …»
    "dhammesu": "hiện tượng",                      # first «giữa tất cả các hiện tượng»; CROSSCHECK «điều» (ananussutesu)
    "anupalitto": "không bị vấy bẩn",
    "taṇha": "khao khát", "khaye": "sự diệt tận", "vimutto": "được giải thoát",
    "sayaṃ": "tự mình", "abhiññāya": "sau khi" + GAP + "hiểu biết trực tiếp",   # «Sau khi tự mình hiểu biết trực tiếp»
    "ācariyo": "thầy", "sadiso": "người giống như", "vijjati": "hiện hữu",   # na vijjati «không hiện hữu»
    "devakasmiṃ": "chư thiên",                     # sadevakasmiṃ «cùng với chư thiên» (sa- «cùng với»)
    "paṭipuggalo": "ai sánh ngang",
    "anuttaro": "không có ai cao hơn", "eko": "duy nhất",
    "sītibhūto": "đã trở nên mát mẻ", "nibbuto": "đã lắng dịu",
    "cakkaṃ": "bánh xe", "pavattetuṃ": "chuyển", "gacchāmi": "đi đến", "puraṃ": "thành",
    "andhībhūtasmiṃ": "đã trở nên mù lòa", "āhañchaṃ": "sẽ đánh", "amata": "bất tử", "dundubhiṃ": "tiếng trống",
    "dudrabhinti": NDE,                            # only in the bracket [khác chính tả (Ka.): dudrabhinti]
    "āvuso": "hiền giả", "paṭijānāsi": "tự nhận", "ananta": "vô biên",
    "jino": "bậc chiến thắng", "jinā": "bậc chiến thắng",   # «những bậc chiến thắng» («những» dropped)
    "mādisā": "người như Ta", "ve": "quả thật", "āsava": "ô nhiễm",
    "jitā": "đã bị" + GAP + "chiến thắng", "pāpakā": "xấu ác", "tasmā": "vì vậy", "upaka": "U-pa-ka",
    "ariya": "cao quý", "ariyasaccaṃ": "sự thật cao quý", "sacca": "sự thật",
    "dukkhaṃ ariyasaccaṃ": "sự thật cao quý về khổ đau",   # inner «về» kept
    "anussutesu": "được nghe",                     # of ananussutesu «chưa từng được nghe» (pi-4)
    "udapādi": "đã khởi lên", "ñāṇaṃ": "hiểu biết", "paññā": "trí tuệ", "vijjā": "hiểu biết chân thật",
    "āloko": "ánh sáng",
    "pariññeyyaṃ": "cần được hiểu biết trọn vẹn", "pahātabbaṃ": "cần dứt bỏ",
    "sacchikātabbaṃ": "cần được tự mình chứng nghiệm", "bhāvetabbaṃ": "cần được tu tập",
    "dukkhasamudayaṃ": "sự phát sinh của khổ đau", "dukkhanirodhaṃ": "sự chấm dứt khổ đau",
    "dukkhasamudayo": NDE, "dukkhanirodho": NDE,   # only in the brackets [khác chính tả (Syā., Kaṃ.): …]
    # ---- 5-406 … 5-412 Aparāpi samannāgatakathā «người đang thực hành để tự mình chứng nghiệm …»
    "paṭipanno puggalo": _NT, "paṭipannena puggalena": _NT, "paṭipanno": "đang thực hành",
    "paṭipannena": "đang thực hành", "puggalena": "người",
    "sacchikiriyāya": "tự mình chứng nghiệm", "arahattasacchikiriyāya": _TTA,
    "arahattasacchikiriyāya samannāgato": _TTA + GAP + _TB,
    "anāgāmiphalasacchikiriyāya samannāgato": _TQA + GAP + _TB,
    "sakadāgāmiphalasacchikiriyāya samannāgato": _TQS + GAP + _TB,
    # ---- 5-413 … 5-417 Sabbasaṃyojanappahānakathā
    "pahīyanti": "được dứt bỏ", "saṃyojanā pahīyanti": "xiềng xích được dứt bỏ", "saṃyojanā": "xiềng xích",
    "saṃyojanānaṃ": "xiềng xích", "pahānaṃ": "sự dứt bỏ", "pahīnā": "đã được dứt bỏ",
    "vuttaṃ bhagavatā": "Đức Thế Tôn đã nói", "pahānaṃ vuttaṃ": "đã nói rằng sự dứt bỏ",   # inner «rằng» kept
    "sakkāyadiṭṭhiṃ pajahati": "dứt bỏ quan điểm về tự ngã",
    "oḷārikaṃ pajahati": "dứt bỏ" + GAP + "ở dạng thô",   # notes-map-4 oḷārikaṃ jahati
    "oḷārikaṃ kāmarāgaṃ pajahati": "dứt bỏ sự tham đắm dục lạc ở dạng thô",
    "aṇusahagataṃ pajahati": "dứt bỏ" + GAP + "ở dạng nhỏ nhiệm",   # notes-map-3
    "kāmarāgabyāpādānaṃ": "sự tham đắm dục lạc và ác ý", "tanubhāvaṃ": "sự suy yếu",
    "rāga": "sự tham đắm", "rūpa": "cõi hình sắc", "arūpa": "cõi không hình sắc",   # «sự tham đắm cõi hình sắc»
    "māna": "sự kiêu mạn", "uddhacca": "sự xao động", "avijjāya": "vô minh",
    "avasesa": "còn sót lại",                      # of anavasesa «không còn sót lại» (pi-4)
    # ---- 5-417 uddāna «Tóm tắt của chương này – …, cũng vậy với sáu sự bình thản, …»
    "uddānaṃ": "Tóm tắt",                          # notes-map-9
    "evamevaṃ": "cũng vậy",
}

OVERRIDES = {
    "5-12-9-1-0": {"kathā": "Bàn" + GAP + "về"},   # Aparāpi samannāgatakathā «Bàn thêm về …» (as ^5-3-1-0)
    "5-387": {"eva": "ngay"},                      # first diṭṭheva dhamme «ngay trong đời này»; CROSSCHECK «thật»
    "5-402": {"eva": "chỉ",                        # first dveva gatiyo «chỉ có hai hướng đi»; CROSSCHECK «chính», «thật»
              "dhamma": "lẽ phải",                 # dhammiko / dhammarājā / dhammena «… lẽ phải»
              "assa": "ngựa",                      # assaratanaṃ «báu vật ngựa»
              "patto": "đã đạt được"},             # janapadatthāvariyappatto «đã đạt được sự ổn định của đất nước»
    "5-412": {"kathā": "Bàn" + GAP + "về"},        # closer «Phần bàn thêm về sự được trang bị đã hoàn tất.»
    "5-403": {"bodhiyā": "cây Bồ-đề",              # bodhiyā mūle «dưới gốc cây Bồ-đề» (map_3_vi)
              "buddho": "Đức Phật"},               # «là đệ tử rồi trở thành Đức Phật» (map_4_vi)
    "5-405": {"cakkhuṃ": "con mắt"},               # «con mắt đã khởi lên» (notes-map-3)
    "5-413": {"vata": "nghi thức"},                # first sīlabbataparāmāsaṃ (before «vata re»); CROSSCHECK «chắc chắn»
}

ALLOWED = {}


def context12(kw, kws, text):
    """Segment rules of this chapter (None = no rule)."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k == "arahatta":            # member of arahattamaggo / -phalaṃ «con đường / thành quả A-la-hán» (pi-4 «A-la-hán»)
        if s & {"arahattamaggo", "arahattamaggena", "arahattaphalaṃ"}:   # / of arahattasacchikiriyāya «… trạng thái
            return "A-la-hán"                                            # A-la-hán» (notes-map-3)
        return "trạng thái A-la-hán"
    if k == "bodhisatto okkantaniyāmo":            # «Bồ-tát, trong lời dạy …, đã bước vào sự cố định» / uddāna
        return join(text, [_BT, _CĐ])              # «Bồ-tát đã bước vào sự cố định» (contiguous where it stands so)
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        v = context12(kw, kws, text)
        if v is not None:
            return v
        return value5(kw, kws, T12, text)
    return resolve


def show(lo, hi, only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or (v != "???" and present(v, vi.get(bid, ""))) else " <<MISS"
                if only_miss and not flag:
                    continue
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
