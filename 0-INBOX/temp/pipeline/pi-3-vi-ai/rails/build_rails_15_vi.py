"""Builder for the Vietnamese rails of pi-3 chapter 15 (Cuddasamanayo, «Phương pháp thứ mười bốn», ^3-456 .. ^3-518),
plain audience. Last chapter: ends with the book colophon.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/15-cuddasamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/15-cuddasamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the approved
ch15 frame of rails/vi-rails-formulas.md (asserted). Identical Pāli follows the finished chapters:
  - elided items «Xena ye dhammā…» = «những hiện tượng nào cùng với X…» (ch3 .. ch12, asserted against ch9 / ch11);
  - the dissociation relative clause «những hiện tượng nào không gắn liền với X» (ch9 frame, asserted);
  - answers «te dhammā [asaṅkhataṃ khandhato ṭhapetvā] N … saṅgahitā» = ch4 «những hiện tượng ấy[, xét theo khối thì
    ngoại trừ …,] được gộp vào …» (B4.answer, imported), abridged «…, những hiện tượng ấy …» as ch4 / ch11;
  - «Katihi asaṅgahitā? …» = the sample ch2 (S.Q_OUT, S.answer_out with «chúng»);
  - the instrumental names = S.NAMES / S.DHAMMA_ATTR unchanged (as ch5 .. ch12; B11.nom and B11.ATTR_SPECIAL);
  - the summary verse of ^3-518 = ch9 ^3-318, copied line for line (B9.VERSE, asserted against 9-atthamanayo.md);
  - closing line S.CLOSINGS, colophon S.COLOPHON.
All imports are read-only (importing writes nothing). New strings: notes-rails-15.md.

usage: python -I -X utf8 build_rails_15_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)
import build_rails_4_vi as B4      # noqa: E402  (read-only import; writes nothing)
import build_rails_9_vi as B9      # noqa: E402  (read-only import; writes nothing)
import build_rails_11_vi as B11    # noqa: E402  (read-only import; writes nothing)

NAME = "15-cuddasamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"
N, D = S.NAMES, S.DHAMMA_ATTR

# ================================================================== frame pieces (approved ch15 frame; ch9 / ch4 / ch2)
WHICH = B9.WHICH          # ye dhammā = «những hiện tượng nào»
WITH = B9.WITH            # X-ena on an elided item = «cùng với»
TE = B9.TE                # te dhammā = «những hiện tượng ấy»
DISSOC = B9.DISSOC        # vippayuttā (+ instrumental) = «không gắn liền với»
PRON_OUT = S.PRON["ā"]    # «chúng» in the «na kehici … asaṅgahitā» answer (plural, as the sample ch2)
assert (WHICH, WITH, TE, DISSOC) == (B11.WHICH, B11.WITH, B11.TE, B11.DISSOC) == (
    B4.WHICH, B4.WITH, B4.THOSE, B11.DISSOC)


def frame15(x_vi):
    """Xena ye dhammā vippayuttā (last item)"""
    return f"{WHICH} {DISSOC} {x_vi}"


def answer(asx, nums_in, nums_out):
    """te dhammā [asaṅkhataṃ khandhato ṭhapetvā] N … saṅgahitā. Katihi asaṅgahitā? N … asaṅgahitā."""
    return f"{B4.answer(asx, nums_in)}. {S.Q_OUT} {S.answer_out(nums_out, PRON_OUT)}."


# ================================================================== reference items in the instrumental
INSTR_SPECIAL = {  # instrumental Pāli -> nominative key of S.NAMES (irregular)
    "avijjāya": "avijjā",
    "avijjāpaccayā saṅkhārehi": "avijjāpaccayā saṅkhārā",       # plural here; name unchanged (as ch11 / ch12)
    "saṅkhārapaccayā viññāṇena": "saṅkhārapaccayā viññāṇaṃ",
    "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "phassapaccayā vedanāya": "phassapaccayā vedanā",
    "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "paridevena": "paridevo", "sokena": "soko", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ",
    "upāyāsena": "upāyāso",
    "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "iddhipādena": "iddhipādo",
    "jhānena": "jhānaṃ", "appamaññāya": "appamaññā",
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
    "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā", "cittena": "cittaṃ",
    "manasikārena": "manasikāro", "adhimokkhena": "adhimokkho",
}
REGULAR = [("khandhena", "khandho"), ("āyatanena", "āyatanaṃ"), ("dhātuyā", "dhātu"), ("saccena", "saccaṃ"),
           ("ndriyena", "ndriyaṃ"), ("bhavena", "bhavo")]
ATTR_SPECIAL = dict(B11.ATTR_SPECIAL)   # vipākadhammadhammehi, nevavipāka…, upādādhammehi, na hetusahetukehi (as ch11)
ATTR_SPECIAL.update({
    "na hetuahetukehi dhammehi": D["na hetū ahetukā"],         # ^3-495 compound spelling, as na hetusahetukehi (as meant)
    "bahiddhāhi dhammehi": D["bahiddhā"],                       # ^3-491 instrumental of the indeclinable bahiddhā
})
used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k in ATTR_SPECIAL:
        v = f"{S.DHAMMA_N} {ATTR_SPECIAL[k]}"
    elif k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {D[' '.join(B11.nom(w) for w in k[: -len(' dhammehi')].split())]}"
    elif k == "kammabhavena":
        v = B11.INSTR["kammabhavena"]                          # (pi-2), no variant bracket here (as ch5 .. ch12)
    elif k in INSTR_SPECIAL:
        v = N[INSTR_SPECIAL[k]]
    else:
        v = next(N[k[: -len(a)] + b] for a, b in REGULAR if k.endswith(a))
    if k in B11.INSTR:                                         # identical Pāli = identical Vietnamese (ch11)
        assert B11.INSTR[k] == v, (k, v)
    used.append(v)
    return v


# ================================================================== segment grammar
YE = " ye dhammā"
Q_FULL = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? Te dhammā "
SEG = re.compile(r"^(?P<subj>.*?) ye (?P<dh>dhammā )?vippayuttā"
                 + r"(?P<mid>" + re.escape(Q_FULL) + r"|…pe… te dhammā |… te dhammā )"
                 + r"(?P<asx>asaṅkhataṃ khandhato ṭhapetvā )?(?P<c1>" + S.CNT + r") saṅgahitā\. "
                 + r"Katihi asaṅgahitā\? (?P<c2>" + S.CNT + r") asaṅgahitā\.$")
NO_DHAMMA = []   # ^3-487 «paṇītehi dhammehi ye vippayuttā» («dhammā» missing; reported)


def subject(p):
    items = [x.strip() for x in p.replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        assert it.endswith(YE), it
        parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
    parts.append(frame15(ref_vi(items[-1])))
    return S.cap("… ".join(parts))


def content_line(p):
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    if not m.group("dh"):
        NO_DHAMMA.append(p[:60])
    subj = subject(m.group("subj"))
    ans = answer(bool(m.group("asx")), S.parse_counts(m.group("c1")), S.parse_counts(m.group("c2")))
    if m.group("mid") == Q_FULL:
        return f"{subj} {S.THEN} {TE} {S.Q_IN} {S.cap(ans)}"
    return f"{subj}…, {ans}"                                    # vippayuttā…(pe…) te dhammā (abridged, as ch4 / ch11)


# ================================================================== summary verse (= ch9 ^3-318) and colophon
VERSE = dict(B9.VERSE)
COLOPHON_P = "Dhātukathāpakaraṇaṃ niṭṭhitaṃ."


def translate_segment(lines):
    out = []
    for ln in lines:
        if ln.startswith("#"):
            out.append(S.heading_vi(ln))
        elif ln in S.CLOSINGS:
            out.append(S.CLOSINGS[ln])
        elif ln in VERSE:
            out.append(VERSE[ln])
        elif ln == COLOPHON_P:
            out.append(S.COLOPHON)
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
    f = _formula("Xena ye dhammā vippayuttā, te dhammā katihi … saṅgahitā? (ch15)")
    got = f"{S.cap(frame15('X'))} {S.THEN} {TE} {S.Q_IN}"
    assert got == f, f"ch15 frame differs:\n{got}\n{f}"
    # the relative clause is the one of the approved ch9 frame
    assert _formula("Xena ye dhammā vippayuttā, te dhammā katihi … sampayuttāti? Natthi. (ch9)").startswith(
        S.cap(frame15("X")) + f" {S.THEN} {TE} ")
    assert _formula("te dhammā (answer subject)") == TE
    assert _formula("Colophon (end of ch15)") == S.COLOPHON
    assert _formula("Vippayuttenasaṅgahitāsaṅgahitapadaniddeso cuddasamo. (closing line)") == S.CLOSINGS[
        "Vippayuttenasaṅgahitāsaṅgahitapadaniddeso cuddasamo."]


def check_precedents():
    """Identical Pāli = identical Vietnamese: ch9 verse and elided items, ch4 asaṅkhata answer, ch2 asaṅgahita."""
    ch9 = (S.OUT / "9-atthamanayo.md").read_text(encoding="utf-8")
    for v in VERSE.values():
        assert v in ch9.splitlines(), v
    assert f"{S.cap(WHICH)} {WITH} {N['vedanākkhandho']}… {WHICH} {WITH} {N['saññākkhandho']}…" in ch9
    ch4 = (S.OUT / "4-tatiyanayo.md").read_text(encoding="utf-8")
    assert f"…, {TE}, {S.ASANKHATA}, {S.IN} " in ch4
    ch2 = (S.OUT / "2-pathamanayo.md").read_text(encoding="utf-8")
    for nums in [(0, 0, 0), (0, 0, 1), (0, 0, 5), (0, 0, 6)]:
        a = f"{S.Q_OUT} {S.answer_out(nums, PRON_OUT)}."
        if nums != (0, 0, 6):
            assert a in ch2, a


def check_names():
    """Every name used occurs in the approved formulas file (pi-1 / pi-2 ones are asserted by S.check_reuse)."""
    txt = FORMULAS.read_text(encoding="utf-8")
    missing = [v for v in set(used) if f"= {v.split(' [')[0]}" not in txt]
    assert not missing, missing


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_formulas()
    check_precedents()
    txt = render()
    check_names()
    assert "chín mươi chín" not in txt
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt and ".." not in txt
    assert "được được" not in txt and "là là" not in txt
    assert txt.rstrip().endswith(f"{S.COLOPHON} ^3-518")
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    tagged = sorted({v for v in used if S.reuse_tag(v)})
    print(f"{NAME}: {n} segments; {len(set(used))} reference names ({len(tagged)} with pi-1/pi-2 tag); "
          f"{n_reuse} pi-1/pi-2 strings asserted; «ye» without «dhammā»: {NO_DHAMMA}")
