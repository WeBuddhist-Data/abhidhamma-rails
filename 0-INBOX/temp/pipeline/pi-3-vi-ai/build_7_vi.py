# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 7-chatthanayo.md (Chaṭṭhanayo, method 6,
Sampayogavippayogapadaniddeso: the first association method).

usage: python -I -X utf8 build_7_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\7-chatthanayo.md,
after the pi-1 / pi-2 string checks (B.check_sources(), which also covers the strings registered here) pass.
Reuses the approved sample builder (build_sample_vi) verbatim; the coordinator's SHARED FRAMES are fixed
strings below; formulas new to this chapter are in notes-7.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "7-chatthanayo.md"
METHOD = 6                                  # Chaṭṭhanayo = method 6 = file 7

# ---------------------------------------------------------------- shared frames (coordinator)
ASSOC = B.pi1("gắn liền với")                # sampayutta
DISS = "không " + ASSOC                     # vippayutta
Q_FULL = "{s} " + ASSOC + " bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
#   X katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttoti?
Q_ABBR = "{s} " + ASSOC + " bao nhiêu?"      # X…pe… sampayuttoti?  (the elided katihi … carries «bao nhiêu»)
NATTHI = "Không có."                        # Natthi.
Q_DISS = B.cap(DISS) + " bao nhiêu?"         # Katihi vippayutto?  = «Không gắn liền với bao nhiêu?»
KEHICI = "một số hiện tượng trong"           # kehici (… kehici sampayutto / vippayutto)


# ---------------------------------------------------------------- counts (any subset of khandha / āyatana / dhātu)
K_RX = r"na kehici khandhehi|ekena khandhena|\S+ khandhehi"
A_RX = r"na kehici āyatanehi|\S+āyatane(?:na|hi)"
D_RX = r"na kāhici dhātūhi|ekāya dhātuyā|\S+ dhātūhi"


def split_counts(s):
    """'X tīhi khandhehi ekenāyatanena sattahi dhātūhi' -> ('X', [3, 1, 7]); a missing slot is absent (False),
    a 'na kehici' slot is None."""
    slots = [False, False, False]
    for i, rx, table in ((2, D_RX, B._ND), (1, A_RX, B._NA), (0, K_RX, B._NK)):
        m = re.search(rf"(?:^| )({rx})$", s, re.I)
        if m:
            w = m.group(1)
            if w.lower().startswith("na "):
                slots[i] = None
            else:
                key = (w if i == 1 else w.split()[0])
                key = key[:1].lower() + key[1:]            # sentence-initial 'Catūhi', 'Ekena' …
                slots[i] = table[key]
            s = s[:m.start()]
    assert slots != [False, False, False], s
    return s, slots


def pos_counts(slots):
    """[3, 1, 7] -> 'ba khối, một lĩnh vực nhận biết, bảy yếu tố' (missing slots skipped)."""
    assert None not in slots, slots
    return ", ".join(B.count_phrase(n, noun) for n, noun in zip(slots, B.NOUNS) if n is not False)


def diss_answer(slots, pron):
    """Answer of 'Katihi vippayutto?' (capitalised, no stop).
    positive: 'Không gắn liền với bốn khối, một lĩnh vực nhận biết, bảy yếu tố'
    na kehici …: 'Không có khối nào, không có lĩnh vực nhận biết nào mà nó không gắn liền với, nhưng không gắn
    liền với ba yếu tố' (the sample's «na kehici … asaṅgahitā» frame, B.excl)."""
    items = [(n, noun) for n, noun in zip(slots, B.NOUNS) if n is not False]
    runs = []
    for n, noun in items:
        pos = n is not None
        if runs and runs[-1][0] == pos:
            runs[-1][1].append((n, noun))
        else:
            runs.append((pos, [(n, noun)]))
    parts = []
    for pos, its in runs:
        if pos:
            parts.append(DISS + " " + ", ".join(B.count_phrase(n, noun) for n, noun in its))
        else:
            parts.append(", ".join(f"không có {noun} nào" for _, noun in its) + f" mà {pron} {DISS}")
    return B.cap(", nhưng ".join(parts))


# ---------------------------------------------------------------- subjects
FIX = {   # Pāli as written -> as meant (plain spelling slip / missing punctuation; reported)
    "Dassanena pahātabbā dhammā bhāvanāya pahātabbā dhammā…":       # ^3-269: '…' missing between the two names
        "Dassanena pahātabbā dhammā… bhāvanāya pahātabbā dhammā…",
    "na hetusahetukā dhammā": "na hetū sahetukā dhammā",             # ^3-279: compound spelling of 'na hetū sahetukā'
}


def subject_vi(s):
    for a, b in FIX.items():
        s = s.replace(a, b)
    return B.vi_subject(s)


# ---------------------------------------------------------------- one content line
Q_FULL_RX = re.compile(r"^(?P<s>.+?) katihi khandhehi katihāyatanehi katihi dhātūhi sampayutt\w+ti\?$")
Q_ABBR_RX = re.compile(r"^(?P<s>.+?) sampayutt\w+ti\?$")
Q_DISS_RX = re.compile(r"^Katihi vippayutt\w+\?$")


def clause_vi(c, first):
    """One clause ('…;' separated) of a statement sentence, without its final punctuation."""
    m = re.fullmatch(r"(?P<body>.+?) (?P<keh>kehici )?(?P<v>(?:sampayutt|vippayutt)\w+)", c)
    assert m, c
    body, keh, v = m.group("body"), m.group("keh"), m.group("v")
    subj, slots = split_counts(body)
    verb = ASSOC if v.startswith("sampayutt") else DISS
    if None in slots:                                       # na kehici … vippayutto (answer only)
        assert not subj and not keh and verb == DISS and first, c
        pron = B.PRON_SG if v.endswith(("o", "aṃ")) else B.PRON_PL
        return diss_answer(slots, pron)
    pred = verb + " " + (KEHICI + " " if keh else "") + pos_counts(slots)
    if subj:
        assert first, c
        sv = subject_vi(subj)
        if ASSOC in sv.split("…")[-1]:
            # last member ends in «… gắn liền với X»: «thì» before the predicate (the sample's B.THI rule
            # against «được được»), so «gắn liền với X gắn liền với …» is not read as one phrase
            return f"{sv} {B.THI} {pred}"
        return f"{sv} {pred}"
    return B.cap(pred) if first else pred


def sentence_vi(s):
    m = Q_FULL_RX.match(s)
    if m:
        return Q_FULL.format(s=subject_vi(m.group("s")))
    if Q_DISS_RX.match(s):
        return Q_DISS
    m = Q_ABBR_RX.match(s)
    if m:
        return Q_ABBR.format(s=subject_vi(m.group("s")))
    if s == "Natthi.":
        return NATTHI
    assert s.endswith("."), s
    clauses = s[:-1].split("; ")
    return "; ".join(clause_vi(c, i == 0) for i, c in enumerate(clauses)) + "."


def line_vi(body):
    sents = re.split(r"(?<=[.?]) ", body)
    return " ".join(sentence_vi(x) for x in sents)


# ---------------------------------------------------------------- summary verse of ^3-305 (uddāna) and closing
B.pi1("sự sống")                               # jīvitaṃ (pi-1 ^1-19 «… sự sống, năng lực sống»)
B.pi1("Bộ đôi xen giữa nhỏ")                    # Cūḷantaradukaṃ -> cūḷantara = «phần xen giữa nhỏ»
B.pi1("Bộ đôi xen giữa lớn")                    # Mahantaradukaṃ -> mahantara = «phần xen giữa lớn»
B.pi1("Ma trận bộ ba")                          # tika = bộ ba
B.pi1("Nhóm về gốc rễ")                         # gocchaka = nhóm (as in ch5)
B.pi2("sáu lĩnh vực nhận biết")                 # saḷāyatanaṃ
B.pi2("phần tinh thần và vật chất")             # nāmarūpaṃ
PADA = "đề mục"                                 # pada (as in ch5 and the padaniddeso headings)
VERSE = {
    "Dhammāyatanaṃ dhammadhātu, dukkhasaccañca jīvitaṃ;":
        f"{B.cap(B.AYATANA['dhammāyatanaṃ'])}, {B.DHATU['dhammadhātu']}, "
        f"{B.SACCA['dukkhasaccaṃ']} và sự sống;",
    "Saḷāyatanaṃ nāmarūpaṃ, cattāro ca mahābhavā.":
        "Sáu lĩnh vực nhận biết, phần tinh thần và vật chất, cùng bốn sự hiện hữu lớn.",
    "Jāti jarā ca maraṇaṃ, tikesvekūnavīsati;":
        f"{B.cap(B.OTHER['jāti'])}, {B.OTHER['jarā']} và {B.OTHER['maraṇaṃ']}, trong các bộ ba có mười chín;",
    "Gocchakesu ca paññāsa, aṭṭha cūḷantare padā.":
        f"Trong các nhóm có năm mươi, trong phần xen giữa nhỏ có {B.NUM[8]} {PADA}.",
    "Mahantare pannarasa, aṭṭhārasa tato pare;":
        f"Trong phần xen giữa lớn có {B.NUM[15]}, phần sau đó có {B.NUM[18]};",
    "Tevīsa padasataṃ etaṃ, sampayoge na labbhatīti.":
        f"Một trăm hai mươi ba {PADA} này không có trong {B.ASSOC_N}.",
    "Sampayogavippayogapadaniddeso chaṭṭho.": B.niddesa_closing(METHOD),
}


# ---------------------------------------------------------------- build
def build():
    out = []
    for seg in B._segments(os.path.join(B.PALI_DIR, NAME)):
        vi = []
        for i, line in enumerate(seg):
            idm = B.ID.search(line)
            bid = idm.group(1) if idm else None
            body = B.ID.sub("", line).strip()
            h = B._heading(line)
            if h:
                hashes, title, _ = h
                if title == "Chaṭṭhanayo":
                    t = B.CHAPTER_TITLES[METHOD + 1]
                elif title == "Sampayogavippayogapadaniddeso":
                    t = B.niddesa_heading(METHOD)
                else:
                    t = B.SUBHEADINGS[title]
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            else:
                assert i == 0, line
                t = line_vi(body)
            vi.append(t + (f" {bid}" if bid else ""))
        out.append("\n".join(vi))
    return "\n\n".join(out) + "\n"


def main():
    n1, n2 = B.check_sources()
    text = build()
    assert unicodedata.normalize("NFC", text) == text
    assert "—" not in text and "–" not in text and ":-" not in text and "…." not in text
    assert "là là" not in text and "được được" not in text
    with open(os.path.join(B.OUT_DIR, NAME), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {NAME}")


if __name__ == "__main__":
    main()
