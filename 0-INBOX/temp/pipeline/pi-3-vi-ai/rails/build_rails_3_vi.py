"""Builder for the Vietnamese rails of pi-3 chapter 3 (Dutiyanayo, «Phương pháp thứ hai»), plain audience.

Writes AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/3-dutiyanayo.md only.
Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/3-dutiyanayo.md) with the locked termbase and
the approved formulas (rails/vi-rails-formulas.md, ch3 frame). All shared strings come from build_rails_sample_vi
(imported read-only); the ch3 frame is asserted against the formulas file, and every pi-1 / pi-2 name it uses
is asserted to still occur in those rails (S.check_reuse plus a per-name tag check).

usage: python -I -X utf8 build_rails_3_vi.py
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "3-dutiyanayo.md"
FORMULAS = S.RAILS / "vi-rails-formulas.md"

# ------------------------------------------------------------------ fixed strings (ch3)
ITEMS_OF = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                      # X-ena / X-ehi
BY_K = "theo cách gộp vào khối"                        # khandhasaṅgahena
BY_A = "theo cách gộp vào lĩnh vực nhận biết"           # āyatanasaṅgahena
BY_D = "theo cách gộp vào yếu tố"                       # dhātusaṅgahena
THOSE = "những hiện tượng ấy"                          # te dhammā
Q_OUT_FULL = (f"{S.OUT_} {S.HOW_MANY} {S.KHANDHA}, {S.HOW_MANY} {S.AYATANA} và {S.HOW_MANY} {S.DHATU}?")

used_names = []


def name_of(instr):
    """Instrumental Pāli X -> (Vietnamese name, pronoun)."""
    x = instr[0].lower() + instr[1:]
    if x.endswith(" dhammehi"):
        key = x[: -len(" dhammehi")]
        assert key.endswith("ehi"), x
        key = key[:-3] + "ā"
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR[key]}"
        used_names.append(v)
        return v, "chúng"
    if x == "upādādhammehi":
        v = f"{S.DHAMMA_N} {S.DHAMMA_ATTR['upādā']}"
        used_names.append(v)
        return v, "chúng"
    for a, b in (("āyatanena", "āyatanaṃ"), ("dhātuyā", "dhātu"), ("ndriyena", "ndriyaṃ"),
                 ("bhavena", "bhavo"), ("devena", "devo")):
        if x.endswith(a):
            v = S.NAMES[x[: -len(a)] + b]
            used_names.append(v)
            return v, "nó"
    raise KeyError(instr)


def head(subjects):
    """«Những hiện tượng nào cùng với A… những hiện tượng nào được gộp vào cùng với Z theo cách gộp vào khối,
    nhưng không được gộp vào cùng với nó theo cách gộp vào lĩnh vực nhận biết và theo cách gộp vào yếu tố»."""
    names = [name_of(s) for s in subjects]
    parts = [f"{ITEMS_OF} {WITH} {v}…" for v, _ in names[:-1]]
    last, pron = names[-1]
    parts.append(f"{ITEMS_OF} {S.IN} {WITH} {last} {BY_K}, {S.BUT} {S.OUT_} {WITH} {pron} {BY_A} và {BY_D}")
    return S.cap(" ".join(parts))


TAIL_P = (" khandhasaṅgahena saṅgahitā āyatanasaṅgahena asaṅgahitā dhātusaṅgahena asaṅgahitā")
Q_P = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi asaṅgahitā? Te dhammā "
AB_P = "…pe… te dhammā "
LINE = re.compile(r"^(?P<subj>.+?)" + re.escape(TAIL_P) + r"(?P<mid>" + re.escape(Q_P) + "|" + re.escape(AB_P)
                  + r")(?P<cnt>.+) asaṅgahitā\.$")


def content_line(p):
    m = LINE.match(p)
    assert m, p
    subjects = [s.strip() for s in m.group("subj").split("…") if s.strip()]
    for s in subjects:
        assert s.endswith(" ye dhammā"), s
    subjects = [s[: -len(" ye dhammā")] for s in subjects]
    nums = S.parse_counts(m.group("cnt"))
    assert all(nums), nums
    ans = f"{THOSE} {S.OUT_} {S.counts_vi(list(zip(S.CATS, nums)))}."
    h = head(subjects)
    if m.group("mid") == Q_P:
        return f"{h}, {S.THEN} {THOSE} {Q_OUT_FULL} {S.cap(ans)}"
    return f"{h}…, {ans}"


# ------------------------------------------------------------------ summary verse of ^3-178
VERSE = {
    "Dasāyatanā sattarasa dhātuyo,": "Mười lĩnh vực nhận biết, mười bảy yếu tố,",
    "Sattindriyā asaññābhavo ekavokārabhavo;":
        f"Bảy năng lực, {S.NAMES['asaññābhavo']}, {S.NAMES['ekavokārabhavo']};",
    "Paridevo sanidassanasappaṭighaṃ,": f"{S.cap(S.NAMES['paridevo'])}, điều {S.DHAMMA_ATTR['sanidassanasappaṭighā']},",
    "Anidassanaṃ punadeva [punareva (pī.)] sappaṭighaṃ upādāti.":
        f"Điều {S.DHAMMA_ATTR['anidassanā']}, rồi lại {S.spell('Pī.', 'punareva')} "
        f"điều {S.DHAMMA_ATTR['sappaṭighā']}, điều {S.DHAMMA_ATTR['upādā']}.",
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


def check_frame():
    """The full ch3 sentence must equal the approved formula with X / nó / N filled in."""
    txt = FORMULAS.read_text(encoding="utf-8")
    line = next(ln for ln in txt.splitlines() if "(ch3) = " in ln)
    vi = line.split("(ch3) = ", 1)[1].replace(" (proposed for ch3-15)", "")
    built = content_line("Cakkhāyatanena ye dhammā" + TAIL_P + Q_P
                         + "catūhi khandhehi dvīhāyatanehi aṭṭhahi dhātūhi asaṅgahitā.")
    exp = (vi.replace("cùng với X", f"cùng với {S.NAMES['cakkhāyatanaṃ']}")
             .replace("N khối, N lĩnh vực nhận biết và N yếu tố",
                      S.counts_vi([(S.KHANDHA, 4), (S.AYATANA, 2), (S.DHATU, 8)])))
    assert built == exp, f"\n{built}\n{exp}"
    # abridged form «…, những hiện tượng ấy (không) được gộp vào N khối, …»
    ab = next(ln for ln in txt.splitlines() if ln.startswith("…pe… te dhammā N"))
    assert "…, những hiện tượng ấy (không) được gộp vào N khối, …" in ab


def check_used_reuse():
    missing = [v for v in used_names if not S.reuse_tag(v)]
    assert not missing, f"names without pi-1 / pi-2 tag: {missing}"


def render():
    segs = S.pali_segments(S.PALI / NAME)
    blocks = []
    for lines, bid in segs:
        vi = translate_segment(lines)
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_frame()
    txt = render()
    check_used_reuse()
    n = S.check_against_pali(txt, S.PALI / NAME)
    assert "…." not in txt and "pe…" not in txt
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{NAME}: {n} segments; {len(set(used_names))} names checked; {n_reuse} pi-1/pi-2 strings asserted")
