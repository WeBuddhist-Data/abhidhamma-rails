"""Builder for the Vietnamese rails of pi-3 chapter 9 (Aṭṭhamanayo, «Phương pháp thứ tám», ^3-317 .. ^3-318),
plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/9-atthamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/9-atthamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md: Samucchede
«sự phân tích», labbhati / labbhare «tìm thấy») and the approved ch9 frame of rails/vi-rails-formulas.md
(asserted). Shared strings are imported from build_rails_sample_vi (read-only). Elided items «Xena ye dhammā…»
use the ch3 / ch4 / ch5 / ch8 form «những hiện tượng nào cùng với X…» (identical Pāli). Verse words shared with
the ch7 verse (^3-305) and ch4 «atha» are kept identical. New strings: notes-rails-9.md.

usage: python -I -X utf8 build_rails_9_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "9-atthamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== frame pieces (approved ch3-15 formulas)
WHICH = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                  # X-ena on an elided item (as ch3 / ch4 / ch5 / ch8)
TE = "những hiện tượng ấy"                         # te dhammā
ASSOC = "gắn liền với"                             # sampayuttā
DISSOC = "không gắn liền với"                      # vippayuttā (+ instrumental)
NATTHI = "Không có."                               # Natthi.
Q_ASSOC = f"{ASSOC} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?"


def frame9(x_vi):
    """Xena ye dhammā vippayuttā, te dhammā katihi … sampayuttāti? Natthi."""
    return f"{WHICH} {DISSOC} {x_vi} {S.THEN} {TE} {Q_ASSOC} {NATTHI}"


# ================================================================== reference items in the instrumental
INSTR = {  # instrumental Pāli -> nominative key of S.NAMES (formula: names unchanged)
    "rūpakkhandhena": "rūpakkhandho", "vedanākkhandhena": "vedanākkhandho",
    "saññākkhandhena": "saññākkhandho", "saṅkhārakkhandhena": "saṅkhārakkhandho",
    "viññāṇakkhandhena": "viññāṇakkhandho",
}
ATTR = {"saraṇehi": "saraṇā", "araṇehi": "araṇā"}   # X-ehi dhammehi -> key of S.DHAMMA_ATTR
used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR[k[: -len(' dhammehi')]]]}"
    else:
        v = S.NAMES[INSTR[k]]
    used.append(v)
    return v


# ================================================================== segment grammar
YE = " ye dhammā"
SEG = re.compile(r"^(?P<subj>.*?) ye dhammā vippayuttā, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi "
                 r"sampayuttāti\? Natthi\.$")


def content_line(p):
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    items = [x.strip() for x in m.group("subj").replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        assert it.endswith(YE), it
        parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
    parts.append(frame9(ref_vi(items[-1])))
    return S.cap("… ".join(parts))


# ================================================================== summary verse (uddāna) of ^3-318, lines 2-6
SIXFOLD = "sáu lĩnh vực nhận biết"                 # saḷāyatanaṃ (pi-2, as ch7 verse)
NAMARUPA = "phần tinh thần và vật chất"            # nāmarūpaṃ (pi-2, termbase; as ch7 verse)
LIFE = "sự sống"                                   # jīvitaṃ (termbase; as ch7 verse)
ATHA = "rồi"                                       # atha (as ch4 verse «dasasvatha» = «Rồi trong mười nhóm»)
TIKE = f"trong các {S.low(S.SUB_HEADINGS['Tikaṃ'])}"   # tike = «trong các bộ ba» (as ch7 / ch8 tikesu)
NOT_FOUND = "không tìm thấy"                       # na labbhare / na labbhanti (APPROVED 2)
ANTARE = "phần xen giữa"                           # antare (termbase), as ch7 cūḷantare / mahantare
GOCCHAKE = "trong các nhóm"                        # gocchake (termbase «nhóm»), as ch7 gocchakesu
ANALYSIS = "sự phân tích"                          # Samucchede (APPROVED 3)
VERSE = {
    "Dhammāyatanaṃ dhammadhātu, atha jīvitaṃ nāmarūpaṃ;":
        f"{S.cap(S.NAMES['dhammāyatanaṃ'])}, {S.NAMES['dhammadhātu']}, {ATHA} {LIFE}, {NAMARUPA};",
    "Saḷāyatanaṃ jātijarāmataṃ, dve ca tike na labbhare.":
        f"{S.cap(SIXFOLD)}, {S.NAMES['jāti']}, {S.NAMES['jarā']} và {S.NAMES['maraṇaṃ']}, "
        f"và {S.NUM[2]} {TIKE} {NOT_FOUND}.",
    "Paṭhamantare satta ca, gocchake dasa aparante;":
        f"Và trong {ANTARE} {S.ORD[1]} có {S.NUM[7]}, {GOCCHAKE} có {S.NUM[10]}, trong {ANTARE} sau;",
    "Cuddasa cha ca matthake, iccete sattacattālīsa dhammā;":
        f"Có {S.NUM[14]}, và ở phần cuối có {S.NUM[6]}, như vậy bốn mươi bảy hiện tượng này;",
    "Samucchede na labbhanti, moghapucchakena cāti.":
        f"{S.cap(NOT_FOUND)} trong {ANALYSIS}, và vì câu hỏi rỗng.",
}
REUSE9 = [  # (Pāli, Vietnamese as reused, book)
    ("saḷāyatanaṃ (nāmarūpapaccayā saḷāyatanaṃ)", SIXFOLD, 2),
    ("nāmarūpaṃ", NAMARUPA, 2),
]


def translate_segment(lines):
    out = []
    for ln in lines:
        if ln.startswith("#"):
            out.append(S.heading_vi(ln))
        elif ln in S.CLOSINGS:
            out.append(S.CLOSINGS[ln])
        elif ln in VERSE:
            out.append(VERSE[ln])
        else:
            out.append(content_line(ln))
    return out


def render():
    blocks = []
    for lines, bid in S.pali_segments(S.PALI / NAME):
        vi = translate_segment(lines)
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


# ================================================================== checks
def _formula(key):
    txt = FORMULAS.read_text(encoding="utf-8")
    line = next(ln for ln in txt.splitlines() if ln.startswith(key))
    return line.split(" = ", 1)[1].replace(" (proposed for ch3-15)", "")


def check_formulas():
    f = _formula("Xena ye dhammā vippayuttā, te dhammā katihi … sampayuttāti? Natthi. (ch9)")
    got = S.cap(frame9("X"))
    assert got == f, f"ch9 frame differs:\n{got}\n{f}"
    # termbase / APPROVED words used in the verse
    tb = (S.ROOT / "AI_translation" / "vietnamese" / "pi-3-pali-vietnamese-termbase-plain.md").read_text(
        encoding="utf-8")
    for key, vi in [("labbhare", "tìm thấy"), ("labbhati", "tìm thấy"), ("mogha", "rỗng"),
                    ("pucchakena", "câu hỏi"), ("mataṃ", "sự chết"), ("jīvitaṃ", "sự sống"),
                    ("antare", "phần xen giữa"), ("gocchake", "nhóm"), ("nāmarūpaṃ", NAMARUPA),
                    ("sattacattālīsa dhammā", "bốn mươi bảy hiện tượng"), ("cuddasa", "mười bốn"),
                    ("dasa", "mười")]:
        line = next(ln for ln in tb.splitlines() if ln.startswith(f"{key}:"))
        assert line.rstrip().endswith(f": {vi}}}"), line
    appr = (S.RAILS.parent / "termbase" / "APPROVED.md").read_text(encoding="utf-8")
    assert f"«{ANALYSIS}»" in appr and "labbhati «tìm thấy»" in appr
    assert S.NAMES["maraṇaṃ"] == "sự chết"


def check_reuse9():
    t = {1: "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_DIR.glob("*.md"))).lower(),
         2: "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI2_DIR.glob("*.md"))).lower()}
    missing = [f"(pi-{b}) {p} = {v}" for p, v, b in REUSE9 if v.lower() not in t[b]]
    assert not missing, missing


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_reuse9()
    check_formulas()
    txt = render()
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    tagged = sorted({v for v in used if S.reuse_tag(v)})
    print(f"{NAME}: {n} segments; {len(set(used))} reference names ({len(tagged)} with pi-1/pi-2 tag); "
          f"{n_reuse + len(REUSE9)} pi-1/pi-2 strings asserted")
