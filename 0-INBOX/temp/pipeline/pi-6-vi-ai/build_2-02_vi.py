# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 2-02-khandhayamaka.md (nirodhavāra continued, uppādanirodhavāra,
pariññāvāra), and FRAME-SETTER of family E (pariññāvāra: parijānāti in its tenses and the person frames).

Families A / B come VERBATIM from build_2-01_vi (members, verbs, beings, planes, question and answer frames); the
person / place shape there is the 7-01 one. Family E reuses the 7-01 yo / so question frame (YO_REL_VI, YO_DEM_VI,
YO_Q_FRAME, YO_VERB["parijānāti"]) and the 7-04 nominative-person answer frames (BUT_C, BOTH_C, STATEMENT_PERSON,
STATEMENT_RES, PERSON_NOM_VI), and adds the tenses, the new persons and the relative subjects.

Later chapters with a pariññāvāra (Āyatana, Dhātu, Sacca, Saṅkhāra, Dhamma, Indriya …) use:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    E = importlib.import_module("build_2-02_vi")
    E.e_q(x, v1, y, v2, label="Ka", vapana=False)   (Ka) yo X v1 so Y v2ti?   (x, y = Vietnamese object phrases)
    E.e_vparse("na parijānittha")                    -> (base, tense, neg) triple, any tense / number
    E.e_pred(o, v) / E.e_deny(o, v)                  «hiểu biết trọn vẹn X» … / the predicate after «no ca»
    E.e_subject("Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te")  -> (Vietnamese head, res or None)
    E.e_but(subj, x, v1, y, v2) / E.e_both(subj, x, v1, y, v2)          whole answer sentences
    E.translate_e(sentence, member_fn)               the whole family-E sentence parser (member_fn: Pāli -> VI)
    E.PARINNA_EXACT                                  Pariññāvāro. and the bare time headings
Also new for family B (any yamaka): who2() (the «ye ca … upapajjitvā parinibbāyissanti [tesaṃ cavantānaṃ]» groups),
pe_fragment() («Yattha X v…pe….»), PARIPUNNA («(yatthakaṃ paripuṇṇaṃ kātabbaṃ)»), YATHA_VIBHATTA, pe_end().

Importing writes nothing; run  python -I -X utf8 -B build_2-02_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B (frame-setter)
A = importlib.import_module("build_7-01_vi")     # yo / so question frame, YO_VERB (family C frame-setter)
C4 = importlib.import_module("build_7-04_vi")    # nominative person answer frames (coordinator «From 7-04»)

NAME = "2-02-khandhayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
SLIPS = []

# ================================================================ FAMILY E: pariññāvāra
E_BASE = "hiểu biết trọn vẹn"                    # parijānāti (pi-2 / pi-5 «hiểu biết trọn vẹn»; 7-01 YO_VERB)
E_PRED = "{v} {o}"                               # verb + object (rūpakkhandhaṃ parijānāti = hiểu biết trọn vẹn khối vật chất)
# tenses / polarity / «no ca» denial: the family-B tables of build_2-01_vi, so both families say the same:
#   parijānāti / parijānanti     = hiểu biết trọn vẹn        na … = không hiểu biết trọn vẹn     no ca na … = vẫn hiểu biết trọn vẹn
#   parijānittha                 = đã hiểu biết trọn vẹn     na … = chưa từng hiểu biết trọn vẹn no ca na … = đã từng hiểu biết trọn vẹn
#   parijānissati / parijānissanti = sẽ hiểu biết trọn vẹn   na … = sẽ không hiểu biết trọn vẹn  no ca na … = vẫn sẽ hiểu biết trọn vẹn
E_V = r"(?:na )?parijān(?:ātīti|āti|anti|itthāti|ittha|issatīti|issati|issanti)"
E_VFORM = re.compile(r"(?P<neg>na )?parijān(?P<t>ātīti|āti|anti|itthāti|ittha|issatīti|issati|issanti)")
E_TENSE = {"āti": "pres", "ātīti": "pres", "anti": "pres", "ittha": "past", "itthāti": "past",
           "issati": "fut", "issatīti": "fut", "issanti": "fut"}       # plural = singular (Vietnamese has no number)
E_REL = A.YO_REL_VI["yo"]                        # yo = người nào (7-01)
E_DEM = A.YO_DEM_VI["so"]                        # so = người ấy (7-01)
E_Q_FRAME = A.YO_Q_FRAME                         # «{rel} {pa}, thì có phải {dem} {pb} không?» (7-01)
E_VA_PANA = A.VA_PANA                            # yo vā pana = «Còn người nào …» (7-01)
E_BUT_C = C4.BUT_C                               # «{pa}, nhưng {dem}{no}»  (A v1, no ca B v2; no pronoun after no ca)
E_BOTH_C = C4.BOTH_C                             # «{pa}, đồng thời cũng {pb}»  (Añca v1 Bñca v2)
E_STATEMENT_PERSON = C4.STATEMENT_PERSON         # «{head} {clause}.»  (nominative person subject, no comma)
E_STATEMENT_RES = C4.STATEMENT_RES               # «{head}, thì {res} {clause}.»  (relative subject + te)
E_TE = "những người ấy"                          # te (resumptive; 7-04 «te tato» = những người ấy, đối với nơi ấy)
# persons (nominative subjects; pi-4 / pi-5; 7-04 PERSON_NOM_VI)
AGGAMAGGA_NOM = "Người có được con đường tối thượng"
# Aggamaggasamaṅgī (coordinator «Shared person terms», = 7-05 … 7-08; pi-4 maggasamaṅgī «người có được con đường»;
# aṭṭhakathā: the one at the moment of the arahant path)
E_PERSON_NOM = dict(C4.PERSON_NOM_VI, **{"Aggamaggasamaṅgī": AGGAMAGGA_NOM})   # Arahā = Bậc A-la-hán (7-04) …
E_PERSON_ACC = {"arahantaṃ": low(C4.PERSON_NOM_VI["Arahā"]),                 # arahantañca … ṭhapetvā
                "aggamaggasamaṅgiṃ": low(AGGAMAGGA_NOM)}                      # aggamaggasamaṅgiñca … ṭhapetvā
E_AVASESA = "những hạng người"                   # avasesā puggalā (coordinator: puggala «hạng người», pi-4 / 7-04), via F.a_except_n
E_YE = {                                         # relative subjects «Ye … (te)» / «ye ca … (te)»
    "maggaṃ paṭilabhissanti": "những người nào sẽ đạt được con đường",                  # magga «con đường» pi-4
    "puthujjanā maggaṃ na paṭilabhissanti": "những người phàm phu nào sẽ không đạt được con đường",  # pi-4 / pi-5
}
E_AND = " và "                                   # «X ye ca …» = «X và …»
PARINNA_EXACT = {"Pariññāvāro.": S.SECTION["Pariññāvāro"] + "."}   # Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.


def e_vparse(s):
    mm = E_VFORM.fullmatch(s)
    if not mm:
        raise ValueError(f"unparsed parijānāti form {s!r}")
    return (E_BASE, E_TENSE[mm["t"]], bool(mm["neg"]))


def e_pred(o, v):
    return E_PRED.format(v=F.verb(*v), o=o)


def e_deny(o, v):
    return E_PRED.format(v=F.deny(*v), o=o)


def e_q(x, v1, y, v2, label="Ka", vapana=False):
    """(Ka) yo X v1 so Y v2ti? / (Kha) yo vā pana …; x, y = Vietnamese objects, v1, v2 = e_vparse triples."""
    s = E_Q_FRAME.format(rel=E_REL, pa=e_pred(x, v1), dem=E_DEM, pb=e_pred(y, v2))
    if vapana:
        s = E_VA_PANA + low(s)
    return f"{LABEL_VI[label]} {cap(s)}" if label else cap(s)


E_EXCEPT_RE = re.compile(r"(?P<a>\S+?)ñca (?P<b>\S+?)ñca ṭhapetvā avasesā puggalā")
E_PERSON_RE = "|".join(sorted(E_PERSON_NOM, key=len, reverse=True))
E_SUBJ_RE = re.compile(rf"(?P<p>{E_PERSON_RE})?(?: ?(?P<ye>[Yy]e(?P<ca> ca)? (?P<rel>.+)))?")


def e_subject(s):
    """Pāli subject of a pariññā answer -> (Vietnamese head, resumptive or None)."""
    res = None
    if s.endswith(" te"):
        s, res = s[:-3], E_TE
    mm = E_EXCEPT_RE.fullmatch(s)
    if mm:
        a, b = (E_PERSON_ACC[low(w) + "ṃ"] for w in (mm["a"], mm["b"]))
        return cap(F.a_except_n(F.a_and(a, b), E_AVASESA)), res
    mm = E_SUBJ_RE.fullmatch(s)
    if not mm or not (mm["p"] or mm["ye"]):
        raise ValueError(f"unparsed pariññā subject {s!r}")
    parts = [E_PERSON_NOM[mm["p"]]] if mm["p"] else []
    if mm["ye"]:
        assert bool(mm["ca"]) == bool(mm["p"]), s          # «X ye ca …» / «Ye …»
        parts.append(E_YE[mm["rel"]])
    assert res or not mm["ye"], s
    return cap(E_AND.join(parts)), res


def _e_statement(subj, clause):
    head, res = e_subject(subj)
    if res:
        return cap(E_STATEMENT_RES.format(head=head, res=res, clause=clause))
    return cap(E_STATEMENT_PERSON.format(head=head, clause=clause))


def e_but(subj, x, v1, y, v2):
    """S X v1, no ca Y v2.  (x, y Vietnamese objects; v1, v2 triples)"""
    return _e_statement(subj, E_BUT_C.format(pa=e_pred(x, v1), dem="", no=e_deny(y, v2)))


def e_both(subj, x, v1, y, v2):
    """S Xñca v1 Yñca v2."""
    return _e_statement(subj, E_BOTH_C.format(pa=e_pred(x, v1), pb=e_pred(y, v2)))


E_Q_RE = re.compile(rf"\((?P<l>Ka|Kha)\) yo(?P<vp> vā pana)? (?P<x>\S+) (?P<v1>{E_V}) so (?P<y>\S+) (?P<v2>{E_V})\?")
E_BUT_RE = re.compile(rf"(?P<s>.+?) (?P<x>\S+) (?P<v1>{E_V}), no ca (?P<y>\S+) (?P<v2>{E_V})\.")
E_BOTH_RE = re.compile(rf"(?P<s>.+?) (?P<x>\S+ñca) (?P<v1>{E_V}) (?P<y>\S+ñca) (?P<v2>{E_V})\.")


def _ca_obj(w):
    return w[:-3] + "ṃ" if w.endswith("ñca") else w      # rūpakkhandhañca -> rūpakkhandhaṃ


def translate_e(s, member_fn):
    """Family-E sentence -> Vietnamese, or None. member_fn: Pāli accusative member -> Vietnamese noun phrase."""
    if s in PARINNA_EXACT:
        return PARINNA_EXACT[s]
    mm = E_Q_RE.fullmatch(s)
    if mm:
        vp = bool(mm["vp"])
        if vp != (mm["l"] == "Kha"):
            SLIPS.append(f"label ({mm['l']}) on a {'vā pana' if vp else 'non-vā pana'} question: {s[:50]}")
        return e_q(member_fn(mm["x"]), e_vparse(mm["v1"]), member_fn(mm["y"]), e_vparse(mm["v2"]),
                   label=mm["l"], vapana=vp)
    mm = E_BUT_RE.fullmatch(s)
    if mm:
        return e_but(mm["s"], member_fn(mm["x"]), e_vparse(mm["v1"]), member_fn(mm["y"]), e_vparse(mm["v2"]))
    mm = E_BOTH_RE.fullmatch(s)
    if mm:
        return e_both(mm["s"], member_fn(_ca_obj(mm["x"])), e_vparse(mm["v1"]), member_fn(_ca_obj(mm["y"])),
                      e_vparse(mm["v2"]))
    return None


# ================================================================ family B additions (any yamaka)
YE_CA_CAVANTA = "những người đang chết đi mà sau khi tái sinh vào {p} sẽ nhập Niết-bàn trọn vẹn"
# ye ca <P>ṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ (inside a genitive beings phrase)
YE_CA_JOIN = " và "                              # <beings> ye ca … = «<beings> và …»
YE_CA_RE = re.compile(r"(?P<p>\S+) upapajjitvā parinibbāyissanti(?P<c> tesaṃ cavantānaṃ)?")


def _acc_plane(w):
    case, stem = F._plane_case(w)
    assert case == "acc", w
    return F.PLANE[stem]


def who2(phrase):
    """F.who() plus the syndetic «… ye ca <P>ṃ upapajjitvā parinibbāyissanti [tesaṃ cavantānaṃ]» group."""
    if " ye ca " not in phrase:
        return F.who(phrase)
    left, right = phrase.split(" ye ca ", 1)
    mm = YE_CA_RE.fullmatch(right)
    if not mm:
        raise ValueError(f"unparsed ye ca group {phrase!r}")
    p = _acc_plane(mm["p"])
    r = (YE_CA_CAVANTA if mm["c"] else F.YE_UPAPAJJITVA).format(p=p)
    return F.who(left) + YE_CA_JOIN + r


PE = A.PE                                        # …pe… = … (sample)
PE_FRAG = "{rel} mà {a} {pa}"                    # Yattha X v…pe…. = «Ở nơi nào mà X v…» (start of Q_FRAME)
PARIPUNNA = "(phần về nơi chốn nên được trình bày đầy đủ)"   # (yatthakaṃ paripuṇṇaṃ kātabbaṃ)
YATHA_VIBHATTA = "(Như {x} đã được phân tích trong {v}, ở đây cũng nên phân tích như vậy)."
# (Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ). (pi-2 ^2 «(Như đã được phân tích trong …,
# ở đây cũng nên phân tích như vậy.)»; the Pāli period stands outside the bracket)
FRAG_RE = re.compile(r"(?P<w>Yattha|Yassa|Yassa yattha) (?P<x>\S+) (?P<v>(?:na )?\S+?)(?P<e>…pe…\.| \(yatthakaṃ "
                     r"paripuṇṇaṃ kātabbaṃ\)\.)")


def pe_fragment(kind, x, v, end):
    """«Yattha X v…pe….» / «Yattha X v (yatthakaṃ paripuṇṇaṃ kātabbaṃ).»"""
    s = cap(PE_FRAG.format(rel=F.REL_VI[kind], a=x, pa=F.verb(*v)))
    return s + (PE if end.startswith("…") else f" {PARIPUNNA}.")


def pe_end(vi_sentence):
    """A statement ending «…pe….»: its period gives way to «…» (7-04 rule; «….» is never written)."""
    assert vi_sentence.endswith("."), vi_sentence
    return vi_sentence[:-1] + PE


# ================================================================ closing lines of this chapter
EXACT = {
    "Nirodhavāro.": cap(S.SECTION["nirodhavāro"]) + ".",                       # Mục về sự chấm dứt.
    "Uppādanirodhavāro.": S.SECTION["Uppādanirodhavāro"] + ".",                # Mục về sự sinh khởi và sự chấm dứt.
    "Pavattivāro niṭṭhito.": f"{S.SECTION['Pavattivāro']} {S.NITTHITA}.",      # Mục về sự diễn tiến đã hoàn tất.
    "Khandhayamakapāḷi niṭṭhitā.": S.yamaka_end("Khandhayamakaṃ"),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
    "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).":
        YATHA_VIBHATTA.format(x=low(S.SECTION["Paccuppannātītavāro"]), v=low(S.SECTION["uppādavāro"])),
    "No.": A.NO,                                                               # Không.
    **PARINNA_EXACT,
}

# source slips (rendered as meant; each must apply exactly once)
SLIP_FIX = [
    ("tassa vadanākkhandho nirujjhitthāti?", "tassa vedanākkhandho nirujjhitthāti?",
     "^6-2-185: «vadanākkhandho» = vedanākkhandho (spelling)"),
    ("saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati.",
     "saññākkhandho ca nirujjhissati vedanākkhandho ca nirujjhati.",
     "^6-2-134: second «ca» missing («… vedanākkhandho nirujjhati»); rendered with the «đồng thời … cũng» frame"),
    ("rūpakkhandho ca na nirujjhittha, vedanākkhandho ca na nirujjhissati.",
     "rūpakkhandho ca na nirujjhittha vedanākkhandho ca na nirujjhissati.",
     "^6-2-151: comma inside the «A ca … B ca …» clause; the Vietnamese frame has its comma anyway"),
    ("tesaṃ tattha rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati.",
     "tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca na nirujjhati.",
     "^6-2-163: first «ca» missing («rūpakkhandho nuppajjati vedanākkhandho ca …»); rendered with the both-frame"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, why in SLIP_FIX:
        if a in s:
            s = s.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return s


# ================================================================ sentence translation
def translate_sentence(s, ctx=""):
    s = fix_slips(s)
    if s in EXACT:
        return EXACT[s]
    if s.endswith("…pe…."):
        mm = FRAG_RE.fullmatch(s)
        if mm:
            kind = mm["w"].lower()
            return pe_fragment(kind, F.m(mm["x"]), F.vparse(mm["v"], ctx), mm["e"])
        return pe_end(translate_sentence(s[:-len("…pe….")] + ".", ctx))
    mm = FRAG_RE.fullmatch(s)
    if mm:
        return pe_fragment(mm["w"].lower(), F.m(mm["x"]), F.vparse(mm["v"], ctx), mm["e"])
    r = translate_e(s, F.m)
    if r:
        return r
    for rx, both in ((F.B_PERSON_NOT, False), (F.B_PERSON_BOTH, True)):
        mm = rx.fullmatch(s)
        if mm:
            if not both:
                assert bool(mm["t"]) == bool(mm["t2"]), s
            res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
            f = F.b_both if both else F.b_not
            return f(res, who2(mm["g"]), F.m(mm["x"]), F.vparse(mm["v1"], ctx), F.m(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return F.translate_sentence(s, ctx)


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + F.heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    return " ".join(translate_sentence(s, ctx) for s in F.split_sentences(t)) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for ln in src.splitlines():
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("hiểu biết trọn vẹn", 2), ("hiểu biết trọn vẹn", 5), ("không hiểu biết trọn vẹn", 5),
    ("có được con đường", 4), ("con đường", 4), ("tối thượng", 2), ("Bậc A-la-hán", 4),
    ("bậc A-la-hán", 5), ("những người phàm phu", 4), ("những người phàm phu", 5), ("hạng người", 4),
    ("đạt được", 2), ("ở đây cũng nên phân tích như vậy", 2), ("Như đã được phân tích trong", 2),
    ("đầy đủ", 2), ("nên được trình bày", 2), ("phần về", 1), ("chết đi", 2), ("tái sinh", 2),
    ("nhập Niết-bàn trọn vẹn", 5),
]   # «No. = Không.» is the coordinator's shared frame (7-01 NO), not a pi-1..5 string


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (2-02): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT:
            yield p
            continue
        yield from F.split_sentences(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 2-02 and against 2-01."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s) if s not in EXACT else EXACT[s]
        if seen.setdefault(s, t) != t:
            bad += 1
    p201 = (S.PALI_DIR / F.NAME).read_text(encoding="utf-8")
    shared = 0
    for s in set(_sentences(p201)) & set(seen):
        shared += 1
        if F.translate_sentence(s, "") != seen[s] and s not in EXACT:
            print("DIFFERS FROM 2-01:", s)
            bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 2-01")
    return bad


def check_family_e():
    """Family E present tense = the 7-01 YO_VERB proposal for parijānāti, byte for byte."""
    o = "khối vật chất"
    yv = A.YO_VERB
    assert e_pred(o, e_vparse("parijānāti")) == yv["parijānāti"]["p"].format(t=o)
    assert e_deny(o, e_vparse("parijānāti")) == yv["parijānāti"]["no"].format(t=o)
    assert e_pred(o, e_vparse("na parijānāti")) == yv["na parijānāti"]["p"].format(t=o)
    assert e_deny(o, e_vparse("na parijānāti")) == yv["na parijānāti"]["no"].format(t=o)
    assert E_PERSON_NOM["Arahā"] == "Bậc A-la-hán"


def main():
    S.check_cross_book()
    F.check_cross_book()
    check_cross_book()
    check_family_e()
    SLIPS.clear(); F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in used:
        print("SLIP", why)
    for c, w in F.SLIPS + [("", x) for x in SLIPS]:
        print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
