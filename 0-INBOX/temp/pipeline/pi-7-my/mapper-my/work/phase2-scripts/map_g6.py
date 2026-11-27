"""pi-7 Burmese keyword mapping, PHASE 2, group g6: part 5 (5-01-anuloma-tikatika … 5-20-paccaniyanuloma-dukaduka).

Imports the shared module map7_rules.py (never edited: md5 909bed2528b27eb55051c73f3ce28f81) and holds only the g6
chapter tables, the per-segment overrides and the new g6 context functions. Writes <ch>.mapped.md for the 20
chapters, in chapter order, and prints the three verify checks of the phase-1 brief per chapter (keyword
preservation `bad`, presence failures, «, » / «၊» / « / » in a value) with the (no direct equivalent) count.
Deterministic: no clock, no randomness, sorted / ordered iteration only; a second run gives byte-identical files.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g6.py
"""
import sys
import pathlib
import hashlib
import collections

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

G6 = ["5-01-anuloma-tikatika", "5-02-anuloma-dukaduka", "5-03-paccaniya-tika", "5-04-paccaniya-duka",
      "5-05-paccaniya-dukatika", "5-06-paccaniya-tikaduka", "5-07-paccaniya-tikatika", "5-08-paccaniya-dukaduka",
      "5-09-anulomapaccaniya-tika", "5-10-anulomapaccaniya-duka", "5-11-anulomapaccaniya-dukatika",
      "5-12-anulomapaccaniya-tikaduka", "5-13-anulomapaccaniya-tikatika", "5-14-anulomapaccaniya-dukaduka",
      "5-15-paccaniyanuloma-tika", "5-16-paccaniyanuloma-duka", "5-17-paccaniyanuloma-dukatika",
      "5-18-paccaniyanuloma-tikaduka", "5-19-paccaniyanuloma-tikatika", "5-20-paccaniyanuloma-dukaduka"]

_M = {}          # the mapper in use (the context functions below look up a keyword's inner term with it)


# ---------------------------------------------------------------------------------------------------------------------
# new g6 context functions
# ---------------------------------------------------------------------------------------------------------------------
def _inner(kw, pali, my):
    """the value the mapper gives another keyword form in this segment (no cache, no SRC entry)."""
    try:
        return R.finish(_M["m"]._lookup(_M["ch"], "__g6inner__", kw, pali, my))
    except KeyError:
        return None
    finally:
        _M["m"].SRC.pop(("__g6inner__", kw), None)


def f_nana(kw, pali, my):
    """G6-1 (T8 applied twice): na + a no-X / na-X term of part 5 (nanoāsavo, nanosaññojanañca, nanaaraṇo …) = the na-X
    form of the inner term's value in THIS segment: inner «X မဟုတ်သော» -> «X မဟုတ်သည် မဟုတ်သော» (the text's «… မဟုတ်သည်
    မဟုတ်သော», harmonise H21). The R1 ca / ñca forms go through their base form first; an inner value with a « … » gap
    is not used (the gapped T8 candidate «N ဖြစ်သော … မဟုတ်» is the module slip of G6-3)."""
    w = R.low(kw)
    for b in R.base_forms(w) + [w]:
        if not b.startswith("na") or len(b) < 6:
            continue
        v = _inner(b[2:], pali, my)
        if v in (None, R.NONE) or " … " in v:
            continue
        c = R.pick_phrase(R.neg_term(v), my)
        if c is not None:
            return c
    return "@prior"


def f_r1(kw, pali, my):
    """G6-2 (pi-6 R1, enforced): a «-ñca / -ñceva / -ca / -pi» keyword = the value of its base form in the same segment
    (the module reaches the term family of the «ñca» form before the base form's pi-1 … pi-6 value: Āsavañca «စိတ်
    အစွန်းအထင်း ဖြစ်သော» against Āsavaṃ «စိတ်အစွန်းအထင်း» in one segment)."""
    for b in R.base_forms(kw):
        v = _inner(b, pali, my)
        if v is not None:
            return v
    return "@prior"


FUNCS = {"nana": f_nana, "r1": f_r1}

# ---------------------------------------------------------------------------------------------------------------------
# group table (every g6 chapter): keywords the module leaves unmapped, or maps wrongly, in part 5
# ---------------------------------------------------------------------------------------------------------------------
NA_ABY = "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော"
COMMON = {
    # the dassanena triad: «သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊ ဘာဝနာ ပွားများခြင်းဖြင့်လည်း ပယ်ရမည်
    # မဟုတ်သော»: neva + dassanena = the noun (pi-1 / pi-2 dassanena) with the negative of its member, as the module's
    # nabhāvanāya «ဘာဝနာ ပွားများခြင်း … မဟုတ်သော» (T8); the first member ends at the list comma «မဟုတ်၊»
    "nevadassanena": "သစ္စာကို မြင်ခြင်း … မဟုတ်",
    # titles and heading parts (rule 7 / R6: whole, rule 1: the plural «များ» goes)
    "Kusalattikasanidassanattikaṃ": "ကုသိုလ် သုံးမျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ",
    "saññojanādidukāni": "နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ",
    "Saññojanādiduka": "နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ",
    "sahetukādidukāni": "အမြစ် ရှိခြင်း စသည်တို့၏ နှစ်မျိုးတွဲ",
    "hetvādidukāni": "အမြစ် စသည်တို့၏ နှစ်မျိုးတွဲ",
    "saññojanādigocchakāni": "နှောင်ကြိုး စသည်တို့၏ အစု",
    "saññojanādigocchakaṃ": "နှောင်ကြိုး စသည်တို့၏ အစု",
    "Hetusahetukadukādi": "အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ စသည်",
    "Anulomadukatikapaṭṭhānato": "အဟုတ်ပြ ပုံစံ … နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ",
    # -sadisa notes (T5 «…နှင့် တူသည်»); where the text adds the head noun «သဘောတရား» it is gapped (phase-1 §A5)
    "Sappaccayadukasadisaṃ": "အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်",
    "lokiyadukasadisaṃ": "လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်",
    "sappaccayasadisaṃ": ("အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်", "အကြောင်း ရှိသော … နှင့် တူသည်"),
    "atītasadisaṃ": "အတိတ် … နှင့် တူသည်",
    # the mūla notes of 5-11: «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို အခြေခံခြင်း» (the added head
    # noun gapped, phase-1 §A5; the «လည်း» of the abyākata term stays, R7)
    "Abyākatamūlaṃ": NA_ABY + " … အခြေခံခြင်း",
    "Abyākatamūle": NA_ABY + " … အခြေခံခြင်း",
    "paccayavasena": "အကြောင်းအလိုက်",
    # na-X / no-X terms of part 5 the module leaves unmapped (T8)
    "nocittasaṃsaṭṭhasamuṭṭhānasahabhuṃ": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော",
    "nocittasaṃsaṭṭhasamuṭṭhānasahabhū": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော",
    "Narūpiṃ": "ရုပ် မဟုတ်သော",
    "nanoāsavo": "@nana", "nanoāsavaṃ": "@nana", "nanoāsavañca": "@nana",
    "nanosaññojanaṃ": "@nana", "nanosaññojanañca": "@nana", "nanoganthañca": "@nana",
    "nanoupādā": "@nana", "nanaaraṇo": "@nana",
    # module overrides (G6-3): the gapped T8 candidate «N ဖြစ်သော … မဟုတ်» / «မှီ၍ … မဟုတ်သော» where the text has the
    # plain na-X form «N မဟုတ်သော» (noupādā: upādā pi-2 «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော», na-X rule T8)
    "noupādā": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော",
    "noyogaṃ": "ထမ်းပိုး မဟုတ်သော",
    "noāsavañca": "စိတ်အစွန်းအထင်း မဟုတ်သော",
    # module overrides (G6-2, R1): the «ñca» form takes its base form's value in the segment
    "āsavañca": "@r1", "sekkhañca": "@r1",
    # «nanakenaci viññeyyaṃ» «တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သည် မဟုတ်သော»: kenaci = pi-2 «တစ်စုံတစ်ခုသော
    # စိတ်» (rule 1: «ဖြင့်» goes), the two negatives after viññeyyaṃ's «သိနိုင်» (rule 10 gap)
    "nanakenaci": "တစ်စုံတစ်ခုသော စိတ် … မဟုတ်သည် မဟုတ်သော",
    # notes
    "āmasanaṃ": "ရည်ညွှန်းပုံ",
    "Paccanīyadukamattāni": "အငြင်းပြ ပုံစံ နှစ်မျိုးတွဲများသာ",
    "Ekapañhameva": "ပြဿနာ တစ်ခု",
    "Cittasamuṭṭhānarūpameva": "စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်",
    "chabbīsa": "နှစ်ဆယ့်ခြောက်ခု",
    "chabbīsati": "နှစ်ဆယ့်ခြောက်ခု",
    "Ete": "ဤတို့",
    "purimanayena": "ရှေ့နည်း",
    "ovattā": "ပြောင်းပြန် ဖြစ်သော",
}
# chapter-only entries
SPEC = {}
TABLES = {ch: dict(COMMON, **SPEC.get(ch, {})) for ch in G6}

# per-segment overrides (sid -> {kw: value}): a keyword of ONE segment
CTX = {
    # «na vattabbaṃ dhammaṃ» «ခေါ်ဆို၍ မရသော သဘောတရား»: na is not a keyword here, so vattabbaṃ carries the
    # negative (the pi-1 / pi-2 «ခေါ်ဆို၍ ရ» stands in the segment only by the negative infix, not as a phrase: U3)
    "7-58-56": {"vattabbaṃ": "ခေါ်ဆို၍ မရသော"},
    # «kusale khandhe» «ကုသိုလ် အစုအဝေးတို့» (module override G6-4: the pi-2 «ကုသိုလ် သဘောတရား» stands in the segment
    # only as the rendering of «Kusalañca … dhammaṃ», another phrase; rule 1 / one word per keyword)
    "7-63-4": {"kusale": "ကုသိုလ်"},
}


def mapper():
    M = R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS, stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
    _M["m"] = M
    return M


def map_chapter(M, ch):
    """M.map_chapter(ch) with the chapter known to the context functions (their inner lookups use its table)."""
    _M["ch"] = ch
    return M.map_chapter(ch)


def run(write=True):
    M = mapper()
    out = {}
    for ch in G6:
        lines, problems, unmapped, nne = map_chapter(M, ch)
        out[ch] = (lines, problems, unmapped, nne)
        if write:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return M, out


def main():
    M, out = run()
    tot = collections.Counter()
    for ch in G6:
        lines, problems, unmapped, nne = out[ch]
        n, bad, fails, punct, ruled = R.verify_file(ch)
        md5 = hashlib.md5((HERE / f"{ch}.mapped.md").read_bytes()).hexdigest()
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} md5 {md5}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, fails=len(fails), punct=len(punct), unmapped=len(unmapped), nde=nne,
                   bad=len(bad))
    src = collections.Counter((v or "?").split(":")[0] for (sid, k), v in M.SRC.items() if not sid.startswith("__"))
    print("total", dict(sorted(tot.items())))
    print("sources", src.most_common())


if __name__ == "__main__":
    main()
