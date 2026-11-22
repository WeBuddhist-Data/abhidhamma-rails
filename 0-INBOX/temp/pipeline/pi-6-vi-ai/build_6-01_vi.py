# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 6-01-sankharayamaka.md (Saṅkhārayamaka, first part:
paṇṇattivāra, pavattivāra uppādavāra, nirodhavāra (1)-(2)).

Frames come VERBATIM from the frame-setters:
    build_sample_vi (labels, section headings, «Đúng vậy.», but_not / both)
    build_2-01_vi   (family A question / answer frames; family B question frame, verbs, «no ca» verbs, short
                     answers, beings / planes (who, PLANE, BEINGS_OF …), the 7-01 person / place shape)
    build_2-02_vi   (pe_fragment, YE_CA_CAVANTA / YE_CA_JOIN)
    build_8_vi      (moments: AT, OF, MOMENT, citta(), SAMANGI, NIRODHA_PERSONS, OTHERS, FOR)
This module adds the Saṅkhāra members, the breathing / thought moments («vinā …»), the jhānas as persons and as
places, the «yassa cittassa anantarā … pacchimacittaṃ uppajjissati» time phrase and the editorial lines; 6-02
imports it:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    X = importlib.import_module("build_6-01_vi")
    X.m(word)            Saṅkhāra member (any case form) -> Vietnamese
    X.head(pali_head)    answer head (time / place / beings items) -> Vietnamese (lowercase start)
    X.translate_sentence(s), X.translate_line(line, ctx), X.heading(t), X.EXACT

Importing writes nothing; run  python -I -X utf8 -B build_6-01_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")     # pe_fragment, YE_CA_* (family B additions)
C8 = importlib.import_module("build_8_vi")       # moments, samaṅgī, nirodhasamāpanna (family D frame-setter)

NAME = "6-01-sankharayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
SLIPS = []

# ================================================================ members (MEMBER, m())
# pi-2 ^2-226: kāyasaṅkhāro / vacīsaṅkhāro / cittasaṅkhāro = sự tạo tác bằng thân / bằng lời nói / bằng tâm
KAYA_S, VACI_S, CITTA_S = "sự tạo tác bằng thân", "sự tạo tác bằng lời nói", "sự tạo tác bằng tâm"
MEMBER = {
    "kāyasaṅkhāro": KAYA_S, "kāyasaṅkhāraṃ": KAYA_S,
    "vacīsaṅkhāro": VACI_S, "vacīsaṅkhāraṃ": VACI_S,
    "cittasaṅkhāro": CITTA_S, "cittasaṅkhāraṃ": CITTA_S,
    "kāyo": "thân", "kāyaṃ": "thân",                     # kāya (pi-1 «thân»)
    "vacī": "lời nói", "vaciṃ": "lời nói",              # vacī (pi-5 «lời nói», vacībheda «sự phát ra lời nói»)
    "cittaṃ": "tâm",                                    # citta (pi-1 core)
    "saṅkhāro": "sự tạo tác",                           # saṅkhāro (pi-2 «sự tạo tác»)
    "saṅkhārā": F.MEMBER["saṅkhārā"],                   # saṅkhārā = các tạo tác (2-01, pi-5)
}


def m(w):
    return MEMBER[low(w)]


# ^6-6-1 (uddesa)
BREATH = "hơi thở vào và hơi thở ra"                    # assāsapassāsā (pi-5)
THOUGHT = "sự hướng tâm và sự duy trì tâm"              # vitakkavicārā (pi-1 / pi-5)
UDDESA_PI = ("Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, "
             "vitakkavicārā vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi "
             "cittasampayuttakā dhammā cittasaṅkhāro.")
UDDESA_VI = (f"Ba sự tạo tác – {KAYA_S}, {VACI_S}, {CITTA_S}. {cap(BREATH)} là {KAYA_S}, {THOUGHT} là {VACI_S}, "
             f"tri giác và cảm giác là {CITTA_S}. Ngoại trừ {THOUGHT}, tất cả các hiện tượng gắn liền với tâm đều "
             f"là {CITTA_S}.")
# saññā ca vedanā ca = tri giác và cảm giác (pi-5); cittasampayuttakā dhammā = các hiện tượng gắn liền với tâm (pi-1)

# ================================================================ family A sentences (frames of 2-01)
A_Q_RE = re.compile(r"\((?P<l>Ka|Kha)\) (?P<n1>na )?(?P<x>\S+) (?P<n2>na )?(?P<y>\S+?)\?")
A_BUT_RE = re.compile(r"(?P<s>\S+) na (?P<b>\S+), (?P<a>\S+)\.")                      # S na B, A.
A_NEITHER_RE = re.compile(r"(?P<a>\S+?)ñca (?P<b>\S+?)ñca ṭhapetvā avasesā na ceva (?P<c>\S+) na ca (?P<d>\S+)\.")
A_BOTH_RE = re.compile(r"(?P<s>\S+) (?P<a>\S+) ceva (?P<b>\S+) ca\.")                  # S A ceva B ca.
A_REST_RE = re.compile(r"Avasesā (?P<n>saṅkhārā)(?P<v> \[[^\]]+\])? na (?P<b>\S+)\.")   # Avasesā N [var] na B.


def _acc(w):
    return w[:-3] + "ṃ"          # Kāyañca -> Kāyaṃ ; Vaciñca -> Vaciṃ ; kāyasaṅkhārañca -> kāyasaṅkhāraṃ


def a_sentence(s):
    mm = A_Q_RE.fullmatch(s)
    if mm and low(mm["x"]) in MEMBER and low(F._strip_ti(mm["y"])) in MEMBER:
        assert bool(mm["n1"]) == bool(mm["n2"]), s
        return F.a_q(m(mm["x"]), m(F._strip_ti(mm["y"])), neg=bool(mm["n1"]), label=mm["l"])
    mm = A_BUT_RE.fullmatch(s)
    if mm:
        return F.a_but_not(m(mm["s"]), F.a_not(m(mm["b"])), F.a_is(m(mm["a"])))
    mm = A_NEITHER_RE.fullmatch(s)
    if mm:
        a, b = m(_acc(mm["a"] + "ñca")), m(_acc(mm["b"] + "ñca"))
        return F.a_neither(F.a_except(F.a_and(a, b)), m(mm["c"]), m(mm["d"]))
    mm = A_BOTH_RE.fullmatch(s)
    if mm:
        return F.a_both(m(mm["s"]), F.a_is(m(mm["a"])), F.a_is(m(mm["b"])))
    mm = A_REST_RE.fullmatch(s)
    if mm:
        return F.a_rest(m(mm["n"]), F.a_not(m(mm["b"])), F._var_vi(mm["v"]))
    return None


# ================================================================ answer heads (time / place / beings items)
ORD = {"paṭhama": "thứ nhất", "dutiya": "thứ hai", "tatiya": "thứ ba", "catuttha": "thứ tư"}
JHANA = "tầng thiền {o}"                           # paṭhamajjhāna … (pi-1 «tầng thiền thứ nhất»)
SAMAPANNA = "những người đang nhập {j}"            # Xjjhānaṃ samāpannānaṃ (pi-5 «người đang nhập tầng thiền …»)
MOMENT_OF = {                                       # genitive before -kkhaṇe -> Vietnamese «của …»
    "assāsapassāsānaṃ": BREATH,
    "vitakkavicārānaṃ": THOUGHT,
    "cittassa": C8.citta(),
    "avitakkaavicāracittassa": "tâm không có sự hướng tâm cũng không có sự duy trì tâm",   # pi-1 avitakkaavicāra
    "savitakkasavicārapacchimacittassa": "tâm cuối cùng có sự hướng tâm và sự duy trì tâm",  # pi-1 savitakkasavicāra
}
LAST_AVITAKKA = "tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm"
# avitakkaavicāraṃ pacchimacittaṃ / avitakkaavicārapacchimacitta- («cuối cùng» first: clearer than 8's
# «tâm <kind> cuối cùng» with a two-noun kind)
VINA = "{t} khi không có {w}"                       # vinā Wehi <G> Xkkhaṇe (vinā «without»)
VINA_W = {"assāsapassāsehi": BREATH, "vitakkavicārehi": THOUGHT}
ANANTARA = "vào tâm mà ngay sau đó {c} sẽ sinh khởi"
# yassa cittassa anantarā <K> pacchimacittaṃ uppajjissati (time phrase: at the citta right after which …)
ANANTARA_K = {"kāmāvacarānaṃ": f"{C8.citta(last=True)} của {F.BEINGS_OF.format(p=F.PLANE['kāmāvacara'])}",
              "avitakkaavicāraṃ": LAST_AVITAKKA}
VATTAMANE = "khi tâm thứ hai đang diễn ra"          # dutiye citte vattamāne (pi-5 «khi tâm … đang diễn ra»)
BHUMI = {"savitakkasavicārabhūmiyaṃ": "ở cấp độ có sự hướng tâm và sự duy trì tâm",          # pi-1 ^1-1000
         "avitakkaavicārabhūmiyaṃ": "ở cấp độ không có sự hướng tâm cũng không có sự duy trì tâm"}  # pi-1 ^1-1002
SABBESAM = "tất cả chúng sinh"                      # sabbesaṃ (alone; pi-2 «ở tất cả chúng sinh»)
TESAMYEVA = "chính những người ấy"                  # tesaṃyeva (7-01 «chính những hạng người ấy» without puggala)
PLACE_LIST = F.PLACE_IN                             # «trong {p}» (2-01), p = comma list

J_RE = r"(?:paṭhama|dutiya|tatiya|catuttha)jjhān"
LOCP = r"(?:kāmāvacare|rūpāvacare|arūpāvacare|asaññasatte)"
GENP = r"(?:kāmāvacarānaṃ|rūpāvacarānaṃ|arūpāvacarānaṃ|suddhāvāsānaṃ)"
ACCP = r"(?:rūpāvacaraṃ|arūpāvacaraṃ)"


def _jhana(w):
    mm = re.fullmatch(r"(paṭhama|dutiya|tatiya|catuttha)jjhān(?:aṃ|e)", w)
    return JHANA.format(o=ORD[mm.group(1)])


def _plane(w):
    case, stem = F._plane_case(w)
    assert case, w
    return F.PLANE[stem]


def _loc_item(w):
    return _jhana(w) if "jjhān" in w else _plane(w)


def _who(phrase):
    v = F.who(phrase)
    assert v.startswith("ở "), v
    return v[2:]


ITEMS = [   # (regex at the current position, kind, function of the match -> Vietnamese)
    (rf"yassa cittassa anantarā (?P<k>kāmāvacarānaṃ|avitakkaavicāraṃ) pacchimacittaṃ uppajjissati", "time",
     lambda g: ANANTARA.format(c=ANANTARA_K[g["k"]])),
    (rf"(?:vinā (?P<w>assāsapassāsehi|vitakkavicārehi) )?(?P<g>{'|'.join(MOMENT_OF)}) (?P<t>uppāda|bhaṅga)kkhaṇe", "time",
     lambda g: (VINA.format(t=_moment(g), w=VINA_W[g["w"]]) if g["w"] else _moment(g))),
    (r"dutiye citte vattamāne", "time", lambda g: VATTAMANE),
    (rf"(?P<j>(?:{J_RE}aṃ )+)samāpannānaṃ", "beings",
     lambda g: SAMAPANNA.format(j=F.LIST_SEP.join(_jhana(w) for w in g["j"].split()))),
    (rf"(?P<p>(?:{LOCP} )+)pacchimabhavikānaṃ", "beings", lambda g: _who(g[0])),
    (rf"(?P<p>(?:{LOCP} )+)pacchimacittasamaṅgīnaṃ", "beings",
     lambda g: C8.SAMANGI.format(c=C8.citta(last=True)) + " "
     + PLACE_LIST.format(p=F.LIST_SEP.join(_plane(w) for w in g["p"].split()))),
    (r"avitakkaavicārapacchimacittasamaṅgīnaṃ", "beings", lambda g: C8.SAMANGI.format(c=LAST_AVITAKKA)),
    (r"pacchimacittasamaṅgīnaṃ", "beings", lambda g: C8.SAMANGI.format(c=C8.citta(last=True))),
    (r"(?P<b>savitakkasavicārabhūmiyaṃ|avitakkaavicārabhūmiyaṃ)", "place", lambda g: BHUMI[g["b"]]),
    (r"nirodhasamāpannānaṃ", "beings", lambda g: C8.NIRODHA_PERSONS),
    (r"asaññasattānaṃ", "beings", lambda g: _who("asaññasattānaṃ")),
    (r"suddhāvāsaṃ upapajjantānaṃ", "beings", lambda g: _who(g[0])),
    (rf"ye ca (?P<p>(?:{ACCP} )*{ACCP}) upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ", "ye",
     lambda g: E.YE_CA_CAVANTA.format(p=F.LIST_SEP.join(_plane(w) for w in g["p"].split()))),
    (rf"(?P<l>(?:(?:{LOCP}|{J_RE}e) )*(?:{LOCP}|{J_RE}e))", "place",
     lambda g: PLACE_LIST.format(p=F.LIST_SEP.join(_loc_item(w) for w in g["l"].split()))),
    (rf"(?:itaresaṃ )?(?:{GENP} )*{GENP}", "beings", lambda g: _who(g[0])),
    (r"sabbesaṃ", "beings", lambda g: SABBESAM),
    (r"itaresaṃ", "beings", lambda g: C8.OTHERS),
    (r"tesaṃyeva", "beings", lambda g: TESAMYEVA),
]
ITEMS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ITEMS]


def _moment(g):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[g["t"]], c=MOMENT_OF[g["g"]]))


def head(phrase):
    """Pāli head of an answer (before «tesaṃ / tattha / tesaṃ tattha») -> Vietnamese, lowercase start.
    Items are joined with ", "; a run of beings items shares one «ở» (2-01 WHO_HEAD / LIST_SEP; 8 «Ở những người
    khác, vào khoảnh khắc …»); «ye ca …» joins the run with « và » (2-02)."""
    s = low(phrase)
    pieces = []                      # [kind, text or list]
    while s:
        for rx, kind, f in ITEMS:
            mm = rx.match(s)
            if mm:
                v = f(mm)
                if kind == "beings":
                    if pieces and pieces[-1][0] == "beings":
                        pieces[-1][1].append(v)
                    else:
                        pieces.append(["beings", [v]])
                elif kind == "ye":
                    assert pieces and pieces[-1][0] == "beings", phrase
                    pieces[-1][1][-1] += E.YE_CA_JOIN + v
                else:
                    pieces.append([kind, v])
                s = s[mm.end():].lstrip()
                break
        else:
            raise ValueError(f"unparsed head {phrase!r} at {s!r}")
    out = [C8.for_(F.LIST_SEP.join(v)) if k == "beings" else v for k, v in pieces]
    return ", ".join(out)


# ================================================================ family B sentences
V = r"(?:na )?\S+"
MEM = r"\S+saṅkhāro"
B_Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w1>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                    r"[Yy]attha vā pana|[Yy]assa|[Yy]attha) (?P<x>\S+) (?P<v1>(?:na )?\S+) "
                    r"(?P<w2>tassa tattha|tassa|tattha) (?P<y>\S+) (?P<v2>(?:na )?\S+)\?")
RES = r"tesaṃ tattha|tesaṃ|tattha"
B_NOT_RE = re.compile(rf"(?P<g>.+?) (?P<r>{RES}) (?P<x>{MEM}) (?P<v1>{V}), no ca (?P<r2>{RES}) (?P<y>{MEM}) "
                      rf"(?P<v2>{V})\.")
B_BOTH_RE = re.compile(rf"(?P<g>.+?) (?P<r>{RES}) (?P<x>{MEM}) ca (?P<v1>{V}) (?P<y>{MEM}) ca (?P<v2>{V})\.")
B_SHORT_RE = re.compile(r"(?P<b>Uppajj|Nirujjh)(?P<t>ati|ittha|issati)\.")
# fragments
FRAG_Q_RE = re.compile(r"\((?P<l>Ka|Kha)\) (?P<w>yassa vā pana yattha|yassa vā pana|yattha vā pana)(?: (?P<x>\S+))?"
                       r"…pe…(?P<p>[?.])")
FRAG_RE = re.compile(r"(?P<w>Yassa vā pana yattha|Yassa yattha|Yassa|Yattha) (?P<x>\S+) (?P<v>(?:na )?\S+?)…pe…\.?")
Q_PE_RE = re.compile(r"(?P<q>.+\?)…Pe…\.")       # «… nirujjhatīti?…Pe….»


def kind_of(w):
    return w.lower().replace(" vā pana", "")


def b_question(mm, ctx):
    kind = kind_of(mm["w1"])
    kind2 = {"tassa": "yassa", "tattha": "yattha", "tassa tattha": "yassa yattha"}[mm["w2"]]
    assert kind == kind2, mm[0]
    kha = "vā pana" in mm["w1"]
    if mm["l"] and kha != (mm["l"] == "Kha"):
        SLIPS.append((ctx, f"label ({mm['l']}) on a {'vā pana' if kha else 'non-vā pana'} question"))
    return F.b_q(kind, m(mm["x"]), F.vparse(mm["v1"], ctx), m(mm["y"]), F.vparse(mm["v2"], ctx), kha=kha,
                 label=mm["l"])


def frag_question(mm):
    """(Kha) yassa vā pana…pe…? = (b) Còn ở người nào…?  (8 «Còn ở người nào…?»)"""
    kind = kind_of(mm["w"])
    s = F.VA_PANA + F.REL_VI[kind]
    if mm["x"]:
        s += f" mà {m(mm['x'])}"
    return f"{LABEL_VI[mm['l']]} {cap(s)}{E.PE}" + ("?" if mm["p"] == "?" else "")


def frag(mm, ctx):
    """Yassa yattha X v…pe…. / Yattha X v…pe… / Yassa vā pana yattha X v…pe…. = «… mà X v…»"""
    w = mm["w"]
    kind = kind_of(w)
    if "vā pana" in w:
        s = E.PE_FRAG.format(rel=F.REL_VI[kind], a=m(mm["x"]), pa=F.verb(*F.vparse(mm["v"], ctx)))
        return cap(F.VA_PANA + s) + E.PE
    return E.pe_fragment(kind, m(mm["x"]), F.vparse(mm["v"], ctx), "…pe…")


# ================================================================ editorial lines, headings, closing lines
YASSAKA = "phần về người"                     # yassaka (the yassa section; 2-02 «phần về nơi chốn» = yatthaka)
YASSAYATTHAKA = "phần về người và nơi chốn"   # yassayatthaka
YATTHAKA = "phần về nơi chốn"                 # yatthaka (2-02 PARIPUNNA)
BOTH_SECTIONS = f"{YASSAKA} và {YASSAYATTHAKA}"
NIRODHA_CASE = f"trường hợp {C8.NIRODHA_PERSONS}"   # nirodhasamāpannānanti (the phrase «for those in cessation»)
EXACT = {
    UDDESA_PI: UDDESA_VI,
    "(Kha) paccanīkaṃ": f"{LABEL_VI['Kha']} {S.SECTION['paccanīkaṃ']}",          # plain line ^6-6-2, ^6-6-4
    "4 (Ṅa) paccanīkaokāso": f"4 {LABEL_VI['Ṅa']} {S.SECTION['paccanīkaokāso']}",  # plain line ^6-6-65 (as written)
    "Paṇṇattiuddesavāro.": F.PANNATTI_UDDESAVARO,
    "Paṇṇattivāro.": S.SECTION["Paṇṇattivāro"] + ".",
    "Paṇṇattiniddesavāro.": F.PANNATTI_NIDDESAVARO,
    "Uppādavāro.": cap(S.SECTION["uppādavāro"]) + ".",
    "Āmantā.": S.AMANTA,
    "Natthi.": F.NATTHI,
    "No.": F.NO,
    "(Yassakampi yassayatthakampi sadisaṃ.)": f"({cap(BOTH_SECTIONS)} đều giống nhau.)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        f"({cap(BOTH_SECTIONS)} đều nên được trình bày chi tiết giống nhau, trong {YASSAYATTHAKA} thì không có "
        f"{NIRODHA_CASE}.)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        f"({cap(BOTH_SECTIONS)} đều nên được trình bày chi tiết giống nhau, trong {YASSAYATTHAKA} thì không nên "
        f"đưa vào {NIRODHA_CASE}.)",
    "(Yatthakampi sabbattha ekasadisaṃ).": f"({cap(YATTHAKA)} cũng giống nhau ở mọi chỗ).",
    ("(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
     "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)"):
        (f"(Như các câu hỏi về quá khứ, cả {YASSAKA} lẫn {YASSAYATTHAKA}, cả {low(S.SECTION['anulomaṃ'])} lẫn "
         f"{low(S.SECTION['paccanīkaṃ'])}, đã được phân tích trong {S.SECTION['uppādavāro']}, trong "
         f"{S.SECTION['nirodhavāro']} cũng nên phân tích như vậy, không có sự khác biệt.)"),
}
SECTION_EXTRA = {
    "Suddhasaṅkhāravāro": S.VARO.format(x="các tạo tác thuần túy"),   # = Suddhakhandhavāro «Mục về các khối thuần túy»
    "Nirodhavāro": cap(S.SECTION["nirodhavāro"]),                      # heading «#### Nirodhavāro»
    "paccanīkaokāsā": S.SECTION["paccanīkaokāso"],                     # ^6-6-16-5-0 «paccanīkaokāsā» (slip, as meant)
}


def heading(t):
    if t in SECTION_EXTRA:
        return SECTION_EXTRA[t]
    mm = re.fullmatch(r"\((?P<l>[^)]+)\) (?P<w>\S+)", t)
    if mm and mm["w"] in SECTION_EXTRA:
        if mm["w"] == "paccanīkaokāsā":
            SLIPS.append(("heading ^6-6-16-5-0", "«paccanīkaokāsā» = paccanīkaokāso (spelling), rendered as meant"))
        return f"{LABEL_VI[mm['l']]} {SECTION_EXTRA[mm['w']]}"
    return F.heading(t)


# ================================================================ sentence / line translation
def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    r = a_sentence(s)
    if r:
        return r
    mm = Q_PE_RE.fullmatch(s)
    if mm:
        return translate_sentence(mm["q"], ctx) + E.PE
    mm = B_Q_RE.fullmatch(s)
    if mm:
        return b_question(mm, ctx)
    mm = FRAG_Q_RE.fullmatch(s)
    if mm:
        if mm["p"] == ".":
            SLIPS.append((ctx, f"«{s}»: question fragment ends with «.»; kept without «?»"))
        return frag_question(mm)
    mm = FRAG_RE.fullmatch(s)
    if mm:
        return frag(mm, ctx)
    for rx, both in ((B_NOT_RE, False), (B_BOTH_RE, True)):
        mm = rx.fullmatch(s)
        if mm:
            res = mm["r"]
            if not both:
                assert res == mm["r2"], s
            f = F.b_both if both else F.b_not
            return f(res, head(mm["g"]), m(mm["x"]), F.vparse(mm["v1"], ctx), m(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    mm = B_SHORT_RE.fullmatch(s)
    if mm:
        return F.b_short(F.VERB_BASE[low(mm["b"])], F.TENSE_OF[mm["t"]])
    raise ValueError(f"unmatched sentence: {s!r}")


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
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
    (KAYA_S, 2), (VACI_S, 2), (CITTA_S, 2), (KAYA_S, 5), (VACI_S, 5), (CITTA_S, 5),
    ("sự tạo tác", 2), ("các tạo tác", 5), (BREATH, 5), (THOUGHT, 1), (THOUGHT, 5), ("tri giác và cảm giác", 5),
    ("Các hiện tượng gắn liền với tâm", 1), ("thân", 1), ("lời nói", 5),
    ("tầng thiền thứ nhất", 1), ("tầng thiền thứ hai", 1), ("tầng thiền thứ ba", 1), ("tầng thiền thứ tư", 1),
    ("người đang nhập tầng thiền thứ nhất", 5), ("người đang nhập tầng thiền thứ tư", 5),
    ("vào khoảnh khắc sinh khởi", 5), ("vào khoảnh khắc tan rã", 5),
    ("không có sự hướng tâm cũng không có sự duy trì tâm", 1), ("có sự hướng tâm và sự duy trì tâm", 1),
    ("Ở cấp độ có sự hướng tâm và sự duy trì tâm", 1),
    ("Ở cấp độ không có sự hướng tâm cũng không có sự duy trì tâm", 1),
    ("ở tất cả chúng sinh", 2), ("đang diễn ra", 5), ("nên được trình bày chi tiết", 2), ("sự khác biệt", 5),
    ("thành tựu thiền chấm dứt", 5), ("người có được", 5), ("cõi dục lạc", 1), ("cõi hình sắc", 1),
    ("cõi không hình sắc", 1), ("Vô Tưởng", 2), ("tái sinh", 2), ("chết đi", 2), ("nhập Niết-bàn trọn vẹn", 5),
    ("thuần túy", 5), ("dị bản", 1), ("Đúng vậy.", 5), ("Không có.", 3), ("ngoại trừ", 2),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (6-01): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frame_setters():
    """Heads that 8 / 2-01 already settled come out byte-identical."""
    for p in ("Pacchimacittasamaṅgīnaṃ", "Itaresaṃ", "Nirodhasamāpannānaṃ asaññasattānaṃ",
              "Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ",
              "Cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ"):
        assert head(p) == C8.P_SUBJ[p], (p, head(p), C8.P_SUBJ[p])
    for p in ("Suddhāvāsaṃ upapajjantānaṃ asaññasattānaṃ", "Asaññasattānaṃ", "Rūpāvacarānaṃ arūpāvacarānaṃ"):
        assert head(p) == F.who(p), (p, head(p), F.who(p))
    assert head("Asaññasatte") == F.where("Asaññasatte")
    assert a_sentence("(Kha) saṅkhārā vacīsaṅkhāro?").startswith("(b) Các tạo tác có phải là")
    print("frame-setter checks: OK")


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
    """Identical Pāli sentence -> identical Vietnamese, within 6-01 and against 2-01 / 2-02."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for mod in (F, E):
        other = set(_sentences((S.PALI_DIR / mod.NAME).read_text(encoding="utf-8")))
        for s in other & set(seen):
            shared += 1
            t = mod.EXACT.get(s) if s in getattr(mod, "EXACT", {}) else mod.translate_sentence(s, "")
            if t != seen[s]:
                print(f"DIFFERS FROM {mod.NAME}:", s, "|", t, "|", seen[s])
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 2-01 / 2-02")
    return bad


# line-check problems expected because the Pāli itself has «?…pe…» (a question followed by «…pe…»)
EXPECTED_SEQ = "?…"


def main():
    S.check_cross_book()
    F.check_cross_book()
    E.check_cross_book()
    check_cross_book()
    check_frame_setters()
    SLIPS.clear(); F.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    pl = [x for x in pali.splitlines() if x.strip()]
    vl = [x for x in text.splitlines() if x.strip()]
    kept = []
    for p in probs:
        mm = re.search(r"line (\d+): bad sequence$", p)
        if mm:
            i = int(mm.group(1)) - 1
            rest = vl[i].replace(EXPECTED_SEQ, "")
            if "?…Pe…" in pl[i] and not any(b in rest for b in ("là là", ". .", "….", ".…", "?…", ",…", "  ", ":-",
                                                                  '"', "'", " ,", " .", "—")):
                print("EXPECTED (Pāli «?…pe…»):", p)
                continue
        kept.append(p)
    for bad in ("….", ".…", ",…", "  ", "là là", "—", ":-"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len(vl)} lines, {segs} segments")
    for w, c in {w: c for c, w in reversed(F.SLIPS + SLIPS)}.items():
        print("SLIP", c, "|", w)
    for p in kept[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not kept else f"{len(kept)} problems")
    sys.exit(1 if kept else 0)


if __name__ == "__main__":
    main()
