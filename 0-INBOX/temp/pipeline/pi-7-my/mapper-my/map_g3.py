"""pi-7 Burmese keyword mapping, PHASE 2, group g3: the part-3 gocchakas 3-01 … 3-08.

Uses the shared module map7_rules.py (imported; phase 2 used md5 909bed2528b27eb55051c73f3ce28f81). Holds only the
chapter tables and the context functions of this group. Writes <ch>.mapped.md for the eight chapters and prints, per
chapter, the three checks of the phase-1 brief (keyword preservation, presence, punctuation), the (no direct
equivalent) count and the S1 (stem fallback) review counts. Notes: notes-g3.md.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g3.py

Phase 3 (2026-11-26): the module overrides and the book-wide group values moved into map7_rules.py (BOOK, the module
fixes 1-9); this script keeps only what is local to the group. phase3-changes.tsv lists every value that changed.
"""
import sys
import pathlib
import collections

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

CHAPTERS = ["3-01-hetugocchaka", "3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka",
            "3-05-ganthagocchaka", "3-06-oghayogagocchaka", "3-07-nivaranagocchaka", "3-08-paramasagocchaka"]

# G1 (the gocchaka item is the bare noun N, its no-X «N မဟုတ်သော») is the module's cluster_cands since phase 3.


# ---------------------------------------------------------------------------------------------------------------------
# Group table (every chapter of g3): keywords the module leaves unmapped, and module values that are wrong here.
# A tuple = the first value the segment has (alt); a plain value is final (checked by the verifier).
# ---------------------------------------------------------------------------------------------------------------------
_SAR = "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု"
_ISA = "ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်း"
T_G3 = {
    # module overrides (notes-g3 «Module overrides»)
    # S1 corrections (stem values checked by eye)
    "assādanā": "သာယာ နှစ်သက်ခြင်း",                     # the noun «(… သာယာ နှစ်သက်ခြင်း မရှိ)»; stem verb «သာယာ»
    # keywords the module leaves unmapped: the text's phrase in dictionary form
    "pavatteyeva": "ဘဝ ဖြစ်စဉ်",                        # «ဘဝ ဖြစ်စဉ်၌ပင်» (rule 1 «၌», rule 9 eva «ပင်»)
    "vajjetabbā": "ဖယ်ရှားရမည့်", 
    "ninnetabbaṃ": "ထည့်သွင်းရမည့်", "parivattetabbā": "လှည့်ပြောင်းရမည့်",
    "jānitvā": "သိ၍",                                   # «… သိ၍ ပြုရမည်» (pi-1: absolutives keep «၍»)
    "vibhajantena": "ခွဲခြမ်းစိတ်ဖြာလျက်",                # the text's adverbial, as FRAME anumajjantena (H10)
    "agge": "ရှေ့ဆုံး",                                 # «… ရှေ့ဆုံးတွင် ပြုရမည်» (rule 1: «တွင်» goes)
    "nahetucittasamaṅgissa": "အမြစ် မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ",   # T12 «X-cittasamaṅgissa»
    "Dvikkhattuṃ": "နှစ်ကြိမ်", "catukkhattuṃ": "လေးကြိမ်", "ubhopete": "ထိုနှစ်ပါးလုံး",
    # -sadisa notes (T5: «…နှင့် တူသည်»; the adverbial «…နှင့် တူအောင်» before «ပြုရမည်»)
    "paṭhamadukasadisaṃ": "ပထမ နှစ်မျိုးတွဲနှင့် တူသည်",
    "ganthadukasadisaṃ": "အထုံး နှစ်မျိုးတွဲနှင့် တူသည်",
    "parāmāsadukasadisaṃ": "မှားယွင်းသော ယူဆမှု နှစ်မျိုးတွဲနှင့် တူသည်",
    # the named saññojanas and ganthas (the text's «X နှောင်ကြိုး / X … ကိုယ် အထုံး»; rule 1: «များ / ကို / တို့အား» go)
    "kāmarāgasaññojanaṃ": "ကာမရာဂ နှောင်ကြိုး",
    "diṭṭhisaññojanaṃ": "အယူ နှောင်ကြိုး", "diṭṭhisaññojanassa": "အယူ နှောင်ကြိုး",
    "avijjāsaññojanaṃ": "အမှန်ကို မသိမှု နှောင်ကြိုး", "avijjāsaññojanassa": "အမှန်ကို မသိမှု နှောင်ကြိုး",
    "vicikicchāsaññojanaṃ": "ယုံမှားမှု နှောင်ကြိုး", "mānasaññojanaṃ": "မာန နှောင်ကြိုး",
    "sīlabbataparāmāsasaññojanaṃ": f"{_SAR} နှောင်ကြိုး",
    "saññojanasampayuttakā": "နှောင်ကြိုးနှင့် ယှဉ်တွဲသော",   # T13 X-sampayutta
    "idaṃsaccābhinivesaṃ": _ISA, "idaṃsaccābhiniveso": _ISA,  # «…ခြင်းဟူသော ကိုယ် အထုံး» (kāyaganthaṃ its own keyword)
    "idaṃsaccābhinivesakāyaganthaṃ": f"{_ISA}ဟူသော ကိုယ် အထုံး",   # as pi-1 abhijjhākāyagantho «…ခြင်းဟူသော ကိုယ် အထုံး»
    "noganthādhipati": "အထုံး မဟုတ်သော အကြီးအမှူး",           # T12 «X-adhipati»
}
# per-segment overrides (sid -> {kw: value}): a keyword of ONE segment
CTX = {
    # «(Ārammaṇañca sahajātañca upanissayañca … parivattetabbaṃ)» «(အာရုံဟူသော အကြောင်းကိုလည်းကောင်း …)»: the
    # condition name (T1, R1: «ကိုလည်းကောင်း» goes); the module's bare «အာရုံ» is only part of it
    "7-28-116": {"Ārammaṇañca": "အာရုံဟူသော အကြောင်း"},
}


def tables():
    # phase 3: the G1 item values (item_table) are the module's cluster_cands (the coordinator's book-wide decision)
    return {ch: dict(T_G3) for ch in CHAPTERS}


def mapper():
    return R.Mapper(chapter_tables=tables(), ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def base_mapper():
    """the module alone (as the phase-1 dry run): for the S1 review and the override counts."""
    return R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def pairs(lines):
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            yield sid, k, v


def main():
    M, B = mapper(), base_mapper()
    tot = collections.Counter()
    s1 = collections.Counter()
    over = collections.Counter()
    newly = collections.Counter()
    for ch in CHAPTERS:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        blines, _, bun, _ = B.map_chapter(ch)
        bsrc = dict(B.SRC)
        bun = set(bun)
        for (sid, k, v), (_, _, bv) in zip(pairs(lines), pairs(blines)):
            if (sid, k) in bun:
                newly[ch] += 1
            elif bsrc.get((sid, k)) == "stem":
                s1["kept" if v == bv else "corrected"] += 1
            elif v != bv:
                over[(k, bv, v)] += 1
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, nde=nne, fails=len(fails), unmapped=len(unmapped), ruled=len(ruled))
    print("total", dict(tot))
    print("S1 stem uses: kept", s1["kept"], "corrected", s1["corrected"])
    print("newly mapped uses", sum(newly.values()), dict(newly))
    print("module values overridden (uses)", sum(over.values()), "in", len(over), "keyword / value pairs")
    if "--over" in sys.argv:
        for (k, bv, v), c in sorted(over.items(), key=lambda x: (R.low(x[0][0]), x[0][1], x[0][2])):
            print(f"   {k}: {bv} -> {v} ({c})")


if __name__ == "__main__":
    main()
