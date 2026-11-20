"""Build the Pāli->Vietnamese keyword maps for pi-2 parts 10-bojjhangavibhango, 11-maggangavibhango and
12-jhanavibhango.

usage: python -I -X utf8 map_10-12_vi.py                    (writes the three <part>.mapped.md and verifies them)
       python -I -X utf8 map_10-12_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                            segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules) -> T1012 (this script's table)
-> T79 (map_7-9_vi.py) -> T45 (map_4-5_vi.py) -> map_common_vi.value(): KH (pi-2 table) -> the approved pi-1 chain.
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md,
notes-map-4-5.md, notes-map-6.md, notes-map-7-9.md, notes-map-10-12.md.
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


def _imp(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # import only: the earlier scripts build nothing unless run as a script
    return mod


M79 = _imp("map_79_vi", "map_7-9_vi.py")
T45, T79, context79 = M79.T45, M79.T79, M79.context

PARTS = ["10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango"]

_KX = "không xác định về mặt đạo đức"
_CS = "chi phần giác ngộ là "
_BJ = "chi phần giác ngộ"

T1012 = {
    # ================================================================ ch. 10 headings and names
    "bojjhaṅga": _BJ, "bojjhaṅgā": _BJ, "bojjhaṅgānaṃ": _BJ, "bojjhaṅgehi": _BJ,
    "sambojjhaṅga": _BJ,
    # ---- Suttanta (^2-467)
    "uppajjati": "sinh khởi", "passambhati": "lắng dịu", "kāyopi": "thân", "nepakkena": "sự khôn ngoan",
    "nepakka": "sự khôn ngoan", "satinepakkena": "sự tỉnh thức và sự khôn ngoan",
    "samāhitaṃ": "đã được định tâm", "cirakatampi": "những việc đã làm từ lâu",
    "cirabhāsitampi": "những lời đã nói từ lâu", "viharanto": "khi sống", "samannāgato": "được trang bị",
    "pavicinati": "tìm hiểu", "pavicarati": "xem xét", "parivīmaṃsamāpajjati": "thẩm xét toàn diện",
    "āpajjati": "thực hiện",                                             # pi-1; of parivīmaṃsamāpajjati: context()
    "sukhino": "có hạnh phúc", "paramena": "tột bậc", "āraddhaṃ": "được khởi động",
    "pītimanassa": "có tâm hân hoan", "satimā": "có sự tỉnh thức", "anussaritā": "nhớ lại được",
    "saritā": "nhớ được", "asallīnaṃ": "không chùng xuống", "dhammaṃ": "hiện tượng",
    "nirāmisā": "không có tính trần tục", "ajjhupekkhitā": "nhìn với sự bình thản trọn vẹn", "paññāya": "trí tuệ",
    # ---- ^2-469
    "sambodhāya": "sự giác ngộ hoàn toàn", "abhiññāya": "sự hiểu biết trực tiếp", "nibbānāya": "Niết-bàn",
    "kāyikaṃ": "nơi thân", "citta": "tâm",                               # kāya: context (kāyapassaddhi)
    "pavicayo": "sự tìm hiểu kỹ",
    "tadapi": "cũng",                                                    # «A cũng là “X”» (predicate «là» dropped)
    "saṃvattati": "dẫn đến", "cetasikaṃ": "trong tâm",
    "vitakko": "sự hướng tâm", "vicāro": "sự duy trì tâm",
    "kāyapassaddhi": "sự an tịnh của thân tinh thần", "cittapassaddhi": "sự an tịnh của tâm",
    # ---- ^2-471
    "viveka": "sự tách biệt", "virāga": "sự phai nhạt", "nirodha": "sự chấm dứt", "vossagga": "sự buông xả",
    "pariṇāmiṃ": "hướng đến", "sambojjhaṅgaṃ bhāveti": "tu tập chi phần giác ngộ",
    # ---- Abhidhamma (^2-474)
    "khandhassa": "khối", "vedanākkhandhassa": "khối cảm giác", "saññākkhandhassa": "khối tri giác",
    "saṅkhārakkhandhassa": "khối tạo tác", "viññāṇakkhandhassa": "khối thức",
    "passambhanā": "sự lắng dịu", "paṭippassambhanā": "sự lắng dịu hoàn toàn",
    "paṭippassambhitattaṃ": "trạng thái đã lắng dịu hoàn toàn", "paṭippassaddhi": "sự an tịnh hoàn toàn",
    "pāmojjaṃ": "sự phấn khởi", "āmodanā": "sự vui vẻ", "pamodanā": "sự vui thích", "hāso": "sự tươi cười",
    "pahāso": "sự rạng rỡ", "vitti": "sự mãn nguyện", "odagyaṃ": "sự phấn chấn", "attamanatā": "sự hài lòng",
    "upekkhanā": "sự giữ bình thản", "ajjhupekkhanā": "sự bình thản trọn vẹn", "majjhattatā": "sự cân bằng",
    "cittassa": "tâm",
    # ---- Pañhāpucchaka
    "vitakka": "sự hướng tâm", "vicāra": "sự duy trì tâm", "vicārā": "sự duy trì tâm", "vitakkā": "sự hướng tâm",
    "na hetū": "không phải là gốc rễ", "cittā": "tâm",
    "saṃsaṭṭha": "hòa lẫn", "upādā": "phái sinh", "dhamma": "hiện tượng",
    "araṇāti": "không có xung đột",
    # ================================================================ ch. 11 (Maggaṅga)
    "aṅga": "chi phần", "aṅgaṃ": "chi phần", "aṅgānaṃ": "chi phần", "maggaṅga": "chi phần của con đường",
    "maggaṅgā": "chi phần của con đường", "maggaṅgānaṃ": "chi phần của con đường",
    "maggo": "con đường", "ariyo": "cao quý", "seyyathidaṃ": "cụ thể là",
    "aṭṭhaṅgiko": "gồm tám chi phần", "aṭṭhaṅgiko maggo": "con đường gồm tám chi phần",
    "pañcaṅgiko": "gồm năm chi phần", "pañcaṅgiko maggo": "con đường gồm năm chi phần",
    "saṅkappo": "tư duy", "vācā": "lời nói", "ājīvo": "sinh kế", "kammanto": "hành động",
    # accusative / instrumental members of sammā-X (^2-489 «tu tập X đúng đắn», ^2-497 «gắn liền với X đúng đắn»)
    "diṭṭhiṃ": "quan điểm", "saṅkappaṃ": "tư duy", "vācaṃ": "lời nói", "kammantaṃ": "hành động",
    "ājīvaṃ": "sinh kế", "vāyāmaṃ": "nỗ lực", "satiṃ": "tỉnh thức", "samādhiṃ": "định tâm",
    "diṭṭhiyā": "quan điểm", "saṅkappena": "tư duy", "vāyāmena": "nỗ lực", "satiyā": "tỉnh thức",
    "samādhinā": "định tâm",
    # ^2-487 Suttanta definitions (ch. 4 values)
    "musāvādā veramaṇī": "sự kiềm chế việc nói dối", "pāṇātipātā veramaṇī": "sự kiềm chế việc sát hại sinh mạng",
    "adinnādānā veramaṇī": "sự kiềm chế việc lấy của không được cho",
    "kāmesumicchācārā veramaṇī": "sự kiềm chế hành vi sai trái trong các dục lạc",
    "jīvikaṃ": "nuôi sống bản thân",                                   # jīvikaṃ kappeti «nuôi sống bản thân»
    "vitakkavicārānaṃ": "sự hướng tâm và sự duy trì tâm",
    "dhammesu dhammānupassī": "hiện tượng" + GAP + "quán sát các hiện tượng",
    "citte cittānupassī": "tâm" + GAP + "quán sát tâm",
    "sukhaṃ": "hạnh phúc",                                               # jhāna formula (ch. 4 ^2-205); feeling: context
    # ^2-492 abstention string
    "ārati": "sự tránh xa", "virati": "sự kiêng tránh", "paṭivirati": "sự kiêng tránh hoàn toàn",
    "veramaṇī": "sự kiềm chế", "velā": "giới hạn", "setu": "cây cầu", "ghāto": "sự phá bỏ",
    "duccaritehi": "hành vi xấu", "byappanā": "sự gắn tâm chặt chẽ",
    # ================================================================ ch. 12 (Jhāna)
    "jhāna": "tầng thiền", "mātikā": "ma trận",
    # ---- ^2-508 matrix: conduct
    "pātimokkha": "bộ giới luật căn bản", "saṃvara": "sự thu thúc", "saṃvaro": "sự thu thúc",
    "saṃvuto": "được thu thúc", "ācāra": "hạnh kiểm đúng đắn", "gocara": "nơi lui tới thích hợp",
    "sampanno": "đầy đủ", "aṇumattesu": "nhỏ nhặt", "vajjesu": "lỗi", "aṇumattesu vajjesu": "lỗi nhỏ nhặt",
    "bhaya": "sự nguy hiểm", "dassāvī": "thấy", "samādāya": "thọ trì", "sikkhati": "tu học",
    "sikkhā": "tu học", "padesu": "điều",                               # sikkhāpadesu «các điều tu học»
    "indriyesu": "giác quan", "gutta": "phòng hộ", "dvāro": "cửa", "bhojane": "ăn uống",
    "mattaññū": "biết tiết độ", "bhojane mattaññū": "biết tiết độ trong ăn uống",
    "pubbarattāpararattaṃ": "đầu đêm và cuối đêm",
    "jāgariyānuyogamanuyutto": "chuyên tâm thực hành việc thức canh", "anuyutto": "chuyên tâm",
    "sātaccaṃ": "sự liên tục", "nepakkaṃ": "sự khôn ngoan", "bodhi": "sự giác ngộ",
    "pakkhikānaṃ": "hỗ trợ", "bodhipakkhikānaṃ": "hỗ trợ cho sự giác ngộ",
    "bodhipakkhikānaṃ dhammānaṃ": "hiện tượng hỗ trợ cho sự giác ngộ",
    "sampajānakārī": "hành động với sự hiểu biết rõ ràng", "sampajāna": "sự hiểu biết rõ ràng",
    "abhikkante": "khi đi tới", "paṭikkante": "khi đi lui", "ālokite": "khi nhìn thẳng",
    "vilokite": "khi nhìn quanh", "samiñjite": "khi co tay chân", "pasārite": "khi duỗi tay chân",
    "saṅghāṭi": "y ngoài", "patta": "bát", "cīvara": "y", "dhāraṇe": "khi mang",
    "asite": "khi ăn", "pīte": "khi uống", "khāyite": "khi nhai", "sāyite": "khi nếm",
    "uccāra": "đại tiện", "passāva": "tiểu tiện", "gate": "khi đi", "ṭhite": "khi đứng", "nisinne": "khi ngồi",
    "sutte": "khi ngủ", "jāgarite": "khi thức", "bhāsite": "khi nói", "tuṇhībhāve": "khi im lặng",
    "tuṇhī": "im lặng",
    "vivittaṃ": "thanh vắng", "senāsanaṃ": "chỗ ở", "vivittaṃ senāsanaṃ": "chỗ ở thanh vắng", "bhajati": "lui tới",
    "araññaṃ": "rừng", "rukkha": "cây", "mūlaṃ": "gốc", "pabbataṃ": "núi", "kandaraṃ": "khe núi",
    "guhaṃ": "hang núi", "susānaṃ": "bãi tha ma", "vanapatthaṃ": "rừng sâu", "patthaṃ": "rừng sâu",
    "abbhokāsaṃ": "khoảng trời trống", "palāla": "rơm", "puñjaṃ": "đống",
    "saddaṃ": "tiếng động", "nigghosaṃ": "ồn ào", "vijanavātaṃ": "vắng hơi người", "vātaṃ": "hơi",
    "manussa": "người đời", "rāhasseyyakaṃ": "kín đáo", "paṭisallāna": "sự độc cư", "sāruppaṃ": "thích hợp",
    "suññāgāragato": "đi đến ngôi nhà trống", "āgāra": "nhà", "gato": "đi đến", "nisīdati": "ngồi xuống",
    "pallaṅkaṃ": "kiết già", "ābhujitvā": "xếp chân", "ujuṃ": "ngay thẳng", "kāyaṃ": "thân",
    "parimukhaṃ": "trước mặt", "upaṭṭhapetvā": "thiết lập",
    # ---- ^2-508: hindrances
    "abhijjhaṃ": "sự thèm muốn", "vigatābhijjhena": "đã lìa sự thèm muốn", "cetasā": "tâm",
    "vigatābhijjhena cetasā": "tâm đã lìa sự thèm muốn", "parisodheti": "làm trong sạch hoàn toàn",
    "cittaṃ parisodheti": "làm trong sạch hoàn toàn tâm",
    "byāpāda": "ác ý", "padosaṃ": "sự sân hận dữ dội", "pāṇa": "chúng sinh", "bhūta": "muôn loài",
    "ānukampī": "thương xót", "hitānukampī": "thương xót và mong điều lợi ích",
    "thinamiddhaṃ": "sự uể oải và đờ đẫn", "āloka": "ánh sáng", "saññī": "có tri giác", "sato": "tỉnh thức",
    "uddhaccakukkuccaṃ": "sự xao động và hối tiếc", "anuddhato": "không xao động",
    "vūpasanta": "đã lắng dịu hoàn toàn", "vicikicchaṃ": "sự hoài nghi", "tiṇṇa": "đã vượt qua",
    "akathaṃkathī": "không còn băn khoăn", "kusalesu": "thiện", "kusalesu dhammesu": "hiện tượng thiện",
    "nīvaraṇe": "chướng ngại", "upakkilese": "những thứ làm vẩn đục", "dubbalīkaraṇe": "làm suy yếu",
    "vicikicchaṃ pahāya": "sau khi dứt bỏ sự hoài nghi",
    "thinamiddhaṃ pahāya": "sau khi dứt bỏ sự uể oải và đờ đẫn",
    "uddhaccakukkuccaṃ pahāya": "sau khi dứt bỏ sự xao động và hối tiếc",
    "akusalehi": "bất thiện", "akusalehi dhammehi": "hiện tượng bất thiện", "dhammehi": "hiện tượng",
    "domanassānaṃ": "nỗi buồn", "dukkhassa": "sự khó chịu",
    # ---- ^2-508: formless
    "rūpasaññānaṃ": "tri giác về hình sắc", "paṭighasaññānaṃ": "tri giác về sự va chạm", "paṭigha": "sự va chạm",
    "nānattasaññānaṃ": "tri giác về sự đa dạng", "saññānaṃ": "tri giác", "amanasikārā": "không chú tâm",
    "ananto": "vô tận", "ākāso": "không gian", "natthi kiñcī": "không có gì cả",
    "ākāsānañcāyatanaṃ": "lĩnh vực không gian vô tận", "viññāṇañcāyatanaṃ": "lĩnh vực thức vô tận",
    "ākiñcaññāyatanaṃ": "lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatanaṃ": "lĩnh vực không phải tri giác cũng không phải không tri giác",
    "āyatanaṃ": "lĩnh vực", "viññāṇa": "thức",
    # ---- ^2-509 «Idhā»
    "diṭṭhiyā": "quan điểm", "khantiyā": "sự chấp nhận", "ruciyā": "sự ưa thích", "ādāye": "sự tiếp nhận",
    "dhamme": "Giáo Pháp", "vinaye": "Giới Luật", "dhammavinaye": "Giáo Pháp và Giới Luật", "pāvacane": "lời dạy",
    "brahmacariye": "đời sống tu hành trong sạch", "cariye": "đời sống tu hành", "satthu": "Bậc Đạo Sư",
    "sāsane": "giáo huấn", "tena": "vì thế",
    # ---- ^2-510 «Bhikkhū»
    "samaññāya": "danh xưng", "paṭiññāya": "sự tự xưng", "bhikkhatīti": "đi khất thực",
    "bhikkhakoti": "người khất thực", "bhikkhā": "khất thực", "cariyaṃ": "đời sống", "bhinna": "vụn",
    "paṭa": "mảnh vải", "dharoti": "mặc", "bhindati": "phá vỡ", "bhinnattā": "đã phá vỡ",
    "odhiso": "một phần", "anodhiso": "toàn bộ", "kilesānaṃ": "phiền não", "pahānā": "dứt bỏ",
    "sekkho": "còn đang tu học", "asekkho": "đã hoàn tất tu học", "aggo": "hàng đầu", "bhadro": "hiền thiện",
    "sāro": "cốt lõi", "samaggena saṅghena": "Tăng đoàn hòa hợp", "saṅghena": "Tăng đoàn",
    "ñatticatutthena": "gồm một lời đề nghị và ba lần tuyên bố", "ñatti": "lời đề nghị", "kammena": "tăng sự",
    "akuppena": "không thể bị hủy bỏ", "ṭhānārahena": "xứng đáng được duy trì", "ārahena": "xứng đáng",
    "upasampanno": "đã được thọ giới đầy đủ",
    # ---- ^2-511 … 2-516 (pātimokkha, ācāra / gocara, vajja, sikkhā)
    "sīlaṃ": "giới hạnh", "sīla": "giới hạnh", "patiṭṭhā": "nền tảng", "ādi": "khởi đầu", "caraṇaṃ": "sự thực hành",
    "saṃyamo": "sự tự chế", "saṃyama": "sự tự chế", "mokkhaṃ": "sự giải thoát", "pāmokkhaṃ": "điều đứng đầu",
    "samāpattiyā": "để thành tựu", "saṃvutoti": "được thu thúc",
    "kāyiko": "bằng thân", "vācasiko": "bằng lời nói", "avītikkamo": "sự không vi phạm",
    "vītikkamo": "sự vi phạm", "kāyiko avītikkamo": "sự không vi phạm bằng thân",
    "ācāro": "hạnh kiểm đúng đắn", "anācāro": "hạnh kiểm sai trái", "dussīlyaṃ": "sự phạm giới",
    "ekacco": "có người", "dānena": "việc biếu", "veḷu": "tre", "puppha": "hoa", "phala": "trái cây",
    "sināna": "đồ tắm", "dantakaṭṭha": "cây chà răng", "cāṭukamyatāya": "lời nịnh bợ",
    "muggasūpyatāya": "lời nửa thật nửa giả", "pāribhaṭayatāya": "việc chăm bẵm con trẻ",
    "jaṅgha": "chạy", "pesanikena": "việc vặt", "buddha": "Đức Phật", "paṭikuṭṭhena": "bị" + GAP + "chê trách",
    "ājīvena": "sinh kế",
    "gocaro": "nơi lui tới thích hợp", "agocaro": "nơi lui tới không thích hợp", "gocarena": "nơi lui tới thích hợp",
    "ācārena": "hạnh kiểm đúng đắn", "vesiyā": "kỹ nữ", "vidhavā": "góa phụ", "thulla": "lớn tuổi",
    "kumāri": "thiếu nữ", "paṇḍaka": "người ái nam ái nữ", "pānāgāra": "quán rượu", "saṃsaṭṭho": "giao du",
    "rājūhi": "vua chúa", "rāja": "vua chúa", "mahāmattehi": "quan đại thần", "titthiyehi": "đạo sĩ ngoại đạo",
    "sāvakehi": "đệ tử", "ananulomikena": "không thích đáng", "kulāni": "gia đình", "saddhāni": "có niềm tin",
    "bhūtāni": "như", "akkosaka": "hay mắng nhiếc", "paribhāsakāni": "lăng mạ", "kāmāni": "mong",
    "anattha": "không lợi ích", "ahita": "không tốt lành", "hita": "tốt lành", "aphāsuka": "không thoải mái",
    "phāsuka": "thoải mái", "khema": "an ổn", "yoga": "an ổn",                # yogakkhema «an ổn» (not the cluster «ách»)
    "bhikkhūnaṃ": "tỳ-khưu", "bhikkhunīnaṃ": "tỳ-khưu-ni", "upāsakānaṃ": "nam cư sĩ", "upāsikānaṃ": "nữ cư sĩ",
    "kāsāva": "y cà-sa", "pajjotāni": "rực sáng", "isi": "bậc ẩn sĩ", "vāta": "gió", "paṭivātāni": "thổi qua lại",
    "sevati": "gần gũi", "payirupāsati": "thường xuyên lui tới hầu cận",
    "appamattakāni": "nhỏ", "oramattakāni": "nhỏ bé", "lahusāni": "nhẹ", "sammatāni": "được xem là",
    "karaṇīyāni": "cần được xử lý bằng", "cittuppādakaraṇīyāni": "cần được xử lý bằng sự khởi tâm",
    "uppāda": "khởi", "manasikāra": "sự chú tâm", "paṭibaddhāni": "gắn liền với", "vajja": "lỗi",
    "ādīnava": "sự tai hại", "nissaraṇa": "lối thoát",
    "sabbena sabbaṃ": "một cách toàn bộ", "sabbathā": "về mọi mặt", "asesaṃ": "không thiếu sót",
    "nissesaṃ": "không sót lại gì", "padesū": "điều", "sikkhāyo": "sự tu học",
    # ---- ^2-517 sense restraint (pi-1 ^1-1352 … words where the same)
    "guttadvāratā": "sự phòng hộ cửa", "gutti": "sự canh giữ", "agutti": "sự không canh giữ",
    "gopanā": "sự bảo vệ", "ārakkho": "sự che chở", "cakkhunā": "mắt", "sotena": "tai", "ghānena": "mũi",
    "jivhāya": "lưỡi", "kāyena": "thân", "manasā": "ý", "rūpaṃ": "hình sắc", "gandhaṃ": "mùi", "rasaṃ": "vị",
    "phoṭṭhabbaṃ": "vật xúc chạm", "dhammaṃ": "hiện tượng", "sutvā": "nghe", "ghāyitvā": "ngửi",
    "sāyitvā": "nếm", "phusitvā": "chạm", "viññāya": "nhận biết", "nimitta": "dấu hiệu", "gāhī": "nắm giữ",
    "cakkhundriyaṃ": "năng lực mắt", "manindriyaṃ": "năng lực ý", "asaṃvutaṃ": "không được thu thúc",
    "cakkhundriyaṃ asaṃvutaṃ": "năng lực mắt không được thu thúc",
    "manindriyaṃ asaṃvutaṃ": "năng lực ý không được thu thúc", "viharantaṃ": "sống",
    "abhijjhādomanassā": "sự thèm muốn và nỗi buồn", "domanassā": "nỗi buồn", "pāpakā": "xấu ác",
    "anvāssaveyyuṃ": "có thể tràn vào", "saṃvarāya": "thu thúc", "paṭipajjati": "thực hành",
    "rakkhati": "bảo vệ", "saṃvaraṃ āpajjati": "thực hiện sự thu thúc",
    "akusalā dhammā": "hiện tượng" + GAP + "bất thiện",                # «các hiện tượng xấu ác bất thiện»
    # ---- ^2-518 food
    "mattaññutā": "sự biết tiết độ", "bhojane mattaññutā": "sự biết tiết độ trong ăn uống",
    "santuṭṭhitā": "sự biết đủ", "asantuṭṭhitā": "sự không biết đủ", "paṭisaṅkhā": "suy xét",
    "yoniso": "đúng cách", "ayoniso": "không đúng cách", "āhāreti": "ăn", "davāya": "vui đùa",
    "madāya": "say sưa", "maṇḍanāya": "trang điểm", "vibhūsanāya": "làm đẹp", "kāyassa": "thân",
    "yāpanāya": "kéo dài", "vihiṃsūparatiyā": "chấm dứt sự bức bách",
    "brahmacariyānuggahāya": "hỗ trợ đời sống tu hành trong sạch", "ānuggahāya": "hỗ trợ", "iti": "như vậy",
    "purāṇañca": "cũ", "vedanaṃ": "cảm giác", "yātrā": "sự duy trì mạng sống", "anavajjatā": "sự không có lỗi",
    "phāsu": "thoải mái", "vihāro": "sự an trú",
    # ---- ^2-519 wakefulness
    "rattiyā": "đêm", "yāmaṃ": "canh", "majjhima": "giữa", "caṅkamena": "đi kinh hành", "nisajjāya": "ngồi",
    "āvaraṇīyehi": "gây chướng ngại", "āvaraṇīyehi dhammehi": "hiện tượng gây chướng ngại",
    "āvaraṇīyehi dhammehi cittaṃ": "tâm khỏi các hiện tượng gây chướng ngại",
    "dakkhiṇena": "bên phải", "passena": "nghiêng", "sīha": "sư tử", "seyyaṃ": "tư thế",
    "pāde": "chân", "accādhāya": "đặt" + GAP + "lên", "saññaṃ": "tri giác", "manasikaritvā": "sau khi chú tâm",
    "paccuṭṭhāya": "sau khi thức dậy",
    # ---- ^2-520 … 2-522
    "sātacca": "sự liên tục", "nepakka": "sự khôn ngoan", "aṅgo": "chi phần", "aṅgā": "chi phần",
    # ---- ^2-523 … 2-525 clear comprehension
    "sato sampajānakārī": "hành động với sự tỉnh thức và hiểu biết rõ ràng",
    "abhikkamati": "đi tới", "paṭikkamati": "đi lui", "āloketi": "nhìn thẳng", "viloketi": "nhìn quanh",
    "samiñjeti": "co tay chân", "pasāreti": "duỗi tay chân",
    "paṭissati": "sự hồi tưởng", "saraṇatā": "sự ghi nhớ", "dhāraṇatā": "sự gìn giữ trong trí nhớ",
    "apilāpanatā": "sự không hời hợt", "asammusanatā": "sự không quên lãng", "satindriyaṃ": "năng lực tỉnh thức",
    "sampajaññaṃ": "sự hiểu biết rõ ràng", "paññindriyaṃ": "năng lực trí tuệ",
    # ---- ^2-526 … 2-537 lodging and posture
    "santike": "ở gần", "dūre": "ở xa", "anākiṇṇaṃ": "không bị" + GAP + "chen chúc",
    "gahaṭṭhehi": "người tại gia", "pabbajitehi": "người xuất gia",
    "mañcopi": "giường", "pīṭhampi": "ghế", "bhisipi": "nệm", "bibbohanampi": "gối", "vihāropi": "tịnh xá",
    "aḍḍhayogopi": "nhà một mái", "pāsādopi": "lâu đài", "aṭṭopi": "tháp canh", "māḷopi": "nhà mái tròn",
    "leṇampi": "động đá", "guhāpi": "hang", "mūlampi": "gốc", "gumbopi": "bụi",          # -pi «cũng»: frame
    "bhikkhū": "tỳ-khưu", "paṭikkamanti": "lui về", "yattha vā pana": "hoặc bất cứ nơi nào",
    "sambhajati": "lui tới thường xuyên", "nisevati": "gần gũi thường xuyên", "saṃsevati": "gần gũi trọn vẹn",
    "nikkhamitvā": "sau khi đi ra", "bahi": "ngoài", "indakhīlā": "cột trụ ở cổng làng",
    "pabbato": "núi", "kandarā": "khe núi", "guhā": "hang núi", "abbhokāso": "khoảng trời trống", "puñjo": "đống",
    "adhivacanaṃ": "tên gọi", "senāsanānaṃ": "chỗ ở", "senāsanānaṃ adhivacanaṃ": "tên gọi của những chỗ ở",
    "vanapattha": "rừng sâu", "pattha": "rừng sâu", "dūrānametaṃ": "xa xôi", "vanasaṇḍānametaṃ": "lùm rừng",
    "bhīsanakānametaṃ": "đáng sợ", "salomahaṃsānametaṃ": "làm sởn tóc gáy", "pariyantānametaṃ": "ở vùng biên",
    "manussūpacārānametaṃ": "có người qua lại", "ūpacārānametaṃ": "qua lại",   # of «na manussūpacārānametaṃ»
    "durabhisambhavānametaṃ": "khó chịu đựng",
    "mūla": "gốc", "arañña": "rừng", "nisinno": "đã ngồi", "ujuko": "ngay thẳng", "kāyo": "thân",
    "ṭhito": "được giữ vững", "paṇihito": "được đặt đúng cách",
    "nāsikagge": "chóp mũi", "agge": "chóp", "mukha": "miệng", "nimitte": "vùng",
    # ---- ^2-538 … 2-550 the hindrance lemmas (pi-1 strings ^1-1160 … 1163)
    "pahāyā": "sau khi dứt bỏ", "vigatābhijjhena": "đã lìa sự thèm muốn", "ābhijjhena": "sự thèm muốn",
    "abhijjhāya": "sự thèm muốn", "sodheti": "làm trong sạch", "moceti": "làm cho thoát khỏi",
    "vimoceti": "làm cho thoát hẳn", "parimoceti": "làm cho thoát hoàn toàn",
    "parisodhetī": "làm trong sạch hoàn toàn", "cittaṃ parisodhetī": "làm trong sạch hoàn toàn tâm",
    "byāpādo": "ác ý", "padoso": "sự sân hận dữ dội", "asuropo": "sự nói năng cộc cằn",
    "kujjhitattaṃ": "trạng thái khởi giận", "dussanā": "sự khởi sân",   # the noun itself (pi-1 «khởi sân» = fragment)
    "abyāpannaṃ": "không có ác ý", "abyāpannacitto": "có tâm không ác ý",
    "viharatī": "sống",
    "thinamiddhaṃ pahāyā": "sau khi dứt bỏ sự uể oải và đờ đẫn", "thinaṃ": "sự uể oải",
    "thiyanā": "sự khởi uể oải", "anto": "bên trong", "samorodho": "sự bế tắc", "onāho": "sự bao phủ",
    "pariyonāho": "sự bao phủ hoàn toàn", "akalyatā": "sự không khỏe khoắn", "suppaṃ": "giấc ngủ",
    "suppanā": "sự ngủ", "pacalāyikā": "sự gà gật", "līyitattaṃ": "trạng thái khởi co rút",
    "vigata": "đã lìa", "thinamiddhassa": "sự uể oải và đờ đẫn", "middhassa": "đờ đẫn",
    "cattattā": "đã được xả bỏ", "vantattā": "đã được nhả ra", "muttattā": "đã được thả ra",
    "pahīnattā": "đã được dứt bỏ", "paṭinissaṭṭhattā": "đã được buông bỏ",
    "pahīnapaṭinissaṭṭhattā": "đã được dứt bỏ và buông bỏ",
    "ālokā": "sáng sủa", "vivaṭā": "được khai mở", "parisuddhā": "trong sạch", "pariyodātā": "sáng tỏ",
    "thinamiddhā": "sự uể oải và đờ đẫn",
    "uddhaccakukkuccaṃ pahāyā": "sau khi dứt bỏ sự xao động và hối tiếc", "uddhaccaṃ": "sự xao động",
    "avūpasamo": "sự không lắng xuống", "vikkhepo": "sự tán loạn", "cetaso vikkhepo": "sự tán loạn của tâm",
    "bhantattaṃ": "trạng thái rối loạn", "akappiye": "không được phép", "kappiye": "được phép",
    "avajje": "không đáng chê trách", "vajje": "đáng chê trách", "saññitā": "tri giác",
    "evarūpaṃ": "thuộc loại như vậy", "yaṃ": "điều mà", "kukkuccāyanā": "sự khởi hối tiếc",
    "vippaṭisāro": "sự ân hận", "vilekhā": "sự giằng xé", "vilekho": "sự giằng xé",
    "kukkuccassa": "hối tiếc", "uddhaccakukkuccassa": "sự xao động và hối tiếc",
    "uddhaccakukkuccā": "sự xao động và hối tiếc", "samitaṃ": "đã được làm lắng dịu",
    "vūpasantaṃ": "đã lắng dịu hoàn toàn", "vūpasantacitto": "có tâm đã lắng dịu hoàn toàn",
    "vicikicchaṃ pahāyā": "sau khi dứt bỏ sự hoài nghi", "vicikicchā": "sự hoài nghi",
    "kaṅkhāyanā": "sự khởi nghi ngờ", "vimati": "sự phân vân", "dveḷhakaṃ": "sự lưỡng lự",
    "dvidhāpatho": "sự đứng trước ngã ba đường", "saṃsayo": "sự ngờ vực", "anekaṃsa": "không" + GAP + "điều chắc chắn",
    "gāho": "nắm giữ", "āsappanā": "sự chần chừ", "parisappanā": "sự do dự", "apariyogāhaṇā": "sự không đi sâu",
    "chambhitattaṃ": "trạng thái cứng đờ",
    "tiṇṇo": "đã vượt qua", "nittiṇṇo": "đã vượt thoát", "pāra": "bờ bên kia",
    "vicikicchāya": "sự hoài nghi", "vicikicchati": "hoài nghi", "nikkathaṃkathī": "hết băn khoăn",
    "vikathaṃkatho": "lìa băn khoăn", "nīvaraṇehi": "chướng ngại", "nirujjhati": "chấm dứt",
    "chando": "ý muốn", "chandarāgo": "ý muốn và sự tham đắm", "saṅkapparāgo": "sự tham đắm do tư duy",
    "kāmo": "dục lạc", "kāmacchando": "ý muốn dục lạc",
    # ---- ^2-565 … 2-577 the first and second jhāna lemmas
    "cāro": "sự chuyển động của tâm", "anucāro": "sự chuyển động tiếp nối", "upavicāro": "sự duy trì tâm sát sao",
    "anusandhanatā": "sự gắn kết liên tục" + GAP + "với đối tượng", "anupekkhanatā": "sự theo dõi sát đối tượng",
    "jātā": "đã sinh", "sañjātā": "đã sinh ra", "nibbattā": "đã phát khởi", "abhinibbattā": "đã hình thành",
    "pātubhūtā": "đã xuất hiện", "viveke": "sự tách biệt", "samādhimhi": "định tâm", "sampasādo": "sự trong sáng",
    "cittassekaggatā": "sự nhất tâm", "ekaggatā": "sự nhất tâm",
    "pītisukha": "sự hân hoan và hạnh phúc", "sahagataṃ": "đi kèm", "sahajātaṃ": "cùng sinh",
    "saṃsaṭṭhaṃ": "hòa lẫn", "sampayuttaṃ": "gắn liền",
    "cetasikaṃ sātaṃ": "sự khoan khoái trong tâm", "cetasikaṃ sukhaṃ": "sự dễ chịu trong tâm", "sātaṃ": "khoan khoái",
    "sātaṃ sukhaṃ": "khoan khoái và dễ chịu", "sātaṃ sukhaṃ vedayitaṃ": "cảm nhận khoan khoái và dễ chịu",
    "sātā sukhā vedanā": "cảm giác khoan khoái và dễ chịu", "sukhaṃ vedayitaṃ": "cảm nhận" + GAP + "dễ chịu",
    "sukhā vedanā": "cảm giác" + GAP + "dễ chịu", "cetosamphassajaṃ": "sinh từ sự tiếp xúc của tâm",
    "samāpajjatīti": "chứng nhập", "gaṇanānupubbatā": "theo thứ tự đếm", "ānupubbatā": "thứ tự",
    "jhānassa": "tầng thiền", "lābho": "sự đạt được", "upasampajjā": "chứng nhập",
    "vitakkavicārānaṃ vūpasamā": "sự hướng tâm và sự duy trì tâm lắng xuống",
    "ajjhatta": "ở nơi bản thân", "sampasādana": "sự trong sáng", "ekodibhāva": "sự hợp nhất",
    # ---- ^2-583 … 2-597 the third and fourth jhāna lemmas
    "khandho": "khối", "sukhañca": "hạnh phúc", "paṭisaṃvedetī": "cảm nhận",
    "buddhā": "Đức Phật", "sāvakā": "đệ tử", "desenti": "thuyết giảng", "paññapenti": "trình bày",
    "paṭṭhapenti": "xác lập", "vivaranti": "khai mở", "vibhajanti": "phân tích", "uttāniṃ": "làm sáng tỏ",
    "pakāsenti": "công bố",
    "kāyasamphassajaṃ": "sinh từ sự tiếp xúc của thân", "dukkhaṃ vedayitaṃ": "cảm nhận" + GAP + "khó chịu",
    "asātaṃ dukkhaṃ vedayitaṃ": "cảm nhận bứt rứt và khó chịu", "asātā dukkhā vedanā": "cảm giác bứt rứt và khó chịu",
    "somanassaṃ": "niềm vui", "nāsātaṃ": "không bứt rứt",
    "adukkhamasukhā vedanā": "cảm giác không khó chịu cũng không dễ chịu", "pārisuddhi": "hoàn toàn trong sạch",
    # ---- ^2-598 … 2-621 the formless lemmas
    "catutthassa jhānassa": "tầng thiền thứ tư", "rūpa": "hình sắc", "rūpāvacara": "thuộc cõi hình sắc",
    "samāpattiṃ": "sự chứng đạt", "upapannassa": "người đã tái sinh", "diṭṭhadhamma": "ngay trong đời này",
    "vihārissa": "an trú", "sukhavihārissa": "người an trú trong hạnh phúc",
    "atikkanto": "đã vượt qua", "vītikkanto": "đã vượt khỏi", "samatikkanto": "đã vượt qua hoàn toàn",
    "samatikkammā": "vượt qua",
    "vuccanti paṭighasaññāyo": "được gọi là các tri giác về sự va chạm", "sadda": "âm thanh",
    "phoṭṭhabba": "vật xúc chạm",
    "asamāpannassa": "người chưa chứng nhập", "samaṅgissa": "có", "manasi karoti": "chú tâm",
    "gataṃ": "điều được xem là", "aghaṃ": "khoảng không", "vivaro": "kẽ hở", "asamphuṭṭhaṃ": "không bị" + GAP + "chạm đến",
    "bhūtehi": "yếu tố", "mahābhūtehi": "yếu tố cơ bản", "ṭhapeti": "đặt", "saṇṭhapeti": "đặt" + GAP + "vững chắc",
    "pharati": "lan tỏa", "cetasikā": "yếu tố đồng hành với tâm", "āyatanassa": "lĩnh vực",
    "ākāsānañcāyatanassa": "lĩnh vực không gian vô tận", "ākāsaṃ": "không gian", "phuṭṭhaṃ": "chạm đến",
    "anantaṃ": "vô tận",
    "viññāṇañcāyatanassa": "lĩnh vực thức vô tận", "ākiñcaññāyatanassa": "lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatanassa": "lĩnh vực không phải tri giác cũng không phải không tri giác",
    "vibhāveti": "làm cho tan biến",
    "saṅkhārāvasesasamāpattiṃ": "sự chứng đạt còn sót lại các sự tạo tác", "āvasesa": "còn sót lại",
    "santato": "như là điều an tịnh", "nāsaññī": "không có tri giác",
    "nevasaññīnāsaññī": "không phải có tri giác cũng không phải không có tri giác",
    "jhānāni": "tầng thiền",
    # ---- Abhidhammabhājanīya (^2-624 …; ch. 6 opening values)
    "rūpārūpāvacarakiriyā": "Tâm mang tính chức năng thuộc cõi hình sắc và cõi không hình sắc",
    "kiriyā": "mang tính chức năng", "ārūpāvacara": "cõi không hình sắc",
    "maggaṃ": "con đường", "maggaṃ bhāveti": "tu tập con đường", "ūpapattiyā": "tái sinh",
    "rūpūpapattiyā": "tái sinh vào cõi hình sắc", "arūpūpapattiyā": "tái sinh vào cõi không hình sắc",
    "rūpūpapattiyā maggaṃ": "con đường dẫn đến tái sinh vào cõi hình sắc",
    "arūpūpapattiyā maggaṃ": "con đường dẫn đến tái sinh vào cõi không hình sắc",
    "pathavī": "đất", "kasiṇaṃ": "đề mục bao trùm", "pathavīkasiṇaṃ": "đề mục bao trùm là đất",
    "pañcaṅgikaṃ": "gồm năm chi phần", "caturaṅgikaṃ": "gồm bốn chi phần", "tivaṅgikaṃ": "gồm ba chi phần",
    "duvaṅgikaṃ": "gồm hai chi phần", "pañcamaṃ": "thứ năm", "sukhassa": "sự dễ chịu",
    "nevasaññānāsaññāyatana": "lĩnh vực không phải tri giác cũng không phải không tri giác",
    "upacitattā": "tích lũy", "kusalassa kammassa": "nghiệp thiện",               # «đã được tạo và tích lũy»
    "rūpāvacarassa": "thuộc cõi hình sắc", "arūpāvacarassa": "thuộc cõi không hình sắc",
    # ---- ^2-636 / 2-637 kiriya openings (ch. 6 / pi-1 values)
    "kiriyaṃ": "mang tính chức năng", "nākusalaṃ": "không phải bất thiện",
    "neva kusalaṃ nākusalaṃ": "không phải thiện không phải bất thiện",              # comma dropped (ch. 4)
    "vihāraṃ": "an trú", "sukhavihāraṃ": "an trú trong hạnh phúc",
    "rūpāvacaraṃ": "thuộc cõi hình sắc", "arūpāvacaraṃ": "thuộc cõi không hình sắc",
    "arūpāvacaraṃ jhānaṃ": "tầng thiền thuộc cõi không hình sắc",
    "rūpāvacaraṃ jhānaṃ": "tầng thiền thuộc cõi hình sắc",
    # ---- Pañhāpucchaka (^2-639 … 2-641): «X – etthuppannaṃ Y ṭhapetvā …» «ngoại trừ Y sinh khởi trong đó»
    "jhānānaṃ": "tầng thiền", "ṭhapetvā": "ngoại trừ", "etthuppannaṃ": "sinh khởi trong đó",
    "vedanaṃ": "cảm giác", "sukhaṃ vedanaṃ": "cảm giác dễ chịu", "pītiṃ": "sự hân hoan",
    "upekkhaṃ": "sự bình thản", "vicāre": "sự duy trì tâm", "vitakkavicāre": "sự hướng tâm và sự duy trì tâm",
    "etthuppannaṃ sukhaṃ": "hạnh phúc sinh khởi trong đó",
    "etthuppannaṃ pītiṃ": "sự hân hoan sinh khởi trong đó",
    "etthuppannaṃ upekkhaṃ": "sự bình thản sinh khởi trong đó",
    "etthuppannaṃ vicāraṃ": "sự duy trì tâm sinh khởi trong đó",
    "etthuppanne vitakkavicāre": "sự hướng tâm và sự duy trì tâm sinh khởi trong đó",
}
for _n, _v in (("pañc", "năm"), ("catur", "bốn"), ("tiv", "ba"), ("duv", "hai")):
    T1012[f"{_n}aṅgikaṃ jhānaṃ"] = f"tầng thiền gồm {_v} chi phần"
for _a in ("dūrānametaṃ", "durabhisambhavānametaṃ", "salomahaṃsānametaṃ", "pariyantānametaṃ"):
    T1012[f"{_a} senāsanānaṃ"] = "chỗ ở " + T1012[_a]               # «những chỗ ở xa xôi» («những» frame)
for _st, _v in (("sati", "sự tỉnh thức"), ("dhammavicaya", "sự tìm hiểu các hiện tượng"), ("vīriya", "sự tinh tấn"),
                ("pīti", "sự hân hoan"), ("passaddhi", "sự an tịnh"), ("samādhi", "định tâm"),
                ("upekkhā", "sự bình thản")):
    T1012[f"{_st}sambojjhaṅga"] = _CS + _v                              # stem of X-sambojjhaṅgasampayuttā


def context(bid, kw, k, s, text, kws):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set, kws: raw keywords). None = no rule."""
    if k == "saṅkhāra":       # stem of saṅkhārakkhandho / -khandhassa (tạo tác) / of padhānasaṅkhāra (sự tạo tác)
        if s & {"saṅkhārakkhandho", "saṅkhārakkhandhassa"}:
            return "tạo tác"
    if k == "āpajjati" and "parivīmaṃsamāpajjati" in s:   # «thẩm xét toàn diện» (one Vietnamese phrase)
        return "thẩm xét toàn diện"
    if k == "kāya":           # stem of kāyapassaddhi «sự an tịnh của thân tinh thần» (pi-1) / «bằng thân» elsewhere
        return "thân tinh thần" if present("thân tinh thần", text) else "thân"
    if k in ("sati", "satiyā"):   # the factor «sự tỉnh thức»; only inside «tỉnh thức đúng đắn»: «tỉnh thức» (ch. 4)
        return "sự tỉnh thức" if present("sự tỉnh thức", text) else "tỉnh thức"
    if k == "sato":           # «với sự tỉnh thức và hiểu biết rõ ràng» (^2-523, 2-525) / «tỉnh thức và …»
        return "sự tỉnh thức" if "sato sampajānakārī" in s else "tỉnh thức"
    if k in ("aṭṭhaṅgiko maggo", "pañcaṅgiko maggo"):   # «Con đường cao quý gồm tám chi phần» (ch. 4 ^2-205)
        v = "con đường gồm " + ("tám" if k[0] == "a" else "năm") + " chi phần"
        return v if present(v, text) else "con đường" + GAP + v[len("con đường "):]
    if k == "ariya" and "sāvako" in s:   # ariyasāvako «vị đệ tử của bậc thánh»
        return "bậc thánh"
    if k == "sampanno":       # «đầy đủ hạnh kiểm …» (ācāragocarasampanno) / «đã thành tựu» in the upeto list
        return "đã thành tựu" if "upeto" in s else "đầy đủ"
    if k == "patta":          # pattadānena «việc biếu lá» / saṅghāṭipattacīvara «bát»
        return "lá" if "veḷu" in s else "bát"
    if k == "vattati" and "samādāya" in s:   # samādāya vattati «thọ trì và thực hành»
        return "thực hành"
    if k in ("viharati", "viharatī"):   # «sống» (conduct passages) / «an trú» (jhāna passages, pi-1)
        return "sống" if present("sống", text) and not present("an trú", text.split("sống")[0]) else "an trú"
    if k == "kāyassa":        # middha string «… của thân tinh thần» (pi-1 ^1-1163) / «thân này» (^2-518)
        return "thân tinh thần" if present("thân tinh thần", text) else "thân"
    if k == "middhaṃ" and "thinaṃ" in s:     # the defined noun «sự đờ đẫn» (^2-546)
        return "sự đờ đẫn"
    if k == "kukkuccaṃ" and "uddhaccaṃ" in s:   # the defined noun «sự hối tiếc» (^2-552)
        return "sự hối tiếc"
    if k == "akusalā dhammā":   # «các hiện tượng bất thiện» / «các hiện tượng xấu ác bất thiện»
        return "hiện tượng bất thiện" if present("hiện tượng bất thiện", text) else "hiện tượng" + GAP + "bất thiện"
    if k == "gato" and "pāra" in s:         # pāraṅgato «đã sang bờ bên kia»
        return "đã sang"
    if k == "kappeti" and "sīha" in s:       # sīhaseyyaṃ kappeti «nằm … theo tư thế sư tử»
        return "nằm"
    if k == "saddaṃ":         # appasaddaṃ «ít tiếng động» / the sense object «âm thanh»
        return "tiếng động" if present("tiếng động", text) and not present("âm thanh", text) else "âm thanh"
    if k == "dhammaṃ" and "manasā" in s:     # manasā dhammaṃ viññāya «nhận biết đối tượng của ý bằng ý»
        return "đối tượng của ý"
    if k == "bhikkhu":        # «vị tỳ-khưu» / bare «tỳ-khưu» in the «Bhikkhū» definitions
        return "vị tỳ-khưu" if present("vị tỳ-khưu", text) else "tỳ-khưu"
    return context79(bid, kw, k, s, text, kws)


OVERRIDES = {
    # fragment of -vipākadhammadhammā (as ^2-170, ^2-217, ^2-388)
    "2-484": {"dhammā": NDE},
    # «Sukhassa ca pahānā …»: the defined nouns «sự dễ chịu» / «sự khó chịu» (bodily)
    "2-594": {"sukhaṃ": "sự dễ chịu", "dukkhaṃ": "sự khó chịu"},
    # somanassa / domanassa strings: «sự dễ chịu trong tâm» / «sự khó chịu trong tâm»
    "2-595": {"sukhaṃ": "dễ chịu", "dukkhaṃ": "khó chịu", "cetasikaṃ": "trong tâm"},
    # «trạng thái trong tâm không khoan khoái cũng không bứt rứt» (pi-1 rule)
    "2-596": {"cetasikaṃ": "trạng thái trong tâm"},
}


def resolver_for(part):
    vi = read_vietnamese(part)
    table = {**T45, **T79, **T1012}

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
