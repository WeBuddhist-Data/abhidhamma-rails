# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 3-01-ayatanayamaka.md (Āyatanayamaka, first part).

Frames: family A / B from build_2-01_vi (imported, used verbatim), with the twelve bases substituted
(pi-1 / pi-2 Vietnamese). Frames 2-01 did not cover (the «…pe…» shortenings of the cycle sections, the
attribute beings «sacakkhukānaṃ …», multi-plane place answers, the editorial notes) are settled here and listed
in notes-3-01.md; the later Āyatana chapters (3-02 … 3-06) import this module:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    A3 = importlib.import_module("build_3-01_vi")
    A3.BASE / A3.MEMBER / A3.m() / A3.ATTR / A3.who3() / A3.where3() / A3.translate_line() …

Importing writes nothing; run  python -I -X utf8 -B build_3-01_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")

NAME = "3-01-ayatanayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL

# ================================================================ members
AYATANA = "lĩnh vực nhận biết"                     # āyatana (core, pi-1)
AYATANA_PL = f"các {AYATANA}"                       # āyatanā (2-01: the Pāli number is kept)
# the twelve bases (pi-2 ^2-155 / ^2-168: «lĩnh vực mắt, lĩnh vực tai …»), in the order of this chapter
BASE = {
    "cakkhāyatana": "lĩnh vực mắt", "sotāyatana": "lĩnh vực tai", "ghānāyatana": "lĩnh vực mũi",
    "jivhāyatana": "lĩnh vực lưỡi", "kāyāyatana": "lĩnh vực thân", "rūpāyatana": "lĩnh vực hình sắc",
    "saddāyatana": "lĩnh vực âm thanh", "gandhāyatana": "lĩnh vực mùi", "rasāyatana": "lĩnh vực vị",
    "phoṭṭhabbāyatana": "lĩnh vực vật xúc chạm", "manāyatana": "lĩnh vực ý",
    "dhammāyatana": "lĩnh vực đối tượng của ý",
}
TWELVE = "Mười hai lĩnh vực nhận biết"              # Dvādasāyatanāni (pi-2)
# the bare words of the padasodhana questions (pi-2 termbase; rūpa = vật chất and dhamma = hiện tượng as in 2-01)
BARE = {
    ("cakkhu", "cakkhū", "cakkhuṃ"): "mắt", ("sotaṃ",): "tai", ("ghānaṃ",): "mũi", ("jivhā", "jivhaṃ"): "lưỡi",
    ("kāyo", "kāyaṃ"): "thân", ("rūpaṃ",): "vật chất", ("saddo", "saddaṃ"): "âm thanh",
    ("gandho", "gandhaṃ"): "mùi", ("raso", "rasaṃ"): "vị", ("phoṭṭhabbo", "phoṭṭhabbaṃ"): "vật xúc chạm",
    ("mano", "manaṃ"): "ý", ("dhammo", "dhammaṃ"): "hiện tượng",
    ("āyatanaṃ",): AYATANA, ("āyatanā",): AYATANA_PL,
}
MEMBER = {w: v for ks, v in BARE.items() for w in ks}
for _k, _v in BASE.items():
    MEMBER[_k + "ṃ"] = _v
SLIP_ALIAS = {"sotāyanaṃ": "sotāyatanaṃ"}          # ^6-3-13 «sotāyananti» (spelling slip)
SLIPS = F.SLIPS                                     # shared list (vparse also appends to it)


def m(w, ctx=""):
    w = low(w)
    if w in SLIP_ALIAS:
        SLIPS.append((ctx, f"«{w}» read as «{SLIP_ALIAS[w]}»"))
        w = SLIP_ALIAS[w]
    return MEMBER[w]


def strip_ti(w):
    """cakkhāyatananti -> cakkhāyatanaṃ; cakkhūti -> cakkhū; jivhāti -> jivhā (2-01 _strip_ti)."""
    if w.endswith("nti"):
        return w[:-3] + "ṃ"
    if w.endswith("ti"):
        return w[:-2]
    return w


def norm_ca(w):
    """Cakkhuñca -> cakkhuṃ; rūpañceva -> rūpaṃ."""
    if w.endswith("ñceva"):
        return w[:-5] + "ṃ"
    if w.endswith("ñca"):
        return w[:-3] + "ṃ"
    return w


# word-sense subjects of the niddesa (2-01 A_SENSE «X hiểu theo nghĩa Y»)
SENSE = {
    "Dibbacakkhu paññācakkhu": F.a_sense("mắt", "thiên nhãn, mắt trí tuệ"),          # dibbacakkhu «thiên nhãn» pi-5
    "Dibbasotaṃ taṇhāsotaṃ": F.a_sense("tai", "thiên nhĩ, dòng chảy của khao khát"),  # dibbasota «thiên nhĩ» pi-5
    "Sīlagandho samādhigandho paññāgandho":
        F.a_sense("mùi", "hương của giới hạnh, hương của định tâm, hương của trí tuệ"),   # sīla «giới hạnh» pi-2
    "Attharaso dhammaraso vimuttiraso":
        F.a_sense("vị", "vị của ý nghĩa, vị của Giáo Pháp, vị của sự giải thoát"),       # attha «ý nghĩa» pi-2
}
SENSE_RE = "|".join(re.escape(k) for k in SENSE)

# ================================================================ headings
HEAD3 = {
    "Suddhāyatanavāro": S.VARO.format(x=f"{AYATANA_PL} thuần túy"),
    "Suddhāyatanamūlacakkavāro": S.VARO.format(x=f"vòng luân chuyển dựa trên {AYATANA_PL} thuần túy"),
}


def heading(t):
    return HEAD3.get(t) or F.heading(t)


# ================================================================ editorial notes and closing lines
CYCLE = "vòng luân chuyển"                                       # cakka (sample SECTION «vòng luân chuyển»)
MULAKA = "(Phần dựa trên {x})"                                   # (Cakkhāyatanamūlakaṃ) (7-01 «(Phần dựa trên …)»)
SAMKHITTA = "Tóm lược"                                           # saṃkhittaṃ (pi-5 «(Tóm lược)»)
YASSAKA = "phần về người"                                        # yassaka (the yassa section)
YATTHAKA = "phần về nơi chốn"                                    # yatthaka (the yattha section)
SABBATTHA_NOTE = "ở mọi chỗ"                                     # sabbattha in the editorial notes
TABBA = "nên"                                                    # -tabbaṃ in the notes (2-02 «nên …», pi-2)
TIMES = [low(S.SECTION[k]).replace("mục về ", "") for k in (
    "Paccuppannavāro", "Atītavāro", "Anāgatavāro", "Paccuppannātītavāro", "Paccuppannānāgatavāro",
    "Atītānāgatavāro")]                                          # hiện tại … quá khứ và tương lai (sample)


def multi_variant(br):
    """[yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)] -> [dị bản (Sī.): yassakampi sadisaṃ; (Syā.): …]
    (pi-2 format «[dị bản (Sī.): lapilakaṃ; (Ka., Sī.): lampikaṃ]»)."""
    inner = br.strip()[1:-1]
    items = re.findall(r"\s*(?P<t>[^,()]+?) \((?P<s>[^)]+)\),?", inner)
    assert items and "".join(f"{t} ({s})" for t, s in items).replace(" ", "") == \
        inner.replace(",", "").replace(" ", ""), br
    parts = [f"({', '.join(F.SIGLA[x] for x in s.split())}): {t}" for t, s in items]
    return f"[{S.VAR} {'; '.join(parts)}]"


V_UPARI = "[uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)]"
V_YASSAKA = "[yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)]"
NOTE_UPARI = (f"(Ở nơi nào mà {BASE['ghānāyatana']} sinh khởi, thì ở nơi ấy {BASE['manāyatana']} và "
              f"{BASE['dhammāyatana']} đều giống nhau, không có gì khác biệt, nhưng {TABBA} hiểu rằng ở phần sau "
              f"có sự tóm lược các mục {multi_variant(V_UPARI)}.)")
NOTE_YATTHAKA = (f"({cap(YATTHAKA)} thì ở {', ở '.join(TIMES)}, {SABBATTHA_NOTE} đều giống nhau, chỉ {TABBA} thêm "
                 f"vào tên gọi {F.verb('sinh khởi', 'pres')}, {F.verb('sinh khởi', 'past')})")
NOTE_YASSAKA = f"({low(SAMKHITTA)}, giống như {YASSAKA} {multi_variant(V_YASSAKA)})"

EXACT_LINE = {
    ("Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, "
     "saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ."):
        f"{TWELVE} – {', '.join(BASE.values())}.",
    ("(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana "
     f"vārasaṅkhepo {V_UPARI} tīti jānitabbaṃ.)"): NOTE_UPARI,
}
EXACT_BODY = {                       # sentence body (final punctuation split off) -> Vietnamese body
    "(Cakkaṃ bandhitabbaṃ)": f"({cap(TABBA)} nối kết thành {CYCLE})",
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena)":
        f"({cap(TABBA)} nối kết thành {CYCLE} dựa trên từng thuật ngữ một, không để nhầm lẫn)",
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ)":
        f"(Khi nối kết thành {CYCLE}, {SABBATTHA_NOTE} {TABBA} trả lời: {S.AMANTA[:-1]})",
    "(Saṃkhittaṃ)": f"({SAMKHITTA})",
    ("(yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha "
     "sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ)"): NOTE_YATTHAKA,
    "Paṇṇattiuddesavāro": F.PANNATTI_UDDESAVARO[:-1],
    "Paṇṇattiniddesavāro": F.PANNATTI_NIDDESAVARO[:-1],
    "Āmantā": S.AMANTA[:-1],
    "Natthi": F.NATTHI[:-1],
}

# ================================================================ family B additions
ATTR = {                              # sacakkhukānaṃ … (beings with / without a base), new
    "sacakkhukānaṃ": "có mắt", "acakkhukānaṃ": "không có mắt",
    "sasotakānaṃ": "có tai", "asotakānaṃ": "không có tai",
    "saghānakānaṃ": "có mũi", "aghānakānaṃ": "không có mũi",
    "sarūpakānaṃ": "có vật chất", "arūpakānaṃ": "không có vật chất",
    "sacittakānaṃ": "có tâm", "acittakānaṃ": "không có tâm",
}
ATTR_JOIN = " và "                    # Sacakkhukānaṃ asotakānaṃ = có mắt và không có tai (one group, two attributes)
ATTR_GROUP = "{h} {p} {a}"            # những người đang tái sinh có mắt và không có tai


def who3(phrase):
    """2-01 who() plus the attribute groups («Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ»)."""
    w = [low(x) for x in phrase.split()]
    if not any(x in ATTR for x in w):
        return F.who(phrase)
    groups, i, n = [], 0, len(w)
    while i < n:
        j = i
        mod = None
        if w[j] in ("sabbesaṃ", "itaresaṃ"):
            mod, j = w[j], j + 1
        attrs = []
        while j < n and w[j] in ATTR:
            attrs.append(ATTR[w[j]]); j += 1
        assert j < n and w[j] in ("upapajjantānaṃ", "cavantānaṃ"), phrase
        vi = F.PARTICIPLE[w[j]][0]
        if attrs:
            groups.append(ATTR_GROUP.format(h=F.HEAD[mod], p=vi, a=ATTR_JOIN.join(attrs)))
        else:
            g = F.who(" ".join(w[i:j + 1]))
            head0 = F.WHO_HEAD.format(g="")
            assert g.startswith(head0), g
            groups.append(g[len(head0):])
        i = j + 1
    return F.WHO_HEAD.format(g=F.LIST_SEP.join(groups))


def where3(locs):
    """Asaññasatte arūpe / Rūpāvacare arūpāvacare … -> «trong cõi Vô Tưởng, cõi không hình sắc» (2-01 PLACE_IN and
    LIST_SEP); a single plane = F.where()."""
    ps = []
    for x in locs.split():
        case, stem = F._plane_case(low(x))
        assert case == "loc", locs
        ps.append(F.PLANE[stem])
    out = F.PLACE_IN.format(p=F.LIST_SEP.join(ps))
    if len(ps) == 1:
        assert out == F.where(locs)
    return out


def b_head(kind, x, v):
    """The first half of a shortened question: «ở nơi nào mà X đã sinh khởi» (Q_FRAME head)."""
    return f"{F.REL_VI[kind]} mà {x} {F.verb(*v)}"


# ================================================================ sentence translation
V = r"(?:na )?\S+"
B_Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w1>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                    r"[Yy]attha vā pana|[Yy]assa|[Yy]attha) (?P<x>\S+) (?P<v1>" + V + r") (?P<w2>tassa tattha|tassa|"
                    r"tattha) (?P<y>\S+) (?P<v2>" + V + ")")
B_HEAD_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w>[Yy]attha|[Yy]assa) (?P<x>\S+āyatanaṃ) (?P<v>" + V + ")")
RES = r"(?P<res>tesaṃ tattha|tesaṃ|tattha)"
B_NOT_RE = re.compile(r"(?P<g>.+?) " + RES + r" (?P<x>\S+āyatanaṃ) (?P<v1>" + V + r"), no ca (?P<res2>tesaṃ tattha|"
                      r"tesaṃ|tattha) (?P<y>\S+āyatanaṃ) (?P<v2>" + V + ")")
B_BOTH_RE = re.compile(r"(?P<g>.+?) " + RES + r" (?P<x>\S+āyatana)ñca (?P<v1>" + V + r") (?P<y>\S+āyatana)ñca "
                       r"(?P<v2>" + V + ")")
B_SHORT_RE = re.compile(r"(?P<b>Uppajj|Nirujjh)(?P<t>ati|ittha|issati)")
MULAKA_RE = re.compile(r"\((?P<b>\S+āyatana)mūlakaṃ\)")
YASSAKA_RE = re.compile(r"(?P<a>.+) \(saṃkhittaṃ yassakasadisaṃ " + re.escape(V_YASSAKA) + r" \)")
AV = r"(?:avaseso|avasesaṃ|avasesā)"


def _a_question(body, ctx):
    mm = re.fullmatch(r"(?:\((?P<l>Ka|Kha)\) )?(?P<b>.+)", body)
    lab, b = mm["l"], mm["b"]
    b2 = re.sub(r"(?<!\S)([Nn])āyatan", r"\1a āyatan", b)        # nāyatanā / nāyatanaṃ = na āyatanā / …
    t = b2.split()
    if len(t) == 4 and low(t[0]) == "na" and t[2] == "na":
        neg, x, y = True, t[1], t[3]
    elif len(t) == 2:
        neg, x, y = False, t[0], t[1]
    else:
        return None
    y = strip_ti(y)
    if low(x) not in MEMBER or (low(y) not in MEMBER and low(y) not in SLIP_ALIAS):
        return None
    out = F.a_q(m(x, ctx), m(y, ctx), neg=neg, label=lab)
    if not lab and b[:1].islower():
        out = low(out)
    return out


def _a_statement(body, ctx):
    g = None
    r = [
        (rf"(?P<s>{SENSE_RE}) (?P<a>\S+), na (?P<b>\S+)",
         lambda g: F.a_but_not(SENSE[g["s"]], F.a_is(m(g["a"])), F.a_not(m(g["b"])))),
        (rf"(?P<s>{SENSE_RE}) na (?P<b>\S+), (?P<a>\S+)",
         lambda g: F.a_but_not(SENSE[g["s"]], F.a_not(m(g["b"])), F.a_is(m(g["a"])))),
        (rf"(?P<e>\S+) ṭhapetvā avasesā (?P<n>āyatanā) na (?P<b>\S+), (?P<a>\S+)",
         lambda g: F.a_but_not(F.a_except_n(m(g["e"]), m(g["n"])), F.a_not(m(g["b"])), F.a_is(m(g["a"])))),
        (rf"(?P<e>\S+) ṭhapetvā {AV} (?P<a>\S+), na (?P<b>\S+)",
         lambda g: F.a_but_not(F.a_except(m(g["e"])), F.a_is(m(g["a"])), F.a_not(m(g["b"])))),
        (rf"(?P<e>\S+) ṭhapetvā {AV} na (?P<b>\S+), (?P<a>\S+)",
         lambda g: F.a_but_not(F.a_except(m(g["e"])), F.a_not(m(g["b"])), F.a_is(m(g["a"])))),
        (rf"(?P<a>\S+ñca) (?P<b>\S+ñca) ṭhapetvā {AV}(?P<v> \[[^\]]+\])? na ceva (?P<c>\S+) na ca (?P<d>\S+)",
         lambda g: F.a_neither(F.a_except(F.a_and(m(norm_ca(g["a"])), m(norm_ca(g["b"]))))
                               + (" " + F.variant(g["v"].strip()) if g["v"] else ""), m(g["c"]), m(g["d"]))),
        (r"(?P<s>\S+) (?P<a>\S+?)(?P<k>ñceva| ceva) (?P<b>\S+ñca)",
         lambda g: F.a_both(m(g["s"]), F.a_is(m(g["a"] + ("ṃ" if g["k"] == "ñceva" else ""))),
                            F.a_is(m(norm_ca(g["b"]))))),
        (r"[Aa]vasesā (?P<n>āyatanā) na (?P<b>\S+)",
         lambda g: F.a_rest(m(g["n"]), F.a_not(m(g["b"])))),
    ]
    for p, f in r:
        g = re.fullmatch(p, body)
        if g:
            out = f(g)
            return low(out) if body[:1].islower() else out
    return None


def _fragment(body, ctx):
    """Pieces of the «…pe…» lines that are not whole sentences."""
    mm = re.fullmatch(r"(?P<e>\S+) ṭhapetvā", body)
    if mm:                                                            # Sotaṃ ṭhapetvā…
        out = F.A_EXCEPT.split(",")[0].format(x=m(mm["e"]))          # «ngoại trừ X»
    elif re.fullmatch(r"na ca (?P<d>\S+)", body):                     # …na ca āyatanā. (A_NEITHER tail)
        out = "cũng " + F.a_not(m(body.split()[-1]))
    elif re.fullmatch(r"na (?P<b>\S+)", body):                        # …na cakkhāyatanaṃ (A_REST tail)
        out = F.a_not(m(body.split()[-1]))
    elif low(body) in MEMBER:                                         # ghānaṃ… jivhā… (a run of subjects)
        out = m(body)
    else:
        mm = B_HEAD_RE.fullmatch(body)
        if not mm:
            return None
        kind = low(mm["w"])
        out = b_head(kind, m(mm["x"]), F.vparse(mm["v"], ctx))
        out = f"{LABEL[mm['l']]} {cap(out)}" if mm["l"] else cap(out) if body[0].isupper() else out
        return out
    return cap(out) if body[:1].isupper() else out


def _strip_end(s):
    return s[:-1] if s and s[-1] in ".?" else s


def tr(body, punct, ctx, pe=False):
    """One Pāli sentence body (final punctuation split off) -> Vietnamese, + the Pāli punctuation."""
    if body == "":
        return punct
    if body + punct in F.EXACT and punct:
        return F.EXACT[body + punct]
    if body in EXACT_BODY:
        return EXACT_BODY[body] + punct
    mm = MULAKA_RE.fullmatch(body)
    if mm:
        return MULAKA.format(x=BASE[low(mm["b"])]) + punct
    mm = YASSAKA_RE.fullmatch(body)
    if mm:
        return _strip_end(tr(mm["a"], ".", ctx)) + " " + NOTE_YASSAKA + punct
    mm = B_Q_RE.fullmatch(body)
    if mm:
        kind = low(mm["w1"]).replace(" vā pana", "")
        assert kind == {"tassa": "yassa", "tattha": "yattha", "tassa tattha": "yassa yattha"}[mm["w2"]], body
        kha = "vā pana" in mm["w1"]
        if mm["l"] and kha != (mm["l"] == "Kha"):
            SLIPS.append((ctx, f"label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept"))
        out = F.b_q(kind, m(mm["x"]), F.vparse(mm["v1"], ctx), m(mm["y"]), F.vparse(mm["v2"], ctx), kha=kha,
                    label=mm["l"])
        return _strip_end(out) + punct
    for rx, both in ((B_NOT_RE, False), (B_BOTH_RE, True)):
        mm = rx.fullmatch(body)
        if mm:
            res = mm["res"]
            if not both:
                assert res == mm["res2"], body
            head = where3(mm["g"]) if res == "tattha" else who3(mm["g"])
            x = m(mm["x"] + ("ṃ" if both else ""))
            y = m(mm["y"] + ("ṃ" if both else ""))
            f = F.b_both if both else F.b_not
            return _strip_end(f(res, head, x, F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx))) + punct
    mm = B_SHORT_RE.fullmatch(body)
    if mm and punct == ".":
        return F.b_short(F.VERB_BASE[low(mm["b"])], F.TENSE_OF[mm["t"]])
    out = _a_question(body, ctx)
    if out:
        return _strip_end(out) + punct
    out = _a_statement(body, ctx)
    if out:
        return _strip_end(out) + punct
    if pe:
        out = _fragment(body, ctx)
        if out:
            return out + punct
    raise ValueError(f"unmatched sentence: {body!r}{punct} ({ctx})")


def tr_sentences(text, ctx, pe=False):
    out = []
    for s in F.split_sentences(text):
        s = s.strip()
        if s and s[-1] in ".?":
            out.append(tr(s[:-1], s[-1], ctx, pe))
        else:
            out.append(tr(s, "", ctx, pe))
    return " ".join(x for x in out if x)


PE_SPLIT = re.compile(r"…(?:pe|Pe)…|…")
PAST_RUN_RE = re.compile(r"Yassa (?P<xs>.+?) (?P<v1>uppajjittha) tassa (?P<ys>.+?) (?P<v2>uppajjitthāti)\? Āmantā\.")


def _run(xs):
    """ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ -> «lĩnh vực mũi… lĩnh vực hình sắc… lĩnh vực ý»."""
    return "… ".join(m(x.strip()) for x in PE_SPLIT.split(xs))


def tr_pe(text, ctx):
    """A line with «…pe…» / «…»: each piece between the ellipses is translated in place; the ellipsis stays at the
    same spot. A period before or after the ellipsis gives way to it (7-04 «Đúng vậy…»); «?…» is written «? …»."""
    mm = PAST_RUN_RE.fullmatch(text)
    if mm:                                                           # ^6-3-38 / ^6-3-39 (one question, a run)
        q = F.b_q("yassa", _run(mm["xs"]), F.vparse(mm["v1"], ctx), _run(mm["ys"]), F.vparse(mm["v2"], ctx),
                  label=None)
        return f"{q} {S.AMANTA}"
    pieces = []
    for chunk in PE_SPLIT.split(text):
        lead = chunk[:len(chunk) - len(chunk.lstrip())]
        trail = chunk[len(chunk.rstrip()):]
        core = chunk.strip()
        pieces.append(lead + (tr_sentences(core, ctx, pe=True) if core else "") + trail)
    out = "…".join(pieces)
    prev = None
    while prev != out:
        prev = out
        out = out.replace(".…", "…").replace("….", "…").replace("?…", "? …")
    return out


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        if t.startswith("Dvādas"):
            SLIPS.append((ctx, "uddesa list: no comma after «sotāyatanaṃ»; comma written"))
        if "tīti jānitabbaṃ" in t:
            SLIPS.append((ctx, "«vārasaṅkhepo … tīti jānitabbaṃ»: «tīti» read as «(hotī)ti» (nên hiểu rằng …)"))
        return EXACT_LINE[t] + sid
    if "uppajjittharūpāyatanañca" in t:
        SLIPS.append((ctx, "«uppajjittharūpāyatanañca»: missing space, read as «uppajjittha rūpāyatanañca»"))
        t = t.replace("uppajjittharūpāyatanañca", "uppajjittha rūpāyatanañca")
    if "…" in t:
        return tr_pe(t, ctx) + sid
    return tr_sentences(t, ctx) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for ln in src.splitlines():
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ cross-book asserts
CROSS_BOOK = [
    ("Mười hai lĩnh vực nhận biết – lĩnh vực mắt, lĩnh vực tai, lĩnh vực mũi, lĩnh vực lưỡi, lĩnh vực thân", 2),
    ("lĩnh vực hình sắc, lĩnh vực âm thanh, lĩnh vực mùi, lĩnh vực vị, lĩnh vực vật xúc chạm", 2),
    ("lĩnh vực ý, lĩnh vực đối tượng của ý", 2), ("lĩnh vực nhận biết", 1), ("các lĩnh vực nhận biết", 1),
    ("mắt", 2), ("tai", 2), ("mũi", 2), ("lưỡi", 2), ("thân", 2), ("vật chất", 1), ("âm thanh", 2), ("mùi", 2),
    ("vị", 2), ("vật xúc chạm", 2), ("ý", 2), ("hiện tượng", 1), ("tâm", 1),
    ("thiên nhãn", 5), ("thiên nhĩ", 5), ("khao khát", 2), ("giới hạnh", 2), ("định tâm", 2), ("trí tuệ", 2),
    ("ý nghĩa", 2), ("Giáo Pháp", 1), ("sự giải thoát", 1), ("(Tóm lược)", 5), ("vòng luân chuyển", 5),
    ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("cõi không hình sắc", 1), ("thuần túy", 5), ("Phần dựa trên", 2),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (3-01): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_extra(text):
    """Chapter-level checks beyond S.check_lines: no Pāli left, every ellipsis rule kept."""
    probs = []
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("….", ".…", "?…", "  ", "là là", "āyatan", "uppajj", "tesaṃ", "tattha", " ca ", ",,"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    check_cross_book()
    del SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + check_extra(text)
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
