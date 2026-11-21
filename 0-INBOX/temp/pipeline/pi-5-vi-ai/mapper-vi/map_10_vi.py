"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 10: 10-dutiyavaggo.

usage: python -I -X utf8 -B map_10_vi.py                    (writes 10-dutiyavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_10_vi.py show lo hi [miss]   (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 -B map_10_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_10_vi.py ctx bid word ...    (Vietnamese around each word in segment bid)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context10 (segment rules) -> T10 -> context2 of map_2_vi (the
arahant-formula rules) -> map_5_vi.subject_predicate -> value5(kw, kws, PRIOR, text) of map_sample_vi, where PRIOR =
the finished chapter tables (T3 over T2 over T4 … T7) under T10.
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-10.md.
"""
import pathlib
import sys
from collections import Counter

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

PART = "10-dutiyavaggo"

_ARA = "bậc A-la-hán"

_XT = "sự xuất tinh bất tịnh"                      # asuci sukkavissaṭṭhi
_DTT = "đã được tự mình chứng nghiệm"
_GG = "việc được người khác giảng giải"             # paravitāraṇā
_SDK = "thông thạo các hiện tượng của mình"         # sadhammakusala
_PDK = "thông thạo các hiện tượng của người khác"   # paradhammakusala
_DN = "người đang nhập"                            # samāpannassa
_PRL = "sự phát ra lời nói"                        # vacībhedo
_IPP = "quy luật tùy thuộc vào điều kiện"          # idappaccayatā

T10 = {
    # ---- headings: «Chương thứ hai», «Bàn về việc người khác đưa đến», «… sự không biết», «… sự nghi ngờ», «… việc
    # được người khác giảng giải», «… sự phát ra lời nói», «… việc nêu lên khổ đau», «… sự duy trì của tâm», «… tro
    # nóng», «… sự thấu hiểu tuần tự», «… lời nói», «… sự chấm dứt»
    "upahāra": "việc" + GAP + "đưa đến", "upahāro": "việc" + GAP + "đưa đến",   # parūpahāra «việc người khác đưa đến»
    "para": "người khác",
    "aññāṇa": "sự không biết", "aññāṇaṃ": "sự không biết",
    "vitāraṇa": "việc được" + GAP + "giảng giải", "vitāraṇā": "việc được" + GAP + "giảng giải",
    "bheda": "sự phát ra", "vacī": "lời nói", "vacībheda": _PRL, "vacībhedo": _PRL,
    "āhāra": "việc nêu lên", "āhāro": "việc nêu lên",   # dukkhāhāra «việc nêu lên khổ đau»
    "āhārakathā": "Bàn về việc nêu lên",            # extraction artefact of Dukkhāhārakathā
    "ṭhiti": "sự duy trì", "cittaṭṭhiti": "sự duy trì của tâm", "citta": "tâm",
    "kukkuḷa": "tro nóng", "kukkuḷā": "tro nóng",
    "abhisamaya": "sự thấu hiểu", "abhisamayo": "sự thấu hiểu",
    "anupubbābhisamayo": "sự thấu hiểu tuần tự",
    "vohāra": "lời nói", "vohāro": "lời nói", "vohāraṃ": "lời nói", "vohārena": "lời nói",
    "nirodhakathā": "Bàn về sự chấm dứt",
    # ---- 5-307 «bậc A-la-hán có sự xuất tinh bất tịnh … sự tham đắm, sự tham đắm dục lạc, sự ám ảnh của tham đắm
    # dục lạc, xiềng xích tham đắm dục lạc, dòng lũ dục lạc, ách dục lạc, chướng ngại ý muốn dục lạc … các vị thiên
    # thuộc nhóm Ma vương đưa sự xuất tinh bất tịnh đến cho bậc A-la-hán … của những người khác … qua các lỗ chân lông»
    "asuci": "bất tịnh", "asuciṃ": "bất tịnh",     # «sự xuất tinh bất tịnh» (Vietnamese fuses sukka-vissaṭṭhi into
    "sukka": "tinh", "vissaṭṭhi": "xuất", "vissaṭṭhiṃ": "xuất",   # «xuất tinh»: members as pi-2 / pi-4 thiên nhãn)
    "sukkavissaṭṭhi": "sự xuất tinh", "sukkavissaṭṭhiṃ": "sự xuất tinh",
    "asuci sukkavissaṭṭhi": _XT, "asuciṃ sukkavissaṭṭhiṃ": _XT,
    "upasaṃharanti": "đưa" + GAP + "đến",
    "asuciṃ upasaṃharanti": "đưa" + GAP + "bất tịnh đến",
    "asuciṃ sukkavissaṭṭhiṃ upasaṃharanti": "đưa " + _XT + " đến",
    "devatā": "vị thiên", "kāyikā": "thuộc nhóm", "mārakāyikā": "thuộc nhóm Ma vương",
    "mārakāyikā devatā": "vị thiên thuộc nhóm Ma vương",
    "mārakāyikā upasaṃharanti": "thuộc nhóm Ma vương đưa" + GAP + "đến",
    "mārakāyikā asuciṃ upasaṃharanti": "thuộc nhóm Ma vương đưa" + GAP + "bất tịnh đến",
    "puthujjanassa": "người phàm phu", "janassa": "người",
    "puthujjanassa asuci": "người phàm phu" + GAP + "bất tịnh",
    "kāmarāgo": "sự tham đắm dục lạc", "kāma": "dục lạc",
    "chanda": "ý muốn", "kāmacchanda": "ý muốn dục lạc",
    "kāmacchandanīvaraṇaṃ": "chướng ngại ý muốn dục lạc", "nīvaraṇaṃ": "chướng ngại",
    "saṃyojanaṃ": "xiềng xích", "ogho": "dòng lũ", "yogo": "ách", "pariyuṭṭhānaṃ": "sự ám ảnh",
    "aññesaṃ": "người khác",                       # «của những người khác» («những» dropped)
    "lomakūpehi": "lỗ chân lông",
    # ---- 5-308 «Vì lý do gì? Vì chúng ta sẽ gieo sự phân vân … sự phân vân về Bậc Đạo Sư, … Giáo Pháp, … sự tu học
    # … về quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện … là thứ tiết ra từ
    # những gì đã ăn, đã uống, đã nhai, đã nếm … bất cứ ai ăn, uống, nhai, nếm … trẻ em … những người ái nam ái nữ»
    "kāraṇā": "lý do", "vimatiṃ": "sự phân vân",
    "satthari": "Bậc Đạo Sư", "sikkhāya": "sự tu học",
    "idappaccayatāpaṭiccasamuppannesu": _IPP + " và" + GAP + "sinh khởi tùy thuộc vào điều kiện",
    "idappaccayatā": _IPP, "paccayatā": _IPP,
    "ida": NDE,                                    # idappaccayatā: no word of its own (as pi-5 ch3 vāso)
    "paṭicca": "tùy thuộc vào điều kiện",          # pi-1 (ch2 «tùy thuộc vào» where the text has only that)
    "paṭiccasamuppannesu": "sinh khởi tùy thuộc vào điều kiện", "samuppannesu": "sinh khởi",
    "paṭiccasamuppannesu dhammesu": "hiện tượng sinh khởi tùy thuộc vào điều kiện",
    "dhammesu vimati": "sự phân vân" + GAP + "hiện tượng",
    "nissando": "thứ tiết ra",
    "asita": "đã ăn", "pīta": "đã uống", "khāyita": "đã nhai", "sāyitassa": "đã nếm",
    "asanti": "ăn", "pivanti": "uống", "khādanti": "nhai", "sāyanti": "nếm", "khādanti sāyanti": "nhai nếm",
    "dārakā": "trẻ em", "paṇḍakā": "người ái nam ái nữ", "devā": "chư thiên",
    # ---- 5-309 «nó có chỗ chứa … phân và nước tiểu»
    "āsayo": "chỗ chứa", "uccāra": "phân", "passāvo": "nước tiểu",
    # ---- 5-310 «hưởng thụ hành vi dâm dục, làm phát sinh chuyện dâm dục, sống trên chiếc giường chật chội vì con cái,
    # hưởng dùng gỗ đàn hương xứ Ca-thi, mang vòng hoa, hương thơm, dầu thoa, nhận vàng bạc»
    "methunaṃ dhammaṃ": "hành vi dâm dục", "methunaṃ": "chuyện dâm dục",   # methunaṃ uppādeyya (own keyword)
    "paṭiseveyya": "hưởng thụ", "uppādeyya": "làm phát sinh",
    "putta": "con cái", "sambādha": "chật chội", "sayanaṃ": "chiếc giường", "ajjhāvaseyya": "sống trên",
    "kāsikacandanaṃ": "gỗ đàn hương xứ Ca-thi", "candanaṃ": "gỗ đàn hương", "paccanubhaveyya": "hưởng dùng",
    "mālā": "vòng hoa", "gandha": "hương thơm", "vilepanaṃ": "dầu thoa", "dhāreyya": "mang",
    "rajataṃ": "bạc", "sādiyeyya": "nhận",         # jātarūparajataṃ «vàng bạc»
    "diṭṭhi": "quan điểm", "vicikicchā": "sự hoài nghi", "thinaṃ": "sự uể oải", "uddhaccaṃ": "sự xao động",
    "ahirikaṃ": "sự không biết hổ thẹn", "anottappaṃ": "sự không biết ghê sợ tội lỗi",
    # ---- 5-311 «đã tu tập các sự thiết lập tỉnh thức… các nỗ lực đúng đắn… các nền tảng thần thông… các năng lực…
    # các sức mạnh… các chi phần giác ngộ» + the arahant formula (ch2 T2 / context2)
    "satipaṭṭhānā": "sự thiết lập tỉnh thức", "satipaṭṭhānaṃ": "sự thiết lập tỉnh thức",
    "paṭṭhānaṃ": "sự thiết lập", "sati": "tỉnh thức",   # pi-1 SATI_BARE (only inside «sự thiết lập tỉnh thức»)
    "pādā": "nền tảng",                            # iddhipādā (ch5 «bàn chân» is the body part)
    "indriyā": "năng lực", "indriyaṃ": "năng lực",
    "anottappa": "sự không biết ghê sợ tội lỗi", "ottappa": "biết ghê sợ tội lỗi",
    "vītarāgo": "đã lìa tham đắm", "arahā vītarāgo": _ARA + " đã lìa tham đắm",
    "sacchikataṃ": _DTT,                           # sacchikātabbaṃ sacchikataṃ
    "pariññātaṃ": "đã được hiểu biết trọn vẹn",    # the arahant formula (ch2; ch3 override ^5-277)
    "nirodha": "sự chấm dứt",
    # ---- 5-312 «bậc A-la-hán thông thạo các hiện tượng của mình / của người khác»
    "kusalassa": "thông thạo",
    "sadhammakusalassa arahato": _ARA + " " + _SDK,
    "sadhammakusalo vītarāgo": _SDK + " đã lìa tham đắm",
    "sadhammakusalassa paravitāraṇā": _SDK + GAP + _GG,
    # ---- 5-313 sutta «những vị tỳ-khưu là người phàm phu, thành tựu giới hạnh, tỉnh thức và hiểu biết rõ ràng mà đi
    # vào giấc ngủ, thì đồ bất tịnh của họ không thoát ra … những vị ẩn sĩ bên ngoài đã lìa tham đắm đối với các dục
    # lạc … điều không thể xảy ra, không có cơ hội» [Đại Phẩm 353, tương đồng về ý nghĩa; …] … «y phục, đồ ăn khất
    # thực, chỗ ở, thuốc men và vật dụng chữa bệnh»
    "keci": NDE,                                   # only in the bracket [dị bản (Sī.): ye keci]
    "janā": "người", "sampannā": "thành tựu", "satā": "tỉnh thức", "sampajānā": "hiểu biết rõ ràng",
    "niddaṃ": "giấc ngủ", "muccati": "thoát ra", "bāhirakā": "bên ngoài", "isayo": "ẩn sĩ",
    "kāmesu": "dục lạc", "vītarāgā": "đã lìa tham đắm", "rāgā": "tham đắm",
    "anavakāso": "không có cơ hội", "avakāso": "cơ hội",
    "samānaṃ": "tương đồng",                       # atthato samānaṃ «tương đồng về ý nghĩa»
    "cīvara": "y phục", "piṇḍapāta": "đồ ăn khất thực", "senāsana": "chỗ ở", "gilāna": "chữa bệnh",
    "bhesajja": "thuốc men", "parikkhāraṃ": "vật dụng",
    "arahattaṃ": "trạng thái A-la-hán",
    # ---- 5-314 «vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, xiềng
    # xích vô minh, chướng ngại vô minh … bị sự không biết chi phối, có thể sát hại sinh mạng, lấy của không được cho,
    # nói dối, nói lời chia rẽ, nói lời thô ác, nói lời phù phiếm, đột nhập nhà, cướp bóc, cướp một ngôi nhà, mai phục
    # bên đường, đi lại với vợ người khác, cướp phá làng, cướp phá thị trấn»
    "avijjā": "vô minh", "avijjogho": "dòng lũ vô minh", "avijjāyogo": "ách vô minh",
    "avijjānusayo": "khuynh hướng tiềm ẩn vô minh", "anusayo": "khuynh hướng tiềm ẩn",
    "avijjāpariyuṭṭhānaṃ": "sự ám ảnh của vô minh", "avijjāsaṃyojanaṃ": "xiềng xích vô minh",
    "avijjānīvaraṇaṃ": "chướng ngại vô minh",
    "aññāṇapakato": "bị sự không biết chi phối", "pakato": "bị" + GAP + "chi phối",
    "pāṇaṃ": "sinh mạng", "haneyya": "sát hại", "pāṇaṃ haneyya": "sát hại sinh mạng",
    "musā": "dối", "bhaṇeyya": "nói", "pisuṇaṃ": "lời chia rẽ", "pharusaṃ": "lời thô ác",
    "samphaṃ": "phù phiếm", "palapeyya": "nói lời",   # samphaṃ palapeyya «nói lời phù phiếm» (ch3 palāpino)
    "sandhiṃ": "nhà", "chindeyya": "đột nhập",     # sandhiṃ chindeyya «đột nhập nhà»
    "nillopaṃ": "cướp bóc", "hareyya": "cướp bóc",  # nillopaṃ hareyya «cướp bóc» (one Vietnamese verb for both)
    "ekāgāriyaṃ kareyya": "cướp một ngôi nhà", "eka": "một",
    "paripanthe": "bên đường", "tiṭṭheyya": "mai phục",
    "dāraṃ": "vợ", "ghātaṃ": "cướp phá", "gāma": "làng", "nigama": "thị trấn",
    "puthujjanassa aññāṇaṃ": "người phàm phu" + GAP + "sự không biết",
    "dhammesu ñāṇaṃ": "biết" + GAP + "hiện tượng",   # of dhammesu aññāṇaṃ «sự không biết về … các hiện tượng»
    "ñāṇa niṭṭhitā": "biết đã hoàn tất",           # of Aññāṇakathā niṭṭhitā «… sự không biết đã hoàn tất»
    # ---- 5-317 sutta quotes «Ta nói sự diệt tận các ô nhiễm là cho người biết, cho người thấy … sự phát sinh của
    # vật chất … sự biến mất của vật chất … người không hiểu biết trực tiếp, không hiểu biết trọn vẹn, không làm phai
    # nhạt, không dứt bỏ tất cả thì không thể đi đến sự diệt tận khổ đau … tên và họ của những người nữ, người nam …
    # đường đúng và đường sai … tên của cỏ, gỗ và cây rừng»
    "jānato": "người biết", "passato": "người thấy", "āsavānaṃ": "ô nhiễm", "khayaṃ": "sự diệt tận",
    "atthaṅgamo": "sự biến mất", "viññāṇassa": "thức",
    "dukkhasamudayo": "sự phát sinh của khổ đau", "dukkhanirodho": "sự chấm dứt khổ đau",
    "dukkhanirodha": "sự chấm dứt khổ đau", "dukkhanirodhaṃ": "sự chấm dứt khổ đau",
    "dukkhasamudayaṃ": "sự phát sinh của khổ đau",
    "paṭipadā": "cách thực hành",
    "abhijānaṃ": "hiểu biết trực tiếp", "parijānaṃ": "hiểu biết trọn vẹn",   # anabhijānaṃ / aparijānaṃ: positive
    "virājayaṃ": "làm phai nhạt", "pajahaṃ": "dứt bỏ",                       # part (pi-1); also the positive line
    "bhabbo": "có thể", "abhabbo": "không thể",
    "itthi": "người nữ", "purisānaṃ": "người nam", "nāma": "tên", "gottaṃ": "họ", "gotte": "họ",
    "amaggaṃ": "đường sai", "amagge": "đường sai",
    "tiṇa": "cỏ", "kaṭṭha": "gỗ", "vanappatīnaṃ": "cây rừng", "kaṭṭhavanappatīnaṃ": "gỗ và cây rừng",
    "sakkāya": "tự ngã", "diṭṭhī": "quan điểm",
    "sīlabbataparāmāso": "sự hiểu sai lệch về giới hạnh và nghi thức", "parāmāso": "sự hiểu sai lệch",
    "sīlabbataparāmāsaṃ": "sự hiểu sai lệch về giới hạnh và nghi thức", "parāmāsaṃ": "sự hiểu sai lệch",
    "sīlabbata": "giới hạnh và nghi thức", "vataṃ": "nghi thức",
    "saṃyojanāni": "xiềng xích", "pahīyanti": "được dứt bỏ", "saha": "cùng với",
    # ---- 5-318 «sự hoài nghi, sự ám ảnh của hoài nghi, xiềng xích hoài nghi, chướng ngại hoài nghi … sự nghi ngờ về
    # Bậc Đạo Sư»
    "kaṅkhā": "sự nghi ngờ",
    "vicikicchāsaṃyojanaṃ": "xiềng xích hoài nghi", "vicikicchānīvaraṇaṃ": "chướng ngại hoài nghi",
    "vicikicchāpariyuṭṭhānaṃ": "sự ám ảnh của hoài nghi",
    "dhammesu kaṅkhā": "sự nghi ngờ" + GAP + "hiện tượng",
    # ---- 5-321 verses «Khi các hiện tượng thật sự hiện rõ, Nơi vị bà-la-môn nhiệt tâm, đang thiền định; Thì mọi nghi
    # ngờ của vị ấy đều tan biến, Vì vị ấy hiểu rõ hiện tượng cùng với nguyên nhân. … đã biết sự diệt tận của các
    # điều kiện. … Vị ấy đứng vững, xua tan đạo quân của Ma vương, Như mặt trời chiếu sáng bầu trời. Bất cứ nghi ngờ
    # nào, ở đời này hay ở đời sau, Thuộc về mình hay thuộc về người khác; Những người thiền định đều dứt bỏ tất cả,
    # Những người nhiệt tâm, sống đời sống tu hành trong sạch. Những ai đã vượt qua nghi ngờ, giữa các chúng sinh đầy
    # nghi ngờ; Không còn ngờ vực, đã thoát khỏi trói buộc, vật cúng dường cho họ có quả lớn. Sự công bố Giáo Pháp ở
    # đây là như vậy, Ở đó không có đệ tử nào nghi ngờ điều gì; Đấng đã vượt qua dòng lũ, đã cắt đứt hoài nghi, Chúng
    # tôi đảnh lễ Đức Phật, bậc Chiến Thắng, bậc chúa tể của loài người»
    "pātubhavanti": "hiện rõ", "ātāpino": "nhiệt tâm", "jhāyato": "đang thiền định",
    "brāhmaṇassa": "vị bà-la-môn",                 # the text's classifier kept (ch3 sāvakassa «vị đệ tử»)
    "vapayanti": "tan biến", "pajānāti": "hiểu rõ", "hetu": "nguyên nhân",
    "vidhūpayaṃ": "xua tan", "tiṭṭhati": "đứng vững", "senaṃ": "đạo quân",
    "sūriyo": "mặt trời", "suriyova": NDE,         # only in the bracket [khác chính tả (…): suriyova]
    "iva": "Như", "obhāsayaṃ": "chiếu sáng", "antalikkhaṃ": "bầu trời",
    "huraṃ": "ở đời sau",                          # idha vā huraṃ vā «ở đời này hay ở đời sau» (adverb keeps «ở»)
    "saka": "mình", "vediyā": "thuộc về",          # sakavediyā vā paravediyā vā «Thuộc về mình hay thuộc về …»
    "jhāyino": "người thiền định", "pajahanti": "dứt bỏ",
    "brahma": "trong sạch", "cariyaṃ": "đời sống tu hành", "carantā": "sống",
    "samatikkantā": "đã vượt qua", "pāṇisu": "chúng sinh",
    "asaṃsayā": "không còn ngờ vực", "saṃsayā": "ngờ vực",
    "visaṃyuttā": "đã thoát khỏi trói buộc", "mahapphalaṃ": "có quả lớn",
    "pakāsanā": "sự công bố", "kiṃ": "điều gì", "kaṅkhati": "nghi ngờ",
    "nitthiṇṇa": "đã vượt qua", "oghaṃ": "dòng lũ",
    "buddhaṃ": "Đức Phật", "namassāma": "đảnh lễ", "jinaṃ": "bậc Chiến Thắng", "jana": "loài người",
    "indā": "bậc chúa tể",
    "arahatte": "trạng thái A-la-hán",
    # ---- 5-322 «phải được người khác dẫn dắt, phải tin vào người khác, phải dựa vào người khác, bị lệ thuộc vào người
    # khác, không biết, không thấy, mê mờ, không hiểu biết rõ ràng»
    "pattiyo": "phải tin vào", "paccayo": "phải dựa vào", "paṭibaddhabhū": "bị lệ thuộc vào",
    "jānāti": "biết", "sammūḷho": "mê mờ", "asammūḷho": "không mê mờ",
    "sampajāno": "hiểu biết rõ ràng",              # of asampajāno «không hiểu biết rõ ràng» (positive part)
    "arahato paravitāraṇā": _ARA + GAP + _GG,      # «bậc A-la-hán có việc …» (existential «có» = frame)
    "puthujjanassa paravitāraṇā": "người phàm phu" + GAP + _GG,
    # ---- 5-325 verses «Ta sẽ không có khả năng giải thoát Bất cứ người còn nghi hoặc nào ở đời, này Đô-ta-ca; Và khi
    # hiểu biết trực tiếp Giáo Pháp tối thượng, Như vậy, con sẽ vượt qua dòng lũ này» [Kinh Tập 1070 …; Tiểu Nghĩa
    # Thích 33, phần giải thích câu hỏi của thanh niên Đô-ta-ca]
    "sahissāmi": "có khả năng", "pamocanāya": "giải thoát", "kañci": "bất cứ" + GAP + "nào",
    "dhotaka": "Đô-ta-ca", "seṭṭhaṃ": "tối thượng", "taresi": "vượt qua",
    # ---- 5-326 «người đang nhập thành tựu thiền có sự phát ra lời nói … ở mọi nơi … vào mọi lúc … trong mọi thành
    # tựu thiền … sự phát ra cử động thân … có lời nói … có thân»
    "samāpannassa": _DN,                           # the text adds the object «thành tựu thiền» where none is named
    "samāpattīsu": "thành tựu thiền", "samāpattiṃ": "thành tựu thiền",
    "samāpannassa vacībhedo": _DN + GAP + _PRL, "samāpannānaṃ vacībhedo": _DN + GAP + _PRL,
    "bhedo": "sự phát ra", "kāya": "thân","kāyabhedo": "sự phát ra cử động thân",
    "kāyo": "thân", "vācā": "lời nói",
    # ---- 5-327 «trong khi biết là khổ đau, nói ra lời là khổ đau»
    "jānanto": "trong khi biết", "bhāsati": "nói ra", "bhāsanti": "nói ra", "vācaṃ": "lời",
    "vācaṃ bhāsati": "nói ra lời", "vācaṃ bhāsanti": "nói ra lời",
    # ---- 5-328 «Hiểu biết có phạm vi đối tượng là sự thật … Tai có phạm vi đối tượng là âm thanh … sự tụ hợp của hai
    # sự tiếp xúc, hai cảm giác, hai tri giác, hai chủ ý, hai tâm»
    "sacca": "sự thật", "sadda": "âm thanh", "samodhānaṃ": "sự tụ hợp",
    "vedanānaṃ": "cảm giác", "saññānaṃ": "tri giác",
    # ---- 5-329 «người đang nhập thành tựu thiền với đề mục bao trùm là đất … nước … lửa … gió … màu xanh … màu vàng …
    # màu đỏ … màu trắng … lĩnh vực không gian vô tận … thức vô tận … không có gì cả … không phải tri giác cũng không
    # phải không tri giác … thành tựu thiền thuộc thế gian … tầng thiền thứ nhất thuộc thế gian … tầng thiền thứ tư»
    "pathavīkasiṇaṃ": "đề mục bao trùm là đất", "pathavī": "đất",
    "āpo": "nước", "tejo": "lửa", "vāyo": "gió",
    "nīla": "màu xanh", "lohita": "màu đỏ", "odāta": "màu trắng",
    "ākāsa": "không gian", "ānañca": "vô tận", "ākāsānañca": "không gian vô tận",
    "viññāṇañca": "thức vô tận", "viññāṇa": "thức",
    "ākiñcañña": "không có gì cả", "ākiñcaññāyatanaṃ": "lĩnh vực không có gì cả",
    "nevasaññānāsaññā": "không phải tri giác cũng không phải không tri giác",
    "asaññā": "không tri giác",                    # of nāsaññā «không phải không tri giác» (own a- kept)
    "saññā": "tri giác",
    "nevasaññānāsaññāyatanaṃ samāpannassa": _DN + " lĩnh vực không phải tri giác cũng không phải không tri giác",
    "samāpattiṃ samāpannassa": _DN + " thành tựu thiền",
    "catutthaṃ samāpannassa": _DN + GAP + "thứ tư",
    "catutthaṃ jhānaṃ": "tầng thiền thứ tư", "jhānaṃ": "tầng thiền",
    "jhānaṃ vacībhedo": "tầng thiền" + GAP + _PRL,
    "lokiya": "thuộc thế gian", "lokiyaṃ": "thuộc thế gian", "lokiye": "thuộc thế gian",
    "lokiyasamāpattiṃ": "thành tựu thiền thuộc thế gian",
    "lokiyaṃ jhānaṃ": "tầng thiền" + GAP + "thuộc thế gian",
    # ---- 5-330 / 5-331 «tầng thiền thứ nhất vượt thế gian»
    "lokuttaraṃ": "vượt thế gian", "lokuttaro": "vượt thế gian", "lokuttarena": "vượt thế gian",
    "lokuttaraṃ jhānaṃ": "tầng thiền" + GAP + "vượt thế gian",
    # ---- 5-332 «Đức Thế Tôn đã nói rằng sự hướng tâm và sự duy trì tâm là các sự tạo tác bằng lời nói … lời nói có
    # nguồn gốc từ sự hướng tâm … lời nói có nguồn gốc từ tri giác»
    "vitakkavicārā": "sự hướng tâm và sự duy trì tâm", "vitakka": "sự hướng tâm", "vicārā": "sự duy trì tâm",
    "vacīsaṅkhārā": "sự tạo tác bằng lời nói",     # «là các sự tạo tác bằng lời nói» («các» dropped)
    "vitakkavicārā vacīsaṅkhārā": "sự hướng tâm và sự duy trì tâm là các sự tạo tác bằng lời nói",
    "jhānaṃ vitakkavicārā": "tầng thiền" + GAP + "sự hướng tâm và sự duy trì tâm",
    "samuṭṭhānā": "có nguồn gốc từ",
    # ---- 5-333 «đối với người đang nhập tầng thiền thứ nhất, lời nói đã chấm dứt … sự hân hoan … hơi thở vào và hơi
    # thở ra … tri giác về hình sắc … sự chấm dứt tri giác và cảm giác … âm thanh là cái gai của tầng thiền thứ nhất
    # [câu hỏi dựa trên Kinh Cái Gai …]» and the verses of Abhibhū «vị đệ tử tên là A-tỳ-phù của Đức Thế Tôn Thi-khí,
    # bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn, đứng ở cõi Phạm Thiên, đã dùng giọng nói làm cho mười nghìn thế giới
    # nghe biết – ‘Hãy khởi sự, hãy tiến bước, hãy chuyên chú vào giáo huấn của Đức Phật; Hãy đánh tan đạo quân của
    # Thần Chết, như voi phá ngôi nhà bằng lau sậy. Ai trong Giáo Pháp và Giới Luật này, sẽ sống không buông lung;
    # Sau khi dứt bỏ vòng luân hồi của sự sinh, sẽ đi đến tận cùng của khổ đau’» [Tăng Chi Bộ Kinh 1, trong Chương Ba
    # Pháp; …]
    "niruddhā": "đã chấm dứt", "pīti": "sự hân hoan", "assāsapassāsā": "hơi thở vào và hơi thở ra",
    "ākāsānañcāyatanaṃ samāpannassa": _DN + " lĩnh vực không gian vô tận",
    "saññāvedayitanirodhaṃ": "sự chấm dứt tri giác và cảm giác", "saññāvedayita": "tri giác và cảm giác",
    "vedayita": "cảm giác", "nirodhaṃ": "sự chấm dứt",
    "saññāvedayitanirodhaṃ samāpannassa": _DN + " sự chấm dứt tri giác và cảm giác",
    "saddo": "âm thanh", "kaṇḍako": "cái gai", "pucchati": "câu hỏi",   # [… nissāya pucchati] «[câu hỏi dựa trên …]»
    "sikhissa bhagavato": "Đức Thế Tôn Thi-khí",   # honorific with its noun, Vietnamese order
    "sambuddhassa": "bậc Tự Giác Ngộ", "sammāsambuddhassa": "bậc Tự Giác Ngộ Hoàn Toàn",
    "sāvako": "vị đệ tử", "ṭhito": "đứng",         # brahmaloke ṭhito «đứng ở cõi Phạm Thiên»
    "dasasahassi": "mười nghìn", "sarena": "giọng nói", "viññāpesi": "làm cho" + GAP + "nghe biết",
    "ārabbhatha": "Hãy khởi sự", "nikkamatha": "hãy tiến bước", "yuñjatha": "hãy chuyên chú",
    "buddha": "Đức Phật", "sāsane": "giáo huấn",
    "dhunātha": "Hãy đánh tan", "maccuno": "Thần Chết", "naḷa": "lau sậy", "āgāraṃ": "ngôi nhà",
    "kuñjaro": "voi", "yo": "Ai", "vinaye": "Giới Luật", "appamatto": "không buông lung",
    "vihassati": "sống", "vihessati": NDE, "viharissati": NDE,   # only in [khác chính tả (…): vihessati; dị bản (Ka.): …]
    "pahāya": "Sau khi dứt bỏ", "jāti": "sự sinh", "saṃsāraṃ": "vòng luân hồi",
    "dukkhassantaṃ": "tận cùng của khổ đau", "dukkhassa": "khổ đau",
    "tika": "Ba Pháp", "nipāte": "Chương",         # tikanipāte «Chương Ba Pháp»
    # ---- 5-334 «việc nêu lên khổ đau là chi phần của con đường … nói ra lời là khổ đau, tất cả họ đều tu tập con
    # đường … những người phàm phu ngu si … kẻ giết mẹ… kẻ giết cha… kẻ giết bậc A-la-hán… kẻ làm chảy máu
    # [dị bản (Sī., Ka.): lohituppādako; nhưng ở những chỗ khác chỉ thấy ruhiruppādako]… kẻ chia rẽ Tăng đoàn»
    "aṅgaṃ": "chi phần", "maggaṃ bhāventi": "tu tập con đường", "bhāventi": "tu tập",
    "bāla": "ngu si", "ghātako": "kẻ giết", "uppādako": "kẻ làm chảy", "bhedako": "kẻ chia rẽ",
    "aññaṭṭhānesu": "chỗ khác", "dissati": "thấy",   # translated note after the colon (ALLOWED)
    # ---- 5-335 «một tâm duy trì suốt một ngày … nửa ngày là khoảnh khắc sinh khởi, … khoảnh khắc suy tàn … mười,
    # hai mươi, ba mươi, bốn mươi, năm mươi năm, một trăm năm … một nghìn năm … mười sáu nghìn năm … một kiếp …
    # mười sáu kiếp … ba mươi hai kiếp … sáu mươi bốn kiếp … năm trăm kiếp … hàng nghìn kiếp … hai mươi nghìn kiếp …
    # bốn mươi nghìn kiếp … sáu mươi nghìn kiếp … tám mươi bốn nghìn kiếp … bốn mươi hai nghìn kiếp»
    "ekaṃ": "một", "ekaṃ cittaṃ": "một tâm",
    "divaso": "ngày", "uppāda": "sinh khởi", "vaya": "suy tàn", "khaṇo": "khoảnh khắc",
    "divaso uppādakkhaṇo": "ngày là khoảnh khắc sinh khởi",
    "dasa": "mười", "vīsati": "hai mươi", "tiṃsa": "ba mươi", "cattārīsa": "bốn mươi", "paññāsa": "năm mươi",
    "saṭṭhi": "sáu mươi", "caturāsīti": "tám mươi bốn", "dvecattārīsa": "bốn mươi hai",
    "soḷasa": "mười sáu", "bāttiṃsa": "ba mươi hai", "catusaṭṭhi": "sáu mươi bốn",
    "sataṃ": "trăm", "sahassaṃ": "nghìn", "sahassāni": "nghìn",
    "vassasataṃ": "một trăm năm", "vassasahassaṃ": "một nghìn năm",
    "soḷasa vassasahassāni": "mười sáu nghìn năm", "soḷasa sahassāni": "mười sáu nghìn",
    "vīsati sahassāni": "hai mươi nghìn",
    "kappaṃ": "kiếp", "kappe": "kiếp", "kappa": "kiếp", "kappassa": "kiếp",
    "soḷasa kappe": "mười sáu kiếp", "bāttiṃsa kappe": "ba mươi hai kiếp", "catusaṭṭhi kappe": "sáu mươi bốn kiếp",
    "kappasatāni": "trăm kiếp", "kappasahassāni": "nghìn kiếp",
    "soḷasa kappasahassāni": "mười sáu nghìn kiếp", "vīsati kappasahassāni": "hai mươi nghìn kiếp",
    "cattārīsa kappasahassāni": "bốn mươi nghìn kiếp", "dvecattārīsa kappasahassāni": "bốn mươi hai nghìn kiếp",
    "bahuṃ": "nhiều lần", "uppajjitvā": "sinh khởi rồi", "nirujjhanti": "chấm dứt", "nirujjhati": "chấm dứt",
    "lahu": "nhanh", "dhammā lahuparivattā": "hiện tượng" + GAP + "thay đổi nhanh",
    "lahuparivattaṃ cittaṃ": "tâm thay đổi nhanh",
    "upamā": "ví dụ", "sukarā": "dễ",             # upamāpi na sukarā «ngay cả một ví dụ cũng không dễ đưa ra»
    "makkaṭo": "con khỉ", "araññe": "rừng", "pavane": "khu rừng rậm", "vane": "rừng rậm",
    "caramāno": "đi lang thang", "sākhaṃ": "cành cây", "gaṇhati": "nắm lấy", "muñcitvā": "buông" + GAP + "ra",
    "mano": "ý", "rattiyā": "đêm",
    # ---- 5-336 «thức qua mắt … tâm bất thiện… đi kèm với sự tham đắm… sự kiêu mạn … sự uể oải … với chính tâm mà
    # người ta thấy hình sắc bằng mắt … đi tới … đi lui … nhìn thẳng … nhìn quanh … co … duỗi»
    "akusalaṃ cittaṃ": "tâm bất thiện", "sahagataṃ": "đi kèm", "sahagataṃ cittaṃ": "tâm đi kèm",
    "māna": "sự kiêu mạn", "thina": "sự uể oải", "uddhacca": "sự xao động", "ahirika": "sự không biết hổ thẹn",
    "cakkhunā": "mắt", "sotena": "tai", "ghānena": "mũi", "jivhāya": "lưỡi", "kāyena": "thân",
    "abhikkamati": "đi tới", "āloketi": "nhìn thẳng", "viloketi": "nhìn quanh",
    "samiñjeti": "co", "pasāreti": "duỗi",
    # ---- 5-337 «một tâm của chư thiên sinh vào lĩnh vực không gian vô tận duy trì suốt tuổi thọ … chư thiên Tứ Đại
    # Thiên Vương … Ba Mươi Ba … Đâu Suất … Hóa Lạc … Tha Hóa Tự Tại … Phạm Chúng … Phạm Phụ … Đại Phạm … Thiểu Quang
    # … Vô Lượng Quang … Quang Âm … Thiểu Tịnh … Vô Lượng Tịnh … Biến Tịnh … Quảng Quả … Vô Phiền … Vô Nhiệt … Thiện
    # Hiện … Sắc Cứu Cánh … một phần ba của kiếp … nửa kiếp … chốc chốc lại sinh khởi, chốc chốc lại chấm dứt …
    # chốc chốc lại chết đi»
    "upagānaṃ": "sinh vào", "devānaṃ": "chư thiên", "upagānaṃ devānaṃ": "chư thiên sinh vào",
    "manussānaṃ": "loài người", "yāvata": "suốt", "āyukaṃ": "tuổi thọ",
    "mahārājikānaṃ": "Đại Thiên Vương", "rājikānaṃ": "Thiên Vương", "tāvatiṃsānaṃ": "Ba Mươi Ba",
    "tusitānaṃ": "Đâu Suất", "nimmāna": "Hóa", "ratīnaṃ": "Lạc",
    "nimmita": "Hóa", "vasa": "Tự Tại", "vattīnaṃ": "Tự Tại",   # paranimmitavasavattī «Tha Hóa Tự Tại» (para: context)
    "pārisajjānaṃ": "Chúng", "purohitānaṃ": "Phụ",  # brahmapārisajjā / brahmapurohitā «Phạm Chúng / Phạm Phụ»
    "brahmānaṃ devānaṃ": "chư thiên" + GAP + "Phạm",   # member of mahābrahmānaṃ «chư thiên Đại Phạm»
    "mahābrahmānaṃ devānaṃ": "chư thiên Đại Phạm",
    "paritta": "Thiểu", "appamāṇa": "Vô Lượng", "ābhānaṃ": "Quang", "ābhassarānaṃ": "Quang Âm",
    "subhānaṃ": "Tịnh", "kiṇhānaṃ": "Biến", "vehapphalānaṃ": "Quảng Quả", "phalānaṃ": "Quả",
    "avihānaṃ": "Vô Phiền", "atappānaṃ": "Vô Nhiệt", "sudassānaṃ": "Thiện Hiện",
    "akaniṭṭhānaṃ devānaṃ": "chư thiên Sắc Cứu Cánh",
    "muhuttaṃ": "chốc chốc", "cavanti": "chết đi",
    # ---- 5-338 «tất cả các tạo tác, không trừ ra phần nào, đều là tro nóng … cảm giác dễ chịu, hạnh phúc thuộc thân,
    # hạnh phúc thuộc tâm, hạnh phúc cõi trời, … do lợi lộc, do được kính trọng, do xe cộ, do giường nằm, do quyền uy,
    # do quyền thống trị, của người tại gia, của đời sống sa-môn, … còn chấp trước, không còn chấp trước, có tính trần
    # tục, không có tính trần tục, có sự hân hoan, … của tầng thiền, của sự giải thoát, dục lạc, của sự từ bỏ, của sự
    # tách biệt, của sự an tịnh, của sự giác ngộ»
    "odhiṃ": "trừ ra phần nào",                    # of anodhiṃ katvā «không trừ ra phần nào» (positive part)
    "sukhā vedanā": "cảm giác dễ chịu", "sukhā": "dễ chịu",
    "kāyikaṃ": "thuộc thân", "cetasikaṃ": "thuộc tâm",
    "dibbaṃ sukhaṃ": "hạnh phúc cõi trời", "mānusakaṃ sukhaṃ": "hạnh phúc cõi người",
    "sakkāra": "được kính trọng", "yāna": "xe cộ", "sayana": "giường nằm", "issariya": "quyền uy",
    "ādhipacca": "quyền thống trị", "gihi": "người tại gia", "sāmañña": "đời sống sa-môn",
    "upadhi": "chấp trước",                        # upadhisukhaṃ «hạnh phúc còn chấp trước» (no sa- in the keyword: no
    "nirūpadhi": "không còn chấp trước",           # «còn», as ch5 rajaṃ)
    "sāmisaṃ": "có tính trần tục", "nirāmisaṃ": "không có tính trần tục", "pītikaṃ": "có sự hân hoan",
    "jhāna": "tầng thiền", "vimutti": "sự giải thoát", "nekkhamma": "sự từ bỏ", "viveka": "sự tách biệt",
    "upasama": "sự an tịnh", "sambodha": "sự giác ngộ",
    "dukkhā vedanā": "cảm giác khó chịu", "dukkhā": "khó chịu",
    "soka": "sự sầu muộn", "parideva": "sự than khóc", "domanassa": "nỗi buồn", "upāyāsā": "sự tuyệt vọng",
    # sutta «tất cả đều đang bốc cháy … mắt đang bốc cháy, các hình sắc …, thức qua mắt …, sự tiếp xúc của mắt …;
    # điều được cảm nhận nào sinh khởi do sự tiếp xúc của mắt làm điều kiện … lửa tham đắm, lửa sân hận, lửa si mê …
    # ý thức …, sự tiếp xúc của ý»
    "ādittaṃ": "đang bốc cháy", "rūpā": "hình sắc", "cakkhuviññāṇaṃ": "thức qua mắt",
    "cakkhusamphasso": "sự tiếp xúc của mắt", "manosamphasso": "sự tiếp xúc của ý", "manoviññāṇaṃ": "ý thức",
    "yamidaṃ": "nào", "vedayitaṃ": "điều được cảm nhận", "agginā": "lửa",
    "sotaṃ": "tai", "saddā": "âm thanh", "ghānaṃ": "mũi", "gandhā": "mùi", "jivhā": "lưỡi", "rasā": "vị",
    "phoṭṭhabbā": "vật xúc chạm",
    # sutta «năm loại dục lạc … Các hình sắc được nhận biết bằng mắt, đáng mong muốn, đáng yêu mến, đáng ưa thích, có
    # vẻ đáng yêu, gắn liền với dục lạc, hấp dẫn»
    "kāmaguṇā": "loại dục lạc", "guṇā": "loại",
    "cakkhuviññeyyā rūpā": "hình sắc được nhận biết bằng mắt", "viññeyyā": "được nhận biết",
    "iṭṭhā": "đáng mong muốn", "kantā": "đáng yêu mến", "manāpā": "đáng ưa thích", "piyarūpā": "có vẻ đáng yêu",
    "kāmūpasaṃhitā": "gắn liền với dục lạc", "upasaṃhitā": "gắn liền", "rajanīyā": "hấp dẫn",
    # sutta «các ông đã khéo được lợi, thời cơ để sống đời sống tu hành trong sạch đã được các ông nắm lấy … các địa
    # ngục có tên gọi là sáu lĩnh vực tiếp xúc … các cõi trời …»
    "suladdhaṃ": "đã khéo được lợi",               # paṭiladdho «đã được … nắm lấy»: override ^5-338
    "brahmacariya": "đời sống tu hành trong sạch", "cariya": "đời sống tu hành", "vāsāya": "sống",
    "phassa": "tiếp xúc", "āyatanikā": "lĩnh vực", "nirayā": "địa ngục", "saggā": "cõi trời",
    "aniṭṭha": "không đáng mong muốn", "akanta": "không đáng yêu mến", "amanāpa": "không đáng ưa thích",
    "gandhaṃ": "mùi", "rasaṃ": "vị", "phoṭṭhabbaṃ": "vật xúc chạm", "saddaṃ": "âm thanh",
    # «sự bố thí có kết quả không đáng mong muốn … có kết quả pha tạp, đưa đến sự khó chịu … đưa đến sự dễ chịu, có
    # quả trổ dễ chịu … giới hạnh… sự hành trì ngày trai giới…»
    "dānaṃ": "sự bố thí", "phalaṃ": "kết quả", "udrayaṃ": "đưa đến",   # (phalaṃ «thành quả»: context10)
    "sukhudrayaṃ sukhavipākaṃ": "đưa đến sự dễ chịu có quả trổ dễ chịu",   # comma dropped (pi-1)
    "sīlaṃ": "giới hạnh", "uposatho": "sự hành trì ngày trai giới",
    # verses «Hạnh phúc là sự tách biệt của người biết đủ, người đã nghe Giáo Pháp, người thấy rõ; Hạnh phúc là không
    # ác ý ở đời, là sự chế ngự đối với các loài hữu tình. Hạnh phúc là sự lìa tham ở đời, là sự vượt qua các dục
    # lạc; Sự điều phục kiêu mạn cho rằng có tôi, đó thật là hạnh phúc tối thượng. … đó là hạnh phúc tuyệt đối; Ba loại
    # hiểu biết chân thật đã được chứng đạt …»
    "sukho": "Hạnh phúc", "viveko": "sự tách biệt", "tuṭṭhassa": "người biết đủ", "suta": "đã nghe",
    "dhammassa": "Giáo Pháp", "abyāpajjaṃ": "không ác ý", "byāpajjaṃ": "ác ý",
    "bhūtesu": "loài hữu tình", "saṃyamo": "sự chế ngự",
    "kāmānaṃ": "dục lạc", "samatikkamo": "sự vượt qua", "vinayo": "sự điều phục",
    "ve": "thật", "paramaṃ": "tối thượng", "accanta": "tuyệt đối",
    "vijjā": "hiểu biết chân thật", "anuppattā": "đã được chứng đạt",
    # ---- 5-339 «có sự thấu hiểu tuần tự … tu tập con đường vào dòng một cách tuần tự … tự mình chứng nghiệm thành
    # quả A-la-hán …»
    "anupubba": "tuần tự", "anupubbena": "một cách tuần tự",
    "maggaṃ bhāveti": "tu tập con đường", "bhāveti": "tu tập",
    "sotāpattimaggaṃ": "con đường vào dòng", "sakadāgāmimaggaṃ": "con đường trở lại một lần",
    "anāgāmimaggaṃ": "con đường không trở lại", "arahattamaggaṃ": "con đường A-la-hán",
    "sotāpattimaggo": "con đường vào dòng", "sakadāgāmimaggo": "con đường trở lại một lần",
    "anāgāmimaggo": "con đường không trở lại", "arahattamaggo": "con đường A-la-hán",
    "arahattaphalaṃ": "thành quả A-la-hán",
    "phalaṃ sacchikaroti": "tự mình chứng nghiệm thành quả", "sacchikaroti": "tự mình chứng nghiệm",
    # ---- 5-340 … 5-343 «dứt bỏ một phần tư quan điểm về tự ngã, sự hoài nghi, sự hiểu sai lệch … một phần tư là bậc
    # vào dòng … đã đạt đến thành quả vào dòng … người tái sinh tối đa bảy lần, người đi từ gia đình này sang gia
    # đình khác, người có một hạt giống, có niềm tin trong sáng không lay chuyển nơi Đức Phật …» (ch3 ^5-274 …)
    "catubhāgaṃ": "một phần tư", "catubhāgaṃ jahati": "dứt bỏ một phần tư",
    "catubhāgaṃ sakadāgāmī": "một phần tư là bậc trở lại một lần",   # inner «là» kept (ch3 Ekadesaṃ X)
    "catubhāgaṃ vītarāgo": "một phần tư đã lìa tham đắm",
    "patto": "đã đạt đến", "buddhe": "Đức Phật",   # «nơi Đức Phật» (ch5 «vị Phật» where the text says so)
    "kolaṅkolo": "người đi từ gia đình này sang gia đình khác",
    "vicikicchaṃ": "sự hoài nghi", "diṭṭhiṃ": "quan điểm",
    "sotāpanno": "bậc vào dòng", "sakadāgāmī": "bậc trở lại một lần", "anāgāmī": "bậc không trở lại",
    "arahā": _ARA,
    "puggalo": "người", "paṭipanno puggalo": "người đang thực hành", "paṭipanno": "đang thực hành",
    "sacchikiriyāya": "tự mình chứng nghiệm",
    "sotāpattiphala": "thành quả vào dòng", "phala": "thành quả", "upasampajja": "chứng nhập",
    "sotāpattiphalappatto sacchikato": "đã đạt đến thành quả vào dòng" + GAP + "đã tự mình chứng nghiệm",
    "sakadāgāmiphalappatto sacchikato": "đã đạt đến thành quả trở lại một lần" + GAP + "đã tự mình chứng nghiệm",
    "anāgāmiphalappatto sacchikato": "đã đạt đến thành quả không trở lại" + GAP + "đã tự mình chứng nghiệm",
    "arahattappatto sacchikato": "đã đạt đến trạng thái A-la-hán" + GAP + "đã tự mình chứng nghiệm",
    "oḷārikaṃ": "ở dạng thô", "oḷārikaṃ byāpādaṃ": "ác ý ở dạng thô", "byāpādaṃ": "ác ý",
    "akaniṭṭha": "cõi Sắc Cứu Cánh", "parinibbāyī": "nhập Niết-bàn trọn vẹn",
    "upahacca": "khi gần mạng chung",              # pi-4 («khi gần» only where kālakiriyaṃ has its own keyword)
    "anāgāmiphalasacchikiriyāya jahati": "tự mình chứng nghiệm thành quả không trở lại" + GAP + "dứt bỏ",
    "arahattasacchikiriyāya": "tự mình chứng nghiệm trạng thái A-la-hán",
    "mānaṃ": "sự kiêu mạn",
    # ---- 5-344 «trong khi thấy khổ đau, nên gọi là người đang thực hành … người đã đứng vững trong thành quả …
    # việc thấy khổ đau là vô ích» [dấu hiệu câu hỏi của người theo học thuyết của chúng ta]
    "dakkhanto": "trong khi thấy", "phale": "thành quả", "niratthiyaṃ": "vô ích",
    "lakkhaṇaṃ": "dấu hiệu", "samudayaṃ": "sự phát sinh", "maggaṃ": "con đường",
    # ---- 5-345 «khi khổ đau đã được thấy, bốn sự thật đã được thấy … sự thật về khổ đau … khi khối vật chất đã được
    # thấy là vô thường, năm khối … lĩnh vực mắt … mười hai lĩnh vực nhận biết … yếu tố mắt … mười tám yếu tố … năng
    # lực mắt … hai mươi hai năng lực … bằng bốn hiểu biết … bốn mươi bốn … bảy mươi bảy»
    "dukkhe": "khổ đau", "saccaṃ": "sự thật", "dukkhasaccaṃ": "sự thật về khổ đau", "saccāni": "sự thật",
    "rūpakkhandhe": "khối vật chất", "khandhe": "khối", "khandhā": "khối", "aniccato": "là vô thường",
    "cakkhāyatane": "lĩnh vực mắt", "āyatanāni": "lĩnh vực nhận biết", "dvādasa": "mười hai",
    "cakkhudhātuyā": "yếu tố mắt", "dhātuyā": "yếu tố", "dhātuyo": "yếu tố", "aṭṭhārasa": "mười tám",
    "cakkhundriye": "năng lực mắt", "indriye": "năng lực", "indriyāni": "năng lực", "bāvīsati": "hai mươi hai",
    "cakkhu": "mắt", "ñāṇehi": "hiểu biết",
    "phalāni": "thành quả", "sotāpattiphalāni": "thành quả vào dòng",
    "catucattārīsa": "bốn mươi bốn", "sattasattati": "bảy mươi bảy",
    # ---- 5-346 sutta «ví như đại dương dần dần thấp xuống, dần dần nghiêng xuống, dần dần dốc xuống, không đột ngột
    # là vực thẳm … trong Giáo Pháp và Giới Luật này, có sự tu học tuần tự …, không có sự thấu triệt hiểu biết trọn
    # vẹn một cách đột ngột» … «Người trí, dần dần theo thứ tự, từng chút một, trong từng khoảnh khắc; Như người thợ
    # luyện bạc, hãy gột sạch cấu uế của chính mình» … «tôn giả trưởng lão Kiều-phạm-ba-đề … Này các hiền giả, điều
    # này tôi đã được nghe trực tiếp từ Đức Thế Tôn …»
    "samuddo": "đại dương", "ninno": "thấp xuống", "poṇo": "nghiêng xuống", "pabbhāro": "dốc xuống",
    "āyatakena": "đột ngột", "sikkhā": "sự tu học", "paṭivedho": "sự thấu triệt",
    "khaṇe": "khoảnh khắc", "rajatassa": "bạc",
    "gavampati": "Kiều-phạm-ba-đề", "āvuso": "hiền giả", "sammukhā": "trực tiếp", "sutaṃ": "đã được nghe",
    "bhagavato": "Đức Thế Tôn",                    # «từ Đức Thế Tôn», «Đức Phật, Đức Thế Tôn» (KV «Thế Tôn» only in
                                                   # «Đức Phật Thế Tôn»)
    # ---- 5-347 … 5-352 «lời nói của Đức Phật, Đức Thế Tôn vượt thế gian … va chạm vào tai vượt thế gian … người ta
    # nhận biết rõ bằng thức vượt thế gian … các đệ tử nhận biết rõ, không phải những người phàm phu»
    "sote": "tai", "viññāṇena": "thức", "paṭivijānanti": "nhận biết rõ", "sāvakā": "đệ tử",
    "puthujjanā paṭivijānanti": "người phàm phu nhận biết rõ",
    "vohāraṃ paṭivijānanti": "nhận biết rõ lời nói",
    "viññeyyo": "được nhận biết", "sota": "tai",
    "bojjhaṅgo": "chi phần giác ngộ", "aṅgo": "chi phần", "padhānaṃ": "nỗ lực",
    "suṇanti": "nghe", "vohāraṃ suṇanti": "nghe lời nói",
    "lokuttaro dhammo": "hiện tượng vượt thế gian",
    # 5-349 «có thể tham đắm vào lời nói … khơi dậy sự tham đắm, hấp dẫn, đáng ham muốn, làm say đắm, trói buộc, làm mê
    # mẩn … sân hận … khơi dậy sự sân hận, khơi dậy sự phẫn nộ, khơi dậy sự ác cảm … si mê … khơi dậy sự si mê, tạo ra
    # sự không biết, làm cho không có mắt, làm chấm dứt trí tuệ, thuộc về phía gây phiền não, không dẫn đến Niết-bàn»
    "rajjeyyuṃ": "tham đắm", "rajanīyo": "hấp dẫn", "kamanīyo": "đáng ham muốn", "madanīyo": "làm say đắm",
    "bandhanīyo": "trói buộc", "mucchanīyo": "làm mê mẩn",
    "dusseyyuṃ": "sân hận", "dosaṭṭhāniyo": "khơi dậy sự sân hận", "kopaṭṭhāniyo": "khơi dậy sự phẫn nộ",
    "kopa": "sự phẫn nộ", "paṭigha": "sự ác cảm",
    "muyheyyuṃ": "si mê", "mohaṭṭhāniyo": "khơi dậy sự si mê",
    "karaṇo": "tạo ra",                            # aññāṇakaraṇo «tạo ra sự không biết» (first; acakkhukaraṇo «làm cho»)
    "acakkhu": "không có mắt", "paññā": "trí tuệ", "nirodhiko": "làm chấm dứt",
    "vighāta": "gây phiền não", "avighāta": "không" + GAP + "gây phiền não", "pakkhiko": "thuộc về phía",
    "saṃvattaniko": "dẫn đến",
    # 5-350 «những người phàm phu ngu si nghe lời nói …»
    "suṇāti": "nghe",
    # 5-351 «có thể dùng cây gậy bằng vàng để chỉ cả đống lúa lẫn đống vàng … Đức Thế Tôn dùng lời nói vượt thế gian để
    # nói về cả hiện tượng thuộc thế gian lẫn hiện tượng vượt thế gian … cây gậy bằng gỗ thầu dầu»
    "buddhassa": "Đức Phật",                       # Buddhassa bhagavato «Đức Phật, Đức Thế Tôn»
    "sovaṇṇamayāya": "bằng vàng", "elaṇḍiyāya": "bằng gỗ thầu dầu", "laṭṭhiyā": "cây gậy", "puñjo": "đống",
    "bhagavā": "Đức Thế Tôn", "voharati": "nói về", "voharantassa": "khi nói về",
    "lokuttarena vohārena": "lời nói vượt thế gian",
    "lokiyaṃ lokuttaraṃ": "thuộc thế gian" + GAP + "vượt thế gian",
    "bhagavā voharati": "Đức Thế Tôn nói về",
    # 5-352 «lời nói … khi nói về điều thuộc thế gian thì thuộc thế gian … khi nói về con đường thì là con đường …»
    "vohāro lokiyo": "lời nói" + GAP + "thuộc thế gian",
    "vedanaṃ": "cảm giác", "saññaṃ": "tri giác",
    # ---- 5-353 «hai sự chấm dứt … hai sự thật về sự chấm dứt … hai nơi che chở… hai nơi ẩn náu… hai nơi nương tựa…
    # hai nơi đến cuối cùng… hai điều bất biến… hai điều bất tử… hai Niết-bàn … sự cao thấp, sự thấp kém và ưu việt,
    # sự hơn kém, hoặc ranh giới, hoặc sự phân chia, hoặc đường vạch, hoặc khoảng cách … người ta làm chấm dứt do suy
    # xét những tạo tác đã chấm dứt không do suy xét … bị phá vỡ hoàn toàn … nhờ con đường cao quý … không sinh khởi
    # lại» + the summary verse
    "nirodhā": "sự chấm dứt", "nirodhasaccāni": "sự thật về sự chấm dứt",
    "tāṇāni": "nơi che chở", "leṇāni": "nơi ẩn náu", "saraṇāni": "nơi nương tựa", "parāyaṇāni": "nơi đến cuối cùng",
    "accutāni": "điều bất biến", "amatāni": "điều bất tử",
    "hīna": "thấp kém", "paṇīta": "ưu việt", "avakaṃso": "kém",   # ukkaṃsāvakaṃso «sự hơn kém»
    "sīmā": "ranh giới", "rāji": "đường vạch", "antarikā": "khoảng cách",
    "paṭisaṅkhā": "do suy xét", "nirodhenti": "làm chấm dứt", "niruddhe": "đã chấm dứt",
    "bhaggā": "bị phá vỡ", "ariyamaggaṃ": "con đường cao quý",
    "puna": "lại", "uppajjanti": "sinh khởi",      # na puna uppajjanti «không sinh khởi lại»
    "uddānaṃ": "Tóm tắt", "vaggo": "Chương",
}

PRIOR = {**map_7_vi.T7, **map_6_vi.T6, **map_5_vi.T5, **map_4_vi.T4, **map_2_vi.T2, **map_3_vi.T3, **T10}


def context10(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "dhamma":              # sadhammakusala «thông thạo các hiện tượng của mình» / dhammacakkhu, dhammavinaya,
        if any(x.startswith("sadhammakusal") for x in s):          # dhammañca seṭṭhaṃ «Giáo Pháp»
            return "hiện tượng"
        return "Giáo Pháp"
    if k == "samudaya":            # samudayadhammaṃ «có bản chất phát sinh» (ch3 ^5-278) / «sự phát sinh»
        return "phát sinh" if "nirodhadhammaṃ" in s else "sự phát sinh"
    if k == "ariya":               # ariyasāvaka / ariyamagga «cao quý» / ariyakantehi sīlehi «các bậc thánh»
        return "bậc thánh" if "ariyakantehi sīlehi" in s else "cao quý"
    if k == "magga":               # maggāmaggaṃ «đường đúng và đường sai» / «con đường»
        return "đường đúng" if s & {"amaggaṃ", "amagge"} else "con đường"
    if k in ("ñāṇaṃ", "ñāṇa"):     # of aññāṇa «sự không biết» (positive part) / «hiểu biết» (5-328 Ñāṇaṃ)
        return "biết" if s & {"aññāṇaṃ", "aññāṇa"} else "hiểu biết"
    if k == "pīta":                # asitapīta «đã uống» / pītakasiṇa «màu vàng»
        return "màu vàng" if "nīla" in s else "đã uống"
    if k == "phalaṃ":              # iṭṭhaphalaṃ … «có kết quả …» (5-338) / «thành quả»
        return "kết quả" if "dānaṃ" in s else "thành quả"
    if k == "uppāda":              # anuppādadhammo «không nảy sinh» (ch2) / uppādakkhaṇo «khoảnh khắc sinh khởi»
        return "nảy sinh" if "anabhāvaṅkato" in s else "sinh khởi"
    if k == "uppajjati":           # «sinh khởi» (citta, vedayita) / «sinh ra»
        return pick(text, "sinh khởi", "sinh ra")
    if k in ("rāga", "dosa", "moha"):   # «sự tham đắm …» / «lửa tham đắm, lửa sân hận, lửa si mê» (5-338)
        noun = {"rāga": "tham đắm", "dosa": "sân hận", "moha": "si mê"}[k]
        return pick(text, "sự " + noun, noun)
    if k == "dhammaṃ":             # the āyatana list «đối tượng của ý» / «hiện tượng»
        return pick(text, "đối tượng của ý", "hiện tượng")
    if k == "sacchikato":          # «đã tự mình chứng nghiệm» (ch3) / the arahant formula «đã được …» (ch2)
        return pick(text, "đã tự mình chứng nghiệm", _DTT)
    if k == "accanta":             # accantasukhaṃ «hạnh phúc tuyệt đối» / accantabhaggā «bị phá vỡ hoàn toàn»
        return pick(text, "tuyệt đối", "hoàn toàn")
    if k == "arahatta":            # arahattasacchikiriyāya «trạng thái A-la-hán» / arahattamagga «con đường A-la-hán»
        return pick(text, "trạng thái A-la-hán", "A-la-hán")
    if k == "khaṇo":               # uppādakkhaṇo «khoảnh khắc sinh khởi» / khaṇo vo paṭiladdho «thời cơ»
        return pick(text, "khoảnh khắc", "thời cơ")
    if k == "māna":                # mānasahagataṃ «đi kèm với sự kiêu mạn» / asmimāna «kiêu mạn cho rằng có tôi»
        return pick(text, "sự kiêu mạn", "kiêu mạn")
    return None


OVERRIDES = {
    "5-321": {"dhamma": "hiện tượng"},             # sahetudhammaṃ «hiện tượng cùng với nguyên nhân» (first; also
                                                   # dhammapakāsanā «Giáo Pháp»: CROSSCHECK)
    "5-333": {"rūpa": "hình sắc"},                 # rūpasaññā «tri giác về hình sắc»
    "5-337": {"para": "Tha"},                      # paranimmitavasavattī «Tha Hóa Tự Tại»
    "5-338": {"passato": "người thấy rõ",          # sutadhammassa passato «người đã nghe Giáo Pháp, người thấy rõ»
              "Cakkhuṃ": "mắt",                   # Cakkhuṃ ādittaṃ «mắt đang bốc cháy» (dhammacakkhuṃ «con mắt»)
              "paṭiladdho": "đã được" + GAP + "nắm lấy",   # khaṇo vo paṭiladdho «thời cơ … đã được các ông nắm lấy»
              "tena": "Vậy"},                      # tena hi vattabbaṃ «Vậy thì nên nói» (Russian «значит»)
    "5-343": {"rūpa": "cõi hình sắc"},             # rūparāgaṃ «sự tham đắm cõi hình sắc» (ch3)
    "5-344": {"ṭhito": "đã đứng vững"},            # phale ṭhito «người đã đứng vững trong thành quả»
    "5-345": {"rūpa": "vật chất"},                 # Rūpakkhandhe «khối vật chất»
    "5-353": {"bhedo": "sự phân chia"},            # sīmā vā bhedo vā «hoặc sự phân chia» (first; Vacībhedo «sự phát
                                                   # ra»: CROSSCHECK)
}

ALLOWED = {
    ("5-334", "aññaṭṭhānesu"): "«nhưng ở những chỗ khác chỉ thấy ruhiruppādako» (aññaṭṭhānesu pana … dissati) is "
                               "the translated note after the colon of the variant bracket [dị bản (Sī., Ka.): "
                               "lohituppādako; …], which present() strips",
    ("5-334", "dissati"): "same bracket as aññaṭṭhānesu",
}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        text = vi.get(bid, "")
        v = context10(kw, k, kws, text)
        if v is not None:
            return v
        if k in T10:
            return T10[k]
        v = map_2_vi.context2(kw, k, kws, text)
        if v is not None:
            return v
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


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:5]}" + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


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
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["ctx"]:
        ctx(sys.argv[2], sys.argv[3:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
