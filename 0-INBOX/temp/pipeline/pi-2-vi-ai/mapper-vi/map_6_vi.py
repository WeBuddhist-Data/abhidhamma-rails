"""Build the Pāli->Vietnamese keyword map for pi-2 part 6-paticcasamuppadavibhango.

usage: python -I -X utf8 map_6_vi.py              (writes 6-paticcasamuppadavibhango.mapped.md and verifies it)
       python -I -X utf8 map_6_vi.py dump [miss]  (every distinct keyword=value with count, first segments and the
                                                   approved pi-1 map's most common value; with «miss» only presence
                                                   misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules: the dependent-origination links,
-hetuka compounds, object lists, nāma/rūpa, dukkha …) -> T6 (this script's table) -> T45 (map_4-5_vi.py, the ch. 4
jāti / jarā / maraṇa / soka … strings) -> map_common_vi.value(): KH (pi-2 table) -> the approved pi-1 chain.
Conventions: pi-1 vi-map-conventions.md, vi-map-conventions-pi2.md, notes-map-2-3.md, notes-map-4-5.md,
notes-map-6.md.

The links («X làm điều kiện cho Y» in the chains, «Y do X làm điều kiện» in the questions and answers): a keyword
Xpaccayā takes the form of its FIRST occurrence in the segment's Vietnamese (chain «X làm điều kiện cho» or name
«do X làm điều kiện»); the -pi form «X cũng làm điều kiện cho» drops «cũng» (« … »), as notes-map-4-5.md.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata
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

PART = "6-paticcasamuppadavibhango"
_KX = "không xác định về mặt đạo đức"

# ---------------------------------------------------------------------------- link nouns (build_6_vi.py N)
LINKN = {
    "avijjā": ["vô minh"],
    "saṅkhāra": ["sự tạo tác", "các sự tạo tác"],      # «các» kept only inside «do các sự tạo tác làm điều kiện»
    "viññāṇa": ["thức"],
    "nāma": ["phần tinh thần"],
    "nāmarūpa": ["phần tinh thần và vật chất"],
    "saḷāyatana": ["sáu lĩnh vực nhận biết"],
    "chaṭṭhāyatana": ["lĩnh vực nhận biết thứ sáu"],
    "phassa": ["sự tiếp xúc"],
    "vedanā": ["cảm giác"],
    "taṇhā": ["khao khát"],
    "upādāna": ["sự bám víu"],
    "bhava": ["sự hiện hữu"],
    "jāti": ["sự sinh"],
    "adhimokkha": ["sự quyết định"],
    "paṭigha": ["sự ác cảm"],
    "vicikicchā": ["sự hoài nghi"],
    "uddhacca": ["sự xao động"],
    "pasāda": ["lòng tin trong sáng"],
    "kusalamūla": ["gốc rễ thiện", "các gốc rễ thiện"],
    "akusalamūla": ["gốc rễ bất thiện", "các gốc rễ bất thiện"],
}
COND, BY = "làm điều kiện cho", "làm điều kiện"
# members (Xpaccayā cut out of a longer compound): (chain forms, name forms), with « … » where the compound's other
# words stand in between
MEMBERS = {
    "rūpa": ([f"vật chất {COND}"], [f"do{GAP}vật chất {BY}"]),                       # of nāmarūpapaccayā
    "āyatana": ([f"lĩnh vực nhận biết {COND}", f"lĩnh vực nhận biết{GAP}{COND}"],    # saḷāyatana- / chaṭṭhāyatana-
                [f"do{GAP}lĩnh vực nhận biết {BY}", f"do lĩnh vực nhận biết{GAP}{BY}"]),
    "mūla": ([f"gốc rễ{GAP}{COND}"], [f"do{GAP}gốc rễ{GAP}{BY}"]),                   # (a)kusalamūla- (thiện …)
}


def _rx(v, gap):
    parts = [re.escape(p) for p in v.split(GAP)]
    return re.compile(r"(?<!\w)" + (r"(?:\W+\w+){0,%d}?\W+" % gap).join(parts) + r"(?!\w)")


def _norm(text):
    text = re.sub(r"\[[^\]]*\]", " ", unicodedata.normalize("NFC", text)).lower()
    return text


_FAIL = object()


def first(cands, text, gap=3, default=_FAIL):
    """cands: values, or (detect, value) pairs. The value whose detect string occurs first in `text` (« … » gaps of
    at most `gap` words); ties: list order. The value must pass the presence check. Nothing found: `default`, or the
    first candidate's value."""
    t = _norm(text)
    best = None
    for i, c in enumerate(cands):
        d, v = c if isinstance(c, tuple) else (c, c)
        m = _rx(unicodedata.normalize("NFC", d).lower(), gap).search(t)
        if m and present(v, text) and (best is None or m.start() < best[0]):
            best = (m.start(), i, v)
    if best:
        return best[2]
    if default is not _FAIL:
        return default
    c = cands[0]
    return c[1] if isinstance(c, tuple) else c


def prio(cands, text):
    """the first candidate present in `text`."""
    for c in cands:
        if present(c, text):
            return c
    return cands[0]


def link_value(stem, text, chain_only=False):
    """Xpaccayā: the form of its first occurrence, chain «X làm điều kiện cho» or name «do X làm điều kiện»; only
    where neither occurs, the -pi form «X cũng làm điều kiện cho» (value «X … làm điều kiện cho»: «cũng» dropped).
    chain_only for a capitalised keyword (sentence-initial: the chain or the quoted lemma «“Phần tinh thần làm điều
    kiện cho sự tiếp xúc”»). None: not a link stem."""
    if stem in LINKN:
        xs = LINKN[stem]
        # chain: the leading «các» of «các sự tạo tác / các gốc rễ thiện làm điều kiện cho» is frame (dropped);
        # name: «do các sự tạo tác làm điều kiện» keeps its inner «các»
        chain, name = [f"{xs[0]} {COND}"], [f"do {x} {BY}" for x in xs]
        pi = [(f"{xs[0]} cũng {COND}", xs[0] + GAP + COND)]
    elif stem in MEMBERS:
        (chain, name), pi = MEMBERS[stem], []
    else:
        return None
    v = first(chain + ([] if chain_only else name), text, gap=5, default=None)
    return v if v is not None or not pi else first(pi, text)


# ---------------------------------------------------------------------------- -hetuka compounds (Hetucatukka)
HETU_Y = {"saṅkhāro": "sự tạo tác", "viññāṇaṃ": "thức", "nāmaṃ": "phần tinh thần", "phasso": "sự tiếp xúc",
          "vedanā": "cảm giác", "taṇhā": "khao khát", "upādānaṃ": "sự bám víu"}
HETU_X = {"avijjā": "vô minh", "saṅkhāra": "sự tạo tác", "viññāṇa": "thức", "nāma": "phần tinh thần",
          "phassa": "sự tiếp xúc", "vedanā": "cảm giác", "taṇhā": "khao khát"}

# ---------------------------------------------------------------------------- objects («có đối tượng là X»)
OBJ = {"rūp": "hình sắc", "sadd": "âm thanh", "gandh": "mùi", "ras": "vị", "phoṭṭhabb": "vật xúc chạm",
       "dhamm": "đối tượng của ý"}

T6 = {
    # ---- headings
    "paṭicca": "tùy thuộc vào điều kiện", "samuppāda": "sự sinh khởi",      # «Phân tích sự sinh khởi tùy thuộc …»
    "catukkaṃ": "bộ bốn", "paccayacatukkaṃ": "bộ bốn về điều kiện", "hetu": "nguyên nhân",
    "sampayuttacatukkaṃ": "bộ bốn về sự gắn liền", "aññamañña": "sự tương hỗ",
    "aññamaññacatukkaṃ": "bộ bốn về sự tương hỗ", "mātikā": "ma trận",
    "niddeso": "giải thích", "vipākaniddeso": "giải thích phần quả", "mūlaka": "dựa trên",
    "mūlakavipāka": "quả dựa trên",                                     # «phần quả dựa trên các gốc rễ thiện»
    "kusala": "thiện", "akusala": "bất thiện", "abyākata": _KX,
    # ---- the chain
    "saṅkhāro": "sự tạo tác", "saṅkhārā": "sự tạo tác", "nāmaṃ": "phần tinh thần", "nāma": "phần tinh thần",
    "nāmarūpaṃ": "phần tinh thần và vật chất", "nāmarūpa": "phần tinh thần và vật chất",
    "saḷāyatanaṃ": "sáu lĩnh vực nhận biết", "saḷāyatana": "sáu lĩnh vực nhận biết",
    "chaṭṭhāyatanaṃ": "lĩnh vực nhận biết thứ sáu", "chaṭṭhāyatana": "lĩnh vực nhận biết thứ sáu",
    "phasso": "sự tiếp xúc", "phassa": "sự tiếp xúc", "taṇhā": "khao khát", "upādānaṃ": "sự bám víu",
    "upādāna": "sự bám víu", "bhavo": "sự hiện hữu", "bhava": "sự hiện hữu", "jāti": "sự sinh",
    "jarāmaraṇaṃ": "sự lão hóa và sự chết", "jarā": "sự lão hóa", "maraṇaṃ": "sự chết",
    "pasādo": "lòng tin trong sáng", "avijjā": "vô minh",
    "soka": "sự sầu muộn", "parideva": "sự than khóc", "domanassupāyāsā": "nỗi buồn và sự tuyệt vọng",
    "upāyāsā": "sự tuyệt vọng",
    "kevalassa": "toàn bộ", "kevalassa dukkhakkhandhassa": "toàn bộ khối khổ đau",
    "dukkhakkhandhassa": "khối khổ đau", "khandhassa": "khối", "samudayo": "sự phát sinh",
    "saṅgati": "sự kết hợp", "samodhānaṃ": "sự tụ hợp", "pātubhāvo": "sự xuất hiện",
    "tena": "vì thế",                                                    # «Vì thế nên mới nói rằng …»
    "samaye": "vào lúc ấy",
    # ---- Suttanta definitions
    "dukkhe": "khổ đau", "samudaye": "sự phát sinh", "dukkhasamudaye": "sự phát sinh của khổ đau",
    "nirodhe": "sự chấm dứt", "dukkhanirodhe": "sự chấm dứt khổ đau", "aññāṇaṃ": "sự không biết",
    "puññābhisaṅkhāro": "sự tạo tác thuộc về phước", "apuññābhisaṅkhāro": "sự tạo tác không thuộc về phước",
    "āneñjābhisaṅkhāro": "sự tạo tác dẫn đến trạng thái bất động", "ābhisaṅkhāro": "sự tạo tác",
    "kāyasaṅkhāro": "sự tạo tác bằng thân", "kāya": "thân", "vacī": "lời nói", "citta": "tâm",
    "cetanā": "chủ ý", "dāna": "sự bố thí", "sīla": "giới hạnh", "bhāvanā": "sự tu tập",
    "kāmāvacarā": "thuộc cõi dục lạc", "rūpāvacarā": "thuộc cõi hình sắc", "arūpāvacarā": "thuộc cõi không hình sắc",
    "āvacarā": "thuộc cõi",
    "upādāya rūpaṃ": "vật chất phái sinh từ",
    "kāmupādānaṃ": "sự bám víu vào dục lạc", "diṭṭhupādānaṃ": "sự bám víu vào quan điểm",
    "sīlabbatupādānaṃ": "sự bám víu vào giới hạnh và nghi thức",
    "attavādupādānaṃ": "sự bám víu vào học thuyết về tự ngã", "atta": "tự ngã",
    "kammabhavo": "sự hiện hữu dưới dạng nghiệp", "upapattibhavo": "sự hiện hữu dưới dạng tái sinh",
    "kāma": "dục lạc", "arūpa": "không hình sắc", "asaññā": "không có tri giác",
    "nevasaññānāsaññā": "không phải có tri giác cũng không phải không có tri giác",
    "ekavokāra": "gồm một khối", "catuvokāra": "gồm bốn khối", "pañcavokāra": "gồm năm khối",
    "gāmi": "dẫn đến",                                                   # bhavagāmikammaṃ «nghiệp dẫn đến sự hiện hữu»
    "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm",
    "tesaṃ tesaṃ": "từng", "sattānaṃ": "chúng sinh", "khandhānaṃ": "khối", "āyatanānaṃ": "lĩnh vực nhận biết",
    # ---- Abhidhamma definitions
    "adassanaṃ": "sự không thấy", "laṅgī": "then cài", "moho": "sự si mê", "mūlaṃ": "gốc rễ",
    "akusalamūlaṃ": "gốc rễ bất thiện", "kusalamūlaṃ": "gốc rễ thiện",
    "sañcetanā": "sự cố ý", "sañcetayitattaṃ": "trạng thái đã cố ý",
    "tajjā": "tương ứng", "indriyaṃ": "năng lực", "mano": "ý",
    "phusanā": "sự chạm",
    "nibbatti": "sự phát khởi", "abhinibbatti": "sự hình thành", "abhinibbati": "sự hình thành",   # ^2-273 slip as meant
    "khayo": "sự hủy diệt", "vayo": "sự suy tàn", "bhedo": "sự tan rã", "paribhedo": "sự tan rã hoàn toàn",
    "aniccatā": "tính vô thường", "antaradhānaṃ": "sự biến mất", "jīraṇatā": "sự hao mòn", "āyuno": "tuổi thọ",
    "cakkhāyatanassa": "lĩnh vực mắt", "sotāyatanassa": "lĩnh vực tai", "ghānāyatanassa": "lĩnh vực mũi",
    "jivhāyatanassa": "lĩnh vực lưỡi", "kāyāyatanassa": "lĩnh vực thân",
    "cittajaṃ": "sinh từ tâm", "samuṭṭhānaṃ": "do" + GAP + "sinh ra", "hetukaṃ": "có" + GAP + "làm nguyên nhân",
    "hetuko": "có" + GAP + "làm nguyên nhân", "hetukā": "có" + GAP + "làm nguyên nhân",
    "nissāya": "dựa vào", "rūpaṃ nissāya": "vật chất mà" + GAP + "dựa vào", "vattati": "vận hành",
    "adhimuccanā": "sự khởi quyết định", "tadadhimuttatā": "trạng thái đã quyết định về điều đó",
    "alobho": "sự không tham lam", "adoso": "sự không sân hận", "amoho": "sự không si mê",
    "kusalamūlā": "gốc rễ thiện", "mūlā": "gốc rễ",
    "sammā": "đúng đắn",
    # ---- mind-type, vipāka, kiriya and jhāna openings (pi-1 values; «có đối tượng là …» of this chapter)
    "yaṃ yaṃ": "bất cứ thứ gì", "ārammaṇaṃ": "đối tượng", "uppannaṃ": "sinh khởi", "uppannā": "sinh khởi",
    "sasaṅkhārena": "có sự thúc đẩy", "sampayuttaṃ": "gắn liền", "sampayutto": "gắn liền", "sampayuttā": "gắn liền",
    "vippayuttaṃ": "không gắn liền", "vippayuttā": "không gắn liền",
    "ñāṇavippayuttaṃ": "không gắn liền với hiểu biết", "ñāṇavippayuttā": "không gắn liền với hiểu biết",
    "diṭṭhigata": "sự mắc kẹt trong các quan điểm",
    "kāmāvacarassa kusalassa": "thiện thuộc cõi dục lạc", "kusalassa kammassa": "nghiệp thiện",
    "vipākaṃ": "quả", "vipākā": "quả", "āvacarassa": "thuộc cõi",
    "rūpūpapattiyā": "tái sinh vào cõi hình sắc", "arūpūpapattiyā": "tái sinh vào cõi không hình sắc",
    "ūpapattiyā": "tái sinh", "ūpapattiyā maggaṃ": "con đường dẫn đến tái sinh", "maggaṃ": "con đường",
    "bhāveti": "tu tập", "pathavī": "đất", "pathavīkasiṇaṃ": "đề mục bao trùm là đất",
    "ākiñcaññāyatanaṃ": "lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatana": "lĩnh vực không phải tri giác cũng không phải không tri giác",
    "apacayagāmiṃ": "dẫn đến sự giảm trừ", "ābhiññaṃ": "sự hiểu biết trực tiếp", "paṭipadaṃ": "cách thực hành",
    "paṭipadaṃ dandhābhiññaṃ": "cách thực hành" + GAP + "sự hiểu biết trực tiếp chậm chạp",
    "kiriyā": "mang tính chức năng", "kiriyaṃ": "mang tính chức năng",
    "ākusalā": "bất thiện", "ākusalaṃ": "bất thiện",                    # of nākusalā «không phải bất thiện»
    "arūpāvacaraṃ jhānaṃ": "tầng thiền thuộc cõi không hình sắc",
    # ---- members and strings settled on the dump
    "mūla": "gốc rễ", "akusalamūla": "gốc rễ bất thiện", "kusalamūla": "gốc rễ thiện",
    "ñāṇaṃ": "biết",                                                     # of aññāṇaṃ «sự không biết» (pi-1)
    "alubbhanā": "sự không khởi lòng tham", "adussanā": "sự không khởi sân",   # keep their a- (own word)
    "sukhaṃ": "dễ chịu", "sukhā vedanā": "cảm giác" + GAP + "dễ chịu",   # feeling string (pi-1)
    "sātaṃ sukhaṃ": "khoan khoái và dễ chịu", "sātaṃ sukhaṃ vedayitaṃ": "cảm nhận khoan khoái và dễ chịu",
    "sātā sukhā vedanā": "cảm giác khoan khoái và dễ chịu",
    "dukkhaṃ": "khó chịu",                                               # ch4 ^2-196 / ^2-197
    "asātaṃ dukkhaṃ": "bứt rứt và khó chịu", "asātaṃ dukkhaṃ vedayitaṃ": "cảm nhận bứt rứt và khó chịu",
    "asātā dukkhā vedanā": "cảm giác bứt rứt và khó chịu",
    "nāsātaṃ": "không bứt rứt",                                          # «không khoan khoái cũng không bứt rứt»
    "asuropo": "sự nói năng cộc cằn",                                    # notes-map-2-3
    "anekaṃsa": "không" + GAP + "điều chắc chắn",                       # anekaṃsaggāho «sự không nắm giữ được …»
    "dvidhāpatho": "sự đứng trước ngã ba đường", "apariyogāhaṇā": "sự không đi sâu",
    "chambhitattaṃ": "trạng thái cứng đờ",                               # pi-1 thambhitattaṃ
    "cetaso vikkhepo": "sự tán loạn của tâm", "nandirāgo": "sự tham đắm vì thích thú",
    "titthāyatanaṃ": "lĩnh vực của các học thuyết ngoại đạo", "maggapariyāpannaṃ": "nằm trong con đường",
    "parisoko": "nỗi sầu thấm sâu",                                      # of antoparisoko
}


def context(bid, kw, k, s, text):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k.endswith("paccayā"):
        stem = k[:-len("paccayā")]
        if stem == "":
            return first([COND, "do" + GAP + BY], text, gap=8)
        v = link_value(stem, text, chain_only=kw[0].isupper())
        if v is not None:
            return v
    m = re.match(r"^(\S+) (\S+?)hetuk(?:o|aṃ|ā)$", k)
    if m and m.group(1) in HETU_Y and m.group(2) in HETU_X:
        y, x = HETU_Y[m.group(1)], HETU_X[m.group(2)]     # «Y do X làm điều kiện, có X làm nguyên nhân» (name)
        return first([f"{y} có {x} làm nguyên nhân", f"{y}{GAP}có {x} làm nguyên nhân"], text, gap=8)
    if k == "cetasikaṃ":                 # pi-1: «trạng thái trong tâm» in «cetasikaṃ neva sātaṃ nāsātaṃ»
        return "trạng thái trong tâm" if "nāsātaṃ" in s and not ({"cetasikaṃ sātaṃ", "cetasikaṃ asātaṃ"} & s) \
            else "trong tâm"
    if k == "sukha":                     # body consciousness «có sự dễ chịu đi kèm»; sukhavihāra «hạnh phúc»
        return "sự dễ chịu" if "sukhasahagataṃ" in s else "hạnh phúc"
    if k == "sukhasahagataṃ":
        return "có sự dễ chịu đi kèm"
    if k == "dhamma":                    # dhammataṇhā «khao khát đối tượng của ý»; dhammavicayo «… các hiện tượng»
        return "hiện tượng" if "dhammavicayo" in s else "đối tượng của ý"
    m = re.match(r"^(rūp|sadd|gandh|ras|phoṭṭhabb|dhamm)ārammaṇ(?:aṃ|ā)$", k)
    if m:
        o = OBJ[m.group(1)]
        if m.group(1) == "rūp":
            return f"có đối tượng là {o}"
        return prio([f"có đối tượng là {o}", f"có đối tượng là{GAP}{o}"], text)
    if k == "rūpaṃ":                     # nāma / rūpa members (harmonised «phần vật chất», pi-1 ^1-1317)
        return prio(["phần vật chất", "vật chất"], text)
    if k == "dukkha":                    # dukkhakkhandha «khối khổ đau»; dukkhapaṭipadaṃ «khó khăn»
        return prio(["khổ đau", "khó khăn"], text)
    if k == "āyatanaṃ":
        return prio(["lĩnh vực nhận biết", "lĩnh vực"], text)
    if k == "saṅkhāra":                  # stem of saṅkhārakkhandho (tạo tác) or of saṅkhārapaccayā (sự tạo tác)
        return "tạo tác" if "saṅkhārakkhandho" in s else "sự tạo tác"
    if k == "viññāṇadhātu":
        return prio(["yếu tố thức", "yếu tố" + GAP + "thức"], text)
    if k in ("dhammā kusalā", "dhammā akusalā", "dhammā abyākatā"):
        a = {"dhammā kusalā": "thiện", "dhammā akusalā": "bất thiện", "dhammā abyākatā": _KX}[k]
        return prio([f"hiện tượng {a}", f"hiện tượng{GAP}{a}"], text)
    if k == "viharati":
        return "an trú" if present("an trú", text) else "sống"
    return None


OVERRIDES = {
    "2-232": {"Rūpa": "hình sắc"},                       # Rūpataṇhā «khao khát hình sắc»
    "2-234": {"rūpa": "hình sắc", "saññā": "có tri giác"},   # rūpabhavo / saññābhavo «sự hiện hữu … có tri giác»
    "2-289": {"gāho": "nắm giữ"},                        # anekaṃsaggāho «sự không nắm giữ được …» (pi-1)
}


def resolve(bid, kw, kws, vi):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    text = vi.get(bid, "")
    v = context(bid, kw, k, s, text)
    if v is not None:
        return v
    return value(kw, kws, {**T45, **T6}, text)


def resolver():
    vi = read_vietnamese(PART)
    return lambda bid, kw, kws: resolve(bid, kw, kws, vi)


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
        p1 = pi1_map_values(kw).most_common(1)
        p1 = p1[0][0] if p1 else ""
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 and p1 != v else "")
              + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(len(sys.argv) > 2)
    else:
        build_part(PART, resolver())
        verify(PART)
