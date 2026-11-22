# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 4-dhatuyamaka.md (the whole Dhātuyamaka).

Frames: family A / B from build_2-01_vi, the Āyatana frames of build_3-01_vi (sense subjects, «…pe…» lines,
attribute beings who3(), editorial notes «(Nên nối kết thành vòng luân chuyển)» …), family E from build_2-02_vi
and the «phần <yamaka>» wording of build_6-02_vi, all imported and used verbatim, with the eighteen elements
(pi-2 Dhātuvibhaṅga ^2-183) substituted. Items none of them covered are listed in notes-4.md.

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    D4 = importlib.import_module("build_4_vi")

Importing writes nothing; run  python -I -X utf8 -B build_4_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")       # families A / B
E = importlib.import_module("build_2-02_vi")       # family E (pariññāvāra)
A3 = importlib.import_module("build_3-01_vi")      # Āyatana frames (sense subjects, notes, who3, «…pe…» rules)
X62 = importlib.import_module("build_6-02_vi")     # part(): «phần <yamaka title>» inside the notes

NAME = "4-dhatuyamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []

# ================================================================ members
DHATU = "yếu tố"                                    # dhātu (core, pi-1)
DHATU_PL = f"các {DHATU}"                           # dhātū (the Pāli number is kept, as 2-01 / 3-01)
# the eighteen elements (pi-2 ^2-183 «Mười tám yếu tố – yếu tố mắt, …»), in the order of this chapter's uddesa
ELEMENT = {
    "cakkhudhātu": "yếu tố mắt", "sotadhātu": "yếu tố tai", "ghānadhātu": "yếu tố mũi",
    "jivhādhātu": "yếu tố lưỡi", "kāyadhātu": "yếu tố thân", "rūpadhātu": "yếu tố hình sắc",
    "saddadhātu": "yếu tố âm thanh", "gandhadhātu": "yếu tố mùi", "rasadhātu": "yếu tố vị",
    "phoṭṭhabbadhātu": "yếu tố vật xúc chạm", "cakkhuviññāṇadhātu": "yếu tố thức qua mắt",
    "sotaviññāṇadhātu": "yếu tố thức qua tai", "ghānaviññāṇadhātu": "yếu tố thức qua mũi",
    "jivhāviññāṇadhātu": "yếu tố thức qua lưỡi", "kāyaviññāṇadhātu": "yếu tố thức qua thân",
    "manodhātu": "yếu tố ý", "manoviññāṇadhātu": "yếu tố ý thức", "dhammadhātu": "yếu tố đối tượng của ý",
}
EIGHTEEN = "Mười tám yếu tố"                        # Aṭṭhārasa dhātuyo (pi-2 ^2-183)
# bare words: the 3-01 BARE words (mắt, tai … ý, hiện tượng), without its āyatana entries, plus the five
# consciousnesses and manoviññāṇa (pi-1 «thức qua mắt», pi-2 «yếu tố ý thức»)
MEMBER = {w: v for ks, v in A3.BARE.items() for w in ks if not w.startswith("āyatan")}
VINNANA = {"cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân"}
for _k, _v in VINNANA.items():
    MEMBER[f"{_k}viññāṇaṃ"] = f"thức qua {_v}"
MEMBER["manoviññāṇaṃ"] = "ý thức"
for _k, _v in ELEMENT.items():
    MEMBER[_k] = MEMBER[_k + "ṃ"] = _v               # nominative / accusative (cakkhudhātuṃ ṭhapetvā, parijānāti)
MEMBER.update({"dhātu": DHATU, "dhātuṃ": DHATU, "dhātū": DHATU_PL})
assert all(MEMBER[w] == A3.MEMBER[w] for w in MEMBER if w in A3.MEMBER)   # same bare words as 3-01


def m(w):
    return MEMBER[low(w)]


def strip_ti(w):
    """cakkhudhātūti -> cakkhudhātu; cakkhūti -> cakkhu; dhātūti -> dhātu (dhātu + iti, singular as in the uddesa
    «(Ka) cakkhu dhātu?»); sotanti -> sotaṃ; kāyoti -> kāyo."""
    if w.endswith("nti"):
        return w[:-3] + "ṃ"
    if w.endswith("ūti"):
        return w[:-3] + "u"
    if w.endswith("ti"):
        return w[:-2]
    return w


norm_ca = A3.norm_ca                                # Cakkhuñca -> cakkhuṃ; cakkhudhātuñca -> cakkhudhātuṃ

# ================================================================ headings
HEAD4 = {
    "Suddhadhātuvāro": S.VARO.format(x=f"{DHATU_PL} thuần túy"),                       # = Suddhāyatanavāro
    "Suddhadhātumūlacakkavāro": S.VARO.format(x=f"vòng luân chuyển dựa trên {DHATU_PL} thuần túy"),
}


def heading(t):
    return HEAD4.get(t) or F.heading(t)


# ================================================================ editorial notes (new; built from 3-01 / 6-02 pieces)
TABBA, CYCLE = A3.TABBA, A3.CYCLE                   # «nên», «vòng luân chuyển» (3-01)
BIND = f"nối kết thành {CYCLE}"                     # cakkaṃ bandhati (3-01 «(Nên nối kết thành vòng luân chuyển)»)
part = X62.part                                     # <X>yamake = «phần các cặp câu hỏi về …» (6-02)
PANNATTI = low(S.SECTION["Paṇṇattivāro"]).replace("mục về ", "")    # paṇṇatti = sự định danh
AMANTA_BARE = S.AMANTA[:-1]                         # «Đúng vậy» inside a note (3-01)
ANSWERED = "đều được trả lời: " + AMANTA_BARE       # … āmantā (in a note)
UBHATO = "cả hai phía"                              # ubhato (both questions of the pair)
SADISA = "{x} giống như {y}"                        # Xsadiso / Xsadisā
SAMKHITTA = low(A3.SAMKHITTA)                       # saṃkhittaṃ = tóm lược (pi-5; 3-01 lowercase in a note)
ELLIPTIC_Q = "{x} thì sao"                          # a bare «X?» / «Na X?» cut down by …pe… (new)
NEG_HEAD = "những gì không phải là {x}"            # «Na X…» = the head of the A_NEG_Q frame (2-01)
SAMSANDITABBA = f"{TABBA} đối chiếu với các phần các cặp câu hỏi khác"  # aññehi yamakehi saṃsanditabbaṃ
VITTHARA = "nên được trình bày chi tiết"           # vitthāretabbā (3-05, pi-2)
VIBHAJ = "nên được phân tích"                       # vibhajitabbaṃ (6-02)

V46 = "[dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ]"
V46_VI = f"[{S.VAR} (Sī., Ka.): dhātu; {SAMSANDITABBA}]"

EXACT_LINE = {
    ("Aṭṭhārasa dhātuyo – cakkhudhātu, sotadhātu, ghānadhātu, jivhādhātu, kāyadhātu, rūpadhātu, saddadhātu, "
     "gandhadhātu, rasadhātu, phoṭṭhabbadhātu, cakkhuviññāṇadhātu, sotaviññāṇadhātu, ghānaviññāṇadhātu, "
     "jivhāviññāṇadhātu, kāyaviññāṇadhātu, manodhātu, manoviññāṇadhātu, dhammadhātu."):
        f"{EIGHTEEN} – {', '.join(ELEMENT.values())}.",
    f"(Kha) dhātū {V46} sotadhātu?…Pe…":
        F.a_q(f"{DHATU_PL} {V46_VI}", ELEMENT["sotadhātu"], label="Kha") + " " + A3.F.C7.PE,
    "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)":
        f"(Như {CYCLE} đã được nối kết trong {part('Āyatanayamakaṃ')}, ở đây cũng {TABBA} {BIND} như vậy.)",
    "(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti. Cakkaṃ bandhitabbaṃ).":
        (f"(Như {PANNATTI} trong {part('Āyatanayamakaṃ')}, {PANNATTI} trong {part('Dhātuyamakaṃ')} cũng như vậy. "
         f"{cap(TABBA)} {BIND})."),
    "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)":
        (f"(Như {PANNATTI} của {part('Āyatanayamakaṃ')}, {PANNATTI} của {part('Dhātuyamakaṃ')} cũng {VITTHARA} "
         f"như vậy)"),
    "(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).":
        (f"(Như {part('Āyatanayamakaṃ')} đã được phân tích, {part('Dhātuyamakaṃ')} cũng {VIBHAJ} như vậy, "
         f"nên được trình bày giống nhau)."),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
}
EXACT_BODY = dict(A3.EXACT_BODY, **{                # sentence body (final punctuation split off) -> Vietnamese
    "(Jivhāpi ghānadhātusadisā)": f"({cap(MEMBER['jivhā'])} cũng {SADISA.format(x='', y=ELEMENT['ghānadhātu'])[1:]})",
    "(Saddo ghānasadiso)": f"({cap(SADISA.format(x=MEMBER['saddo'], y=MEMBER['ghānaṃ']))})",
    "(Phoṭṭhabbo ghānasadiso)": f"({cap(SADISA.format(x=MEMBER['phoṭṭhabbo'], y=MEMBER['ghānaṃ']))})",
    "(saṃkhittaṃ [yaṃ saṃkhittaṃ (syā.)], ubhato āmantā)":
        f"({SAMKHITTA} {F.variant('[yaṃ saṃkhittaṃ (syā.)]')}, {UBHATO} {ANSWERED})",
    "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi)":
        f"({cap(TABBA)} {BIND}, tất cả {ANSWERED}, cả ở hai phía lẫn ở các phần còn lại)",
    "(dhātuyamakaṃ paripuṇṇaṃ peyyālena)": f"({part('Dhātuyamakaṃ')} là đầy đủ, với các chỗ lược bớt)",
    "Dhātuyamakaṃ niṭṭhitaṃ": S.yamaka_end("Dhātuyamakaṃ")[:-1],
})
SENSE = A3.SENSE                                    # Dibbacakkhu paññācakkhu … (3-01)
SENSE_RE = A3.SENSE_RE

# source slips rendered as meant (spelling only); each must apply exactly once
SLIP_FIX = [
    ("jivha ṭhapetvā…pe…", "jivhaṃ ṭhapetvā…pe…", "^6-4-15: «jivha ṭhapetvā» = jivhaṃ (spelling)"),
    ("Cakkhu ca dhātuñca ṭhapetvā", "Cakkhuñca dhātuñca ṭhapetvā",
     "^6-4-17: «Cakkhu ca dhātuñca» = Cakkhuñca (spelling)"),
]
SLIP_USED = {}
NOTED = [   # translated as written; reported
    "^6-4-17: «Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu.» (the parallel has «na cakkhu, dhātu»): as written, "
    "«Ngoại trừ mắt, các yếu tố còn lại không phải là yếu tố mắt.»",
    "^6-4-17: «na ca dhātu» (twice; ^6-4-15 has «na ca dhātū»): as written, singular «yếu tố»",
    "^6-4-15 … ^6-4-17: «avasesā dhātū na cakkhu, dhātu» (singular «dhātu» after a plural subject): «là yếu tố»",
    "^6-4-4: the variant bracket «[dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ]» carries an editorial remark",
    "^6-4-17: «(Yathā āyatanayamakassa … vitthāretabbā)» has no final period; none written",
]

# ================================================================ sentence translation
V = r"(?:na )?\S+"
RES = r"(?P<res>tesaṃ tattha|tesaṃ|tattha)"
B_NOT_RE = re.compile(r"(?P<g>.+?) " + RES + r" (?P<x>\S+dhātu) (?P<v1>" + V + r"), no ca (?P<res2>tesaṃ tattha|"
                      r"tesaṃ|tattha) (?P<y>\S+dhātu) (?P<v2>" + V + ")")
B_BOTH_RE = re.compile(r"(?P<g>.+?) " + RES + r" (?P<x>\S+dhātu) ca (?P<v1>" + V + r") (?P<y>\S+dhātu) ca "
                       r"(?P<v2>" + V + ")")
E_Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?[Yy]o(?P<vp> vā pana)? (?P<x>\S+) (?P<v1>{E.E_V}) so (?P<y>\S+) "
                    rf"(?P<v2>{E.E_V})")
AV = r"(?:avaseso|avasesaṃ|avasesā)"
VAR = r"(?P<v> \[[^\]]+\])?"


def _var(g):
    return " " + F.variant(g["v"].strip()) if g["v"] else ""


def _a_question(body, ctx):
    mm = re.fullmatch(r"(?:\((?P<l>Ka|Kha)\) )?(?P<b>.+)", body)
    lab, b = mm["l"], mm["b"]
    t = b.split()
    if len(t) == 4 and low(t[0]) == "na" and t[2] == "na":
        neg, x, y = True, t[1], t[3]
    elif len(t) == 2:
        neg, x, y = False, t[0], t[1]
    else:
        return None
    y = strip_ti(y)
    if low(x) not in MEMBER or low(y) not in MEMBER:
        return None
    out = F.a_q(m(x), m(y), neg=neg, label=lab)
    if not lab and b[:1].islower():
        out = low(out)
    return out


A_STATEMENTS = [
    (rf"(?P<s>{SENSE_RE}) (?P<a>\S+), na (?P<b>\S+)",
     lambda g: F.a_but_not(SENSE[g["s"]], F.a_is(m(g["a"])), F.a_not(m(g["b"])))),
    (rf"(?P<s>{SENSE_RE}) na (?P<b>\S+), (?P<a>\S+)",
     lambda g: F.a_but_not(SENSE[g["s"]], F.a_not(m(g["b"])), F.a_is(m(g["a"])))),
    (rf"(?P<e>\S+) ṭhapetvā avasesā (?P<n>dhātū) na (?P<b>\S+), (?P<a>\S+)",
     lambda g: F.a_but_not(F.a_except_n(m(g["e"]), m(g["n"])), F.a_not(m(g["b"])), F.a_is(m(g["a"])))),
    (rf"(?P<e>\S+) ṭhapetvā avasesā (?P<n>dhātū) na (?P<b>\S+)",      # ^6-4-17 (as written, no «, dhātu»)
     lambda g: cap(F.a_except_n(m(g["e"]), m(g["n"]))) + " " + F.a_not(m(g["b"])) + "."),
    (rf"(?P<e>\S+) ṭhapetvā {AV} (?P<a>\S+){VAR}, na (?P<b>\S+)",
     lambda g: F.a_but_not(F.a_except(m(g["e"])), F.a_is(m(g["a"])) + _var(g), F.a_not(m(g["b"])))),
    (rf"(?P<e>\S+) ṭhapetvā {AV} na (?P<b>\S+), (?P<a>\S+)",
     lambda g: F.a_but_not(F.a_except(m(g["e"])), F.a_not(m(g["b"])), F.a_is(m(g["a"])))),
    (rf"(?P<a>\S+ñca) (?P<b>\S+ñca) ṭhapetvā {AV}{VAR} na ceva (?P<c>\S+) na ca (?P<d>\S+)",
     lambda g: F.a_neither(F.a_except(F.a_and(m(norm_ca(g["a"])), m(norm_ca(g["b"])))) + _var(g),
                           m(g["c"]), m(g["d"]))),
    (r"(?P<s>\S+) (?P<a>\S+?)(?P<k>ñceva| ceva) (?P<b>\S+) ca",
     lambda g: F.a_both(m(g["s"]), F.a_is(m(g["a"] + ("ṃ" if g["k"] == "ñceva" else ""))), F.a_is(m(g["b"])))),
    (rf"[Aa]vasesā (?P<n>dhātū){VAR} na (?P<b>\S+)",
     lambda g: F.a_rest(m(g["n"]), F.a_not(m(g["b"])), _var(g))),
]
A_STATEMENTS = [(re.compile(p), f) for p, f in A_STATEMENTS]


def _a_statement(body):
    for rx, f in A_STATEMENTS:
        g = rx.fullmatch(body)
        if g:
            out = f(g)
            return low(out) if body[:1].islower() else out
    return None


def _fragment(body, punct):
    """Pieces of the «…pe…» lines that are not whole sentences."""
    mm = re.fullmatch(r"(?P<e>\S+) ṭhapetvā", body)
    if mm:                                                            # Sotaṃ ṭhapetvā… (3-01)
        out = F.A_EXCEPT.split(",")[0].format(x=m(mm["e"]))
    elif re.fullmatch(r"[Nn]a (?P<b>\S+)", body) and low(body.split()[1]) in MEMBER:
        out = NEG_HEAD.format(x=m(body.split()[1]))                   # Na jivhā… / Na ghānaṃ?…
    elif low(body) in MEMBER:                                         # ghānaṃ… jivhā… / Ghānaviññāṇaṃ?…
        out = m(body)
    else:
        return None
    if punct == "?":
        out = ELLIPTIC_Q.format(x=out)
    return (cap(out) if body[:1].isupper() else out) + punct


def _strip_end(s):
    return s[:-1] if s and s[-1] in ".?" else s


def tr(body, punct, ctx, pe=False):
    """One Pāli sentence body (final punctuation split off) -> Vietnamese, + the Pāli punctuation."""
    if body == "":
        return punct
    if body in EXACT_BODY:
        return EXACT_BODY[body] + punct
    mm = E_Q_RE.fullmatch(body)
    if mm:
        vp = bool(mm["vp"])
        out = E.e_q(m(mm["x"]), E.e_vparse(mm["v1"]), m(mm["y"]), E.e_vparse(mm["v2"]), label=mm["l"],
                    vapana=vp)
        return _strip_end(out) + punct
    mm = A3.B_Q_RE.fullmatch(body)
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
            head = A3.where3(mm["g"]) if res == "tattha" else A3.who3(mm["g"])
            f = F.b_both if both else F.b_not
            out = f(res, head, m(mm["x"]), F.vparse(mm["v1"], ctx), m(mm["y"]), F.vparse(mm["v2"], ctx))
            return _strip_end(out) + punct
    out = _a_question(body, ctx)
    if out:
        return _strip_end(out) + punct
    out = _a_statement(body)
    if out:
        return _strip_end(out) + punct
    if pe:
        out = _fragment(body, punct)
        if out:
            return out
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


PE_SPLIT = A3.PE_SPLIT                              # …pe… / …Pe… / …


def tr_pe(text, ctx):
    """3-01 tr_pe rule: each piece between the ellipses is translated in place, the ellipsis stays at its spot;
    a period before or after the ellipsis gives way to it; «?…» is written «? …»."""
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


def fix_slips(t):
    for a, b, why in SLIP_FIX:
        if a in t:
            t = t.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return t


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    t = fix_slips(t)
    if "…" in t:
        return tr_pe(t, ctx) + sid
    return tr_sentences(t, ctx) + sid


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
    (f"{EIGHTEEN} – yếu tố mắt, yếu tố hình sắc, yếu tố thức qua mắt, yếu tố tai", 2),
    *((v, 2) for v in ELEMENT.values()),
    ("thức qua mắt", 1), ("thức qua tai", 1), ("thức qua mũi", 1), ("thức qua lưỡi", 1), ("thức qua thân", 1),
    ("ý thức", 2), ("yếu tố", 1), ("các yếu tố", 1), ("ở đây cũng nên phân tích như vậy", 2),
    ("được trình bày chi tiết", 2), ("đầy đủ", 2), ("giống như", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (4): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """The shared frames come out exactly as in 3-01 once the member is swapped (spot checks)."""
    a3 = A3.translate_line("(Ka) na cakkhu na cakkhāyatananti? Āmantā.", "")
    assert a3.replace("lĩnh vực mắt", "yếu tố mắt") == translate_line("(Ka) na cakkhu na cakkhudhātūti? Āmantā.", "")
    a3 = A3.translate_line("Dibbacakkhu paññācakkhu cakkhu, na cakkhāyatanaṃ. Cakkhāyatanaṃ cakkhu ceva "
                           "cakkhāyatanañca.", "")
    d4 = translate_line("Dibbacakkhu paññācakkhu cakkhu, na cakkhudhātu. Cakkhudhātu cakkhu ceva cakkhudhātu ca.", "")
    assert a3.replace("lĩnh vực mắt", "yếu tố mắt").replace("Lĩnh vực mắt", "Yếu tố mắt") == d4, (a3, d4)
    a3 = A3.translate_line("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanaṃ uppajjati, no ca tesaṃ "
                           "sotāyatanaṃ uppajjati.", "")
    d4 = translate_line("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhudhātu uppajjati, no ca tesaṃ "
                        "sotadhātu uppajjati.", "")
    assert a3.replace("lĩnh vực", "yếu tố") == d4, (a3, d4)
    a3 = A3.translate_line("Cakkhuṃ ṭhapetvā avasesā āyatanā na cakkhu, āyatanā. Cakkhuñca āyatanañca ṭhapetvā "
                           "avasesā na ceva cakkhu na ca āyatanā.", "")
    d4 = translate_line("Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhu, dhātū. Cakkhuñca dhātuñca ṭhapetvā avasesā na "
                        "ceva cakkhu na ca dhātū.", "")
    assert a3.replace("lĩnh vực nhận biết", "yếu tố") == d4, (a3, d4)
    print("frame checks against 3-01: OK")


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese within the chapter."""
    seen, bad = {}, 0
    for ln in pali.splitlines():
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        if not t.strip() or t.startswith("#") or "…" in t or t in EXACT_LINE:
            continue
        for s in F.split_sentences(fix_slips(t)):
            s = s.strip()
            v = tr(s[:-1], s[-1], "") if s[-1] in ".?" else tr(s, "", "")
            if seen.setdefault(s, v) != v:
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences")
    return bad


def check_extra(text):
    probs = []
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("….", ".…", "?…", ",…", "  ", "là là", "dhāt", "uppajj", "tesaṃ", "tattha", " ca ", ",,", "—"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    A3.check_cross_book()
    check_cross_book()
    check_frames()
    del SLIPS[:]
    SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + check_extra(text)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in used:
        print("SLIP", why)
    for c, w in SLIPS + F.SLIPS:
        print("SLIP", c, "|", w)
    for n in NOTED:
        print("AS WRITTEN", n)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
