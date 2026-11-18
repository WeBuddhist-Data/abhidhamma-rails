"""Pāli->Vietnamese keyword map for pi-1 parts 4-02-nikkhepakandam (flood … closing Abhidhamma pairs) and
4-03-nikkhepakandam (the Suttanta pairs and their glosses).

usage: python -I -X utf8 map_4-02_4-03_vi.py              (writes both .mapped.md files and verifies them)
       python -I -X utf8 map_4-02_4-03_vi.py dump PART [miss]
                                                         (prints every distinct keyword=value with count; with
                                                          «miss» only the presence misses; writes nothing)

Importing this file writes nothing. It imports map_4-01_vi.py (and through it map_3-02_3-03_vi.py,
map_2-05_3-01_vi.py, map_2-04_vi.py, map_2-02_2-03_vi.py); none of them rewrites its output on import.
Resolution order per keyword:
  OVERRIDES[bid][kw] -> context() (4-02 / 4-03 segment rules) -> ADD402 -> the whole 4-01 resolver
  (its OVERRIDES are keyed by 4-01 segment ids, so they never fire here; then the 4-01 context(), the 2-05
  context05(), ADD401, MATRIX, «dhammā X», the 3-02/3-03 value(), T05 via ch2_value)
Conventions: vi-map-conventions.md and the earlier notes-map-*.md; new: notes-map-4-02_4-03.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, MATRIX, NDE, build_part, lc, present,  # noqa: E402
                           read_keywords, read_vietnamese, verify)

_spec = importlib.util.spec_from_file_location("map_4_01_vi", HERE / "map_4-01_vi.py")
_p401 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_p401)          # import only: its __main__ block does not run

PARTS = ("4-02-nikkhepakandam", "4-03-nikkhepakandam")

_CN = "chướng ngại"
_BV = "sự bám víu"
_TT = "sự thành thạo về"

# New keys and the 4-02 / 4-03 readings (this table precedes all the earlier tables).
ADD402 = {
    # ---------------------------------------------------------------- hindrances (^1-1158 …)
    "kāmacchandanīvaraṇaṃ": f"{_CN} ý muốn dục lạc", "byāpādanīvaraṇaṃ": f"{_CN} ác ý",
    "thinamiddhanīvaraṇaṃ": f"{_CN} uể oải và đờ đẫn",
    "uddhaccakukkuccanīvaraṇaṃ": f"{_CN} xao động và hối tiếc",
    "uddhaccanīvaraṇaṃ": f"{_CN} xao động", "kukkuccanīvaraṇaṃ": f"{_CN} hối tiếc",
    "vicikicchānīvaraṇaṃ": f"{_CN} hoài nghi", "avijjānīvaraṇaṃ": f"{_CN} vô minh",
    "avijjānīvaraṇena": f"{_CN} vô minh",
    # stems inside «chướng ngại X» have no «sự» (as the 4-01 fetter-name lists); «sự X» by override where
    # the bare word stands in the segment (^1-1161, ^1-1164, ^1-1166)
    "kāmacchanda": "ý muốn dục lạc", "byāpāda": "ác ý", "thina": "uể oải", "middha": "đờ đẫn",
    "uddhacca": "xao động", "kukkucca": "hối tiếc",
    # thina / middha strings (^1-1162, ^1-1163, ^1-1242)
    "akallatā": "sự không khỏe khoắn", "akammaññatā": "sự không dễ vận dụng",
    "olīyanā": "sự chùng xuống", "sallīyanā": "sự chùng xuống hoàn toàn", "līnaṃ": "sự co rút",
    "līyanā": "sự khởi co rút", "thinaṃ": "sự uể oải", "thiyanā": "sự khởi uể oải",
    "thiyitattaṃ": "trạng thái khởi uể oải",
    "onāho": "sự bao phủ", "antosamorodho": "sự bế tắc bên trong", "middhaṃ": "sự đờ đẫn",
    "soppaṃ": "giấc ngủ", "pacalāyikā": "sự gà gật", "supanā": "sự ngủ", "supitattaṃ": "trạng thái đã ngủ",
    # kukkucca (^1-1166)
    "kappiye": "được phép", "avajje": "không đáng chê trách", "vajja": "đáng chê trách",
    "saññitā": "tri giác",                                  # «Tri giác điều … là …»
    "kukkuccaṃ": "sự hối tiếc", "kukkuccāyanā": "sự khởi hối tiếc", "vippaṭisāro": "sự ân hận",
    "nīvaraṇāni": "chướng ngại",                            # Tāneva nīvaraṇāni «Chính những chướng ngại ấy»
    "nīvaraṇā ceva nīvaraṇiyā": f"vừa là {_CN} vừa là đối tượng của {_CN}",
    "nīvaraṇavippayuttā nīvaraṇiyā": f"không gắn liền với {_CN} nhưng là đối tượng của {_CN}",
    # ---------------------------------------------------------------- great intermediate pairs (^1-1191 …)
    "cittañca": "tâm",                                      # «Tâm; và toàn bộ / và vật chất còn lại …»
    "avasesañca": "còn lại", "avasesañca rūpaṃ": "vật chất còn lại",
    "vattabbaṃ": "nên nói",                                 # na vattabbaṃ «không nên nói»
    "sampayuttanti": "gắn liền",                            # «rằng nó “gắn liền với tâm”» (-nti has no word)
    "cittavisaṃsaṭṭhā": "không hòa lẫn với tâm",
    "dhammā cittavisaṃsaṭṭhā": "hiện tượng không hòa lẫn với tâm",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānasahabhuno":
        "hiện tượng vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm",   # commas dropped
    "cittahetukaṃ": "có tâm làm gốc rễ",                    # as 3-02 cittahetukaṃ
    # ---------------------------------------------------------------- clinging (^1-1219 …)
    "kāmupādānaṃ": f"{_BV} vào dục lạc", "kāmupādānena": f"{_BV} vào dục lạc",
    "diṭṭhupādānaṃ": f"{_BV} vào quan điểm", "sīlabbatupādānaṃ": f"{_BV} vào giới hạnh và nghi thức",
    "sīlabbatupādānañca": f"{_BV} vào giới hạnh và nghi thức",
    "attavādupādānaṃ": f"{_BV} vào học thuyết về tự ngã",
    "kāmupādānaṃ diṭṭhupādānena": f"{_BV} vào dục lạc" + GAP + f"{_BV} vào quan điểm",
    "upādānañceva": _BV,                                    # «vừa là sự bám víu vừa gắn liền với …»
    "upādānāni": _BV,                                       # Tāneva upādānāni «Chính những sự bám víu ấy»
    "upādānā ceva upādāniyā": f"vừa là {_BV} vừa là đối tượng của {_BV}",
    "upādānavippayuttā upādāniyā": f"không gắn liền với {_BV} nhưng là đối tượng của {_BV}",
    "atta": "tự ngã", "vāda": "học thuyết",                 # attavāda «học thuyết về tự ngã»
    # «natthi dinnaṃ …» / «atthi dinnaṃ …» (^1-1221, ^1-1369, ^1-1371)
    "natthi": "không có", "atthi": "có",                    # atthi of natthi = the positive part
    "hutaṃ": "cúng dường", "dukkaṭānaṃ": "làm xấu", "kammānaṃ": "nghiệp", "mātā": "mẹ", "pitā": "cha",
    "sattā": "chúng sinh", "opapātikā": "hóa sinh", "brāhmaṇā": "bà-la-môn",
    "gatā": "đi",                                           # sammaggatā «đi đúng đường»
    "paṭipannā": "thực hành", "abhiññā": "hiểu biết trực tiếp", "sacchikatvā": "chứng nghiệm",
    "pavedentīti": "tuyên bố",
    # ---------------------------------------------------------------- defilements (^1-1235 …)
    "vatthūni": "chỗ dựa", "ahirīkaṃ": "sự không biết hổ thẹn", "māno": "sự kiêu mạn", "kileso": "phiền não",
    "uddhaccaṃ anottappena": "sự xao động" + GAP + "sự không biết ghê sợ tội lỗi",
    "uddhaccaṃ ahirikena": "sự xao động" + GAP + "sự không biết hổ thẹn",
    "ahirikaṃ anottappena": "sự không biết hổ thẹn" + GAP + "sự không biết ghê sợ tội lỗi",
    "ahirikaṃ uddhaccena": "sự không biết hổ thẹn" + GAP + "sự xao động",
    "anottappaṃ uddhaccena": "sự không biết ghê sợ tội lỗi" + GAP + "sự xao động",
    "anottappaṃ ahirikena": "sự không biết ghê sợ tội lỗi" + GAP + "sự không biết hổ thẹn",
    "kilesavippayuttā saṃkilesikā": "không gắn liền với phiền não nhưng là đối tượng của phiền não",
    # ---------------------------------------------------------------- spheres (^1-1287 …)
    "avicinirayaṃ": "địa ngục Vô Gián", "pariyantaṃ": "giới hạn",
    "karitvā": "lấy" + GAP + "làm",                        # «Lấy X làm giới hạn bên dưới»
    "deve": "chư thiên", "nimmita": "Hóa", "vasavattī": "Tự Tại",   # paranimmitavasavattī «Tha Hóa Tự Tại»
    "khandha": "khối", "āyatanā": "lĩnh vực nhận biết",     # khandhadhātu āyatanā «các khối, các yếu tố, …»
    "apariyāpannā": "không nằm trong các cõi tồn tại",
    "brahma": "Phạm Thiên",                                 # brahmalokaṃ «cõi Phạm Thiên»
    "samāpannassa": "người đã chứng nhập", "upapannassa": "người đã tái sinh",
    "vihārissa": "người an trú", "diṭṭhadhamma": "ngay trong đời này",
    # ---------------------------------------------------------------- 4-03: discourse pairs (^1-1303 …)
    "sampayuttakā": "gắn liền",
    "dhammā vijjābhāgino": "hiện tượng thuộc về phía hiểu biết chân thật",
    "dhammā avijjābhāgino": "hiện tượng thuộc về phía vô minh",
    "maggesu": "con đường", "magge": "con đường", "upariṭṭhime": "cao nhất",
    "ahirīkañca": "sự không biết hổ thẹn",
    "duccaritaṃ": "hành vi xấu", "caritaṃ": "hành vi",     # of sucaritaṃ «hành vi tốt» (su- = tốt)
    "dhammā atapanīyā": "hiện tượng không gây dằn vặt",
    # naming string (^1-1313 … 1-1315)
    "saṅkhā": "sự định danh", "samaññā": "danh xưng chung", "vohāro": "cách gọi thông thường",
    "nāmakammaṃ": "sự đặt tên", "nāmadheyyaṃ": "danh hiệu", "abhilāpo": "lời diễn tả",
    "dhammā adhivacanapathā": "hiện tượng" + GAP + "phạm vi của tên gọi",      # «… đều là phạm vi của …»
    "dhammā niruttipathā": "hiện tượng" + GAP + "phạm vi của cách diễn đạt",
    "dhammā paññattipathā": "hiện tượng" + GAP + "phạm vi của khái niệm",
    "nāmaṃ": "phần tinh thần", "nāma": "phần tinh thần",
    # views (^1-1320 … 1-1327)
    "attā": "tự ngã", "ucchijjissati": "sẽ bị đoạn diệt",
    "vuccati antavā diṭṭhi": "được gọi là quan điểm về sự hữu hạn",
    "vuccati anantavā diṭṭhi": "được gọi là quan điểm về sự vô hạn",
    "vuccati pubbantānudiṭṭhi": "được gọi là quan điểm về quá khứ",
    "vuccati aparantānudiṭṭhi": "được gọi là quan điểm về tương lai",
    "uppajjati": "sinh khởi", "uppajjati diṭṭhi": "sinh khởi" + GAP + "quan điểm",
    # (dov)acassatā / mittatā (^1-1332 … 1-1335)
    "sahadhammike": "đúng theo Giáo Pháp", "vuccamāne": "được nhắc nhở",
    "dovacassāyaṃ": "sự khó bảo", "dovacassiyaṃ": "tính khó bảo", "sovacassāyaṃ": "sự dễ bảo",
    "sovacassiyaṃ": "tính dễ bảo", "gāhitā": "sự tiếp nhận", "vippaṭikūla": "ngang trái",
    "paṭikūla": "ngang trái", "vipaccanīka": "việc làm trái", "sātatā": "sự thích thú",
    "anādariyaṃ": "sự thiếu tôn trọng", "anādaratā": "thái độ thiếu tôn trọng",
    "agāravatā": "sự thiếu kính trọng", "appaṭissavatā": "sự không vâng lời", "paṭissavatā": "vâng lời",
    "sagāravatā": "sự kính trọng", "sādariyaṃ": "sự tôn trọng", "sādaratā": "thái độ tôn trọng",
    "sappaṭissavatā": "sự vâng lời",
    "puggalā": "người", "dussīlā": "phạm giới", "sutā": "học hỏi", "maccharino": "keo kiệt",
    "duppaññā": "kém trí tuệ", "sīlavanto": "giữ giới", "cāgavanto": "rộng lượng", "paññavanto": "có trí tuệ",
    "sevanā": "sự giao du", "nisevanā": "sự thường xuyên giao du", "saṃsevanā": "sự giao du mật thiết",
    "bhajanā": "sự gần gũi", "sambhajanā": "sự gần gũi mật thiết", "bhatti": "sự gắn bó",
    "sampavaṅkatā": "sự nghiêng về phía",                  # taṃsampavaṅkatā «sự nghiêng về phía họ»
    # skills (^1-1336 … 1-1345)
    "khandhā": "nhóm",                                      # āpattikkhandhā «nhóm lỗi vi phạm»
    "vuccati āpattikusalatā": f"được gọi là {_TT} các lỗi vi phạm",
    "vuccati āpattivuṭṭhānakusalatā": f"được gọi là {_TT} việc ra khỏi lỗi vi phạm",
    "vuccati samāpattikusalatā": f"được gọi là {_TT} các thành tựu thiền",
    "vuccati samāpattivuṭṭhānakusalatā": f"được gọi là {_TT} việc xuất khỏi các thành tựu thiền",
    "vuccati dhātukusalatā": f"được gọi là {_TT} các yếu tố",
    "vuccati āyatanakusalatā": f"được gọi là {_TT} các lĩnh vực nhận biết",
    "vuccati paṭiccasamuppādakusalatā": f"được gọi là {_TT} sự sinh khởi tùy thuộc vào điều kiện",
    "vuccati ṭhānakusalatā": f"được gọi là {_TT} điều có thể xảy ra",
    "vuccati aṭṭhānakusalatā": f"được gọi là {_TT} điều không thể xảy ra",
    "aṭṭhārasa": "mười tám", "sotaviññāṇa": "thức qua tai", "ghānaviññāṇa": "thức qua mũi",
    "jivhāviññāṇa": "thức qua lưỡi", "dhātūnaṃ": "yếu tố",  # «các yếu tố ấy» (3-02 «vật» is the sound list)
    # dependent arising (^1-1343)
    "paccayā": "làm điều kiện cho", "bhavo": "sự hiện hữu", "jarā": "già", "maraṇaṃ": "chết",
    "soka": "sự sầu muộn", "parideva": "sự than khóc", "upāyāsā": "sự tuyệt vọng",
    "samudayo": "sự phát sinh", "kevalassa": "toàn bộ",
    # ṭhāna / aṭṭhāna (^1-1344, ^1-1345)
    "ye ye": "nào", "uppādāya": "sự sinh khởi", "taṃ taṃ": "đó",
    # ajjava … sākhalya (^1-1346 … 1-1350)
    "avaṅkatā": "sự không cong queo", "akuṭilatā": "sự không vặn vẹo",
    "nīca": "khiêm nhường", "cittatā": "tâm",               # nīcacittatā «sự khiêm nhường của tâm»
    "khamanatā": "sự bao dung", "adhivāsanatā": "sự chịu đựng", "acaṇḍikkaṃ": "sự không hung dữ",
    "anasuropo": "sự không thô lỗ",
    "kāyiko": "bằng thân", "vācasiko": "bằng lời nói", "avītikkamo": "sự không vi phạm",
    "vītikkamo": "sự vi phạm", "soraccaṃ": "sự hiền hòa", "saṃvaro": "sự thu thúc",
    "dussilyaṃ": "sự phạm giới",
    "sākhalyaṃ": "sự hòa nhã", "aṇḍakā": "thô cộc", "kakkasā": "cay nghiệt",
    "kaṭukā": "làm" + GAP + "đau lòng",                    # parakaṭukā «làm người khác đau lòng»
    "abhisajjanī": "xúc phạm", "kodha": "sự giận dữ", "sāmantā": "gần", "saṃvattanikā": "đưa đến",
    "tathārūpiṃ": NDE,                                      # «Từ bỏ lời nói …», «nói lời nói …»: no word for «such»
    "neḷā": "không có lỗi", "kaṇṇa": "tai", "pemanīyā": "dễ mến", "hadaya": "lòng",
    "gamā": "thấm vào", "porī": "lịch sự", "kantā": "yêu mến", "manāpā": "ưa thích",
    "bhāsitā hoti": "nói", "saṇha": "dịu dàng", "sakhila": "hòa nhã", "apharusa": "không thô ác",
    # paṭisanthāra, sense doors, food (^1-1351 … 1-1355)
    "paṭisanthārā": "loại niềm nở tiếp đón", "paṭisanthārako": "niềm nở tiếp đón", "āmisa": "vật phẩm",
    "ekacco": "có người",                                   # Idhekacco «Ở đời này, có người»
    "disvā": "thấy", "sutvā": "nghe", "ghāyitvā": "ngửi", "sāyitvā": "nếm", "phusitvā": "chạm",
    "viññāya": "nhận biết", "dhammaṃ": "đối tượng của ý",
    "nimitta": "dấu hiệu tổng quát", "gāhī": "nắm giữ",     # nimittaggāhī «nắm giữ dấu hiệu tổng quát»
    "asaṃvutaṃ": "không được thu thúc", "viharantaṃ": "sống",
    "abhijjhādomanassā": "sự thèm muốn nỗi buồn", "domanassā": "nỗi buồn", "pāpakā": "xấu ác",
    "anvāssaveyyuṃ": "có thể tràn vào", "saṃvarāya": "để thu thúc", "paṭipajjati": "thực hành",
    "rakkhati": "bảo vệ", "āpajjati": "thực hiện",
    "agutti": "sự không canh giữ", "agopanā": "sự không bảo vệ", "anārakkho": "sự không che chở",
    "asaṃvaro": "sự không thu thúc", "gopanā": "sự bảo vệ", "ārakkho": "sự che chở",
    "appaṭisaṅkhā": "không suy xét", "paṭisaṅkhā": "suy xét", "ayoniso": "không đúng cách",
    "āhāraṃ": "thức ăn", "āhāreti": "ăn",
    "davāya": "để vui đùa", "madāya": "để say sưa", "maṇḍanāya": "để trang điểm", "vibhūsanāya": "để làm đẹp",
    "yāpanāya": "kéo dài", "vihiṃsā": "sự bức bách", "brahmacariya": "đời sống tu hành trong sạch",
    "anuggahāya": "để hỗ trợ", "purāṇañca": "cũ", "yātrā": "sự duy trì mạng sống",
    "anavajjatā": "sự không có lỗi", "phāsu": "thoải mái", "vihāro": "sự an trú", "cāti": NDE,
    # sati / muṭṭhasacca (^1-1356, ^1-1358)
    "muṭṭhasaccaṃ": "sự mất tỉnh thức", "asati": "sự không tỉnh thức", "ananussati": "sự không nhớ lại",
    "appaṭissati": "sự không hồi tưởng", "sammusanatā": "quên lãng",   # of asammusanatā (1-1358)
    # bhāvanābala … (^1-1361 …)
    "āsevanā": "sự thực hành", "bahulīkammaṃ": "sự làm đi làm lại", "bojjhaṅgā": "chi phần giác ngộ",
    # diṭṭhivisuddhi and the glosses (^1-1373 …)
    "kammassakata": "nghiệp là tài sản của chính mình", "anulomika": "thuận theo", "phala": "thành quả",
    "diṭṭhissa": "quan điểm", "padhānanti": "sự nỗ lực",
    "bhayaṃ": "nỗi sợ", "byādhi": "bệnh", "maraṇa": "chết", "saṃvejaniyaṃ": "đáng xúc động",
    "ṭhānanti": "điều",
    "bhikkhu": "vị tỳ-khưu", "uppannānaṃ": "đã sinh khởi", "anuppādāya": "không sinh khởi",
    "chandaṃ": "ý muốn", "janeti": "khởi lên", "vāyamati": "nỗ lực", "ārabhati": "khởi động",
    "paggaṇhāti": "nâng" + GAP + "lên", "cittaṃ paggaṇhāti": "nâng tâm lên", "padahati": "ra sức nỗ lực",
    "cittaṃ paggaṇhāti padahati": "nâng tâm lên ra sức nỗ lực",          # comma dropped
    "ṭhitiyā": "được duy trì", "asammosāya": "không bị mai một", "vepullāya": "được lớn mạnh",
    "pāripūriyā": "được hoàn thiện",
    "kusalesu dhammesūti": "hiện tượng thiện",
    "padhānasminti": "nỗ lực", "sakkacca": "chu đáo", "kiriyatā": "sự làm", "sātacca": "liên tục",
    "ṭhita": NDE,                                           # aṭṭhitakiriyatā «sự làm một cách bền bỉ»
    "olīna": "chùng xuống",                                 # anolīnavuttitā «sự hành xử không chùng xuống»
    "nivāsa": "đời sống", "cuti": "sự chết", "upapāte": "tái sinh", "āsavānaṃ": "ô nhiễm",
    "vimuttīti": "sự giải thoát", "vimuttiyo": "loại giải thoát", "adhimutti": "sự thoát ly",
    "ñāṇanti": "hiểu biết",
}

# Per-segment readings (the Vietnamese of THAT segment words the keyword differently).
OVERRIDES = {
    # hindrance stems where the bare word stands in the segment («Có sự uể oải, có sự đờ đẫn» …)
    "1-1161": {"thina": "sự uể oải", "middha": "sự đờ đẫn"},
    "1-1164": {"uddhacca": "sự xao động", "kukkucca": "sự hối tiếc"},
    "1-1166": {"uddhacca": "sự xao động"},                # «cả sự xao động này lẫn sự hối tiếc này»
    "1-1158": {"vicikicchā": "hoài nghi"},                # only «chướng ngại hoài nghi»
    "1-1176": {"vicikicchā": "hoài nghi"},
    "1-1163": {"kāyassa": "thân tinh thần"},              # kāyassa akallatā «… của thân tinh thần»
    "1-1201": {"yaṃ": "bất cứ" + GAP + "nào"},           # yaṃ vā panaññampi atthi rūpaṃ (as 3-02)
    "1-1287": {"yaṃ": NDE, "para": "Tha"},                # «Tha Hóa Tự Tại»; yaṃ: «thì …», no word
    "1-1289": {"yaṃ": NDE},
    "1-1291": {"yaṃ": NDE},
    # 4-03
    "1-1317": {"rūpaṃ": "phần vật chất", "vuccati rūpaṃ": "được gọi là phần vật chất"},
    "1-1320": {"bhava": "sự hiện hữu", "vuccati bhavadiṭṭhi": "được gọi là quan điểm về sự hiện hữu",
               "Bhavissati": "sẽ tồn tại"},
    "1-1321": {"vibhava": "sự không hiện hữu", "bhavissati": "sẽ" + GAP + "tồn tại",
               "vuccati vibhavadiṭṭhi": "được gọi là quan điểm về sự không hiện hữu"},
    "1-1326": {"yā": "điều", "ārabbha": "liên quan đến"},  # «Điều sinh khởi liên quan đến quá khứ»
    "1-1327": {"yā": "điều", "ārabbha": "liên quan đến"},
    "1-1333": {"saddhā": "có niềm tin"},                  # of assaddhā «không có niềm tin»
    "1-1335": {"saddhā": "có niềm tin"},
    "1-1334": {"sātatā": "thích thú"},                    # avipaccanīkasātatā «sự không thích thú …»
    "1-1339": {"vuṭṭhāna": "việc xuất khỏi", "vuṭṭhānakusalatā": "sự thành thạo về việc xuất khỏi"},
    "1-1343": {"rūpaṃ": "phần vật chất", "jāti": "sự sinh",
               "dukkha": "sự đau khổ"},                   # sokaparidevadukkha… «sự đau khổ» (also «khối khổ đau»)
    "1-1344": {"hetū": "nguyên nhân"},                    # hetū paccayā «là nguyên nhân, là điều kiện»
    "1-1345": {"hetū": "nguyên nhân"},
    "1-1350": {"sukhā": "êm"},                            # kaṇṇasukhā «êm tai»
    "1-1351": {"dhamma": "Giáo Pháp"},                    # dhammapaṭisanthāra «… bằng Giáo Pháp»
    "1-1352": {"rūpaṃ": "hình sắc"},
    "1-1354": {"rūpaṃ": "hình sắc"},
    "1-1353": {"santuṭṭhitā": "biết đủ"},                 # asantuṭṭhitā «sự không biết đủ»
    "1-1355": {"santuṭṭhitā": "sự biết đủ", "mattaññutā": "sự biết tiết độ"},
    "1-1356": {"pilāpanatā": "sự hời hợt", "sammusanatā": "sự quên lãng",   # the words themselves here
               "sati": "tỉnh thức", "anussati": "nhớ lại", "paṭissati": "hồi tưởng",   # a-fragments
               "saraṇatā": "ghi nhớ", "dhāraṇatā": "gìn giữ trong trí nhớ"},
    "1-1374": {"yā": NDE},                                # «“…” – nghĩa là trí tuệ …»: no word
    "1-1375": {"yo": NDE},
    "1-1376": {"jāti": "sinh"},                           # «nỗi sợ sinh» / «sinh, già, bệnh, chết»
    "1-1377": {"uppādāya": "được sinh khởi"},             # «để các hiện tượng thiện chưa sinh khởi được sinh khởi»
    "1-1378": {"yā": NDE, "kamyatā": "sự mong muốn"},     # bhiyyokamyatā «sự mong muốn nhiều hơn nữa»
    "1-1379": {"yā": NDE},
}


def _val(k):
    """Table value of a lower-cased keyword: ADD402 first, then the 4-01 tables."""
    if k in ADD402:
        return ADD402[k]
    return _p401._value(k)


def context(bid, kw, k, s, text):
    """4-02 / 4-03 segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k.startswith("vuccati ") and k not in ADD402:      # «đây được gọi là X»
        return "được gọi là " + _val(k[len("vuccati "):])
    if k in ("akusalā dhammā", "kusalā dhammā"):         # «Tất cả các hiện tượng bất thiện» (contiguous)
        whole = MATRIX[k]
        if present(whole, text):
            return whole
        return None                                       # «các hiện tượng thiện và bất thiện» (4-01 rule)
    if k == "sāsavā kusalābyākatā dhammā":               # «…, không gắn liền với …, là đối tượng của ô nhiễm»
        whole = _p401.ADD401[k]
        return whole if present(whole, text) else whole.replace(" là đối tượng", GAP + "là đối tượng")
    if k == "pahātabbahetukā" and present("có gốc rễ cần dứt bỏ", text):
        return "có gốc rễ cần dứt bỏ"                     # «không có gốc rễ cần dứt bỏ …» (^1-1272, ^1-1274)
    if k == "cetasikā" and "cittacetasikā" not in s:     # the matrix adjective (^1-1195, ^1-1196)
        return MATRIX["cetasikā"]
    if "dvedhāpatho" in s and k in _VICI:                 # vicikicchā string (as 4-01 ^1-1008 / ^1-1123)
        return _VICI[k]
    if k == "phalaṃ" and "kammānaṃ" in s:                 # natthi / atthi string: «quả và kết quả của các nghiệp …»
        return "quả"
    return None


_VICI = {"patho": "đường", "gāho": "nắm giữ", "dhamme": "Giáo Pháp"}


def resolver_for(part):
    vi = read_vietnamese(part)
    base = _p401.resolver_for(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        v = context(bid, kw, k, s, vi.get(bid, ""))
        if v is not None:
            return v
        if k in ADD402:
            return ADD402[k]
        return base(bid, kw, kws)
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
            if v == "???" or not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        print(f"{kw}={v}  [{n}]" + (f"  MISS {m} {where[(kw, v)][:6]}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], len(sys.argv) > 3)
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
