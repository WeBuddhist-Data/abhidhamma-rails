# -*- coding: utf-8 -*-
"""pi-3 Dhātukathā, Vietnamese plain zero-shot: chapter 13-dvadasamanayo.md (Dvādasamanayo, method 12,
sampayuttena saṅgahitaṃ asaṅgahitaṃ).

usage: python -I -X utf8 build_13_vi.py
Writes only AI_translation\\vietnamese\\pi-3-vietnamese-plain-zeroshot_split_chapters\\13-dvadasamanayo.md,
after B.check_sources() confirms that every pi-1 / pi-2 string (the sample's, ch4's, ch7's, ch8's, ch11's and
this file's) still occurs in the pi-1 / pi-2 Vietnamese rails text. Block IDs are copied from the Pāli at build time.
Frames are taken verbatim from the finished chapters: relative chain, «… gắn liền với nó / chúng», «tehi …»
from build_8_vi (E8); the instrumental members and the last-member pronoun rule from build_11_vi (E11);
the saṅgahitā main question from build_4_vi (E4); the inclusion answers from the sample (B.incl, B.Q_EXCL,
B.excl). Formulas new to this chapter: notes-13.md.
"""
import os, re, sys, unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as E4       # noqa: E402  (importing writes nothing)
import build_8_vi as E8       # noqa: E402  (importing writes nothing)
import build_11_vi as E11     # noqa: E402  (importing writes nothing)

CH = "13-dvadasamanayo.md"
N = 12  # method number (file 13)

# ---------------------------------------------------------------- shared frames (verbatim from earlier chapters)
REL, ASSOC, TE = E8.REL, E8.ASSOC, E8.TE
Q_MAIN = E4.Q_MAIN
assert REL == "đối với {x}, những hiện tượng nào"
assert ASSOC == "gắn liền với" and TE == "những hiện tượng đó"
assert Q_MAIN == ", thì những hiện tượng đó được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?"

# ---------------------------------------------------------------- members in the instrumental
SING = dict(E11.SING)
SING["manodhātuyā"] = "manodhātu"          # as ch8 INSTR


def member(p):
    """One instrumental member (lower-case Vietnamese) and whether it is plural (as build_11_vi.member)."""
    p = p.strip()
    p = p[:1].lower() + p[1:]
    plural = p.split()[-1].endswith(("ehi", "īhi", "ūhi"))
    v = B.vi_item(SING[p]) if p in SING else B.vi_item(E11.nominative(p))
    return v, plural


def chain_vi(chain):
    """'Aena ye dhammā… Bena ye dhammā… Cena ye dhammā' -> «Đối với A, những hiện tượng nào… đối với B, …»;
    pronoun of «… gắn liền với nó / chúng» = number of the last member (ch11 rule)."""
    parts = [x.strip() for x in chain.split("…")]
    out, last_plural = [], None
    for x in parts:
        assert x.endswith(" ye dhammā"), (x, chain)
        v, last_plural = member(x[:-len(" ye dhammā")])
        out.append(REL.format(x=v))
    return B.cap("… ".join(out)), (B.PRON_PL if last_plural else B.PRON_SG)


_LINE = re.compile(
    r"^(?P<chain>.+?) sampayuttā"
    r"(?:(?P<q>, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā\? Te dhammā )"
    r"|(?P<pe>…(?P<comma>,)? te dhammā ))"
    rf"(?P<inc>{B.COUNTS_RX}) saṅgahitā\. Katihi asaṅgahitā\? (?P<exc>{B.COUNTS_RX}) asaṅgahitā\.$", re.I)   # re.I: sentence-initial «Dvīhi», «Ekena», «Catūhi» (as B._SEG)


def segment_vi(line):
    line = line.replace("…pe…", "…")     # ^3-418 …pe… (between members and before «te dhammā»)
    m = _LINE.match(line)
    assert m, line
    chain, pron = chain_vi(m.group("chain"))
    head = f"{chain} {ASSOC} {pron}"
    if m.group("q"):
        tail = f"{Q_MAIN} {B.cap(TE)}"
    else:
        tail = "…" + (m.group("comma") or "") + f" {TE}"   # ^3-421 «sampayuttā…, te dhammā»: comma kept
    inc = B.incl(B.parse_counts(m.group("inc")))
    exc = B.excl(B.parse_counts(m.group("exc")), B.PRON_PL)
    return f"{head}{tail} {inc}. {B.Q_EXCL} {exc}."


# ---------------------------------------------------------------- closing verse of ^3-447 (uddāna)
B.pi1("Bộ đôi xen giữa lớn")          # mahantaraduka (pi-1 Mahantaradukaṃ)
PITTHI = B.pi1("Bộ đôi cuối")         # piṭṭhiduka (pi-1 Piṭṭhidukaṃ)
B.pi2("mười bốn năng lực")            # cuddasindriyā (pi-2 ^2-993)
PADA = "đề mục"                       # pada (as ch7 and the padaniddeso headings)
VERSE = {
    "Rūpakkhandhā cattāro, manāyatanameva ca;":
        f"{B.cap(B.NUM[4])} {B.KH} ngoài {B.KHANDHA['rūpakkhandho']}, và cả {B.AYATANA['manāyatanaṃ']};",
    "Viññāṇadhātuyo satta, dve saccā cuddasindriyā.":
        f"{B.cap(B.NUM[7])} {B.DH} thức, {B.NUM[2]} sự thật, {B.NUM[14]} năng lực.",
    "Paccaye dvādasa padā, tato upari soḷasa;":
        f"Trong phần điều kiện có {B.NUM[12]} {PADA}, từ đó trở đi có {B.NUM[16]};",
    "Tikesu aṭṭha gocchake, tecattālīsameva ca.":
        f"Trong các {B.SUBHEADINGS['Tikaṃ'].lower()} có {B.NUM[8]}, và trong các nhóm có cả bốn mươi ba.",
    "Mahantaraduke satta, padā piṭṭhidukesu cha;":
        f"Trong các bộ đôi xen giữa lớn có {B.NUM[7]}, trong các {PITTHI.lower()} có {B.NUM[6]} {PADA};",
    "Navamassa padassete, niddese saṅgahaṃ gatāti.":
        f"Những {PADA} này đã {B.INCL} trong phần giải thích {PADA} {B.ORDINAL[9]}.",
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
                if title == "Dvādasamanayo":
                    t = B.CHAPTER_TITLES[N + 1]
                elif title == "Sampayuttenasaṅgahitāsaṅgahitapadaniddeso":
                    t = B.niddesa_heading(N)
                else:
                    raise AssertionError(line)
                vi.append(f"{hashes} {t} {bid}")
                continue
            if body in VERSE:
                t = VERSE[body]
            elif body == "Sampayuttenasaṅgahitāsaṅgahitapadaniddeso dvādasamo.":
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
    assert "là là" not in text and "được được" not in text and ".." not in text
    with open(os.path.join(B.OUT_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"pi-1 strings OK: {n1}; pi-2 strings OK: {n2}; wrote {CH}")


if __name__ == "__main__":
    main()
