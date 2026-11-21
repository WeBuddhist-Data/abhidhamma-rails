"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 22: 22-cuddasamavaggo.

usage: python -I -X utf8 -B map_22_vi.py                    (writes 22-cuddasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_22_vi.py show lo hi [miss]   (segments lo..hi with every pair, Russian and the finished
                                                             chapters' values where they differ; writes nothing)
       python -I -X utf8 -B map_22_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_22_vi.py ctx bid word ...    (Vietnamese around each word in segment bid)
       python -I -X utf8 -B map_22_vi.py look kw ...         (values of the finished chapter tables)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context22 (segment rules) -> T22 -> context5 -> the finished
chapter tables T19 … T2 (latest first; a value counts only where it stands in this segment's Vietnamese, as map_17_vi)
-> map_5_vi.subject_predicate -> value5(kw, kws, T22, text) of map_sample_vi (FORMULAS -> KV -> two-word composition
-> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-22.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, editorial_text, en_ru, join, lc, pick, present,  # noqa: E402,F401
                           read_keywords, read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401
import map_5_vi  # noqa: E402

PART = "22-cuddasamavaggo"

_GR = "gốc rễ"                                       # mūla (T4; T12 «gốc» is a substring here)
_GRT = "gốc rễ thiện"
_GRBT = "gốc rễ bất thiện"
_NK = "nối kết"                                       # paṭisandahati «gốc rễ bất thiện nối kết với gốc rễ thiện»
_SK = "sinh khởi"
_SLV = "sáu lĩnh vực nhận biết"                       # saḷāyatana (keyword with its numeral keeps it, pi-3)
_VCCQ = "vật chất cao quý"                           # ariyarūpa
_MK = "sự mắc kẹt trong các quan điểm"               # diṭṭhigata (the text's «sự» and inner «các» kept; ch1 KV
                                                     # «mắc kẹt trong quan điểm» is another text)
_KXĐ = "không xác định về mặt đạo đức"
_CHS = "cõi hình sắc"
_CKHS = "cõi không hình sắc"
_TC = "tìm cầu"
_STTT = "sự thành tựu thiền"                         # samāpatti (the text writes «sự»; T14 «thành tựu thiền»)
_TĐ = "sự tham đắm"

T22 = {
    # ---- headings «Chương thứ mười bốn»; «(136) 1. Bàn về sự nối kết giữa thiện và bất thiện» … «(144) 9. Bàn về
    # những gì không nằm trong các cõi tồn tại»; closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS)
    "cuddasamavaggo": "Chương thứ mười bốn",       # heading and «Chương thứ mười bốn.» (as T19 ekādasamavaggo)
    "cuddasama": "thứ mười bốn",
    "vaggo": "chương",
    "paṭisandahana": "sự nối kết",
    "uppatti": "sự sinh khởi",                     # Saḷāyatanuppattikathā «… sự sinh khởi của sáu lĩnh vực nhận biết»
    "saḷāyatana": _SLV, "saḷāyatanaṃ": _SLV,
    "āyatana": "lĩnh vực nhận biết", "āyatanaṃ": "lĩnh vực nhận biết",   # members of saḷāyatana (pi-3)
    "paccaya": "điều kiện",                        # Anantarapaccayakathā «Bàn về điều kiện kế cận» (KV «dựa vào» is
    "anantara": "kế cận",                          # another text)
    "anantarapaccaya": "điều kiện kế cận",
    "ariya": "cao quý", "ariyarūpa": _VCCQ, "ariyarūpaṃ": _VCCQ,
    "anusayo": "khuynh hướng tiềm ẩn", "añño": "khác", "aññaṃ": "khác",   # «… là khác» (predicate «là» dropped)
    "vippayuttaṃ": "không gắn liền", "citta": "tâm",
    "pariyuṭṭhānaṃ": "sự ám ảnh",
    "abyākata": _KXĐ, "abyākataṃ": _KXĐ, "abyākatā": _KXĐ, "abyākate": _KXĐ,
    # ---- 5-686 … 5-690 «gốc rễ bất thiện nối kết với gốc rễ thiện … sự hướng đến… sự mong cầu nào để điều bất thiện
    # sinh khởi … điều thiện sinh khởi nơi người không hướng đến… nơi người không mong cầu … nơi người chú tâm không
    # đúng cách … tri giác về sự từ bỏ sinh khởi ngay sau tri giác về dục lạc …»
    "paṭisandahati": _NK,                          # the governing «với» dropped (pi-3 sampayutta «gắn liền»)
    "mūlaṃ": _GR, "kusalamūlaṃ": _GRT, "akusalamūlaṃ": _GRBT,
    "kusala": "thiện", "akusala": "bất thiện",
    "akusalamūlaṃ paṭisandahati": _GRBT + " " + _NK, "kusalamūlaṃ paṭisandahati": _GRT + " " + _NK,
    "uppajjati": _SK, "uppajjanti": _SK,           # (context5 «sinh ra» is jāyate in 5-692)
    "uppādāya": _SK,                               # «để điều bất thiện sinh khởi»: the dative frame «để» dropped (T15
                                                   # paṭilābhāya, pi-4 sacchikiriyāya)
    "kusalaṃ uppajjati": "điều thiện " + _SK,      # the text's «điều» kept (map_15 kusalaṃ «điều thiện»)
    "akusalaṃ uppajjati": "điều bất thiện " + _SK,
    "akusalamūlaṃ uppajjati": _GRBT + " " + _SK,
    "paṇidhi": "sự mong cầu", "paṇidahantassa": "người mong cầu",   # T17
    "āvaṭṭanā": "sự hướng đến", "āvaṭṭentassa": "người hướng đến",
    "manasikaroto": "người chú tâm",               # «nơi người chú tâm …» (T17)
    "yoniso": "đúng cách", "ayoniso": "không đúng cách",
    "anantarā": "ngay sau", "anantarā uppajjati": _SK + " ngay sau",   # Vietnamese order
    "saññā": "tri giác", "kāma": "dục lạc", "nekkhamma": "sự từ bỏ",   # «tri giác về dục lạc / về sự từ bỏ»
    "byāpāda": "ác ý", "abyāpāda": "sự không ác ý",   # own a- kept, the text's «sự»
    "vihiṃsā": "sự hãm hại", "avihiṃsā": "sự không hãm hại",
    "mettā": "lòng từ ái", "mettāya": "lòng từ ái", "karuṇā": "lòng trắc ẩn", "karuṇāya": "lòng trắc ẩn",
    "muditā": "niềm vui đồng cảm", "muditāya": "niềm vui đồng cảm",
    "upekkhā": "sự bình thản", "upekkhāya": "sự bình thản",
    "arati": "sự không hoan hỷ", "aratiyā": "sự không hoan hỷ",
    "paṭighassa": "sự ác cảm", "paṭighaṃ": "sự ác cảm",
    # 5-690 «tham đắm nơi chính sự vật nào, thì lìa tham đắm nơi chính sự vật ấy»
    "rajjati": "tham đắm", "virajjati": "lìa tham đắm",
    "vatthusmiṃ": "sự vật",                        # the locative frame «nơi» dropped («chính» = eva, no keyword)
    # ---- 5-691 / 5-692 «sáu lĩnh vực nhận biết hình thành trong bụng mẹ … người đầy đủ mọi bộ phận lớn nhỏ, có các
    # năng lực không khiếm khuyết, đi vào bụng mẹ … nhờ tâm tìm cầu sự tái sinh mà lĩnh vực mắt hình thành … bàn tay,
    # bàn chân, đầu, tai, mũi, miệng, răng … đối với người ở trong bụng mẹ, lĩnh vực mắt sinh khởi về sau … làm nghiệp
    # để có được mắt … tóc, lông, móng, răng, xương»
    "saṇṭhāti": "hình thành",                      # T15
    "mātu": "mẹ", "kucchismiṃ": "bụng", "kucchi": "bụng",   # «trong bụng mẹ» (locative frame «trong» dropped)
    "okkamati": "đi vào",
    "aṅga": "bộ phận lớn", "paccaṅgī": "nhỏ",      # sabbaṅgapaccaṅgī «đầy đủ mọi bộ phận lớn nhỏ»: aṅga «bộ phận lớn»
                                                   # (major limbs), paccaṅga «nhỏ» (minor; Russian «большие / малые
                                                   # части тела»)
    "indriyo": "năng lực",                         # ahīnindriyo «có các năng lực không khiếm khuyết» («các» dropped)
    "hīna": "khiếm khuyết",                        # of ahīna «không khiếm khuyết» (positive part)
    "cittena": "tâm", "upapattesiyena": _TC + " sự tái sinh", "upapattesiyena cittena": "tâm " + _TC + " sự tái sinh",
    "cakkhu": "mắt", "cakkhāyatanaṃ": "lĩnh vực mắt", "sota": "tai", "sotāyatanaṃ": "lĩnh vực tai",
    "ghāna": "mũi", "ghānāyatanaṃ": "lĩnh vực mũi", "jivhā": "lưỡi", "jivhāyatanaṃ": "lĩnh vực lưỡi",
    "hatthā": "bàn tay", "pādā": "bàn chân", "sīsaṃ": "đầu", "kaṇṇo": "tai", "nāsikā": "mũi", "mukhaṃ": "miệng",
    "dantā": "răng",
    "gatassa": "người ở trong",                    # mātukucchigatassa «đối với người ở trong bụng mẹ» (frame «đối với»
    "mātukucchigatassa": "người ở trong bụng mẹ",  # dropped; the genitive noun with its «người», as manasikaroto)
    "cakkhāyatanaṃ uppajjati": "lĩnh vực mắt " + _SK, "jivhāyatanaṃ uppajjati": "lĩnh vực lưỡi " + _SK,
    "paṭilābhāya": "có được",                      # cakkhupaṭilābhāya «để có được mắt» (T15; dative «để» dropped)
    "kammaṃ karoti": "làm nghiệp", "karoti": "làm",
    "kesā": "tóc", "lomā": "lông", "nakhā": "móng", "aṭṭhī": "xương", "aṭṭhī uppajjanti": "xương " + _SK,
    # 5-692 SN 1.235 «Đầu tiên có giọt phôi, từ giọt phôi có khối bọt; Từ khối bọt sinh ra miếng thịt, từ miếng thịt
    # phát sinh khối cứng; Từ khối cứng sinh ra các nhánh chi … Và những gì mẹ của người ấy ăn, thức ăn, thức uống và
    # món ăn; Nhờ đó người ấy duy trì sự sống ở đó, con người ở trong bụng mẹ»
    "kalalaṃ": "giọt phôi", "abbudaṃ": "khối bọt", "pesi": "miếng thịt", "ghano": "khối cứng",
    "pasākhā": "nhánh chi",                        # «các nhánh chi» («các» dropped)
    "jāyate": "sinh ra", "jāyanti": "sinh ra", "nibbattate": "phát sinh",
    "nibbattati": NDE,                             # only in the variant bracket [… (Pī., Ka.): nibbattati]
    "yaṃ": "những gì",                             # Yañcassa «Và những gì …» (the relative pronoun as written; not the
                                                   # plural marker of a noun)
    "bhuñjati": "ăn", "annaṃ": "thức ăn", "pānaṃ": "thức uống", "bhojanaṃ": "món ăn",
    "yāpeti": "duy trì sự sống", "naro": "con người",
    # ---- 5-693 … 5-697 «thức qua tai sinh khởi ngay sau thức qua mắt … nơi người chú tâm đến dấu hiệu của hình sắc
    # … chỉ có hình sắc làm đối tượng … tùy thuộc vào mắt và các hình sắc, sinh khởi thức qua mắt … năm loại thức sinh
    # khởi liền sau nhau … có ai đó múa, hát, chơi nhạc, vừa thấy hình sắc, vừa nghe âm thanh …»
    "cakkhuviññāṇassa": "thức qua mắt", "sotaviññāṇassa": "thức qua tai", "jivhāviññāṇassa": "thức qua lưỡi",
    "sotaviññāṇaṃ": "thức qua tai", "ghānaviññāṇaṃ": "thức qua mũi", "jivhāviññāṇaṃ": "thức qua lưỡi",
    "kāyaviññāṇaṃ": "thức qua thân",
    "cakkhuviññāṇassa anantarā": "ngay sau thức qua mắt",   # Vietnamese order (preposition before its noun)
    "jivhāviññāṇassa anantarā": "ngay sau thức qua lưỡi",
    "sotaviññāṇaṃ uppajjati": "thức qua tai " + _SK, "ghānaviññāṇaṃ uppajjati": "thức qua mũi " + _SK,
    "kāyaviññāṇaṃ uppajjati": "thức qua thân " + _SK, "cakkhuviññāṇaṃ uppajjati": "thức qua mắt " + _SK,
    "jivhāviññāṇaṃ uppajjati": "thức qua lưỡi " + _SK,
    "anantarā sotaviññāṇaṃ uppajjati": "thức qua tai " + _SK + " ngay sau",
    "anantarā ghānaviññāṇaṃ uppajjati": "thức qua mũi " + _SK + " ngay sau",
    "anantarā kāyaviññāṇaṃ uppajjati": "thức qua thân " + _SK + " ngay sau",
    "uppajjati sotaviññāṇaṃ": _SK + " thức qua tai", "uppajjati cakkhuviññāṇaṃ": _SK + " thức qua mắt",
    "uppajjati kāyaviññāṇaṃ": _SK + " thức qua thân", "uppajjati jivhāviññāṇaṃ": _SK + " thức qua lưỡi",
    "paṭicca": "tùy thuộc vào",
    "paṭicca uppajjati": "tùy thuộc vào" + GAP + _SK,   # T14
    "paṭicca uppajjati sotaviññāṇaṃ": "tùy thuộc vào" + GAP + _SK + " thức qua tai",
    "paṭicca uppajjati cakkhuviññāṇaṃ": "tùy thuộc vào" + GAP + _SK + " thức qua mắt",
    "paṭicca uppajjati kāyaviññāṇaṃ": "tùy thuộc vào" + GAP + _SK + " thức qua thân",
    "paṭicca uppajjati jivhāviññāṇaṃ": "tùy thuộc vào" + GAP + _SK + " thức qua lưỡi",
    "cakkhuṃ": "mắt", "jivhaṃ": "lưỡi",
    "rūpe": "hình sắc", "rasa": "vị", "rase": "vị",   # «các hình sắc / các vị» («các» dropped)
    "nimittaṃ": "dấu hiệu",
    "ārammaṇaṃ": "có" + GAP + "làm đối tượng",     # rūpārammaṇaṃ «có hình sắc làm đối tượng» (T13)
    "samanantarā": "liền sau", "samanantarā uppajjanti": _SK + " liền sau",   # T18
    "viññāṇā": "loại thức", "pañcaviññāṇā": "năm loại thức",   # keyword with its numeral keeps it (pi-3)
    "pañcaviññāṇā uppajjanti": "năm loại thức " + _SK,
    "pañcaviññāṇā samanantarā uppajjanti": "năm loại thức " + _SK + " liền sau",
    "naccati": "múa", "gāyati": "hát", "vādeti": "chơi nhạc",
    "suṇāti": "nghe", "ghāyati": "ngửi", "sāyati": "nếm", "phusati": "chạm",   # T15 / T18
    "saddaṃ": "âm thanh", "gandhaṃ": "mùi", "rasaṃ": "vị", "phoṭṭhabbaṃ": "vật xúc chạm", "koci": "ai đó",
    # ---- 5-698 / 5-699 «vật chất cao quý phái sinh từ các yếu tố cơ bản … là thiện … không phải là đối tượng của ô
    # nhiễm … không bị sự hiểu sai lệch nắm giữ … bất cứ vật chất nào cũng là bốn yếu tố cơ bản và vật chất phái sinh
    # từ bốn yếu tố cơ bản»
    "upādāya": "phái sinh",                        # pi-1 upādā «phái sinh» (the governing «từ» dropped; KV «dựa vào»
                                                   # is another text)
    "ariyarūpaṃ upādāya": _VCCQ + " phái sinh",
    "ariyarūpaṃ kusalaṃ": _VCCQ + " là thiện",     # inner «là» kept
    "mahābhūtānaṃ": "yếu tố cơ bản", "bhūtānaṃ": "yếu tố",   # «các yếu tố cơ bản» («các» dropped)
    "kusalaṃ": "thiện",
    # ---- 5-700 / 5-701 «khuynh hướng tiềm ẩn tham đắm dục lạc là khác, sự ám ảnh của tham đắm dục lạc là khác …
    # khi tâm thiện hay không xác định về mặt đạo đức đang diễn ra, người phàm phu nên gọi là “có khuynh hướng tiềm ẩn”
    # … “bị ám ảnh”»
    "vicikicchā": "hoài nghi",                     # first: vicikicchānusayo «khuynh hướng tiềm ẩn hoài nghi» (as T17);
                                                   # CROSSCHECK «sự hoài nghi là khác» (Aññā vicikicchā)
    "añño aññaṃ kāmarāgapariyuṭṭhānaṃ": "khác sự ám ảnh của tham đắm dục lạc là khác",   # extraction artefact of «Añño
                                                   # kāmarāgānusayo aññaṃ kāmarāgapariyuṭṭhānaṃ»: the adjacent words,
                                                   # comma dropped (pi-3 āyatanehi N-hi)
    "pariyuṭṭhito": "bị ám ảnh",                   # contiguous here (T2 «bị … ám ảnh» is another text)
    "citte": "tâm", "abyākate citte": "tâm" + GAP + _KXĐ,   # T17
    "vattamāne": "khi" + GAP + "đang diễn ra",     # participle keeps «khi» (coordinator rule; T17 = 5-556, identical
    "citte vattamāne": "khi tâm" + GAP + "đang diễn ra",   # Pāli; T19 dropped «khi»: CROSSCHECK)
    "tena hi rāgo": "Vậy thì " + _TĐ, "rāgo": _TĐ,
    # ---- 5-702 «tâm có tham đắm, tâm có sân hận, tâm có si mê… tâm bất thiện, tâm bị phiền não làm vẩn đục»
    "pariyuṭṭhānaṃ cittavippayuttaṃ": "sự ám ảnh không gắn liền với tâm",
    "rāgaṃ": "tham đắm", "dosaṃ": "sân hận", "mohaṃ": "si mê",   # members of sarāgaṃ … (T13)
    "saṃkiliṭṭhaṃ": "bị phiền não làm vẩn đục", "saṃkiliṭṭhaṃ cittaṃ": "tâm bị phiền não làm vẩn đục",
    "akusalaṃ": "bất thiện", "akusalaṃ cittaṃ": "tâm bất thiện",
    # ---- 5-703 … 5-705 «sự tham đắm cõi hình sắc tiềm ẩn trong cõi hình sắc, nằm trong cõi hình sắc … tìm cầu sự
    # thành tựu thiền, tìm cầu sự tái sinh, an trú trong hạnh phúc ngay trong đời này, đi kèm với tâm tìm cầu sự thành
    # tựu thiền … cùng sinh, hòa lẫn, gắn liền, có cùng sự sinh khởi, có cùng sự chấm dứt, có cùng chỗ dựa, có cùng đối
    # tượng … sự tham đắm âm thanh tiềm ẩn trong yếu tố âm thanh … sự tham đắm dục lạc tiềm ẩn trong cõi dục lạc»
    "anuseti": "tiềm ẩn",
    "dhātuṃ": "cõi",                               # first rūpadhātuṃ / arūpadhātuṃ «cõi»; CROSSCHECK saddadhātuṃ «yếu tố»
    "rūpadhātuṃ": _CHS, "arūpadhātuṃ": _CKHS, "kāmadhātuṃ": "cõi dục lạc", "saddadhātuṃ": "yếu tố âm thanh",
    "arūpa": _CKHS,                                # rūparāga / arūparāga «tham đắm cõi (không) hình sắc» (pi-4; rūpa:
                                                   # context22)
    "rūparāgo anuseti": _TĐ + " " + _CHS + " tiềm ẩn", "arūparāgo anuseti": _TĐ + " " + _CKHS + " tiềm ẩn",
    "kāmarāgo anuseti": _TĐ + " dục lạc tiềm ẩn", "kāmarāgo": _TĐ + " dục lạc",
    "saddarāgo": _TĐ + " âm thanh", "gandharāgo": _TĐ + " mùi", "rasarāgo": _TĐ + " vị",
    "phoṭṭhabbarāgo": _TĐ + " vật xúc chạm",
    "sadda": "âm thanh", "gandha": "mùi", "phoṭṭhabba": "vật xúc chạm",
    "samāpatti": _STTT, "upapatti": "sự tái sinh", "esiyo": _TC,
    "samāpattesiyo": _TC + " " + _STTT, "upapattesiyo": _TC + " sự tái sinh",
    "samāpattesiyena cittena": "tâm " + _TC + " " + _STTT,
    "diṭṭhadhamma": "ngay trong đời này", "sukha": "hạnh phúc",
    "vihāro": "an trú", "sukhavihāro": "an trú trong hạnh phúc",   # head first, inner «trong» kept (sample rule)
    "diṭṭhadhammasukhavihārena cittena": "tâm an trú trong hạnh phúc ngay trong đời này",
    "sahagato": "đi kèm", "saha": "cùng", "jāto": "sinh",   # sahajāto «cùng sinh» (T17 jātā)
    "saṃsaṭṭho": "hòa lẫn", "sampayutto": "gắn liền",
    "uppādo": "sự sinh khởi", "nirodho": "sự chấm dứt", "ārammaṇo": "đối tượng",   # eka- «có cùng …»
    # ---- 5-706 … 5-708 «sự mắc kẹt trong các quan điểm không xác định về mặt đạo đức … cái không xác định về mặt đạo
    # đức thuộc quả của nghiệp, cái không xác định về mặt đạo đức mang tính chức năng … sự tiếp xúc gắn liền với sự mắc
    # kẹt trong các quan điểm là bất thiện … có kết quả, có quả trổ … các lỗi mà đứng đầu là quan điểm sai lầm … một
    # trong hai cõi tái sinh – địa ngục hoặc cõi súc sinh»
    "diṭṭhigataṃ": _MK, "gataṃ": "sự mắc kẹt", "diṭṭhi": "quan điểm",
    "diṭṭhigataṃ abyākataṃ": _MK + " " + _KXĐ, "diṭṭhigataṃ akusalaṃ": _MK + " là bất thiện",   # inner «là» kept
    "tena hi diṭṭhigataṃ": "Vậy thì " + _MK,
    "kiriyā": "mang tính chức năng", "akusalo": "bất thiện",
    "phalaṃ": "kết quả",                           # aphalaṃ / saphalaṃ «không có / có kết quả» (5-707; T18)
    "vuttāni bhagavatā": "Đức Thế Tôn đã nói",     # as T17 vuttā bhagavatā (the text has no «đến» here, unlike T11)
    "vajjāni": "lỗi", "paramāni": "đứng đầu",      # micchādiṭṭhiparamāni vajjāni «các lỗi mà đứng đầu là quan điểm
                                                   # sai lầm»
    "micchādiṭṭhi": "quan điểm sai lầm",
    "akusalā": "bất thiện", "kusalā": "thiện",
    "gatīnaṃ": "cõi tái sinh", "vadāmi": "nói", "nirayaṃ": "địa ngục",   # KV gati; T11
    "yoniṃ": "cõi", "tiracchānayoniṃ": "cõi súc sinh", "tiracchāna": "súc sinh",
    # 5-708 SN 4.416 / AN 1.306 «‘Thế gian là trường tồn’ … ‘thế gian là hữu hạn’ … ‘linh hồn là khác, thân thể là
    # khác’ … ‘Như Lai còn tồn tại sau khi chết’ … bất cứ nghiệp bằng thân nào tương xứng với quan điểm, được thực hiện
    # trọn vẹn, được thọ trì … đều đưa đến điều không đáng mong muốn, không đáng yêu mến, không đáng ưa thích, đến điều
    # không lợi ích, đến khổ đau»
    "antavā": "hữu hạn", "anantavā": "vô hạn",
    "micchādiṭṭhikassa": "có quan điểm sai lầm",   # micchādiṭṭhikassa purisapuggalassa «con người có quan điểm sai lầm»
                                                   # (the head noun is purisapuggalassa)
    "yathā": "tương xứng với",                     # yathādiṭṭhi «tương xứng với quan điểm» (T17 «tùy theo» is another
                                                   # text)
    "samattaṃ": "được thực hiện trọn vẹn", "samādinnaṃ": "được thọ trì",
    "kāyakammaṃ": "nghiệp bằng thân", "vacīkammaṃ": "nghiệp bằng lời nói", "manokammaṃ": "nghiệp bằng ý",
    "kāya": "thân", "vacī": "lời nói", "mano": "ý",
    "aniṭṭhāya": "điều không đáng mong muốn",      # own a- kept; the text's «điều» (as ahitāya)
    "akantāya": "không đáng yêu mến", "amanāpāya": "không đáng ưa thích",
    "ahitāya": "điều không lợi ích", "dukkhāya": "khổ đau",
    # ---- 5-709 / 5-710 «… nền tảng thần thông, năng lực, sức mạnh, chi phần giác ngộ … người phàm phu nên gọi là “đã
    # lìa tham đắm đối với các dục lạc” … Tóm tắt của chương này – … sáu nhóm thức … tùy theo cõi mà tiềm ẩn trong
    # chính cõi ấy …»
    "dhātu": "cõi",                                # yathādhātu «tùy theo cõi» (uddāna)
    "kāyā": "nhóm", "viññāṇa": "thức",             # chaviññāṇakāyā «sáu nhóm thức»
}

OVERRIDES = {
    "5-692": {"hoti": "có"},                       # «Đầu tiên có giọt phôi, từ giọt phôi có khối bọt»: the segment's «có»
                                                   # for hoti (pi-1 hoti rule)
    "5-694": {"eva": "chỉ"},                       # first rūpārammaṇaññeva «chỉ có hình sắc làm đối tượng» (T16);
                                                   # CROSSCHECK attheva «thật», taññeva «chính»
    "5-696": {"eva": "chỉ"},                       # rasārammaṇaññeva (as 5-694)
    "5-708": {"hoti": "còn tồn tại",               # ‘hoti tathāgato paraṃ maraṇā’ «Như Lai còn tồn tại sau khi chết»
              "yaṃ": "bất cứ" + GAP + "nào"},      # yañceva kāyakammaṃ «bất cứ nghiệp bằng thân nào» (pi-2 Yaṃ kiñci)
}

ALLOWED = {
}

_DONE = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)


def _tables():
    """[(chapter, table)] of the finished chapters."""
    out = []
    for n in _DONE:
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        t = getattr(m, f"T{n}", None)
        if t:
            out.append((n, t))
    return out


_TABLES = None


def tables():
    global _TABLES
    if _TABLES is None:
        _TABLES = _tables()
    return _TABLES


def context22(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k in ("rūpa", "rūpaṃ"):     # rūparāgo «sự tham đắm cõi hình sắc» (pi-4) / the aggregate «vật chất» (ariyarūpa,
        if k == "rūpa" and s & {"rūpadhātuṃ", "rūparāgo anuseti"}:   # 5-702, 5-706) / the visible object «hình sắc»
            return _CHS                                              # (rūpanimittaṃ, 5-694; rūpañca passati, 5-697)
        return pick(text, "vật chất", "hình sắc")
    if k == "phalaṃ":              # aphalaṃ / saphalaṃ «(không) có kết quả» (5-707) / the path list «thành quả» (5-709)
        return pick(text, "kết quả", "thành quả")
    if k == "rāgo":                # «sự tham đắm» / vītarāgo «đã lìa tham đắm» (5-710 uddāna: no «sự»)
        return pick(text, _TĐ, "tham đắm")
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context22(kw, k, kws, text)
        if v is not None:
            return v
        if k in T22:
            return T22[k]
        v = context5(kw, k, kws, text)
        if v is not None:
            return v
        for n, t in reversed(tables()):            # the finished chapters (latest first) where their value stands in
            if k in t and t[k] != NDE and present(t[k], text):   # this segment
                return t[k]
        v = map_5_vi.subject_predicate(kw, kws, text)
        if v:
            return v
        return value5(kw, kws, T22, text)
    return resolve


def _prior_values(k):
    return {n: t[k] for n, t in tables() if k in t}


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
                src = " [T22]" if lc(kw) in T22 else (" [prior]" if p else "")
                print(f"   {kw}={v}{src}  [ru:{e[1]}]{ps}{flag}")


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


def ctx(bid, words, width=60):
    t = editorial_text(read_vietnamese(PART).get(bid, ""))
    low = t.lower()
    for w in words:
        pos = low.find(w.lower())
        n = 0
        while pos >= 0 and n < 3:
            print(f"[{w}] …{t[max(0, pos - width):pos + len(w) + width]}…".replace("\n", " / "))
            pos = low.find(w.lower(), pos + 1)
            n += 1
        if n == 0:
            print(f"[{w}] (absent)")


_FINISHED = ["preamble", "1-puggalakatha", "2-parihanikatha", "3-brahmacariyakatha", "4-jahatikatha",
             "5-sabbamatthitikatha", "6-atitakkhandhadikatha", "7-ekaccam-atthitikatha", "8-satipatthanakatha",
             "9-hevatthikatha", "10-dutiyavaggo", "11-tatiyavaggo", "12-catutthavaggo", "13-pancamavaggo",
             "14-chatthavaggo", "15-sattamavaggo", "16-atthamavaggo", "17-navamavaggo", "18-dasamavaggo",
             "19-ekadasamavaggo"]


def look(words):
    """Values of the finished chapter tables and of the finished pi-5 mapped files (reference only)."""
    here = pathlib.Path(__file__).resolve().parent
    want = {lc(w): w for w in words}
    found = {k: Counter() for k in want}
    for part in _FINISHED:
        f = here / f"{part}.mapped.md"
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").split("\n"):
            if not line.startswith("["):
                continue
            rest = line.partition("] ")[2]
            for pair in rest.split(", "):
                kw, _, v = pair.partition("=")
                if lc(kw) in found:
                    found[lc(kw)][(v, part.split("-")[0])] += 1
    for k, w in want.items():
        print(w, "T:", _prior_values(k), "KV:", KV.get(k), "F:", FORMULAS.get(k), "M:", dict(found[k].most_common(8)))


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["ctx"]:
        ctx(sys.argv[2], sys.argv[3:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
