"""Per-line scan of the rails families (stricter than the per-segment adherence check; model pi-5-my/rails/line_scan.py,
read only): a Burmese line whose Pāli line holds the family's Pāli form must not keep the zero-shot form the family
replaces (forbid), must hold the termbase form (req) where the family states one, or must hold it as many times as the
Pāli form occurs (eq). A family may name a Pāli «unless» regex: lines matching it are not scanned for it. Variant
readings in square brackets stay Pāli and are not counted.
pi-6: the termbase was built from this zero-shot's keyword map, so most families are «req» proofs that the locked
decisions hold on every line (the §A items the termbase decides, the chosen departures, the answer register); L01 is
the one rails change (§A1).
usage: line_scan.py <pali dir> <burmese dir> [--stats]   (one line per failure; nothing = clean; --stats: Pāli hits)"""
import pathlib
import re
import sys
import unicodedata

pd, md = map(pathlib.Path, sys.argv[1:3])
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None)
    # ---- the rails change
    ("L01 §A1 yassa cittassa anantarā = «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (each occurrence)", r"(?i)yassa cittassa anantarā",
     r"အကြင်စိတ်၏ ချက်ချင်း နောက်၌", "eq", None),
    ("L01 §A1 yassa cittassa anantarā (old «မိမိ စိတ်၏»)", r"(?i)yassa cittassa anantarā", r"မိမိ", "forbid", None),
    # ---- §A items the termbase decides (map-harmonise §A; termbase notes-part5 5d), proved on every line
    ("§A2 / review fix B2 kāmāvacarānaṃ pacchimacittaṃ uppajjissati = «နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ကာမဘုံ၌ ရှိသူတို့» (the "
     "beings, sense 1; fix-brief.md B2 replaces the adjective «ကာမဘုံနှင့် ဆိုင်သော» here)",
     r"(?i)kāmāvacarānaṃ pacchimacittaṃ", r"နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ကာမဘုံ၌ ရှိသူတို့", "eq", None),
    ("review fix B2 kāmāvacarānaṃ pacchimacittaṃ (old adjective «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်»)",
     r"(?i)kāmāvacarānaṃ pacchimacittaṃ", r"ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်", "forbid", None),
    ("§A2 / review fix C2 Kāmāvacarānaṃ pacchimacittassa = «ကာမဘုံ၌ ရှိသူတို့၏ နောက်ဆုံး စိတ်၏» (the beings, sense 1; "
     "genitive before the moment)",
     r"(?i)kāmāvacarānaṃ pacchimacittassa", r"ကာမဘုံ၌ ရှိသူတို့၏ နောက်ဆုံး စိတ်၏", "eq", None),
    ("§A8 aggaphalassa = «အမြတ်ဆုံး ဖိုလ်»", r"(?i)aggaphalassa", r"အမြတ်ဆုံး ဖိုလ်", "req", None),
    ("§A9 sadisa = «…နှင့် တူညီ…» (no «တူညီအောင်» without kātabbaṃ)", r"(?i)sadis", r"တူညီအောင်", "forbid", r"kātabb"),
    ("§A9 sadisa = «တူညီ…» («Xနှင့် တူညီသည်»; «Xလည်း Yလည်း တူညီသည်»; adverb «တူညီစွာ»)", r"(?i)sadis", r"တူညီ", "req", None),
    ("§A11 uppādakkhaṇe = «ဖြစ်ခြင်း ခဏ» (the moment)", r"(?i)uppādakkhaṇ", r"ဖြစ်ခြင်း ခဏ", "req", None),
    ("§A11 uppādakkhaṇe (not «ဖြစ်ပေါ်ခြင်း ခဏ»)", r"(?i)uppādakkhaṇ", r"ဖြစ်ပေါ်ခြင်း ခဏ", "forbid", None),
    ("§A11 Uppādavāro / Uppajjanavāro = «ဖြစ်ပေါ်ခြင်းအလိုက်» (the vāra name)", r"(?i)uppādavār|uppajjanavār",
     r"ဖြစ်ပေါ်ခြင်း", "req", None),
    ("§A12 kāyasaṅkhāra = «ကိုယ်၏ ပြုပြင်ဖန်တီးမှု»", r"(?i)kāyasaṅkhār", r"ကိုယ်၏ ပြုပြင်ဖန်တီးမှု", "req", None),
    ("§A12 kāyasaṅkhāra (not «ကိုယ် ပြုပြင်ဖန်တီးမှု»)", r"(?i)kāyasaṅkhār", r"ကိုယ် ပြုပြင်ဖန်တီး", "forbid", None),
    ("§A13 sacchikaroti joined «မျက်မှောက်ပြု…» (no spaced positive)", r"(?i)sacchikar|sacchākāsi",
     r"မျက်မှောက် ပြု", "forbid", None),
    ("§A13 sacchikaroti: the negative stays spaced «မျက်မှောက် မပြု…»", r"(?i)sacchikar|sacchākāsi", r"မျက်မှောက်မပြု",
     "forbid", None),
    ("atītānāgata = «အတိတ် … အနာဂတ်» (pi-5 locked; spelled out with cittaṃ)", r"(?i)atītānāgat", r"အတိတ်.*အနာဂတ်",
     "req", None),
    # ---- chosen departures and senses (termbase APPROVED.md)
    ("yattha = «အကြင်နေရာ»", r"(?<![a-zā-ṃ])[Yy]attha(?![a-zā-ṃ])", r"အကြင်နေရာ", "req", None),
    ("uppajjamāna = «ဖြစ်ပေါ်ဆဲ»", r"(?i)uppajjamān", r"ဖြစ်ပေါ်ဆဲ", "req", None),
    ("nirujjhamāna = «ချုပ်ငြိမ်းဆဲ»", r"(?i)nirujjhamān", r"ချုပ်ငြိမ်းဆဲ", "req", None),
    ("nirujjhissati / -anti = future «ချုပ်ငြိမ်း(ကြ)လိမ့်မည် / …မည့်»", r"(?i)nirujjhiss",
     r"ချုပ်ငြိမ်း(?:ကြ)?(?:လိမ့်မည်|မည့်)", "req", None),
    ("uppajjissati / -anti = future «ဖြစ်ပေါ်(ကြ)လိမ့်မည် / …မည့်»", r"(?i)(?<!a)uppajjiss|upapajjissati",
     r"ဖြစ်ပေါ်(?:ကြ)?(?:လိမ့်မည်|မည့်)", "req", None),
    ("avasesa = «ကြွင်းကျန်သော»", r"(?i)avases", r"ကြွင်းကျန်", "req", None),
    ("anuloma = «အဟုတ်ပြ ပုံစံ»", r"(?i)anulom", r"အဟုတ်ပြ", "req", None),
    ("paccanīka = «အငြင်းပြ ပုံစံ»", r"(?i)paccanīk", r"အငြင်းပြ", "req", r"(?i)paccanīkaokās"),
    ("rūpadhātuṃ (ch. 7, the plane) = «သိမ်မွေ့သော ရုပ်ဘုံ»", r"rūpadhātuṃ", r"သိမ်မွေ့သော ရုပ်ဘုံ", "req", None),
    # ---- the answer register (APPROVED.md: Natthi «မရှိပါ။», Āmantā «ဟုတ်ပါသည်။»)
    ("answer Āmantā = «ဟုတ်ပါသည်။» / «ဟုတ်ပါသည်( )…။» (each)", r"Āmantā", r"ဟုတ်ပါသည်(?: ?…)?။", "eq", None),
    ("answer Natthi = «မရှိပါ။»", r"(?<![a-zā-ṃ])Natthi\.", r"မရှိပါ။", "req", None),
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
            STATS[fam] += hits
            found = re.findall(brx, b2)
            if (mode == "forbid" and found) or (mode == "req" and not found) or (mode == "eq" and len(found) != hits):
                print(f"{p.name}:{k}\t{fam}\t{mode}\t{(found or [''])[0]}" + (f"\t{len(found)}/{hits}" if mode == "eq" else ""))
if "--stats" in sys.argv:
    for f, n in STATS.items():
        print(f"stats\t{n}\t{f}")
