"""Russian plain zero-shot of pi-6 (Yamaka): chapter 3-02-ayatanayamaka.md.

Āyatana members, helpers and the driver come from build_3-01_ru (imported, never edited); families A / B from
build_2-01_ru, the 2-02 person units (extra "ye ca …" units, pv_abbr) from build_2-02_ru, the person / place
shape from build_7-01_ru.  This module adds:
  - ay2_person_intro(): the 3-01 Āyatana person parser (sa-X-ka / a-X-ka, beings lists) widened with every
    2-01 / 2-02 person unit (pacchimabhavika, parinibbanta, "ye Xaṃ upapajjitvā parinibbāyissanti", itaresaṃ …)
    and with "a-X-kānaṃ <plane>aṃ upapajjantānaṃ"; patched into build_3-01_ru only inside ay2_units()
    (3-01's own output is asserted unchanged);
  - pe_question(): "Yassa X V tassa Y1…pe… Y2… Y3 V-ti?" (abbreviated member lists), which reproduces 3-01's
    fixed lines of the same shape (asserted);
  - the fixed note "(tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti)".

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_3-02_ru.py
Import: importlib.import_module("build_3-02_ru")   (importing never writes any file)
"""
import contextlib
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

A = importlib.import_module("build_3-01_ru")    # Āyatana members, AY_CFG, tr_line
D = A.D                                         # build_2-01_ru: families A + B
C = A.C                                         # build_7-01_ru: person / place shape
E = importlib.import_module("build_2-02_ru")    # PERSON_UNITS_2_02, pv_abbr
CHAPTER = "3-02-ayatanayamaka.md"
PREV_CHAPTER = "3-01-ayatanayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Family B: person units of the Āyatanayamaka (future, present-past and their negatives)
# =============================================================================================
# "Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti": two planes, joined with «и» as 2-01's
# "{P}aṃ {P}aṃ upapajjantānaṃ" («перерождается {in1} и {in2}»).
PERSON_UNITS_3_02 = [
    (r"ye {P}aṃ {P}aṃ upapajjitvā parinibbāyissanti",
     "тех, кто, переродившись {in1} и {in2}, достигнет окончательного угасания", True),
]
UNITS = PERSON_UNITS_3_02 + E.PERSON_UNITS_2_02 + D.PERSON_UNITS
# "acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ": 3-01's «тех, кто перерождается без глаза» + 2-01's place
REBORN_IN = A.REBORN.replace("{desc}", "{desc} {in1}")      # тех, кто перерождается {desc} {in1}
assert REBORN_IN == "тех, кто перерождается {desc} {in1}", REBORN_IN


def ay2_person_units(intro, planes=None, have=None):
    planes = A.AY_PLANES if planes is None else planes
    have = A.AY_HAVE if have is None else have
    toks = lower1(intro).split()
    pre = D._plane_re(planes)
    plane_acc = re.compile(pre + "aṃ")
    beings_rx = re.compile(pre + "ānaṃ")
    units, i = [], 0
    while i < len(toks):
        if toks[i:i + 2] == ["sabbesaṃ", "cavantānaṃ"]:                       # as 3-01
            units.append([A.ALL_DYING, True])
            i += 2
            continue
        j, descs = i, []
        while j < len(toks) and A.have_desc(toks[j], have):                    # as 3-01 (+ optional plane)
            descs.append(A.have_desc(toks[j], have))
            j += 1
        if descs:
            loc = None
            if j < len(toks) and plane_acc.fullmatch(toks[j]):
                loc = planes[plane_acc.fullmatch(toks[j]).group(1)]["in"]
                j += 1
            if j >= len(toks) or toks[j] != "upapajjantānaṃ":
                raise ValueError(f"person intro not parsed: {intro!r}")
            desc = A.HAVE_JOIN.join(descs)
            units.append([A.REBORN.format(desc=desc) if loc is None else REBORN_IN.format(desc=desc, in1=loc),
                          True])
            i = j + 1
            continue
        beings = []
        while j < len(toks) and beings_rx.fullmatch(toks[j]):                  # as 3-01
            beings.append(planes[beings_rx.fullmatch(toks[j]).group(1)]["beings"])
            j += 1
        if beings:
            units.append([A.ru_and(beings), False])
            i = j
            continue
        rest = " ".join(toks[i:])                                               # 2-01 / 2-02 units
        for rx, ru, rel in UNITS:
            m = re.compile(rx.replace("{P}", pre)).match(rest)
            if m and (m.end() == len(rest) or rest[m.end()] == " "):
                g = [planes[x] for x in m.groups()] + [{"in": "", "beings": ""}] * 2
                units.append([ru.format(in1=g[0]["in"], in2=g[1]["in"], b1=g[0]["beings"], b2=g[1]["beings"]),
                              rel])
                i += len(rest[: m.end()].split())
                break
        else:
            raise ValueError(f"person intro not parsed at {toks[i]!r} in {intro!r}")
    out, k = [], 0                                                              # itaresaṃ: as 2-01
    while k < len(units):
        t, rel = units[k]
        if t == D.ITARESAM and k + 1 < len(units):
            nt, nrel = units[k + 1]
            t = D.ITARESAM + nt[3:] if nt.startswith("тех, кто") else f"{D.ITARESAM} {nt}"
            rel = nrel
            k += 1
        out.append([t, rel])
        k += 1
    return out


def ay2_person_intro(intro, planes=None, have=None):
    """Joined exactly as build_3-01_ru.ay_person_intro / build_2-01_ru.person_intro."""
    units = ay2_person_units(intro, planes, have)
    s = "У " + units[0][0]
    for i in range(1, len(units)):
        last = i == len(units) - 1
        sep = ((", и " if units[i - 1][1] else " и ") if last else ", ")
        s += sep + "у " + units[i][0]
    return s + ("," if units[-1][1] else "") + " "


@contextlib.contextmanager
def ay2_units():
    """Use ay2_person_intro inside build_3-01_ru (and the 2-02 units in build_2-01_ru) for the block only."""
    old = A.ay_person_intro
    A.ay_person_intro = ay2_person_intro
    try:
        with E.extra_units():
            yield
    finally:
        A.ay_person_intro = old


# =============================================================================================
# Questions with abbreviated member lists: "Yassa X V tassa Y1…pe… Y2… Y3 V-ti?"
# =============================================================================================
PE_Q_RE = re.compile(r"(?P<rel>yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha) "
                     r"(?P<xs>.+?) (?P<n1>na |n)?(?P<v1>" + D.V_RE + r") (?P<cor>tassa tattha|tassa|tattha) "
                     r"(?P<ys>.+?) (?P<n2>na |n)?(?P<v2>" + D.VTI_RE + r")")
LIST_SEP = re.compile(r"…pe… |… ")


def _pred_list(names, v, neg, subj):
    """['ghānāyatanaṃ', 'rūpāyatanaṃ'] -> «возникала сфера носа… сфера видимых форм» (3-01 fixed lines)."""
    ks = [subj[n] for n in names]
    return D.verb(v, ks[0]["g"], neg) + " " + "… ".join(k["nom"] for k in ks)


def pe_question(body, subj=None):
    subj = A.AY_PV_SUBJ if subj is None else subj
    m = PE_Q_RE.fullmatch(lower1(body))
    if not m:
        raise ValueError(f"abbreviated question not parsed: {body!r}")
    rel = m.group("rel")
    kind = "yassa yattha" if ("yassa" in rel and "yattha" in rel) else ("yassa" if "yassa" in rel else "yattha")
    xs, ys = LIST_SEP.split(m.group("xs")), LIST_SEP.split(m.group("ys"))
    p1 = _pred_list(xs, m.group("v1"), bool(m.group("n1")), subj)
    p2 = _pred_list(ys, D.PV_VERB_TI[m.group("v2")], bool(m.group("n2")), subj)
    q = D.PV_Q[kind].format(p1=p1, p2=p2)
    return (D.PV_KHA + lower1(q) if "vā pana" in rel else q), subj[ys[-1]]


def pe_line(text, cfg):
    """A question line whose question has '…pe…', or None."""
    label = ""
    m = A.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    q, sep, a = text.partition("?")
    if not sep or "…pe… " not in q or not PE_Q_RE.fullmatch(lower1(q)):
        return None
    ru, y = pe_question(q, cfg["pv_subj"])
    return label + ru + (" " + A.ay_answers(a, cfg, y) if a.strip() else "")


# =============================================================================================
# Fixed lines and slips
# =============================================================================================
# "Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti)."
# sadisaṃ = «одинаковы» as 3-01's ekasadisaṃ; sadisāyeva honti = «в точности одинаковы» (eva).
SADISA_NOTE = (C.Q_PERSON.split(",")[0].format(p1=A._pv("uppajjissati", "cakkhu"))
               + f" (у того {A.AY_K['mana']['nom']} и {A.AY_K['dhamma']['nom']} одинаковы, эти две в точности "
               "одинаковы).")
AY2_FIXED = dict(A.AY_FIXED)
AY2_FIXED.update({
    "Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti).":
        SADISA_NOTE,
})
SLIPS = [   # (old, new, note): plain slips rendered as meant; each must occur exactly once
    ("tesaṃ tattha rūpāyatanañca ca uppajjittha", "tesaṃ tattha rūpāyatanañca uppajjittha",
     "^6-3-75: 'rūpāyatanañca ca uppajjittha': doubled 'ca' (parallel lines have one)"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


AY2_CFG = dict(A.AY_CFG)
AY2_CFG["fixed"] = AY2_FIXED


# =============================================================================================
# Driver
# =============================================================================================
def tr_line(text, cfg=None):
    cfg = AY2_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    m = A.TAIL_RE.fullmatch(text)
    if m and not text.startswith("#"):
        return tr_line(m.group(1), cfg) + f" ({A.TAILS[m.group(2)]}){m.group(3)}"
    r = E.pv_abbr(text, cfg["pv_subj"])                 # "Yattha X V…pe…."
    if r is not None:
        return r
    r = pe_line(text, cfg)
    if r is not None:
        return r
    return A.tr_line(text, cfg)


def translate_text(src, cfg=None):
    out = []
    with ay2_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "в мире чувственных желаний"), ("1", "в мире форм"), ("1", "в мире без форм"),
    ("2", "достигают окончательного угасания"), ("2", "перерождаются"), ("2", "умирают"),
]


def check_previous_unchanged():
    """The widened person parser must not change 3-01's own output; pe_question must give 3-01's fixed lines."""
    src = (B.PALI_DIR / PREV_CHAPTER).read_text(encoding="utf-8")
    on_disk = (B.OUT_DIR / PREV_CHAPTER).read_text(encoding="utf-8")
    with ay2_units():
        again = A.translate_text(src, A.AY_CFG)
        again2 = translate_text(src, AY2_CFG)
    assert again == on_disk, "3-01 output would change with the 3-02 person parser"
    assert again2 == on_disk, "the 3-02 driver does not reproduce 3-01"
    for k, v in A.AY_FIXED.items():
        if "…pe… " in k.partition("?")[0] and PE_Q_RE.fullmatch(lower1(k.partition("?")[0])):
            assert pe_line(k, AY2_CFG) == v, (k, pe_line(k, AY2_CFG), v)
    return src, on_disk


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    prev = check_previous_unchanged()
    SLIP_LOG.clear()
    A.SLIP_LOG.clear()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md"]]
    D.consistency(pairs + [prev, (src, ru)])
    if "--dry" in sys.argv:
        print(ru)
        return
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG + A.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 3-01, 7-01); 3-01 unchanged")


if __name__ == "__main__":
    main()
