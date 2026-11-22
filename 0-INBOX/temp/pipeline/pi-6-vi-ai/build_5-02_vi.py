# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 5-02-saccayamaka.md (Saccayamaka: nirodhavāra from the present
section on, uppādanirodhavāra up to the present-and-past section).

Every frame comes VERBATIM from the frame-setters:
  build_5-01_vi (T): sacca members m(), the answer-head parser head_vi(), the whole family-B sentence parser
                     translate_sentence(), variant(), the citta moments, persons, planes;
  build_2-01_vi (F): families A / B (question / answer frames, verbs and tenses, RES_VI, STATEMENT_RES, REL_VI …);
  build_2-02_vi (E): pe_fragment(), pe_end(), «Nirodhavāro.»;
  build_8_vi (C8):   citta(last=True) «tâm cuối cùng», PE;
  build_6-01_vi (C6, finished chapter): the editorial-note words YASSAKA / YATTHAKA / YASSAYATTHAKA / NIRODHA_CASE
                     and the «(b) Còn ở người nào…» shortening.
Settled here (listed in notes-5-02.md): the heading «Pavatti 3. uppādanirodhavāro», the «pacchimacittassa …kkhaṇe»
moment, a variant bracket closing an answer head, the «…pe…» half-answers and the editorial notes of this chapter.

Local extensions of build_5-01_vi (additive only, in memory; nothing T already translated changes): one HEAD_RULES_C
entry (pacchimacittassa), one VAR_TAIL entry, and _groups() accepts a variant bracket at the end of a head.

Importing writes nothing; run  python -I -X utf8 -B build_5-02_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

T = importlib.import_module("build_5-01_vi")     # this yamaka's frame-setter
F = importlib.import_module("build_2-01_vi")     # families A / B
E = importlib.import_module("build_2-02_vi")     # family E, pe_fragment / pe_end
C8 = importlib.import_module("build_8_vi")       # aspect forms and moments
C6 = importlib.import_module("build_6-01_vi")    # editorial-note words (finished chapter)
assert T.F is F and T.E is E and T.C8 is C8

NAME = "5-02-saccayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
PE = C8.PE                                        # …pe… = …
SLIPS = []

# ================================================================ local extensions of the 5-01 head parser
# Pacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của tâm cuối cùng (8, 6-01)
PACCHIMA_RX = re.compile(r"(?:pacchimacittassa (?P<mo>uppāda|bhaṅga)kkhaṇe)(?P<comma>,)?(?: |$)")
if not any(rx is PACCHIMA_RX or rx.pattern == PACCHIMA_RX.pattern for rx, _k, _f in T.HEAD_RULES_C):
    T.HEAD_RULES_C.append((PACCHIMA_RX, "T", lambda g: T._moment(g["mo"], C8.citta(last=True))))

# variant tail: «[paṭilabhissanti tassa cittassa uppādakkhaṇe (sī. syā.) uppādavāre pana pāṭhantaraṃ natthi]»
T.VAR_TAIL.setdefault(" uppādavāre pana pāṭhantaraṃ natthi",
                      f", nhưng trong {S.SECTION['uppādavāro']} thì không có {S.VAR}")
# pāṭhantara «dị bản» (the variant label itself); «, nhưng trong mục về sự sinh khởi thì không có dị bản»

_ORIG_GROUPS = getattr(T, "_ORIG_GROUPS_502", T._groups)
T._ORIG_GROUPS_502 = _ORIG_GROUPS
_END_VAR = re.compile(r"(?P<h>.+?) (?P<v>\[[^\]]+\])")


def _groups(g):
    """T._groups plus a variant bracket closing the head (^6-5-97, ^6-5-122): it follows the last group."""
    mm = _END_VAR.fullmatch(g)
    if mm:
        out = _ORIG_GROUPS(mm["h"])
        out[-1][1] += " " + T.variant(mm["v"])
        return out
    return _ORIG_GROUPS(g)


T._groups = _groups

# ================================================================ headings
SECTION_502 = {
    "Pavatti 3. uppādanirodhavāro": f"{S.SECTION['Pavatti']} 3. {low(S.SECTION['Uppādanirodhavāro'])}",
    # = «Pavatti 2. nirodhavāro» «Sự diễn tiến 2. mục về sự chấm dứt» (sample)
}


def heading(t):
    return SECTION_502[t] if t in SECTION_502 else T.heading(t)


# ================================================================ editorial notes
YASSAKA, YATTHAKA, YASSAYATTHAKA = C6.YASSAKA, C6.YATTHAKA, C6.YASSAYATTHAKA   # phần về người / nơi chốn / người và nơi chốn
BOTH_SECTIONS = C6.BOTH_SECTIONS                 # phần về người và phần về người và nơi chốn
NIRODHA_CASE = C6.NIRODHA_CASE                   # trường hợp những người nhập thành tựu thiền chấm dứt
NO_DIFF = "không có sự khác biệt"                # natthi nānākaraṇaṃ (6-01; nānākaraṇa «sự khác biệt» pi-5)
SAME = "đều giống nhau"                          # sadisaṃ (6-01)
CA_LAN = "cả {a} lẫn {b}"                        # Xampi Yampi (6-01 «cả chiều thuận lẫn chiều nghịch»)
ANU_PACC = CA_LAN.format(a=low(S.SECTION["anulomaṃ"]), b=low(S.SECTION["paccanīkaṃ"]))
# bare section names (uppāde, nirodhe, uppādanirodhe: no «vāra») = «sự sinh khởi», «sự chấm dứt», «sự sinh khởi và
# sự chấm dứt»; with «vāra» the sample's «mục về …»
BARE = {"uppāde": "sự sinh khởi", "nirodhe": "sự chấm dứt", "uppādanirodhe": "sự sinh khởi và sự chấm dứt"}
VARA = {"uppādavāre": S.SECTION["uppādavāro"], "nirodhavāre": S.SECTION["nirodhavāro"],
        "uppādanirodhavāre": low(S.SECTION["Uppādanirodhavāro"])}
YATTHAKA_SAME = "({y} thì ở {a}, ở {b}, ở {c} {same}, {nd})."
YATHA_VIBHATTA_1 = "(Như {q}, {ap}, đã được phân tích trong {v}, ở {w} cũng nên phân tích như vậy, {nd})."
YATHA_VIBHATTA_2 = "(Như {q} đã được phân tích trong {v}, trong {w} cũng nên phân tích như vậy, {ap})."
ATITA_Q = "các câu hỏi về quá khứ"                # atītā pucchā (6-01)
PAC_ATITA_Q = "Các câu hỏi về hiện tại và quá khứ"   # paccuppannaatītā pucchā (S.SECTION Paccuppannātītavāro)
ASAMMOHA = "nên phân tích mà không mê lầm"       # asammohantena vibhajitabbā (sammoha «sự mê lầm» pi-1)
NOT_INCLUDE = "trong {y} cũng không nên đưa vào {n}"   # yassayatthakepi … na kātabbaṃ (6-01 «không nên đưa vào»)
DIFF_IN = "ở {a} và {b} thì có sự khác biệt"     # samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ


def _inner(vi_sentence):
    """A whole Vietnamese answer used inside a note: lowercase start, no final period."""
    assert vi_sentence.endswith("."), vi_sentence
    return low(vi_sentence[:-1])


def _note_152():
    ans = F.b_both("tesaṃ tattha", T.head_vi("Aggamaggassa bhaṅgakkhaṇe arahantānaṃ asaññasattānaṃ"),
                   T.m("maggasaccaṃ"), F.vparse("na nirujjhissati"), T.m("samudayasaccaṃ"), F.vparse("nuppajjissati"))
    return (f"({cap(BOTH_SECTIONS)} {SAME}, "
            f"{DIFF_IN.format(a=T.m('samudayasaccaṃ'), b=T.m('maggasaccaṃ'))}, {_inner(ans)}).")


EXACT_LINE = {
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).":
        YATTHAKA_SAME.format(y=cap(YATTHAKA), a=BARE["uppāde"], b=BARE["nirodhe"], c=BARE["uppādanirodhe"],
                             same=SAME, nd=NO_DIFF),
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).":
        YATTHAKA_SAME.format(y=cap(YATTHAKA), a=VARA["uppādavāre"], b=VARA["nirodhavāre"],
                             c=VARA["uppādanirodhavāre"], same=SAME, nd=NO_DIFF),
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({cap(YASSAYATTHAKA)} cũng nên được trình bày chi tiết giống như vậy).",
    "(Yassakampi [yassakampi yatthakampi (sī. syā.)] yassayatthakampi sadisaṃ, yassayatthakepi "
    "nirodhasamāpannānanti cetaṃ na kātabbaṃ).":
        (f"({cap(YASSAKA)} {T.variant('[yassakampi yatthakampi (sī. syā.)]')} và {YASSAYATTHAKA} {SAME}, và "
         f"{NOT_INCLUDE.format(y=YASSAYATTHAKA, n=NIRODHA_CASE)})."),
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({cap(BOTH_SECTIONS)} {SAME}, {NOT_INCLUDE.format(y=YASSAYATTHAKA, n=NIRODHA_CASE)}).",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, "
    "natthi nānākaraṇaṃ).":
        YATHA_VIBHATTA_1.format(q=ATITA_Q, ap=ANU_PACC, v=VARA["uppādavāre"], w=BARE["nirodhe"], nd=NO_DIFF),
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        YATHA_VIBHATTA_2.format(q=ATITA_Q, v=VARA["uppādavāre"], w=VARA["uppādanirodhavāre"], ap=ANU_PACC),
    "(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, aggamaggassa bhaṅgakkhaṇe, "
    "arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati samudayasaccañca nuppajjissati).":
        _note_152(),
    "(Paccuppannaatītā [paccuppannenātītā (syā.)] pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi "
    "yassayatthakampi anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).":
        (f"({PAC_ATITA_Q} {T.variant('[paccuppannenātītā (syā.)]')}, "
         f"{CA_LAN.format(a='trong ' + VARA['uppādavāre'], b='trong ' + VARA['uppādanirodhavāre'])}, "
         f"{CA_LAN.format(a=f'{YASSAKA}, {YATTHAKA}', b=YASSAYATTHAKA)}, {ANU_PACC}, {SAME}, {ASAMMOHA})."),
}

# ================================================================ sentences
EXACT = {
    "Nirodhavāro.": E.EXACT["Nirodhavāro."],                                    # Mục về sự chấm dứt. (2-02)
    "(Yassakampi yassayatthakampi sadisaṃ).": f"({cap(BOTH_SECTIONS)} {SAME}).",  # = 6-01 «(… đều giống nhau.)»
}
MEM = r"(?:dukkha|samudaya|nirodha|magga)saccaṃ"
PE_Q_DOT_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w>[Yy]assa vā pana)…pe…\.")
FRAG_RE = re.compile(rf"(?P<w>Yassa yattha|Yattha|Yassa) (?P<x>{MEM}) (?P<v>(?:na )?\S+?)…pe…\.")
PLACE_HALF_RE = re.compile(rf"(?P<g>\S+) tattha (?P<x>{MEM}) (?P<v>(?:na )?[^\s…]+)…pe…\.")
PE_MID_RE = re.compile(r"(?P<g1>.+?) tesaṃ tattha …pe… (?P<g2>.+?) tesaṃ tattha…pe…\.")
assert F.STATEMENT_RES.startswith("{head}, thì {res} ")
RES_HEAD = "{head}, thì {res}"                   # the opening of F.STATEMENT_RES, before the clause


def pe_question_dot(mm):
    """(Kha) yassa vā pana…pe…. = (b) Còn ở người nào…  (6-01; «?» only where the Pāli has it)"""
    s = cap(F.VA_PANA + F.REL_VI["yassa"]) + PE
    return f"{LABEL_VI[mm['l']]} {s}" if mm["l"] else s


# source slips (rendered as meant; each must apply the stated number of times)
SLIP_FIX = [
    ("samudayasaccañca na nirujjhiti.", "samudayasaccañca na nirujjhati.", 1,
     "^6-5-125: «na nirujjhiti» = na nirujjhati (spelling; the question has «na nirujjhatīti»)"),
    ("(Kha) yassa vā pana yattha maggasaccaṃ nirujjhissati tassa tattha samudayasaccaṃ nirujjhitthāti.",
     "(Kha) yassa vā pana yattha maggasaccaṃ nirujjhissati tassa tattha samudayasaccaṃ nirujjhitthāti?", 1,
     "^6-5-130: the (Kha) question ends in «.»; written with «?»"),
]
SLIP_USED = {}
QMARK_LINE = F.b_q("yassa yattha", T.m("maggasaccaṃ"), F.vparse("nirujjhissati"), T.m("samudayasaccaṃ"),
                   F.vparse("nirujjhitthāti"), kha=True, label="Kha")   # the whitelisted «?» line (^6-5-130)
STATIC_NOTES = [   # points in lines translated by EXACT_LINE / as written
    "^6-5-152 (note): commas inside «aggamaggassa bhaṅgakkhaṇe, arahantānaṃ …» change nothing (head parsed as one)",
    "^6-5-138 (note): no comma before «natthi nānākaraṇaṃ» (^6-5-90 has one); Vietnamese comma written",
    "^6-5-124: «… asaññasattaṃ upapajjantānaṃ arūpe aggamaggassa ca phalassa ca bhaṅgakkhaṇe asaññasattaṃ "
    "upapajjantānaṃ …» names the same group twice; both kept (as 5-01 ^6-5-76)",
]


def fix_slips(s):
    for a, b, _n, why in SLIP_FIX:
        if a in s:
            SLIP_USED[why] = SLIP_USED.get(why, 0) + s.count(a)
            s = s.replace(a, b)
    return s


def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    mm = PE_Q_DOT_RE.fullmatch(s)
    if mm:
        return pe_question_dot(mm)
    mm = FRAG_RE.fullmatch(s)                    # Yattha / Yassa yattha X (na) v…pe…. = «Ở nơi nào mà X v…»
    if mm:
        return E.pe_fragment(mm["w"].lower(), T.m(mm["x"]), F.vparse(mm["v"], ctx), "…pe….")
    mm = PLACE_HALF_RE.fullmatch(s)              # Asaññasatte tattha X v…pe…. (half of a place answer)
    if mm:
        clause = f"{T.m(mm['x'])} {F.verb(*F.vparse(mm['v'], ctx))}"
        return E.pe_end(cap(F.STATEMENT_RES.format(head=T.head_vi(mm["g"]), res=F.RES_VI["tattha"], clause=clause)))
    mm = PE_MID_RE.fullmatch(s)                  # ^6-5-148: two heads, each cut after «tesaṃ tattha»
    if mm:
        res = F.RES_VI["tesaṃ tattha"]
        a = cap(RES_HEAD.format(head=T.head_vi(mm["g1"]), res=res))
        b = RES_HEAD.format(head=low(T.head_vi(mm["g2"])), res=res)
        return f"{a} {PE} {b}{PE}"
    if s.endswith("…pe….") and "?" not in s:     # a whole answer cut by «…pe…»: its period gives way to «…»
        return E.pe_end(translate_sentence(s[:-len("…pe….")] + ".", ctx))
    return T.translate_sentence(s, ctx)


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    t = fix_slips(t)
    return " ".join(translate_sentence(s, ctx) for s in F.split_sentences(t)) + sid


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
    ("sự khác biệt", 5), ("mê lầm", 1), ("giống nhau", 5), ("phân tích như vậy", 2), ("đưa vào", 1),
    ("trường hợp", 5), ("dị bản", 2), ("tái sinh", 2), ("khoảnh khắc", 5),
]   # new (no pi-1..5 string): «tâm cuối cùng» (8 / 6-01), «không mê lầm» (asammohantena)


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (5-02): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """The imported frames still say what this chapter relies on (frame-setters / finished chapters)."""
    T.check_frames()
    assert T.EXACT_LINE["(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ)."] == \
        f"({cap(BOTH_SECTIONS)} cũng nên được trình bày chi tiết giống như vậy)."            # 5-01
    assert C6.EXACT["(Yassakampi yassayatthakampi sadisaṃ.)"] == f"({cap(BOTH_SECTIONS)} {SAME}.)"   # 6-01
    mm = C6.FRAG_Q_RE.fullmatch("(Kha) yassa vā pana…pe….")
    assert pe_question_dot(PE_Q_DOT_RE.fullmatch("(Kha) yassa vā pana…pe….")) == C6.frag_question(mm)
    assert T.head_vi("Pacchimacittassa bhaṅgakkhaṇe") == "Vào khoảnh khắc tan rã của tâm cuối cùng"   # = 8 / 6-01
    assert C6.EXACT[("(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi "
                     "vibhattaṃ evaṃ nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)")].endswith(
        f"cũng nên phân tích như vậy, {NO_DIFF}.)")
    assert ANU_PACC in C6.EXACT[("(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi "
                                 "paccanīkampi vibhattaṃ evaṃ nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)")]
    assert E.pe_fragment("yattha", T.m("dukkhasaccaṃ"), F.vparse("uppajjati"), "…pe….") == \
        T.translate_sentence("Yattha dukkhasaccaṃ uppajjati…pe….")                         # = 5-01 FRAG_NOTE_RE


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT_LINE:
            continue
        yield from F.split_sentences(fix_slips(p))


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 5-02 and against 5-01."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    p501 = (S.PALI_DIR / T.NAME).read_text(encoding="utf-8")
    shared = 0
    for s in set(T._sentences(p501)) & set(seen):
        shared += 1
        if T.translate_sentence(s) != seen[s]:
            print("DIFFERS FROM 5-01:", s)
            bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 5-01")
    return bad


def main():
    S.check_cross_book()
    F.check_cross_book()
    T.check_cross_book()
    check_cross_book()
    check_frames()
    SLIPS.clear(); T.SLIPS.clear(); F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    # ^6-5-130: the one «?» written for a Pāli question ending in «.» (SLIP_FIX; as 2-01 ^6-2-36 whitelists its one)
    vl = [x for x in text.splitlines() if x.strip()]
    qok = [p for p in probs if re.fullmatch(rf"{re.escape(NAME)} line (\d+): '\?' count 0 vs 1", p)
           and vl[int(p.split(" line ")[1].split(":")[0]) - 1] == QMARK_LINE]
    assert len(qok) == 1, qok
    probs = [p for p in probs if p not in qok]
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", " ,", " ."):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, n, why in SLIP_FIX:
        assert used.get(why) == n, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in used:
        print("SLIP", why)
    for w in STATIC_NOTES + sorted(set(SLIPS + T.SLIPS)) + [f"{c} | {w}" for c, w in F.SLIPS]:
        print("NOTE", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
