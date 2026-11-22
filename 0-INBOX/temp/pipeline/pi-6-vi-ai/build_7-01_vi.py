# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-01-anusayayamaka.md: FRAME-SETTER of family C (Anusayayamaka).

The later Anusaya chapters (7-02 … 7-11) import this module and use its frames VERBATIM:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    import importlib; A = importlib.import_module("build_7-01_vi")
    A.translate_line(line)            # the whole sentence parser (extend A.SENTENCES / A.EXACT for new shapes)
    A.tl("kāmarāgānusayo ca paṭighānusayo ca")   # tendency list -> Vietnamese
    A.question(rel, dem, a, b, va, vb, label, vapana)  # yassa / yattha / yassa yattha pair questions
    A.statement(per, places, res, clause)        # answers naming persons and places
    A.VERB, A.PERSON_VI, A.PLACE_VI, A.RES_VI, A.REL_VI, A.DEM_VI, A.NO_CA_VI, A.MULAKA ...

Slots: tendency (TENDENCY_VI), person (PERSON_VI), place / plane / feeling (PLACE_VI), polarity and verb (VERB: each
Pāli verb form has «p» = its predicate and «no» = the predicate after «no ca …», i.e. its denial), relative / demonstrative
(REL_VI / DEM_VI / RES_VI / NO_CA_VI). Frames marked PROPOSED are not used in 7-01: the agent of that chapter checks
them against its Pāli and reports changes. The yo / so, yato / tato frames (sānusaya, pajahati, parijānāti) are in
YO_REL_VI / YO_DEM_VI / YO_VERB / question_yo.

DASH RULE: the frames add no dash; the only dash of 7-01 is the Pāli one in ^6-7-1. No quotes in 7-01.
Importing writes nothing; run  python -I -X utf8 -B build_7-01_vi.py  to rebuild the chapter file.
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

CH = "7-01-anusayayamaka.md"
cap, low = B.cap, B.low

# ================================================================ the seven latent tendencies (pi-2 ^2-816, ^2-949)
ANUSAYA = "khuynh hướng tiềm ẩn"                          # anusaya (pi-2, pi-5; approved cross-book)
STEMS = ["kāmarāg", "paṭigh", "mān", "diṭṭh", "vicikicch", "bhavarāg", "avijj"]
TENDENCY_VI = {                                             # <stem>ānusayo / -ānusayaṃ / -ānusayena
    "kāmarāg": f"{ANUSAYA} tham đắm dục lạc",               # kāmarāgānusayo
    "paṭigh": f"{ANUSAYA} ác cảm",                          # paṭighānusayo
    "mān": f"{ANUSAYA} kiêu mạn",                           # mānānusayo
    "diṭṭh": f"{ANUSAYA} quan điểm",                        # diṭṭhānusayo
    "vicikicch": f"{ANUSAYA} hoài nghi",                    # vicikicchānusayo
    "bhavarāg": f"{ANUSAYA} tham đắm hiện hữu",             # bhavarāgānusayo
    "avijj": f"{ANUSAYA} vô minh",                          # avijjānusayo
}
SLIP_STEMS = {"kāmārāg": "kāmarāg"}                         # kāmārāgānusayo (source slip, rendered as meant)
SEVEN = f"Bảy {ANUSAYA}"                                    # Sattānusayā (pi-2 ^2-816)
SEVEN_LIST = f"{SEVEN} – " + ", ".join(TENDENCY_VI[s] for s in STEMS) + "."
# Sattānusayā – kāmarāgānusayo, …, avijjānusayo. (= pi-2 ^2-816 verbatim)
ANUSAYA_PL = {"anusayā": ANUSAYA}                           # anusayā (plural, 7-10 / 7-11)
SLIPS = []                                                  # source slips met while building (reported)

TOKEN_RE = re.compile(r"(?P<s>" + "|".join(STEMS + list(SLIP_STEMS)) + r")ānusay(?:o|aṃ|ena|ā)")


def tendency(word):
    m = TOKEN_RE.fullmatch(word)
    if not m:
        raise ValueError(f"not a tendency: {word!r}")
    s = m["s"]
    if s in SLIP_STEMS:
        SLIPS.append(word)
        s = SLIP_STEMS[s]
    return TENDENCY_VI[s]


PE = "…"                                                    # …pe… (sample rule)
AND = " và "                                                # A ca B ca -> A và B ; A ca B ca C ca -> A, B và C


def tl(phrase):
    """Tendency list: «X», «X ca», «X ca Y ca …», «X…pe… Y» (a run of questions), «X ca…pe… Y ca»."""
    toks = re.sub(r"\s*…pe…\s*", " …pe… ", phrase).split()
    names, pe_after, is_ca = [], [], False
    for w in toks:
        if w == "ca":
            is_ca = True
        elif w == "…pe…":
            pe_after[-1] = True
        else:
            names.append(tendency(w))
            pe_after.append(False)
    out = names[0]
    for i in range(1, len(names)):
        last = i == len(names) - 1
        if pe_after[i - 1]:
            sep = PE + " " + ("và " if is_ca and last else "")
        elif is_ca:
            sep = AND if last else ", "
        else:
            raise ValueError(f"list without ca / pe: {phrase!r}")
        out += sep + names[i]
    return out


# ================================================================ verbs and polarity
# p  = the predicate (statement and question);  no = the predicate after «no ca <dem>» (its denial, said plainly)
VERB = {
    "anuseti": dict(p="nằm sẵn", no="không nằm sẵn"),                  # anuseti (pi-2 «nằm sẵn»; approved)
    "anusenti": dict(p="nằm sẵn", no="không nằm sẵn"),                 # anusenti (plural; Vietnamese has no number)
    "nānuseti": dict(p="không nằm sẵn", no="vẫn nằm sẵn"),             # PROPOSED 7-02 (no ca … nānuseti = still lies latent)
    "nānusenti": dict(p="không nằm sẵn", no="vẫn nằm sẵn"),            # PROPOSED 7-02
    "uppajjati": dict(p="sinh khởi", no="không sinh khởi"),            # PROPOSED 7-10 (uppajjati pi-1 «sinh khởi»)
    "nuppajjati": dict(p="không sinh khởi", no="vẫn sinh khởi"),       # PROPOSED 7-10
    "pahīno": dict(p="đã được dứt bỏ", no="chưa được dứt bỏ"),         # PROPOSED 7-09 (pi-5 pahīna / appahīna)
    "pahīnā": dict(p="đã được dứt bỏ", no="chưa được dứt bỏ"),         # PROPOSED 7-09
    "appahīno": dict(p="chưa được dứt bỏ", no="đã được dứt bỏ"),       # PROPOSED 7-09 / 7-10
    "appahīnā": dict(p="chưa được dứt bỏ", no="đã được dứt bỏ"),       # PROPOSED 7-09 / 7-10
}
VERB_SLIP = {"anusanti": "anusenti"}                        # source slip ^6-7-35 «anusanti», rendered as meant
NA_VATTABBO = "{a} không nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”"
# PROPOSED 7-09 / 7-10: X na vattabbo "pahīno"ti vā "appahīno"ti vā (Pāli quotes -> “…”)


def qform(v):                                               # anuseti -> anusetīti ; pahīno -> pahīnoti
    return v[:-1] + "īti" if v.endswith("i") else v + "ti"


V_RE = "|".join(sorted(list(VERB) + list(VERB_SLIP), key=len, reverse=True))
VQ = {qform(v): v for v in VERB}
VQ_RE = "|".join(sorted(VQ, key=len, reverse=True))


def verb(v):
    if v in VERB_SLIP:
        SLIPS.append(v)
        v = VERB_SLIP[v]
    return VERB[v]


# ================================================================ persons (pi-4 / pi-5), places (pi-1 / pi-2 / pi-5)
PERSON_VI = {
    "Anāgāmissa": "Ở bậc không trở lại",                     # anāgāmī (pi-4 «bậc không trở lại»)
    "Puthujjanassa": "Ở người phàm phu",                     # puthujjana (pi-1 / pi-4 «người phàm phu»)
    "Arahato": "Ở bậc A-la-hán",                             # PROPOSED 7-02 … (arahant «bậc A-la-hán» pi-5)
    "Dvinnaṃ puggalānaṃ": "Ở hai hạng người",                # dvinnaṃ puggalānaṃ (pi-4 «hai hạng người»)
    "Tiṇṇaṃ puggalānaṃ": "Ở ba hạng người",
    "Catunnaṃ puggalānaṃ": "Ở bốn hạng người",
    "Tesaññeva puggalānaṃ": "Ở chính những hạng người ấy",   # tesaññeva puggalānaṃ
    "Tasseva puggalassa": "Ở chính hạng người ấy",           # tasseva puggalassa
}
PLACE_VI = {                                                # locatives, joined with ", "
    "kāmadhātuyā dvīsu vedanāsu": "nơi hai loại cảm giác trong cõi dục lạc",   # kāmadhātu «cõi dục lạc» pi-2
    "kāmadhātuyā tīsu vedanāsu": "nơi ba loại cảm giác trong cõi dục lạc",
    "dukkhāya vedanāya": "nơi cảm giác khó chịu",            # pi-1 / pi-5 «nơi cảm giác khó chịu»
    "rūpadhātuyā": "trong cõi hình sắc",                     # rūpadhātu (plane) «cõi hình sắc» pi-2
    "arūpadhātuyā": "trong cõi không hình sắc",              # arūpadhātu «cõi không hình sắc» pi-2
    "sabbasakkāyapariyāpannesu dhammesu": "nơi tất cả các hiện tượng nằm trong tự ngã",
    # sakkāya «tự ngã» (pi-1 sakkāyadiṭṭhi), pariyāpanna «nằm trong» (pi-1 / pi-2); aṭṭhakathā: = tebhūmakā dhammā
    "apariyāpanne": "nơi những gì không nằm trong các cõi tồn tại",   # PROPOSED 7-02 (pi-1 apariyāpanna)
    "sabbattha": "ở mọi nơi",                                # PROPOSED 7-02 …
}
PERSON_RE = "|".join(sorted(PERSON_VI, key=len, reverse=True))
PLACE_RE = "|".join(sorted(PLACE_VI, key=len, reverse=True))

# relative / demonstrative frames of the person / place questions and answers
REL_VI = {"yassa": "ở người nào", "yattha": "ở nơi nào", "yassa yattha": "ở người nào, ở nơi nào"}
DEM_VI = {"tassa": "ở người ấy", "tattha": "ở nơi ấy", "tassa tattha": "ở người ấy, ở nơi ấy"}
RES_VI = {"ettha": "ở đó", "tassa tattha": "ở người ấy, ở nơi ấy", "tesaṃ tattha": "ở những người ấy, ở nơi ấy"}
NO_CA_VI = {"tassa": "ở người ấy", "tesaṃ": "ở những người ấy", "tattha": "ở nơi ấy",
            "tassa tattha": "ở người ấy, ở nơi ấy", "tesaṃ tattha": "ở những người ấy, ở nơi ấy"}
VA_PANA = "Còn "                                            # yassa vā pana … (sample «Còn bất cứ gì …»)

# ================================================================ question frames
Q_FRAME = "{rel} mà {a} {pa}, thì {dem} có phải {b} {pb} không?"
# (Ka) yassa A anuseti tassa B anusetīti?  /  yattha … tattha …  /  yassa yattha … tassa tattha …
KATTHA_Q = "{a} {p} ở đâu?"                                 # Kattha A anuseti?


def question(rel, dem, a, b, va, vb, label=None, vapana=False):
    s = Q_FRAME.format(rel=REL_VI[rel], a=tl(a), pa=verb(va)["p"], dem=DEM_VI[dem], b=tl(b), pb=verb(VQ[vb])["p"])
    if vapana:
        s = VA_PANA + s
    return f"{B.LABEL[label]} {cap(s)}" if label else cap(s)


# PROPOSED (7-03 … 7-08): yo / so, yato / tato with sānusaya / niranusaya (instrumental) and pajahati /
# parijānāti (accusative). «{t}» = the tendency list.
YO_REL_VI = {"yo": "người nào", "yato": "đối với nơi nào mà", "yo yato": "người nào, đối với nơi nào mà"}
YO_DEM_VI = {"so": "người ấy", "tato": "đối với nơi ấy", "so tato": "người ấy, đối với nơi ấy"}
YO_VERB = {
    "sānusayo": dict(p="có {t}", no="không có {t}"),                         # Xena sānusayo (Sānusayavāro)
    "niranusayo": dict(p="không có {t}", no="vẫn có {t}"),                   # Xena niranusayo
    "pajahati": dict(p="dứt bỏ {t}", no="không dứt bỏ {t}"),                 # Xaṃ pajahati (pi-1 pajahana «dứt bỏ»)
    "nappajahati": dict(p="không dứt bỏ {t}", no="vẫn dứt bỏ {t}"),
    "parijānāti": dict(p="hiểu biết trọn vẹn {t}", no="không hiểu biết trọn vẹn {t}"),  # pi-2 «hiểu biết trọn vẹn»
    "na parijānāti": dict(p="không hiểu biết trọn vẹn {t}", no="vẫn hiểu biết trọn vẹn {t}"),
}
YO_Q_FRAME = "{rel} {pa}, thì có phải {dem} {pb} không?"
# (Ka) yo Xena sānusayo so Yena sānusayoti?  ->  (a) Người nào có X, thì có phải người ấy có Y không?
TADEKATTHA = "những gì cùng hiện diện với nó"               # PROPOSED: Tadekaṭṭhaṃ pajahati (pi-1 «cùng hiện diện với»)


def question_yo(rel, dem, a, b, v, label=None, vapana=False):
    f = YO_VERB[v]["p"]
    s = YO_Q_FRAME.format(rel=YO_REL_VI[rel], pa=f.format(t=tl(a)), dem=YO_DEM_VI[dem], pb=f.format(t=tl(b)))
    if vapana:
        s = VA_PANA + low(s)
    return f"{B.LABEL[label]} {cap(s)}" if label else cap(s)


# ================================================================ answers
AMANTA = B.AMANTA                                           # Āmantā. = Đúng vậy. (sample, pi-5)
NO = "Không."                                               # No.
NATTHI = "Không có."                                        # Natthi. (pi-3 «Không có.»)
SIMPLE_C = "{a} {p}"                                        # A anuseti
BUT_C = "{a} {p}, nhưng {dem} {b} {no}"                     # A anuseti, no ca tassa B anuseti
BOTH_C = "{a} {p}, đồng thời {b} cũng {p2}"                 # A ca anuseti B ca anuseti («đồng thời»: no second «và»)
STATEMENT_RES = "{head}, thì {res} {clause}."               # <person> <places> tassa tattha / ettha <clause>.
STATEMENT = "{head}, {clause}."                             # <person> <clause>.


def statement(per, places, res, clause):
    head = ", ".join(([PERSON_VI[per]] if per else []) + [PLACE_VI[p] for p in places])
    if not head:
        return cap(clause) + "."
    if res:
        return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))
    return cap(STATEMENT.format(head=head, clause=clause))


SUBJ_RE = re.compile(
    rf"(?P<per>{PERSON_RE})?(?P<pl>(?: ?(?:{PLACE_RE}))*) ?(?P<res>tassa tattha|tesaṃ tattha|ettha)? ?(?P<body>.+)",
    flags=re.I)
BUT_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE}), no ca (?P<dem>tassa tattha|tesaṃ tattha|tassa|tesaṃ|tattha) "
                    rf"(?P<b>.+?) (?P<vb>{V_RE})")
BOTH_RE = re.compile(rf"(?P<a>.+? ca) (?P<va>{V_RE}) (?P<b>.+? ca) (?P<vb>{V_RE})")
SIMPLE_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE})")


def lower1(s):
    return s[:1].lower() + s[1:]


def parse_statement(s):
    m = SUBJ_RE.fullmatch(s.rstrip("."))
    per = m["per"]
    if per:
        per = next(k for k in PERSON_VI if k.lower() == per.lower())
    pl_txt = (m["pl"] or "").strip()
    places = []
    while pl_txt:
        hit = re.match(rf"({PLACE_RE})(?: |$)", lower1(pl_txt))
        if not hit:
            raise ValueError(f"unparsed places in {s!r}")
        places.append(hit.group(1))
        pl_txt = pl_txt[hit.end():].strip()
    body = m["body"]
    for rx, kind in ((BUT_RE, "but"), (BOTH_RE, "both"), (SIMPLE_RE, "simple")):
        b = rx.fullmatch(body)
        if b:
            break
    else:
        raise ValueError(f"unparsed clause: {s!r}")
    if kind == "but":
        clause = BUT_C.format(a=tl(b["a"]), p=verb(b["va"])["p"], dem=NO_CA_VI[b["dem"]], b=tl(b["b"]),
                              no=verb(b["vb"])["no"])
    elif kind == "both":
        clause = BOTH_C.format(a=tl(b["a"]), p=verb(b["va"])["p"], b=tl(b["b"]), p2=verb(b["vb"])["p"])
    else:
        clause = SIMPLE_C.format(a=tl(b["a"]), p=verb(b["va"])["p"])
    return statement(per, places, m["res"], clause)


# ================================================================ headings, closing lines, cycle labels
SECTION = dict(B.SECTION)
PATILOMA = "Chiều ngược"                                    # paṭilomaṃ (paṭiloma «chiều ngược», terms file)
SECTION.update({                                            # -vāra spellings of the paṭiloma chapters (PROPOSED)
    "Sānusayavāra": SECTION["Sānusayavāro"], "Pajahanavāra": SECTION["Pajahanavāro"],
    "Pariññāvāra": SECTION["Pariññāvāro"], "Pahīnavāra": SECTION["Pahīnavāro"],
    "Uppajjanavāro": B.VARO.format(x="sự sinh khởi"),       # PROPOSED 7-10
    "dhātupucchāvāro": "Mục hỏi theo các yếu tố",           # PROPOSED 7-10 (parallel to dhātuvisajjanāvāro, terms file)
})
VARA_OF = {"Anusayavāre": "Anusayavāra", "Sānusayavāre": "Sānusayavāro", "Pajahanavāre": "Pajahanavāro",
           "Pariññāvāre": "Pariññāvāro", "Pahīnavāre": "Pahīnavāro"}
DIRECTION = {"anulomaṃ": SECTION["anulomaṃ"], "paṭilomaṃ": PATILOMA}
VARE_DIR = "{d} trong {v}."                                 # Anusayavāre anulomaṃ. = Chiều thuận trong mục về …
MULAKA = {                                                  # (Ekamūlakaṃ) … (Chakkamūlakaṃ)
    "Eka": "(Phần dựa trên một mục)",
    "Duka": "(Phần dựa trên bộ đôi)",                       # pi-2 Dukamūlakaṃ «Phần dựa trên bộ đôi»
    "Tika": "(Phần dựa trên bộ ba)",                        # pi-2 Tikamūlakaṃ «Phần dựa trên bộ ba»
    "Catukka": "(Phần dựa trên bộ bốn)",
    "Pañcaka": "(Phần dựa trên bộ năm)",
    "Chakka": "(Phần dựa trên bộ sáu)",
}
MULAKA_RE = re.compile(r"\((?P<n>Eka|Duka|Tika|Catukka|Pañcaka|Chakka)mūlakaṃ ?\)")
MAHAVARO_1 = f"{SECTION['Mahāvāro']} 1. {SECTION['anusayavāro']}"   # Mahāvāro 1. anusayavāro

EXACT = {
    "Anusayayamakaṃ": B.YAMAKA["Anusayayamakaṃ"],
    ("Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, "
     "avijjānusayo."): SEVEN_LIST,
    "Uppattiṭṭhānavāro": SECTION["Uppattiṭṭhānavāro"],
    "Uppattiṭṭhānavāro.": SECTION["Uppattiṭṭhānavāro"] + ".",
    "Mahāvāro 1. anusayavāro": MAHAVARO_1,
    "Anusayavāro.": SECTION["Anusayavāra"] + ".",           # PROPOSED 7-02
}


def heading(t):
    if t in EXACT:
        return EXACT[t]
    m = re.fullmatch(r"\((?P<l>Ka|Kha|Ga|Gha|Ṅa|Ca)\) (?P<w>\S+)", t)
    if m and m["w"] in SECTION:
        return f"{B.LABEL[m['l']]} {SECTION[m['w']]}"
    if t in SECTION:
        return SECTION[t]
    raise ValueError(f"unmatched heading: {t!r}")


# ================================================================ sentence parser
Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]assa|[Yy]attha)(?P<vp> vā pana)?(?P<y2> yattha)? "
                  rf"(?P<a>.+?) (?P<va>{V_RE}) (?P<d>tassa tattha|tassa|tattha) (?P<b>.+?) ?(?P<vb>{VQ_RE})\?")
KATTHA_RE = re.compile(rf"Kattha (?P<a>.+?) (?P<va>{V_RE})\?")
SPLIT_RE = re.compile(r"(?<=[?.])\s+(?=\S)")               # sentence split (sample rule)


def translate_sentence(s):
    if s == "Āmantā.":
        return AMANTA
    if s == "No.":
        return NO
    if s == "Natthi.":
        return NATTHI
    if s in EXACT:
        return EXACT[s]
    m = MULAKA_RE.fullmatch(s)
    if m:
        if " )" in s:
            SLIPS.append(s)
        return MULAKA[m["n"]]
    m = re.fullmatch(r"(?P<v>\w+vāre) (?P<d>anulomaṃ|paṭilomaṃ)\.", s)
    if m and m["v"] in VARA_OF:
        return VARE_DIR.format(d=DIRECTION[m["d"]], v=low(SECTION[VARA_OF[m["v"]]]))
    m = KATTHA_RE.fullmatch(s)
    if m:
        return cap(KATTHA_Q.format(a=tl(m["a"]), p=verb(m["va"])["p"]))
    m = Q_RE.fullmatch(s)
    if m:
        y1 = m["y1"].lower()
        rel = "yassa yattha" if m["y2"] else y1
        return question(rel, m["d"], m["a"], m["b"], m["va"], m["vb"], m["l"], bool(m["vp"]))
    return parse_statement(s)


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    sents = SPLIT_RE.split(t)
    return " ".join(translate_sentence(s) for s in sents) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ cross-book asserts (pi-N rails contain the string)
CROSS_BOOK = [
    (SEVEN_LIST.rstrip("."), 2), (f"bảy {ANUSAYA}", 2), ("nằm sẵn", 2), ("thì ở đó", 2),
    ("nơi cảm giác khó chịu", 5), ("cảm giác khó chịu", 1), ("bảy loại cảm giác", 2),
    ("trong cõi dục lạc", 2), ("trong cõi hình sắc", 2), ("trong cõi không hình sắc", 2),
    ("chết ở cõi hình sắc rồi tái sinh vào cõi không hình sắc", 5),
    ("quan điểm về tự ngã", 1), ("nằm trong", 1), ("nằm trong cõi dục lạc", 2),
    ("không nằm trong các cõi tồn tại", 1),
    ("bậc không trở lại", 4), ("người phàm phu", 4), ("hai hạng người", 4), ("hạng người", 4),
    ("bậc A-la-hán", 5), ("Không có.", 3), ("Đúng vậy.", 5),
    ("Phần dựa trên bộ đôi.", 2), ("Phần dựa trên bộ ba.", 2),
    ("đã được dứt bỏ", 5), ("chưa được dứt bỏ", 5), ("hiểu biết trọn vẹn", 2), ("cùng hiện diện với", 1),
    ("sinh khởi", 1), ("dứt bỏ", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_repeats(pali, vi):
    """Identical Pāli sentence -> identical Vietnamese sentence (within the chapter)."""
    seen, bad = {}, 0
    for p, v in zip([ln for ln in pali.splitlines() if ln.strip()], [ln for ln in vi.splitlines() if ln.strip()]):
        if p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        for s in SPLIT_RE.split(p):
            t = translate_sentence(s)
            if seen.setdefault(s, t) != t:
                bad += 1
    return bad


def main():
    check_cross_book()
    SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali, text) == 0, "identical Pāli rendered differently"
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len([ln for ln in text.splitlines() if ln.strip()])} lines, {segs} segments")
    print("source slips rendered as meant:", sorted(set(SLIPS)))
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
