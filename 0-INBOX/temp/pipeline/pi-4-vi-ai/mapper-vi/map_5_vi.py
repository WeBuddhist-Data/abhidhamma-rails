"""Build the Pāli->Vietnamese keyword map for pi-4 part 5-catukkapuggalapannatti (Puggalapaññatti, the fours).

usage: python -I -X utf8 map_5_vi.py                     (writes 5-catukkapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_5_vi.py dump [miss]         (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 map_5_vi.py show lo hi          (segments lo..hi: Pāli, Vietnamese, pairs; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T5 (this script's table) -> map_common_vi.value():
context4 -> PG -> the pi-3 chain (T15 … -> context3 -> KD -> pi-2 -> pi-1).
Conventions: pi-1 / pi-2 / pi-3 conventions + notes, vi-map-conventions-pi4.md, map_sample_vi.py.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, en_ru, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "5-catukkapuggalapannatti"

_SINH = "việc sát hại sinh mạng"
_LAY = "việc lấy của không được cho"
_TA = "hành vi sai trái trong các dục lạc"
_DOI = "việc nói dối"

T5 = {
    # ---- the ten courses of action (^4-132 … ^4-143): «sát hại sinh mạng, lấy của không được cho, có hành vi sai trái
    # trong các dục lạc, nói dối, dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả …»
    "atipātī": "sát hại", "atipāte": "sát hại", "atipātā": "sát hại", "atipātaṃ": "sát hại",
    "pāṇātipātī": "sát hại sinh mạng", "pāṇātipāte": "sát hại sinh mạng", "pāṇātipātaṃ": _SINH,
    "puggalo pāṇātipātī": "người sát hại sinh mạng",
    "ādāyī": "lấy", "vādī": "nói", "vāde": "nói",
    "cārī": "có hành vi", "micchācārī": "có hành vi sai trái", "kāmesumicchācārī": "có hành vi sai trái trong các dục lạc",
    "cāre": "hành vi", "kāmesumicchācārā": _TA,
    "ṭhāyī": "dùng", "ṭhāne": "dùng",                        # pamādaṭṭhāyī / -ṭhāne «dùng … dẫn đến sự buông thả»
    "samādapeti": "khuyến khích", "paraṃ": "người khác",
    "asappurisena": "người không chân chính", "sappurisena": "người chân chính",
    "paṭivirato": "kiêng tránh", "puggalo paṭivirato": "người kiêng tránh",
    "pāṇātipātā paṭivirato": "kiêng tránh " + _SINH, "adinnādānā paṭivirato": "kiêng tránh " + _LAY,
    "kāmesumicchācārā paṭivirato": "kiêng tránh " + _TA, "musāvādā paṭivirato": "kiêng tránh " + _DOI,
    "veramaṇiyā": "kiềm chế", "pāṇātipātā veramaṇiyā": "kiềm chế " + _SINH,
    "adinnādānā veramaṇiyā": "kiềm chế " + _LAY, "musāvādā veramaṇiyā": "kiềm chế " + _DOI,
    "palāpī": "nói lời", "palāpā": "nói lời", "palāpaṃ": "nói lời", "sampha": "phù phiếm",   # «nói lời phù phiếm»
    "pisuṇa": "chia rẽ", "vāco": "nói lời", "pharusa": "thô ác",                             # pisuṇa- / pharusavāco
    "abhijjhālu": "có sự thèm muốn",                         # also the fragment of anabhijjhālu «không có sự thèm muốn»
    "anabhijjhāya": "không có sự thèm muốn",
    "byāpanna": "ác ý", "abyāpanna": "không ác ý",
    "pāpataro": "người xấu hơn", "pāpa": "xấu",
    "pāpadhammena": "người có phẩm chất xấu", "pāpadhammataro": "người có phẩm chất xấu hơn",
    "samā": "đúng đắn",                                      # samādiṭṭhi (^4-142, slip for sammādiṭṭhi) «quan điểm đúng đắn»
    # ---- blame (^4-144 … ^4-147)
    "kammena": "nghiệp", "sāvajjena": "có lỗi", "anavajjena": "không có lỗi", "bahulaṃ": "nhiều", "vajjo": "lỗi",
    # ---- understanding (^4-148 … ^4-151)
    "abhisamayo": "sự thấu hiểu", "puggalassa abhisamayo": "người" + GAP + "sự thấu hiểu",
    "velāya": "lúc", "udāhaṭa": "được nêu ra",
    "saṃkhittena": "vắn tắt", "vitthārena": "chi tiết", "vibhajiyamāne": "được phân tích",
    "uddesato": "học thuộc", "paripucchato": "hỏi han", "yoniso": "một cách khôn ngoan",
    "manasi": "chú tâm", "karoto": "chú tâm",                # manasikaroto «chú tâm» (one Vietnamese word for both)
    "mitte": "người bạn", "kalyāṇamitte": "người bạn tốt", "sevato": "gần gũi", "bhajato": "kết giao",
    "payirupāsato": "thân cận", "anupubbena": "dần dần",
    "suṇato": "nghe", "dhārayato": "ghi nhớ", "vācayato": "dạy người khác tụng đọc", "jātiyā": "đời sống",
    # ---- ready replies (^4-152 … ^4-155)
    "vadati": "trả lời", "yuttaṃ": "xác đáng", "pañhaṃ": "câu hỏi", "sīghaṃ": "nhanh",
    # ---- Dhamma speakers (^4-156)
    "parisā": "hội chúng", "sahita": "mạch lạc", "sahitaṃ": "mạch lạc", "asahitassa": "không mạch lạc",
    "asahitaṃ": "không mạch lạc", "saṅkhaṃ gacchati": "được kể là", "kathiko": "thuyết giảng",
    "dhammakathiko bhāsati": "người thuyết giảng Giáo Pháp nói",
    # ---- similes (^4-157 … ^4-163, ^4-170): the compared thing with the text's classifier
    "saṃvijjamānā": "được tìm thấy",                         # santo saṃvijjamānā «đang có mặt, được tìm thấy»
    "valāhako": "đám mây mưa", "gajjitā": "gầm sấm", "vassitā": "mưa", "kattā": "làm",
    "puggalo gajjitā": "người gầm sấm", "puggalo vassitā": "người mưa",
    "mūsikā": "con chuột", "gādhaṃ": "hang", "gādhaṃ kattā": "đào hang", "vasitā": "ở",
    "puggalo kattā": "người đào", "puggalo vasitā": "người ở",
    "pariyāpuṇāti": "học thuộc", "dhammaṃ pariyāpuṇāti": "học thuộc Giáo Pháp",
    "puggalo pariyāpuṇāti": "người học thuộc",
    "ambaṃ": "quả xoài", "āmaṃ": "xanh", "pakka": "chín", "vaṇṇī": "trông như", "vaṇṇi": "trông như",
    "puggalo āmo": "người xanh", "puggalo pakko": "người chín",
    "pāsādikaṃ": "có dáng vẻ đáng mến",
    "abhikkantaṃ": "khi đi tới", "paṭikkantaṃ": "khi đi lui", "ālokitaṃ": "khi nhìn thẳng",
    "samiñjitaṃ": "khi co tay chân", "pasāritaṃ": "khi duỗi tay chân",
    "samiñjitaṃ pasāritaṃ": "khi co tay chân khi duỗi tay chân",
    "samiñjite pasārite": "khi co tay chân khi duỗi tay chân",
    "dhāraṇaṃ": "khi mang", "saṅghāṭi dhāraṇaṃ": "khi mang y ngoài", "saṅghāṭi dhāraṇe": "khi mang y ngoài",
    "patta dhāraṇaṃ": "khi mang" + GAP + "bình bát", "patta dhāraṇe": "khi mang" + GAP + "bình bát",
    "cīvaradhāraṇaṃ": "khi mang" + GAP + "y phục", "cīvaradhāraṇe": "khi mang" + GAP + "y phục",
    "kumbho": "cái chum", "tuccho": "rỗng", "pihito": "được đậy kín", "vivaṭo": "để mở",
    "puggalo tuccho": "người rỗng", "puggalo pūro": "người đầy",
    "udakarahado": "hồ nước", "gambhīra": "sâu", "uttāno": "cạn", "obhāso": "trông như",
    "puggalo gambhīro": "người sâu", "puggalo uttāno": "người cạn",
    "balībaddo": "con bò đực", "parisaṃ": "hội chúng", "caṇḍo": "hung dữ", "gava": "đàn",
    "ubbejitā": "làm cho" + GAP + "sợ hãi", "puggalo caṇḍo": "người hung dữ",
    "puggalo ubbejitā": "người làm cho" + GAP + "sợ hãi",
    "āsīviso": "con rắn độc", "āsīvisā": "rắn độc", "viso": "nọc độc", "āgata": "phát nhanh",
    "āgataviso": "có nọc độc phát nhanh", "ghora": "dữ dội", "kujjhati": "nổi giận", "abhiṇhaṃ": "thường hay",
    "kho": "quả thật", "neva": "không", "assa": "của người ấy",
    "ciraṃ dīgharattaṃ": "lâu dài suốt một thời gian dài",
    "rukkho": "cái cây", "sāro": "có lõi", "sāra": "có lõi", "pheggu": "không có lõi", "parivāro": "xung quanh",
    "sāraparivāro": "xung quanh có lõi", "phegguparivāro": "xung quanh không có lõi",
    "sāro parivāro": "có lõi" + GAP + "xung quanh", "pheggu parivāro": "không có lõi" + GAP + "xung quanh",
    "puggalo sāro": "người có lõi", "puggalo pheggu": "người không có lõi",
    "puggalo sāro parivāro": "người có lõi" + GAP + "xung quanh",
    "puggalo pheggu parivāro": "người không có lõi" + GAP + "xung quanh",
    "puggalo dussīlo": "người phạm giới", "sīlavatī": "giữ giới", "kalyāṇadhammā": "có phẩm chất tốt",
    # ---- praise and blame (^4-164 … ^4-166)
    "avaṇṇa": "chê trách", "avaṇṇaṃ bhāsati": "nói lời chê trách", "vaṇṇaṃ bhāsati": "nói lời khen ngợi",
    "puggalo avaṇṇaṃ bhāsati": "người nói lời chê trách", "puggalo vaṇṇaṃ bhāsati": "người nói lời khen ngợi",
    "puggalo avaṇṇaṃ bhāsitā": "người nói lời chê trách", "puggalo vaṇṇaṃ bhāsitā": "người nói lời khen ngợi",
    "puggalo titthiyānaṃ vaṇṇaṃ bhāsati": "người nói lời khen ngợi các đạo sĩ ngoại đạo",
    "titthiyānaṃ": "đạo sĩ ngoại đạo", "buddhānaṃ": "vị Phật", "sāvakānaṃ": "đệ tử",
    "janeti": "làm phát sinh", "pasādaṃ janeti": "làm phát sinh lòng tin trong sáng",
    "puggalo janeti": "người làm phát sinh", "puggalo pasādaṃ janeti": "người làm phát sinh lòng tin trong sáng",
    "puggalo appasādaṃ janeti": "người làm phát sinh sự thiếu lòng tin trong sáng",
    "paṭipadāya": "cách thực hành", "duppaṭipadāya": "cách thực hành tồi tệ",
    "paṭipannānaṃ": "thực hành", "duppaṭipannānaṃ": "thực hành tồi tệ",
    "sammāpaṭipannā": "thực hành đúng đắn", "sammāpaṭipannānaṃ": "thực hành đúng đắn",
    "micchāpaṭipannānaṃ": "thực hành sai lầm",
    "veyyākaraṇāya": "trả lời", "pañhassa": "câu hỏi", "sampajāno": "hiểu biết rõ ràng", "sato": "tỉnh thức",
    # ---- livelihood (^4-167)
    "nerayikā": "chúng sinh địa ngục", "abhinibbattati": "phát sinh", "uṭṭhahato": "ra sức", "ghaṭato": "cố gắng",
    "vāyamato": "nỗ lực", "upajīvino": "sống nhờ", "puggalassa ājīvo": "người" + GAP + "sinh kế",
    "paranimmitavasavattideve": "chư thiên Tha Hóa Tự Tại", "vasa": "Tự Tại", "vattī": "Tự Tại",
    "upari": "cao hơn",
    # ---- darkness and light (^4-168, ^4-169)
    "kule": "gia đình", "caṇḍāla": "hạ tiện", "nesāda": "thợ săn", "vena": "thợ đan tre", "rathakāra": "thợ đóng xe",
    "pukkusa": "người dọn rác", "dalidde": "nghèo khổ", "pāna": "thức uống", "anna": "thức ăn",
    "kasira": "chật vật", "vuttike": "sống", "kasirena": "một cách khó khăn",
    "dubbaṇṇo": "xấu xí", "duddasiko": "khó coi", "okoṭimako": "thấp lùn", "bahu": "nhiều", "ābādho": "bệnh tật",
    "kāṇo": "chột mắt", "kuṇī": "cụt tay", "khañjo": "què chân", "pakkhahato": "bại liệt", "pakkha": "bại liệt",
    "acchādo": "y phục", "yānassa": "xe cộ", "mālā": "vòng hoa", "gandha": "hương thơm",
    "vilepanassa": "dầu thoa", "vilepana": "dầu thoa", "seyyā": "giường nằm", "āvasatha": "chỗ ở",
    "padīpeyyassa": "đèn đuốc",
    "carati": "thực hiện", "duccaritaṃ carati": "thực hiện hành vi xấu", "caritvā": "sau khi thực hiện",
    "gatiṃ": "cõi", "khattiya": "quý tộc", "mahāsāla": "giàu có", "aḍḍhe": "sung túc", "dhane": "tài sản",
    "bhoge": "của cải", "pahūta": "nhiều", "rajate": "bạc", "rajata": "bạc", "upakaraṇe": "vật dụng",
    "abhirūpo": "đẹp đẽ", "dassanīyo": "dễ nhìn", "pāsādiko": "đáng mến", "paramāya": "tuyệt vời",
    "paccājāto": "tái sinh", "puggalo paccājāto": "người tái sinh",
    "puggalo tamo": "người trong bóng tối", "puggalo joti": "người trong ánh sáng",
    "puggalo uṇṇatoṇato": "người đang ở cao và đi xuống thấp",
    "puggalo oṇatoṇato": "người đang ở thấp và đi xuống thấp",
    # ---- measure (^4-171, ^4-172)
    "pariṇāhaṃ": "bề ngang", "pāripūriṃ": "sự tròn đầy", "passitvā": "sau khi thấy", "pamāṇaṃ": "thước đo",
    "gahetvā": "lấy", "vaṇṇanāya": "lời khen ngợi", "thomanāya": "lời tán dương", "pasaṃsanāya": "lời ca ngợi",
    "vaṇṇahārikāya": "lời truyền tụng tiếng tốt",
    "dukkara": "khó làm", "kārikaṃ": "khổ hạnh", "vividhaṃ": "khác nhau", "paññaṃ": "trí tuệ",
    # ---- own good / others' good (^4-173)
    "sīlasampanno": "thành tựu về giới hạnh", "samādhisampanno": "thành tựu về định tâm",
    "paññāsampanno": "thành tựu về trí tuệ", "vimuttisampanno": "thành tựu về sự giải thoát",
    "sampadāya": "thành tựu", "sīlasampadāya": "thành tựu về giới hạnh",
    "samādhisampadāya": "thành tựu về định tâm", "paññāsampadāya": "thành tựu về trí tuệ",
    "vimuttisampadāya": "thành tựu về sự giải thoát",
    "ñāṇadassana": "sự hiểu biết và thấy rõ", "dassana": "thấy rõ",
    "vimuttiñāṇadassana": "sự hiểu biết và thấy rõ về sự giải thoát",
    # ---- the self-tormentor (^4-174)
    "acelako": "lõa thể", "ācāro": "lề lối", "hattha": "tay", "apalekhano": "liếm",
    "ehi": "được mời đến", "tiṭṭha": "dừng lại", "abhihaṭaṃ": "thức ăn được mang đến", "uddissa": "riêng cho mình",
    "kataṃ": "được làm", "nimantanaṃ": "lời mời thọ thực", "sādiyati": "nhận",
    "kumbhi": "nồi", "mukhā": "miệng", "kaḷopi": "chảo", "eḷaka": "ngưỡng cửa", "antaraṃ": "qua",
    "daṇḍa": "cây gậy", "musala": "chày giã gạo", "bhuñjamānānaṃ": "đang ăn",
    "gabbhiniyā": "người phụ nữ mang thai", "pāyamānāya": "người phụ nữ đang cho con bú", "purisa": "đàn ông",
    "saṅkittīsu": "thức ăn quyên góp", "sā": "con chó", "upaṭṭhito": "đang chực chờ", "makkhikā": "ruồi",
    "saṇḍasaṇḍacārinī": "bu thành đàn", "macchaṃ": "cá", "suraṃ": "rượu mạnh", "merayaṃ": "rượu men",
    "thusodakaṃ": "nước cám lên men", "pivati": "uống",
    "āgāriko": "nhà", "ālopiko": "miếng", "dattiyā": "phần thức ăn được cho",
    "dattīhi": "phần thức ăn được cho", "yāpeti": "sống nhờ", "ekāhikaṃ": "một ngày một lần", "āhāraṃ": "ăn",
    "pariyāya": "định kỳ",
    "sāka": "rau", "sāmāka": "kê", "nīvāra": "lúa hoang", "daddula": "vụn da", "haṭa": "rêu", "kaṇa": "cám",
    "ācāma": "cơm cháy", "piññāka": "bã vừng", "tiṇa": "cỏ", "go": "bò", "maya": "phân", "vana": "rừng",
    "mūla": "rễ cây", "pavatta": "tự rụng",
    "dhāreti": "mặc", "sāṇāni": "vải gai", "masāṇāni": "vải sợi pha", "chava": "tử thi", "dussāni": "vải liệm",
    "paṃsukūlāni": "vải bỏ đi", "paṃsu": "bỏ đi", "kūlāni": "vải", "tirīṭāni": "vải vỏ cây",
    "ajinaṃ": "da linh dương", "khipaṃ": "dải", "kusa": "cỏ", "vāka": "sợi vỏ cây", "phalaka": "ván gỗ",
    "kesa": "tóc", "kambalaṃ": "chăn", "vāḷa": "lông đuôi thú", "ulūka": "chim cú", "pakkhaṃ": "lông cánh",
    "ulukapakkhampi": NDE,                                   # only inside the variant bracket kept in Pāli
    "massu": "râu", "massuṃ": "râu", "locako": "nhổ", "locana": "nhổ",
    "ubbhaṭṭhako": "đứng mãi", "āsana": "chỗ ngồi", "paṭikkhitto": "từ chối",
    "ukkuṭiko": "ngồi chồm hổm", "ukkuṭika": "ngồi chồm hổm", "kaṇṭaka": "gai", "apassayiko": "nằm",
    "sāya": "buổi chiều", "tatiyakaṃ": "lần thứ ba", "orohana": "xuống", "vihitaṃ": "cách",
    # ---- the tormentor of others (^4-175)
    "orabbhiko": "kẻ giết cừu", "sūkariko": "kẻ giết heo", "sākuṇiko": "kẻ bẫy chim", "māgaviko": "kẻ săn nai",
    "luddo": "thợ săn", "macchaghātako": "kẻ giết cá", "coro": "kẻ trộm", "cora": "kẻ trộm", "ghātako": "giết",
    "bandhanāgāriko": "cai ngục", "kurūra": "tàn ác", "kammantā": "làm nghề",
    "puggalo parantapo": "người hành hạ người khác",
    # ---- both (^4-176)
    "rājā": "vua", "khattiyo": "quý tộc", "muddhāvasitto": "đã làm lễ đăng quang", "mahāsālo": "giàu có",
    "puratthimena": "phía đông", "narassa": "người", "sandha": "hội trường", "āgāraṃ": "hội trường",
    "kārāpetvā": "cho xây", "ohāretvā": "cạo bỏ", "khara": "thô ráp", "abbhañjitvā": "xoa",
    "miga": "nai", "visāṇena": "sừng", "kaṇḍuvamāno": "gãi", "pavisati": "đi vào", "saddhiṃ": "cùng với",
    "mahesiyā": "hoàng hậu", "brāhmaṇena purohitena": "vị bà-la-môn tế sư", "purohitena": "tế sư",
    "anantarahitāya": "trống", "bhūmiyā": "mặt đất", "harita": "cỏ xanh", "upalittāya": "được rải",
    "seyyaṃ kappeti": "nằm", "gāviyā": "con bò cái", "rūpa": "hình sắc", "vacchāya": "con bê", "thane": "núm vú",
    "purohito yāpeti": "tế sư dùng để sống", "aggiṃ": "lửa", "avasesena": "phần còn lại",
    "usabhā": "con bò mộng", "vacchatarā": "con bò tơ đực", "vacchatariyo": "con bò tơ cái", "ajā": "con dê",
    "urabbhā": "con cừu", "assā": "con ngựa", "haññantu": "hãy giết", "yañña": "tế lễ", "rukkhā": "cây",
    "yūpa": "cột tế", "dabbhā": "cỏ", "barihisa": "rải nơi tế lễ",
    "dāsā": "nô lệ", "pessā": "người hầu", "kammakarā": "người làm công", "tajjitā": "bị đe dọa",
    "rudamānā": "khóc", "parikammāni": "công việc",
    # the translated editorial bracket «[phần trong ngoặc ( ) không có trong bản chép tay Tích Lan. Trong kinh
    # Kandaraka thuộc Trung Bộ Kinh cũng như vậy]» (present() strips brackets: ALLOWED)
    "sīhaḷa": "Tích Lan", "potthake": "bản chép tay", "majjhima": "Trung", "majjhimanikāye": "Trung Bộ Kinh",
    "kandaraka": "Kandaraka", "kandarakasutte": "kinh Kandaraka", "evameva": "cũng như vậy",
    "attantapa": "Attantapa",
    # ---- neither (^4-177 … ^4-185)
    "uppajjati": "xuất hiện", "vijjā": "hiểu biết chân thật", "caraṇa": "hạnh kiểm",
    "sugato": "bậc đã khéo đi đến đích", "vidū": "hiểu biết", "anuttaro": "vô song", "damma": "cần được rèn luyện",
    "sārathi": "bậc dẫn dắt", "satthā": "bậc đạo sư", "deva": "chư thiên", "bhagavā": "Đức Thế Tôn",
    "brāhmaṇiṃ": "bà-la-môn", "pajaṃ": "chúng sinh", "abhiññā": "hiểu biết trực tiếp", "pavedeti": "tuyên bố",
    "deseti": "thuyết giảng", "ādi": "phần đầu", "majjhe": "phần giữa",
    "majjhekalyāṇaṃ": "tốt đẹp ở phần giữa", "byañjanaṃ": "văn từ", "kevala": "hoàn toàn", "ekanta": "hoàn toàn",
    "paripuṇṇaṃ": "đầy đủ", "parisuddhaṃ": "thanh tịnh", "paripuṇṇaṃ parisuddhaṃ": "đầy đủ" + GAP + "thanh tịnh",
    "brahmacariyaṃ": "đời sống tu hành trong sạch", "pakāseti": "làm sáng tỏ",
    "suṇāti": "nghe", "putto": "con trai", "saddhaṃ": "niềm tin", "paṭisañcikkhati": "suy xét",
    "sambādho": "chật hẹp", "ghara": "gia đình", "raja": "bụi bặm", "āpatho": "con đường",
    "pabbajjā": "đời sống xuất gia", "sukaraṃ": "dễ", "agāraṃ": "gia đình", "ajjhāvasatā": "sống trong",
    "likhitaṃ": "được đánh bóng", "kāsāyāni": "màu vàng đất", "vatthāni": "tấm y",
    "anagāriyaṃ": "đời không gia đình", "bhogakkhandhaṃ": "khối tài sản", "ñāti": "thân quyến",
    "parivaṭṭaṃ": "vòng", "pahāya": "từ bỏ",
    "pabbajito": "đã xuất gia", "bhikkhūnaṃ": "tỳ-khưu", "sikkhā": "sự tu học", "ājīva": "nếp sống",
    "nihita": "đã bỏ", "daṇḍo": "gậy", "sattho": "dao", "lajjī": "biết hổ thẹn", "dayāpanno": "có lòng nhân hậu",
    "hita": "điều lợi ích", "anukampī": "thương xót",
    "pāṭikaṅkhī": "mong đợi", "athenena": "không trộm cắp", "sucibhūtena": "đã trở nên trong sạch",
    "abrahmacariyaṃ": "lối sống không trong sạch", "brahmacārī": "sống đời sống trong sạch", "ārā": "tránh xa",
    "methunā": "sự giao hợp", "gāma": "người thế tục", "musāvādaṃ": _DOI,
    "theto": "đáng tin cậy", "paccayiko": "đáng tin tưởng", "visaṃvādako": "lừa dối",
    "pisuṇaṃ": "chia rẽ", "akkhātā": "nói lại", "bhedāya": "chia rẽ", "bhinnānaṃ": "bị chia rẽ",
    "sandhātā": "hòa giải", "samagga": "sự hòa hợp", "rato": "vui thích", "nandī": "hoan hỷ",
    "karaṇiṃ": "tạo nên", "pharusaṃ": "thô ác", "nelā": "không có lỗi", "hadaya": "lòng", "gamā": "thấm vào",
    "kantā": "yêu mến", "manāpā": "ưa thích", "vinaya": "Giới Luật", "nidhānavatiṃ": "đáng ghi nhớ",
    "sāpadesaṃ": "có lý lẽ", "pariyantavatiṃ": "có giới hạn",
    "samārambhā": "làm hại", "bīja": "hạt giống", "bhattiko": "ăn" + GAP + "bữa", "ratti": "ban đêm",
    "virato": "tránh xa", "vikāla": "sai giờ", "bhojanā": "ăn", "nacca": "múa", "vādita": "nhạc",
    "visūka": "trò giải trí", "dassanā": "xem", "dhāraṇa": "đeo", "maṇḍana": "trang sức", "vibhūsana": "tô điểm",
    "sayanā": "giường", "mahā": "lớn", "paṭiggahaṇā": "nhận", "paṭiggahaṇā paṭivirato": "kiêng tránh việc nhận",
    "āmaka": "chưa nấu", "itthi": "phụ nữ", "kumārikā": "thiếu nữ", "dāsi": "nô tỳ nữ", "dāsa": "nô lệ nam",
    "aja": "dê", "kukkuṭa": "gà", "sūkara": "heo", "hatthi": "voi", "vaḷava": "ngựa cái",
    "khetta": "ruộng đất", "vatthu": "đất đai", "dūteyya": "người đưa tin", "pahiṇa": "việc vặt", "gamana": "chạy",
    "tulā": "cân", "kūṭa": "gian lận", "kaṃsa": "tiền đồng", "ukkoṭana": "hối lộ", "vañcana": "lừa đảo",
    "nikati": "gian trá", "sāci": "quanh co", "yogā": "thủ đoạn", "chedana": "chặt chém", "vadha": "giết hại",
    "bandhana": "giam cầm", "viparāmosa": "cướp đường", "ālopa": "cướp bóc", "sahasākārā": "bạo lực",
    "santuṭṭho": "biết đủ", "parihārikena": "che", "cīvarena": "y phục", "piṇḍapātena": "thức ăn khất thực",
    "yena yeneva": "bất cứ nơi đâu", "samādāya": "mang theo", "sakuṇo": "con chim", "ḍeti": "bay",
    "bhāro": "mang theo", "anavajja": "không có lỗi", "ariyena sīlakkhandhena": "khối giới hạnh cao quý",
    "iminā ariyena samannāgato": "được trang bị" + GAP + "cao quý này",
    "nimitta": "dấu hiệu tổng quát", "saṃvarāya": "thu thúc",  # as map_3 (sense doors; datives without «để»)
    "cariyaṃ": "đời sống tu hành",                           # brahmacariyaṃ (as map_3 / map_4)
    "abyāseka": "không bị vẩn đục", "rūpaṃ": "hình sắc", "saddaṃ": "âm thanh", "phusitvā": "chạm",
    "āpajjati": "thực hiện", "indriya": "giác quan",
    "vigatathinamiddho viharati": "sống đã lìa sự uể oải và đờ đẫn",
    "kārī": "hành động", "bhāve": "khi", "piṇḍapāta": "đi khất thực", "paṭikkanto": "trở về",
    "bhattaṃ": "bữa ăn", "santuṭṭhiyā": "sự biết đủ", "mūlaṃ": "gốc", "giri": "núi",
    "saṃvarena": "sự thu thúc", "uddhato": "xao động", "kathaṃkathī": "băn khoăn",
    "upakkilese": "thứ làm vẩn đục", "jaṃ": "sinh từ", "eva": "hoàn toàn",
    "samāhite": "đã an định", "samāhite citte": "tâm đã an định", "parisuddhe": "trong sạch",
    "pariyodāte": "trong sáng", "anaṅgaṇe": "không còn vết nhơ", "mudubhūte": "trở nên mềm dẻo",
    "kammaniye": "dễ vận dụng", "āneñja": "sự bất động", "abhininnāmeti": "dẫn", "ñāṇāya": "sự hiểu biết",
    "pubbenivāsa": "đời sống trước", "vīsaṃ": "hai mươi", "tiṃsaṃ": "ba mươi", "cattālīsaṃ": "bốn mươi",
    "paññāsaṃ": "năm mươi", "āhāro": "thức ăn", "uddesaṃ": "chi tiết",
    "vihārī": "an trú",
    "cuti": "sự chết", "upapāta": "sự tái sinh", "upapajjamāne": "đang tái sinh", "upage": "đi theo",
    "caritena": "hành vi",
    "jānato": "biết", "vimuccati": "được giải thoát", "bhava": "hiện hữu", "vusitaṃ": "đã được sống trọn",
    "nāparaṃ": "không còn gì khác",
    # ---- the remaining fours (^4-186 … ^4-190)
    "pahīno": "được dứt bỏ",                                 # appahīno «chưa được dứt bỏ» (fragment, positive part)
    "maggassa": "con đường", "lokuttaramaggassa": "con đường" + GAP + "vượt thế gian", "phalassa": "thành quả",
    "puggalo lābhī vipassanāya": "người có được sự thấu suốt",
    "puggalo paṭisevati": "người hưởng thụ", "paṭisevati": "hưởng thụ", "pāpaṃ": "ác", "kammaṃ": "nghiệp",
    "mukhena": "mặt", "rudamāno": "khóc lóc", "anāsavaṃ": "không còn ô nhiễm",
    "cetovimuttiṃ paññāvimuttiṃ": "sự giải thoát của tâm sự giải thoát nhờ trí tuệ",
    "gāmī": "đi", "sota": "dòng", "ṭhita": "đứng vững",
    "aññāya": "hiểu", "attha": "ý nghĩa", "puggalassa sutaṃ": "người" + GAP + "học",
    "sakid": "một lần",
}


def ctx5(bid, kw, k, kws, text):
    """Segment rules of this part (None = no rule)."""
    s = set(lc(x) for x in kws)
    if k == "pāṇa":                # pāṇātipāta «sát hại sinh mạng» / sabbapāṇabhūta «mọi chúng sinh»
        return "chúng sinh" if present("chúng sinh", text) else "sinh mạng"
    if k == "attanā":              # attanā ca … «tự mình» / brahmabhūtena attanā «với bản thân»
        return "với bản thân" if present("với bản thân", text) else "tự mình"
    if k == "sammā":               # sammāsambuddho «Hoàn Toàn» / sammādiṭṭhi, sammāpaṭipannā «đúng đắn»
        return "Hoàn Toàn" if "sammāsambuddho" in s else "đúng đắn"
    if k == "dhammaṃ":             # manasā dhammaṃ «đối tượng của ý» / dhammaṃ pariyāpuṇāti, deseti «Giáo Pháp»
        for v in ("đối tượng của ý", "Giáo Pháp"):
            if present(v, text):
                return v
    if k == "ññū":                 # ugghaṭita- / vipañcitaññū «hiểu» (sample 4-M-10) / kālaññū «biết»
        return "hiểu" if s & {"ugghaṭita", "vipañcita"} else "biết"
    if k == "patta":               # «bình bát» / sapattabhāro «đôi cánh» (^4-180)
        return "bình bát" if present("bình bát", text) else "đôi cánh"
    if k == "cīvara" and present("y phục", text):
        return "y phục"
    if k in ("puggalo pāṇātipātī", "puggalo paṭivirato") and present("có người tự mình", text):
        return "người" + GAP + T5[k][len("người "):]            # «có người tự mình sát hại / kiêng tránh …»
    if k == "ṭhite" and "āneñja" in s:                        # «vững vàng» in the jhāna-mind list (khi đứng: ^4-182)
        return "vững vàng"
    return None


OVERRIDES = {
    "4-137": {"vācāya": "lời"},                               # «nói lời chia rẽ», «nói lời thô ác»
    "4-141": {"dhamma": "phẩm chất"},                         # pāpadhammena «người có phẩm chất xấu»
    "4-143": {"dhamma": "phẩm chất"},                         # kalyāṇadhammena / -taro «người có phẩm chất tốt»
    "4-156": {"eva": NDE, "kusalā": "thông thạo"},            # dhammakathikotveva «được kể là người thuyết giảng …»
    "4-170": {"pāpadhammo": "có phẩm chất xấu"},              # attribute «có người phạm giới, có phẩm chất xấu»
    "4-158": {"kattā": "đào"},                                # gādhaṃ kattā «đào hang»
    "4-167": {"para": "Tha"},                                 # paranimmitavasavattideve «chư thiên Tha Hóa Tự Tại»
    "4-174": {"phala": "trái cây",                            # vanamūlaphalāhāro «rễ cây và trái cây» (pi-1)
              "mutta": "buông thả"},                          # muttācāro «buông thả các lề lối»
    "4-176": {"ajinaṃ": "da thú", "daṇḍa": "roi gậy", "mukhā": "mặt", "yāpeti": "dùng để sống",
              "rūpa": "màu lông",                               # sarūpavacchāya «có con bê cùng màu lông»
              "puggalo attantapo": "người" + GAP + "tự hành hạ bản thân",
              "sutte": "kinh"},                                 # kandarakasuttepi (translated editorial bracket)
    "4-177": {"viharati": "sống",                             # «ngay trong đời này sống không còn đói khát»
              "paccājāto": "sinh ra"},                        # kule paccājāto «người sinh ra trong một gia đình»
    "4-178": {"viharati": "sống", "brahma": "trong sạch",    # brahmacārī «sống đời sống trong sạch»
              "attha": "ý nghĩa"},
    "4-179": {"eḷaka": "cừu", "gava": "bò", "assa": "ngựa đực", "bhūta": "cây cỏ", "mālā": "vòng hoa"},
    "4-180": {"sukhaṃ": "hạnh phúc"},                         # anavajjasukhaṃ «niềm hạnh phúc không có lỗi»
    "4-181": {"sukhaṃ": "hạnh phúc", "cakkhunā": "mắt"},
    "4-182": {"viharati": "sống",                             # «sống với tâm đã lìa …», «sống không xao động»
              "pahāya": "sau khi dứt bỏ"},                    # «sau khi dứt bỏ sự thèm muốn …» (pi-2)
    "4-183": {"sukhaṃ": "hạnh phúc", "dukkhassa": "sự khó chịu",   # sukhañca kāyena; dukkhassa ca pahānā
              "upapanno": "đã tái sinh"},                     # idhūpapanno «tôi đã tái sinh ở đây»
    "4-184": {"gate": "cõi"},                                 # sugate duggate «ở cõi tốt lành, ở cõi xấu»
    "4-185": {"viharati": "sống", "kataṃ": "đã được làm xong", "hoti": "có"},   # «có sự hiểu biết rằng …»
    "4-186": {"doso": "sự sân hận", "moho": "sự si mê",      # «Người mà sự sân hận chưa được dứt bỏ» (as rāgo
              "māno": "sự kiêu mạn"},                         # «sự tham đắm», context4)
    "4-188": {"brahma": "trong sạch", "carati": "sống"},      # «vẫn sống đời sống tu hành trong sạch»
    "4-190": {"Katamo puggalo": "thế nào là sa-môn"},         # «Thế nào là sa-môn bất động?»
}

_BRACKET = "only in the translated editorial bracket, which present() strips"
ALLOWED = {
    ("4-176", k): _BRACKET for k in ("sīhaḷa", "potthake", "majjhima", "majjhimanikāye", "kandaraka",
                                     "kandarakasutte", "sutte", "evameva")
}
ALLOWED.update({("4-182", k): _BRACKET for k in ("kandaraka", "kandarakasutte", "attantapa")})


def resolve_factory():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        v = ctx5(bid, kw, lc(kw), kws, text)
        if v is not None:
            return v
        return value(kw, kws, T5, text)
    return resolve


def dump(only_miss=False):
    res = resolve_factory()
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
        er = en_ru(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:6]}" + (f"  en/ru:{er[0]}|{er[1]}" if er else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, width=None):
    res = resolve_factory()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            p = pi.get(bid, '')
            print(f"== {i} [{bid}]\n-- PI {p[:width] if width else p}")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else "   <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}   [{e[0]} | {e[1]}]{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if sys.argv[4:5] else None)
    else:
        build_part(PART, resolve_factory())
        verify(PART, ALLOWED)
