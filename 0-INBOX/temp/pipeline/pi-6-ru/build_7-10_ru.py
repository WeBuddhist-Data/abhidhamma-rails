"""Russian plain zero-shot of pi-6 (Yamaka): 7-10-anusayayamaka.md (Pahīnavāra paṭiloma place / person and place;
Uppajjanavāra; (Ka) dhātupucchāvāra).

Every pahīna frame comes from build_7-09_ru (tr_line9, answers9, na_vattabba, FIXED with "Pahīnavāre paṭilomaṃ." /
"Pahīnavāro.", heading9, check_local9) and through it from build_7-01 … 7-08 (imported, never edited); uppajjati
«возникает» from 7-01 VERB (= 2-01 present tense). New here (all listed in notes-7-10.md):
  - dhātupucchā question frame (DHATU_* below), settled for 7-11:
    "Kāmadhātuyā cutassa (na) rūpadhātuṃ upapajjantassa kati anusayā anusenti, kati anusayā nānusenti,
    kati anusayā bhaṅgā?" = «У того, кто, умерев в мире чувственных желаний, перерождается (не) в мире форм,
    сколько скрытых склонностей залегает, сколько скрытых склонностей не залегает, сколько скрытых склонностей
    подлежит разделению?»  (cuto … upapajjati: pi-5 1-puggalakatha «умерев в мире форм, перерождается в мире без
    форм»; bhaṅgā: coordinator decision, aṭṭhakathā ^6-152 gerundive "evaṃ vibhajitabbā" -> «подлежит разделению»)
  - negated planes «не в мире X», two «не в мире X и не в мире Y» (Pāli "na X na Y").
  - mūlaka tails for the negated planes (MULAKA10).
  - "(vitthāretabbaṃ)" = «(следует развернуть)» (7-01 VITTHARETABBAM, pi-5), placed where the Pāli has it.
  - closings "Uppajjanavāro." / "Dhātupucchāvāro." (7-01 EXTRA_HEADINGS).
  - the bare number line "9" (^6-7-311) stays.
  - stray punctuation kept (user rule): ^6-7-325 ". Paṭighānusayo na vattabbo …" (a full stop where the series has
    "; "), ^6-7-335 first sentence group ends with "." instead of "?" (line 229).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-10_ru.py [--dry]
Import: importlib.import_module("build_7-10_ru")   (importing never writes any file)
Reuse (7-11): DHATU_SRC_RU, DHATU_DST_RU, planes_ru(), dhatu_who(), DHATU_KATI_RU, BHANGA_RU, DHATU_BHANGA_NATTHI10
        (proposal), dhatu_sentence(), MULAKA10, FIXED10, tr_line10(), FINISHED
"""
import importlib
import pathlib
import re
import sys
import unicodedata

PIPE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(PIPE) not in sys.path:
    sys.path.insert(0, str(PIPE))
import build_sample_ru as B   # noqa: E402

C = importlib.import_module("build_7-01_ru")
D = importlib.import_module("build_7-02_ru")
E = importlib.import_module("build_7-03_ru")
M = importlib.import_module("build_7-07_ru")
P = importlib.import_module("build_7-09_ru")

CHAPTER = "7-10-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# Dhātupucchā (planes: pi-1 / pi-2 «в мире чувственных желаний / форм / без форм»)
# ---------------------------------------------------------------------------------------------
DHATU_SRC_RU = {k: C.LOCI[k] for k in ("kāmadhātuyā", "rūpadhātuyā", "arūpadhātuyā")}   # «в мире …» (cutassa)
DHATU_DST_RU = dict(C.DHATU_DST)                                                       # «в мире …» (upapajjantassa)
assert DHATU_SRC_RU["kāmadhātuyā"] == DHATU_DST_RU["kāmadhātuṃ"] == "в мире чувственных желаний"
NEG_PLANE = "не {x}"                 # "na kāmadhātuṃ" = «не в мире чувственных желаний»
NEG_PLANE_JOIN = " и "               # "na kāmadhātuṃ na arūpadhātuṃ" = «не в мире …, и не в мире …» without comma
DHATU_WHO = "у того, кто, умерев {src}, перерождается {dst}"      # pi-5 «кто, умерев в мире форм, перерождается в …»
BHANGA_RU = "подлежит разделению"    # bhaṅgā (coordinator; aṭṭhakathā: "anusenti nānusentīti evaṃ vibhajitabbā")
DHATU_KATI_RU = ", ".join([
    "сколько " + C.ANUSAYA_HEAD_PL["gen"] + " " + C.VERB["anuseti"][0],
    "сколько " + C.ANUSAYA_HEAD_PL["gen"] + " не " + C.VERB["nānuseti"][0],
    "сколько " + C.ANUSAYA_HEAD_PL["gen"] + " " + BHANGA_RU,
])   # kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā
assert DHATU_KATI_RU == ("сколько скрытых склонностей залегает, сколько скрытых склонностей не залегает, "
                         "сколько скрытых склонностей подлежит разделению")
DHATU_Q_FRAME = "{who}, {kati}{end}"
# For 7-11 (dhātuvisajjanāvāra; coordinator): "anusayā bhaṅgā natthi" = «скрытых склонностей, подлежащих разделению, нет»
DHATU_BHANGA_NATTHI10 = C.ANUSAYA_HEAD_PL["gen"] + ", подлежащих разделению, нет"
assert DHATU_BHANGA_NATTHI10 == "скрытых склонностей, подлежащих разделению, нет"

DHATU_RE = re.compile(r"((?:na )?\w+dhātuyā(?: na \w+dhātuyā)*) cutassa ((?:na )?\w+dhātuṃ(?: na \w+dhātuṃ)*) "
                      r"upapajjantassa kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā([?.])")


def planes_ru(s, table):
    """'kāmadhātuyā' -> «в мире чувственных желаний»; 'na kāmadhātuyā na arūpadhātuyā' -> «не в мире чувственных
    желаний и не в мире без форм» (table: DHATU_SRC_RU or DHATU_DST_RU)."""
    toks = s.split(" ")
    items, neg = [], False
    for t in toks:
        if t == "na":
            neg = True
            continue
        items.append((neg, table[t]))
        neg = False
    assert len({n for n, _ in items}) == 1, s          # all negated or none
    if not items[0][0]:
        assert len(items) == 1, s
        return items[0][1]
    return NEG_PLANE_JOIN.join(NEG_PLANE.format(x=x) for _, x in items)


def dhatu_who(src, dst):
    return DHATU_WHO.format(src=planes_ru(src, DHATU_SRC_RU), dst=planes_ru(dst, DHATU_DST_RU))


def dhatu_sentence(s):
    """One dhātupucchā question (ends with '?', or with '.' as written) -> Russian."""
    m = DHATU_RE.fullmatch(C.lower1(s))
    if not m:
        raise ValueError(f"dhātu question not parsed: {s!r}")
    src, dst, end = m.groups()
    return cap(DHATU_Q_FRAME.format(who=dhatu_who(src, dst), kati=DHATU_KATI_RU, end=end))


# ---------------------------------------------------------------------------------------------
# Mūlaka tails, vitthāretabbaṃ, fixed lines
# ---------------------------------------------------------------------------------------------
MULAKA10 = dict(C.MULAKA)
MULAKA10.update({
    "Nakāmadhātumūlakaṃ": "На основе не мира чувственных желаний",
    "Narūpadhātumūlakaṃ": "На основе не мира форм",
    "Naarūpadhātumūlakaṃ": "На основе не мира без форм",
    "Nakāmanaarūpadhātumūlakaṃ": "На основе не мира чувственных желаний и не мира без форм",
    "Narūpanaarūpadhātumūlakaṃ": "На основе не мира форм и не мира без форм",
    "Nakāmanarūpadhātumūlakaṃ": "На основе не мира чувственных желаний и не мира форм",
})
for _k, _v in MULAKA10.items():
    if _k.startswith("Na") and _k not in C.MULAKA:
        assert _v.startswith("На основе не мира ")
MULAKA_TAIL_RE = re.compile(r"(.*?) \((\w+mūlakaṃ)\)")

VITTHARA = {   # Pāli ending -> (Pāli kept, Russian appended)
    " (vitthāretabbaṃ).": (".", " (" + C.VITTHARETABBAM + ")."),          # ^6-7-330, inside the sentence
    " (Vitthāretabbaṃ).": ("", " (" + cap(C.VITTHARETABBAM) + ")."),       # line 212, its own sentence
}

FIXED10 = dict(P.FIXED)
FIXED10["Uppajjanavāro."] = C.VARO_CLOSING.format(heading=C.EXTRA_HEADINGS["Uppajjanavāro"])
FIXED10["Dhātupucchāvāro."] = C.VARO_CLOSING.format(heading=cap(C.EXTRA_HEADINGS["dhātupucchāvāro"]))
assert FIXED10["Pahīnavāre paṭilomaṃ."] == "Отрицательная форма в разделе об устранённом."
assert FIXED10["Pahīnavāro."] == "Раздел об устранённом."


# ---------------------------------------------------------------------------------------------
# Lines
# ---------------------------------------------------------------------------------------------
def tr_line10(body):
    if not body.strip():
        return ""
    if body in FIXED10:
        return FIXED10[body]
    if body.startswith("#"):
        return P.heading9(body)
    if body.strip().isdigit():                 # "9" (^6-7-311): a number stays
        return body
    tail = ""
    m = MULAKA_TAIL_RE.fullmatch(body)
    if m and m.group(2) in MULAKA10 and "cutassa" in body:
        body, tail = m.group(1), f" ({MULAKA10[m.group(2)]})"
    if "cutassa" in body:
        sents = re.split(r"(?<=[?.]) (?=\S)", body.strip())
        return " ".join(dhatu_sentence(s) for s in sents) + tail
    for pk, (keep, ru_end) in VITTHARA.items():
        if body.endswith(pk):
            out = P.tr_line9(body[:-len(pk)] + keep)
            if keep:
                assert out.endswith(keep), out
                out = out[:-len(keep)]
            return out + ru_end
    return P.tr_line9(body)


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line10(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_10 = [
    ("5", "кто, умерев в мире форм, перерождается в мире без форм"),   # cuto … upapajjati
    ("5", "так следует развернуть всё"),                               # vitthāretabba (7-01)
]
FINISHED = P.FINISHED + ["7-09-anusayayamaka.md"]


def check_crossbook_10():
    cache, missing = {}, []
    for b, s in CROSSBOOK_10:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_local10(ru, src):
    P.check_local9(ru, src)
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if p.startswith("#"):
            continue
        assert p.count("cutassa") == r.count("умерев") == r.count(DHATU_KATI_RU), r
        assert p.count("bhaṅgā?") == r.count(BHANGA_RU + "?") and p.count("bhaṅgā.") == r.count(BHANGA_RU + "."), r
        assert p.count("na ") + p.count("Na ") == r.count("не в мире ") if "cutassa" in p else True, r
        assert ("uppajj" in p) == ("возникает" in r), r
        assert p.count("itthāretabbaṃ") == r.count("ледует развернуть"), r


def dry():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for i, r in enumerate(translate_file(src).split("\n"), 1):
        print(i, r)


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    D.check_crossbook_02()
    E.check_crossbook_03()
    M.G.check_crossbook_05()
    M.check_crossbook_07()
    P.check_crossbook_09()
    check_crossbook_10()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local10(ru, src)
    shared = M.check_consistency7(src, ru, FINISHED)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "| lines shared with finished chapters:",
          shared)
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    if "--dry" in sys.argv:
        dry()
    else:
        main()
