"""Builder for the Vietnamese rails translation of pi-3 chapter 5 (Catutthanayo, «Phương pháp thứ tư»),
plain audience.

Writes AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/5-catutthanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/5-catutthanayo.md) with the locked termbase
AI_translation/vietnamese/pi-3-pali-vietnamese-termbase-plain.md (+ pi-3-vi-ai/termbase/APPROVED.md). Every string
comes from the approved sample builder (imported read-only as S) or from the fixed constants below, so identical
Pāli gives byte-identical Vietnamese. New strings are listed in notes-rails-5.md.

usage: python -I -X utf8 build_rails_5_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (read-only import; writes nothing)

NAME = "5-catutthanayo.md"

# ================================================================== frame (approved, ch5)
WHICH = "những hiện tượng nào"                       # ye dhammā
WITH = "cùng với"                                    # X-ena (instrumental of association)
THOSE = "các hiện tượng đó"                          # tehi dhammehi
TE = "những hiện tượng ấy"                           # te dhammā
BY3 = (f"theo cách gộp vào {S.KHANDHA}, theo cách gộp vào {S.AYATANA} "
       f"và theo cách gộp vào {S.DHATU}")            # khandhasaṅgahena saṅgahitā āyatana… dhātu… saṅgahitā
APPROVED_CH5 = ("Những hiện tượng nào được gộp vào cùng với X theo cách gộp vào khối, theo cách gộp vào lĩnh vực "
                "nhận biết và theo cách gộp vào yếu tố; những hiện tượng nào được gộp vào cùng với các hiện tượng "
                "đó theo cách gộp vào khối, theo cách gộp vào lĩnh vực nhận biết và theo cách gộp vào yếu tố, thì "
                "những hiện tượng ấy được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết và bao nhiêu yếu tố?")


def frame5(x_vi):
    return (f"{WHICH} {S.IN} {WITH} {x_vi} {BY3}; {WHICH} {S.IN} {WITH} {THOSE} {BY3}, "
            f"thì {TE} {S.Q_IN}")


assert S.cap(frame5("X")) == APPROVED_CH5, "ch5 frame differs from the approved formula"

P_FRAME = ("khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā, tehi dhammehi ye "
           "dhammā khandhasaṅgahena saṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā, te dhammā "
           "katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? Te dhammā ")
P_ANSWER = re.compile(r"^(?P<c>.+) saṅgahitā\.$")

# ================================================================== X in the instrumental -> subject names (S)
N, D = S.NAMES, S.DHAMMA_ATTR


def dh(attr):
    return f"{S.DHAMMA_N} {D[attr]}"


INSTR = {
    # truths
    "samudayasaccena": N["samudayasaccaṃ"], "maggasaccena": N["maggasaccaṃ"],
    # faculties
    "itthindriyena": N["itthindriyaṃ"], "purisindriyena": N["purisindriyaṃ"],
    "sukhindriyena": N["sukhindriyaṃ"], "dukkhindriyena": N["dukkhindriyaṃ"],
    "somanassindriyena": N["somanassindriyaṃ"], "domanassindriyena": N["domanassindriyaṃ"],
    "upekkhindriyena": N["upekkhindriyaṃ"], "saddhindriyena": N["saddhindriyaṃ"],
    "vīriyindriyena": N["vīriyindriyaṃ"], "satindriyena": N["satindriyaṃ"],
    "samādhindriyena": N["samādhindriyaṃ"], "paññindriyena": N["paññindriyaṃ"],
    "anaññātaññassāmītindriyena": N["anaññātaññassāmītindriyaṃ"], "aññindriyena": N["aññindriyaṃ"],
    "aññātāvindriyena": N["aññātāvindriyaṃ"],
    # dependent origination and the grief series
    "avijjāya": N["avijjā"],
    "avijjāpaccayā saṅkhārena": N["avijjāpaccayā saṅkhārā"],     # singular instrumental; name kept unchanged
    "saḷāyatanapaccayā phassena": N["saḷāyatanapaccayā phasso"],
    "vedanāpaccayā taṇhāya": N["vedanāpaccayā taṇhā"],
    "taṇhāpaccayā upādānena": N["taṇhāpaccayā upādānaṃ"],
    "kammabhavena": "sự hiện hữu dưới dạng nghiệp",                # (pi-2), without the ch2 variant bracket
    "sokena": N["soko"], "paridevena": N["paridevo"], "dukkhena": N["dukkhaṃ"],
    "domanassena": N["domanassaṃ"], "upāyāsena": N["upāyāso"],
    # inner-matrix topics
    "satipaṭṭhānena": N["satipaṭṭhānaṃ"], "sammappadhānena": N["sammappadhānaṃ"],
    "appamaññāya": N["appamaññā"], "pañcahi indriyehi": N["pañcindriyāni"],
    "pañcahi balehi": N["pañca balāni"], "sattahi bojjhaṅgehi": N["satta bojjhaṅgā"],
    "ariyena aṭṭhaṅgikena maggena": N["ariyo aṭṭhaṅgiko maggo"],
    "phassena": N["phasso"], "cetanāya": N["cetanā"], "adhimokkhena": N["adhimokkho"],
    "manasikārena": N["manasikāro"],
    # matrix dyads (X dhammehi = «các hiện tượng X»)
    "hetūhi dhammehi": dh("hetū"), "hetūhi ceva sahetukehi ca dhammehi": dh("hetū ceva sahetukā ca"),
    "hetūhi ceva hetusampayuttehi ca dhammehi": dh("hetū ceva hetusampayuttā ca"),
    "kilesehi dhammehi": dh("kilesā"),
    "kilesehi ceva saṃkilesikehi ca dhammehi": dh("kilesā ceva saṃkilesikā ca"),
    "kilesehi ceva saṃkiliṭṭhehi ca dhammehi": dh("kilesā ceva saṃkiliṭṭhā ca"),
    "kilesehi ceva kilesasampayuttehi ca dhammehi": dh("kilesā ceva kilesasampayuttā ca"),
}
# bare instrumental nouns with neither «dhammehi» nor «ye dhammā» (translated as written); the first five are
# identical to build_rails_4_vi.py BARE (ch4 ^3-187), the last three are built on the same pattern
BARE = {"saṃyojanehi": "các xiềng xích", "ganthehi": "các nút thắt", "oghehi": "các dòng lũ",
        "yogehi": "các ách", "nīvaraṇehi": "các chướng ngại",
        "āsavehi": "các ô nhiễm", "parāmāsehi": "các sự hiểu sai lệch", "upādānehi": "các sự bám víu"}
YE = " ye dhammā"


def item_vi(p, full=False):
    """'Xena ye dhammā' -> «những hiện tượng nào cùng với X»; bare 'Xehi' -> «cùng với X».
    full=True: the item that carries the frame («… được gộp vào cùng với X …»)."""
    p = p.strip()
    if p.endswith(YE):
        x = p[: -len(YE)]
        x_vi = INSTR[x[0].lower() + x[1:]]
        return frame5(x_vi) if full else f"{WHICH} {WITH} {x_vi}"
    assert not full, p
    return f"{WITH} {BARE[p[0].lower() + p[1:]]}"


def run_vi(p, last_full=False):
    """A run of items separated by «…»; a final «…» / «….» / «… .» stays as «…» (never «….»)."""
    p = p.strip()
    trailing = bool(re.search(r"…\s*\.?$", p))
    p = re.sub(r"…\s*\.?$", "", p)
    items = [x for x in (s.strip() for s in p.split("…")) if x]
    vi = [item_vi(x, full=(last_full and i == len(items) - 1)) for i, x in enumerate(items)]
    return S.cap("… ".join(vi) + ("…" if trailing else ""))


def frame_line(p):
    head, tail = p.split(P_FRAME)
    m = P_ANSWER.match(tail)
    assert m, tail
    nums = S.parse_counts(m.group("c"))
    return f"{run_vi(head, last_full=True)} {S.cap(TE)} {S.answer_in(nums)}."


# ================================================================== summary verse (uddāna) of ^3-192
PADA = "đề mục"                                     # pada (as in «Giải thích đề mục về …»)
UDDANA = {
    "Dve saccā pannarasindriyā, ekādasa paṭiccapadā;":
        f"Hai sự thật, mười lăm năng lực, mười một {PADA} về sự sinh khởi tùy thuộc vào điều kiện;",
    "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti [tiṃsavidhanti (pī.)].":
        f"Tiếp theo rồi lại có mười một, ở đây {PADA} thuộc các nhóm gồm ba mươi loại "
        + S.spell("Pī.", "tiṃsavidhanti") + ".",
}
REUSE5 = [("Dve saccā", "Hai sự thật", 2)]          # pi-2 Dhammahadayavibhaṅga
# puna: no termbase entry; closest sibling punareva «rồi lại» (as ch3 punadeva)


def translate_line(ln):
    if ln.startswith("#"):
        return S.heading_vi(ln)
    if ln in S.CLOSINGS:
        return S.CLOSINGS[ln]
    if ln in UDDANA:
        return UDDANA[ln]
    if P_FRAME in ln:
        return frame_line(ln)
    return run_vi(ln)


def render():
    blocks = []
    for lines, bid in S.pali_segments(S.PALI / NAME):
        vi = [translate_line(ln) for ln in lines]
        assert len(vi) == len(lines), bid
        vi[-1] = f"{vi[-1]} ^{bid}"
        blocks.append("\n".join(vi))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


def check_reuse5():
    t2 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI2_DIR.glob("*.md"))).lower()
    missing = [f"(pi-{b}) {p} = {v}" for p, v, b in REUSE5 if v.lower() not in t2]
    assert not missing, missing


if __name__ == "__main__":
    n_reuse = S.check_reuse()
    check_reuse5()
    txt = render()
    assert "…." not in txt and "—" not in txt and "–" not in txt
    n = S.check_against_pali(txt, S.PALI / NAME)
    (S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
    print(f"{NAME}: {n} segments; {n_reuse + len(REUSE5)} pi-1/pi-2 strings asserted")
