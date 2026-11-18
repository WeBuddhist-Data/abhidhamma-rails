"""Pāli->Vietnamese keyword map for pi-1 part 4-01-nikkhepakandam (summary of the triads; root, short
intermediate, taint, fetter and tie groups).

usage: python -I -X utf8 map_4-01_vi.py            (writes 4-01-nikkhepakandam.mapped.md and verifies it)
       python -I -X utf8 map_4-01_vi.py dump       (prints every distinct keyword=value with count and presence
                                                    misses; writes nothing)

Importing this file writes nothing (it imports map_3-02_3-03_vi.py, which imports map_2-05_3-01_vi.py,
map_2-04_vi.py and map_2-02_2-03_vi.py; none of them rewrites its output on import).
Resolution order per keyword:
  OVERRIDES[bid][kw] -> context() -> the 2-05 context05() (with the 2-04 / 2-02 rules) -> ADD401 -> MATRIX
  -> «dhammā X» = MATRIX «X dhammā» or «hiện tượng X» -> the 3-02/3-03 value() (RUPA -> «rūpaṃ X» rules ->
  ADD301 -> MATRIX) -> T05 via ch2_value; a «dhammā X» value not found contiguous becomes «hiện tượng … X»
Matrix item names take the MATRIX value unless the segment's Vietnamese words them differently.
Conventions: vi-map-conventions.md and the earlier notes-map-*.md; new: notes-map-4-01.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, MATRIX, NDE, build_part, ch2_value, lc, present,  # noqa: E402
                           read_keywords, read_vietnamese, verify)

_spec = importlib.util.spec_from_file_location("map_3_02_3_03_vi", HERE / "map_3-02_3-03_vi.py")
_p302 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_p302)          # import only: its __main__ block does not run
T05 = _p302.T05

PART = "4-01-nikkhepakandam"

_p301 = _p302._p301                      # map_2-05_3-01_vi.py (context05: the 2-05 / 2-04 / 2-02 context rules)

_ASD = "yếu tố không do điều kiện tạo thành"
_KH = "nút thắt của thân"
_SILA = "sự hiểu sai lệch về giới hạnh và nghi thức"
_IDAM = "sự cố chấp rằng chỉ điều này là sự thật"      # «sự cố chấp rằng “chỉ điều này là sự thật”» (quotes dropped)
_ARB = "sinh khởi khi lấy" + GAP + "làm"                # ārabbha ye uppajjanti
_CC = "tâm và các yếu tố đồng hành với tâm"             # cittacetasikā

# New keys and the 4-01 readings (this table precedes MATRIX and the earlier tables).
ADD401 = {
    # ---------------------------------------------------------------- headings and closing lines
    "nikkhepa": "tóm lược", "nikkhepaṃ": "tóm lược",          # «Phần tóm lược», «Tóm lược các bộ ba / đôi»
    # ---------------------------------------------------------------- frame of the triads
    "rūpakkhandho": "khối vật chất",
    "bhūmiyaṃ": "cấp độ",                                   # «Ở cấp độ có …» («Ở» = locative frame)
    "kāmāvacare": "thuộc cõi dục lạc", "rūpāvacare": "thuộc cõi hình sắc",
    "arūpāvacare": "thuộc cõi không hình sắc", "avacare": "thuộc cõi",
    "sampayutto": "gắn liền",                               # taṃsampayutto «những gì gắn liền với chúng / nó»
    "kusalamūlāni": "gốc rễ thiện", "akusalamūlāni": "gốc rễ bất thiện", "mūlāni": "gốc rễ",
    "kāyakammaṃ": "nghiệp bằng thân", "vacīkammaṃ": "nghiệp bằng lời nói", "manokammaṃ": "nghiệp bằng ý",
    "vacīkammaṃ manokammaṃ": "nghiệp bằng lời nói nghiệp bằng ý",     # comma dropped
    "samuṭṭhānaṃ kāyakammaṃ": "do" + GAP + "sinh ra" + GAP + "nghiệp bằng thân",   # «do chúng sinh ra, tức là …»
    "ekaṭṭhā": "cùng hiện diện",                            # tadekaṭṭhā «cùng hiện diện với chúng»
    "ekaṭṭhā ca kilesā": "và các phiền não cùng hiện diện",
    "akusalā dhammā": "hiện tượng" + GAP + "bất thiện",     # kusalākusalā «hiện tượng thiện và bất thiện»
    "abyākatā dhammā": "hiện tượng" + GAP + "không xác định về mặt đạo đức",   # kusala(akusala)ābyākatā
    "akusalābyākatā": "bất thiện và không xác định về mặt đạo đức",
    "sāsavā kusalākusalā dhammā": "hiện tượng thiện và bất thiện là đối tượng của ô nhiễm",
    "sāsavā kusalābyākatā dhammā":
        "hiện tượng thiện và không xác định về mặt đạo đức là đối tượng của ô nhiễm",
    "avasesā": "còn lại", "avaseso": "còn lại",
    "avasesā kusala": "thiện" + GAP + "còn lại",
    "avasesā sāsavā kusala": "thiện" + GAP + "còn lại là đối tượng của ô nhiễm",
    "yañca": "và loại",                                     # yañca rūpaṃ «và loại vật chất …»
    "asaṅkhatā dhātu": _ASD,
    "apariyāpannā maggā": "con đường không nằm trong các cõi tồn tại",
    "maggā apariyāpannā": "con đường không nằm trong các cõi tồn tại",
    "maggā": "con đường", "phalāni": "thành quả", "phalaṃ": "thành quả",
    "sāmañña": "đời sống sa-môn", "upariṭṭhimaṃ": "cao nhất", "arahatta": "A-la-hán",
    "kammāni": "nghiệp", "ānantarikāni": "có quả không gián đoạn",
    "avipakkavipākānaṃ": "có quả chưa chín muồi",
    "tehi dhammehi": "hiện tượng ấy",                       # «có những hiện tượng ấy làm gốc rễ» …
    "yeva": "nào",                                          # Yeva te dhammā … «Những hiện tượng nào … thì chính …»
    # ---------------------------------------------------------------- object triads (ārabbha)
    "uppajjanti": "sinh khởi", "ārabbha ye uppajjanti": _ARB,
    "cittacetasikā": _CC, "uppajjanti cittacetasikā": _CC + " sinh khởi",
    "cetasikā": "yếu tố đồng hành với tâm",                 # «các yếu tố đồng hành với tâm» (MATRIX: đồng hành với tâm)
    "paritte dhamme": "hiện tượng hạn hẹp", "mahaggate dhamme": "hiện tượng rộng lớn",
    "appamāṇe dhamme": "hiện tượng không thể đo lường", "atīte dhamme": "hiện tượng thuộc quá khứ",
    "anāgate dhamme": "hiện tượng thuộc tương lai", "paccuppanne dhamme": "hiện tượng thuộc hiện tại",
    "paritte dhamme ārabbha": "lấy các hiện tượng hạn hẹp làm",
    "mahaggate dhamme ārabbha": "lấy các hiện tượng rộng lớn làm",
    "appamāṇe dhamme ārabbha": "lấy các hiện tượng không thể đo lường làm",
    "atīte dhamme ārabbha": "lấy các hiện tượng thuộc quá khứ làm",
    "anāgate dhamme ārabbha": "lấy các hiện tượng thuộc tương lai làm",
    "paccuppanne dhamme ārabbha": "lấy các hiện tượng thuộc hiện tại làm",
    "bahiddhā dhamme ārabbha": "lấy các hiện tượng ở bên ngoài bản thân làm",
    "dhamme ārabbha": "lấy các hiện tượng" + GAP + "làm",   # ^1-1055 (ajjhattabahiddhā between)
    # ---------------------------------------------------------------- path triad (^1-1038 … 1-1040)
    "ariya": "cao quý", "ariyamagga": "con đường cao quý", "ariyamaggaṃ": "con đường cao quý",
    "samaṅgissa": "người có được", "aṅgāni": "chi phần", "maggahetū": "gốc rễ của con đường",
    "bhāvayantassa": "đang tu tập", "maggaṃ bhāvayantassa": "đang tu tập con đường",
    # ---------------------------------------------------------------- arisen / past / internal
    "jātā": "đã sinh ra", "sañjātā": "đã sinh thành", "nibbattā": "đã phát sinh",
    "abhinibbattā": "đã phát sinh rõ rệt", "pātubhūtā": "đã hiện ra",
    "samuppannā": "đã sinh khởi trọn vẹn", "uṭṭhitā": "đã trỗi dậy", "samuṭṭhitā": "đã trỗi dậy trọn vẹn",
    "aṃsena": "phần",                                       # X-aṃsena saṅgahitā «được xếp vào phần X»
    "niruddhā": "đã chấm dứt", "vigatā": "đã mất đi", "vipariṇatā": "đã biến đổi",
    "abbhatthaṅgatā": "đã biến mất hoàn toàn", "uppajjitvā": "sau khi sinh khởi",
    "saṅkhārā": "sự tạo tác", "saṅkhāre": "sự tạo tác",     # «các sự tạo tác»
    "tesaṃ tesaṃ": "từng", "paccattaṃ": "riêng từng người", "pāṭipuggalikā": "thuộc về cá nhân",
    "puggalānaṃ": "người",                                  # parapuggalānaṃ «từng người khác»
    # ---------------------------------------------------------------- roots (^1-1059 …)
    "kusalahetū": "gốc rễ thiện", "akusalahetū": "gốc rễ bất thiện",
    "abyākatahetū": "gốc rễ không xác định về mặt đạo đức",
    "kāmāvacarahetū": "gốc rễ thuộc cõi dục lạc", "rūpāvacarahetū": "gốc rễ thuộc cõi hình sắc",
    "arūpāvacarahetū": "gốc rễ thuộc cõi không hình sắc",
    "apariyāpannahetū": "gốc rễ không nằm trong các cõi tồn tại",
    "vipākato": "quả",                                      # «các quả của các hiện tượng thiện»
    "kiriya": "mang tính chức năng",
    "kusalānaṃ": "thiện", "kusalānaṃ dhammānaṃ": "hiện tượng thiện",
    "kusalānaṃ vā dhammānaṃ": "hiện tượng thiện",           # the first vā has no word («… hoặc trong …»)
    "abyākatesu vā dhammesu": "hoặc" + GAP + "hiện tượng không xác định về mặt đạo đức",
    "mohena": "sự si mê",                                   # «… có gốc rễ là sự si mê»
    # adosa with mettā (^1-1062)
    "metti": "lòng từ ái", "mettāyanā": "sự khởi lòng từ ái", "anuddā": "lòng thương mến",
    "anuddāyanā": "sự khởi lòng thương mến", "hitesitā": "sự mong muốn điều lợi ích", "hita": "điều lợi ích",
    "anukampā": "lòng thương xót",
    # knowledge / non-knowledge of the truths (amoha, moha, avijjā)
    "dukkhe": "khổ đau", "dukkhe ñāṇaṃ": "hiểu biết về khổ đau", "dukkhe aññāṇaṃ": "sự không biết về khổ đau",
    "samudaye": "sự phát sinh", "nirodhe": "sự chấm dứt", "dukkhanirodhe": "sự chấm dứt khổ đau",
    "idappaccayatā": "quy luật tùy thuộc vào điều kiện",
    "paṭiccasamuppannesu": "sinh khởi tùy thuộc vào điều kiện",
    "paṭiccasamuppannesu dhammesu": "hiện tượng sinh khởi tùy thuộc vào điều kiện",
    "samuppannesu": "sinh khởi", "samuppannesu dhammesu": "hiện tượng sinh khởi",
    "sambojjha": "giác ngộ", "aṅgo": "chi phần",            # dhammavicayasambojjhaṅgo «chi phần giác ngộ là …»
    "adassanaṃ": "sự không thấy", "ananubodho": "sự không hiểu ra", "asambodho": "sự không tỉnh ngộ",
    "apariyogāhanā": "sự không đi sâu", "asamapekkhanā": "sự không xem xét",
    "apaccavekkhaṇā": "sự không xem xét lại", "paccavekkhaṇā": "xem xét lại",
    "apaccakkhakammaṃ": "sự không tự mình thấy rõ", "asampajaññaṃ": "sự thiếu hiểu biết rõ ràng",
    # ---------------------------------------------------------------- relatives, frame of the strings
    "evarūpā": "thuộc loại như vậy", "evarūpo": "thuộc loại như vậy", "evarūpaṃ": "thuộc loại như vậy",
    # ---------------------------------------------------------------- views and fetters of seeing (^1-1006 …)
    "saṃyojanāni": "xiềng xích",
    "sakkāya": "tự ngã", "sakkāyadiṭṭhi": "quan điểm về tự ngã",
    "sīla": "giới hạnh", "vata": "nghi thức", "sīlabbata": "giới hạnh và nghi thức",
    "sīlabbataparāmāso": _SILA, "sīlabbataparāmāsaṃ": _SILA,
    "sīlabbataparāmāsa": "hiểu sai lệch về giới hạnh và nghi thức",   # stem: «xiềng xích hiểu sai lệch về …»
    "puthujjano": "người phàm phu", "assutavā": "không được học hỏi", "ariyānaṃ": "bậc thánh",
    "dhammassa": "Giáo Pháp", "akovido": "không thông thạo", "avinīto": "không được rèn luyện",
    "sappurisānaṃ": "người chân chính", "purisānaṃ": "người",
    "samanupassati": "xem", "attato": "tự ngã", "rūpavantaṃ": "có vật chất",
    "paṭiggāho": "sự bám chặt",                             # gāho paṭiggāho «sự nắm giữ, sự bám chặt»
    "satthari": "Bậc Đạo Sư", "kaṅkhati": "nghi ngờ", "sikkhāya": "sự tu học",
    "dvedhāpatho": "sự đứng trước ngã ba đường",
    "thambhitattaṃ": "trạng thái cứng đờ",                  # vicikicchā string (2-04); 3-03 «căng cứng» is āpo
    "ito": "Giáo Pháp này",                                 # Ito bahiddhā «bên ngoài Giáo Pháp này»
    "samaṇa": "sa-môn", "brāhmaṇānaṃ": "bà-la-môn", "suddhi": "trong sạch",
    # ---------------------------------------------------------------- the lobha string (^1-1065, ^1-1141)
    "rāgo": "sự tham đắm", "anunayo": "sự chiều theo", "anurodho": "sự xuôi theo", "nandī": "sự thích thú",
    "icchā": "sự mong muốn", "mucchā": "sự mê đắm", "gedho": "sự thèm khát",
    "paligedho": "sự thèm khát mãnh liệt", "saṅgo": "sự dính mắc", "paṅko": "vũng bùn", "ejā": "sự xao xuyến",
    "māyā": "sự huyễn hoặc", "janikā": "kẻ sinh ra", "sañjananī": "kẻ tạo thành", "sibbinī": "kẻ khâu nối",
    "jālinī": "kẻ giăng lưới", "saritā": "dòng chảy", "visattikā": "sự vướng mắc khắp nơi",
    "suttaṃ": "sợi chỉ", "visaṭā": "sự lan tràn", "āyūhinī": "kẻ thúc đẩy", "dutiyā": "người bạn đồng hành",
    "paṇidhi": "sự mong cầu", "netti": "sợi dây dẫn đến",  # bhavanetti «sợi dây dẫn đến hiện hữu»
    "vanaṃ": "rừng", "vanatho": "bụi rậm", "santhavo": "sự thân thiết",
    "sineho": "sự luyến ái",                                # also kāmasneho «sự luyến ái dục lạc»; 3-03 «chất ẩm» is āpo
    "apekkhā": "sự quyến luyến", "paṭibandhu": "mối thân thuộc", "āsā": "sự mong mỏi",
    "āsisanā": "sự trông mong", "dhana": "tài sản", "putta": "con cái",
    "jappā": "sự thèm thuồng", "pajappā": "sự thèm thuồng mãnh liệt", "abhijappā": "sự thèm thuồng tột độ",
    "jappanā": "sự khởi thèm thuồng", "loluppaṃ": "sự ham hố", "loluppāyanā": "sự khởi ham hố",
    "pucchañjikatā": "sự xu nịnh", "sādhu": "điều tốt đẹp", "kamyatā": "sự ham",   # sādhukamyatā «sự ham điều tốt đẹp»
    "adhamma": "phi pháp", "visama": "bất chính", "nikanti": "sự ưa thích", "nikāmanā": "sự ham muốn",
    "patthanā": "sự mong ước", "pihanā": "sự ước ao", "sampatthanā": "sự mong ước mãnh liệt",
    "bhava": "hiện hữu",                                    # bhavanetti, bhavataṇhā «khao khát được hiện hữu», bhavāsavo
    "vibhava": "không còn hiện hữu",                        # vibhavataṇhā «khao khát không còn hiện hữu»
    "nirodha": "sự chấm dứt",                               # nirodhataṇhā «khao khát sự chấm dứt»
    "gantho": "nút thắt", "upādānaṃ": "sự bám víu", "āvaraṇaṃ": "sự che lấp", "nīvaraṇaṃ": "chướng ngại",
    "chādanaṃ": "sự che đậy", "bandhanaṃ": "sự trói buộc", "upakkileso": "sự làm ô uế", "latā": "dây leo",
    "vevicchaṃ": "sự bủn xỉn", "dukkha": "khổ đau",         # dukkhamūlaṃ «gốc rễ của khổ đau»
    "nidānaṃ": "căn nguyên", "pabhavo": "cội nguồn", "pāso": "bẫy", "baḷisaṃ": "lưỡi câu",
    "visayo": "lãnh địa", "nadī": "dòng sông", "gaddulaṃ": "dây xích", "samuddo": "biển",
    "jīvita": "mạng sống",                                  # jīvitāsā «sự mong mỏi mạng sống»
    # ---------------------------------------------------------------- the dosa string (^1-1066, 1-1120, 1-1142)
    "anatthaṃ": "hại", "acarīti": "đã gây", "acarī": "đã gây", "caratīti": "đang gây",   # «… đã gây hại cho ta»
    "āghāto": "sự oán giận", "jāyati": "khởi lên", "āghāto jāyati": "sự oán giận khởi lên",
    "piyassa": "yêu quý", "manāpassa": "ưa thích", "aṭṭhāne": "vô cớ",
    "paṭighāto": "sự phẫn uất", "paṭighaṃ": "sự ác cảm", "kopo": "sự nổi nóng",
    "pakopo": "sự nổi nóng dữ dội", "sampakopo": "sự nổi nóng tột độ", "padoso": "sự sân hận dữ dội",
    "sampadoso": "sự sân hận tột độ", "kodho": "sự giận dữ", "kujjhanā": "sự khởi giận",
    # ---------------------------------------------------------------- taints (^1-1102 …)
    "āsavo": "ô nhiễm", "kāmāsavo": "ô nhiễm dục lạc", "bhavāsavo": "ô nhiễm hiện hữu",
    "diṭṭhāsavo": "ô nhiễm quan điểm", "avijjāsavo": "ô nhiễm vô minh", "avijjāsavena": "ô nhiễm vô minh",
    "kāmesu": "dục lạc", "chando": "ý muốn", "kāmacchando": "ý muốn dục lạc", "kāmarāgo": "sự tham đắm dục lạc",
    "pariḷāho": "sự nóng bỏng",
    "sassato": "trường tồn", "jīvaṃ": "linh hồn", "sarīranti": "thân thể", "sarīraṃ": "thân thể",
    "aññaṃ": "khác", "hoti": "còn tồn tại", "hoti tathāgato": "Như Lai còn tồn tại",
    "maraṇāti": "chết", "maraṇā": "chết",                   # paraṃ maraṇā «sau khi chết»
    "moghamaññanti": "mọi điều khác đều sai",
    # ---------------------------------------------------------------- fetters (^1-1118 …)
    "kāmarāgasaṃyojanaṃ": "xiềng xích tham đắm dục lạc", "paṭighasaṃyojanaṃ": "xiềng xích ác cảm",
    "mānasaṃyojanaṃ": "xiềng xích kiêu mạn", "vicikicchāsaṃyojanaṃ": "xiềng xích hoài nghi",
    "sīlabbataparāmāsasaṃyojanaṃ": "xiềng xích hiểu sai lệch về giới hạnh và nghi thức",
    "bhavarāgasaṃyojanaṃ": "xiềng xích tham đắm hiện hữu", "issāsaṃyojanaṃ": "xiềng xích ganh tị",
    "macchariyasaṃyojanaṃ": "xiềng xích keo kiệt", "avijjāsaṃyojanaṃ": "xiềng xích vô minh",
    "avijjāsaṃyojanena": "xiềng xích vô minh",
    "issā": "sự ganh tị", "macchariya": "keo kiệt",
    "kāmarāga": "sự tham đắm dục lạc",                      # 2-03 value; fetter-name lists: OVERRIDES
    # conceit (^1-1121)
    "maññanā": "sự tự đánh giá mình", "maññitattaṃ": "trạng thái tự đánh giá mình", "unnati": "sự tự cao",
    "unnamo": "sự vênh vang", "dhajo": "ngọn cờ", "ketu": "được giương cờ",
    "ketukamyatā": "sự mong muốn" + GAP + "được giương cờ",   # «sự mong muốn của tâm được giương cờ»
    "sadiso": "bằng", "hīno": "kém",                        # «Ta bằng người», «Ta kém người»
    # envy (^1-1126)
    "issāyanā": "sự khởi ganh tị", "usūyā": "sự đố kỵ", "usūyanā": "sự khởi đố kỵ", "para": "người khác",
    "sakkāra": "sự tôn vinh", "garukāra": "sự kính trọng", "mānana": "sự quý trọng", "vandana": "sự đảnh lễ",
    "pūjanāsu": "sự cúng dường",
    # stinginess (^1-1127)
    "macchariyāni": "loại keo kiệt", "āvāsa": "chỗ ở", "kula": "gia đình", "vaṇṇa": "lời khen",
    "maccharāyanā": "sự khởi keo kiệt", "kadariyaṃ": "sự hà tiện", "kaṭukañcukatā": "sự bo bo",
    "aggahitattaṃ": "trạng thái khép chặt",
    "saṃyojanā ceva saṃyojaniyā": "vừa là xiềng xích vừa là đối tượng của xiềng xích",
    "saṃyojanavippayuttā saṃyojaniyā": "không gắn liền với xiềng xích nhưng là đối tượng của xiềng xích",
    # ---------------------------------------------------------------- ties (^1-1140 …)
    "kāyagantho": _KH, "sacca": "sự thật",
    "abhijjhā kāyagantho": f"{_KH} bằng sự thèm muốn", "abhijjhākāyaganthena": f"{_KH} bằng sự thèm muốn",
    "byāpādo kāyagantho": f"{_KH} bằng sự ác ý",
    "sīlabbataparāmāso kāyagantho": f"{_KH} bằng {_SILA}",
    "sīlabbataparāmāsaṃ kāyaganthaṃ": f"{_KH} bằng {_SILA}",
    "idaṃsaccābhiniveso kāyagantho": f"{_KH} bằng {_IDAM}",
    "idaṃ saccābhiniveso kāyagantho": f"{_KH} bằng {_IDAM}",
    "vuccati abhijjhā kāya": "được gọi là" + GAP + "thân bằng sự thèm muốn",
    "vuccati byāpādo kāya": "được gọi là" + GAP + "thân bằng sự ác ý",
    "vuccati sīlabbataparāmāso kāya": "được gọi là" + GAP + f"thân bằng {_SILA}",
    "vuccati idaṃsaccābhiniveso kāya": "được gọi là" + GAP + f"thân bằng {_IDAM}",
    "ganthā ceva ganthaniyā": "vừa là nút thắt vừa là đối tượng của nút thắt",
    "ganthavippayuttā ganthaniyā": "không gắn liền với nút thắt nhưng là đối tượng của nút thắt",
    # ---------------------------------------------------------------- dhammā X (the item as the question / answer words it)
    "dhammā ācayagāmino": "hiện tượng dẫn đến sự tích lũy",
    "dhammā apacayagāmino": "hiện tượng dẫn đến sự giảm trừ",
    "dhammā neva ācayagāmi": "hiện tượng không dẫn đến sự tích lũy",
    "dhammā appaṭighā": "hiện tượng không có tính va chạm",
    "dhammā avitakkaavicārā": "hiện tượng không có sự hướng tâm cũng không có sự duy trì tâm",
    "dhammā dassanena pahātabbahetukā": "hiện tượng có gốc rễ cần dứt bỏ bằng sự thấy chân lý",
    "dhammā bhāvanāya pahātabbahetukā": "hiện tượng có gốc rễ cần dứt bỏ bằng sự tu tập",
    "pahātabbahetukā": "có gốc rễ" + GAP + "cần dứt bỏ",   # ^1-1019 «có gốc rễ không cần dứt bỏ …»
    "dhammā hetuvippayuttā": "hiện tượng không gắn liền với gốc rễ",
    "dhammā micchattaniyatā": "hiện tượng cố định theo hướng sai lầm",
    "dhammā sammattaniyatā": "hiện tượng cố định theo hướng đúng đắn",
    "dhammā pītisahagatā": "hiện tượng có sự hân hoan đi kèm",
    "dhammā sukhasahagatā": "hiện tượng có hạnh phúc đi kèm",
    "dhammā upekkhāsahagatā": "hiện tượng có sự bình thản đi kèm",
    "dhammā saṃyojanā": "hiện tượng là xiềng xích",          # «Đây là các hiện tượng là xiềng xích»
}
for _s, _v in (("cakkhu", "mắt"), ("sota", "tai"), ("ghāna", "mũi"), ("jivhā", "lưỡi"), ("kāya", "thân")):
    ADD401[f"dhammā {_s}"] = f"hiện tượng mà {_v}"         # ^1-1101 «Những hiện tượng mà mắt có thể nhận biết …»

# Fetter-name lists (^1-1118, ^1-1136): the stem inside «xiềng xích X» has no «sự»
_FETTER_BARE = {"paṭigha": "ác cảm", "māna": "kiêu mạn", "vicikicchā": "hoài nghi", "issā": "ganh tị",
                "rāga": "tham đắm", "kāmarāga": "tham đắm dục lạc", "parāmāsa": "hiểu sai lệch"}
OVERRIDES = {
    "1-1118": dict(_FETTER_BARE),
    "1-1136": {**_FETTER_BARE, "Kāmarāga": "tham đắm dục lạc"},
    "1-1120": {"paṭigha": "ác cảm"},          # paṭighasaṃyojanaṃ; the string word is paṭighaṃ «sự ác cảm»
    "1-1124": {"parāmāsa": "hiểu sai lệch"},  # sīlabbataparāmāsa(-saṃyojanaṃ) «xiềng xích hiểu sai lệch …»
    "1-1122": {"sīlabbataparāmāsa": "hiểu sai lệch về giới hạnh và nghi thức"},
    "1-1024": {"sekkhā": NDE},                 # only the member of asekkhā «người đã hoàn tất tu học»
    "1-1092": {"Yo": "nào"},                   # Yo eva so dhammo … «Hiện tượng nào …»
    "1-1127": {"dhamma": "Giáo Pháp"},         # dhammamacchariyaṃ «keo kiệt về Giáo Pháp»
}
# vicikicchā string: patho / gāho only inside dvedhāpatho / anekaṃsaggāho
for _b in ("1-1008", "1-1123"):
    OVERRIDES[_b] = {"patho": "đường", "gāho": "nắm giữ", "dhamme": "Giáo Pháp"}


def context(bid, kw, k, s, text):
    """4-01 segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k in ("yo", "yā", "yaṃ"):                        # «Bất cứ điều gì (thuộc loại như vậy) là …»
        return "bất cứ điều gì"
    if k == "rūpa" and "rūpakkhandho" in s and not s & {"rūpāvacarā", "rūpāvacare", "rūpāvacara"}:
        return "vật chất"                               # rūpakkhandho «khối vật chất» (no rūpāvacar- in the segment)
    if k == "ñāṇaṃ" and "aññāṇaṃ" in s:                 # moha string: fragment of aññāṇaṃ «sự không biết»
        return "biết"
    if k == "sampajaññaṃ" and "asampajaññaṃ" in s:      # fragment of asampajaññaṃ (as 2-04 1-390)
        return "hiểu biết rõ ràng"
    if k == "uppannā" and "jātā" in s and "dhammā uppannā" not in s and "dhammā paccuppannā" not in s:
        return "sinh khởi"                              # anuppannā «chưa sinh khởi» (^1-1042, ^1-1045; aspect dropped)
    if k in _NEG_UPP and "jātā" in s and "dhammā uppannā" not in s and "dhammā paccuppannā" not in s:
        return _NEG_UPP[k]                              # ajātā … «chưa sinh ra …» (positive part, aspect dropped)
    if k == "niyatā" and "pāṭipuggalikā" in s:          # «cố hữu» (^1-1050, ^1-1051)
        return "cố hữu"
    if k == "bahiddhā" and "ito" in s:                  # Ito bahiddhā «bên ngoài Giáo Pháp này»
        return "bên ngoài"
    if k == "hetukā" and "maggahetū" in s:              # maggahetukā «lấy con đường làm gốc rễ»
        return "lấy" + GAP + "làm gốc rễ"
    if k == "ārammaṇā" and "ariyamaggaṃ" in s and "uppajjanti" in s and "adhipatino" not in s:
        return "lấy" + GAP + "làm đối tượng"            # maggārammaṇā (^1-1038; as MATRIX 1-M1-16)
    if k == "kamyatā" and "ketukamyatā" in s:           # «sự mong muốn của tâm được giương cờ»
        return "sự mong muốn"
    if k == "sampaggāho" and "ketukamyatā" in s:        # conceit string «sự tự đề cao»
        return "sự tự đề cao"
    if k == "māna" and "maññanā" in s:                  # conceit string «sự kiêu mạn»
        return "sự kiêu mạn"
    if k == "dhamme" and "ārabbha" in s:                # ^1-1055 «các hiện tượng …»
        return "hiện tượng"
    if k == "sāsavā kusalākusalābyākatā dhammā":
        whole = "hiện tượng thiện bất thiện và không xác định về mặt đạo đức là đối tượng của ô nhiễm"
        return whole if present(whole, text) else whole.replace(" là đối tượng", GAP + "là đối tượng")
    if k.startswith("vuccati ") and k not in ADD401:    # «đây được gọi là X»
        return "được gọi là " + _value(k[len("vuccati "):])
    return None


_NEG_UPP = {"sañjātā": "sinh thành", "nibbattā": "phát sinh", "abhinibbattā": "phát sinh rõ rệt",
            "pātubhūtā": "hiện ra", "samuppannā": "sinh khởi trọn vẹn", "uṭṭhitā": "trỗi dậy",
            "samuṭṭhitā": "trỗi dậy trọn vẹn"}
_NEG_UPP["jātā"] = "sinh ra"


def _value(k, t05=True):
    """Table value of a lower-cased keyword (no segment rules); t05=False leaves T05 to ch2_value."""
    if k in ADD401:
        return ADD401[k]
    if k in MATRIX:
        return MATRIX[k]
    if k.startswith("dhammā "):                         # the matrix item as «hiện tượng X»
        x = k[len("dhammā "):]
        if f"{x} dhammā" in MATRIX:
            return MATRIX[f"{x} dhammā"]
        return "hiện tượng " + _value(x)
    try:
        return _p302.value(k)
    except KeyError:
        if not t05:
            raise
        return T05[k]


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        v = context(bid, kw, k, s, vi.get(bid, ""))
        if v is None:
            v = _p301.context05(bid, k, s)
        if v is not None:
            return v
        try:
            v = _value(k, t05=False)
        except KeyError:
            return ch2_value(kw, kws, T05)
        text = vi.get(bid, "")
        if k.startswith("dhammā ") and v.startswith("hiện tượng ") and not present(v, text):
            v = "hiện tượng" + GAP + v[len("hiện tượng "):]   # «Những hiện tượng nào X?» (nào between)
        return v
    return resolve


def dump(part):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss = Counter(), Counter()
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            if v == "???" or not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        print(f"{kw}={v}  [{n}]" + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(PART)
    else:
        build_part(PART, resolver_for(PART))
        verify(PART)
