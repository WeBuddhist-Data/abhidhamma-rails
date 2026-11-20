"""Build the Pāli->Vietnamese keyword map for pi-2 part 17-khuddakavatthuvibhango.

usage: python -I -X utf8 map_17_vi.py                    (writes 17-khuddakavatthuvibhango.mapped.md and verifies it)
       python -I -X utf8 map_17_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                         segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context17() (segment rules) -> T17 (this script's table)
-> map_16_vi.context() -> T16 -> map_13-15_vi.context() -> T1315 -> T1012 -> T79 -> T45 -> map_common_vi.value():
KH (pi-2 table) -> the approved pi-1 chain.
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md …
notes-map-16.md, notes-map-17.md.
"""
import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, present,  # noqa: E402
                           read_keywords, read_pali, read_vietnamese, value, verify)


def _imp(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # import only: the earlier scripts build nothing unless run as a script
    return mod


M16 = _imp("map_16_vi", "map_16_vi.py")
T45, T79, T1012, T1315, T16 = M16.T45, M16.T79, M16.T1012, M16.T1315, M16.T16
context16, context1315 = M16.context, M16.context1315

PARTS = ["17-khuddakavatthuvibhango"]

_SM = "sự say sưa"
_KM = "sự kiêu mạn"
_GS = "gắn với đời sống thế tục"
_NDT = "Niết-bàn ngay trong đời này"

T17 = {
    # ================================================================ headings and the matrix (2-832 … 2-842)
    "khuddaka": "nhỏ", "vatthu": "chủ đề",                              # «Phân tích các chủ đề nhỏ»
    # ---- ekaka: mada
    "mado": _SM, "jātimado": _SM + " vì xuất thân", "gottamado": _SM + " vì dòng họ",
    "pāripūrimado": _SM + " vì sự hoàn hảo", "gottamadādī": _SM + " vì dòng họ và những điều tương tự",
    "ādī": "những điều tương tự", "ādīni": "những điều tương tự", "ganthādī": "nút thắt và những điều tương tự",
    "gotta": "dòng họ", "ārogya": "sức khỏe", "yobbana": "tuổi trẻ", "lābha": "lợi lộc",
    "purekkhāra": "sự được ưu tiên", "parivāra": "đoàn tùy tùng", "rattaññu": "thâm niên",
    "piṇḍapātika": "hạnh khất thực", "anavaññāta": "việc không bị xem nhẹ", "anavaññatti": "việc không bị xem nhẹ",
    "iriyāpatha": "tư thế", "yasa": "danh tiếng", "sippa": "nghề thủ công", "āroha": "chiều cao",
    "pariṇāha": "vóc người to lớn", "saṇṭhāna": "hình dáng", "pāripūri": "sự hoàn hảo", "siloka": "tiếng tăm",
    "pamādo": "sự buông thả", "thambho": "sự cứng đầu", "sārambho": "sự tranh hơn",
    "atricchatā": "sự tham muốn quá độ", "mahicchatā": "sự có nhiều tham muốn", "pāpicchatā": "sự có ước muốn xấu xa",
    "siṅgaṃ": "sự kiểu cách", "tintiṇaṃ": "sự khó tính", "cāpalyaṃ": "sự phù phiếm",
    "asabhāga": "không thích đáng", "vutti": "lối cư xử", "arati": "sự không hoan hỷ", "tandī": "sự lười nhác",
    "vijambhitā": "sự vươn vai", "bhatta": "bữa ăn", "sammado": "sự ngầy ngật",
    "līnattaṃ": "sự co rút", "cetaso ca līnattaṃ": "sự co rút của tâm",
    "kuhanā": "sự lừa gạt", "lapanā": "sự nói ngọt", "nemittikatā": "sự ra dấu gợi ý", "nippesikatā": "sự chèn ép",
    "nijigīsanatā": "sự" + GAP + "tìm kiếm", "lābhaṃ nijigīsanatā": "sự" + GAP + "tìm kiếm lợi lộc",
    # ---- ekaka: māna
    "sadisohamasmīti": "Tôi bằng người", "hīnohamasmīti": "Tôi kém người", "seyyohamasmīti": "Tôi hơn người",
    "seyyassa": "của người vốn hơn người", "sadisassa": "của người vốn bằng người",
    "hīnassa": "của người vốn kém người",
    "atimāno": "sự ngạo mạn", "mānātimāno": "sự kiêu mạn chồng chất", "ātimāno": "chồng chất",
    "omāno": "sự tự ti", "adhimāno": "sự tự đánh giá quá cao", "asmimāno": _KM + " “Tôi là”",
    "micchāmāno": _KM + " sai lầm",
    # ---- ekaka: vitakka
    "janapada": "xứ sở", "amara": "sự bất tử", "paṭisaṃyutto": "liên quan đến",
    "paṭisaṃyutto vitakko": "sự hướng tâm liên quan đến", "ānuddayatā": "sự quan tâm",
    "parānuddayatāpaṭisaṃyutto": "liên quan đến sự quan tâm đến người khác",
    # ---- duka
    "upanāho": "sự ôm hận", "makkho": "sự gièm pha", "paḷāso": "sự ganh đua", "macchariyañca": "sự keo kiệt",
    "māyā": "sự xảo trá", "sāṭheyyañca": "sự gian xảo",
    "antavādiṭṭhi": "quan điểm về sự hữu hạn", "anantavādiṭṭhi": "quan điểm về sự vô hạn",
    "pāpa": "người xấu", "pāpamittatā": "sự kết bạn với người xấu",
    "anajjavo": "sự không ngay thật", "amaddavo": "sự không mềm mỏng", "akkhanti": "sự không nhẫn nại",
    "asoraccañca": "sự không hiền hòa", "asākhalyañca": "sự không hòa nhã",
    "appaṭisanthāro": "sự không niềm nở tiếp đón", "aguttadvāratā": "sự không phòng hộ cửa",
    "amattaññutā": "sự không biết tiết độ", "bhojane amattaññutā": "sự không biết tiết độ trong ăn uống",
    "muṭṭhassaccañca": "sự mất tỉnh thức", "muṭṭhassaccaṃ": "sự mất tỉnh thức",
    "vipatti": "sự suy đồi", "diṭṭhivipatti": "sự suy đồi về quan điểm", "sīlavipatti": "sự suy đồi về giới hạnh",
    "saṃyojanañca": "xiềng xích",
    # ---- tika
    "akusalavitakkā": "sự hướng tâm bất thiện", "akusalasaññā": "tri giác bất thiện",
    "akusaladhātuyo": "yếu tố bất thiện", "duccaritāni": "hành vi xấu", "esanā": "sự tìm cầu", "vidhā": "sự so sánh",
    "bhayāni": "nỗi sợ hãi", "tamāni": "sự tăm tối", "titthāyatanāni": "lĩnh vực của các học thuyết ngoại đạo",
    "kiñcanā": "sự vướng bận", "aṅgaṇāni": "vết nhơ", "malāni": "sự dơ bẩn", "visamāni": "sự lệch lạc",
    "aggī": "ngọn lửa", "kasāvā": "chất cặn bẩn", "assāda": "sự thỏa thích",
    "assādadiṭṭhi": "quan điểm về sự thỏa thích", "attānudiṭṭhi": "quan điểm xem có tự ngã",
    "vihesā": "sự gây phiền nhiễu", "cariyā": "hành vi", "adhammacariyā": "hành vi phi pháp",
    "nānattasaññā": "tri giác về sự đa dạng", "kosajjaṃ": "sự lười biếng",
    "asampajaññatā": "sự thiếu hiểu biết rõ ràng", "assaddhiyaṃ": "sự thiếu niềm tin",
    "avadaññutā": "sự không rộng lượng", "kamyatā": "muốn", "saddhammaṃ": "Giáo Pháp chân chính",
    "asotukamyatā": "sự không muốn nghe", "upārambha": "bắt lỗi", "upārambhacittatā": "sự có tâm hay bắt lỗi",
    "ayoniso": "không khôn ngoan", "ayoniso manasikāro": "sự chú tâm không khôn ngoan",
    "kummagga": "con đường lệch lạc",
    # ---- catukka
    "taṇhuppādā": "nguyên nhân khởi lên khao khát", "agati": "con đường sai trái", "gamanāni": "sự đi theo",
    "vipariyāsā": "sự đảo ngược", "anariya": "không cao quý", "vohārā": "cách nói", "diṭṭhiyo": "quan điểm",
    # ---- pañcaka
    "saṅgā": "sự dính mắc", "sallā": "mũi tên", "khilā": "sự chai cứng", "vinibandhā": "sự trói buộc",
    "verā": "điều gây thù địch", "ādīnavā": "điều nguy hại", "akkhantiyā": "sự không nhẫn nại",
    "nibbānavādā": "học thuyết về Niết-bàn",
    # ---- chakka
    "vivāda": "tranh cãi", "chandarāgā": "sự tham đắm do ý muốn", "virodha": "sự chống đối", "kāyā": "nhóm",
    "agāravā": "sự thiếu kính trọng", "parihāniyā": "dẫn đến suy thoái",
    "parihāniyā dhammā": "hiện tượng dẫn đến suy thoái", "upavicārā": "sự lưu tâm",
    "somanassupavicārā": "sự lưu tâm gắn với niềm vui", "domanassupavicārā": "sự lưu tâm gắn với nỗi buồn",
    "upekkhupavicārā": "sự lưu tâm gắn với sự bình thản", "gehasitāni": _GS, "gehasitā": _GS,
    "somanassāni": "niềm vui", "domanassāni": "nỗi buồn", "gehasitāni somanassāni": "niềm vui " + _GS,
    "gehasitāni domanassāni": "nỗi buồn " + _GS, "gehasitā upekkhā": "sự bình thản " + _GS,
    # ---- sattaka … dasaka
    "anusayā": "khuynh hướng tiềm ẩn", "pariyuṭṭhānāni": "sự ám ảnh", "asaddhammā": "điều không chân chính",
    "kusītavatthūni": "chỗ dựa của sự lười biếng", "kusīta": "sự lười biếng",
    "lokadhammesu": "hiện tượng thế gian", "micchattā": "sự sai lầm", "dosā": "lỗi",
    "asaññī": "không có tri giác", "asaññi": "không có tri giác",
    "nevasaññināsaññi": "không phải có tri giác cũng không phải không có tri giác",
    "āghāta": "sự oán giận", "navavidhā": "chín loại", "mūlakā": "bắt nguồn từ",
    "mūlakā dhammā": "hiện tượng bắt nguồn từ", "iñjitāni": "sự dao động", "maññitāni": "sự tưởng tượng",
    "phanditāni": "sự rung động", "papañcitāni": "sự suy diễn lan man", "saṅkhatāni": "điều được tạo tác",
    "maññitādīni": "sự tưởng tượng và những điều tương tự",
    "pathā": "con đường", "dasa saṃyojanāni": "mười xiềng xích", "dasa micchattā": "mười sự sai lầm",
    "dasavatthukā": "có mười chủ đề", "vatthukā": "có" + GAP + "chủ đề",
    "dasavatthukā micchādiṭṭhi": "quan điểm sai lầm có mười chủ đề", "antaggāhikā": "chấp giữ cực đoan",
    "antaggāhikā diṭṭhi": "quan điểm chấp giữ cực đoan",
    "dasavatthukā antaggāhikā diṭṭhi": "quan điểm chấp giữ cực đoan có mười chủ đề",
    # ---- taṇhāvicarita
    "taṇhāvicarita": "dòng khao khát", "vicarita": "dòng", "vicaritāni": "dòng",
    "taṇhāvicaritāni": "dòng khao khát", "ajjhattikassa": "phần bên trong", "bāhirassa": "phần bên ngoài",
    "bhagavatā": "Đức Thế Tôn", "veyyākaraṇe": "bài giảng", "gatāni": NDE, "sataṃ": "một trăm",
    "dvāsaṭṭhi": "sáu mươi hai", "vuttāni": "đã được" + GAP + "nói đến", "chattiṃsa": "ba mươi sáu",
    # ================================================================ ekaka definitions (2-843 …)
    # ---- mada (+ the pi-1 ^1-1239 māna string)
    "jātiṃ paṭicca": "dựa vào xuất thân", "paṭicca": "dựa vào", "majjanā": "sự khởi say sưa",
    "majjitattaṃ": "trạng thái khởi say sưa", "unnāmo": "sự vênh vang", "unnati": "sự tự cao",
    "gottaṃ": "dòng họ", "ārogyaṃ": "sức khỏe", "yobbanaṃ": "tuổi trẻ", "jīvitaṃ": "sự sống", "lābhaṃ": "lợi lộc",
    "sakkāraṃ": "sự tôn vinh", "garukāraṃ": "sự kính trọng", "purekkhāraṃ": "sự được ưu tiên",
    "parivāraṃ": "đoàn tùy tùng", "bhogaṃ": "của cải", "vaṇṇaṃ": "sắc đẹp", "sutaṃ": "sự học hỏi",
    "paṭibhānaṃ": "tài ứng đáp", "rattaññutaṃ": "thâm niên", "piṇḍapātikattaṃ": "hạnh khất thực",
    "anavaññātaṃ": "việc không bị xem nhẹ", "iriyāpathaṃ": "tư thế", "iddhiṃ": "thần thông", "yasaṃ": "danh tiếng",
    "sīlaṃ": "giới hạnh", "jhānaṃ": "tầng thiền", "sippaṃ": "nghề thủ công", "ārohaṃ": "chiều cao",
    "pariṇāhaṃ": "vóc người to lớn", "saṇṭhānaṃ": "hình dáng", "pāripūriṃ": "sự hoàn hảo",
    # ---- pamāda (2-846)
    "kāyaduccarite": "hành vi xấu bằng thân", "vacīduccarite": "hành vi xấu bằng lời nói",
    "manoduccarite": "hành vi xấu bằng ý", "duccarite": "hành vi xấu", "kāmaguṇesu": "đối tượng của dục lạc",
    "guṇesu": "đối tượng", "kāmaguṇehi": "đối tượng của dục lạc", "guṇehi": "đối tượng",
    "vossaggo": "sự buông lơi", "cittassa vossaggo": "sự buông lơi của tâm",
    "ānuppadānaṃ": "sự tiếp tục để mặc", "asakkaccakiriyatā": "sự làm không chu đáo",
    "asātaccakiriyatā": "sự làm không liên tục", "anaṭṭhitakiriyatā": "sự làm có ngừng nghỉ",
    "anaṭṭhita": "có ngừng nghỉ", "vuttitā": "sự hành xử", "anāsevanā": "sự không thực hành",
    "abhāvanā": "sự không tu tập", "abahulīkammaṃ": "sự không làm đi làm lại", "anadhiṭṭhānaṃ": "sự không quyết tâm",
    "ananuyogo": "sự không chuyên cần", "pamajjanā": "sự khởi buông thả", "pamajjitattaṃ": "trạng thái khởi buông thả",
    # ---- thambha / sārambha
    "kakkhaḷiyaṃ": "tính thô cứng", "phārusiyaṃ": "tính thô lỗ", "ujucittatā": "sự cao ngạo của tâm",
    "amudutā": "sự không mềm mại", "thambhitattaṃ": "trạng thái khởi cứng đầu",
    "paṭisārambho": "sự tranh hơn đáp trả", "sārambhanā": "hành động tranh hơn",
    "paṭisārambhanā": "hành động tranh hơn đáp trả", "paṭisārambhitattaṃ": "trạng thái tranh hơn đáp trả",
    # ---- atricchatā / mahicchatā / pāpicchatā
    "itarītara": "thế này hay thế khác", "piṇḍapāta": "đồ ăn khất thực", "senāsana": "chỗ ở",
    "gilāna": "chữa bệnh", "paccaya": "vật dụng", "bhesajja": "thuốc men", "asantuṭṭhassa": "người không biết đủ",
    "bhiyyokamyatā": "sự mong muốn nhiều hơn nữa", "icchā": "sự mong muốn",
    "icchāgatā": "trạng thái bị mong muốn chi phối",
    "assaddho": "không có niềm tin", "dussīlo": "phạm giới", "appassuto": "ít học hỏi", "ārāmo": "ưa thích",
    "kusīto": "lười biếng", "muṭṭhassatī": "mất tỉnh thức", "asamāhito": "không được định tâm",
    "duppañño": "kém trí tuệ", "akhīṇāsavo": "chưa diệt tận các ô nhiễm", "saddhoti": "người có niềm tin",
    "sīlavāti": "người giữ giới", "bahussutoti": "người học rộng", "pavivittoti": "người sống tách biệt",
    "āraddhavīriyoti": "người tinh tấn", "upaṭṭhitassatīti": "người có sự tỉnh thức được thiết lập",
    "samāhitoti": "người được định tâm", "paññavāti": "người có trí tuệ",
    "khīṇāsavoti": "người đã diệt tận các ô nhiễm", "jano": "người ta", "jānātū": "biết", "icchati": "mong muốn",
    # ---- siṅga / tintiṇa / cāpalya
    "siṅgāratā": "sự điệu đà", "cāturatā": "sự khôn lỏi", "cāturiyaṃ": "tính khôn lỏi",
    "parikkhattatā": "sự quanh co", "pārikkhattiyaṃ": "tính quanh co",
    "tintiṇāyanā": "sự khởi khó tính", "tintiṇāyitattaṃ": "trạng thái khởi khó tính", "loluppaṃ": "sự ham hố",
    "loluppāyanā": "sự khởi ham hố", "loluppāyitattaṃ": "trạng thái khởi ham hố", "pucchañjikatā": "sự xu nịnh",
    "sādhukamyatā": "sự mong muốn điều tốt đẹp",
    "maṇḍanā": "sự trang trí", "vibhūsanā": "sự tô điểm", "keḷanā": "sự nâng niu",
    "parikeḷanā": "sự nâng niu khắp nơi", "giddhikatā": "sự ham thích", "giddhikattaṃ": "tính ham thích",
    "capalatā": "sự nhẹ dạ", "pūti": "hôi thối", "bāhirānaṃ": "bên ngoài", "parikkhārānaṃ": "vật dụng",
    # ---- asabhāgavutti / arati / tandī / vijambhitā
    "mātari": "mẹ", "pitari": "cha", "jeṭṭhe": "người lớn tuổi hơn", "bhātari": "anh em", "ācariyesu": "vị thầy",
    "upajjhāye": "thầy tế độ", "buddhe": "Đức Phật", "sāvakesu": "đệ tử", "aññataraññataresu": "bất kỳ" + GAP + "nào",
    "garu": "kính trọng", "ṭhāniyesu": "đáng", "ggāhitā": "sự tiếp nhận", "anādariyatā": "thái độ thiếu tôn trọng",
    "appatissavatā": "sự không vâng lời", "agāravatā": "sự thiếu kính trọng",
    "pantesu": "xa vắng", "senāsanesu": "chỗ ở", "aratitā": "trạng thái không hoan hỷ",
    "anabhirati": "sự không thích thú", "anabhiramaṇā": "sự không ưa thích", "ukkaṇṭhitā": "sự chán chường",
    "paritassitā": "sự bồn chồn",
    "tandiyanā": "sự khởi lười nhác", "tandimanakatā": "tâm trạng lười nhác", "ālasyaṃ": "sự biếng trễ",
    "ālasyāyanā": "sự khởi biếng trễ", "ālasyāyitattaṃ": "trạng thái khởi biếng trễ",
    "jambhanā": "sự vươn mình", "vijambhanā": "sự vươn mình mạnh", "ānamanā": "sự cúi xuống",
    "vinamanā": "sự ngả ra", "sannamanā": "sự co lại", "paṇamanā": "sự nghiêng người",
    "byādhiyakaṃ": "sự uể oải như bệnh",
    # ---- bhattasammada / cetaso līnatta
    "bhuttāvissa": "người đã ăn xong", "kilamatho": "sự mệt mỏi", "duṭṭhullaṃ": "sự nặng nề",
    "thīyanā": "sự khởi uể oải",
    # ---- kuhanā … nijigīsanatā («Ở người bám vào lợi lộc, sự tôn vinh và tiếng tăm, …»; comma dropped)
    "lābhasakkārasilokasannissitassa": "người bám vào lợi lộc sự tôn vinh và tiếng tăm",
    "lābhasakkārasilokasannissito": "người bám vào lợi lộc sự tôn vinh và tiếng tăm",
    "sannissitassa": "bám vào", "sannissito": "bám vào", "pāpicchassa": "có ước muốn xấu xa",
    "pāpiccho": "có ước muốn xấu xa", "icchāpakatassa": "bị ước muốn chi phối", "icchāpakato": "bị ước muốn chi phối",
    "pakatassa": "chi phối", "pakato": "chi phối",
    "saṅkhātena": "bằng điều gọi là", "sāmantajappitena": "lời nói bóng gió", "jappitena": "lời nói",
    "iriyāpathassa": "tư thế", "aṭhapanā": "sự sắp đặt", "ṭhapanā": "sự bày đặt", "saṇṭhapanā": "sự dàn dựng",
    "bhākuṭitā": "sự nhăn mặt", "bhākuṭiyaṃ": "vẻ nhăn mặt", "kuhāyanā": "sự khởi lừa gạt",
    "kuhitattaṃ": "trạng thái khởi lừa gạt",
    "paresaṃ": "người khác", "ālapanā": "sự bắt chuyện", "sallapanā": "sự trò chuyện thân mật",
    "ullapanā": "sự tâng bốc", "samullapanā": "sự tâng bốc hết mức", "unnahanā": "sự bợ đỡ",
    "samunnahanā": "sự bợ đỡ hết mức", "ukkācanā": "sự gợi lòng", "samukkācanā": "sự gợi lòng hết mức",
    "anuppiyabhāṇitā": "sự nói lời chiều lòng", "cāṭukamyatā": "lời nịnh bợ", "muggasūpyatā": "lời nửa thật nửa giả",
    "pāribhaṭayatā": "việc chăm bẵm con trẻ",
    "nimittakammaṃ": "việc ra dấu", "obhāsakammaṃ": "việc gợi ý", "sāmantajappā": "lời nói bóng gió",
    "parikathā": "lời nói vòng vo",
    "akkosanā": "sự mắng nhiếc", "vambhanā": "sự khinh miệt", "garahaṇā": "sự chê trách", "ukkhepanā": "sự chế giễu",
    "samukkhepanā": "sự chế giễu hết mức", "khipanā": "sự nhạo báng", "saṅkhipanā": "sự nhạo báng hết mức",
    "pāpanā": "sự bêu xấu", "sampāpanā": "sự bêu xấu hết mức", "avaṇṇahārikā": "sự loan truyền tiếng xấu",
    "avaṇṇa": "tiếng xấu", "hārikā": "sự loan truyền", "parapiṭṭhimaṃsikatā": "sự nói xấu sau lưng",
    "harati": "mang" + GAP + "đến", "āharati": "mang" + GAP + "về",
    # ---- māna (2-866 …): the twelve grounds
    "gottena": "dòng họ", "kolaputtiyena": "gia thế", "vaṇṇapokkharatāya": "vẻ đẹp dung mạo",
    "pokkharatāya": "dung mạo", "dhanena": "tài sản", "ajjhenena": "việc học tập kinh sách",
    "kammāyatanena": "ngành nghề", "āyatanena": "ngành", "sippāyatanena": "ngành thủ công",
    "vijjāṭṭhānena": "lĩnh vực học thuật", "ṭṭhānena": "lĩnh vực", "sutena": "sự học hỏi",
    "paṭibhānena": "tài ứng đáp", "vatthunā": "điều", "mānaṃ": "sự kiêu mạn", "omānaṃ": "sự tự ti",
    "jappeti": "nuôi dưỡng", "mānaṃ jappeti": "nuôi dưỡng sự kiêu mạn", "omānaṃ jappeti": "nuôi dưỡng sự tự ti",
    "omaññanā": "sự tự đánh giá thấp mình", "omaññitattaṃ": "trạng thái tự đánh giá thấp mình",
    "hīḷanā": "sự tự chê bai", "ohīḷanā": "sự tự chê bai thậm tệ", "ohīḷitattaṃ": "trạng thái tự chê bai thậm tệ",
    "attuññā": "sự tự coi thường", "attavaññā": "sự tự xem nhẹ", "attaparibhavo": "sự tự khinh miệt",
    "parehi": "người khác", "attānaṃ": "mình", "dahati": "tự cho", "sadisaṃ": "bằng", "sadiso": "bằng",
    "atimaññati": "tự cho" + GAP + "vượt trên",
    "adhigata": "đã chứng đắc", "kata": "đã làm", "sacchikata": "đã chứng nghiệm",
    "pāpakena": "xấu ác", "pāpakena vā kammāyatanena": "ngành nghề xấu ác", "sīlena": "giới hạnh",
    "vatena": "nghi thức", "sīlabbatena": "giới hạnh và nghi thức",
    # ---- vitakka (2-885 …)
    "gehasito": _GS, "geha": "đời sống thế tục", "ñātake": "người thân", "janapadaṃ": "xứ sở",
    "dukkara": "khổ hạnh", "kāritā": "việc thực hành", "gata": NDE,      # diṭṭhigata- «các quan điểm»
    "gihīhi": "người tại gia", "sahanandī": "vui cùng họ", "sahasokī": "buồn cùng họ",
    "sukhitesu": "khi họ hạnh phúc", "dukkhitesu": "khi họ khổ", "dukkhito": "khổ", "sukhito": "hạnh phúc",
    "uppannesu": "khi có", "kicca": "việc", "karaṇīyesu": "cần làm", "attanā": "tự mình", "yogaṃ": "dấn thân",
    "āpajjati": "dấn thân vào", "pare": "người khác", "avajāniṃsūti": "xem nhẹ",
    # ================================================================ duka definitions (2-891 …)
    "aparakālaṃ": "lúc sau", "pubbakālaṃ": "lúc trước", "upanayhanā": "sự khởi ôm hận",
    "upanayhitattaṃ": "trạng thái khởi ôm hận", "aṭṭhapanā": "sự lưu giữ", "anusaṃsandanā": "sự nối kết",
    "anuppabandhanā": "sự kéo dài liên tục", "daḷhīkammaṃ": "sự làm cho bền chặt",
    "makkhāyanā": "sự khởi gièm pha", "makkhāyitattaṃ": "trạng thái khởi gièm pha", "niṭṭhuriyaṃ": "sự khắc nghiệt",
    "niṭṭhuriyakammaṃ": "hành động khắc nghiệt", "paḷāsāyanā": "sự khởi ganh đua",
    "paḷāsāhāro": "sự ôm giữ sự ganh đua", "vivādaṭṭhānaṃ": "chỗ phát sinh tranh cãi",
    "yugaggāho": "sự đòi ngang hàng", "appaṭinissaggo": "sự không chịu buông bỏ",
    "macchariyaṃ": "sự keo kiệt",
    "caritvā": "sau khi làm", "vācāya": "lời nói", "paṭicchādanahetuṃ": "vì muốn che giấu", "pāpikaṃ": "xấu xa",
    "icchaṃ": "ước muốn", "paṇidahati": "đặt ra", "jaññā": "biết", "saṅkappeti": "suy tính", "bhāsati": "nói",
    "parakkamati": "hành động", "māyāvitā": "tính xảo trá", "accāsarā": "sự lấn lướt", "vañcanā": "sự lừa dối",
    "nikati": "sự gian lận", "vikiraṇā": "sự đánh lạc hướng", "pariharaṇā": "sự lảng tránh",
    "gūhanā": "sự giấu giếm", "parigūhanā": "sự giấu giếm kỹ", "chādanā": "sự che đậy",
    "anuttānīkammaṃ": "sự không bày tỏ", "anāvikammaṃ": "sự không bộc lộ", "vocchādanā": "sự che đậy hoàn toàn",
    "saṭho": "gian trá", "parisaṭho": "rất gian trá", "saṭhaṃ": "sự gian trá", "saṭhatā": "tính gian trá",
    "sāṭheyyaṃ": "sự gian xảo", "kakkaratā": "sự xảo quyệt", "kakkariyaṃ": "tính xảo quyệt",
    "ajjhosānaṃ": "sự đắm chìm", "bhavissati": "sẽ tồn tại", "mūlaṃ": "gốc rễ",
    "vippaṭikula": "ngang trái", "sampavaṅkatā": "sự nghiêng theo", "appassutā": "ít học hỏi",
    "anajjavatā": "tính không ngay thật", "amaddavatā": "sự không mềm mỏng", "kaṭhinatā": "sự cứng nhắc",
    "akkhamanatā": "sự không bao dung", "anadhivāsanatā": "sự không chịu đựng", "asoraccaṃ": "sự không hiền hòa",
    "kaṇḍakā": "gai góc", "parakaṭukā": "làm người khác đau lòng", "ābhisajjanī": "xúc phạm",
    "asamādhisaṃvattanikā": "không đưa đến định tâm", "bhāsitā": "nói",
    "asaṇhavācatā": "sự không dịu dàng trong lời nói", "asakhilavācatā": "sự không hòa nhã trong lời nói",
    "pharusavācatā": "sự thô ác trong lời nói", "asākhalyaṃ": "sự không hòa nhã",
    "appaṭisanthārako": "không niềm nở tiếp đón",
    "ggāhī": "nắm giữ", "indriyaṃ asaṃvutaṃ": "năng lực" + GAP + "không được thu thúc",
    "assati": "sự không tỉnh thức", "adhāraṇatā": "sự không gìn giữ trong trí nhớ",
    # ================================================================ tika definitions (2-909 …): pi-1 ^1-1065 lobha list
    "āsīsanā": "sự trông mong", "puttāsā": "sự mong mỏi con cái", "chadanaṃ": "sự che đậy",
    "nirodhataṇhā": "khao khát sự chấm dứt", "nandirāgo": "sự tham đắm vì thích thú",
    "appiyassa": "không yêu quý", "amanāpassa": "không ưa thích", "manopadoso": "sự sân hận dữ dội của ý",
    "jīvitāsā": "sự mong mỏi sự sống", "samuddo": "đại dương", "dukkhappabhavo": "cội nguồn của khổ đau",
    "saritā": "dòng chảy", "rūpāsā": "sự mong mỏi hình sắc", "gandhāsā": "sự mong mỏi mùi",
    "saddāsā": "sự mong mỏi âm thanh", "rasāsā": "sự mong mỏi vị", "phoṭṭhabbāsā": "sự mong mỏi vật xúc chạm",
    "dhanāsā": "sự mong mỏi tài sản", "lābhāsā": "sự mong mỏi lợi lộc", "parigedho": "sự thèm khát mãnh liệt",
    "gedho": "sự thèm khát", "āyūhanī": "kẻ thúc đẩy", "sotaṃ": "dòng nước",
    # ---- akusalavitakka / saññā / dhātu, duccarita
    "kāmavitakko": "sự hướng tâm đến dục lạc", "byāpādavitakko": "sự hướng tâm đến ác ý",
    "vihiṃsāvitakko": "sự hướng tâm đến sự hãm hại", "kāmapaṭisaṃyutto": "liên quan đến dục lạc",
    "kāmapaṭisaṃyuttā": "liên quan đến dục lạc", "paṭisaṃyuttā": "liên quan đến", "kāmasaññā": "tri giác về dục lạc",
    "byāpādasaññā": "tri giác về ác ý", "vihiṃsāsaññā": "tri giác về sự hãm hại",
    "byāpādadhātu": "yếu tố ác ý", "vihiṃsādhātu": "yếu tố hãm hại",
    "pāṇātipāto": "việc sát hại sinh mạng", "ātipāto": "việc sát hại", "ādānaṃ": "việc lấy",
    "musāvādo": "việc nói dối", "pisuṇā": "chia rẽ", "pharusā": "thô ác", "samphappalāpo": "việc nói lời phù phiếm",
    "kāyaduccaritaṃ": "hành vi xấu bằng thân", "vacīduccaritaṃ": "hành vi xấu bằng lời nói",
    "manoduccaritaṃ": "hành vi xấu bằng ý", "akusalaṃ kāyakammaṃ": "nghiệp bất thiện bằng thân",
    "akusalaṃ vacīkammaṃ": "nghiệp bất thiện bằng lời nói", "akusalaṃ manokammaṃ": "nghiệp bất thiện bằng ý",
    # ---- saṃyojana (pi-1 ^1-1262 …), taṇhā, esanā, vidhā, bhaya, tama
    "manovilekho": "sự giằng xé của ý", "saṅghe": "Tăng đoàn", "vantaṃ": "có", "adassāvī": "không thấy",
    "rūpaṃ attato samanupassati": "xem vật chất là tự ngã",
    "kāmesanā": "sự tìm cầu dục lạc", "bhavesanā": "sự tìm cầu sự hiện hữu",
    "brahmacariyesanā": "sự tìm cầu đời sống tu hành trong sạch", "tadekaṭṭhaṃ": "cùng hiện diện với nó",
    "ekaṭṭhaṃ": "cùng hiện diện",
    "sadisohamasmī": "Tôi bằng người", "hīnohamasmī": "Tôi kém người", "seyyohamasmī": "Tôi hơn người",
    "bhayānakaṃ": "sự kinh hãi", "lomahaṃso": "sự dựng tóc gáy", "utrāso": "sự hoảng hốt",
    "cetaso utrāso": "sự hoảng hốt của tâm", "nādhimuccati": "không quyết định",
    "sampasīdati": "có lòng tin trong sáng",
    # ---- titthāyatana, kiñcana, tika (24) …
    "samaṇo": "sa-môn", "brāhmaṇo": "bà-la-môn", "evaṃvādī": "có học thuyết như vầy",
    "evaṃdiṭṭhī": "có quan điểm như vầy", "diṭṭhī": "quan điểm", "purisapuggalo": "con người",
    "yaṃ kiñcāyaṃ": "bất cứ điều gì" + GAP + "này", "issara": "đấng Tự Tại", "nimmāna": "sự sáng tạo",
    "ahetu": "không có nguyên nhân", "appaccayā": "không có điều kiện", "kiñcanaṃ": "sự vướng bận",
    "pātabyataṃ āpajjati": "lao vào sự đắm say",
    "anaddā": "sự coi thường", "anaddāyanā": "sự khởi coi thường", "anaddāyitattaṃ": "trạng thái khởi coi thường",
    "asīlyaṃ": "sự thiếu lễ độ", "acittīkāro": "sự không quý trọng",
    "saddahati": "tin", "buddhaṃ": "Đức Phật", "assaddahanā": "sự không tin tưởng", "anokappanā": "sự không tin chắc",
    "bhavantattaṃ": "trạng thái rối loạn",                               # ^2-933 slip for bhantattaṃ, as meant
    "adaṭṭhukamyatā": "sự không muốn nhìn", "asametukamyatā": "sự không muốn đến gặp",
    "asamāgantukamyatā": "sự không muốn cùng hội họp",
    "anicce": "điều vô thường", "nicca": "thường còn", "subha": "đẹp", "asubhe": "điều không đẹp",
    "vippaṭikulena": "trái ngược", "anāvaṭṭanā": "sự hướng đến liên tục",
    # ================================================================ catukka / pañcaka (2-939 …)
    "bhikkhuno": "vị tỳ-khưu",
    "sabrahmacārīsu": "bạn đồng tu", "kupito": "nổi giận", "anattamano": "không hài lòng",
    "āhatacitto": "có tâm bị tổn thương", "khilajāto": "trở nên chai cứng",
    "micchācāro": "hành vi sai trái", "vādo": "việc nói",
    # ---- diṭṭhadhammanibbānavāda (2-943)
    "bho": "thưa ngài", "samappito": "được thỏa mãn", "samaṅgībhūto": "được đầy đủ", "paricāreti": "tận hưởng",
    "ettāvatā": "chỉ đến chừng ấy", "paramadiṭṭhadhammanibbānappatto": "đạt đến Niết-bàn tối thượng ngay trong đời này",
    "paramadiṭṭhadhammanibbāna": "Niết-bàn tối thượng ngay trong đời này", "parama": "tối thượng",
    "paramadiṭṭhadhammanibbānaṃ paññapenti": "trình bày Niết-bàn tối thượng ngay trong đời này",
    "natthīti": "không tồn tại", "vadesi": "nói", "kissa hetu": "vì sao", "aniccā": "vô thường",
    "vipariṇāmadhammā": "có bản chất biến đổi", "aññathābhāvā": "trở nên khác đi", "yadeva": "bởi vì",
    "vitakkitaṃ": "sự hướng tâm", "vicāritaṃ": "sự duy trì tâm",
    "vitakkitaṃ vicāritaṃ": "sự hướng tâm" + GAP + "sự duy trì tâm", "akkhāyati": "được xem là",
    "uppilāvitaṃ": "sự phấn khích", "evaṃdiṭṭhi": "có quan điểm như vầy",
    # ================================================================ chakka (2-944 …)
    "sandiṭṭhi": "quan điểm của mình", "agāravo": "thiếu kính trọng", "appatisso": "không vâng lời",
    "agāravo viharati": "sống thiếu kính trọng", "appamāde": "sự không buông thả",
    "paṭisanthāre": "sự niềm nở tiếp đón",
    "kammārāmatā": "sự ưa thích công việc", "ārāmatā": "sự ưa thích", "bhassārāmatā": "sự ưa thích nói chuyện",
    "niddārāmatā": "sự ưa thích ngủ nghỉ", "saṅgaṇikārāmatā": "sự ưa thích tụ tập",
    "manāpiyesu": "đáng ưa thích", "rūpesu": "hình sắc", "saddesu": "âm thanh", "gandhesu": "mùi", "rasesu": "vị",
    "phoṭṭhabbesu": "vật xúc chạm", "gehasitaṃ": _GS,
    "gehasitaṃ cetasikaṃ sātaṃ": _GS + GAP + "sự khoan khoái trong tâm",
    # ---- cha diṭṭhiyo (2-948)
    "diṭṭhi uppajjati": "quan điểm" + GAP + "khởi lên", "saccato": "như là sự thật",
    "thetato": "như là điều chắc chắn", "saccato thetato": "như là sự thật như là điều chắc chắn", "me": "tôi",
    "anattānaṃ": "cái không phải tự ngã", "sañjānāmī": "nhận biết", "vado": "cái nói", "vedeyyo": "cái cảm nhận",
    "jāto": "sinh ra", "nāhosi": "không phải trước đây không có", "nicco": "thường còn", "dhuvo": "bền vững",
    "avipariṇāmadhammo": "có bản chất không biến đổi",
    # ================================================================ sattaka (2-949 …)
    "kāmarāgānusayo": "khuynh hướng tiềm ẩn tham đắm dục lạc", "mānānusayo": "khuynh hướng tiềm ẩn kiêu mạn",
    "diṭṭhānusayo": "khuynh hướng tiềm ẩn quan điểm", "vicikicchānusayo": "khuynh hướng tiềm ẩn hoài nghi",
    "avijjānusayo": "khuynh hướng tiềm ẩn vô minh", "ānusayo": "khuynh hướng tiềm ẩn",
    "bhavarāgānusayo": "khuynh hướng tiềm ẩn tham đắm hiện hữu",
    "ahiriko": "người không biết hổ thẹn", "anottappī": "người không biết ghê sợ tội lỗi",
    # ---- satta diṭṭhiyo (2-951)
    "mahābhūtiko": "yếu tố cơ bản", "bhūtiko": "yếu tố", "pettika": "cha mẹ", "sambhavo": "sinh ra",
    "vinassati": "bị hủy diệt", "hoti paraṃ maraṇā": "tồn tại sau khi chết", "sammā samucchinno": "hoàn toàn bị đoạn diệt",
    "ettāvatā sammā": "chỉ đến chừng ấy" + GAP + "hoàn toàn",
    "ettāvatā sammā samucchinno": "chỉ đến chừng ấy" + GAP + "hoàn toàn bị đoạn diệt",
    "ucchedaṃ": "sự đoạn diệt", "vināsaṃ": "sự hủy diệt", "vibhavaṃ": "sự không còn hiện hữu",
    "dibbo": "thuộc cõi trời", "kabaḷīkāra": "thức ăn", "bhakkho": "dùng", "jānāsi": "biết",
    "manomayo": "do ý tạo thành", "sabbaṅgapaccaṅgī": "đầy đủ mọi bộ phận lớn nhỏ",
    "ahīnindriyo": "có các năng lực không khiếm khuyết", "indriyo": "năng lực",
    "āyatanūpago": "đạt đến lĩnh vực", "ākiñcaññāyatanūpago": "đạt đến lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatanūpago": "đạt đến lĩnh vực không phải tri giác cũng không phải không tri giác",
    "ākāsānañcāyatanūpago": "đạt đến lĩnh vực không gian vô tận",
    "viññāṇañcāyatanūpago": "đạt đến lĩnh vực thức vô tận", "natthi kiñcīti": "không có gì cả",
    # ================================================================ aṭṭhaka (2-953 …)
    "bhikkhunā": "vị tỳ-khưu", "kataṃ": "đã làm xong", "karontassa": "làm", "handāhaṃ": "vậy ta hãy",
    "nipajjāmī": "nằm nghỉ", "nipajjati": "nằm nghỉ", "kilamissati": "sẽ mệt mỏi", "kilanto": "mệt mỏi",
    "vīriyaṃ": "tinh tấn", "appattassa": "điều chưa đạt được",
    "appattassa pattiyā": "để đạt được điều chưa đạt được", "anadhigatassa": "điều chưa chứng đắc",
    "adhigamāya": "chứng đắc", "anadhigatassa adhigamāya": "để chứng đắc điều chưa chứng đắc",
    "asacchikatassa": "điều chưa chứng nghiệm",
    "asacchikatassa sacchikiriyāya": "để chứng nghiệm điều chưa chứng nghiệm",
    "kusītavatthu": "chỗ dựa" + GAP + "của sự lười biếng", "gāmaṃ": "làng", "nigamaṃ": "thị trấn",
    "piṇḍāya": "khất thực", "caranto": "đi", "piṇḍāya caranto": "đi khất thực", "lūkhassa": "thô",
    "paṇītassa": "ngon", "bhojanassa": "thức ăn", "yāvadatthaṃ": "như mình cần", "alatthaṃ": "đã nhận được",
    "akammañño": "không dễ vận dụng", "māsācitaṃ": "nặng nề như hạt đậu ngâm nước", "appamattako": "nhẹ",
    "ābādho": "chứng bệnh", "kappo": "lý do chính đáng", "vuṭṭhito": "khỏi bệnh", "gelaññā": "bệnh",
    "dubbalo": "yếu ớt", "tassa evaṃ hoti": "vị ấy nghĩ như vầy",
    "lābhe": "được lợi lộc", "alābhe": "mất lợi lộc", "yase": "được danh tiếng", "ayase": "mất danh tiếng",
    "pasaṃsāya": "được khen ngợi", "nindāya": "bị chê trách", "sukhe": "được hạnh phúc",
    "muta": "đã cảm nhận", "viññāta": "đã nhận biết",
    # ---- purisadosa (2-957)
    "bhikkhuṃ": "một tỳ-khưu", "āpattiyā": "lỗi vi phạm", "codenti": "buộc tội",
    "codiyamāno": "bị" + GAP + "buộc tội", "sarāmi": "nhớ", "assatiyāva": "với lý do không nhớ",
    "nibbeṭheti": "chối bỏ", "codakaṃyeva": "chính người buộc tội", "paṭippharati": "chống lại",
    "bālassa": "ngu dốt", "abyattassa": "thiếu hiểu biết", "bhaṇitena": "lời nói", "bhaṇitabbaṃ": "nói",
    "kiṃ nu kho": "có ích gì", "paccāropeti": "buộc tội ngược lại", "itthannāmaṃ": "có tên như thế này",
    "āpanno": "đã phạm", "paṭikarohī": "sửa lỗi", "aññenāññaṃ": "chuyện này sang chuyện khác",
    "paṭicarati": "lảng tránh", "apanāmeti": "đưa" + GAP + "ra ngoài", "kopañca": "sự nổi nóng",
    "dosañca": "sự sân hận", "appaccayañca": "sự bất mãn", "pātukaroti": "để lộ", "bāhā": "tay",
    "vikkhepakaṃ": "vung", "majjhe": "giữa", "bhaṇati": "nói", "anādiyitvā": "không đếm xỉa đến",
    "sāpattikova": "vẫn mang lỗi", "yenakāmaṃ": "đâu tùy ý", "pakkamati": "bỏ đi", "tuṇhībhūto": "im lặng",
    "viheseti": "làm phiền", "āyasmanto": "tôn giả", "atibāḷhaṃ": "quá", "byāvaṭā": "bận tâm",
    "sikkhaṃ": "sự tu học", "paccakkhāya": "từ bỏ", "hīnāyāvattissāmī": "quay về đời sống thấp kém",
    "āvattissāmī": "quay về", "āvattitvā": "quay về", "attamanā": "hài lòng",
    # ---- asaññī / nevasaññīnāsaññī (2-958 …)
    "arūpī": "không có hình sắc", "arogo": "không bệnh tật", "arogo paraṃ maraṇā": "không bệnh tật sau khi chết",
    "asaññīti naṃ paññapenti": "trình bày rằng nó không có tri giác",
    "saññīnāsaññī": "có tri giác cũng không phải không có tri giác",   # fragment of nevasaññīnāsaññī-
    # ================================================================ navaka (2-963 …)
    "taṇhaṃ": "khao khát", "vinicchayo": "sự phán định", "pariggaho": "sự chiếm hữu", "ādhikaraṇaṃ": "vì",
    "daṇḍādāna": "cầm gậy", "satthādāna": "cầm dao", "ādāna": "cầm", "kalaha": "cãi cọ", "viggaha": "xung đột",
    "tuvaṃtuvaṃ": "gọi nhau mày tao", "pesuñña": "nói lời đâm thọc",
    "iñjitametaṃ": "một sự dao động", "saṅkhatametaṃ": "một điều được tạo tác",
    # ================================================================ taṇhāvicarita (2-973 … 2-976)
    "asasmīti": "Tôi thường còn", "sātasmīti": "Tôi đoạn diệt", "aññathāsmīti": "Tôi khác đi",
    "anavakāriṃ": "không tách riêng", "kañci dhammaṃ anavakāriṃ": "không tách riêng bất cứ hiện tượng nào",
    "avakāriṃ": "tách riêng", "kañci dhammaṃ avakāriṃ": "tách riêng bất cứ hiện tượng nào",
    "chandaṃ paṭilabhati": "có được ý muốn", "mānaṃ paṭilabhati": "có được sự kiêu mạn",
    "diṭṭhiṃ paṭilabhati": "có được quan điểm",
    "khattiyo": "người thuộc giai cấp quý tộc", "vesso": "người thuộc giai cấp thương nhân",
    "suddo": "người thuộc giai cấp lao động", "gahaṭṭho": "người tại gia", "pabbajito": "người xuất gia",
    "devo": "vị trời", "manusso": "con người", "parapuggalaṃ": "người khác", "upanidhāya": "so với",
    "niccosmi": "tôi thường còn", "dhuvosmi": "tôi bền vững", "sassatosmi": "tôi trường tồn",
    "avipariṇāmadhammosmīti": "tôi có bản chất không biến đổi", "vinassissāmi": "tôi sẽ bị hủy diệt",
    "ucchijjissāmi": "tôi sẽ bị đoạn diệt",
    # ---- 2-977
    "ekaccasassatikā": "trường tồn một phần", "antānantikā": "về hữu hạn và vô hạn", "ānantikā": "vô hạn",
    "amarā": "như lươn", "vikkhepikā": "lẩn tránh", "adhicca": "ngẫu nhiên", "samuppannikā": "sinh khởi",
    "soḷasa": "mười sáu",
    # ================================================================ the 2-U segments (tika … dasaka bodies)
    "aṅgaṇaṃ": "vết nhơ", "malaṃ": "sự dơ bẩn",
    "viheṭheti": "quấy hại", "satte": "chúng sinh", "pāṇinā": "tay", "leḍḍunā": "cục đất", "daṇḍena": "gậy",
    "satthena": "vũ khí", "rajjuyā": "dây thừng", "heṭhanā": "sự quấy hại", "viheṭhanā": "sự quấy hại nặng nề",
    "hiṃsanā": "sự làm hại", "vihiṃsanā": "sự hãm hại", "rosanā": "sự làm khổ", "virosanā": "sự làm khổ nặng nề",
    "parūpaghāto": "sự gây hại cho người khác", "ūpaghāto": "sự gây hại",
    "visamacariyā": "lệch lạc", "paṭisevanā": "sự lui tới",
    "asavanakamyatā": "sự không muốn lắng nghe", "anuggahetukamyatā": "sự không muốn học hỏi",
    "adhāretukamyatā": "sự không muốn ghi nhớ",
    "upārambho": "sự bắt lỗi", "anupārambho": "sự bắt lỗi liên tục", "upārambhanā": "hành động bắt lỗi",
    "anupārambhanā": "hành động bắt lỗi liên tục", "anupārambhitattaṃ": "trạng thái bắt lỗi liên tục",
    "uññā": "sự coi thường", "avaññā": "sự xem nhẹ", "paribhavo": "sự khinh miệt", "randha": "kẽ hở",
    "visamaṃ": "sự lệch lạc", "taṃsampavaṅkatā": "sự nghiêng về phía",
    "attavādupādānañca": "sự bám víu vào học thuyết về tự ngã",
    "āgatiṃ": "con đường sai trái", "chandāgatiṃ": "con đường sai trái vì ưa thích",
    "dosāgatiṃ": "con đường sai trái vì sân hận", "mohāgatiṃ": "con đường sai trái vì si mê",
    "bhayāgatiṃ": "con đường sai trái vì sợ hãi", "agatigamanaṃ": "sự đi theo con đường sai trái",
    "vagga": "phe phái", "vāri": "nước",
    "vipariyāso": "sự đảo ngược", "saññāvipariyāso": "sự đảo ngược của tri giác",
    "cittavipariyāso": "sự đảo ngược của tâm", "diṭṭhivipariyāso": "sự đảo ngược của quan điểm",
    "amutavāditā": "việc nói là chưa cảm nhận", "aviññātavāditā": "việc nói là chưa nhận biết",
    "cora": "trộm cướp", "ūmi": "sóng", "kumbhīla": "cá sấu", "āvaṭṭa": "xoáy nước", "susukā": "cá dữ",
    "attānuvāda": "sự tự trách", "ānuvāda": "chỉ trích",
    "parānuvādabhayaṃ": "nỗi sợ hãi về sự bị người khác chỉ trích", "daṇḍa": "hình phạt", "duggati": "cõi xấu",
    "sayaṅkataṃ": "do chính mình tạo ra", "sukhadukkha": "sự dễ chịu và sự khó chịu", "samuppannaṃ": "sinh khởi",
    "rāgaggi": "ngọn lửa tham đắm", "dosaggi": "ngọn lửa sân hận", "mohaggi": "ngọn lửa si mê",
    "dosa": "sân hận", "moha": "si mê",
    "kāme": "dục lạc", "avītarāgo": "chưa lìa tham đắm", "avigatacchando": "chưa lìa ý muốn",
    "avigatapemo": "chưa lìa sự yêu thích", "avigatapipāso": "chưa lìa sự khát khao",
    "avigatapariḷāho": "chưa lìa sự nóng bỏng", "avigatataṇho": "chưa lìa khao khát",
    "udarāvadehakaṃ": "no căng bụng", "bhuñjitvā": "sau khi ăn", "seyyasukhaṃ": "thú vui nằm",
    "passasukhaṃ": "thú vui trở mình", "middhasukhaṃ": "thú vui ngủ", "nikāyaṃ": "cõi",
    "paṇidhāya": "với ước nguyện", "brahmacariyaṃ": "đời tu hành trong sạch", "tapena": "khổ hạnh",
    "thinamiddha": "uể oải và đờ đẫn", "uddhaccakukkucca": "xao động và hối tiếc",
    "voropitā": "bị tước đoạt", "voropito": "bị tước đoạt", "duṭṭhena": "độc ác",
    "uppāditaṃ": "bị làm cho chảy", "saṅgho": "Tăng đoàn",
    "abhivadanti": "tuyên bố", "paññāpenti": "trình bày", "diṭṭhadhammanibbānaṃ": _NDT,
    "janassa": "người", "appiyo": "không được" + GAP + "yêu quý", "vera": "thù địch", "sammūḷho": "trong mê muội",
    "kālaṅkaroti": "chết", "upapajjati": "tái sinh",
    "ājīvaka": "sinh kế", "asiloka": "tiếng xấu", "parisa": "hội chúng", "sārajja": "rụt rè",
    "amanāpiyesu": "không đáng ưa thích", "saṃsaggārāmatā": "sự ưa thích giao du",
    "papañcārāmatā": "sự ưa thích suy diễn lan man", "upavicarati": "lưu tâm đến",
    "upekkhāṭṭhāniyaṃ": "làm khởi lên sự bình thản", "upekkhāṭṭhāniyesu": "làm khởi lên sự bình thản",
    "somanassaṭṭhāniyaṃ": "làm khởi lên niềm vui", "domanassaṭṭhāniyaṃ": "làm khởi lên nỗi buồn",
    "gehasitaṃ cetasikaṃ asātaṃ": _GS + GAP + "sự bứt rứt trong tâm",
    "gehasitaṃ cetasikaṃ": _GS + GAP + "trạng thái trong tâm",
    # ---- full items here (pi-1 had them only as fragments of negated words)
    "nāsaññī": "không phải không có tri giác", "bhayaṃ": "nỗi sợ hãi", "byādhi": "bệnh tật",
    "davāya": "để vui đùa", "madāya": "để say sưa", "maṇḍanāya": "để trang điểm", "vibhūsanāya": "để làm đẹp",
    "saṃvarāya": "để thu thúc", "sammusanatā": "sự quên lãng", "pilāpanatā": "sự hời hợt",
    "jimhatā": "sự quanh co", "vaṅkatā": "sự cong queo", "kuṭilatā": "sự vặn vẹo", "kakkhaḷatā": "sự thô cứng",
    "puthujjano": "người phàm phu",
}

PRIO = {   # same Pāli, the segment's own Vietnamese (first candidate present in the segment)
    "jāti": ["xuất thân", "sự sinh"], "jīvita": ["sự sống", "mạng sống"],
    "vaṇṇa": ["sắc đẹp", "vẻ đẹp", "lời khen"], "bhoga": ["của cải", "tài sản"],
    "icchatā": ["tham muốn", "ước muốn"], "ādi": ["những điều tương tự", "khởi đầu"],
    "vibhava": ["sự không hiện hữu", "sự không còn hiện hữu", "không còn hiện hữu"],
    "vibhavadiṭṭhi": ["quan điểm về sự không hiện hữu", "quan điểm về sự không còn hiện hữu"],
    "āyatanāni": ["lĩnh vực", "lĩnh vực nhận biết"], "uppādā": ["nguyên nhân khởi lên", "loại"],
    "ānantarikāni": ["trổ quả ngay kiếp kế tiếp", "có quả không gián đoạn"], "vādā": ["học thuyết", "nói"],
    "paṭighāto": ["sự va chạm", "sự phẫn uất"], "purisa": ["con người", "nam tính"],
    "upādāya": ["dựa vào", "tùy thuộc vào"],
    "jātiṃ": ["xuất thân", "sự sinh", "đời"], "cīvara": ["y phục", "y"], "jātiyā": ["xuất thân", "sự sinh"],
    "mucchā": ["sự lịm người", "sự mê đắm"], "pariḷāho": ["sự nóng nực", "sự nóng bỏng"],
    "icchā": ["sự mong muốn", "ước muốn"], "nimittaṃ": ["sự ra dấu", "dấu hiệu"],
    "obhāso": ["sự gợi ý", "hào quang"], "hīno": ["kém", "thấp kém"],
    "viharati": ["sống", "an trú"], "yaṃ": ["điều", "mà"],
    "samāpattiyā": ["sự chứng đạt", "để" + GAP + "xảy ra nơi mình"], "duppaññā": ["kém trí tuệ", "trí tuệ kém"],
    "cakkhunā": ["nhãn", "mắt"], "rūpaṃ": ["vật chất", "hình sắc"], "āpajjati": ["dấn thân vào", "thực hiện"],
    "akusalā dhammā": ["hiện tượng bất thiện", "hiện tượng" + GAP + "bất thiện"],
    "ayoniso": ["không khôn ngoan", "không đúng cách"],
    "rūpataṇhā": ["khao khát cõi hình sắc", "khao khát hình sắc"], "māyā": ["sự xảo trá", "sự huyễn hoặc"],
    "paṭicca": ["dựa vào", "tùy thuộc vào điều kiện"], "carati": ["đang gây", "đang làm", "sống", "đi lại"],
    "dukkha": ["khổ đau", "khó khăn", "sự khó chịu"],
    "vihiṃsā": ["sự hãm hại", "hãm hại", "sự bức bách"], "kāmadhātu": ["yếu tố dục lạc", "cõi dục lạc"],
    "dhātu": ["yếu tố", "cõi"], "bahiddhā": ["ở bên ngoài bản thân", "bên ngoài", "ngoài"],
    "kāyakammaṃ": ["nghiệp bằng thân", "nghiệp" + GAP + "bằng thân"],
    "vacīkammaṃ": ["nghiệp bằng lời nói", "nghiệp" + GAP + "bằng lời nói"],
    "manokammaṃ": ["nghiệp bằng ý", "nghiệp" + GAP + "bằng ý"],
    "thambhitattaṃ": ["trạng thái khởi cứng đầu", "trạng thái cứng đờ"],
    "jātiṃ paṭicca": ["dựa vào xuất thân", "dựa vào sự sinh"],
    "sukhaṃ": ["hạnh phúc", "dễ chịu", "thú vui"], "gacchati": ["đi theo", "được"], "aggi": ["ngọn lửa", "lửa"],
    "anuyutto": ["chuyên tâm", "chuyên chú"], "rūpe": ["vật chất", "hình sắc"],
    "uddhacca": ["sự xao động", "xao động"], "amanāpo": ["không đáng ưa thích", "không được ưa thích"],
    "kasāvo": ["chất cặn bẩn", "vị chát"], "labhati": ["nhận được", "đạt được"],
    "vajja": ["lỗi lầm", "đáng chê trách"], "nimitta": ["dấu hiệu tổng quát", "dấu hiệu"], "dukkhaṃ": ["khổ đau", "khó chịu"], "doso": ["sự sân hận", "lỗi"],
    "dhammaṃ": ["hiện tượng", "Giáo Pháp"], "sato": ["với sự tỉnh thức", "đang hiện hữu"],
    "kāmā": ["dục lạc", "mong"], "oḷārikaṃ": ["ở dạng thô", "thô"],
    "uppajjati": ["sinh khởi", "khởi lên"], "pāpakānaṃ": ["xấu ác", "xấu"], "bhavissati": ["sẽ tồn tại", "về sau sẽ"],
    "sammā": ["đúng đắn", "hoàn toàn"], "pattiyā": ["đạt đến", "đạt được"],
    "sacchikiriyāya": ["tự mình chứng nghiệm", "chứng nghiệm"], "vatthu": ["chủ đề", "chỗ dựa"],
    "maggo": ["con đường", "đường"], "pāripūriṃ": ["sự hoàn hảo", "đầy đủ"],
    "uppanno": ["đã sinh khởi", "đã phát sinh", "phát sinh"], "suta": ["sự học hỏi", "sự lắng nghe", "đã nghe"],
    "sati": ["sự tỉnh thức", "tỉnh thức", "khi có"], "paṭilabhati": ["đạt được", "có được"],
    "sassata": ["sự trường tồn", "trường tồn"], "visama": ["bất chính", "lệch lạc"],
    "sampavaṅkatā": ["sự nghiêng theo", "sự nghiêng về phía"], "sevanā": ["sự giao du", "sự đi theo"],
    "nisevanā": ["sự thường xuyên giao du", "sự thường xuyên đi theo"],
    "saṃsevanā": ["sự giao du mật thiết", "sự đi theo mật thiết"],
    "aññataraññatarena": ["điều này hay điều khác", "thứ này hay thứ khác"], "uccheda": ["sự đoạn diệt", "đoạn diệt"], "chandarāgo": ["ý muốn và sự tham đắm", "sự tham đắm do ý muốn"],
    "ārakkho": ["sự che chở", "sự canh giữ"], "vivāda": ["tranh cãi", "tranh chấp"],
    "musāvādā": ["việc nói dối", "nói dối"], "rāga": ["sự tham đắm", "tham đắm"], "paṭigha": ["sự va chạm", "ác cảm"],
    "māna": ["sự kiêu mạn", "kiêu mạn"], "vicikicchā": ["sự hoài nghi", "hoài nghi"],
    "issā": ["sự ganh tị", "ganh tị"], "parāmāsa": ["sự hiểu sai lệch", "hiểu sai lệch"], "bhikkhu": ["vị tỳ-khưu", "tỳ-khưu"], "nāma": ["phần tinh thần", "mà"], "diṭṭhigata": ["sự mắc kẹt trong các quan điểm", "quan điểm"],
    "ṭhapanā": ["sự bày đặt", "sự giữ lại"], "saṇṭhapanā": ["sự dàn dựng", "sự giữ chặt"],
    "dhamma": ["hiện tượng", "Giáo Pháp"], "kiriyā": ["mang tính chức năng", "việc làm"],
    "ggāho": ["sự nắm giữ điều đảo ngược", "sự dốc sức"], "gataṃ": ["sự mắc kẹt trong", "điều được xem là"],
    "sampaggāho": ["sự dốc sức", "sự tự đề cao"], "thambhanā": ["sự khởi cứng đầu", "sự căng cứng"],
}

OVERRIDES = {
    "2-905": {"dhammaṃ": "đối tượng của ý"},          # «khi nhận biết đối tượng của ý bằng ý» (manasā dhammaṃ viññāya)
    "2-909": {"dhamma": "đối tượng của ý"},           # dhammataṇhā «khao khát đối tượng của ý» (pi-1 stem convention)
    "2-947": {"dhammesu": "đối tượng của ý"},         # manāpiyesu dhammesu «các đối tượng của ý đáng ưa thích»
    "2-919": {"hoti": "còn tồn tại"},                 # «Như Lai không phải còn tồn tại …» (as ch16 ^2-815)
    "2-972": {"hoti": "còn tồn tại"},
    "2-U34": {"hoti": "còn tồn tại"},
    "2-943": {"dukkhā": "khổ đau"},                   # kāmā … aniccā dukkhā «là vô thường, là khổ đau»
    "2-U24": {"dhammaṃ": "đối tượng của ý"},          # as ^2-905
    "2-U60": {"dhammesu": "đối tượng của ý"},         # manāpiyesu dhammesu (dhammā = «những hiện tượng» there)
    "2-U53": {"deva": "chư thiên"},                   # devanikāyaṃ «một cõi chư thiên»
    "2-U48": {"uppajjati": "khởi lên"},               # diṭṭhi uppajjati «quan điểm … khởi lên»
    "2-957": {"doso": "lỗi"},                         # purisadoso «lỗi … của con người» (dosañca = sự sân hận)
}


def prio(cands, text):
    for c in cands:
        if present(c, text):
            return c
    return cands[0]


def context17(bid, kw, k, s, text, kws):
    if k == "māno" and "sự kiêu mạn" not in lc(text):
        if "atimāno" in s:
            return "sự ngạo mạn"              # «Sự ngạo mạn»: the Vietnamese fuses ati + māna
        if "omāno" in s:
            return "sự tự ti"                 # the omāna string (o + māna fused)
    if k == "ānudiṭṭhi":                       # attānudiṭṭhi «quan điểm xem có tự ngã» / pubbantānudiṭṭhi «quan điểm về»
        return "quan điểm xem" if "attānudiṭṭhi" in s else "quan điểm về"
    if k == "mānā":                            # navavidhā mānā «chín loại kiêu mạn» / sattamānā «bảy loại kiêu mạn»
        return "kiêu mạn" if "navavidhā" in s else "loại kiêu mạn"
    if (k in ("dhamma", "dhammaṃ", "dhammesu", "dhammā") and "hiện tượng" not in lc(text)
            and "đối tượng của ý" in text):
        return "đối tượng của ý"              # stem / object of mind (pi-1 convention); no «hiện tượng» in the segment
    if k == "jappā":                           # sāmantajappā «lời nói bóng gió» / lobha list «sự thèm thuồng»
        return "lời nói" if "sāmantajappā" in s else "sự thèm thuồng"
    if k in PRIO:
        return prio(PRIO[k], text)
    return None


def resolver_for(part):
    vi = read_vietnamese(part)
    table = {**T45, **T79, **T1012, **T1315, **T16, **T17}

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context17(bid, kw, k, s, text, kws)
        if v is not None:
            return v
        if k in T17:
            return T17[k]
        v = context16(bid, kw, k, s, text, kws, table)
        if v is not None:
            return v
        if k in T16:
            return T16[k]
        v = context1315(bid, kw, k, s, text, kws)
        if v is not None:
            return v
        return value(kw, kws, table, text)
    return resolve


_CTX = {"māno", "ānudiṭṭhi", "mānā", "dhamma", "dhammaṃ", "dhammesu", "dhammā", "jappā"}


def dump(part, only_miss=False, only_fallback=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            if only_fallback and (lc(kw) in T17 or lc(kw) in PRIO or lc(kw) in _CTX
                                  or kw in OVERRIDES.get(bid, {})):
                continue
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
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(part, lo=0, hi=10 ** 6, all_kw=False, pali=False):
    """Segments lo..hi (line index in the keyword file) that have misses: Vietnamese + keyword=value (!! = miss)."""
    res = resolver_for(part)
    vi = read_vietnamese(part)
    pi = read_pali(part) if pali else {}
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if not lo <= i < hi:
            continue
        text = vi.get(bid, "")
        out, nm = [], 0
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            m = v == "???" or (v != NDE and not present(v, text))
            nm += m
            if m or all_kw:
                out.append(("!!" if m else "") + f"{kw}={v}")
        if nm or all_kw:
            if pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"== {i} [{bid}] {text}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), "all" in sys.argv[5:], "pali" in sys.argv[5:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"], sys.argv[3:4] == ["fallback"])
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
