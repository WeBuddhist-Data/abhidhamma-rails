"""Builder for the Vietnamese rails of pi-3 chapter 14 (Terasamanayo, «Phương pháp thứ mười ba», ^3-448 .. ^3-455),
plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/14-terasamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/14-terasamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the
approved formulas (rails/vi-rails-formulas.md: the ch6 / ch14 piece, the ch12 question «…, thì những hiện tượng ấy
gắn liền với bao nhiêu …?», the ch7 answer pieces, «Không có.», the abridged «…, những hiện tượng ấy …»).
Shared strings come from build_rails_sample_vi (S), build_rails_6_vi (B6: instrumental names, nom(), the ^3-227
verse) and build_rails_7_vi (B7: answer parts), all imported read-only (importing writes nothing). Elided items
«Xena ye dhammā…» use the ch3-ch12 form «những hiện tượng nào cùng với X…». New strings: notes-rails-14.md.

usage: python -I -X utf8 build_rails_14_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)
import build_rails_6_vi as B6      # noqa: E402  (read-only import; writes nothing)
import build_rails_7_vi as B7      # noqa: E402  (read-only import; writes nothing)

NAME = "14-terasamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== frame pieces (approved)
WHICH = B6.WHICH            # ye dhammā = những hiện tượng nào
WITH = B6.WITH              # X-ena (elided item) = cùng với
TE = B6.TE                  # te dhammā = những hiện tượng ấy
BY3_NEG = B6.BY3_NEG        # khandhasaṅgahena asaṅgahitā … = theo cách gộp vào khối, … hay theo cách gộp vào yếu tố
Q_SAM = B7.Q_SAM_FULL       # katihi … sampayuttā(ti)? = gắn liền với bao nhiêu khối, …?
Q_VIP = B7.Q_VIP            # Katihi vippayuttā? = Không gắn liền với bao nhiêu?
NATTHI = B7.NATTHI          # Natthi. = Không có.

N, D = S.NAMES, S.DHAMMA_ATTR

# matrix names not in S.DHAMMA_ATTR (pi-1 matrix names, asserted against the pi-1 rails)
ATTR14 = {
    "asaṃyojaniyā": "không phải là đối tượng của xiềng xích",
    "aganthaniyā": "không phải là đối tượng của nút thắt",
    "anoghaniyā": "không phải là đối tượng của dòng lũ",
    "ayoganiyā": "không phải là đối tượng của ách",
    "anīvaraṇiyā": "không phải là đối tượng của chướng ngại",
    "anupādāniyā": "không phải là đối tượng của sự bám víu",
    "upādānasampayuttā": "gắn liền với sự bám víu",
    "upādānasampayuttā ceva no ca upādānā": "gắn liền với sự bám víu nhưng không phải là sự bám víu",
    "upādānavippayuttā anupādāniyā": "không gắn liền với sự bám víu và không phải là đối tượng của sự bám víu",
}
# not a matrix item (^3-453; ch6 ^3-219 has «āsavasampayuttehi ceva no ca āsavehi» here): translated as written,
# built on «āsavasampayuttā ceva no ca āsavā» with «không gắn liền với» (reported)
ATTR_AS_WRITTEN = {
    "āsavavippayuttā ceva no ca āsavā": "không gắn liền với ô nhiễm nhưng không phải là ô nhiễm",
}
ATTR_SPECIAL = {   # instrumental «X dhammehi» whose key is not the regular conversion
    "upādādhammehi": D["upādā"],                                  # as ch6
    "vipākadhammadhammehi": D["vipākadhammadhammā"],              # as ch6
    "na hetusahetukehi dhammehi": D["na hetū sahetukā"],          # compound spelling, as ch6 / ch7 / ch10
}
used = []


def name_of(instr):
    """Instrumental Pāli X -> Vietnamese name (unchanged subject name)."""
    x = instr[0].lower() + instr[1:]
    if x in ATTR_SPECIAL:
        v = f"{S.DHAMMA_N} {ATTR_SPECIAL[x]}"
    elif x.endswith(" dhammehi"):
        key = " ".join(B6.nom(w) for w in x[: -len(" dhammehi")].split())
        attr = D.get(key) or ATTR14.get(key) or ATTR_AS_WRITTEN[key]
        v = f"{S.DHAMMA_N} {attr}"
    else:
        v = B6.INSTR[x]
    used.append(v)
    return v


def neg_frame(x_vi):
    """«những hiện tượng nào không được gộp vào cùng với X theo cách gộp vào khối, … hay theo cách gộp vào yếu tố»"""
    return f"{WHICH} {S.OUT_} {WITH} {x_vi} {BY3_NEG}"


def head_vi(subj):
    """'A ye dhammā… B ye dhammā…pe… Z ye dhammā' -> «Những hiện tượng nào cùng với A… … những hiện tượng nào
    không được gộp vào cùng với Z …» (as ch6)."""
    items = [s.strip() for s in subj.replace("…pe…", "…").split("…") if s.strip()]
    for s in items:
        assert s.endswith(" ye dhammā"), s
    items = [s[: -len(" ye dhammā")] for s in items]
    parts = [f"{WHICH} {WITH} {name_of(s)}…" for s in items[:-1]]
    parts.append(neg_frame(name_of(items[-1])))
    return S.cap(" ".join(parts))


def answer(a):
    """'tīhi khandhehi sampayuttā; ekenāyatanena ekāya dhātuyā kehici sampayuttā' -> «gắn liền với ba khối; …»"""
    return "; ".join(B7.part_vi(x) for x in a.split("; "))


# ================================================================== segment grammar
TAIL = r" khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā (?P<dh>dhātusaṅgahena|dhātusaṅgena) asaṅgahitā"
LINE = re.compile(
    r"^(?P<subj>.+?)" + TAIL
    + r"(?:, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttā(?:ti)?\? "
      r"(?:Te dhammā (?P<pos1>[^.?]+)\.|Natthi(?P<nt>[.?]))"
    + r"|(?:…pe…|…) te dhammā (?P<pos2>[^.?]+)\.)"
    + r" Katihi vippayuttā\? (?P<neg>[^?]+\.)$")
slips = []


def content_line(p, bid):
    m = LINE.match(p)
    assert m, p
    if m.group("dh") == "dhātusaṅgena":
        slips.append((bid, "dhātusaṅgena for dhātusaṅgahena (rendered as meant)"))
    if m.group("nt") == "?":
        slips.append((bid, "«Natthi?» for «Natthi.» (rendered «Không có.»)"))
    head = head_vi(m.group("subj"))
    if m.group("pos2"):                                  # …pe… te dhammā / … te dhammā (abridged question)
        first = f"{head}…, {TE} {answer(m.group('pos2'))}."
    elif m.group("pos1"):
        first = f"{head}, {S.THEN} {TE} {Q_SAM} {S.cap(TE)} {answer(m.group('pos1'))}."
    else:
        first = f"{head}, {S.THEN} {TE} {Q_SAM} {NATTHI}"
    return f"{first} {Q_VIP} {B7.answer_vi(m.group('neg'))}"


# ================================================================== summary verse of ^3-455 (= ch6 ^3-227, split
# where this Pāli splits; ch6 strings copied, the ch6 variant bracket is not in this Pāli)
V6 = B6.VERSE
_v6_3 = V6["Visaṃsaṭṭhaṃ samuṭṭhāna-sahabhu anuparivatti;"]
_v6_4 = V6["Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho."]
_bahira, _rest = _v6_4.split(", cả hai; ")
VERSE = {
    "Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;":
        V6["Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;"],
    "Dve bhavā jātijarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ.":     # jātijarā = jāti jarā
        V6["Dve bhavā jāti jarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ."],
    "Visaṃsaṭṭhaṃ samuṭṭhānasahabhu, anuparivatti bāhiraṃ upādā;":
        f"{_v6_3[:-1]}, {S.low(_bahira)};",
    "Dve visayo esanayo subuddhoti.":
        S.cap("cả hai; " + _rest.replace(" " + S.reading("Syā.", "dvevīsati"), "")),
}


def translate_segment(lines, bid):
    out = []
    for ln in lines:
        if ln.startswith("#"):
            out.append(S.heading_vi(ln))
        elif ln in S.CLOSINGS:
            out.append(S.CLOSINGS[ln])
        elif ln in VERSE:
            out.append(VERSE[ln])
        else:
            out.append(content_line(ln, bid))
    return out


def render():
    blocks = []
    for lines, bid in S.pali_segments(S.PALI / NAME):
        vi = translate_segment(lines, bid)
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
    # ch6 / ch14 piece
    f = _formula("… khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā (ch6, ch14)")
    assert f == f"… {S.OUT_} {WITH} X {BY3_NEG}", f
    # question part of the approved ch12 frame
    f = _formula("Xena ye dhammā khandhasaṅgahena saṅgahitā … , te dhammā katihi … sampayuttā? (ch12)")
    assert f.endswith(f", {S.THEN} {TE} {Q_SAM}"), f
    # te dhammā; abridged answer; ch7 pieces
    assert _formula("te dhammā (answer subject)") == TE
    assert _formula("…pe… te dhammā N").startswith(f"…, {TE} ")
    assert _formula("X katihi khandhehi katihāyatanehi katihi dhātūhi sampayutto(ti)? Natthi.") == f"X {Q_SAM} {NATTHI}"
    assert _formula("Katihi vippayutto? N khandhehi").startswith(f"{Q_VIP} ")
    assert _formula("; ekenāyatanena ekāya dhātuyā kehici vippayutto.") == \
        "; " + B7.part_vi("ekenāyatanena ekāya dhātuyā kehici vippayuttā") + "."
    # ch7 notes / ch10: «; ekenāyatanena ekāya dhātuyā kehici sampayuttā»
    assert B7.part_vi("ekenāyatanena ekāya dhātuyā kehici sampayuttā") == \
        "gắn liền với một số hiện tượng thuộc một lĩnh vực nhận biết và một yếu tố"
    # the ch6 verse strings are those of the approved ch6 file
    ch6 = (S.OUT / "6-pancamanayo.md").read_text(encoding="utf-8")
    for v in V6.values():
        assert v in ch6, v


def check_reuse14():
    """The new matrix names are the pi-1 ones; the chain / answer shapes occur in the finished chapters."""
    t1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_DIR.glob("*.md"))).lower()
    missing = [v for v in ATTR14.values() if f"hiện tượng {v}" not in t1 and f"hiện tượng nào {v}" not in t1]
    assert not missing, missing
    ch10 = (S.OUT / "10-navamanayo.md").read_text(encoding="utf-8")
    assert f"{TE} gắn liền với ba khối; gắn liền với một số hiện tượng thuộc một lĩnh vực nhận biết và một yếu tố." \
        in ch10
    return len(ATTR14)


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    n14 = check_reuse14()
    check_formulas()
    txt = render()
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{NAME}: {n} segments; {len(set(used))} reference names; {n_reuse + n14} pi-1/pi-2 strings asserted; "
          f"slips: {slips}")
