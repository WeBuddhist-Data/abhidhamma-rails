# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 14-terasamanayo.md (Terasamanayo, method 13,
asaṅgahitena sampayuttaṃ vippayuttaṃ).

usage: python -I -X utf8 build_14_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\14-terasamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's, those of the imported chapter
builders and this file's) still occurs in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the
Pāli at build time.
Strings reused verbatim (identical Pāli):
  build_6_vi  (E6): relative head «đối với X, những hiện tượng nào», the three «không được gộp vào theo cách …»
                    modifiers, «… những hiện tượng đó», instrumental members, summary-verse lines;
  build_10_vi (E10): main question «, thì những hiện tượng đó gắn liền với bao nhiêu …?», sampayuttā answers
                    (khandha-only, kehici);
  build_7_vi  (E7): «Không có.», «Không gắn liền với bao nhiêu?», vippayuttā answers (with kehici).
Formulas new to this chapter: notes-14.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_6_vi as E6       # noqa: E402  (importing writes nothing)
import build_7_vi as E7       # noqa: E402  (importing writes nothing)
import build_10_vi as E10     # noqa: E402  (importing writes nothing)

CH = "14-terasamanayo.md"
N = 13  # method number (file 14)

# ---------------------------------------------------------------- shared frames (verbatim from earlier chapters)
REL = E6.REL                     # Xena ye dhammā = «đối với X, những hiện tượng nào»
MODS_EX = E6.MODS_EX             # khandhasaṅgahena asaṅgahitā āyatanasaṅgahena … dhātusaṅgahena asaṅgahitā
ANS_SHORT = E6.ANS_SHORT         # …pe… te dhammā / … te dhammā = «… những hiện tượng đó»
Q_MAIN = E10.Q_MAIN              # , te dhammā katihi … sampayuttā(ti)?
TE = E10.TE                      # te dhammā (answer)
NATTHI = E7.NATTHI               # Natthi.
Q_DISS = E7.Q_DISS               # Katihi vippayuttā?
assert REL == "đối với {x}, những hiện tượng nào"
assert MODS_EX == ("không được gộp vào theo cách gộp vào khối, không được gộp vào theo cách gộp vào lĩnh vực "
                   "nhận biết, không được gộp vào theo cách gộp vào yếu tố")
assert Q_MAIN == ", thì những hiện tượng đó gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
assert ANS_SHORT == "… những hiện tượng đó" and TE == "những hiện tượng đó"
assert NATTHI == "Không có." and Q_DISS == "Không gắn liền với bao nhiêu?"

# ---------------------------------------------------------------- matrix names not in the sample (pi-1)
EXTRA = {
    "asaṃyojaniyā": B.pi1("không phải là đối tượng của xiềng xích"),          # pi-1 ^1-M2-21
    "aganthaniyā": B.pi1("không phải là đối tượng của nút thắt"),             # ^1-M2-27
    "anoghaniyā": B.pi1("không phải là đối tượng của dòng lũ"),               # ^1-M2-33
    "ayoganiyā": B.pi1("không phải là đối tượng của ách"),                    # ^1-M2-39
    "anīvaraṇiyā": B.pi1("không phải là đối tượng của chướng ngại"),          # ^1-M2-45
    "anupādāniyā": B.pi1("không phải là đối tượng của sự bám víu"),           # ^1-M2-70
    "upādānasampayuttā": B.pi1("gắn liền với sự bám víu"),
    "upādānasampayuttā ceva no ca upādānā":
        B.pi1("gắn liền với sự bám víu nhưng không phải là sự bám víu"),       # ^1-M2-73
    "upādānavippayuttā anupādāniyā":
        B.pi1("không gắn liền với sự bám víu và không phải là đối tượng của sự bám víu"),   # pi-1 Nikkhepa
    # ^3-453 as written (not a pi-1 matrix name; reported): pi-1 words only
    "āsavavippayuttā ceva no ca āsavā":
        B.pi1("không gắn liền với ô nhiễm") + " " + B.pi1("nhưng không phải là ô nhiễm"),
}
for _k, _v in EXTRA.items():
    assert _k not in B.MATRIX_PRED, _k
    if _k not in ("upādānavippayuttā anupādāniyā", "āsavavippayuttā ceva no ca āsavā"):
        B.pi1("Các hiện tượng " + _v)          # the pi-1 matrix line itself


def member(p):
    """One instrumental member (without 'ye dhammā') -> Vietnamese (lower case); singular members and the
    regular matrix names go through build_6_vi.instr_item (same strings as ch6)."""
    p = p.strip()
    p = p[:1].lower() + p[1:]
    if p.endswith("dhammehi"):
        if p.endswith(" dhammehi"):
            key = " ".join(E6._nom_word(w) for w in p[:-len(" dhammehi")].split())
        else:
            key = p[:-len("dhammehi")]
        key = E6.ALIAS.get(key, key)
        if key in EXTRA:
            return B.DHAMMA + " " + EXTRA[key]
    return E6.instr_item(p)


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, những hiện tượng nào»."""
    parts = [x.strip() for x in chain.split("…")]
    out = []
    for x in parts:
        assert x.endswith(" ye dhammā"), (x, chain)
        out.append(REL.format(x=member(x[:-len(" ye dhammā")])))
    return B.cap("… ".join(out))


# ---------------------------------------------------------------- one content line
_MODS = "khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā"
_LINE = re.compile(
    rf"^(?P<chain>.+?) {_MODS}"
    r"(?:, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā(?:ti)?\? (?P<full>.+)"
    r"|… te dhammā (?P<short>.+))$")
FIXES = (   # as written -> as meant (plain spelling slip / punctuation; reported)
    ("…pe…", "…"),                                            # ^3-449
    (" …", "…"),                                              # ^3-454, ^3-455 stray space before «…»
    ("dhātusaṅgena asaṅgahitā", "dhātusaṅgahena asaṅgahitā"), # ^3-454 spelling slip
    ("sampayuttāti? Natthi? ", "sampayuttāti? Natthi. "),     # ^3-450 «?» for «.» after Natthi
)


def assoc_vi(s, first):
    """'[Te dhammā] tīhi khandhehi sampayuttā; ekenāyatanena ekāya dhātuyā kehici sampayuttā.'"""
    m = re.fullmatch(r"(?P<te>[Tt]e dhammā )?(?P<ans>.+ sampayuttā)\.", s)
    assert m and m.group("te"), s
    te = B.cap(TE) if first else TE
    return f"{te} {E10.answer_vi(m.group('ans'))}."


def rest_vi(rest, short):
    """Sentences after the main question (full) or after «… te dhammā» (short)."""
    sents = re.split(r"(?<=[.?]) ", ("te dhammā " + rest) if short else rest)
    out = []
    for i, s in enumerate(sents):
        if s == "Natthi.":
            out.append(NATTHI)
        elif re.fullmatch(r"Katihi vippayuttā\?", s):
            out.append(Q_DISS)
        elif s.lower().startswith("te dhammā "):
            assert i == 0, rest
            out.append(assoc_vi(s, not short))
        else:
            assert s.endswith("vippayuttā.") and "sampayutt" not in s, s
            out.append(E7.sentence_vi(s))
    return " ".join(out)


def segment_vi(line):
    for a, b in FIXES:
        line = line.replace(a, b)
    m = _LINE.match(line)
    assert m, line
    head = f"{chain_vi(m.group('chain'))} {MODS_EX}"
    if m.group("full") is not None:
        return f"{head}{Q_MAIN} {rest_vi(m.group('full'), False)}"
    vi = rest_vi(m.group("short"), True)
    assert vi.startswith(TE + " "), vi
    return f"{head}{ANS_SHORT}{vi[len(TE):]}"


# ---------------------------------------------------------------- summary verse of ^3-455 (uddāna) and closing
_V6 = E6.VERSE
_V6_1 = _V6["Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;"]
_V6_2 = _V6["Dve bhavā jāti jarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ."]
_V6_3 = _V6["Visaṃsaṭṭhaṃ samuṭṭhāna-sahabhu anuparivatti;"]
_V6_4 = _V6["Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho."]
_PAIR, _DVE = "Điều thuộc phần bên ngoài và điều phái sinh", ", hai điều; "    # bāhiraṃ upādā / dve (ch6)
_SUBUDDHO = "phạm vi [dị bản (Syā.): dvevīsati] của phương pháp này đã được hiểu rõ."
assert _V6_3.endswith(";") and _V6_4 == _PAIR + _DVE + _SUBUDDHO
VERSE = {
    # line 1: identical Pāli (ch6 ^3-227)
    "Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;": _V6_1,
    # line 2: ch6 has «jāti jarā», here the compound «jātijarā»: same Vietnamese
    "Dve bhavā jātijarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ.": _V6_2,
    # line 3: ch6 lines 3 and 4 regrouped as the Pāli splits them (bāhiraṃ upādā now end line 3)
    "Visaṃsaṭṭhaṃ samuṭṭhānasahabhu, anuparivatti bāhiraṃ upādā;":
        _V6_3[:-1] + ", " + _PAIR[:1].lower() + _PAIR[1:] + ";",
    # line 4: «dve» starts the line (no variant bracket here); -ti dropped (ch3 pattern)
    "Dve visayo esanayo subuddhoti.":
        B.cap(_DVE[2:]) + _SUBUDDHO.replace(" [dị bản (Syā.): dvevīsati]", ""),
}


def build():
    out = []
    for seg in B._segments(os.path.join(B.PALI_DIR, CH)):
        vi = []
        for i, line in enumerate(seg):
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip() if bid else line.strip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                if title == "Terasamanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Asaṅgahitenasampayuttavippayuttapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    raise AssertionError(line)
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body == "Asaṅgahitenasampayuttavippayuttapadaniddeso terasamo.":
                t = B.niddesa_closing(N)
            else:
                assert i == 0, line
                t = segment_vi(body)
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = B.check_sources()
    text = build()
    assert unicodedata.normalize("NFC", text) == text
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text and "pe…" not in text
    assert "là là" not in text and "được được" not in text and " …" not in text and ".." not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
