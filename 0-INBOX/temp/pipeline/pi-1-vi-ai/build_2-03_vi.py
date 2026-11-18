"""Build the Vietnamese plain zero-shot of pi-1 part 2-03 (Lokuttarakusalaṃ, ^1-1-5-0 … ^1-364).

usage: python -I -X utf8 build_2-03_vi.py      (checks, then writes the part)

Importing this file does NOT build anything.
Method: the approved builders are imported unchanged (build_matika_vi = M, build_ch2_01_sample_vi = C,
build_2-01_2-02_vi = B). This part only ADDS entries to B's formula tables (in memory; nothing of the
earlier parts is rewritten) and two answer frames B does not know (anaññātaññassāmītindriya /
aññindriya). Every other line goes through B's own line translator, so every formula shared with the
earlier parts stays byte-identical. A cross-check compares every Pāli line that also occurs in 2-01 / 2-02
with the Vietnamese already published for it.

Reusable pieces: NEW_NAMES, TOKENS, compose(), ABST(), G_ANANNATA, G_ANNA, LEADS, STAGE, TWENTY_V,
SUNNATA_Q, APPANIHITA_Q, translate_line().
"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)
B = importlib.import_module("build_2-01_2-02_vi")  # importing does not write

PART = "2-03-cittuppadakandam.md"
PALI_DIR, OUT_DIR = B.PALI_DIR, B.OUT_DIR
DASH, PE, ELL, TASMIM, KUSALA = B.DASH, B.PE, B.ELL, B.TASMIM, B.KUSALA


def add(table, new):
    """add entries to one of B's tables; never overwrite an existing entry"""
    for k, v in new.items():
        assert k not in table or table[k] == v, ("would change an earlier formula", k)
        table[k] = v


# =========================================================================================
# 1. Matrix wording reused
# =========================================================================================
LOK = M.PRED[("1-M2-12", "b")]          # lokuttara = vượt thế gian
NIYY = M.PRED[("1-M2-97", "a")]         # niyyānika = dẫn đến giải thoát
APACAYA = M.PRED[("1-M1-10", "b")]      # apacayagāmi = dẫn đến sự giảm trừ
assert (LOK, NIYY, APACAYA) == ("vượt thế gian", "dẫn đến giải thoát", "dẫn đến sự giảm trừ")
LEADS = f"{NIYY} và {APACAYA}"          # niyyānikaṃ apacayagāmiṃ

# =========================================================================================
# 2. Names
# =========================================================================================
VACA, KAMMANTA, AJIVA = "lời nói đúng đắn", "hành động đúng đắn", "sinh kế đúng đắn"
NEW_NAMES = {
    "anaññātaññassāmītindriyaṃ": "năng lực biết được điều chưa từng biết",
    "aññindriyaṃ": "năng lực hiểu biết trọn vẹn",
    "sammāvācā": VACA,
    "sammākammanto": KAMMANTA,
    "sammāājīvo": AJIVA,
}
add(B.NAME, NEW_NAMES)
add(B.COUNTED, {
    "navindriyāni": "chín năng lực",
    "aṭṭhaṅgiko maggo": "con đường gồm tám chi phần",
})

# =========================================================================================
# 3. Synonym strings: earlier strings + suffix tokens, joined with ", "
# =========================================================================================
MAGGA = "chi phần của con đường, thuộc về con đường"   # maggaṅgaṃ maggapariyāpannaṃ


def BOJJH(x):
    """X-sambojjhaṅgo = «chi phần giác ngộ là X»"""
    return f"chi phần giác ngộ là {x}"


WORD = dict(zip("passaddhi paṭipassaddhi".split(), C.WL["passaddhi"]))
TOKENS = {
    "maggaṅgaṃ maggapariyāpannaṃ": MAGGA,
    "pītisambojjhaṅgo": BOJJH(C.N["pīti"]),                    # sự hân hoan
    "samādhisambojjhaṅgo": BOJJH("định tâm"),                  # samādhi (core term)
    "vīriyasambojjhaṅgo": BOJJH(C.WL["cetasiko"][13]),         # vīriyaṃ = sự tinh tấn
    "satisambojjhaṅgo": BOJJH(C.N["sati"]),                    # sự tỉnh thức
    "dhammavicayasambojjhaṅgo": BOJJH(C.WL["paññā"][4]),       # dhammavicayo = sự tìm hiểu các hiện tượng
    "passaddhisambojjhaṅgo": BOJJH(WORD["passaddhi"]),         # sự an tịnh
    "sammāvācā": VACA,
    "sammākammanto": KAMMANTA,
    "sammāājīvo": AJIVA,
}
assert C.WL["cetasiko"][13] == "sự tinh tấn" and C.WL["paññā"][4] == "sự tìm hiểu các hiện tượng"
assert WORD["passaddhi"] == "sự an tịnh"

# abstention strings
ABST_P = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
ABST_W = ["sự kiêng tránh", "sự kiêng tránh hoàn toàn", "sự kiềm chế", "sự không làm", "sự không thực hiện",
          "sự không rơi vào lỗi vi phạm", "sự không vượt quá giới hạn", "sự phá bỏ cây cầu"]


def ABST(obj):
    """'<obj> ārati virati … setughāto': «sự tránh xa <obj>, sự kiêng tránh, …»"""
    return ", ".join([f"sự tránh xa {obj}"] + ABST_W)


add(B.STR, {
    "catūhi vacīduccaritehi " + ABST_P: ABST("bốn loại hành vi xấu bằng lời nói"),
    "tīhi kāyaduccaritehi " + ABST_P: ABST("ba loại hành vi xấu bằng thân"),
    "micchāājīvā " + ABST_P: ABST("sinh kế sai lầm"),
})


def compose(s):
    """A synonym string = the longest known string it starts with + suffix tokens."""
    best = max((k for k in B.STR if s == k or s.startswith(k + " ")), key=len, default=None)
    if best is None:
        raise KeyError("no base string for: " + s[:80])
    out, rest = [B.STR[best]], s[len(best):].strip()
    while rest:
        for t in sorted(TOKENS, key=len, reverse=True):
            if rest == t or rest.startswith(t + " "):
                out.append(TOKENS[t])
                rest = rest[len(t):].strip()
                break
        else:
            raise KeyError(f"unknown token at {rest!r}")
    return ", ".join(out)


def register(s):
    """make B.str_vi know the (prefix-stripped) string s"""
    for p, _ in B.STR_PREFIX:
        if s.startswith(p):
            s = s[len(p):]
            break
    if s not in B.STR:
        B.STR[s] = compose(s)


# =========================================================================================
# 4. The answer frames of anaññātaññassāmītindriya / aññindriya
#    'Yā tesaṃ dhammānaṃ … sacchikiriyāya S – idaṃ tasmiṃ samaye X hoti.' (like the jīvitindriya
#    frame: no «tasmiṃ samaye» before the string) = «Điều <G>, tức là S – đây là X vào lúc ấy.»
# =========================================================================================
REALIZE = "nhằm tự mình chứng nghiệm những hiện tượng ấy, vốn"   # tesaṃ dhammānaṃ … sacchikiriyāya
G_ANANNATA_P = "tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya"
G_ANNA_P = "tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya"
_KNOWN = ["được biết", "được thấy", "được đạt đến", "được nhận biết", "được tự mình chứng nghiệm"]
G_ANANNATA = REALIZE + " " + ", ".join("chưa " + w for w in _KNOWN)
G_ANNA = REALIZE + " " + ", ".join("đã " + w for w in _KNOWN)
GQ = {G_ANANNATA_P: G_ANANNATA, G_ANNA_P: G_ANNA}
KRE = re.compile(r"Yā (tesaṃ dhammānaṃ .+? sacchikiriyāya) (.+?)( – |, )((?:idaṃ|ayaṃ) tasmiṃ samaye .+)$")


def rest_vi(rest):
    """'idaṃ tasmiṃ samaye X hoti…pe… Y hoti…pe… ye vā pana … – ime dhammā kusalā.'"""
    out = []
    for i, p in enumerate(re.split(r"(…pe…\s*)", rest)):
        if i % 2:
            out.append(p.replace(PE, ELL))
        elif p:
            m = re.fullmatch(r"(\S+) hoti", p)
            out.append(B.there_vi(m.group(1)) if m else B.tail_vi(p))
    return "".join(out)


def realize_qa(line):
    m = B.QRE.fullmatch(line)
    name, _, mark, rest = m.groups()
    k = KRE.fullmatch(rest)
    if not (mark == "?" and k):
        return None
    g, s, sep, tail = k.groups()
    register(s)
    sep = f" {DASH} " if sep.strip() == DASH else ", "   # ^1-364: the Pāli has «,» (kept)
    return f"{B.q_vi(name)}? Điều {GQ[g]}, tức là {B.STR[s]}{sep}" + rest_vi(tail)


# =========================================================================================
# 5. Opening sentences: intros for B.kusala_vi, and the qualifiers suññataṃ / appaṇihitaṃ
# =========================================================================================
PERSON = "Vào lúc một người tu tập"   # Yasmiṃ samaye … bhāveti (as B.PERSON)
assert B.PERSON.startswith(PERSON + " ")
J_LOK = f"tầng thiền {LOK}"            # lokuttaraṃ jhānaṃ
GOAL = "để đạt đến giai đoạn thứ"       # … bhūmiyā pattiyā
NOREST = "dứt bỏ không còn sót lại"     # anavasesappahānāya
KAMARAGA = "sự tham đắm dục lạc và ác ý"   # kāmarāgabyāpādā
STAGE_P = {
    1: "diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā",
    2: "kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā",
    3: "kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā",
    4: "rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā",
}
STAGE = {
    1: f"nhằm dứt bỏ sự mắc kẹt trong các quan điểm, {GOAL} nhất",
    2: f"nhằm làm suy yếu {KAMARAGA}, {GOAL} hai",
    3: f"nhằm {NOREST} {KAMARAGA}, {GOAL} ba",
    4: (f"nhằm {NOREST} sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, "
        f"sự xao động và vô minh, {GOAL} tư"),
}
LEAD_P = "niyyānikaṃ apacayagāmiṃ"
TWENTY_P = ["maggaṃ", "satipaṭṭhānaṃ", "sammappadhānaṃ", "iddhipādaṃ", "indriyaṃ", "balaṃ", "bojjhaṅgaṃ",
            "saccaṃ", "samathaṃ", "dhammaṃ", "khandhaṃ", "āyatanaṃ", "dhātuṃ", "āhāraṃ", "phassaṃ", "vedanaṃ",
            "saññaṃ", "cetanaṃ", "cittaṃ"]
TWENTY_V = ["con đường", "sự thiết lập tỉnh thức", "nỗ lực đúng đắn", "nền tảng thần thông", "năng lực",
            "sức mạnh", "chi phần giác ngộ", "sự thật", C.N["samatho"], "hiện tượng", "khối",
            "lĩnh vực nhận biết", "yếu tố", "dưỡng chất", C.N["phasso"], C.N["vedanā"], C.N["saññā"],
            C.N["cetanā"], C.N["cittaṃ"]]
assert len(TWENTY_P) == len(TWENTY_V) == 19
NEW_INTROS = [(f"lokuttaraṃ jhānaṃ bhāveti {LEAD_P} {STAGE_P[n]} ", f"{PERSON} {J_LOK}, {LEADS}, {STAGE[n]}, ")
              for n in (1, 2, 3, 4)]
NEW_INTROS.append((
    (PE + " ").join(f"lokuttaraṃ {o} bhāveti" for o in TWENTY_P) + f" {LEAD_P} {STAGE_P[1]} ",
    f"{PERSON} " + (ELL + " tu tập ").join(f"{o} {LOK}" for o in TWENTY_V) + f", {LEADS}, {STAGE[1]}, "))
for p, _ in NEW_INTROS:
    assert not any(p.startswith(q) or q.startswith(p) for q, _ in B.INTROS), p
B.INTROS.extend(NEW_INTROS)

SUNNATA_Q = "với tính chất trống rỗng"         # suññataṃ (qualifies the absorption)
APPANIHITA_Q = "với tính chất không mong cầu"  # appaṇihitaṃ
add(B.PH, {"suññataṃ": SUNNATA_Q, "appaṇihitaṃ": APPANIHITA_Q})
assert B.PH_MAX >= 1

# =========================================================================================
# 6. Headings and closing lines (headings verbatim from vi-zeroshot-terms.md)
# =========================================================================================
HEAD = {
    "Suddhikapaṭipadā": "Cách thực hành đơn thuần",
    "Suññataṃ": "Sự trống rỗng",
    "Suññatamūlakapaṭipadā": "Cách thực hành dựa trên sự trống rỗng",
    "Appaṇihitaṃ": "Sự không mong cầu",
    "Appaṇihitamūlakapaṭipadā": "Cách thực hành dựa trên sự không mong cầu",
    "Vīsati mahānayā": "Hai mươi phương pháp lớn",
    "Adhipati": "Yếu tố chủ đạo",
}
NEW_EXACT = {"#### Lokuttarakusalaṃ": f"#### Tâm thiện {LOK}"}
for p, v in HEAD.items():
    NEW_EXACT[f"##### {p}"] = f"##### {v}"
    NEW_EXACT[f"{p}."] = f"{v}."
for p, v in zip(("Paṭhamo", "Dutiyo", "Tatiyo", "Catuttho"), ("nhất", "hai", "ba", "tư")):
    NEW_EXACT[f"{p} maggo."] = f"Con đường thứ {v}."
NEW_EXACT["Lokuttaraṃ cittaṃ."] = f"Tâm {LOK}."
add(B.EXACT, NEW_EXACT)


# =========================================================================================
# 7. Line dispatch and build
# =========================================================================================
def translate_line(line):
    if line not in B.EXACT and B.QRE.fullmatch(line):
        r = realize_qa(line)
        if r is not None:
            return r
        a = B.QRE.fullmatch(line).group(4)
        m = B.ARE.fullmatch(a)
        if m:
            register(m.group(1))
    return B.translate_line(line)


def render(segs):
    out = []
    for bid, lines in segs:
        vi = [B.cap(translate_line(l)) for l in lines]
        for p, r in zip(lines, vi):
            B.check_line(p, r)
        vi[-1] += f" ^{bid}"
        out.append("\n".join(vi))
    return out


def earlier_pairs():
    """Pāli line -> published Vietnamese line, from the finished parts 2-01 and 2-02"""
    pairs = {}
    for name in ("2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"):
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
    # identical Pāli = identical Vietnamese across the parts
    prev = earlier_pairs()
    shared = 0
    for (bid, pl), seg in zip(segs, out):
        vl = re.sub(r" \^[0-9A-Za-z-]+$", "", seg).split("\n")
        for p, v in zip(pl, vl):
            if p in prev:
                assert prev[p] == v, (bid, p[:80], v[:120], prev[p][:120])
                shared += 1
    return text, len(segs), shared


if __name__ == "__main__":
    print("headings equal the terms file:", B.check_headings())
    text, n, shared = build()
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and ":-" not in text
    (OUT_DIR / PART).write_bytes(text.encode("utf-8"))
    print("wrote", OUT_DIR / PART, n, "segments;", shared, "lines identical to the same Pāli in 2-01/2-02")
