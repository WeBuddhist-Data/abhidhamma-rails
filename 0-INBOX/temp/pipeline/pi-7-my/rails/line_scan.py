"""Per-line scan of the rails families (stricter than the per-segment adherence check; model pi-6-my/rails/line_scan.py,
read only): a Burmese line whose Pāli line holds the family's Pāli form must not keep the zero-shot form the family
replaces (forbid), must hold the termbase form (req) where the family states one, or must hold it as many times as the
Pāli form occurs (eq). A family may name a Pāli «unless» regex: lines matching it are not scanned for it. Variant
readings in square brackets stay Pāli and are not counted.
pi-7: L01 … L10 and R01 … R03 are the rails changes (the loose adherence test cannot see L02, L08, L09 cut forms and
R01: their old form holds the term's chunks); the «§A … / chosen departure» families are «req» proofs that the
decided items and the approved choices hold on every line.
usage: line_scan.py <pali dir> <burmese dir> [--stats]   (one line per failure; nothing = clean; --stats: Pāli hits)"""
import pathlib
import re
import sys
import unicodedata

pd, md = map(pathlib.Path, sys.argv[1:3])
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
W = r"[\wāīūṃṅñṭḍṇḷ]"
B0, B1 = r"(?<!" + W + ")", r"(?!" + W + ")"
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None)
    # ---- the rails changes
    ("L01 avasesa = «ကြွင်းကျန်…» (each occurrence)", r"(?i)avases", r"ကြွင်းကျန်", "eq", None),
    ("L01 avasesa (old «ကြွင်းသော / ကြွင်းသည်»)", r"(?i)avases", r"ကြွင်းသ", "forbid", None),
    ("L02 nānākaraṇa / ninnāna / nānaṃ = «ကွဲပြားမှု»", r"(?i)nānākaraṇ|ninnān|" + B0 + r"nānaṃ", r"ကွဲပြားမှု", "req", None),
    ("L02 nānākaraṇa (old «ကွဲပြားချက်»)", r"(?i)nānākaraṇ|ninnān|" + B0 + r"nānaṃ", r"ကွဲပြားချက်", "forbid", None),
    ("L02 ninnāna (old «ကွဲပြားခြင်း», kept only for nānattaṃ)", r"(?i)ninnān|" + B0 + r"nānaṃ", r"ကွဲပြားခြင်း", "forbid",
     r"(?i)nānatt"),
    ("L02 no «ကွဲပြားချက်» anywhere", r".", r"ကွဲပြားချက်", "forbid", None),
    ("L03 §A15 suciṇṇāni = «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု» (each)", r"(?i)suciṇṇ", r"ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု", "eq", None),
    ("L03 suciṇṇāni (old «ကောင်းစွာ ပြုခဲ့ဖူးသည်»)", r"(?i)suciṇṇ", r"ပြုခဲ့ဖူး", "forbid", None),
    ("L04 §A16 tadārammaṇatā = «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်»", r"(?i)tadārammaṇatā", r"ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်",
     "eq", None),
    ("L04 §A35 niruddhe = «ချုပ်ငြိမ်းသွားသော»", B0 + r"niruddhe" + B1, r"ချုပ်ငြိမ်းသွားသော", "eq", None),
    ("L04 niruddhe (old «ချုပ်ငြိမ်းသောအခါ»)", B0 + r"niruddhe" + B1, r"ချုပ်ငြိမ်းသောအခါ", "forbid", None),
    ("L05 §A37 vibhajantena = «ခွဲခြမ်းစိတ်ဖြာလျက်»", r"vibhajantena", r"ခွဲခြမ်းစိတ်ဖြာလျက်", "eq", None),
    ("L06 §A14 ṭhānāṭhānakosalla = «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း»", r"(?i)ṭhānāṭhānakosall",
     r"ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း", "eq", None),
    ("L07 §A19 pavatti = «ဘဝ ဖြစ်စဉ်»", r"(?i)pavatt", r"ဘဝ ဖြစ်စဉ်", "req", None),
    ("L07 pavatti (old «ဘဝ ဖြစ်ဆဲ ကာလ»)", r"(?i)pavatt", r"ဖြစ်ဆဲ ကာလ", "forbid", None),
    ("L08 nillopaṃ = «လုယက်ပစ္စည်း» (each)", r"(?i)nillop", r"လုယက်ပစ္စည်း", "eq", None),
    ("L08 nillopaṃ (old «ဥစ္စာကို လုယူ / ဥစ္စာကို…»)", r"(?i)nillop", r"ဥစ္စာကို(?: လုယူ|…)", "forbid", None),
    ("L09 §A8 uposatha(kamma) = «ဥပုသ်(ကို) စောင့်ထိန်း…» (each, also cut by …pe…)", r"(?i)uposatha",
     r"ဥပုသ်(?:ကို)? စောင့်ထိန်း", "eq", None),
    ("L09 §A8 ekāgārikaṃ = «အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်…» (each)", r"(?i)ekāgārik",
     r"အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်", "eq", None),
    ("L09 §A8 gāmaghātaṃ = «ရွာကို ဖျက်ဆီး၍ လုယက်…» (each)", r"(?i)gāmaghāt", r"ရွာကို ဖျက်ဆီး၍ လုယက်", "eq", None),
    ("L09 §A8 nigamaghātaṃ = «နိဂုံးကို ဖျက်ဆီး၍ လုယက်…» (each)", r"(?i)nigamaghāt", r"နိဂုံးကို ဖျက်ဆီး၍ လုယက်", "eq", None),
    ("L10 §A18 uppannaṃ samāpajj- = «ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စား…» (each)", B0 + r"uppannaṃ samāpajj",
     r"ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စား", "eq", None),
    ("L10 uppannaṃ samāpajj- (old nominalised «ဖြစ်ပေါ်ပြီးသည်ကို»)", B0 + r"uppannaṃ samāpajj", r"ဖြစ်ပေါ်ပြီးသည်ကို",
     "forbid", None),
    ("L10 uppannaṃ utu(ṃ) = «ဖြစ်ပေါ်ပြီးသော ရာသီဥတု» (each)", r"(?i)" + B0 + r"uppannaṃ utu", r"ဖြစ်ပေါ်ပြီးသော ရာသီဥတု", "eq", None),
    ("L10 no nominalised «ဖြစ်ပေါ်ပြီးသည်ကို» anywhere", r".", r"ဖြစ်ပေါ်ပြီးသည်ကို", "forbid", None),
    ("R01 §A36 saññojanādidukāni = «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ»", r"(?i)saññojanādiduk",
     r"နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ", "eq", None),
    ("R02 / R03 §A4 «yathā [W] X-sadisaṃ» = «… Xနှင့် တူသည့်အတိုင်း» (each)", r"(?i)yathā (?:\S+ )?\S*sadisaṃ",
     r"နှင့် တူသည့်အတိုင်း", "eq", None),
    # ---- §A items the termbase decides (map-harmonise §A; termbase notes-part5 5e), proved on every line
    ("§A1 samanantarā (adverb) = «ကောင်းစွာ ချက်ချင်း နောက်»", B0 + r"samanantarā" + B1, r"ကောင်းစွာ ချက်ချင်း နောက်", "req",
     None),
    ("§A2 paccavekkh- = «ပြန်လည် ဆင်ခြင်»", r"(?i)paccavekkh", r"ပြန်လည် ဆင်ခြင်", "req", None),
    ("§A3 kusalākusal- = «ကုသိုလ်နှင့် အကုသိုလ်» (the three-term heading compound Kusalākusalābyākata- is a list)",
     r"(?i)kusalākusal", r"ကုသိုလ်နှင့် အကုသိုလ်", "req", r"(?i)kusalākusalābyākat"),
    ("§A13 aniccato = «မမြဲဟု»", r"(?i)aniccato", r"မမြဲဟု", "req", None),
    ("§A22 passitvā = «ကြည့်၍»", r"(?i)passitvā", r"ကြည့်၍", "req", None),
    ("§A27 nānākkhaṇika = «ခဏ ကွဲပြား…» (the kamma label, kept apart from nānākaraṇa)", r"(?i)nānāk?khaṇik",
     r"ခဏ ကွဲပြား", "req", None),
    ("§A33 nevadassanena = «သစ္စာကို မြင်ခြင်း…»", r"(?i)nevadassanena", r"သစ္စာကို မြင်ခြင်း", "req", None),
    ("§A35 / §A16 the 1-03 frame (tadārammaṇatā with vipāko)", r"(?i)vipāko tadārammaṇatā",
     r"ကံ၏ အကျိုး ဖြစ်သော စိတ်သည် ထိုအာရုံကိုပင်", "req", None),
    # ---- chosen departures and key choices (termbase APPROVED.md)
    ("jappeti = «ဖြစ်ပေါ်စေ…» (kept apart from uppādeti)", r"(?i)jappeti", r"ဖြစ်ပေါ်စေ", "req", None),
    ("paccavekkhati (verb) = «ပြန်လည် ဆင်ခြင်…»", r"(?i)paccavekkhat|paccavekkhant", r"ပြန်လည် ဆင်ခြင်", "req", None),
]
BR = re.compile(r"\[[^\]]*\]")
STATS = {f[0]: 0 for f in FAM}
for p in sorted(pd.glob("*.md")):
    pl = [N(l) for l in p.read_text(encoding="utf-8-sig").splitlines()]
    ml = [N(l) for l in (md / p.name).read_text(encoding="utf-8").splitlines()]
    for k, (a, b) in enumerate(zip(pl, ml), 1):
        a2, b2 = BR.sub("", a), BR.sub("", b)
        for fam, prx, brx, mode, unless in FAM:
            hits = len(re.findall(prx, a2))
            if not hits or (unless and re.search(unless, a2)):
                continue
            STATS[fam] += hits if prx != "." else 1
            found = re.findall(brx, b2)
            if (mode == "forbid" and found) or (mode == "req" and not found) or (mode == "eq" and len(found) != hits):
                print(f"{p.name}:{k}\t{fam}\t{mode}\t{(found or [''])[0]}" + (f"\t{len(found)}/{hits}" if mode == "eq" else ""))
if "--stats" in sys.argv:
    for f, n in STATS.items():
        print(f"stats\t{n}\t{f}")
