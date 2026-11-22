"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-11 (Anusayayamaka: (Kha) dhātuvisajjanāvāra, the answers of the
dhātupucchāvāra; the Anusayayamaka closing and the homage).

Imports (all READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S    build_rails_sample_vi   HOMAGE, yamaka_end, NUM / only (numeral + eva), checks
  C    build_rails_7-01_vi     family C setter: AT, THEN, LIE_LATENT, FAMILY_TERMS (kassaci, bhaṅgā, Natthi,
                               upapajjati), heading(), write()
  P9   build_rails_7-09_vi     (imported by P10; its checks are run)
  P10  build_rails_7-10_vi     DHATU, parse_planes, dhatu_phrase, dhatu_head, PERSON_SG, CUTASSA, UPA_PREP,
                               ANUSAYA_PL, DLABEL_RE, dhatu_label (the dhātupucchāvāra frames)
  (P10 itself imports 7-02, 7-06, 7-07, 2-01, 5-01.)
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; P11 = importlib.import_module("build_rails_7-11_vi")

NEW FRAMES (exposed as named constants / functions):
  NUM_VI / latent_vi()   "kassaci satta anusayā anusenti, kassaci pañca …" = «ở một số chúng sinh, bảy khuynh hướng
                         tiềm ẩn nằm sẵn, ở một số chúng sinh, năm …» (kassaci «ở một số chúng sinh», user / pi-2,
                         with pi-2's comma); "satteva anusayā anusenti" = «chỉ có bảy khuynh hướng tiềm ẩn nằm sẵn»
                         (sample: numeral + eva «Chỉ có …»)
  NO_BHANGA              "anusayā bhaṅgā natthi" = «không có khuynh hướng tiềm ẩn phải phân chia»
  no_rebirth_vi()        "<fr> cutassa <to> upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, …"
                         = «Ở người đã chết đi khỏi <fr>, không có cái gọi là sự tái sinh vào <to>, khi tái sinh xuống
                         phía dưới thì chỉ tái sinh vào cõi dục lạc, …»
  sentence_vi() / answers_vi() / tr_line() / build()
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-11_vi.py
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

C = importlib.import_module("build_rails_7-01_vi")     # family C setter (READ-ONLY)
P9 = importlib.import_module("build_rails_7-09_vi")    # READ-ONLY
P10 = importlib.import_module("build_rails_7-10_vi")   # READ-ONLY (dhātu frames)

CHAPTER = "7-11-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-11.md"
ADH_DIR = RAILS_DIR / "adh-7-11"
cap = S.cap
SEEN = {"kassaci": 0, "satteva": 0, "no_rebirth": [], "nama_joined": []}

# ---------------------------------------------------------------------------------------------------------------
# 1. Strings (all taken from the imported modules / termbase; asserted below)
# ---------------------------------------------------------------------------------------------------------------
KASSACI = C.FAMILY_TERMS["kassaci"]                          # «ở một số chúng sinh» (user decision, pi-2)
assert KASSACI == "ở một số chúng sinh"
NUM_VI = {"satta": "bảy", "pañca": "năm", "tayo": "ba"}      # pi-2 «bảy khuynh hướng tiềm ẩn», «năm khối»; S.NUM «ba»
assert NUM_VI["tayo"] == S.NUM["Tayo eva"]
ONLY = "chỉ có"                                              # numeral + eva (sample Tīṇeva «Chỉ có ba …», pi-5)
assert S.only("Tīṇeva", "X") == f"{cap(ONLY)} {S.NUM['Tīṇeva']} X."
ANUSAYA_PL = P10.ANUSAYA_PL                                  # anusayā «khuynh hướng tiềm ẩn» (termbase)
LIE = C.LIE_LATENT                                           # anusenti «nằm sẵn»
assert C.VERB["anusenti"][0] == LIE
NATTHI = C.FAMILY_TERMS["Natthi (in 7-11: anusayā bhaṅgā natthi)"]   # «không có»
BHANGA = C.FAMILY_TERMS["bhaṅgā"]                             # «phải phân chia» (user decision)
NO_BHANGA = f"{NATTHI} {ANUSAYA_PL} {BHANGA}"                # anusayā bhaṅgā natthi
assert P10.KATI_Q.endswith(f"{ANUSAYA_PL} {BHANGA}")         # = the 7-10 question's last slot

UPAPATTI_NAMA = "cái gọi là sự tái sinh"                    # upapatti nāma / upapattināma (termbase upapattināma)
UPAPAJJAMANO = "khi tái sinh"                                # upapajjamāno (termbase)
HETTHA = "xuống phía dưới"                                   # heṭṭhā (no termbase entry; no pi-1 … pi-5 precedent)
YEVA = "chỉ"                                                 # kāmadhātuṃyeva «chỉ … cõi dục lạc» (termbase)
UPAPAJJATI = C.FAMILY_TERMS["upapajjati"]                    # «tái sinh»
INTO = P10.UPA_PREP                                          # «vào» (2-01 upapajjantānaṃ preposition)
assert INTO == "vào" and UPAPAJJATI == "tái sinh"
KAMA_ONLY = f"{YEVA} {UPAPAJJATI} {INTO} {P10.DHATU['kāma']}"   # kāmadhātuṃyeva upapajjati

# ---------------------------------------------------------------------------------------------------------------
# 2. Frames
# ---------------------------------------------------------------------------------------------------------------
NUM_ALT = "|".join(NUM_VI)
KASSACI_RE = re.compile(rf"kassaci ({NUM_ALT}) anusayā anusenti")
SATTEVA_PALI = "satteva anusayā anusenti"
NO_BHANGA_PALI = "anusayā bhaṅgā natthi"


def latent_vi(text):
    """'kassaci satta anusayā anusenti, kassaci pañca …' → «ở một số chúng sinh, bảy … nằm sẵn, ở một số …»;
    'satteva anusayā anusenti' → «chỉ có bảy … nằm sẵn». Anything else raises."""
    if text == SATTEVA_PALI:
        SEEN["satteva"] += 1
        return f"{ONLY} {NUM_VI['satta']} {ANUSAYA_PL} {LIE}"
    out = []
    for part in text.split(", "):
        m = KASSACI_RE.fullmatch(part)
        if not m:
            raise ValueError(f"not a kassaci clause: {part!r} in {text!r}")
        out.append(f"{KASSACI}, {NUM_VI[m.group(1)]} {ANUSAYA_PL} {LIE}")
    if len(out) < 2:
        raise ValueError(f"a single kassaci clause: {text!r}")
    SEEN["kassaci"] += 1
    return ", ".join(out)


def tail_vi(text):
    """'<latent>; anusayā bhaṅgā natthi' → «<latent>; không có khuynh hướng tiềm ẩn phải phân chia»."""
    pre, sep, post = text.rpartition("; ")
    if not sep or post != NO_BHANGA_PALI:
        raise ValueError(f"no '; {NO_BHANGA_PALI}' at the end: {text!r}")
    return f"{latent_vi(pre)}; {NO_BHANGA}"


NO_REBIRTH_RE = re.compile(r"(.+?) cutassa (.+?) upapatti( ?)nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva "
                           r"upapajjati, (.+)")


def no_rebirth_vi(m):
    """«Ở người đã chết đi khỏi <fr>, không có cái gọi là sự tái sinh vào <to>, khi tái sinh xuống phía dưới thì
    chỉ tái sinh vào cõi dục lạc, <tail>» (the planes after cutassa are in -yā: parse_planes 'abl' form)."""
    if not m.group(1)[:1].isupper():
        raise ValueError(f"head in lower case: {m.group(0)!r}")
    fr = P10.dhatu_phrase(*P10.parse_planes(m.group(1), "abl"))
    to = P10.dhatu_phrase(*P10.parse_planes(m.group(2), "abl"))
    if not m.group(3):
        SEEN["nama_joined"].append(m.group(0)[:70])
    SEEN["no_rebirth"].append(m.group(0)[:70])
    return (f"{cap(C.AT)} {P10.PERSON_SG} {P10.CUTASSA} {fr}, {NATTHI} {UPAPATTI_NAMA} {INTO} {to}, "
            f"{UPAPAJJAMANO} {HETTHA} {C.THEN} {KAMA_ONLY}, {tail_vi(m.group(4))}")


def sentence_vi(s):
    """One answer sentence (ends in «.»)."""
    if not s.endswith("."):
        raise ValueError(f"sentence without «.»: {s!r}")
    body = s[:-1]
    if m := NO_REBIRTH_RE.fullmatch(body):
        return no_rebirth_vi(m) + "."
    head, rest = P10.dhatu_head(body)
    return head + tail_vi(rest) + "."


def answers_vi(text):
    return " ".join(sentence_vi(x) for x in re.split(r"(?<=\.) ", text.strip()) if x)


FIXED = {
    "Dhātuvisajjavāro.": C.heading("Dhātuvisajjavāro") + ".",          # closing label (= 7-10 «Dhātupucchāvāro.»)
    "Anusayayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Anusaya"),              # = 4, 8, 9-03 «<X>yamakaṃ niṭṭhitaṃ.»
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,        # = 2-02, 4, 9-03
}
assert FIXED["Dhātuvisajjavāro."] == "Mục trả lời theo các cõi."
assert P10.FIXED["Dhātupucchāvāro."] == P10.DHATUPUCCHAVARO + "."


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {C.heading(text)}"
    else:
        label = ""
        if mm := P10.DLABEL_RE.search(body):
            label = " " + P10.dhatu_label(mm)
            body = body[:mm.start()]
        out = FIXED[body] if body in FIXED else answers_vi(body)
        out += label
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
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
# 3. Checks
# ---------------------------------------------------------------------------------------------------------------
REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("kassaci ekādasāyatanāni pātubhavanti (pi-2 ^2-… dhammahadaya)", f"; {KASSACI}, mười một", "2"),
    ("satta anusayā (pi-2 ^2-949)", f"{NUM_VI['satta']} {ANUSAYA_PL}", "2"),
    ("pañcakkhandhā (pi-2)", f"{NUM_VI['pañca']} khối", "2"),
    ("pañceva (pi-5 «chỉ năm»)", f"{YEVA} {NUM_VI['pañca']}", "5"),
]
TERMBASE_USED = [
    ("dhātuvisajjanāvāro", "mục trả lời theo các cõi"), ("Dhātuvisajjavāro", "mục trả lời theo các cõi"),
    ("Kāmadhātuyā", P10.DHATU["kāma"]), ("kāmadhātuṃ", P10.DHATU["kāma"]), ("rūpadhātuyā", P10.DHATU["rūpa"]),
    ("arūpadhātuyā", P10.DHATU["arūpa"]), ("arūpadhātuṃ", P10.DHATU["arūpa"]),
    ("anusayā", ANUSAYA_PL), ("anusenti", LIE), ("bhaṅgā", BHANGA), ("Natthi", NATTHI),
    ("upapatti", "sự tái sinh"), ("upapattināma", UPAPATTI_NAMA), ("upapajjamāno", UPAPAJJAMANO),
    ("upapajjati", UPAPAJJATI), ("kāmadhātuṃyeva", f"{YEVA} … {P10.DHATU['kāma']}"),
    ("Anusayayamakaṃ", S.yamaka_title("Anusaya")), ("Namo", "Kính lễ"), ("bhagavato", "Đức Thế Tôn"),
    ("arahato", "bậc A-la-hán"), ("sammāsambuddhassa", "bậc Tự Giác Ngộ Hoàn Toàn"),
] + [(f"{x}dhātumūlakaṃ", P10._lc(P10.dhatu_label(P10.DLABEL_RE.search(f" ({x}dhātumūlakaṃ)"))[1:-1]))
     for x in P10.DLABEL_PALI]
USER_DECISIONS = ["kassaci «ở một số chúng sinh»", "bhaṅgā «phải phân chia»", "kāmadhātuṃyeva «chỉ … cõi dục lạc»"]


def check_reused():
    P10.check_reused()                       # 7-10's own (and 7-09's) reuse assertions still hold
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)
    ap = unicodedata.normalize("NFC", P10.R7.P5.APPROVED.read_text(encoding="utf-8"))
    bad = [d for d in USER_DECISIONS if d not in ap]
    assert not bad, "user decisions not found in APPROVED.md: " + repr(bad)


def check_family():
    """7-10 rebuilt by its own module = its chapter file (the imported frames are unchanged); this chapter's heads =
    7-10's dhatu_head, byte for byte."""
    saved = {k: list(v) for k, v in P10.SEEN.items()}
    name = "7-10-anusayayamaka.md"
    mine = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in P10.build(name)) + "\n")
    theirs = (S.OUT_DIR / name).read_text(encoding="utf-8")
    if mine != theirs:
        diff = [(x, y) for x, y in zip(mine.splitlines(), theirs.splitlines()) if x != y]
        raise AssertionError(f"{name} rebuilt differs: {diff[:2]}")
    for k in P10.SEEN:
        P10.SEEN[k][:] = saved[k]
    h, _ = P10.dhatu_head("Arūpadhātuyā cutassa kāmadhātuṃ upapajjantassa X")
    assert h == "Ở người đã chết đi khỏi cõi không hình sắc và đang tái sinh vào cõi dục lạc, "
    assert P10.dhatu_phrase(*P10.parse_planes("na kāmadhātuyā na arūpadhātuyā", "abl")) == \
        "nơi không phải là cõi dục lạc cũng không phải là cõi không hình sắc"


# ---------------------------------------------------------------------------------------------------------------
# 4. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-11 (Anusayayamaka: (Kha) dhātuvisajjanāvāra; closing, homage): frames and fixed strings", "",
         "Generated by build_rails_7-11_vi.py. Imports S, 7-01 (family C), 7-09 and 7-10 (DHATU, parse_planes, "
         "dhatu_phrase, dhatu_head, CUTASSA, DLABEL_RE, dhatu_label …): their strings, byte for byte; the builder "
         "rebuilds 7-10 with its own module and asserts it equals the 7-10 chapter file. Import with "
         "importlib.import_module(\"build_rails_7-11_vi\").", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Answers of the dhātu section (new)")
    row("kassaci (user decision, pi-2 with its comma)", f"{KASSACI}, …")
    row("kassaci satta / pañca / tayo anusayā anusenti",
        f"{KASSACI}, {NUM_VI['satta']} / {NUM_VI['pañca']} / {NUM_VI['tayo']} {ANUSAYA_PL} {LIE}")
    row(SATTEVA_PALI, latent_vi(SATTEVA_PALI) + "  (sample numeral + eva «Chỉ có …»; commentary: niyametvā vuttaṃ)")
    row(NO_BHANGA_PALI, NO_BHANGA + "  (Natthi «không có», bhaṅgā «phải phân chia»)")
    row("upapatti nāma / upapattināma", UPAPATTI_NAMA + "  (termbase upapattināma)")
    row("heṭṭhā upapajjamāno", f"{UPAPAJJAMANO} {HETTHA}  (upapajjamāno termbase; heṭṭhā: gap, no precedent)")
    row("kāmadhātuṃyeva upapajjati", KAMA_ONLY + "  (termbase «chỉ … cõi dục lạc»)")
    for p in ("Kāmadhātuyā cutassa kāmadhātuṃ upapajjantassa kassaci satta anusayā anusenti, kassaci pañca anusayā "
              "anusenti; anusayā bhaṅgā natthi.",
              "Rūpadhātuyā cutassa kāmadhātuṃ upapajjantassa satteva anusayā anusenti; anusayā bhaṅgā natthi.",
              "Na kāmadhātuyā na arūpadhātuyā cutassa na rūpadhātuṃ na arūpadhātuṃ upapajjantassa satteva anusayā "
              "anusenti; anusayā bhaṅgā natthi.",
              "Arūpadhātuyā cutassa rūpadhātuyā upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, "
              "satteva anusayā anusenti; anusayā bhaṅgā natthi.",
              "Na kāmadhātuyā na rūpadhātuyā cutassa na kāmadhātuyā na arūpadhātuyā upapatti nāma natthi, heṭṭhā "
              "upapajjamāno kāmadhātuṃyeva upapajjati, satteva anusayā anusenti; anusayā bhaṅgā natthi."):
        row(p, sentence_vi(p))
    h("Imported (7-10): heads and labels")
    row("<fr> cutassa <to> upapajjantassa", "Ở người đã chết đi khỏi <fr> và đang tái sinh vào <to>, …  (7-10 "
                                             "dhatu_head)")
    row("<fr> cutassa (no upapajjantassa)", f"{cap(C.AT)} {P10.PERSON_SG} {P10.CUTASSA} <fr>, …")
    for x in P10.DLABEL_PALI:
        row(f"({x}dhātumūlakaṃ)", P10.dhatu_label(P10.DLABEL_RE.search(f" ({x}dhātumūlakaṃ)")))
    h("Heading, closings, homage")
    row("(Kha) dhātuvisajjanāvāro (heading)", C.heading("(Kha) dhātuvisajjanāvāro") + "  (S.LATER_HEADINGS)")
    for k, v in FIXED.items():
        row(k, v)
    h("Pāli as written (reported)")
    for s in sorted(set(SEEN["nama_joined"])):
        o.append(f"- «upapattināma» written as one word (elsewhere «upapatti nāma»; termbase has both): same "
                 f"Vietnamese: {s}…")
    o.append("- The planes after cutassa in the no-rebirth sentences are in -yā (rūpadhātuyā upapatti, na kāmadhātuyā "
             "na arūpadhātuyā upapatti): «sự tái sinh vào …».")
    o.append("- The Pāli's own commas kept: «…, ở một số chúng sinh, năm …; …» and «… natthi, heṭṭhā …, …».")
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    print("kassaci sentences:", SEEN["kassaci"], "satteva:", SEEN["satteva"], "no-rebirth:", len(SEEN["no_rebirth"]))
    for x in sorted(set(SEEN["nama_joined"])):
        print("upapattināma joined:", x)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)


if __name__ == "__main__":
    main()
