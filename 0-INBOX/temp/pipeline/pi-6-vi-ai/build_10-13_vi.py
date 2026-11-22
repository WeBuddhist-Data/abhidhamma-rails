# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-13-indriyayamaka.md: the Indriyayamaka pariññāvāra (the six time
sections, anuloma / paccanīka), the close of the Indriyayamaka and of the whole book.

Frames come VERBATIM from the frame-setters:
  build_2-02_vi (E): family E, the yo / so question frame (e_q), e_pred / e_deny, the answer frames (E_BUT_C,
      E_BOTH_C, E_STATEMENT_PERSON, E_STATEMENT_RES), E_PERSON_NOM / E_PERSON_ACC, E_YE, E_TE, E_REL / E_DEM,
      PARINNA_EXACT;
  build_2-01_vi (F): the tense tables (verb / deny), a_except_n / a_and, variant(), heading(), split_sentences, NO;
  build_10-01_vi (I): the faculty table (m());  build_3-01_vi (A3): MULAKA «(Phần dựa trên …)»;
  build_7-01_vi (A7): YO_VERB pajahati «dứt bỏ»;  build_9-01_vi (D9): BH_VERB bhāveti «tu tập»;
  build_7-04_vi (C4): «Dve / Tayo / Cattāro puggalā», Anāgāmī;  build_7-06_vi (N6): the path persons;
  build_5-03_vi (T53): pajahati in the three tenses (its vparse is asserted against ours);
  build_sample_vi (S): labels, SECTION, AMANTA, yamaka_end, BOOK_END, check_lines.
New here (notes-10-13.md): sacchikaroti «tự mình chứng nghiệm» in the three tenses, bhāveti past / future, the
numbers Pañca … Aṭṭha puggalā, «X maggasamaṅgino», «Yo aggaphalaṃ sacchikaroti / sacchākāsi so», «Ye puthujjanā
maggaṃ paṭilabhissanti te», the «ṭhapetvā» groups with maggasamaṅgino / aṭṭhamaka / anāgāmimaggasamaṅgī.

Importing writes nothing; run  python -I -X utf8 -B build_10-13_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")      # families A / B (tense tables, except / and, variants)
E = importlib.import_module("build_2-02_vi")      # family E frame-setter
I = importlib.import_module("build_10-01_vi")     # faculty table
A3 = importlib.import_module("build_3-01_vi")     # MULAKA
A7 = importlib.import_module("build_7-01_vi")     # YO_VERB pajahati
C4 = importlib.import_module("build_7-04_vi")     # nominative persons
N6 = importlib.import_module("build_7-06_vi")     # path persons
D9 = importlib.import_module("build_9-01_vi")     # BH_VERB bhāveti
T53 = importlib.import_module("build_5-03_vi")    # pajahati tenses in family E

NAME = "10-13-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
SLIPS = []

# ================================================================ verbs (base, tense, neg) via the 2-01 tables
# parijānāti = hiểu biết trọn vẹn (2-02); pajahati = dứt bỏ (7-01 / 5-03); bhāveti = tu tập (9-01);
# sacchikaroti = tự mình chứng nghiệm (pi-4 / pi-5 «sacchikaroti: tự mình chứng nghiệm») [new here]
BASE_VI = {
    "parijān": E.E_BASE,
    "pajah": A7.YO_VERB["pajahati"]["p"].replace(" {t}", ""),
    "bhāv": D9.BH_VERB["bhāveti"]["p"].replace(" {t}", ""),
    "sacchikar": "tự mình chứng nghiệm",
}
VERB_RE = {
    "parijān": (r"na ", r"ātīti|āti|anti|itthāti|ittha|issatīti|issati|issanti"),
    "pajah": (r"nap", r"atīti|ati|anti|itthāti|ittha|issatīti|issati|issanti"),
    "bhāv": (r"na ", r"etīti|eti|enti|itthāti|ittha|essatīti|essati|essanti"),
    "sacchikar": (r"na ", r"otīti|oti|onti|itthāti|ittha|issatīti|issati|issanti"),
}
TENSE = {}
for _e in ("ātīti", "āti", "anti", "atīti", "ati", "etīti", "eti", "enti", "otīti", "oti", "onti"):
    TENSE[_e] = "pres"
for _e in ("itthāti", "ittha"):
    TENSE[_e] = "past"
for _e in ("issatīti", "issati", "issanti", "essatīti", "essati", "essanti"):
    TENSE[_e] = "fut"
V = "|".join(rf"(?:{n})?{b}(?:{t})" for b, (n, t) in VERB_RE.items())
VFORM = re.compile("|".join(rf"(?P<n{i}>{n})?(?P<b{i}>{b})(?P<t{i}>{t})"
                            for i, (b, (n, t)) in enumerate(VERB_RE.items())))


def vparse(s):
    mm = VFORM.fullmatch(s)
    if not mm:
        raise ValueError(f"unparsed verb {s!r}")
    for i in range(len(VERB_RE)):
        if mm[f"b{i}"]:
            return (BASE_VI[mm[f"b{i}"]], TENSE[mm[f"t{i}"]], bool(mm[f"n{i}"]))
    raise AssertionError(s)


# ================================================================ persons
NUM_VI = {"Dve": "Hai", "Tayo": "Ba", "Cattāro": "Bốn", "Pañca": "Năm", "Cha": "Sáu", "Satta": "Bảy",
          "Aṭṭha": "Tám"}                         # pi-4 «Năm / Sáu / Bảy / Tám hạng người»; 7-04 Hai / Ba / Bốn
PUGGALA = "hạng người"                            # puggalā (pi-4, 7-04)
MAGGI = N6.MAGGI                                  # maggasamaṅgī = người có được con đường (7-06)
PERSON_NOM = dict(E.E_PERSON_NOM)                 # Arahā, Anāgāmī, Dve / Tayo / Cattāro puggalā, Aggamaggasamaṅgī …
PERSON_NOM.update({
    "Anāgāmimaggasamaṅgī": cap(N6.ANAGAMI_M),     # Người có được con đường không trở lại (7-06)
    "Aṭṭhamako": cap(N6.ATTHAMAKA),               # Người thứ tám (7-05 / 7-06)
})
for _n, _v in NUM_VI.items():
    PERSON_NOM.setdefault(f"{_n} puggalā", f"{_v} {PUGGALA}")          # Pañca puggalā = Năm hạng người
    PERSON_NOM[f"{_n} maggasamaṅgino"] = f"{_v} {MAGGI}"               # Tayo maggasamaṅgino = Ba người có được con đường
PERSON_ACC = {                                    # members of a «… ṭhapetvā» group (lowercase Vietnamese)
    "aggamaggasamaṅgi": E.E_PERSON_ACC["aggamaggasamaṅgiṃ"],           # người có được con đường tối thượng (2-02)
    "arahanta": E.E_PERSON_ACC["arahantaṃ"],                           # bậc A-la-hán (2-02)
    "anāgāmimaggasamaṅgi": N6.ANAGAMI_M,                               # người có được con đường không trở lại (7-06)
    "aṭṭhamaka": N6.ATTHAMAKA,                                         # người thứ tám (7-06)
}
for _n, _v in NUM_VI.items():
    PERSON_ACC[f"{_n} maggasamaṅgino"] = f"{low(_v)} {MAGGI}"          # Dve maggasamaṅgino (acc.) = hai người … (7-06)
AGGAPHALA = "thành quả tối thượng"                # aggaphalaṃ (5-03 «thành quả tối thượng»)
REL_SUBJ = {                                      # relative subjects -> (head, resumptive)
    "Yo aggaphalaṃ sacchikaroti so": (
        cap(f"{E.E_REL} {E.e_pred(AGGAPHALA, (BASE_VI['sacchikar'], 'pres', False))}"), E.E_DEM),
    "Yo aggaphalaṃ sacchākāsi so": (                                   # aorist = past (đã …)
        cap(f"{E.E_REL} {E.e_pred(AGGAPHALA, (BASE_VI['sacchikar'], 'past', False))}"), E.E_DEM),
    "Ye puthujjanā maggaṃ paṭilabhissanti te": (
        cap(E.E_YE["puthujjanā maggaṃ na paṭilabhissanti"].replace(" sẽ không ", " sẽ ")), E.E_TE),
    "Ye puthujjanā maggaṃ na paṭilabhissanti te": (cap(E.E_YE["puthujjanā maggaṃ na paṭilabhissanti"]), E.E_TE),
}
EXCEPT_TAIL = " ṭhapetvā avasesā puggalā"
VAR_RE = re.compile(r" (\[[^\]]+\])")


def _acc(w):
    w = w.strip()
    if w in PERSON_ACC:
        return PERSON_ACC[w]
    raise ValueError(f"unparsed excluded person {w!r}")


def subject(s):
    """Pāli subject of an answer -> (Vietnamese head, resumptive or None)."""
    if s in REL_SUBJ:
        return REL_SUBJ[s]
    var = ""
    mm = VAR_RE.search(s)
    if mm:
        var = F.variant(mm[1])
        s = s[:mm.start()] + s[mm.end():]
        where = mm.start()
    if s.endswith(EXCEPT_TAIL):
        g = s[:-len(EXCEPT_TAIL)]
        m2 = re.fullmatch(r"(?P<a>.+?)(?:ñca| ca) (?P<b>\S+?)ñca", g)
        if m2:
            x = F.a_and(_acc(low(m2["a"]) if not m2["a"].endswith("maggasamaṅgino") else m2["a"]), _acc(m2["b"]))
        else:
            x = _acc(g)
        if var:
            assert where == len(g), s                   # the bracket follows the whole group
            x = f"{x} {var}"
        return cap(F.a_except_n(x, E.E_AVASESA)), None
    if var:
        num, rest = s[:where], s[where:].strip()
        if rest == "puggalā" and num in NUM_VI:          # Aṭṭha [satta (…)] puggalā = Tám [dị bản …] hạng người
            return f"{NUM_VI[num]} {var} {PUGGALA}", None
        if s in PERSON_NOM and where == len(s):          # Tayo maggasamaṅgino [tayo puggalā (pī.)]
            return f"{PERSON_NOM[s]} {var}", None
        raise ValueError(f"unparsed bracketed subject {s!r}")
    if s in PERSON_NOM:
        return PERSON_NOM[s], None
    raise ValueError(f"unparsed subject {s!r}")


def statement(subj, clause):
    head, res = subject(subj)
    if res:
        return cap(E.E_STATEMENT_RES.format(head=head, res=res, clause=clause))
    return cap(E.E_STATEMENT_PERSON.format(head=head, clause=clause))


# ================================================================ sentences
FAC_W = r"\S+ndriyaṃ"
Q_RE = re.compile(rf"\((?P<l>Ka|Kha)\) yo(?P<vp> vā pana)? (?P<x>{FAC_W}) (?P<v1>{V}) so (?P<y>{FAC_W}) (?P<v2>{V})\?")
BUT_RE = re.compile(rf"(?P<s>.+?) (?P<x>{FAC_W}) (?P<v1>{V}), no ca (?P<y>{FAC_W}) (?P<v2>{V})\.")
BOTH_RE = re.compile(rf"(?P<s>.+?) (?P<x>\S+ndriyañca) (?P<v1>{V}) (?P<y>\S+ndriyañca) (?P<v2>{V})\.")
MULAKA_RE = re.compile(r"\((?P<s>\S+ndriya)mūlakaṃ\)(?P<p>\.?)")


def mem(w):
    return I.m(w[:-3] + "ṃ" if w.endswith("ñca") else w)


EXACT = {
    "Āmantā.": S.AMANTA,                                              # Đúng vậy. (sample)
    "No.": F.NO,                                                      # Không. (7-01)
    **E.PARINNA_EXACT,                                                # Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
    "Indriyayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Indriyayamakaṃ"),      # Phần các cặp câu hỏi về các năng lực đã hoàn tất.
    "Yamakapakaraṇaṃ niṭṭhitaṃ.": S.BOOK_END,                         # Bộ “Các cặp câu hỏi” đã hoàn tất.
}


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s in EXACT:
        return EXACT[s]
    mm = MULAKA_RE.fullmatch(s)
    if mm:
        return A3.MULAKA.format(x=I.FACULTY_VI[low(mm["s"])]) + mm["p"]
    mm = Q_RE.fullmatch(s)
    if mm:
        vp = bool(mm["vp"])
        if vp != (mm["l"] == "Kha"):
            SLIPS.append(f"{ctx}: label ({mm['l']}) on a {'vā pana' if vp else 'non-vā pana'} question; kept")
        return E.e_q(I.m(mm["x"]), vparse(mm["v1"]), I.m(mm["y"]), vparse(mm["v2"]), label=mm["l"], vapana=vp)
    mm = BUT_RE.fullmatch(s)
    if mm:
        return statement(mm["s"], E.E_BUT_C.format(pa=E.e_pred(I.m(mm["x"]), vparse(mm["v1"])), dem="",
                                                   no=E.e_deny(I.m(mm["y"]), vparse(mm["v2"]))))
    mm = BOTH_RE.fullmatch(s)
    if mm:
        return statement(mm["s"], E.E_BOTH_C.format(pa=E.e_pred(mem(mm["x"]), vparse(mm["v1"])),
                                                    pb=E.e_pred(mem(mm["y"]), vparse(mm["v2"]))))
    raise ValueError(f"unmatched sentence {s!r} ({ctx})")


def split13(t):
    """F.split_sentences, plus a «(Xmūlakaṃ)» note after the last sentence as its own piece."""
    out = []
    for s in F.split_sentences(t):
        mm = re.fullmatch(r"(?P<a>.+[.?]) (?P<n>\(\S+mūlakaṃ\)\.?)", s.strip())
        out.extend([mm["a"], mm["n"]] if mm else [s])
    return out


# ================================================================ source slips (line level; each must apply once)
SLIP_FIX = [
    ("Dve puggalā aññindriyaṃ bhāvessanti no ca domanassindriyaṃ pajahissanti, pañca puggalā aññindriyañca "
     "bhavissanti domanassindriyañca pajahissanti.",
     "Dve puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti. Pañca puggalā aññindriyañca "
     "bhāvessanti domanassindriyañca pajahissanti.",
     "^6-10-452 (line 170): comma after «pajahissanti» instead of before «no ca»; «bhavissanti» = bhāvessanti "
     "(spelling); rendered as two sentences as in the parallel lines"),
    ("Cha puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca "
     "bhāvessanti, domanassindriyañca pajahanti.",
     "Cha puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahanti. Anāgāmimaggasamaṅgī aññindriyañca "
     "bhāvessanti domanassindriyañca pajahanti.",
     "^6-10-468 (line 313): no period before «anāgāmimaggasamaṅgi» (= Anāgāmimaggasamaṅgī), stray comma inside the "
     "«Xñca … Yñca …» clause; plural verbs with a singular subject (no difference in Vietnamese)"),
    ("(Kha) yo vā pana aññindriyaṃ bhāvessati. So anaññātaññassāmītindriyaṃ bhāvitthāti?",
     "(Kha) yo vā pana aññindriyaṃ bhāvessati so anaññātaññassāmītindriyaṃ bhāvitthāti?",
     "^6-10-477 (line 395): stray period inside the question («bhāvessati. So»); one question"),
    ("Dve puggalā aññindriyaṃ bhāvessanti no ca anaññātaññassāmītindriyaṃ bhāvittha.",
     "Dve puggalā aññindriyaṃ bhāvessanti, no ca anaññātaññassāmītindriyaṃ bhāvittha.",
     "^6-10-477 (line 396): comma before «no ca» missing"),
    ("yo domanassindriyaṃ nappajjahittha so", "yo domanassindriyaṃ nappajahittha so",
     "^6-10-480 (line 432): «nappajjahittha» = nappajahittha (spelling)"),
    ("anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.", "anaññātaññassāmītindriyaṃ na bhāvessatīti? Āmantā.",
     "^6-10-455 (line 191): the (Ka) question ends in «.»; written with «?»"),
    ("so cakkhundriyaṃ na parijānissatīti.", "so cakkhundriyaṃ na parijānissatīti?",
     "^6-10-455 (line 192): the (Kha) question ends in «.»; written with «?»"),
]
QMARK_WHITELIST = ("anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.",   # source lines (file lines 191, 192)
                   "so cakkhundriyaṃ na parijānissatīti.")                  # whose «?» count differs on purpose
STATIC_NOTES = [
    "^6-10-454 (line 184): «Aggamaggasamaṅgī … sacchikarissanti, no ca … bhāvessanti» plural verbs with a singular "
    "subject (no difference in Vietnamese)",
    "^6-10-459 (line 227): «Aggamaggasamaṅgī … pajahittha … parijānanti» plural verb (no difference in Vietnamese)",
    "^6-10-435 (lines 5-6): the cakkhundriya series opens with sotindriya «parijānāti» (Āmantā), as written",
]
SLIP_USED = {}


def fix_slips(t):
    for a, b, why in SLIP_FIX:
        if a in t:
            t = t.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return t


# ================================================================ lines and file
def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + F.heading(t) + sid
    t = fix_slips(t)
    return " ".join(translate_sentence(s, ctx) for s in split13(t) if s.strip()) + sid


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
    ("tự mình chứng nghiệm", 4), ("tự mình chứng nghiệm", 5), ("tu tập", 1), ("dứt bỏ", 1),
    ("hiểu biết trọn vẹn", 2), ("Năm hạng người", 4), ("Sáu hạng người", 4), ("Bảy hạng người", 4),
    ("Tám hạng người", 4), ("người thứ tám", 5), ("con đường không trở lại", 5), ("thành quả", 5),
    ("những người phàm phu", 4), ("có được con đường", 4), ("năng lực của người đã hiểu biết trọn vẹn", 2),
    ("năng lực biết được điều chưa từng biết", 2), ("năng lực nỗi buồn", 2), ("năng lực mắt", 2),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-13): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    o = "năng lực mắt"
    # pajahati / parijānāti: same triples as 5-03 / 2-02
    for v in ("pajahati", "nappajahati", "pajahittha", "nappajahittha", "pajahissati", "nappajahissanti",
              "parijānāti", "na parijānittha", "parijānissanti", "pajahatīti", "nappajahitthāti"):
        assert vparse(v) == T53.vparse(v), v
    # bhāveti present = 9-01 BH_VERB, byte for byte
    for v, k in (("bhāveti", "bhāveti"), ("na bhāveti", "na bhāveti")):
        assert E.e_pred(o, vparse(v)) == D9.BH_VERB[k]["p"].format(t=o)
        assert E.e_deny(o, vparse(v)) == D9.BH_VERB[k]["no"].format(t=o)
    assert E.e_pred(o, vparse("pajahati")) == A7.YO_VERB["pajahati"]["p"].format(t=o)
    assert E.e_deny(o, vparse("nappajahati")) == A7.YO_VERB["nappajahati"]["no"].format(t=o)
    # subjects shared with 2-02 / 7-04 / 7-06
    assert subject("Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā")[0] == \
        E.e_subject("Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā")[0]
    assert subject("Ye puthujjanā maggaṃ na paṭilabhissanti te") == \
        E.e_subject("Ye puthujjanā maggaṃ na paṭilabhissanti te")
    assert subject("Dve maggasamaṅgino ṭhapetvā avasesā puggalā")[0] == \
        N6.PERSON_NOM_VI["Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā"]
    assert subject("Anāgāmimaggasamaṅgī")[0] == N6.PERSON_NOM_VI["Anāgāmimaggasamaṅgī"]
    for k in ("Dve puggalā", "Tayo puggalā", "Cattāro puggalā", "Anāgāmī", "Arahā"):
        assert subject(k)[0] == C4.PERSON_NOM_VI[k], k
    # questions: family E with the 10-01 members
    assert translate_sentence("(Ka) yo cakkhundriyaṃ parijānāti so domanassindriyaṃ pajahatīti?") == \
        E.e_q("năng lực mắt", vparse("parijānāti"), "năng lực nỗi buồn", vparse("pajahati"))
    assert translate_sentence("(Cakkhundriyamūlakaṃ)") == "(Phần dựa trên năng lực mắt)"


def check_repeats(pali):
    seen, bad = {}, 0
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = fix_slips(re.sub(r"\s*\^[\w-]+$", "", ln))
        for s in split13(t):
            if not s.strip():
                continue
            v = translate_sentence(s)
            if seen.setdefault(s.strip(), v) != v:
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences")
    return bad


def main():
    S.check_cross_book()
    check_cross_book()
    check_frames()
    SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    pl = [x for x in pali.splitlines() if x.strip()]
    wl = {f"{NAME} line {n}: '?' count 0 vs 1" for n, x in enumerate(pl, 1)
          if any(p in x for p in QMARK_WHITELIST)}
    assert len(wl) == len(QMARK_WHITELIST) and all("?" not in x for x in pl if any(p in x for p in QMARK_WHITELIST))
    assert wl <= set(probs), (wl, probs[:5])
    probs = [p for p in probs if p not in wl]
    # the book close «Bộ “Các cặp câu hỏi” đã hoàn tất.» carries the title quotes the terms file prescribes
    nb = next(n for n, x in enumerate(pl, 1) if x.startswith("Yamakapakaraṇaṃ niṭṭhitaṃ."))
    q = f"{NAME} line {nb}: quotes pali (0, 0) vs vi (2, 0)"
    assert q in probs and S.BOOK_END in text, q
    probs.remove(q)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", "thì thì", "ndriya", "puggal", "ṭhapetvā"):
        assert bad not in re.sub(r" ?\[[^\]]*\]", "", text), repr(bad)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in list(used) + STATIC_NOTES + SLIPS:
        print("SLIP", why)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
