# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 10: 10-navakapuggalapannatti.md (Navakapuggalapaññatti).

Imports the approved sample builder (names, frames, headings, closers) and the finished ch7 builder (sammāsambuddha /
paccekasambuddha clauses of matrix item ^4-M-12, identical Pāli «…abhisambujjhati, tattha ca sabbaññutaṃ pāpuṇāti
balesu ca vasībhāvaṃ»). The nine definitions repeat the ch2 / ch4 / ch5 / ch7 strings byte for byte; only the
punctuation follows this chapter's Pāli (commas instead of semicolons, no dash, names not in quotes).
run:  python -I -X utf8 build_10_vi.py
Asserts: cross-book strings occur in the pi-1 / pi-2 rails; the shared clauses occur in the ch2 / ch4 / ch5 / ch7
outputs; every person name used equals B.NAME; the names appear in the output; no dash at all.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_7_vi as C7  # noqa: E402  (import only reads 1-matika.md, writes nothing)

N = B.NAME
cap, q = B.cap, B.q
IDHE = B.IDHEKACCO                                   # Ở đời này, có người

NINE = ["sammāsambuddho", "paccekasambuddho", "ubhatobhāgavimutto", "paññāvimutto", "kāyasakkhī",
        "diṭṭhippatto", "saddhāvimutto", "dhammānusārī", "saddhānusārī"]   # matrix ^4-M-14 (1), in order


def close_plain(name):                               # Ayaṃ vuccati puggalo X. (no dash, no quotes; ch4 / ch8 style)
    return f"Người này được gọi là {name}."


# ---------------------------------------------------------------- clauses (sample / ch2 / ch4 / ch5 / ch7 strings)
SAMMA = C7.C1                                        # … abhisambujjhati, tattha ca sabbaññutaṃ … vasībhāvaṃ (ch7)
PACCEKA = C7.C2                                      # … abhisambujjhati, na ca tattha … na ca balesu vasībhāvaṃ (ch7)
VIM_ALL = f"{B.VIMOKKHA}, {B.PANNAYA_ALL}"           # … viharati paññāya cassa disvā āsavā parikkhīṇā honti
VIM_SOME = f"{B.VIMOKKHA}, {B.PANNAYA_SOME}"         # … viharati paññāya cassa disvā ekacce āsavā … (ch4 ^4-95)
TRUTH_FIRST = "hiểu rõ đúng như thật: “Đây là khổ đau”"                       # "idaṃ dukkha"nti yathābhūtaṃ pajānāti
TRUTH_LAST = "hiểu rõ đúng như thật: “Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”"   # "ayaṃ … paṭipadā"ti …
TRUTHS_PE = f"{TRUTH_FIRST}… {TRUTH_LAST}"           # …pe… abbreviation (ch5 ^4-… «“Đây là khổ đau”… hiểu rõ …»)
TATHAGATA_NP = B.TATHAGATA_DHAMMA[:-1]               # tathāgatappaveditā cassa dhammā … vocaritā (ch4)
DITTHI_BODY = f"{TRUTHS_PE}, {TATHAGATA_NP}, {B.PANNAYA_SOME}"
NO_CA_KHO = f", nhưng không được như ở {N['diṭṭhippatto']}"   # no ca kho yathā diṭṭhippattassa (ch2 / ch4)
SOTA = B.PATIPANNO_FOR.format(x="vào dòng")


def anusari_head(ind):                               # Yassa puggalassa … adhimattaṃ hoti, …vāhiṃ …pubbaṅgamaṃ … bhāveti
    return (f"{cap(SOTA)}, có năng lực {ind} vượt trội, tu tập con đường cao quý do {ind} dẫn dắt, "
            f"có {ind} đi trước")                    # ch2 ^4-29 / ^4-30


def anusari_tail(key, res):                          # Sotāpatti… paṭipanno puggalo X, phale ṭhito Y(ti).
    return f"{cap(SOTA)} là {N[key]}; khi đã đứng vững trong thành quả, người ấy là {N[res]}."   # ch2 ^4-29 / ^4-30


CH2 = (B.OUT_DIR / "2-ekakapuggalapannatti.md").read_text(encoding="utf-8")
CH4 = (B.OUT_DIR / "4-tikapuggalapannatti.md").read_text(encoding="utf-8")
CH5 = (B.OUT_DIR / "5-catukkapuggalapannatti.md").read_text(encoding="utf-8")
CH7 = (B.OUT_DIR / "7-chakkapuggalapannatti.md").read_text(encoding="utf-8")
MATIKA = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
CH2_CHECK = [f"{IDHE} {B.NA_HEVA_KHO} {B.VIMOKKHA}; {B.PANNAYA_ALL}", f"{IDHE} {B.VIMOKKHA}; {B.PANNAYA_ALL}",
             anusari_head("trí tuệ"), anusari_head("niềm tin"), anusari_tail("dhammānusārī", "diṭṭhippatto"),
             anusari_tail("saddhānusārī", "saddhāvimutto"), f"{cap(B.PANNAYA_SOME)}{NO_CA_KHO}"]
CH4_CHECK = [f"{IDHE} {VIM_SOME}", f"{B.SACCA_PAJANATI[:-1]}, {TATHAGATA_NP}, {B.PANNAYA_SOME}",
             f"{B.PANNAYA_SOME}{NO_CA_KHO}"]
CH5_CHECK = [TRUTHS_PE]
CH7_CHECK = [f"người nào {SAMMA}, ", f"người nào {PACCEKA}, "]

CROSS = [
    (1, "Tự Giác Ngộ Hoàn Toàn"), (2, "tám sự giải thoát"), (2, "hiểu rõ đúng như thật"), (2, "năng lực niềm tin"),
    (1, "con đường cao quý"), (2, "thành quả vào dòng"), (1, "tự mình chứng nghiệm"), (2, "Như Lai"),
    (2, "sự phát sinh của khổ đau"), (2, "cách thực hành dẫn đến sự chấm dứt khổ đau"),
]


def chapter():
    L = ["#### " + B.CHAPTER_HEADING[10]]
    L.append(f"{q(N['sammāsambuddho'])} {IDHE} {SAMMA}. {close_plain(N['sammāsambuddho'])}")
    L.append(f"{q(N['paccekasambuddho'])} {IDHE} {PACCEKA}. {close_plain(N['paccekasambuddho'])}")
    L.append(f"{q(N['ubhatobhāgavimutto'])} {IDHE} {VIM_ALL}. {close_plain(N['ubhatobhāgavimutto'])}")
    L.append(f"{q(N['paññāvimutto'])} {IDHE} {B.NA_HEVA_KHO} {VIM_ALL}. {close_plain(N['paññāvimutto'])}")
    L.append(f"{q(N['kāyasakkhī'])} {IDHE} {VIM_SOME}. {close_plain(N['kāyasakkhī'])}")
    L.append(f"{q(N['diṭṭhippatto'])} {IDHE} {DITTHI_BODY}. {close_plain(N['diṭṭhippatto'])}")
    L.append(f"{q(N['saddhāvimutto'])} {IDHE} {DITTHI_BODY}{NO_CA_KHO}. {close_plain(N['saddhāvimutto'])}")
    L.append(f"{q(N['dhammānusārī'])} {anusari_head('trí tuệ')}. {close_plain(N['dhammānusārī'])} "
             f"{anusari_tail('dhammānusārī', 'diṭṭhippatto')}")
    L.append(f"{q(N['saddhānusārī'])} {anusari_head('niềm tin')}. {close_plain(N['saddhānusārī'])} "
             f"{anusari_tail('saddhānusārī', 'saddhāvimutto')}")
    L.append(B.NIDDESA_CLOSER[9])
    return L


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    return len(CROSS)


def main():
    n = check_cross()
    for label, txt, checks in (("ch2", CH2, CH2_CHECK), ("ch4", CH4, CH4_CHECK), ("ch5", CH5, CH5_CHECK),
                               ("ch7", CH7, CH7_CHECK)):
        for s in checks:
            assert s in txt, f"{label} clause not found: " + s[:80]
    matrix_item = "(1) " + cap(B.names(*NINE)) + "."
    assert matrix_item in MATIKA, "matrix item ^4-M-14 (1) not found"
    lines = chapter()
    name = "10-navakapuggalapannatti.md"
    text = B.assemble(name, lines)
    (B.OUT_DIR / name).write_bytes(text.encode("utf-8"))
    # person names: equal to B.NAME (sample), asked and named once each
    assert N["sammāsambuddho"] == "bậc Tự Giác Ngộ Hoàn Toàn" and N["paccekasambuddho"] == "bậc Độc Giác"
    assert N["ubhatobhāgavimutto"] == "người được giải thoát theo cả hai cách"
    assert N["paññāvimutto"] == "người được giải thoát nhờ trí tuệ" and N["kāyasakkhī"] == "người chứng nghiệm bằng thân"
    assert N["diṭṭhippatto"] == "người đạt đến quan điểm" and N["saddhāvimutto"] == "người được giải thoát nhờ niềm tin"
    assert N["dhammānusārī"] == "người đi theo Giáo Pháp" and N["saddhānusārī"] == "người đi theo niềm tin"
    for p in NINE:
        assert text.count(f"Thế nào là {N[p]}?") == 1, p
        assert text.count(f"Người này được gọi là {N[p]}.") == 1, p
    assert text.count(f"{IDHE} ") == 7
    for bad in ("—", ":-", "chánh niệm", "….", "–", "là là", "“người", "“bậc"):
        assert bad not in text, bad
    # ch8 (other agent) repeats ^4-204 / the saddhānusārī line in identical Pāli: report, do not fail
    ch8p = B.OUT_DIR / "8-sattakapuggalapannatti.md"
    if ch8p.exists():
        ch8 = ch8p.read_text(encoding="utf-8")
        for ln in (lines[3], lines[9]):
            print("ch8 identical-line check:", "same" if ln in ch8 else "DIFFERS", "|", ln[:60])
    print(f"OK: cross-book strings {n}; clauses ch2 {len(CH2_CHECK)}, ch4 {len(CH4_CHECK)}, ch5 {len(CH5_CHECK)}, "
          f"ch7 {len(CH7_CHECK)}; matrix item 1; wrote {name} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
