"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 2-01-khandhayamaka; frame-setter for the Khandhayamaka members
and for the shared pavatti frames (uppajjati / nirujjhati and their tenses, beings and planes, yassa / tassa /
yattha / tattha).

usage: python -I -X utf8 -B map_2-01_vi.py                     (writes 2-01-khandhayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_2-01_vi.py dump [miss]          (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_2-01_vi.py show lo hi [pi]      (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Later chapters load it with importlib:
    import importlib, sys; sys.path.insert(0, <this folder>)
    K = importlib.import_module("map_2-01_vi")
and use the named tables / helpers:
    KHANDHA           the Khandhayamaka members by inflected form (rūpakkhandho «khối vật chất», rūpaṃ «vật chất» …)
    member_value(kw, members)   any member keyword with -ti / -ñca / -ñceva / ca stripped (rūpanti, Rūpañca,
                      rūpakkhandhañca …); pass your own yamaka's members table (same shape as KHANDHA)
    VERB_STEMS        {stem: Vietnamese verb} (uppajj «sinh khởi», nirujjh «chấm dứt»)
    VERB_FORMS        the tense / polarity / «no ca» forms (see verb_vi); PAVATTI = every fixed verb keyword
    verb_value(kw, pali)        the verb keyword's value from its FIRST occurrence in the Pāli segment (fused n- / separate
                      na / inside a «no ca» clause / short answer)
    PLANES, BEINGS    plane stems -> «cõi …» and the -ānaṃ beings «chúng sinh …»; plane_value(kw, text)
    PERSONS           pacchimabhavikānaṃ, itaresaṃ, upapajjitvā, parinibbāyissanti, the participles …
    RELATIVES         yassa / tassa / yattha / tattha and their combinations (the person / place frame)
    HEADINGS          the chapter's headings not yet in map_sample_vi.FORMULAS
    T201              all of the above that is a fixed value, merged (pass it as your table to value6, or use value201)
    value201(kw, kws, vi, pi, table=None)    your table -> the 2-01 frames -> map_sample_vi.value6
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md.
"""
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_sample_vi import FORMULAS, YM, value6  # noqa: E402
from map_common_vi import (GAP, NDE, build_part, en, lc, pick, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

PART = "2-01-khandhayamaka"

# ---------------------------------------------------------------------------- the Khandhayamaka members
# pi-1 / pi-2 values as the translation writes them; the leading «các» of «các tạo tác» / «các khối» is frame
# (pi-5 saṅkhārā = tạo tác), the Pāli number has no word of its own.
_KH_STEMS = {"rūpa": "vật chất", "vedanā": "cảm giác", "saññā": "tri giác", "saṅkhāra": "tạo tác",
             "viññāṇa": "thức"}
KHANDHA = {
    # khandha (member)
    "khandho": "khối", "khandhaṃ": "khối", "khandhā": "khối", "khandhe": "khối", "khandha": "khối",
    "khandhassa": "khối", "khandhānaṃ": "khối", "khandhehi": "khối", "khandhesu": "khối",
    "pañcakkhandhā": "năm khối",                   # Pañcakkhandhā – … «Năm khối –» (keyword with its numeral, pi-3)
    # the five members
    "rūpaṃ": "vật chất", "rūpa": "vật chất",
    "vedanā": "cảm giác", "vedanaṃ": "cảm giác",
    "saññā": "tri giác", "saññaṃ": "tri giác",
    "saṅkhārā": "tạo tác", "saṅkhāre": "tạo tác", "saṅkhāra": "tạo tác",
    "viññāṇaṃ": "thức", "viññāṇa": "thức",
    # A_SENSE subjects (2-01 builder): «Tri giác hiểu theo nghĩa quan điểm», «Vật chất hiểu theo nghĩa điều đáng
    # yêu, điều khoan khoái» (the whole Vietnamese phrase: «hiểu theo nghĩa» renders the compound relation)
    "diṭṭhisaññā": "tri giác hiểu theo nghĩa quan điểm",
    "piyarūpaṃ": "vật chất hiểu theo nghĩa điều đáng yêu", "sātarūpaṃ": "điều khoan khoái",
}
for _s, _v in _KH_STEMS.items():
    _kk = _s + "kkhandh"                           # rūpa -> rūpakkhandh-, vedanā -> vedanākkhandh-
    for _e in ("o", "aṃ", "ā", "e", "a", "assa", "ānaṃ", "ehi", "esu"):
        KHANDHA[_kk + _e] = "khối " + _v


def _strip_particles(k):
    """lower-case keyword without the question -ti («rūpanti» -> rūpaṃ, «vedanākkhandhoti», «saññāti») and without
    -ñca / -ñceva / ceva («rūpañceva», «Rūpañca», «rūpakkhandhañca»: ca / ceva have no word of their own; «vừa … vừa»,
    «và» are frame, sample rule)."""
    k = lc(k).lower()
    if k.endswith("nti") and len(k) > 4:
        k = k[:-3] + "ṃ"
    elif len(k) > 4 and k.endswith("ti") and k[-3] in "āīūoe":
        k = k[:-2]
    for p in ("ñceva", "ñca"):
        if k.endswith(p):
            return k[: -len(p)] + "ṃ"
    return k


def member_value(kw, members=None):
    """A member keyword of a yamaka (default: KHANDHA), any -ti / -ñca / -ñceva form; None if not a member."""
    members = KHANDHA if members is None else members
    k = lc(kw).lower()
    if k in members:
        return members[k]
    k2 = _strip_particles(kw)
    if k2 in members:
        return members[k2]
    return None


# ---------------------------------------------------------------------------- the pavatti verbs
# The value is the verb with its tense / aspect word; polarity only where it is fused in the keyword (nuppajjati);
# a separate «na» keeps «không» for itself where the text has «không» (na nirujjhati «không chấm dứt» -> nirujjhati =
# chấm dứt; na nirujjhissati «sẽ không chấm dứt» -> nirujjhissati = sẽ … chấm dứt) and has none in the past
# («chưa từng chấm dứt» -> nirujjhittha = chưa từng chấm dứt). After «no ca» the denied negative is said plainly
# («vẫn sinh khởi», «đã từng sinh khởi», «vẫn sẽ sinh khởi»); a denied positive takes «không» from no
# (uppajjati = sinh khởi), «chưa từng» in the past. Short answers «Có sinh khởi.» / «Đã sinh khởi.»: the emphatic
# «Có» is frame.
VERB_STEMS = {"uppajj": "sinh khởi", "nirujjh": "chấm dứt"}
_TENSE = {"ati": "pres", "anti": "pres", "ittha": "past", "iṃsu": "past", "issati": "fut", "issanti": "fut"}
VERB_FORMS = {
    # (polarity, tense) -> template; polarity: pos, neg (fused n-), na (separate na), noca_pos, noca_neg
    ("pos", "pres"): "{v}", ("pos", "past"): "đã {v}", ("pos", "fut"): "sẽ {v}",
    ("neg", "pres"): "không {v}", ("neg", "past"): "chưa từng {v}", ("neg", "fut"): "sẽ không {v}",
    ("na", "pres"): "{v}", ("na", "past"): "chưa từng {v}", ("na", "fut"): "sẽ" + GAP + "{v}",
    ("noca_pos", "pres"): "{v}", ("noca_pos", "past"): "chưa từng {v}", ("noca_pos", "fut"): "sẽ" + GAP + "{v}",
    ("noca_neg", "pres"): "vẫn {v}", ("noca_neg", "past"): "đã từng {v}", ("noca_neg", "fut"): "vẫn sẽ {v}",
}


def _verb_parse(kw):
    """(stem, tense, fused_negative) of a pavatti verb keyword (-ti of the question dropped), else None."""
    k = lc(kw).lower()
    if len(k) > 4 and k.endswith("ti") and k[-3] in "āī":
        k = k[:-3] + {"ā": "a", "ī": "i"}[k[-3]]
    neg = False
    for stem in VERB_STEMS:
        if k.startswith("n" + stem):
            neg, rest = True, k[len(stem) + 1:]
        elif k.startswith(stem):
            rest = k[len(stem):]
        else:
            continue
        if rest in _TENSE:
            return stem, _TENSE[rest], neg
    return None


def verb_vi(stem, tense, polarity):
    return VERB_FORMS[(polarity, tense)].format(v=VERB_STEMS[stem])


PAVATTI = {}
for _st in VERB_STEMS:
    for _end, _t in _TENSE.items():
        PAVATTI[_st + _end] = verb_vi(_st, _t, "pos")
        PAVATTI["n" + _st + _end] = verb_vi(_st, _t, "neg")


def verb_value(kw, pali):
    """The value of a pavatti verb keyword from its FIRST occurrence in the Pāli segment (bare or question -ti form,
    whichever comes first: the first-rendering rule of map-coordinator-rules.md): fused n- (nuppajjati), a separate
    «na» before it, inside a «no ca …» clause (up to the clause end), or plain. None if not a verb."""
    p = _verb_parse(kw)
    if not p:
        return None
    stem, tense, neg = p
    pol = "neg" if neg else "pos"
    if pali:
        m = None
        if kw[:1].isupper():                       # a short answer «Uppajjati.» is its own keyword
            m = re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali)
        if not m:
            # the first rendering in the segment (coordinator): the bare verb and its question -ti form are one verb
            # in the Vietnamese, so the earliest of the two counts («… uppajjitthāti? … no ca … uppajjittha» = đã …)
            k = lc(kw).lower()
            if len(k) > 4 and k.endswith("ti") and k[-3] in "āī":
                forms = [k, k[:-3] + {"ā": "a", "ī": "i"}[k[-3]]]
            else:
                forms = [k, k[:-1] + {"a": "ā", "i": "ī"}.get(k[-1], k[-1]) + "ti"]
            hits = [x for x in (re.search(r"(?<!\w)" + re.escape(f) + r"(?!\w)", pali, re.I) for f in forms) if x]
            m = min(hits, key=lambda x: x.start()) if hits else None
        if m:
            before = pali[: m.start()]
            clause = re.split(r"[.?!,;\n]", before)[-1]   # «no ca» reaches to the clause end (comma included:
                                                          # 8 «… no ca tassa cittaṃ uppannaṃ, tassa cittaṃ …»)
            noca = re.search(r"(?<!\w)no ca(?!\w)", clause) is not None
            sep_na = re.search(r"(?<!\w)na\s+$", before) is not None
            if noca:
                pol = "noca_neg" if (neg or sep_na) else "noca_pos"
            elif sep_na and not neg:
                pol = "na"
    return verb_vi(stem, tense, pol)


# ---------------------------------------------------------------------------- planes and beings
# plane stem -> «cõi …» (accusative upapajjantānaṃ «tái sinh vào cõi …», locative «Trong cõi …», ablative
# cavantānaṃ «chết đi khỏi cõi …»: «vào», «trong», «khỏi» are the case frame); -ānaṃ (the beings) = «chúng sinh …»
# as the text writes it (asaññasattānaṃ «chúng sinh Vô Tưởng», arūpānaṃ «chúng sinh trong cõi không hình sắc»).
PLANES = {
    "asaññasatt": "cõi Vô Tưởng", "arūp": "cõi không hình sắc",
    "pañcavokār": "cõi gồm năm khối", "catuvokār": "cõi gồm bốn khối", "ekavokār": "cõi gồm một khối",
    "suddhāvās": "cõi Tịnh Cư",
}
BEINGS = {s: ("chúng sinh Vô Tưởng" if s == "asaññasatt" else "chúng sinh trong " + v) for s, v in PLANES.items()}
_PLANE_END = ("aṃ", "e", "ā", "a", "esu")
_PLANE_ORDER = sorted(PLANES, key=len, reverse=True)


def _plane_stem(word):
    k = lc(word).lower()
    for s in _PLANE_ORDER:
        if k.startswith(s):
            end = k[len(s):]
            if end == "ānaṃ" or end in _PLANE_END:
                return s, end
            return None
    return None


def plane_candidates(kw):
    p = _plane_stem(kw)
    if not p:
        return None
    s, end = p
    if end == "ānaṃ":
        return [BEINGS[s], PLANES[s]]
    return [PLANES[s], BEINGS[s]]


def _first(kw, pali):
    if not pali:
        return None
    m = re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali)
    return m or re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali, re.I)


def _after_itaresam(kw, pali):
    """True if the keyword's first occurrence stands in «Itaresaṃ <P>ānaṃ [<P>ānaṃ …]» («Ở những chúng sinh khác
    trong cõi gồm bốn khối, cõi gồm năm khối»: «chúng sinh» is the head of the whole group, taken by itaresaṃ)."""
    m = _first(kw, pali)
    if not m:
        return False
    words = re.split(r"[.?!\n]", pali[: m.start()])[-1].split()
    while words and (_plane_stem(words[-1]) or (None, ""))[1] == "ānaṃ":
        words.pop()
    return bool(words) and lc(words[-1]).lower() == "itaresaṃ"


def plane_value(kw, text, pali=None):
    c = plane_candidates(kw)
    if not c:
        return None
    if c[0].startswith("chúng sinh") and _after_itaresam(kw, pali):
        c = [c[1]] + c
    return pick(text, *c)


def itaresam_value(pali, text):
    """itaresaṃ alone «những người khác» = người khác; before the beings «Itaresaṃ pañcavokārānaṃ» «những chúng sinh
    khác trong cõi gồm năm khối» = chúng sinh khác (head noun + khác; the plane keyword then takes «cõi …»)."""
    m = _first("Itaresaṃ", pali) or _first("itaresaṃ", pali)
    if m:
        nxt = pali[m.end():].split()
        if nxt and (_plane_stem(nxt[0]) or (None, ""))[1] == "ānaṃ":
            return pick(text, "chúng sinh khác", "người khác")
    return pick(text, "người khác", "chúng sinh khác")


# ---------------------------------------------------------------------------- persons and participles
# «những người …»: the leading «những» is frame (pi-4); the head noun «người» / «chúng sinh» is kept where it is the
# keyword's own word (pacchimabhavikānaṃ «những người thuộc kiếp sống cuối cùng», itaresaṃ «những người khác»).
PERSONS = {
    "pacchimabhavikānaṃ": "người thuộc kiếp sống cuối cùng",
    "itaresaṃ": "người khác",                      # context: «những chúng sinh khác» where the text has it
    "upapajjantānaṃ": "đang tái sinh", "cavantānaṃ": "đang chết đi",
    "parinibbantānaṃ": "đang nhập Niết-bàn trọn vẹn",
    "upapajjitvā": "sau khi tái sinh",             # gerund keeps «sau khi» (pi-5 coordinator)
    "parinibbāyissanti": "sẽ nhập Niết-bàn trọn vẹn",
    "parinibbāyanti": "nhập Niết-bàn trọn vẹn",
    "sabbesaṃ": "tất cả",                          # Sabbesaṃ cavantānaṃ «Ở tất cả những người đang chết đi»
}

# ---------------------------------------------------------------------------- the person / place relatives
# «(a) Ở người nào mà A …, thì ở người ấy có phải B … không? (b) Còn ở người nào mà …»; «Ở nơi nào mà …, thì ở nơi
# ấy …»; «Ở người nào, ở nơi nào mà …, thì ở người ấy, ở nơi ấy …» (7-01 shape). The case word «ở» is frame for the
# pronouns, kept for the place adverbs; commas dropped inside a value (pi-1).
RELATIVES = {
    "yassa": "người nào", "tassa": "người ấy", "yassa vā pana": "còn" + GAP + "người nào",
    "yattha": "ở nơi nào", "tattha": "ở nơi ấy", "yattha vā pana": "còn ở nơi nào",
    "yassa yattha": "người nào ở nơi nào", "tassa tattha": "người ấy ở nơi ấy",
    "yassa vā pana yattha": "còn" + GAP + "người nào ở nơi nào",
    "tesaṃ": "người ấy", "tesaṃ tattha": "người ấy ở nơi ấy",
    "ye": "người nào",                             # Ye arūpaṃ upapajjitvā … «Những người nào …» (context: pavatti)
}

# ---------------------------------------------------------------------------- headings of this chapter
HEADINGS = {
    "paṇṇattiuddesavāro": "mục nêu đề mục về sự định danh",
    "paṇṇattiniddesavāro": "mục giải thích về sự định danh",
    "pavatti": "sự diễn tiến",                     # «Sự diễn tiến 2. mục về sự chấm dứt»
}

T201 = {**KHANDHA, **PAVATTI, **PERSONS, **HEADINGS}


def frames201(kw, kws, vi, pi, members=None):
    """The 2-01 segment rules (members, verbs, planes, persons, relatives). None = no rule."""
    k = lc(kw).lower()
    v = member_value(kw, members)
    if v is not None and present(v, vi):           # members only where the segment has them (rūpaṃ = hình sắc
        return v                                   # in the āyatana chapters falls through)
    v = verb_value(kw, pi)
    if v is not None:
        return v
    if plane_candidates(kw):
        v = plane_value(kw, vi, pi)
        if v:
            return v
    if k == "itaresaṃ":
        return itaresam_value(pi, vi) or PERSONS[k]
    if k in PERSONS:
        return PERSONS[k]
    if k == "ye" and present("người nào", vi) and not present("bất cứ", vi):
        return RELATIVES["ye"]
    if k in RELATIVES and k != "ye":
        return RELATIVES[k]
    if k in HEADINGS:
        return HEADINGS[k]
    return None


def value201(kw, kws, vi, pi, table=None, members=None):
    """your table -> the 2-01 frames -> map_sample_vi.value6 (context6 -> FORMULAS -> YM -> compose -> pi-5 chain)."""
    k = lc(kw)
    if table and k in table:
        return table[k]
    v = frames201(kw, kws, vi, pi, members)
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
        return value201(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
