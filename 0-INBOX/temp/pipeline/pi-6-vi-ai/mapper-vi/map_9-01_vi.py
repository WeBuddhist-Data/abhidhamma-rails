"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 9-01-dhammayamaka (Dhammayamaka: paṇṇattivāra, pavattivāra /
uppādavāra), and the FRAME TABLES of the Dhammayamaka for the later chapters 9-02 and 9-03.

usage: python -I -X utf8 -B map_9-01_vi.py                  (writes 9-01-dhammayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_9-01_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_9-01_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. 9-02 / 9-03 load it with importlib:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\mapper-vi")
    D = importlib.import_module("map_9-01_vi")
    D.DHAMMA_ADJ      kusala «thiện», akusala «bất thiện», abyākata «không xác định về mặt đạo đức» (predicate / attribute)
    D.DHAMMA_NOUN     the same as nouns «hiện tượng thiện» … (subject, «các hiện tượng thiện» with «các» dropped)
    D.DHAMMA9         every fixed member form: kusalā / kusalāti = thiện; kusalā dhammā / dhammāti / ca dhammā /
                      dhammaṃ / dhamme / kusalānaṃ = hiện tượng thiện; dhammā / dhamme / dhammaṃ alone = hiện tượng
    D.dhamma_value(kw, vi, pi)   any member keyword (one to three words); the -aṃ / -añca forms (kusalaṃ, Kusalañca)
                      by their FIRST occurrence in the segment (user decision for the sample): the noun where it is the
                      object of ṭhapetvā or stands before dhammaṃ («Ngoại trừ hiện tượng thiện»), else the sample rule
                      (predicate «không phải là thiện» = thiện); «Kusalañca dhamme» = «hiện tượng thiện và các hiện
                      tượng» (connective «và» kept, pi-1 rūpañca nibbānañca); «hiện tượng … X» where the text splits it
    D.CITTA_KIND9     kusalavippayutta «không gắn liền với các hiện tượng thiện» (and akusala-, the two-member chains)
    D.OWNER9          kusalānaṃ / akusalānaṃ / abyākatānaṃ as the owner of a moment = «các hiện tượng …» (inner «các»
                      kept: «khoảnh khắc sinh khởi của các hiện tượng thiện»)
    D.citta9(word), D.moment9(kw, text)   «tâm <kind>», «khoảnh khắc sinh khởi / tan rã của <owner>» (8 / 5-01 rule:
                      the «vào» of the locative is frame); other owners via map_5-01_vi.NOUN_OF / citta5 / map_8_vi
    D.BHAVANA_STEMS   bhāve «tu tập», pajah «dứt bỏ» (bhāvanāvāra, 9-03 ^6-9-229; proposal checked against that
                      segment); D.BHAVANA every fixed form; D.bhavana_value(kw, pali) by the polarity of the verb's
                      first occurrence (the 2-01 rule, map_2-01_vi.VERB_FORMS: a separate na keeps «không» for itself,
                      fused nappajahati = «không dứt bỏ»)
    D.HEAD9           Suddhadhammavāro, Suddhadhammamūlacakkavāro, Bhāvanāvāro, Paṇṇattiniddesavāro, the placeholder
    D.T901            all fixed values merged (lower-case keys)
    D.value901(kw, kws, vi, pi, table=None)
                      your table -> T901 -> dhamma_value -> moment9 / citta9 -> bhavana_value -> map_5-01_vi tables
                      (persons, planes, path verbs, moment owners) -> map_2-01_vi.value201 (verbs by the 2-01
                      first-occurrence rule, planes / beings, itaresaṃ, relatives) -> map_sample_vi.value6
Values are the words of the zero-shot translation; the translation file is the truth, so every later chapter checks
them against its segments (the presence check does).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-2-02.md, notes-map-8.md,
notes-map-5-01.md, notes-map-9-01.md.
"""
import importlib
import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_common_vi import (GAP, NDE, build_part, en, lc, pick, present, present_strict, read_keywords,  # noqa: E402
                           read_pali, read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = importlib.import_module("map_2-01_vi")          # shared pavatti frames (verbs, planes, beings, relatives)
P = importlib.import_module("map_2-02_vi")          # pariññā verbs and persons (paṭilabhissanti)
C = _load("map_8_vi", "map_8_vi.py")                # moments, citta kinds, aspect forms
T5 = importlib.import_module("map_5-01_vi")         # citta5, moment5, PERSONS5, PLANES5 (pavatte), PATH, NOUN_OF

PART = "9-01-dhammayamaka"

# ---------------------------------------------------------------------------- the Dhammayamaka members
# «(a) Những gì là thiện có phải là các hiện tượng thiện không?» (kusalā kusalā dhammā?): the bare adjective is the
# predicate («là» dropped, pi-1), «X dhammā» the noun «hiện tượng X» (leading «các» dropped, pi-1 dhammā kusalā)
DHAMMA_ADJ = {"kusala": "thiện", "akusala": "bất thiện", "abyākata": "không xác định về mặt đạo đức"}
DHAMMA_NOUN = {x: "hiện tượng " + v for x, v in DHAMMA_ADJ.items()}
_X_ORDER = sorted(DHAMMA_ADJ, key=len, reverse=True)
DHAMMA9 = {"dhammā": "hiện tượng", "dhamme": "hiện tượng", "dhammaṃ": "hiện tượng", "dhammo": "hiện tượng",
           "dhammānaṃ": "hiện tượng", "dhammāti": "hiện tượng"}
for _x in DHAMMA_ADJ:
    _b = _x[:-1]                                    # kusal-
    DHAMMA9[_b + "ā"] = DHAMMA_ADJ[_x]
    DHAMMA9[_b + "āti"] = DHAMMA_ADJ[_x]
    DHAMMA9[_b + "ānaṃ"] = DHAMMA_NOUN[_x]          # «của các hiện tượng thiện» alone: leading «các» dropped
    for _d, _e in (("dhammā", "ā"), ("dhammāti", "ā"), ("dhammaṃ", "aṃ"), ("dhamme", "e"), ("dhammo", "o"),
                   ("dhammānaṃ", "ānaṃ")):
        DHAMMA9[_b + _e + " " + _d] = DHAMMA_NOUN[_x]
        DHAMMA9[_b + _e + " ca " + _d] = DHAMMA_NOUN[_x]   # abyākatā ca dhammā «đồng thời các hiện tượng … cũng …»
    DHAMMA9[_b + "añca dhamme"] = DHAMMA_NOUN[_x] + " và các hiện tượng"   # Kusalañca dhamme ca ṭhapetvā


def _norm(kw):
    return " ".join(lc(w).lower() for w in kw.split())


def _first_pali(word, pali):
    """the first word-bounded occurrence of `word` (case-insensitive) in the Pāli segment, or None."""
    if not pali:
        return None
    return re.search(r"(?<!\w)" + re.escape(word) + r"(?!\w)", pali, re.I)


def _noun_by_position(word, pali):
    """True where the -aṃ / -añca form's first occurrence is a noun: the object of ṭhapetvā («Kusalaṃ ṭhapetvā»,
    «Kusalañca dhamme ca ṭhapetvā») or the attribute of dhammaṃ («kusalaṃ dhammaṃ bhāveti»)."""
    m = _first_pali(word, pali)
    if not m:
        return False
    nxt = re.split(r"[.?!,;\n]", pali[m.end():])[0].split()
    return bool(nxt) and (nxt[0].lower() in ("ṭhapetvā", "dhammaṃ")
                          or nxt[:3] == ["dhamme", "ca", "ṭhapetvā"])


def dhamma_value(kw, vi, pi=None):
    """A Dhammayamaka member keyword (kusalā, kusalāti, kusalā dhammā, kusalā dhammāti, kusalā ca dhammā, Kusalaṃ,
    Kusalañca, Kusalañca dhamme, kusalānaṃ, dhammā …) as the segment writes it; None if not one."""
    k = _norm(kw)
    words = k.split()
    stem = None
    if len(words) == 1:
        w = words[0]
        for x in _X_ORDER:
            if w in (x + "ṃ", x + "ñca", x + "ñceva", x + "nti"):
                stem = x
                break
        if stem:                                   # first-occurrence rule (sample, user decision)
            if _noun_by_position(kw, pi):
                cands = [DHAMMA_NOUN[stem], DHAMMA_ADJ[stem]]
            elif w.endswith(("ñca", "ñceva")):     # -ñca: the member value (coordinator; = the noun)
                cands = [DHAMMA_NOUN[stem], DHAMMA_ADJ[stem]]
            else:
                cands = [DHAMMA_ADJ[stem], DHAMMA_NOUN[stem]]
            return pick(vi, *cands) or cands[0]
    if k not in DHAMMA9:
        return None
    v = DHAMMA9[k]
    if v == "hiện tượng" or len(words) == 1 or present_strict(v, vi):
        return v
    for x in _X_ORDER:                             # the text splits it: «hiện tượng … X» (sample rule)
        if v == DHAMMA_NOUN[x] and present("hiện tượng" + GAP + DHAMMA_ADJ[x], vi):
            return "hiện tượng" + GAP + DHAMMA_ADJ[x]
    return v


# ---------------------------------------------------------------------------- citta kinds and moments
# «vào khoảnh khắc sinh khởi của tâm không gắn liền với các hiện tượng thiện (và không gắn liền với các hiện tượng
# bất thiện)»; «vào khoảnh khắc sinh khởi của các hiện tượng thiện» (kusalānaṃ uppādakkhaṇe): the inner «các» is kept,
# the «vào» of the locative is frame (8, 5-01)
CITTA_KIND9 = {
    "kusalavippayutta": "không gắn liền với các hiện tượng thiện",
    "akusalavippayutta": "không gắn liền với các hiện tượng bất thiện",
    "abyākatavippayutta": "không gắn liền với các hiện tượng không xác định về mặt đạo đức",   # proposal
    "kusalavippayuttaakusalavippayutta":
        "không gắn liền với các hiện tượng thiện và không gắn liền với các hiện tượng bất thiện",
    "akusalavippayuttakusalavippayutta":
        "không gắn liền với các hiện tượng bất thiện và không gắn liền với các hiện tượng thiện",
}
OWNER9 = {x[:-1] + "ānaṃ": "các " + v for x, v in DHAMMA_NOUN.items()}
_CITTA_ENDS = ("cittassa", "citte", "cittaṃ", "cittā", "citta")


def citta9(word):
    """<kind>cittassa / -citte / -cittaṃ (CITTA_KIND9) -> «tâm <kind>»; other cittas via map_5-01_vi.citta5 (cittassa
    «tâm», Pacchimacittasamaṅgīnaṃ «người có được tâm cuối cùng» …). None if not a citta."""
    k = C.norm(lc(word))
    for e in _CITTA_ENDS:
        if k.endswith(e) and k[: -len(e)] in CITTA_KIND9:
            return "tâm " + CITTA_KIND9[k[: -len(e)]]
    return T5.citta5(word)


def moment9(kw, text):
    """«<owner> uppādakkhaṇe / bhaṅgakkhaṇe» = «khoảnh khắc sinh khởi / tan rã của <owner>»; owner = OWNER9 (kusalānaṃ
    «các hiện tượng thiện»), CITTA_KIND9, then map_5-01_vi (NOUN_OF, citta5). None if not a moment keyword."""
    words = kw.split()
    if len(words) == 2:
        m = C.moment_value(words[1], text)
        if not m:
            return None
        w = lc(words[0]).lower()
        owner = OWNER9.get(w) or T5.NOUN_OF.get(w) or citta9(words[0])
        return (m + " của " + owner) if owner else None
    if len(words) == 1:
        return C.moment_value(kw, text)
    return None


# ---------------------------------------------------------------------------- the bhāvanāvāra verbs (9-03)
# «(a) Người nào tu tập hiện tượng thiện, thì có phải người ấy dứt bỏ hiện tượng bất thiện không? … Người nào không tu
# tập hiện tượng thiện, thì có phải người ấy không dứt bỏ hiện tượng bất thiện không?» (yo kusalaṃ dhammaṃ bhāveti so
# akusalaṃ dhammaṃ pajahatīti? … na bhāveti … nappajahatīti?): the value is the verb (pi-6 conventions); a separate
# na keeps «không» for itself (na bhāveti -> bhāveti = tu tập), the fused nappajahati keeps it (= 7-01 VERBS)
BHAVANA_STEMS = {"bhāve": "tu tập", "pajah": "dứt bỏ"}
_BH_ENDINGS = {"bhāve": {"ti": "pres", "nti": "pres", "ssati": "fut", "ssanti": "fut", "suṃ": "past"},
               "pajah": {"ati": "pres", "anti": "pres", "issati": "fut", "issanti": "fut", "ittha": "past",
                         "iṃsu": "past"}}
BHAVANA = {}
for _st, _ends in _BH_ENDINGS.items():
    for _e, _t in _ends.items():
        BHAVANA[_st + _e] = K.VERB_FORMS[("pos", _t)].format(v=BHAVANA_STEMS[_st])
for _e, _t in _BH_ENDINGS["pajah"].items():         # fused n-: nappajahati «không dứt bỏ» (= 7-01 VERBS)
    BHAVANA["nappajah" + _e] = K.VERB_FORMS[("neg", _t)].format(v=BHAVANA_STEMS["pajah"])
for _k in list(BHAVANA):                            # the question forms: bhāvetīti, pajahatīti, nappajahatīti
    if " " not in _k and _k[-1] == "i":
        BHAVANA[_k[:-1] + "īti"] = BHAVANA[_k]
BHAVANA.update({"bhāvanāvāro": "mục về sự tu tập", "bhāvanā": "sự tu tập",
                "kusalaṃ dhammaṃ": DHAMMA_NOUN["kusala"], "akusalaṃ dhammaṃ": DHAMMA_NOUN["akusala"],
                "abyākataṃ dhammaṃ": DHAMMA_NOUN["abyākata"]})


def _bh_parse(kw):
    k = lc(kw).lower()
    neg = k.startswith("nappajah")
    if neg:
        k = k[2:]
    cands = [k]
    if len(k) > 4 and k.endswith("īti"):
        cands.append(k[:-3] + "i")
    for c in cands:
        for st, ends in _BH_ENDINGS.items():
            if c.startswith(st) and c[len(st):] in ends:
                return st, ends[c[len(st):]], neg, c
    return None


def bhavana_value(kw, pali=None):
    """bhāveti / bhāvetīti / pajahati / pajahatīti / nappajahati …: the verb with its tense word by the polarity of
    its first occurrence in the Pāli (map_2-02_vi._polarity: the 2-01 rule). None if not a bhāvanā verb."""
    p = _bh_parse(kw)
    if not p:
        return None
    st, t, neg, base = p
    if neg:
        return K.VERB_FORMS[("neg", t)].format(v=BHAVANA_STEMS[st])
    pol = "pos"
    if pali:
        forms = [base] + ([base[:-1] + "īti"] if base.endswith("i") else [])
        pol = P._polarity(forms, pali)
    return K.VERB_FORMS[(pol, t)].format(v=BHAVANA_STEMS[st])


# ---------------------------------------------------------------------------- headings and editorial words
HEAD9 = {
    "suddhadhammavāro": "mục về các hiện tượng thuần túy",          # inner «các» kept (3-01 / 5-01 Suddha-)
    "suddhadhammamūlacakkavāro": "mục về vòng luân chuyển dựa trên các hiện tượng thuần túy",
    "paṇṇattiniddesavāro": K.HEADINGS["paṇṇattiniddesavāro"],     # «Mục giải thích về sự định danh.» (2-01)
    "paṇṇattiuddesavāro": K.HEADINGS["paṇṇattiuddesavāro"],
    "dhammayamakapāḷi": "các cặp câu hỏi về các hiện tượng",       # closer, lower case as written (sample rule)
    "(no direct equivalent)": NDE,                                 # the keyword-file placeholder (coordinator)
}
TITLE9 = {"dhammayamakaṃ": S.FORMULAS["dhammayamakaṃ"]}            # heading «Các cặp câu hỏi về các hiện tượng»;
                                                                   # running text / closer: lower case (map_8_vi)

T901 = {**BHAVANA, **HEAD9}
_T5_FIXED = {**T5.T501}


def value901(kw, kws, vi, pi, table=None):
    """your table -> T901 -> dhamma_value -> moment9 / citta9 -> bhavana_value -> map_5-01_vi fixed tables ->
    map_2-01_vi.value201 (members = DHAMMA9; verbs, planes, beings, relatives) -> map_sample_vi.value6."""
    k = _norm(kw)
    if table:
        for x in (kw, lc(kw), k):
            if x in table:
                return table[x]
    if k in T901:
        return T901[k]
    if k in TITLE9:                                # «Dhammayamakaṃ niṭṭhitaṃ» «Phần các cặp câu hỏi về … đã hoàn tất»
        v = TITLE9[k]
        if vi.lstrip().startswith("#") or not present(v[:1].lower() + v[1:], vi):
            return v
        return v[:1].lower() + v[1:]
    v = dhamma_value(kw, vi, pi)
    if v is not None:
        return v
    v = moment9(kw, vi)
    if v:
        return v
    if " " not in kw:
        v = citta9(kw)
        if v:
            return v
    v = bhavana_value(kw, pi)
    if v is not None:
        return v
    if k in _T5_FIXED:
        return _T5_FIXED[k]
    if k in T5.NOUN_OF:
        return T5.NOUN_OF[k]
    if k in ("paṭilabhissanti", "paṭilabhissānti"):
        return pick(vi, "sẽ đạt được", "sẽ" + GAP + "đạt được") or "sẽ đạt được"
    return K.value201(kw, kws, vi, pi, None, DHAMMA9)


# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value901(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False, part=PART):
    res, vi = resolver(part), read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
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
    res, vi, pi = resolver(part), read_vietnamese(part), read_pali(part)
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
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
