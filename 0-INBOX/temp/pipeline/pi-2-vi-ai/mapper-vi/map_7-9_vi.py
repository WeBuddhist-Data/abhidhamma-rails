"""Build the Pāli->Vietnamese keyword maps for pi-2 parts 7-satipatthanavibhango, 8-sammappadhanavibhango and
9-iddhipadavibhango.

usage: python -I -X utf8 map_7-9_vi.py                    (writes the three <part>.mapped.md and verifies them)
       python -I -X utf8 map_7-9_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                          segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules) -> T79 (this script's table)
-> T45 (map_4-5_vi.py: the ch. 4 path / satipaṭṭhāna / effort strings) -> map_common_vi.value(): KH (pi-2 table)
-> the approved pi-1 chain (pi1_value).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md,
notes-map-4-5.md, notes-map-6.md, notes-map-7-9.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, present,  # noqa: E402
                           read_keywords, read_vietnamese, value, verify)

_spec = importlib.util.spec_from_file_location("map_45_vi", HERE / "map_4-5_vi.py")
M45 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M45)            # import only: map_4-5_vi.py builds nothing unless run as a script
T45 = M45.T45

PARTS = ["7-satipatthanavibhango", "8-sammappadhanavibhango", "9-iddhipadavibhango"]

_KX = "không xác định về mặt đạo đức"
_SP = "sự thiết lập tỉnh thức"
_IP = "nền tảng thần thông"
_PS = "sự tạo tác bằng nỗ lực"
_CS = "chi phần giác ngộ là "

T79 = {
    # ================================================================ headings and titles
    "satipaṭṭhāna": _SP, "paṭṭhāna": "sự thiết lập", "satipaṭṭhānavibhaṅgo": "phân tích " + _SP,
    "satipaṭṭhānaṃ": _SP, "satipaṭṭhānā": _SP, "satipaṭṭhānānaṃ": _SP,
    "paṭṭhānaṃ": "sự thiết lập", "paṭṭhānā": "sự thiết lập", "paṭṭhānānaṃ": "sự thiết lập",
    "niddeso": "giải thích", "ānupassanā": "sự quán sát", "anupassanā": "sự quán sát",
    "ānupassanāniddeso": "giải thích sự quán sát",
    "kāyānupassanā": "sự quán sát thân", "vedanānupassanā": "sự quán sát các cảm giác",   # inner «các» kept
    "cittānupassanā": "sự quán sát tâm", "dhammānupassanā": "sự quán sát các hiện tượng",
    "kāyānupassanāniddeso": "giải thích sự quán sát thân",
    "vedanānupassanāniddeso": "giải thích sự quán sát các cảm giác",
    "cittānupassanāniddeso": "giải thích sự quán sát tâm",
    "dhammānupassanāniddeso": "giải thích sự quán sát các hiện tượng",
    "padhāna": "nỗ lực", "padhānā": "nỗ lực", "padhānānaṃ": "nỗ lực",               # member of sammappadhāna-
    "sammappadhānavibhaṅgo": "phân tích các nỗ lực đúng đắn",                        # «Phân tích các nỗ lực đúng đắn»
    "sammappadhānā": "nỗ lực đúng đắn", "sammappadhānaṃ": "nỗ lực đúng đắn", "sammappadhānānaṃ": "nỗ lực đúng đắn",
    "iddhipāda": _IP, "iddhi": "thần thông", "pāda": "nền tảng", "pādā": "nền tảng", "pādānaṃ": "nền tảng",
    "iddhipādo": _IP, "iddhipādā": _IP, "iddhipādaṃ": _IP, "iddhipādānaṃ": _IP,
    "chandiddhipādo": _IP + " bằng ý muốn", "vīriyiddhipādo": _IP + " bằng tinh tấn",
    "cittiddhipādo": _IP + " bằng tâm", "vīmaṃsiddhipādo": _IP + " bằng sự thẩm xét",
    # ================================================================ ch. 7 Suttanta formula
    "ātāpī": "nhiệt tâm", "ātāpo": "sự nhiệt tâm", "sampajāno": "hiểu biết rõ ràng",
    "sampajaññaṃ": "sự hiểu biết rõ ràng", "satimā": "có sự tỉnh thức", "vineyya": "sau khi chế ngự",
    "ānupassī": "quán sát", "anupassī": "quán sát", "kāyānupassī": "quán sát thân",
    "vedanānupassī": "quán sát các cảm giác", "cittānupassī": "quán sát tâm",
    "dhammānupassī": "quán sát các hiện tượng",
    "kāyānupassī viharati": "sống quán sát thân", "vedanānupassī viharati": "sống quán sát các cảm giác",
    "cittānupassī viharati": "sống quán sát tâm", "dhammānupassī viharati": "sống quán sát các hiện tượng",
    "viharatīti": "sống",
    "kāye": "thân", "vedanāsu": "cảm giác", "citte": "tâm", "dhammesu": "hiện tượng",
    "vedanāsu vedanānupassī": "cảm giác" + GAP + "quán sát các cảm giác",    # as ch4 kāye kāyānupassī
    "abhijjhā": "sự thèm muốn", "domanassaṃ": "nỗi buồn", "abhijjhādomanassaṃ": "sự thèm muốn và nỗi buồn",
    "abhijjhādomanassa": "sự thèm muốn và nỗi buồn", "loke": "thế gian",
    "loke abhijjhādomanassaṃ": "sự thèm muốn và nỗi buồn đối với thế gian",
    "loke abhijjhādomanassa": "sự thèm muốn và nỗi buồn đối với thế gian",
    "bhikkhu": "vị tỳ-khưu", "kāyo": "thân", "cittaṃ": "tâm",
    # body parts (ch3 lists) and the paccavekkhaṇā frame
    "kesā": "tóc", "lomā": "lông", "nakhā": "móng", "dantā": "răng", "taco": "da", "maṃsaṃ": "thịt",
    "nhāru": "gân", "aṭṭhi": "xương", "miñjaṃ": "tủy xương", "vakkaṃ": "thận", "hadayaṃ": "tim",
    "yakanaṃ": "gan", "kilomakaṃ": "màng hoành", "pihakaṃ": "lá lách", "papphāsaṃ": "phổi", "antaṃ": "ruột",
    "antaguṇaṃ": "màng ruột", "udariyaṃ": "thức ăn trong dạ dày", "karīsaṃ": "phân", "pittaṃ": "mật",
    "semhaṃ": "đờm", "pubbo": "mủ", "lohitaṃ": "máu", "sedo": "mồ hôi", "medo": "mỡ", "assu": "nước mắt",
    "vasā": "mỡ lỏng", "kheḷo": "nước bọt", "siṅghāṇikā": "nước mũi", "lasikā": "dịch khớp", "mutta": "nước tiểu",
    "kāye kesā": "thân" + GAP + "tóc",                                   # «Trong thân này có tóc»
    "atthissa": "của người ấy có",                                       # «Trong thân của người ấy có»
    "paccavekkhati": "quán xét", "talā": "lòng bàn",                     # pādatalā «lòng bàn chân» (pāda: context)
    "kesamatthakā": "đỉnh tóc", "matthakā": "đỉnh", "pariyantaṃ": "được bao bọc bởi",   # tacapariyantaṃ
    "pakārassa": "loại", "asucino": "bất tịnh",                          # nānappakārassa asucino «nhiều loại bất tịnh»
    "nimittaṃ": "dấu hiệu", "taṃ nimittaṃ āsevati": "thực hành dấu hiệu ấy",
    "taṃ nimittaṃ āsevitvā": "thực hành dấu hiệu ấy", "āsevati": "thực hành", "āsevitvā": "thực hành",
    "bhāveti": "tu tập", "bhāvetvā": "tu tập", "bahulīkaroti": "làm đi làm lại", "bahulīkaritvā": "làm đi làm lại",
    "vavatthapeti": "xác định", "vavatthapetvā": "xác định",            # svāvatthitaṃ «cho thật rõ ràng» (no keyword)
    "upasaṃharati": "đưa" + GAP + "đến", "cittaṃ upasaṃharati": "đưa tâm đến",
    "vedanāsu cittaṃ": "tâm" + GAP + "cảm giác",                          # «đưa tâm đến các cảm giác …»
    # the anupassī / ātāpī … definitions
    "upeto": "có được", "samupeto": "có được trọn vẹn", "upapanno": "đã đạt đến", "sampanno": "đã thành tựu",
    "samannāgato": "được trang bị",
    "iriyati": "vận động", "vattati": "tiến triển", "pāleti": "gìn giữ", "yapeti": "tiếp diễn", "yāpeti": "kéo dài",
    "carati": "đi lại", "viharati": "sống",
    "tena": "vì thế", "tattha": "ở đây",
    "vicayo": "sự tìm hiểu", "dhammavicayo": "sự tìm hiểu các hiện tượng", "dhamma": "hiện tượng",
    "vicaya": "sự tìm hiểu", "dhammavicaya": "sự tìm hiểu các hiện tượng",
    "pajānanā": "sự hiểu rõ", "paññā": "trí tuệ", "diṭṭhi": "quan điểm", "amoho": "sự không si mê",
    "sammā": "đúng đắn", "sati": "sự tỉnh thức", "anussati": "sự nhớ lại",
    "ārambho": "sự khởi động", "vīriyārambho": "sự khởi động tinh tấn", "cetasiko": "trong tâm",
    "cetasiko vīriyārambho": "sự khởi động tinh tấn trong tâm",
    # loka / abhijjhā / domanassa definitions (ch6 strings)
    "khandhā": "khối", "upādāna": "sự bám víu",                         # «năm khối làm đối tượng cho sự bám víu»
    "rāgo": "sự tham đắm", "sārāgo": "sự say đắm", "cittassa": "tâm",     # «sự say đắm của tâm»
    "cetasikaṃ": "trong tâm", "asātaṃ": "bứt rứt", "cetasikaṃ asātaṃ": "sự bứt rứt trong tâm",
    "cetasikaṃ dukkhaṃ": "sự khó chịu trong tâm", "dukkhaṃ": "khó chịu", "dukkhā": "khó chịu",
    "cetosamphassa": "sự tiếp xúc của tâm", "cetosamphassajaṃ": "sinh từ sự tiếp xúc của tâm",
    "cetosamphassajā": "sinh từ sự tiếp xúc của tâm", "vedayitaṃ": "cảm nhận", "vedanā": "cảm giác",
    "dukkhaṃ vedayitaṃ": "cảm nhận" + GAP + "khó chịu", "dukkhā vedanā": "cảm giác" + GAP + "khó chịu",
    "asātaṃ dukkhaṃ": "bứt rứt và khó chịu", "asātaṃ dukkhaṃ vedayitaṃ": "cảm nhận bứt rứt và khó chịu",
    "asātā dukkhā vedanā": "cảm giác bứt rứt và khó chịu",
    # «Như vậy, sự thèm muốn này … đã được chế ngự, đã được chế ngự hoàn toàn, …»
    "paṭivinītā": "đã được chế ngự hoàn toàn", "santā": "đã lắng yên", "samitā": "đã được làm lắng dịu",
    "vūpasantā": "đã lắng dịu hoàn toàn", "atthaṅgatā": "đã biến mất", "abbhatthaṅgatā": "đã biến mất hoàn toàn",
    "appitā": "đã đi đến kết thúc", "byappitā": "đã đi đến kết thúc hoàn toàn", "sositā": "đã bị làm khô cạn",
    "visositā": "đã bị làm khô cạn hoàn toàn", "byantīkatā": "đã bị làm cho tiêu tan",
    # vedanānupassanā
    "pajānāti": "hiểu rõ", "vedayamāno": "khi cảm nhận",
    "vedayāmī": "tôi đang cảm nhận", "vedayatī": "người ấy đang cảm nhận",   # the personal ending -> pronoun
    "sukhaṃ": "dễ chịu", "sukhaṃ vedanaṃ": "cảm giác dễ chịu", "dukkhaṃ vedanaṃ": "cảm giác khó chịu",
    "adukkhamasukhaṃ": "không khó chịu cũng không dễ chịu",
    "sāmisaṃ": "có tính trần tục", "nirāmisaṃ": "không có tính trần tục",
    # cittānupassanā: «hoặc đối với tâm có tham đắm …» (vā … cittaṃ = hoặc … tâm; «đối với» has no keyword)
    "rāgaṃ": "tham đắm", "dosaṃ": "sân hận", "mohaṃ": "si mê",
    "saṃkhittaṃ": "co rút", "vikkhittaṃ": "tán loạn", "mahaggataṃ": "rộng lớn", "amahaggataṃ": "không rộng lớn",
    "sauttaraṃ": "còn có điều cao hơn", "anuttaraṃ": "không có điều gì cao hơn",
    "samāhitaṃ": "được định tâm", "asamāhitaṃ": "không được định tâm",
    "vimuttaṃ": "được giải thoát", "avimuttaṃ": "không được giải thoát",
    # dhammānupassanā
    "santaṃ": "có",                                                      # santaṃ vā ajjhattaṃ X «khi ở nơi bản thân có X»
    "kāmacchandaṃ": "ý muốn dục lạc", "kāma": "dục lạc", "chandaṃ": "ý muốn", "byāpādaṃ": "ác ý",
    "thinamiddhaṃ": "sự uể oải và đờ đẫn", "thina": "uể oải", "middhaṃ": "đờ đẫn",
    "uddhaccakukkuccaṃ": "sự xao động và hối tiếc", "uddhacca": "sự xao động", "kukkuccaṃ": "hối tiếc",
    "vicikicchaṃ": "sự hoài nghi",
    "uppādo": "nảy sinh", "anuppādo": "không nảy sinh",                 # «… nảy sinh» / «không nảy sinh trở lại»
    "uppannassa": "đã sinh khởi", "anuppannassa": "chưa sinh khởi", "pahīnassa": "đã được dứt bỏ",
    "pāripūrī": "hoàn thiện",                                            # «được tu tập đến chỗ hoàn thiện»
    "samādhi": "định tâm", "pīti": "sự hân hoan", "passaddhi": "sự an tịnh", "upekkhā": "sự bình thản",
    "sambojjhaṅgaṃ": "chi phần giác ngộ", "sambojjhaṅgo": "chi phần giác ngộ",
    # ================================================================ Abhidhamma openings (ch4 / ch6 values)
    "pahānāya": "dứt bỏ", "diṭṭhigatānaṃ": "sự mắc kẹt trong các quan điểm",
    "diṭṭhigatānaṃ pahānāya": "dứt bỏ sự mắc kẹt trong các quan điểm",
    "jhānaṃ": "tầng thiền", "jhānaṃ bhāveti": "tu tập tầng thiền", "uttaraṃ": "vượt", "uttarā": "vượt",
    "apacaya": "sự giảm trừ", "apacayagāmiṃ": "dẫn đến sự giảm trừ",
    "dukkhapaṭipadaṃ": "cách thực hành khó khăn", "paṭipadaṃ": "cách thực hành",
    "dandhābhiññaṃ": "sự hiểu biết trực tiếp chậm chạp",
    "paṭipadaṃ dandhābhiññaṃ": "cách thực hành" + GAP + "sự hiểu biết trực tiếp chậm chạp",
    "ābhiññaṃ": "sự hiểu biết trực tiếp", "pattiyā": "đạt đến", "bhūmiyā": "giai đoạn",
    "vivicceva": "hoàn toàn tách khỏi", "kāmehi": "dục lạc", "vivicceva kāmehi": "hoàn toàn tách khỏi các dục lạc",
    "upasampajja": "chứng nhập", "upasampajja viharati": "chứng nhập và an trú", "samaye": "vào lúc ấy",
    "magga": "con đường", "maggaṅgaṃ": "chi phần của con đường", "sampayuttā": "gắn liền",
    "avasesā": "còn lại", "avasesā dhammā": "hiện tượng còn lại", "dhammā": "hiện tượng",
    "phasso": "sự tiếp xúc", "avikkhepo": "sự không tán loạn", "paggāho": "sự dốc sức",
    "katattā": "đã được tạo", "bhāvitattā": "tu tập", "suññataṃ": "tính chất trống rỗng",   # pi-1 ^1-505
    "kusalassa jhānassa": "tầng thiền thiện", "kusalā": "thiện",
    # ================================================================ ch. 8 (Sammappadhāna)
    "janeti": "khởi lên", "chandaṃ janeti": "khởi lên ý muốn", "vāyamati": "nỗ lực",
    "ārabhati": "khởi động", "vīriyaṃ ārabhati": "khởi động tinh tấn",
    "paggaṇhāti": "nâng" + GAP + "lên", "cittaṃ paggaṇhāti": "nâng tâm lên", "padahati": "ra sức nỗ lực",
    "janetīti": "khởi lên", "chandaṃ janetīti": "khởi lên ý muốn", "vāyamatīti": "nỗ lực",
    "ārabhatīti": "khởi động", "vīriyaṃ ārabhatīti": "khởi động tinh tấn",
    "paggaṇhātīti": "nâng" + GAP + "lên", "cittaṃ paggaṇhātīti": "nâng tâm lên", "padahatīti": "ra sức nỗ lực",
    "anuppannānaṃ": "chưa sinh khởi", "uppannānaṃ": "đã sinh khởi", "pāpakānaṃ": "xấu ác",
    "anuppādāya": "không sinh khởi", "uppādāya": "được sinh khởi", "ṭhitiyā": "được duy trì",
    "asammosāya": "không bị mai một", "vepullāya": "được lớn mạnh", "pāripūriyā": "được hoàn thiện",
    "dhammānaṃ": "hiện tượng", "akusalānaṃ": "bất thiện", "kusalānaṃ": "thiện",
    "akusalānaṃ dhammānaṃ": "hiện tượng" + GAP + "bất thiện",           # skips «xấu ác»
    "kusalānaṃ dhammānaṃ": "hiện tượng thiện",
    "khandho": "khối", "sampayutto": "gắn liền", "kāya": "thân", "vacī": "lời nói",
    "kāyakammaṃ": "nghiệp bằng thân", "vacīkammaṃ": "nghiệp bằng lời nói", "manokammaṃ": "nghiệp bằng ý",
    "samuṭṭhānaṃ": "do" + GAP + "sinh ra",                               # «do chúng sinh ra»
    "kilesā": "phiền não", "ekaṭṭhā": "cùng hiện diện", "mūlāni": "gốc rễ",
    "akusalamūlāni": "gốc rễ bất thiện", "kusalamūlāni": "gốc rễ thiện",
    "lobho": "sự tham lam", "doso": "sự sân hận", "moho": "sự si mê",
    "alobho": "sự không tham lam", "adoso": "sự không sân hận",
    "viññāṇa": "thức", "saññā": "tri giác",
    # chanda string
    "chando": "ý muốn", "chandikatā": "sự khởi ý muốn", "kattu": "hành động", "kamyatā": "sự muốn",
    "kusalo": "thiện", "kusalo dhammacchando": "ý muốn thiện đối với các hiện tượng",
    "imaṃ chandaṃ janeti": "khởi lên ý muốn này", "sañjaneti": "làm sinh ra",
    "samuṭṭhapeti": "làm trỗi dậy trọn vẹn", "nibbatteti": "làm phát khởi",
    # vīriya / citta lemmas
    "imaṃ vīriyaṃ ārabhati": "khởi động sự tinh tấn này", "samārabhati": "khởi động trọn vẹn",
    "imaṃ cittaṃ paggaṇhāti": "nâng tâm này lên", "sampaggaṇhāti": "nâng lên trọn vẹn",
    "upatthambheti": "nâng đỡ", "paccupatthambheti": "nâng đỡ vững chắc",
    "mānasaṃ": "tâm trí", "mano": "ý", "tajjā": "tương ứng", "dhātu": "yếu tố",
    "manoviññāṇa": "ý thức", "manoviññāṇadhātu": "yếu tố ý thức",
    # «Sự duy trì là sự không mai một, …»
    "asammoso": "sự không mai một", "vepullaṃ": "sự lớn mạnh",          # ṭhiti / pāripūrī: context
    "vīriyasambojjhaṅgo": _CS + "sự tinh tấn", "samādhisambojjhaṅgo": _CS + "định tâm",
    "dhammavicayasambojjhaṅgo": _CS + "sự tìm hiểu các hiện tượng", "satisambojjhaṅgo": _CS + "sự tỉnh thức",
    # ================================================================ ch. 9 (Iddhipāda)
    "chanda": "ý muốn", "citta": "tâm", "vīmaṃsā": "sự thẩm xét", "vīmaṃsaṃ": "sự thẩm xét",
    "chandasamādhi": "định tâm nhờ ý muốn", "vīriyasamādhi": "định tâm nhờ tinh tấn",
    "cittasamādhi": "định tâm nhờ tâm", "vīmaṃsāsamādhi": "định tâm nhờ sự thẩm xét",
    "saṅkhāra": "sự tạo tác", "padhānasaṅkhāra": _PS, "saṅkhāro": "sự tạo tác", "padhānasaṅkhāro": _PS,
    "saṅkhārā": "sự tạo tác", "padhānasaṅkhārā": _PS,                    # «các sự tạo tác bằng nỗ lực» («các» frame)
    "samannāgataṃ": "được trang bị", "samannāgataṃ iddhipādaṃ": _IP + " được trang bị",
    "samādhipadhānasaṅkhārasamannāgataṃ": "được trang bị định tâm" + GAP + "và sự tạo tác bằng nỗ lực",
    "samādhipadhānasaṅkhārasamannāgato": "được trang bị định tâm" + GAP + "và sự tạo tác bằng nỗ lực",
    "iddhipādaṃ bhāveti": "tu tập " + _IP, "iddhipādaṃ bhāvetī": "tu tập " + _IP,
    "adhipatiṃ": "yếu tố chủ đạo",                                       # adhipatiṃ karitvā «lấy … làm yếu tố chủ đạo»
    "labhati": "đạt được", "samādhiṃ": "định tâm", "labhati samādhiṃ": "đạt được định tâm",
    "ekaggataṃ": "sự nhất tâm", "cittassekaggataṃ": "sự nhất tâm",       # pi-1 cittassekaggatā
    "abhisaññahitvā": "gom", "abhisaññūhitvā": "gom", "abhisaṅkhipitvā": "thu tóm lại",   # ^2-432 slip as meant
    "ekajjhaṃ": "làm một",                                               # of tadekajjhaṃ «tất cả lại làm một»
    "saṅkhyaṃ gacchati": "được tính", "saṅkhyaṃ": "tính", "gacchati": "được",
    "tveva": "là",                                                       # «-tveva saṅkhyaṃ gacchati» «thì được tính là “…”»
    "samatho": "sự tĩnh lặng", "avisāhāro": "sự không phân tán", "avisāhaṭa": "không phân tán",
    "saṇṭhiti": "sự vững vàng", "avaṭṭhiti": "sự vững chãi", "indriyaṃ": "năng lực", "balaṃ": "sức mạnh",
    "samādhindriyaṃ": "năng lực định tâm", "vīriyindriyaṃ": "năng lực tinh tấn",
    "nikkamo": "sự dấn bước", "parakkamo": "sự xông pha", "uyyāmo": "sự gắng sức", "ussāho": "sự hăng hái",
    "ussoḷhī": "sự bền chí", "thāmo": "sức bền", "asithila": "không lơi lỏng", "anikkhitta": "không buông bỏ",
    "dhura": "gánh", "dhuratā": "gánh", "sampaggāho": "sự dốc sức",
    "samiddhi": "sự thịnh đạt", "ijjhanā": "sự thành tựu", "samijjhanā": "sự thành tựu trọn vẹn",
    "paṭilābho": "sự có được", "patti": "sự đạt đến", "sampatti": "sự đạt đến trọn vẹn", "phusanā": "sự chạm",
    "sacchikiriyā": "sự tự mình chứng nghiệm", "upasampadā": "sự chứng nhập",
    "viññāṇakhandho": "khối thức",                                       # ^2-443 slip as meant
    # ================================================================ Pañhāpucchaka
    "saraṇā": "có xung đột", "araṇā": "không có xung đột", "abyākatā": _KX, "akusalā": "bất thiện",
    "na hetu": "không phải là gốc rễ", "hetu": "gốc rễ", "visaṃsaṭṭho": "không hòa lẫn",
    "acetasiko": "không phải là yếu tố đồng hành với tâm", "ajjhattiko": "thuộc phần bên trong",
    "sukha": "hạnh phúc",
}
for _k, _v in (("ajjhattaṃ", "ở nơi bản thân"), ("bahiddhā", "ở bên ngoài bản thân"),
               ("ajjhattabahiddhā", "ở nơi bản thân và ở bên ngoài bản thân")):
    T79[_k] = _v
    for _n, _nv in (("kāye", "thân"), ("vedanāsu", "cảm giác"), ("citte", "tâm"), ("dhammesu", "hiện tượng")):
        T79[f"{_k} {_n}"] = f"{_nv} {_v}"                                # «(các) cảm giác ở nơi bản thân» («các» frame)
for _x, _v in (("sukhaṃ", "dễ chịu"), ("dukkhaṃ", "khó chịu")):
    for _a, _av in (("sāmisaṃ", "có tính trần tục"), ("nirāmisaṃ", "không có tính trần tục")):
        T79[f"{_a} {_x}"] = f"{_v} {_av}"
        T79[f"{_a} {_x} vedanaṃ"] = f"cảm giác {_v} {_av}"
for _p, _v in (("sarāgaṃ", "có tham đắm"), ("vītarāgaṃ", "đã lìa tham đắm"), ("sadosaṃ", "có sân hận"),
               ("vītadosaṃ", "đã lìa sân hận"), ("samohaṃ", "có si mê"), ("vītamohaṃ", "đã lìa si mê"),
               ("saṃkhittaṃ", "co rút"), ("vikkhittaṃ", "tán loạn"), ("mahaggataṃ", "rộng lớn"),
               ("amahaggataṃ", "không rộng lớn"), ("sauttaraṃ", "còn có điều cao hơn"),
               ("anuttaraṃ", "không có điều gì cao hơn"), ("samāhitaṃ", "được định tâm"),
               ("asamāhitaṃ", "không được định tâm"), ("vimuttaṃ", "được giải thoát"),
               ("avimuttaṃ", "không được giải thoát")):
    T79[f"{_p} vā cittaṃ"] = f"hoặc{GAP}tâm {_v}"                        # «hoặc đối với tâm có tham đắm»
# awakening factors (accusative / genitive forms of ch4's X-sambojjhaṅgo)
for _st, _v in (("sati", "sự tỉnh thức"), ("dhammavicaya", "sự tìm hiểu các hiện tượng"), ("vīriya", "sự tinh tấn"),
                ("pīti", "sự hân hoan"), ("passaddhi", "sự an tịnh"), ("samādhi", "định tâm"),
                ("upekkhā", "sự bình thản")):
    T79[f"{_st}sambojjhaṅgaṃ"] = _CS + _v
    T79[f"{_st}sambojjhaṅgassa"] = _CS + _v
    T79[f"{_st}sambojjhaṅgo"] = _CS + _v
    T79[f"{_st}sambojjhaṅgassa uppādo"] = _CS + _v + GAP + "nảy sinh"
    T79[f"uppannassa {_st}sambojjhaṅgassa"] = _CS + _v + " đã sinh khởi"
    T79[f"anuppannassa {_st}sambojjhaṅgassa"] = _CS + _v + " chưa sinh khởi"
    T79[f"{_st}sambojjhaṅgassa bhāvanāya pāripūrī"] = _CS + _v + GAP + "được tu tập đến chỗ hoàn thiện"
# hindrances in the dhammānupassanā clauses («ý muốn dục lạc chưa sinh khởi nảy sinh …»)
for _g, _l, _v in (("kāmacchandassa", "kāmacchandassa", "ý muốn dục lạc"),
                   ("vicikicchāya", "vicikicchāya", "sự hoài nghi")):
    _f = "uppannāya" if _g.endswith("āya") else "uppannassa"
    _af = "anuppannāya" if _g.endswith("āya") else "anuppannassa"
    _pf = "pahīnāya" if _g.endswith("āya") else "pahīnassa"
    T79[f"{_g} uppādo"] = _v + GAP + "nảy sinh"
    T79[f"{_f} {_g}"] = _v + " đã sinh khởi"
    T79[f"{_af} {_g}"] = _v + " chưa sinh khởi"
    T79[f"{_af} {_g} uppādo"] = _v + " chưa sinh khởi nảy sinh"
    T79[f"{_pf} {_g}"] = _v + " đã được dứt bỏ"


def context(bid, kw, k, s, text, kws):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set, kws: raw keywords). None = no rule."""
    if k == "viharati":       # first occurrence: «sống quán sát …» (satipaṭṭhāna formula) before «an trú» (jhāna)
        return "sống" if present("sống", text) else "an trú"
    if k == "vāyāmo":         # the defined noun of «Vāyamatīti» and the vīriya string: «sự nỗ lực»; sammāvāyāmo: «nỗ lực»
        return "sự nỗ lực" if ("Vāyamatīti" in kws or "asithila" in s) else "nỗ lực"
    if k == "padhānaṃ":       # «Tattha katamaṃ padhānaṃ?» «sự nỗ lực»; member of sammappadhānaṃ «nỗ lực đúng đắn»
        return "nỗ lực" if "sammappadhānaṃ" in s else "sự nỗ lực"
    if k in ("ārammaṇo", "ārammaṇā", "ārammaṇaṃ"):
        return "có đối tượng" if present("có đối tượng", text) else "lấy" + GAP + "làm đối tượng"
    if k in ("hetuko", "hetukā", "hetukaṃ"):
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    if k == "saṅkhāra":       # stem of saṅkhārakkhandho (tạo tác) / of padhānasaṅkhāra (sự tạo tác)
        return "tạo tác" if "saṅkhārakkhandho" in s else "sự tạo tác"
    if k == "dhammā kusalā":
        return "hiện tượng" + GAP + "thiện"                                # «Những hiện tượng này là thiện»
    if k == "ṭhiti":          # «Sự duy trì là …» (^2-406 / 2-420) vs the samādhi / vīriya strings «sự ổn định»
        return "sự duy trì" if "asammoso" in s else "sự ổn định"
    if k == "pāripūrī":
        return "sự hoàn thiện" if "asammoso" in s else "hoàn thiện"
    if k == "pāda":           # pādatalā «lòng bàn chân» (^2-356) / Iddhipāda «nền tảng thần thông»
        return "chân" if "kesā" in s else "nền tảng"
    return None


OVERRIDES = {
    # fragment of -vipākadhammadhammā (as ^2-170, ^2-217)
    "2-388": {"dhammā": NDE},
    "2-429": {"dhammā": NDE},
    "2-464": {"dhammā": NDE},
}


def resolver_for(part):
    vi = read_vietnamese(part)
    table = {**T45, **T79}

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context(bid, kw, k, s, text, kws)
        if v is not None:
            return v
        return value(kw, kws, table, text)
    return resolve


def dump(part, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
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
        p1 = pi1_map_values(kw).most_common(1)
        p1 = p1[0][0] if p1 else ""
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 and p1 != v else "")
              + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], len(sys.argv) > 3)
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
