"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 15: 15-sattamavaggo.

usage: python -I -X utf8 -B map_15_vi.py                    (writes 15-sattamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_15_vi.py show lo hi [miss]   (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 -B map_15_vi.py ctx bid word ...    (Vietnamese around each word in segment bid)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context15 (segment rules) -> T15 -> map_5_vi.subject_predicate
-> value5(kw, kws, PRIOR, text) of map_sample_vi, where PRIOR = the finished chapter tables (T2 … T12, as map_10_vi)
under T15.
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-15.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, editorial_text, en_ru, join, lc, pick, present,  # noqa: E402
                           read_keywords, read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401
import map_2_vi  # noqa: E402
import map_3_vi  # noqa: E402
import map_4_vi  # noqa: E402
import map_5_vi  # noqa: E402
import map_6_vi  # noqa: E402
import map_7_vi  # noqa: E402
import map_8_vi  # noqa: E402
import map_9_vi  # noqa: E402
import map_10_vi  # noqa: E402
import map_11_vi  # noqa: E402
import map_12_vi  # noqa: E402

PART = "15-sattamavaggo"

_YT = "yếu tố đồng hành với tâm"                   # cetasika (pi-2)
_PTH = "phát sinh từ sự thọ hưởng"                 # paribhogamaya
_PH = "phước " + _PTH                              # paribhogamayaṃ puññaṃ (head noun first)
_KN = "sự không biết ghê sợ tội lỗi"               # anottappa (pi-1)
_HT = "hiện tượng có khả năng sinh ra quả"         # vipākadhammadhammo
_DM = "được cảm nhận"                              # vedaniya

T15 = {
    # ---- headings «Chương thứ bảy»; «Bàn về những gì được gộp vào», «… những gì gắn liền», «… yếu tố đồng hành với
    # tâm», «… sự bố thí», «… phước phát sinh từ sự thọ hưởng», «… quả của hiện tượng cao quý», «… việc cho rằng quả
    # của nghiệp là hiện tượng có khả năng sinh ra quả»
    "sattamavaggo": "Chương thứ bảy",              # heading and «Chương thứ bảy.» (as map_12 Catutthavaggo)
    "saṅgahita": "được gộp vào",                   # «những gì được gộp vào» («những gì» = frame, as map_12 anāsava)
    "saṅgahitakathā": "Bàn về những gì được gộp vào",   # whole heading (map_12 niyāmokkantikathā)
    "sampayuttakathā": "Bàn về những gì gắn liền",
    "cetasika": _YT, "cetasikakathā": "Bàn về " + _YT,
    "cetasiko": _YT, "cetasikā": _YT, "cetasikaṃ": _YT,   # «hiện tượng là yếu tố đồng hành với tâm» (not pi-1 «trong
                                                          # tâm»: the text's predicate noun, pi-2)
    "maya": "phát sinh từ", "paribhogamayaṃ": _PTH,
    "paribhogamayapuñña": _PH, "paribhogamayapuññakathā": "Bàn về " + _PH,
    "paribhogamayaṃ puññaṃ": _PH,
    "tena hi puññaṃ": "Vậy thì phước", "tena hi paribhogamayaṃ puññaṃ": "Vậy thì " + _PH,
    "puñña": "phước", "puññaṃ": "phước", "puññāni": "việc phước",   # «các việc phước» («các» dropped)
    "ariyadhamma": "hiện tượng cao quý",
    "vipākadhammadhammo": _HT,                     # «là hiện tượng có khả năng sinh ra quả» (dhamma «hiện tượng»; pi-2
                                                   # bare predicate «có khả năng sinh ra quả» = vipākadhamma)
    "vipāko vipākadhammadhammo": "quả của nghiệp là " + _HT,   # inner «là» kept
    # ---- 5-471 «Lĩnh vực mắt được tính vào khối nào? Được tính vào khối vật chất … được tính vào, được kể vào, nằm
    # trong …»
    "viññāṇakkhandha": "khối thức", "vedanākkhandha": "khối cảm giác", "rūpakkhandha": "khối vật chất",
    "saṅkhārakkhandha": "khối tạo tác", "saññākkhandha": "khối tri giác",
    "gaṇanaṃ": "tính", "uddesaṃ": "kể",            # gaṇanaṃ / uddesaṃ gacchati «được tính vào / được kể vào»
    "cakkhu": "mắt", "saṅkhāra": "tạo tác", "gandha": "mùi",
    "dukkhā": "khó chịu", "sukhā vedanā": "cảm giác dễ chịu",   # contiguous here (pi-2)
    # ---- 5-472 «giống như hai con bò đực được gộp vào bằng dây thừng hay bằng dây ách, đồ ăn khất thực được gộp vào
    # bằng túi treo, con chó được gộp vào bằng dây xích … [lời của người theo học thuyết của chúng ta (cần xem Chú
    # giải)]»
    "dāmena": "dây thừng", "yottena": "dây ách", "balibaddā": "bò đực", "sikkāya": "túi treo",
    "piṇḍapāto": "đồ ăn khất thực", "gaddulena": "dây xích",
    "sakavādi": "người theo học thuyết của chúng ta",   # FORMULAS sakavādī (short -i in the editorial bracket)
    # ---- 5-473 «đi kèm, cùng sinh, hòa lẫn, có cùng sự sinh khởi, có cùng sự chấm dứt, có cùng chỗ dựa, có cùng đối
    # tượng»
    "sahajātā": "cùng sinh", "vedanākkhandho sahajāto": "khối cảm giác cùng sinh",
    "saha": "cùng",                                # sahagatā / sahajātā (notes-map-11; T12 «ngay khi» is saha upapattiyā)
    # ---- 5-474 «giống như dầu thấm vào, thâm nhập vào trong hạt mè, nước ép thấm vào, thâm nhập vào trong cây mía»
    "tilamhi": "hạt mè", "ucchumhi": "cây mía", "raso": "nước ép",   # locative frame «trong» dropped
    "anugataṃ": "thấm vào", "anugatā": "thấm vào", "anupaviṭṭhaṃ": "thâm nhập vào", "anupaviṭṭhā": "thâm nhập vào",
    # ---- 5-475 / 5-476 «sự tiếp xúc … cảm giác… tri giác… chủ ý… niềm tin… sự tinh tấn… sự tỉnh thức… sự định tâm…
    # trí tuệ… sự tham đắm… sự sân hận… sự si mê… sự không biết ghê sợ tội lỗi»
    "sati": "sự tỉnh thức", "satiyā": "sự tỉnh thức", "satiṃ": "sự tỉnh thức",   # the factor (notes-map-8)
    "saddhāya": "niềm tin", "rāgena": "sự tham đắm", "dosena": "sự sân hận",
    "ottappena": "biết ghê sợ tội lỗi",            # of anottappena (positive part, notes-map-2)
    "anottappena": _KN, "anottappāsikā": "yếu tố đồng hành với " + _KN,   # «là yếu tố đồng hành với sự không biết …»
    # ---- 5-477 verse «Vì tâm này và các hiện tượng là yếu tố đồng hành với tâm, Đối với người đã hiểu rõ, chúng không
    # phải là tự ngã; Sau khi biết cả hai điều ấy, thấp kém và ưu việt, Người thấy đúng đắn đã biết điều có bản chất
    # tan rã» / sutta «vị tỳ-khưu chỉ ra cả tâm …, chỉ ra cả điều được hướng tâm đến, chỉ ra cả điều được duy trì tâm
    # vào»
    "saṃviditassa": "người đã hiểu rõ", "hīna": "thấp kém", "viditvā": "sau khi biết",   # gerund keeps «sau khi»
    "daso": "người thấy", "paloka": "tan rã",      # Sammaddaso «Người thấy đúng đắn»; palokadhamma «có bản chất tan rã»
    "ādisati": "chỉ ra",
    "vitakkitaṃ": "điều được hướng tâm đến", "vicāritaṃ": "điều được duy trì tâm vào",   # the text's «điều» kept
    # ---- 5-479 / 5-482 «sự bố thí có kết quả đáng mong muốn, … có kết quả không pha tạp, đưa đến sự dễ chịu, có quả
    # trổ dễ chịu … thuốc men và vật dụng chữa bệnh» [giống với câu hỏi của người theo học thuyết khác sẽ được nói ở
    # phần sau, cần tham khảo Chú giải]
    "iṭṭhaphalaṃ": "có kết quả đáng mong muốn", "phalo": "kết quả",   # member of iṭṭhaphalo … (sample phalā / phalaṃ)
    "udrayaṃ": "đưa đến", "udrayo": "đưa đến",
    "sukhudrayaṃ": "đưa đến sự dễ chịu", "sukhudrayo": "đưa đến sự dễ chịu",
    "parikkhāro": "vật dụng",
    "sadisā": "giống với", "pucchāya": "câu hỏi", "vuccamānāya": "sẽ được nói",
    # ---- 5-480 verse «Niềm tin, sự biết hổ thẹn và sự bố thí thiện, Những hiện tượng này được những người chân chính
    # noi theo; Vì người ta nói đây là con đường thuộc cõi trời, Vì nhờ điều này mà người ta đi đến thế giới chư thiên»
    # and the sutta of the five great gifts
    "hiriyaṃ": "sự biết hổ thẹn", "anuyātā": "noi theo", "diviyaṃ": "thuộc cõi trời",
    "dānāni": "sự bố thí", "mahādānaṃ": "sự bố thí lớn", "mahādānāni": "sự bố thí lớn",   # «những» dropped
    "aggaññāni": "được biết là bậc nhất", "rattaññāni": "được biết là lâu đời",
    "vaṃsaññāni": "được biết là thuộc dòng truyền thống", "porāṇāni": "cổ xưa",
    "asaṅkiṇṇāni": "không lẫn lộn", "asaṅkiṇṇapubbāni": "trước đây chưa từng lẫn lộn",   # notes-map-5
    "saṅkiṇṇa": "lẫn lộn",                         # of asaṅkiṇṇa- (positive part; not the arahant formula «đã lấp»)
    "paṭikuṭṭhāni": "bị" + GAP + "phản đối",       # of appaṭikuṭṭhāni «không bị các sa-môn … phản đối» (notes-map-5)
    "pahāya": "sau khi dứt bỏ",                    # gerund keeps «sau khi» (coordinator rule)
    "atipātaṃ": "việc sát hại",                    # T11 atipātā (the text's «việc»)
    "pamādaṭṭhānaṃ": "dẫn đến sự buông thả",       # T11 pamādaṭṭhānā
    "aparimāṇānaṃ": "vô lượng", "abhayaṃ": "sự không sợ hãi",
    "averaṃ": "sự không thù địch", "abyābajjhaṃ": "sự không thù hằn",
    "veraṃ": "thù địch", "byābajjhaṃ": "thù hằn",  # of averaṃ / abyābajjhaṃ (positive part; pi-1 byāpajjo)
    "micchācāraṃ": "hành vi sai trái", "vādaṃ": "việc nói",   # musāvādaṃ «việc nói dối» (musā = dối)
    "puna": "Lại nữa",                             # Puna caparaṃ «Lại nữa» (KV pana)
    # ---- 5-481 «có người cho thức ăn, cho thức uống, cho vải, cho xe cộ, cho vòng hoa, cho hương thơm, cho dầu thoa,
    # cho giường nằm, cho chỗ ở, cho đèn đuốc»; «vật để bố thí là sự bố thí»
    "annaṃ": "thức ăn", "pānaṃ": "thức uống", "yānaṃ": "xe cộ", "mālaṃ": "vòng hoa", "gandhaṃ": "hương thơm",
    "seyyaṃ": "giường nằm", "āvasathaṃ": "chỗ ở", "padīpeyyaṃ": "đèn đuốc",
    "deyyadhammo": "vật để bố thí",
    # ---- 5-483 «tăng trưởng như dây leo, … như dây quấn, … như cây, … như cỏ, … như đám cỏ lau»
    "viya": "như", "māluvā": "dây quấn", "rukkho": "cây", "muñja": "cỏ lau", "puñjo": "đám",
    "samādhi": "sự định tâm",                      # the factor (the text's «sự»; context15 for the other forms)
    # ---- 5-484 «người bố thí, sau khi thực hiện sự bố thí, không lưu ý … có đối với người hướng đến … người chú hướng
    # … người lưu ý … người chú tâm … người khởi chủ ý … người mong ước … người mong cầu»
    "dāyako": "người bố thí", "samannāharati": "lưu ý",
    "āvaṭṭentassa": "người hướng đến", "ābhogassa": "người chú hướng", "samannāharantassa": "người lưu ý",
    "manasikarontassa": "người chú tâm", "cetayantassa": "người khởi chủ ý", "patthayantassa": "người mong ước",
    "paṇidahantassa": "người mong cầu",           # the text's head noun «người» kept (no «khi»)
    # ---- 5-485 «khởi lên sự hướng tâm đến dục lạc, … đến ác ý, … đến sự hãm hại … các hiện tượng thiện và bất thiện,
    # có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong sáng cùng với các mặt đối lập của chúng đi đến chỗ
    # cùng hiện diện đối mặt nhau» and AN 4.47 «bốn điều rất xa cách nhau … bầu trời và mặt đất … bờ bên này của biển …
    # nơi mặt trời mọc lên … giáo pháp của người hiền thiện và giáo pháp của kẻ không hiền thiện»
    "vitakketi": "khởi lên", "vihiṃsā": "sự hãm hại",
    "anavajjā": "không có lỗi", "sukka": "trong sáng", "sukka dhammā": "hiện tượng" + GAP + "trong sáng",
    "sappaṭibhāgā": "cùng với các mặt đối lập của chúng",   # inner «các» kept
    "sammukhībhāvaṃ": "cùng hiện diện đối mặt nhau",        # notes-map-5 sammukhībhāvo
    "sappaṭibhāgā sammukhībhāvaṃ āgacchanti":
        "cùng với các mặt đối lập của chúng đi đến chỗ cùng hiện diện đối mặt nhau",
    "vidūrāni": "xa cách nhau",                    # suvidūravidūrāni «rất xa cách nhau» («rất» = the su-)
    "nabhaṃ": "bầu trời", "samuddassa": "biển", "verocano": "mặt trời", "abbhudeti": "mọc lên",
    "dhammo": "giáo pháp",                         # satañca dhammo «giáo pháp của người hiền thiện» (as written)
    "asataṃ": "kẻ không hiền thiện",               # own a- kept
    "pabha": "vầng sáng", "karo": NDE,             # Pabhaṅkaro «vầng sáng»: karo has no word of its own
    "dūrataraṃ": "xa hơn",
    "byāyiko": "bị hao mòn",                       # of abyāyiko «không bị hao mòn» (positive part)
    "tiṭṭheyya": "kéo dài",                        # optative: the bare verb (map_12)
    "khippaṃ": "nhanh chóng", "veti": "tàn phai",
    # ---- 5-486 verses «Những người trồng vườn cây, trồng rừng, những người làm cầu; Những người cho trạm nước uống và
    # giếng nước, cho chỗ trú ngụ. Đối với họ, cả ngày lẫn đêm, phước luôn luôn tăng trưởng; Đứng vững trong Giáo Pháp,
    # thành tựu về giới hạnh, những người ấy đi đến cõi trời» and AN 4.51 «bốn dòng chảy phước này, dòng chảy thiện, là
    # dưỡng chất của hạnh phúc, thuộc về cõi trời, có quả trổ dễ chịu, dẫn đến cõi trời, đưa đến điều đáng mong muốn …
    # khi vị tỳ-khưu thọ hưởng y phục …»
    "ārāma": "vườn cây", "setu": "cầu", "kārakā": "người làm",   # setukārakā «những người làm cầu» (not ch12 Sê-tu)
    "papaṃ": "trạm nước uống", "upassayaṃ": "chỗ trú ngụ", "ratto": "đêm", "ṭhā": "đứng vững",
    "abhisandā": "dòng chảy", "abhisando": "dòng chảy",
    "āhārā": "dưỡng chất", "āhāro": "dưỡng chất",  # «là dưỡng chất của hạnh phúc» (no «loại» here)
    "sovaggikā": "thuộc về cõi trời", "vipākā": "quả trổ",   # sukhavipākā «có quả trổ dễ chịu»
    "sagga": "cõi trời", "saṃvattati": "đưa đến",  # saggasaṃvattanikā «dẫn đến cõi trời»; iṭṭhāya … saṃvattati «đưa đến»
    "iṭṭhāya": "đáng mong muốn", "kantāya": "đáng yêu mến", "manāpāya": "đáng ưa thích",
    "paribhuñjamāno": "khi" + GAP + "thọ hưởng",   # participle keeps «khi»
    # ---- 5-487 «người nhận, sau khi nhận, không thọ hưởng, vứt bỏ, cho đi … hoặc vua chúa lấy đi, hoặc kẻ trộm lấy
    # đi, hoặc lửa thiêu đốt, hoặc nước cuốn trôi, hoặc những người thừa kế không ưa thích lấy đi»
    "paṭiggāhako": "người nhận", "chaḍḍeti": "vứt bỏ",
    "rājāno": "vua chúa", "corā": "kẻ trộm", "dahati": "thiêu đốt", "vahati": "cuốn trôi",
    "appiyā": "không ưa thích", "dāyādā": "người thừa kế",
    # ---- 5-488 «từ đây cho … món ăn cứng, … món ăn mềm, … nước uống … một người là người làm cho một người khác, sự dễ
    # chịu và sự khó chịu do người khác làm ra»
    "khādanīyaṃ": "món ăn cứng", "bhojanīyaṃ": "món ăn mềm", "pānīyaṃ": "nước uống",
    "kārako": "người làm",                         # the text's agent noun (sample «người tạo» where it says so)
    "parakataṃ sukhadukkhaṃ": "sự dễ chịu và sự khó chịu do người khác làm ra",
    "yāpenti": "duy trì sự sống",                  # «mà ở đó duy trì sự sống»
    # ---- 5-489 «các ngạ quỷ tùy hỷ với người đang thực hiện sự bố thí vì lợi ích của họ, làm cho tâm trong sáng»
    "petā": "ngạ quỷ", "atthāya": "lợi ích",       # «vì» = the dative frame (sample hitāya)
    "dentaṃ": "người đang thực hiện", "anumodenti": "tùy hỷ", "pasādenti": "làm cho" + GAP + "trong sáng",
    # ---- 5-490 verses «Nước mưa rơi xuống chỗ cao, chảy xuôi về chỗ thấp; Cũng vậy, những gì được cho từ đây đem lại
    # lợi ích cho các ngạ quỷ. Như những dòng sông đầy nước làm đầy biển cả; … Vì ở đó không có việc cày cấy, việc chăn
    # bò không hiện hữu ở đó; Không có việc buôn bán như thế … các ngạ quỷ, những người đã qua đời»
    "unname": "chỗ cao", "vuṭṭhaṃ": "mưa rơi xuống", "pavattati": "chảy xuôi", "upakappati": "đem lại lợi ích",
    "vārivahā": "dòng sông", "paripūrenti": "làm đầy", "sāgaraṃ": "biển cả",
    "kasī": "việc cày cấy", "gorakkha": "việc chăn bò", "tādisī": "như thế",
    "kālaṅkatā": "người đã qua đời", "kālaṅkatānaṃ": "người đã qua đời",   # «những» dropped
    # ---- 5-491 AN 5.31 «thấy rõ năm lý do này, cha mẹ mong muốn có người con trai sinh ra trong gia đình … Được nuôi
    # dưỡng, nó sẽ nuôi dưỡng chúng ta … nó sẽ nhận lấy gia tài, hoặc nữa, nó sẽ dâng phần cúng dường cho các ngạ quỷ
    # … những người sáng suốt … những người hiền thiện, … biết ơn và ghi nhớ ơn … nhớ lại những gì đã được làm trước
    # đây … như đối với những người đã làm ơn trước. Làm theo lời khuyên dạy, nuôi dưỡng những người đã nuôi mình,
    # không làm suy tàn dòng dõi gia đình; … người con trai ấy đáng được khen ngợi»
    "ṭhānāni": "lý do", "sampassantā": "thấy rõ", "pitaro": "cha",   # mātāpitaro «cha mẹ» (mātā = mẹ)
    "puttaṃ": "người con trai", "icchanti": "mong muốn", "jāyamānaṃ": "sinh ra",   # no «khi» in the text
    "bhaṭo": "được nuôi dưỡng", "dāyajjaṃ": "gia tài", "atha": "hoặc nữa", "dakkhiṇaṃ": "phần cúng dường",
    "paṇḍitā": "người sáng suốt", "santo": "người hiền thiện",   # «những» dropped (KV santo «đang có mặt» elsewhere)
    "katavedino": "ghi nhớ ơn", "anussaraṃ": "nhớ lại", "kārinaṃ": "người đã làm ơn",
    "ovāda": "lời khuyên dạy", "posī": "nuôi dưỡng", "hāpayaṃ": "làm suy tàn",   # of ahāpayaṃ (positive part)
    "pasaṃsiyo": "đáng được khen ngợi",
    # ---- 5-492 / 5-495 «được cảm nhận là dễ chịu, được cảm nhận là khó chịu … có đối tượng … có thể mua, bán, cầm cố,
    # thu gom, chọn lựa»
    "vedaniyā": _DM, "vedaniyaṃ": _DM,
    "sukhavedaniyā": _DM + " là dễ chịu", "sukhavedaniyaṃ": _DM + " là dễ chịu",   # inner «là» kept
    "dukkhavedaniyā": _DM + " là khó chịu", "dukkhavedaniyaṃ": _DM + " là khó chịu",
    "āṭhapetuṃ": "cầm cố", "ocinituṃ": "thu gom", "vicinituṃ": "chọn lựa",
    # ---- 5-493 «đất hình thành trước, chúng sinh xuất hiện sau … tạo nghiệp để có được quả của nghiệp … nhập Niết-bàn
    # trọn vẹn» and the verse «Không chung cho những người khác, là kho báu kẻ trộm không lấy đi được; Con người hãy làm
    # các việc phước, nếu thực hành hành vi tốt»
    "sādhāraṇā": "thứ chung", "saṇṭhāti": "hình thành", "uppajjanti": "xuất hiện",   # notes-map-3
    "paṭilābhāya": "có được",                      # «để» = the dative frame (pi-4 sacchikiriyāya)
    "karonti": "tạo", "kammaṃ karonti": "tạo nghiệp", "parinibbāyanti": "nhập Niết-bàn trọn vẹn",
    "acoraharaṇo": "kẻ trộm không lấy đi được", "haraṇo": "lấy đi được", "nidhi": "kho báu",
    "kayirātha": "hãy làm", "macco": "con người",  # «hãy» kept as the imperatives (Hãy thừa nhận)
    "caritaṃ": "hành vi", "care": "thực hành",     # sucaritaṃ care «thực hành hành vi tốt»
    # ---- 5-494 / 5-497 «nghiệp dẫn đến quyền uy, nghiệp dẫn đến quyền thống trị … nghiệp dẫn đến sự xấu xí, nghiệp
    # dẫn đến tuổi thọ ngắn»
    "saṃvattaniyaṃ": "dẫn đến", "adhipacca": "quyền thống trị",
    "issariyasaṃvattaniyaṃ kammaṃ": "nghiệp dẫn đến quyền uy",   # head noun first
    "dubbaṇṇa": "sự xấu xí", "dubbaṇṇasaṃvattaniyaṃ kammaṃ": "nghiệp dẫn đến sự xấu xí",
    "āyuka": "tuổi thọ",                           # appāyuka «tuổi thọ ngắn»
    # ---- 5-496 «sự lão hóa và sự chết của các hiện tượng thiện, là quả của các hiện tượng bất thiện»
    "akusalānaṃ vipāko": "quả" + GAP + "bất thiện", "kusalānaṃ vipāko": "quả" + GAP + "thiện",   # head noun first
    "kusalānaṃ akusalānaṃ": "thiện và bất thiện",  # Kusalānañca akusalānañca «các hiện tượng thiện và bất thiện»
    # ---- 5-498 «đời sống sa-môn có quả lớn, đời sống bà-la-môn có quả lớn … quả của sự bố thí … quả của giới hạnh …
    # quả của sự tu tập»
    "sāmaññaṃ": "đời sống sa-môn", "brahmaññaṃ": "đời sống bà-la-môn",
    "dānaphalaṃ": "quả của sự bố thí", "bhāvanāphalaṃ": "quả của sự tu tập",
    "arahatta": "A-la-hán",                        # only «thành quả A-la-hán» here (map_12 context12)
    # ---- 5-499 / 5-500 «điều thiện thuộc cõi dục lạc có quả trổ, dẫn đến sự tích lũy … điều thiện vượt thế gian»
    "arūpa": "không hình sắc",                     # arūpāvacaraṃ «thuộc cõi không hình sắc» (pi-1)
    "lokuttaraṃ kusalaṃ": "điều thiện vượt thế gian",   # the text's «điều» kept (pi-3 asaṅkhataṃ)
    "savipākaṃ ācayagāmī": "có quả trổ dẫn đến sự tích lũy",   # comma dropped (pi-1)
    # ---- 5-501 «đối với từng cái một, không có việc đi đến tận cùng của khổ đau, không có sự cắt đứt vòng xoay … cùng
    # một nghĩa … với chính tâm nào mà giết hại sinh mạng thì với chính tâm ấy bị thiêu đốt trong địa ngục, … vui hưởng
    # ở cõi trời»
    "tassa tasseva": "từng cái một",               # (sample «từng người như vậy» where the text says so)
    "dukkhassa antakiriyā": "việc đi đến tận cùng của khổ đau", "vaṭṭa": "vòng xoay",   # notes-map-5 vaṭṭe
    "ekaṭṭhe": "cùng một nghĩa",                   # sample aṭṭhe «nghĩa» (ch3 tadekaṭṭhe «cùng hiện diện» is another text)
    "hanati": "giết hại", "niraye": "địa ngục", "paccati": "bị thiêu đốt",
    "sagge": "cõi trời", "modati": "vui hưởng",    # locative frame «ở» / «trong» dropped
    # ---- 5-502 uddāna «Sự gộp vào, điều gắn liền, …» and «bốn khối không có hình sắc»
    "saṅgaho": "Sự gộp vào",                       # line-initial capital kept (map_9 Upalabbho, map_11 Balaṃ)
    "arūpino": "không có hình sắc",
}

PRIOR = {**map_7_vi.T7, **map_6_vi.T6, **map_5_vi.T5, **map_4_vi.T4, **map_2_vi.T2, **map_3_vi.T3,
         **map_8_vi.T8, **map_9_vi.T9, **map_10_vi.T10, **map_11_vi.T11, **map_12_vi.T12, **T15}


def context15(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    if k in ("samādhiṃ", "samādhinā"):              # the factor «sự định tâm» (T12 «định tâm» where only that stands)
        return pick(text, "sự định tâm", "định tâm")
    if k in ("ārammaṇā", "ārammaṇaṃ"):              # ekārammaṇā «có cùng đối tượng» (eka «cùng»: the noun, as uppādā
        if present("có cùng đối tượng", text):     # «sự sinh khởi») / sārammaṇā «có đối tượng» (pi-1 / pi-2)
            return "đối tượng"
        return "có đối tượng"
    if k == "sāvako":              # ariyasāvako «vị đệ tử cao quý» (map_10 «vị đệ tử») / «là đệ tử» (map_12)
        return pick(text, "vị đệ tử", "đệ tử")
    return None


OVERRIDES = {
    "5-471": {"rūpa": "vật chất",                  # first Rūpakkhandhagaṇanaṃ «khối vật chất»; CROSSCHECK «hình sắc»
                                                   # (Rūpāyatanaṃ «lĩnh vực hình sắc»)
              "gacchati": "được" + GAP + "vào"},   # gaṇanaṃ gacchati «được tính vào» (gaṇanaṃ «tính», uddesaṃ «kể»)
    "5-479": {"phalaṃ": "kết quả",                 # iṭṭhaphalaṃ «có kết quả …» (map_10 context10 with dānaṃ)
              "sukha": "sự dễ chịu"},              # first sukhudrayaṃ «đưa đến sự dễ chịu»; CROSSCHECK «dễ chịu»
                                                   # (sukhavipākaṃ «có quả trổ dễ chịu»)
    "5-480": {"deti": "ban",                       # abhayaṃ deti «ban cho … sự không sợ hãi», «ban sự không thù địch»
              "gacchati": "đi đến"},               # gacchati devalokaṃ «người ta đi đến thế giới chư thiên»
    "5-482": {"sukha": "sự dễ chịu"},              # first sukhudrayo «đưa đến sự dễ chịu»; CROSSCHECK «dễ chịu»
    "5-485": {"pathavī": "mặt đất",                # Nabhañca pathavī ca «bầu trời và mặt đất» (the text's word)
              "eva": "y"},                         # first tatheva hoti «vẫn y như vậy»; CROSSCHECK Attheva «thật»
    "5-487": {"deti": "thực hiện"},                # dāyako dānaṃ deti «người bố thí thực hiện sự bố thí»
    "5-488": {"Añño": "một người",                 # first Añño aññassa kārako «một người là người làm cho một người
                                                   # khác»; also «một người làm, một người khác cảm nhận»
              "dukkhaṃ": "sự khó chịu"},           # sukhadukkhaṃ «sự dễ chịu và sự khó chịu» (context5)
    "5-490": {"eva": "cũng"},                      # first Evameva «Cũng vậy, những gì được cho từ đây»; CROSSCHECK
                                                   # Attheva «thật»
    "5-492": {"dukkha": "khó chịu"},               # first dukkhavedaniyā «được cảm nhận là khó chịu»
    "5-495": {"dukkha": "khó chịu"},
    "5-498": {"phalaṃ": "quả"},                    # first mahapphalaṃ «có quả lớn» (also dānaphalaṃ «quả của …»);
                                                   # CROSSCHECK «thành quả» (sotāpattiphalaṃ …)
    "5-499": {"rūpa": "hình sắc", "kusalaṃ": "điều thiện"},   # rūpāvacaraṃ «thuộc cõi hình sắc» (pi-1 rūpa); «điều
    "5-500": {"rūpa": "hình sắc", "kusalaṃ": "điều thiện"},   # thiện thuộc cõi dục lạc» (the text's «điều» kept)
    "5-501": {"deti": "thực hiện"},                # dānaṃ deti «thực hiện sự bố thí»
}

ALLOWED = {
}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        text = vi.get(bid, "")
        v = context15(kw, k, kws, text)
        if v is not None:
            return v
        if k in T15:
            return T15[k]
        if k not in PRIOR:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, PRIOR, text)
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


def ctx(bid, words, width=60):
    t = editorial_text(read_vietnamese(PART).get(bid, ""))
    low = t.lower()
    for w in words:
        pos = low.find(w.lower())
        n = 0
        while pos >= 0 and n < 3:
            print(f"[{w}] …{t[max(0, pos - width):pos + len(w) + width]}…".replace("\n", " / "))
            pos = low.find(w.lower(), pos + 1)
            n += 1
        if n == 0:
            print(f"[{w}] (absent)")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["ctx"]:
        ctx(sys.argv[2], sys.argv[3:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
