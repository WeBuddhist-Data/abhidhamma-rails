"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 25: 25-sattarasamavaggo.

usage: python -I -X utf8 -B map_25_vi.py                    (writes 25-sattarasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_25_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_25_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_25_vi.py look kw ...         (finished chapter tables, KV, FORMULAS, pi-1 … pi-4 maps)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context25 (segment rules of this chapter) -> T25 -> context5 ->
the finished chapter tables T23, T21 … T2 (latest first; a value counts only where it stands in this segment, as
map_21_vi / map_23_vi) -> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T25, text) of map_sample_vi
(FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-25.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "25-sattarasamavaggo"

_TL = "sự tích lũy"                                 # upacaya / upacayo (T23)
_TLP = _TL + " phước"                               # puññūpacaya(-o)
_CC = "cái chết"                                    # maccu (KV «sự chết» is 5-226)
_KĐL = "không đúng lúc"                             # akāla (own a- kept)
_GK = "gắn kết với các năng lực"                    # indriyabaddhaṃ «những gì gắn kết với các năng lực» (inner «với
                                                    # các» kept; «những gì» = the substantive frame)
_PCD = "phần cúng dường"                            # dakkhiṇā / dakkhiṇaṃ
_LTT = "làm thanh tịnh"                             # visodheti
_XĐ = "xứng đáng"
_TĐ = "Tăng đoàn"
_TP = "từ phía "                                    # -to «từ phía …» (the ablative's preposition kept, as pi-3
                                                    # khandhato «xét theo khối»)

T25 = {
    # ---- headings «Chương thứ mười bảy» (repeated before every discussion), «(166) 1. Bàn về sự tích lũy phước của
    # bậc A-la-hán» … «(176) 11. Bàn về sự thanh tịnh của phần cúng dường»; closers «Phần bàn về … đã hoàn tất.»
    # (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS); 5-801 «Chương thứ mười bảy.»
    "sattarasamavaggo": "Chương thứ mười bảy",      # as map_18 … map_23
    "sattarasama": "thứ mười bảy",
    "upacaya": _TL, "upacayo": _TL, "puññūpacaya": _TLP, "puññūpacayo": _TLP,
    "akāla": _KĐL, "maccu": _CC, "akālamaccu": _CC + " " + _KĐL,
    "kammato": "do nghiệp",                        # Sabbamidaṃ kammato «tất cả điều này đều do nghiệp»
    "kammavipākato": "do quả của nghiệp",
    "baddha": "gắn kết", "baddhaṃ": "gắn kết",     # Indriyabaddhakathā «Bàn về những gì gắn kết với các năng lực»
    "ṭhapetvā": "ngoại trừ",                       # «ngoại trừ con đường cao quý» (KV «ngoài» is 5-209; pi-1 … pi-3)
    "dakkhiṇā": _PCD, "dakkhiṇaṃ": _PCD,
    "visuddhi": "sự thanh tịnh", "visuddhiyo": "sự thanh tịnh",
    "dakkhiṇāvisuddhi": "sự thanh tịnh của " + _PCD,   # head noun first, inner «của» kept
    # ---- 5-776 … 5-779 «Có phải bậc A-la-hán có sự tích lũy phước không? … sự tích lũy điều không phải phước …
    # tạo tác sự tạo tác thuộc về phước, tạo tác sự tạo tác dẫn đến trạng thái bất động, làm nghiệp dẫn đến cõi tái
    # sinh, … sự hiện hữu, … quyền uy, … quyền thống trị, … của cải lớn, … đoàn tùy tùng lớn, … sự vinh hiển cõi trời,
    # … sự vinh hiển cõi người … tích lũy … giảm trừ … đứng vững sau khi đã giảm trừ … có thể thực hiện sự bố thí»
    "apuñña": "điều không phải phước",             # own a- kept; the text's «điều» (as T21 asāta)
    "abhisaṅkhāraṃ": "sự tạo tác",                 # puññābhisaṅkhāraṃ «sự tạo tác thuộc về phước»
    "āneñja": "trạng thái bất động",               # (pi-4 «sự bất động» is another text)
    "saṃvattaniyaṃ kammaṃ": "nghiệp dẫn đến",       # Vietnamese order
    "gati": "cõi tái sinh",                        # KV / T14 (T20 «cõi» is another text)
    "bhava": "sự hiện hữu",                        # «nghiệp dẫn đến sự hiện hữu» (the text's «sự»)
    "sobhagya": "sự vinh hiển", "bhoga": "của cải",
    "deva": "cõi trời", "manussa": "cõi người",    # devasobhagya «sự vinh hiển cõi trời» (as KV dibbaṃ / mānusakaṃ)
    "ācināti": "tích lũy", "apacināti": "giảm trừ",   # as T2 ācinati / apacinati
    "visinetvā": "sau khi đã phân tán",            # as T2 visinitvā
    "ṭhito": "đứng vững",                          # as T2 (T10 / T11 «đứng» is another text)
    "arahā dadeyya": "bậc A-la-hán" + GAP + "thực hiện",   # first «bậc A-la-hán có thể thực hiện sự bố thí»
                                                   # (subject first; optative: «có thể» = frame; as T21 kappaṭṭho dadeyya)
    # ---- 5-780 … 5-782 «Có phải bậc A-la-hán không có cái chết không đúng lúc không? … kẻ giết bậc A-la-hán …
    # Người nào tước đoạt mạng sống của một bậc A-la-hán, … khi còn sự sống, còn phần còn lại của sự sống …»; sutta
    # «… các nghiệp có chủ ý đã được tạo, đã được tích lũy khi chưa được cảm nhận; … ngay trong đời này, hoặc trong lần
    # tái sinh kế tiếp, hoặc trong một lượt khác về sau» (as T20 5-635)
    "voropeti": "tước đoạt",                       # jīvitā voropeti «tước đoạt mạng sống»
    "paṭisaṃveditvā": "khi" + GAP + "được cảm nhận",   # of appaṭisaṃveditvā (positive part; T20 paṭisaṃviditvā)
    "upapajjaṃ": "lần tái sinh kế tiếp",           # as T20 upapajje
    # ---- 5-783 / 5-784 «… có nguyên nhân là những gì đã làm trước đây … do quả của nghiệp mà có thể sát hại sinh
    # mạng … có thể cướp một ngôi nhà … có thể cướp phá làng… có thể cướp phá thị trấn»
    "kata": "đã làm",                              # pubbekatahetu «những gì đã làm trước đây» (pi-2)
    "ghātakaṃ": "cướp phá",                        # gāmaghātakaṃ kareyya «cướp phá làng»
    "ekāgārikaṃ kareyya": "cướp một ngôi nhà",
    # ---- 5-785 verses «Do nghiệp mà thế gian vận hành …, do nghiệp mà muôn loài vận hành …; Chúng sinh bị nghiệp
    # ràng buộc, như chốt trục của cỗ xe đang chạy. Do nghiệp mà người ta được danh tiếng, lời khen ngợi, Do nghiệp mà
    # bị mất mát, bị giết hại và bị giam cầm; Biết rằng nghiệp ấy tạo nên sự khác biệt …»
    "vattatī": "vận hành", "pajā": "muôn loài",
    "vattati": NDE, "vattate": NDE,                # only in the variant brackets [khác chính tả (…): vattati; dị bản
                                                   # (?): vattate] (as KV mahiso)
    "nibandhanā": "bị" + GAP + "ràng buộc",        # Kammanibandhanā «bị nghiệp ràng buộc»
    "rathassa": "cỗ xe", "āṇī": "chốt trục", "yāyato": "đang chạy",
    "kittiṃ": "danh tiếng", "pasaṃsaṃ": "lời khen ngợi", "vadhaṃ": "bị giết hại", "bandhaṃ": "bị giam cầm",
    "nānā": "sự khác biệt", "karaṇaṃ": "tạo nên",  # nānākaraṇaṃ «tạo nên sự khác biệt»
    "viditvā": "biết",                             # «Biết rằng …» (no «sau khi» here; T15 is another text)
    # ---- 5-786 … 5-788 «chỉ những gì gắn kết với các năng lực mới là khổ đau … những gì gắn kết với các năng lực là
    # vô thường … [cặp câu hỏi này phải đứng trước …] … đời sống tu hành trong sạch được sống dưới sự hướng dẫn của Đức
    # Thế Tôn để hiểu biết trọn vẹn khổ đau gắn kết với các năng lực … không sinh khởi trở lại»
    "indriyabaddhaṃ aniccaṃ": _GK + " là vô thường",   # inner «là» kept (sample); of anindriyabaddhaṃ in 5-787
                                                       # (positive part)
    "indriyabaddhassa dukkhassa": "khổ đau " + _GK,    # head noun first, as the text
    "dvayena": "cặp",                              # pucchādvayena «cặp câu hỏi» (editorial bracket)
    "bhagavati": "Đức Thế Tôn",                    # «dưới sự hướng dẫn của Đức Thế Tôn» (locative frame dropped)
    "vussati": "được sống", "pariññāya": "hiểu biết trọn vẹn",   # «để» = dative frame (pi-4 sacchikiriyāya)
    "puna": "trở lại",                             # na puna uppajjati «không sinh khởi trở lại»
    # ---- 5-789 / 5-790 «… sự phát sinh của khổ đau cũng là khổ đau … Đức Thế Tôn đã nói rằng có bốn sự thật cao quý
    # … con đường cao quý là vô thường …»
    "ariyamaggo anicco": "con đường cao quý là vô thường",   # inner «là» kept (sample)
    "ariyamaggo dukkho": "con đường cao quý là khổ đau",
    "vuttāni bhagavatā": "Đức Thế Tôn đã nói",     # FORMULAS vuttaṃ bhagavatā (T11 «… đã nói đến» is another text)
    "dukkhasamudayo dukkho": "sự phát sinh của khổ đau" + GAP + "khổ đau",   # «… cũng là khổ đau» (pi «cũng», predicate
                                                                            # «là» = frame)
    # ---- 5-791 … 5-794 «Tăng đoàn xứng đáng được dâng lễ vật, xứng đáng được tiếp đãi, xứng đáng nhận phần cúng dường,
    # xứng đáng được chắp tay cung kính, là ruộng phước vô thượng của thế gian … Như lửa nhận lễ vật, như đất nhận cơn
    # mưa từ đám mây lớn; Tăng đoàn thành tựu định tâm, nhận phần cúng dường … làm cho phần cúng dường được thành tựu»
    "āhuneyyo": _XĐ + " được dâng lễ vật", "āhuneyyā": _XĐ + " được dâng lễ vật",
    "pāhuneyyo": _XĐ + " được tiếp đãi", "pāhuneyyā": _XĐ + " được tiếp đãi",
    "dakkhiṇeyyo": _XĐ + " nhận " + _PCD, "dakkhiṇeyyā": _XĐ + " nhận " + _PCD,
    "añjalikaraṇīyo": _XĐ + " được chắp tay cung kính", "añjalikaraṇīyā": _XĐ + " được chắp tay cung kính",
    "karaṇīyo": _XĐ + " được" + GAP + "cung kính", "karaṇīyā": _XĐ + " được" + GAP + "cung kính",   # member («chắp
                                                                                                  # tay» = añjali)
    "anuttaraṃ": "vô thượng", "khettaṃ": "ruộng", "puññakkhettaṃ": "ruộng phước",
    "saṅgho āhuneyyo": _TĐ + " " + _XĐ + " được dâng lễ vật",
    "paṭiggaṇhāti": "nhận", "saṅgho paṭiggaṇhāti": _TĐ + " nhận",
    "dakkhiṇaṃ paṭiggaṇhāti": "nhận " + _PCD, "saṅgho dakkhiṇaṃ paṭiggaṇhāti": _TĐ + " nhận " + _PCD,
    "visodheti": _LTT, "saṅgho visodheti": _TĐ + " " + _LTT,
    "dakkhiṇaṃ visodheti": _LTT + " " + _PCD, "saṅgho dakkhiṇaṃ visodheti": _TĐ + " " + _LTT + " " + _PCD,
    "āhutiṃ": "lễ vật", "jātavedo": "lửa", "medanī": "đất", "meghaṃ": "đám mây",   # mahāmeghaṃ «đám mây lớn»
    "samādhi": "định tâm",                         # samādhisampanno «thành tựu định tâm» (T17)
    "ārādhenti": "làm cho" + GAP + "được thành tựu",
    "dakkhiṇaṃ ārādhenti": "làm cho " + _PCD + " được thành tựu",
    # ---- 5-795 / 5-796 «Tăng đoàn ăn, uống, nhai, nếm … tổ chức bữa ăn cho Tăng đoàn, tổ chức bữa ăn cho các vị được
    # chỉ định, tổ chức việc dâng cháo … bữa ăn theo nhóm, bữa ăn thay thế, bữa ăn với thức ăn còn dư … tám loại thức
    # uống – nước xoài, nước trái trâm, nước chuối có hạt, nước chuối không hạt, nước hoa ma-đu-ca, nước nho, nước củ
    # súng, nước trái pha-ru-sa-ca»
    "bhuñjati": "ăn", "saṅgho bhuñjati": _TĐ + " ăn",
    "khādati": "nhai", "khādati sāyati": "nhai nếm",   # «nhai, nếm» (comma dropped, pi-1)
    "maggo bhuñjati": "con đường ăn", "phalaṃ bhuñjati": "thành quả ăn",
    "bhattāni": "bữa ăn", "bhattāni karonti": "tổ chức bữa ăn",   # Vietnamese order
    "uddesa": "vị được chỉ định",                  # uddesabhattāni «bữa ăn cho các vị được chỉ định» («các» dropped)
    "yāgu": "cháo", "bhojanaṃ": "bữa ăn", "parampara": "thay thế", "atiritta": "còn dư",
    "pānāni": "loại thức uống",                    # aṭṭha pānāni «tám loại thức uống» (classifier kept, as pi-1 āhārā)
    "amba": "xoài", "ambapānaṃ": "nước xoài",      # (pi-4 «quả xoài» is another text)
    "jambu": "trái trâm", "jambupānaṃ": "nước trái trâm",
    "coca": "chuối có hạt", "moca": "chuối không hạt",
    "madhuka": "hoa ma-đu-ca", "madhukapānaṃ": "nước hoa ma-đu-ca",
    "muddika": "nho", "muddikapānaṃ": "nước nho", "sāluka": "củ súng", "sālukapānaṃ": "nước củ súng",
    "phārusakapānaṃ": "nước trái pha-ru-sa-ca",
    # ---- 5-798 «Này Kiều-đàm-di, hãy cho Tăng đoàn, … thì cả Ta sẽ được tôn kính …»; Sakka's verses «Đối với những
    # con người đang tế lễ, những chúng sinh mong cầu phước; Đang tạo phước còn chấp trước … Bốn bậc đang thực hành, và
    # bốn bậc đã đứng vững nơi thành quả; Đó là Tăng đoàn ngay thẳng, an định trong trí tuệ và giới hạnh. … Tăng đoàn
    # này bao la, rộng lớn, Không thể đo lường, như nước của đại dương; … những đệ tử tối thắng của bậc anh hùng giữa
    # loài người, Những người đem lại ánh sáng, họ tuyên thuyết Giáo Pháp. … được tế lễ tốt đẹp, Những ai thực hiện sự
    # bố thí hướng về Tăng đoàn; Phần cúng dường ấy đã đến với Tăng đoàn, … được các bậc hiểu biết thế gian tán thán.
    # Nhớ lại sự tế lễ như vậy, Những ai tràn đầy niềm hoan hỷ, đi lại …; Sau khi loại bỏ vết nhơ keo kiệt cùng với gốc
    # rễ, Không bị chê trách, họ đi đến nơi chốn cõi trời»
    "pūjito": "được tôn kính", "sakko": "Sakka", "indo": "vua",   # devānamindo «vua của chư thiên»
    "yajamānānaṃ": "đang tế lễ", "manussānaṃ": "con người",       # (KV «loài người» is 5-230; nara here)
    "apekkhāna": "mong cầu", "pāṇinaṃ": "chúng sinh", "opadhikaṃ": "còn chấp trước",
    "paṭipannā": "đang thực hành", "ṭhitā": "đã đứng vững",       # phale ṭhitā (pi-4 phaleṭhito «đã đứng vững»)
    "ujubhūto": "ngay thẳng", "saṅgho ujubhūto": _TĐ + " ngay thẳng",
    "samāhito": "an định",                         # paññāsīlasamāhito «an định trong trí tuệ và giới hạnh»
    "vipulo": "bao la", "saṅgho vipulo": _TĐ + GAP + "bao la",   # «Tăng đoàn này bao la» («này» skipped)
    "appameyyo": "không thể đo lường", "udadhi": "nước", "sāgaro": "đại dương",   # udadhīva sāgaro «như nước của
                                                                                  # đại dương»
    "seṭṭhā": "tối thắng", "nara": "loài người",   # naravīra «bậc anh hùng giữa loài người»
    "pabhā": "ánh sáng", "karā": "đem lại",        # pabhaṅkarā «Những người đem lại ánh sáng»
    "udīrayanti": "tuyên thuyết", "dhammamudīrayanti": "tuyên thuyết Giáo Pháp",
    "yiṭṭhaṃ": "được tế lễ",                       # suyiṭṭhaṃ «được tế lễ tốt đẹp»
    "uddissa": "hướng về",                         # saṅghamuddissa «hướng về Tăng đoàn» (pi-4 is another text)
    "gatā": "đã đến",                              # saṅghagatā «đã đến với Tăng đoàn»
    "vaṇṇitā": "được" + GAP + "tán thán", "vidūna": "bậc hiểu biết",   # lokavidūna «các bậc hiểu biết thế gian»
    "yaññaṃ": "sự tế lễ", "anussarantā": "nhớ lại",
    "veda": "niềm hoan hỷ", "jātā": "tràn đầy",    # vedajātā «tràn đầy niềm hoan hỷ» (T17 / T23 «sinh» is sahajātā)
    "viharanti": NDE,                              # only in the variant bracket [dị bản (Sī., Ka.): viharanti]
    "vineyya": "sau khi loại bỏ",                  # gerund «sau khi» (map 4 / 5)
    "macchera": "keo kiệt", "malaṃ": "vết nhơ",    # maccheramalaṃ «vết nhơ keo kiệt»
    "aninditā": "không bị chê trách",              # own a- kept
    "saggaṃ": "cõi trời", "ṭhānaṃ": "nơi chốn",    # saggamupenti ṭhānaṃ «đi đến nơi chốn cõi trời»
    # ---- 5-799 «Đức Thế Tôn là bậc đứng đầu giữa loài hai chân, bậc tối thắng …, bậc dẫn đầu …, bậc tối thượng …,
    # bậc ưu việt nhất giữa loài hai chân, bậc không ai sánh bằng, bậc ngang bằng với những bậc không ai sánh bằng,
    # bậc không có ai ngang hàng, bậc không có ai tương tự, bậc không có người đối địch … Có ai tối thắng hơn hay ngang
    # bằng với Đức Phật; Bậc đã đạt đến vị trí đứng đầu giữa những bậc xứng đáng được dâng lễ vật, Cho những người cầu
    # phước, mong tìm quả bao la» (epithets with their head noun «bậc», as T12 aggo / seṭṭho)
    "dvipadānaṃ": "loài hai chân",
    "aggo": "bậc đứng đầu", "uttamo": "bậc tối thượng", "pavaro": "bậc ưu việt nhất",
    "asamo": "bậc không ai sánh bằng",             # own a- kept
    "samo": "ngang bằng",                          # asamasamo «ngang bằng với …»; verse «hay ngang bằng»
    "paṭisamo": "ngang hàng", "paṭibhāgo": "tương tự", "paṭipuggalo": "người đối địch",   # of appaṭi- (positive part)
    "āhuneyyānaṃ": "bậc " + _XĐ + " được dâng lễ vật",
    "aggataṃ": "vị trí đứng đầu", "atthikānaṃ": "người cầu", "esinaṃ": "mong tìm", "vipula": "bao la",
    # ---- 5-800 / 5-801 «sự bố thí được thanh tịnh chỉ từ phía người bố thí, không phải từ phía người nhận … một số
    # người nhận … cho bậc vào dòng … Này A-nan, có bốn sự thanh tịnh của phần cúng dường này!»
    "dānaṃ visujjhati": "sự bố thí được thanh tịnh", "visujjhati": "được thanh tịnh",
    "dāyakato": _TP + "người bố thí", "paṭiggāhakato": _TP + "người nhận", "paṭiggāhakā": "người nhận",
    "sotāpanne": "bậc vào dòng",
}

OVERRIDES = {
    "5-780": {"Yo": "người nào"},                  # «Người nào tước đoạt mạng sống …» (KV «ai» is 5-118)
    "5-782": {"eva": "ngay"},                      # first: diṭṭheva dhamme «ngay trong đời này» (CROSSCHECK; later
                                                   # Attheva suttanto «thật»; as map_20 5-635)
    "5-801": {"eva": "chỉ",                        # first: Dāyakatova «chỉ từ phía người bố thí» (CROSSCHECK; later
                                                   # ceva «cả … lẫn», Attheva suttanto «thật»)
              "dukkhaṃ": "khổ đau"},               # the free word of the uddāna «… mới là khổ đau», «… là khổ đau»
                                                   # (English / Russian «suffering»; context5 «sự khó chịu» is the member
                                                   # of sukhadukkhaṃ, mapped by its own keywords here; CROSSCHECK)
}

ALLOWED = {}

_FINISHED = list(range(2, 22)) + [23]          # chapters 22 and 24 are being mapped at the same time: not used


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 21, 23)."""
    out = []
    for n in _FINISHED:
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        t = getattr(m, f"T{n}", None)
        if t:
            out.append((n, t))
    return out


_TABLES = _tables()
import map_5_vi  # noqa: E402


def context25(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "phalaṃ":              # member of mahapphalaṃ «có quả lớn» / «con đường nhận, thành quả nhận» (5-792 …)
        return "quả" if "mahapphalaṃ" in s else pick(text, "thành quả", "quả")
    if k == "nirodha":             # dukkhanirodhagāminī «sự chấm dứt khổ đau» (5-790) / nirodhadhammaṃ «có bản chất
        return "sự chấm dứt" if "dukkhanirodha" in s else "chấm dứt"   # chấm dứt» (5-786)
    if k == "indriyabaddhaṃ dukkhaṃ":   # «khổ đau gắn kết với các năng lực, đã được hiểu biết trọn vẹn» (5-788) / the
        return pick(text, "khổ đau " + _GK, _GK + GAP + "khổ đau")   # thesis «chỉ những gì gắn kết với các năng lực
                                                                      # mới là khổ đau» («mới» = eva, «là» = frame)
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context25(kw, k, kws, text)
        if v is not None:
            return v
        if k in T25:
            return T25[k]
        v = context5(kw, k, kws, text)
        if v is not None:
            return v
        for n, t in reversed(_TABLES):             # the finished chapters (latest first) where their value stands in
            if k in t and (t[k] == NDE or present(t[k], text)):   # this segment
                return t[k]
        if " " in kw:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, T25, text)
    return resolve


def _prior_values(k):
    return {n: t[k] for n, t in _TABLES if k in t}


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
                p = _prior_values(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                src = " [T25]" if lc(kw) in T25 else (" [prior]" if p else "")
                print(f"   {kw}={v}{src}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


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


def look(words):
    """Values of the finished chapter tables and of the pi-1 … pi-4 maps (reference only)."""
    from map_common_vi import pi1_map_values, pi2_map_values, pi3_map_values, pi4_map_values
    for w in words:
        k = lc(w)
        print(w, "T:", _prior_values(k), "KV:", KV.get(k), "F:", FORMULAS.get(k))
        for name, f in (("pi1", pi1_map_values), ("pi2", pi2_map_values), ("pi3", pi3_map_values),
                        ("pi4", pi4_map_values)):
            try:
                v = f(w)
            except Exception:  # noqa: BLE001
                v = None
            if v:
                print("   ", name, dict(v.most_common(4)))


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
