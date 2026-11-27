"""pi-7 Burmese keyword mapping, PHASE 2, group g4: 3-09-mahantaraduka, 3-10-upadanagocchaka, 4-01-kilesagocchaka.

Imports the shared module map7_rules.py (never edits it) and holds only the chapter tables, the per-segment overrides
and the new context functions of this group (notes-g4.md gives the reasons). Writes <ch>.mapped.md for the three
chapters and prints the three checks of the phase-1 brief per chapter (keyword preservation, presence, punctuation),
the (no direct equivalent) count and the S1 stem-fallback uses that remain.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g4.py
"""
import sys
import pathlib

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

CHAPTERS = ["3-09-mahantaraduka", "3-10-upadanagocchaka", "4-01-kilesagocchaka"]
NONE = R.NONE

# ---- G1: «X-dukasadisa» «X နှစ်မျိုးတွဲနှင့် တူသည်» (T5 -sadisa; the text's «တူကြသည်» by the ending rule, its adverbial
# «…နှင့် တူအောင်» before «ပြုရမည်»): X = the dyad name of the text's own heading «X နှစ်မျိုးတွဲ» (T9 heading lexicon)
DUKA = {
    "cittasamuṭṭhāna": "စိတ်မှ ဖြစ်ပေါ်လာခြင်း",
    "cittasahabhū": "စိတ်နှင့်အတူ တည်ရှိခြင်း",
    "lokiya": "လောကနှင့် သက်ဆိုင်ခြင်း",
    "upādāna": "စွဲလမ်းမှု",
    "sappītika": "ပီတိ ရှိခြင်း",
    "arūpa": "ရုပ်မရှိသော ဘုံ",                       # the text's own name (notes-g4 §F item 3)
    "arūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း",
    "kilesa": "ကိလေသာ",
    "pahātabbahetuka": "ပယ်ရမည့် အမြစ်",               # «dassanena pahātabbahetukadukasadisā»: dassanena has its own value
}
# ---- G2: «X-gamanasadisa» / «dutiyavārasadisa»: the text's «ပထမ / ဒုတိယ သွားပုံ», «ဒုတိယ ဖော်ပြချက်» + «နှင့် တူသည်»
GAMANA = {"paṭhamagamana": "ပထမ သွားပုံ", "dutiyagamana": "ဒုတိယ သွားပုံ", "dutiyavāra": "ဒုတိယ ဖော်ပြချက်"}


def sadisa_entries():
    out = {}
    for x, v in list((k + "duka", d + " နှစ်မျိုးတွဲ") for k, d in DUKA.items()) + list(GAMANA.items()):
        for e in ("sadisaṃ", "sadisā", "sadiso"):
            out[x + e] = (v + "နှင့် တူသည်", v + "နှင့် တူအောင်")
    return out


# ---- G3: «diṭṭhigatavippayuttalobhasahagata-» in any case (T7: the generator's stacked qualifiers «A၊ B», the «၊»
# dropped by rule 6); -adhipati «X အကြီးအမှူး» (T12)
DLS = "အယူမှားနှင့် ကင်းကွာသော၊ လောဘနှင့်အတူ ဖြစ်သော"
DLS_KW = {"diṭṭhigatavippayuttalobhasahagat" + e: DLS for e in ("aṃ", "e", "ā", "ānaṃ", "o", "assa", "ena", "a")}
DLS_KW["diṭṭhigatavippayuttalobhasahagatādhipati"] = DLS + " အကြီးအမှူး"


def f_natthi_g4(kw, pali, my):
    """natthi (module f_natthi), except where the module's «မရှိသည်» stands in the segment only inside the term «…
    မရှိသည်လည်း မဟုတ်» (nevasaññānāsaññāyatana): then the note's own «မရှိ» (pi-5 Q5)."""
    v = R.f_natthi(kw, pali, my)
    if v == "မရှိသည်" and R.flat(my).count("မရှိသည်") == R.flat(my).count("မရှိသည်လည်း မဟုတ်"):
        return "မရှိ"
    return v


FUNCS = {"natthi_g4": f_natthi_g4}

# ---- the tables: one group table (G4) for the three chapters; a CTX entry only for a keyword of one segment
G4 = {
    **sadisa_entries(),
    **DLS_KW,
    # module overrides (notes-g4 §C)
    "pīti": "ပီတိ",                                   # the noun pīti «ပီတိ» (FRAME's pīti = pi + iti NONE)
    "natthi": "@natthi_g4",
    "ajjhattikassa": "အတွင်းပိုင်း",                     # the pi-2 «အတွင်း» stands only inside «အတွင်းပိုင်း»
    "noupādā": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော",   # T8 na-X of upādā (the module gave «မှီ၍ … မဟုတ်သော»)
    "kilesānañca": "ကိလေသာ",                          # the noun «ကိလေသာတို့အားလည်းကောင်း» (R1 / rule 1)
    "tadārammaṇatā": "ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်",   # rule 1: «ဖြင့်» goes (the module gave «စိတ်သည်»)
    "pañcaviññāṇaṃ": "သိစိတ် ငါးပါး",                 # pi-5 pañcaviññāṇā (the module gave «သိစိတ်»)
    "cakkaṃ": "စက်ဝိုင်း", "cakkā": "စက်ဝိုင်း",       # the text's «(စက်ဝိုင်း)» (the module gave «စက်»)
    "uppādenti": "ဖြစ်စေသည်",                         # LEXW uppādeti; the plural «ကြ» by the ending rule (rule 4)
    "vipassanti": "ထိုးထွင်း၍ ရှုသည်",                # LEXW vipassati, as uppādenti
    "gaṇetabbā": "ရေတွက်ရမည့်",                       # rule 3 (FRAME gaṇetabbaṃ); the text's «ရေတွက်ရမည်» by M7
    "vitthāretabbāni": "အကျယ် ချဲ့ရမည့်",             # rule 3 (FRAME vitthāretabbā)
    "paripuṇṇā": "ပြည့်စုံသည်",                       # the text's verb «ပြည့်စုံကြသည်» (rule 4; the module gave «ပြည့်စုံ»)
    "paccavekkhitvā": "ပြန်လည် ဆင်ခြင်၍",             # S1 corrected: U3, the pi-7 word of paccavekkhati + «၍»
    # newly mapped keywords (notes-g4 §B)
    "nti": NONE,                                      # the quotative «"vipāka"nti»: ti alone (rule 9)
    "upanissayā": "အားကြီးသော အမှီ",                  # «tīṇi upanissayā» the three kinds: the bare name (T1)
    "upādinnamūlake": "ကံကြောင့် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း",   # T6 X-mūlaka (rule 1: «၌» goes)
    "asammohantena": "မရောထွေးစေဘဲ",                  # = FRAME asammuyhantena (pi-4 P3 / A2)
    "cakkhusampadaṃ": "မျက်စိ ပြည့်စုံခြင်း", "vaṇṇasampadaṃ": "အဆင်းအရောင် ပြည့်စုံခြင်း",
    "gandhasampadaṃ": "အနံ့ ပြည့်စုံခြင်း", "rasasampadaṃ": "အရသာ ပြည့်စုံခြင်း",
    "ekasadisā": "တူညီသည်",                           # «tiṇṇampi ekasadisā» «သုံးခုလုံး တူညီကြသည်» (rule 4)
    "gamanā": "သွားပုံ",
    "garukārammaṇā": "လေးစားဖွယ်ရာ အာရုံ",            # «… အာရုံအဖြစ် ပြုရမည်» (rule 1)
    "iminākāreneva": "ဤ ပုံစံ",                       # R1 (eva «ပင်» goes); rule 1: «အတိုင်း» goes (vācanāmaggena)
    "kātabbāni": "ပြုရမည့်",                          # rule 3, as kātabbā
    "niyāmetabbaṃ": "သတ်မှတ်ရမည့်", "niyāmetabbā": "သတ်မှတ်ရမည့်",   # rule 3; the text's «…ရမည်» by M7
    "noupādācittasamaṅgissa": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ",   # T12 / pi-6 R8
    "pavattipaṭisandhi": "ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ",       # «ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း» (rule 1, R7 gap)
    "pavattipaṭisandhiyā": "ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ",
    "pavesetvā": "ထည့်သွင်း၍",                       # absolutive «…၍» (pi-1)
    "paṭhamasseva": "ပထမ",                            # R1; the text's head noun «ပြဿနာ» and «၌သာ» are not the keyword's
    "pūretukāmena": "ပြည့်စုံစေလိုသူ",                 # agent noun (pi-4 P6); rule 1: «သည်» goes
    "sabbaṭṭhāne": "နေရာ အားလုံး",                    # rule 1: «၌» goes
    "uddharitabbaṃ": "ထုတ်နုတ်ရမည့်", "uddharitabbo": "ထုတ်နုတ်ရမည့်",   # rule 3
    "viññāṇañcāyatanavipākassa": "အဆုံး မရှိသော သိစိတ် နယ်ပယ် ကံ၏ အကျိုး",   # rule 1: «အား» goes
    "ākāsānañcāyatanakusalaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ကုသိုလ်",
    "dassetabbo": "ပြသရမည့်",                         # rule 3
    "ninnānā": "ကွဲပြားမှု မရှိ",                      # the text's «ကွဲပြားမှု မရှိ» (FRAME ninnānākaraṇaṃ «ကွဲပြားချက် မရှိ»)
    "nānākaraṇaṃ": "ကွဲပြားချက်",                     # «… ကွဲပြားချက် ဖြစ်သည်» (rule 2)
    "vibhajantena": "ခွဲခြမ်းစိတ်ဖြာသူ",              # agent noun (pi-4 P6)
    "āmasanaṃ": "ရည်ညွှန်းပုံ", "āmasanā": "ရည်ညွှန်းပုံ",
    "anulomapaccayavāraṃ": "အဟုတ်ပြ ပုံစံ၏ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",   # T5 order + vāra
    "anulomapaṭiccavāro": "အဟုတ်ပြ ပုံစံ၏ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",
    "arūpamissake": "ရုပ် မဟုတ်သော သဘောတရားနှင့် ရောနှောသော",   # the text's head noun «အပိုင်း» is not the keyword's
    "dassanadukaṃ": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ",   # the text's dyad name (rule 7)
    "dutiyavāre": "ဒုတိယ ဖော်ပြချက်",                 # rule 1: «၌» goes
    "gāmaghātaṃ": ("ရွာကို ဖျက်ဆီး၍ လုယက်သည်", "ရွာ"),   # T11; the bare noun where «…pe…» cuts the verb off (as
                                                       # STOCK uposathakammaṃ)
    "likhitaṃ": "ရေးထားသော",                          # «heṭṭhā likhitaṃ lekhaṃ» «ရှေ့၌ ရေးထားသော စာ» (rule 3)
    "niyatamicchādiṭṭhiyā": "ကျိန်းသေသော မှားယွင်းသော အယူ",   # rule 1: «အား» goes
    "pahātabbabhājanakāraṇe": "ပယ်ရမည့် … သဘောတရားကို ခွဲခြားသည့် နည်းလမ်း",   # the na of nabhāvanāya in the gap
    "pahātabbahetukādhipati": ("ပယ်ရမည့် အမြစ် ရှိသော အကြီးအမှူး", "ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး"),   # T12
    "passitvā": "ကြည့်၍",                             # «anulomaṃ passitvā» «… ကို ကြည့်၍» (absolutive)
    "paṭhamaṃ": "ပထမ",                                # «paṭhamaṃ jhānaṃ / maggaṃ» «ပထမ ဈာန် / မဂ်»
    "paṭighātatthāya": "ချေဖျက်ရန်",                  # «tassa paṭighātatthāya» «ထိုအမှုကို ချေဖျက်ရန်»
    "pākatikā": "ပကတိ",                               # «… ပကတိအတိုင်း» (rule 1: «အတိုင်း» goes, as vācanāmaggena)
    "sakabhaṇḍe": "မိမိ ပစ္စည်း",                     # rule 1: «၌» goes
    "vicikicchāsahagatamohaṭṭhāne": "ယုံမှားမှုနှင့်အတူ ဖြစ်သော မောဟ၏ နေရာ",   # rule 1: «၌» goes
    "ṭhānāṭhānakosallassa": "ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း",   # rule 1: the final «အား» goes
}
T_309 = dict(G4)
T_310 = dict(G4)
T_401 = dict(G4)
TABLES = {"3-09-mahantaraduka": T_309, "3-10-upadanagocchaka": T_310, "4-01-kilesagocchaka": T_401}
CTX = {
    # «Tatiyo bhāgo niṭṭhito» «တတိယ အပိုင်း ပြီးဆုံးပြီ» (the module gave «သဘော»)
    "7-33-116": {"bhāgo": "အပိုင်း"},
    # «vipāke rūpāvacare khandhe» «ကံ၏ အကျိုး ဖြစ်သော … အစုအဝေး»: the attributive (rule 3, STOCK vipāko); the module's
    # plain-noun fallthrough gave «ကံ၏ အကျိုး»
    "7-35-232": {"vipāke": "ကံ၏ အကျိုး ဖြစ်သော"},
}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS,
                    stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW, G4]))


def main():
    M = mapper()
    for ch in CHAPTERS:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        stem = [kv for l in lines for kv in l[1:].split("] ", 1)[1].split(", ")
                if M.SRC.get((l[1:].split("] ", 1)[0], kv.split("=", 1)[0])) == "stem"]
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)} stem {len(stem)}")
        for x in unmapped[:20]:
            print("   UNMAPPED", x)
        for x in fails[:20]:
            print("   FAIL", x)
        for x in punct[:10]:
            print("   PUNCT", x)


if __name__ == "__main__":
    main()
