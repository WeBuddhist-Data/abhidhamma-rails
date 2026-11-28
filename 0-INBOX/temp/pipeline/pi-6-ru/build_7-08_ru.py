"""Russian plain zero-shot of pi-6 (Yamaka): 7-08-anusayayamaka.md (Pariññāvāra paṭiloma: person and place;
closing "Pariññāvāre paṭilomaṃ." / "Pariññāvāro.").

Every frame comes from build_7-07_ru (imported, never edited), which builds on build_7-01_ru … build_7-06_ru,
build_2-02_ru (family E: «полностью понимает», negated «не понимает полностью», never «не полностью понимает»)
and build_sample_ru. Nothing new is settled here; the only local handling is the stray Pāli comma of ^6-7-257
("… kāmadhātuyā tīsu vedanāsu, apariyāpanne so tato …"), which is kept: the Russian place list already carries a
comma at exactly that point (7-01 LOCI_SEP «, »), so the line reads «… в трёх видах чувства, в не принадлежащем …»;
the builder asserts the comma is there.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-08_ru.py [--dry]
Import: importlib.import_module("build_7-08_ru")   (importing never writes any file)
"""
import importlib
import pathlib
import sys
import unicodedata

PIPE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(PIPE) not in sys.path:
    sys.path.insert(0, str(PIPE))
import build_sample_ru as B   # noqa: E402

M = importlib.import_module("build_7-07_ru")
C = M.C

CHAPTER = "7-08-anusayayamaka.md"

# ---------------------------------------------------------------------------------------------
# Stray Pāli comma (user rule: a wrong or stray punctuation mark stays as written).
# Pāli place lists have no separator; the Russian joins places with C.LOCI_SEP «, ». The comma after
# "tīsu vedanāsu" therefore falls on a Russian comma: parse without it, then assert the comma is in place.
# ---------------------------------------------------------------------------------------------
STRAY_COMMA = {
    "kāmadhātuyā tīsu vedanāsu, apariyāpanne": "kāmadhātuyā tīsu vedanāsu apariyāpanne",   # ^6-7-257
}
STRAY_COMMA_RU = C.LOCI[ "kāmadhātuyā tīsu vedanāsu"] + C.LOCI_SEP + C.LOCI["apariyāpanne"]
assert C.LOCI_SEP == ", "


def tr_line8(body, mode):
    stray = [k for k in STRAY_COMMA if k in body]
    for k in stray:
        body = body.replace(k, STRAY_COMMA[k])
    out = M.tr_line(body, mode)
    for _ in stray:
        assert STRAY_COMMA_RU in out, out
    return out


def translate_file(src_text):
    out, mode = [], "puggala"
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        if body.startswith("#"):
            mode = M.E.mode_of(body)
        out.append(tr_line8(body, mode) + (bid or ""))
    return "\n".join(out)


FINISHED = M.FINISHED + ["7-07-anusayayamaka.md"]


def check_local8(ru, src):
    M.check_local7(ru, src)
    assert src.count("Pariññāvāre paṭilomaṃ.") == ru.count(M.FIXED["Pariññāvāre paṭilomaṃ."]) == 1
    assert src.count("Pariññāvāro.") == ru.count(M.FIXED["Pariññāvāro."]) == 1
    assert "полностью понимает" in ru and "не понимает полностью" in ru


def dry():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for i, (p, r) in enumerate(zip(src.split("\n"), translate_file(src).split("\n")), 1):
        print(i, r)


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    M.D.check_crossbook_02()
    M.E.check_crossbook_03()
    M.G.check_crossbook_05()
    M.check_crossbook_07()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local8(ru, src)
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
