# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-10-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra
(5) paccuppannānāgatavāra: (Gha) paccanīkapuggalo, and the heading + «…pe…» line of (Ṅa) paccanīkaokāso).

Frames, imported and used VERBATIM:
  build_10-08_vi  (R8): translate_sentence() for every question (yassa / yattha, «…pe…» runs, «?…Pe….»), mūlaka
                  notes (through 10-04 / 10-02), _persons() / _moment() / SABBE / NIRODHA = the head8 element rule for
                  the attribute beings, the plane beings, pavatte and the citta moments (head8 checked);
  build_10-06_vi  (R6): S_NOT / S_BOTH (person answers with tesaṃ / tāsaṃ), _last_kind() «tâm cuối cùng gắn liền với
                  …», the «ye / yā (ca) …» clause regexes' word lists (AWITH / ACCP), head6 (checked);
  build_10-05_vi  (Y5): YE_FRAME, UPA_ATTR, BHAVA / BHAVA_AND, YE_NOUN, YE_ATTR, SAHA (ye_bhava / ye_attr checked);
  build_10-02_vi  (P): fm(), ATTR10, PARTICIPLE10, split10, heading, PAVATTE;
  build_2-01_vi   (F): b_not / b_both, vparse, PLANE / _plane_case, PARTICIPLE, HEAD, PACCHIMA, WHO_HEAD, LIST_SEP,
                  YE_UPAPAJJITVA;
  build_2-02_vi   (E): YE_CA_JOIN «… và …», YE_CA_CAVANTA «những người đang chết đi mà sau khi tái sinh vào …»;
  build_3-03_vi   (A33): YE_CA_UPAPAJJANTA «những người đang tái sinh mà sau khi tái sinh vào …», who33 (checked);
  build_3-01_vi   (A3): ATTR_GROUP / ATTR_JOIN;
  build_10-09_vi  (H9): _at() + ANANTARA_REL «vào khoảnh khắc … của tâm mà ngay sau đó {c} sẽ sinh khởi» (same Pāli,
                  same run), head9 (checked);
  build_10-12_vi  (H12): translate_sentence (checked; coordinator frame «ye ca upekkhāya … parinibbāyissanti»);
  build_6-01_vi   (X6): ANANTARA (asserted);
  build_8_vi      (C8): SAMANGI «những người có được {c}», citta(last=True), AT / OF / MOMENT, P_SUBJ (checked);
  labels from build_sample_vi.LABEL.
New here (notes-10-10.md): YE_PART (a «ye / yā ca …» clause closed by «tesaṃ cavantānaṃ / tesaṃ upapajjantānaṃ /
tāsaṃ upapajjantīnaṃ», 2-02 YE_CA_CAVANTA / 3-03 YE_CA_UPAPAJJANTA generalised to every clause kind and to the
nouns người nam / người nữ), «ye purisā / yā itthiyo upekkhāya … upapajjitvā», «yā itthiyo <planes> upapajjitvā»,
«pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ», «yassa cittassa anantarā <K>pacchimacittaṃ uppajjissati tassa cittassa
<moment>», «<K>pacchimacittassa <moment>», «<K>pacchimacittasamaṅgīnaṃ», and the answer-head rule head10x().

Importing writes nothing; run  python -I -X utf8 -B build_10-10_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

R8 = importlib.import_module("build_10-08_vi")   # questions, head8 element rule
R6 = importlib.import_module("build_10-06_vi")   # person-answer regexes, last-citta kinds, head6
Y5 = importlib.import_module("build_10-05_vi")   # «ye …» clause pieces
R = R8.R                                          # build_10-04_vi
P = R8.P                                          # build_10-02_vi
F = R8.F                                          # build_2-01_vi
I = R8.I                                          # build_10-01_vi
A3 = R8.A3                                        # build_3-01_vi
T5 = R8.T5                                        # build_5-01_vi
C8 = R8.C8                                        # build_8_vi
E = R6.E                                          # build_2-02_vi
X6 = R6.X6                                        # build_6-01_vi
A33 = importlib.import_module("build_3-03_vi")    # YE_CA_UPAPAJJANTA, who33
H9 = importlib.import_module("build_10-09_vi")    # anantarā … tassa cittassa <moment> (same Pāli), head9 (checked)
H12 = importlib.import_module("build_10-12_vi")   # «ye ca upekkhāya … parinibbāyissanti» (coordinator; checked)

NAME = "10-10-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = F.WHO_HEAD.format(g="")                      # «ở »

# ================================================================ the «ye / yā (ca) …» clauses
YE_FRAME = Y5.YE_FRAME                            # «những {n} nào sau khi {what} sẽ nhập Niết-bàn trọn vẹn» (10-05)
YE_PART = YE_FRAME.replace("{n} nào", "{n} {part} mà")
# … ye ca <clause> tesaṃ cavantānaṃ / upapajjantānaṃ = «những <n> đang chết đi / đang tái sinh mà sau khi …» (new:
# 2-02 YE_CA_CAVANTA and 3-03 YE_CA_UPAPAJJANTA, generalised to every clause kind; asserted below)
assert YE_PART != YE_FRAME
assert YE_PART.format(n="người", part=F.PARTICIPLE["cavantānaṃ"][0], what="tái sinh vào {p}") == E.YE_CA_CAVANTA
assert YE_PART.format(n="người", part=F.PARTICIPLE["upapajjantānaṃ"][0], what="tái sinh vào {p}") == \
    A33.YE_CA_UPAPAJJANTA
UPA_PLANE = "tái sinh vào {p}"                    # <planes> upapajjitvā (2-01 YE_UPAPAJJITVA)
assert YE_FRAME.format(n="người", what=UPA_PLANE) == F.YE_UPAPAJJITVA
NOUN_PERSON = "người"                             # bare ye = những người (2-01)
AWITH = r"(?:upekkhāya|somanassena)"
ACCP = r"(?:rūpāvacaraṃ|arūpāvacaraṃ|arūpaṃ|kāmāvacaraṃ|pañcavokāraṃ)"
REL = r"(?P<rel>ye ca|yā ca|ye|yā)"
NOUN = r"(?P<n>purisā|itthiyo)"
YE_CLAUSE = re.compile(
    rf"{REL} (?:"
    rf"{NOUN} eteneva bhāvena katici bhave dassetvā (?:(?P<a>{AWITH}) upapajjitvā )?parinibbāyissanti"
    rf"|(?P<h>sacakkhukā|saghānakā) (?P<ha>{AWITH}) upapajjitvā parinibbāyissanti"
    rf"|(?:(?P<n2>purisā|itthiyo) )?(?P<a2>{AWITH}) upapajjitvā parinibbāyissanti"
    rf"|(?:(?P<n3>purisā|itthiyo) )?(?P<pl>{ACCP}(?: {ACCP})*) upapajjitvā parinibbāyissanti"
    rf")(?= |$)")
YE_TAIL = re.compile(r"(?P<r>tesaṃ|tāsaṃ) (?P<p>cavantānaṃ|upapajjantānaṃ|upapajjantīnaṃ)(?= |$)")


def _planes(s):
    out = []
    for w in s.split():
        case, stem = F._plane_case(w)
        assert case == "acc", s
        out.append(F.PLANE[stem])
    return F.LIST_SEP.join(out)


def _clause(mm):
    """One «ye / yā (ca) …» clause -> (noun, what) of YE_FRAME / YE_PART."""
    g = mm.groupdict()
    noun = g["n"] or g["n2"] or g["n3"]
    if noun:
        assert mm["rel"].startswith("yā") == (noun == "itthiyo"), mm[0]
    else:
        assert mm["rel"].startswith("ye"), mm[0]
    n = Y5.YE_NOUN[noun] if noun else NOUN_PERSON
    if g["n"]:                                                       # eteneva bhāvena … (10-05 ye_bhava)
        what = Y5.BHAVA if not g["a"] else Y5.BHAVA_AND.format(b=Y5.BHAVA, u=Y5.UPA_ATTR.format(a=Y5.SAHA[g["a"]]))
    elif g["h"]:                                                     # sacakkhukā upekkhāya … (10-05 ye_attr)
        what = Y5.UPA_ATTR.format(a=A3.ATTR_JOIN.join([Y5.YE_ATTR[g["h"]], Y5.SAHA[g["ha"]]]))
    elif g["a2"]:                                                    # (purisā) upekkhāya upapajjitvā … (new)
        what = Y5.UPA_ATTR.format(a=Y5.SAHA[g["a2"]])
    else:                                                            # (itthiyo) <planes> upapajjitvā … (2-01)
        what = UPA_PLANE.format(p=_planes(g["pl"]))
    return n, what


def ye_vi(clauses, tail=None):
    """[(noun, what, has_ca)], tail participle (or None) -> [(vi, has_ca)]."""
    out = []
    for n, what, ca in clauses:
        if tail:
            out.append((YE_PART.format(n=n, part=F.PARTICIPLE[P.PARTICIPLE10.get(tail, tail)][0], what=what), ca))
        else:
            out.append((YE_FRAME.format(n=n, what=what), ca))
    return out


# ================================================================ last citta, anantarā
LAST = C8.citta(last=True)                         # «tâm cuối cùng» (8)
TASSA_CITTASSA = T5.NOUN_OF["tassa cittassa"]      # «tâm ấy» (5-01)


def last_kind(k):
    """'' -> «tâm cuối cùng»; upekkhāsampayutta -> «tâm cuối cùng gắn liền với sự bình thản» (10-06 / 10-05)."""
    return R6._last_kind(k) if k else LAST


def last_moment(k, mo):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[mo], c=last_kind(k)))


SPECIAL = [   # (regex at the current position, function -> list of (kind, vi, has_ca))
    (re.compile(r"yassa cittassa anantarā (?P<k>\S+?)pacchimacittaṃ uppajjissati tassa cittassa "
                r"(?P<mo>uppāda|bhaṅga)kkhaṇe(?= |$)"),
     lambda m: [("T", H9._at(m["mo"], H9.ANANTARA_REL.format(c=R6._last_kind(m["k"]))), False)]),
    # = 10-09 (same Pāli, same run): «vào khoảnh khắc tan rã của tâm mà ngay sau đó <tâm cuối cùng K> sẽ sinh khởi»
    # (6-01 ANANTARA relative under the 8 moment; «tassa cittassa <moment>» is its correlative)
    (re.compile(r"(?P<k>\S*?)pacchimacittassa (?P<mo>uppāda|bhaṅga)kkhaṇe(?= |$)"),
     lambda m: [("T", last_moment(m["k"], m["mo"]), False)]),
    (re.compile(r"(?P<k>\S*?)pacchimacittasamaṅgīnaṃ(?= |$)"),
     lambda m: [("P", C8.SAMANGI.format(c=last_kind(m["k"])), False)]),
    (re.compile(r"pacchimabhavikānaṃ (?P<a>itthīnaṃ|purisānaṃ) (?P<p>upapajjantīnaṃ|upapajjantānaṃ)(?= |$)"),
     lambda m: [("P", A3.ATTR_GROUP.format(h=f"{F.HEAD[None]} {F.PACCHIMA}",
                                           p=F.PARTICIPLE[P.PARTICIPLE10[m["p"]]][0], a=P.ATTR10[m["a"]]), False)]),
]


def _els8(w):
    """The head8 element rule (10-08) over a word list -> [(kind, vi)] (persons without «ở»)."""
    els, i, n = [], 0, len(w)
    while i < n:
        x = w[i]
        if x == "pavatte":
            els.append(("T", P.PAVATTE)); i += 1
        elif x.endswith("cittassa"):
            els.append(("T", R8._moment(x, w[i + 1]))); i += 2
        elif x == "nirodhasamāpannānaṃ":
            els.append(("P", R8.NIRODHA)); i += 1
        elif x == "sabbesaṃ" and (i + 1 == n or w[i + 1] == "pavatte" or w[i + 1].endswith("cittassa")):
            els.append(("P", R8.SABBE)); i += 1
        else:
            j = i
            while j < n and w[j] != "pavatte" and not w[j].endswith("cittassa") and w[j] != "nirodhasamāpannānaṃ":
                j += 1
            els.extend(("P", t) for t in R8._persons(w[i:j]))
            i = j
    return els


def head10x(g, ctx=""):
    """Pāli answer head (before the resumptive tesaṃ / tāsaṃ) -> Vietnamese head, capitalised.
    T (time) stands alone; P (genitive persons) take «ở» unless they follow other persons (2-01 WHO_HEAD / LIST_SEP);
    a «ye / yā ca …» clause joins the piece before it with « và » (2-02 YE_CA_JOIN), a sentence-initial «ye …» has no
    «ở» (2-01); a «tesaṃ cavantānaṃ / upapajjantānaṃ» closing the «ye» clauses goes into each of them (YE_PART);
    everything else goes through the 10-08 head8 element rule; pieces joined «, » (= 10-06 head6, 10-08 head8)."""
    p = low(g)
    pos, buf, els = 0, [], []

    def flush():
        if buf:
            els.extend((k, v, False) for k, v in _els8(buf))
            buf.clear()

    while pos < len(p):
        for rx, fn in SPECIAL:
            mm = rx.match(p, pos)
            if mm:
                flush()
                els.extend(fn(mm))
                pos = mm.end() + 1
                break
        else:
            mm = YE_CLAUSE.match(p, pos)
            if mm:
                flush()
                clauses = []
                while mm:
                    n, what = _clause(mm)
                    clauses.append((n, what, mm["rel"].endswith(" ca")))
                    pos = mm.end() + 1
                    mm = YE_CLAUSE.match(p, pos)
                tm = YE_TAIL.match(p, pos)
                tail = None
                if tm:
                    assert (tm["r"] == "tāsaṃ") == (tm["p"] == "upapajjantīnaṃ"), g
                    tail = tm["p"]
                    pos = tm.end() + 1
                els.extend(("Y", vi, ca) for vi, ca in ye_vi(clauses, tail))
                continue
            sp = p.find(" ", pos)
            sp = len(p) if sp < 0 else sp
            buf.append(p[pos:sp])
            pos = sp + 1
    flush()
    pieces = []                                    # [kind, text]
    for kind, vi, ca in els:
        if kind == "Y" and ca:
            assert pieces, g
            pieces[-1][1] += E.YE_CA_JOIN + vi
            continue
        if kind == "Y":
            assert not pieces, g
        if kind == "P" and not (pieces and pieces[-1][0] == "P"):
            vi = OI + vi
            pieces.append(["P", vi])
        elif kind == "P":
            pieces[-1][1] += F.LIST_SEP + vi
        else:
            pieces.append([kind, vi])
    return cap(F.LIST_SEP.join(t for _, t in pieces))


# ================================================================ sentences
S_NOT, S_BOTH = R6.S_NOT, R6.S_BOTH


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s.endswith(".") and (" tesaṃ " in s or " tāsaṃ " in s):
        body = s[:-1]
        for rx, both in ((S_NOT, False), (S_BOTH, True)):
            mm = rx.fullmatch(body)
            if not mm:
                continue
            if not both:
                assert mm["r"] == mm["r2"] and bool(mm["t"]) == bool(mm["t2"]), s
            if mm["r"] == "tāsaṃ":
                assert "upapajjantīnaṃ" in mm["g"], s
            res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
            f = F.b_both if both else F.b_not
            return f(res, head10x(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
        raise ValueError(f"unmatched person answer: {s!r} ({ctx})")
    return R8.translate_sentence(s, ctx)          # questions, «?…Pe….», mūlaka notes (10-08 / 10-04 / 10-02)


SLIP_FIX = [   # (Pāli as written, as read, report); each applies once
    ("tesaṃ itthindriyaṃ na uppajjissanti, no ca", "tesaṃ itthindriyaṃ na uppajjissati, no ca",
     "^6-10-385 (line 14): «itthindriyaṃ na uppajjissanti» (plural verb with a singular subject) read as "
     "«na uppajjissati», as in the parallel rows"),
    ("tesaṃ itthindriyaṃ na uppajjati no ca tesaṃ upekkhindriyaṃ", "tesaṃ itthindriyaṃ na uppajjati, no ca tesaṃ "
     "upekkhindriyaṃ", "^6-10-387 (line 74): comma missing before «no ca»; written"),
    ("no ca tesaṃ manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca",
     "no ca tesaṃ manindriyaṃ na uppajjissati. Pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca",
     "^6-10-393 (line 133): full stop missing between the two answer sentences; written"),
]
SLIP_USED = {}


def fix_slips(t, count=True):
    for a, b, why in SLIP_FIX:
        if a in t:
            t = t.replace(a, b)
            if count:
                SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return t


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
    t = fix_slips(t)
    return " ".join(translate_sentence(x, ctx) for x in P.split10(t) if x.strip()) + sid


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
    ("nhập Niết-bàn trọn vẹn", 5), ("ngay sau", 5), ("gắn liền với", 1), ("người nam", 2), ("người nữ", 2),
    ("chúng sinh Vô Tưởng", 5), ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("tái sinh", 2), ("chết đi", 2),
    ("thành tựu thiền chấm dứt", 5), ("một số", 2), ("sau khi", 2),
]


def check_cross_book():
    texts = {b: "\n".join(x.read_text(encoding="utf-8") for x in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-10): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    g = "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ"
    assert head10x(g) == cap(A33.who33(g)), (head10x(g), A33.who33(g))                       # 3-03 / 2-02
    g = ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti "
         "tesaṃ upapajjantānaṃ")
    assert head10x(g) == cap(A33.who33(g)), (head10x(g), A33.who33(g))                       # 3-03
    g = "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti"
    assert head10x(g) == cap(E.who2(g)), (head10x(g), E.who2(g))                             # 2-02
    for g in ("Pacchimacittassa uppādakkhaṇe", "Pacchimacittassa bhaṅgakkhaṇe", "Pacchimacittasamaṅgīnaṃ"):
        assert head10x(g) == cap(C8.P_SUBJ[g]), (head10x(g), C8.P_SUBJ[g])                    # 8
    for g in ("Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
              "Yā itthiyo eteneva bhāvena katici bhave dassetvā upekkhāya upapajjitvā parinibbāyissanti",
              "Ye sacakkhukā somanassena upapajjitvā parinibbāyissanti",
              "Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti"):
        assert head10x(g) == R6.head6(g), (head10x(g), R6.head6(g))                            # 10-06 / 10-05
    assert head10x("Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti") == cap(Y5.ye_bhava("purisā"))
    assert head10x("Ye saghānakā upekkhāya upapajjitvā parinibbāyissanti") == cap(Y5.ye_attr("saghānakā", "upekkhāya"))
    # coordinator (from 10-12): «ye ca upekkhāya / somanassena upapajjitvā parinibbāyissanti» without a closing
    # «tesaṃ <participle>» = «và những người nào sau khi tái sinh có sự bình thản / niềm vui đi kèm sẽ nhập …»
    for a, x in (("upekkhāya", "sự bình thản"), ("somanassena", "niềm vui")):
        h = head10x(f"Rūpāvacarānaṃ ye ca {a} upapajjitvā parinibbāyissanti")
        assert h.endswith(f" và những người nào sau khi tái sinh có {x} đi kèm sẽ nhập Niết-bàn trọn vẹn"), h
    g = "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ"
    assert head10x(g) == H9.head9(g) == "Ở những người thuộc kiếp sống cuối cùng đang tái sinh là người nữ", g
    g = "Pacchimacittassa bhaṅgakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati " \
        "tassa cittassa bhaṅgakkhaṇe"
    assert head10x(g) == ("Vào khoảnh khắc tan rã của tâm cuối cùng, vào khoảnh khắc tan rã của tâm mà ngay sau đó "
                          "tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi"), head10x(g)
    assert X6.ANANTARA == "vào tâm mà ngay sau đó {c} sẽ sinh khởi"
    assert TASSA_CITTASSA == "tâm ấy" and T5._moment("bhaṅga", TASSA_CITTASSA) == "vào khoảnh khắc tan rã của tâm ấy"
    assert last_kind("somanassasampayutta") == Y5.last_citta("somanassasampayutta")
    assert P.ATTR10["itthīnaṃ"] == "là người nữ" and P.ATTR10["purisānaṃ"] == "là người nam"
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Gha"] == "(d)" and S.LABEL["Ṅa"] == "(đ)"


KNOWN_DIFF = re.compile(r"[Pp]acchimabhavikānaṃ (?:itthīnaṃ|purisānaṃ) upapajjant")
# «Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ»: no earlier chapter has it; 10-08 head8 would split it into two groups
# («những người thuộc kiếp sống cuối cùng, những người đang tái sinh là người nữ»); here one group as 2-01 who()
# renders «Pacchimabhavikānaṃ <plane>ṃ upapajjantānaṃ» («những người thuộc kiếp sống cuối cùng đang tái sinh …»).


def check_parallel(pali):
    """Every sentence the sibling Indriya parsers translate, and every head that head8 / head6 / head5 / who33 parse,
    comes out byte-identical here."""
    mods = [("10-09", H9), ("10-12", H12), ("10-08", R8), ("10-06", R6), ("10-05", Y5), ("10-04", R), ("10-02", P)]
    heads = [("head9", H9.head9), ("head8", R8.head8), ("head6", R6.head6), ("head5", Y5.head5),
             ("who33", A33.who33), ("head4", R.head4), ("head10", P.head10)]
    probs, n = [], {"known": 0}
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = fix_slips(re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln), count=False)
        for s in P.split10(t):
            s = s.strip()
            if not s:
                continue
            mine = translate_sentence(s, "check")
            known = bool(KNOWN_DIFF.search(s))
            if known:
                n["known"] += 1                    # head8 reads it as two groups; one group here (= 10-09)
            for tag, mod in mods:
                if known and tag not in ("10-09", "10-12"):
                    continue
                try:
                    theirs = mod.translate_sentence(s, "check")
                except (AssertionError, ValueError, KeyError, TypeError, IndexError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if theirs != mine:
                    probs.append(f"differs from {tag}: {s[:70]} | {theirs} | {mine}")
            mm = (S_NOT.fullmatch(s[:-1]) or S_BOTH.fullmatch(s[:-1])) if s.endswith(".") else None
            if not mm:
                continue
            g, h = mm["g"], head10x(mm["g"], "check")
            for tag, fn in heads:
                if known and tag != "head9":
                    continue
                try:
                    o = cap(fn(g))
                except (AssertionError, ValueError, KeyError, TypeError, IndexError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if o != h:
                    probs.append(f"head differs from {tag}: {g} | {o} | {h}")
    for mod in (R8, R6, Y5, R, P, F, A33):
        if hasattr(mod, "SLIPS"):
            del mod.SLIPS[:]
    del SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    return probs


RUNNING = set()        # chapters still being written at the same time (none left when this chapter was finished)


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in another written pi-6 chapter has the same Vietnamese
    (10-09 runs at the same time: a difference there is a warning)."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs, warn = [], []
    for vp in sorted(S.OUT_DIR.glob("*.md")):
        nm = vp.name
        if nm == NAME or nm == "preamble.md":
            continue
        pp = S.PALI_DIR / nm
        if not pp.exists():
            continue
        p1 = pp.read_text(encoding="utf-8").splitlines()
        v1 = vp.read_text(encoding="utf-8").splitlines()
        if len(p1) != len(v1):
            print(f"note: {nm} line count differs from its Pāli; not compared")
            continue
        ref = {strip(a): strip(b) for a, b in zip(p1, v1) if a.strip()}
        k = 0
        for a, b in zip(pali.splitlines(), text.splitlines()):
            if a.strip() and strip(a) in ref:
                k += 1
                if ref[strip(a)] != strip(b):
                    (warn if nm in RUNNING else probs).append(f"differs from {nm}: {a[:70]}")
        if k:
            print(f"lines shared with {nm} checked: {k}")
    for w in warn:
        print("WARN", w)
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    I.check_cross_book()
    P.check_cross_book()
    check_cross_book()
    check_frames()
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    pprobs = check_parallel(pali)
    SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for a, b, why in SLIP_FIX:
        if SLIP_USED.get(why) != 1:
            probs.append(f"slip fix used {SLIP_USED.get(why)} times: {why}")
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì", "cittassa",
                    "là không phải", "ndriya", "….", "  ", "là là", "ānaṃ", "īnaṃ", "Āmantā", "eteneva", "bhāv",
                    "anantarā", "pacchima", "parinibb", " ye ", " yā ", "itthiyo", "purisā", "sẽ sẽ", "và và",
                    "samaṅg", "Sabbesaṃ", "sabbesaṃ", "Natthi", "Pe…", "mà mà", "nào nào"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in SLIP_USED:
        print("SLIP", why)
    seen = set()
    for c, w in SLIPS + R8.SLIPS + R6.SLIPS + R.SLIPS + P.SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
