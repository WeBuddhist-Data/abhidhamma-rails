"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 14: 14-chatthavaggo.

usage: python -I -X utf8 -B map_14_vi.py                  (writes 14-chatthavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_14_vi.py show lo hi [miss] (segments lo..hi with every pair, the values of the finished
                                                           chapters' tables and English | Russian; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context14 (segment rules of this chapter) -> value5(kw, kws, T14,
text) of map_sample_vi (T14 -> context5 -> FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-14.md.
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

PART = "14-chatthavaggo"

_KD = "không do điều kiện tạo thành"               # asaṅkhata (predicate; KV asaṅkhato)
_D = "do điều kiện tạo thành"                       # saṅkhata (predicate; KV saṅkhato)
_DK = "điều " + _KD                                 # asaṅkhata as the noun («hai điều không do điều kiện tạo thành»)
_CĐ = "sự cố định"                                  # niyāma (T12)
_PS = "sự sinh khởi tùy thuộc vào điều kiện"        # paṭiccasamuppāda
_NS = "thành tựu thiền chấm dứt"                    # nirodhasamāpatti
_KG = "không gian"                                  # ākāsa
_TĐ = "thấy được"                                   # sanidassana (KV sanidassanaṃ)
_NT = "nghiệp bằng thân"                            # kāyakamma
_YĐ = "yếu tố đất"

T14 = {
    # ---- headings «Chương thứ sáu», «(53) 1. Bàn về sự cố định» … «(62) 10. Bàn về việc cho rằng nghiệp bằng thân
    # thấy được»; closers «Phần bàn về … đã hoàn tất.» (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS)
    "chaṭṭhavaggo": "Chương thứ sáu",              # heading and «Chương thứ sáu.» (line-initial capital kept, map_12)
    "chaṭṭha": "thứ sáu",                          # member (FORMULAS chaṭṭho)
    "niyāma": _CĐ, "niyāmo": _CĐ, "niyamo": _CĐ,   # T12; Niyamo (uddāna spelling) the same
    "niyāmaṃ": _CĐ,
    "samuppāda": "sự sinh khởi", "samuppādo": "sự sinh khởi",   # pi-1 Cittuppāda «sự sinh khởi»
    "paṭiccasamuppāda": _PS, "paṭiccasamuppādo": _PS,
    "sacca": "sự thật",                            # Saccakathā «Bàn về các sự thật» («các» dropped)
    "āruppa": "trạng thái không hình sắc", "āruppā": "trạng thái không hình sắc",
    "samāpatti": "thành tựu thiền",                # pi-1
    "nirodhasamāpatti": _NS,
    "ākāsa": _KG, "ākāso": _KG, "ākāsaṃ": _KG,
    "sanidassano": _TĐ, "sanidassanā": _TĐ, "sanidassanāni": _TĐ,
    "ākāso sanidassano": _KG + " " + _TĐ,
    "pathavīdhātu": _YĐ, "pathavīdhātu sanidassanā": _YĐ + " " + _TĐ,
    "dhātu sanidassanā": "yếu tố" + GAP + _TĐ,     # fragment of Pathavīdhātu sanidassanā «yếu tố đất thấy được»
    "cakkhundriyaṃ": "năng lực mắt", "cakkhundriyaṃ sanidassanaṃ": "năng lực mắt " + _TĐ,
    "indriyaṃ": "năng lực", "indriyāni": "năng lực",
    "kāya": "thân",                                # Kāyakammaṃ «nghiệp bằng thân»; kāyasaṅkhāro «sự tạo tác bằng thân»
    "kāyakammaṃ": _NT,                             # inner «bằng» kept (Vietnamese order)
    "kāyakammaṃ sanidassanaṃ": _NT + " " + _TĐ,
    "kammaṃ sanidassanaṃ": "nghiệp" + GAP + _TĐ,   # fragment of Kāyakammaṃ sanidassanaṃ
    # ---- the asaṅkhata frame «Có phải X không do điều kiện tạo thành không? … Có phải là Niết-bàn, nơi che chở,
    # nơi ẩn náu, nơi nương tựa, nơi đến cuối cùng, điều bất biến, điều bất tử không?»
    "asaṅkhato": _KD, "asaṅkhatā": _KD,            # predicate (5-458 the noun «từ điều …»: override)
    "asaṅkhatāni": _KD,                            # predicate «bốn sự thật không do …» / noun «hai điều …»: context14
    "saṅkhato": _D, "saṅkhatā": _D,
    "niyāmo asaṅkhato": _CĐ + " " + _KD, "niyāmo saṅkhato": _CĐ + " " + _D,
    "nibbānaṃ asaṅkhataṃ": "Niết-bàn " + _KD,
    "tāṇaṃ": "nơi che chở", "tāṇāni": "nơi che chở",       # the classifier «nơi» / «điều» kept (pi-1 nominalisers);
    "leṇaṃ": "nơi ẩn náu", "leṇāni": "nơi ẩn náu",         # numerals «hai», «năm» … dropped (pi-1)
    "saraṇaṃ": "nơi nương tựa", "saraṇāni": "nơi nương tựa",
    "parāyanaṃ": "nơi đến cuối cùng", "parāyanāni": "nơi đến cuối cùng",
    "accutaṃ": "điều bất biến", "accutāni": "điều bất biến",
    "amataṃ": "điều bất tử", "amatāni": "điều bất tử",     # (map_8 «sự bất tử» where the text says so)
    # «Có phải giữa hai Niết-bàn có sự cao thấp, sự thấp kém và ưu việt, sự hơn kém, hoặc ranh giới, hoặc sự phân
    # chia, hoặc đường vạch, hoặc khoảng cách không?»
    "hīna": "thấp kém", "paṇītatā": "ưu việt",     # members of hīnapaṇītatā «sự thấp kém và ưu việt»
    "avakaṃso": "kém",                             # member of ukkaṃsāvakaṃso «sự hơn kém»
    "sīmā": "ranh giới", "rāji": "đường vạch", "antarikā": "khoảng cách",
    # «Có phải có những người bước vào, đạt được, làm sinh khởi, làm phát khởi, làm khởi lên, làm dấy lên, làm hình
    # thành, làm hình thành trọn vẹn, làm sinh ra, làm sinh ra trọn vẹn sự cố định không?»
    "okkamanti": "bước vào", "samāpajjanti": "nhập", "paṭilabhanti": "đạt được",
    "uppādenti": "làm sinh khởi", "samuppādenti": "làm phát khởi",
    "samuṭṭhāpenti": "làm dấy lên", "samuṭṭhapenti": "làm dấy lên",
    "nibbattenti": "làm hình thành", "abhinibbattenti": "làm hình thành trọn vẹn",
    "janenti": "làm sinh ra", "sañjanenti": "làm sinh ra trọn vẹn",
    "niyāmaṃ okkamanti": "bước vào" + GAP + _CĐ,   # verb … object in the Vietnamese order
    # ---- 5-446 / 5-447 «sự cố định vào dòng … sự cố định A-la-hán … con đường A-la-hán … sự cố định theo hướng sai
    # lầm … khi sự cố định đã sinh khởi rồi chấm dứt»
    "maggo": "con đường", "magga": "con đường",
    "maggo saṅkhato": "con đường " + _D, "maggo asaṅkhato": "con đường " + _KD,
    "arahatta": "A-la-hán",                        # «sự cố định A-la-hán», «con đường A-la-hán» (T12 context)
    "arahattamaggo": "con đường A-la-hán", "sotāpattimaggo": "con đường vào dòng",
    "sotāpatti": "vào dòng", "sakadāgāmi": "trở lại một lần", "anāgāmi": "không trở lại",
    "arahattaniyāmo asaṅkhato": _CĐ + " A-la-hán " + _KD,
    "sotāpattiniyāmo asaṅkhato": _CĐ + " vào dòng " + _KD,
    "micchatta": "hướng sai lầm", "sammatta": "hướng đúng đắn",   # pi-1 MATRIX («theo hướng …»)
    "uppajja": "đã sinh khởi rồi",                 # gerund (niyāme uppajja niruddhe «khi sự cố định đã sinh khởi rồi
    "niruddhe": "chấm dứt",                        # chấm dứt»: «rồi» renders the gerund, as sample hutvā «là … rồi»)
    # ---- 5-449 … 5-451 paṭiccasamuppāda
    "paṭiccasamuppādo asaṅkhato": _PS + " " + _KD, "paṭiccasamuppādo saṅkhato": _PS + " " + _D,
    "avijjā": "vô minh", "avijjā asaṅkhatā": "vô minh " + _KD,
    "avijjāpaccayā saṅkhatā": "do vô minh làm điều kiện " + _D,   # extraction artefact (avijjāpaccayā saṅkhārā
    "avijjāpaccayā asaṅkhatā": "do vô minh làm điều kiện " + _KD,  # saṅkhatā «các sự tạo tác do vô minh làm …»)
    "viññāṇaṃ": "thức", "nāmarūpaṃ": "phần tinh thần và vật chất",
    "jāti": "sự sinh", "jarā": "sự lão hóa", "maraṇaṃ": "sự chết", "jarāmaraṇaṃ": "sự lão hóa và sự chết",
    # 5-450 sutta «Này các tỳ-khưu, sự sinh làm điều kiện cho sự lão hóa và sự chết. Dù các Như Lai xuất hiện hay các
    # Như Lai không xuất hiện, yếu tố ấy vẫn đứng vững, sự ổn định của các hiện tượng, tính cố định của các hiện
    # tượng, quy luật tùy thuộc vào điều kiện. Như Lai giác ngộ, thấu hiểu điều ấy. Sau khi giác ngộ, sau khi thấu
    # hiểu, nói ra, thuyết giảng, công bố, thiết lập, mở bày, phân tích, làm cho rõ ràng … tính đúng như thật, tính
    # không sai lệch, tính không khác đi, quy luật tùy thuộc vào điều kiện …»
    "paccayā": "làm điều kiện cho",                # jātipaccayā jarāmaraṇaṃ «sự sinh làm điều kiện cho …» (pi-3 chain)
    "avijjāpaccayā": "vô minh làm điều kiện cho",  # «vô minh làm điều kiện cho các sự tạo tác»
    "saṅkhārapaccayā": "sự tạo tác làm điều kiện cho",   # «các sự tạo tác làm điều kiện cho thức» («các» dropped)
    "uppādā": "xuất hiện",                         # Uppādā vā tathāgatānaṃ «Dù các Như Lai xuất hiện»
    "ṭhitā": "đứng vững",
    "dhātu": "yếu tố",
    "ṭhitatā": "sự ổn định", "dhammaṭṭhitatā": "sự ổn định của các hiện tượng",   # inner «các» kept
    "niyāmatā": "tính cố định", "dhammaniyāmatā": "tính cố định của các hiện tượng",
    "dhamma": "hiện tượng",
    "ida": NDE,                                    # idappaccayatā «quy luật tùy thuộc vào điều kiện»: no word for ida
    "paccayatā": "quy luật tùy thuộc vào điều kiện",   # (the Vietnamese renders the compound as a whole)
    "idappaccayatā": "quy luật tùy thuộc vào điều kiện",
    "abhisambujjhati": "giác ngộ", "abhisameti": "thấu hiểu",
    "abhisambujjhitvā": "sau khi giác ngộ", "abhisametvā": "sau khi thấu hiểu",   # gerunds «sau khi» (map 4)
    "ācikkhati": "nói ra", "deseti": "thuyết giảng", "paññāpeti": "công bố",   # (KV «đề ra» where the text says so)
    "paṭṭhapeti": "thiết lập", "vivarati": "mở bày", "vibhajati": "phân tích",
    "uttāniṃ": "làm cho rõ ràng",                  # uttāniṃ karoti (karoti not a keyword here)
    "bhava": "sự hiện hữu",                        # Bhavapaccayā «sự hiện hữu làm điều kiện cho sự sinh» (5-452:
                                                   # context14)
    "tathatā": "tính đúng như thật", "avitathatā": "tính không sai lệch", "anaññathatā": "tính không khác đi",
    "dvādasa": "mười hai", "dvādasa asaṅkhatāni": "mười hai " + _DK,   # keyword with its numeral keeps it (pi-3)
    # ---- 5-452 … 5-454 Saccakathā «sự thật về khổ đau … khổ đau nơi thân, khổ đau trong tâm, sự sầu muộn, sự than
    # khóc, khổ đau, nỗi buồn và sự tuyệt vọng … khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện
    # hữu … quan điểm đúng đắn… định tâm đúng đắn»
    "saccaṃ": "sự thật", "saccāni": "sự thật",
    "saccāni asaṅkhatāni": "sự thật " + _KD,
    "dukkhasaccaṃ": "sự thật về khổ đau",          # inner «về» kept (notes-map-12 dukkhaṃ ariyasaccaṃ)
    "nirodhasaccaṃ": "sự thật về sự chấm dứt",
    "dukkha": "khổ đau", "dukkhaṃ asaṅkhataṃ": "khổ đau " + _KD, "dukkhaṃ saṅkhataṃ": "khổ đau " + _D,
    "samudaya": "sự phát sinh", "samudayo": "sự phát sinh",   # notes-map-3
    "samudayo asaṅkhato": "sự phát sinh " + _KD, "samudayo saṅkhato": "sự phát sinh " + _D,
    "nirodho": "sự chấm dứt", "nirodho asaṅkhato": "sự chấm dứt " + _KD,
    "kāyikaṃ": "nơi thân", "cetasikaṃ": "trong tâm",   # pi-1 cetasikaṃ «trong tâm»
    "soka": "sự sầu muộn", "parideva": "sự than khóc", "domanassa": "nỗi buồn", "upāyāsā": "sự tuyệt vọng",
    "taṇhā": "khao khát", "kāmataṇhā": "khao khát dục lạc", "kāma": "dục lạc",
    "bhavataṇhā": "khao khát được hiện hữu", "vibhavataṇhā": "khao khát không còn hiện hữu",
    "vibhava": "không còn hiện hữu",
    "diṭṭhi": "quan điểm", "samādhi": "định tâm",  # sammādiṭṭhi … sammāsamādhi (sammā: context5 «đúng đắn»)
    # 5-454 sutta «bốn điều này đúng như thật, không sai lệch, không khác đi! … ‘đây là sự phát sinh của khổ đau’…
    # ‘đây là sự chấm dứt khổ đau’»
    "avitathāni": "không sai lệch",
    "aññathāni": "khác đi",                        # of anaññathāni «không khác đi» (positive part; KV aññatha)
    "dukkhasamudayo": "sự phát sinh của khổ đau", "dukkhanirodho": "sự chấm dứt khổ đau",
    "dukkhaṃ": "khổ đau",
    # ---- 5-455 / 5-456 Āruppakathā «lĩnh vực không gian vô tận là sự hiện hữu, cõi tái sinh, nơi cư trú của chúng
    # sinh, vòng luân hồi, cách sinh, chỗ trú của thức, sự có được sự tồn tại cá nhân … nghiệp đi đến lĩnh vực không
    # gian vô tận … chúng sinh sinh ra, già đi, qua đời, chết đi, tái sinh … sự hiện hữu gồm bốn khối»
    "ākāsānañcāyatanaṃ asaṅkhataṃ": "lĩnh vực không gian vô tận " + _KD,
    "ākāsānañca": "không gian vô tận",             # T11
    "ānañca": "vô tận",
    "bhavo": "sự hiện hữu", "gati": "cõi tái sinh", "saṃsāro": "vòng luân hồi", "yoni": "cách sinh",
    "āvāso": "nơi cư trú", "satta": "chúng sinh",  # T11 (sattāvāso «nơi cư trú của chúng sinh»)
    "viññāṇa": "thức", "ṭhiti": "chỗ trú",         # viññāṇaṭṭhiti «chỗ trú của thức»
    "attabhāvapaṭilābho": "sự có được sự tồn tại cá nhân", "atta": "cá nhân",   # T11
    "attabhāva": "sự tồn tại cá nhân",
    "ākāsānañcāyatanūpagaṃ kammaṃ": "nghiệp đi đến lĩnh vực không gian vô tận",   # Vietnamese order
    "upagaṃ": "đi đến", "upagā": "đi đến",         # (notes-map-4 «đã đi đến» where the text has «đã»)
    "jāyanti": "sinh ra", "jīyanti": "già đi", "mīyanti": "qua đời", "cavanti": "chết đi",   # KV jāyati …
    "vedanā": "cảm giác", "saññā": "tri giác",
    "saṅkhārā viññāṇaṃ": "tạo tác thức",           # «các tạo tác, thức» (extraction artefact; comma dropped, pi-3)
    "catuvokāra": "gồm bốn khối", "catuvokārabhavo": "sự hiện hữu gồm bốn khối",   # KV / T11
    "anejā": "bất động",
    "vuttā bhagavatā": "Đức Thế Tôn đã nói",       # «Đức Thế Tôn đã nói rằng …» (as vuttaṃ bhagavatā)
    "bhagavatā": "Đức Thế Tôn",
    # ---- 5-457 … 5-459 Nirodhasamāpattikathā «từ sự chấm dứt, sự trong sạch, sự xuất khỏi được nhận ra … đối với
    # người đang nhập sự chấm dứt, trước tiên sự tạo tác bằng lời nói chấm dứt, sau đó sự tạo tác bằng thân … ba sự
    # tiếp xúc chạm đến người đã xuất khỏi sự chấm dứt – sự tiếp xúc trống rỗng, sự tiếp xúc không có dấu hiệu, sự
    # tiếp xúc không mong cầu … tâm nghiêng về sự tách biệt, hướng về sự tách biệt, xuôi về sự tách biệt»
    "nirodhasamāpatti asaṅkhatā": _NS + " " + _KD,
    "nirodhā": "sự chấm dứt",                      # ablative («từ» = the case frame, dropped)
    "vodānaṃ": "sự trong sạch", "vuṭṭhānaṃ": "sự xuất khỏi", "paññāyati": "được nhận ra",
    "samāpajjantassa": "người đang nhập", "vuṭṭhahantassa": "người đang xuất khỏi",   # «đối với người đang …»
    "vuṭṭhitaṃ": "người đã xuất khỏi",             # «chạm đến người đã xuất khỏi» (sample paṭijānantaṃ «người …»)
    "nirujjhati": "chấm dứt", "uppajjati": "sinh khởi",
    "saṅkhāro": "sự tạo tác",                      # the text's «sự» (KV «tạo tác» where the text has no «sự»)
    "vacī": "lời nói", "vacīsaṅkhāro": "sự tạo tác bằng lời nói",
    "kāyasaṅkhāro": "sự tạo tác bằng thân",
    "citta": "tâm", "cittasaṅkhāro": "sự tạo tác bằng tâm", "cittaṃ": "tâm",
    "phassā": "sự tiếp xúc", "phasso": "sự tiếp xúc", "phusanti": "chạm đến",
    "suññato": "trống rỗng", "animitto": "không có dấu hiệu", "appaṇihito": "không mong cầu",
    "viveka": "sự tách biệt", "ninnaṃ": "nghiêng về", "poṇaṃ": "hướng về", "pabbhāraṃ": "xuôi về",
    # ---- 5-460 … 5-462 Ākāsakathā «… làm cho cái không phải không gian trở thành không gian … các loài chim di
    # chuyển, mặt trăng và mặt trời di chuyển, các vì sao di chuyển, biến hóa thần thông, cử động cánh tay, cử động
    # bàn tay, ném cục đất, ném cây chùy, ném thần thông …, ném mũi tên … bao quanh không gian mà làm nhà, làm kho …
    # khi giếng đang được đào … khi giếng trống đang được lấp đầy, … khi chum trống đang được lấp đầy, không gian
    # biến mất»
    "ākāso asaṅkhato": _KG + " " + _KD,
    "pakkhino": "loài chim", "candima": "mặt trăng", "sūriyā": "mặt trời", "tārakarūpāni": "vì sao",
    "iddhiṃ": "thần thông", "vikubbanti": "biến hóa",   # (KV vikubbati «thi triển» where the text says so)
    "bāhuṃ": "cánh tay", "pāṇiṃ": "bàn tay", "leḍḍuṃ": "cục đất", "laguḷaṃ": "cây chùy", "usuṃ": "mũi tên",
    "khipanti": "ném",
    "parivāretvā": "bao quanh",                    # gerund, no «sau khi» in the text («bao quanh … mà làm …»)
    "gharāni": "nhà", "koṭṭhāni": "kho", "koṭṭhe": "kho", "karonti": "làm",
    "khaññamāne": "khi" + GAP + "đang được đào",   # participles keep «khi» (loc. abs.)
    "pūriyamāne": "khi" + GAP + "đang được lấp đầy",
    "tuccha": "trống", "kumbhiyā": "chum", "antaradhāyati": "biến mất",
    # ---- 5-463 … 5-470 «… là hình sắc, lĩnh vực hình sắc, yếu tố hình sắc, màu xanh, màu vàng, màu đỏ, màu trắng,
    # được nhận biết bằng mắt, va chạm vào mắt … tùy thuộc vào mắt và không gian, sinh khởi thức qua mắt»
    "rūpa": "hình sắc", "rūpe": "hình sắc",        # «các hình sắc» (the visible object, pi-1)
    "rūpāyatanaṃ": "lĩnh vực hình sắc", "rūpadhātu": "yếu tố hình sắc",
    "cakkhu": "mắt", "cakkhuviññāṇaṃ": "thức qua mắt",
    "uppajjati cakkhuviññāṇaṃ": "sinh khởi thức qua mắt",
    "paṭicca uppajjati": "tùy thuộc vào" + GAP + "sinh khởi",   # «tùy thuộc vào mắt và không gian, sinh khởi …»
    "paṭicca uppajjati cakkhuviññāṇaṃ": "tùy thuộc vào" + GAP + "sinh khởi thức qua mắt",
    "cakkhusmiṃ paṭihaññati": "va chạm vào mắt",   # Vietnamese order, inner «vào» kept
    "atthi": NDE,                                  # 5-463: only in the bracket [dị bản (?): atthi]
    # 5-464 «thấy khoảng giữa hai cái cây, khoảng giữa hai cây cột, lỗ khóa, lỗ cửa sổ»
    "antaraṃ": "khoảng giữa", "rukkhānaṃ": "cái cây", "thambhānaṃ": "cây cột",   # classifiers as written
    "tāḷacchiddaṃ": "lỗ khóa", "chiddaṃ": "lỗ", "vātapāna": "cửa sổ",
    # 5-466 «thấy mặt đất, tảng đá, ngọn núi … nước … lửa đang cháy … những cái cây đang bị gió lay động»
    "pathavī": "đất",                              # (context5 «đất» / «địa»)
    "āpo": "nước", "āpodhātu": "yếu tố nước", "tejo": "lửa", "tejodhātu": "yếu tố lửa",
    "vāyo": "gió", "vāyodhātu": "yếu tố gió",
    "bhūmiṃ": "mặt đất", "pāsāṇaṃ": "tảng đá", "pabbataṃ": "ngọn núi",
    "passasi": NDE,                                # only in the bracket [dị bản (Sī., Syā., Ka.): passasi, …]
    "jalantaṃ": "đang cháy", "vātena": "gió", "rukkhe": "cái cây",
    "sañcāliyamāne": "đang bị" + GAP + "lay động",   # «đang bị gió lay động» (no «khi» in the text)
    # 5-468 «thấy mắt, tai, mũi, lưỡi, thân»
    "cakkhuṃ": "mắt", "sotaṃ": "tai", "ghānaṃ": "mũi", "jivhaṃ": "lưỡi", "kāyaṃ": "thân",
    # 5-470 «thấy người đang đi tới, đang đi lui, đang nhìn thẳng, đang nhìn quanh, đang co lại, đang duỗi ra …
    # Chương thứ sáu. Tóm tắt của chương này – … bốn yếu tố cơ bản, năm năng lực, nghiệp bằng thân cũng vậy.»
    "abhikkamantaṃ": "đang đi tới", "ālokentaṃ": "đang nhìn thẳng",   # «người» stands once for all six
    "samiñjentaṃ": "đang co lại", "pasārentaṃ": "đang duỗi ra",
    "mahābhūtā": "yếu tố cơ bản", "bhūtā": "yếu tố",   # members of mahābhūtā «yếu tố cơ bản» (mahā «cơ bản»)
    "tatheva": "cũng vậy",                         # «nghiệp bằng thân cũng vậy» (KV «y như vậy» where the text says so)
    "uddānaṃ": "Tóm tắt",                          # T9 / T11
    "vaggo": "chương",
}

OVERRIDES = {
    "5-450": {"eva": "vẫn"},                       # first ṭhitāva sā dhātu «yếu tố ấy vẫn đứng vững»; CROSSCHECK «thật»
                                                   # (Attheva suttanto)
    "5-452": {"bhava": "được hiện hữu"},           # bhavataṇhā «khao khát được hiện hữu» (pi-1 1-M2-110)
    "5-458": {"Asaṅkhatā": _DK},                   # Asaṅkhatā vodānaṃ … «từ điều không do điều kiện tạo thành»
}

ALLOWED = {}


def context14(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "asaṅkhatāni":         # noun «hai / năm … điều không do điều kiện tạo thành» / predicate «bốn sự thật
        if "saccāni asaṅkhatāni" in s:             # không do …» (Saccakathā, uddāna)
            return _KD
        return pick(text, _DK, _KD)
    if k == "nirodha":             # member of nirodhasamāpatti «thành tựu thiền chấm dứt» / Nirodhasaccaṃ «sự thật về
        if "nirodhasamāpatti" in s or "nirodhasamāpatti asaṅkhatā" in s:   # sự chấm dứt» (notes-map-3)
            return "chấm dứt"
        return "sự chấm dứt"
    if k == "paṭicca":             # paṭiccasamuppāda «tùy thuộc vào điều kiện» / «tùy thuộc vào mắt và …»
        return pick(text, "tùy thuộc vào điều kiện", "tùy thuộc vào")
    if k == "saṅkhārā":            # «các sự tạo tác» (5-449 …) / «các tạo tác» (5-455)
        return pick(text, "sự tạo tác", "tạo tác")
    if k == "paccayā":             # «sự sinh làm điều kiện cho …» (sutta, 5-450 / 5-451) / «các sự tạo tác do vô minh
        return pick(text, "làm điều kiện cho", "do" + GAP + "làm điều kiện")   # làm điều kiện» (5-449; KV)
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        v = context14(kw, lc(kw), kws, text)
        if v is not None:
            return v
        return value5(kw, kws, T14, text)
    return resolve


def _prior():
    """{kw: {chapter: value}} of the finished chapters' tables (reference only)."""
    out = {}
    for n in (2, 3, 4, 5, 6, 7, 8, 9, 11, 12):
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
