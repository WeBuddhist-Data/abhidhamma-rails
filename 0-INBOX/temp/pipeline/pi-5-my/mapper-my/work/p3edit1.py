"""phase 3 edit 1 of map5_rules.py: stock overrides, the three mechanics, G1-G3 / S1 / S3 in the Mapper."""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "map5_rules.py"
s = p.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)


# ---- docstring
rep('''Usage in a chapter script (see map_ch1.py):''', '''Phase 3 (2026-11-21, coordinator decisions on phase 2): the module overrides of the two phase-2 groups that hold
beyond one segment are here (STOCK «phase 3» block, FUNCS «phase 3» block); the three mechanics are fixed (negate():
a gapped negative «S … မV» is checked part by part; glue(): a verb is not glued through a «…ခြင်း / …ရန် / …ရာ» noun
phrase; phrase_present(): the perfect predicate «Xပြီး ဖြစ်» stands for «Xပြီးသော» as in presence()); the book-wide
rules of phase 2 run in the Mapper for every chapter: S1 stem fallback (stem_fn), S3 / G3 negatives inside a multiword
keyword (negate), G1 / G2 the Pāli order of two composed members (pali_order). Single-segment forms stay as CTX rules
in the chapter scripts.

Usage in a chapter script (see map_ch1.py):''')

# ---- STOCK: overrides of phase 2 that hold beyond one segment
rep('''    "phalaṃ": "@phala", "bojjha": "@bojjha", "aṅgā": "@anga", "gati": "@gati", "taṇhā": "@tanha",
}''', '''    "phalaṃ": "@phala", "bojjha": "@bojjha", "aṅgā": "@anga", "gati": "@gati", "taṇhā": "@tanha",
    # phase 3: the module overrides of phase 2 (notes-ch2-15.md, notes-ch16-31.md «Module overrides») that hold beyond
    # one segment; a tuple («a», «b», …) = the first value the segment has as a phrase, then one present by the ending
    # rules, else the pi-1 … pi-4 value (alt)
    "parinibbāyī": "ပရိနိဗ္ဗာန် ပြုသော",                     # Q8 / pi-4 (the pi-5 terms list «…ပြုသူ»)
    "parinibbuto": ("ပရိနိဗ္ဗာန် ပြုပြီးသော", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သော", "ပရိနိဗ္ဗာန် ပြုတော်မူသော"),
    "parinibbute": ("ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော", "ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော"),
    "thero": ("မထေရ်", "ထေရ်"),
    "sukhadukkhaṃ": ("ချမ်းသာနှင့် ဆင်းရဲ", "ချမ်းသာ ဆင်းရဲ", "သုခ ဒုက္ခ"),
    "nirodhadhammaṃ": ("ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော", "ချုပ်ငြိမ်းခြင်း သဘော ရှိသော"),
    "aṅga": "@anga", "aṅgo": "@anga", "aṅgaṃ": "@anga", "aṅgānaṃ": "@anga",
    "dhammo": ("သဘောတရား", "တရား"),
    "maggo": "@magga", "maggaṃ": "@magga", "magga": "@magga",
    "rāga": ("ရာဂ", "တပ်မက်မှု"), "rāgo": ("ရာဂ", "တပ်မက်မှု"),
    "samāpatti": ("ဈာန် ဝင်စားခြင်း", "သမာပတ်"),
    "nirodho": ("ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"), "nirodhaṃ": ("ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"),
    "dhātū": "@dhatu_plane", "dukkhā": "@dukkha", "jano": "@jana", "janassa": "@jana",
}''')

# ---- FUNCS: phase 3
rep('''    "gati": lambda kw, pali, my: "လားရာ" if "လားရာ" in my else "@prior",''',
    '''    "gati": lambda kw, pali, my: "လားရာ" if "လားရာ" in my else "@prior",
    # phase 3 (ch16-31 override 5): the member aṅga of bojjhaṅga (one Burmese word «ဗောဇ္ဈင်», pi-2 decision 4) =
    # (no direct equivalent) where the FIRST aṅga compound of the Pāli is bojjhaṅga; else «အင်္ဂါ»
    "anga": lambda kw, pali, my: NONE if (first_compound(strip_brackets(pali), [
        (r"[a-zāīūṃṅñṭḍṇḷ]*bojjhaṅg", "B"), (r"[a-zāīūṃṅñṭḍṇḷ]+aṅg", "A"), ("aṅg", "A")]) == "B"
        and "ဗောဇ္ဈင်" in my) else ("အင်္ဂါ" if "အင်္ဂါ" in my else "@prior"),''')
rep('''    "antarika": lambda kw, pali, my: "ကြားအပိုင်း" if "ကြားအပိုင်း" in my else "@prior",''',
    '''    # jhānantarikā «ဈာန်တို့အကြား ကာလ» (ch26, phase 3), else «ကြားအပိုင်း»
    "antarika": lambda kw, pali, my: "အကြား ကာလ" if "အကြား ကာလ" in my else (
        "ကြားအပိုင်း" if "ကြားအပိုင်း" in my else "@prior"),''')
rep('''    "bhavito": lambda kw, pali, my: "ပွားများပြီးသော" if presence("ပွားများပြီးသော", my)[0] else (
        "ပွားများသော" if presence("ပွားများသော", my)[0] else "@prior"),''',
    '''    "bhavito": lambda kw, pali, my: "ပွားများပြီးသော" if presence("ပွားများပြီးသော", my)[0] else (
        "ပွားများထားသော" if presence("ပွားများထားသော", my)[0] else (           # phase 3 (ch16-31 override 7)
            "ပွားများသော" if presence("ပွားများသော", my)[0] else "@prior")),''')
rep('''    "hitaya": pref("အကျိုးစီးပွား", "အကျိုး"),''', '''    "hitaya": pref("အကျိုးစီးပွား", "အကျိုး"),
    # phase 3: magga = the path «မဂ်» where the text has it, the road «လမ်း» (maggāmagga, the verses) otherwise
    "magga": lambda kw, pali, my: "မဂ်" if "မဂ်" in my and not re.search(r"maggāmagg", pali) else (
        "လမ်း" if "လမ်း" in my else ("မဂ်" if "မဂ်" in my else "@prior")),
    # phase 3 (ch16-31 override 10): dhātū before «ti» (kāma- / rūpa- / arūpadhātūti) the plane «ဘုံ», else «ဓာတ်»
    "dhatu_plane": lambda kw, pali, my: "ဘုံ" if "ဘုံ" in my and re.search(r"(kāma|rūpa)dhāt", pali) else (
        "ဓာတ်" if "ဓာတ်" in my else "@prior"),
    # phase 3: jano / janassa of puthujjana: the one Burmese word «ပုထုဇဉ်» goes to puthu (pi-2 decision 4)
    "jana": lambda kw, pali, my: NONE if "puthujjan" in pali.lower() and "ပုထုဇဉ်" in my else "@prior",''')

# aññā: sammadaññāvimutto «သိ၍», aññāpaṭivedha «ရဟန္တာ ဖိုလ်» (ch2-15 override)
rep('''    if v == "K" and "အပြည့်အဝ သိမြင်" in my:
        return "အပြည့်အဝ သိမြင်ခြင်း" if "အပြည့်အဝ သိမြင်ခြင်း" in my else "@prior"
    return f_anna(kw, pali, my)''', '''    if v == "K" and "အပြည့်အဝ သိမြင်" in my:
        return "အပြည့်အဝ သိမြင်ခြင်း" if "အပြည့်အဝ သိမြင်ခြင်း" in my else "@prior"
    # phase 3 (ch2-15 override): sammadaññāvimutto «… သိ၍ လွတ်မြောက်», aññāpaṭivedha «ရဟန္တာ ဖိုလ်ကို ထိုးထွင်း»
    v = first_compound(p, [("sammadaññ", "သိ၍"), ("aññāpaṭivedh", "ရဟန္တာ ဖိုလ်")])
    if v is not None and presence(v, my)[0]:
        return v
    return f_anna(kw, pali, my)''')

# ---- alt()
rep('''def in_text(pali_word, value):''', '''def alt(*vals):
    """phase 3 (the phase-2 tuples, group rule S2): the first value the segment's Burmese has as a phrase, then the
    first present by the ending rules, else the pi-1 … pi-4 value (one sense per segment, the text's own word)."""
    def f(kw, pali, my):
        for v in vals:
            if v == NONE or presence(v, my)[0] and phrase_ok(v, my):
                return v
        for v in vals:
            if presence(v, my)[0]:
                return v
        return "@prior"
    return f


def in_text(pali_word, value):''')

# ---- mechanic 3: phrase_present accepts the perfect predicate «Xပြီး ဖြစ်» for «Xပြီးသော»
rep('''def phrase_present(s, my):
    """the phrase stands in the text, its final «သည် / သော» standing for one of the text's endings (rules 3 / 4)."""
    if s in my:
        return True
    if s.endswith("သည်"):
        return any(s[:-3] + e in my for e in VERB_FROM)
    if s.endswith("သော"):
        return any(s[:-3] + e in my for e in ATTR_FROM)
    return False''', '''def phrase_present(s, my, verb_from=None):
    """the phrase stands in the text, its final «သည် / သော» standing for one of the text's endings (rules 3 / 4); a
    perfect participle «Xပြီးသော» also as the text's perfect predicate «Xပြီး ဖြစ်» (phase 3: as presence() does)."""
    if s in my:
        return True
    if s.endswith("သည်"):
        return any(s[:-3] + e in my for e in (verb_from or VERB_FROM))
    if s.endswith("သော"):
        if s.endswith("ပြီးသော") and s[:-3] + " ဖြစ်" in my:
            return True
        return any(s[:-3] + e in my for e in ATTR_FROM)
    return False


# phase 3: a finite verb is glued to its neighbour only in a verbal form, not through a noun phrase «…ခြင်း / …ရန်
# / …ရာ» («ရဟန္တာ၏ ဆုတ်ယုတ်ခြင်း» is parihāni, not «Parihāyati arahā»)
GLUE_VERB_FROM = tuple(e for e in VERB_FROM if e not in ("ခြင်း", "ရန်", "ရာ"))''')

# ---- mechanic 2: glue
rep('''    a_last, b_first = a.split(" … ")[-1], b.split(" … ")[0]
    if phrase_present(f"{a_last}{b_first}", my) and not phrase_present(f"{a_last} {b_first}", my):
        return "\\0"            # one written word in the text («နတ်မျက်စိ»): no space
    for p in PARTICLES:
        if phrase_present(f"{a_last}{p} {b_first}", my):
            return p + " "
    return None''', '''    a_last, b_first = a.split(" … ")[-1], b.split(" … ")[0]
    vf = GLUE_VERB_FROM if is_verb(b) and " … " not in b else None
    if phrase_present(f"{a_last}{b_first}", my, vf) and not phrase_present(f"{a_last} {b_first}", my, vf):
        return "\\0"            # one written word in the text («နတ်မျက်စိ»): no space
    for p in PARTICLES:
        if phrase_present(f"{a_last}{p} {b_first}", my, vf):
            return p + " "
    return None''')

# ---- mechanic 1: neg_value -> negate (part by part; S3 / G3)
rep('''def neg_value(v, my):
    """«na / no X»: a verb «Xသည်» -> «မXသည်» where the text builds the negative with the prefix (pi-1 rule 9: free na
    = the text's prefix «မ»); otherwise the text's «X မဟုတ်» (pi-1 rule 5, the free negative = «… မဟုတ်»)."""
    if v == NONE:
        return v
    if v.endswith("သည်"):
        st = v[:-3]
        head, _, last = st.rpartition(" ")
        cand = (head + " " if head else "") + "မ" + last     # pi-2 «na uppajjati = … မဖြစ်ပေါ်»
        if cand in my:
            return cand
    if v.endswith("သော"):
        return v[:-3] + "သည် မဟုတ်သော"
    return v + " မဟုတ်"''', '''def negate(v, my):
    """«na / no X» and a negative inside a multiword keyword (S3 / G3, Q5): the LAST verb chunk «Xသည် / Xသော» becomes
    the text's «မX» (pi-1 rule 9: free na = the text's prefix «မ»; pi-2 «na uppajjati = … မဖြစ်ပေါ်»), or its infix
    «XမY» (ဖြစ်ပေါ် / တွေ့ရ …), or «X မဟုတ်» (pi-1 rule 5); every « … » part is checked in the text by itself (phase 3:
    the old check took a gapped «S … မV» as one literal phrase and never found it). With no such form: «X … မဟုတ်»
    where the text has «မဟုတ်» (pi-1 rule 5), else «X မဟုတ်» (the module's earlier fallback)."""
    if v == NONE:
        return v
    head, sep, last = v.rpartition(" … ")
    pre, sp, w = last.rpartition(" ")
    base = head + sep + pre + sp
    if w.endswith(("သည်", "သော")) and len(w) > 3:
        st = w[:-3]
        cands = [base + st[:i] + "မ" + st[i:] for i in range(0, len(st))] + [base + st + " မဟုတ်"]
        for c in cands:
            if all(p in my for p in c.split(" … ")):
                return c
    if v.endswith("သော"):
        return v[:-3] + "သည် မဟုတ်သော"
    if "မဟုတ်" in my and v + " မဟုတ်" not in my:
        return v + " … မဟုတ်"
    return v + " မဟုတ်"


neg_value = negate             # the phase-1 name''')
rep('''            v = self.lookup(ch, sid, rest, pali, my)
            return neg_value(v, my)''', '''            v = self.lookup(ch, sid, rest, pali, my)
            return negate(v, my)''')

p.write_text(s, encoding="utf-8")
print("ok")
