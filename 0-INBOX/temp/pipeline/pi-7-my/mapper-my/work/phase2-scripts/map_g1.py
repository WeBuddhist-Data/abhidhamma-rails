"""pi-7 Burmese keyword mapping, PHASE 2, group g1: 1-01-kusalattika, 1-03-vipakattika, 1-04-upadinnattika,
1-05-sankilitthattika.

Imports the shared module map7_rules.py (never edited here). This file holds only the g1 chapter tables, the g1
per-segment overrides and one g1 context function. Writes <ch>.mapped.md for the four chapters and prints the three
checks of the phase-1 brief per chapter (keyword preservation `bad`, presence failures, «, » / «၊» / « / » in a value),
the (no direct equivalent) count, the unmapped keywords and every stem-fallback (S1) use.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g1.py [--diff]
"""
import sys
import re
import pathlib
import collections

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map7_rules as R          # noqa: E402

G1 = ["1-01-kusalattika", "1-03-vipakattika", "1-04-upadinnattika", "1-05-sankilitthattika"]

_NAYAPAYA_N = "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်"   # nevasaññānāsaññāyatana (my7 terms)
_VINNANANCA = "အဆုံး မရှိသော သိစိတ် နယ်ပယ်"                                          # viññāṇañcāyatana (my7 terms)
_KIRIYA = "ပြုရုံမျှသာ ဖြစ်သော"          # kiriya (module STOCK kiriyaṃ; the text's head noun «စိတ်» is its addition, A5)
_ABY = "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော"                                     # abyākata (rule 6: no «၊»)

# ---------------------------------------------------------------------------------------------------------------------
# 1. keywords the module leaves unmapped (the text's phrase, dictionary form)
# ---------------------------------------------------------------------------------------------------------------------
NEW = {
    # sa-X heading part (T4, as phase-1 Saindriya / Sādhipati): «Sahetādhipati-indriyaghaṭanā» «အမြစ်ဟူသော အကြောင်း၊
    # အကြီးအမှူးဟူသော အကြောင်းနှင့် စွမ်းရည်ဟူသော အကြောင်း ပါဝင်သော ပေါင်းစပ်ချက်»
    "Sahetādhipati": "အမြစ်ဟူသော အကြောင်း အကြီးအမှူးဟူသော အကြောင်း … ပါဝင်သော",
    # the dvandva in a heading names both conditions (T4); the inner «နှင့်» stays (rule 1)
    "vigatāvigatapaccayā": "ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းနှင့် မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း",
    # notes: the text's adverbials (as phase-1 asammuyhantena «မရောထွေးစေဘဲ»)
    "sajjhāyantena": "သရဇ္ဈာယ်လျက်",
    "asammohantena": "မရောထွေးစေဘဲ", "Asammohantena": "မရောထွေးစေဘဲ",
    # «nakamme gaṇite» «… ကို ရေတွက်သောအခါ»: a locative absolute = the attributive, «အခါ» goes (pi-5 niruddhe
    # «ချုပ်ငြိမ်းသွားသော»)
    "gaṇite": "ရေတွက်သော",
    # «(imāni tīṇi mūlāni ekasadisāni)» «(… တူညီကြသည်)»: rule 4, the plural «ကြ» by the ending rule (T5 -sadisā)
    "ekasadisāni": "တူညီသည်",
    # «gaṇanā gambhīrā sukhumatarā ca» «ရေတွက်ချက်သည် နက်နဲ၍ ပို၍ သိမ်မွေ့သည်»: the comparative «ပို၍» is -tara
    "sukhumatarā": "ပို၍ သိမ်မွေ့သည်",
    # «(Cakkaṃ bandhitabbaṃ.)» «(စက်ဝိုင်း ဖွဲ့ရမည်။)»: rule 3 gerundive
    "bandhitabbaṃ": "ဖွဲ့ရမည့်",
    # «Paṭṭhānapāḷi paṭhamo bhāgo niṭṭhito» «… ပထမ အပိုင်း ပြီးဆုံးပြီ» (my7 terms «(Paṭhamo bhāgo) = (ပထမ အပိုင်း)»)
    "bhāgo": "အပိုင်း",
    # the arūpa-sphere compounds: my7 terms for the sphere + the head (rule 1: «အား» / «သည်» go; kiriya as A5)
    "viññāṇañcāyatanavipākassa": f"{_VINNANANCA} ကံ၏ အကျိုး",
    "viññāṇañcāyatanakiriyassa": f"{_VINNANANCA} {_KIRIYA}",
    "nevasaññānāsaññāyatanakusalaṃ": f"{_NAYAPAYA_N} ကုသိုလ်",
    "nevasaññānāsaññāyatanakusalassa": f"{_NAYAPAYA_N} ကုသိုလ်",
    "nevasaññānāsaññāyatanakiriyaṃ": f"{_NAYAPAYA_N} {_KIRIYA}",
    # «cetopariyañāṇena vipākābyākatakiriyābyākatacittasamaṅgissa cittaṃ jānāti» (pi-6 R8 / T12 -cittasamaṅgissa;
    # rule 6: the «၊» between the two qualifiers goes)
    "vipākābyākatakiriyābyākatacittasamaṅgissa": f"ကံ၏ အကျိုး ဖြစ်သော {_ABY} {_KIRIYA} {_ABY} စိတ်နှင့် ပြည့်စုံသူ",
    # «anuppannaṃ kiriyasamāpattiṃ uppādeti» «မဖြစ်ပေါ်သေးသော ပြုရုံမျှသာ ဖြစ်သော သမာပတ်ကို ဖြစ်စေသည်»
    "kiriyasamāpattiṃ": f"{_KIRIYA} သမာပတ်",
    "Dibbasotadhātu": "နတ်နား ဓာတ်",                   # notes-ch1-01 dibbasotadhātu (pi-5 sotadhātuyā «နား ဓာတ်»)
    "Utu": "ရာသီဥတု", "utu": "ရာသီဥတု",                # notes-ch1-01 utu; module SAMUTTHANA utu
    # the four paṭisambhidā and ṭhānāṭhānakosalla (notes-ch1-01; rule 1: «အား» goes)
    "atthappaṭisambhidāya": "အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်",
    "dhammappaṭisambhidāya": "တရားကို ပိုင်းခြားသိသော ဉာဏ်",
    "niruttippaṭisambhidāya": "စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်",
    "paṭibhānappaṭisambhidāya": "ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်",
    # 1-01 «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း», 1-03 … 1-05 «ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော
    # အကြောင်း၌ ကျွမ်းကျင်မှု» (text inconsistency; the segment's own form)
    "ṭhānāṭhānakosallassa": ("ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း",
                             "ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု"),
    # «niyatamicchādiṭṭhiyā» «ကျိန်းသေသော မှားယွင်းသော အယူအား» (notes-ch1-01; rule 1)
    "niyatamicchādiṭṭhiyā": "ကျိန်းသေသော မှားယွင်းသော အယူ",
    # «tassa paṭighātatthāya» «ထိုအမှုကို ချေဖျက်ရန်» (tassa is not a keyword of these segments)
    "paṭighātatthāya": "ချေဖျက်ရန်",
    # «pubbe suciṇṇāni»: 1-01 «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့» (module FRAME, A5), 1-03 … 1-05 «ကောင်းစွာ
    # ပြုခဲ့ဖူးသည်တို့» (rule 1: «တို့ကို» goes; text inconsistency)
    "suciṇṇāni": ("ကောင်းစွာ ကျင့်ခဲ့ဖူးသော", "ကောင်းစွာ ပြုခဲ့ဖူးသည်"),
}

# ---------------------------------------------------------------------------------------------------------------------
# 2. module overrides (a module value that is wrong in these chapters; for phase 3)
# ---------------------------------------------------------------------------------------------------------------------
OVERRIDE = {
    # module term family gives «ကျိန်းသေသော» (only the first member)
    "niyatamicchādiṭṭhi": "ကျိန်းသေသော မှားယွင်းသော အယူ",
    # module «စိတ်သည်» (the supplied head noun of vipāko, not the keyword); rule 1: «ဖြင့်» goes
    "tadārammaṇatā": ("ထိုအာရုံကို အာရုံပြုသည့် အနေ", "ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်"),
    # module «ထိုးထွင်း၍ ရှုကြသည်» / «ဖြစ်စေကြသည်»: the plural «ကြ» goes (rule 4, as vipassati, abhinandanti,
    # paccavekkhanti); uppādenti also got the pi-5 «ဖြစ်ပေါ်စေသည်», which stands in ^7-2-423 only for jappeti
    "vipassanti": "ထိုးထွင်း၍ ရှုသည်",
    "uppādenti": "ဖြစ်စေသည်",
    # module «… ရမည်»: rule 3 gerundive «…ရမည့်», as the module's vitthāretabbaṃ / gaṇetabbaṃ
    "vitthāretabbāni": "အကျယ် ချဲ့ရမည့်",
    "gaṇetabbā": "ရေတွက်ရမည့်", "gaṇetabbāti": "ရေတွက်ရမည့်",
    # module «နက်» (part of the word): «နက်နဲ၍ ပို၍ သိမ်မွေ့သည်», two predicates with one ending, the bare verb (U1)
    "gambhīrā": "နက်နဲ",
    # module «စက်»: «(Cakkaṃ bandhitabbaṃ.)» «(စက်ဝိုင်း ဖွဲ့ရမည်။)»
    "Cakkaṃ": "စက်ဝိုင်း",
    # module pi-2 «ကုသိုလ် သဘောတရား»: «kusale khandhe» «ကုသိုလ် အစုအဝေး», «kusale niruddhe» «ကုသိုလ်
    # ချုပ်ငြိမ်းသောအခါ»; the «သဘောတရား» of the segment belongs to dhammo / dhammaṃ
    "kusale": "ကုသိုလ်",
    # module «တည်သော»: «nahetuyā ṭhitena» «… မဟုတ်ခြင်း၌ တည်၍» (the text's adverbial, as -antena)
    "ṭhitena": "တည်၍",
    # module cond family «ကံ၏ အကျိုး» (the bare condition name): «Vipākañca nevavipāka…dhammañca dhammaṃ paṭicca»
    # «ကံ၏ အကျိုး ဖြစ်သော သဘောတရားနှင့် …» is the triad term (R1: vipākaṃ, module STOCK)
    "Vipākañca": "ကံ၏ အကျိုး ဖြစ်သော",
    # module FRAME f_natthi «မရှိသည်» in the headings «Natthi-vigatapaccayā / -vigatadukāni / -vigatāvigatapaccayā»
    # «မရှိခြင်းဟူသော အကြောင်း …» and the note «(Natthi-vigataṃ …)» «(မရှိခြင်း၊ …)»: a hyphen-compound part takes
    # the case of the compound (T4)
    "Natthi": "@g1_natthi",
}

COMMON = dict(NEW)
COMMON.update(OVERRIDE)
TABLES = {ch: dict(COMMON) for ch in G1}

# per-segment overrides (sid -> {kw: value})
CTX = {
    # module pi-2 «ကျင့်ကြံဆဲသူ၏»: rule 1, the «၏» goes («ကျင့်ကြံဆဲသူတို့သည် …», «ကျင့်ကြံဆဲသူတို့၏ …»)
    "7-2-423": {"sekkhā": "ကျင့်ကြံဆဲသူ"},
    # module «ကြောင့်»: «(Ekekaṃ paccayaṃ mūlakaṃ kātūna …)» «(အကြောင်း တစ်ခုစီကို အခြေခံ ပြု၍ …)»
    "7-2-85": {"paccayaṃ": "အကြောင်း"},
}


def f_g1_natthi(kw, pali, my):
    """Natthi as a hyphen-compound part (T4): in a heading the condition name «မရှိခြင်းဟူသော အကြောင်း», in a note
    the bare name «မရှိခြင်း» («(Natthi-vigataṃ anantarasadisaṃ …)» «(မရှိခြင်း၊ ပျောက်ကွယ်ခြင်းသည် …)»); else the
    module's f_natthi."""
    if re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + "-", pali):
        cands = [R.cname("natthi")] if pali.lstrip().startswith("#") else [R.N["natthi"]]
        v = R.pick_phrase(cands, my)
        if v is not None:
            return v
    return R.f_natthi(kw, pali, my)


FUNCS = {"g1_natthi": f_g1_natthi}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS, stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))


def run(write=True):
    M = mapper()
    out = {}
    for ch in G1:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        out[ch] = (lines, problems, unmapped, nne)
        if write:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return M, out


def compare_prior():
    """uses whose value differs from every pi-1 … pi-6 value of the same keyword (or of its base form, R1)."""
    diffs = collections.defaultdict(collections.Counter)
    for ch in G1:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if pv and v not in pv:
                    diffs[(k, v)][pv.most_common(1)[0][0]] += 1
    return diffs


def main():
    M, out = run()
    for ch in G1:
        lines, problems, unmapped, nne = out[ch]
        n, bad, fails, punct, ruled = R.verify_file(ch)
        stem = [(sid, k) for (sid, k), s in M.SRC.items() if s == "stem" and any(l.startswith(f"[{sid}] ") for l in lines)]
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)} stem {len(stem)}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        for sid, k in sorted(stem):
            print(f"   STEM ^{sid} {k}")
    if "--diff" in sys.argv:
        for (k, v), c in sorted(compare_prior().items(), key=lambda x: -sum(x[1].values())):
            print(f"   DIFF {k} = {v}   prior {dict(c)}")


if __name__ == "__main__":
    main()
