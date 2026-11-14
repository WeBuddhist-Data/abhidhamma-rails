"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapter 2-03
(the world-transcending wholesome mind, ^1-1-5-0 … ^1-364).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/2-03-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-2-03.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never
edited: build_rails_sample_ru.py (S) and build_rails_2-01_2-02_ru.py (B). B's tables (NAMES, STR, PIECES,
INTROS, EXACT) are extended in memory with the new 2-03 material below, so every passage 2-03 shares with
2-01/2-02 (definitions, synonym strings, jhāna formulas, modes of progress, counted names, the ṭhapetvā
line, the «ye vā pana» tail) comes out byte-identical. A check rebuilds 2-01 and 2-02 in memory with the
extended tables and requires them to equal the finished files byte for byte.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

usage: python -I -X utf8 build_rails_2-03_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_01_2_02_ru", HERE / "build_rails_2-01_2-02_ru.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)        # importing writes nothing

PART = "2-03-cittuppadakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
TS = S.TS
cap = S.cap

# =========================================================================================
# 1. New names (nominative)
# =========================================================================================
NEW_NAMES = {
    "anaññātaññassāmītindriyaṃ": "способность познания непознанного",
    "aññindriyaṃ": "способность окончательного знания",
    "sammāvācā": "правильная речь",
    "sammākammanto": "правильное действие",
    "sammāājīvo": "правильный образ жизни",
    "navindriyāni": "девять способностей",
    "aṭṭhaṅgiko maggo": "восьмичастный путь",
}
for _k in NEW_NAMES:
    assert _k not in B.NAMES, _k
B.NAMES.update(NEW_NAMES)

# =========================================================================================
# 2. Synonym strings: bases + suffix items (each suffix item is one more comma item)
# =========================================================================================
MAGGA_P = "maggaṅgaṃ maggapariyāpannaṃ"
MAGGA_R = "фактор пути, входящий в путь"
ABST_P = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
ABST_R = ("воздержание, полное воздержание, уклонение, неделание, несовершение, невпадение в проступок, "
          "непереступание границы, разрушение моста")
NEW_BASES = {
    "tajjāmanoviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ":
        S.TAJJA.format("ое") + " " + B.S_CETANA_PLAIN,
    "catūhi vacīduccaritehi " + ABST_P: "отстранение от четырёх видов дурного речевого поведения, " + ABST_R,
    "tīhi kāyaduccaritehi " + ABST_P: "отстранение от трёх видов дурного телесного поведения, " + ABST_R,
    "micchāājīvā " + ABST_P: "отстранение от неправильного образа жизни, " + ABST_R,
    # the kāya/citta strings of the sample (^1-40 … ^1-51), here without variants
    "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ": S.S_PASSADDHI,
    "lahutā lahupariṇāmatā adandhanatā avitthanatā": S.S_LAHUTA,
    "mudutā maddavatā akakkhaḷatā akathinatā": S.S_MUDUTA,
    "kammaññatā kammaññattaṃ kammaññabhāvo": S.S_KAMMANNATA,
    "paguṇatā paguṇattaṃ paguṇabhāvo": S.S_PAGUNATA,
    "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā": S.S_UJUKATA,
}
for _k in NEW_BASES:
    assert _k not in B.STR, _k
SUFFIX = {
    MAGGA_P: MAGGA_R,
    "pītisambojjhaṅgo": "фактор пробуждения восторга",
    "samādhisambojjhaṅgo": "фактор пробуждения сосредоточения",
    "vīriyasambojjhaṅgo": "фактор пробуждения усердия",
    "satisambojjhaṅgo": "фактор пробуждения осознанности",
    "dhammavicayasambojjhaṅgo": "фактор пробуждения исследования явлений",
    "passaddhisambojjhaṅgo": "фактор пробуждения безмятежности",
    "sammāvācā": NEW_NAMES["sammāvācā"],
    "sammākammanto": NEW_NAMES["sammākammanto"],
    "sammāājīvo": NEW_NAMES["sammāājīvo"],
}
COMPOSED = {}     # Pāli string -> Russian, every composed string actually used (for the notes)


class StrTable(dict):
    """B.STR plus composition: longest base, then suffix items, joined by «, »."""

    def __missing__(self, pi):
        bases = [k for k in self.keys() if pi.startswith(k + " ")]
        if not bases:
            raise KeyError("no base for: " + pi)
        base = max(bases, key=len)
        out, rest = [dict.__getitem__(self, base)], pi[len(base):].strip()
        while rest:
            for t in sorted(SUFFIX, key=len, reverse=True):
                if rest == t or rest.startswith(t + " "):
                    out.append(SUFFIX[t])
                    rest = rest[len(t):].strip()
                    break
            else:
                raise KeyError(f"unknown suffix at {rest!r} in {pi!r}")
        COMPOSED[pi] = ", ".join(out)
        return COMPOSED[pi]


B.STR = StrTable(B.STR)
B.STR.update(NEW_BASES)

# =========================================================================================
# 3. Definitions B does not cover: the kāya/citta frame and the two «tesaṃ dhammānaṃ» faculties
# =========================================================================================
KAYA_RE = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti\? Yā tasmiṃ samaye "
                     r"(vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa|viññāṇakkhandhassa) (.+?) – "
                     r"(?:ayaṃ|idaṃ) tasmiṃ samaye (\S+) hoti\.")
GEN = {"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa": S.KAYA_GEN,
       "viññāṇakkhandhassa": S.CITTA_GEN}


def kaya_ru(m):
    f, gen, s, f2 = m.groups()
    assert f == f2
    return S.definition(f, S.body(B.STR[s], GEN[gen]))


ANN_P = {"anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ":
         "не познаны, не увидены, не достигнуты, не узнаны и не постигнуты непосредственно",
         "ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ":
         "познаны, увидены, достигнуты, узнаны и постигнуты непосредственно"}
ANN_RE = re.compile(r"Katamaṃ tasmiṃ samaye (\S+) hoti\? Yā tesaṃ dhammānaṃ (" + "|".join(ANN_P)
                    + r") sacchikiriyāya (.+?)(,| –) (idaṃ tasmiṃ samaye .*)$")
ANN_LEAD = "То, что для непосредственного постижения тех явлений, которые {}, есть {}"
AVIKKHEPO_P = "avikkhepo hoti"


def ann_ru(m):
    f, adj, s, sep, rest = m.groups()
    # ^1-364: «…pe… avikkhepo hoti…pe…» inside the tail = «… есть отсутствие отвлечения…»
    rest = rest.replace(AVIKKHEPO_P, B.there_list(AVIKKHEPO_P))
    return (f"Что такое {B.name(f)} {TS}? " + ANN_LEAD.format(ANN_P[adj], B.STR[s])
            + ("," if sep == "," else ", –") + " " + B.tail_ru(rest))


# =========================================================================================
# 4. «Katame dhammā kusalā? Yasmiṃ samaye lokuttaraṃ …» openings
# =========================================================================================
LEAD_P = "niyyānikaṃ apacayagāmiṃ"
STAGES = [   # (Pāli, Russian) purpose phrases of the four paths
    ("diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā",
     "для устранения приверженности воззрениям, для достижения первой ступени"),
    ("kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā",
     "для ослабления чувственной страсти и недоброжелательности, для достижения второй ступени"),
    ("kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā",
     "для устранения без остатка чувственной страсти и недоброжелательности, для достижения третьей ступени"),
    ("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā",
     "для устранения без остатка страсти к миру форм, страсти к миру без форм, самомнения, беспокойства "
     "и неведения, для достижения четвёртой ступени"),
]
WHO = "В то время, когда кто-либо"
WHEN = WHO + " развивает"
LOK_JH_R = "надмирское медитативное погружение, ведущее к освобождению и ведущее к убыванию"
LOK_CITTA_R = "надмирский ум, ведущий к освобождению и ведущий к убыванию"
TWENTY = [   # the «vīsati mahānayā»: what is developed (accusative), before the mind
    ("maggaṃ", "надмирский путь"),
    ("satipaṭṭhānaṃ", "надмирскую основу осознанности"),
    ("sammappadhānaṃ", "надмирское правильное усилие"),
    ("iddhipādaṃ", "надмирскую основу сверхспособностей"),
    ("indriyaṃ", "надмирскую способность"),
    ("balaṃ", "надмирскую силу"),
    ("bojjhaṅgaṃ", "надмирский фактор пробуждения"),
    ("saccaṃ", "надмирскую истину"),
    ("samathaṃ", "надмирское успокоение"),
    ("dhammaṃ", "надмирское явление"),
    ("khandhaṃ", "надмирскую совокупность"),
    ("āyatanaṃ", "надмирскую сферу восприятия"),
    ("dhātuṃ", "надмирский элемент"),
    ("āhāraṃ", "надмирское питание"),
    ("phassaṃ", "надмирский контакт"),
    ("vedanaṃ", "надмирское чувство"),
    ("saññaṃ", "надмирское восприятие"),
    ("cetanaṃ", "надмирское намерение"),
]
TWENTY_P = "…pe… ".join(f"lokuttaraṃ {p} bhāveti" for p, _ in TWENTY) + "…pe… "
TWENTY_R = "… ".join(f"развивает {r}" for _, r in TWENTY) + "… "
NEW_INTROS = {}
for _p, _r in STAGES:
    NEW_INTROS[f"lokuttaraṃ jhānaṃ bhāveti {LEAD_P} {_p} "] = f"{WHEN} {LOK_JH_R}, {_r}"
NEW_INTROS[f"{TWENTY_P}lokuttaraṃ cittaṃ bhāveti {LEAD_P} {STAGES[0][0]} "] = (
    f"{WHO} {TWENTY_R}развивает {LOK_CITTA_R}, {STAGES[0][1]}")
assert "развивает развивает" not in "".join(NEW_INTROS.values())
B.INTROS.update(NEW_INTROS)

# descriptions of the absorption (neuter, agree with «погружение»)
NEW_DESC = {"suññataṃ": "пустое", "appaṇihitaṃ": "свободное от устремлений"}
for _k, _v in NEW_DESC.items():
    assert _k not in B.PIECES
    B.PIECES[_k] = [("desc", _v, False)]

# =========================================================================================
# 5. Headings and closing lines
# =========================================================================================
PP = "Способ практики"
H = {
    "Suddhikapaṭipadā": "Простой способ практики",
    "Suññataṃ": "Пустое",
    "Suññatamūlakapaṭipadā": f"{PP}, основанный на пустоте",
    "Appaṇihitaṃ": "Свободное от устремлений",
    "Appaṇihitamūlakapaṭipadā": f"{PP}, основанный на свободе от устремлений",
    "Vīsati mahānayā": "Двадцать великих методов",
    "Adhipati": "Преобладание",
}
NEW_EXACT = {"#### Lokuttarakusalaṃ": "#### Надмирский благой ум"}
for _p, _r in H.items():
    NEW_EXACT[f"##### {_p}"] = f"##### {_r}"
    NEW_EXACT[f"{_p}."] = f"{_r}."
NEW_EXACT.update({
    "Paṭhamo maggo.": "Первый путь.",
    "Dutiyo maggo.": "Второй путь.",
    "Tatiyo maggo.": "Третий путь.",
    "Catuttho maggo.": "Четвёртый путь.",
    "Lokuttaraṃ cittaṃ.": "Надмирский ум.",
})
for _k in NEW_EXACT:
    assert _k not in B.EXACT, _k
B.EXACT.update(NEW_EXACT)


# =========================================================================================
# 6. Line dispatch, render, build
# =========================================================================================
def translate_line(line):
    if line in B.EXACT:
        return B.EXACT[line]
    m = KAYA_RE.fullmatch(line)
    if m:
        return kaya_ru(m)
    m = ANN_RE.fullmatch(line)
    if m:
        return ann_ru(m)
    return B.translate_line(line)


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
            rlines.append(r)
        rlines[-1] += f" ^{sid}"
        blocks.append("\n".join(rlines))
    return blocks


def check_earlier_unchanged():
    """The extended tables must leave 2-01 and 2-02 exactly as finished."""
    for fn_name, fn in (("2-01-cittuppadakandam.md", B.build_2_01), ("2-02-cittuppadakandam.md", B.build_2_02)):
        text, _ = fn()
        assert text == (S.OUT / fn_name).read_bytes().decode("utf-8"), fn_name
    print("2-01, 2-02: rebuilt in memory with the 2-03 tables, byte-identical to the finished files")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Russian rails: new formulas of 2-03", "",
         "Generated by build_rails_2-03_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md or notes-2-01_2-02.md are not repeated.", "",
         "## Frames", "",
         "Katamo/Katamā/Katamaṃ tasmiṃ samaye F hoti? Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa "
         f"saṅkhārakkhandhassa S – … = Что такое F {TS}? То, что {TS} {S.KAYA_GEN} есть S, – это F {TS}.",
         f"… Yā tasmiṃ samaye viññāṇakkhandhassa S – … = … То, что {TS} {S.CITTA_GEN} есть S, – …",
         "Yā tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya S – = "
         + ANN_LEAD.format(ANN_P["anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ"], "S") + ", –",
         "Yā tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya S, (^1-364, "
         "comma as written) = " + ANN_LEAD.format(ANN_P["ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ"], "S")
         + ",",
         f"…pe… avikkhepo hoti…pe… (inside a tail, ^1-364) = … {B.there_list(AVIKKHEPO_P)}…",
         "", "## Openings of the world-transcending paths", ""]
    for p, r in NEW_INTROS.items():
        L.append(f"Yasmiṃ samaye {p.strip()} … = {r} и[,] …")
    L += [f"{LEAD_P} (after jhānaṃ) = {LOK_JH_R.split(', ', 1)[1]}; after cittaṃ = "
          f"{LOK_CITTA_R.split(', ', 1)[1]}"]
    for p, r in STAGES:
        L.append(f"{p} = {r}")
    for p, r in TWENTY:
        L.append(f"lokuttaraṃ {p} bhāveti = развивает {r}")
    L += ["lokuttaraṃ cittaṃ bhāveti niyyānikaṃ apacayagāmiṃ = развивает " + LOK_CITTA_R,
          "", "### Descriptions of the absorption (neuter)", ""]
    for p, r in NEW_DESC.items():
        L.append(f"{p} = {r}")
    L += ["dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ = с трудным способом практики и медленным высшим знанием, пустое "
          "(two descriptions joined by «, »; the same for appaṇihitaṃ and for the four modes)",
          "", "## Synonym strings", ""]
    for p, r in NEW_BASES.items():
        L.append(f"{p} = {r}")
    for p, r in SUFFIX.items():
        L.append(f"… {p} (appended item) = …, {r}")
    L += ["", "### Composed strings used in 2-03", ""]
    for p, r in COMPOSED.items():
        L.append(f"{p} = {r}")
    L += ["", "## Names (nominative)", ""]
    for p, r in NEW_NAMES.items():
        L.append(f"{p} = {r}")
    L += ["", "## Headings and closing lines", ""]
    for p, r in NEW_EXACT.items():
        L.append(f"{p} = {r}")
    (HERE / "notes-2-03.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-2-03.md")


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
