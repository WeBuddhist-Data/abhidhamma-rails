# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 5-01-saccayamaka.md (Saccayamaka, paṇṇattivāra and uppādavāra).

Families A / B come VERBATIM from build_2-01_vi (question / answer frames, verbs, beings, planes; the person / place
shape there is the 7-01 one); additions from build_2-02_vi (relative subjects E_YE, pe_fragment, pe_end), and the
citta-moment vocabulary from build_8_vi (AT / OF / MOMENT, THEY, NIRODHA_PERSONS, SAMANGI, citta()).

New here (the Saccayamaka is the first yamaka whose pavattivāra names citta moments, paths and persons): the four
truths as members, and a head parser for the long genitive / locative answer heads («Sabbesaṃ upapajjantānaṃ pavatte
taṇhāvippayuttacittassa uppādakkhaṇe …»). 5-02 and 5-03 (and later Saṅkhāra / Dhamma / Indriya agents) use:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    T = importlib.import_module("build_5-01_vi")
    T.m("samudayasaccaṃ")            member word -> Vietnamese noun phrase (sacca members)
    T.head_vi("Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe")   answer head -> «Ở …, trong quá trình …»
    T.translate_sentence(s, ctx)     the whole sentence parser (families A, B; «?…pe…» shortenings)
    T.variant(br)                    variant bracket incl. the «evaṃ …» tails
    T.HEAD_RULES / T.PLANE_LOC / T.NOUN_OF / T.CITTA_KIND     tables to extend locally

Importing writes nothing; run  python -I -X utf8 -B build_5-01_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")     # family E, E_YE relative subjects, pe_fragment / pe_end
C8 = importlib.import_module("build_8_vi")       # citta moments (family D)

NAME = "5-01-saccayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
SLIPS = []

# ================================================================ members (pi-2 Saccavibhaṅga / Dhammahadayavibhaṅga)
# pi-2 ^2-982: «Sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường»
# pi-2 4-saccavibhango: «Bốn sự thật – khổ đau, sự phát sinh của khổ đau, …»
SACCA_STEM = {"dukkha": "khổ đau", "samudaya": "sự phát sinh", "nirodha": "sự chấm dứt", "magga": "con đường"}
SACCA_OF = "sự thật về {x}"
MEMBER = {
    "saccaṃ": "sự thật", "saccā": "các sự thật",                   # sacca (sg / pl: the Pāli number is kept, 2-01)
    "dukkhaṃ": SACCA_STEM["dukkha"],
    "samudayo": SACCA_STEM["samudaya"], "samudayaṃ": SACCA_STEM["samudaya"],
    "nirodho": SACCA_STEM["nirodha"], "nirodhaṃ": SACCA_STEM["nirodha"],
    "maggo": SACCA_STEM["magga"], "maggaṃ": SACCA_STEM["magga"],
}
for _k, _v in SACCA_STEM.items():
    MEMBER[f"{_k}saccaṃ"] = SACCA_OF.format(x=_v)
CATTARI = ("Bốn sự thật – " + ", ".join(SACCA_OF.format(x=v) for v in SACCA_STEM.values()) + ".")
# Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ. (missing comma rendered as meant)
KAYIKA_CETASIKA = f"{SACCA_STEM['dukkha']} nơi thân, {SACCA_STEM['dukkha']} trong tâm"
# Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ (pi-1 kāyika «nơi thân», cetasika «trong tâm»; the member word «khổ đau» is kept so
# the answer names the same «dukkha» the question asks about)
SUBJECT = {"Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ": KAYIKA_CETASIKA}


def m(w):
    """Member word (any case form, capitalised or not, «-ñca» accepted) -> Vietnamese noun phrase."""
    w = low(w)
    if w.endswith("ñca"):
        w = w[:-3] + "ṃ"
    return MEMBER[w]


def subj(w):
    return SUBJECT.get(w) or m(w)


# ================================================================ variants
VAR_TAIL = {
    " evamuparipi": F.EVAMUPARIPI,                                             # 2-01 «, cũng vậy ở các chỗ sau»
    " evaṃ avasesesu tīsu saccesu": ", cũng vậy ở ba sự thật còn lại",
    " evaṃ puggalokāsepi nirodhavārepi": (", cũng vậy ở phần về người và nơi chốn và ở "
                                          + low(S.SECTION["nirodhavāro"])),
    " puggalokāsavārepi": ", cũng vậy ở mục về người và nơi chốn",
}


def variant(br):
    """[t (sī. syā.) tail] -> [dị bản (Sī., Syā.): t<tail>] (2-01 variant() plus the «evaṃ …» tails)."""
    mm = re.fullmatch(r"\[(?P<t>.+?) \((?P<s>[^)]+)\)(?P<e>[^\]]*)\]", br)
    assert mm, br
    sig = ", ".join(F.SIGLA[x] for x in mm["s"].split())
    return f"[{S.VAR} ({sig}): {mm['t']}{VAR_TAIL[mm['e']] if mm['e'] else ''}]"


def _var_vi(v):
    return f" {variant(v.strip())}" if v else ""


# ================================================================ headings
SECTION_5 = {
    "Suddhasaccavāro": S.VARO.format(x="các sự thật thuần túy"),                       # = Suddhakhandhavāro frame
    "Suddhasaccamūlacakkavāro": S.VARO.format(x="vòng luân chuyển dựa trên các sự thật thuần túy"),
    "Paṇṇattivāra": S.SECTION["Paṇṇattivāro"],     # ^6-5-6-0 stem form of Paṇṇattivāro (before «(Kha) niddeso»)
}


def heading(t):
    return SECTION_5[t] if t in SECTION_5 else F.heading(t)


# ================================================================ FAMILY A (2-01 frames, sacca members)
A_Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<n>[Nn]a )?(?P<x>\S+) (?:na )?(?P<y>\S+?)\?")


def a_question(s):
    mm = A_Q_RE.fullmatch(s)
    if not mm:
        return None
    x, y = low(mm["x"]), low(F._strip_ti(mm["y"]))
    if x not in MEMBER or y not in MEMBER:
        return None
    neg = bool(mm["n"])
    rest = s.split(") ", 1)[-1] if mm["l"] else s
    assert (" na " in rest) == neg, s                 # «na X na Y» or «X Y», never mixed
    if mm["l"]:
        return F.a_q(m(x), m(y), neg=neg, label=mm["l"])
    q = F.a_q(m(x), m(y), neg=neg, label=None)
    return q if s[0].isupper() else low(q)


def _pred(p):
    return F.a_not(m(p[3:])) if p.startswith("na ") else F.a_is(m(p))


A_EXCEPT_RE = re.compile(r"(?P<e>[^\[]+?) ṭhapetvā (?:avasesā|avasesaṃ|avaseso)(?P<n> saccā)? (?P<p1>(?:na )?\S+?)"
                         r"(?P<v> \[[^\]]+\])?,? (?P<p2>(?:na )?\S+)\.")
A_NEITHER_RE = re.compile(r"(?P<a>\S+)ñca (?P<b>\S+)ñca ṭhapetvā (?:avasesā|avasesaṃ|avaseso) na ceva (?P<c>\S+) "
                          r"na ca (?P<d>\S+)\.")
A_BOTH_RE = re.compile(r"(?P<s>.+?) (?P<a>\S+?)(?P<k>ñceva| ceva) (?P<b>\S+?)ñca\.")
A_REST_RE = re.compile(r"Avasesā (?P<n>saccā)(?P<v> \[[^\]]+\])? na (?P<b>\S+)\.")
EXCEPT_PE = F.A_EXCEPT.split(",")[0]          # «ngoại trừ {x}» (X ṭhapetvā…pe…)


def a_answer(s):
    mm = A_NEITHER_RE.fullmatch(s)
    if mm:
        return F.a_neither(F.a_except(F.a_and(m(mm["a"] + "ṃ"), m(mm["b"] + "ṃ"))), m(mm["c"]), m(mm["d"]))
    mm = A_EXCEPT_RE.fullmatch(s)
    if mm and "ñca" not in mm["e"] and (mm["p1"].startswith("na ") != mm["p2"].startswith("na ")):
        e = subj(mm["e"])
        head = F.a_except_n(e, m(mm["n"].strip())) if mm["n"] else F.a_except(e)
        if mm["v"] and "," not in s.split("]", 1)[1][:1]:
            SLIPS.append(f"«…{mm['p1']}{mm['v']} {mm['p2']}.»: no comma after the variant bracket; frame comma kept")
        return F.a_but_not(head, _pred(mm["p1"]) + _var_vi(mm["v"]), _pred(mm["p2"]))
    mm = A_BOTH_RE.fullmatch(s)
    if mm:
        a = mm["a"] + ("ṃ" if mm["k"] == "ñceva" else "")
        return F.a_both(subj(mm["s"]), F.a_is(m(a)), F.a_is(m(mm["b"] + "ṃ")))
    mm = A_REST_RE.fullmatch(s)
    if mm:
        return F.a_rest(m(mm["n"]), F.a_not(m(mm["b"])), _var_vi(mm["v"]))
    if s.endswith("ṭhapetvā…pe…."):
        parts = [p.strip() for p in s[:-1].split(C8.PE + "pe" + C8.PE) if p.strip()]
        out = []
        for p in parts:
            pm = re.fullmatch(r"(\S+) ṭhapetvā", p)
            assert pm, s
            out.append(EXCEPT_PE.format(x=m(pm[1])))
        return cap((C8.PE + " ").join(out)) + C8.PE   # «Ngoại trừ sự phát sinh… ngoại trừ sự chấm dứt…»
    return None


# ================================================================ FAMILY B: the answer head parser
# Every Pāli head is a sequence of groups. Person groups (genitive, or a relative clause) stand in one run under one
# «ở» (2-01 WHO_HEAD / LIST_SEP; 8 NIRODHA_ASANNA); a time / plane phrase stands on its own; groups are joined with
# «, »; «ye ca …» joins its run with «và» (2-02 YE_CA_JOIN); a sentence-initial «Ye …» relative takes no «ở» (2-01
# YE_UPAPAJJITVA). The inner resumptive «tesaṃ» (… ye ca … tesaṃ upapajjantānaṃ …) opens a new run «ở những người ấy».
PLANE_LOC = dict(F.PLANE, **{"apāya": "cõi khổ"})          # apāya «cõi khổ» (pi-2 Ñāṇavibhaṅga «tái sinh vào cõi khổ»)
AVASESA_LOC = "{p} còn lại"                                  # Avasese catuvokāre pañcavokāre
ANANTARA = "những người sẽ đạt được con đường tối thượng ngay sau tâm nào đó"
# yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (anantarā «ngay sau», coord = 9-01 / 6-01 «ngay sau đó»; aggamagga «con đường tối thượng»,
# coordinator; paṭilabhati «đạt được» 2-02; aṭṭhakathā ^6-176: the citta right before the path)
YE_ANNE = "những người khác nào sẽ đạt được con đường"   # ye caññe maggaṃ paṭilabhissanti (2-02 E_YE + «khác»)
ARAHANTANAM = "các bậc A-la-hán"                         # arahantānaṃ (pi-5 «các bậc A-la-hán»)
AGGAMAGGA_GEN = "những " + low(E.AGGAMAGGA_NOM)           # aggamaggasamaṅgīnaṃ = những người có được con đường tối thượng
ABHISAMETAVI = {"abhisametāvīnaṃ": "những người đã thấu hiểu",     # abhisameti «thấu hiểu» (pi-5)
                "anabhisametāvīnaṃ": "những người chưa thấu hiểu"}
SABBESAM_ALONE = "tất cả chúng sinh"                     # bare Sabbesaṃ (coord «Shared person terms»; pi-2, 6-01)
INNER_TESAM = C8.THEY                                    # inner tesaṃ = những người ấy
INNER_TESAM_PART = "{t} khi {p}"                         # tesaṃ upapajjantānaṃ = những người ấy khi đang tái sinh
PAVATTE = "trong đời sống"                               # pavatte (coord «Shared person terms», = 9-01)
PAVATTE_JOIN = "{a}, {b}"                                # pavatte cittassa uppādakkhaṇe = trong đời sống, vào …
CITTA_KIND = {                                           # <kind>cittassa … / <kind>citte vattamāne
    "": "tâm",
    "taṇhāvippayutta": "tâm không gắn liền với khao khát",           # taṇhā «khao khát» (core), vippayutta pi-1
    "maggavippayutta": "tâm không gắn liền với con đường",
    "taṇhāvippayuttamaggavippayutta": "tâm không gắn liền với khao khát và không gắn liền với con đường",
    "maggavippayuttataṇhāvippayutta": "tâm không gắn liền với con đường và không gắn liền với khao khát",
    "upapatti": "tâm tái sinh",                                      # upapatti (upapajjati «tái sinh» pi-2)
    "dutiye": "tâm thứ hai", "dutiye akusale": "tâm bất thiện thứ hai",
}
NOUN_OF = {                                              # <X>ssa / <X>ya uppādakkhaṇe / bhaṅgakkhaṇe
    "taṇhāya": "khao khát", "maggassa": "con đường", "aggamaggassa": "con đường tối thượng",
    "phalassa": "thành quả",                                         # phala «thành quả» (core)
    "maggassa ca phalassa ca": "con đường và thành quả",
    "aggamaggassa ca phalassa ca": "con đường tối thượng và thành quả",
    "tassa cittassa": "tâm ấy",                                      # yassa cittassa … tassa cittassa (8 «tâm nào … tâm ấy»)
}
VATTAMANA = "khi {c} đang diễn ra"                       # citte vattamāne (pi-5 «khi tâm … đang diễn ra»)


def _moment(mo, noun):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[mo], c=noun))   # vào khoảnh khắc sinh khởi của <noun>


def _who01(phrase):
    w = F.who(phrase)
    assert w.startswith("ở "), w
    return w[2:]


_PL = "(?:catuvokār|pañcavokār|asaññasatt|suddhāvās)"      # plane stems (+ aṃ acc / ā abl)
_LOC = "(?:arūp|pañcavokār|catuvokār|asaññasatt|apāy)"     # locative plane stems (+ e)
_NOUN_RE = "|".join(sorted(map(re.escape, NOUN_OF), key=len, reverse=True))
_KIND_RE = "taṇhāvippayuttamaggavippayutta|maggavippayuttataṇhāvippayutta|taṇhāvippayutta|maggavippayutta|upapatti"
# (regex, kind, function). kinds: R = sentence-initial relative (no «ở»), P = person group, N = person group that opens a
# new run (inner tesaṃ), J = «ye ca» group joined with «và», T = time / place group, V = pavatte (joins the next T)
HEAD_RULES = [
    (r"ye ca puthujjanā maggaṃ na paṭilabhissanti", "J", lambda g: E.E_YE["puthujjanā maggaṃ na paṭilabhissanti"]),
    (r"ye caññe maggaṃ paṭilabhissanti", "J", lambda g: YE_ANNE),
    (r"ye puthujjanā maggaṃ na paṭilabhissanti", "R", lambda g: E.E_YE["puthujjanā maggaṃ na paṭilabhissanti"]),
    (r"ye maggaṃ paṭilabhissanti", "R", lambda g: E.E_YE["maggaṃ paṭilabhissanti"]),
    (r"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti", "P", lambda g: ANANTARA),
    (r"tesaṃ (?P<p>upapajjantānaṃ|cavantānaṃ)", "N",
     lambda g: INNER_TESAM_PART.format(t=INNER_TESAM, p=F.PARTICIPLE[g["p"]][0])),
    (r"tesaṃ", "N", lambda g: INNER_TESAM),
    (r"(?P<a>an)?abhisametāvīnaṃ(?: (?P<p>upapajjantānaṃ|cavantānaṃ))?", "P",
     lambda g: ABHISAMETAVI[(g["a"] or "") + "abhisametāvīnaṃ"] + (f" {F.PARTICIPLE[g['p']][0]}" if g["p"] else "")),
    (rf"(?:(?:sabbesaṃ|itaresaṃ) )?(?:{_PL}(?:aṃ|ā) )*(?:upapajjantānaṃ|cavantānaṃ)", "P",
     lambda g: _who01(g[0].rstrip(", "))),
    (r"itaresaṃ (?:catuvokār|pañcavokār)ānaṃ(?: (?:catuvokār|pañcavokār)ānaṃ)*", "P", lambda g: _who01(g[0].rstrip(", "))),
    (r"suddhāvāsānaṃ|asaññasattānaṃ", "P", lambda g: _who01(g[0].rstrip(", "))),
    (r"āpāyikānaṃ", "P", lambda g: F.BEINGS_OF.format(p=PLANE_LOC["apāya"])),
    (r"aggamaggasamaṅgīnaṃ", "P", lambda g: AGGAMAGGA_GEN),
    (r"arahantānaṃ", "P", lambda g: ARAHANTANAM),
    (r"pacchimacittasamaṅgīnaṃ", "P", lambda g: C8.SAMANGI.format(c=C8.citta(last=True))),
    (r"nirodhasamāpannānaṃ", "P", lambda g: C8.NIRODHA_PERSONS),
    (r"sabbesaṃ", "P", lambda g: SABBESAM_ALONE),
    (r"itaresaṃ", "P", lambda g: F.HEAD["itaresaṃ"]),
    (r"pavatte", "V", lambda g: PAVATTE),
    (rf"(?P<k>{_KIND_RE})?cittassa(?P<v> \[[^\]]+\])? (?P<mo>uppāda|bhaṅga)kkhaṇe", "T",
     lambda g: _moment(g["mo"], CITTA_KIND[g["k"] or ""]) + _var_vi(g["v"])),
    (rf"(?P<n>{_NOUN_RE}) (?P<mo>uppāda|bhaṅga)kkhaṇe", "T", lambda g: _moment(g["mo"], NOUN_OF[g["n"]])),
    (r"(?P<d>dutiye(?: akusale)?) citte vattamāne", "T", lambda g: VATTAMANA.format(c=CITTA_KIND[g["d"]])),
    (r"taṇhāvippayuttacitte vattamāne", "T", lambda g: VATTAMANA.format(c=CITTA_KIND["taṇhāvippayutta"])),
    (rf"(?P<av>avasese )?(?P<pl>{_LOC}e(?: {_LOC}e)*)", "T", lambda g: _place(g)),
]
HEAD_RULES_C = [(re.compile(f"(?:{rx})" + r"(?P<comma>,)?(?: |$)"), k, f) for rx, k, f in HEAD_RULES]


def _place(g):
    planes = [PLANE_LOC[w[:-1] + "a"] for w in g["pl"].split()]
    p = F.LIST_SEP.join(planes)
    if g["av"]:
        p = AVASESA_LOC.format(p=p)
    return F.PLACE_IN.format(p=p)


def _groups(g):
    s = low(g)
    pos, out = 0, []
    while pos < len(s):
        for rx, kind, f in HEAD_RULES_C:
            mm = rx.match(s, pos)
            if mm and mm.end() > pos:
                if kind == "R" and pos != 0:
                    continue
                if mm["comma"]:
                    SLIPS.append(f"comma inside the head «…{mm[0].strip()} …»: groups are comma-joined anyway")
                out.append([kind, f(mm)])
                pos = mm.end()
                break
        else:
            vm = re.compile(r"(\[[^\]]+\]) ").match(s, pos)
            if vm and out:                      # a variant bracket between two groups stays after the first
                out[-1][1] += " " + variant(vm[1])
                pos = vm.end()
                continue
            raise ValueError(f"unparsed head {g!r} at {s[pos:]!r}")
    return out


def head_vi(g):
    """Pāli answer head (the words before the resumptive tesaṃ / tattha) -> Vietnamese head (capitalised)."""
    gs, merged, i = _groups(g), [], 0
    while i < len(gs):                          # pavatte + the next time phrase = one group
        kind, text = gs[i]
        if kind == "V":
            assert i + 1 < len(gs) and gs[i + 1][0] == "T", g
            merged.append(["T", PAVATTE_JOIN.format(a=text, b=gs[i + 1][1])])
            i += 2
            continue
        merged.append([kind, text])
        i += 1
    chunks = []                                 # [run kind, text]: P = «ở …» run, R / J = relative run, T = time / place
    for kind, text in merged:
        last = chunks[-1] if chunks else None
        if kind == "T":
            chunks.append(["T", text])
        elif kind == "J":
            if last and last[0] in ("P", "R"):
                last[1] += E.YE_CA_JOIN + text                  # «X và những người … nào …»
            else:
                chunks.append(["J", E.YE_CA_JOIN.lstrip() + text])  # after a time phrase: «…, và những người …»
        elif kind == "P" and last and last[0] == "P":
            last[1] += F.LIST_SEP + text                        # one «ở» over the run (2-01 WHO_HEAD / LIST_SEP)
        elif kind == "R":
            assert not chunks, g
            chunks.append(["R", text])
        else:                                                   # P opening a run, N (inner tesaṃ)
            chunks.append(["P", F.WHO_HEAD.format(g=text)])
    return cap(F.LIST_SEP.join(c[1] for c in chunks))


# ================================================================ FAMILY B sentences
MEM_B = r"(?:dukkha|samudaya|nirodha|magga)sacca"
VB = r"(?:na )?\S+"
B_NOT = re.compile(rf"(?P<g>.+) tesaṃ(?P<t> tattha)? (?P<x>{MEM_B}ṃ) (?P<v1>{VB}), no ca tesaṃ(?P<t2> tattha)? "
                   rf"(?P<y>{MEM_B}ṃ) (?P<v2>{VB})\.")
B_BOTH = re.compile(rf"(?P<g>.+) tesaṃ(?P<t> tattha)? (?P<x>{MEM_B})ñca (?P<v1>{VB}) (?P<y>{MEM_B})ñca (?P<v2>{VB})\.")
B_PLACE_NOT = re.compile(rf"(?P<g>.+?) tattha (?P<x>{MEM_B}ṃ) (?P<v1>{VB}), no ca tattha (?P<y>{MEM_B}ṃ) (?P<v2>{VB})\.")
B_PLACE_BOTH = re.compile(rf"(?P<g>.+?) tattha (?P<x>{MEM_B})ñca (?P<v1>{VB}) (?P<y>{MEM_B})ñca (?P<v2>{VB})\.")
PE_Q_RE = re.compile(r"\((?P<l>Ka|Kha)\) (?P<w>yassa vā pana yattha|yassa vā pana|yattha vā pana)"
                     r"(?: (?P<x>\S+) (?P<v1>[^\s…]+))?…pe…(?: (?P<v2>[^\s…]+))?\?")
PE_Q_TAIL = " {v} không"                                  # «… uppajjitthāti?» = «… đã sinh khởi không?»
FRAG_NOTE_RE = re.compile(r"(?P<w>Yattha) (?P<x>\S+) (?P<v>[^\s…]+)…pe…(?: (?P<n>\([^)]+\)))?\.")
NOTE = {    # editorial notes (yatthaka «phần về nơi chốn» 2-02 PARIPUNNA; yassaka «phần về người», sadisa «giống
    #           như» / «giống nhau», textual sabbattha «ở mọi chỗ»: all = 3-01; kātabbaṃ «nên được trình bày» 2-02)
    "(yatthakā sadisā sabbe)": "(tất cả các phần về nơi chốn đều giống nhau)",
    "(yatthakampi yassayatthakasadisaṃ kātabbaṃ)":
        "(phần về nơi chốn cũng nên được trình bày giống như phần về người và nơi chốn)",
}
EXACT_LINE = {
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        "(Phần về người và phần về người và nơi chốn cũng nên được trình bày chi tiết giống như vậy).",
    # vitthāretabba «nên được trình bày chi tiết» (pi-2 ^2 «cũng nên được trình bày chi tiết như vậy»)
    "(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).":
        ("(Phần về nơi chốn ở mọi chỗ cũng giống nhau. Sự khác biệt về câu chữ thì giống như phần về nơi chốn "
         "ở trên)."),
    # tanti «câu chữ (của văn bản)»; heṭṭhā «ở trên» (earlier in the text)
}


def b_member(w):
    return m(w + "ṃ" if w.endswith("sacca") else w)      # B_BOTH captures the stem before «ñca»


def b_pe_question(mm):
    kind = mm["w"].replace(" vā pana", "")
    s = F.VA_PANA + F.REL_VI[kind]
    if mm["x"]:
        s += f" mà {b_member(mm['x'])} {F.verb(*F.vparse(mm['v1']))}"
    s += C8.PE
    if mm["v2"]:
        s += PE_Q_TAIL.format(v=F.verb(*F.vparse(mm["v2"])))
    return f"{LABEL_VI[mm['l']]} {cap(s)}?"


def b_question(s, ctx):
    mm = F.B_Q_RE.fullmatch(s)
    plain = False
    if not mm:
        mm = F.B_Q_RE.fullmatch("(Ka) " + low(s)) if s[:1] in "Yy" else None
        plain = True
        if not mm:
            return None
    kind = mm["w1"].replace(" vā pana", "")
    kind2 = {"tassa": "yassa", "tattha": "yattha", "tassa tattha": "yassa yattha"}[mm["w2"]]
    assert kind == kind2, s
    kha = "vā pana" in mm["w1"]
    if not plain and kha != (mm["l"] == "Kha"):
        SLIPS.append(f"{ctx}: label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept")
    return F.b_q(kind, b_member(mm["x"]), F.vparse(mm["v1"], ctx), b_member(mm["y"]), F.vparse(mm["v2"], ctx),
                 kha=kha, label=None if plain else mm["l"])


def b_answer(s, ctx):
    for rx, both in ((B_NOT, False), (B_BOTH, True)):
        mm = rx.fullmatch(s)
        if mm:
            if not both:
                assert bool(mm["t"]) == bool(mm["t2"]), s
            res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
            f = F.b_both if both else F.b_not
            return f(res, head_vi(mm["g"]), b_member(mm["x"]), F.vparse(mm["v1"], ctx), b_member(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    for rx, both in ((B_PLACE_NOT, False), (B_PLACE_BOTH, True)):
        mm = rx.fullmatch(s)
        if mm:
            f = F.b_both if both else F.b_not
            return f("tattha", head_vi(mm["g"]), b_member(mm["x"]), F.vparse(mm["v1"], ctx), b_member(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return None


# ================================================================ exact sentences / lines
EXACT = {
    "Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ.": CATTARI,
    "Paṇṇattiuddesavāro.": F.PANNATTI_UDDESAVARO,                 # Mục nêu đề mục về sự định danh.
    "Paṇṇattiniddesavāro.": F.PANNATTI_NIDDESAVARO,               # Mục giải thích về sự định danh.
    "Uppādavāro.": cap(S.SECTION["uppādavāro"]) + ".",            # Mục về sự sinh khởi. (= 2-02 «Nirodhavāro.»)
    "Āmantā.": S.AMANTA,
    "Natthi.": F.NATTHI,
    "No.": F.NO,
}

# source slips (rendered as meant; each must apply the stated number of times)
SLIP_FIX = [
    ("Āmantā.…Pe….", "Āmantā…pe….", 3, "^6-5-22 / ^6-5-26: «Āmantā.…Pe….» (period before …pe…) = «Āmantā…pe….» "
                                       "(^6-5-20); rendered «Đúng vậy…»"),
    ("paṭilabhissānti", "paṭilabhissanti", 1, "^6-5-74: «paṭilabhissānti» = paṭilabhissanti (spelling)"),
    ("asaññattā cavantānaṃ", "asaññasattā cavantānaṃ", 1, "^6-5-76: «asaññattā» = asaññasattā (spelling)"),
    ("paṭilabhissanti ye [paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi] caññe",
     "paṭilabhissanti [paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi] ye caññe", 1,
     "^6-5-69: the variant bracket stands between «ye» and «caññe»; placed after the first group in Vietnamese"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, _n, why in SLIP_FIX:
        if a in s:
            SLIP_USED[why] = SLIP_USED.get(why, 0) + s.count(a)
            s = s.replace(a, b)
    return s


PE_Q_SPLIT = re.compile(r"\?\s?…[Pp]e…\s?")


def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    if s.startswith("…Pe… ") or s.startswith("…pe… "):        # «? …Pe… saccā nirodhasaccanti?…» (split at «? »)
        return C8.PE + " " + translate_sentence(s[len("…Pe… "):], ctx)
    if PE_Q_SPLIT.search(s):                                   # «Saccā dukkhaṃ?…Pe… saccā maggo?» / «…?…Pe….»
        first, rest = PE_Q_SPLIT.split(s, 1)
        t1 = translate_sentence(first + "?", ctx)
        if rest == ".":
            return f"{t1} {C8.PE}"                            # «… không? …»
        return f"{t1} {C8.PE} {translate_sentence(rest, ctx)}"
    mm = PE_Q_RE.fullmatch(s)
    if mm:
        return b_pe_question(mm)
    mm = FRAG_NOTE_RE.fullmatch(s)
    if mm:
        frag = E.pe_fragment(mm["w"].lower(), b_member(mm["x"]), F.vparse(mm["v"], ctx), "…pe….")
        return frag + (f" {NOTE[mm['n']]}." if mm["n"] else "")
    for f in (a_question, a_answer):
        r = f(s)
        if r:
            return r
    r = b_question(s, ctx)
    if r:
        return r
    r = b_answer(s, ctx)
    if r:
        return r
    if s.endswith("…pe…."):
        return E.pe_end(translate_sentence(s[:-len("…pe….")] + ".", ctx))
    mm = F.B_SHORT_RE.fullmatch(s)
    if mm:
        return F.b_short(F.VERB_BASE[low(mm["b"])], F.TENSE_OF[mm["t"]])
    raise ValueError(f"unmatched sentence: {s!r}")


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    t = fix_slips(t)
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
    ("Bốn sự thật – ", 2), ("Sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường", 2),
    ("khổ đau", 2), ("sự phát sinh", 2), ("sự chấm dứt", 2), ("con đường", 4), ("sự thật", 2),
    ("nơi thân", 1), ("trong tâm", 1), ("khao khát", 2), ("không gắn liền với", 1), ("cõi khổ", 2),
    ("thấu hiểu", 5), ("đang diễn ra", 5), ("ngay sau", 5),("các bậc A-la-hán", 5), ("tối thượng", 2),
    ("đạt được", 2), ("thành quả", 1), ("tâm bất thiện", 1), ("khoảnh khắc sinh khởi", 5),
    ("khoảnh khắc tan rã", 5), ("tái sinh", 2), ("những người phàm phu", 4), ("nên được trình bày chi tiết", 2),
    ("thuần túy", 5), ("thứ hai", 1), ("câu chữ", 4), ("sự khác biệt", 2),
    ("tất cả chúng sinh", 2), ("đời sống", 1),
]   # new (no pi-1..5 string): «tâm tái sinh» (upapatticitta), «những người đã / chưa thấu hiểu» (abhisametāvī), «ở trên» (heṭṭhā)


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (5-01): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT_LINE or p in EXACT:
            continue
        yield from F.split_sentences(fix_slips(p))


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese (the parser is deterministic; this guards the tables)."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    print(f"repeat check: {len(seen)} distinct sentences")
    return bad


def check_frames():
    """The imported frames still say what this chapter relies on."""
    assert variant("[avasesā khandhā khandhā (syā.) evamuparipi]") == \
        F.variant("[avasesā khandhā khandhā (syā.) evamuparipi]")
    assert C8.NIRODHA_ASANNA == "ở " + C8.NIRODHA_PERSONS + F.LIST_SEP + F.BEINGS["asaññasatta"]
    assert head_vi("Nirodhasamāpannānaṃ asaññasattānaṃ") == cap(C8.NIRODHA_ASANNA)
    assert head_vi("Itaresaṃ") == cap(F.who("Itaresaṃ"))
    assert head_vi("Asaññasatte") == cap(F.where("Asaññasatte"))
    assert E.E_YE["maggaṃ paṭilabhissanti"] == "những người nào sẽ đạt được con đường"


def main():
    S.check_cross_book()
    F.check_cross_book()
    check_cross_book()
    check_frames()
    SLIPS.clear(); F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", " ,", " ."):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, n, why in SLIP_FIX:
        assert used.get(why) == n, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in used:
        print("SLIP", why)
    for w in sorted(set(SLIPS)) + [f"{c} | {w}" for c, w in F.SLIPS]:
        print("NOTE", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
