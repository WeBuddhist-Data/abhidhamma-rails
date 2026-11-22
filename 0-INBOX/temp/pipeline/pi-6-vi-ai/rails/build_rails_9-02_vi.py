"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 9-02 (Dhammayamaka 2: pavattivāra nirodhavāra + the start of the
uppādanirodhavāra).

Everything comes from the Dhammayamaka module build_rails_9-01_vi (members, verbs, questions, answer heads,
answer frames, headings) and, through it, 2-01 (families A, B), 7-01 (answer shapes) and 8 (moments, kinds of mind).
All are imported READ-ONLY. This file adds only what 9-01's parsers do not know:
  NEW_GEN / gen_vi()      genitives before a moment that 9-01 does not have: Pacchimacittassa «tâm cuối cùng»
                          (8's mind_gen_vi), kusalākusalānaṃ «các hiện tượng thiện và bất thiện» (termbase; pi-1)
  head_parts() / answer_head()  9-01's head parser, with the new moment parts cut out and placed in order
  b_sentence() / sentence() / sentences() / tr_line() / build()  9-01's line translator with these heads
  FIXED                   the headings run into a segment as a line: "(Ca) paccanīkapuggalokāsā",
                          "(Ga) anulomapuggalokāsā" (= 2-01's heading wording)
A line the parsers cannot place raises ValueError: there is no silent fallback.

Import READ-ONLY (importing writes nothing):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; DY2 = importlib.import_module("build_rails_9-02_vi")

usage: python -I -X utf8 -B build_rails_9-02_vi.py [--probe]
"""
import importlib
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
DY = importlib.import_module("build_rails_9-01_vi")   # Dhammayamaka module (READ-ONLY)
B, C, D = DY.B, DY.C, DY.D                              # 2-01, 7-01, 8 (READ-ONLY, the same module objects)

CHAPTER = "9-02-dhammayamaka.md"
N = "9-02"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
cap = S.cap
PE = S.PE


# ===============================================================================================================
# 1. Genitives before a moment that 9-01 does not know
# ===============================================================================================================
NEW_GEN = {
    # kusalākusalānaṃ (bhaṅgakkhaṇe): termbase «hiện tượng thiện và bất thiện»; pi-1 ^1-994 «… của các hiện tượng
    # thiện và bất thiện»; «các» as 9-01 DHAMMA_GEN «các hiện tượng thiện»
    "kusalākusalānaṃ": f"các {S.SUBJ['kusala']} {C.AND} {S.KIND['akusala']}",
}


def gen_vi(word):
    """Genitive before a moment → Vietnamese. 9-01's gen_vi first; then Pacchima…cittassa (8's mind_gen_vi:
    «tâm cuối cùng») and NEW_GEN. Unknown → None."""
    try:
        g = DY.gen_vi(word)
    except ValueError:
        g = None
    if g is not None:
        return g
    w = DY.lc(word)
    if w in NEW_GEN:
        return NEW_GEN[w]
    if w.endswith("cittassa") and "pacchima" in w:
        return D.mind_gen_vi(word)
    return None


def _new_moment(toks, i):
    """Token i is a genitive that only this file knows, followed by a moment word."""
    if i + 1 >= len(toks) or DY.lc(toks[i + 1]) not in D.MOMENT:
        return False
    try:
        if DY.gen_vi(toks[i]) is not None:
            return False
    except ValueError:
        pass
    return gen_vi(toks[i]) is not None


def head_parts(head):
    """9-01's head_parts, with the new moment parts (NEW_GEN / pacchima- + moment) cut out and kept in place.
    A moment closes a person run in 9-01 as well, so cutting there changes nothing else."""
    toks = head.split()
    parts, chunk, i = [], [], 0
    while i < len(toks):
        if _new_moment(toks, i):
            if chunk:
                parts += DY.head_parts(" ".join(chunk))
                chunk = []
            parts.append(DY.moment_vi(toks[i + 1], gen_vi(toks[i])))
            i += 2
            continue
        chunk.append(toks[i])
        i += 1
    if chunk:
        parts += DY.head_parts(" ".join(chunk))
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def answer_head(head, loc):
    if loc == "tattha":
        return B.place_head(head)                             # «Ở cõi X, ở cõi Y» (2-01 / 7-01)
    return cap(", ".join(head_parts(head)))


# ===============================================================================================================
# 2. Answer sentences (9-01's b_sentence regexes with these heads; family A / short answers from 9-01 / 2-01)
# ===============================================================================================================
LOC_RE = DY.LOC_RE


def b_sentence(s):
    if m := re.fullmatch(r"(.+?) " + LOC_RE + r" (.+?), no ca \2 (.+?)\.", s):
        head, loc, c1, c2 = m.groups()
        a, v1 = DY.split_mv(c1)
        b, v2 = DY.split_mv(c2)
        return B.b_noca(answer_head(head, loc), loc, a, v1, b, v2)
    if m := re.fullmatch(r"(.+?) " + LOC_RE + r" (\S+) ca dhammā ((?:na )?\S+) (\S+) ca dhammā ((?:na )?\S+)\.", s):
        head, loc, k1, w1, k2, w2 = m.groups()
        return B.b_both(answer_head(head, loc), loc, DY.DHAMMA.subj(f"{k1} dhammā"), DY.verb(w1),
                        DY.DHAMMA.subj(f"{k2} dhammā"), DY.verb(w2))
    return None


def sentence(s):
    if s in B.SHORT:                                          # Āmantā. / No. / Natthi. / Nirujjhanti. …
        return B.SHORT[s]
    if s in DY.SECTION_END:                                   # Nirodhavāro. …
        return DY.SECTION_END[s]
    out = b_sentence(s)
    if out is not None:
        return out
    out = DY.a_sentence(s)
    if out is not None:
        return out
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest):
    parts = [x for x in re.split(r"(?<=\.) ", rest.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ===============================================================================================================
# 3. Fixed lines and the line translator (= 9-01 tr_line with the functions above)
# ===============================================================================================================
FIXED = dict(DY.FIXED) | {   # headings run into a segment as its last line (^6-9-120, ^6-9-135): 2-01 heading wording
    "(Ca) paccanīkapuggalokāsā": DY.heading("(Ca) paccanīkapuggalokāsā"),
    "(Ga) anulomapuggalokāsā": DY.heading("(Ga) anulomapuggalokāsā"),
}


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if "[" in body:
        raise ValueError(f"variant bracket not handled: {p!r}")
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {DY.heading(text)}"
    elif body in FIXED:
        out = FIXED[body]
    elif (q := DY.pq_question(body)) or (q := DY.name_question(body)):
        out, rest = q
        if rest.strip() == DY.CUT_AFTER_Q:
            out += PE
        elif rest.strip():
            out += " " + sentences(rest)
    else:
        out = sentences(body)
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    return [[tr_line(ln) for ln in seg] for seg in S.segments_of(name)]


def probe(name=CHAPTER):
    bad = 0
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                tr_line(ln)
            except ValueError as e:
                bad += 1
                print("FAIL:", e, "\n   ", ln[:160])
    print("failing lines:", bad)


# ===============================================================================================================
# 4. Reuse assertions and shared strings
# ===============================================================================================================
REUSED = [
    ("kusalākusalānaṃ dhammānaṃ vipākā (pi-1 ^1-994)", "của các hiện tượng thiện và bất thiện", "1"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_shared():
    """Strings that must equal the setters' byte for byte."""
    assert gen_vi("Pacchimacittassa") == D.mind_gen_vi("Pacchimacittassa") == f"{D.MIND} {D.FINAL}"
    assert NEW_GEN["kusalākusalānaṃ"].startswith(DY.DHAMMA_GEN["kusalānaṃ"] + " ")
    assert FIXED["(Ca) paccanīkapuggalokāsā"] == B.heading("(Ca) paccanīkapuggalokāsā", DY.X_PL, DY.YAMAKA)
    # this file's translator = 9-01's on 9-01's own heads
    for hd in ("Sabbesaṃ cittassa bhaṅgakkhaṇe kusalavippayuttaakusalavippayuttacittassa uppādakkhaṇe "
               "nirodhasamāpannānaṃ asaññasattānaṃ", "Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā "
               "aggamaggaṃ paṭilabhissanti tassa cittassa bhaṅgakkhaṇe asaññasattānaṃ", "Itaresaṃ",
               "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ"):
        assert answer_head(hd, "tesaṃ") == DY.answer_head(hd, "tesaṃ"), hd
    s = "Arūpe kusalānaṃ uppādakkhaṇe tesaṃ kusalā dhammā uppajjanti, no ca tesaṃ abyākatā dhammā uppajjanti."
    assert sentence(s) == DY.sentence(s)
    # the 9-01 chapter re-translates identically with this file's translator (identical Pāli = identical Vietnamese)
    vi01 = (S.OUT_DIR / DY.CHAPTER).read_text(encoding="utf-8")
    assert "\n\n".join("\n".join(tr_line(x) for x in seg) for seg in S.segments_of(DY.CHAPTER)) + "\n" == vi01


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Dhammayamaka 2): nirodhavāra and the start of the uppādanirodhavāra", "",
           "Builder: build_rails_9-02_vi.py. Imports build_rails_9-01_vi READ-ONLY (and through it 2-01, 7-01, 8): "
           "members, verbs, questions, answer frames, headings and short answers are 9-01's strings byte for byte. "
           "New here: `NEW_GEN`, `gen_vi` (adds Pacchima…cittassa and kusalākusalānaṃ before a moment), `head_parts` / "
           "`answer_head` (9-01's parser with those parts cut in), `FIXED` (headings run into a segment as a line), "
           "`b_sentence`, `sentence`, `tr_line`, `build`. The builder asserts that its translator reproduces the 9-01 "
           "chapter byte for byte. Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("New strings set here")
    row("Pacchimacittassa bhaṅgakkhaṇe", DY.moment_vi("bhaṅgakkhaṇe", gen_vi("Pacchimacittassa")))
    row("kusalākusalānaṃ bhaṅgakkhaṇe", DY.moment_vi("bhaṅgakkhaṇe", gen_vi("kusalākusalānaṃ")))
    for p in ("(Ca) paccanīkapuggalokāsā", "(Ga) anulomapuggalokāsā"):
        row(p + " (line)", FIXED[p])
    h("Headings, closings, short answers met here (9-01 / 2-01 strings)")
    for p in ("(1) Paccuppannavāro", "(5) Paccuppannānāgatavāro", "(6) Atītānāgatavāro", "Uppādanirodhavāro",
              "(Ca) paccanīkapuggalokāsā"):
        row(p, DY.heading(p))
    row("Nirodhavāro.", DY.SECTION_END["Nirodhavāro."])
    for p in ("Nirujjhanti.", "Nirujjhittha.", "Nirujjhissanti.", "Āmantā.", "No.", "Natthi."):
        row(p, B.SHORT[p])
    row("nirujjhanti / na nirujjhanti", f"{DY.verb('nirujjhanti')[0]} / {DY.verb('na nirujjhanti')[0]}")
    row("nirujjhittha / na nirujjhittha", f"{DY.verb('nirujjhittha')[0]} / {DY.verb('na nirujjhittha')[0]}")
    row("nirujjhissanti / na nirujjhissanti", f"{DY.verb('nirujjhissanti')[0]} / {DY.verb('na nirujjhissanti')[0]}")
    h("Answer heads with the new parts")
    for hd in ("Pacchimacittassa bhaṅgakkhaṇe",
               "Sabbesaṃ upapajjantānaṃ pavatte kusalavippayuttacittassa uppādakkhaṇe arūpe kusalākusalānaṃ bhaṅgakkhaṇe",
               "Kusalavippayuttacittassa uppādakkhaṇe akusalavippayuttacittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ "
               "asaññasattānaṃ", "Itaresaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("Sample lines as built")
    for s in ("(Ka) yassa kusalā dhammā nirujjhanti tassa akusalā dhammā nirujjhantīti? No.",
              "(Ka) yattha kusalā dhammā na nirujjhanti tattha abyākatā dhammā na nirujjhantīti? Nirujjhanti.",
              "Pacchimacittassa bhaṅgakkhaṇe tesaṃ kusalā ca dhammā na nirujjhissanti abyākatā ca dhammā na "
              "nirujjhissanti.",
              "Akusalānaṃ bhaṅgakkhaṇe tesaṃ kusalā dhammā na uppajjanti, no ca tesaṃ akusalā dhammā na nirujjhanti.",
              "Asaññasatte tattha abyākatā dhammā nirujjhittha, no ca tattha kusalā dhammā uppajjittha.",
              "Yattha kusalā dhammā nirujjhanti tattha akusalā dhammā nirujjhitthāti?…Pe…."):
        row(s, tr_line(s))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- kusalākusalānaṃ (before bhaṅgakkhaṇe): termbase «hiện tượng thiện và bất thiện»; with 9-01's «các» "
        "(DHAMMA_GEN) and pi-1 ^1-994 «của các hiện tượng thiện và bất thiện».",
        "- Pacchimacittassa: 8's mind_gen_vi «tâm cuối cùng» (termbase).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-9-120: the heading «(Ca) paccanīkapuggalokāsā» stands as the last line of the segment (after the "
        "paccanīkaokāso answers of the Atītavāra): kept as a line «(e) Chiều nghịch theo người và nơi chốn».",
        "- ^6-9-135: «Yattha …ti?…Pe….» followed by the heading «(Ga) anulomapuggalokāsā» as a second line: kept as "
        "two lines, «… không?…» and «(c) Chiều thuận theo người và nơi chốn».",
        "- ^6-9-125, ^6-9-130, ^6-9-135, ^6-9-140, ^6-9-145, ^6-9-150, ^6-9-155, ^6-9-160: unlabelled "
        "«Yattha …ti?…Pe….» = «… không?…» (9-01).",
        "- ^6-9-162: «Nirodhavāro.» (no niṭṭhito) = «Mục về sự chấm dứt.» (9-01 SECTION_END).",
        "- Termbase adherence: 16 misses, all «Itaresaṃ catuvokārānaṃ pañcavokārānaṃ» = 2-01's one group «chúng sinh "
        "khác trong cõi gồm bốn khối và cõi gồm năm khối» (as 9-01): not genuine.",
        "",
    ]
    return "\n".join(out)


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    DY.check_reused()
    DY.check_shared()
    check_reused()
    check_shared()
    segs = build()
    S.write(CHAPTER, segs)
    ADH_DIR.mkdir(exist_ok=True)
    (ADH_DIR / CHAPTER).write_bytes((S.OUT_DIR / CHAPTER).read_bytes())
    print("wrote", ADH_DIR / CHAPTER)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)


if __name__ == "__main__":
    main()
