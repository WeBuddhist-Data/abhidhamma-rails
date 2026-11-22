# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-11-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra,
(5) paccuppannānāgatavāra: (Ca) paccanīkapuggalokāsā, «yassa yattha X na uppajjati tassa tattha Y na uppajjissati»).

Frames, imported and used VERBATIM:
  build_10-04_vi  (R): translate_sentence() for every «yassa yattha» question (with «…pe…» runs), the mūlaka notes
                  (through build_10-02_vi), the answer regexes P4_NOT / P4_BOTH;
  build_10-08_vi  (H8): _persons() / _moment() (attribute beings of 10-02 with and without a plane, «itaresaṃ»,
                  genitive plane beings through 2-01 who(), «<kind>cittassa uppāda/bhaṅgakkhaṇe»), the head8 rule;
  build_10-07_vi  (H7): head7 rule (one «ở» over a run of persons, a time phrase alone, «ye ca» joined « và »);
  build_10-05_vi  (Y5): YE_FRAME, BHAVA, UPA_ATTR, YE_NOUN, YE_ATTR, SAHA, ye_bhava(), ye_attr(), last_citta();
  build_10-02_vi  (P): fm(), ATTR10, PAVATTE, split10, heading;
  build_2-01_vi   (F): b_not / b_both, vparse, who(), HEAD, PACCHIMA, PARTICIPLE, WHO_HEAD, LIST_SEP;
  build_2-02_vi   (E): YE_CA_CAVANTA, YE_CA_JOIN;   build_3-03_vi (A33): YE_CA_UPAPAJJANTA;
  build_3-01_vi   (A3): ATTR, ATTR_GROUP, ATTR_JOIN;
  build_5-01_vi   (T5): SABBESAM_ALONE (bare Sabbesaṃ = tất cả chúng sinh);
  build_6-01_vi   (X6): ANANTARA «vào tâm mà ngay sau đó {c} sẽ sinh khởi»;
  build_8_vi      (C8): AT / OF / MOMENT, when(…, last=True), SAMANGI, citta(last=True);
  labels from build_sample_vi.LABEL.
New here (notes-10-11.md): «ye ca / yā ca … parinibbāyissanti tesaṃ cavantānaṃ / upapajjantānaṃ, tāsaṃ cavantīnaṃ /
upapajjantīnaṃ» with the 10-05 clauses (YE_PART = 2-02 YE_CA_CAVANTA / 3-03 YE_CA_UPAPAJJANTA shape), «ye ca [purisā /
itthiyo] upekkhāya upapajjitvā …», «pacchimabhavikānaṃ <attribute> upapajjantānaṃ», «yassa cittassa anantarā …
uppajjissati tassa cittassa <moment>», «<kind>pacchimacittassa <moment>», «<kind>pacchimacittasamaṅgīnaṃ».

Importing writes nothing; run  python -I -X utf8 -B build_10-11_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # family B
E = importlib.import_module("build_2-02_vi")     # ye ca join, YE_CA_CAVANTA
I = importlib.import_module("build_10-01_vi")    # faculty table, check_extra
P = importlib.import_module("build_10-02_vi")    # Indriya pavatti frames
R = importlib.import_module("build_10-04_vi")    # yassa yattha questions, answer regexes
Y5 = importlib.import_module("build_10-05_vi")   # future «ye …» clauses, last_citta
H7 = importlib.import_module("build_10-07_vi")   # head7 (future paccanīkapuggalokāsā)
H8 = importlib.import_module("build_10-08_vi")   # head8 (mixed-tense paccanīkapuggalokāsā)
A3 = importlib.import_module("build_3-01_vi")    # attribute words / groups
A33 = importlib.import_module("build_3-03_vi")   # YE_CA_UPAPAJJANTA
T5 = importlib.import_module("build_5-01_vi")    # bare sabbesaṃ
X6 = importlib.import_module("build_6-01_vi")    # ANANTARA
C8 = importlib.import_module("build_8_vi")       # moments, samaṅgī, last citta

NAME = "10-11-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = F.WHO_HEAD.format(g="")                      # «ở »
assert OI == R.OI == H8.OI == H7.OI

# ================================================================ «ye ca …» clauses with a participle (new)
YE_PART = "những {n} {part} mà sau khi {what} sẽ nhập Niết-bàn trọn vẹn"
# ye ca … parinibbāyissanti tesaṃ cavantānaṃ / upapajjantānaṃ: 2-02 YE_CA_CAVANTA / 3-03 YE_CA_UPAPAJJANTA shape
assert YE_PART.format(n="người", part=F.PARTICIPLE["cavantānaṃ"][0], what="tái sinh vào {p}") == E.YE_CA_CAVANTA
assert YE_PART.format(n="người", part=F.PARTICIPLE["upapajjantānaṃ"][0], what="tái sinh vào {p}") == \
    A33.YE_CA_UPAPAJJANTA
assert Y5.YE_FRAME == "những {n} nào sau khi {what} sẽ nhập Niết-bàn trọn vẹn"
PART_OF = {"cavantānaṃ": "cavantānaṃ", "cavantīnaṃ": "cavantānaṃ", "upapajjantānaṃ": "upapajjantānaṃ",
           "upapajjantīnaṃ": "upapajjantānaṃ"}    # feminine = same Vietnamese (10-02 PARTICIPLE10)


def ye_clause(n, h, bh, s, part):
    """One «ye ca / yā ca …» clause -> Vietnamese (10-05 pieces; with a participle in the 2-02 / 3-03 shape)."""
    noun = Y5.YE_NOUN[n] if n else "người"
    if bh:
        assert n and not h, (n, h, bh, s)
        what = Y5.BHAVA if not s else Y5.BHAVA_AND.format(b=Y5.BHAVA, u=Y5.UPA_ATTR.format(a=Y5.SAHA[s]))
    else:
        assert s and not (n and h), (n, h, bh, s)
        attrs = ([Y5.YE_ATTR[h]] if h else []) + [Y5.SAHA[s]]
        what = Y5.UPA_ATTR.format(a=A3.ATTR_JOIN.join(attrs))
    if part:
        return YE_PART.format(n=noun, part=F.PARTICIPLE[PART_OF[part]][0], what=what)
    return Y5.YE_FRAME.format(n=noun, what=what)


# ================================================================ time phrases and persons (new pieces)
assert C8.AT == "vào {x}" and X6.ANANTARA.startswith("vào ")
ANANTARA_CITTA = X6.ANANTARA[len("vào "):]          # «tâm mà ngay sau đó {c} sẽ sinh khởi» (6-01)
assert C8.AT.format(x=ANANTARA_CITTA) == X6.ANANTARA


def last_kind(k):
    """'' -> «tâm cuối cùng»; upekkhāsampayutta -> «tâm cuối cùng gắn liền với sự bình thản» (10-05 last_citta)."""
    return C8.citta(last=True) if not k else Y5.last_citta(k)


def at_moment(mo, c):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[mo], c=c))   # vào khoảnh khắc <mo> của <c> (8)


PACCHIMA_ATTR_H = F.HEAD[None] + " " + F.PACCHIMA  # «những người thuộc kiếp sống cuối cùng» (2-01 who)
PACCHIMA_ATTR = {"itthīnaṃ", "purisānaṃ", "saghānakānaṃ", "sacakkhukānaṃ"}


def _pacchima_attr(m):
    """Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ = những người thuộc kiếp sống cuối cùng đang tái sinh là người nữ
    (2-01 who «… thuộc kiếp sống cuối cùng đang tái sinh vào …» with the 10-02 / 3-01 attribute group order)."""
    return A3.ATTR_GROUP.format(h=PACCHIMA_ATTR_H, p=F.PARTICIPLE[PART_OF[m["p"]]][0], a=P.ATTR10[m["a"]])


YE_RE = (r"(?P<rel>ye ca|yā ca) (?:(?P<n>purisā|itthiyo) )?(?:(?P<h>sacakkhukā|saghānakā) )?"
         r"(?:(?P<bh>eteneva bhāvena katici bhave dassetvā) )?(?:(?P<s>upekkhāya|somanassena) upapajjitvā )?"
         r"parinibbāyissanti(?: (?P<r>tesaṃ|tāsaṃ) (?P<pt>cavantānaṃ|cavantīnaṃ|upapajjantānaṃ|upapajjantīnaṃ))?")


def _ye(m):
    if m["rel"] == "yā ca":
        assert m["n"] == "itthiyo", m[0]
    if m["r"] == "tāsaṃ":
        assert m["n"] == "itthiyo" and m["pt"].endswith("īnaṃ"), m[0]
    return ye_clause(m["n"], m["h"], m["bh"], m["s"], m["pt"])


ELEMENTS = [   # (regex at the current position, kind, function); T time (alone), P person (one «ở»), Y «ye ca»
    (r"yassa cittassa anantarā (?P<k>\S+?)pacchimacittaṃ uppajjissati tassa cittassa (?P<mo>uppāda|bhaṅga)kkhaṇe",
     "T", lambda m: at_moment(m["mo"], ANANTARA_CITTA.format(c=last_kind(m["k"])))),
    (r"(?P<k>\S*?)pacchimacittassa (?P<mo>uppāda|bhaṅga)kkhaṇe", "T",
     lambda m: at_moment(m["mo"], last_kind(m["k"]))),
    (r"(?P<k>\S*?cittassa) (?P<mo>(?:uppāda|bhaṅga)kkhaṇe)", "T", lambda m: H8._moment(m["k"], m["mo"])),
    (r"pavatte", "T", lambda m: P.PAVATTE),
    (r"(?P<k>\S*?)pacchimacittasamaṅgīnaṃ", "P", lambda m: C8.SAMANGI.format(c=last_kind(m["k"]))),
    (r"sabbesaṃ(?= (?:pavatte|\S*cittassa) )", "P", lambda m: T5.SABBESAM_ALONE),
    (r"pacchimabhavikānaṃ (?P<a>" + "|".join(sorted(PACCHIMA_ATTR)) + r") (?P<p>upapajjantānaṃ|upapajjantīnaṃ)", "P",
     _pacchima_attr),
    (YE_RE, "Y", _ye),
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]


def head11(g):
    """Pāli answer head (before tesaṃ / tāsaṃ tattha) -> Vietnamese head, capitalised. Every other stretch of person
    words goes through 10-08 _persons(); consecutive persons share one «ở» (2-01 / 10-07 / 10-08), a time phrase stands
    alone, «ye ca …» joins the person before it with « và » (2-02); pieces joined «, »."""
    p, i, pieces, buf = low(g), 0, [], []        # pieces: [kind, [texts]]

    def add(kind, vi):
        if kind == "P" and pieces and pieces[-1][0] == "P":
            pieces[-1][1].append(vi)
        elif kind == "Y":
            assert pieces and pieces[-1][0] == "P", g
            pieces[-1][1][-1] += E.YE_CA_JOIN + vi
        else:
            pieces.append([kind, [vi]])

    def flush():
        if buf:
            for grp in H8._persons(buf):
                add("P", grp)
            buf.clear()

    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            mm = rx.match(p, i)
            if mm:
                flush()
                add(kind, fn(mm))
                i = mm.end() + 1
                break
        else:
            j = p.find(" ", i)
            j = len(p) if j < 0 else j
            buf.append(p[i:j])
            i = j + 1
    flush()
    out = [OI + F.LIST_SEP.join(v) if k == "P" else v[0] for k, v in pieces]
    return cap(F.LIST_SEP.join(out))


# ================================================================ sentences
def translate_sentence(s, ctx=""):
    s = s.strip()
    if s.endswith("."):
        body = s[:-1]
        for rx, both in ((R.P4_NOT, False), (R.P4_BOTH, True)):
            mm = rx.fullmatch(body)
            if not mm:
                continue
            if not both:
                assert mm["r"] == mm["r2"], s
            if mm["r"] == "tāsaṃ":                      # feminine resumptive = same Vietnamese (10-02)
                assert "upapajjantīnaṃ" in mm["g"] or "itthiyo" in mm["g"], s
            f = F.b_both if both else F.b_not
            return f("tesaṃ tattha", head11(mm["g"]), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return R.translate_sentence(s, ctx)                  # questions, mūlaka notes (10-04 / 10-02)


SLIP_FIX = [   # (Pāli as written, as read, report)
    ("Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ", "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ",
     "«purisānaṃ uppajjantānaṃ» (uppajjati «arise» for upapajjati «be reborn»; every parallel has upapajjantānaṃ) "
     "read as «purisānaṃ upapajjantānaṃ»"),
]


def fix_slips(t, ctx=""):
    for a, b, why in SLIP_FIX:
        if a in t:
            SLIPS.append((ctx, why))
            t = t.replace(a, b)
    return t


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
    t = fix_slips(t, ctx)
    return " ".join(translate_sentence(x, ctx) for x in P.split10(t) if x.strip()) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for k, ln in enumerate(src.splitlines(), 1):
        out.append(translate_line(ln, f"line {k} (segment after ^{seg})") if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("người nam", 2), ("người nữ", 2), ("có mắt", 4), ("sau khi tái sinh", 4), ("nhập Niết-bàn trọn vẹn", 5),
    ("gắn liền với sự bình thản", 1), ("gắn liền với niềm vui", 2), ("không gắn liền với", 1), ("ngay sau", 5),
    ("khoảnh khắc tan rã", 5), ("tất cả chúng sinh", 2), ("đời sống", 1), ("chúng sinh Vô Tưởng", 5),
    ("chết đi", 2), ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("cõi không hình sắc", 5), ("gồm năm khối", 2),
    ("gồm bốn khối", 2), ("một số", 2),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-11): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    g = "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti"
    assert cap(E.who2(g)).startswith("Ở những người thuộc kiếp sống cuối cùng đang tái sinh vào cõi gồm năm khối")
    for g in ("Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ", "Sabbesaṃ cavantānaṃ acakkhukānaṃ "
              "upapajjantānaṃ", "Catuvokārā pañcavokārā cavantānaṃ pavatte cittassa bhaṅgakkhaṇe",
              "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ"):
        assert head11(g) == H8.head8(g), (head11(g), H8.head8(g))                            # 10-08
    for g in ("Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ", "Pacchimacittasamaṅgīnaṃ"):
        assert head11(g) == H7.head7(g), (head11(g), H7.head7(g))                            # 10-07
    g = "Kāmāvacare parinibbantānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti"
    assert head11(g) == cap(F.who("Kāmāvacare parinibbantānaṃ")) + E.YE_CA_JOIN + Y5.ye_bhava("purisā")
    assert ye_clause("purisā", None, True, None, None) == Y5.ye_bhava("purisā")
    assert ye_clause("itthiyo", None, True, "upekkhāya", None) == Y5.ye_bhava("itthiyo", "upekkhāya")
    assert ye_clause(None, "sacakkhukā", None, "upekkhāya", None) == Y5.ye_attr("sacakkhukā", "upekkhāya")
    assert ye_clause("purisā", None, True, None, "cavantānaṃ") == \
        "những người nam đang chết đi mà sau khi trải qua một số kiếp sống trong chính trạng thái ấy sẽ nhập Niết-bàn trọn vẹn"
    assert at_moment("bhaṅga", last_kind("")) == C8.when("bhaṅga", last=True) == \
        C8.P_SUBJ["Pacchimacittassa bhaṅgakkhaṇe"]
    assert last_kind("upekkhāsampayutta") == "tâm cuối cùng gắn liền với sự bình thản" == \
        H7.last_kind("upekkhā")
    assert C8.SAMANGI.format(c=last_kind("")) == C8.P_SUBJ["Pacchimacittasamaṅgīnaṃ"][len(OI):]
    assert P.ATTR10["itthīnaṃ"] == "là người nữ" and P.ATTR10["saghānakānaṃ"] == "có mũi"
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ca"] == "(e)"


WARNED = set()


def check_parallel(pali):
    """Every sentence that a same-yamaka parser (10-02 … 10-08) can translate, and every answer head that head4 / head5
    / head6 / head7 / head8 / who3 / who32 can translate, comes out byte-identical here (10-06's repeated «ở» inside a
    run of persons is a known warning, as 10-07)."""
    mods = [("10-04", R), ("10-02", P), ("10-05", Y5), ("10-07", H7), ("10-08", H8)]
    heads = [("head4", R.head4), ("head5", Y5.head5), ("head7", H7.head7), ("head8", H8.head8),
             ("who3", A3.who3), ("who32", importlib.import_module("build_3-02_vi").who32)]
    for tag, nm in (("10-03", "build_10-03_vi"), ("10-06", "build_10-06_vi"), ("10-09", "build_10-09_vi"),
                    ("10-10", "build_10-10_vi"), ("10-12", "build_10-12_vi")):
        try:
            mod = importlib.import_module(nm)
            if not hasattr(mod, "translate_sentence"):
                print(f"note: {nm} has no translate_sentence yet; not compared")
                continue
            mods.append((tag, mod))
            for h in ("head13", "head6", "head9", "head10x", "head12"):
                if hasattr(mod, h):
                    heads.append((h, getattr(mod, h)))
        except Exception as e:                        # noqa: BLE001
            print(f"note: {nm} not importable: {e}")
    probs, n = [], {k: 0 for k, _m in mods + heads}
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = fix_slips(re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for s in P.split10(t):
            s = s.strip()
            if not s:
                continue
            mine = translate_sentence(s, "check")
            for tag, mod in mods:
                try:
                    theirs = mod.translate_sentence(s, "check")
                except Exception:                     # noqa: BLE001  (a parser that does not cover this Pāli)
                    continue
                n[tag] += 1
                if theirs != mine:
                    _diff(tag, f"differs from {tag}: {s[:70]} | {theirs} | {mine}", theirs, mine, probs)
            mm = R.P4_NOT.fullmatch(s[:-1]) or R.P4_BOTH.fullmatch(s[:-1])
            if not mm:
                continue
            h = head11(mm["g"])
            for tag, fn in heads:
                try:
                    o = cap(fn(mm["g"]))
                except Exception:                     # noqa: BLE001
                    continue
                n[tag] += 1
                if o != h:
                    _diff(tag, f"head differs from {tag}: {mm['g']} | {o} | {h}", o, h, probs)
    for _t, mod in mods:
        if hasattr(mod, "SLIPS"):
            del mod.SLIPS[:]
    for mod in (F, E):
        del mod.SLIPS[:]
    del SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    for w in sorted(WARNED):
        print("WARN", w)
    return probs


SPLIT_PACCHIMA = (F.PACCHIMA + F.LIST_SEP + F.HEAD[None] + " ", F.PACCHIMA + " ")
# 10-08 head8 / 3-02 who32 never met «Pacchimabhavikānaṃ <attribute> upapajjantānaṃ» (their Pāli has none) and would
# split it into two groups «những người thuộc kiếp sống cuối cùng, những người đang tái sinh có mũi»; here it is one
# group, as 2-01 who() reads «Pacchimabhavikānaṃ <plane>ṃ upapajjantānaṃ» (new, notes-10-11.md).


def _diff(tag, msg, theirs, mine, probs):
    if tag in ("10-06", "head6") and theirs.replace(", ở ", ", ") == mine.replace(", ở ", ", "):
        WARNED.add(f"{tag} repeats «ở» inside a run of persons (one «ở» kept here, = 2-01 / 10-04 / 10-07 / 10-08)")
        return
    if tag in ("10-08", "head8", "who32", "10-10", "head10x") and theirs.replace(*SPLIT_PACCHIMA) == mine:
        # 10-10 (same run, unfinished at this build) splits «Pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ» but
        # not «… itthīnaṃ upapajjantīnaṃ»; 10-09 (finished, head9) keeps one group for both, as here.
        WARNED.add(f"{tag} splits «Pacchimabhavikānaṃ <attribute> upapajjantānaṃ» into two groups (one group kept "
                   f"here, = 2-01 who «… thuộc kiếp sống cuối cùng đang tái sinh vào …»)")
        return
    probs.append(msg)


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in another written Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs = []
    for k in range(1, 14):
        nm = f"10-{k:02d}-indriyayamaka.md"
        vp = S.OUT_DIR / nm
        if nm == NAME or not vp.exists():
            continue
        p1 = (S.PALI_DIR / nm).read_text(encoding="utf-8").splitlines()
        v1 = vp.read_text(encoding="utf-8").splitlines()
        if len(p1) != len(v1):
            print(f"note: {nm} line count differs from its Pāli; not compared")
            continue
        ref = {strip(p): strip(v) for p, v in zip(p1, v1) if p.strip()}
        c = 0
        for p, v in zip(pali.splitlines(), text.splitlines()):
            if p.strip() and strip(p) in ref:
                c += 1
                if ref[strip(p)] != strip(v):
                    probs.append(f"differs from {nm}: {p[:70]}")
        print(f"lines shared with {nm} checked: {c}")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    I.check_cross_book()
    P.check_cross_book()
    R.check_cross_book()
    check_cross_book()
    check_frames()
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    pprobs = check_parallel(pali)
    for mod in (P, R, F, E, Y5, H7, H8):
        if hasattr(mod, "SLIPS"):
            del mod.SLIPS[:]
    del SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì", "bhāv",
                    "là không phải", "ndriya", "ānaṃ", "īnaṃ", "Āmantā", "….", "  ", "là là", "ye ca", "yā ca",
                    "itthiyo", "purisā", "pacchima", "anantarā", "parinibb", "cittassa", "eteneva", "sẽ sẽ",
                    "và và", "samaṅg", "sabbesaṃ", "Sabbesaṃ", "ṃ"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + P.SLIPS + R.SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
