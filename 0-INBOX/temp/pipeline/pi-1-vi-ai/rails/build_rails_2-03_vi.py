"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapter 2-03 (the world-transcending wholesome mind, ^1-1-5-0 … ^1-364).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/2-03-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-2-03.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_vi.py (S) and build_rails_2-01_2-02_vi.py (B). B's tables (NAMES, STR, PIECES, INTROS,
EXACT) are extended in memory with the new 2-03 material below, so every passage 2-03 shares with 2-01/2-02
(definitions, synonym strings, jhāna formulas, modes of progress, counted names, the ṭhapetvā line, the
«ye vā pana» tail) comes out byte-identical. A check rebuilds 2-01 and 2-02 in memory with the extended
tables and requires them to equal the finished files byte for byte.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.
Later chapter builders may import this file (importing writes nothing).

usage: python -I -X utf8 build_rails_2-03_vi.py
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

_spec = importlib.util.spec_from_file_location("build_rails_2_01_2_02_vi", HERE / "build_rails_2-01_2-02_vi.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)        # importing writes nothing

PART = "2-03-cittuppadakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
TS = S.TS
cap = S.cap

# =========================================================================================
# 1. New names (nominative)
# =========================================================================================
NEW_NAMES = {
    "anaññātaññassāmītindriyaṃ": "năng lực biết được điều chưa từng biết",
    "aññindriyaṃ": "năng lực hiểu biết trọn vẹn",
    "sammāvācā": "lời nói đúng đắn",
    "sammākammanto": "hành động đúng đắn",      # no termbase entry for kammanta (see notes)
    "sammāājīvo": "sinh kế đúng đắn",
    "navindriyāni": "chín năng lực",
    "aṭṭhaṅgiko maggo": "con đường gồm tám chi phần",
}
for _k in NEW_NAMES:
    assert _k not in B.NAMES, _k
B.NAMES.update(NEW_NAMES)

# =========================================================================================
# 2. Synonym strings: bases + appended items (each appended item is one more «, » item)
# =========================================================================================
MAGGA_P = "maggaṅgaṃ maggapariyāpannaṃ"
MAGGA_V = "chi phần của con đường, nằm trong con đường"
ABST_P = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
ABST_V = ("sự kiêng tránh, sự kiêng tránh hoàn toàn, sự kiềm chế, sự không làm, sự không thực hiện, "
          "sự không rơi vào lỗi vi phạm, sự không vượt quá giới hạn, sự phá bỏ cây cầu")
ARATI = "sự tránh xa"
S_CETANA_TAJJA = S.S_CETANA.replace(" " + S.reading("Syā.", "sañcetayitattaṃ"), "")   # no variant here
assert "[" not in S_CETANA_TAJJA and S_CETANA_TAJJA.startswith(f"chủ ý {S.TAJJA}, ")
NEW_BASES = {
    "tajjāmanoviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ": S_CETANA_TAJJA,
    "catūhi vacīduccaritehi " + ABST_P: f"{ARATI} bốn hành vi xấu bằng lời nói, {ABST_V}",
    "tīhi kāyaduccaritehi " + ABST_P: f"{ARATI} ba hành vi xấu bằng thân, {ABST_V}",
    "micchāājīvā " + ABST_P: f"{ARATI} sinh kế sai lầm, {ABST_V}",
    # the kāya/citta strings of the sample (^1-40 … ^1-51), here without variants
    "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ": S.S_PASSADDHI,
    "lahutā lahupariṇāmatā adandhanatā avitthanatā": S.S_LAHUTA,
    "mudutā maddavatā akakkhaḷatā akathinatā": S.S_MUDUTA,
    "kammaññatā kammaññattaṃ kammaññabhāvo": S.S_KAMMANNATA,
    "paguṇatā paguṇattaṃ paguṇabhāvo": S.S_PAGUNATA,
    "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā": S.S_UJUKATA,
}
for _k in NEW_BASES:
    assert _k not in B.STR, _k
SBJ = "chi phần giác ngộ là"                     # X-sambojjhaṅgo = «chi phần giác ngộ là X»
SUFFIX = {
    MAGGA_P: MAGGA_V,
    "pītisambojjhaṅgo": f"{SBJ} sự hân hoan",
    "samādhisambojjhaṅgo": f"{SBJ} định tâm",
    "vīriyasambojjhaṅgo": f"{SBJ} sự tinh tấn",
    "satisambojjhaṅgo": f"{SBJ} sự tỉnh thức",
    "dhammavicayasambojjhaṅgo": f"{SBJ} sự tìm hiểu các hiện tượng",
    "passaddhisambojjhaṅgo": f"{SBJ} sự an tịnh",
    "sammāvācā": NEW_NAMES["sammāvācā"],
    "sammākammanto": NEW_NAMES["sammākammanto"],
    "sammāājīvo": NEW_NAMES["sammāājīvo"],
}
COMPOSED = {}     # Pāli string -> Vietnamese, every composed string actually used (for the notes)


def compose(pi, table):
    """longest base of `table`, then appended items -> (base Vietnamese, [appended Vietnamese])"""
    bases = [k for k in table.keys() if pi.startswith(k + " ")]
    if not bases:
        raise KeyError("no base for: " + pi)
    base = max(bases, key=len)
    out, rest = [], pi[len(base):].strip()
    while rest:
        for t in sorted(SUFFIX, key=len, reverse=True):
            if rest == t or rest.startswith(t + " "):
                out.append(SUFFIX[t])
                rest = rest[len(t):].strip()
                break
        else:
            raise KeyError(f"unknown appended item at {rest!r} in {pi!r}")
    return dict.__getitem__(table, base), out


class StrTable(dict):
    """B.STR plus composition: longest base, then appended items, joined by «, »."""

    def __missing__(self, pi):
        base, items = compose(pi, self)
        COMPOSED[pi] = ", ".join([base] + items)
        return COMPOSED[pi]


B.STR = StrTable(B.STR)
B.STR.update(NEW_BASES)

# =========================================================================================
# 3. Definitions B does not cover: the kāya/citta frame and the two «tesaṃ dhammānaṃ» faculties
# =========================================================================================
KAYA_RE = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti\? Yā tasmiṃ samaye "
                     r"(vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa|viññāṇakkhandhassa) (.+?) – "
                     r"(?:ayaṃ|idaṃ) tasmiṃ samaye (\S+) hoti\.")
GEN = {"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa": S.KAYA_GEN,
       "viññāṇakkhandhassa": S.CITTA_GEN}


def kaya_vi(m):
    """«của khối …» follows the base string; the appended sambojjhaṅga item comes after it"""
    f, gen, s, f2 = m.groups()
    assert f == f2
    base, items = compose(s, B.STR) if s not in B.STR else (B.STR[s], [])
    bod = ", ".join([S.body(base, GEN[gen])] + items)
    COMPOSED.setdefault(f"{gen} {s}", bod[len(f"{S.REL} {TS} là "):])
    return S.definition(f, bod)


ANN_P = {"anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ":
         "chưa được biết, chưa được thấy, chưa được đạt đến, chưa được nhận biết và chưa được tự mình chứng nghiệm",
         "ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ":
         "đã được biết, đã được thấy, đã được đạt đến, đã được nhận biết và đã được tự mình chứng nghiệm"}
ANN_RE = re.compile(r"Katamaṃ tasmiṃ samaye (\S+) hoti\? Yā tesaṃ dhammānaṃ (" + "|".join(ANN_P)
                    + r") sacchikiriyāya (.+?)(,| –) (idaṃ tasmiṃ samaye .*)$")
ANN_LEAD = S.REL + ", để tự mình chứng nghiệm những hiện tượng ấy vốn {}, là {}"
AVIKKHEPO_P = "avikkhepo hoti"


def ann_vi(m):
    f, adj, s, sep, rest = m.groups()
    # ^1-364: «…pe… avikkhepo hoti…pe…» inside the tail = «… có sự không tán loạn…»
    rest = rest.replace(AVIKKHEPO_P, B.there_list(AVIKKHEPO_P))
    return (B.q_vi(f, "hoti") + "? " + ANN_LEAD.format(ANN_P[adj], B.STR[s])
            + ("," if sep == "," else " –") + " " + B.tail_vi(rest))


# =========================================================================================
# 4. «Katame dhammā kusalā? Yasmiṃ samaye lokuttaraṃ …» openings
# =========================================================================================
LEAD_P = "niyyānikaṃ apacayagāmiṃ"
LEAD_V = "dẫn đến giải thoát và dẫn đến sự giảm trừ"
STAGES = [   # (Pāli, Vietnamese) purpose phrases of the four paths
    ("diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā",
     "để dứt bỏ sự mắc kẹt trong các quan điểm, để đạt đến giai đoạn thứ nhất"),
    ("kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā",
     "để làm suy yếu sự tham đắm dục lạc và ác ý, để đạt đến giai đoạn thứ hai"),
    ("kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā",
     "để dứt bỏ sự tham đắm dục lạc và ác ý không còn sót lại, để đạt đến giai đoạn thứ ba"),
    ("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā",
     "để dứt bỏ sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động "
     "và vô minh không còn sót lại, để đạt đến giai đoạn thứ tư"),
]
WHO = "Vào lúc một người"
DEV = "tu tập"                                   # bhāveti
LOK = "vượt thế gian"                            # lokuttaraṃ
LOK_JH_V = f"tầng thiền {LOK} {LEAD_V}"
LOK_CITTA_V = f"tâm {LOK} {LEAD_V}"
TWENTY = [   # the «vīsati mahānayā»: what is developed (termbase phrase entries «lokuttaraṃ X»)
    ("maggaṃ", "con đường"),
    ("satipaṭṭhānaṃ", "sự thiết lập tỉnh thức"),
    ("sammappadhānaṃ", "nỗ lực đúng đắn"),          # APPROVED: sammappadhāna = sammāvāyāma
    ("iddhipādaṃ", "nền tảng thần thông"),
    ("indriyaṃ", "năng lực"),
    ("balaṃ", "sức mạnh"),
    ("bojjhaṅgaṃ", "chi phần giác ngộ"),
    ("saccaṃ", "sự thật"),
    ("samathaṃ", "sự tĩnh lặng"),
    ("dhammaṃ", "hiện tượng"),
    ("khandhaṃ", "khối"),
    ("āyatanaṃ", "lĩnh vực nhận biết"),
    ("dhātuṃ", "yếu tố"),
    ("āhāraṃ", "dưỡng chất"),
    ("phassaṃ", "sự tiếp xúc"),
    ("vedanaṃ", "cảm giác"),
    ("saññaṃ", "tri giác"),
    ("cetanaṃ", "chủ ý"),
]
TWENTY_P = "…pe… ".join(f"lokuttaraṃ {p} bhāveti" for p, _ in TWENTY) + "…pe… "
TWENTY_V = "… ".join(f"{DEV} {r} {LOK}" for _, r in TWENTY) + "… "
NEW_INTROS = {}
for _p, _r in STAGES:
    NEW_INTROS[f"lokuttaraṃ jhānaṃ bhāveti {LEAD_P} {_p} "] = f"{WHO} {DEV} {LOK_JH_V}, {_r}, "
NEW_INTROS[f"{TWENTY_P}lokuttaraṃ cittaṃ bhāveti {LEAD_P} {STAGES[0][0]} "] = (
    f"{WHO} {TWENTY_V}{DEV} {LOK_CITTA_V}, {STAGES[0][1]}, ")
for _k in NEW_INTROS:
    assert _k not in B.INTROS, _k
B.INTROS.update(NEW_INTROS)

# descriptions of the absorption (after the jhāna, joined with «, »)
NEW_DESC = {"suññataṃ": "có tính chất trống rỗng", "appaṇihitaṃ": "có tính chất không mong cầu"}
for _k, _v in NEW_DESC.items():
    assert _k not in B.PIECES
    B.PIECES[_k] = [_v]

# =========================================================================================
# 5. Headings and closing lines
# =========================================================================================
PP = "Cách thực hành"
H = {
    "Suddhikapaṭipadā": f"{PP} đơn thuần",
    "Suññataṃ": "Tính chất trống rỗng",
    "Suññatamūlakapaṭipadā": f"{PP} dựa trên sự trống rỗng",
    "Appaṇihitaṃ": "Tính chất không mong cầu",
    "Appaṇihitamūlakapaṭipadā": f"{PP} dựa trên sự không mong cầu",
    "Vīsati mahānayā": "Hai mươi phương pháp lớn",
    "Adhipati": "Yếu tố chủ đạo",
}
NEW_EXACT = {"#### Lokuttarakusalaṃ": f"#### Tâm thiện {LOK}"}
for _p, _r in H.items():
    NEW_EXACT[f"##### {_p}"] = f"##### {_r}"
    NEW_EXACT[f"{_p}."] = f"{_r}."
NEW_EXACT.update({
    "Paṭhamo maggo.": "Con đường thứ nhất.",
    "Dutiyo maggo.": "Con đường thứ hai.",
    "Tatiyo maggo.": "Con đường thứ ba.",
    "Catuttho maggo.": "Con đường thứ tư.",
    "Lokuttaraṃ cittaṃ.": f"Tâm {LOK}.",
})
for _k in NEW_EXACT:
    assert _k not in B.EXACT, _k
B.EXACT.update(NEW_EXACT)


# =========================================================================================
# 6. Line dispatch, render, build
# =========================================================================================
def translate_line(line):
    if line in B.EXACT:
        return B.EXACT[line]
    m = KAYA_RE.fullmatch(line)
    if m:
        return kaya_vi(m)
    m = ANN_RE.fullmatch(line)
    if m:
        return ann_vi(m)
    return B.translate_line(line)


def render(segs):
    blocks = []
    for sid, plines in segs:
        vlines = []
        for p in plines:
            v = unicodedata.normalize("NFC", cap(translate_line(p)))
            B.check_vi(v)
            assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
            assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
            assert p.count("…pe…") <= v.count("…"), ("pe", sid)
            assert p.endswith("?") == v.endswith("?"), ("question", sid)
            assert "  " not in v and " ," not in v and ",," not in v and "..." not in v, ("spacing", sid, v)
            vlines.append(v)
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def check_earlier_unchanged():
    """The extended tables must leave 2-01 and 2-02 exactly as finished."""
    for fn_name, fn in (("2-01-cittuppadakandam.md", B.build_2_01), ("2-02-cittuppadakandam.md", B.build_2_02)):
        text, _ = fn()
        assert unicodedata.normalize("NFC", text) == (S.OUT / fn_name).read_bytes().decode("utf-8"), fn_name
    print("2-01, 2-02: rebuilt in memory with the 2-03 tables, byte-identical to the finished files")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Vietnamese rails: new formulas of 2-03", "",
         "Generated by build_rails_2-03_vi.py from its fixed strings; import that file instead of retyping. "
         "Strings already in vi-rails-formulas.md or notes-2-01_2-02.md are not repeated. Format: Pāli = tiếng Việt.",
         "", "## Frames", "",
         "Katamo/Katamā/Katamaṃ tasmiṃ samaye F hoti? Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa "
         f"saṅkhārakkhandhassa S X-sambojjhaṅgo – … = {B.q_vi('phasso', 'hoti').replace('sự tiếp xúc', 'F')}? "
         f"{S.body('S', S.KAYA_GEN)}, {SBJ} X – đó là F {TS}.",
         f"… Yā tasmiṃ samaye viññāṇakkhandhassa S – … = … {S.body('S', S.CITTA_GEN)} – …",
         "Yā tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya S – = "
         + ANN_LEAD.format(ANN_P["anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ"], "S") + " –",
         "Yā tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya S, (^1-364, "
         "comma as written, no dash added) = "
         + ANN_LEAD.format(ANN_P["ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ"], "S") + ",",
         f"…pe… avikkhepo hoti…pe… (inside a tail, ^1-364) = … {B.there_list(AVIKKHEPO_P)}…",
         "", "## Openings of the world-transcending paths", ""]
    for p, r in NEW_INTROS.items():
        L.append(f"Yasmiṃ samaye {p.strip()} … = {r}…")
    L += [f"{LEAD_P} = {LEAD_V}",
          f"lokuttaraṃ jhānaṃ bhāveti {LEAD_P} = {DEV} {LOK_JH_V}"]
    for p, r in STAGES:
        L.append(f"{p} = {r}")
    for p, r in TWENTY:
        L.append(f"lokuttaraṃ {p} bhāveti = {DEV} {r} {LOK}")
    L += [f"lokuttaraṃ cittaṃ bhāveti {LEAD_P} = {DEV} {LOK_CITTA_V}",
          "", "### Descriptions of the absorption", ""]
    for p, r in NEW_DESC.items():
        L.append(f"{p} = {r}")
    L += ["dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ = " + B.chunks("dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ", B.PIECES)
          + " (two descriptions joined by «, »; the same for appaṇihitaṃ and for the four modes)",
          "", "## Synonym strings", ""]
    for p, r in NEW_BASES.items():
        L.append(f"{p} = {r}")
    L.append(f"{ABST_P} (after its object) = {ABST_V}")
    for p, r in SUFFIX.items():
        L.append(f"… {p} (appended item) = …, {r}")
    L += ["", "### Composed strings used in 2-03", ""]
    for p, r in COMPOSED.items():
        L.append(f"{p} = {r}")
    L += ["", "## Names", ""]
    for p, r in NEW_NAMES.items():
        L.append(f"{p} = {r}")
    L += ["", "## Headings and closing lines", ""]
    for p, r in NEW_EXACT.items():
        L.append(f"{p} = {r}")
    (HERE / "notes-2-03.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                        newline="\n")
    print("wrote", HERE / "notes-2-03.md")


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
