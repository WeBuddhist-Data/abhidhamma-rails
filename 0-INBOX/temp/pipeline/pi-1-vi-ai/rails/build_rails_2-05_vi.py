"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapter 2-05 (the world-transcending resultant minds, the unwholesome-result minds and the functional minds;
^1-1-8-0 … ^1-582, closing chapter 2).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/2-05-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-2-05.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_vi.py (S) and build_rails_2-04_vi.py (D, which loads build_rails_2-03_vi.py = T and
build_rails_2-01_2-02_vi.py = B and extends B's tables in memory). B.NAMES and B.STR get new keys only, and D's
TAIL_REPL one more closing («amoho abyākatamūlaṃ»); the openings of this chapter use copies (ATTR5, PIECES5,
INTROS5), never B's or D's own tables. The unwholesome-result and functional minds mirror D's wholesome-result
frames exactly where the Pāli is parallel. A check rebuilds 2-01, 2-02, 2-03 and 2-04 in memory with the extended
tables and requires them to equal the finished files byte for byte.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md: bodily pain dukkha = «khó chịu», so the unwholesome-result body-consciousness
^1-556 … ^1-561 takes «có sự khó chịu đi kèm», «sự khó chịu», never «sự đau khổ»). Translated fresh from the Pāli.
Later chapter builders may import this file (importing writes nothing).

usage: python -I -X utf8 build_rails_2-05_vi.py
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_04_vi", HERE / "build_rails_2-04_vi.py")
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)        # importing writes nothing; D.T = 2-03 builder, D.B = extended 2-01/2-02 builder
T, B = D.T, D.B

PART = "2-05-cittuppadakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
TS = S.TS
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"
ABY = D.ABY
LOK = T.LOK                                        # vượt thế gian

# =========================================================================================
# 1. New names (nominative)
# =========================================================================================
ANNATAVI = "người đã hiểu biết trọn vẹn"           # aññātāvī (termbase)
NEW_NAMES = {
    "dukkhindriyaṃ": "năng lực khó chịu",          # termbase; APPROVED: bodily pain = «khó chịu»
    "aññātāvindriyaṃ": f"năng lực của {ANNATAVI}",  # no entry: built from aññātāvī + indriya
}
for _k in NEW_NAMES:
    assert _k not in B.NAMES, _k
B.NAMES.update(NEW_NAMES)
assert B.NAMES["dukkhaṃ"] == "sự khó chịu"

# =========================================================================================
# 2. Synonym strings (placed after «Điều mà vào lúc ấy là »)
# =========================================================================================
# painful bodily feeling: D's pleasant bodily string with «khoan khoái» -> «bứt rứt», «dễ chịu» -> «khó chịu»
P_KDUKKHA = ("kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
             "kāyasamphassajā asātā dukkhā vedanā")
KDUK_HEAD = D.KSUK_HEAD.replace("khoan khoái", "bứt rứt")
KDUK_TAIL = D.KSUK_TAIL.replace("khoan khoái", "bứt rứt").replace("dễ chịu", "khó chịu")
assert KDUK_HEAD == "sự bứt rứt nơi thân"
assert KDUK_TAIL == ("sự khó chịu nơi thân, cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của thân, "
                     "cảm giác bứt rứt và khó chịu sinh từ sự tiếp xúc của thân")
assert D.DUK_TAIL.startswith("sự khó chịu trong tâm, cảm nhận bứt rứt và khó chịu")    # the mental parallel
NEW_STR = {
    P_KDUKKHA: f"{KDUK_HEAD}, {KDUK_TAIL}",
    "tajjākāyaviññāṇadhātusamphassajaṃ " + P_KDUKKHA:
        f"{KDUK_HEAD} {D.tajja(D.TAJJA_DH['tajjākāyaviññāṇadhātu'])}, {KDUK_TAIL}",
    D.SAMADHI_P: D.SAMADHI_V,                      # cittassekaggatā / samādhindriyaṃ without sammāsamādhi
    D.VIRIYA_P: D.VIRIYA_V,                        # vīriyindriyaṃ without sammāvāyāmo
}
for _k in NEW_STR:
    assert _k not in B.STR, _k
B.STR.update(NEW_STR)

# aññātāvindriyaṃ: «Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S – idaṃ …» (parallel to S.body_jivita «ở những …»)
AWARE = "sự hiểu biết trọn vẹn"                    # aññā (termbase «hiểu biết trọn vẹn», as a noun)
ANNV_LEAD = f"{S.REL} ở những hiện tượng ấy của {ANNATAVI} là {AWARE}, "
ANNV_RE = re.compile(r"Katamaṃ tasmiṃ samaye (aññātāvindriyaṃ) hoti\? Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā "
                     r"(.+?) – (idaṃ tasmiṃ samaye .*)$")


def annv_vi(m):
    f, s, rest = m.groups()
    return B.q_vi(f, "hoti") + "? " + ANNV_LEAD + B.STR[s] + " – " + B.tail_vi(rest)


# =========================================================================================
# 3. Closings: one more «X abyākatamūlaṃ» for D's tail wrapper
# =========================================================================================
NEW_TAIL = ("amoho abyākatamūlaṃ", f"{S.FN['amoho']}, {D.ROOT_ABY}")
assert NEW_TAIL[0] not in dict(D.TAIL_REPL)
D.TAIL_REPL.append(NEW_TAIL)

# =========================================================================================
# 4. «Katame dhammā abyākatā? Yasmiṃ samaye …» sentences
# =========================================================================================
# attributes of the unwholesome-result and functional minds (copy of D.ATTR)
NEW_ATTR = {
    "sotaviññāṇaṃ uppannaṃ hoti": "thức qua tai sinh khởi",
    "dukkhasahagataṃ": "có sự khó chịu đi kèm",    # APPROVED: bodily pain = «khó chịu» (never «sự đau khổ»)
}
for _k in NEW_ATTR:
    assert _k not in D.ATTR, _k
ATTR5 = dict(D.ATTR)
ATTR5.update(NEW_ATTR)
assert ATTR5["ghānaviññāṇaṃ uppannaṃ hoti"] == "thức qua mũi sinh khởi"

# pieces of the absorption openings (copy of B.PIECES)
NEW_PIECES = {
    "animittaṃ": ["có tính chất không có dấu hiệu"],   # termbase «tính chất không có dấu hiệu», as suññataṃ in 2-03
    T.STAGES[2][0]: [T.STAGES[2][1]],                # ^1-553: the later paths inside a …pe… run
    T.STAGES[3][0]: [T.STAGES[3][1]],
    # ^1-553 «kāmarā gabyāpādānaṃ»: a space inside kāmarāgabyāpādānaṃ, a plain spelling slip rendered as meant
    "kāmarā gabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā": [T.STAGES[2][1]],
}
for _k in NEW_PIECES:
    assert _k not in B.PIECES, _k
PIECES5 = dict(B.PIECES)
PIECES5.update(NEW_PIECES)

# «X-nti kusalaṃ …pe… Y-nti vipāko» (^1-508 …): which absorption is the wholesome one, which its result
MARK_RE = re.compile(r"(.*\S)nti (kusalaṃ|vipāko)")
MARKS = {"kusalaṃ": " (tâm thiện)", "vipāko": " (quả của nghiệp)"}

VIP_AK = D.VIP_KAMA.replace("nghiệp thiện thuộc cõi dục lạc", "nghiệp bất thiện")
assert VIP_AK == "là quả của nghiệp bất thiện đã được tạo và tích lũy"
AK_KAMMA_P = "akusalassa kammassa katattā upacitattā "
KIRIYA_P = "kiriyā neva kusalā nākusalā na ca kammavipākā"
KIRIYA_JH_P = "kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ"
# termbase: kusalā nākusalā / kusalaṃ nākusalaṃ = «không phải thiện không phải bất thiện»; kammavipāka- = «quả của nghiệp»
KIRIYA_V = "mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải quả của nghiệp"
DDSV_P = "diṭṭhadhammasukhavihāraṃ"
DDSV_V = "để an trú trong hạnh phúc ngay trong đời này"
KIR_SUBJ = {"manodhātu uppannā hoti": "yếu tố ý", "manoviññāṇadhātu uppannā hoti": "yếu tố ý thức"}
SPHERE_ACC = {"rūpāvacaraṃ": D.SPHERE["rūpāvacarassa"], "arūpāvacaraṃ": D.SPHERE["arūpāvacarassa"]}
TASSEVA_P = "Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ "
TASSEVA_V = f"Là quả của chính {B.JH} thiện {LOK} ấy đã được tạo và tu tập, {D.WHO_RES} "

INTROS5 = {}   # Pāli opening (after «Yasmiṃ samaye ») -> (Vietnamese opening, table of the pieces that follow)
for _p, _v in B.INTROS.items():                     # the world-transcending openings of 2-03 (and 2-02)
    INTROS5[_p] = (_v, PIECES5)
_p2 = f"lokuttaraṃ jhānaṃ bhāveti {T.LEAD_P} {T.STAGES[1][0]}"   # ^1-553: followed by «…pe…», not a space
assert B.INTROS[_p2 + " "].endswith(", ")
INTROS5[_p2] = (B.INTROS[_p2 + " "][:-2], PIECES5)
INTROS5[TASSEVA_P] = (TASSEVA_V, PIECES5)
for _p, _v in D.VIP_SUBJ.items():
    INTROS5[f"{AK_KAMMA_P}{_p} "] = (f"Vào lúc {_v} sinh khởi, {VIP_AK}, ", ATTR5)
for _p, _v in KIR_SUBJ.items():
    INTROS5[f"{_p} {KIRIYA_P} "] = (f"Vào lúc {_v} sinh khởi, {KIRIYA_V}, ", ATTR5)
for _p, _v in SPHERE_ACC.items():
    INTROS5[f"{_p} jhānaṃ bhāveti {KIRIYA_JH_P} {DDSV_P} "] = (
        f"{T.WHO} {T.DEV} {B.JH} {_v}, {KIRIYA_V}, {DDSV_V}, ", PIECES5)
NEW_INTROS = {k: v for k, v in INTROS5.items() if k not in B.INTROS}
SLIPS = []     # (segment, note) collected while building


def chunks5(x, table):
    """B.chunks per «…pe…» part, plus the «-nti kusalaṃ / -nti vipāko» markers"""
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
        elif part.strip():
            mark = ""
            m = MARK_RE.fullmatch(part.strip())
            if m:
                part, mark = m.group(1) + "ṃ", MARKS[m.group(2)]
            out.append(B.chunks(part, table) + mark)
    return "".join(out)


TAIL_RE = re.compile(r"(.*? hoti)(…pe…\s*(?:ime dhammā (?:kusalā|akusalā|abyākatā)|ye vā pana).*|; ye vā pana.*)")


def clause5(s, sid):
    """one «Yasmiṃ samaye …» or «Tasseva …» clause up to its closing"""
    for p, (intro, table) in sorted(INTROS5.items(), key=lambda kv: -len(kv[0])):
        if s.startswith(p):
            s = s[len(p):]
            break
    else:
        raise KeyError("intro: " + s[:80])
    idx = s.index(" tasmiṃ samaye ")
    x, rest = s[:idx].rstrip(), s[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = " " + DASH, x[:-1].rstrip()
    elif x.endswith(","):
        sep, x = ",", x[:-1]
    else:
        sep = ","          # ^1-579: no comma before «tasmiṃ samaye», rendered as meant (as ^1-189)
        SLIPS.append((sid, "no comma before «tasmiṃ samaye»: rendered as meant (comma)"))
    rest = re.sub(r"\s+…pe…", PE, rest)               # «hoti …pe…»: the space is dropped (as in 2-01 … 2-04)
    m = TAIL_RE.fullmatch(rest)
    return (intro + chunks5(x, table) + sep + f" thì {TS} " + B.there_list(m.group(1))
            + B.tail_vi(m.group(2)))


OPEN5_RE = re.compile(r"Katame dhammā abyākatā\? Yasmiṃ samaye (.+)$")


def open5(line, sid):
    body = OPEN5_RE.fullmatch(line).group(1)
    parts = re.split(r" (?=[Tt]asseva )", body)
    assert len(parts) <= 2
    out = D.Q_ABY + " " + clause5(parts[0], sid)
    if len(parts) == 2:
        if not parts[0].endswith("ime dhammā kusalā."):
            # ^1-528: «… ime dhammā kusalā tasseva …», no full stop: rendered as meant (full stop)
            assert parts[0].endswith("ime dhammā kusalā") and parts[1].startswith("tasseva "), sid
            out += "."
            SLIPS.append((sid, "«ime dhammā kusalā tasseva»: no full stop, rendered as meant («.» and «Là …»)"))
        out += " " + clause5("T" + parts[1][1:], sid)
    return out


# =========================================================================================
# 5. Headings and closing lines
# =========================================================================================
VIP_AK_K = "là quả của nghiệp bất thiện"            # Akusalavipāka- (as D's «là quả của nghiệp thiện»)
assert D.VIP_K == "là quả của nghiệp thiện"
LOK_VIP = f"Quả của nghiệp {LOK}"                  # Lokuttaravipāka- (as D's «Quả của nghiệp thuộc cõi …»)
M1_VIP = "quả của con đường thứ nhất"              # paṭhamamaggavipāka
M2_VIP = "quả của con đường thứ hai trở đi"        # dutiyādimaggavipāka
SUD = "đơn thuần"                                   # suddhika
SUNN = "Sự trống rỗng"                              # Suññata (heading)
APP = "Sự không mong cầu"                           # Appaṇihita (heading)
PP_ALL = "và các cách thực hành"                    # -paṭipadā after suññata / appaṇihita
CHANDA = D.ATTR["chandādhipateyyaṃ"]                # lấy ý muốn làm yếu tố chủ đạo
KIR = "mang tính chức năng"                         # kiriyā
ABY_KIND = f"Loại {ABY}"                            # -abyākataṃ / abyākatā (termbase «loại không xác định …»)
AHET = "không có gốc rễ"                            # ahetuka
SAHET = "có gốc rễ"                                 # sahetuka
H_TEXT = {      # heading word (also the closing line + «.») -> Vietnamese
    "Suddhikasuññataṃ": f"{SUNN} {SUD}",
    "Suññatapaṭipadā": f"{SUNN} {PP_ALL}",
    "Suddhikaappaṇihitaṃ": f"{APP} {SUD}",          # termbase heading entry
    "Appaṇihitapaṭipadā": f"{APP} {PP_ALL}",
    "Chandādhipateyyasuddhikapaṭipadā": f"{T.PP} {SUD}, {CHANDA}",
    "Chandādhipateyyasuddhikasuññatā": f"{SUNN} {SUD}, {CHANDA}",
    "Rūpāvacarakiriyā": f"Tâm {KIR} {D.SPHERE['rūpāvacarassa']}",
    "Arūpāvacarakiriyā": f"Tâm {KIR} {D.SPHERE['arūpāvacarassa']}",
}
H5 = {
    "#### Lokuttaravipāka-paṭhamamaggavipākā": f"#### {LOK_VIP}: {M1_VIP}",
    "Paṭhamamaggavipāko.": f"{cap(M1_VIP)}.",
    "##### Dutiyādimaggavipāko": f"##### {cap(M2_VIP)}",
    "Dutiyādimaggavipāko.": f"{cap(M2_VIP)}.",
    "Lokuttaravipāko.": f"{LOK_VIP}.",
    "#### Akusalavipākaabyākataṃ": f"#### {ABY_KIND} {VIP_AK_K}",
    "##### Akusalavipākapañcaviññāṇāni": f"##### Năm loại thức {VIP_AK_K}",
    "Akusalavipākapañcaviññāṇāni.": f"Năm loại thức {VIP_AK_K}.",
    "##### Akusalavipākamanodhātu": f"##### Yếu tố ý {VIP_AK_K}",
    "Akusalavipākā manodhātu.": f"Yếu tố ý {VIP_AK_K}.",
    "##### Akusalavipākamanoviññāṇadhātu": f"##### Yếu tố ý thức {VIP_AK_K}",
    "Akusalavipākā manoviññāṇadhātu.": f"Yếu tố ý thức {VIP_AK_K}.",
    "Vipākā abyākatā.": f"Quả của nghiệp {ABY}.",              # termbase heading entry
    "#### Ahetukakiriyāabyākataṃ": f"#### {ABY_KIND} {KIR}, {AHET}",
    "##### Kiriyāmanodhātu": f"##### Yếu tố ý {KIR}",           # termbase heading entry
    "Kiriyā manodhātu.": f"Yếu tố ý {KIR}.",
    "##### Kiriyāmanoviññāṇadhātusomanassasahagatā": f"##### Yếu tố ý thức {KIR}, {B.ATTR['somanassasahagataṃ']}",
    "Kiriyā manoviññāṇadhātu somanassasahagatā.": f"Yếu tố ý thức {KIR}, {B.ATTR['somanassasahagataṃ']}.",
    "##### Kiriyāmanoviññāṇadhātuupekkhāsahagatā": f"##### Yếu tố ý thức {KIR}, {B.ATTR['upekkhāsahagataṃ']}",
    "Kiriyā manoviññāṇadhātu upekkhāsahagatā.": f"Yếu tố ý thức {KIR}, {B.ATTR['upekkhāsahagataṃ']}.",
    "Ahetukā kiriyā abyākatā.": f"{ABY_KIND} {KIR}, {AHET}.",
    "##### Sahetukakāmāvacarakiriyā": f"##### Tâm {KIR} thuộc cõi dục lạc, {SAHET}",
    "Sahetukā kāmāvacarakiriyā.": f"Tâm {KIR} thuộc cõi dục lạc, {SAHET}.",
    "Kiriyā abyākatā.": f"{ABY_KIND} {KIR}.",                   # termbase heading entry
    "Cittuppādakaṇḍaṃ niṭṭhitaṃ.": "Phần về sự sinh khởi của tâm đã hoàn tất.",
}
for _p, _v in H_TEXT.items():
    H5[f"##### {_p}"] = f"##### {_v}"
    H5[f"{_p}."] = f"{_v}."
assert H5["#### Ahetukakiriyāabyākataṃ"].startswith("#### Loại không xác định về mặt đạo đức mang tính chức năng")
for _k in H5:
    assert _k not in B.EXACT and _k not in D.H, _k
assert B.EXACT["##### Suddhikapaṭipadā"] and B.EXACT["Vīsati mahānayā."]


# =========================================================================================
# 6. Line dispatch, render, build
# =========================================================================================
def translate_line(line, sid=""):
    if line in H5:
        return H5[line]
    if OPEN5_RE.fullmatch(line):
        return open5(line, sid)
    m = ANNV_RE.fullmatch(line)
    if m:
        return annv_vi(m)
    return D.translate_line(line)


PAIN_SEGS = {f"1-{i}" for i in range(556, 562)}      # the unwholesome-result body-consciousness


def render(segs):
    blocks = []
    for sid, plines in segs:
        vlines = []
        for p in plines:
            v = unicodedata.normalize("NFC", cap(translate_line(p, sid)))
            B.check_vi(v)
            assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
            assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
            assert p.count("…pe…") <= v.count("…"), ("pe", sid)
            assert p.endswith("?") == v.endswith("?"), ("question", sid)
            assert v.endswith(".") or v.endswith("…") or v.startswith("#"), ("stop", sid, v[-40:])
            assert "  " not in v and " ," not in v and ",," not in v and "..." not in v, ("spacing", sid, v)
            assert "đau khổ" not in v and "khổ đau" not in v, ("pain", sid)
            if sid in PAIN_SEGS:
                assert "hạnh phúc" not in v and "dễ chịu" not in v.replace("không dễ chịu", ""), ("pain", sid)
            vlines.append(v)
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def check_earlier_unchanged():
    """The extended tables and the extra closing must leave 2-01 … 2-04 exactly as finished."""
    for fn_name, fn in (("2-01-cittuppadakandam.md", B.build_2_01), ("2-02-cittuppadakandam.md", B.build_2_02),
                        ("2-03-cittuppadakandam.md", T.build), ("2-04-cittuppadakandam.md", D.build)):
        text, _ = fn()
        assert unicodedata.normalize("NFC", text) == (S.OUT / fn_name).read_bytes().decode("utf-8"), fn_name
    print("2-01, 2-02, 2-03, 2-04: rebuilt in memory with the 2-05 tables, byte-identical to the finished files")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Vietnamese rails: new formulas of 2-05", "",
         "Generated by build_rails_2-05_vi.py from its fixed strings; import that file instead of retyping. "
         "Strings already in vi-rails-formulas.md, notes-2-01_2-02.md, notes-2-03.md or notes-2-04.md are not "
         "repeated. Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"… ime dhammā kusalā. {TASSEVA_P.strip()} J, tasmiṃ samaye … = … {D.A_KUSALA_K}. {TASSEVA_V}J, thì {TS} …",
         f"Yasmiṃ samaye {AK_KAMMA_P}vipākaṃ/vipākā X uppannaṃ/uppannā hoti A, tasmiṃ samaye … = "
         f"Vào lúc X sinh khởi, {VIP_AK}, A, thì {TS} …",
         f"{AK_KAMMA_P}vipāka- = {VIP_AK}",
         f"Yasmiṃ samaye X uppannā hoti {KIRIYA_P} A, tasmiṃ samaye … = Vào lúc X sinh khởi, {KIRIYA_V}, A, "
         f"thì {TS} …",
         f"{KIRIYA_P} / {KIRIYA_JH_P} = {KIRIYA_V}",
         f"{DDSV_P} = {DDSV_V}",
         f"X-nti kusalaṃ (in a …pe… run, ^1-508 …) = X{MARKS['kusalaṃ']}",
         f"Y-nti vipāko (in a …pe… run, ^1-508 …) = Y{MARKS['vipāko']}",
         f"Katamaṃ tasmiṃ samaye aññātāvindriyaṃ hoti? Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S – = "
         f"{B.q_vi('aññātāvindriyaṃ', 'hoti')}? {ANNV_LEAD}S –",
         f"…pe… {NEW_TAIL[0]}…pe… = … {NEW_TAIL[1]}…",
         "«avikkhepo hoti…pe… ye vā pana …» closing a clause (^1-553) = «có sự không tán loạn… hoặc …»",
         "", "## Openings", ""]
    for p, (v, _) in NEW_INTROS.items():
        if p == TASSEVA_P:
            continue                               # in «Frames» above
        if p == _p2:
            L.append(f"Yasmiṃ samaye {p}…pe… (^1-553, the later paths in a …pe… run) = {v}… …")
            continue
        L.append(f"Yasmiṃ samaye {p.strip()} … = {v}…")
    L += ["", "### Attributes and pieces", ""]
    for p, v in NEW_ATTR.items():
        L.append(f"{p} = {v}")
    for p, v in NEW_PIECES.items():
        L.append(f"{p} = {' | '.join(v)}")
    L += ["", "## Synonym strings", ""]
    for p, v in NEW_STR.items():
        L.append(f"{p} = {v}")
    L += ["", "## Names", ""]
    for p, v in NEW_NAMES.items():
        L.append(f"{p} = {v}")
    L += ["", "## Headings and closing lines", ""]
    for p, v in H5.items():
        L.append(f"{p} = {v}")
    L += ["", "## Source slips (translated as written; punctuation and spacing rendered as meant)", ""]
    for sid, note in dict.fromkeys(SLIPS):
        L.append(f"^{sid}: {note}")
    L += ["^1-553: «kāmarā gabyāpādānaṃ» (space inside the word) = kāmarāgabyāpādānaṃ, rendered as meant",
          "^1-544: «upasampajja viharati, animittaṃ» (extra comma): the pieces are joined with «, » anyway",
          "^1-574: «samādhindriyaṃ hoti manindriyaṃ hoti» (no comma): rendered as meant (comma)",
          "^1-515, ^1-528, ^1-576: «hoti …pe…» with a space: the space is dropped"]
    (HERE / "notes-2-05.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                        newline="\n")
    print("wrote", HERE / "notes-2-05.md")


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
