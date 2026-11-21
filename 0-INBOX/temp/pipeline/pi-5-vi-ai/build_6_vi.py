# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 6: 6-atitakkhandhadikatha.md (Atītakkhandhādikathā,
^5-6-0 … ^5-298).

Imports the approved sample builder (build_sample_vi) for every debate frame; the chapter's own repeated
phrases are fixed strings below, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there; the sample's per-line checks (IDs, dashes, quotes, NFC,
foreign letters) are run against the Pāli.

run:  python -I -X utf8 build_6_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "6-atitakkhandhadikatha.md"

# ================================================================ terms
PAST = "quá khứ"            # atītaṃ (the past, as subject)
FUT = "tương lai"           # anāgataṃ
PRES = "hiện tại"           # paccuppannaṃ
KH_PL = "các khối"          # khandhā
KH_SG = "khối"              # khandho
AY = "lĩnh vực nhận biết"   # āyatanaṃ (core term)
DH = "yếu tố"               # dhātu (core term)
KDA = f"{KH_PL}, {DH}, {AY}"   # khandhā dhātu āyatanaṃ / āyatananti
AT = "tồn tại"              # atthi (sample)
NAT = "không tồn tại"       # natthi (sample)

RUPA_A, RUPA_F, RUPA_P = (f"{B.RUPA} {t}" for t in (PAST, FUT, PRES))        # atītaṃ / anāgataṃ / paccuppannaṃ rūpaṃ
VIN_A, VIN_F, VIN_P = (f"{B.VINNANA} {t}" for t in (PAST, FUT, PRES))        # … viññāṇaṃ
VED_A = f"{B.VEDANA} {PAST}"                                                  # atītā vedanā
SAN_A = f"{B.SANNA} {PAST}"                                                   # atītā saññā
SANKH_A = f"{B.SANKHARA} {PAST}"                                              # atītā saṅkhārā

ANF = f"{KDA} {PAST} và {FUT}, chúng {NAT}"
# atītānāgatā khandhā dhātu āyatanaṃ natthi cete (cete = ca ete, aṭṭhakathā ^5-231)

# ================================================================ sutta passages
NIRUTTI = "phạm vi của cách diễn đạt"      # niruttipathā (pi-1 ^1-M2-107)
ADHIVACANA = "phạm vi của tên gọi"          # adhivacanapathā (pi-1 ^1-M2-106)
PANNATTI = "khái niệm"                      # paññatti[pathā] (pi-1 ^1-M2-108 «phạm vi của khái niệm»)
VINNUHI = "bởi những người hiểu biết"       # viññūhi (new)
SUTTA_NIRUTTI = f"“Này các tỳ-khưu, có ba phạm vi này của cách diễn đạt, {ADHIVACANA}, {PANNATTI}… {VINNUHI}…”"
# "tayome, bhikkhave, niruttipathā adhivacanapathā paññatti…pe… viññūhīti…pe…"
# tayome = «có ba … này» (ch2 «có năm hiện tượng này»); paññatti…pe… cut inside the compound: rendered as written.

KHANDHA_TAIL = ("dù thuộc quá khứ, thuộc tương lai hay thuộc hiện tại, ở nơi bản thân hay ở bên ngoài bản thân, "
                "ở dạng thô hay ở dạng vi tế, thấp kém hay ưu việt, ở xa hay ở gần")   # pi-2 ^2-2 … ^2-26
SUTTA_KHANDHA = (f"“Này các tỳ-khưu, bất cứ {B.RUPA} nào, {KHANDHA_TAIL}, đó được gọi là khối {B.RUPA}. "
                 f"Bất cứ {B.VEDANA} nào… bất cứ {B.SANNA} nào… bất cứ sự tạo tác nào… "
                 f"bất cứ {B.VINNANA} nào, dù thuộc quá khứ, thuộc tương lai hay thuộc hiện tại… "
                 f"đó được gọi là khối {B.VINNANA}”")
# "yaṃ kiñci, bhikkhave, rūpaṃ atītānāgatapaccuppannaṃ … yaṃ dūre santike vā, ayaṃ vuccati rūpakkhandho. Yā kāci
# vedanā… yā kāci saññā… ye keci saṅkhārā… yaṃ kiñci viññāṇaṃ atītānāgatapaccuppannaṃ…pe… ayaṃ vuccati
# viññāṇakkhandho"ti  (pi-2 khandhavibhaṅga wording without «gom tất cả lại làm một và thu tóm lại –», absent here)

CROSS = [
    ("lĩnh vực nhận biết", 2), ("yếu tố", 1), ("khối vật chất", 2), ("khối thức", 2),
    ("Các hiện tượng thuộc quá khứ", 1), ("Các hiện tượng thuộc tương lai", 1), ("Các hiện tượng thuộc hiện tại", 1),
    (NIRUTTI, 1), (ADHIVACANA, 1), ("phạm vi của khái niệm", 1),   # «Này các tỳ-khưu» (bhikkhave): pi-5 ch2 / ch4, not in pi-1..4
    ("Bất cứ vật chất nào, " + KHANDHA_TAIL + ",", 2), ("Bất cứ thức nào, dù thuộc quá khứ, thuộc tương lai hay "
                                                          "thuộc hiện tại", 2),
    ("Bất cứ cảm giác nào", 2), ("Bất cứ tri giác nào", 2), ("Bất cứ sự tạo tác nào", 2),
    ("đó được gọi là khối vật chất", 2), ("đó được gọi là khối thức", 2),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"ch6 cross-book asserts: {len(CROSS)} strings found in pi-1..4 rails")


# ================================================================ line patterns
AM, NHP = B.AMANTA, B.NA_HEVAM_PE


def is_(s, x):
    return f"{s} là {x}"


def simple(s, first, full, var="", head=None):
    """S khandhāti? Āmantā. S atthīti? Na hevaṃ vattabbe…pe… S āyatananti? … S khandhā dhātu āyatananti? …
    full=False: … S āyatanaṃ…pe… S dhātu…pe… S khandhā dhātu āyatananti? Āmantā. S atthīti? …"""
    out = f"{B.Q(head or is_(s, first))} {AM} {B.Q(f'{s} {AT}')} {NHP}"
    if full:
        for x in (AY, DH):
            out += f" {B.q(is_(s, x))} {AM} {B.Q(f'{s} {AT}')} {NHP}"
    else:
        out += f" {is_(s, AY)}… {is_(s, DH)}…"
    out += f" {B.q(is_(s, KDA) + var)} {AM} {B.Q(f'{s} {AT}')} {NHP}"
    return out


def contrast(a, b, ex, first, full):
    """A khandhā A atthīti? Āmantā. B khandhā B atthīti? Na hevaṃ vattabbe…pe… (āyatanaṃ, dhātu, khandhā dhātu
    āyatanaṃ in full, or with full=False: A āyatanaṃ…pe… A dhātu…pe… A khandhā dhātu āyatanaṃ … )"""
    def pair(x, lower):
        qa = (B.q if lower else B.Q)(f"{is_(a, x)}, {a} {ex}")
        return f"{qa} {AM} {B.Q(f'{is_(b, x)}, {b} {ex}')} {NHP}"
    out = pair(first, False)
    if full:
        for x in (AY, DH):
            out += " " + pair(x, True)
    else:
        out += f" {is_(a, AY)}… {is_(a, DH)}…"
    return out + " " + pair(KDA, True)


def build():
    d = B.Doc()
    d.head(3, B.KATHA.format(x="các khối quá khứ và các mục khác"), "5-6-0")    # Atītakkhandhādikathā
    d.head(4, "Không dựa trên chứng cứ từ kinh", "5-6-1-0")                      # Nasuttasādhanaṃ
    var = f" [{B.SPELL} (Syā.): khandhadhātuāyatananti]"
    l21b = contrast(VIN_F, VIN_P, NAT, KH_SG, False)
    d.seg("5-297",
          simple(PAST, KH_PL, True, var=var),
          simple(FUT, KH_PL, True),
          contrast(PRES, PAST, AT, KH_PL, True),
          contrast(PRES, FUT, AT, KH_PL, True),
          contrast(PAST, PRES, NAT, KH_PL, True),
          contrast(FUT, PRES, NAT, KH_PL, False),
          simple(RUPA_A, KH_SG, True),
          simple(RUPA_F, KH_SG, False),
          contrast(RUPA_P, RUPA_A, AT, KH_SG, False),
          contrast(RUPA_P, RUPA_F, AT, KH_SG, False),
          contrast(RUPA_A, RUPA_P, NAT, KH_SG, False),
          contrast(RUPA_F, RUPA_P, NAT, KH_SG, False),
          simple(VIN_A, KH_SG, False, head=f"{VED_A}… {SAN_A}… {SANKH_A}… {is_(VIN_A, KH_SG)}"),
          simple(VIN_F, KH_SG, False),
          contrast(VIN_P, VIN_A, AT, KH_SG, False),
          contrast(VIN_P, VIN_F, AT, KH_SG, False),
          contrast(VIN_A, VIN_P, NAT, KH_SG, False) + " " + l21b[:1].lower() + l21b[1:])
    d.head(4, "Chứng cứ từ kinh", "5-6-2-0")                                     # Suttasādhanaṃ
    d.seg("5-298",
          f"{B.NA_VATTABBAM_Q(ANF)} {AM} {B.NANU_VUTTAM} {SUTTA_NIRUTTI}. {B.ATTHEVA} {AM} {B.TENA_HI_NA(ANF)}",
          f"{B.Q(ANF)} {AM} {B.NANU_VUTTAM} {SUTTA_KHANDHA}. {B.ATTHEVA} {AM} {B.TENA_HI_NA(ANF)}",
          B.KATHA_END.format(x="các khối quá khứ và các mục khác"))
    return d.text()


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
