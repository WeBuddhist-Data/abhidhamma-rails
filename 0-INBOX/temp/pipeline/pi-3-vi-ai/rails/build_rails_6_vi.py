"""Builder for the Vietnamese rails of pi-3 chapter 6 (Pañcamanayo, «Phương pháp thứ năm»), plain audience.

Writes AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/6-pancamanayo.md only.
Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/6-pancamanayo.md) with the locked termbase and
the approved formulas (rails/vi-rails-formulas.md, the ch6 / ch14 piece, «tehi dhammehi ye dhammā …» and the
abridged answer). Shortened chain items follow chapter 3 («những hiện tượng nào cùng với X…», no verb; the frame
is on the last item). All shared strings come from build_rails_sample_vi (imported read-only); the frame pieces are
asserted against the formulas file, every pi-1 / pi-2 string against those rails (S.check_reuse), and every name
used against the formulas file. New strings: notes-rails-6.md.

usage: python -I -X utf8 build_rails_6_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "6-pancamanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ------------------------------------------------------------------ fixed strings (ch6)
WHICH = "những hiện tượng nào"                           # ye dhammā
WITH = "cùng với"                                        # X-ena / X-ehi
THOSE = "các hiện tượng đó"                              # tehi dhammehi
TE = "những hiện tượng ấy"                               # te dhammā
BY3_NEG = (f"theo cách gộp vào {S.KHANDHA}, theo cách gộp vào {S.AYATANA} "
           f"hay theo cách gộp vào {S.DHATU}")            # khandhasaṅgahena asaṅgahitā āyatana… dhātu… asaṅgahitā
Q_OUT_FULL = f"{S.OUT_} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?"

N, D = S.NAMES, S.DHAMMA_ATTR

# X in the instrumental (not «… dhammehi») -> subject name, unchanged
INSTR = {
    "rūpakkhandhena": N["rūpakkhandho"], "vedanākkhandhena": N["vedanākkhandho"],
    "saññākkhandhena": N["saññākkhandho"], "saṅkhārakkhandhena": N["saṅkhārakkhandho"],
    "viññāṇakkhandhena": N["viññāṇakkhandho"],
    "cakkhāyatanena": N["cakkhāyatanaṃ"], "phoṭṭhabbāyatanena": N["phoṭṭhabbāyatanaṃ"],
    "manāyatanena": N["manāyatanaṃ"], "dhammāyatanena": N["dhammāyatanaṃ"],
    "cakkhudhātuyā": N["cakkhudhātu"], "phoṭṭhabbadhātuyā": N["phoṭṭhabbadhātu"],
    "cakkhuviññāṇadhātuyā": N["cakkhuviññāṇadhātu"], "manodhātuyā": N["manodhātu"],
    "manoviññāṇadhātuyā": N["manoviññāṇadhātu"], "dhammadhātuyā": N["dhammadhātu"],
    "samudayasaccena": N["samudayasaccaṃ"], "maggasaccena": N["maggasaccaṃ"],
    "nirodhasaccena": N["nirodhasaccaṃ"],
    "avijjāya": N["avijjā"],
    "avijjāpaccayā saṅkhārena": N["avijjāpaccayā saṅkhārā"],      # name kept unchanged (as ch5)
    "saṅkhārapaccayā viññāṇena": N["saṅkhārapaccayā viññāṇaṃ"],
    "viññāṇapaccayā nāmarūpena": N["viññāṇapaccayā nāmarūpaṃ"],
    "nāmarūpapaccayā saḷāyatanena": N["nāmarūpapaccayā saḷāyatanaṃ"],
    "saḷāyatanapaccayā phassena": N["saḷāyatanapaccayā phasso"],
    "phassapaccayā vedanāya": N["phassapaccayā vedanā"],
    "vedanāpaccayā taṇhāya": N["vedanāpaccayā taṇhā"],
    "taṇhāpaccayā upādānena": N["taṇhāpaccayā upādānaṃ"],
    "kammabhavena": "sự hiện hữu dưới dạng nghiệp",               # (pi-2), without the ch2 variant (as ch5)
    "arūpabhavena": N["arūpabhavo"], "nevasaññānāsaññābhavena": N["nevasaññānāsaññābhavo"],
    "catuvokārabhavena": N["catuvokārabhavo"], "asaññābhavena": N["asaññābhavo"],
    "ekavokārabhavena": N["ekavokārabhavo"],
    "iddhipādena": N["iddhipādo"],
    "jātiyā": N["jāti"], "jarāya": N["jarā"], "maraṇena": N["maraṇaṃ"],
    "sokena": N["soko"], "paridevena": N["paridevo"], "dukkhena": N["dukkhaṃ"],
    "domanassena": N["domanassaṃ"], "upāyāsena": N["upāyāso"],
    "satipaṭṭhānena": N["satipaṭṭhānaṃ"], "sammappadhānena": N["sammappadhānaṃ"], "jhānena": N["jhānaṃ"],
    "appamaññāya": N["appamaññā"], "pañcahi indriyehi": N["pañcindriyāni"],
    "pañcahi balehi": N["pañca balāni"], "sattahi bojjhaṅgehi": N["satta bojjhaṅgā"],
    "ariyena aṭṭhaṅgikena maggena": N["ariyo aṭṭhaṅgiko maggo"],
    "phassena": N["phasso"], "vedanāya": N["vedanā"], "saññāya": N["saññā"], "cetanāya": N["cetanā"],
    "adhimokkhena": N["adhimokkho"], "manasikārena": N["manasikāro"], "cittena": N["cittaṃ"],
}
for _k in [k for k in N if k.endswith("ndriyaṃ")]:              # Cakkhundriyena … aññātāvindriyena
    INSTR[_k[: -len("ndriyaṃ")] + "ndriyena"] = N[_k]

# «X dhammehi» whose nominative key is not the regular conversion (reported)
ATTR_SPECIAL = {
    "upādādhammehi": D["upādā"],
    "vipākadhammadhammehi": D["vipākadhammadhammā"],              # «dhammehi» fused into the compound
    "paccupannārammaṇehi dhammehi": D["paccuppannārammaṇā"],      # spelling slip paccupanna- for paccuppanna-
    "na hetusahetukehi [na hetū sahetukehi (sī.), na hetūhi sahetukehi (syā. ka.)] dhammehi":
        D["na hetū sahetukā"] + " [khác chính tả (Sī.): na hetū sahetukehi; dị bản (Syā., Ka.): na hetūhi sahetukehi]",
}
VARIANT_PRECEDENT = "[khác chính tả (Syā., Ka.): lohitaṅgo; dị bản (?): lohitako]"   # pi-2 ^2-… two readings


def nom(w):
    """Instrumental plural word of a matrix attribute -> nominative plural (key form of S.DHAMMA_ATTR)."""
    if w.endswith("īhi"):
        return w[:-3] + "ino"            # ācayagāmīhi, maggādhipatīhi, rūpīhi, cittānuparivattīhi
    if w.endswith("bhūhi"):
        return w[:-3] + "uno"            # cittasahabhūhi -> cittasahabhuno
    if w.endswith("hetūhi"):
        return w[:-2]                    # hetūhi -> hetū
    if w.endswith("ehi"):
        return w[:-3] + "ā"
    return w                             # ceva, ca, na, no, dassanena, bhāvanāya, sukhāya, vedanāya …


used_names = []


def name_of(instr):
    """Instrumental Pāli X -> Vietnamese name (unchanged subject name)."""
    x = instr[0].lower() + instr[1:]
    if x in ATTR_SPECIAL:
        v = f"{S.DHAMMA_N} {ATTR_SPECIAL[x]}"
    elif x.endswith(" dhammehi"):
        key = " ".join(nom(w) for w in x[: -len(" dhammehi")].split())
        v = f"{S.DHAMMA_N} {D[key]}"
    else:
        v = INSTR[x]
    used_names.append(v)
    return v


def chain(subj, full_tail):
    """'A ye dhammā… B ye dhammā…pe… Z ye dhammā' -> «những hiện tượng nào cùng với A… … những hiện tượng nào
    <full_tail(Z)>»; a «…pe…» between items is the single «…» at the same spot."""
    subj = subj.replace("…pe…", "…")
    items = [s.strip() for s in subj.split("…") if s.strip()]
    for s in items:
        assert s.endswith(" ye dhammā"), s
    items = [s[: -len(" ye dhammā")] for s in items]
    parts = [f"{WHICH} {WITH} {name_of(s)}…" for s in items[:-1]]
    parts.append(full_tail(name_of(items[-1])))
    return " ".join(parts)


def neg_frame(x_vi):
    """«những hiện tượng nào không được gộp vào cùng với X theo cách gộp vào khối, … hay theo cách gộp vào yếu tố»."""
    return f"{WHICH} {S.OUT_} {WITH} {x_vi} {BY3_NEG}"


TAIL_P = " khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā"
TEHI = "tehi dhammehi ye dhammā"
Q_P = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi asaṅgahitā? Te dhammā "
LINE = re.compile(r"^(?P<subj>.+?)" + re.escape(TAIL_P) + r",? " + re.escape(TEHI)
                  + r"(?:(?P<full>" + re.escape(TAIL_P + Q_P) + r")|(?P<ab>…pe… te dhammā ))"
                  + r"(?P<cnt>.+) asaṅgahitā\.$")
missing_comma = []


def content_line(p, bid):
    m = LINE.match(p)
    assert m, p
    if not re.search(re.escape(TAIL_P) + ", " + re.escape(TEHI), p):
        missing_comma.append(bid)       # «… asaṅgahitā tehi dhammehi …»: rendered with the usual «;»
    head = S.cap(chain(m.group("subj"), neg_frame))
    nums = S.parse_counts(m.group("cnt"))
    assert all(nums), nums
    ans = f"{TE} {S.OUT_} {S.counts_vi(list(zip(S.CATS, nums)))}."
    if m.group("full"):
        return f"{head}; {neg_frame(THOSE)}, {S.THEN} {TE} {Q_OUT_FULL} {S.cap(ans)}"
    return f"{head}; {WHICH} {WITH} {THOSE}…, {ans}"


# ------------------------------------------------------------------ summary verse of ^3-227
V_RUPA = "vật chất"                                  # Rūpaṃ (termbase), also in maccurūpaṃ
VERSE = {
    "Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;":
        f"{S.cap(V_RUPA)}, {N['dhammāyatanaṃ']}, {N['dhammadhātu']}, nữ tính, nam tính, sự sống, "
        f"phần tinh thần và vật chất;",
    "Dve bhavā jāti jarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ.":
        f"Hai sự hiện hữu, {N['jāti']}, {N['jarā']}, sự chết, {V_RUPA}, điều {D['anārammaṇā']}, "
        f"điều {D['no cittā']}, điều {D['cittavippayuttā']}.",
    "Visaṃsaṭṭhaṃ samuṭṭhāna-sahabhu anuparivatti;":
        "Điều không hòa lẫn với nó, điều do nó sinh ra, điều cùng tồn tại với nó, điều vận hành theo nó;",
    "Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho.":
        f"Điều {D['bāhirā']}, điều {D['upādā']}, cả hai; phạm vi {S.reading('Syā.', 'dvevīsati')} "
        f"của phương pháp này đã được hiểu rõ.",
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


def check_frame():
    """The ch6 pieces must equal the approved formulas."""
    txt = FORMULAS.read_text(encoding="utf-8")

    def vi_of(prefix):
        ln = next(x for x in txt.splitlines() if x.startswith(prefix))
        return ln.split(" = ", 1)[1].replace(" (proposed for ch3-15)", "")

    piece = vi_of("… khandhasaṅgahena asaṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā (ch6")
    assert piece == f"… {S.OUT_} {WITH} X {BY3_NEG}", piece
    assert vi_of("tehi dhammehi ye dhammā …") == f"{WHICH} … {WITH} {THOSE} …"
    assert vi_of("…pe… te dhammā N") == f"…, {TE} (không) {S.IN} N {S.KHANDHA}, …"
    assert vi_of("te dhammā (answer subject)") == TE
    # the «; … thì những hiện tượng ấy …» joint as in the approved ch5 frame
    assert f"; {WHICH} {S.IN} {WITH} {THOSE} " in vi_of("Xena ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena "
                                                       "saṅgahitā dhātusaṅgahena saṅgahitā, tehi")
    assert f", {S.THEN} {TE} {Q_OUT_FULL} " in vi_of("Xena ye dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena "
                                                     "asaṅgahitā")
    # «…pe… te dhammā N …» after «tehi dhammehi ye dhammā» = ch3 abridged answer
    ch3 = (S.OUT / "3-dutiyanayo.md").read_text(encoding="utf-8")
    assert f"…, {TE} {S.OUT_} " in ch3 and f"{WHICH} {WITH} " in ch3


def check_names():
    """Every name used occurs in the approved formulas file (pi-1 / pi-2 ones are asserted by S.check_reuse)."""
    txt = FORMULAS.read_text(encoding="utf-8")
    missing = [v for v in set(used_names) if f"= {v.split(' [')[0]}" not in txt]
    assert not missing, missing
    t2 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI2_DIR.glob("*.md")))
    assert VARIANT_PRECEDENT in t2


def render():
    blocks = []
    for lines, bid in S.pali_segments(S.PALI / NAME):
        vi = translate_segment(lines, bid)
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_frame()
    txt = render()
    check_names()
    n = S.check_against_pali(txt, S.PALI / NAME)
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    assert "được được" not in txt and "là là" not in txt
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{NAME}: {n} segments; {len(set(used_names))} names checked; {n_reuse} pi-1/pi-2 strings asserted; "
          f"missing comma before «tehi»: {missing_comma}")
