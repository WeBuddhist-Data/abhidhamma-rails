"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 6-01-sankharayamaka; frame-setter for the Saṅkhārayamaka
members (kāya- / vacī- / cittasaṅkhāra, kāyo / vacī / cittaṃ, assāsapassāsā, vitakkavicārā), the jhānas, the
vitakka kinds of the citta and the two bhūmi, so that 6-02 imports them.

usage: python -I -X utf8 -B map_6-01_vi.py                     (writes 6-01-sankharayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_6-01_vi.py dump [miss]          (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_6-01_vi.py show lo hi [pi]      (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. 6-02 loads it with importlib:
    import importlib, sys; sys.path.insert(0, <this folder>)
    X = importlib.import_module("map_6-01_vi")
and uses the named tables / helpers:
    SANKHARA          the members by inflected form (kāyasaṅkhāro «sự tạo tác bằng thân», kāyo «thân», vacī «lời
                      nói», cittaṃ «tâm», saṅkhāro «sự tạo tác», saṅkhārā «tạo tác» / «sự tạo tác» …)
    member6(kw, text) any member keyword (-ti / -ñca / -ñceva stripped); saṅkhārā by what the segment writes
    BREATH            assāsapassāsā / vitakkavicārā in every case («hơi thở vào và hơi thở ra», «sự hướng tâm và sự
                      duy trì tâm»)
    JHANA             paṭhama- … catutthajjhāna in every case («tầng thiền thứ nhất» … «tầng thiền thứ tư»)
    VKIND             the vitakka kinds of a citta (savitakkasavicāra «có sự hướng tâm và sự duy trì tâm»,
                      avitakkaavicāra «không có sự hướng tâm cũng không có sự duy trì tâm»)
    BHUMI             Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ («cấp độ …»)
    citta6(kw)        <VKIND>[pacchima]cittassa / -cittaṃ / -cittasamaṅgīnaṃ («tâm [cuối cùng] <kind>», «người có
                      được tâm …»); falls back on map_8_vi.citta_value
    moment6(kw, text) «<citta> uppādakkhaṇe / bhaṅgakkhaṇe» = «khoảnh khắc sinh khởi / tan rã của <citta>»
    beings6(kw, vi, pi)   genitive plane-beings (kāmāvacarānaṃ …): map_3-02_vi.beings_value + «cõi X» after itaresaṃ
    PLANES6, PERSONS6, EDITORIAL6, HEADINGS6    planes, persons, editorial lines and headings of this chapter
    T601              every fixed value above, merged
    value601(kw, kws, vi, pi, table=None)    your table -> T601 -> the 6-01 rules -> the 8 / 3-01 / 2-01 frames ->
                      map_sample_vi.value6
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-8.md, notes-map-6-01.md.
"""
import importlib
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_sample_vi import value6  # noqa: E402
from map_common_vi import (NDE, GAP, build_part, en, lc, pick, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

K = importlib.import_module("map_2-01_vi")       # frames201, verb_value, planes, beings, persons, relatives
C = importlib.import_module("map_8_vi")          # value8 pieces: moments, citta kinds, persons
A3 = importlib.import_module("map_3-01_vi")      # PLANE_LOC / BEINGS_GEN (kāmāvacara / rūpāvacara / arūpāvacara)
A302 = importlib.import_module("map_3-02_vi")    # beings_value: the position rule for genitive plane-beings

PART = "6-01-sankharayamaka"

# ---------------------------------------------------------------------------- the Saṅkhārayamaka members
# pi-2 ^2-226 / pi-5: «sự tạo tác bằng thân / lời nói / tâm»; kāyo thân (pi-1), vacī lời nói (pi-5), cittaṃ tâm.
# saṅkhāro (member, «vừa là sự tạo tác vừa là …») = sự tạo tác; saṅkhārā «Các tạo tác» = tạo tác (leading «các» is
# frame, 2-01 / pi-5), «Ba sự tạo tác» = sự tạo tác (member6 picks by the segment).
_SK = {"kāya": "sự tạo tác bằng thân", "vacī": "sự tạo tác bằng lời nói", "citta": "sự tạo tác bằng tâm"}
SANKHARA = {
    "kāyo": "thân", "kāyaṃ": "thân", "kāya": "thân", "kāyassa": "thân",
    "vacī": "lời nói", "vaciṃ": "lời nói", "vacīṃ": "lời nói", "vaci": "lời nói",
    "cittaṃ": "tâm", "citta": "tâm", "cittassa": "tâm", "citte": "tâm",
    "saṅkhāro": "sự tạo tác", "saṅkhāraṃ": "sự tạo tác",
    "saṅkhārā": "tạo tác", "saṅkhāre": "tạo tác", "saṅkhārānaṃ": "tạo tác",
    "cittasampayuttakā": "gắn liền với tâm",       # «các hiện tượng gắn liền với tâm» (pi-1 MATRIX cittasampayutta)
    "vedanā": "cảm giác", "saññā": "tri giác",     # «tri giác và cảm giác là sự tạo tác bằng tâm»
}
for _s, _v in _SK.items():
    for _e in ("o", "aṃ", "ā", "e", "a", "assa", "ānaṃ"):
        SANKHARA[_s + "saṅkhār" + _e] = _v


def _strip(kw):
    """lower case, the question -ti and -ñca / -ñceva dropped («vacīti» -> vacī, «Vaciñca» -> vaciṃ,
    «cittanti» -> cittaṃ, «kāyasaṅkhārañca» -> kāyasaṅkhāraṃ)."""
    k = lc(kw).lower()
    if k.endswith("nti") and len(k) > 4:
        return k[:-3] + "ṃ"
    if len(k) > 4 and k.endswith("ti") and k[-3] in "āīūoe":
        return k[:-2]
    for p in ("ñceva", "ñca"):
        if k.endswith(p):
            return k[: -len(p)] + "ṃ"
    return k


def member6(kw, text):
    """A Saṅkhārayamaka member keyword (any -ti / -ñca form); None if not one. saṅkhārā = «tạo tác» where the
    segment writes «các tạo tác», else «sự tạo tác» («Ba sự tạo tác»)."""
    k = lc(kw).lower()
    k2 = k if k in SANKHARA else _strip(kw)
    if k2 not in SANKHARA:
        return None
    v = SANKHARA[k2]
    if v == "tạo tác" and not present("các tạo tác", text):
        return pick(text, "sự tạo tác", "tạo tác") or v
    return v


# ---------------------------------------------------------------------------- breathing and applied / sustained thought
BREATH = {}
for _e in ("ā", "ānaṃ", "ehi", "e", "aṃ", "a"):
    BREATH["assāsapassās" + _e] = "hơi thở vào và hơi thở ra"          # pi-5
    BREATH["vitakkavicār" + _e] = "sự hướng tâm và sự duy trì tâm"     # pi-1 / pi-5

# ---------------------------------------------------------------------------- the jhānas («Trong tầng thiền thứ tư»:
# the locative «Trong» is frame; «Ở những người đang nhập tầng thiền thứ tư»: samāpannānaṃ = người đang nhập)
_ORD = {"paṭhama": "thứ nhất", "dutiya": "thứ hai", "tatiya": "thứ ba", "catuttha": "thứ tư"}
JHANA = {}
for _o, _v in _ORD.items():
    for _e in ("aṃ", "e", "ā", "ena", "assa", "a", "āni"):
        JHANA[_o + "jjhān" + _e] = "tầng thiền " + _v
    JHANA[_o + "jjhānaṃ"] = "tầng thiền " + _v

# ---------------------------------------------------------------------------- vitakka kinds of the citta and the bhūmi
VKIND = {"savitakkasavicāra": "có sự hướng tâm và sự duy trì tâm",
         "avitakkaavicāra": "không có sự hướng tâm cũng không có sự duy trì tâm"}
BHUMI = {"savitakkasavicārabhūmiyaṃ": "cấp độ có sự hướng tâm và sự duy trì tâm",       # pi-1 ^1-1000
         "avitakkaavicārabhūmiyaṃ": "cấp độ không có sự hướng tâm cũng không có sự duy trì tâm"}  # «Ở» is frame
# the bare kind (yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ … «tâm cuối cùng không có …»)
VKIND_FORMS = {}
for _s, _v in VKIND.items():
    for _e in ("aṃ", "ā", "o", "e", "a"):
        VKIND_FORMS[_s[:-1] + _e] = _v


def citta6(kw):
    """<VKIND>[pacchima]cittassa / -cittaṃ / -cittasamaṅgīnaṃ: «tâm [cuối cùng] <kind>» (Savitakkasavicāra-
    pacchimacittassa «tâm cuối cùng có sự hướng tâm và sự duy trì tâm», avitakkaavicāracittassa «tâm không có …»),
    «người có được tâm cuối cùng <kind>» for -samaṅgīnaṃ; else map_8_vi.citta_value (pacchimacittaṃ «tâm cuối
    cùng», Pacchimacittasamaṅgīnaṃ «người có được tâm cuối cùng»). None if not a citta compound."""
    k = C.norm(lc(kw).lower())
    for s, v in VKIND.items():
        if not k.startswith(s):
            continue
        rest = k[len(s):]
        person = False
        for p in ("samaṅgīnaṃ", "samaṅgī", "samaṅgino"):
            if rest.endswith(p):
                rest, person = rest[: -len(p)], True
                break
        last = rest.startswith("pacchima")
        if last:
            rest = rest[len("pacchima"):]
        if rest not in ("cittassa", "cittaṃ", "citta", "cittā", "citte"):
            return None
        out = "tâm " + ("cuối cùng " if last else "") + v
        return ("người có được " + out) if person else out
    return C.citta_value(kw)


def moment6(kw, text):
    """«<citta> uppādakkhaṇe / bhaṅgakkhaṇe» = «khoảnh khắc sinh khởi / tan rã của <citta>» (map_8_vi.moment_value
    with citta6 for the genitive). None if not one."""
    words = kw.split()
    if len(words) != 2:
        return None
    m = C.moment_value(words[1], text)
    c = citta6(words[0])
    if m and c:
        return m + " của " + c
    return None


# ---------------------------------------------------------------------------- planes, persons
PLANES6 = dict(A3.PLANE_LOC)                       # kāmāvacare / rūpāvacare / arūpāvacare / asaññasatte … «cõi …»
PLANES6.update({"arūpāvacaraṃ": "cõi không hình sắc", "rūpāvacaraṃ": "cõi hình sắc",   # upapajjitvā «tái sinh
                "kāmāvacaraṃ": "cõi dục lạc"})                                         # vào cõi …» («vào» frame)
PERSONS6 = {
    "samāpannānaṃ": "người đang nhập",             # «Ở những người đang nhập tầng thiền thứ nhất» (pi-5)
    "nirodhasamāpannānaṃ": "người nhập thành tựu thiền chấm dứt",   # 8
    "nirodhasamāpannānanti": "người nhập thành tựu thiền chấm dứt",
    "tesaṃyeva": "chính những người ấy",           # «ở chính những người ấy» (inner «những» kept, pi-1)
    "anantarā": "ngay sau",                        # «vào tâm mà ngay sau đó tâm cuối cùng … sẽ sinh khởi» (pi-5)
    "vattamāne": "khi" + GAP + "đang diễn ra",     # «khi tâm thứ hai đang diễn ra» (pi-5; participle keeps «khi»)
}

# ---------------------------------------------------------------------------- editorial lines and headings
EDITORIAL6 = {
    # (Yassakampi yassayatthakampi sadisaṃ.) «(Phần về người và phần về người và nơi chốn đều giống nhau.)»;
    # -pi has no word of its own («đều», «cả … lẫn» are the frame; 3-01 yassaka / yatthakaṃ)
    "yassakampi": "phần về người", "yassayatthakampi": "phần về người và nơi chốn",
    "yassayatthake": "phần về người và nơi chốn", "yatthakampi": "phần về nơi chốn",
    "yassaka": "phần về người", "yatthaka": "phần về nơi chốn", "yassayatthaka": "phần về người và nơi chốn",
    "uppādavāre": "mục về sự sinh khởi", "nirodhavārepi": "mục về sự chấm dứt", "nirodhavāre": "mục về sự chấm dứt",
    "anulomampi": "chiều thuận", "paccanīkampi": "chiều nghịch",
    "pucchā": "câu hỏi",                           # «Như các câu hỏi về quá khứ» (pi-5; «các» frame)
    "(no direct equivalent)": NDE,                 # placeholder keyword with no Pāli word (coordinator rule)
}
HEADINGS6 = {
    "suddhasaṅkhāravāro": "mục về các tạo tác thuần túy",   # = Suddhakhandhavāro (sample FORMULAS)
    "paṇṇattiuddesavāro": "mục nêu đề mục về sự định danh",  # 2-01
    "paṇṇattiniddesavāro": "mục giải thích về sự định danh",
    "paccanīkaokāsā": "chiều nghịch theo nơi chốn",          # ^6-6-16-5-0 spelling of paccanīkaokāso
}

T601 = {}
T601.update(BREATH)
T601.update(JHANA)
T601.update(BHUMI)
T601.update(VKIND_FORMS)
T601.update(PLANES6)
T601.update(PERSONS6)
T601.update(EDITORIAL6)
T601.update(HEADINGS6)


def rules601(kw, kws, vi, pi):
    """The 6-01 segment rules. None = no rule."""
    v = member6(kw, vi)
    if v is not None:
        return v
    v = moment6(kw, vi)
    if v is not None:
        return v
    if " " not in kw:
        v = citta6(kw)
        if v is not None:
            if v.startswith("người ") and C._after_itaresam(kw, pi):
                return v[len("người "):]
            return v
    k = lc(kw).lower()
    if k in A3.BEINGS_GEN:
        return beings6(kw, vi, pi)
    return None


def beings6(kw, vi, pi):
    """kāmāvacarānaṃ / rūpāvacarānaṃ / arūpāvacarānaṃ / suddhāvāsānaṃ … (3-01 BEINGS_GEN) by their FIRST occurrence
    in the Pāli: «chúng sinh trong cõi X», but «cõi X» where the head «chúng sinh» belongs to the word before (a
    preceding being of a list, «Rūpāvacarānaṃ arūpāvacarānaṃ» «chúng sinh trong cõi hình sắc, cõi không hình sắc»,
    or itaresaṃ, «itaresaṃ rūpāvacarānaṃ» «những chúng sinh khác trong cõi hình sắc», 2-01 rule)."""
    k = lc(kw).lower()
    cands = A3.BEINGS_GEN[k]
    m = A302._first(kw, pi)
    if m and len(cands) > 1:
        words = re.split(r"[.?!\n]", pi[: m.start()])[-1].split()
        if words and lc(words[-1]).lower() == "itaresaṃ":     # coordinator rule (2-01, 3-03)
            return pick(vi, cands[1], cands[0]) or cands[1]
    return A302.beings_value(kw, vi, pi)                     # the 3-02 position rule (coordinator)


def value601(kw, kws, vi, pi, table=None):
    """your table -> T601 -> the 6-01 rules -> the 2-01 frames (verbs, planes, persons, relatives) ->
    map_sample_vi.value6."""
    k = lc(kw).lower()
    if table and k in table:
        return table[k]
    if k in T601:
        return T601[k]
    if _strip(kw) in T601:
        return T601[_strip(kw)]
    v = rules601(kw, kws, vi, pi)
    if v is not None:
        return v
    v = K.frames201(kw, kws, vi, pi, members={})
    if v is not None:
        return v
    return value6(kw, kws, table, vi)


# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value601(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(part=PART, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                v = res(bid, kw, kws)
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(PART, sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver_for(PART))
        verify(PART, ALLOWED)
