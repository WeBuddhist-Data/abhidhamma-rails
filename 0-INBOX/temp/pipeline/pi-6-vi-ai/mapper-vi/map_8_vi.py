"""Build the Pāli->Vietnamese keyword map of pi-6 8-cittayamaka (Cittayamaka), and expose the family-D frame tables.

usage: python -I -X utf8 -B map_8_vi.py                      (writes 8-cittayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_8_vi.py dump [miss]          (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_8_vi.py show lo hi [pi]      (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing. Frame-setter of the aspect forms and the citta kinds (map-coordinator-rules.md):
later chapters load it with importlib and reuse its named tables / helpers:
    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("map_8_vi", pathlib.Path(__file__).with_name("map_8_vi.py"))
    C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    C.TENSE, C.ASPECT, C.ASPECT_NOUN, C.MOMENT, C.TIME, C.KIND, C.PERSONS8, C.HEAD8
    C.tense_value(kw, text), C.aspect_value(kw, text), C.citta_value(kw), C.moment_value(kw, text),
    C.vara_value(kw), C.value8(kw, kws, table, text)
Resolution order per keyword: OVERRIDES[bid][kw] -> value8(): your table -> T8 (fixed values of this chapter) ->
the family-D rules (tense / aspect / moment / time / citta kinds / headings) -> map_sample_vi.value6 (context6 ->
FORMULAS -> YM -> compose -> the pi-5 chain).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md; the Vietnamese frames of notes-8.md / build_8_vi.py.
"""
import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_sample_vi as S  # noqa: E402
from map_common_vi import (GAP, NDE, build_part, en, pick, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

PART = "8-cittayamaka"

# ---------------------------------------------------------------------------- tense of uppajjati / nirujjhati
# the value is the verb with its tense word (pi-6 conventions: polarity only where fused in the keyword, i.e. «không»
# belongs to the separate na). Where the segment has the form only inside a negative («sẽ không sinh khởi»), the
# tense word and the verb are joined with « … » (the na between them is not part of the keyword).
TENSE = {
    "uppajjati": "sinh khởi", "uppajjittha": "đã sinh khởi", "uppajjissati": "sẽ sinh khởi",
    "nirujjhati": "chấm dứt", "nirujjhittha": "đã chấm dứt", "nirujjhissati": "sẽ chấm dứt",
}
# the same with the negation fused into the keyword (2-01 proposals in map_sample_vi.FORMULAS)
TENSE_NEG = {
    "nuppajjati": "không sinh khởi", "nuppajjittha": "chưa từng sinh khởi", "nuppajjissati": "sẽ không sinh khởi",
    "nanirujjhati": "không chấm dứt", "nanirujjhittha": "chưa từng chấm dứt", "nanirujjhissati": "sẽ không chấm dứt",
}

# ---------------------------------------------------------------------------- aspect forms (participles)
# stem -> predicate value («tâm đang sinh khởi», «tâm ở trạng thái đã sinh khởi»); uppanna / niruddha keep «ở trạng
# thái» (8-cittayamaka: arisen and not yet ceased, kept apart from uppajjittha «đã sinh khởi»); the second
# candidate is the plain pi-2 value for chapters whose text has no «ở trạng thái»
ASPECT = {
    "uppajjamāna": ["đang sinh khởi"],
    "nirujjhamāna": ["đang chấm dứt"],
    "uppanna": ["ở trạng thái đã sinh khởi", "đã sinh khởi"],
    "niruddha": ["ở trạng thái đã chấm dứt", "đã chấm dứt"],
}
# the same as nouns in the section headings («Mục về trạng thái đang sinh khởi và sự không chấm dứt»)
ASPECT_NOUN = {
    "uppajjamāna": "trạng thái đang sinh khởi", "nirujjhamāna": "trạng thái đang chấm dứt",
    "uppanna": "trạng thái đã sinh khởi", "niruddha": "trạng thái đã chấm dứt",
    "uppāda": "sự sinh khởi", "nirodha": "sự chấm dứt", "nanirodha": "sự không chấm dứt",
    "atīta": "quá khứ", "anāgata": "tương lai", "paccuppanna": "hiện tại",
}

# ---------------------------------------------------------------------------- moments and the time of the citta
MOMENT = {
    "uppādakkhaṇa": "khoảnh khắc sinh khởi", "bhaṅgakkhaṇa": "khoảnh khắc tan rã",   # pi-5
    "nirodhakkhaṇa": "khoảnh khắc chấm dứt",                                            # proposal (not in 8)
    "khaṇa": "khoảnh khắc",
    "atikkantakāla": "thời của nó đã qua",                                              # (14) frame
    "vītikkanta": "đã vượt qua", "avītikkanta": "chưa vượt qua",
}
# Atītaṃ / Anāgataṃ / Paccuppannaṃ cittaṃ «Tâm thuộc quá khứ / tương lai / hiện tại» (pi-1 / pi-2)
TIME = {
    "atīta": "thuộc quá khứ", "anāgata": "thuộc tương lai", "paccuppanna": "thuộc hiện tại",
    "atītānāgata": "thuộc quá khứ và tương lai",
}

# ---------------------------------------------------------------------------- the citta kinds
# K in «tâm <K>» (pi-1 / pi-2 values, notes-8 KIND); pacchima «cuối cùng» stands after the kind
KIND = {
    "kusala": "thiện", "akusala": "bất thiện", "abyākata": "không xác định về mặt đạo đức",
    "sarāga": "có tham đắm", "vītarāga": "đã lìa tham đắm", "sadosa": "có sân hận", "vītadosa": "đã lìa sân hận",
    "samoha": "có si mê", "vītamoha": "đã lìa si mê", "saṃkhitta": "co rút", "vikkhitta": "tán loạn",
    "mahaggata": "rộng lớn", "amahaggata": "không rộng lớn", "sauttara": "còn có điều cao hơn",
    "anuttara": "không có điều gì cao hơn", "samāhita": "được định tâm", "asamāhita": "không được định tâm",
    "vimutta": "được giải thoát", "avimutta": "không được giải thoát",
    "saraṇa": "có xung đột", "araṇa": "không có xung đột",
    "pacchima": "cuối cùng",
}
# «tâm gắn liền với cảm giác X» (pi-1 matrix / pi-2): sukhāya vedanāya sampayuttaṃ = the three keywords
FEELING = {"sukhāya": "dễ chịu", "dukkhāya": "khó chịu", "adukkhamasukhāya": "không khó chịu cũng không dễ chịu"}
_KIND_ORDER = sorted(KIND, key=len, reverse=True)

# ---------------------------------------------------------------------------- persons of the answers
# «Ở những người …»: «Ở» (case) and the leading «những» are frame (pi-6 / pi-4 tesaṃ «người ấy»)
PERSONS8 = {
    "itaresaṃ": "người khác",
    "nirodhasamāpannānaṃ": "người nhập thành tựu thiền chấm dứt",   # pi-5 «thành tựu thiền chấm dứt»
    "asaññasattānaṃ": "chúng sinh Vô Tưởng",                         # sample FORMULAS
}

# ---------------------------------------------------------------------------- headings and editorial lines
HEAD8 = {
    "suddhacittasāmaññaṃ": "tâm thuần túy nói chung", "suddhacittasāmañña": "tâm thuần túy nói chung",
    "puggalavāro": "mục về người", "dhammavāro": "mục về hiện tượng",
    "puggaladhammavāro": "mục về người và hiện tượng",
    "uppādanirodhakālasambhedavāro": "mục về sự kết hợp các thời của sự sinh khởi và sự chấm dứt",
    "nanirodhavāro": "mục về" + GAP + "sự không chấm dứt",           # of Uppajjamāna-nanirodhavāro (inner «và» frame)
    "atikkantakālavāro": "mục về thời đã qua",
    "suttantacittamissakaviseso": "trường hợp đặc biệt kết hợp với các loại tâm theo kinh",
    "abhidhammacittamissakaviseso": "trường hợp đặc biệt kết hợp với các loại tâm theo Vi Diệu Pháp",
    "yamakāni": "phần",                                              # tīṇi yamakāni «Ba phần» (numeral dropped)
    "saraṇaaraṇā": "loại có xung đột và không có xung đột",          # «các loại …» (leading «các» dropped)
    "cittake": "tâm",                                                # «Phần về tâm ở người nào …»
    "(no direct equivalent)": NDE,                                   # placeholder keyword with no Pāli word
}

# the yamaka titles inside running text («(Ba phần, các cặp câu hỏi về gốc rễ, các cặp câu hỏi về tâm và …)»): lower
# case as written (sample rule for the closers); in a # heading the title keeps «Các» (map_sample_vi.FORMULAS)
TITLE_RUNNING = {k: v[:1].lower() + v[1:] for k, v in S.FORMULAS.items() if k.endswith("yamakaṃ")}

# fixed values of this chapter (checked against the segments; the rules below give the rest)
T8 = {**HEAD8, **PERSONS8,
      "cittaṃ": "tâm", "citta": "tâm",
      "sampayuttaṃ": "gắn liền", "vedanāya": "cảm giác"}


# ---------------------------------------------------------------------------- helpers
def norm(k):
    """Lower-case keyword without the question -ti and the particles -ñca / -ñceva («uppajjissatīti» ->
    «uppajjissati», «uppajjitthāti» -> «uppajjittha», «uppannanti» / «uppannañceva» -> «uppannaṃ»)."""
    k = k.lower()
    if k.endswith("īti") and len(k) > 5:
        return k[:-3] + "i"
    if k.endswith("āti") and len(k) > 5:
        return k[:-3] + "a"
    if k.endswith("nti") and len(k) > 5:
        return k[:-3] + "ṃ"
    for p in ("ñceva", "ñca"):
        if k.endswith(p) and len(k) > len(p) + 3:
            return k[: -len(p)] + "ṃ"
    return k


_ENDS = ("ānaṃ", "āni", "aṃ", "ā", "o", "e", "a", "ena", "assa", "āya", "ehi", "esu", "")


def _stem(k, stems=None):
    """(stem ending in -a, ending) of an -a stem keyword; with `stems`, only a stem of that collection (longest
    first), so that «uppajjamānaṃ» is uppajjamāna + aṃ, not uppajjama + ānaṃ."""
    if stems is not None:
        for s in sorted(stems, key=len, reverse=True):
            if k.startswith(s[:-1]) and k[len(s) - 1:] in _ENDS:
                return s, k[len(s) - 1:]
        return k, None
    for e in _ENDS[:-1]:
        if k.endswith(e) and len(k) > len(e) + 2:
            return k[: -len(e)] + "a", e
    return k, ""


# Polarity of the keyword's FIRST occurrence in the Pāli segment (the 2-01 rule, map_2-01_vi.VERB_FORMS, copied here
# so that this module does not depend on a chapter still being mapped): pos = plain; neg = n- fused in the keyword;
# na = a separate na before it (its «không» is not part of the value; in the past «chưa từng» fuses both); noca_pos /
# noca_neg = inside a «no ca …» clause, the denied positive / the denied negative said plainly («vẫn …»).
TENSE_FORMS = {
    ("pos", "pres"): "{v}", ("pos", "past"): "đã {v}", ("pos", "fut"): "sẽ {v}",
    ("neg", "pres"): "không {v}", ("neg", "past"): "chưa từng {v}", ("neg", "fut"): "sẽ không {v}",
    ("na", "pres"): "{v}", ("na", "past"): "chưa từng {v}", ("na", "fut"): "sẽ" + GAP + "{v}",
    ("noca_pos", "pres"): "{v}", ("noca_pos", "past"): "chưa từng {v}", ("noca_pos", "fut"): "sẽ" + GAP + "{v}",
    ("noca_neg", "pres"): "vẫn {v}", ("noca_neg", "past"): "đã từng {v}", ("noca_neg", "fut"): "vẫn sẽ {v}",
}
VERBS = {"uppajj": "sinh khởi", "nirujjh": "chấm dứt"}
_TENSE_END = {"ati": "pres", "anti": "pres", "ittha": "past", "iṃsu": "past", "issati": "fut", "issanti": "fut"}


def polarity(kw, pali):
    """pos / na / noca_pos / noca_neg of the keyword's first occurrence in the Pāli segment (pos without Pāli)."""
    if not pali:
        return "pos"
    m = re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali) or \
        re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali, re.I)
    if not m:
        return "pos"
    before = pali[: m.start()]
    # the «no ca» clause ends at a comma too: «yassa cittaṃ uppajjittha no ca tassa cittaṃ uppannaṃ, tassa cittaṃ
    # uppajjissatīti?» (question (11)) asks about a plain «sẽ sinh khởi»
    clause = re.split(r"[.?!,\n]", before)[-1]
    sep_na = re.search(r"(?<!\w)na\s+$", before) is not None
    if re.search(r"(?<!\w)no ca(?!\w)", clause):
        return "noca_neg" if sep_na else "noca_pos"
    return "na" if sep_na else "pos"


def _load_201():
    spec = importlib.util.spec_from_file_location("pi6_map_2_01_vi",
                                                  pathlib.Path(__file__).resolve().with_name("map_2-01_vi.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


F201 = _load_201()


def tense_value(kw, text, pali=None):
    """uppajjati / uppajjittha / uppajjissati / nirujjhati … (with -ti, with fused n-): always the current
    map_2-01_vi.verb_value (coordinator rule: no local tense override). None if not a pavatti verb."""
    return F201.verb_value(kw, pali or "")


def aspect_value(kw, text, heading=False, pali=None):
    """uppajjamāna / nirujjhamāna / uppanna / niruddha in any case (-aṃ, -ā, -ānaṃ …, with -ti / -ñca / -ñceva):
    the predicate value («đang sinh khởi», «ở trạng thái đã sinh khởi»; «vẫn …» where the first occurrence is the
    denied negative of a «no ca» clause, as the tenses); the noun («trạng thái đang sinh khởi») for the bare stem of
    a heading member. None if not an aspect form."""
    k = norm(kw)
    stem, end = _stem(k, ASPECT)
    if stem not in ASPECT:
        return None
    cands = list(ASPECT[stem])
    if heading or end in ("", "a"):
        cands = [ASPECT_NOUN[stem]] + cands
    elif polarity(kw, pali) == "noca_neg":
        cands = ["vẫn " + c for c in cands] + cands
    return pick(text, *cands) or cands[0]


def citta_value(kw):
    """X-cittassa / X-cittaṃ / X-citta (X = kinds, pacchima) -> «tâm <kind> [cuối cùng]» (Pacchimacittassa «tâm cuối
    cùng», Sarāgapacchimacittassa «tâm có tham đắm cuối cùng», Pacchimakusalacittassa «tâm thiện cuối cùng»);
    X-cittasamaṅgīnaṃ -> «người có được tâm …». None if not one."""
    k = norm(kw)
    person = False
    for s in ("samaṅgīnaṃ", "samaṅgī", "samaṅgino"):
        if k.endswith(s):
            k, person = k[: -len(s)], True
            break
    for e in ("assa", "aṃ", "ā", "āni", "a"):
        if k.endswith("citt" + e):
            pre = k[: -len("citt" + e)]
            break
    else:
        return None
    kinds, last = [], False
    while pre:
        for x in _KIND_ORDER:
            if pre.startswith(x):
                if x == "pacchima":
                    last = True
                else:
                    kinds.append(KIND[x])
                pre = pre[len(x):]
                break
        else:
            return None
    v = " ".join(["tâm"] + kinds + (["cuối cùng"] if last else []))
    return ("người có được " + v) if person else v


def moment_value(kw, text):
    """uppādakkhaṇa / bhaṅgakkhaṇa / khaṇa (any case, with -ñca) = «khoảnh khắc …» («Vào» of the locative is frame);
    «<X>cittassa uppādakkhaṇe» = «khoảnh khắc sinh khởi của <citta>». None if not a moment keyword."""
    words = kw.split()
    if len(words) == 2:
        m = moment_value(words[1], text)
        c = citta_value(words[0])
        if m and c:
            return m + " của " + c
        return None
    k = norm(kw)
    stem, _ = _stem(k, MOMENT)
    if stem in MOMENT:
        return MOMENT[stem]
    return None


def time_value(kw):
    """Atītaṃ / anāgatañca / Paccuppannaṃ / Atītānāgataṃ (cittaṃ) = «thuộc quá khứ» …"""
    stem, _ = _stem(norm(kw), TIME)
    return TIME.get(stem)


_VARA_TOKENS = sorted(ASPECT_NOUN, key=len, reverse=True)


def vara_value(kw):
    """<A><B>vāro section titles built from aspect / time members = «mục về <A> và <B>» (Uppāduppannavāro «mục về sự
    sinh khởi và trạng thái đã sinh khởi», Uppajjamānananirodhavāro «… trạng thái đang sinh khởi và sự không chấm
    dứt»); the final -a of a member drops before u- (uppāda + uppanna = uppāduppanna). None if not parseable."""
    k = kw.lower().replace("-", "")
    if not k.endswith("vāro"):
        return None
    s, i, parts = k[:-4], 0, []
    while i < len(s):
        for t in _VARA_TOKENS:
            if s.startswith(t, i):
                parts.append(ASPECT_NOUN[t])
                i += len(t)
                break
            if t.endswith("a") and s.startswith(t[:-1], i) and s[i + len(t) - 1: i + len(t)] == "u":
                parts.append(ASPECT_NOUN[t])
                i += len(t) - 1
                break
        else:
            return None
    if not parts:
        return None
    return "mục về " + " và ".join(parts)


def _after_itaresam(kw, pali):
    """True if the keyword's first occurrence in the Pāli stands right after «Itaresaṃ» / «itaresaṃ»."""
    if not pali:
        return False
    m = re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali)
    return bool(m) and re.search(r"(?<!\w)[Ii]taresaṃ\s+$", pali[: m.start()]) is not None


def value8(kw, kws, table=None, text=None, pali=None):
    """table -> T8 -> family-D rules -> map_sample_vi.value6 (pali = the Pāli segment, for the polarity rule)."""
    t = text or ""
    kl = kw.lower()
    if table and kl in table:
        return table[kl]
    if kl in T8:
        return T8[kl]
    if norm(kw) in T8:                             # -ti of the question / -ñca dropped («dhammayamakanti»)
        return T8[norm(kw)]
    heading = t.lstrip().startswith("#")
    if norm(kw) in TITLE_RUNNING and not heading:
        return TITLE_RUNNING[norm(kw)]
    for fn in (lambda: tense_value(kw, t, pali), lambda: moment_value(kw, t), lambda: citta_value(kw),
               lambda: time_value(kw), lambda: vara_value(kw)):
        v = fn()
        if v:
            if v.startswith("người ") and _after_itaresam(kw, pali):
                return v[len("người "):]           # «Ở những người khác có được tâm»: the head goes to Itaresaṃ (2-01)
            return v
    v = aspect_value(kw, t, heading, pali)
    if v:
        return v
    k = norm(kw)
    if k in KIND:
        return KIND[k]
    stem, _ = _stem(k, KIND)
    if stem in KIND and stem != "pacchima":
        return KIND[stem]
    if k in FEELING:
        return FEELING[k]
    return S.value6(kw, kws, table, t)


# part-specific values
T8_PART = {}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi, pi = read_vietnamese(PART), read_pali(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value8(kw, kws, T8_PART, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
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


def show(lo, hi, with_pali=False):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            e = en(bid)
            out = []
            for kw in kws:
                v = res(bid, kw, kws)
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v} [{e.get(kw, '')}]{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
