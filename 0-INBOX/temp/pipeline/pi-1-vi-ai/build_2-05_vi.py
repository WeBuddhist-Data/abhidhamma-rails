"""Build the Vietnamese plain zero-shot of pi-1 part 2-05 (world-transcending results, results of the
unwholesome, functional minds; ^1-1-8-0 … ^1-582).

usage: python -I -X utf8 build_2-05_vi.py      (checks, then writes the part)

Importing this file does NOT build anything.
Method: the approved builders are imported unchanged (build_matika_vi = M, build_ch2_01_sample_vi = C,
build_2-01_2-02_vi = B, build_2-03_vi = D, build_2-04_vi = E). This part only ADDS entries to their formula
tables (in memory; an existing entry is never changed) plus three frames they do not know:
  - the world-transcending result «… ime dhammā kusalā. Tasseva lokuttarassa kusalassa jhānassa katattā
    bhāvitattā vipākaṃ …» (the wholesome half through B.kusala_vi, byte-identical to 2-03);
  - the one-sentence runs with «…nti kusalaṃ» / «…nti vipāko»;
  - the answer of aññātāvindriya («Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā …»).
Every other line goes through E.translate_line (2-04's dispatcher, which falls back to 2-03 and 2-01/2-02),
so every formula shared with the earlier parts stays byte-identical. Cross-checks: every Pāli line that also
occurs in 2-01 … 2-04 gets the published Vietnamese; every earlier line still renders as published.

Reusable pieces: NEW_NAMES, NEW_PH, NEW_OPEN, TASSEVA_LOK, TAG, KIRIYA_V, SUKHAVIHARA_V, RESULT_AKUSALA,
S_KAYADUKKHA, G_ANNATAVI, ANNA_V, x2_vi(), rest2_vi(), open2_vi(), lok_vi(), translate_line().
"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)
B = importlib.import_module("build_2-01_2-02_vi")  # importing does not write
D = importlib.import_module("build_2-03_vi")       # importing does not write (adds 2-03 entries to B)
E = importlib.import_module("build_2-04_vi")       # importing does not write (adds 2-04 entries to B / D)

PART = "2-05-cittuppadakandam.md"
PALI_DIR, OUT_DIR = B.PALI_DIR, B.OUT_DIR
DASH, PE, ELL, TASMIM = B.DASH, B.PE, B.ELL, B.TASMIM
add = D.add   # add entries to a table; never overwrite an existing entry
ABYAKATA_V = E.ABYAKATA_V

# =========================================================================================
# 1. Names
# =========================================================================================
ANNA_V = "sự hiểu biết trọn vẹn"                 # aññā (aññindriyaṃ = năng lực hiểu biết trọn vẹn, 2-03)
assert B.NAME["aññindriyaṃ"] == "năng lực " + ANNA_V[len("sự "):]
ANNATAVI = "người đã hiểu biết trọn vẹn"         # aññātāvī
NEW_NAMES = {
    "dukkhindriyaṃ": "năng lực khó chịu",        # pairs with sukhindriyaṃ = năng lực dễ chịu (2-04)
    "aññātāvindriyaṃ": f"năng lực của {ANNATAVI}",
}
for k in NEW_NAMES:
    assert k not in B.NAME, k
add(B.NAME, NEW_NAMES)
assert B.NAME["sukhindriyaṃ"] == "năng lực dễ chịu" and B.NAME["dukkhaṃ"] == "sự đau khổ"

# =========================================================================================
# 2. Strings
# =========================================================================================
# kāyika dukkha: the 2-04 mental asāta/dukkha string with «nơi thân» / «của thân», as the 2-04 kāyika sukha string
S_KAYADUKKHA = E.S_DUKKHA.replace("trong tâm", "nơi thân").replace("tiếp xúc của tâm", "tiếp xúc của thân")
assert S_KAYADUKKHA == E.S_KAYASUKHA.replace("khoan khoái", "bứt rứt").replace("dễ chịu", "khó chịu")
add(B.STR, {
    "kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā "
    "vedanā": S_KAYADUKKHA,
})

# =========================================================================================
# 3. Phrases of the opening sentences (B.PH, joined with «, » by B.chunk_vi)
# =========================================================================================
KIRIYA_V = ("mang tính chức năng, không phải thiện, không phải bất thiện, "
            "cũng không phải là quả của nghiệp")      # kiriyā neva kusalā nākusalā na ca kammavipākā
SUKHAVIHARA_V = "nhằm an trú trong hạnh phúc ngay trong đời này"   # diṭṭhadhammasukhavihāraṃ (cf. sukhavihārī)
assert "an trú trong hạnh phúc" in B.PH[[k for k in B.PH if k.startswith("pītiyā ca virāgā ")][0]]
ANIMITTA_Q = "với tính chất không có dấu hiệu"   # animittaṃ (as suññataṃ / appaṇihitaṃ in 2-03)
assert D.SUNNATA_Q == "với tính chất trống rỗng" and D.APPANIHITA_Q == "với tính chất không mong cầu"
NEW_PH = {
    "animittaṃ": ANIMITTA_Q,
    "kiriyā neva kusalā nākusalā na ca kammavipākā": KIRIYA_V,
    "kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ": KIRIYA_V,
    "diṭṭhadhammasukhavihāraṃ": SUKHAVIHARA_V,
    "sotaviññāṇaṃ uppannaṃ hoti": f"{E.EAR} sinh khởi",
    "dukkhasahagataṃ": "có sự đau khổ đi kèm",    # dukkhaṃ (factor) = sự đau khổ; cf. sukhasahagataṃ
}
add(B.PH, NEW_PH)
B.PH_MAX = max(B.PH_MAX, max(len(k.split()) for k in NEW_PH))
assert B.PH["sukhasahagataṃ"] == "có hạnh phúc đi kèm"

# «…nti kusalaṃ» / «…nti vipāko» inside a run (the quoted qualifier, then what it names)
TAG = {"kusalaṃ": "(thiện)", "vipāko": "(quả của nghiệp)"}
NTI_RE = re.compile(r"(.*\S)nti (kusalaṃ|vipāko)")


def chunk2_vi(part):
    m = NTI_RE.fullmatch(part)
    if m:
        return B.chunk_vi(m.group(1) + "ṃ") + " " + TAG[m.group(2)]
    return B.chunk_vi(part)


def x2_vi(x):
    """B.x_vi plus the «…nti kusalaṃ / vipāko» chunks"""
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(part.replace(PE, ELL))
        elif part.strip():
            out.append(chunk2_vi(part))
    return "".join(out)


# =========================================================================================
# 4. Opening intros (after «Yasmiṃ samaye »)
# =========================================================================================
RESULT_AKUSALA = "như là quả của nghiệp bất thiện đã được tạo và tích lũy"
assert RESULT_AKUSALA == E.RESULT_KAMA.replace("nghiệp thiện thuộc cõi dục lạc", "nghiệp bất thiện")
AKAMMA_P = "akusalassa kammassa katattā upacitattā "
PERSON = D.PERSON   # Vào lúc một người tu tập
NEW_OPEN = [
    (AKAMMA_P + "vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti ", f"Vào lúc {E.EYE} sinh khởi {RESULT_AKUSALA}, "),
    (AKAMMA_P + "vipākā manodhātu uppannā hoti ", f"Vào lúc yếu tố ý sinh khởi {RESULT_AKUSALA}, "),
    (AKAMMA_P + "vipākā manoviññāṇadhātu uppannā hoti ", f"Vào lúc yếu tố ý thức sinh khởi {RESULT_AKUSALA}, "),
    ("manodhātu uppannā hoti ", "Vào lúc yếu tố ý sinh khởi, "),
    ("manoviññāṇadhātu uppannā hoti ", "Vào lúc yếu tố ý thức sinh khởi, "),
    ("rūpāvacaraṃ jhānaṃ bhāveti ", f"{PERSON} tầng thiền thuộc cõi hình sắc, "),
    ("arūpāvacaraṃ jhānaṃ bhāveti ", f"{PERSON} tầng thiền thuộc cõi không hình sắc, "),
]
# second to fourth path in one run (^1-553; «kāmarā gabyāpādānaṃ» read as kāmarāgabyāpādānaṃ)
STAGES_234_P = (f"lokuttaraṃ jhānaṃ bhāveti {D.LEAD_P} {D.STAGE_P[2]}{PE} kāmarā gabyāpādānaṃ anavasesappahānāya "
                f"tatiyāya bhūmiyā pattiyā{PE} {D.STAGE_P[4]} ")
assert D.STAGE_P[3] == "kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā"
STAGES_234 = (STAGES_234_P,
              f"{PERSON} {D.J_LOK}, {D.LEADS}, {D.STAGE[2]}{ELL} {D.STAGE[3]}{ELL} {D.STAGE[4]}, ")
for p, _ in NEW_OPEN + [STAGES_234]:
    assert not any(p.startswith(q) or q.startswith(p) for q, _ in E.OPEN_INTROS + B.INTROS), p
B.INTROS.append(STAGES_234)   # the wholesome half of ^1-553 goes through B.kusala_vi
ALL_INTROS = E.OPEN_INTROS + B.INTROS + NEW_OPEN

# =========================================================================================
# 5. Rest of an opening sentence (after «tasmiṃ samaye »): E.rest_vi + new pieces
# =========================================================================================
add(E.PIECES, {
    "amoho abyākatamūlaṃ": f"{C.N['amoho']}, {E.ABY_ROOT}",   # as alobho / adoso abyākatamūlaṃ (2-04)
    f"{B.YVP_P} {DASH} {ABYAKATA_V}": B.tail_vi(f"{B.YVP_P} {DASH} {ABYAKATA_V}"),
})


def rest2_vi(rest):
    return E.rest_vi(rest)


# =========================================================================================
# 6. Opening sentences «Katame dhammā abyākatā? Yasmiṃ samaye …, tasmiṃ samaye …» (one sentence)
# =========================================================================================
def split_body(body):
    """intro, x, rest of 'Yasmiṃ samaye <body>' (without 'Yasmiṃ samaye ')"""
    for p, r in ALL_INTROS:
        if body.startswith(p):
            body, intro = body[len(p):], r
            break
    else:
        raise KeyError("intro: " + body[:80])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    if x.endswith(","):
        x = x[:-1]   # ^1-579: no comma in the Pāli; Vietnamese punctuation needs one (as B.kusala_vi, ^1-189)
    return intro, x, rest


def open2_vi(line):
    kind, body = E.OPEN_RE.fullmatch(line).groups()
    intro, x, rest = split_body(body)
    return M.QUESTION(E.KIND[kind]) + " " + intro + x2_vi(x) + f", {C.THEN} " + rest2_vi(rest)


# =========================================================================================
# 7. World-transcending results: the wholesome sentence (B.kusala_vi, byte-identical to 2-03)
#    + «Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ …» (its result)
# =========================================================================================
TASSEVA_LOK = "Như là quả của chính tầng thiền thiện vượt thế gian ấy đã được tạo và tu tập, khi một người"
assert TASSEVA_LOK == E.TASSEVA("x").replace("nghiệp thiện thuộc x", "tầng thiền thiện " + D.LOK).replace(
    "tích lũy", "tu tập")
LOK_RE = re.compile(
    r"Katame dhammā abyākatā\? (Yasmiṃ samaye .*? ime dhammā kusalā)(\.?) ([Tt])asseva lokuttarassa kusalassa "
    r"jhānassa katattā bhāvitattā vipākaṃ (.*?), tasmiṃ samaye (.*)$")
STRAY_RE = re.compile(r"(\S+) hoti …pe…")


def kusala2_vi(kus_p):
    """B.kusala_vi on 'Yasmiṃ samaye … ime dhammā kusalā[.]' without the question;
    a stray space before «…pe…» in the list («phasso hoti …pe…») is mirrored"""
    stray = STRAY_RE.findall(kus_p)
    norm = STRAY_RE.sub(lambda m: m.group(1) + " hoti" + PE, kus_p)
    v = B.kusala_vi("Katame dhammā kusalā? " + norm)
    assert v.startswith(B.Q_KUSALA + " ")
    v = v[len(B.Q_KUSALA) + 1:]
    for name in stray:
        a, b = f"{B.there_vi(name)}{ELL}", f"{B.there_vi(name)} {ELL}"
        assert v.count(a) == 1, (name, v[:200])
        v = v.replace(a, b)
    return v


def lok_vi(line):
    m = LOK_RE.fullmatch(line)
    if not m:
        return None
    kus_p, stop, t, x, rest = m.groups()
    kus = kusala2_vi(kus_p + stop)
    xv = x2_vi(x)
    lead = ", " if xv.startswith("khi ") else " "
    res = TASSEVA_LOK if t == "T" else TASSEVA_LOK[0].lower() + TASSEVA_LOK[1:]
    join = " " if stop else "; "   # ^1-528: no full stop before «tasseva» (lower case); a semicolon is written
    assert (stop == ".") == (t == "T"), line[:80]
    return (M.QUESTION(C.ABYAKATA) + " " + kus + join + res + lead + xv + f", {C.THEN} " + rest2_vi(rest))


# =========================================================================================
# 8. The answer of aññātāvindriya (frame of jīvitindriya: «Điều có ở …, tức là S – …»)
# =========================================================================================
G_ANNATAVI = f"ở các hiện tượng ấy của {ANNATAVI}"   # tesaṃ aññātāvīnaṃ dhammānaṃ (cf. C.G_JIVITA)
assert C.G_JIVITA == "ở các hiện tượng phi vật chất ấy"
ANNATAVI_RE = re.compile(r"Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā (.+?) – ((?:idaṃ|ayaṃ) tasmiṃ samaye .+)$")


def annatavi_qa(line):
    m = B.QRE.fullmatch(line)
    if not m:
        return None
    name, _, mark, rest = m.groups()
    k = ANNATAVI_RE.fullmatch(rest)
    if not (mark == "?" and k):
        return None
    s, tail = k.groups()
    D.register(s)
    return (f"{B.q_vi(name)}? Điều có {G_ANNATAVI}, tức là {ANNA_V}, {B.STR[s]} {DASH} "
            + D.rest_vi(E.presub(tail)))


# =========================================================================================
# 9. Headings and closing lines (headings verbatim from vi-zeroshot-terms.md; B.check_headings checks them)
# =========================================================================================
AKU = "là quả của nghiệp bất thiện"
KIR = "mang tính chức năng"
HEAD = {
    "#### Lokuttaravipāka-paṭhamamaggavipākā": f"#### Các quả {D.LOK}: quả của con đường thứ nhất",
    "##### Suddhikasuññataṃ": "##### Sự trống rỗng đơn thuần",
    "##### Suññatapaṭipadā": "##### Cách thực hành với sự trống rỗng",
    "##### Suddhikaappaṇihitaṃ": "##### Sự không mong cầu đơn thuần",
    "##### Appaṇihitapaṭipadā": "##### Cách thực hành với sự không mong cầu",
    "##### Chandādhipateyyasuddhikapaṭipadā": "##### Cách thực hành đơn thuần với ý muốn làm yếu tố chủ đạo",
    "##### Chandādhipateyyasuddhikasuññatā": "##### Sự trống rỗng đơn thuần với ý muốn làm yếu tố chủ đạo",
    "##### Dutiyādimaggavipāko": "##### Quả của con đường thứ hai và các con đường tiếp theo",
    "#### Akusalavipākaabyākataṃ": f"#### Loại không xác định về mặt đạo đức {AKU}",
    "##### Akusalavipākapañcaviññāṇāni": f"##### Năm loại thức {AKU}",
    "##### Akusalavipākamanodhātu": f"##### Yếu tố ý {AKU}",
    "##### Akusalavipākamanoviññāṇadhātu": f"##### Yếu tố ý thức {AKU}",
    "#### Ahetukakiriyāabyākataṃ": f"#### Loại không xác định về mặt đạo đức, {KIR}, không có gốc rễ",
    "##### Kiriyāmanodhātu": f"##### Yếu tố ý {KIR}",
    "##### Kiriyāmanoviññāṇadhātusomanassasahagatā": f"##### Yếu tố ý thức {KIR}, {E.ACC['somanassa']}",
    "##### Kiriyāmanoviññāṇadhātuupekkhāsahagatā": f"##### Yếu tố ý thức {KIR}, {E.ACC['upekkhā']}",
    "##### Sahetukakāmāvacarakiriyā": "##### Tâm chức năng có gốc rễ thuộc cõi dục lạc",
    "##### Rūpāvacarakiriyā": "##### Tâm chức năng thuộc cõi hình sắc",
    "##### Arūpāvacarakiriyā": "##### Tâm chức năng thuộc cõi không hình sắc",
}
CLOSE = {
    "Suddhikasuññataṃ.": "Sự trống rỗng đơn thuần.",
    "Suññatapaṭipadā.": "Cách thực hành với sự trống rỗng.",
    "Suddhikaappaṇihitaṃ.": "Sự không mong cầu đơn thuần.",
    "Appaṇihitapaṭipadā.": "Cách thực hành với sự không mong cầu.",
    "Chandādhipateyyasuddhikapaṭipadā.": "Cách thực hành đơn thuần với ý muốn làm yếu tố chủ đạo.",
    "Chandādhipateyyasuddhikasuññatā.": "Sự trống rỗng đơn thuần với ý muốn làm yếu tố chủ đạo.",
    "Paṭhamamaggavipāko.": "Quả của con đường thứ nhất.",
    "Dutiyādimaggavipāko.": "Quả của con đường thứ hai và các con đường tiếp theo.",
    "Lokuttaravipāko.": f"Quả {D.LOK}.",
    "Akusalavipākapañcaviññāṇāni.": f"Năm loại thức {AKU}.",
    "Akusalavipākā manodhātu.": f"Yếu tố ý {AKU}.",
    "Akusalavipākā manoviññāṇadhātu.": f"Yếu tố ý thức {AKU}.",
    "Vipākā abyākatā.": "Các quả của nghiệp, không xác định về mặt đạo đức.",   # cf. #### Abyākatavipāko (2-04)
    "Kiriyā manodhātu.": f"Yếu tố ý {KIR}.",
    "Kiriyā manoviññāṇadhātu somanassasahagatā.": f"Yếu tố ý thức {KIR}, {E.ACC['somanassa']}.",
    "Kiriyā manoviññāṇadhātu upekkhāsahagatā.": f"Yếu tố ý thức {KIR}, {E.ACC['upekkhā']}.",
    "Ahetukā kiriyā abyākatā.": f"Các loại không xác định về mặt đạo đức, {KIR}, không có gốc rễ.",
    "Sahetukā kāmāvacarakiriyā.": "Tâm chức năng có gốc rễ thuộc cõi dục lạc.",
    "Rūpāvacarakiriyā.": "Tâm chức năng thuộc cõi hình sắc.",
    "Arūpāvacarakiriyā.": "Tâm chức năng thuộc cõi không hình sắc.",
    "Kiriyā abyākatā.": f"Các loại không xác định về mặt đạo đức, {KIR}.",
    "Cittuppādakaṇḍaṃ niṭṭhitaṃ.": "Phần về sự sinh khởi của tâm đã hoàn tất.",   # terms file
}
add(B.EXACT, HEAD)
add(B.EXACT, CLOSE)
assert B.EXACT["Suddhikapaṭipadā."] == "Cách thực hành đơn thuần."
assert "Vipākā abyākatā." not in E.CLOSE


# =========================================================================================
# 10. Line dispatch and build
# =========================================================================================
def translate_line(line):
    if line in B.EXACT:
        return B.EXACT[line]
    r = lok_vi(line)
    if r is not None:
        return r
    r = E.sphere_vi(line)
    if r is not None:
        return r
    if E.OPEN_RE.fullmatch(line):
        v = open2_vi(line)
        try:
            ev = E.open_vi(line)   # 2-04's frame, where it applies, gives the same Vietnamese
        except (KeyError, AssertionError):
            ev = None
        assert ev is None or ev == v, (line[:80], ev[:200], v[:200])
        return v
    r = annatavi_qa(line)
    if r is not None:
        return r
    return E.translate_line(line)


def render(segs):
    out = []
    for bid, lines in segs:
        vi = [B.cap(translate_line(l)) for l in lines]
        for p, r in zip(lines, vi):
            B.check_line(p, r)
            assert "…pe…" not in r and "pe…" not in r, (bid, r[:120])
        vi[-1] += f" ^{bid}"
        out.append("\n".join(vi))
    return out


EARLIER = ("2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md", "2-03-cittuppadakandam.md",
           "2-04-cittuppadakandam.md")


def earlier_pairs():
    """Pāli line -> published Vietnamese line, from the finished parts 2-01 … 2-04"""
    pairs = {}
    for name in EARLIER:
        ps = B.segments((PALI_DIR / name).read_text(encoding="utf-8"))
        vs = B.segments((OUT_DIR / name).read_text(encoding="utf-8"))
        for (b1, pl), (b2, vl) in zip(ps, vs):
            assert b1 == b2 and len(pl) == len(vl)
            for p, v in zip(pl, vl):
                pairs.setdefault(p, v)
    return pairs


def build():
    segs = B.segments((PALI_DIR / PART).read_text(encoding="utf-8"))
    out = render(segs)
    text = "\n\n".join(out) + "\n"
    prev = earlier_pairs()
    shared = 0
    for (bid, pl), seg in zip(segs, out):
        vl = re.sub(r" \^[0-9A-Za-z-]+$", "", seg).split("\n")
        for p, v in zip(pl, vl):
            if p in prev:
                assert prev[p] == v, (bid, p[:80], v[:120], prev[p][:120])
                shared += 1
    # every earlier Pāli line still renders as published, through 2-04's dispatcher and through this one
    rechecked = skipped = 0
    for p, v in prev.items():
        if p.startswith("#") or p in B.EXACT:
            continue
        try:
            got_e = B.cap(E.translate_line(p))
        except Exception:   # a few 2-01 sample lines are hand-built (variant brackets); skip them
            skipped += 1
            continue
        if "[" in p and got_e != v:
            skipped += 1
            continue
        assert got_e == v, ("earlier line changed", p[:80], got_e[:120], v[:120])
        assert B.cap(translate_line(p)) == v, ("this dispatcher differs on an earlier line", p[:80])
        rechecked += 1
    print(f"earlier parts: {rechecked} lines re-rendered identically, {skipped} hand-built lines skipped")
    return text, len(segs), shared


if __name__ == "__main__":
    print("headings equal the terms file:", B.check_headings())
    text, n, shared = build()
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and ":-" not in text
    (OUT_DIR / PART).write_bytes(text.encode("utf-8"))
    print("wrote", OUT_DIR / PART, n, "segments;", shared, "lines identical to the same Pāli in 2-01 … 2-04")
