"""phase 3 edit 4: map_ch2-15.py — overrides now in the module go; S1 / S3 are the module's (stem=, negate)."""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "map_ch2-15.py"
s = p.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)


rep('''    "aṅgo": NONE, "pahīnaṃ": "ပယ်ပြီးသော", "janassa": NONE, ''', '''    "pahīnaṃ": "ပယ်ပြီးသော", ''')
rep('''    "thero": "မထေရ်", "Sāriputto thero"''', '''    "Sāriputto thero"''')
rep('''    "aññā": "သိ၍", "attho"''', '''    "attho"''')
rep('''"sukhadukkhaṃ": ("ချမ်းသာနှင့် ဆင်းရဲ", "ချမ်းသာ ဆင်းရဲ"),''', '')
rep('''    "aṅgo": NONE, "kopaṭṭhāniyo"''', '''    "kopaṭṭhāniyo"''')
rep(''', "nirodhadhammaṃ": ("ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော", "ချုပ်ငြိမ်းခြင်း သဘော ရှိသော"),''', ',')
rep(''' "aññā": ("ရဟန္တာ ဖိုလ်",),''', '')
rep('''"gatā": "အာရုံပြုသော", "aṅgo": NONE, ''', '''"gatā": "အာရုံပြုသော", ''')
rep('''"atthaṅgamāya": "ချုပ်ငြိမ်းရန်", "aṅga": NONE, ''', '''"atthaṅgamāya": "ချုပ်ငြိမ်းရန်", ''')
rep(''', "parinibbute": "ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော",''', ',')
rep(''', "parinibbuto": "ပရိနိဗ္ဗာန် ပြုတော်မူသော",''', ',')
rep('''"pahīno": "ပယ်ပြီးသော", "aṅga": "@anga", ''', '''"pahīno": "ပယ်ပြီးသော", ''')
rep('''    "maggo bhāvito": ("မဂ်ကို ပွားများပြီးသော", "မဂ် … ပွားများပြီးသော"), "bojjhaṅgā bhāvitā": ("ဗောဇ္ဈင်တို့ကို ပွားများပြီးသော", "ဗောဇ္ဈင် … ပွားများပြီးသော"),''', '''    # (phase 3: maggo bhāvito / bojjhaṅgā bhāvitā glue «Xကို ပွားများပြီး ဖြစ်» in the module, mechanic 3)''')
# the glue mechanic (mechanic 2) makes the CTX of ^5-239 unnecessary
rep('''    # «Parihāyati arahā» against «ရဟန္တာ၏ ဆုတ်ယုတ်ခြင်း» (parihāni) of the same segment: the proposition's own words
    "5-239": {"Parihāyati arahā": "ရဟန္တာ … ဆုတ်ယုတ်သည်"},
''', '''    # (phase 3: ^5-239 «Parihāyati arahā» no longer glued through «ရဟန္တာ၏ ဆုတ်ယုတ်ခြင်း»: module glue, mechanic 2)
''')
# S3: the module negates (negate); no automatic @neg entries
rep('''        for _, kws in R.keyword_rows(ch):
            for k in kws:
                ws = [R.low(w) for w in k.split()]
                if len(ws) > 2 and ("na" in ws or "no" in ws) or len(ws) == 2 and ws[1] in ("na", "no"):
                    d.setdefault(k, "@neg")
''', '')
rep('''        v = R.pi_get(kw, my)[0] or stem_value(kw, my)''', '''        v = R.pi_get(kw, my)[0] or (MM["m"].stem(kw, my) if " " not in kw else None)''')
i = s.index("_POOL = {}")
j = s.index("def mapper():")
s = s[:i] + '''def stem_tables():
    """the tables of the S1 stem pool (module make_stem): ch1, the module, this group's."""
    return [C1.T_CH1, R.FRAME, R.STOCK, T_GROUP] + [T[c] for c in CHAPTERS]


_Mapper = R.Mapper


''' + s[j:]
rep('''    MM["m"] = _Mapper(chapter_tables=tables(ch1=False), ctx=CTX, funcs=FUNCS2)
    return _Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS2)''', '''    stem = R.make_stem(stem_tables())
    MM["m"] = _Mapper(chapter_tables=tables(ch1=False), ctx=CTX, funcs=FUNCS2, stem=stem)
    M = _Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS2, stem=stem)
    _map = M.map_chapter

    def map_chapter(ch):
        CUR["ch"] = ch
        return _map(ch)
    M.map_chapter = map_chapter
    return M''')
rep("Imports the shared module map5_rules.py (phase 1; NOT edited here).", "Imports the shared module map5_rules.py (phase 1; phase 3 moved this group's module overrides, S1 and S3 into it).")
p.write_text(s, encoding="utf-8")
print("ok")
