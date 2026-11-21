# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot, chapter 8: 8-sattakapuggalapannatti.md (Sattakapuggalapaññatti).

Imports the approved sample builder (names, frames, headings, closers) and the finished ch4 builder (arahant formula).
The seven water-persons are the approved matrix names ^4-M-13 (1) (B.SATTAKA_UDAKA) verbatim; the ubhatobhāga,
paññāvimutta … saddhānusārī clauses repeat ch2 / ch4 strings byte for byte.
run:  python -I -X utf8 build_8_vi.py
Asserts: cross-book strings occur in the pi-1 / pi-2 rails; the names occur in the Vietnamese matrix item; the shared
clauses occur in the ch2 / ch4 outputs; every person name used equals B.NAME / B.SATTAKA_UDAKA; no dash at all.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4  # noqa: E402  (import only reads 1-matika.md, writes nothing)

N = B.NAME
cap, q = B.cap, B.q
IDHE = B.IDHEKACCO                                   # Ở đời này, có người
SO = "Người ấy"                                      # So (pi-2 ^2-… «Người ấy»)
U = B.SATTAKA_UDAKA                                  # matrix ^4-M-13 (1) names, in order

# ---------------------------------------------------------------- frames (new, ch8)
KATHAM_Q = "Và như thế nào là {x}?"                  # Kathañca puggalo … hoti? (pi-2 Kathañca … «Và … như thế nào?»)
EVAM_CLOSE = "Như vậy là {x}."                       # Evaṃ puggalo … hoti. (pi-2 «Như vậy là …»)


def kq(x):
    return KATHAM_Q.format(x=x)


def ev(x):
    return EVAM_CLOSE.format(x=x)


# ---------------------------------------------------------------- the five good qualities
KUSALESU = "trong các hiện tượng thiện"              # kusalesu dhammesu (pi-2 NIYAMA)
SADDHA, HIRI, OTTAPPA, VIRIYA, PANNA = ("niềm tin", "sự biết hổ thẹn", "sự biết ghê sợ tội lỗi",
                                        "sự tinh tấn", "trí tuệ")   # pi-1 ^1-12, ^1-38, ^1-39, ^1-13 …, ^1-16
QUALITIES = (SADDHA, HIRI, OTTAPPA, VIRIYA, PANNA)
SADHU = "tốt thay"                                    # sāhu / sādhu


def ummujjati(v1="", v2=""):
    """Idhekacco puggalo ummujjati "sāhu saddhā kusalesu dhammesu, sādhu hirī … paññā kusalesu dhammesū"ti."""
    parts = [f"{SADHU} {SADDHA} {KUSALESU}", f"{SADHU}{v1} {HIRI} {KUSALESU}", f"{SADHU} {OTTAPPA} {KUSALESU}",
             f"{SADHU} {VIRIYA}{v2} {KUSALESU}", f"{SADHU} {PANNA} {KUSALESU}"]
    return f"{IDHE} trồi lên với ý nghĩ: “{cap(', '.join(parts))}”."


HAYATI = "không đứng yên, không tăng trưởng, mà chỉ suy giảm"   # neva tiṭṭhati no vaḍḍhati hāyatiyeva
THITA = "không suy giảm, không tăng trưởng, mà đứng yên"         # neva hāyati no vaḍḍhati ṭhitā/ṭhitaṃ hoti


def tassa(state):
    s = "; ".join(f"{x} ấy của người ấy {state}" for x in QUALITIES)
    return cap(s) + "."


# ---------------------------------------------------------------- fruits (sample / ch2 / ch4 strings)
SOTAPANNA = SO + B.SOTAPANNA_BASE[len(B.IDHEKACCO):] + "."       # So tiṇṇaṃ … sambodhiparāyano.
SAKADAGAMI_CORE = ("nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, sân hận và si mê, là "
                   f"{N['sakadāgāmī']}, chỉ trở lại thế gian này một lần rồi")              # ch2 ^4-34
SAKADAGAMI = f"{SO}, {SAKADAGAMI_CORE} trở thành {B.DUKKHASSANTAKARO}."  # … āgantvā dukkhassantakaro hoti.
ANAGAMI = SO + B.ANAGAMI_BASE[len(B.IDHEKACCO):]                    # So pañcannaṃ … tasmā lokā.
ARAHANT = f"{SO}, {C4.ARAHATTA}."                                   # So āsavānaṃ khayā … viharati. (ch4)

# ---------------------------------------------------------------- ^4-204 … ^4-206 (ch2 / ch4 clauses)
SOTA = B.PATIPANNO_FOR.format(x="vào dòng")
ANUSARI_HEAD = (f"{cap(SOTA)}, có năng lực niềm tin vượt trội, tu tập con đường cao quý do niềm tin dẫn dắt, "
                "có niềm tin đi trước")                                                    # ch2 ^4-30
ANUSARI_TAIL = (f"{cap(SOTA)} là {N['saddhānusārī']}; khi đã đứng vững trong thành quả, người ấy là "
                f"{N['saddhāvimutto']}.")                                                   # ch2 ^4-30


def close_plain(name):                         # Ayaṃ vuccati puggalo X. (no dash, no quotes; ch4 unquoted style)
    return f"Người này được gọi là {name}."


CH2 = (B.OUT_DIR / "2-ekakapuggalapannatti.md").read_text(encoding="utf-8")
CH4 = (B.OUT_DIR / "4-tikapuggalapannatti.md").read_text(encoding="utf-8")
MATIKA = (B.OUT_DIR / "1-matika.md").read_text(encoding="utf-8")
CH2_CHECK = [SAKADAGAMI_CORE, ANUSARI_HEAD, ANUSARI_TAIL, B.SOTAPANNA_BASE[len(B.IDHEKACCO):],
             B.ANAGAMI_BASE[len(B.IDHEKACCO):], f"{IDHE} {B.VIMOKKHA}; {B.PANNAYA_ALL}"]
CH4_CHECK = [C4.ARAHATTA, f"{IDHE} {B.VIMOKKHA}, {B.PANNAYA_SOME}"]

CROSS = [
    (2, KUSALESU), (1, "niềm tin"), (1, "sự biết hổ thẹn"), (1, "sự biết ghê sợ tội lỗi"), (1, "sự tinh tấn"),
    (1, "trí tuệ"), (1, "đen tối"), (1, "các hiện tượng bất thiện"), (2, "Như vậy là"), (2, "như thế nào?"),
    (2, "Người ấy"), (2, "tăng trưởng"),
]


def chapter():
    L = ["#### " + B.CHAPTER_HEADING[8]]
    # ^4-203 (7 lines)
    L.append(f"{kq(U[0])} {IDHE} mang các hiện tượng bất thiện hoàn toàn đen tối. {ev(U[0])}")
    L.append(f"{kq(U[1])} "
             + ummujjati(" [khác chính tả (Sī., Syā.): sāhu, cũng vậy ở cả ba chỗ]",
                         " [khác chính tả (Sī., Syā.): viriyaṃ]")
             + f" {tassa(HAYATI)} {ev(U[1])}")
    L.append(f"{kq(U[2])} {ummujjati()} {tassa(THITA)} {ev(U[2])}")
    L.append(f"{kq(U[3])} {ummujjati()} {SOTAPANNA} {ev(U[3])}")
    L.append(f"{kq(U[4])} {ummujjati()} {SAKADAGAMI} {ev(U[4])}")
    L.append(f"{kq(U[5])} {ummujjati()} {ANAGAMI} {ev(U[5])}")
    L.append(f"{kq(U[6])} {ummujjati()} {ARAHANT} {ev(U[6])}")
    # ^4-204
    L.append(f"{q(N['ubhatobhāgavimutto'])} {IDHE} {B.VIMOKKHA}, {B.PANNAYA_ALL}. "
             + close_plain(N['ubhatobhāgavimutto']))
    # ^4-205 (…pe… abbreviation; the Pāli ends «dhammānusārī ….», no question mark)
    L.append(f"Thế nào là {N['paññāvimutto']}… {N['kāyasakkhī']}… {N['diṭṭhippatto']}… {N['saddhāvimutto']}… "
             f"{N['dhammānusārī']}…")
    # ^4-206 (2 lines)
    L.append(f"{q(N['saddhānusārī'])} {ANUSARI_HEAD}. {close_plain(N['saddhānusārī'])} {ANUSARI_TAIL}")
    L.append(B.NIDDESA_CLOSER[7])
    return L


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    return len(CROSS)


def main():
    n = check_cross()
    for s in CH2_CHECK:
        assert s in CH2, "ch2 clause not found: " + s[:80]
    for s in CH4_CHECK:
        assert s in CH4, "ch4 clause not found: " + s[:80]
    matrix_item = f"(1) {B.TYPES_COUNT[7]} giống như {B.SIMILE['udaka']}. {cap(', '.join(U))}."
    assert matrix_item in MATIKA, "matrix item ^4-M-13 (1) not found"
    matrix_item2 = "(2) " + cap(B.names("ubhatobhāgavimutto", "paññāvimutto", "kāyasakkhī", "diṭṭhippatto",
                                         "saddhāvimutto", "dhammānusārī", "saddhānusārī")) + "."
    assert matrix_item2 in MATIKA, "matrix item ^4-M-13 (2) not found"
    lines = chapter()
    name = "8-sattakapuggalapannatti.md"
    text = B.assemble(name, lines)
    (B.OUT_DIR / name).write_bytes(text.encode("utf-8"))
    # person names: equal to the sample constants and present in the output
    assert len(U) == 7
    for nm in U:
        assert text.count(f"Và như thế nào là {nm}?") == 1 and text.count(f"Như vậy là {nm}.") == 1, nm
    for p in ("ubhatobhāgavimutto", "saddhānusārī"):
        assert f"Thế nào là {N[p]}?" in text and f"Người này được gọi là {N[p]}." in text, p
    assert N["ubhatobhāgavimutto"] == "người được giải thoát theo cả hai cách"
    assert N["saddhānusārī"] == "người đi theo niềm tin" and N["saddhāvimutto"] == "người được giải thoát nhờ niềm tin"
    assert N["sakadāgāmī"] == "bậc trở lại một lần"
    for p in ("paññāvimutto", "kāyasakkhī", "diṭṭhippatto", "dhammānusārī"):
        assert N[p] + "…" in text, p
    assert text.count("Ở đời này, có người trồi lên với ý nghĩ: “Tốt thay niềm tin") == 6
    for bad in ("—", ":-", "chánh niệm", "….", "–", "là là"):
        assert bad not in text, bad
    print(f"OK: cross-book strings {n}; ch2 clauses {len(CH2_CHECK)}; ch4 clauses {len(CH4_CHECK)}; "
          f"matrix items 2; wrote {name} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
