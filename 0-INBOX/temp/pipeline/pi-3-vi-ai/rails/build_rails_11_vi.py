"""Builder for the Vietnamese rails of pi-3 chapter 11 (Dasamanayo, «Phương pháp thứ mười», ^3-353 .. ^3-408),
plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/11-dasamanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/11-dasamanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the approved
formulas (rails/vi-rails-formulas.md). The ch11 frame «Xena ye dhammā vippayuttā, tehi dhammehi ye dhammā vippayuttā»
is the approved ch8 frame with «gắn liền với X» -> «không gắn liền với X» (asserted). Answers, «kehici», the «na
kehici» answer with «những hiện tượng ấy», the elided items «những hiện tượng nào cùng với X…» and the abridged
«…, những hiện tượng ấy …» follow ch8 (identical Pāli, asserted against 8-sattamanayo.md); the instrumental names
follow ch5 / ch6 (S.NAMES / S.DHAMMA_ATTR unchanged); the closing verse is ^3-305 of ch7, copied line for line
(asserted against 7-chatthanayo.md). New strings: notes-rails-11.md.

usage: python -I -X utf8 build_rails_11_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "11-dasamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"
N, D = S.NAMES, S.DHAMMA_ATTR

# ================================================================== frame pieces (approved ch3-15 formulas, as ch8)
WHICH = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                  # X-ena on an elided item (as ch3 .. ch8)
THOSE_REF = "các hiện tượng đó"                    # tehi dhammehi
TE = "những hiện tượng ấy"                         # te dhammā
ASSOC = "gắn liền với"                             # sampayuttā (only for the formula check)
DISSOC = "không gắn liền với"                      # vippayuttā (+ instrumental)
SOME = "một số hiện tượng"                         # kehici (termbase)
Q_DIS = f"{DISSOC} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?"


def frame11(x_vi):
    """Xena ye dhammā vippayuttā, tehi dhammehi ye dhammā vippayuttā"""
    return f"{WHICH} {DISSOC} {x_vi}; {WHICH} {DISSOC} {THOSE_REF}"


def counted_dis(nums, subj):
    """te dhammā N khandhehi … vippayuttā (as ch8). Zero runs: «không có khối nào, không có lĩnh vực nhận biết nào
    mà <subj> không gắn liền với», then «, nhưng không gắn liền với N yếu tố»."""
    groups = S._groups(nums)
    parts = []
    for i, (zero, items) in enumerate(groups):
        if zero:
            parts.append(", ".join(f"không có {c} nào" for c, _ in items) + f" mà {subj} {DISSOC}")
        elif i == 0:
            parts.append(f"{subj} {DISSOC} {S.counts_vi(items)}")
        else:
            parts.append(f"{DISSOC} {S.counts_vi(items)}")
    assert groups[0][0] or len(groups) == 1, nums
    return f", {S.BUT} ".join(parts)


KEHICI_P = "; ekenāyatanena ekāya dhātuyā kehici vippayuttā"
KEHICI_VI = f"; {DISSOC} {SOME} thuộc {S.counts_vi([(S.AYATANA, 1), (S.DHATU, 1)])}"

# ================================================================== reference items in the instrumental
INSTR = {  # instrumental Pāli -> subject name, unchanged (as ch5 / ch6 / ch8)
    "rūpakkhandhena": N["rūpakkhandho"], "vedanākkhandhena": N["vedanākkhandho"],
    "saññākkhandhena": N["saññākkhandho"], "saṅkhārakkhandhena": N["saṅkhārakkhandho"],
    "viññāṇakkhandhena": N["viññāṇakkhandho"],
    "cakkhāyatanena": N["cakkhāyatanaṃ"], "phoṭṭhabbāyatanena": N["phoṭṭhabbāyatanaṃ"],
    "manāyatanena": N["manāyatanaṃ"],
    "cakkhudhātuyā": N["cakkhudhātu"], "phoṭṭhabbadhātuyā": N["phoṭṭhabbadhātu"],
    "cakkhuviññāṇadhātuyā": N["cakkhuviññāṇadhātu"], "manoviññāṇadhātuyā": N["manoviññāṇadhātu"],
    "samudayasaccena": N["samudayasaccaṃ"], "maggasaccena": N["maggasaccaṃ"],
    "nirodhasaccena": N["nirodhasaccaṃ"],
    "avijjāya": N["avijjā"],
    "avijjāpaccayā saṅkhārehi": N["avijjāpaccayā saṅkhārā"],      # plural here; name unchanged
    "saṅkhārapaccayā viññāṇena": N["saṅkhārapaccayā viññāṇaṃ"],
    "saḷāyatanapaccayā phassena": N["saḷāyatanapaccayā phasso"],
    "phassapaccayā vedanāya": N["phassapaccayā vedanā"],
    "vedanāpaccayā taṇhāya": N["vedanāpaccayā taṇhā"],
    "taṇhāpaccayā upādānena": N["taṇhāpaccayā upādānaṃ"],
    "kammabhavena": "sự hiện hữu dưới dạng nghiệp",               # (pi-2), no variant here (as ch5 / ch6 / ch7)
    "rūpabhavena": N["rūpabhavo"], "arūpabhavena": N["arūpabhavo"],
    "nevasaññānāsaññābhavena": N["nevasaññānāsaññābhavo"], "catuvokārabhavena": N["catuvokārabhavo"],
    "asaññābhavena": N["asaññābhavo"], "ekavokārabhavena": N["ekavokārabhavo"],
    "sokena": N["soko"], "paridevena": N["paridevo"], "dukkhena": N["dukkhaṃ"],
    "domanassena": N["domanassaṃ"], "upāyāsena": N["upāyāso"],
    "satipaṭṭhānena": N["satipaṭṭhānaṃ"], "sammappadhānena": N["sammappadhānaṃ"],
    "iddhipādena": N["iddhipādo"], "jhānena": N["jhānaṃ"], "appamaññāya": N["appamaññā"],
    "pañcahi indriyehi": N["pañcindriyāni"], "pañcahi balehi": N["pañca balāni"],
    "sattahi bojjhaṅgehi": N["satta bojjhaṅgā"],
    "ariyena aṭṭhaṅgikena maggena": N["ariyo aṭṭhaṅgiko maggo"],
    "phassena": N["phasso"], "vedanāya": N["vedanā"], "saññāya": N["saññā"], "cetanāya": N["cetanā"],
    "cittena": N["cittaṃ"], "manasikārena": N["manasikāro"], "adhimokkhena": N["adhimokkho"],
}
for _k in [k for k in N if k.endswith("ndriyaṃ")]:              # cakkhundriyena … aññātāvindriyena
    INSTR[_k[: -len("ndriyaṃ")] + "ndriyena"] = N[_k]

ATTR_SPECIAL = {  # «X dhammehi» whose nominative key is not the regular conversion (reported)
    "vipākadhammadhammehi": D["vipākadhammadhammā"],              # «dhammehi» fused into the compound (as ch6)
    "nevavipākanavipākadhammadhammehi": D["nevavipākanavipākadhammadhammā"],
    "upādādhammehi": D["upādā"],                                   # as ch3 / ch6
    "na hetusahetukehi dhammehi": D["na hetū sahetukā"],           # compound spelling, as ch7 ^3-279 (as meant)
    "anārammaṇehi [anupādiṇṇehi (sī. ka.)] dhammehi":
        D["anārammaṇā"] + " " + S.reading("Sī., Ka.", "anupādiṇṇehi"),
}
SUBJ_FIX = {
    # ^3-357: «..» for «…» between two items; rendered as meant
    "kāyindriyena ye dhammā.. itthindriyena": "kāyindriyena ye dhammā… itthindriyena",
}


def nom(w):
    """Instrumental plural word of a matrix attribute -> nominative plural (key form of S.DHAMMA_ATTR); as ch6."""
    if w.endswith("īhi"):
        return w[:-3] + "ino"            # ācayagāmīhi, maggādhipatīhi, rūpīhi, cittānuparivattīhi
    if w.endswith("bhūhi"):
        return w[:-3] + "uno"            # cittasaṃsaṭṭhasamuṭṭhānasahabhūhi -> …sahabhuno
    if w.endswith("hetūhi"):
        return w[:-2]                    # hetūhi -> hetū
    if w.endswith("ehi"):
        return w[:-3] + "ā"
    return w                             # ceva, ca, na, no, dassanena, bhāvanāya, sukhāya, vedanāya …


used = []


def ref_vi(p):
    k = p[0].lower() + p[1:]
    if k in ATTR_SPECIAL:
        v = f"{S.DHAMMA_N} {ATTR_SPECIAL[k]}"
    elif k.endswith(" dhammehi"):
        v = f"{S.DHAMMA_N} {D[' '.join(nom(w) for w in k[: -len(' dhammehi')].split())]}"
    else:
        v = INSTR[k]
    used.append(v)
    return v


# ================================================================== segment grammar
YE = " ye dhammā"
PRED = " ye dhammā vippayuttā, tehi dhammehi ye dhammā vippayuttā"
Q_FULL = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi vippayuttā? Te dhammā "
SEG = re.compile(r"^(?P<subj>.*?)" + re.escape(PRED)
                 + r"(?P<mid>" + re.escape(Q_FULL) + r"|… te dhammā |…pe… te dhammā )"
                 + r"(?P<cnt>" + S.CNT + r") vippayuttā(?P<keh>" + re.escape(KEHICI_P) + r")?\.$")


def subject(p):
    for a, b in SUBJ_FIX.items():
        p = p.replace(a, b)
    items = [x.strip() for x in p.replace("…pe…", "…").split("…")]
    assert all(items), p
    parts = []
    for it in items[:-1]:
        assert it.endswith(YE), it
        parts.append(f"{WHICH} {WITH} {ref_vi(it[: -len(YE)])}")
    parts.append(frame11(ref_vi(items[-1])))
    return S.cap("… ".join(parts))


def content_line(p):
    m = SEG.match(p)
    if not m:
        raise ValueError(f"unparsed: {p}")
    nums = S.parse_counts(m.group("cnt"))
    ans = counted_dis(nums, TE) + (KEHICI_VI if m.group("keh") else "")
    subj = subject(m.group("subj"))
    if m.group("mid") == Q_FULL:
        return f"{subj}, {S.THEN} {TE} {Q_DIS} {S.cap(ans)}."
    return f"{subj}…, {ans}."                       # vippayuttā…(pe…) te dhammā (abridged question)


# ================================================================== summary verse = ^3-305 (ch7), copied unchanged
PADA = "đề mục"
VERSE = {
    "Dhammāyatanaṃ dhammadhātu, dukkhasaccañca jīvitaṃ;":
        f"{S.cap(N['dhammāyatanaṃ'])}, {N['dhammadhātu']}, {N['dukkhasaccaṃ']} và sự sống;",
    "Saḷāyatanaṃ nāmarūpaṃ, cattāro ca mahābhavā.":
        "Sáu lĩnh vực nhận biết, phần tinh thần và vật chất, và bốn sự hiện hữu lớn.",
    "Jāti jarā ca maraṇaṃ, tikesvekūnavīsati;":
        f"{S.cap(N['jāti'])}, {N['jarā']} và {N['maraṇaṃ']}, trong các bộ ba có mười chín;",
    "Gocchakesu ca paññāsa, aṭṭha cūḷantare padā.":
        f"Và trong các nhóm có năm mươi, trong phần xen giữa nhỏ có tám {PADA}.",
    "Mahantare pannarasa, aṭṭhārasa tato pare;":
        "Trong phần xen giữa lớn có mười lăm, trong phần sau đó có mười tám;",
    "Tevīsa padasataṃ etaṃ, sampayoge na labbhatīti.":
        f"Một trăm hai mươi ba {PADA} này không tìm thấy trong sự gắn liền.",
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
    # ch8 frame with the first «gắn liền với X» negated = ch11 frame
    f = _formula("Xena ye dhammā sampayuttā, tehi dhammehi ye dhammā vippayuttā, te dhammā")
    f11 = f.replace(f"{S.cap(WHICH)} {ASSOC} X;", f"{S.cap(WHICH)} {DISSOC} X;", 1)
    assert f11 != f
    got = f"{S.cap(frame11('X'))}, {S.THEN} {TE} {Q_DIS}"
    assert got == f11, f"ch11 frame differs:\n{got}\n{f11}"
    f = _formula("Katihi vippayutto?")
    assert f.endswith(f"{S.cap(DISSOC)} N {S.KHANDHA}, N {S.AYATANA} và N {S.DHATU}."), f
    f = _formula("; ekenāyatanena ekāya dhātuyā kehici vippayutto.")
    assert f == KEHICI_VI + ".", f"{f}\n{KEHICI_VI}."
    f = _formula("na kehici khandhehi na kehici āyatanehi N dhātūhi vippayuttā")
    got = counted_dis((0, 0, 99), "chúng").replace("chín mươi chín", "N")
    assert got == f, f"na kehici differs:\n{got}\n{f}"
    assert _formula("te dhammā (answer subject)") == TE


def check_precedents():
    """Identical Pāli = identical Vietnamese: ch8 pieces and the ch7 verse ^3-305."""
    ch7 = (S.OUT / "7-chatthanayo.md").read_text(encoding="utf-8").splitlines()
    for v in VERSE.values():
        assert v in ch7, v
    ch8 = (S.OUT / "8-sattamanayo.md").read_text(encoding="utf-8")
    for piece in [f"{S.cap(WHICH)} {WITH} {N['vedanākkhandho']}… {WHICH} {WITH} {N['saññākkhandho']}…",
                  f"{WHICH} {DISSOC} {THOSE_REF}…, {TE} {DISSOC} {S.NUM[4]} {S.KHANDHA}",
                  f"{WHICH} {DISSOC} {THOSE_REF}…, không có {S.KHANDHA} nào, không có {S.AYATANA} nào mà {TE} "
                  f"{DISSOC}, {S.BUT} {DISSOC} ",
                  f"{WHICH} {DISSOC} {THOSE_REF}, {S.THEN} {TE} {Q_DIS} ",
                  KEHICI_VI + ". ^"]:
        assert piece in ch8, piece


def check_names():
    """Every name used occurs in the approved formulas file (pi-1 / pi-2 ones are asserted by S.check_reuse)."""
    txt = FORMULAS.read_text(encoding="utf-8")
    missing = [v for v in set(used) if f"= {v.split(' [')[0]}" not in txt]
    assert not missing, missing


S.NUM.setdefault(99, "chín mươi chín")   # placeholder used only by check_formulas (never in the text)


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_formulas()
    check_precedents()
    txt = render()
    check_names()
    assert "chín mươi chín" not in txt
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt and ".." not in txt
    assert "được được" not in txt and "là là" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    tagged = sorted({v for v in used if S.reuse_tag(v)})
    print(f"{NAME}: {n} segments; {len(set(used))} reference names ({len(tagged)} with pi-1/pi-2 tag); "
          f"{n_reuse} pi-1/pi-2 strings asserted")
