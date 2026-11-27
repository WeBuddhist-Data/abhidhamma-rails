"""Burmese zero-shot of pi-7 2-01-vitakkattika, 2-02-pitittika («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»).

usage: python3 -I -X utf8 make_ch2-01-02.py [chapter ...] [--dev] [--out DIR]
Every line goes through my7_formulas.translate() with the approved sample's tables (make_sample.py, imported for its
tables only) and the finished group 1-03 … 1-05 (make_ch1-03-05.py, IMPORTED for its in-memory extensions only: its
main block, which writes its chapters, never runs), plus the frames of this script (the two triads, their nouns and
templates). No file of the sample or of another group is edited: their tables are extended in memory here, and every
new string is logged in notes-ch2-01-02.md. A sentence that no frame matches stops the run; it is never guessed.
--dev lists every unmatched skeleton instead of stopping (nothing is written).
"""
import collections
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my7_formulas as F  # noqa: E402
import make_sample as S  # noqa: E402,F401  (tables only)

_spec = importlib.util.spec_from_file_location("make_ch1_03_05", HERE / "make_ch1-03-05.py")
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)          # in-memory extensions of 1-03 … 1-05 (its __main__ block does not run)
_TABLES = ("NOUN", "QUAL", "FIXED", "LEX", "NOTES", "HLINES", "SK", "SKF", "COUNT", "PREFIX", "TIKA_NAME", "TRIADS",
           "TRIAD_END", "HEAD")
_BEFORE = {t: dict(getattr(F, t)) for t in _TABLES}        # the tables as the sample + 1-03 … 1-05 leave them

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["2-01-vitakkattika.md", "2-02-pitittika.md"]
C, END, PE, W = F.C, F.END, F.PE, F.W
WCH = r"[\wāīūṃṅñṭḍṇḷ]"

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the two triads (pi-1 final)
_tw = G._tw
TRIADS_ADD = {
    "vitakka": {
        "savitakkasavicār": _tw("savitakkasavicārā dhammā", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော", "^1-M1-6"),
        "avitakkavicāramatt": _tw("avitakkavicāramattā dhammā", "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော",
                                  "^1-M1-6"),
        "avitakkaavicār": _tw("avitakkaavicārā", "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော", "^1-M1-6"),
    },
    "piti": {
        "pītisahagat": _tw("pītisahagatā dhammā", "ပီတိနှင့်အတူ ဖြစ်သော", "^1-M1-7"),
        "sukhasahagat": _tw("sukhasahagatā dhammā", "သာယာမှုနှင့်အတူ ဖြစ်သော", "^1-M1-7"),
        "upekkhāsahagat": _tw("upekkhāsahagatā dhammā", "ဥပေက္ခာနှင့်အတူ ဖြစ်သော", "^1-M1-7"),
    },
}
# «pītisahagatā ca sukhasahagatā ca tayo khandhā» (one noun accompanied by BOTH): prep() joins the two terms into
# one slot, rendered as two stacked qualifiers «A၊ B N» (the module's stacking of two «…နှင့်အတူ ဖြစ်သော»); with the
# noun dhamma the module's own coordination «A သဘောတရားနှင့် B သဘောတရား» stays (two kinds of phenomena)
PITISUKHA = TRIADS_ADD["piti"]["pītisahagat"] + C + " " + TRIADS_ADD["piti"]["sukhasahagat"]
TRIADS_ADD["piti"]["pītisukhasahagat"] = PITISUKHA
_END = G._END.replace("|āni|", "|āni|ena|opi|amūlakā|amūlake|agacchantena|")
F.TRIADS.update(TRIADS_ADD)
F.TRIAD_END.update({"vitakka": _END, "piti": _END})
F.rebuild()
_TERMW = r"(?:[Ss]avitakkasavicār|[Aa]vitakkavicāramatt|[Aa]vitakkaavicār|[Pp]ītisahagat|[Ss]ukhasahagat|[Uu]pekkhāsahagat)"


# ===================================================================================== Pāli preparation (in memory)
_PS_CASE = r"(ā|o|aṃ|assa|ena|āya|e|ānaṃ)"


def prep(text):
    text = G.prep(text)
    # harmonise H1: the subject «anulomaṃ» before «X-assa vitakkassa ca» (parser token, see the LEX entry above)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])[Aa]nulomaṃ (?=(?:gotrabhussa|vodānassa) vitakkassa ca)", "anulomaṃ_subj ", text)
    # pīti + sukha on one noun (not dhamma): one slot «pītisukhasahagat-»
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])([Pp])ītisahagat" + _PS_CASE + r" ca sukhasahagat\2 ca (?!dhamm)",
                  r"\1ītisukhasahagat\2 ", text)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])([Pp])ītisahagat(a|āna)ñca sukhasahagat\2ñca (?!dhamm)",
                  r"\1ītisukhasahagat\2ṃ ", text)
    text = text.replace("pītisahagatasukhasahagatacittasamaṅgissa", "pītisukhasahagatacittasamaṅgissa")
    # «X-ādhipati» = «X-o adhipati» (as 1-03 … 1-05 prep for its terms)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _TERMW + r"|[Pp]ītisukhasahagat)ādhipati(?![\wāīūṃṅñṭḍṇḷ])", r"\1o adhipati",
                  text)
    for i, a in enumerate(NOTEP):
        text = text.replace(a, f"(⁑{i})")
    for a, b in SLIP_FIX.items():
        if a in text:
            F.SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    return text


SLIP_FIX = {"vicākānaṃ": "vipākānaṃ", "avitakka vicāramattassa": "avitakkavicāramattassa",
            "savitakkasavicārassa ca maggassa ca": "savitakkasavicārassa maggassa ca",
            "avitakkavicāramattā khandhā mahābhūte paṭicca": "avitakkavicāramattā khandhā ⁂ mahābhūte paṭicca",
            "pītisukhasahagatānaṃ āsevanapaccayena": "pītisukhasahagatānaṃ dhammānaṃ āsevanapaccayena",
            # the recipient after «… parikammaṃ» is genitive (the module's LEX entry is the instrumental)
            "parikammaṃ dibbāya sotadhātuyā": "parikammaṃ dibbāya·sotadhātuyā"}


# ===================================================================================== nouns of this group
VITAKKA = W("vitakko", "စတင်ကြံစည်မှု", "1")
VICARA = W("vicāro", "ဆက်လက်သုံးသပ်မှု", "1")
F.add_noun(VITAKKA, n=["vitakko"], a=["vitakkaṃ"], g=["vitakkassa"])
F.add_noun(VICARA, n=["vicāro"], a=["vicāraṃ"], g=["vicārassa"])
F.add_lex("n", {"vitakko": VITAKKA, "vicāro": VICARA})
F.add_lex("a", {"vitakkaṃ": VITAKKA, "vicāraṃ": VICARA})
F.add_lex("g", {"vitakkassa": VITAKKA, "vicārassa": VICARA})
# «Xñca» written together = «Xṃ ca» (the 1-03 … 1-05 prep list, extended in memory)
G.NCA.update({"vitakkañca", "vicārañca", "cuticittañca", "anulomañca", "parikammañca", "vodānañca", "phalañca",
              "bhavaṅgañca"})
G.NCA.update({w[0].upper() + w[1:] for w in list(G.NCA)})

# «sukhasahagataṃ kāyaviññāṇaṃ» (the sample's LEX phrase): the term is now a slot, the noun stands alone
F.add_lex("na", {"kāyaviññāṇaṃ": F.KAYAVINNANA})
F.add_lex("g", {"kāyaviññāṇassa": F.KAYAVINNANA})
# harmonise H1: «anulomaṃ» (the conformity mind) as the SUBJECT before a coordinated recipient «X-assa vitakkassa ca»
# (2-01 ^…, 2 lines: was «လျော်ညီခြင်း စိတ်ကို …», the na-kind object marker before an x item): «… စိတ်သည်»
F.add_lex("n", {"anulomaṃ_subj": F.LEX["anulomaṃ"][0]})

# ===================================================================================== engine extensions (in memory)
# (a) coordination by head nouns: «A B ca» (one «ca» after the last conjunct) and lists whose «ca» the module's
#     _conj() cannot split («khandhānaṃ vicārassa ca cittasamuṭṭhānānaṃ ca rūpānaṃ»): each conjunct ends at its head
#     noun; qualifiers (terms, numbers, QUAL) precede it. Used only where the module's split fails.
_conj0 = F._conj


def _is_head(w):
    if w in F.NP_NUM or w in F.QUAL:
        return False
    return w in F.NOUN or w in F.FIXED or "\u0002" in w or G.TOK in w


def _head_split(words):
    if "ca" not in words:
        return None
    # a «ca» after a term belongs to a term coordination («§T§o ca §T§o ca dhammā»): not this frame
    if any(w == "ca" and i and words[i - 1].startswith("§T§") for i, w in enumerate(words)):
        return None
    if not any(w == "ca" and i and _is_head(words[i - 1]) for i, w in enumerate(words)):
        return None
    ws = [w for w in words if w != "ca"]
    parts, cur = [], []
    for w in ws:
        cur.append(w)
        if _is_head(w):
            parts.append(cur)
            cur = []
    if cur or len(parts) < 2:
        return None
    cases = {(F.NOUN.get(p[-1]) or F.FIXED.get(p[-1]) or (None, None))[1] for p in parts}
    if len(cases - {None}) > 1:              # the conjuncts of one NP share their case
        return None
    return parts


def _parts_ok(parts):
    return all(p and _is_head(p[-1]) and not any(_is_head(w) for w in p[:-1]) for p in parts)


def _conj(words):
    r = _conj0(words)
    if r is not None and _parts_ok(r):
        return r
    h = _head_split(words)
    return h if h is not None else r


F._conj = _conj

# (b) coordination inside the lexicon frame (pañhāvāra sentences whose nouns are LEX entries): «A ca B ca» and
#     «A B ca» (A, B = [terms] + one LEX item of the same case) become one item rendered as the module's
#     coordination: «Aလည်းကောင်း၊ Bလည်းကောင်း» (nominative), «Aအားလည်းကောင်း၊ …» (recipient), «Aကိုလည်းကောင်း၊ …»
#     (object); plural nouns take «တို့» before a case mark. A following «ārabbha» / «garuṃ katvā» / verb is
#     unchanged (the module's post rule puts it after the group).
_lex0 = F.lex
_CASE_MARK = {"n": "", "g": "အား", "a": "ကို", "na": "ကို", "i": "ဖြင့်", "G": "၏"}
_GROUP_N = [0]


def _conjunct(words, end):
    """the conjunct ending at words[end-1]: (start, kind, Burmese without mark, plural, n_terms) or None"""
    for n in (3, 2, 1):
        st = end - n
        if st < 0:
            continue
        key = " ".join(words[st:end])
        if key in F.LEX and F.LEX[key][1] in _CASE_MARK:
            my, kind = F.LEX[key]
            k = st
            while k > 0 and words[k - 1].startswith("§T§") and words[k - 1][3:] in F.TERM_TAIL_OK:
                k -= 1
            pl = my.endswith("+")
            return k, kind, my[:-1] if pl else my, pl, st - k
    return None


def _compat(k1, k2):
    return k1 == k2 or {k1, k2} in ({"n", "na"}, {"a", "na"})


def _group_my(items, tvals):
    out, ti = [], 0
    for (_, kind, my, pl, nt) in items:
        pre = " ".join(tvals[ti:ti + nt])
        ti += nt
        kinds = {it[1] for it in items}
        mark = "" if "n" in kinds else _CASE_MARK[kind]
        num = re.search(r" (?:" + "|".join(F.PAA.values()) + r")$", my)
        out.append((pre + " " if pre else "") + my + ("တို့" if pl and mark and not num else "") + mark + F.LAKAUNG)
    return (C + " ").join(out)


def lex(frag, slots, ti, ci, ki, di, vi):
    lead = frag[:len(frag) - len(frag.lstrip())]
    words = frag.strip().split(" ")
    if "ca" not in words:
        return _lex0(frag, slots, ti, ci, ki, di, vi)
    # term positions (slot index of each §T§ word, in order)
    tpos = {}
    for i, w in enumerate(words):
        if w.startswith("§T§"):
            tpos[i] = len(tpos)
    groups = []                      # (start, end, items)
    i = 0
    while i < len(words):
        if words[i] != "ca":
            i += 1
            continue
        b = _conjunct(words, i)
        if b is None:
            raise KeyError("lex coordination: " + " ".join(words))
        items, st, end = [b], b[0], i + 1
        while True:                  # «A ca B ca [C ca]»: the following conjuncts each closed by «ca»
            e = next((e for e in range(end + 1, min(end + 12, len(words))) if words[e] == "ca"), None)
            c = _conjunct(words, e) if e is not None else None
            if c is None or c[0] != end:
                break
            items.append(c)
            end = e + 1
        if len(items) == 1:          # «A B ca»: the item just before B, of the same case
            a = _conjunct(words, st)
            if a is None or not _compat(a[1], b[1]) or (groups and groups[-1][1] > a[0]):
                raise KeyError("lex coordination: " + " ".join(words))
            items.insert(0, a)
            st = a[0]
        groups.append((st, end, items))
        i = end
    # replace each group by a placeholder LEX item (kind x), the group's terms removed from the slots
    new_words, new_t, used_t = [], [], 0
    gi, i = 0, 0
    tvals = slots["T"][ti[0]:]
    rem = []
    while i < len(words):
        if gi < len(groups) and i == groups[gi][0]:
            st, end, items = groups[gi]
            idx = [tpos[k] for k in range(st, end) if k in tpos]
            key = f"§G{_GROUP_N[0]}§"
            _GROUP_N[0] += 1
            nxt = gi + 1 < len(groups) and groups[gi + 1][0] == end
            F.LEX[key] = (_group_my(items, [tvals[j] for j in idx]) + (C if nxt else ""), "x")   # «…၊ » between groups
            new_words.append(key)
            used_t += len(idx)
            i = end
            gi += 1
            continue
        if i in tpos:
            rem.append(tvals[tpos[i]])
        new_words.append(words[i])
        i += 1
    sl = dict(slots)
    sl["T"] = rem
    t2 = [0]
    try:
        r = _lex0(lead + " ".join(new_words), sl, t2, ci, ki, di, vi)
    finally:
        for k in [k for k in F.LEX if k.startswith("§G")]:
            del F.LEX[k]
    ti[0] += t2[0] + used_t
    return r


F.lex = lex

# (c) «[NP-nom] NP-acc Xpaccayā» (vippayutta: «Khandhā vatthuṃ vippayuttapaccayā») = «NP-သည် NP-ကို …ကြောင့်», as
#     the lexicon frame renders it in 1-01 / 1-03 («အစုအဝေးတို့သည် မှီရာ ဝတ္ထုကို ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့်»)
def nom_acc(words, terms):
    """«[NP-nom] NP-acc» -> Burmese, or None; every split point is tried (the subject may be absent)"""
    for j in range(len(words) - 1, -1, -1):
        aw, bw = words[:j], words[j:]
        try:
            if aw and F._case_of(aw) != "n":
                continue
            if F._case_of(bw) != "a":
                continue
            it = iter(terms)
            a_my, _, k1 = F.np_my(aw, it, "n") if aw else ("", 0, 0)
            b_my, _, k2 = F.np_my(bw, it, "a")
        except (KeyError, StopIteration, IndexError, ValueError):
            continue
        if k1 + k2 != len(terms):
            continue
        return (a_my + " " if a_my else "") + b_my
    return None


_NA_RE = re.compile(r"^(?P<np>[^§…]+?)(?P<ch>(?: §C§ā)+)(?P<end>[.,;]?)$")


def nom_acc_unit(sk, slots):
    m = _NA_RE.match(sk.strip())
    if not m or any(slots[k] for k in "KVD"):
        return None
    words = m["np"].split()
    if any(w in F.LINK or w in F.VERB for w in words):
        return None
    np = nom_acc(words, slots["T"])
    if np is None:
        return None
    return np + " " + F.chain(m["ch"].strip(), slots, [0], [0], [0]) + F.punct(m["end"])


_panha1 = F.panha


_COMMA_DASH = re.compile(r"^(?P<a>.* uppajj(?:ati|anti)(?: §C§ā)+), (?P<b>.+)$")


def comma_dash(sk, slots):
    """«… uppajjati naadhipatipaccayā, X paṭicca Y, …»: a comma where the frame has «–» (kept as «၊»; logged)"""
    m = _COMMA_DASH.match(sk.strip())
    if not m:
        return None
    parts = [m["a"], m["b"]]
    sa, sb = G._sub_slots(parts, slots)
    try:
        ti, ci, ki, di = [0], [0], [0], [0]
        a = F.clause(m["a"], sa, ti, ci, ki, di)
        if (ti[0], ci[0]) != (len(sa["T"]), len(sa["C"])):
            return None
    except (KeyError, StopIteration):
        return None
    b = G.pairs2(m["b"], sb) or panha(m["b"], sb)
    if b is None:
        return None
    F.SLIPS.add("«… uppajjati Xpaccayā, …»: a comma where the frame has a dash (rendered «၊», no dash added)")
    return a + C + " " + b


def panha(sk, slots):
    r = nom_acc_unit(sk, slots)
    if r is None:
        r = comma_dash(sk, slots)
    if r is None:
        r = _panha1(sk, slots)
    if r is None:
        r = panha_multi(sk, slots)
    if r is None:
        r = panha_note_count(sk, slots)
    if r is None:
        r = panha_note(sk, slots)
    return r


def panha_multi(sk, slots):
    """two pañhā sentences joined by «, » in one unit («khandhā vatthussa X-ena paccayo, vatthu khandhānaṃ …»)"""
    body = sk.strip()
    end = ""
    if body[-1:] in ".;":
        body, end = body[:-1], F.punct(body[-1])
    parts = re.split(r"(?<=paccayo), ", body)
    if len(parts) < 2:
        return None
    outs = []
    for p, sub in zip(parts, G._sub_slots(parts, slots)):
        r = panha(p, sub)
        if r is None:
            return None
        outs.append(r)
    return (C + " ").join(outs) + end


def panha_note(sk, slots):
    """a pañhā sentence (or NP-nom NP-dat) followed by a closing note: «X dhammo Yassa dhammassa (note).»"""
    body = sk.strip()
    end = ""
    if body[-1:] in ".;,":
        body, end = body[:-1], F.punct(body[-1])
    note = next((k for k in sorted(F.NOTES, key=len, reverse=True) if body.endswith(" " + k)), None)
    if note is None or (F.NOTES[note] or "").count("§"):
        return None
    head = body[:-len(note) - 1]
    r = panha(head, slots)
    return None if r is None else f"{r} {F.NOTES[note]}{end}"


def panha_note_count(sk, slots):
    """«… (saṃkhittaṃ) satta.»: a count after a closing note"""
    m = re.match(r"^(?P<h>.+ \([^()]+\)) (?P<n>\S+?)(?P<e>[.,]?)$", sk.strip())
    if not m or m["n"] not in F.COUNT:
        return None
    h = m["h"]
    note = next((k for k in F.NOTES if h.endswith(" " + k)), None)
    if note is None:
        return None
    head = h[:-len(note) - 1]
    r = _panha1(head, slots) or G.bits(head, slots)
    if r is None:
        return None
    return f"{r} {F.NOTES[note]} {F.COUNT[m['n']]}" + F.punct(m["e"])


F.panha = panha
_part_my0 = G.part_my


def part_my(p, sub):
    if " ⁂ " in p:                          # a missing comma between two pairs (prep marks it; nothing added)
        ps = p.split(" ⁂ ")
        outs = [part_my(x, y) for x, y in zip(ps, G._sub_slots(ps, sub))]
        return None if None in outs else " ".join(outs)
    r = nom_acc_unit(p, sub)
    return r if r is not None else _part_my0(p, sub)


G.part_my = part_my

# (d) counts above twenty-four (and the short forms ekavīsa / bāvīsa): Burmese number words + «ခု» (as 1-03 … 1-05)
NUM_ADD = {"ekavīsa": (21, "နှစ်ဆယ့်တစ်"), "pañcavīsa": (25, "နှစ်ဆယ့်ငါး"), "chabbīsa": (26, "နှစ်ဆယ့်ခြောက်"),
           "sattavīsa": (27, "နှစ်ဆယ့်ခုနစ်"), "aṭṭhavīsa": (28, "နှစ်ဆယ့်ရှစ်"), "ekūnatiṃsa": (29, "နှစ်ဆယ့်ကိုး"),
           "tiṃsa": (30, "သုံးဆယ်"), "ekatiṃsa": (31, "သုံးဆယ့်တစ်"), "dvattiṃsa": (32, "သုံးဆယ့်နှစ်"),
           "tettiṃsa": (33, "သုံးဆယ့်သုံး"), "catuttiṃsa": (34, "သုံးဆယ့်လေး"), "pañcatiṃsa": (35, "သုံးဆယ့်ငါး"),
           "chattiṃsa": (36, "သုံးဆယ့်ခြောက်"), "sattatiṃsa": (37, "သုံးဆယ့်ခုနစ်"), "bāvīsa": (22, "နှစ်ဆယ့်နှစ်")}
for _w, (_n, _my) in NUM_ADD.items():
    F.COUNT[_w] = new(_w, _my + "ခု")
    F.COUNT_VAL[_w] = _n
    G.SKF[_w] = F.COUNT[_w]
F._CNT_ALT = "|".join(sorted(F.COUNT, key=len, reverse=True))
F.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + F._LOC_ALT + r")) (?P<num>"
                        + F._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")
# the term endings of 1-03 … 1-05 exclude «-e <count>» («vipāke dasa» is the condition, not the term): the new counts
# are added to that exclusion (all triads), so «vipāke ekavīsa» stays the condition
_NUMS2 = "|".join(sorted(list(F.COUNT) + G._TEENW + list(NUM_ADD), key=len, reverse=True))
for _tri, _rx in list(F.TRIAD_END.items()):
    if G._END in _rx or _END in _rx:
        F.TRIAD_END[_tri] = _rx.replace(_END, _END.replace(G._NUMS, _NUMS2)).replace(
            G._END, G._END.replace(G._NUMS, _NUMS2))
F.rebuild()

# (e) a counting line with bare locatives that share the following count («āhāre indriye jhāne magge sattatiṃsa»,
#     «… avigate sabbattha dasa», «… jhāne sabbe dasa»): each bare locative «Nဟူသော အကြောင်း၌» followed by «၊»;
#     sabbattha «နေရာတိုင်း၌» (as 1-01), sabbe «အားလုံး». Rendered token by token from the Pāli; anything else stops.
SABBATTHA = new("sabbattha", "နေရာတိုင်း၌")
SABBE = new("sabbe (before a count)", "အားလုံး")
_LOCW = re.compile(r"^(?P<neg>[Nn]a|[Nn]o)?(?P<loc>" + F._LOC_ALT + r")$", re.I)
_ABW = re.compile(r"^(?P<neg>[Nn]a|[Nn]o)?(?P<stem>" + "|".join(sorted(F.STEMS, key=len, reverse=True))
                  + r")paccayā$", re.I)


def count_line(u):
    found = re.findall(r"(\s*)(…|\([^()]*\)|[^\s…]+)", u)
    toks = [t for _, t in found]
    if not any(t.rstrip(",.") in ("sabbattha", "sabbe") for t in toks) and not re.search(
            r"(?:^|[\s…])(?:na|no)?[a-zāī]+(?:e|yā) (?:na|no)?[a-zāī]+(?:e|yā) ", u, re.I):
        return None
    out, prev, bare = [], None, False
    for ws, t in found:
        sp = " " if ws and out else ""            # the source's spacing
        if t == "…":
            out.append(sp + F.PE)
            prev = "pe"
            continue
        if t.startswith("("):
            if t not in F.NOTES:
                return None
            out.append(sp + F.NOTES[t])
            prev = "note"
            continue
        core, p = t.rstrip(",."), t[len(t.rstrip(",.")):]
        if not core:
            out.append(F.punct(p))
            continue
        lw, ab = _LOCW.match(core), _ABW.match(core)
        if ab:
            my, kind = F.cond(ab["stem"].lower(), "ab", bool(ab["neg"])), "ab"
        elif lw and lw["loc"].lower() in F.LOC2STEM:
            my, kind = F.cond(F.LOC2STEM[lw["loc"].lower()], "loc", bool(lw["neg"])), "loc"
        elif core in F.COUNT:
            my, kind = F.COUNT[core], "cnt"
        elif core == "sabbattha":
            my, kind = SABBATTHA, "all"
        elif core == "sabbe":
            my, kind = SABBE, "all"
        else:
            return None
        if prev in ("loc",) and kind in ("loc",) and not out[-1].endswith((C, END)):
            out[-1] += C                                    # «A၌၊ B၌ …»
        if prev == "ab" and kind == "loc" and not out[-1].endswith((C, END)):
            out[-1] += C                                    # «A-ကြောင့်၊ B-၌ …» (the module's chain)
        out.append(sp + my + F.punct(p))
        bare |= prev == "loc" and kind == "loc"
        prev = kind
    return "".join(out) if (bare or any(t.rstrip(",.") in ("sabbattha", "sabbe") for t in toks)) else None


_unit1 = F.unit_my


_PS_TAIL = re.compile(r"^(?P<h>.*[^\s.,;]) (?P<p>[Pp]aṭisandhikkhaṇe)…\.$")


def unit_my(u):
    lead = u[:len(u) - len(u.lstrip())]
    r = count_line(u.strip())
    if r is not None:
        return lead + r
    m = _PS_TAIL.match(u.strip())
    if m and "–" not in u:                  # «… vicāro ca paṭisandhikkhaṇe…pe….»: no full stop before the prefix
        F.SLIPS.add("«… vicāro ca paṭisandhikkhaṇe…pe….»: no full stop before «paṭisandhikkhaṇe» (none added)")
        return lead + _unit1(m["h"]) + " " + F.PREFIX["paṭisandhikkhaṇe"] + F.PE + END
    return _unit1(u)


F.unit_my = unit_my

# (f) pañhāvāra nouns of this group
F.add_qual(F.QUAL["purimā purimā"], "purimo purimo")
F.add_qual(F.QUAL["pacchimānaṃ pacchimānaṃ"], "pacchimassa pacchimassa")
_PRK = G.PARIKAMMA
DIBBA_C = F.LEX["dibbena cakkhunā"][0]
DIBBA_S = F.LEX["dibbāya sotadhātuyā"][0]
F.add_lex("g", {"jhānassa": "ဈာန်", "dibbassa cakkhussa": DIBBA_C, "dibbāya·sotadhātuyā": DIBBA_S,
                "ākāsānañcāyatanassa": G.AY["ākāsānañcāyatana"], "ākiñcaññāyatanassa": G.AY["ākiñcaññāyatana"],
                "upapatticittassa": F.LEX["upapatticittassa"][0]})
F.LEX["dibbāya sotadhātuyā parikammaṃ"] = (f"{DIBBA_S}၏ {_PRK}", "na")
for _k in ("jhānassa", "dibbassa cakkhussa", "ākāsānañcāyatanassa", "viññāṇañcāyatanassa",
           "ākiñcaññāyatanassa", "nevasaññānāsaññāyatanassa", "iddhividhañāṇassa", "cetopariyañāṇassa",
           "pubbenivāsānussatiñāṇassa", "yathākammūpagañāṇassa", "anāgataṃsañāṇassa"):
    F.LEX.setdefault(f"{_k} parikammaṃ", (f"{F.LEX[_k][0]}၏ {_PRK}", "na"))
for _o, _my in G.ORD.items():
    F.add_lex("x", {f"{_o}e jhāne": f"{_my} ဈာန်၌"})
F.add_lex("na", {"cuticittaṃ": F.LEX["cuticittaṃ"][0], "rūpāyatanaṃ": F.FIXED["rūpāyatanaṃ"][0],
                 "phoṭṭhabbāyatanaṃ": F.FIXED["phoṭṭhabbāyatanaṃ"][0], "cakkhāyatanaṃ": F.FIXED["cakkhāyatanaṃ"][0],
                 "kāyāyatanaṃ": F.FIXED["kāyāyatanaṃ"][0]})
F.add_lex("a", {"phoṭṭhabbaṃ": "အထိအတွေ့", "samāpattiṃ": F.LEX["samāpattiṃ uppādeti"][0].split("ကို")[0],
                "abhiññaṃ": F.LEX["abhiññaṃ uppādeti"][0].split("ကို")[0]})
F.add_lex("g", {"cakkhuviññāṇassa": F.FIXED["cakkhuviññāṇassa"][0]})
F.add_fixed(F.KATATTARUPA, "g", True, "kaṭattā rūpānaṃ")
F.add_qual(F.QUAL["vicikicchāsahagato"], "vicikicchāsahagataṃ")
F.add_qual(F.QUAL["uddhaccasahagato"], "uddhaccasahagataṃ")
F.add_noun(F.LEX["moho"][0], n=["moho"])

HLINES = {}
SK = {}
SKF = {}
SKF["dve khandhe ca"] = f"{F.KHANDHA} {F.PAA[2]}ကို{F.LAKAUNG}"      # «…pe… dve khandhe ca…pe…» (cut short)
F.TIKA_NAME["Vitakkattikaṃ"] = W("Vitakkattikaṃ", "စတင်ကြံစည်မှု သုံးမျိုးတွဲ", "2", "^2-18-10-5-0")
F.TIKA_NAME["Pītittikaṃ"] = new("Pītittikaṃ", "ပီတိ " + F.TIKA)
for _p in ("Vitakkattikaṃ", "Pītittikaṃ"):
    HLINES[f"{_p} niṭṭhitaṃ."] = F.finished(F.TIKA_NAME[_p])

# ===================================================================================== notes and instructions
# Words of the instructions (NEW unless marked; the 1-01 / 1-03 … 1-05 / sample words where they exist)
KATABBA = new("kātabbaṃ / -ā / -o / -āni", "ပြုရမည်")                 # as 1-01
PANHA = G.PANHA                                                       # pañhā «ပြဿနာ» (1-03 … 1-05)
VITTH = S.PH["vitthāretabbo"]                                         # «အကျယ် ချဲ့ရမည်» (sample)
GANETABBA = S.PH["gaṇetabbaṃ"]                                        # «ရေတွက်ရမည်» (sample)
GANANA = S.GANANA                                                     # gaṇanā «ရေတွက်ချက်» (sample)
VIBHAJ, VIBHATTA = G.VIBHAJ, G.VIBHATTA                               # 1-03 … 1-05
EVAM = S.PH["evaṃ"]                                                   # «ထိုနည်းတူ» (sample)
EVAM_THUS = "ဤသို့"          # harmonise H14: «evaṃ» without «yathā» = «ဤသို့» (2-03 … 2-06 lineage); «yathā … evaṃ» «ထိုနည်းတူ»
SAJJH = S.PH["sajjhāyamaggena"]                                       # sample
ASAMM = S.PH["asammuyhantena"]                                        # «မရောထွေးစေဘဲ» (sample; asammohantena 1-03)
ANUMAJJ = new("anumajjantena", "ပြန်လည် စိစစ်လျက်")     # harmonise H10: = 2-03 … 2-06, 2-12 … 2-17, 3-01 (most chapters)
NIYAM = new("niyāmetabbaṃ / -ā", "သတ်မှတ်ရမည်")
UDDHAR = new("uddharitabbā", "ထုတ်နုတ်ရမည်")
DIPET = new("dīpetabbo / -ā", "ဖော်ပြရမည်")
DASSET = new("dassetabbo", "ပြသရမည်")
PASSITVA = new("passitvā", "ကြည့်၍")
PARIPUNNA = F.W("paripuṇṇaṃ", "ပြည့်စုံ")                              # sample / 1-01
SAMPUNNA = new("sampuṇṇā", "အပြည့်အစုံ ဖြစ်သော")
SADISA = F.SADISA                                                     # «နှင့် တူသည်» (sample)
SADISA_PL = new("-sadisā (plural)", "နှင့် တူကြသည်")                   # as 1-01 -sadisāni
SADISA_KAT = new("-sadisaṃ kātabbaṃ / -sadiso kātabbo", "နှင့် တူအောင် " + KATABBA)   # as 1-01
AVASESA = new("avasesa- (attributive)", "ကြွင်းသော")                  # 1-01 «ကြွင်းသည်»
IMINA = new("iminā kāraṇena", "ဤနည်းလမ်းဖြင့်")
VISESA = new("viseso", "ထူးခြားချက်")
NATTHI = "မရှိ"                                                       # sample NOTES
SUKHA_N = F.QUAL["sukhasahagataṃ"][:-len(F.SAHAGATA)]                   # sukha (noun) «သာယာမှု» (pi-1 term)
ARUPE = "ရုပ်မရှိသော ဘုံ၌"                                             # arūpe (burmese-style planes «ရုပ်မရှိသော ဘုံ»)
PAVATTI = new("pavatti / pavatte", "ဘဝ ဖြစ်ဆဲ ကာလ")
UDAHARANA = new("udāharaṇa", "ဥပမာ")
YATTHA = F.W("yattha", "အကြင်နေရာ", "6")                               # pi-6
TATTHA = new("tattha", "ထိုနေရာ")
AGACCHATI = new("āgacchati", "ပါဝင်လာ၏")
ARUPA_N = F.ARUPA + " " + F.DHAMMA                                    # arūpa (noun) «ရုပ် မဟုတ်သော သဘောတရား»
SUDDHIKA = F.HEAD["Suddhaṃ"]                                          # «ရိုးရိုး» (sample heading)
NAYA = new("naya", "နည်း")
TATHA = new("tathā (after yathā)", "ထို့အတူ")
VARA_N = {v: F.HEAD[v] for v in ("Paṭiccavāro", "Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro",
                                 "Sampayuttavāro", "Pañhāvāro")}
PATICCA_V = VARA_N["Paṭiccavāro"]
PS = f"{F.PATISANDHI} နေသော ခဏ"                                       # paṭisandhikkhaṇa (module PREFIX without ၌)
cn, cd = F.cname, F.cond
CNT = F.COUNT


def negbare(st):
    """«naXsadisaṃ»: the bare name with the negation, as the positive «(Xsadisaṃ)» «(Nနှင့် တူသည်)»"""
    return f"{F.N[st]} {F.NOT}ခြင်း"


# notes without slot words: Pāli text -> Burmese (F.NOTES, used by every frame)
F.NOTES.update({
    "(paṭisandhikkhaṇe natthi)": f"({PS} {NATTHI})",
    "(purejāte paṭisandhikkhaṇe natthi)": f"({cd('purejāta', 'loc')} {PS} {NATTHI})",
    "(naadhipatipaṭisandhikkhaṇe paripuṇṇaṃ)": f"({cd('adhipati', 'loc', True)} {PS}၌ {PARIPUNNA}သည်)",
    '("arūpe"ti niyāmetabbaṃ "paṭisandhikkhaṇe"ti ca)':
        f"(“{ARUPE}”ဟုလည်းကောင်း{C} “{PS}၌”ဟုလည်းကောင်း {NIYAM})",
    "(paripuṇṇaṃ, paṭisandhi natthi)": f"({PARIPUNNA}သည်{C} {F.PATISANDHI} {NATTHI})",
    "(paṭiccavārasadisā)": f"({PATICCA_V}{SADISA_PL})",
    "(dasa pañhā vitthāretabbā)": f"({PANHA} {CNT['dasa']}ကို {VITTH})",
    "(dasa pañhā kātabbā)": f"({PANHA} {CNT['dasa']} {KATABBA})",
    "(natthipi vigatampi anantarasadisaṃ)": f"({F.N['natthi']}လည်း{C} {F.N['vigata']}လည်း {F.N['anantara']}{SADISA})",
    "(sukhamūle tīṇi)": f"({SUKHA_N}ကို အခြေခံခြင်း၌ {CNT['tīṇi']})",
    "(cattāripi gaṇanāni passitvā kātabbāni)": f"({GANANA} {CNT['cattāri']}လုံးကိုလည်း {PASSITVA} {KATABBA})",
    "(paripuṇṇaṃ kātabbaṃ)": f"({PARIPUNNA}အောင် {KATABBA})",
    "(paccanīyaṃ paripuṇṇaṃ kātabbaṃ)": f"(အငြင်းပြ ပုံစံကို {PARIPUNNA}အောင် {KATABBA})",
    "(evaṃ paṭisandhikkhaṇe cattāro)": f"({EVAM_THUS} {PS}၌ {F.PAA[4]})",
    "(pavattipi, paṭisandhipi dīpetabbā)": f"({PAVATTI}ကိုလည်း{C} {F.PATISANDHI}ကိုလည်း {DIPET})",
    "(dve vārā vitthāretabbā)": f"(ဖော်ပြချက် {CNT['dve']}ကို {VITTH})",
    "(paṭhamaudāharaṇe pavatte paṭisandhikkhaṇe satta pañhā kātabbā)":
        f"(ပထမ {UDAHARANA}၌ {PAVATTI}၌{C} {PS}၌ {PANHA} {CNT['satta']} {KATABBA})",
    "(yathā paṭiccanaye tathā pañca pañhā kātabbā)":
        f"({PATICCA_V}၏ {NAYA}၌ ပြုသကဲ့သို့ {TATHA} {PANHA} {CNT['pañca']} {KATABBA})",
    "(naārammaṇasadisaṃ)": f"({negbare('ārammaṇa')}{SADISA})",
    "(paṭisandhikāni cattāri.": f"({F.PATISANDHI}နှင့် ဆိုင်သည်တို့ {CNT['cattāri']}{END}",
})
# notes whose Pāli holds condition words: prep() puts a placeholder in their place (the checker reads the Pāli)
PITI_T = TRIADS_ADD["piti"]["pītisahagat"]
NOTEP = {"(āsevane vipākaṃ natthi)": f"({cd('āsevana', 'loc')} ကံ၏ အကျိုး {NATTHI})",
         "(anantarapaccayopi samanantarapaccayopi sadiso)":
         f"({cn('anantara')}လည်း{C} {cn('samanantara')}လည်း {G.SADISO})",
         "(paṭiccasadisaṃ sahajāte dasa pañhā)":
         f"({F.HEAD['Paṭiccavāro']}{SADISA}{C} {cd('sahajāta', 'loc')} {PANHA} {CNT['dasa']})",
         "(cattāri kātabbāni, pītisahagataṃ anumajjantena vibhajitabbaṃ)":
         f"({CNT['cattāri']} {KATABBA}{C} {PITI_T} {F.DHAMMA}ကို {ANUMAJJ} {VIBHAJ})"}
for _i, (_p, _my) in enumerate(NOTEP.items()):
    F.NOTES[f"(⁑{_i})"] = _my


# whole units: registered by their Pāli (after prep), keyed by the skeleton; templates use the slots in order
def sk(pali, tpl):
    key, slots = F.slot(F.lc(F.pe(pali.strip())))
    F.render(tpl, slots)                     # every slot must be used (raises otherwise)
    SK[key] = tpl


def kloc(sl, i=0):
    st, ng, num = sl["K"][i]
    return cd(st, "loc", ng), CNT[num]


HLINES["(Dutiyo bhāgo)"] = new("(Dutiyo bhāgo)", "(ဒုတိယ အပိုင်း)")
HLINES["Paccanīye"] = S.PH["paccanīye"]
HLINES["Paccanīyānulomaṃ"] = "အငြင်းပြ အဟုတ်ပြ ပုံစံ"
SK["§C§o"] = "{C1.n}"                                                   # «Hetupaccayo.» (a line naming the condition)

# --- whole units (2-01 vitakkattika) ---------------------------------------------------------------------------------
THUS = new("evaṃ (thus)", "ဤသို့")                                     # 1-03 «evaṃ kātūna» «ဤသို့ ပြု၍»
MUL_A = new("-mūlakā (attributive)", "ကို အခြေခံသော")
GACCH = new("gacchantena (with saha / X-)", "တွဲ၍ သွားစေလျက်")
VIPAKA_N = "ကံ၏ အကျိုး"                                                 # vipāka (noun; 1-03 «kammaṃ vipākassa»)
MOHA = F.LEX["moho"][0]
GANENTENA = new("gaṇentena", "ရေတွက်သောအခါ")
GAMANA = new("gamanāni", "သွားပုံ")
LAK = F.LAKAUNG
DH = F.DHAMMA
sk("(dve paccayā sajjhāyamaggena vibhattā, evaṃ avasesā vīsatipaccayā vibhajitabbā.)",
   f"({F.PACCAYA} {F.PAA[2]}ကို {SAJJH} {VIBHATTA} {AVASESA} {F.PACCAYA} {G.TEEN['vīsati'][1]}ပါးကိုလည်း {EVAM_THUS} "
   f"{VIBHAJ}{END})")
sk("(Napurejātamūlake yathā suddhikaṃ arūpaṃ, tathā arūpā kātabbā).",
   f"({cd('purejāta', 'n', True)}{F.MULAKA}၌ {SUDDHIKA} {ARUPA_N}ကဲ့သို့{C} {TATHA} {ARUPA_N}များကို {KATABBA}){END}")
sk("(Naāsevanamūlake avitakkavicāramattaṃ vipākena saha gacchantena napurejātasadisaṃ kātabbaṃ, "
   "avitakkavicāramattañca avitakkavicāramattagacchantena vipāko dassetabbo.)",
   f"({cd('āsevana', 'n', True)}{F.MULAKA}၌ {{T1}} {DH}ကို {VIPAKA_N}နှင့်အတူ {GACCH} {negbare('purejāta')}"
   f"{SADISA_KAT}{C} {{T2}} {DH}ကိုလည်း {{T3}} {DH}နှင့် {GACCH} {{T4}} {DH}ကို {DASSET}{END})")
sk("(Sahajātavāropi paṭiccavārasadiso kātabbo.)", f"({VARA_N['Sahajātavāro']}ကိုလည်း {PATICCA_V}{SADISA_KAT}{END})")
sk("(Avasesesu dvīsu ghaṭanesu pavatti paṭisandhi vitthāretabbā.)",
   f"({AVASESA} {F.GHATANA} {CNT['dve']}တို့၌ {PAVATTI}နှင့် {F.PATISANDHI}ကို {VITTH}{END})")
sk("(Hetupaccayaṃ anumajjantena paccayavāro vitthāretabbo.",
   f"({{C1.obj}} {ANUMAJJ} {VARA_N['Paccayavāro']}ကို {VITTH}{END}")
sk("Yathā paṭiccagaṇanā evaṃ gaṇetabbā.", f"{G.YX['paṭiccagaṇanā']}အတိုင်း {EVAM} {GANETABBA}{END}")
sk("Adhipatiyā sattatiṃsa, purejāte ca āsevane ca ekavīsa, ayaṃ ettha viseso.)",
   f"{{K1}}{C} {cd('purejāta', 'loc')}{LAK}{C} {cd('āsevana', 'loc')}{LAK} {CNT['ekavīsa']}{C} ဤနေရာ၌ "
   f"ဤသည်မှာ {VISESA} ဖြစ်သည်{END})")
SK["paccanīye"] = S.PH["paccanīye"]
sk("nahetuyā tettiṃsa pañhā, sattasu ṭhānesu satta mohā uddharitabbā mūlapadesuyeva.",
   lambda sl: (f"{kloc(sl)[0]} {PANHA} {kloc(sl)[1]}{C} နေရာ {CNT['satta']}၌ {MOHA} {CNT['satta']}ကို မူလ "
               f"{F.PADA}တို့၌သာ {UDDHAR}{END}"))
sk("Naārammaṇe satta cittasamuṭṭhānā uddharitabbā.",
   lambda sl: f"{kloc(sl)[0]} {G.CITTASAM} ရုပ် {kloc(sl)[1]}ကို {UDDHAR}{END}")
for _t in ("Savitakkasavicāramūlakā", "Avitakkavicāramattamūlakā"):
    sk(f"{_t} satta pañhā naadhipatiyā kātabbā.",
       f"{{T1}} {DH}{MUL_A} {PANHA} {CNT['satta']}ကို {cd('adhipati', 'loc', True)} {KATABBA}{END}")
    sk(f"({_t} sattapi pañhā paripuṇṇā.)",
       f"({{T1}} {DH}{MUL_A} {PANHA} {CNT['satta']}လုံးလည်း {PARIPUNNA}ကြသည်{END})")
    sk(f"({_t} pañca pañhā kātabbā, vipākanti niyāmetabbā.)",
       f"({{T1}} {DH}{MUL_A} {PANHA} {CNT['pañca']} {KATABBA}{C} {VIPAKA_N}ဟု {NIYAM}{END})")
    for _n in ("satta", "pañca"):
        sk(f"({_t} iminā kāraṇena {_n} pañhā vibhajitabbā.)",
           f"({{T1}} {DH}{MUL_A} {PANHA} {CNT[_n]}ကို {IMINA} {VIBHAJ}{END})")
        sk(f"({_t} {_n} pañhā iminā kāraṇena vibhajitabbā.)",
           f"({{T1}} {DH}{MUL_A} {PANHA} {CNT[_n]}ကို {IMINA} {VIBHAJ}{END})")
    sk(f"({_t[:-1]}e avasesā pañhā sahajātapaccayasadisā.)",
       f"({{T1}} {DH}{F.MULAKA}၌ {AVASESA} {PANHA}တို့သည် {cn('sahajāta')}{SADISA_PL}{END})")
    sk(f"({_t} pañca pañhā.", f"({{T1}} {DH}{MUL_A} {PANHA} {CNT['pañca']}{END}")
sk("(Paṭhamaghaṭanāyaṃ sampuṇṇā satta pañhā kātabbā.)",
   f"(ပထမ {F.GHATANA}၌ {SAMPUNNA} {PANHA} {CNT['satta']} {KATABBA}{END})")
sk("(Paṭisandhikkhaṇe pañca pañhā kātabbā.", f"({PS}၌ {PANHA} {CNT['pañca']} {KATABBA}{END}")
sk("Yattha avitakkavicāramattaṃ āgacchati tattha vipākaṃ kātabbaṃ.",
   f"{YATTHA}၌ {{T1}} {DH} {AGACCHATI} {TATTHA}၌ {{T2}} {DH}အဖြစ် {KATABBA}{END}")
sk("Yattha avitakkavicāramattopi āgacchati, tattha vipākā kātabbā.",
   f"{YATTHA}၌ {{T1}} {DH}သည်လည်း {AGACCHATI}{C} {TATTHA}၌ {{T2}} {DH}များအဖြစ် {KATABBA}{END}")
sk("Naadhipatimūlake sattatiṃsa pañhā kātabbā.)",
   f"{cd('adhipati', 'n', True)}{F.MULAKA}၌ {PANHA} {CNT['sattatiṃsa']} {KATABBA}{END})")
sk("Naanantarampi {naanantarepi (ka.)} nasamanantarampi naaññamaññampi naupanissayampi satta pañhā rūpaṃyeva.",
   f"{cd('anantara', 'loc', True)}လည်း {{V1}}{C} {cd('samanantara', 'loc', True)}လည်း{C} "
   f"{cd('aññamañña', 'loc', True)}လည်း{C} {cd('upanissaya', 'loc', True)}လည်း {PANHA} {CNT['satta']}{C} "
   f"ရုပ်သာ ဖြစ်သည်{END}")
sk("Napurejāte sattatiṃsa paṭiccavārapaccanīyasadisaṃ.", f"{{K1}}သည် {PATICCA_V}၏ အငြင်းပြ ပုံစံ{SADISA}{END}")
sk("Napacchājāte sattatiṃsa, naāsevanepi sadisaṃ.", f"{{K1}}{C} {cd('āsevana', 'loc', True)}လည်း တူသည်{END}")
sk("(Navipāke sattatiṃsa pañhā kātabbā.", lambda sl: f"({kloc(sl)[0]} {PANHA} {kloc(sl)[1]} {KATABBA}{END}")
sk("Naāhārapaccayā naindriyapaccayā najhānapaccayā namaggapaccayā nasampayuttapaccayā navippayuttapaccayā "
   "nonatthipaccayā novigatapaccayā vitthāretabbā.)",
   lambda sl: (C + " ").join(cd(st, "n", ng) for st, ng in sl["C"]) + f"ကို {VITTH}{END})")
sk("(Nissayampi ninnānaṃ)", f"({cn('nissaya')}သည်လည်း {G.NANATTA} {NATTHI})")
sk("(Hetupaccayaṃ anumajjantena sabbe paccayā vitthāretabbā).",
   f"({{C1.obj}} {ANUMAJJ} {F.PACCAYA} အားလုံးကို {VITTH}){END}")
sk("(Paccanīyaṃ kātabbaṃ asammohantena.)", f"(အငြင်းပြ ပုံစံကို {ASAMM} {KATABBA}{END})")
sk("Avasesā sahajātapaccayasadisā.)", f"ကြွင်းသည်တို့သည် {cn('sahajāta')}{SADISA_PL}{END})")
HLINES["*Natthivigatāvigatapaccayā*"] = G.HLINES["*Natthi-vigatāvigatapaccayā*"]
sk("(Natthipaccayañca vigatapaccayañca anantarasadisaṃ, avigataṃ atthisadisaṃ.)",
   f"({cn('natthi')}{LAK}{C} {cn('vigata')}{LAK} {F.N['anantara']}{SADISA}{C} {F.N['avigata']}သည် "
   f"{F.N['atthi']}{SADISA}{END})")
sk("(Ghaṭanā kusalattikasadisāyeva.", f"({F.GHATANA}များသည် {S.KT}နှင့်ပင် တူကြသည်{END}")
sk("Pañhāvāragaṇanaṃ evaṃ asammohantena gaṇetabbaṃ.)",
   f"{F.HEAD['Pañhāvāro']}၏ {GANANA}ကို {THUS} {ASAMM} {GANETABBA}{END})")
sk("Paccanīyuddhāro.", F.HEAD["Paccanīyuddhāro"] + END)
sk("(Paccanīyaṃ gaṇentena imāni padāni anumajjantena gaṇetabbāni.)",
   f"(အငြင်းပြ ပုံစံကို {GANENTENA} ဤ {F.PADA}တို့ကို {ANUMAJJ} {GANETABBA}{END})")
sk("(Anulomapaccanīyagaṇanā iminā kāraṇena gaṇetabbā.)", f"({G.YX['anulomapaccanīyagaṇanā']}ကို {IMINA} {GANETABBA}{END})")
sk("(Paccanīyānulomaṃ iminā kāraṇena vibhajitabbaṃ.)", f"(အငြင်းပြ အဟုတ်ပြ ပုံစံကို {IMINA} {VIBHAJ}{END})")

# --- whole units (2-02 pītittika) ------------------------------------------------------------------------------------
sk("(Evaṃ anulomagaṇanā gaṇetabbā.)", f"({THUS} {G.YX['anulomagaṇanā']}ကို {GANETABBA}{END})")
sk("(Iminā kāraṇena dasa pañhā vitthāretabbā.)", f"({IMINA} {PANHA} {CNT['dasa']}ကို {VITTH}{END})")
SKF["(paripuṇṇaṃ, paṭisandhi natthi)"] = F.NOTES["(paripuṇṇaṃ, paṭisandhi natthi)"]
sk("(Namaggapaccayā nahetupaccayasadisaṃ.", f"({{C1.ab}} {F.NOTES['(nahetupaccayasadisaṃ)'][1:-1]}{END}")
sk("Moho natthi.", f"{MOHA} {NATTHI}{END}")
sk("Navippayuttapaccayā paripuṇṇaṃ arūpapañhameva.)",
   f"{{C1.ab}} {ARUPA_N}ဆိုင်ရာ {PANHA}သာ {PARIPUNNA}သည်{END})")
sk("(Anulomapaccanīyaṃ vitthārena gaṇetabbaṃ.)", f"(အဟုတ်ပြ အငြင်းပြ ပုံစံကို {G.NEW['vitthārena']} {GANETABBA}{END})")
HLINES["*2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*"] = \
    G.HLINES["*2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*"].replace("*2-6 ", "*2-6. ")
sk("(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.)",
   "(" + (C + " ").join(VARA_N[v] + "လည်း" for v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro",
                                                       "Sampayuttavāro")) + f" {PATICCA_V}{SADISA_PL}{END})")
sk("(Iminā kāraṇena sabbesaṃ padānaṃ paccayoti dīpetabbo).",
   f"({IMINA} {F.PADA} အားလုံးတို့အား {F.PACCAYA} ဖြစ်သည်ဟု {DIPET}){END}")
sk("(Tāniyeva ca gamanāni niyāmetabbāni.)", f"(ထို {GAMANA}များကိုပင်လည်း {NIYAM}{END})")
sk("Pītinayaṃ passitvā kātabbaṃ).", f"ပီတိ {NAYA}ကို {PASSITVA} {KATABBA}){END}")
sk("(Yathā paṭiccavāre hetupaccaye evaṃ vitthāretabbā dasa pañhā.)",
   f"({PATICCA_V}၌ {cn('hetu')}၌ ပြုသကဲ့သို့ {EVAM} {PANHA} {CNT['dasa']}ကို {VITTH}{END})")
sk("(Kusalattikaṃ anulomaṃ anumajjantena gaṇetabbaṃ.)", f"({S.KT}၏ အဟုတ်ပြ ပုံစံကို {ANUMAJJ} {GANETABBA}{END})")
for _p, _my in (("Paccanīyaṃ", "အငြင်းပြ ပုံစံ"), ("Anulomapaccanīyaṃ", "အဟုတ်ပြ အငြင်းပြ ပုံစံ"),
                ("Paccanīyānulomaṃ", "အငြင်းပြ အဟုတ်ပြ ပုံစံ")):
    sk(f"({_p} anumajjantena gaṇetabbaṃ.)", f"({_my}ကို {ANUMAJJ} {GANETABBA}{END})")
for _st in F.STEMS:                                    # bare condition stems before «…» («āhāra… indriya…»)
    SKF.setdefault(_st, F.N[_st])

F.HLINES.update(HLINES)
F.SK.update(SK)
F.SKF.update(SKF)


REVIEW = False


def chapter(name):
    txt = F.translate(prep((PALI / name).read_text(encoding="utf-8-sig")))
    if not F.DEV or REVIEW:
        (OUT / name).write_text(txt, encoding="utf-8")
        print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


if __name__ == "__main__":
    F.DEV = "--dev" in sys.argv
    if "--out" in sys.argv:
        REVIEW = True
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    for n in names:
        chapter(n)
    if F.DEV:
        for k, v in F.UNSEEN.items():
            print("SK:", k)
            print("   ", v)
        print(len(F.UNSEEN), "unmatched")
    if F.SLIPS:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")
    if "--new" in sys.argv:                  # every string this script adds, and any existing value it changes
        for t in _TABLES:
            for k, v in getattr(F, t).items():
                if k not in _BEFORE[t]:
                    v = "(frame)" if callable(v) else (v[0] if isinstance(v, tuple) else v)
                    print(f"- {k} = {v}  [{t}]")
                elif _BEFORE[t][k] != v:
                    print(f"CHANGED [{t}] {k}")
        for k, v in NEW.items():
            print(f"- {k} = {v}  [NEW]")
