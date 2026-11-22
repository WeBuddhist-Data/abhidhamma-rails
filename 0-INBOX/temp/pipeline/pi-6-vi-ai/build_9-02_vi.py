# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 9-02-dhammayamaka.md (Dhammayamaka part 2: the nirodhavāra and
the uppādanirodhavāra of the pavattivāra).

Everything comes from build_9-01_vi (the frame-setter of this yamaka: members, who9 answer heads, the B question /
answer parser, short answers, «?…Pe….»), which itself takes families A / B verbatim from build_2-01_vi, the moments
and persons from build_8_vi and the yo / so, NO, PE constants from build_7-01_vi.

Added here (listed in notes-9-02.md):
  - answer-head elements 9-01 did not meet: «pacchimacittassa bhaṅgakkhaṇe» (8 when(..., last=True)) and
    «kusalākusalānaṃ bhaṅgakkhaṇe» (pi-1 «các hiện tượng thiện và bất thiện»);
  - the plain (non-#) heading lines «(Ga) anulomapuggalokāsā» / «(Ca) paccanīkapuggalokāsā» that the Pāli prints
    as ordinary lines: rendered with the heading text, kept plain (8 ^6-8-82 rule).

Importing writes nothing; run  python -I -X utf8 -B build_9-02_vi.py  to build the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

D = importlib.import_module("build_9-01_vi")     # Dhammayamaka frame-setter
F = D.F                                          # build_2-01_vi (families A / B)
E = D.E                                          # build_2-02_vi
C8 = D.C8                                        # build_8_vi (moments, persons)

NAME = "9-02-dhammayamaka.md"
cap, low = S.cap, S.low

# ================================================================ answer-head elements new in 9-02
KUSALAKUSALA = "các hiện tượng thiện và bất thiện"      # kusalākusalānaṃ (pi-1 «quả của các hiện tượng thiện và bất thiện»)
NEW_ELEMENTS = [
    (r"pacchimacittassa (?P<m>uppāda|bhaṅga)kkhaṇe", "T", lambda m: C8.when(m["m"], last=True)),   # = 8 P_SUBJ
    (r"kusalākusalānaṃ (?P<m>uppāda|bhaṅga)kkhaṇe", "T", lambda m: D._at(m["m"], KUSALAKUSALA)),
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in NEW_ELEMENTS] + D.ELEMENTS


def who9(phrase):
    """= build_9-01_vi.who9 with the 9-02 elements added in front (same joining rules)."""
    p, i, out, prev_p = low(phrase), 0, [], False
    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            m = rx.match(p, i)
            if m:
                vi = fn(m)
                if kind == "P" and not prev_p:
                    vi = D.OI + vi
                out.append(vi)
                prev_p = kind == "P"
                i = m.end() + 1
                break
        else:
            raise ValueError(f"unparsed head {phrase!r} at {p[i:]!r}")
    return F.LIST_SEP.join(out)


def b_answer(s):
    """= build_9-01_vi.b_answer, using who9 above."""
    for rx, both in ((D.B_NOT9, False), (D.B_BOTH9, True)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if not both:
            assert m["r"] == m["r2"], s
        res = m["r"]
        head = D.where9(m["g"]) if res == "tattha" else who9(m["g"])
        f = F.b_both if both else F.b_not
        return f(res, head, D.member(m["x"]), D.vparse9(m["v1"]), D.member(m["y"]), D.vparse9(m["v2"]))
    return None


# ================================================================ plain heading lines
PLAIN_HEADINGS = {"(Ga) anulomapuggalokāsā", "(Ca) paccanīkapuggalokāsā"}   # printed without ##### in the Pāli


def translate_sentence(s, ctx=""):
    if s in D.EXACT:
        return D.EXACT[s]
    if s.endswith(D.PE_Q):
        return translate_sentence(s[:-len(D.PE_Q) + 1], ctx) + " " + D.A7.PE
    r = b_answer(s)
    if r:
        return r
    return D.translate_sentence(s, ctx)


def translate_line(line, ctx=""):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + D.heading(t) + sid
    if t in PLAIN_HEADINGS:
        return D.heading(t) + sid
    if t in D.EXACT:
        return D.EXACT[t] + sid
    return " ".join(translate_sentence(x, ctx) for x in F.split_sentences(t)) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for ln in src.splitlines():
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    (KUSALAKUSALA, 1), ("cuối cùng", 5), ("khoảnh khắc tan rã", 5),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (9-02): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in D.EXACT or p in PLAIN_HEADINGS:
            continue
        yield from F.split_sentences(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese within 9-02, and against 9-01 / 2-01 / 2-02 where shared."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for mod in (D, F, E):
        other = (S.PALI_DIR / mod.NAME).read_text(encoding="utf-8")
        for s in set(_sentences(other)) & set(seen):
            shared += 1
            if mod.translate_sentence(s, "") != seen[s]:
                print(f"DIFFERS FROM {mod.NAME}:", s)
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 9-01 / 2-01 / 2-02")
    return bad


def check_frames():
    assert who9("Pacchimacittassa bhaṅgakkhaṇe") == low(C8.P_SUBJ["Pacchimacittassa bhaṅgakkhaṇe"])
    assert who9("Sabbesaṃ cittassa uppādakkhaṇe kusalavippayuttacittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ "
                "asaññasattānaṃ") == D.who9("Sabbesaṃ cittassa uppādakkhaṇe kusalavippayuttacittassa bhaṅgakkhaṇe "
                                             "nirodhasamāpannānaṃ asaññasattānaṃ")
    assert D.heading("(Ga) anulomapuggalokāsā") == f"{S.LABEL['Ga']} {S.SECTION['anulomapuggalokāsā']}"
    assert D.vparse9("na nirujjhissanti") == (F.VERB_BASE["nirujjh"], "fut", True)


def main():
    S.check_cross_book()
    F.check_cross_book()
    D.check_cross_book()
    check_cross_book()
    check_frames()
    D.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for w in D.SLIPS:
        print("SLIP", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
