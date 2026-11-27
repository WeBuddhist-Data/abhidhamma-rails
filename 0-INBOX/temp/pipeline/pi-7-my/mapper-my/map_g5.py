"""pi-7 Burmese keyword mapping, PHASE 2, group g5: part 4 dukatika / tikaduka (4-02 … 4-21).

Imports the shared module map7_rules.py (never edited here); holds only the chapter tables and the per-segment
overrides of g5. Writes <ch>.mapped.md for the 20 chapters and runs the three checks of the phase-1 brief per chapter.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g5.py

Phase 3 (2026-11-26): the module overrides and the book-wide group values moved into map7_rules.py (BOOK, the module
fixes 1-9); this script keeps only what is local to the group. phase3-changes.tsv lists every value that changed.
"""
import sys
import pathlib

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

CHAPTERS = [
    "4-02-dukatika-hetuduka", "4-03-dukatika-sahetukaduka", "4-04-dukatika-sappaccayaduka",
    "4-05-dukatika-asavaduka", "4-06-dukatika-sannojanaduka", "4-07-dukatika-ganthaduka",
    "4-08-dukatika-nivaranaduka", "4-09-dukatika-paramasaduka", "4-10-dukatika-sarammanaduka",
    "4-11-dukatika-upadanaduka", "4-12-dukatika-kilesaduka", "4-13-dukatika-dassanenapahatabbaduka",
    "4-14-dukatika-saranaduka", "4-15-tikaduka-hetuduka", "4-16-tikaduka-sappaccayaduka",
    "4-17-tikaduka-asavaduka", "4-18-tikaduka-sarammanaduka", "4-19-tikaduka-kilesaduka",
    "4-20-tikaduka-dassanenapahatabbaduka", "4-21-tikaduka-sauttaraduka",
]

# ---- the text's phrases of the g5 -sadisa notes (G5-1): «<the dyad>(၏ <its term>) နှင့် တူသည်», the adverbial
# «…နှင့် တူအောင်» before «အကျယ် ချဲ့ရမည်» (module T5 / harmonise H19); the list comma «၊» of the abyākata term goes
# (rule 6); the text's own «သဘောတရား» inside the phrase stays (it stands inside the value, A5 drops only a final one)
_AB = "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား"
_KU = "ကုသိုလ် သဘောတရား"
_AK = "အကုသိုလ် သဘောတရား"
_LOKIYA = "လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ"


def _sad(x):
    """an X-sadisa note: the dictionary form «Xနှင့် တူသည်», else the text's adverbial «Xနှင့် တူအောင်» (alt)."""
    return (x + "နှင့် တူသည်", x + "နှင့် တူအောင်")


SADISA = {
    "lokiyadukaabyākatasadisaṃ": _sad(f"{_LOKIYA}၏ {_AB}"),
    "lokiyadukakusalasadisaṃ": _sad(f"{_LOKIYA}၏ {_KU}"),
    "lokiyalokuttaragamanasadisaṃ": _sad("လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း၏ သွားပုံ"),
    "cittasaṃsaṭṭhasamuṭṭhānadukaabyākatasadisaṃ": _sad(f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ၏ {_AB}"),
    "cittadukakusalasadisaṃ": _sad(f"စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ {_KU}"),
    "upādānadukaakusalasadisaṃ": _sad(f"စွဲလမ်းမှု နှစ်မျိုးတွဲ၏ {_AK}"),
    "kilesadukaakusalasadisaṃ": _sad(f"ကိလေသာ နှစ်မျိုးတွဲ၏ {_AK}"),
    "kāmāvacaradukaabyākatasadisaṃ": _sad(f"ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ {_AB}"),
}

# context functions of g5: none (the cluster items keep the module value: see notes-g5 «Unclear», U-g5-1)
FUNCS = {}

# group table (all g5 chapters): keywords the module leaves unmapped or maps wrongly in g5
GROUP = {
    **SADISA,
    # unmapped in the module (G5-2 … G5-6)
    "imamhi": "ဤ",                                     # «Imamhi dukatike» «ဤ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ၌»
    "ādimhi": "အစ",                                    # «(ādimhi tīṇi …)» «(အစ၌ သုံးခု …)» (rule 1: «၌» goes)
    "cetasikadukamūlā": "စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲကို အခြေခံသော",   # «… mūlā tīṇi gamanā» (rule 3)
    "saññojanādidukāni": "နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်",  # heading «Kusalattika-saññojanādidukāni» (T5 -ādi)
    # module overrides (G5-7 … G5-9)
}
# chapter tables: only what differs from GROUP in one chapter
TABLES = {ch: {} for ch in CHAPTERS}
# per-segment overrides (sid -> {kw: value}): the elliptic «(dassane ekaṃ, nadassane dve)» of 4-13 (G5-10): dassane
# takes the pi-1 / pi-2 / pi-3 value of dassanena «သစ္စာကို မြင်ခြင်း», as the module gives dassanena and nadassane /
# nadassanena «သစ္စာကို မြင်ခြင်း … မဟုတ်သော» in the same chapter (the module's «မြင်ခြင်း» is the pi-5 value of another
# kind of segment); the text's supplied «ဖြင့် ပယ်ရမည့် သဘောတရား၌» fills the Pāli ellipsis and has no keyword
CTX = {"7-47-6": {"dassane": "သစ္စာကို မြင်ခြင်း"}, "7-47-17": {"dassane": "သစ္စာကို မြင်ခြင်း"}}


def mapper():
    tabs = {ch: {**GROUP, **TABLES[ch]} for ch in CHAPTERS}
    return R.Mapper(chapter_tables=tabs, ctx=CTX, funcs=FUNCS,
                    stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def main():
    M = mapper()
    tot = {"lines": 0, "fails": 0, "punct": 0, "unmapped": 0, "nde": 0}
    for ch in CHAPTERS:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot["lines"] += n
        tot["fails"] += len(fails)
        tot["punct"] += len(punct)
        tot["unmapped"] += len(unmapped)
        tot["nde"] += nne
    print("TOTAL", tot)


if __name__ == "__main__":
    main()
