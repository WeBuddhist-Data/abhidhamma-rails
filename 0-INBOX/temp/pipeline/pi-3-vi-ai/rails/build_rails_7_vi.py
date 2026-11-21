"""Builder for the Vietnamese rails of pi-3 chapter 7 (Chaṭṭhanayo, «Phương pháp thứ sáu»), plain audience.

Writes AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/7-chatthanayo.md only.
Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/7-chatthanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md) and the
approved ch7 frames of rails/vi-rails-formulas.md (sampayutta / vippayutta, kehici). All shared strings come from
build_rails_sample_vi (imported read-only as S); the ch7 frames are asserted against the formulas file, and the
pi-1 / pi-2 strings used are asserted to still occur in those rails. New strings: notes-rails-7.md.

usage: python -I -X utf8 build_rails_7_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "7-chatthanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ================================================================== fixed strings (approved ch7 frames)
SAM = "gắn liền với"                      # sampayutto / -ā / -aṃ (with the instrumental)
VIP = "không gắn liền với"                # vippayutto / -ā / -aṃ
KEHICI = "một số hiện tượng thuộc"        # kehici (termbase «một số hiện tượng»)
NATTHI = "Không có."                      # Natthi.
Q_SAM_FULL = f"{SAM} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?"
Q_SAM_SHORT = f"{SAM} {S.HOW_MANY}?"      # …pe… sampayuttanti?
Q_VIP = f"{S.cap(VIP)} {S.HOW_MANY}?"     # Katihi vippayutto?
PRON = {"o": "nó", "aṃ": "nó", "ā": "chúng"}

# ================================================================== subjects
EXTRA_NAMES = {
    "kammabhavo": "sự hiện hữu dưới dạng nghiệp",          # (pi-2); no variant bracket here (as ch5)
}
SUBJ_FIX = {
    # ^3-269: «…» missing between the first two items; rendered as meant (as ^3-298)
    "Dassanena pahātabbā dhammā bhāvanāya pahātabbā dhammā…":
        "Dassanena pahātabbā dhammā… bhāvanāya pahātabbā dhammā…",
}
ATTR_FIX = {
    "na hetusahetukā": "na hetū sahetukā",                  # ^3-279 spelling (compound) rendered as meant
}


def item_vi(p):
    p = p.strip()
    key = p[0].lower() + p[1:]
    if key in EXTRA_NAMES:
        return EXTRA_NAMES[key]
    if p.endswith(" dhammā"):
        a = key[: -len(" dhammā")]
        if a in ATTR_FIX:
            return f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR_FIX[a]]}"
    return S.item_vi(p)


def subject_vi(p):
    """Pāli subject (items separated by «…», «…pe…» allowed) -> Vietnamese, first letter capital."""
    for a, b in SUBJ_FIX.items():
        if p.startswith(a):
            p = b + p[len(a):]
    p = p.replace("…pe…", "…").strip()
    trailing = p.endswith("…")
    items = [x for x in (s.strip() for s in p.split("…")) if x]
    vi = "… ".join(item_vi(x) for x in items) + ("…" if trailing else "")
    if not trailing and "gắn liền" in item_vi(items[-1]):
        vi = f"{vi} {S.THEN}"     # «… gắn liền với X thì gắn liền với …» (readability, like S.subj_head)
    return S.cap(vi)


# ================================================================== answer parts
PART = re.compile(r"^(?:(?P<k>na kehici khandhehi|ekena khandhena|\S+ khandhehi) ?)?"
                  r"(?:(?P<a>na kehici āyatanehi|\S+āyatanena|\S+āyatanehi) ?)?"
                  r"(?:(?P<d>na kāhici dhātūhi|ekāya dhātuyā|\S+ dhātūhi) ?)?"
                  r"(?P<keh>kehici )?(?P<v>sampayutt|vippayutt)(?P<e>o|ā|aṃ)$")


def _num(cat, s):
    if s.startswith("na "):
        return 0
    if cat == S.KHANDHA:
        return S.K_NUM[s.split()[0]]
    if cat == S.AYATANA:
        return S.A_NUM[re.sub(r"āyatane(?:hi|na)$", "", s)]
    return S.D_NUM[s.split()[0]]


def part_vi(p):
    """One «;»-part of an answer -> Vietnamese (lower-case start)."""
    p = p[0].lower() + p[1:]
    m = PART.match(p)
    assert m, p
    verb = VIP if m.group("v") == "vippayutt" else SAM
    nums = [(c, _num(c, m.group(g))) for c, g in zip(S.CATS, "kad") if m.group(g)]
    assert nums, p
    if any(n == 0 for _, n in nums):            # Na kehici khandhehi na kehici āyatanehi N dhātūhi vippayutto
        assert verb == VIP and not m.group("keh"), p
        groups = []
        for c, n in nums:
            z = n == 0
            if groups and groups[-1][0] == z:
                groups[-1][1].append((c, n))
            else:
                groups.append((z, [(c, n)]))
        out = []
        for z, items in groups:
            if z:
                out.append(", ".join(f"không có {c} nào" for c, _ in items) + f" mà {PRON[m.group('e')]} {verb}")
            else:
                out.append(f"{verb} {S.counts_vi(items)}")
        return f", {S.BUT} ".join(out)
    if m.group("keh"):
        return f"{verb} {KEHICI} {S.counts_vi(nums)}"
    return f"{verb} {S.counts_vi(nums)}"


def answer_vi(a):
    """'Catūhi khandhehi … vippayutto; ekenāyatanena ekāya dhātuyā kehici vippayutto.' -> sentence."""
    assert a.endswith("."), a
    return S.cap("; ".join(part_vi(x) for x in a[:-1].split("; "))) + "."


# ================================================================== content lines
VSPLIT = re.compile(r" Katihi vippayutt(?:o|ā|aṃ)\? ")
Q_FULL = re.compile(r"^(?P<s>.+?) katihi khandhehi katihāyatanehi katihi dhātūhi sampayutt\w+ti\? Natthi\.$")
Q_SHORT = re.compile(r"^(?P<s>.+?)\s*sampayutt\w+ti\? Natthi\.$")
POS = re.compile(r"^(?P<s>.+?) (?P<r>(?:ekena khandhena|\S+ khandhehi) .+)$")


def content_line(p):
    parts = VSPLIT.split(p)
    assert len(parts) == 2, p
    head, neg = parts
    m = Q_FULL.match(head)
    if m:
        h = f"{subject_vi(m.group('s'))} {Q_SAM_FULL} {NATTHI}"
    else:
        m = Q_SHORT.match(head)
        if m:
            h = f"{subject_vi(m.group('s'))} {Q_SAM_SHORT} {NATTHI}"
        else:
            m = POS.match(head)
            assert m, head
            r = answer_vi(m.group("r"))
            h = f"{subject_vi(m.group('s'))} {S.low(r)}"
    return f"{h} {Q_VIP} {answer_vi(neg)}"


# ================================================================== summary verse of ^3-305
PADA = "đề mục"                                         # padā (verse), as ch4 / ch5
VERSE = {
    "Dhammāyatanaṃ dhammadhātu, dukkhasaccañca jīvitaṃ;":
        f"{S.cap(S.NAMES['dhammāyatanaṃ'])}, {S.NAMES['dhammadhātu']}, {S.NAMES['dukkhasaccaṃ']} và sự sống;",
    "Saḷāyatanaṃ nāmarūpaṃ, cattāro ca mahābhavā.":
        "Sáu lĩnh vực nhận biết, phần tinh thần và vật chất, và bốn sự hiện hữu lớn.",
    "Jāti jarā ca maraṇaṃ, tikesvekūnavīsati;":
        f"{S.cap(S.NAMES['jāti'])}, {S.NAMES['jarā']} và {S.NAMES['maraṇaṃ']}, trong các bộ ba có mười chín;",
    "Gocchakesu ca paññāsa, aṭṭha cūḷantare padā.":
        f"Và trong các nhóm có năm mươi, trong phần xen giữa nhỏ có tám {PADA}.",
    "Mahantare pannarasa, aṭṭhārasa tato pare;":
        "Trong phần xen giữa lớn có mười lăm, trong phần sau đó có mười tám;",
    "Tevīsa padasataṃ etaṃ, sampayoge na labbhatīti.":
        f"Một trăm hai mươi ba {PADA} này không tìm thấy trong sự gắn liền.",
}
REUSE7 = [  # (Pāli, Vietnamese as reused, book)
    ("saḷāyatanaṃ (nāmarūpapaccayā saḷāyatanaṃ)", "sáu lĩnh vực nhận biết", 2),
    ("nāmarūpaṃ", "phần tinh thần và vật chất", 2),
    ("Cūḷantaradukaṃ", "xen giữa nhỏ", 1),
    ("Mahantaradukaṃ", "xen giữa lớn", 1),
]


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


# ================================================================== checks
def check_frames():
    """Each approved ch7 frame occurs in the formulas file, and the built lines equal it with X / N filled in."""
    txt = FORMULAS.read_text(encoding="utf-8")
    approved = [
        "X gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố? Không có.",
        "X… gắn liền với bao nhiêu? Không có.",
        "Không gắn liền với bao nhiêu? Không gắn liền với N khối, N lĩnh vực nhận biết và N yếu tố.",
        "X gắn liền với ba khối, ….",
        "; không gắn liền với một số hiện tượng thuộc một lĩnh vực nhận biết và một yếu tố.",
        "; gắn liền với một số hiện tượng thuộc một khối, một lĩnh vực nhận biết và một yếu tố.",
        "không có khối nào, không có lĩnh vực nhận biết nào mà chúng không gắn liền với, nhưng không gắn liền với "
        "N yếu tố",
    ]
    for a in approved:
        assert f"= {a} (proposed for ch3-15)" in txt, a
    rk = S.NAMES["rūpakkhandho"]
    b1 = content_line("Rūpakkhandho katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttoti? Natthi. "
                      "Katihi vippayutto? Catūhi khandhehi ekenāyatanena sattahi dhātūhi vippayutto; "
                      "ekenāyatanena ekāya dhātuyā kehici vippayutto.")
    e1 = (approved[0].replace("X", S.cap(rk)) + " "
          + approved[2].replace("N khối, N lĩnh vực nhận biết và N yếu tố",
                                S.counts_vi([(S.KHANDHA, 4), (S.AYATANA, 1), (S.DHATU, 7)]))[:-1]
          + approved[4])
    assert b1 == e1, f"\n{b1}\n{e1}"
    b2 = content_line("Rūpabhavo…pe… sampayuttoti? Natthi. Katihi vippayutto? "
                      "Na kehici khandhehi na kehici āyatanehi tīhi dhātūhi vippayutto.")
    e2 = (approved[1].replace("X", S.cap(S.NAMES["rūpabhavo"])) + f" {Q_VIP} "
          + S.cap(approved[6].replace("chúng", "nó").replace("N yếu tố", "ba yếu tố")) + ".")
    assert b2 == e2, f"\n{b2}\n{e2}"
    b3 = content_line("Saṅkhārakkhandho tīhi khandhehi ekenāyatanena sattahi dhātūhi sampayutto; "
                      "ekena khandhena ekenāyatanena ekāya dhātuyā kehici sampayutto. Katihi vippayutto? "
                      "Ekena khandhena dasahāyatanehi dasahi dhātūhi vippayutto; "
                      "ekenāyatanena ekāya dhātuyā kehici vippayutto.")
    e3 = (f"{S.cap(S.NAMES['saṅkhārakkhandho'])} {SAM} "
          f"{S.counts_vi([(S.KHANDHA, 3), (S.AYATANA, 1), (S.DHATU, 7)])}" + approved[5] + f" {Q_VIP} "
          + approved[2].split("? ", 1)[1].replace("N khối, N lĩnh vực nhận biết và N yếu tố",
                                                   S.counts_vi([(S.KHANDHA, 1), (S.AYATANA, 10), (S.DHATU, 10)]))[:-1]
          + approved[4])
    assert b3 == e3, f"\n{b3}\n{e3}"
    assert e3.startswith(approved[3].replace("X", S.cap(S.NAMES["saṅkhārakkhandho"]))[:-2])


def check_reuse7():
    t = {1: "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_DIR.glob("*.md"))).lower(),
         2: "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI2_DIR.glob("*.md"))).lower()}
    missing = [f"(pi-{b}) {p} = {v}" for p, v, b in REUSE7 if v.lower() not in t[b]]
    assert not missing, missing


def render():
    blocks = []
    for lines, bid in S.pali_segments(S.PALI / NAME):
        vi = translate_segment(lines)
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_reuse7()
    check_frames()
    txt = render()
    assert "…." not in txt and "pe…" not in txt and "—" not in txt and "–" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{NAME}: {n} segments; {n_reuse + len(REUSE7)} pi-1/pi-2 strings asserted")
