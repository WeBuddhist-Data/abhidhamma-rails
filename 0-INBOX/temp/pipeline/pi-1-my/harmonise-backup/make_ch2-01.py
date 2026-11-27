"""Burmese zero-shot of pi-1 chapter 2-01 (Cittuppādakaṇḍa: the eight wholesome cittas of the sense sphere).

usage: python3 -I -X utf8 make_ch2-01.py [--terms]
Every line is generated from the Pāli by my_formulas.translate_cu() through the Cittuppāda section of my_formulas.py
(NAMES, SYN, GEN, BODY, CITTA_KIND, QUAL, ARAMMANA, the frames); a line no rule matches stops the run
(my_formulas.Miss), nothing is guessed. --terms (also done by default) rewrites the «## Cittuppāda (2-01)» section at
the end of my-zeroshot-terms.md (the rest of that file, written by make_sample.py, is kept as it is).
Model for 2-02 … 5: copy this file, add your entries to the my_formulas tables in memory, call F.rebuild_cu(), and
change NAMES_OUT and the terms section heading.
"""
import pathlib
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["2-01-cittuppadakandam.md"]
TERMS_HEAD = "## Cittuppāda (2-01)"


def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name):
    write(name, F.translate_cu((PALI / name).read_text(encoding="utf-8-sig")))


def terms_section():
    L = [TERMS_HEAD, "",
         "Added by make_ch2-01.py from the Cittuppāda section of my_formulas.py (additive; nothing above changed).", ""]
    L += ["### Frames", "",
          f"Katame dhammā kusalā? = {F.KATAME_KUSALA}။",
          f"Yasmiṃ samaye … uppannaṃ hoti = … {F.UPPANNA} {F.YASMIM}",
          f"X-ārammaṇaṃ vā = X{F.ARAMMANA_VA}",
          f"yaṃ yaṃ vā panārabbha = {F.YAM_YAM}",
          f"tasmiṃ samaye = {F.TASMIM}", f"Tasmiṃ kho pana samaye = {F.KHO_PANA_SAMAYE}",
          f"X hoti / honti = X {F.CU_HOTI['sg']} / X {F.CU_HOTI['pl']}",
          f"Katamo / Katamā / Katamaṃ tasmiṃ samaye X hoti? = {F.TASMIM} {F.CU_REL['sg']} X {F.CU_Q['sg']}။",
          f"Katame / Katamāni / Katamā tasmiṃ samaye X honti? = {F.TASMIM} {F.CU_REL['pl']} X {F.CU_Q['pl']}။",
          f"Yo / Yā / Yaṃ tasmiṃ samaye A B C – = {F.TASMIM} {F.CU_REL['sg']} A၊ B၊ C –",
          f"ayaṃ / idaṃ tasmiṃ samaye X hoti. = {F.CU_DEM['sg']} {F.TASMIM} {F.CU_REL['sg']} X {F.CU_COP['sg']}။",
          f"ime / imāni / imā tasmiṃ samaye X honti. = {F.CU_DEM['pl']} {F.TASMIM} {F.CU_REL['pl']} X "
          f"{F.CU_COP['pl']}။",
          f"ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā = {F.YEVA}",
          f"ṭhapetvā X-ṃ = X{F.THAPETVA}",
          f"ime dhammā kusalā = {F.IME_KUSALA}",
          f"eko / ekā / ekaṃ X = X {F.NUM['eka']}{F.CL}; counted groups = X N{F.CL}",
          "separators: «, » «; » = «၊ »; «?» «.» = «။»; « – » kept; «…pe…» = «…»", ""]
    L += ["### Building blocks", "",
          f"kāya- (kāyapassaddhi …) = {F.KAYA}", f"-indriya = X၏ {F.INDRIYA}", f"-bala = X၏ {F.BALA}",
          f"sammā- = {F.SAMMA}", f"khandha = {F.KHANDHA}", f"viññāṇa = {F.VINNANA}", f"mano = {F.MANO}",
          f"āhāra = {F.AHARA}", f"jhāna = {F.JHANA}", f"magga = {F.MAGGA}", f"aṅga = {F._ANGA}",
          f"somanassa = {F.SOMANASSA}", f"cetosamphassaja- = {F.CSJ}", f"kaṇḍa = {F.KANDA}",
          f"-vāra / padabhājanī = … {F.VARA}", f"bhāṇavāra = {F.BHANAVARA}", ""]
    L += ["### The citta opening", ""] + [f"{p} = {m}" for p, m in F.CITTA_KIND.items()] + \
         [f"{p} = {m}" for p, m in F.QUAL.items()] + [f"{p} = {m}" for p, m in F.QUAL_ADV.items()] + \
         [f"{p} vā = {m}{F.ARAMMANA_VA}" for p, m in F.ARAMMANA.items()] + [""]
    L += ["### Factor names (NAMES)", ""] + [f"{p} = {m}" for p, m in F.NAMES.items()] + [""]
    L += ["### Synonyms (SYN; items that are also factor names use NAMES)", ""] + \
         [f"{p} = {m}" for p, m in F.SYN.items()] + [""]
    L += ["### List heads (GEN) and sentence definitions (BODY)", ""] + \
         [f"{p} = {m}" for p, m in F.GEN.items()] + [f"{p} = {m}" for p, m in F.BODY.items()] + [""]
    L += ["### Headings and colophons", ""] + [f"{p} = {m}" for p, m in F._CU_TITLES.items()] + [""]
    L += ["### Variant readings", ""] + \
         [f"{p} = {F.VAR_KIND[p]}" for p in ["viriyindriyaṃ", "viriyabalaṃ", "kāyappassaddhi", "cittappassaddhi",
                                              "kāyujjukatā", "cittujjukatā", "sañcetayitattaṃ", "viriyārambho",
                                              "ussoḷhi", "irīyanā", "adūsanā adūsitattaṃ", "paṭippassaddhi",
                                              "paṭippassambhanā", "paṭippassambhitattaṃ", "thapetvā"]]
    return "\n".join(L) + "\n"


def write_terms():
    p = HERE / "my-zeroshot-terms.md"
    txt = p.read_text(encoding="utf-8")
    i = txt.find("\n" + TERMS_HEAD + "\n")
    base = (txt[:i + 1] if i >= 0 else txt).rstrip("\n") + "\n\n"
    p.write_text(unicodedata.normalize("NFC", base + terms_section()), encoding="utf-8")
    print("updated my-zeroshot-terms.md:", TERMS_HEAD)


if __name__ == "__main__":
    for n in NAMES_OUT:
        chapter(n)
    write_terms()
