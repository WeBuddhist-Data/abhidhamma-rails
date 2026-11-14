"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapter 2-05
(the world-transcending results, the unwholesome-resultant and the functional indeterminate minds,
^1-1-8-0 … ^1-582).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/2-05-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-2-05.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never
edited: build_rails_sample_ru.py (S), build_rails_2-04_ru.py (D) and, through D, its extended instances of
build_rails_2-03_ru.py (C = D.C) and build_rails_2-01_2-02_ru.py (B = D.B). B's and D's tables are extended
in memory with the new 2-05 material below, so every passage 2-05 shares with 2-01 … 2-04 (the openings of
the world-transcending paths, the jhāna formulas, the descriptions, the resultant frames, the feeling
strings, definitions, counted names, the ṭhapetvā line, the «ye vā pana» tail) comes out byte-identical.
A check rebuilds 2-01, 2-02, 2-03 and 2-04 in memory with the extended tables and requires them to equal
the finished files byte for byte.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

usage: python -I -X utf8 build_rails_2-05_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_04_ru", HERE / "build_rails_2-04_ru.py")
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)        # importing writes nothing; D extends its own C and B in memory
C = D.C
B = D.B

PART = "2-05-cittuppadakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
TS = S.TS
cap = S.cap
PE, ELL = "…pe…", "…"
Q_ABY = D.Q_ABY
QA_P = "Katame dhammā abyākatā? Yasmiṃ samaye "

# =========================================================================================
# 1. Names (nominative)
# =========================================================================================
NEW_NAMES = {
    "dukkhindriyaṃ": "способность боли",
    "aññātāvindriyaṃ": "способность обладателя окончательного знания",
}
for _k in NEW_NAMES:
    assert _k not in B.NAMES, _k
B.NAMES.update(NEW_NAMES)

# =========================================================================================
# 2. Synonym strings
# =========================================================================================
S_KAYA_DUKKHA = D.S_DUKKHA.replace("душевная", "телесная").replace("контактом ума", "контактом тела")
assert S_KAYA_DUKKHA == ("телесная безотрадность, телесная боль, рождённое контактом тела безотрадное болезненное "
                         "переживание, рождённое контактом тела безотрадное болезненное чувство")
P_KAYA_DUKKHA = ("kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā "
                 "dukkhā vedanā")
NEW_STR = {
    P_KAYA_DUKKHA: S_KAYA_DUKKHA,
    "tajjākāyaviññāṇadhātusamphassajaṃ " + P_KAYA_DUKKHA: D.TAJJA_KAYA.format("ая") + " " + S_KAYA_DUKKHA,
    D.P_SAMADHI_BARE: D.S_SAMADHI_BARE,
    D.P_VIRIYA_BARE: D.S_VIRIYA_BARE,
}
for _k in NEW_STR:
    assert dict.get(B.STR, _k) is None, _k
B.STR.update(NEW_STR)

# «Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S – idaṃ …» (^1-555)
AVI_RE = re.compile(r"Katamaṃ tasmiṃ samaye (\S+) hoti\? Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā (.+?) – "
                    r"(idaṃ tasmiṃ samaye .*)$")
AVI_LEAD = "То, что у тех явлений, обладающих окончательным знанием, есть окончательное знание, {}"


def avi_ru(m):
    f, s, rest = m.groups()
    return f"Что такое {B.name(f)} {TS}? " + AVI_LEAD.format(B.STR[s]) + ", – " + B.tail_ru(rest)


# =========================================================================================
# 3. Tails: «amoho abyākatamūlaṃ»; «…pe… ye vā pana …» after the «hoti» list
# =========================================================================================
D.TAIL_EXTRA.append(("amoho abyākatamūlaṃ", f"{B.NAMES['amoho']} {D.ABY_ROOT}"))
TAIL_RE = re.compile(r"(.*? hoti)((?:…pe…|;) (?:ime dhammā (?:kusalā|abyākatā)|ye vā pana).*)")


def split_at_samaye(body):
    """X, tasmiṃ samaye …; a missing comma before «tasmiṃ samaye» (^1-579) is rendered as meant"""
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    return (x[:-1] if x.endswith(",") else x), rest


def finish(rest):
    m = TAIL_RE.fullmatch(rest)
    return f", {TS} " + B.there_list(m.group(1)) + B.tail_ru(m.group(2))


# =========================================================================================
# 4. Absorption sentences: new descriptions, labels «…nti kusalaṃ / …nti vipāko», new openings
# =========================================================================================
NEW_DESC = {"animittaṃ": "не имеющее признаков"}
for _k, _v in NEW_DESC.items():
    assert _k not in B.PIECES
    B.PIECES[_k] = [("desc", _v, False)]

KUSALA_UM = "благой ум"                  # kusalaṃ (the wholesome mind)
VIPAKA_N = "результат действий"          # vipāko (vipāka)
LABEL = {"kusalaṃ": f"({KUSALA_UM})", "vipāko": f"({VIPAKA_N})"}
LABEL_RE = re.compile(r"(.*\S)nti (kusalaṃ|vipāko)")


def x_jh(x):
    """B.x_jh plus the quotation labels: «…X-nti kusalaṃ» = «…X (благой ум)», «…X-nti vipāko» =
    «…X (результат действий)». Without labels the output equals B.x_jh."""
    out, prev, first = [], None, True
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
            prev = None
            continue
        if not part.strip():
            continue
        label = ""
        m = LABEL_RE.fullmatch(part.strip())
        if m:
            part, label = m.group(1) + "ṃ", " " + LABEL[m.group(2)]
        pcs = B.chunk_pieces(part)
        for j, p in enumerate(pcs):
            text = p[1] + (label if j == len(pcs) - 1 else "")
            if first:
                out.append((" и, " if p[2] else " и ") + text)
                first = False
            elif prev is None:
                out.append(text)
            else:
                out.append(B.join(prev, p) + text)
            prev = p
    return "".join(out)


# the three higher paths in one opening (^1-553); «kāmarā gabyāpādānaṃ» is read as kāmarāgabyāpādānaṃ
SLIPS = {"kāmarā gabyāpādānaṃ": "kāmarāgabyāpādānaṃ"}
HIGHER_P = (f"lokuttaraṃ jhānaṃ bhāveti {C.LEAD_P} " + "…pe… ".join(p for p, _ in C.STAGES[1:]) + " ")
HIGHER_R = f"{C.WHEN} {C.LOK_JH_R}, " + "… ".join(r for _, r in C.STAGES[1:])
assert HIGHER_P not in B.INTROS
B.INTROS[HIGHER_P] = HIGHER_R

# functional absorptions
KIR_JH = "функциональное, ни благое, ни неблагое и не являющееся результатом действий"
SUKHAVIHARA = "для пребывания в счастье в этой жизни"
KIR_TAIL_P = "jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
KIR_INTROS = {
    "rūpāvacaraṃ " + KIR_TAIL_P:
        f"{C.WHO} развивает медитативное погружение, относящееся к миру форм, {KIR_JH}, {SUKHAVIHARA}",
    "arūpāvacaraṃ " + KIR_TAIL_P:
        f"{C.WHO} развивает медитативное погружение, относящееся к миру без форм, {KIR_JH}, {SUKHAVIHARA}",
}
INTROS = dict(B.INTROS)
INTROS.update(KIR_INTROS)

# «Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ J, tasmiṃ samaye …»
TASSEVA_R = ("Вследствие того же совершённого и развитого надмирского благого медитативного погружения, "
             "в качестве его результата, когда кто-либо")
TASSEVA_RE = re.compile(r"lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ (.+)")
TASSEVA_SPLIT = re.compile(r"(\.)? [Tt]asseva ")


def jh_sentence(body):
    for p, r in INTROS.items():
        if body.startswith(p):
            x, rest = split_at_samaye(body[len(p):])
            return r + x_jh(x) + finish(rest)
    raise KeyError("intro: " + body[:80])


def vip_lok_ru(line):
    a, dot, b = TASSEVA_SPLIT.split(line)
    # ^1-528: no full stop before «tasseva» in the Pāli; rendered as meant (full stop, capital)
    ra = B.kusala_ru("Katame dhammā kusalā? " + a[len("Katame dhammā abyākatā? "):] + ".")
    assert ra.startswith(S.Q_KUSALA + " ") and ra.endswith(".")
    ra = Q_ABY + ra[len(S.Q_KUSALA):]
    m = TASSEVA_RE.fullmatch(b)
    x, rest = split_at_samaye(m.group(1))
    xr = x_jh(x)
    assert xr.startswith(" и"), xr[:20]
    return ra + " " + TASSEVA_R + xr[2:] + finish(rest)


# =========================================================================================
# 5. Unwholesome resultants and functional minds of the sense sphere
# =========================================================================================
VKA_P = QA_P + "akusalassa kammassa katattā upacitattā "
VKA_R = "В то время, когда вследствие совершённого и накопленного неблагого действия"
assert D.VK_R.startswith(VKA_R.replace("неблагого", "благого") + ",")
KIR_M = "функциональный, ни благой, ни неблагой и не являющийся результатом действий"
VIP = dict(D.VIP)
NEW_VIP = {
    "sotaviññāṇaṃ uppannaṃ hoti": "возникает слуховое сознание",
    "dukkhasahagataṃ": "сопровождаемое болью",
    "manodhātu uppannā hoti": "возникает элемент ума",
    "manoviññāṇadhātu uppannā hoti": "возникает элемент умственного сознания",
    "kiriyā neva kusalā nākusalā na ca kammavipākā": KIR_M,
}
for _k in NEW_VIP:
    assert _k not in VIP, _k
VIP.update(NEW_VIP)
assert VIP["vipākaṃ sotaviññāṇaṃ uppannaṃ hoti"] == NEW_VIP["sotaviññāṇaṃ uppannaṃ hoti"] + ", " + D.RES_N
KIR_P = (QA_P + "manodhātu uppannā hoti kiriyā", QA_P + "manoviññāṇadhātu uppannā hoti kiriyā")


def x_vip(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
        elif part.strip():
            res = []
            for key, v in B.match(B.words_of(part), VIP):
                assert not v
                res.append(VIP[key])
            out.append(", ".join(res))
    return "".join(out)


def vipaka_akusala_ru(line):
    x, rest = split_at_samaye(line[len(VKA_P):])
    return Q_ABY + " " + VKA_R + " " + x_vip(x) + finish(rest)


def kiriya_ru(line):
    x, rest = split_at_samaye(line[len(QA_P):])
    return Q_ABY + " В то время, когда " + x_vip(x) + finish(rest)


# =========================================================================================
# 6. Headings and closing lines
# =========================================================================================
RES_AK = "являющийся результатом неблагих действий"
assert D.RES_KUS.replace("благих", "неблагих") == RES_AK
KIR_ABY = "Этически неопределённое функциональное"
H = {
    "Lokuttaravipāka-paṭhamamaggavipākā": f"Надмирский {VIPAKA_N}: результаты действий первого пути",
    "Suddhikasuññataṃ": "Простое пустое",
    "Suññatapaṭipadā": "Пустое со способом практики",
    "Suddhikaappaṇihitaṃ": "Простое свободное от устремлений",
    "Appaṇihitapaṭipadā": "Свободное от устремлений со способом практики",
    "Chandādhipateyyasuddhikapaṭipadā": "Простой способ практики с преобладанием желания",
    "Chandādhipateyyasuddhikasuññatā": "Простое пустое с преобладанием желания",
    "Dutiyādimaggavipāko": f"{cap(VIPAKA_N)} второго и последующих путей",
    "Akusalavipākaabyākataṃ": "Этически неопределённое, являющееся результатом неблагих действий",
    "Akusalavipākapañcaviññāṇāni": "Пять видов сознания, являющихся результатом неблагих действий",
    "Akusalavipākamanodhātu": f"Элемент ума, {RES_AK}",
    "Akusalavipākamanoviññāṇadhātu": f"Элемент умственного сознания, {RES_AK}",
    "Ahetukakiriyāabyākataṃ": f"{KIR_ABY}, не имеющее корней",
    "Kiriyāmanodhātu": "Функциональный элемент ума",
    "Kiriyāmanoviññāṇadhātusomanassasahagatā": "Функциональный элемент умственного сознания, сопровождаемый радостью",
    "Kiriyāmanoviññāṇadhātuupekkhāsahagatā":
        "Функциональный элемент умственного сознания, сопровождаемый невозмутимостью",
    "Sahetukakāmāvacarakiriyā": "Функциональный ум, имеющий корни, относящийся к миру чувственных желаний",
    "Rūpāvacarakiriyā": "Функциональный ум, относящийся к миру форм",
    "Arūpāvacarakiriyā": "Функциональный ум, относящийся к миру без форм",
}
CLOSE = {   # closing line Pāli -> heading key
    "Suddhikasuññataṃ.": "Suddhikasuññataṃ",
    "Suññatapaṭipadā.": "Suññatapaṭipadā",
    "Suddhikaappaṇihitaṃ.": "Suddhikaappaṇihitaṃ",
    "Appaṇihitapaṭipadā.": "Appaṇihitapaṭipadā",
    "Chandādhipateyyasuddhikapaṭipadā.": "Chandādhipateyyasuddhikapaṭipadā",
    "Chandādhipateyyasuddhikasuññatā.": "Chandādhipateyyasuddhikasuññatā",
    "Dutiyādimaggavipāko.": "Dutiyādimaggavipāko",
    "Akusalavipākapañcaviññāṇāni.": "Akusalavipākapañcaviññāṇāni",
    "Akusalavipākā manodhātu.": "Akusalavipākamanodhātu",
    "Akusalavipākā manoviññāṇadhātu.": "Akusalavipākamanoviññāṇadhātu",
    "Kiriyā manodhātu.": "Kiriyāmanodhātu",
    "Kiriyā manoviññāṇadhātu somanassasahagatā.": "Kiriyāmanoviññāṇadhātusomanassasahagatā",
    "Kiriyā manoviññāṇadhātu upekkhāsahagatā.": "Kiriyāmanoviññāṇadhātuupekkhāsahagatā",
    "Ahetukā kiriyā abyākatā.": "Ahetukakiriyāabyākataṃ",
    "Sahetukā kāmāvacarakiriyā.": "Sahetukakāmāvacarakiriyā",
    "Rūpāvacarakiriyā.": "Rūpāvacarakiriyā",
    "Arūpāvacarakiriyā.": "Arūpāvacarakiriyā",
}
NEW_EXACT = {
    "Paṭhamamaggavipāko.": f"{cap(VIPAKA_N)} первого пути.",
    "Lokuttaravipāko.": f"Надмирский {VIPAKA_N}.",
    "Vipākā abyākatā.": "Этически неопределённые результаты действий.",
    "Kiriyā abyākatā.": f"{KIR_ABY}.",
    "Cittuppādakaṇḍaṃ niṭṭhitaṃ.": "Раздел о возникновении ума завершён.",
}
for _p, _r in H.items():
    lvl = "####" if _p in ("Lokuttaravipāka-paṭhamamaggavipākā", "Akusalavipākaabyākataṃ",
                           "Ahetukakiriyāabyākataṃ") else "#####"
    NEW_EXACT[f"{lvl} {_p}"] = f"{lvl} {_r}"
for _p, _k in CLOSE.items():
    NEW_EXACT[_p] = H[_k] + "."
for _k in NEW_EXACT:
    assert _k not in B.EXACT, _k
B.EXACT.update(NEW_EXACT)


# =========================================================================================
# 7. Line dispatch, render, build
# =========================================================================================
def translate_line(line):
    line = line.replace(" " + PE, PE)          # stray space before «…pe…»: dropped (as in 2-01 … 2-04)
    for a, b in SLIPS.items():
        line = line.replace(a, b)
    if line in B.EXACT:
        return B.EXACT[line]
    if line.startswith(QA_P) and TASSEVA_SPLIT.search(line):
        return vip_lok_ru(line)
    if line.startswith(VKA_P):
        return vipaka_akusala_ru(line)
    if line.startswith(KIR_P):
        return kiriya_ru(line)
    if line.startswith(QA_P):
        return Q_ABY + " " + jh_sentence(line[len(QA_P):])
    m = AVI_RE.fullmatch(line)
    if m:
        return avi_ru(m)
    return D.translate_line(line)


def render(segs):
    blocks = []
    for sid, plines in segs:
        rlines = []
        for p in plines:
            r = cap(translate_line(p))
            B.check_ru(r)
            assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), sid
            assert p.count("–") + p.count("—") == r.count("–"), ("dash", sid, p[:60], r[:60])
            assert p.count("…pe…") <= r.count("…"), ("pe", sid)
            assert p.endswith("?") == r.endswith("?"), ("question", sid)
            assert "  " not in r and " ," not in r and ",," not in r and "..." not in r, ("spacing", sid, r)
            assert " … " not in r and r.count("?") == p.count("?"), ("form", sid, r)
            assert "развивает развивает" not in r and not re.search(r"(?<!\w)и и(?!\w)", r), ("doubling", sid, r)
            rlines.append(r)
        rlines[-1] += f" ^{sid}"
        blocks.append("\n".join(rlines))
    return blocks


def check_earlier_unchanged():
    """The extended tables must leave 2-01, 2-02, 2-03 and 2-04 exactly as finished."""
    for fn_name, fn in (("2-01-cittuppadakandam.md", B.build_2_01), ("2-02-cittuppadakandam.md", B.build_2_02),
                        ("2-03-cittuppadakandam.md", C.build), ("2-04-cittuppadakandam.md", D.build)):
        text, _ = fn()
        assert text == (S.OUT / fn_name).read_bytes().decode("utf-8"), fn_name
    print("2-01, 2-02, 2-03, 2-04: rebuilt in memory with the 2-05 tables, byte-identical to the finished files")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Russian rails: new formulas of 2-05", "",
         "Generated by build_rails_2-05_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md, notes-2-01_2-02.md, notes-2-03.md or notes-2-04.md are not "
         "repeated.", "",
         "## Frames", "",
         f"… ime dhammā kusalā. Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ J, tasmiṃ "
         f"samaye … = … это благие явления. {TASSEVA_R}[,] J, {TS} … (J as in the jhāna sentences, without the "
         "leading «и»)",
         "… ime dhammā kusalā tasseva … (^1-528, no full stop in the Pāli) = rendered as meant: «… это благие "
         "явления. Вследствие того же …»",
         "X-nti kusalaṃ (closing a jhāna clause or description) = X " + LABEL["kusalaṃ"],
         "X-nti vipāko = X " + LABEL["vipāko"],
         f"Yasmiṃ samaye akusalassa kammassa katattā upacitattā X, tasmiṃ samaye … = {VKA_R} X, {TS} …",
         f"Yasmiṃ samaye manodhātu/manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā A, "
         f"tasmiṃ samaye … = В то время, когда возникает элемент ума/элемент умственного сознания, {KIR_M}, A, "
         f"{TS} …",
         "Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S – (^1-555) = " + AVI_LEAD.format("S") + ", –",
         f"…pe… amoho abyākatamūlaṃ…pe… = … {D.TAIL_EXTRA[-1][1]}…",
         "hoti…pe… ye vā pana … – ime dhammā abyākatā. = … или же …, – это этически неопределённые явления.",
         "", "## Openings", ""]
    L.append(f"Yasmiṃ samaye {HIGHER_P.strip()} … (^1-553) = {HIGHER_R} и[,] …")
    for p, r in KIR_INTROS.items():
        L.append(f"Yasmiṃ samaye {p.strip()} … = {r} и[,] …")
    L += [f"kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ (of the absorption, neuter) = {KIR_JH}",
          f"diṭṭhadhammasukhavihāraṃ = {SUKHAVIHARA}",
          f"kiriyā neva kusalā nākusalā na ca kammavipākā (of the element, masculine) = {KIR_M}",
          "", "### Descriptions of the absorption (neuter)", ""]
    for p, r in NEW_DESC.items():
        L.append(f"{p} = {r}")
    L += ["", "### Pieces of the resultant and functional sentences", ""]
    for p, r in NEW_VIP.items():
        L.append(f"{p} = {r}")
    L += ["", "## Synonym strings", ""]
    for p, r in NEW_STR.items():
        L.append(f"{p} = {r}")
    L += ["", "## Names (nominative)", ""]
    for p, r in NEW_NAMES.items():
        L.append(f"{p} = {r}")
    L += [f"kusalaṃ (in «…nti kusalaṃ») = {KUSALA_UM}", f"vipāko (in «…nti vipāko» and the closings) = {VIPAKA_N}",
          "", "## Headings and closing lines", ""]
    for p, r in NEW_EXACT.items():
        L.append(f"{p} = {r}")
    L += ["", "## Slips rendered as meant", "",
          "kāmarā gabyāpādānaṃ (^1-553, broken word) = as kāmarāgabyāpādānaṃ",
          "missing comma before «tasmiṃ samaye» (^1-579) and between «… hoti … hoti» (^1-574) = comma",
          "missing full stop before «tasseva» (^1-528) = full stop"]
    (HERE / "notes-2-05.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-2-05.md")


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
