"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-08 (Anusayayamaka: pariññāvāra, paṭiloma: person + place;
closing lines «Pariññāvāre paṭilomaṃ.» / «Pariññāvāro.»).

Imports (all READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S  build_rails_sample_vi   labels, «…», checks
  R7 build_rails_7-07_vi     the Verb-parameterised parijānāti / pajahati frames (PARIJ, sentence, question,
                             body_vi, tr_line, build); through it 7-01 (C), 7-03, 7-05, 7-06 and 2-02 (family E)
  C  build_rails_7-01_vi     family C setter: headings, write()
  T2 build_rails_7-02_vi     PATILOMA «Chiều ngược» (the «<paṭiloma> trong mục về …» closing line)
  R6 build_rails_7-06_vi     FIXED closing lines of the pajahati paṭiloma («Pajahanāvāre paṭilomaṃ.», «Pajahanavāro.»)
  E  build_rails_2-02_vi     family E setter (parijānāti)
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; R8 = importlib.import_module("build_rails_7-08_vi")

Every line of 7-08 is built by R7's frames with the parijānāti verb (R7.PARIJ); nothing is re-implemented here.
New here (exposed): FIXED, the two closing lines of the pariññāvāra paṭiloma, built as 7-06's pajahati ones:
  Pariññāvāre paṭilomaṃ. = «Chiều ngược trong mục về sự hiểu biết trọn vẹn.»
  Pariññāvāro.           = «Mục về sự hiểu biết trọn vẹn.»
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-08_vi.py
"""
import importlib
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)

R7 = importlib.import_module("build_rails_7-07_vi")   # verb-parameterised frames (READ-ONLY)
C = importlib.import_module("build_rails_7-01_vi")    # family C setter (READ-ONLY)
T2 = importlib.import_module("build_rails_7-02_vi")   # READ-ONLY
R6 = importlib.import_module("build_rails_7-06_vi")   # READ-ONLY
E = importlib.import_module("build_rails_2-02_vi")    # family E setter (READ-ONLY)

CHAPTER = "7-08-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-08.md"
ADH_DIR = RAILS_DIR / "adh-7-08"
V = R7.PARIJ
assert V.pos == E.PARIJANATI and V.still == E.denied(E.E_VERBS["na parijānāti"])   # family E (2-02)

# ---------------------------------------------------------------------------------------------------------------
# 1. Fixed lines (built as 7-06's FIXED with the pariññāvāra heading of 7-07)
# ---------------------------------------------------------------------------------------------------------------
PARINNAVARO = R7.PARINNAVARO          # «Mục về sự hiểu biết trọn vẹn» (S.LATER_HEADINGS, termbase)
PARINNAVARO_LC = R7.PARINNAVARO_LC
FIXED = dict(R7.FIXED)                # «Pariññāvāre anulomaṃ.» (7-07), kept for later chapters
FIXED.update({
    "Pariññāvāre paṭilomaṃ.": f"{T2.PATILOMA} trong {PARINNAVARO_LC}.",
    "Pariññāvāro.": PARINNAVARO + ".",
})
assert R6.FIXED["Pajahanāvāre paṭilomaṃ."] == f"{T2.PATILOMA} trong {R6.PAJAHANAVARO_LC}."
assert R6.FIXED["Pajahanavāro."] == R6.PAJAHANAVARO + "."
assert T2.PATILOMA == "Chiều ngược" and C.HEADINGS["paṭilomapuggalokāsā"] == "Chiều ngược theo người và nơi chốn"
assert PARINNAVARO == C.heading("Pariññāvāra") == "Mục về sự hiểu biết trọn vẹn"


# A comma between two places of an answer head (^6-7-257 «… kāmadhātuyā tīsu vedanāsu, apariyāpanne so tato …»):
# the head frame (7-06 parse_head / head_vi) already sets a comma between places, so it is dropped before parsing
# and the Vietnamese keeps a comma at that spot. Only place-word, comma, place-word inside a head is allowed.
PLACE_COMMA_RE = re.compile(r"( (?:vedanāsu|vedanāya|rūpadhātuyā|arūpadhātuyā)), "
                            r"(?=(?:apariyāpanne|kāmadhātuyā|rūpadhātuyā|arūpadhātuyā|dukkhāya) (?:\S+ )*?so tato )")
PLACE_COMMAS = []   # reported in the notes


def tr_line(p):
    if m := PLACE_COMMA_RE.search(p):
        PLACE_COMMAS.append(p[max(0, m.start() - 45):m.end() + 25])
        p = PLACE_COMMA_RE.sub(r"\1 ", p)
    return R7.tr_line(p, V, FIXED)


def build(name=CHAPTER):
    """= R7.build with the verb PARIJ and FIXED; PLACE_COMMA_RE applied first (the only addition)."""
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:120]!r}: {e}") from None
        segs.append(out)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# 2. Checks
# ---------------------------------------------------------------------------------------------------------------
TERMBASE_USED = [("paṭilomaṃ", "chiều ngược"), ("paṭilomapuggalokāsā", "chiều ngược theo người và nơi chốn"),
                 ("Pariññāvāro", PARINNAVARO_LC), ("Pariññāvāre", PARINNAVARO_LC)]


def check_reused():
    R7.check_reused()   # 7-01 … 7-07 / 2-02 strings, termbase, APPROVED.md
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)


def check_family():
    """R7's own checks (7-05 / 7-06 rebuilt byte for byte, family E strings) + 7-07 rebuilt = its chapter file."""
    R7.check_family()
    saved = {k: list(v) for k, v in R7.SEEN.items()}
    mine = "\n\n".join("\n".join(s) for s in R7.build(R7.CHAPTER)) + "\n"
    theirs = (S.OUT_DIR / R7.CHAPTER).read_text(encoding="utf-8")
    assert unicodedata.normalize("NFC", mine) == theirs, "7-07 rebuilt differs from its chapter file"
    for k in R7.SEEN:
        R7.SEEN[k][:] = saved[k]


def check_shared(segs):
    """Identical Pāli = identical Vietnamese: every Pāli sentence / question of 7-08 that also occurs in 7-07
    (same frames) is rendered the same (built by the same functions; asserted on the lines' chunks)."""
    p7 = "\n".join(ln for seg in S.segments_of(R7.CHAPTER) for ln in seg)
    n = 0
    for seg in S.segments_of(CHAPTER):
        for ln in seg:
            body = re.sub(r" \^\S+$", "", ln)
            body = C.MULAKA_RE.sub("", body).rstrip()
            if body.startswith("#") or body in FIXED:
                continue
            for ch in R7.CHUNK_RE.split(body):
                if ch in p7:
                    n += 1
    return n


# ---------------------------------------------------------------------------------------------------------------
# 3. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes(n_shared):
    o = ["# Rails 7-08 (Anusayayamaka, pariññāvāra paṭiloma: person + place): frames and fixed strings", "",
         "Generated by build_rails_7-08_vi.py. Every line is built by build_rails_7-07_vi (the Verb-parameterised "
         "7-05 / 7-06 frames, verb PARIJ «hiểu biết trọn vẹn»), which imports 7-01 (family C), 7-03, 7-05, 7-06 and "
         "2-02 (family E): their strings, byte for byte. The builder reruns 7-07's checks (7-05 and 7-06 rebuilt "
         "byte for byte), rebuilds 7-07 and asserts it equals its chapter file. Later chapters import the module "
         "(importlib.import_module(\"build_rails_7-08_vi\")) for FIXED.", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("New fixed lines (built as 7-06 «Pajahanāvāre paṭilomaṃ.» / «Pajahanavāro.»)")
    for k in ("Pariññāvāre paṭilomaṃ.", "Pariññāvāro."):
        row(k, FIXED[k])
    h("Heading")
    row("(Ca) paṭilomapuggalokāsā", C.heading("(Ca) paṭilomapuggalokāsā"))
    h("Frames used (all from 7-07 / 7-06; no new frame)")
    for p in ("(Ka) yo yato kāmarāgānusayaṃ na parijānāti so tato paṭighānusayaṃ na parijānātīti?",
              "Yo yato kāmarāgānusayaṃ na parijānāti so tato diṭṭhānusayaṃ…pe… vicikicchānusayaṃ na parijānātīti?"):
        row(p, R7.question(p, V))
    for p in ("Anāgāmimaggasamaṅgī dukkhāya vedanāya so tato kāmarāgānusayaṃ na parijānāti, no ca so tato "
              "paṭighānusayaṃ na parijānāti.",
              "Sveva puggalo rūpadhātuyā arūpadhātuyā apariyāpanne so tato kāmarāgānusayañca na parijānāti "
              "paṭighānusayañca na parijānāti.",
              "Anāgāmimaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā sabbattha kāmarāgānusayañca na "
              "parijānanti vicikicchānusayañca na parijānanti.",
              "Anāgāmimaggasamaṅgī dukkhāya vedanāya so tato mānānusayañca kāmarāgānusayañca na parijānāti, no ca so "
              "tato paṭighānusayaṃ na parijānāti.",
              "Aṭṭhamako kāmadhātuyā tīsu vedanāsu rūpadhātuyā arūpadhātuyā so tato bhavarāgānusayañca "
              "kāmarāgānusayañca paṭighānusayañca mānānusayañca na parijānāti, no ca so tato diṭṭhānusayañca "
              "vicikicchānusayañca na parijānāti.",
              "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca ṭhapetvā avasesā puggalā sabbattha vicikicchānusayañca na "
              "parijānanti kāmarāgānusayañca paṭighānusayañca mānānusayañca diṭṭhānusayañca na parijānanti …pe…."):
        row(p, R7.sentence(p, V))
    h("Reuse")
    o.append(f"- {n_shared} Pāli questions / sentences of this chapter also occur in 7-07 and are built by the "
             "same functions (identical Vietnamese).")
    h("Pāli as written / punctuation (reported)")
    for p in sorted(set(R7.SEEN["punct"])):
        o.append(f"- {p}")
    for s in sorted(set(R7.SEEN["noca_comma"])):
        o.append(f"- missing comma before no ca, added: {s[:80]}")
    for p in sorted(set(PLACE_COMMAS)):
        o.append(f"- comma between two places of a head: …{p}…: dropped before parsing; the head frame sets a "
                 "comma between places anyway, so the Vietnamese has one at that spot")
    o.append("- ^6-7-256 «Āmantā …pe….», ^6-7-261 «… na parijānanti …pe….»: «…pe…» → «…» (7-03 pe_tail).")
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    segs = build()
    n = check_shared(segs)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes(n)), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for k, v in R7.SEEN.items():
        if k != "both_tad":
            for x in sorted(set(v)):
                print(f"{k}: {x[:110]}")
    print("shared with 7-07:", n)
    for p in sorted(set(PLACE_COMMAS)):
        print("place comma dropped:", p)
    for p, v in sorted(set(C.SLIPS_SEEN)):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
