"""pi-6 Burmese keyword mapping, PHASE 2, group G3: 9-01 … 9-03 dhammayamaka, 10-01 … 10-13 indriyayamaka.

Imports the shared module map6_rules.py (NOT edited) and holds only the G3 group table, a few per-segment overrides
(CTX) and the new context functions of the group (FUNCS_G3). Maps the G3 chapters in chapter order, writes
<ch>.mapped.md, prints the three checks of the phase-1 brief per chapter (keyword preservation `bad []`, presence,
no «, » / «၊» / « / » in a value), and with --report the S1 review (every use whose module-only value comes from the
stem fallback: kept or corrected), the values that differ from pi-1 … pi-5 / the sample, and the phrase scan.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g3.py [chapter-prefix …] [--report] [-v]
Notes: notes-g3.md.
"""
import re
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

NONE = R.NONE
G3 = ["9-01-dhammayamaka", "9-02-dhammayamaka", "9-03-dhammayamaka"] + \
     [f"10-{i:02d}-indriyayamaka" for i in range(1, 14)]


# =====================================================================================================================
# context functions of the group (a table value «@name» calls one)
# =====================================================================================================================
# ---- X-sampayutta / X-vippayutta citta compounds (zero-shot notes ch9-10a / ch10b / ch10c; pi-1 rule 3 «…နှင့်
# ယှဉ်တွဲသော» pi-1 ^1-1, «…နှင့် ကင်းကွာသော» pi-2 ^2-767; two members «Aနှင့် … ၍ Bနှင့် … သော», the text's absolutive)
CMEM = {"kusala": "ကုသိုလ်", "akusala": "အကုသိုလ်", "saddhā": "ယုံကြည်မှု", "somanassa": "ဝမ်းမြောက်မှု",
        "upekkhā": "ဥပေက္ခာ", "ñāṇa": "ဉာဏ်"}
_CM = "(?:akusala|kusala|saddhā|somanassa|upekkhā|ñāṇa)(?:sampayutta|vippayutta)"
_CITTA = re.compile(r"^((?:" + _CM + r")+)(pacchimacittasamaṅg|pacchimacitt|citt)(īnaṃ|ī|assa|aṃ|e|ānaṃ|a)$")
MOMENT = {"uppādakkhaṇe": "ဖြစ်ခြင်း ခဏ", "bhaṅgakkhaṇe": "ပြိုပျက်ခြင်း ခဏ"}


def citta_value(w):
    """«Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ် / နောက်ဆုံး စိတ်»; -pacchimacittasamaṅgī «… နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ» (R8
    agent noun); upapatticitta «ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်» (zero-shot notes ch2-02-4-5, as G1)."""
    w = R.low(w)
    if re.match(r"^upapatticitt(assa|e|aṃ)$", w):
        return "ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်"
    m = _CITTA.match(w)
    if not m:
        return None
    mem = re.findall(r"(akusala|kusala|saddhā|somanassa|upekkhā|ñāṇa)(sampayutta|vippayutta)", m.group(1))
    parts = [CMEM[x] + "နှင့် " + ("ယှဉ်တွဲ" if y == "sampayutta" else "ကင်းကွာ") for x, y in mem]
    head = {"citt": "စိတ်", "pacchimacitt": "နောက်ဆုံး စိတ်", "pacchimacittasamaṅg": "နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ"}
    return " ".join(p + "၍" for p in parts[:-1]) + (" " if len(parts) > 1 else "") + parts[-1] + "သော " + \
        head[m.group(2)]


def f_citta(kw, pali, my):
    """a citta compound alone = its value (rule 1: the case particle goes); with a moment «… စိတ်၏ ဖြစ်ခြင်း ခဏ /
    ပြိုပျက်ခြင်း ခဏ» (harmonise B1: the final «၌» goes, the inner «၏» stays)."""
    ws = kw.split()
    c = citta_value(ws[0])
    if c is None:
        return "@prior"
    if len(ws) == 2 and R.low(ws[1]) in MOMENT:
        return c + "၏ " + MOMENT[R.low(ws[1])]
    return c


# ---- sa-X-ka / a-X-ka persons (G1 rule G3; harmonise B9: the text «X ရှိလျက် / X မရှိဘဲ»; pi-1 rule 3 as Sahetukaṃ
# «အမြစ် ရှိသော»; the text's «ရှိလျက် / မရှိဘဲ» by the ending rule «လျက် / ဘဲ», pi-2 N11)
SAKA = {"cakkhuk": "မျက်စိ", "sotak": "နား", "ghānak": "နှာခေါင်း", "jivhak": "လျှာ", "kāyak": "ကိုယ်", "cittak": "စိတ်"}
_SAKA = re.compile(r"^(sa|a)(cakkhuk|sotak|ghānak|jivhak|kāyak|cittak)(ānaṃ|ā|assa|o|aṃ|e)$")


def f_saka(kw, pali, my):
    m = _SAKA.match(R.low(kw))
    if not m:
        return "@prior"
    return SAKA[m.group(2)] + (" ရှိသော" if m.group(1) == "sa" else " မရှိသော")


# ---- feminine participles -antīnaṃ (group rule W3): «itthīnaṃ upapajjantīnaṃ» «ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့» = the
# text's attributive «Sဆဲ» before the noun (R3; the module's agent noun «Sဆဲသူ» stands in the segment only as the
# word of the masculine upapajjantānaṃ); after a relative «… tāsaṃ upapajjantīnaṃ» «…မိန်းမတို့အနက် ပြန်လည်
# ဖြစ်ပေါ်ဆဲသူတို့» the agent noun (the module value). One sense per segment: the keyword's FIRST occurrence decides.
def f_fem(kw, pali, my):
    pc = R.participle_cands(kw)
    if not pc:
        return "@prior"
    p = R.strip_brackets(pali)
    m = re.search(r"(\S+)\s+" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", p)
    attr = pc[1]                                   # «Sဆဲ»
    if m and m.group(1).lower() != "tāsaṃ" and re.search(re.escape(attr) + " (?!သူ)", my):
        return attr
    for v in pc:
        if R.presence(v, my)[0] and R.phrase_ok(v, my):
            return v
    return "@prior"


# ---- sacchikaroti in every tense (R2): the module's «မျက်မှောက်ပြု…» where the text has it; the bare positive of a
# negated clause (rule 8 / Q5) where the text has only «မျက်မှောက် မပြုခဲ့» = the positive part with the text's own
# spacing «မျက်မှောက် ပြုခဲ့သည်» (pi-5 sacchikaroti «မျက်မှောက် ပြုသည်»); the module's verifier finds «မျက်မှောက်ပြုခဲ့သည်»
# there neither literally nor by an ending rule (the space before the infixed «မ»).
SACCHI_END = {"pres": "သည်", "past": "ခဲ့သည်", "fut": "လိမ့်မည်"}


def f_sacchi(kw, pali, my):
    v = R.morph_value(kw, pali, my)[0]
    if v:
        return v
    pv = R.parse_verb(kw)
    if pv and not pv[2]:
        w = "မျက်မှောက် ပြု" + SACCHI_END[pv[1]]
        if R.presence(w, my)[0]:
            return w
    return "@prior"


# ---- R6 in a body line (G1 rule G1 / G2 rule V1): a vāra named in a colophon line «X-vāro» = «Xအလိုက် ဖော်ပြချက်»;
# a heading line keeps the heading rule's whole part
VARA = [("uppādanirodha", "ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်း"), ("uppāda", "ဖြစ်ပေါ်ခြင်း"), ("nirodha", "ချုပ်ငြိမ်းခြင်း"),
        ("pariññā", "ပိုင်းခြား သိခြင်း"), ("bhāvanā", "ဘာဝနာ ပွားများခြင်း"), ("pavatti", "ဖြစ်ပျက်ခြင်း")]
_VARA = re.compile(r"^(\w+?)vār(o|e|epi|aṃ|ena|a|ampi)$")


def vara_value(kw):
    m = _VARA.match(R.low(kw))
    if not m:
        return None
    for st, my in VARA:
        if m.group(1) == st:
            return my + "အလိုက် ဖော်ပြချက်"
    return None


def f_vara(kw, pali, my):
    if pali.lstrip().startswith("#"):
        h = R.heading_value(kw, pali, my)
        if h:
            return h
    v = vara_value(kw)
    if v and (R.phrase_ok(v, my) or R.phrase_ok(v, R.flat(my))):
        return v
    h = R.heading_value(kw, pali, my)
    return h if h else "@prior"


FUNCS_G3 = {"citta": f_citta, "saka": f_saka, "fem": f_fem, "sacchi": f_sacchi, "vara": f_vara}


# =====================================================================================================================
# group table (every G3 chapter): only what the module does not settle or settles wrongly (notes-g3.md)
# =====================================================================================================================
AÑÑA = "အပြည့်အဝ သိမြင်ခြင်း"                   # aññaṃ = the pi-2 faculty name without «၏ စွမ်းရည်» (ch9-10a)
ANAÑÑA = "မသိရသေးသည်ကို သိရတော့မည်ဟူသော"        # anaññātaññassāmīti = the faculty name without «စွမ်းရည်» (harmonise A2)
AÑÑĀTĀVĪ = "အပြည့်အဝ သိမြင်ပြီးသူ"               # aññātāvī (pi-5)

T_ALL = {
    # yattha «where» = «အကြင်နေရာ» (G1 G8 / G2 O6: the text's «အကြင်နေရာ၌», rule 1)
    "Yattha": "အကြင်နေရာ", "yattha": "အကြင်နေရာ",
    # the bare words of the faculties (padasodhana / paṇṇatti 10-01, 10-02): one sense per segment, the bare word,
    # not the faculty name that the stem fallback took from the same segment
    "aññaṃ": AÑÑA, "Aññaṃ": AÑÑA, "aññanti": AÑÑA, "Aññañca": AÑÑA,
    "anaññātaññassāmīti": ANAÑÑA, "Anaññātaññassāmītiṃ": ANAÑÑA, "Anaññātaññassāmītiñca": ANAÑÑA,
    "anaññātaññāssāmīti": ANAÑÑA,                              # the source slip of 10-01 ^6-10-3 (ch9-10a notes)
    "Aññātāviṃ": AÑÑĀTĀVĪ, "Aññātāviñca": AÑÑĀTĀVĪ,
    # «X-ñca dhamme ca ṭhapetvā» «Xနှင့် သဘောတရားများကို ချန်ထား၍» (9-01 paṇṇatti): the two members with the «နှင့်» of
    # ca … ca between them (Q3; rule 1: the inner particle stays, the plural goes); compose had joined them to the
    # phrase «X သဘောတရား» of the keyword «X dhammā» elsewhere in the segment
    "Kusalañca dhamme": "ကုသိုလ်နှင့် သဘောတရား", "Akusalañca dhamme": "အကုသိုလ်နှင့် သဘောတရား",
    "Abyākatañca dhamme": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … သဘောတရား",     # «… မဟုတ်သော အရာများနှင့် သဘောတရား…»
    # ñāṇasampayuttānaṃ (persons) = «ဉာဏ်နှင့် ယှဉ်တွဲသော» (as the pi-2 ñāṇavippayuttānaṃ «ဉာဏ်နှင့် ကင်းကွာသော»; the
    # text's «… ယှဉ်တွဲလျက်» by the ending rule, harmonise B9)
    "ñāṇasampayuttānaṃ": "ဉာဏ်နှင့် ယှဉ်တွဲသော", "Ñāṇasampayuttānaṃ": "ဉာဏ်နှင့် ယှဉ်တွဲသော",
    # other words (G1 values; pi-2 agga-)
    "taṇhāsotaṃ": "တပ်မက်မှု ရေစီး", "aggaphalaṃ": "အမြတ်ဆုံး ဖိုလ်",
    # the book colophon «Yamakapakaraṇaṃ niṭṭhitaṃ» «“အတွဲလိုက် မေးဖြေခြင်း” ကျမ်း ပြီးဆုံးပြီ» (pi-2 Vibhaṅgapakaraṇaṃ
    # «ခွဲခြမ်းစိတ်ဖြာခြင်း ကျမ်း»: the title + «ကျမ်း», rule 7)
    "Yamakapakaraṇaṃ": "အတွဲလိုက် မေးဖြေခြင်း ကျမ်း",
    # headings with a source digit and no dot («#### 3 Suddhadhammavāro»: R6 cannot split them); the text's whole part
    "Suddhadhammavāro": "ရိုးရိုး သဘောတရား ဖော်ပြချက်",
    "Suddhadhammamūlacakkavāro": "ရိုးရိုး သဘောတရားကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက်",
    # source slips (the text renders the intended word; harmonise A3)
    "Ghānandriyamūlakaṃ": "နှာခေါင်း၏ စွမ်းရည်ကို အခြေခံသော",       # Ghānindriyamūlakaṃ (10-08 ^6-10-336)
    "cavantāna": "စုတေဆဲသူ",                                       # cavantānaṃ (10-08 ^6-10-361)
    # sa-X-ka / a-X-ka persons
    **{k: "@saka" for k in ("Sacakkhukānaṃ", "sacakkhukānaṃ", "acakkhukānaṃ", "Acakkhukānaṃ", "sasotakānaṃ",
                            "asotakānaṃ", "sacakkhukā", "Sacittakānaṃ", "sacittakānaṃ", "Acittakānaṃ")},
}
CTX = {
    # Pāli slips with one letter (harmonise A3): the intended word, the text's form
    "6-10-309": {"upapajjissati": "ဖြစ်ပေါ်လိမ့်မည်"},                # for uppajjissati («… မဖြစ်ပေါ်လိမ့်မည်ကား မဟုတ်»)
    "6-10-398": {"uppajjantānaṃ": "ပြန်လည် ဖြစ်ပေါ်ဆဲ"},              # for upapajjantānaṃ («ပြန်လည် ဖြစ်ပေါ်ဆဲ … ယောက်ျားတို့»)
    "6-10-206": {"uppajjantīnaṃ": "ပြန်လည် ဖြစ်ပေါ်ဆဲ"},              # for upapajjantīnaṃ («ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့»)
}
# every keyword of the G3 chapters that a family function covers goes through it (unless a table has it)
for _ch in G3:
    for _sid, _kws in R.keyword_rows(_ch):
        for _k in _kws:
            if _k in T_ALL:
                continue
            _w = R.low(_k.split()[0])
            if citta_value(_w) is not None and (len(_k.split()) == 1 or R.low(_k.split()[1]) in MOMENT):
                T_ALL[_k] = "@citta"
            elif vara_value(_k):
                T_ALL[_k] = "@vara"
            elif re.match(r"^(sacchikar|sacchākā)", _w):
                T_ALL[_k] = "@sacchi"
            elif re.match(r"^(upapajj|cav)antīnaṃ$", _w):
                T_ALL[_k] = "@fem"
TABLES = {ch: T_ALL for ch in G3}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS_G3, stem=R.make_stem([R.FRAME, R.STOCK, T_ALL]))


def module_only():
    return R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))


# =====================================================================================================================
# reports
# =====================================================================================================================
def s1_review(ch, base, lines):
    """the uses whose MODULE-ONLY value comes from the stem fallback (S1): kept (the final value is the stem value) or
    corrected (a G3 table / context value replaces it)."""
    kept, corr = collections.Counter(), collections.Counter()
    b_lines = base.map_chapter(ch)[0]
    for lb, lf in zip(b_lines, lines):
        sid, rb = lb[1:].split("] ", 1)
        rf = lf.split("] ", 1)[1]
        for kvb, kvf in zip(rb.split(", "), rf.split(", ")):
            k, vb = kvb.split("=", 1)
            vf = kvf.split("=", 1)[1]
            if base.SRC.get((sid, k)) == "stem":
                (kept if vb == vf else corr)[(k, vb, vf)] += 1
    return kept, corr


def diff_report(chs):
    """values that differ from a pi-1 … pi-5 value of the same keyword (or its base form, R1), and from the phase-1
    sample and the G1 / G2 mapped files for the same keyword."""
    other = collections.defaultdict(collections.Counter)
    for ch in R.CHAPTERS:
        if ch in G3 or not (HERE / f"{ch}.mapped.md").exists():
            continue
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                other[k][v] += 1
    same = new = 0
    prior_diff, other_diff = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
    for ch in chs:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if not pv:
                    new += 1
                elif v in pv:
                    same += 1
                else:
                    prior_diff[(k, v)][pv.most_common(1)[0][0]] += 1
                if other.get(k) and v not in other[k]:
                    other_diff[(k, v)][other[k].most_common(1)[0][0]] += 1
    print(f"PRIOR same {same} new {new} diff {sum(sum(c.values()) for c in prior_diff.values())} "
          f"({len(prior_diff)} pairs)")
    for (k, v), c in sorted(prior_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   PRIORDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))
    for (k, v), c in sorted(other_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   GROUPDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))


def phrase_scan(chs):
    """values that the segment's Burmese does not have as a phrase (every « … » part, its final «သည် / သော» by an
    ending rule; also without quotation marks / the list comma): present only chunk by chunk or by an ending rule."""
    c = collections.Counter()
    for ch in chs:
        my = R.burmese(ch)
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            t = my[sid]
            vs = [t, R.flat(t), re.sub("[“”]", "", t), R.flat(re.sub("[“”]", "", t))]
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                if v != NONE and not any(R.phrase_ok(v, x) for x in vs):
                    c[(ch, k, v)] += 1
    print(f"PHRASE not a phrase: {sum(c.values())} uses ({len(c)} pairs)")
    for (ch, k, v), n in sorted(c.items()):
        print(f"   NOPHRASE {ch} {k} = {v} ({n})")


def run(chs):
    M, B = mapper(), module_only()
    tot = collections.Counter()
    allkept, allcorr = collections.Counter(), collections.Counter()
    for ch in chs:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        rules = collections.Counter(r for _, _, _, r in ruled)
        kept, corr = s1_review(ch, B, lines)
        allkept.update(kept)
        allcorr.update(corr)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ending-rule chunks {dict(sorted(rules.items()))} S1 kept {sum(kept.values())} "
              f"corrected {sum(corr.values())}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, nde=nne, fails=len(fails), punct=len(punct), bad=len(bad), unmapped=len(unmapped),
                   kept=sum(kept.values()), corr=sum(corr.values()), ruled=len(ruled))
    print("TOTAL", dict(sorted(tot.items())))
    if "--report" in sys.argv:
        for (k, vb, vf), c in sorted(allkept.items()):
            print(f"   S1 KEPT {k} = {vb} ({c})")
        for (k, vb, vf), c in sorted(allcorr.items()):
            print(f"   S1 CORRECTED {k}: {vb} -> {vf} ({c})")
        diff_report(chs)
        phrase_scan(chs)
    return M


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    run([ch for ch in G3 if not args or any(ch.startswith(a) for a in args)])
