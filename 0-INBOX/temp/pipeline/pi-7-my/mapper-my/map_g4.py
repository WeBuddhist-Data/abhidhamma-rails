"""pi-7 Burmese keyword mapping, PHASE 2, group g4: 3-09-mahantaraduka, 3-10-upadanagocchaka, 4-01-kilesagocchaka.

Imports the shared module map7_rules.py (never edits it) and holds only the chapter tables, the per-segment overrides
and the new context functions of this group (notes-g4.md gives the reasons). Writes <ch>.mapped.md for the three
chapters and prints the three checks of the phase-1 brief per chapter (keyword preservation, presence, punctuation),
the (no direct equivalent) count and the S1 stem-fallback uses that remain.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g4.py

Phase 3 (2026-11-26): the module overrides and the book-wide group values moved into map7_rules.py (BOOK, the module
fixes 1-9); this script keeps only what is local to the group. phase3-changes.tsv lists every value that changed.
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


# ---- G3 (diṭṭhigatavippayuttalobhasahagata- in any case): in the module BOOK since phase 3


FUNCS = {}   # phase 3: G3 (f_natthi_g4) is in the module f_natthi

# ---- the tables: one group table (G4) for the three chapters; a CTX entry only for a keyword of one segment
G4 = {
    **sadisa_entries(),
    # module overrides (notes-g4 §C)
    # newly mapped keywords (notes-g4 §B)
    "nti": NONE,                                      # the quotative «"vipāka"nti»: ti alone (rule 9)
    # T6 X-mūlaka (rule 1: «၌» goes); phase 3 head-noun rule (coordinator): the supplied «သဘောတရားကို» is gapped
    "upādinnamūlake": "ကံကြောင့် ဖြစ်သော … အခြေခံခြင်း",
    "gamanā": "သွားပုံ",
    "iminākāreneva": "ဤ ပုံစံ",                       # R1 (eva «ပင်» goes); rule 1: «အတိုင်း» goes (vācanāmaggena)
    "noupādācittasamaṅgissa": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ",   # T12 / pi-6 R8
    "pavesetvā": "ထည့်သွင်း၍",                       # absolutive «…၍» (pi-1)
    "paṭhamasseva": "ပထမ",                            # R1; the text's head noun «ပြဿနာ» and «၌သာ» are not the keyword's
    "pūretukāmena": "ပြည့်စုံစေလိုသူ",                 # agent noun (pi-4 P6); rule 1: «သည်» goes
    "sabbaṭṭhāne": "နေရာ အားလုံး",                    # rule 1: «၌» goes
    "ākāsānañcāyatanakusalaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ကုသိုလ်",
    "ninnānā": "ကွဲပြားမှု မရှိ",                      # the text's «ကွဲပြားမှု မရှိ» (FRAME ninnānākaraṇaṃ «ကွဲပြားချက် မရှိ»)
    "nānākaraṇaṃ": "ကွဲပြားချက်",                     # «… ကွဲပြားချက် ဖြစ်သည်» (rule 2)
    "vibhajantena": "ခွဲခြမ်းစိတ်ဖြာသူ",              # agent noun (pi-4 P6)
    "anulomapaccayavāraṃ": "အဟုတ်ပြ ပုံစံ၏ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",   # T5 order + vāra
    "anulomapaṭiccavāro": "အဟုတ်ပြ ပုံစံ၏ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",
    # the text's head noun «အပိုင်း» is not the keyword's; the supplied «သဘောတရား» stays inside: a gap would start
    # the next chunk with the particle «နှင့်» (phase 3 head-noun rule, logged exception)
    "arūpamissake": "ရုပ် မဟုတ်သော သဘောတရားနှင့် ရောနှောသော",
    "dassanadukaṃ": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ",   # the text's dyad name (rule 7)
    "dutiyavāre": "ဒုတိယ ဖော်ပြချက်",                 # rule 1: «၌» goes
                                                       # STOCK uposathakammaṃ)
    "likhitaṃ": "ရေးထားသော",                          # «heṭṭhā likhitaṃ lekhaṃ» «ရှေ့၌ ရေးထားသော စာ» (rule 3)
    # the na of nabhāvanāya and the supplied «သဘောတရားကို» in the gap (phase 3 head-noun rule)
    "pahātabbabhājanakāraṇe": "ပယ်ရမည့် … ခွဲခြားသည့် နည်းလမ်း",
    "pahātabbahetukādhipati": ("ပယ်ရမည့် အမြစ် ရှိသော အကြီးအမှူး", "ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး"),   # T12
    "paṭhamaṃ": "ပထမ",                                # «paṭhamaṃ jhānaṃ / maggaṃ» «ပထမ ဈာန် / မဂ်»
    "pākatikā": "ပကတိ",                               # «… ပကတိအတိုင်း» (rule 1: «အတိုင်း» goes, as vācanāmaggena)
    "vicikicchāsahagatamohaṭṭhāne": "ယုံမှားမှုနှင့်အတူ ဖြစ်သော မောဟ၏ နေရာ",   # rule 1: «၌» goes
}
T_309 = dict(G4)
T_310 = dict(G4)
T_401 = dict(G4)
TABLES = {"3-09-mahantaraduka": T_309, "3-10-upadanagocchaka": T_310, "4-01-kilesagocchaka": T_401}
CTX = {
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
