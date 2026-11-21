"""Builder for the Vietnamese rails of pi-3 chapter 13 (Dvādasamanayo, «Phương pháp thứ mười hai»,
^3-417 .. ^3-447), plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/13-dvadasamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/13-dvadasamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md, item 5:
^3-447 «Rūpakkhandhā cattāro» translated as written) and the approved ch13 frame of rails/vi-rails-formulas.md
(asserted). Shared strings are imported from build_rails_sample_vi (read-only): the inclusion answers are the
chapter-2 answer_in / Q_OUT / answer_out. Reference names, elided items «Xena ye dhammā…» («những hiện tượng nào
cùng với X…») and the abridged «sampayuttā… te dhammā» («…, những hiện tượng ấy …») follow ch8 / ch10; the
instrumental tables and verse lines 2-6 are imported read-only from build_rails_10_vi (identical Pāli) and asserted
against the finished ch10 chapter file. New strings: notes-rails-13.md.

usage: python -I -X utf8 build_rails_13_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)
import build_rails_10_vi as C10  # noqa: E402  (read-only import; writes nothing)

NAME = "13-dvadasamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== frame pieces (approved ch3-15 formulas)
WHICH = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                  # X-ena on an elided item (as ch3-ch10)
TE = "những hiện tượng ấy"                         # te dhammā
ASSOC = "gắn liền với"                             # sampayuttā (+ instrumental)
assert (WHICH, WITH, TE, ASSOC) == (C10.WHICH, C10.WITH, C10.TE, C10.ASSOC)


def frame13(x_vi):
    """Xena ye dhammā sampayuttā, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā?"""
    return f"{WHICH} {ASSOC} {x_vi} {S.THEN} {TE} {S.Q_IN}"


def last13(x_vi):
    """Xena ye dhammā sampayuttā (abridged: the question is elided)"""
    return f"{WHICH} {ASSOC} {x_vi}"


# ================================================================== reference items in the instrumental
INSTR = dict(C10.INSTR)                            # names unchanged (S.NAMES), as ch10
ATTR = dict(C10.ATTR)                              # X-ehi dhammehi -> key of S.DHAMMA_ATTR, as ch10
ATTR.update({                                      # new here (with «dhammehi»; ch10 ^3-346 has them bare)
    "saṃyojanehi": "saṃyojanā", "ganthehi": "ganthā", "oghehi": "oghā", "yogehi": "yogā",
    "nīvaraṇehi": "nīvaraṇā",
})
used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR[k[: -len(' dhammehi')]]]}"
    else:
        v = INSTR[k]
    used.append(v)
    return v


# ================================================================== segment grammar
YE = " ye dhammā"
Q_FULL = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? Te dhammā "
SEG = re.compile(r"^(?P<subj>.*?) ye dhammā sampayuttā"
                 r"(?P<mid>" + re.escape(Q_FULL) + r"|…pe… te dhammā |…,? te dhammā )"
                 r"(?P<c1>" + S.CNT + r") saṅgahitā\. Katihi asaṅgahitā\? "
                 r"(?P<c2>" + S.CNT + r") asaṅgahitā\.$")


def subject(p, full):
    items = [x.strip() for x in p.replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        assert it.endswith(YE), it
        parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
    x_vi = ref_vi(items[-1])
    parts.append(frame13(x_vi) if full else last13(x_vi))
    return S.cap("… ".join(parts))


def answer(c1, c2):
    """«được gộp vào …. Không được gộp vào bao nhiêu? Không được gộp vào ….» (chapter-2 answer pieces)"""
    n_in, n_out = S.parse_counts(c1), S.parse_counts(c2)
    assert 0 not in n_in and 0 not in n_out, (c1, c2)      # no «na kehici» answers in this chapter
    return f"{S.answer_in(n_in)}. {S.Q_OUT} {S.answer_out(n_out, S.PRON['ā'])}."


def content_line(p):
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    ans = answer(m.group("c1"), m.group("c2"))
    if m.group("mid") == Q_FULL:
        return f"{subject(m.group('subj'), True)} {S.cap(TE)} {ans}"
    return f"{subject(m.group('subj'), False)}…, {TE} {ans}"   # sampayuttā…(pe…)(,) te dhammā (abridged)


# ================================================================== summary verse (uddāna) of ^3-447, lines 2-7
# line 1 as written (APPROVED 5); lines 2-6 identical to ch10 ^3-352 (line 5 «piṭṭhidukesu» here, «piṭṭhi dukesu»
# in ch10: spacing only, same words)
VERSE = {
    "Rūpakkhandhā cattāro, manāyatanameva ca;":
        f"Bốn {S.KHANDHA} vật chất, và cũng có {S.NAMES['manāyatanaṃ']};",
    "Viññāṇadhātuyo satta, dve saccā cuddasindriyā.":
        C10.VERSE["Viññāṇadhātuyo satta, dve saccā cuddasindriyā."],
    "Paccaye dvādasa padā, tato upari soḷasa;":
        C10.VERSE["Paccaye dvādasa padā, tato upari soḷasa;"],
    "Tikesu aṭṭha gocchake, tecattālīsameva ca.":
        C10.VERSE["Tikesu aṭṭha gocchake, tecattālīsameva ca."],
    "Mahantaraduke satta, padā piṭṭhidukesu cha;":
        C10.VERSE["Mahantaraduke satta, padā piṭṭhi dukesu cha;"],
    "Navamassa padassete, niddese saṅgahaṃ gatāti.":
        C10.VERSE["Navamassa padassete, niddese saṅgahaṃ gatāti."],
}


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
    # ch13 frame (question)
    f = _formula("Xena ye dhammā sampayuttā, te dhammā katihi … saṅgahitā? (ch13)")
    got = S.cap(frame13("X"))
    assert got == f, f"ch13 frame differs:\n{got}\n{f}"
    # chapter-2 answer pieces
    assert _formula("Katihi asaṅgahito/-ā/-aṃ/-āni?") == S.Q_OUT
    assert _formula("N khandhehi N āyatanehi N dhātūhi asaṅgahito.") == \
        f"{S.cap(S.OUT_)} N {S.KHANDHA}, N {S.AYATANA} và N {S.DHATU}."
    assert _formula("te dhammā (answer subject)") == TE
    # ch10 verse lines and the ch10 elided-item / abridged forms (identical Pāli) occur in the finished ch10 file
    t10 = (S.OUT / "10-navamanayo.md").read_text(encoding="utf-8")
    for pali, vi in VERSE.items():
        if not pali.startswith("Rūpakkhandhā"):
            assert f"\n{vi}\n" in t10, vi
    assert C10.VERSE["Arūpakkhandhā cattāro, manāyatanameva ca;"].replace(" phi vật chất", " vật chất") == \
        VERSE["Rūpakkhandhā cattāro, manāyatanameva ca;"]
    assert "những hiện tượng nào cùng với khối tri giác… những hiện tượng nào gắn liền với khối tạo tác" in t10
    # termbase / APPROVED: Rūpakkhandhā as written
    appr = (S.RAILS.parent / "termbase" / "APPROVED.md").read_text(encoding="utf-8")
    assert "«Rūpakkhandhā cattāro»" in appr and "«Bốn khối vật chất»" in appr
    assert S.NAMES["rūpakkhandho"] == f"{S.KHANDHA} vật chất"


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    C10.check_reuse10()
    check_formulas()
    txt = render()
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    tagged = sorted({v for v in used if S.reuse_tag(v)})
    print(f"{NAME}: {n} segments; {len(set(used))} reference names ({len(tagged)} with pi-1/pi-2 tag); "
          f"{n_reuse + len(C10.REUSE10)} pi-1/pi-2 strings asserted")
