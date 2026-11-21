"""Build the SAMPLE Pāli->Vietnamese keyword maps for pi-5 (Kathāvatthu): preamble, 1-puggalakatha.

usage: python -I -X utf8 map_sample_vi.py                     (writes the two <part>.mapped.md and verifies them)
       python -I -X utf8 map_sample_vi.py dump PART [miss]    (every distinct keyword=value with count, first segments
                                                              and the pi-1 … pi-4 map values; writes nothing)
       python -I -X utf8 map_sample_vi.py show PART lo hi [pi]
                                                              (segments lo..hi: Vietnamese (and Pāli), every pair with
                                                              the English / Russian value; writes nothing)
       python -I -X utf8 map_sample_vi.py look kw ...         (pi-1 … pi-4 map values; writes nothing)

Importing this module builds nothing. Later part scripts import from here:
    from map_sample_vi import FORMULAS, KV, context5, value5
Resolution order per keyword: OVERRIDES[bid][kw] -> CORE (preamble only) -> value5(): your table -> FORMULAS (the
recurring debate frames) -> context5 (segment rules) -> KV (pi-5 terms) -> map_common_vi.value(): two-word composition
(Vietnamese order as it stands) -> the pi-4 chain (T3 … T11 -> context4 -> PG -> pi-3 -> pi-2 -> pi-1).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (CORE, GAP, NDE, build_part, compose, en_ru, join, lc, pi1_map_values,  # noqa: E402
                           pi2_map_values, pi3_map_values, pi4_map_values, pi4_value, pick, present, read_keywords,
                           read_pali, read_vietnamese, verify)

PARTS = ["preamble", "1-puggalakatha"]

_TT = "thực tại"
_TTCT = "thực tại chân thật"

# ---------------------------------------------------------------------------- the recurring debate frames
# Values as build_sample_vi.py / vi-zeroshot-terms.md write the formulas (the translation file is the truth).
FORMULAS = {
    # ---- answers, the thesis question
    "āmantā": "Đúng vậy",                          # Āmantā. «Đúng vậy.»
    "vattabbe": "nên nói",                         # Na hevaṃ vattabbe «Không nên nói như vậy»; tena vata re vattabbe
    "vattabbaṃ": "nên nói",
    "vattabbo": "nên gọi là",                      # "X"ti vattabbo «nên gọi là “X”»
    "hevaṃ": "như vậy",
    "nanu": "Chẳng phải",                          # Nanu …ti? «Chẳng phải … sao?»
    "tena hi": "Vậy thì",
    "suttanto": "bài kinh",                        # Attheva suttantoti? «Có bài kinh như vậy thật không?»
    "kāraṇena": "lý do",                           # tena ca kāraṇena «và vì lý do ấy»
    # ---- the rebuttal pentad
    "ājānāhi": "Hãy thừa nhận",
    "niggahaṃ": "sự bác bỏ", "niggaha": "sự bác bỏ", "niggaho": "sự bác bỏ", "niggahe": "sự bác bỏ",
    "paṭikammaṃ": "sự phản bác", "paṭikamma": "sự phản bác", "paṭikamme": "sự phản bác",
    "upanayana": "sự áp dụng", "niggamana": "sự kết luận",
    "paṭipādanā": "việc dẫn dắt lập luận",
    "dukkaṭe": "được thực hiện sai trái",          # se niggahe dukkaṭe «là sự bác bỏ được thực hiện sai trái»
    "sukate": "được thực hiện đúng đắn", "sukatā": "được thực hiện đúng đắn",
    "vata": "chắc chắn",                           # tena vata re vattabbe «thì này bạn, chắc chắn nên nói»
    "re": "này bạn",
    "micchā": "sai",                               # «Điều bạn nói ở đây là sai –» (context5: «sai lầm» where only
                                                   # «… idaṃ te micchā» «là sai lầm của bạn»)
    "paṭiññāya": "lời khẳng định",
    "hetāya": "chính" + GAP + "này",               # tattha hetāya paṭiññāya «dựa trên chính lời khẳng định này»
    "tava": "của bạn",                             # «lời khẳng định này của bạn»
    "paṭijānantaṃ": "người thừa nhận",             # «bạn, người thừa nhận như vậy»
    "paṭijānantā": "người thừa nhận",              # «chúng tôi, những người thừa nhận như vậy» («những» dropped)
    "niggahetabbe": "nên bị bác bỏ",               # context5: «nên bác bỏ» in «Không nên bác bỏ như vậy»
    "niggahetabbā": "nên bị" + GAP + "bác bỏ",     # «không nên bị bạn bác bỏ như vậy»
    "niggaṇhāma": "bác bỏ",                        # «Vậy chúng tôi bác bỏ bạn»
    "niggaṇhāsi": "bác bỏ",                        # «Vậy mà bạn bác bỏ tôi»; «lời bác bỏ mà bạn đã đưa ra»
    "suniggahito": "bị bác bỏ một cách đúng đắn",
    "suniggahitova": NDE,                          # only in the variant bracket [dị bản (Syā.): suniggahitova]
    "dunniggahite": "bị bác bỏ một cách sai trái", "dunniggahitā": "bị bác bỏ một cách sai trái",
    "niggahite": "bị bác bỏ",                      # member of dunniggahite
    "hevameva": "cũng y như vậy",                  # hevamevaṃ [khác chính tả (Syā.): hevameva] «cũng y như vậy»
    "hevamevaṃ": "cũng y như vậy",
    # ---- speaker notes [iminā lakkhaṇena sakavādīpucchā / paravādīpucchā dassitā], [ṭīkā oloketabbā]
    "lakkhaṇena": "dấu hiệu", "pucchā": "câu hỏi", "dassitā": "được trình bày",
    "vādī": "người theo học thuyết",               # member of saka- / paravādī (context5: «nói» in saccavādī …)
    "sakavādī": "người theo học thuyết của chúng ta", "paravādī": "người theo học thuyết khác",
    "ṭīkā": "Phụ chú giải", "oloketabbā": "cần tham khảo",
    # ---- section labels
    "anuloma": "chiều thuận", "anulomaṃ": "chiều thuận", "paccanīka": "chiều nghịch", "paccanīkaṃ": "chiều nghịch",
    "anulomapaccanīkaṃ": "Chiều thuận và chiều nghịch", "paccanīkānulomaṃ": "Chiều nghịch và chiều thuận",
    "anulomapañcakaṃ": "Nhóm năm phần theo chiều thuận", "paccanīkapañcakaṃ": "Nhóm năm phần theo chiều nghịch",
    "pañcakaṃ": "Nhóm năm phần", "catukkaṃ": "Nhóm bốn phần",
    "paṭhamo": "thứ nhất", "dutiyo": "thứ hai", "tatiyo": "thứ ba", "catuttho": "thứ tư", "pañcamo": "thứ năm",
    "chaṭṭho": "thứ sáu", "sattamo": "thứ bảy",
    "aṭṭhaka": "Nhóm tám",                         # Aṭṭhakaniggaho «Nhóm tám sự bác bỏ»
    "saṃkhittaṃ": "Tóm lược",                      # (Saṃkhittaṃ) «(Tóm lược)»
    "kathā": "Bàn về",                             # <X>kathā «Bàn về <X>»; closer «Phần bàn về <X> đã hoàn tất.»
    "niṭṭhitā": "đã hoàn tất",
    "anuyogo": "Chất vấn", "anuyoga": "Chất vấn",  # <X>anuyogo «Chất vấn về <X>»
    "saṃsandanaṃ": "Sự đối chiếu", "saṃsandanā": "Sự đối chiếu",
    "sodhanaṃ": "Sự làm sáng tỏ",
    # ---- saccikaṭṭha / paramattha, upalabbhati
    "upalabbhati": "được tìm thấy", "upalabbhanti": "được tìm thấy",
    "nupalabbhati": "không được tìm thấy", "nupalabbhanti": "không được tìm thấy",
    "saccikaṭṭhaparamatthena": "như một thực tại chân thật và tối hậu",
    "saccikaṭṭho": _TTCT, "saccikaṭṭha": _TTCT,
    "aṭṭho": _TT, "aṭṭha": _TT, "atthena": _TT,    # members (-aṭṭha / -attha «thực tại»)
    "paramattho": _TT + GAP + "tối hậu",           # Yo saccikaṭṭho paramattho «thực tại chân thật, tối hậu»
    "paramatthena": _TT + GAP + "tối hậu",         # member of saccikaṭṭhaparamatthena
    "parama": "tối hậu",
}

# ---------------------------------------------------------------------------- pi-5 terms (sample)
KV = {
    # ---- book frame (preamble)
    "kathāvatthu": "Các vấn đề tranh luận",        # title kept whole (as Dhammasaṅgaṇī … Puggalapaññatti)
    "vatthu": "vấn đề",
    "puggala": "người",                            # Puggalakathā «Bàn về người»
    "puggalo": "người",
    # ---- chapter 1 headings
    "suddha": "thuần túy", "suddhika": "thuần túy",
    "okāsa": "nơi chốn", "avayava": "bộ phận",     # «xét theo các bộ phận» (frame «các» dropped)
    "opamma": "phép so sánh", "catukka": "bốn cách", "naya": "phương pháp",
    "lakkhaṇa": "đặc tính",
    "paññatta": "sự định danh",                    # Paññattānuyogo «Chất vấn về sự định danh» (pi-4 paññatti)
    "gati": "cõi tái sinh", "upādā": "phụ thuộc", "purisa": "con người",
    "abhiññā": "loại hiểu biết trực tiếp",         # «các loại hiểu biết trực tiếp» («các» dropped)
    "ñātaka": "người thân", "paṭivedha": "sự thấu triệt", "paṭivedhānuyogo": "Chất vấn về sự thấu triệt",
    "sabhāga": "cùng bản chất",
    # ---- the eight refutations (5-11 … 5-16)
    "sabbattha": "ở mọi nơi", "sabbadā": "vào mọi lúc",       # adverbs (as pi-2 ajjhattaṃ «ở nơi bản thân»)
    "sabbesu": "mọi thứ",                                     # locative «trong mọi thứ» (frame «trong» dropped)
    "aññaṃ": "khác", "añño": "khác", "aññe": "khác",
    # ---- āyatana / dhātu / indriya lists (pi-3 §8 members)
    "cakkhu": "mắt", "sota": "tai", "gandha": "mùi", "itthi": "nữ tính",
    "bahūsu": "nhiều bản",                         # variant label «[dị bản (nhiều bản): …]»
    # ---- 5-46 … 5-52: «vật chất là người… người ở trong vật chất… người tách rời khỏi vật chất…»
    "aññatra": "tách rời khỏi",
    "rūpasmiṃ": "vật chất",                        # rūpasmiṃ puggalo «người ở trong vật chất» (locative frame
                                                   # «ở trong» dropped, as pi-1 Abhidhammapiṭake «Trong …»)
    # ---- Lakkhaṇayuttikathā (5-53, 5-54)
    "saṅkhato": "do điều kiện tạo thành", "asaṅkhato": "không do điều kiện tạo thành",
    "sappaccayo": "có điều kiện", "appaccayo": "không có điều kiện",
    "sassato": "trường tồn", "asassato": "không trường tồn",
    "nimitto": "dấu hiệu",                         # fragment of sanimitto / animitto (positive part)
    "sanimitto": "có dấu hiệu", "animitto": "không có dấu hiệu",
    # ---- Vacanasodhanaṃ (5-55 … 5-60): «Người được tìm thấy, vậy cái được tìm thấy có phải là người không? …
    # trong một số trường hợp là người, trong một số trường hợp không phải là người»
    "kehici": "trong một số trường hợp",
    "vijjamāno": "hiện hữu", "saṃvijjamāno": "thực sự hiện hữu",
    "sabbo": "tất cả",                             # na sabbo puggalo «không phải tất cả đều là người»
    # ---- Paññattānuyogo (5-61 … 5-68)
    "kāmī": "có dục lạc", "kāmino": "có dục lạc", "rūpī": "có hình sắc", "arūpī": "không có hình sắc",
    "dhātuyā": "cõi",                              # member of Rūpadhātuyā «ở cõi hình sắc» (realm, pi-1 / pi-2)
    "sattā": "chúng sinh",
    "koci": "ai đó",                               # atthi ca koci … «và có ai đó …»
    "jāto": "đã sinh ra",                          # «người không có hình sắc đã sinh ra» (pi-2 jāta)
    "kāyo": "thân", "sarīraṃ": "thân thể", "jīvo": "linh hồn", "jīvaṃ": "linh hồn",
    "appiyaṃ": "một không thể tách rời",           # appiyaṃ karitvā «khi xem … là một không thể tách rời»
    "karitvā": "khi xem",
    "aṭṭhe": "nghĩa",                              # ekaṭṭhe «cùng một nghĩa»
    "same": "như nhau", "sama": "ngang nhau",      # samabhāge «ngang nhau»
    "jāte": "loại",                                # tajjāte «cùng một loại»
    # ---- Gatianuyogo (5-69 …)
    "sandhāvati": "trôi lăn", "sandhāvitvāna": "sau khi trôi lăn",
    "sandhāvataṃ": "đang trôi lăn", "saṃsarataṃ": "đang luân chuyển",
    # sutta quote 5-74 «Người ấy, sau khi trôi lăn tối đa bảy lần; Đi đến tận cùng của khổ đau, nhờ diệt tận mọi
    # xiềng xích» [Tương Ưng Bộ Kinh 2.133; Kinh Phật Thuyết Như Vậy 24, cũng có trong Kinh Phật Thuyết Như Vậy]
    "khattu": "lần", "khayā": "diệt tận", "dukkhassanta": "tận cùng của khổ đau",
    "itivu": "Kinh Phật Thuyết Như Vậy", "itivuttake": "Kinh Phật Thuyết Như Vậy",
    # sutta quote 5-75 «Này các tỳ-khưu, vòng luân hồi này không có khởi điểm có thể biết được. Điểm khởi đầu không
    # được nhận ra, đối với các chúng sinh có vô minh làm chướng ngại, có khao khát làm xiềng xích …»
    "anamataggo": "không có khởi điểm có thể biết được", "bhikkhave": "tỳ-khưu",   # vocative frame «Này các» dropped
    "saṃsāro": "vòng luân hồi", "paññāyati": "được nhận ra", "nīvaraṇānaṃ": "chướng ngại",
    "saṃyojanānaṃ": "xiềng xích", "sattānaṃ": "chúng sinh",
    # ---- «Có phải có ai đó là con người rồi trở thành vị trời không?» (Atthi koci X hutvā Y hotīti?)
    "hutvā": "là" + GAP + "rồi",
    "devo": "vị trời", "manusso": "con người",
    "yakkho": "dạ-xoa", "peto": "ngạ quỷ", "nerayiko": "chúng sinh địa ngục", "tiracchānagato": "loài súc sinh",
    "oṭṭho": "lạc đà", "goṇo": "bò", "gadrabho": "lừa", "sūkaro": "heo", "mahiṃso": "trâu",
    "mahiso": NDE,                                 # only in the variant bracket [khác chính tả (…): mahiso]
    # 5-78 «… thì như vậy sẽ không có sự chết, và việc sát hại sinh mạng cũng không được tìm thấy. Nghiệp tồn tại,
    # quả của nghiệp tồn tại, quả của các nghiệp đã làm tồn tại; khi thiện và bất thiện đang trổ quả …»
    "pāṇa": "sinh mạng", "atipāto": "việc sát hại", "maraṇaṃ": "sự chết",
    "kammānaṃ": "nghiệp", "katānaṃ": "đã làm", "kammavipāko": "quả của nghiệp",
    "vipaccamāne": "đang trổ quả", "kusalākusale": "thiện và bất thiện", "akusale": "bất thiện", "kusala": "thiện",
    # the four classes (names with their head noun, pi-4 rule; vi-zeroshot-terms pi-2 wording)
    "khattiyo": "người thuộc giai cấp quý tộc", "brāhmaṇo": "bà-la-môn",
    "vesso": "người thuộc giai cấp thương nhân", "suddo": "người thuộc giai cấp lao động",
    # 5-86 / 5-90 «người bị chặt tay vẫn là người bị chặt tay, … người bị đứt gân… người có bàn tay co quắp…»
    "chinno hoti": "bị chặt" + GAP + "vẫn là",     # X-cchinno X-cchinnova hoti
    "hattha": "tay", "pāda": "chân", "kaṇṇa": "tai", "nāsa": "mũi", "aṅguli": "ngón tay", "aḷa": "ngón cái",
    "kaṇḍara": "gân", "hatthako": "bàn tay", "kuṇi": "co quắp", "phaṇa": "dính ngón",
    "kuṭṭhiyo": "người bị bệnh phong", "gaṇḍiyo": "người bị mụn nhọt", "kilāsiyo": "người bị bệnh bạch biến",
    "sosiyo": "người bị bệnh lao", "apamāriyo": "người bị động kinh",
    # 5-87 / 5-88 «bậc vào dòng, sau khi chết ở thế giới loài người và tái sinh vào thế giới chư thiên»
    "manussalokā": "thế giới loài người", "manussa": "loài người", "deva": "chư thiên",
    "lokā": "thế giới", "upapanno": "tái sinh",
    "lokā upapanno": "thế giới" + GAP + "tái sinh",   # manussalokā cuto devalokaṃ upapanno «chết ở thế giới loài người
                                                       # và tái sinh vào thế giới chư thiên» (lokā = the ablative)
    "vigato": "mất đi",                            # of avigato «không mất đi» (positive part)
    # 5-91 / 5-92 sarūpo / arūpo «cùng với vật chất» / «không có vật chất» (members)
    "rūpo": "vật chất", "vedano": "cảm giác", "sañño": "tri giác", "saṅkhāro": "tạo tác", "viññāṇo": "thức",
    # 5-94 verses «Khi các khối đang tan rã, nếu người ấy cũng tan rã; Thì thành quan điểm về sự đoạn diệt, điều mà
    # Đức Phật đã loại bỏ.»
    "khandhesu": "khối", "bhijjamānesu": "đang tan rã", "bhijjati": "tan rã", "ucchedā": "sự đoạn diệt",
    "bhavati": "thành", "buddhena": "Đức Phật", "vivajjitā": "đã loại bỏ",
    # ---- Upādāpaññattānuyogo (5-95 …): «dựa vào X mà có sự định danh Y» (X upādāya Y-assa paññatti)
    "upādāya": "dựa vào",
    "puggalassa": "người",                         # puggalassa paññatti «sự định danh người» (Vietnamese order)
    "aniccaṃ": "vô thường", "aniccā": "vô thường", "anicco": "vô thường",
    "saṅkhataṃ": "do điều kiện tạo thành", "saṅkhatā": "do điều kiện tạo thành",
    "samuppannaṃ": "sinh khởi", "samuppannā": "sinh khởi", "samuppanno": "sinh khởi",
    "paṭiccasamuppannaṃ": "sinh khởi tùy thuộc vào điều kiện", "paṭiccasamuppannā": "sinh khởi tùy thuộc vào điều kiện",
    "paṭiccasamuppanno": "sinh khởi tùy thuộc vào điều kiện",
    # X-dhamma «có bản chất X»: members khaya / vaya / virāga / nirodha / vipariṇāma = the X
    "khaya": "diệt tận", "vaya": "suy tàn", "virāga": "phai nhạt", "nirodha": "chấm dứt",
    # 5-97 «dựa vào vật chất màu xanh mà có sự định danh người màu xanh …»
    "nīlaṃ": "màu xanh", "pītaṃ": "màu vàng", "lohitaṃ": "màu đỏ", "odātaṃ": "màu trắng",
    "sanidassanaṃ": "thấy được", "anidassanaṃ": "không thấy được", "sappaṭighaṃ": "có tính va chạm",
    "appaṭighaṃ": "không có tính va chạm", "appaṭighassa": "không có tính va chạm",
    # 5-98 … 5-102 «có kết quả, có quả trổ, có kết quả đáng mong muốn, … có kết quả không pha tạp, đưa đến sự dễ
    # chịu, có quả trổ dễ chịu»
    "saphalā": "có kết quả", "saphalaṃ": "có kết quả", "saphalo": "có kết quả",
    "phalā": "kết quả", "phalaṃ": "kết quả",       # members of iṭṭhaphalā …
    "iṭṭha": "đáng mong muốn", "kanta": "đáng yêu mến", "manuñña": "đáng ưa thích", "asecanaka": "không pha tạp",
    "aniṭṭha": "không đáng mong muốn", "akanta": "không đáng yêu mến", "amanuñña": "không đáng ưa thích",
    "secanaka": "pha tạp",
    "kusalaṃ": "thiện", "akusalaṃ": "bất thiện", "kusalassa": "thiện", "akusalassa": "bất thiện",
    "abyākatassa": "không xác định về mặt đạo đức",
    # 5-104 … 5-106 «dựa vào mắt mà nên gọi là “người có mắt” … khi mắt đã chấm dứt»
    "cakkhuṃ": "mắt", "sotaṃ": "tai", "ghānaṃ": "mũi", "jivhaṃ": "lưỡi", "kāyaṃ": "thân", "manaṃ": "ý",
    "cakkhumā": "có mắt", "niruddhe": "đã chấm dứt", "niruddhāya": "đã chấm dứt",
    "micchādiṭṭhiṃ": "quan điểm sai lầm", "micchādiṭṭhiyo": "có quan điểm sai lầm",
    "satiṃ": "tỉnh thức",                          # «tỉnh thức sai lầm / đúng đắn» (pi-1 SATI_BARE)
    # 5-107 … 5-111 «dựa vào hai khối mà có sự định danh hai người»
    "dhātuṃ": "yếu tố", "dhammadhātuṃ": "yếu tố đối tượng của ý", "cakkhudhātuṃ": "yếu tố mắt",
    "bhavaṃ": "sự hiện hữu",                       # «sự hiện hữu gồm một khối» (pi-2 / pi-4 «lần hiện hữu» elsewhere)
    "ekavokāra": "gồm một khối", "catuvokāra": "gồm bốn khối", "pañcavokāra": "gồm năm khối",
    "ekavokārabhavaṃ": "sự hiện hữu gồm một khối", "catuvokārabhavaṃ": "sự hiện hữu gồm bốn khối",
    "pañcavokārabhavaṃ": "sự hiện hữu gồm năm khối",
    # 5-112 … 5-115 similes «giống như dựa vào cái cây mà có sự định danh bóng râm …»
    "rukkhaṃ": "cây", "chāyāya": "bóng râm", "anantara": "kế tiếp", "vāra": "lượt",   # [… ba lượt kế tiếp cũng vậy]
    "gāmaṃ": "làng", "gāmikassa": "dân làng", "raṭṭhaṃ": "đất nước", "rañño": "vua",
    "nigaḷo": "cái cùm", "negaḷiko": "người bị cùm", "rūpavā": "người có vật chất",
    # 5-116 / 5-117 «với mỗi tâm, người sinh ra, già đi, qua đời, chết đi, tái sinh … khi tâm thứ hai đã sinh khởi»
    "jāyati": "sinh ra", "jīyati": "già đi", "mīyati": "qua đời", "cavati": "chết đi",
    "kumārako": "bé trai", "kumārikā": "bé gái",
    "itthī": "phụ nữ", "puriso": "đàn ông", "pabbajito": "người xuất gia", "gahaṭṭho": "người tại gia",
    "citte": "tâm", "uppanne": "đã sinh khởi",
    # 5-118 … 5-120 «Chẳng phải ai thấy, thấy cái gì, thấy nhờ cái gì, người ấy thấy … sao?»
    "yo": "ai", "yaṃ": "cái gì", "yena": "nhờ cái gì",
    "suṇāti": "nghe", "ghāyati": "ngửi", "sāyati": "nếm", "phusati": "chạm", "vijānāti": "nhận biết",
    # 5-121 / 5-122 sutta quote «Này các tỳ-khưu, bằng thiên nhãn thanh tịnh, vượt quá mắt người, Ta thấy chúng sinh
    # đang chết đi, đang tái sinh, … và hiểu rõ các chúng sinh đi theo nghiệp của mình» [Trung Bộ Kinh 1.213, hơi khác
    # một chút]
    "dibbena cakkhunā": "thiên nhãn", "dibbena": "thiên", "cakkhunā": "nhãn",   # pi-2 / pi-4 «thiên nhãn»
    "visuddhena": "thanh tịnh", "atikkanta": "vượt quá", "mānusakena": "người",
    "satte": "chúng sinh", "cavamāne": "đang chết đi", "upapajjamāne": "đang tái sinh",
    "suvaṇṇe": "đẹp đẽ", "dubbaṇṇe": "xấu xí", "sugate": "cõi tốt lành", "duggate": "cõi xấu",
    "upage": "đi theo", "pajānāmi": "hiểu rõ",
    "thokaṃ": "hơi" + GAP + "một chút", "visadisaṃ": "khác",                      # thokaṃ visadisaṃ «hơi khác một chút»
    # 5-122 «… màu xanh, màu vàng, màu đỏ, màu trắng, được nhận biết bằng mắt, va chạm vào mắt …»
    "pītakaṃ": "màu vàng", "lohitakaṃ": "màu đỏ", "viññeyyaṃ": "được nhận biết", "paṭihaññati": "va chạm",
    # ---- Purisakārānuyogo (5-123 …): «người làm và người khiến làm các nghiệp tốt đẹp và xấu ác»
    "kattā": "người làm", "kāretā": "người khiến làm", "kattā kāretā": "người làm và người khiến làm",
    "kalyāṇapāpakāni": "tốt đẹp và xấu ác", "kalyāṇapāpakānaṃ": "tốt đẹp và xấu ác", "kalyāṇa": "tốt đẹp",
    "pāpakāni": "xấu ác", "pāpakānaṃ": "xấu ác", "kammāni": "nghiệp", "kammaṃ": "nghiệp",
    # 5-125 «đối với từng người như vậy, không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt vòng luân
    # chuyển, không có sự nhập Niết-bàn trọn vẹn không còn bám víu»
    "tassa tasseva": "từng người như vậy",         # frame «đối với» dropped (pi-3)
    "dukkhassa antakiriyā": "sự đi đến tận cùng của khổ đau", "vaṭṭa": "vòng luân chuyển",
    "upacchedo": "sự cắt đứt", "parinibbānaṃ": "sự nhập Niết-bàn trọn vẹn",
    "nibbānaṃ": "Niết-bàn",
    # 5-128 … 5-135 «đại địa, đại dương, núi Tu-di vua của các ngọn núi, nước, lửa, gió, cỏ, cây gỗ, cây rừng»
    "mahāpathavī": "đại địa", "mahāsamuddo": "đại dương", "samuddo": "đại dương",
    "sineru": "núi Tu-di", "pabbata": "ngọn núi", "rājā": "vua",   # sineru pabbatarājā «núi Tu-di, vua của các ngọn núi»
    "āpo": "nước", "tejo": "lửa", "vāyo": "gió",
    "tiṇa": "cỏ", "kaṭṭha": "gỗ", "vanappatayo": "cây rừng", "kaṭṭhavanappatayo": "gỗ và cây rừng",
    "aññāni": "khác",
    # 5-136 … «người cảm nhận quả của các nghiệp tốt đẹp và xấu ác» (vipākapaṭisaṃvedī)
    "paṭisaṃvedī": "người cảm nhận", "vipākapaṭisaṃvedī": "người cảm nhận quả", "vipāko": "quả",
    "nibbānassa": "Niết-bàn",
    # 5-143 … «hạnh phúc cõi trời / hạnh phúc cõi người; khổ đau ở cõi khổ / khổ đau ở địa ngục»
    "dibbaṃ": "cõi trời", "dibbassa": "cõi trời", "sukhassa": "hạnh phúc",
    "mānusakaṃ": "cõi người", "mānusakassa": "cõi người",
    "āpāyikaṃ": "ở cõi khổ", "āpāyikassa": "ở cõi khổ", "nerayikaṃ": "ở địa ngục", "nerayikassa": "ở địa ngục",
    # 5-170 … 5-179 «Có phải người ấy làm, người ấy cảm nhận không? … sự dễ chịu và sự khó chịu do tự mình làm ra
    # … tình cờ sinh khởi»
    "karoti": "làm", "karonti": "làm", "paṭisaṃvedeti": "cảm nhận", "paṭisaṃvedenti": "cảm nhận",
    "sayaṃ": "tự mình", "kataṃ": "làm ra", "kāraṃ": "làm ra", "adhicca": "tình cờ",
    "sukhadukkhaṃ": "sự dễ chịu và sự khó chịu",
    # 5-180 … «người tạo nghiệp»
    "kārako": "người tạo", "kammakārako": "người tạo nghiệp",
    "vaggo": "chương",                             # Kalyāṇavaggo paṭhamo «Chương về điều tốt, chương thứ nhất»
    # ---- Abhiññānuyogo (5-193 …): «có ai đó thi triển thần thông … nghe âm thanh bằng yếu tố tai thuộc cõi trời…
    # nhận biết tâm người khác… nhớ lại các đời sống trước… chứng nghiệm sự diệt tận các ô nhiễm»
    "vikubbati": "thi triển", "dibbāya": "thuộc cõi trời", "sotadhātuyā": "yếu tố tai",
    "dibbāya sotadhātuyā": "yếu tố tai thuộc cõi trời", "saddaṃ": "âm thanh",
    "nivāsaṃ": "đời sống",                         # pubbenivāsaṃ «các đời sống trước»
    "sacchikaroti": "chứng nghiệm",                # no «tự mình» here (pi-4 «tự mình chứng nghiệm»)
    # ---- Ñātakānuyogādi (5-197 …)
    "mātā": "mẹ", "pitā": "cha", "bhātā": "anh em trai", "bhaginī": "chị em gái",
    "kāyasakkhi": "người chứng nghiệm bằng thân",
    # ---- Saṅghānuyogo (5-206, 5-207): «bốn đôi người, tám hạng người … xuất hiện nhờ sự xuất hiện của Đức Phật»
    "purisayugā": "đôi người", "yugā": "đôi", "purisapuggalā": "hạng người",
    "pātubhavanti": "xuất hiện", "pātubhavati": "xuất hiện", "pātubhāvā": "sự xuất hiện", "buddha": "Đức Phật",
    "bhagavato": "Thế Tôn",                        # Buddhassa bhagavato «Đức Phật Thế Tôn» (pi-1 «Đức Thế Tôn»)
    "parinibbute": "đã nhập Niết-bàn trọn vẹn", "parinibbuto": "đã nhập Niết-bàn trọn vẹn",
    "ucchinno": "bị đoạn diệt",
    # ---- Saccikaṭṭhasabhāgānuyogo (5-208 …): «người không phải do điều kiện tạo thành cũng không phải không do
    # điều kiện tạo thành … ngoài cái do điều kiện tạo thành và cái không do điều kiện tạo thành, còn có một phạm
    # trù thứ ba khác»
    "neva": "không phải",                          # neva … na «không phải … cũng không phải»
    "ṭhapetvā": "ngoài", "koṭi": "phạm trù",
    "ālapana": "lời xưng hô", "nānaṃ": "khác",     # ālapanamattameva nānaṃ «chỉ khác ở lời xưng hô»
    "dhātuyo": "yếu tố",
    "uppādo": "sự sinh khởi", "vayo": "sự suy tàn", "lakkhaṇāni": "đặc tính",
    "ṭhitassa": "cái đang duy trì",                # ṭhitassa aññathattaṃ «sự đổi khác của cái đang duy trì»
    "asaṅkhatānaṃ": "không do điều kiện tạo thành", "dhammānaṃ": "hiện tượng",
    "atthatthamhi": "còn tồn tại",                 # «… còn tồn tại hay không còn tồn tại? Còn tồn tại.»
    "nissāya": "nương vào", "tiṭṭhati": "duy trì", # «Người nương vào cái gì mà duy trì?»
    # ---- 5-218 … 5-221 «có ai đó, khi đang cảm nhận cảm giác dễ chịu, hiểu rõ “tôi đang cảm nhận …”»
    "vediyamāno": "khi đang cảm nhận",             # «khi» kept (pi-4 upahacca «khi gần mạng chung»)
    # ---- 5-222 … 5-225 «đối với thân sống quán sát thân … đối với các hiện tượng sống quán sát các hiện tượng»
    "dhammesu": "hiện tượng", "vedanāsu": "cảm giác",
    # ---- 5-226 «Hãy nhìn thế gian là trống rỗng, này Mô-gha-ra-gia, luôn luôn tỉnh thức; Nhổ bỏ quan điểm về tự
    # ngã, như thế có thể vượt qua sự chết; Người nhìn thế gian như vậy, vua của sự chết không thấy được» [Kinh Tập
    # 1125; Tiểu Nghĩa Thích 88, phần giải thích câu hỏi của thanh niên Mô-gha-ra-gia]
    "suññato": "trống rỗng", "avekkhassu": "Hãy nhìn", "sadā": "luôn luôn", "sato": "tỉnh thức",
    "atta": "tự ngã", "anudiṭṭhiṃ": "quan điểm về", "ūhacca": "Nhổ bỏ",
    "ohacca": NDE, "uhacca": NDE,                  # only in the bracket [khác chính tả (Syā.): ohacca; (Ka.): uhacca]
    "maccu": "sự chết", "taro": "vượt qua", "avekkhantaṃ": "người nhìn",
    "niddesa": "phần giải thích", "māṇava": "thanh niên",
    # 5-227 / 5-228 «Nhìn cùng với vật chất hay nhìn không có vật chất? … nhìn sau khi ra bên ngoài?»
    "avekkhati": "nhìn", "saha": "cùng với", "rūpena": "vật chất",
    "nikkhamitvā": "sau khi ra", "bahiddhā": "bên ngoài",
    # ---- 5-229 … «Đức Thế Tôn là người nói sự thật, nói đúng lúc, nói điều có thật, nói đúng như thật, nói không
    # sai lệch, nói không khác đi»
    "saccavādī": "người nói sự thật", "tathavādī": "nói đúng như thật", "avitathavādī": "nói không sai lệch",
    "anaññathavādī": "nói không khác đi", "kālavādī": "nói đúng lúc", "bhūtavādī": "nói điều có thật",
    "tatha": "đúng như thật", "vitatha": "sai lệch", "aññatha": "khác đi",   # fragments of avitatha / anaññatha
    "sacca": "sự thật",
    # 5-230 «có một người, khi sinh ra trên thế gian, sinh ra vì lợi ích của nhiều người, vì hạnh phúc của nhiều
    # người, vì lòng thương xót thế gian, vì sự tốt đẹp, lợi ích và hạnh phúc của chư thiên và loài người»
    "uppajjati": "sinh ra", "uppajjamāno": "khi sinh ra", "anukampāya": "lòng thương xót", "sukhāya": "hạnh phúc",
    "manussānaṃ": "loài người",
    # 5-231 [Trung Bộ Kinh 1.356; Kinh Pháp Cú 279, trong Kinh Pháp Cú]
    "dha": "Kinh Pháp Cú", "dhammapade": "Kinh Pháp Cú", "anattā": "không phải là tự ngã",
    # 5-232 «Vị ấy không nghi ngờ, không hoài nghi rằng khi sinh khởi, chỉ có khổ đau sinh khởi; khi chấm dứt, chỉ có
    # khổ đau chấm dứt; nơi vị ấy, về điều này, có sự hiểu biết không dựa vào người khác. Này Ca-chiên-diên, đến mức
    # ấy là có quan điểm đúng đắn»
    "uppajjamānaṃ": "khi sinh khởi", "nirujjhamānaṃ": "khi chấm dứt", "nirujjhati": "chấm dứt",
    "kaṅkhati": "nghi ngờ", "vicikicchati": "hoài nghi",
    "paccaya": "dựa vào",                          # aparappaccaya «không dựa vào người khác»
    "ñāṇaṃ": "sự hiểu biết", "ettāvatā": "đến mức ấy",
    # 5-233 verses of the nun Vajirā «Vì sao ngươi cho rằng có chúng sinh, này Ma vương, ngươi đã mắc kẹt trong quan
    # điểm chăng; Đây chỉ là một đống tạo tác thuần túy … Như khi các bộ phận được ráp lại, thì có từ gọi là cỗ xe;
    # … thì có sự quy ước gọi là chúng sinh. … khổ đau duy trì rồi tan biến; Ngoài khổ đau, không gì sinh ra …»
    "bhikkhunī": "tỳ-khưu-ni", "pāpimantaṃ": "ác độc",
    "kinnu": "Vì sao", "paccesi": "cho rằng", "te": "ngươi", "diṭṭhigataṃ": "mắc kẹt trong quan điểm",
    "saṅkhāra": "tạo tác", "puñjo": "đống",
    "aṅga": "bộ phận", "sambhārā": "được ráp lại", "saddo": "từ", "ratho": "cỗ xe",
    "sammuti": "sự quy ước", "sammati": NDE,       # only in the bracket [dị bản (Syā., Kaṃ.): sammati]
    "sambhoti": "sinh ra", "veti": "tan biến", "nāññatra": "Ngoài" + GAP + "không gì",
    # 5-234 «Chẳng phải tôn giả A-nan đã nói với Đức Thế Tôn thế này sao – “… bạch Thế Tôn, người ta nói như vậy …”
    # “Này A-nan, vì trống rỗng tự ngã hay những gì thuộc về tự ngã, nên gọi là …” … cảm nhận nào sinh khởi do sự tiếp
    # xúc của mắt làm điều kiện»
    "āyasmā": "tôn giả", "āyasmā ānando": "tôn giả A-nan", "bhagavantaṃ": "Đức Thế Tôn",
    "bhante": "bạch Thế Tôn", "attena": "tự ngã", "attaniyena": "những gì thuộc về tự ngã",
    "tasmā": "nên", "yampidaṃ": "nào", "suñño": "trống rỗng",
    "paccayā": "do" + GAP + "làm điều kiện",       # Xsamphassapaccayā (pi-2)
    "vedayitaṃ": "cảm nhận",
    # 5-235 «Này các tỳ-khưu, khi có tự ngã, thì có phải sẽ có ‘cái thuộc về tự ngã của tôi’ không? … sau khi chết tôi
    # sẽ là cái ấy, thường còn, bền vững, trường tồn, có bản chất không biến đổi, tôi sẽ duy trì y như vậy ngang bằng
    # với sự vĩnh cửu – ‘… chẳng phải đây hoàn toàn là một giáo lý ngu si trọn vẹn sao’?»
    "attani": "tự ngã", "attaniyaṃ": "cái thuộc về tự ngã", "pecca": "sau khi chết",
    "nicco": "thường còn", "dhuvo": "bền vững", "sassatisamaṃ": "ngang bằng với sự vĩnh cửu",
    "tatheva": "y như vậy", "ṭhassāmi": "sẽ duy trì", "ṭhānaṃ": "nền tảng",   # diṭṭhiṭṭhānaṃ «nền tảng quan điểm»
    "kevalo": "hoàn toàn", "paripūro": "trọn vẹn", "bāla": "ngu si", "dhammo": "giáo lý",   # bāladhammo
    "saccato": "như là sự thật", "thetato": "như là điều chắc chắn",
    "saccato thetato": "như là sự thật như là điều chắc chắn",   # comma dropped (pi-1)
    # 5-236 «Này Seniya, có ba bậc đạo sư này đang có mặt, thực sự hiện hữu trên thế gian … đề ra tự ngã như là sự
    # thật, như là điều chắc chắn ngay trong đời này … Lại nữa, này Seniya …» [… giống nhau về ý nghĩa]
    "seniya": "Seniya", "satthā": "bậc đạo sư", "satthāro": "bậc đạo sư", "santo": "đang có mặt",
    "saṃvijjamānā": "thực sự hiện hữu", "paññāpeti": "đề ra", "attānaṃ": "tự ngã", "pana": "Lại nữa",
    "sambuddho": "bậc Tự Giác Ngộ", "sammāsambuddho": "bậc Tự Giác Ngộ Hoàn Toàn",
    "atthato": "về ý nghĩa",                       # atthato ekaṃ «giống nhau về ý nghĩa»
    # 5-237 / 5-238 «Có phải Đức Thế Tôn đã nói – “hũ bơ lỏng” không? … hũ dầu… hũ mật ong… hũ đường mía… hũ sữa…
    # hũ nước… đĩa nước uống… chén nước uống… bát nước uống… bữa ăn thường còn… cháo bền vững»
    "vuttaṃ": "đã nói", "vuttaṃ bhagavatā": "Đức Thế Tôn đã nói",
    "kumbho": "hũ", "sappi": "bơ lỏng", "madhu": "mật ong", "phāṇita": "đường mía", "khīra": "sữa", "udaka": "nước",
    "pānīya": "nước uống", "thālakaṃ": "đĩa", "kosakaṃ": "chén", "sarāvakaṃ": "bát",
    "nicca": "thường còn", "dhuva": "bền vững", "bhattaṃ": "bữa ăn", "yāgū": "cháo", "sassatā": "trường tồn",
    # chapter verse «Phần lặp lại của tám sự bác bỏ, sự trôi lăn, sự dựa vào; Với tâm là thứ năm, điều tốt, với thần
    # thông và việc dẫn kinh là thứ tám.»
    "peyyālā": "Phần lặp lại", "sandhāvaniyā": "sự trôi lăn", "cittena": "tâm", "sutta": "kinh",
    "āharaṇena": "việc dẫn", "pañcamaṃ": "thứ năm", "aṭṭhamaṃ": "thứ tám", "iddhi": "thần thông",
    "aññā vedanā": "cảm giác" + GAP + "là khác",  # Aññā sukhā vedanā «cảm giác dễ chịu là khác»
    # ---- sutta quotes: «Có phải Đức Thế Tôn đã nói – “có người thực hành vì lợi ích của bản thân”»
    "hitāya": "lợi ích",                           # attahitāya «vì lợi ích của bản thân» («vì» = the dative frame)
    # ---- «vật chất là khác, cảm giác là khác» (aññaṃ rūpaṃ aññā vedanā; extraction artefacts of three words)
    "aññaṃ aññā vedanā": "khác" + GAP + "cảm giác là khác",
    "aññaṃ aññe saṅkhārā": "khác" + GAP + "tạo tác là khác",
}


_HEADS = {"paññatti": "sự định danh", "paṭisaṃvedī": "người cảm nhận"}


def context5(kw, k, kws, text):
    """Segment rules of the pi-5 debate frame (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "micchā":              # verdict «… là sai –» (also «là sai lầm của bạn», idaṃ te micchā) / the path
        return "sai" if present("là sai", text) else pick(text, "sai lầm", "sai")   # factors «… sai lầm»
    if k == "sammā":               # path factors «… đúng đắn» / sammāsambuddho «bậc Tự Giác Ngộ Hoàn Toàn»
        if s & {"sammāsambuddho", "sammāsambuddhassa"}:
            return "Hoàn Toàn"
        return pick(text, "đúng đắn", "Hoàn Toàn")
    if k in ("saṅkhāre",):         # «các tạo tác» (accusative)
        return pick(text, "sự tạo tác", "tạo tác")
    if k == "kattā kāretā":        # «người làm và người khiến làm» / «người làm, người khiến làm, người cảm nhận …»
        return pick(text, "người làm và người khiến làm", "người làm người khiến làm")
    if k in ("sukha", "dukkhaṃ", "dukkha") and "sukhadukkhaṃ" in s:   # «sự dễ chịu và sự khó chịu»
        return "sự dễ chịu" if k == "sukha" else "sự khó chịu"
    if k == "pathavī":             # «đất» / member of mahāpathavī «đại địa» (no word «đất» in the segment)
        return pick(text, "đất", "địa")
    if k == "upādā" and "parinibbānaṃ" in s:       # anupādāparinibbāna «không còn bám víu» (positive part)
        return "bám víu"
    if k == "puggalānaṃ":          # «các hạng người» (pi-4) / «sự định danh hai người» (5-107 …)
        return pick(text, "hạng người", "người")
    words = k.split()
    if len(words) > 1 and words[-1] in _HEADS:     # «sự định danh <Y>», «người cảm nhận <Y>»: the head noun stands
        rest = [_single(kws, text, None)(w) for w in reversed(words[:-1])]   # before its genitive
        if all(rest) and NDE not in rest:
            v = join(text, [_HEADS[words[-1]]] + rest)
            if v:
                return v
    if k.endswith("dhammaṃ") or k.endswith("dhammā") or k.endswith("dhammo"):
        stem = {"khaya": "diệt tận", "vaya": "suy tàn", "virāga": "phai nhạt", "nirodha": "chấm dứt",
                "vipariṇāma": "biến đổi"}.get(k[: -len("dhammaṃ")] if k.endswith("dhammaṃ") else k[:-len("dhammā")])
        if stem:                   # X-dhamma «có bản chất X»; of aX-dhamma «có bản chất không X» (positive part)
            return pick(text, "có bản chất " + stem, "có bản chất" + GAP + stem) or "có bản chất " + stem
    if k == "niggahetabbe":        # «nên bị bác bỏ như vậy» / Na hevaṃ niggahetabbe «Không nên bác bỏ như vậy»
        return pick(text, "nên bị bác bỏ", "nên bác bỏ")
    if k in ("rūpaṃ", "rūpa"):     # the aggregate «vật chất» (pi-2) / the visible object «hình sắc» (pi-1)
        return pick(text, "vật chất", "hình sắc")
    if k == "saṅkhārā":            # the text writes «các tạo tác» (pi-2 «các sự tạo tác»)
        return pick(text, "sự tạo tác", "tạo tác")
    if k == "aññā":                # aññindriya / aññātāvī «hiểu biết trọn vẹn» (pi-3) / aññā vedanā «khác»
        if s & {"aññindriyaṃ", "aññātāvī", "aññātāvindriyaṃ", "aññātāvī upalabbhati"}:
            return "hiểu biết trọn vẹn"
        return "khác"
    if k == "purisa":              # purisindriya «năng lực nam tính» / Purisakārānuyogo «việc làm của con người» /
        return pick(text, "nam tính", "con người", "người")       # purisayugā «đôi người»
    if k in ("saṅkhataṃ", "asaṅkhataṃ"):           # the noun «cái (không) do điều kiện tạo thành» / the predicate
        v = ("không " if k[0] == "a" else "") + "do điều kiện tạo thành"
        return pick(text, "cái " + v, "điều " + v, v)
    if k == "vādī" and "saccavādī" in s:           # saccavādī kālavādī … «nói sự thật, nói đúng lúc …»
        return "nói"
    if k == "dhammā":              # «các hiện tượng» / the āyatana list «các đối tượng của ý» / «Giáo Pháp» (pi-4)
        return pick(text, "hiện tượng", "đối tượng của ý", "Giáo Pháp")
    if k == "sukhaṃ":              # «hạnh phúc cõi trời» / the feeling «cảm giác dễ chịu», «dễ chịu, khó chịu …»
        if "sukhaṃ vedanaṃ" in s:
            return "dễ chịu"
        return pick(text, "hạnh phúc", "dễ chịu")
    if k == "uppajjati":           # «sinh ra trên thế gian» / «chỉ có khổ đau sinh khởi», «cảm nhận nào sinh khởi»
        return pick(text, "sinh ra", "sinh khởi")
    if k == "aṭṭhaka":             # Aṭṭhakaniggaho «Nhóm tám sự bác bỏ» / verse «Phần lặp lại của tám sự bác bỏ»
        return pick(text, "Nhóm tám", "tám")
    if k == "dukkhaṃ":             # «khổ đau» (āpāyikaṃ dukkhaṃ) / the feeling «cảm giác khó chịu»
        if "dukkhaṃ vedanaṃ" in s:
            return "khó chịu"
        return pick(text, "khổ đau", "sự khó chịu", "khó chịu")
    if k == "atthi":               # «Người tồn tại» (upalabbhati / atthi pair) / existential «có»
        return pick(text, "tồn tại", "có")
    if k == "hoti":                # X hutvā Y hoti «là X rồi trở thành Y» / else no word (pi-1 / pi-4)
        return pick(text, "trở thành") or NDE
    if k == "eva" and "suttanto" in s:             # Attheva suttantoti? «Có bài kinh như vậy thật không?»
        return "thật"
    return None


def _single(kws, text, table):
    def single(w):
        k = lc(w)
        if table and k in table:
            return table[k]
        v = context5(w, k, kws, text)
        if v is not None:
            return v
        if k in FORMULAS:
            return FORMULAS[k]
        if k in KV:
            return KV[k]
        try:
            return pi4_value(w, kws, text)
        except KeyError:
            return None
    return single


def value5(kw, kws, table=None, text=None):
    """table -> FORMULAS -> context5 -> KV -> two-word composition -> the pi-4 chain."""
    k = lc(kw)
    t = text or ""
    if table and k in table:
        return table[k]
    v = context5(kw, k, kws, t)
    if v is not None:
        return v
    if k in FORMULAS:
        return FORMULAS[k]
    if k in KV:
        return KV[k]
    if " " in kw:
        v = compose(kw, kws, t, _single(kws, t, table))
        if v is not None:
            return v
    return pi4_value(kw, kws, t)


# part-specific values (everything recurring lives in FORMULAS / KV)
SAMPLE = {}

# per-segment choices (read from the segments)
OVERRIDES = {
    # ---- preamble
    "5-0": {"kathā": "tranh luận"},                          # Kathāvatthu «Các vấn đề tranh luận» (not «Bàn về»)
    # ---- 1-puggalakatha
    "5-112": {"āmantā": NDE},                                # only «( ) [(āmantā) (?) ba lượt kế tiếp cũng vậy]»: the
                                                             # word stays in Pāli inside the editorial bracket
    "5-238": {"upādāya": "sự dựa vào"},                      # chapter verse «… sự trôi lăn, sự dựa vào»
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        if part == "preamble" and k in CORE:      # the pi-1 preamble values (Namo … sammāsambuddhassa)
            return CORE[k]
        return value5(kw, kws, SAMPLE, vi.get(bid, ""))
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
        ps = []
        for i, f in ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values), (4, pi4_map_values)):
            p = [x for x, _ in f(kw).most_common(2) if x != v]
            if p:
                ps.append(f"pi{i}:{p}")
        er = en_ru(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + ("  " + " ".join(ps) if ps else "")
              + (f"  ru:{er[1]}" if er else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


_REBUTTAL = ("Hãy thừa nhận", "Còn nếu không nên nói", "Nếu ", "Nhưng nếu bạn cho rằng", "Không nên bác bỏ")


def show(part, lo, hi, with_pali=False, short=False):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            t = vi.get(bid, "")
            if short:              # the rebuttal lines repeat the thesis: print the other lines only
                t = "\n".join(l for l in t.split("\n") if not l.startswith(_REBUTTAL))
            print(f"-- VI {t}")
            er = en_ru(bid)
            out = []
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                if short:          # the fixed frame words are hidden unless missing
                    if not flag and (lc(kw) in FORMULAS or lc(kw) in ("puggalo", "puggalo upalabbhati",
                                                                         "puggalo nupalabbhati")):
                        continue
                    out.append(f"{kw}={v}{flag}")
                    continue
                e = er.get(kw, ["", ""])
                out.append(f"{kw}={v} [{e[1]}]{flag}")
            print("   " + " | ".join(out))


def look(kws):
    """the pi-1 … pi-4 map values of each keyword (exact keyword and lower-case first letter)."""
    for kw in kws:
        for k in dict.fromkeys((kw, lc(kw), kw[:1].upper() + kw[1:])):
            out = [f"pi{i}:{dict(f(k).most_common(4))}" for i, f in
                   ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values), (4, pi4_map_values)) if f(k)]
            if out:
                print(k, " ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), "pi" in sys.argv[5:], "short" in sys.argv[5:])
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p, ALLOWED)
