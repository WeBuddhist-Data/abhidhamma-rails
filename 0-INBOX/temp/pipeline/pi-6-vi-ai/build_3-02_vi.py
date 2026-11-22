# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 3-02-ayatanayamaka.md (Āyatanayamaka, pavattivāra continued:
(3) anāgatavāra and (4) paccuppannātītavāra).

Frames: build_3-01_vi (members, «…pe…» shortenings, attribute beings, notes), build_2-01_vi (families A / B) and
build_2-02_vi (who2: «… ye ca <P>ṃ upapajjitvā parinibbāyissanti»), all imported and used verbatim. New here (see
notes-3-02.md): the «…pe…» runs inside one question in every position (RUN_Q_RE), attribute beings together with a
plane («acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ»), «Ye <P1>ṃ <P2>ṃ upapajjitvā parinibbāyissanti», and the
editorial note «(tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti)».

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    A32 = importlib.import_module("build_3-02_vi")
    A32.who32(phrase) / A32.run_q(line, ctx) / A32.translate_line(line, ctx)

Importing writes nothing; run  python -I -X utf8 -B build_3-02_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")      # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")      # who2 (frame-setter of the «ye ca …» groups)
A3 = importlib.import_module("build_3-01_vi")     # Āyatana members, «…pe…», attribute beings (frame-setter)

NAME = "3-02-ayatanayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []

# ================================================================ beings (family B additions)
ATTR_PLANE_GROUP = "{h} {p} {prep} {planes} mà {a}"
# acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ = những người đang tái sinh vào cõi dục lạc mà không có mắt (new; 3-01
# ATTR_GROUP «những người đang tái sinh không có mắt» when no plane is named)


def _strip_head(g):
    head0 = F.WHO_HEAD.format(g="")
    assert g.startswith(head0), g
    return g[len(head0):]


def _ye_planes(phrase):
    """Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti -> 2-01 YE_UPAPAJJITVA with a plane list
    (2-01 LIST_SEP, as «<P1>ṃ <P2>ṃ upapajjantānaṃ»)."""
    mm = re.fullmatch(r"[Yy]e (?P<ps>\S+(?: \S+)+) upapajjitvā parinibbāyissanti", phrase)
    if not mm:
        return None
    ps = []
    for x in mm["ps"].split():
        case, stem = F._plane_case(low(x))
        assert case == "acc", phrase
        ps.append(F.PLANE[stem])
    return F.YE_UPAPAJJITVA.format(p=F.LIST_SEP.join(ps))


def who32(phrase):
    """Beings phrase -> Vietnamese head. 3-01 who3 / 2-02 who2 / 2-01 who where they apply (byte-identical);
    new: attribute groups with a plane, and a plane list after «Ye»."""
    r = _ye_planes(phrase)
    if r:
        return r
    w = [low(x) for x in phrase.split()]
    if not any(x in A3.ATTR for x in w):
        return E.who2(phrase)
    groups, other, i, n = [], [], 0, len(w)

    def flush():
        if other:
            groups.append(_strip_head(F.who(" ".join(other))))
            other.clear()

    while i < n:
        k, mod = i, None
        if w[k] in ("sabbesaṃ", "itaresaṃ") and k + 1 < n and w[k + 1] in A3.ATTR:
            mod, k = w[k], k + 1
        if w[k] not in A3.ATTR:
            other.append(w[i]); i += 1
            continue
        flush()
        attrs = []
        while k < n and w[k] in A3.ATTR:
            attrs.append(A3.ATTR[w[k]]); k += 1
        planes, pcase = [], None
        while k < n:
            case, stem = F._plane_case(w[k])
            if case in ("acc", "abl", "loc") and pcase in (None, case):
                planes.append(F.PLANE[stem]); pcase = case; k += 1
            else:
                break
        assert k < n and w[k] in F.PARTICIPLE, phrase
        vi, prep, need = F.PARTICIPLE[w[k]]
        assert pcase in (None, need), phrase
        a = A3.ATTR_JOIN.join(attrs)
        if planes:
            groups.append(ATTR_PLANE_GROUP.format(h=F.HEAD[mod], p=vi, prep=prep, planes=F.LIST_SEP.join(planes), a=a))
        else:
            groups.append(A3.ATTR_GROUP.format(h=F.HEAD[mod], p=vi, a=a))
        i = k + 1
    flush()
    out = F.WHO_HEAD.format(g=F.LIST_SEP.join(groups))
    try:
        old = A3.who3(phrase)
    except (AssertionError, ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, (phrase, old, out)           # where 3-01 covers the phrase, say exactly what 3-01 says
    return out


# ================================================================ sentences
V = r"(?:na )?\S+"
RES = r"(?P<res>tesaṃ tattha|tesaṃ|tattha)"
B_NOT_RE = re.compile(r"(?P<g>.+?) " + RES + r" (?P<x>\S+āyatanaṃ) (?P<v1>" + V + r"), no ca (?P<res2>tesaṃ tattha|"
                      r"tesaṃ|tattha) (?P<y>\S+āyatanaṃ) (?P<v2>" + V + ")")
B_BOTH_RE = re.compile(r"(?P<g>.+?) " + RES + r" (?P<x>\S+āyatana)ñca (?P<v1>" + V + r") (?P<y>\S+āyatana)ñca "
                       r"(?P<v2>" + V + ")")

# source slips rendered as meant (each must apply exactly once)
SLIP_FIX = [
    ("tesaṃ tattha rūpāyatanañca ca uppajjittha cakkhāyatanañca uppajjati.",
     "tesaṃ tattha rūpāyatanañca uppajjittha cakkhāyatanañca uppajjati.",
     "^6-3-75: «rūpāyatanañca ca uppajjittha»: «ca» written twice; rendered once (both-frame)"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, why in SLIP_FIX:
        if a in s:
            s = s.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return s


def tr_sentence(s, ctx):
    """One Pāli sentence (with its final punctuation). The beings answers use who32(); everything else is the
    3-01 sentence translator."""
    body, punct = (s[:-1], s[-1]) if s and s[-1] in ".?" else (s, "")
    for rx, both in ((B_NOT_RE, False), (B_BOTH_RE, True)):
        mm = rx.fullmatch(body)
        if mm and punct == ".":
            res = mm["res"]
            if not both:
                assert res == mm["res2"], body
            head = A3.where3(mm["g"]) if res == "tattha" else who32(mm["g"])
            x = A3.m(mm["x"] + ("ṃ" if both else ""))
            y = A3.m(mm["y"] + ("ṃ" if both else ""))
            f = F.b_both if both else F.b_not
            return f(res, head, x, F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx))
    return A3.tr(body, punct, ctx)


def tr_sentences(text, ctx):
    return " ".join(tr_sentence(x.strip(), ctx) for x in F.split_sentences(text) if x.strip())


# «…pe…» runs inside one question, on either side (3-01 PAST_RUN_RE generalised; 3-01 _run for the runs)
RUN = r"\S+āyatanaṃ(?:(?:…pe…|…) \S+āyatanaṃ)*"
RUN_Q_RE = re.compile(r"(?P<w1>Yassa vā pana yattha|Yassa yattha|Yassa vā pana|Yassa) (?P<xs>" + RUN + r") (?P<v1>"
                      + V + r") (?P<w2>tassa tattha|tassa) (?P<ys>" + RUN + r") (?P<v2>" + V + r")\?(?P<rest>.*)")


def run_q(t, ctx):
    mm = RUN_Q_RE.fullmatch(t)
    if not mm or "…" not in mm["xs"] + mm["ys"]:
        return None
    kind = mm["w1"].replace(" vā pana", "").lower()
    assert F.DEM_OF[kind] == mm["w2"], t
    q = F.b_q(kind, A3._run(mm["xs"]), F.vparse(mm["v1"], ctx), A3._run(mm["ys"]), F.vparse(mm["v2"], ctx),
              kha="vā pana" in mm["w1"], label=None)
    rest = mm["rest"].strip()
    return q + (" " + tr_sentences(rest, ctx) if rest else "")


# editorial note of ^6-3-52
NOTE_SADISA = ("(thì {dem} {a} và {b} giống nhau, hai điều này thật sự giống nhau)")
# (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti) (new; sadisaṃ «giống nhau» as 3-01
# «ekasadisaṃ … đều giống nhau»; ime dve «hai điều này», sadisā eva «thật sự giống nhau»)
NOTE_RE = re.compile(r"Yassa (?P<x>\S+āyatanaṃ) (?P<v>\S+) \(tassa (?P<a>\S+āyatana)ñca (?P<b>\S+āyatana)ñca sadisaṃ, "
                     r"ime dve sadisāyeva honti\)\.")


def note_sadisa(t, ctx):
    mm = NOTE_RE.fullmatch(t)
    if not mm:
        return None
    head = cap(A3.b_head("yassa", A3.m(mm["x"]), F.vparse(mm["v"], ctx)))
    note = NOTE_SADISA.format(dem=F.DEM_VI["tassa"], a=A3.m(mm["a"] + "ṃ"), b=A3.m(mm["b"] + "ṃ"))
    return f"{head} {note}."


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + A3.heading(t) + sid
    t = fix_slips(t)
    for f in (note_sadisa, run_q):
        r = f(t, ctx)
        if r:
            return r + sid
    if "…" in t:
        return A3.tr_pe(t, ctx) + sid
    return tr_sentences(t, ctx) + sid


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
CROSS_BOOK = [("giống nhau", 5), ("thật sự", 2), ("cõi dục lạc", 1), ("tái sinh", 2)]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s} (found in: {[k for k, v in texts.items() if s in v]})")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (3-02): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#") or "…" in p or "sadisa" in p:
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        yield from (x.strip() for x in F.split_sentences(p) if x.strip())


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 3-02 and against 3-01 / 2-01 output files."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = tr_sentence(fix_slips(s), "")
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for other in ("3-01-ayatanayamaka.md",):
        po = (S.PALI_DIR / other).read_text(encoding="utf-8").splitlines()
        vo = (S.OUT_DIR / other).read_text(encoding="utf-8").splitlines()
        assert len(po) == len(vo)
        for pl, vl in zip(po, vo):
            pl2 = re.sub(r"\s*\^[\w-]+$", "", pl)
            vl2 = re.sub(r"\s*\^[\w-]+$", "", vl)
            if not pl2.strip() or pl.startswith("#") or "…" in pl or "sadisa" in pl2 or "ṭhapetvā" in pl2:
                continue
            ps = [x.strip() for x in F.split_sentences(pl2) if x.strip()]
            if any(x in seen for x in ps):
                try:
                    mine = " ".join(seen.get(x) or tr_sentence(x, "") for x in ps)
                except ValueError:          # a 3-01 line with a slip its own builder repairs: compare by sentence
                    for x in ps:
                        if x in seen and A3.tr_sentences(x, "") != seen[x]:
                            print("DIFFERS FROM 3-01:", x[:80])
                            bad += 1
                    continue
                shared += 1
                if mine != vl2:
                    print("DIFFERS FROM 3-01:", pl2[:80])
                    bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} lines shared with 3-01 checked")
    return bad


def main():
    S.check_cross_book()
    F.check_cross_book()
    A3.check_cross_book()
    check_cross_book()
    SLIPS.clear(); F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    chapter_slips = list(F.SLIPS)                    # check_repeats below also parses 3-01 lines
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + A3.check_extra(text)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in used:
        print("SLIP", why)
    seen = set()
    for c, w in chapter_slips + [("", x) for x in SLIPS]:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
