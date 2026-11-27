"""phase 3: classify every keyword of work/scan-after.tsv (more than one value) as aligned / kept, with its rule.
writes work/scan-class.tsv: keyword, n values, kind, why kept, values."""
import sys, re, pathlib
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
import map7_rules as R

WHY = {
    "anulomaṃ": ("sense", "the order «အဟုတ်ပြ ပုံစံ» or the mind moment «လျော်ညီခြင်း စိတ်» (phase 1 §B, harmonise H1)"),
    "rūpaṃ": ("sense", "matter «ရုပ်» or the visible object «အဆင်းအရောင်» (f_rupam, phase 1 §B)"),
    "assādeti": ("construction", "U1: the bare «သာယာ» where the text joins «သာယာ နှစ်သက်သည်» with one ending, «သာယာသည်» where it has that"),
    "katvā": ("construction", "U2: (no direct equivalent) after an act compound, «ပြု၍» elsewhere (f_karoti)"),
    "kātabbā": ("sense", "«ပြုရမည့်» (do) / «ထည့်ရမည့်» (include: «paṭisandhi kātabbā», 1-03) (phase 1 §A 8)"),
    "dukkhaṃ": ("sense", "bodily pain «နာကျင်မှု» / suffering «ဆင်းရဲ» («pariyiṭṭhimūlakaṃ dukkhaṃ», g2 CTX ^7-11-54)"),
    "ekāgārikaṃ": ("construction", "U2: the whole act «… ဝိုင်း၍ တိုက်သည်», the bare noun where …pe… cuts the verb off"),
    "gāmaghātaṃ": ("construction", "U2 (coordinator): the whole act, the bare «ရွာ» before …pe…"),
    "uposathakammaṃ": ("construction", "U2 (coordinator, g2): the whole act; the text's noun «ဥပုသ် စောင့်ထိန်းခြင်း» before …pe…; the bare «ဥပုသ်» where the text has only that"),
    "natthi": ("grammar / sense", "the condition «မရှိခြင်း» in a ghaṭanā list, the name «… ဟူသော အကြောင်း» as a heading part (T4), the verb «မရှိသည်» / «မရှိ» (module f_natthi, coordinator)"),
    "nevavipākanavipākadhammadhammo": ("grammar", "rule 5: «… သဘောတရား» where the keyword's own -dhammo is the noun; the qualifier alone where a separate dhammo keyword follows (tikaduka «X nahetu dhammo»)"),
    "niruddhe": ("text", "the text has «ချုပ်ငြိမ်းသောအခါ» (1-01, 2-05) and «ချုပ်ငြိမ်းသွားသောအခါ» (1-03 … 3-09); §A"),
    "paripuṇṇaṃ": ("grammar", "fix 9 «ပြည့်စုံသော»; the text's adverb «ပြည့်စုံစွာ» where it has only that («(paripuṇṇaṃ nava)» «(ပြည့်စုံစွာ ကိုးခု)»)"),
    "pavattipaṭisandhi": ("text", "two text forms «ဘဝ ဖြစ်စဉ်» / «ဘဝ ဖြစ်ဆဲ ကာလ» (§A)"),
    "sahajātaṃ": ("grammar", "the kind of a condition «အတူ ပေါ်ပေါက်ခြင်း» in a list, the adjective «အတူ ပေါ်ပေါက်သော» in «sahajātaṃ kāmupādānanti» (^7-U409)"),
    "suciṇṇāni": ("text", "two text forms «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော» / «ကောင်းစွာ ပြုခဲ့ဖူးသော» (§A)"),
    "tadārammaṇatā": ("text", "fix 3: one value per text form (1-01 / 2-05 «… အာရုံပြုသည့် အနေ», 1-03 … «… အာရုံပြုသော အဖြစ်»); §A"),
    "ṭhānāṭhānakosallassa": ("text", "two text forms (§A)"),
    "saññojanādidukāni": ("text", "the headings differ: 4-17 «နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်», 5-xx «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ» (§A)"),
    "vibhajantena": ("text / grammar", "the text has the adverbial «ခွဲခြမ်းစိတ်ဖြာလျက်» (3-05) and the agent noun «ခွဲခြမ်းစိတ်ဖြာသူသည်» (3-10); each segment's form (§A)"),
    "hetudukaṃ": ("sense", "the condition dyad «အမြစ်ဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ» (counting headings of parts 1-4) / the gocchaka dyad «အမြစ် နှစ်မျိုးတွဲ» (3-01, parts 4-5)"),
    "vipāka": ("grammar", "T4: the bare name in a ghaṭanā list, the name «… ဟူသော အကြောင်း» in a heading"),
    "vipākassa": ("sense", "the noun «ကံ၏ အကျိုး» after «kammaṃ» (f_vipakassa), the triad adjective before dhammassa"),
    "vipākaṃ": ("sense", "the triad adjective / the noun (phase 1 §B)"),
    "vipāke": ("sense", "the counting locative (condition), the noun, the adjective of «vipāke … khandhe» (g4 CTX)"),
    "vipāko": ("sense", "the adjective / the noun of «vipāko natthi» «ကံ၏ အကျိုး မရှိ»"),
    "atthi": ("grammar", "the condition (T4), the verb «ရှိသည်» of a note (g2 CTX ^7-10-112), the name in a heading"),
    "pahātabbahetukādhipati": ("construction", "rule 10: «ပယ်ရမည့် အမြစ် ရှိသည် … အကြီးအမှူး» where nadassanena's negative stands inside (g4)"),
    "nīvaraṇasampayuttañca": ("construction", "R7 «လည်း» gap"),
}


def kind(k, vals):
    if k in WHY:
        return WHY[k]
    vs = [v for v, _ in vals]
    if all("နှင့် တူ" in v for v in vs):
        return ("text shape", "-sadisa note: «…နှင့် တူသည် / တူအောင် / တူသည့်အတိုင်း», each segment's form (coordinator)")
    flat = {v.replace(" … ", " ") for v in vs}
    if len(flat) == 1:
        return ("construction", "R7 / rule 10: the « … » gap at the «လည်း» of ca / ceva inside one value")
    if R.cond_parse(k) or R.split_neg(k)[0]:
        return ("grammar", "T1-T4: the condition by its frame (the ablative «…ကြောင့်», the name «…ဟူသော အကြောင်း» in a "
                           "heading / note / counting locative, the bare name in a ghaṭanā list or hyphen compound)")
    return ("?", "?")


rows, unk = [], []
for l in (D / "work/scan-after.tsv").read_text(encoding="utf-8").splitlines():
    k, n, rest = l.split("\t")
    vals = [(m.group(1), m.group(2)) for m in re.finditer(r"(.+?) \((\d+); [^)]*\)(?: \| |$)", rest)]
    kd, why = kind(k, vals)
    if kd == "?":
        unk.append(k)
    rows.append((k, n, kd, why, rest))
(D / "work/scan-class.tsv").write_text("keyword\tvalues\tkind\twhy kept\tvalues (uses; chapters)\n" +
                                       "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
import collections
print(len(rows), collections.Counter(r[2] for r in rows))
print("unclassified", unk)
