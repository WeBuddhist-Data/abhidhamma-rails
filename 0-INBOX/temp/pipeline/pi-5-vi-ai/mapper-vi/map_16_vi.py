"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 16: 16-atthamavaggo.

usage: python -I -X utf8 -B map_16_vi.py                    (writes 16-atthamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_16_vi.py show lo hi [miss]   (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 -B map_16_vi.py dump [miss]         (every distinct keyword=value; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context16 (segment rules) -> T16 -> map_5_vi.subject_predicate ->
value5(kw, kws, PRIOR, text) of map_sample_vi, where PRIOR = the finished chapter tables (T2 … T12, T14) under T16.
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-16.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401
import map_5_vi  # noqa: E402

PART = "16-atthamavaggo"

_HH = "sự hiện hữu"
_KG = _HH + " trong khoảng giữa"                    # antarābhava
_DL = _HH + " ở cõi dục lạc"                        # kāmabhava («ở cõi»: the realm, as pi-1 rūpūpapattiyā)
_HS = _HH + " ở cõi hình sắc"                       # rūpabhava
_KHS = _HH + " ở cõi không hình sắc"                # arūpabhava
_ND = "nghiệp đi đến "                              # X-ūpagaṃ kammaṃ (T14 ākāsānañcāyatanūpagaṃ kammaṃ)
_LQ = "liên quan đến chúng"                         # tappaṭisaññutta / tappaṭisaṃyutta
_PL = "chỉ năm lĩnh vực nhận biết là các dục lạc"   # pañcevāyatanā kāmā (numeral kept with its keyword, pi-3)
_DS = "do" + GAP + "sinh ra"                        # samuṭṭhita (pi-1 samuṭṭhāna «do … sinh ra»)
_TT = "tâm tìm cầu sự tái sinh"                     # upapattesiya citta (T12)

T16 = {
    # ---- headings «Chương thứ tám», «(73) 1. Bàn về sáu cõi tái sinh» … «(83) 11. Bàn về nghiệp làm nguyên nhân»;
    # closers «Phần bàn về … đã hoàn tất.» (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS)
    "aṭṭhamavaggo": "Chương thứ tám",              # heading and «Chương thứ tám.» (line-initial capital kept, map_14)
    "aṭṭhama": "thứ tám", "vaggo": "chương",
    "gatiyo": "cõi tái sinh",                      # «sáu / năm cõi tái sinh» (numeral dropped; T12 «hướng đi» is
                                                   # dveva gatiyo)
    "antarā": "trong khoảng giữa",                 # pi-4 antarā (antarāparinibbāyī)
    "antarābhava": _KG, "antarābhavo": _KG,
    "guṇa": "loại", "kāmaguṇa": "loại dục lạc",    # «Bàn về các loại dục lạc» («các» dropped)
    "kāmakathā": "Bàn về các dục lạc",             # inner «các» kept (pi-1 dhammavicayo)
    "kāmā": "dục lạc",                             # «là các dục lạc» («các» dropped)
    "rūpa": "hình sắc", "arūpa": "không hình sắc", "kāma": "dục lạc",   # members of X-dhātu (dhātu «cõi»); «cõi X»
                                                   # in X-bhava / X-ūpaga (OVERRIDES, as pi-1 / pi-4 rūpa «cõi …»)
    "dhātuyā": "cõi", "rūpadhātuyā": "cõi hình sắc",   # the realm (KV dhātuyā; T10 «yếu tố» is the element)
    "rūpadhātu": "cõi hình sắc", "rūpadhātū": "cõi hình sắc",
    "arūpadhātu": "cõi không hình sắc", "arūpadhātū": "cõi không hình sắc",
    "kāmadhātu": "cõi dục lạc", "kāmadhātū": "cõi dục lạc", "kāmadhātuyā": "cõi dục lạc", "dhātū": "cõi",
    "arūpe": "cõi không hình sắc", "arūpesu": "cõi không hình sắc",   # «trong (các) cõi không hình sắc»
    "rūpaṃ kamma": "vật chất là nghiệp",           # heading Rūpaṃ kammantikathā «… việc cho rằng vật chất là nghiệp»
    # ---- 5-503 / 5-504 «có năm cõi tái sinh – địa ngục, cõi súc sinh, cõi ngạ quỷ, loài người, chư thiên … các
    # a-tu-la Ka-la-kan-chi-ka có cùng dung sắc, cùng sự hưởng thụ, cùng thức ăn, cùng tuổi thọ với các ngạ quỷ, cưới
    # gả với các ngạ quỷ … hội chúng của Vê-pa-chít-ti là chư thiên trước kia … có nhóm a-tu-la»
    "nirayo": "địa ngục", "tiracchāna": "súc sinh", "tiracchānayoni": "cõi súc sinh",
    "vuttā": "đã nói",
    "asurā": "a-tu-la", "asura": "a-tu-la",
    "vaṇṇā": "dung sắc", "bhogā": "sự hưởng thụ", "āhārā": "thức ăn", "āyukā": "tuổi thọ",
    "āvāha": "cưới", "vivāhaṃ": "gả",              # āvāhavivāhaṃ «cưới gả»
    "vepacitti": "Vê-pa-chít-ti", "parisā": "hội chúng", "pubba": "trước kia",
    # ---- 5-505 … 5-509 Antarābhavakathā «sự hiện hữu ở cõi dục lạc … giữa sự hiện hữu ở cõi dục lạc và sự hiện hữu
    # ở cõi hình sắc … đó là cách sinh thứ năm, đó là cõi tái sinh thứ sáu, đó là chỗ trú của thức thứ tám, đó là nơi
    # cư trú của chúng sinh thứ mười … nghiệp đi đến … người tạo nghiệp có quả không gián đoạn … người đi đến cõi chúng
    # sinh Vô Tưởng … người nhập Niết-bàn trọn vẹn trong khoảng giữa»
    "kāmabhavassa rūpabhavassa": _DL + " và " + _HS,      # inner «và» kept (coordinator rule)
    "rūpabhavassa arūpabhavassa": _HS + " và " + _KHS,
    "kāmabhavassa antare antarābhavo": "giữa " + _DL + GAP + _KG,
    "pañcamī": "thứ năm", "chaṭṭhamī": "thứ sáu", "aṭṭhamī": "thứ tám", "dasamo": "thứ mười",
    "antarābhavo bhavo": _KG + " là " + _HH,       # inner «là» kept (sample)
    "kāmabhavo bhavo": _DL + " là " + _HH, "rūpabhavo bhavo": _HS + " là " + _HH,
    "rūpabhavo": _HS, "arūpabhavo": _KHS,
    "antarābhavūpagaṃ": "đi đến " + _KG, "antarābhavūpagā": "đi đến " + _KG,
    "antarābhavūpagaṃ kammaṃ": _ND + _KG, "kāmabhavūpagaṃ kammaṃ": _ND + _DL,
    "kāmaguṇūpagaṃ kammaṃ": _ND + "các loại dục lạc",   # inner «các» kept
    "rūpūpagaṃ kammaṃ": _ND + "vật chất", "vedanūpagaṃ kammaṃ": _ND + "cảm giác",
    "ānantariyassa": "tạo nghiệp có quả không gián đoạn",
    "upagassa": "đi đến", "niraya": "địa ngục", "nirayūpagassa puggalassa": "người đi đến địa ngục",
    "sañña": "Tưởng",                              # of asaññasatta «chúng sinh Vô Tưởng» (positive part, pi-1)
    "antarāparinibbāyī puggalo": "người nhập Niết-bàn trọn vẹn trong khoảng giữa",   # head noun first (pi-4)
    # ---- 5-510 … 5-514 Kāmaguṇakathā / Kāmakathā «chỉ năm loại dục lạc là cõi dục lạc … ý muốn liên quan đến chúng …
    # Năm loại dục lạc ở đời, cùng với ý là thứ sáu, đã được tuyên bố … trong giới luật của bậc thánh … Sự tham đắm do
    # tư duy là dục lạc của con người, Những thứ muôn màu ở đời không phải là các dục lạc; … Những thứ muôn màu vẫn
    # đứng vững y như vậy ở đời; Thế nên, ở đây người trí dẹp bỏ ý muốn» [Tăng Chi Bộ Kinh 6.63, trong Kinh Thấu Triệt]
    "eva": "chỉ",                                  # Pañceva «chỉ năm» (context16: «thật» in Attheva suttanto)
    "tappaṭisaññutto": _LQ, "tappaṭisaṃyutto": _LQ,
    "tappaṭisaññutto chando": "ý muốn " + _LQ, "tappaṭisaṃyutto chando": "ý muốn " + _LQ,
    "tappaṭisaññutto saṅkappo": "tư duy " + _LQ, "tappaṭisaṃyutto saṅkappo": "tư duy " + _LQ,
    "tappaṭisaññuttaṃ somanassaṃ": "niềm vui " + _LQ, "tappaṭisaṃyuttaṃ somanassaṃ": "niềm vui " + _LQ,
    "chaṭṭhā": "thứ sáu",                          # manocchaṭṭhā «cùng với ý là thứ sáu»
    "paveditā": "đã được tuyên bố",
    "uppajjanti": "xuất hiện",                     # notes-map-3 (Buddhas, sāvakayugaṃ)
    "sambuddhā uppajjanti": "bậc Tự Giác Ngộ" + GAP + "xuất hiện",   # of sammāsambuddhā uppajjanti
    "paccekasambuddhā uppajjanti": "bậc Độc Giác xuất hiện",
    "rūpā": "hình sắc",                            # Cakkhuviññeyyā rūpā «Các hình sắc được nhận biết bằng mắt»
    "āyatanā": "lĩnh vực nhận biết", "pañcevāyatanā kāmā": _PL,
    "ariyassa": "bậc thánh", "purisassa": "con người", "saṅkappa": "tư duy",   # saṅkapparāgo «sự tham đắm do tư duy»
    "citrāni": "thứ muôn màu",                     # «Những thứ muôn màu» («Những» dropped)
    "tiṭṭhanti": "đứng vững", "vinayanti": "dẹp bỏ",
    "nibbedhika": "Thấu Triệt",                    # nibbedhikasutte «trong Kinh Thấu Triệt»
    # ---- 5-515 … 5-518 Rūpadhātukathā / Arūpadhātukathā «các hiện tượng thuộc vật chất là cõi hình sắc … chính cõi
    # dục lạc ấy, cõi ấy là cõi hình sắc … người được trang bị sự hiện hữu ở cõi dục lạc thì được trang bị hai sự hiện
    # hữu – sự hiện hữu ở cõi dục lạc và sự hiện hữu ở cõi hình sắc»
    "rūpaṃ bhavo": "vật chất là " + _HH,
    "bhavena": _HH, "bhavehi": _HH,                # «hai / ba sự hiện hữu» (numeral dropped)
    "kāmabhavena samannāgato": "được trang bị " + _DL,   # Vietnamese order
    "kāmabhavena rūpabhavena": _DL + " và " + _HS, "kāmabhavena arūpabhavena": _DL + " và " + _KHS,
    "rūpabhavena arūpabhavena": _HS + " và " + _KHS,
    "kāmadhātu rūpadhātū": "cõi dục lạc" + GAP + "cõi hình sắc",       # «chính cõi dục lạc ấy, cõi ấy là cõi …»
    "kāmadhātu arūpadhātū": "cõi dục lạc" + GAP + "cõi không hình sắc",
    # ---- 5-519 … 5-523 Rūpadhātuyāāyatanakathā «sự tồn tại cá nhân gồm sáu lĩnh vực nhận biết … mùi rễ cây, mùi lõi
    # cây, mùi vỏ cây, mùi lá, mùi hoa, mùi trái cây, mùi tanh, mùi ôi thiu, mùi thơm, mùi hôi … vị rễ cây, vị thân
    # cây … vị chua, vị ngọt, vị đắng, vị cay, vị mặn, vị kiềm, vị chua nhẹ, vị chát, vị ngon, vị không ngon … cái
    # cứng, cái mềm, cái mịn, cái thô ráp, cái mà khi tiếp xúc thì dễ chịu, … khó chịu, cái nặng, cái nhẹ … dấu hiệu
    # của mũi»
    "āyataniko": "gồm" + GAP + "lĩnh vực nhận biết",   # saḷāyataniko «gồm sáu lĩnh vực nhận biết» (pi-3 vokāra)
    "bhāvo": "sự tồn tại", "attabhāvo": "sự tồn tại cá nhân",
    "gandha": "mùi",                               # (T10 «hương thơm» is the perfume)
    "dhamma": "đối tượng của ý",                   # dhammāyatana (pi-1 stem rule)
    "mūla": "rễ cây", "sāra": "lõi cây", "taca": "vỏ cây", "patta": "lá", "phala": "trái cây",
    "āma": "tanh", "su": "thơm", "du": "hôi",      # āmagandho / sugandho / duggandho «mùi tanh / thơm / hôi»
    "khāriyaṃ": "vị kiềm", "loṇiyaṃ": "vị mặn", "pharusaṃ": "cái thô ráp",
    # ---- 5-524 … 5-526 «sự hiện hữu ở cõi hình sắc, cõi tái sinh ở cõi hình sắc … sự có được sự tồn tại cá nhân ở cõi
    # không hình sắc … [dị bản (mọi bản): arūpadhātuyā] … lối thoát khỏi vật chất là cõi không hình sắc … lối thoát
    # khỏi các dục lạc là sự từ bỏ … có các ô nhiễm trong những gì không phải là đối tượng của ô nhiễm»
    "arūpattabhāvapaṭilābho": "sự có được sự tồn tại cá nhân ở cõi không hình sắc",
    "sabbattha": "mọi bản",                        # variant label «dị bản (mọi bản)» (sample bahūsu «nhiều bản»)
    "nissaraṇaṃ": "lối thoát", "rūpānaṃ": "vật chất", "nekkhammaṃ": "sự từ bỏ",
    "anāsavesu": "không phải là đối tượng của ô nhiễm",   # pi-1 bare form («trong những gì …» = frame)
    # ---- 5-527 … 5-538 Rūpaṃ kammantikathā «nghiệp bằng thân dưới dạng vật chất do tâm thiện sinh ra là thiện …
    # có đối tượng, nó có sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong ước, sự mong cầu … niềm
    # tin… sự tinh tấn… sự tỉnh thức… sự định tâm… trí tuệ … không gắn liền với sự tiếp xúc … đồ bất tịnh, nước mắt,
    # máu, mồ hôi … vật chất vừa là thiện vừa là bất thiện … thân là vật chất, nghiệp bằng thân là vật chất»
    "kusalena": "thiện", "kusalena cittena": "tâm thiện",
    "akusalena": "bất thiện", "akusalena cittena": "tâm bất thiện",
    "samuṭṭhitaṃ": _DS, "samuṭṭhito": _DS,
    "samuṭṭhitaṃ rūpaṃ": "vật chất" + GAP + _DS,  # «bất cứ vật chất nào do tâm thiện sinh ra»
    "ārammaṇaṃ": "có đối tượng",                   # of sārammaṇaṃ / anārammaṇaṃ (pi-2 / pi-3 fragment rule)
    "sati": "sự tỉnh thức", "samādhi": "sự định tâm",   # the factors as the text writes them (pi-1)
    "phassa": "sự tiếp xúc",                       # phassavippayuttaṃ «không gắn liền với sự tiếp xúc»
    "phassavippayuttaṃ": "không gắn liền với sự tiếp xúc",
    "vicikicchā": "sự hoài nghi",
    "asuci": "đồ bất tịnh",                        # the text's «đồ» (T10 «bất tịnh» in «sự xuất tinh bất tịnh»)
    "lohitaṃ": "máu",                              # (KV «màu đỏ» is the colour)
    # ---- 5-539 sutta quotes «Ta nói chủ ý là nghiệp; sau khi có chủ ý, người ta làm nghiệp bằng thân, bằng lời nói,
    # bằng ý … chủ ý bằng thân gồm ba loại là nghiệp bằng thân bất thiện, đưa đến sự khó chịu … kẻ rồ dại Sa-mít-thi …
    # du sĩ Ba-liên-phất … trả lời như thế này – ‘Này hiền giả Ba-liên-phất, sau khi làm nghiệp có chủ ý … được cảm
    # nhận là dễ chịu, người ấy cảm nhận sự dễ chịu …’, thì khi trả lời như vậy, … sẽ trả lời một cách đúng đắn»
    "cetayitvā": "sau khi có chủ ý",               # gerunds «sau khi» (map 4)
    "kammaṃ karoti kāyena": "làm nghiệp bằng thân",   # inner «bằng» kept
    "vacīsañcetanā": "chủ ý bằng lời nói",
    "tividhā": "gồm ba loại", "catubbidhā": "gồm bốn loại",
    "sukhudrayaṃ": "đưa đến sự dễ chịu",
    "samiddhi": "Sa-mít-thi", "mogha": "rồ dại", "puriso": "kẻ",   # moghapuriso «kẻ rồ dại»
    "paribbājakassa": "du sĩ", "potaliputtassa": NDE,   # only in the bracket [dị bản (…): potaliputtassa]
    "byākareyya": "trả lời",                       # optative: the bare verb (coordinator rule)
    "byākaramāno": "khi trả lời",                  # participle keeps «khi»
    "āvuso pāṭaliputta": "hiền giả Ba-liên-phất",
    "sañcetaniyaṃ": "có chủ ý", "sañcetaniyaṃ kammaṃ": "nghiệp có chủ ý",
    "vedaniyaṃ": "được cảm nhận", "sukhavedaniyaṃ": "được cảm nhận là dễ chịu",
    "dukkhavedaniyaṃ": "được cảm nhận là khó chịu",
    "vedayati": "cảm nhận",
    # ---- 5-540 … 5-545 Jīvitindriyakathā «năng lực sống thuộc vật chất … tuổi thọ, sự tồn tại, sự tiếp diễn, sự kéo
    # dài, sự vận động, sự tiến triển, sự gìn giữ của những hiện tượng thuộc vật chất … chúng sinh Vô Tưởng … năng lực
    # sống do tâm tìm cầu sự tái sinh sinh ra, khi tâm tìm cầu sự tái sinh đang tan rã, thì tan rã một phần … không
    # còn sót lại … sống bằng hai sự sống, qua đời bằng hai sự chết»
    "rūpajīvita": "sống thuộc vật chất", "arūpajīvita": "sống phi vật chất",   # members of (a)rūpajīvitindriyaṃ
    "vattanā pālanā": "sự tiến triển sự gìn giữ",  # comma dropped (pi-3)
    "rūpīnaṃ arūpīnaṃ": "thuộc vật chất và phi vật chất",   # inner «và» kept
    "āyu": "tuổi thọ",
    "khandha": "khối", "saṅkhārakkhandha": "khối tạo tác",
    "upapattesiye": "tìm cầu sự tái sinh", "upapattesiye citte": _TT,
    "upapattesiyena cittena bhijjati": _TT + GAP + "tan rã",
    "bhijjamāne": "khi" + GAP + "đang tan rã",     # participle keeps «khi» (loc. abs.)
    "citte bhijjamāne": "khi tâm" + GAP + "đang tan rã",
    "upapattesiye citte bhijjamāne": "khi " + _TT + " đang tan rã",
    "samuṭṭhitaṃ jīvitindriyaṃ": "năng lực sống " + _DS, "samuṭṭhito phasso": "sự tiếp xúc " + _DS,
    "avaseso": "còn sót lại",                      # of anavaseso «không còn sót lại» (positive part, pi-4)
    "jīvati": "sống", "jīvitehi": "sự sống", "maraṇehi": "sự chết",
    # ---- 5-546 Kammahetukathā «do nghiệp sát hại sinh mạng … lấy của không được cho … có hành vi sai trái trong các
    # dục lạc … nói dối … nói lời chia rẽ … nói lời thô ác … nói lời phù phiếm … giết mẹ … làm chảy máu … chia rẽ Tăng
    # đoàn … vu khống các bậc A-la-hán … tự mình chứng nghiệm trạng thái A-la-hán» + the uddāna
    "pāṇātipātakammassa": "nghiệp sát hại sinh mạng", "pāṇātipāta": "sát hại sinh mạng", "atipāta": "sát hại",
    "ādāna": "lấy",                                # adinnādāna «lấy của không được cho»
    "micchācāra": "hành vi sai trái", "vāda": "nói",   # musāvāda «nói dối» (ch2 vāda NDE: Vādayutti)
    "palāpa": "nói lời",                           # samphappalāpa «nói lời phù phiếm» (ch3 palāpino)
    "mātu": "mẹ", "uppāda": "làm chảy",            # ruhiruppāda «làm chảy máu» (ch3 / ch10 uppādako «kẻ làm chảy»)
    "bheda": "chia rẽ",                            # saṅghabheda «chia rẽ Tăng đoàn»
    "abbhācikkhati": "vu khống", "abbhācikkhana": "vu khống",
    "sacchikaronti": "tự mình chứng nghiệm",
    "tathā": "cũng vậy", "padesu": "từ",           # only in the translated note of the variant bracket (ALLOWED)
    "jīvitaṃ": "sự sống",
}

_FINISHED = (7, 6, 5, 4, 2, 3, 8, 9, 10, 11, 12, 14)
PRIOR = {}
for _n in _FINISHED:
    PRIOR.update(getattr(importlib.import_module(f"map_{_n}_vi"), f"T{_n}", {}))
PRIOR.update(T16)
PRIOR.pop("rūpaṃ", None)       # context5 decides «vật chất» / «hình sắc» by the segment (also inside compositions)


def context16(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "rūpaṃ":               # the aggregate «vật chất» / taṃ rūpaṃ passati «thấy hình sắc ấy» (5-521)
        return pick(text, "vật chất", "hình sắc")
    if k == "dhātu":               # the element «yếu tố đất …» / the realm «cõi hình sắc …»
        return "yếu tố" if "pathavīdhātu" in s else "cõi"
    if k == "eva":                 # Pañceva «chỉ năm» / Attheva suttanto «thật» (where the segment has no «chỉ»)
        return "chỉ" if present("chỉ", text) else "thật"
    if k == "saṅkhāra":            # khối tạo tác (pi-1) / a- / sasaṅkhāraparinibbāyī «sự thúc đẩy» (pi-4)
        return "tạo tác" if "saṅkhārakkhandha" in s else "sự thúc đẩy"
    if k == "kāyo":                # asurakāyo «nhóm a-tu-la» / manussānaṃ kāyo «thân của loài người»
        return "nhóm" if "asura" in s else "thân"
    return None


_CR = {"rūpa": "cõi hình sắc", "arūpa": "cõi không hình sắc", "kāma": "cõi dục lạc"}   # members of X-bhava, X-ūpaga
_TVC = {"rūpa": "thuộc vật chất", "arūpa": "phi vật chất"}                            # (a)rūpajīvitindriya

OVERRIDES = {
    "5-16-8-1-0": {"rūpa": "vật chất"},            # Arūpe rūpakathā «Bàn về vật chất trong cõi không hình sắc»
    "5-503": {"yoni": "cõi"},                      # tiracchānayoni «cõi súc sinh»
    "5-505": dict(_CR),                            # «sự hiện hữu ở cõi dục lạc / hình sắc / không hình sắc»
    "5-507": dict(_CR),
    "5-508": {"arūpa": "cõi không hình sắc"},      # arūpūpagassa «người đi đến cõi không hình sắc»
    "5-514": {"vinaye": "giới luật"},
    "5-517": {"rūpino dhammā": "hiện tượng" + GAP + "vật chất"},   # of Arūpino dhammā «hiện tượng phi vật chất»
                                                   # (positive part)              # «trong giới luật của bậc thánh» (lower case as written)
    "5-522": {"khandha": "thân cây",               # khandharaso «vị thân cây»
              "dukkha": "khó chịu"},               # dukkhasamphassaṃ «cái mà khi tiếp xúc thì khó chịu»
    "5-526": {"rūpa": "vật chất"},                 # Arūpe rūpakathā closer «vật chất trong cõi không hình sắc»
    "5-539": {"katvā": "sau khi làm",              # kammaṃ katvā «sau khi làm nghiệp» (gerund; ch7 «vì cho rằng»)
              "sammā": "một cách đúng đắn",        # sammā byākaramāno «trả lời một cách đúng đắn»
              "dukkha": "sự khó chịu",             # dukkhudrayaṃ «đưa đến sự khó chịu» (first; dukkhavedaniyaṃ «được
                                                   # cảm nhận là khó chịu»: CROSSCHECK)
              "dukkhaṃ": "sự khó chịu"},           # dukkhaṃ so vedayati «người ấy cảm nhận sự khó chịu»
    "5-540": {"rūpa": _TVC["rūpa"],
              "ṭhiti": "sự tồn tại"},              # the jīvita string (pi-1 context rule)
    "5-541": dict(_TVC),
    "5-542": {"rūpa": _TVC["rūpa"]},
    "5-543": {"rūpa": _TVC["rūpa"]},
    "5-545": {"vattabbe": NDE},                    # only in the bracket [dị bản (…): na hevaṃ vattabbe]
}

ALLOWED = {
    ("5-546", "tathā"): "«cũng vậy ở các từ pitughāta-, arahantaghātakammassa» (tathā … padesu) is the translated "
                        "note after the colon of the variant bracket [dị bản (Syā.): mātughātakakammassa; …], which "
                        "present() strips",
    ("5-546", "padesu"): "same bracket as tathā",
}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        text = vi.get(bid, "")
        v = context16(kw, k, kws, text)
        if v is not None:
            return v
        if k in T16:
            return T16[k]
        if k not in PRIOR:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, PRIOR, text)
    return resolve


def _prior_all(k):
    out = {}
    for n in _FINISHED:
        t = getattr(importlib.import_module(f"map_{n}_vi"), f"T{n}", {})
        if k in t:
            out[n] = t[k]
    return out


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
                p = _prior_all(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


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


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["prior"]:      # the finished chapters' table values of each keyword
        for _k in sys.argv[2:]:
            print(_k, _prior_all(lc(_k)), "KV:", KV.get(lc(_k)), "F:", FORMULAS.get(lc(_k)))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
