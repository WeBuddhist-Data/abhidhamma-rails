# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 7: 7-chakkapuggalapannatti.md (Chakkapuggalapaññatti).

Imports the approved sample builder (names, frames, headings, closers) and the finished ch4 builder (Tatra yvāyaṃ
frame, Sotāpannasakadāgāmino); every clause is a fixed string taken from the approved matrix item ^4-M-12
(1-matika.md, Chakkauddeso (1)), so the definitions repeat the matrix byte for byte.
run:  python -I -X utf8 build_7_vi.py
Asserts: cross-book strings occur in the pi-1 / pi-2 rails; the clauses occur in the Vietnamese matrix item;
every person name used equals B.NAME / the ch4 constant; the names appear in the output.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4  # noqa: E402  (import only reads 1-matika.md, writes nothing)

N = B.NAME
TATRA = C4.TATRA                                   # Tatra yvāyaṃ … = «Trong số đó, … nào …» (ch4)
DATTHABBO = "thì cần hiểu người ấy là {x}"         # X tena daṭṭhabbo / daṭṭhabbā (ch4 «thì cần hiểu bậc đạo sư ấy là X»)
assert C4.DATTHABBO.replace("bậc đạo sư ấy", "người ấy") == DATTHABBO
SOTA_SAKA = C4.SOTA_SAKA[:1].lower() + C4.SOTA_SAKA[1:]   # sotāpannasakadāgāmino (ch4)
SARIPUTTA = "Xá-lợi-phất và Mục-kiền-liên"         # sāriputtamoggallānā (new)
AVASESA_ARAHANTA = "các bậc A-la-hán còn lại"      # avasesā arahantā (pi-2 arahanto «các bậc A-la-hán»; ch2 avasesā «còn lại»)
EVAMUPARIPI = ", cũng vậy ở các chỗ sau"           # evamuparipi inside a variant bracket (pi-2)

# ---------------------------------------------------------------- clauses of matrix item ^4-M-12 (sample constants)
AN, NA_AN = B.ANANUSSUTA, B.NA_ANANUSSUTA
DD, DK = B.DITTHEVA_DHAMME, B.DUKKHASSANTAKARO
SAVAKA = "đạt đến sự toàn hảo của hàng đệ tử"      # sāvakapāramiṃ pāpuṇāti (matrix)
ITTHATTA = "trạng thái này"                        # itthattaṃ (matrix)
C1 = f"{AN}, và ở đó {B.SABBANNUTA} và {B.VASIBHAVA}"
C2 = f"{AN}, nhưng ở đó không {B.SABBANNUTA}, cũng không đạt đến {B.VASIBHAVA}"
C3_HEAD = f"{NA_AN}, nhưng {DD} là {DK}"
C3_TAIL = f"và {SAVAKA}"
C4_ = f"{NA_AN}, {DD} là {DK}, nhưng không {SAVAKA}"
C5 = f"{NA_AN}, và {DD} không phải {DK}, mà là {N['anāgāmī']}, không còn trở lại {ITTHATTA}"
C6 = f"{NA_AN}, và {DD} không phải {DK}, mà còn trở lại {ITTHATTA}"

MATIKA = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
MATRIX_CHECK = [
    f"(1) Có người {C1} [dị bản (Pī.): phalesu]. ",
    f". Có người {C2}. ",
    f". Có người {C3_HEAD} {C3_TAIL}. ",
    f". Có người {C4_}. ",
    f". Có người {NA_AN}, và {DD} không phải {DK}, mà là {N['anāgāmī']}, không còn trở lại "
    f"[dị bản (Syā., Ka.): anāgantvā; Tăng Chi Bộ Kinh 4.171] {ITTHATTA}. ",
    f"còn trở lại {ITTHATTA}.",
]

CROSS = [
    (2, EVAMUPARIPI + "]"), (2, "các bậc A-la-hán"), (2, "Tự Giác Ngộ Hoàn Toàn"),
]


def line(clause, who):
    return f"{TATRA} người nào {clause}, {DATTHABBO.format(x=who)}."


def chapter():
    L = ["#### " + B.CHAPTER_HEADING[7]]
    L.append(line(C1, N["sammāsambuddho"]))
    L.append(line(C2, N["paccekasambuddho"]))
    L.append(line(f"{C3_HEAD} [dị bản (Sī.): dukkhassantaṃ karoti{EVAMUPARIPI}], {C3_TAIL}", SARIPUTTA))
    L.append(line(C4_, AVASESA_ARAHANTA))
    L.append(line(C5, N["anāgāmī"]))
    L.append(line(C6, SOTA_SAKA))
    L.append(B.NIDDESA_CLOSER[6])
    return L


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    return len(CROSS)


def main():
    n = check_cross()
    for m in MATRIX_CHECK:
        assert m in MATIKA, "matrix clause not found: " + m[:80]
    lines = chapter()
    name = "7-chakkapuggalapannatti.md"
    text = B.assemble(name, lines)
    (B.OUT_DIR / name).write_bytes(text.encode("utf-8"))
    # person names: equal to B.NAME (sample) and present in the output
    assert N["sammāsambuddho"] == "bậc Tự Giác Ngộ Hoàn Toàn" and N["paccekasambuddho"] == "bậc Độc Giác"
    assert N["anāgāmī"] == "bậc không trở lại"
    assert SOTA_SAKA == f"các {N['sotāpanno']} và các {N['sakadāgāmī']}"
    for nm in (N["sammāsambuddho"], N["paccekasambuddho"], N["anāgāmī"], SOTA_SAKA, SARIPUTTA, AVASESA_ARAHANTA):
        assert f"thì cần hiểu người ấy là {nm}." in text, nm
    assert text.count(TATRA + " người nào ") == 6
    for bad in ("—", ":-", "chánh niệm", "….", "–"):
        assert bad not in text, bad
    print(f"OK: cross-book strings {n}; matrix clauses {len(MATRIX_CHECK)}; wrote {name} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
