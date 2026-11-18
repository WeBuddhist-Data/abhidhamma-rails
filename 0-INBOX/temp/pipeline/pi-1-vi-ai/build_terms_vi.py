"""Write vi-zeroshot-terms.md and vi-core-terms.md from the two Vietnamese builders
(pi-1 Dhammasaṅgaṇī, plain zero-shot).

usage: python -I -X utf8 build_terms_vi.py
Every heading of AI_translation/pali/pi-1_split_chapters/*.md must have a Vietnamese form in HEADINGS
(the script stops otherwise), so the later chapter agents share one set of headings.
It also checks that the written preamble.md uses the fixed preamble strings below.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402
import build_ch2_01_sample_vi as C  # noqa: E402

ROOT = HERE.parents[3]
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters"
OUT = HERE / "vi-zeroshot-terms.md"
OUT_CORE = HERE / "vi-core-terms.md"

NAMO = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"
BOOK_TITLE = "Liệt kê các hiện tượng"
FRONTMATTER_TITLE = f"{BOOK_TITLE} - tiếng Việt phổ thông"

VAR_ARUPA = M.V("s", "Sī., Syā.", "arūpajjhānāni")
SIXTEEN = "phân tích theo mười sáu cách"

# Pāli heading text (without #) = Vietnamese heading text. Level is kept from the Pāli line.
HEADINGS = {
    # preamble
    "Abhidhammapiṭake": "Trong Tạng Vi Diệu Pháp",
    "Dhammasaṅgaṇīpāḷi": BOOK_TITLE,
    # chapter 1 (as built)
    "Mātikā": M.H_MATIKA.lstrip("# "),
    "Tikamātikā": M.H_TIKA.lstrip("# "),
    "Dukamātikā": M.H_DUKA.lstrip("# "),
    # chapter 2
    "Cittuppādakaṇḍaṃ": C.H_CH2.lstrip("# "),
    "Kāmāvacarakusalaṃ": C.H_KAMA_KUSALA.lstrip("# "),
    "Padabhājanī": C.H_PADA.lstrip("# "),
    "Koṭṭhāsavāro": "Mục về các thành phần",
    "Suññatavāro": "Mục về sự trống rỗng",
    "Rūpāvacarakusalaṃ": "Tâm thiện thuộc cõi hình sắc",
    "Catukkanayo": "Phương pháp chia bốn",
    "Pañcakanayo": "Phương pháp chia năm",
    "Catasso paṭipadā": "Bốn cách thực hành",
    "Cattāri ārammaṇāni": "Bốn loại đối tượng",
    "Dve ārammaṇāni": "Hai loại đối tượng",
    "Soḷasakkhattukaṃ": "Phân tích theo mười sáu cách",
    "Aṭṭhakkhattukaṃ": "Phân tích theo tám cách",
    "Idampi aṭṭhakkhattukaṃ": "Đây cũng là phân tích theo tám cách",
    "Aparampi aṭṭhakkhattukaṃ": "Thêm một phân tích theo tám cách",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": f"Tám đề mục bao trùm, {SIXTEEN}",
    "Abhibhāyatanāni parittāni": "Các lĩnh vực chế ngự hạn hẹp",
    "Appamāṇāni": "Loại không thể đo lường",
    "Tīṇi vimokkhāni soḷasakkhattukāni": f"Ba sự giải thoát, {SIXTEEN}",
    "Cattāri brahmavihārajhānāni soḷasakkhattukāni":
        f"Bốn tầng thiền của các nơi an trú cao thượng, {SIXTEEN}",
    "Asubhajhānaṃ soḷasakkhattukaṃ": f"Tầng thiền về sự không đẹp đẽ, {SIXTEEN}",
    "Arūpāvacarakusalaṃ": "Tâm thiện thuộc cõi không hình sắc",
    "Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "Bốn tầng thiền không hình sắc" + VAR_ARUPA + f", {SIXTEEN}",
    "Tebhūmakakusalaṃ": "Tâm thiện thuộc ba cõi",
    "Lokuttarakusalaṃ": "Tâm thiện vượt thế gian",
    "Suddhikapaṭipadā": "Cách thực hành đơn thuần",
    "Suññataṃ": "Sự trống rỗng",
    "Suññatamūlakapaṭipadā": "Cách thực hành dựa trên sự trống rỗng",
    "Appaṇihitaṃ": "Sự không mong cầu",
    "Appaṇihitamūlakapaṭipadā": "Cách thực hành dựa trên sự không mong cầu",
    "Vīsati mahānayā": "Hai mươi phương pháp lớn",
    "Adhipati": "Yếu tố chủ đạo",
    "Dvādasa akusalāni": "Mười hai loại tâm bất thiện",
    "Abyākatavipāko": "Quả của nghiệp, không xác định về mặt đạo đức",
    "Kusalavipākapañcaviññāṇāni": "Năm loại thức là quả của nghiệp thiện",
    "Kusalavipākamanodhātu": "Yếu tố ý là quả của nghiệp thiện",
    "Kusalavipākamanoviññāṇadhātusomanassasahagatā":
        "Yếu tố ý thức là quả của nghiệp thiện, có niềm vui đi kèm",
    "Kusalavipākamanoviññāṇadhātuupekkhāsahagatā":
        "Yếu tố ý thức là quả của nghiệp thiện, có sự bình thản đi kèm",
    "Aṭṭhamahāvipākā": "Tám quả nghiệp lớn",
    "Rūpāvacaravipākā": "Các quả nghiệp thuộc cõi hình sắc",
    "Arūpāvacaravipākā": "Các quả nghiệp thuộc cõi không hình sắc",
    "Lokuttaravipāka-paṭhamamaggavipākā": "Các quả vượt thế gian: quả của con đường thứ nhất",
    "Suddhikasuññataṃ": "Sự trống rỗng đơn thuần",
    "Suññatapaṭipadā": "Cách thực hành với sự trống rỗng",
    "Suddhikaappaṇihitaṃ": "Sự không mong cầu đơn thuần",
    "Appaṇihitapaṭipadā": "Cách thực hành với sự không mong cầu",
    "Chandādhipateyyasuddhikapaṭipadā": "Cách thực hành đơn thuần với ý muốn làm yếu tố chủ đạo",
    "Chandādhipateyyasuddhikasuññatā": "Sự trống rỗng đơn thuần với ý muốn làm yếu tố chủ đạo",
    "Dutiyādimaggavipāko": "Quả của con đường thứ hai và các con đường tiếp theo",
    "Akusalavipākaabyākataṃ": "Loại không xác định về mặt đạo đức là quả của nghiệp bất thiện",
    "Akusalavipākapañcaviññāṇāni": "Năm loại thức là quả của nghiệp bất thiện",
    "Akusalavipākamanodhātu": "Yếu tố ý là quả của nghiệp bất thiện",
    "Akusalavipākamanoviññāṇadhātu": "Yếu tố ý thức là quả của nghiệp bất thiện",
    "Ahetukakiriyāabyākataṃ": "Loại không xác định về mặt đạo đức, mang tính chức năng, không có gốc rễ",
    "Kiriyāmanodhātu": "Yếu tố ý mang tính chức năng",
    "Kiriyāmanoviññāṇadhātusomanassasahagatā": "Yếu tố ý thức mang tính chức năng, có niềm vui đi kèm",
    "Kiriyāmanoviññāṇadhātuupekkhāsahagatā": "Yếu tố ý thức mang tính chức năng, có sự bình thản đi kèm",
    "Sahetukakāmāvacarakiriyā": "Tâm chức năng có gốc rễ thuộc cõi dục lạc",
    "Rūpāvacarakiriyā": "Tâm chức năng thuộc cõi hình sắc",
    "Arūpāvacarakiriyā": "Tâm chức năng thuộc cõi không hình sắc",
    # chapter 3
    "Rūpakaṇḍaṃ": "Phần về vật chất",
    "Uddeso": "Phần nêu đề mục",
    "Ekakaṃ": "Phân loại theo nhóm một",
    "Dukaṃ": "Phân loại theo nhóm hai",
    "Tikaṃ": "Phân loại theo nhóm ba",
    "Catukkaṃ": "Phân loại theo nhóm bốn",
    "Pañcakaṃ": "Phân loại theo nhóm năm",
    "Chakkaṃ": "Phân loại theo nhóm sáu",
    "Sattakaṃ": "Phân loại theo nhóm bảy",
    "Aṭṭhakaṃ": "Phân loại theo nhóm tám",
    "Navakaṃ": "Phân loại theo nhóm chín",
    "Dasakaṃ": "Phân loại theo nhóm mười",
    "Ekādasakaṃ": "Phân loại theo nhóm mười một",
    "Rūpavibhatti": "Phân tích vật chất",
    "Ekakaniddeso": "Giải thích phân loại theo nhóm một",
    "Dukaniddeso": "Giải thích phân loại theo nhóm hai",
    "Tikaniddeso": "Giải thích phân loại theo nhóm ba",
    "Upādābhājanīyaṃ": "Phân tích vật chất phái sinh",
    # chapter 4
    "Nikkhepakaṇḍaṃ": "Phần tóm lược",
    "Tikanikkhepaṃ": "Tóm lược các bộ ba",
    "Dukanikkhepaṃ": "Tóm lược các bộ đôi",
    "Suttantikadukanikkhepaṃ": "Tóm lược các bộ đôi theo kinh",
    # chapter 5
    "Aṭṭhakathākaṇḍaṃ": "Phần giải thích",
    "Tikaatthuddhāro": "Giải thích ý nghĩa các bộ ba",
    "Dukaatthuddhāro": "Giải thích ý nghĩa các bộ đôi",
}
GROUP_PALI = {
    "1-M-2-1-0": "Hetugocchakaṃ", "1-M-2-2-0": "Cūḷantaradukaṃ", "1-M-2-3-0": "Āsavagocchakaṃ",
    "1-M-2-4-0": "Saṃyojanagocchakaṃ", "1-M-2-5-0": "Ganthagocchakaṃ", "1-M-2-6-0": "Oghagocchakaṃ",
    "1-M-2-7-0": "Yogagocchakaṃ", "1-M-2-8-0": "Nīvaraṇagocchakaṃ", "1-M-2-9-0": "Parāmāsagocchakaṃ",
    "1-M-2-10-0": "Mahantaradukaṃ", "1-M-2-11-0": "Upādānagocchakaṃ", "1-M-2-12-0": "Kilesagocchakaṃ",
    "1-M-2-13-0": "Piṭṭhidukaṃ", "1-M-2-14-0": "Suttantikadukamātikā",
}
for gid, pali in GROUP_PALI.items():
    HEADINGS[pali] = M.GROUPS[gid][0].lstrip("# ")

CLOSINGS = [  # closing lines (not headings) that later chapters will meet
    ("Tikamātikā.", M.END_TIKA),
    ("Abhidhammadukamātikā.", M.END_ABHI_DUKA),
    ("Mātikā niṭṭhitā.", M.END_MATIKA),
] + [(GROUP_PALI[g] + ".", M.GROUPS[g][1]) for g in GROUP_PALI] + [
    ("Padabhājanīyaṃ.", C.END_PADA),
    ("Paṭhamabhāṇavāro.", C.END_BHANA1),
    ("Dutiyabhāṇavāro. (proposed)", "Phần tụng đọc thứ hai."),
    ("<X>kaṇḍaṃ niṭṭhitaṃ. (proposed)",
     "<phần> đã hoàn tất. e.g. Cittuppādakaṇḍaṃ niṭṭhitaṃ. = Phần về sự sinh khởi của tâm đã hoàn tất."),
    ("Nikkhepakaṇḍe dutiyabhāṇavāro. (proposed)", "Phần tụng đọc thứ hai của phần tóm lược."),
    ("Atthuddhāro niṭṭhito. (proposed)", "Phần giải thích ý nghĩa đã hoàn tất."),
    ("Abhidhammadukaṃ. (proposed)", "Các bộ đôi theo Vi Diệu Pháp."),
]

# ---- core terms (cross-book): Pāli = Vietnamese | reason --------------------------------
CORE = [
    ("dhamma (phenomenon)", "hiện tượng",
     "everyday word for 'phenomenon'; «pháp» in this sense is Buddhist jargon a lay reader reads as 'law/method'"),
    ("dhamma (the Teaching)", "Giáo Pháp",
     "established Buddhist word that is also everyday Vietnamese; capitalised, never used for 'phenomenon'"),
    ("khandha", "khối (khối cảm giác, khối tri giác, khối tạo tác, khối thức)",
     "a heap or mass, plain image of 'aggregate'; «uẩn» is specialist Hán-Việt"),
    ("āyatana", "lĩnh vực nhận biết (in compounds: lĩnh vực X, e.g. lĩnh vực ý)",
     "'sphere' of cognition in plain words; «xứ» is specialist"),
    ("dhātu", "yếu tố (manodhātu = yếu tố ý; manoviññāṇadhātu = yếu tố ý thức)",
     "everyday word for 'element/factor'; «giới» would be read as 'world/boundary'"),
    ("sacca", "sự thật (ariyasacca = sự thật cao quý)", "everyday word; «đế» is specialist"),
    ("indriya", "năng lực (saddhindriya = năng lực niềm tin; jīvitindriya = năng lực sống); "
                "the sense organs in «indriyesu guttadvāratā» = giác quan",
     "'faculty' as a capacity; «căn/quyền» are specialist"),
    ("rūpa (matter)", "vật chất (rūpino = thuộc vật chất; arūpino = phi vật chất)",
     "everyday word; keeps the matrix pairs and «hiện tượng phi vật chất» transparent"),
    ("rūpa (visible object)", "hình sắc (rūpāvacara = thuộc cõi hình sắc)",
     "everyday literary word for visible form and colour; shares «sắc» with the established «cõi sắc»"),
    ("citta", "tâm", "everyday Sino-Vietnamese word for 'mind', named in the style file"),
    ("cetasika", "yếu tố đồng hành với tâm (adj. đồng hành với tâm; «cetasikaṃ sātaṃ» = sự khoan khoái trong tâm)",
     "'accompanying the mind' in plain words; «tâm sở» is specialist"),
    ("viññāṇa", "thức (manoviññāṇa = ý thức; viññāṇakkhandha = khối thức)",
     "short everyday element of «ý thức», «nhận thức»; «ý thức» is literally mano + viññāṇa, so it is used for manoviññāṇa"),
    ("vedanā", "cảm giác (sukhā / dukkhā vedanā = cảm giác dễ chịu / khó chịu)",
     "everyday word for 'feeling'; «thọ» is specialist"),
    ("saññā", "tri giác", "common word for 'perception'; «tưởng» means 'imagine' in everyday Vietnamese"),
    ("cetanā", "chủ ý", "everyday word for 'intention' (cố ý, chủ ý); kept apart from saṅkappa = tư duy"),
    ("phassa", "sự tiếp xúc", "everyday word; «xúc» is specialist"),
    ("manasikāra", "sự chú tâm", "everyday word for 'attention'; «tác ý» is specialist"),
    ("saddhā", "niềm tin", "everyday word"),
    ("vīriya", "tinh tấn (sự tinh tấn)",
     "established Buddhist word also used in everyday speech for diligent effort; kept apart from vāyāma / padhāna = nỗ lực"),
    ("sati", "sự tỉnh thức (satindriya = năng lực tỉnh thức; sammāsati = tỉnh thức đúng đắn; micchāsati = tỉnh thức sai lầm)",
     "user decision 2026-11-17: plain everyday word («sống tỉnh thức»); «chánh» already means 'right', "
     "so «chánh niệm» would double it in sammāsati and contradict micchāsati"),
    ("samādhi", "định tâm (sammāsamādhi = định tâm đúng đắn)",
     "everyday «định tâm» = to settle and collect the mind; leaves «thiền» for jhāna"),
    ("paññā", "trí tuệ", "everyday Sino-Vietnamese word, named in the style file"),
    ("jhāna", "tầng thiền (paṭhamajjhāna = tầng thiền thứ nhất)",
     "«thiền» is everyday Vietnamese for meditation; «tầng» shows these are levels of absorption"),
    ("vitakka", "sự hướng tâm", "'directing the mind' to the object; «tầm» is specialist"),
    ("vicāra", "sự duy trì tâm", "'keeping the mind' on the object; pairs with vitakka; «tứ» is specialist"),
    ("pīti", "sự hân hoan", "everyday word for rapture/elation; «hỷ» is specialist"),
    ("sukha", "hạnh phúc (factor, triad 7); dễ chịu (quality of feeling, triad 2); sāta = khoan khoái",
     "everyday words; split as in the approved English and Russian"),
    ("upekkhā", "sự bình thản", "everyday word for equanimity; «xả» means 'to let go/discharge'"),
    ("kusala / akusala / abyākata", "thiện / bất thiện / không xác định về mặt đạo đức",
     "«thiện» is everyday for 'good'; abyākata = 'ethically indeterminate' per the binding lesson, never 'trung tính'"),
    ("hetu", "gốc rễ (kusalamūla = gốc rễ thiện)", "plain word for 'root'; «nhân/căn» are specialist"),
    ("āsava", "ô nhiễm", "everyday word for what taints the mind; «lậu hoặc» is specialist"),
    ("saṃyojana", "xiềng xích", "plain image of 'fetter'; «kiết sử» is specialist"),
    ("gantha", "nút thắt", "plain image of 'tie/knot'"),
    ("ogha", "dòng lũ", "plain image of 'flood'; «bộc lưu» is specialist"),
    ("yoga", "ách", "everyday word for 'yoke'"),
    ("nīvaraṇa", "chướng ngại", "everyday word for 'hindrance'; «triền cái» is specialist"),
    ("parāmāsa", "sự hiểu sai lệch (parāmaṭṭha = bị sự hiểu sai lệch nắm giữ)",
     "plain 'misapprehension'; «kiến chấp/khinh thủ» are specialist"),
    ("upādāna", "sự bám víu (upādāniya = là đối tượng của sự bám víu)",
     "everyday word for 'clinging'; «thủ» is specialist"),
    ("kilesa", "phiền não (saṃkiliṭṭha = bị phiền não làm vẩn đục)",
     "established Buddhist word that is everyday Vietnamese for mental affliction"),
    ("lobha", "tham lam (alobha = sự không tham lam)", "everyday word"),
    ("dosa", "sân hận (adosa = sự không sân hận)", "established Buddhist word that is everyday Vietnamese for hatred/anger"),
    ("moha", "si mê (amoha = sự không si mê)", "everyday word for delusion"),
    ("avijjā", "vô minh (vijjā = hiểu biết chân thật)",
     "established Buddhist word, common in everyday speech; vijjā is kept apart from ñāṇa = hiểu biết"),
    ("taṇhā", "khao khát (bhavataṇhā = khao khát được hiện hữu)", "everyday word for craving; «ái» is specialist"),
    ("diṭṭhi", "quan điểm (sammādiṭṭhi = quan điểm đúng đắn)", "everyday word for 'view'; «kiến» is specialist"),
    ("māna", "sự kiêu mạn", "everyday word for conceit"),
    ("hiri / ottappa", "sự biết hổ thẹn / sự biết ghê sợ tội lỗi (ahirika / anottappa = sự không biết …)",
     "plain descriptions of moral shame and moral dread; «tàm/quý» are specialist"),
    ("lokiya / lokuttara", "thuộc thế gian / vượt thế gian", "plain words; «siêu thế» is less transparent"),
    ("ariya", "cao quý (adj.); bậc thánh (person)", "everyday words"),
    ("magga / phala", "con đường / thành quả",
     "plain words; «đạo» alone reads as 'religion', and «quả» is kept for the result of kamma (vipāka = quả của nghiệp)"),
    ("sotāpanna", "bậc vào dòng", "plain rendering of 'stream-enterer'; «Nhập Lưu» is specialist"),
    ("arahant", "A-la-hán (bậc A-la-hán; arahatta = trạng thái của bậc A-la-hán)",
     "established word kept by the style file"),
    ("nibbāna", "Niết-bàn", "established word kept by the style file"),
    ("bhagavā", "Đức Thế Tôn", "established word kept by the style file"),
    ("bhikkhu", "tỳ-khưu", "established word kept by the style file"),
    ("puggala", "người", "everyday word for 'person'"),
    ("saṅkhāra", "tạo tác (khối tạo tác; các sự tạo tác)", "plain 'formation/fabrication'; «hành» is specialist"),
    ("asaṅkhata", "không do điều kiện tạo thành (saṅkhata = do điều kiện tạo thành; sappaccaya = có điều kiện)",
     "plain 'unconditioned'; «vô vi» is specialist"),
    ("paṭiccasamuppāda", "sự sinh khởi tùy thuộc vào điều kiện (paṭiccasamuppanna = sinh khởi tùy thuộc vào điều kiện)",
     "plain 'dependent arising'; «duyên khởi» is specialist"),
    ("kappa", "kiếp", "established word, also everyday («muôn kiếp»); the context shows the cosmic aeon"),
    ("mātikā", "ma trận (Tikamātikā = Ma trận bộ ba)",
     "'matrix' = a framework grid of headings, as in «ma trận đề thi» (an exam blueprint); not «dàn ý» or «tóm tắt»"),
    ("kamma / vipāka / kiriya", "nghiệp / quả của nghiệp / mang tính chức năng",
     "«nghiệp» is everyday Vietnamese; vipākābyākata = quả của nghiệp, không xác định về mặt đạo đức"),
]

CHOICES = """\
- Book title: Dhammasaṅgaṇīpāḷi = «Liệt kê các hiện tượng» (heading: Vietnamese name only). Frontmatter title: «Liệt kê các hiện tượng - tiếng Việt phổ thông». Alternative: «Phân loại các hiện tượng».
- mātikā = «ma trận»; tika / duka = «bộ ba» / «bộ đôi»; gocchaka = «nhóm»; antaraduka = «các bộ đôi xen giữa».
- Matrix item frame: dhammā = «các hiện tượng» + qualifier («Các hiện tượng thiện.»). Question «Katame dhammā X?» = «Những hiện tượng nào <PRED>?»; answer «ime dhammā X» = «đây là <BARE>.» after the Pāli «–».
- upādiṇṇa = «do nghiệp tạo ra» (the commentarial sense, as the approved English and Hindi); upādāniya = «là đối tượng của sự bám víu».
- -niya / sa- in the groups (sāsava, saṃyojaniya …) = «là đối tượng của X»; the negative = «không phải là đối tượng của X».
- saṃkiliṭṭha = «bị phiền não làm vẩn đục» (kilesa named, so the plain reader sees what clouds it); saṃkilesika = «là đối tượng của phiền não».
- dassana / bhāvanā (pahātabba) = «sự thấy chân lý» / «sự tu tập» («chân lý» is a wording clarification, as in the Hindi and Russian).
- ajjhatta / bahiddhā (triads 20, 21) = «thuộc về bản thân» / «ở bên ngoài bản thân» (ajjhatta = adhi + atta); ajjhattika / bāhira (pair 66) = «thuộc phần bên trong» / «thuộc phần bên ngoài».
- sahagata = «có X đi kèm»; sampayutta / vippayutta = «gắn liền với» / «không gắn liền với»; cetasika = «đồng hành với tâm».
- kāya- in kāyapassaddhi … kāyujukatā = «của thân tinh thần» (the string itself names the three mental aggregates); citta- = «của tâm».
- passaddhi = «sự an tịnh»; samatha = «sự tĩnh lặng»; vipassanā = «sự thấu suốt»; paggāha = «sự dốc sức»; avikkhepa = «sự không tán loạn».
- vīriya = «tinh tấn»; vāyāma / padhāna = «nỗ lực»; saṅkappa = «tư duy»; takka = «suy nghĩ»; cintā = «sự suy tư»; paṭisaṅkhāna = «suy xét».
- ñāṇa = «hiểu biết»; vijjā = «hiểu biết chân thật»; sampajañña = «sự hiểu biết rõ ràng»; dhammavicaya = «sự tìm hiểu các hiện tượng».
- adhivacana / nirutti / paññatti = «tên gọi» / «cách diễn đạt» / «khái niệm»; -patha = «phạm vi của …».
- sīla = «giới hạnh»; vipatti / sampadā / visuddhi = «sự suy đồi» / «sự thành tựu» / «sự trong sạch».
- khaya (in khaye ñāṇaṃ, āsavānaṃ khaya) = «sự diệt tận» (destruction, not exhaustion)."""

NOTES = """\
- ^1-33: the Pāli answer ends with «?» («ayaṃ tasmiṃ samaye adoso hoti?»), unlike every parallel; kept as «?» (looks like a source slip).
- ^1-M2-6, -19, -25, -31, -37, -43, -49, -54, -74, -82 (b): the Pāli line is elliptical (ahetukāpi, anāsavāpi …); the Vietnamese writes the item in full, as the approved English, Hindi and Russian do.
- ^1-M2-126 (b): the variant «[paṭisandhāro ca (ka.)]» stands after «ca»; kept at the end of the item.
- ^1-M2-138 (a) «diṭṭhivisuddhi kho pana»: «kho pana» is a connective; rendered like ^1-M2-137 (b), with «Và …» on the (b) line.
- ^1-1: «yaṃ yaṃ vā panārabbha» = «hay bất cứ thứ gì làm đối tượng» (the object list closes there).
- ^1-34: the paññā string is followed by «amoho kusalamūlaṃ» = «sự không si mê, gốc rễ thiện»."""


def heading_lines():
    seen, out = set(), []
    for f in sorted(PALI_DIR.glob("*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"(#+) (.*?)\s*\^[0-9A-Za-z-]+\s*$", line)
            if m and m.group(2) not in seen:
                seen.add(m.group(2))
                out.append((f.name, m.group(1), m.group(2)))
    return out


def check_preamble():
    want = (f"{NAMO} ^T-1\n\n# {HEADINGS['Abhidhammapiṭake']} ^0\n\n## {BOOK_TITLE} ^1-0\n")
    got = (VI_DIR / "preamble.md").read_text(encoding="utf-8")
    assert got == want, (got, want)


def main():
    check_preamble()
    L = []
    w = L.append
    w("# pi-1 Dhammasaṅgaṇī: Vietnamese plain zero-shot, binding terms")
    w("")
    w("Format: Pāli = Vietnamese, one per line. Reuse every Vietnamese string verbatim (import it, do not retype it).")
    w("Generated by build_terms_vi.py from build_matika_vi.py and build_ch2_01_sample_vi.py; both modules hold the")
    w("strings as Python constants and can be imported by later chapter builders.")
    w("")
    w("## 1. Text frame and headings")
    w("")
    w(f"Namo tassa bhagavato arahato sammāsambuddhassa = {NAMO}")
    w(f"Frontmatter title = {FRONTMATTER_TITLE}")
    missing = []
    cur = None
    for fname, hashes, pali in heading_lines():
        if fname != cur:
            cur = fname
            w(f"### {fname}")
        if pali not in HEADINGS:
            missing.append(pali)
            continue
        w(f"{hashes} {pali} = {hashes} {HEADINGS[pali]}")
    assert not missing, missing
    w("Same heading text at another level (e.g. ##### Kāmāvacarakusalaṃ in 2-02) = same Vietnamese at that level.")
    w("")
    w("Closing lines:")
    for p, r in CLOSINGS:
        w(f"{p} = {r}")
    w("")
    w("## 2. Matrix items (exactly as in 1-matika.md; chapters 4 and 5 must reuse them verbatim)")
    w("")
    w("Line form: ^block-id (letter) Pāli = Vietnamese matrix line ‖ Q = question frame ‖ A = answer frame.")
    w("Inside running sentences use the bare name (build_matika_vi.BARE): lower-case start, no variant bracket, no final «.».")
    w("Katame dhammā X? = «Những hiện tượng nào <PRED>?» (build_matika_vi.QUESTION); ime dhammā X = «đây là <BARE>.» "
      "after the Pāli «–» (build_matika_vi.ANSWER / ANSWER_BARE). Items ^1-M2-109 … 142 are nouns without a question frame.")
    w("List markers (Ka) / (Kha) / (Ga) = (a) / (b) / (c).")
    w("")
    w("### Sets of three (triads)")
    for bid, letter, pali, vi in M.MATRIX_ITEMS_VI:
        if bid == "1-M2-1":
            w("")
            w("### Pairs")
        key = (bid, letter)
        tail = ""
        if M.PRED[key]:
            tail = f" ‖ Q = {M.QUESTION(key)} ‖ A = {C.DASH} {M.ANSWER(key)}"
        w(f"^{bid} ({letter}) {pali} = {vi}{tail}")
    w("")
    w("## 3. Recurring formulas (from the chapter-2 sample, ^1-1 to ^1-57)")
    w("")
    w("### 3a. Frames (X = factor name from 3c; S = synonym string from 3b)")
    for p, r in C.FRAMES.items():
        w(f"{p} = {r}")
    w("")
    w("### 3b. Synonym strings (bare; the frame supplies «Điều có mặt vào lúc ấy, tức là S – đây là X vào lúc ấy.»)")
    for p, r in C.STRINGS.items():
        w(f"{p} = {r}")
    w(f"tajjāmanoviññāṇadhātusamphassajaṃ/-jā (before a string) = và {C.TAJJA} (after «Điều có mặt vào lúc ấy»)")
    w(f"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa = {C.G_KAYA}")
    w(f"viññāṇakkhandhassa = {C.G_CITTA}")
    w(f"tesaṃ arūpīnaṃ dhammānaṃ = {C.G_JIVITA}")
    w(f"paññā string + amoho kusalamūlaṃ = <paññā string>, {C.N['amoho']}, {C.ROOT}")
    w("Variant forms (first occurrences only, as in the Pāli): ^1-5, ^1-13, ^1-19, ^1-33, ^1-40; see S_CETANA_V, "
      "S_VIRIYA_V, S_JIVITA_V, S_ADOSA_V, S_PASSADDHI_V and VAR() in the sample builder.")
    w("Variant brackets = [dị bản (Sī.): …] when a word differs; [khác chính tả (Syā.): …] for spelling only; "
      "sigla capitalised, comma-separated: (Sī., Syā.), (Sī., Ka.), (Ka.).")
    w("")
    w("### 3c. Factor names (same form in «có X», «Vào lúc ấy, X là gì?» and «đây là X vào lúc ấy»)")
    for k, v in C.NAMES.items():
        w(f"{k} = {v}")
    w("")
    w("## 4. Core terms (cross-book proposals; full list with reasons in vi-core-terms.md)")
    w("")
    for p, v, _ in CORE:
        w(f"{p} = {v}")
    w("")
    w("## 5. Term choices")
    w("")
    L.extend(CHOICES.splitlines())
    w("")
    w("## 6. Source notes (translated as written)")
    w("")
    L.extend(NOTES.splitlines())
    text = "\n".join(L) + "\n"
    assert "\n\n\n" not in text
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, "lines", len(L))

    K = ["# Vietnamese core terms (cross-book proposals from the pi-1 sample)", "",
         "Format: Pāli = Vietnamese | reason. Becomes the «Core terms (cross-book)» list of vietnamese-style.md "
         "once approved.", ""]
    K += [f"{p} = {v} | {r}" for p, v, r in CORE]
    OUT_CORE.write_text("\n".join(K) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT_CORE, "terms", len(CORE))


if __name__ == "__main__":
    main()
