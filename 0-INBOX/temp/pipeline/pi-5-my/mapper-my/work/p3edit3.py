"""phase 3 edit 3: map_ch16-31.py — the overrides now in the module go; the Mapper uses the module's lookup."""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "map_ch16-31.py"
s = p.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)


for old in ['''    "parinibbāyī": "ပရိနိဗ္ဗာန် ပြုသော",               # Q8 / pi-4 (the terms list «…ပြုသူ»)\n''',
            '''"dhātū": "@dhatu_plane", ''',
            '''    "sukhadukkhaṃ": ("ချမ်းသာနှင့် ဆင်းရဲ", "ချမ်းသာ ဆင်းရဲ", "သုခ ဒုက္ခ"),\n''',
            '''"dukkhā": "@dukkha", ''',
            '''"jano": "@jana", "janassa": "@jana", "aṅgo": "@anga3", "aṅga": "@anga3", "aṅgaṃ": "@anga3",
    "aṅgānaṃ": "@anga3", "aṅgā": "@anga3",''',
            '''"dhammo": ("သဘောတရား", "တရား"), ''',
            '''    "samāpatti": ("ဈာန် ဝင်စားခြင်း", "သမာပတ်"), ''',
            '''    "parinibbuto": ("ပရိနိဗ္ဗာန် ပြုပြီးသော", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သော"),\n''',
            '''"antarikā": "@antarika3", ''',
            '''    "nirodho": ("ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"), "nirodhaṃ": ("ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"),\n''',
            ''', "maggaṃ": ("မဂ်", "လမ်း"), "magga": ("မဂ်", "လမ်း"), "maggo": ("မဂ်", "လမ်း")''',
            ]:
    rep(old, "    " if old.startswith("    samāpatti") or old.startswith('    "samāpatti') else "")
# keep the indentation of the lines that lost their first entry
s = s.replace('''    "bhāvo": ("သဘော", NONE), \n''', '''    "bhāvo": ("သဘော", NONE),\n''')
rep('''    "bhāvitā": ("ပွားများထားသော", "ပွားများပြီးသော", "ပွားများသော"), "yugaṃ"''', '''    "yugaṃ"''')
rep('''    "bhāvito": ("ပွားများပြီးသော", "ပွားများထားသော", "ပွားများသော"), "saṃvattaniko"''', '''    "saṃvattaniko"''')
rep('''    # antarikā: jhānantarikā «ဈာန်တို့အကြား ကာလ» (ch26), else the module's «ကြားအပိုင်း»
    "antarika3": lambda kw, pali, my: "အကြား ကာလ" if "အကြား ကာလ" in my else R.FUNCS["antarika"](kw, pali, my),
    # aṅga: the member of bojjhaṅga «ဗောဇ္ဈင်» (one Burmese word: the other member, pi-2) = (no direct equivalent) where
    # the FIRST aṅga compound of the Pāli is bojjhaṅga; else «အင်္ဂါ» (maggaṅga «မဂ်၏ အင်္ဂါ» …)
    "anga3": lambda kw, pali, my: NONE if (R.first_compound(R.strip_brackets(pali), [(r"[a-zāīūṃṅñṭḍṇḷ]*bojjhaṅg", "B"),
        (r"[a-zāīūṃṅñṭḍṇḷ]+aṅg", "A"), ("aṅg", "A")]) == "B" and "ဗောဇ္ဈင်" in my) else (
        "အင်္ဂါ" if "အင်္ဂါ" in my else "@prior"),
''', '''    # (phase 3: antarika3, anga3, jana, dhatu_plane moved to the module as @antarika, @anga, @jana, @dhatu_plane)
''')
rep('''    # jano / janassa of puthujjana: the one Burmese word «ပုထုဇဉ်» goes to puthu (pi-2: one word, one member)
    "jana": lambda kw, pali, my: NONE if "puthujjan" in pali.lower() and "ပုထုဇဉ်" in my else "@prior",
''', '')
rep('''    # dhātū before «ti» (kāma- / rūpa- / arūpadhātūti): the plane «ဘုံ», else the element «ဓာတ်»
    "dhatu_plane": lambda kw, pali, my: "ဘုံ" if "ဘုံ" in my and re.search(r"(kāma|rūpa)dhāt", pali) else (
        "ဓာတ်" if "ဓာတ်" in my else "@prior"),
''', '')
# the Mapper: negatives and the Pāli order are the module's now (S3 / G1-G3 book-wide)
i = s.index("NEG = (\"na\", \"no\")")
j = s.index("    def _lookup(self, ch, sid, kw, pali, my):")
s = s[:i] + '''class Mapper(R.Mapper):
    """the module's Mapper (phase 3: G1 / G2 pali_order and G3 negate are in the module); this group adds G4 and the
    ch1-table fallback to the chain."""

''' + s[j:]
rep("    def _lookup(self, ch, sid, kw, pali, my):", "    def _chain(self, ch, sid, kw, pali, my):")
rep("        return super().lookup(ch, sid, kw, pali, my)\n\n\ndef mapper", "        return super()._chain(ch, sid, kw, pali, my)\n\n\ndef mapper")
rep("Imports the shared module map5_rules.py (phase 1; NOT edited here)", "Imports the shared module map5_rules.py (phase 1; phase 3 moved this group's module overrides into it)")
p.write_text(s, encoding="utf-8")
print("ok")
