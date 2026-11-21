"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 11: 11-tatiyavaggo.

usage: python -I -X utf8 -B map_11_vi.py                  (writes 11-tatiyavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_11_vi.py show lo hi [miss] (segments lo..hi with every pair, the values of the finished
                                                           chapters' tables and English | Russian; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context11 (segment rules of this chapter) -> value5(kw, kws, T11,
text) of map_sample_vi (T11 -> context5 -> FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-11.md.
"""
import importlib
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "11-tatiyavaggo"

_NT = "người thứ tám"
_SM = "sự ám ảnh của quan điểm"
_DD = "đã được dứt bỏ"
_UP = "được" + GAP + "hỗ trợ"                    # dhammupatthaddhaṃ «được hiện tượng hỗ trợ»

T11 = {
    # ---- headings «(21) 1. Bàn về các sức mạnh» … «(32) 12. Bàn về lĩnh vực không phải tri giác cũng không phải
    # không tri giác»; closers «Phần bàn về … đã hoàn tất.» (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS)
    "bala": "sức mạnh",                            # Balakathā «Bàn về các sức mạnh» («các» dropped; notes-map-2)
    "ariyaṃ": "cao quý", "ariyā": "cao quý",       # Ariyantikathā «… việc cho rằng là cao quý»; «… là cao quý»
    "vimuttikathā": "Bàn về sự giải thoát",        # heading / closer «Phần bàn về sự giải thoát»
    "vimutti": "sự giải thoát",
    "vimuccamāna": "cái đang được giải thoát",     # Vimuccamānakathā «Bàn về cái đang được giải thoát»
    "vimuccamānaṃ": "cái đang được giải thoát",    # the text's «cái» kept (sample saṅkhataṃ «cái …»)
    "aṭṭhamaka": _NT, "aṭṭhamakassa": _NT,         # «người thứ tám» (name with its head noun, pi-4)
    "aṭṭhamakassa puggalassa": _NT,                # the name with its head noun renders both words (notes-map-3
                                                   # anāgāmī puggalo «bậc không trở lại»)
    "indriya": "năng lực",                         # notes-map-2 (pi-chain «giác quan» is indriyesu)
    "dibbacakkhu": "thiên nhãn", "dibbacakkhuṃ": "thiên nhãn",   # sample dibbena cakkhunā «thiên nhãn»
    "cakkhu": "nhãn",                              # member of dibbacakkhu (sample cakkhunā «nhãn»)
    "dibbasota": "tai thuộc cõi trời", "dibbasotaṃ": "tai thuộc cõi trời",   # «tai thuộc cõi trời»
    "ñāṇakathā": "Bàn về hiểu biết",               # Yathākammūpagatañāṇakathā «Bàn về hiểu biết về việc đi theo …»
    "ñāṇa": "hiểu biết", "ñāṇaṃ": "hiểu biết",     # «hiểu biết đúng như thật» (no «sự»; T5)
    "upagata": "đi theo",                          # member (sample upage «đi theo»)
    "upagataṃ": "việc đi theo",                    # yathākammūpagataṃ «việc đi theo nghiệp của mình» (nominaliser kept)
    "yathākammūpagataṃ": "việc đi theo nghiệp của mình",
    "kamma": "nghiệp",
    "saṃvara": "sự phòng hộ", "saṃvaro": "sự phòng hộ", "asaṃvaro": "sự không phòng hộ",
    "sañña": "có tri giác",                        # of Asañña- «không có tri giác» (positive part, T3 saññasattesu)
    "saññā": "tri giác",                           # the noun («có tri giác» = saññā atthi; heading «… không phải tri
                                                   # giác …»); not the pi-3 bhava-list «có tri giác»
    "nevasaññānāsaññā": "không phải tri giác cũng không phải không tri giác",
    # ---- 5-354 «sức mạnh Như Lai là chung cho đệ tử … bậc chiến thắng, bậc đạo sư, … bậc toàn tri, bậc thấy tất
    # cả, bậc làm chủ Giáo Pháp, chỗ nương tựa của Giáo Pháp … người làm sinh khởi con đường chưa sinh khởi, người
    # làm sinh thành con đường chưa sinh thành, người tuyên thuyết …, người biết con đường, người hiểu con đường,
    # người thông thạo con đường … sự rèn luyện trước đây, sự thực hành trước đây, việc giảng giải Giáo Pháp, việc
    # thuyết giảng Giáo Pháp»
    "sādhāraṇaṃ": "chung", "sāvakasādhāraṇaṃ": "chung cho đệ tử",
    "sāvaka": "đệ tử", "sāvako": "đệ tử",          # T3 sāvaka (the text has no «vị» here)
    "tathāgatassa": "Như Lai",
    "tathāgatabalaṃ sāvakabalaṃ": "sức mạnh Như Lai là sức mạnh của đệ tử",   # inner «là» kept
    "tathāgatabalaṃ sāvakasādhāraṇaṃ": "sức mạnh Như Lai là chung cho đệ tử",
    "tathāgatabalaṃ taṃ sāvakabalaṃ": "sức mạnh Như Lai" + GAP + "là sức mạnh của đệ tử ấy",   # «chính sức mạnh
                                                   # Như Lai ấy là sức mạnh của đệ tử ấy» (the first «ấy» = taññeva)
    "jino": "bậc chiến thắng", "sabbaññū": "bậc toàn tri", "sabbadassāvī": "bậc thấy tất cả",
    "sāmī": "làm chủ",                             # member of dhammassāmī «bậc làm chủ Giáo Pháp» (members without
                                                   # the head noun, pi-4)
    "paṭisaraṇo": "chỗ nương tựa",                 # dhammappaṭisaraṇo «chỗ nương tựa của Giáo Pháp»
    "uppādetā": "người làm sinh khởi", "sañjanetā": "người làm sinh thành",   # agent nouns with their head noun
    "akkhātā": "người tuyên thuyết",
    "uppannassa": "sinh khởi",                     # of anuppannassa «chưa sinh khởi» (positive part)
    "sañjātassa": "sinh thành",                    # of asañjātassa «chưa sinh thành»
    "aññū": "biết", "vidū": "hiểu", "kovido": "thông thạo",   # members of maggaññū / maggavidū / maggakovido
    "pubba": "trước đây", "yogo": "sự rèn luyện", "cariyā": "sự thực hành",
    "akkhānaṃ": "việc giảng giải", "desanā": "việc thuyết giảng",
    # ---- 5-355 «… theo hoàn cảnh, theo nguyên nhân … cách thực hành dẫn đến mọi nơi … chí hướng khác nhau của
    # chúng sinh … sự nhớ lại các đời sống trước … sự chết và sự tái sinh … có sự khác biệt nào … về sự diệt tận
    # các ô nhiễm …»
    "sabbattha": "mọi nơi",                        # sabbatthagāminiṃ «dẫn đến mọi nơi» (no «ở» here)
    "adhimuttikataṃ": "chí hướng", "anussatiṃ": "sự nhớ lại",
    "upapātaṃ": "sự tái sinh", "upapāte": "sự tái sinh",   # cutūpapātaṃ «sự chết và sự tái sinh»
    "khīṇā": "đã bị diệt tận",                     # T4
    "tathāgatassa khīṇā": "Như Lai" + GAP + "đã bị diệt tận",
    "khayena": "sự diệt tận", "nānākaraṇaṃ": "sự khác biệt",
    "vimuttiyā": "sự giải thoát",                  # T4
    "aṭṭhāne": "điều không thể xảy ra",            # ṭhānāṭhāne (as aṭṭhānaṃ)
    # ---- 5-356 «[ở đây, sự phủ nhận này là nhắm vào phương diện chung (cần tham khảo Phụ chú giải)]»
    "sandhāya": "nhắm vào", "paṭikkhepo": "sự phủ nhận", "pakkhaṃ": "phương diện",
    # ---- 5-357 … 5-362 «… con đường vào dòng, thành quả vào dòng … sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền
    # tảng thần thông, năng lực, sức mạnh, chi phần giác ngộ … lấy sự trống rỗng làm đối tượng … vừa chú tâm đến …
    # sự tụ hợp của hai sự tiếp xúc, hai tâm … lấy cái không có dấu hiệu / cái không mong cầu làm đối tượng»
    "manasi karoti": "chú tâm",                    # «vừa chú tâm đến …» (governing «đến» dropped, pi-3)
    "bojjha": "giác ngộ", "bojjhaṅgo": "chi phần giác ngộ",   # notes-map-2
    "phassānaṃ": "sự tiếp xúc", "cittānaṃ": "tâm",  # T4 (tiṇṇaṃ / dvinnaṃ X-ānaṃ)
    "ārammaṇaṃ": "lấy" + GAP + "làm đối tượng",    # X-ārammaṇaṃ «lấy X làm đối tượng» (pi-1 1-M1-16)
    "ārammaṇā": "lấy" + GAP + "làm đối tượng",
    "suññatā": "sự trống rỗng",
    "animitta": "cái không có dấu hiệu", "appaṇihita": "cái không mong cầu",   # the text's «cái» kept
    "phalaṃ": "thành quả",                         # T3 / T4 (KV «kết quả» is saphala)
    "arahattaphalaṃ": "thành quả A-la-hán", "anāgāmiphalaṃ": "thành quả không trở lại",
    "sakadāgāmiphalaṃ": "thành quả trở lại một lần", "sotāpattiphalaṃ": "thành quả vào dòng",
    "arahattamaggo": "con đường A-la-hán", "anāgāmimaggo": "con đường không trở lại",
    "sakadāgāmimaggo": "con đường trở lại một lần", "sotāpattimaggo": "con đường vào dòng",
    "pādā": "nền tảng", "balā": "sức mạnh",         # notes-map-2
    # ---- 5-363 … 5-365 «tâm có tham đắm được giải thoát … đi kèm với sự tham đắm, cùng sinh với …, hòa lẫn …,
    # gắn liền …, cùng tồn tại …, vận hành theo … là đối tượng của phiền não, được giải thoát … tâm có sự tiếp xúc
    # … có cảm giác … đã lìa tham đắm, đã lìa sân hận, đã lìa si mê»
    "saha": "cùng",                                # sahajātaṃ «cùng sinh», sahabhu «cùng tồn tại» (KV «cùng với»: 5-227)
    "jātaṃ": "sinh",                               # member of sahajātaṃ «cùng sinh»
    "saṃkilesiyaṃ": "đối tượng của phiền não", "saṃkilesiyena": "đối tượng của phiền não",
    "sāsavena": "đối tượng của ô nhiễm", "lokiyena": "thuộc thế gian", "āsavena": "ô nhiễm",
    "rāgaṃ": "tham đắm", "dosaṃ": "sân hận", "mohaṃ": "si mê",   # of sarāgaṃ / sadosaṃ / samohaṃ «có tham đắm …»
    "rāgaṃ vimuccati": "tham đắm được giải thoát", "dosaṃ vimuccati": "sân hận được giải thoát",
    "mohaṃ vimuccati": "si mê được giải thoát",    # «tâm có tham đắm được giải thoát» (Vietnamese order as it stands)
    "saphassaṃ": "có sự tiếp xúc", "savedanaṃ": "có cảm giác",
    "vīta": "đã lìa", "vītarāgaṃ": "đã lìa tham đắm", "vītadosaṃ": "đã lìa sân hận", "vītamohaṃ": "đã lìa si mê",
    # ---- 5-366 (the ch3 Odhiso string, T3 values) «một phần đã được giải thoát, một phần chưa được giải thoát …
    # một phần là bậc vào dòng … đã đạt đến thành quả vào dòng, đã có được, đã chứng đắc, đã tự mình chứng nghiệm,
    # chứng nhập và an trú, chạm đến bằng thân rồi an trú … người có một hạt giống, có niềm tin trong sáng không lay
    # chuyển nơi Đức Phật … vào khoảnh khắc sinh khởi … vào khoảnh khắc tan rã»
    "ekadesaṃ": "một phần",
    "vimuttaṃ ekadesaṃ": "một phần đã được giải thoát", "ekadesaṃ vimuttaṃ": "một phần đã được giải thoát",
    "ekadesaṃ avimuttaṃ": "một phần chưa được giải thoát",
    "sotāpattiphalappatto": "đã đạt đến thành quả vào dòng", "arahattappatto": "đã đạt đến trạng thái A-la-hán",
    "adhigato sacchikato": "đã chứng đắc đã tự mình chứng nghiệm",   # comma dropped (T3)
    "sacchikato": "đã tự mình chứng nghiệm", "paṭiladdho": "đã có được",   # T3 (5-378 «chưa …»: override)
    "cuti": "sự chết",                             # cutūpapātaṃ «sự chết và sự tái sinh» (5-383 «lúc chết»: override)
    "viharati": "an trú", "phusitvā": "chạm đến", "phusitvā viharati": "chạm đến" + GAP + "an trú",
    "upasampajja viharati": "chứng nhập và an trú",
    "samannāgato": "có", "avecca": "không lay chuyển", "pasādena": "niềm tin trong sáng",
    "kantehi": "được" + GAP + "yêu quý", "sīlehi": "giới hạnh",
    "ariyakantehi sīlehi": "giới hạnh được các bậc thánh yêu quý",
    "dhamme": "Giáo Pháp", "ekabījī": "người có một hạt giống",
    "saṅkhāra": "sự thúc đẩy", "uddhaṃsoto": "người theo dòng đi lên", "gāmī": "đến",
    "anāgāmiphala": "thành quả không trở lại", "sakadāgāmiphala": "thành quả trở lại một lần",
    "arahattasacchikiriyāya": "tự mình chứng nghiệm trạng thái A-la-hán",
    "vītadoso": "đã lìa sân hận", "vītamoho": "đã lìa si mê", "doso": "sân hận", "moho": "si mê",
    "rāgo": "tham đắm",                            # only vītarāgo «đã lìa tham đắm» (notes-map-2)
    "uppāda": "sinh khởi", "bhaṅga": "tan rã",     # uppādakkhaṇe / bhaṅgakkhaṇe «vào khoảnh khắc sinh khởi / tan rã»
    # ---- 5-367 «Khi vị ấy biết như vậy … [Trường Bộ Kinh 1.248 và các chỗ khác] … đạt đến sự bất động … không còn
    # vết nhơ … có tâm đang tham đắm, đang sân hận, đang si mê, đang bị phiền não làm ô nhiễm … đã bị phá vỡ … đã
    # được làm»
    "jānato": "khi" + GAP + "biết",                # participle keeps «khi» (T3 cutassa «khi … chết»)
    "ādayo": "chỗ khác",                           # T2 («và các chỗ khác»)
    "patte": "đạt đến", "aṅgaṇe": "vết nhơ",       # āneñjappatte «đạt đến sự bất động»; anaṅgaṇe (positive part)
    "mudubhūte": "đã trở nên mềm dẻo",
    "khaya": "sự diệt tận",                        # khayañāṇāya «sự hiểu biết về sự diệt tận …» (T4)
    "rajjamānaṃ": "đang tham đắm", "dussamānaṃ": "đang sân hận", "muyhamānaṃ": "đang si mê",
    "kilissamānaṃ": "đang bị phiền não làm ô nhiễm",
    "bhinnaṃ": "đã bị phá vỡ", "kataṃ": "đã được làm",
    "tena": NDE,                                   # only in the variant bracket [… (Sī., Syā., Kaṃ.): tena hi; …];
                                                   # «Vậy thì» is the keyword Tena hi
    # ---- 5-368 … 5-370 «đối với người thứ tám, sự ám ảnh của quan điểm đã được dứt bỏ … khuynh hướng tiềm ẩn
    # hoài nghi … sự hiểu sai lệch về giới hạnh và nghi thức chưa được dứt bỏ … người thứ tám đã tu tập con đường
    # … đã được dứt bỏ bằng cái không phải con đường … người chuyển đổi dòng dõi»
    "pahīnaṃ": _DD, "pahīno": _DD, "appahīno": "chưa được dứt bỏ",   # T2
    "diṭṭhipariyuṭṭhānaṃ": _SM, "vicikicchāpariyuṭṭhānaṃ": "sự ám ảnh của hoài nghi",
    "diṭṭhipariyuṭṭhānaṃ pahīnaṃ": _SM + " " + _DD,
    "vicikicchā": "hoài nghi",                     # members (the text has no «sự» here)
    "bhāvito": "đã tu tập", "maggo bhāvito": "đã tu tập con đường",   # «người thứ tám đã tu tập con đường»
                                                                       # (notes-map-2)
    "katvā": "vì cho rằng",                        # T7 («vì cho rằng … nó đã được dứt bỏ»)
    # ---- 5-371 «… người thứ tám là người không có niềm tin … là người lười biếng, kém tinh tấn … là người mất
    # tỉnh thức, không hiểu biết rõ ràng … là người không được định tâm, có tâm rối loạn … là người kém trí tuệ, câm
    # điếc»
    "aṭṭhamako puggalo duppañño": _NT + " là người kém trí tuệ",
    "aṭṭhamako puggalo kusīto": _NT + " là người lười biếng",
    "aṭṭhamako puggalo asamāhito": _NT + " là người không được định tâm",
    "aṭṭhamako puggalo muṭṭhassati": _NT + " là người mất tỉnh thức",
    "hīna": "kém",                                 # hīnavīriyo «kém tinh tấn»
    "elamūgo": "câm điếc",                         # T3 elamūgā
    # ---- 5-372 sutta «… do năm năng lực này được trọn vẹn, được viên mãn … Với mức yếu hơn thế … theo mọi cách,
    # bằng mọi phương diện, Ta nói người ấy là ‘người ở bên ngoài, đứng về phía người phàm phu’»
    "samattā": "được trọn vẹn", "paripūrattā": "được viên mãn", "mudutarehi": "mức yếu hơn",
    "sabbena sabbaṃ": "theo mọi cách",             # T5 sabbena
    "sabbathā": "bằng mọi phương diện",            # adverb keeps its preposition (as Sabbattha)
    "vadāmi": "nói", "bāhiro": "người ở bên ngoài", "pakkhe": "phía", "ṭhito": "đứng",
    "puthu": "phàm phu", "jana": "người",          # puthujjanapakkhe «về phía người phàm phu» (T2 / T5)
    # ---- 5-373 … 5-376 «mắt thịt được hiện tượng hỗ trợ thì trở thành thiên nhãn … phạm vi, uy lực, tầm hoạt
    # động … ba mắt – mắt thịt, thiên nhãn, mắt trí tuệ … tai thịt …»
    "upatthaddhaṃ": _UP,
    "maṃsacakkhuṃ": "mắt thịt", "paññācakkhuṃ": "mắt trí tuệ", "cakkhūni": "mắt",
    "maṃsasotaṃ": "tai thịt", "sotāni": "tai",
    "visayo": "phạm vi", "ānubhāvo": "uy lực",
    "vuttāni": "đã nói đến", "vuttāni bhagavatā": "Đức Thế Tôn đã nói đến",
    # verses «… bậc tối thượng trong loài người đã tuyên thuyết … Sự sinh khởi của mắt thịt là con đường của thiên
    # nhãn; Và khi hiểu biết đã sinh khởi … Nhờ có được mắt ấy, được giải thoát khỏi mọi khổ đau»
    "akkhāsi": "đã tuyên thuyết", "udapādi": "đã sinh khởi",
    "paṭilābhā": "có được", "pamuccati": "được giải thoát", "dukkhā": "khổ đau",
    # ---- 5-377 «… “Quả thật, những chúng sinh đáng kính này” … “mang hành vi xấu bằng thân” … “khi thân tan rã,
    # sau khi chết, họ đã tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục”»
    "yathākammūpagataṃ dibbacakkhuṃ": "việc đi theo nghiệp của mình là thiên nhãn",   # inner «là» kept
    "bhonto": "đáng kính", "apāyaṃ": "cõi khổ", "samannāgatā": "mang",   # T3
    # ---- 5-378 verses «Không vì các đời sống trước, cũng không vì thiên nhãn; Vì sự bao quát tâm, vì thần thông, vì
    # sự thanh tịnh của yếu tố tai; Vì sự chết, vì sự tái sinh, tôi không có sự mong cầu»
    "nivāsāya": "đời sống", "pariyāya": "sự bao quát", "iddhiyā": "thần thông",
    "visuddhiyā": "sự thanh tịnh", "cutiyā": "sự chết", "upapattiyā": "sự tái sinh",
    "sāriputto": "Xá-lợi-phất", "āyasmā sāriputto": "tôn giả Xá-lợi-phất",
    # ---- 5-379 / 5-380 «giữa chư thiên có sự phòng hộ … sự kiềm chế việc sát hại sinh mạng … việc dùng rượu nấu,
    # rượu men và chất gây say dẫn đến sự buông thả … tất cả chư thiên đều sát hại sinh mạng, …, có hành vi sai trái
    # trong các dục lạc, nói dối, dùng rượu nấu …»
    "devesu": "chư thiên", "manussesu": "loài người",   # T3 (locative «giữa» dropped)
    "pamādaṭṭhānā": "dẫn đến sự buông thả", "merayamajja": "rượu men và chất gây say",
    "atipātā": "việc sát hại",                     # KV atipāto
    "atipātino": "sát hại", "pāṇātipātino": "sát hại sinh mạng",   # T3
    "cārino": "có hành vi", "micchācārino": "có hành vi sai trái", "vādino": "nói",
    "ṭhāyino": "dùng",                             # surāmerayamajjapamādaṭṭhāyino «dùng rượu nấu … dẫn đến …»
    # ---- 5-381 … 5-385 «giữa chúng sinh Vô Tưởng có tri giác … sự hiện hữu có tri giác, cõi tái sinh có tri giác,
    # nơi cư trú của chúng sinh có tri giác, vòng luân hồi có tri giác, cách sinh có tri giác, sự có được sự tồn tại
    # cá nhân có tri giác … nhờ tri giác ấy mà làm được việc của tri giác»
    "satta": "chúng sinh",                         # sattāvāso «nơi cư trú của chúng sinh»
    "āvāso": "nơi cư trú", "yoni": "cách sinh",
    "attabhāvapaṭilābho": "sự có được sự tồn tại cá nhân", "atta": "cá nhân",
    "saññābhavo": "sự hiện hữu có tri giác", "saññabhavo": "sự hiện hữu có tri giác",
    "asaññabhavo": "sự hiện hữu không có tri giác",
    "saññāgati": "cõi tái sinh có tri giác", "asaññagati": "cõi tái sinh không có tri giác",
    "saññāsaṃsāro": "vòng luân hồi có tri giác", "asaññasaṃsāro": "vòng luân hồi không có tri giác",
    "saññāyoni": "cách sinh có tri giác", "asaññayoni": "cách sinh không có tri giác",
    "pañcavokārabhavo": "sự hiện hữu gồm năm khối", "ekavokārabhavo": "sự hiện hữu gồm một khối",
    "catuvokārabhavo": "sự hiện hữu gồm bốn khối",   # KV ekavokārabhavaṃ … (nominative here)
    "saññāya saññākaraṇīyaṃ": "tri giác" + GAP + "việc của tri giác",   # T5 ñāṇena ñāṇakaraṇīyaṃ
    # 5-383 «có những vị trời gọi là chúng sinh Vô Tưởng; và do sự sinh khởi của tri giác, những vị trời ấy chết đi
    # khỏi thân ấy … Vào lúc chết, vào lúc tái sinh thì có, vào lúc duy trì thì không có»
    "devā": "vị trời", "uppādā": "sự sinh khởi", "kāyā": "thân",
    "upapattikāle": "lúc tái sinh", "kāle": "lúc", "ṭhiti": "duy trì", "upapatti": "tái sinh",
    # ---- 5-386 «lĩnh vực không gian vô tận … Chương thứ ba. Tóm tắt của chương này – Sức mạnh chung, cao quý …
    # cũng vậy, đỉnh cao của sự hiện hữu»
    "ākāsānañca": "không gian vô tận",
    "sukhā vedanā": "cảm giác" + GAP + "dễ chịu",  # fragment of adukkhamasukhā vedanā (pi-1 / pi-2 « … »)
    "uddānaṃ": "Tóm tắt",                          # T9
    "aggaṃ": "đỉnh cao",                           # bhavaggaṃ «đỉnh cao của sự hiện hữu»
    "evameva": "cũng vậy",
}

OVERRIDES = {
    "5-374": {"purisa": "loài người"},             # purisuttamo «bậc tối thượng trong loài người»
    "5-377": {"vata": "Quả thật"},                 # Ime vata bhonto sattā «Quả thật, những chúng sinh đáng kính này»
    "5-378": {"paṭiladdho": "có được",             # appaṭiladdho anadhigato asacchikato «chưa có được, chưa chứng
              "sacchikato": "tự mình chứng nghiệm",   # đắc, chưa tự mình chứng nghiệm thiên nhãn» (positive part)
              "dibbacakkhuṃ sacchikato": "tự mình chứng nghiệm thiên nhãn"},
    "5-383": {"cuti": "chết"},                     # cutikāle «vào lúc chết»
    "5-386": {"Balaṃ": "Sức mạnh", "Sotaṃ": "Tai"},   # chapter verse, line-initial capital kept (map_9 Upalabbho)
}

ALLOWED = {}

_HEADS11 = (("aṭṭhamakassa puggalassa ", _NT), ("puggalassa ", "người"))


def context11(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k in T11:
        return None
    for pre, head in _HEADS11:     # «người thứ tám / người <Y>» («đối với người thứ tám, sự ám ảnh …»): the head
        if k.startswith(pre) and k != pre.strip():  # first, then the rest as one value («… đã được dứt bỏ»)
            rest = kw[len(pre):]
            try:
                rv = value5(rest, kws, T11, text)
            except KeyError:
                return None
            if rv and rv != NDE:
                v = join(text, [head, rv])
                if v:
                    return v
    if k == "arahatta":            # «con đường A-la-hán» / «đã đạt đến trạng thái A-la-hán» (T3)
        return pick(text, "trạng thái A-la-hán", "A-la-hán")
    if k == "vimuttaṃ":            # «cái đã được giải thoát là cái đang được giải thoát» / «đã được giải thoát»
        return pick(text, "cái đã được giải thoát", "đã được giải thoát")
    if k == "dibba":               # dibbacakkhu «thiên nhãn» / dibbasota «tai thuộc cõi trời»
        return pick(text, "thuộc cõi trời", "thiên")
    if k == "cakkhuṃ":             # «mắt thịt», «mắt» / only «thiên nhãn» (5-377, 5-378)
        return pick(text, "mắt", "nhãn")
    if k == "vata" and "sīlabbata" in s and not present("chắc chắn", text):
        return "nghi thức"         # sīlabbata «giới hạnh và nghi thức» (no «vata re» in the segment; notes-map-2)
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        v = context11(kw, lc(kw), kws, text)
        if v is not None:
            return v
        return value5(kw, kws, T11, text)
    return resolve


def _prior():
    """{kw: {chapter: value}} of the finished chapters' tables (reference only)."""
    out = {}
    for n in (2, 3, 4, 5, 6, 7, 9):
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        for k, v in getattr(m, f"T{n}", {}).items():
            out.setdefault(k, {})[n] = v
    return out


def show(lo, hi, only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    pr = _prior()
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
                p = pr.get(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
