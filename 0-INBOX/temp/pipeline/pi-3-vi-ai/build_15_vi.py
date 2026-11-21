# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 15-cuddasamanayo.md (Cuddasamanayo, method 14,
vippayuttena saṅgahitaṃ asaṅgahitaṃ), the last chapter, ending with the book colophon.

usage: python -I -X utf8 build_15_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\15-cuddasamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's, the imported chapters' and this
file's) still occurs in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Reused verbatim: the sample (B: inclusion answers, exclusion answers, ASX, BOOK_END), ch11 (E11: the
instrumental members, «Xena ye dhammā vippayuttā» with the pronoun of the last member), ch4 (inclusion
answer frame after a relative clause) and ch9 (E9.VERSE: the same closing verse). Notes: notes-15.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as E4       # noqa: E402  (importing writes nothing)
import build_9_vi as E9       # noqa: E402  (importing writes nothing)
import build_11_vi as E11     # noqa: E402  (importing writes nothing)

CH = "15-cuddasamanayo.md"
N = 14  # method number (file 15)

# ---------------------------------------------------------------- shared frames (coordinator; verbatim from ch4 / ch11)
REL, DISS, TE = E11.REL, E11.DISS, E11.TE
assert REL == "đối với {x}, những hiện tượng nào"
assert DISS == "không gắn liền với" and TE == "những hiện tượng đó"
Q_MAIN = E4.Q_MAIN
assert Q_MAIN == ", thì những hiện tượng đó được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"
REL_YE = "đối với {x}, những gì"     # ^3-487 '… dhammehi ye vippayuttā' (no «dhammā» after «ye»; as written)
B.pi2("những hiện tượng đó")
B.pi2("Đối với")
B.pi1("những hiện tượng nào")
B.pi1("không gắn liền với")
B.pi2("Bộ “Phân tích các hiện tượng” đã hoàn tất.")   # pi-2 ^2-1044 colophon pattern (B.BOOK_END)

# ---------------------------------------------------------------- members in the instrumental
SING = dict(E11.SING)
SING.update({  # singular members of this chapter not in ch11 -> B.vi_item key (Pāli nominative)
    "sotaviññāṇadhātuyā": "sotaviññāṇadhātu", "ghānaviññāṇadhātuyā": "ghānaviññāṇadhātu",
    "jivhāviññāṇadhātuyā": "jivhāviññāṇadhātu", "kāyaviññāṇadhātuyā": "kāyaviññāṇadhātu",
    "manodhātuyā": "manodhātu",
    "dukkhasaccena": "dukkhasaccaṃ",
    "kāmabhavena": "kāmabhavo", "upapattibhavena": "upapattibhavo", "saññābhavena": "saññābhavo",
    "pañcavokārabhavena": "pañcavokārabhavo",
})
WORD_EXC = dict(E11.WORD_EXC)
WORD_EXC["bahiddhāhi"] = "bahiddhā"          # bahiddhāhi dhammehi -> bahiddhā dhammā (matrix name)
FIX = dict(E11.FIX)
FIX["na hetuahetukā dhammā"] = "na hetū ahetukā dhammā"   # compound spelling, as ch11 na hetusahetukehi (reported)


def nominative(key):
    """'kusalehi dhammehi' -> 'kusalā dhammā' (ch11 rule, with this chapter's word exceptions)."""
    assert key.endswith("dhammehi"), key
    out = []
    for w in key.split():
        if w in WORD_EXC:
            out.append(WORD_EXC[w])
        elif w.endswith("ehi"):
            out.append(w[:-3] + "ā")
        elif w.endswith("īhi"):
            out.append(w[:-3] + "ino")
        elif w.endswith("ūhi"):
            out.append(w[:-3] + "ū")
        else:
            out.append(w)
    nom = " ".join(out)
    return FIX.get(nom, nom)


def member(p):
    """One instrumental member (lower-case Vietnamese) and whether it is plural."""
    p = p.strip()
    p = p[:1].lower() + p[1:]
    plural = p.split()[-1].endswith(("ehi", "īhi", "ūhi", "āhi"))
    v = B.vi_item(SING[p]) if p in SING else B.vi_item(nominative(p))
    return v, plural


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā… Cena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, …»;
    the pronoun of «không gắn liền với nó / chúng» follows the number of the last member (ch11 rule)."""
    parts = [x.strip() for x in chain.split("…")]
    out, last_plural = [], None
    for x in parts:
        if x.endswith(" ye dhammā"):
            v, last_plural = member(x[:-len(" ye dhammā")])
            out.append(REL.format(x=v))
        else:
            assert x == "paṇītehi dhammehi ye", (x, chain)      # ^3-487, «dhammā» missing in the Pāli
            v, last_plural = member(x[:-len(" ye")])
            out.append(REL_YE.format(x=v))
    return B.cap("… ".join(out)), (B.PRON_PL if last_plural else B.PRON_SG)


_LINE = re.compile(
    r"^(?P<chain>.+?) vippayuttā"
    r"(?:(?P<q>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā\? Te dhammā)|(?P<pe>… te dhammā))"
    rf"(?P<asx> asaṅkhataṃ khandhato ṭhapetvā)? (?P<inc>{B.COUNTS_RX}) saṅgahitā\. "
    rf"Katihi asaṅgahitā\? (?P<exc>{B.COUNTS_RX}) asaṅgahitā\.$", re.I)   # re.I: answers open «Ekena» / «Na kehici»


def segment_vi(line):
    line = line.replace("…pe…", "…").replace(" …", "…")   # ^3-462, ^3-471, ^3-517: stray space before «…»
    m = _LINE.match(line)
    assert m, line
    chain, pron = chain_vi(m.group("chain"))
    head = f"{chain} {DISS} {pron}"
    tail = f"{Q_MAIN} {B.cap(TE)}" if m.group("q") else f"… {TE}"
    pred = B.incl(B.parse_counts(m.group("inc")))
    first = f"{head}{tail}, {B.ASX}, {pred}." if m.group("asx") else f"{head}{tail} {pred}."
    return f"{first} {B.Q_EXCL} {B.excl(B.parse_counts(m.group('exc')), B.PRON_PL)}."


# ---------------------------------------------------------------- closing verse of ^3-518 (= ch9 ^3-318 verse) and colophon
VERSE = {k: v for k, v in E9.VERSE.items() if not k.startswith("Vippayuttenasampayuttapadaniddeso")}
assert len(VERSE) == 5
CLOSING = {
    "Vippayuttenasaṅgahitāsaṅgahitapadaniddeso cuddasamo.": B.niddesa_closing(N),
    "Dhātukathāpakaraṇaṃ niṭṭhitaṃ.": B.BOOK_END,
}
assert B.BOOK_END == "Bộ “Thảo luận về các yếu tố” đã hoàn tất."


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
                if title == "Cuddasamanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Vippayuttenasaṅgahitāsaṅgahitapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    t = B.SUBHEADINGS[title]
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body in CLOSING:
                t = CLOSING[body]
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
    assert "là là" not in text and "được được" not in text and ".." not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
