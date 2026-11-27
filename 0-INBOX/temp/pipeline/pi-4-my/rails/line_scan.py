"""Per-line scan of the rails families (stricter than the per-segment adherence check; model pi-3-my/rails/line_scan.py
and pi-2-my/rails/line_scan.py): a Pāli line holding the family's Pāli form whose Burmese line has fewer termbase forms
than the Pāli has hits (req), or still has a wrong form (forbid). A family may name a Pāli «unless» regex: lines
matching it are not scanned for it. Variant readings in square brackets stay Pāli and are not counted.
The families are the layer families L01 … L25 (my_formulas_rails.py: the GENUINE differences and the logged text
inconsistencies H1 … H14 of mapper-my/map-harmonise-notes.md that the locked termbase decides), the bilingual-review
fixes (layer L26 / L27 = B2 / B4, apply_fixes.py F01 … F05) and the review items kept (KR: B3, B4's bhāsati lines,
B5), the kept items
(K: approved rails-step notes, the person-type names, the H items the termbase keeps), and the binding rules
(nāma-rūpa). The loose adherence test cannot see most of them (it strips «တို့» / «များ» and endings, and passes a
keyword when its chunk is anywhere in the segment).
usage: line_scan.py <pali dir> <burmese dir> [--stats]   (prints one line per failure; nothing = clean; --stats: Pāli hits per family)"""
import pathlib
import re
import sys
import unicodedata

pd, md = map(pathlib.Path, sys.argv[1:3])
STATS = {}
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
W = "a-zA-Zāīūṃṅñṭḍṇḷ"
B = rf"(?<![{W}])"          # Pāli word start
E = rf"(?![{W}])"           # Pāli word end
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None)
    ("L01 phale ṭhito = ဖိုလ်၌ တည်နေ (ṭhito|0, H10)", r"phale ṭhito", r"ဖိုလ်၌ တည်နေ", "req", None),
    ("L01 phale ṭhito (old «တည်သော»)", r"^", r"၌ တည်သောအခါ", "forbid", None),
    ("L02 maggasamaṅgino = မဂ်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ် (group NAME, H12)", r"maggasamaṅgino", r"မဂ်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ်",
     "req", None),
    ("L02 maggasamaṅgino (old «… ပြည့်စုံသူ Nယောက်»)", r"maggasamaṅgino", r"ပြည့်စုံသူ [^ ]+ယောက်", "forbid", None),
    ("L03 suṇāti / sutvā / suṇato = ကြား (H6)", rf"{B}(?:suṇāti|sutvā|suṇato){E}", r"ကြား", "req", None),
    ("L03 suṇāti family (old «ကြားရ၏» / «ကြားနာ»)", rf"{B}(?:suṇāti|sutvā|suṇato){E}", r"ကြားရ၏|ကြားနာ(?:၏|၍|သော)", "forbid",
     None),
    ("L04 desenti / desetabbo / dhammadesanā = ဟော, not ဟောကြား", r"{0}(?:desenti|desetabbo|dhammadesanā){1}".format(B, E),
     r"ဟောကြ၏|ဟောရမည်|ဟောခြင်း", "req", None),
    ("L04 desa- (old «ဟောကြားကြ၏ / ဟောကြားရမည် / ဟောကြားခြင်း»)", r"desenti|desetabbo|dhammadesanā",
     r"ဟောကြားကြ၏|ဟောကြားရမည်|ဟောကြားခြင်း", "forbid", None),
    ("L05 pakāsenti / pakāseti = ထင်ရှားပြ (H1)", rf"{B}pakāse(?:nti|ti){E}", r"ထင်ရှားပြ", "req", None),
    ("L05 pakāsenti (old «ထုတ်ဖော် ပြ»)", r"pakāsenti", r"ထုတ်ဖော် ပြ", "forbid", None),
    ("L06 dīgharattaṃ = ရှည်လျားသော ကာလပတ်လုံး (H4)", rf"{B}dīgharattaṃ{E}", r"ရှည်လျားသော ကာလပတ်လုံး", "req", None),
    ("L06 dīgharattaṃ without ciraṃ (old «ကြာမြင့်စွာ»)", rf"{B}dīgharattaṃ{E}", r"ကြာမြင့်စွာ", "forbid", rf"{B}ciraṃ"),
    ("L07 dubbaṇṇa = အဆင်း ဆိုး (H9)", r"dubbaṇṇ", r"အဆင်း ဆိုး", "req", None),
    ("L07 dubbaṇṇa (old «အဆင်း ညှိုး»)", r"^", r"အဆင်း ညှိုး", "forbid", None),
    ("L08 senāsana = အိပ်ရာ နေရာ (H2)", r"senāsana", r"အိပ်ရာ နေရာ", "req", None),
    ("L08 senāsana (old «ကျောင်းအိပ်ရာနေရာ»)", r"^", r"ကျောင်းအိပ်ရာနေရာ", "forbid", None),
    ("L09 purisapuggalo = ပုဂ္ဂိုလ် (old «လူ ပုဂ္ဂိုလ်»)", r"purisapuggalo", r"လူ ပုဂ္ဂိုလ်", "forbid", None),
    ("L10 bhogaṃ = စည်းစိမ်", rf"{B}bhogaṃ{E}", r"စည်းစိမ်", "req", None),
    ("L10 bhogaṃ (old «စည်းစိမ်ဥစ္စာ»)", r"^", r"စည်းစိမ်ဥစ္စာ", "forbid", None),
    ("L11 unnaḷo = ဘဝင် မြင့်, mukharo = စကား များ (spacing, H14)", rf"{B}(?:unnaḷo|mukharo){E}", r"ဘဝင် မြင့်|စကား များ",
     "req", None),
    ("L11 unnaḷo / mukharo (joined forms)", r"^", r"ဘဝင်မြင့်|စကားများ", "forbid", None),
    ("L11 vikiṇṇavāco = ရှုပ်ပွေစွာ စကားကို ပြော", r"vikiṇṇavāco", r"ရှုပ်ပွေစွာ စကားကို (?:မ)?ပြောသူ", "req", None),
    ("L11 vikiṇṇavāco (old «ပြောတတ်သူ»)", r"vikiṇṇavāco", r"ပြောတတ်သူ", "forbid", None),
    ("L12 abhisamayo = ထင်ထင်ရှားရှား … သိမြင်ခြင်း (H7)", r"(?<!an)[aā]bhisamayo", r"ထင်ထင်ရှားရှား (?:မ)?သိမြင်ခြင်း", "req",
     None),
    ("L12 abhisamayo (old «ထိုးဖောက် သိမြင်»)", r"^", r"ထိုးဖောက် သိမြင်", "forbid", None),
    ("L13 atthe / atthaṃ (sātthaṃ) / atthamaññāya = အနက်အဓိပ္ပာယ် (H1)", r"{0}(?:atthe|sātthaṃ|atthamaññāya){1}".format(B, E),
     r"အနက်အဓိပ္ပာယ်", "req", None),
    ("L13 attha (old bare «အနက်»)", r"{0}(?:atthe|sātthaṃ|atthamaññāya){1}".format(B, E), r"အနက်(?!အဓိပ္ပာယ်)", "forbid",
     None),
    ("L14 sabyañjanaṃ = စကားလုံးနှင့် ပြည့်စုံသော (H1)", r"sabyañjanaṃ", r"စကားလုံးနှင့် ပြည့်စုံသော", "req", None),
    ("L14 sabyañjanaṃ (old «သဒ္ဒါ»)", r"sabyañjanaṃ", r"သဒ္ဒါ", "forbid", None),
    ("L15 paṭipanna family = ကျင့်ကြံ (H5)", r"paṭipann|ppaṭipann", r"ကျင့်ကြံ", "req", None),
    ("L15 paṭipanna (old «ကျင့်သော / ကျင့်သူ»)", r"paṭipann|ppaṭipann", r"ကျင့်(?:သော|သူ)", "forbid", None),
    ("L16 abhirūpo dassanīyo pāsādiko = အဆင်းလှ … ကောင်း", rf"{B}abhirūp[oā]{E}", r"အဆင်းလှ", "req", None),
    ("L16 abhirūpo (old «ရုပ်ချော» / «… ဖွယ် ဖြစ်သူ»)", r"^", r"ရုပ်ချော|ဖွယ် ဖြစ်သူ", "forbid", None),
    ("L17 kasira = ပင်ပန်း (kiccha ခက်ခဲ stays)", rf"{B}(?:kasira|akasira)", r"ပင်ပန်း", "req", None),
    ("L17 kasira (old «ခက်ခဲ» without kiccha)", rf"{B}(?:kasira|akasira)", r"ခက်ခဲ", "forbid", r"kicch"),
    ("L18 bahvābādho = အနာရောဂါ များသူ", r"bahvābādho", r"အနာရောဂါ များသူ", "req", None),
    ("L19 kharājina = ကြမ်းသော သမင်သားရေ", r"kharājina", r"ကြမ်းသော သမင်သားရေ", "req", None),
    ("L20 sappi = ထောပတ်ကြည် (H3)", rf"{B}sappi", r"ထောပတ်ကြည်", "req", None),
    ("L20 sappitela (old «ထောပတ်နှင့် ဆီ»)", r"sappitel", r"ထောပတ်နှင့် ဆီ", "forbid", None),
    ("L21 sarūpavaccha = အဆင်းအရောင် တူသော", r"sarūpavacch", r"အဆင်းအရောင် တူသော", "req", None),
    ("L22 rajāpatho = ဖုန်လုံး တက်ရာ လမ်း", r"rajāpatho", r"ဖုန်လုံး တက်ရာ လမ်း", "req", None),
    ("L22 raja (old «မြူမှုန်»)", r"^", r"မြူမှုန်", "forbid", None),
    ("L23 ekanta = လုံးဝ", r"ekanta", r"လုံးဝ", "req", None),
    ("L23 ekanta (old «စင်စစ်»)", r"ekanta", r"စင်စစ်", "forbid", None),
    ("L24 nikati = ကောက်ကျစ်ခြင်း (H8)", r"nikati", r"ကောက်ကျစ်ခြင်း", "req", None),
    ("L24 nikati (old «စဉ်းလဲခြင်း»)", r"nikati", r"စဉ်းလဲခြင်း", "forbid", None),
    ("L25 pamāda (surāmeraya…) = မေ့လျော့မှု", r"majjapamādaṭṭhāy", r"မေ့လျော့မှု", "req", None),
    ("L25 pamāda (old «မေ့လျော့ခြင်း၏ အကြောင်း») outside the pi-2 witness", r"majjapamādaṭṭhāy", r"မေ့လျော့ခြင်း၏", "forbid",
     None),
    # ---- bilingual-review fixes (apply_fixes.py F01 … F05, layer L26 / L27) and the review items kept (KR)
    ("F01 A1 Puggalapaññattimātikā = the approved book title", r"Puggalapaññattimātikā",
     r"“ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း” ခေါင်းစဉ်စာရင်း", "req", None),
    ("F01 A1 (old «ပုဂ္ဂိုလ် သတ်မှတ်ချက် ခေါင်းစဉ်စာရင်း»)", r"^", r"ပုဂ္ဂိုလ် သတ်မှတ်ချက် ခေါင်းစဉ်စာရင်း", "forbid", None),
    ("F02 A6 Evamevaṃ … -(i)me … ūpamā = «… တူသော ဤပုဂ္ဂိုလ်»", r"Evamevaṃ (?:tayome|cattārome|pañcime) ",
     r"တူသော ဤပုဂ္ဂိုလ်", "req", None),
    ("F02 A6 Evamevaṃ without ime: no added «ဤ»", r"Evamevaṃ\s+(?:tayo|cattāro|pañca) ", r"တူသော ဤပုဂ္ဂိုလ်", "forbid",
     None),
    ("F03 B1 narassa = မြို့ (termbase change 2026-11-20)", rf"{B}narassa{E}", r"မြို့၏ အရှေ့ဘက်", "req", None),
    ("F03 B1 narassa (old «လူ၏ အရှေ့ဘက်»)", r"^", r"လူ၏ အရှေ့ဘက်", "forbid", None),
    ("F04 B6 panaññepi keci kurūrakammantā = one more person «… အခြား တစ်စုံတစ်ယောက် ဖြစ်၏»",
     r"panaññepi keci kurūrakammantā", r"ကြမ်းကြုတ်သော အလုပ် ရှိသော အခြား တစ်စုံတစ်ယောက် ဖြစ်၏", "req", None),
    ("F04 B6 (old subject switch «အခြားသူတို့လည်း ဖြစ်ကြ၏»)", r"^", r"အခြားသူတို့လည်း ဖြစ်ကြ၏", "forbid", None),
    ("F05 doubt 5 sāci = ကွေ့ဝိုက်သော (termbase change 2026-11-20)", r"sāciyog", r"ကွေ့ဝိုက်သော နည်းလမ်း", "req", None),
    ("F05 sāci (old «ကောက်ကျစ်သော»)", r"^", r"ကောက်ကျစ်သော", "forbid", None),
    ("L26 B2 vaṇṇopi … saṃvijjati = «… ပုဂ္ဂိုလ်အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏»", r"vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati",
     r"ပုဂ္ဂိုလ်အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏", "req", None),
    ("L26 B2 yo (pi) tattha (a)vaṇṇo = «ထိုတို့အနက် … ရှိသမျှကို»", r"[Yy]o(?:pi)? tattha a?vaṇṇo",
     r"ထိုတို့အနက် (?:ကဲ့ရဲ့|ချီးမွမ်း)ဖွယ် ရှိသမျှကို", "req", None),
    ("L26 B2 (old «ထိုသူ၌ … ဖွယ်» / «ပုဂ္ဂိုလ်သည် ချီးမွမ်းဖွယ်»)", r"^", r"ထိုသူ၌ (?:ကဲ့ရဲ့|ချီးမွမ်း)ဖွယ်|ပုဂ္ဂိုလ်သည် ချီးမွမ်းဖွယ်",
     "forbid", None),
    ("L27 B4 (a)pasādaṃ janeti – … ends with its janeti phrase", r"pasādaṃ janeti – ",
     r"ဟူ၍လည်း (?:မ)?ကြည်ညိုမှုကို ဖြစ်စေ၏", "req", None),
    ("L27 B4 janeti – (old added «ပြောဆို၏»)", r"janeti – ", r"ဟူ၍လည်း ပြောဆို၏", "forbid", None),
    ("KR B4 bhāsati – … keeps «ပြောဆို၏»", rf"{B}bhāsati – ", r"ဟူ၍လည်း ပြောဆို၏", "req", None),
    ("KR B3 paravaṇṇanāya parathomanāya parapasaṃsanāya = the termbase terms in the Pāli order",
     r"paravaṇṇanāya parathomanāya parapasaṃsanāya", r"ချီးမွမ်းစကား၊ ချီးကျူးစကား၊ ထောမနာစကား၊ ဂုဏ်သတင်း ဆောင်ယူချက်",
     "req", None),
    ("KR B5 yā sā vācā … bahujanamanāpā tathārūpiṃ = pi-1 ^1-1350 «… စကား ရှိ၏ ထိုသို့သော …»",
     r"bahujanamanāpā tathārūpiṃ vācaṃ bhāsitā", r"လူအများ စိတ်တွေ့သော စကား ရှိ၏ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏",
     "req", None),
    ("KR B5 yā sā vācā … bahujanamanāpā, tathārūpiṃ = «… စကား ရှိ၏၊ ထိုသို့သော …» (^4-100, the Pāli comma)",
     r"bahujanamanāpā, tathārūpiṃ vācaṃ bhāsitā", r"လူအများ စိတ်တွေ့သော စကား ရှိ၏၊ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏",
     "req", None),
    ("K indriyānaṃ ^4-M-6 = စွမ်းရည် (approved rails-step note)", r"bāvīsatindriyāni", r"စွမ်းရည်", "req", None),
    ("K mahapphalaṃ = အကျိုး ကြီးမား (approved rails-step note)", r"mahapphalaṃ", r"အကျိုး ကြီးမား", "req", None),
    ("K gilānapaccaya = သူနာ (H11)", r"gilānap?paccaya", r"သူနာ", "req", None),
    ("K gilāno / gilānūpamā = လူနာ (H11)", rf"{B}gilān(?:o|ūpamā|ā|aṃ){E}", r"လူနာ", "req", None),
    ("K rūpappamāṇo rūpappasanno … = one approved NAME per pair (H13)", r"[Rr]ūpappamāṇo|[Ll]ūkhappamāṇo",
     r"အတိုင်းအတာ ထား၍", "req", None),
    ("K araññagataṃ = ရောက်သော (^4-198: the text is right)", r"araññagataṃ", r"တောသို့ ရောက်", "req", None),
    ("K bahiddhā(saṃyojano) = အပြင်ပိုင်း, the fetter pair with ajjhatta = အတွင်းပိုင်း (binding rule; nāmarūpa does not occur in pi-4)",
     r"(?i)bahiddh", r"အပြင်ပိုင်း", "req", None),
]
for p in sorted(pd.glob("*.md")):
    a = [N(l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [N(l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for k, (x, y) in enumerate(zip(a, b), 1):
        xr = re.sub(r"\s*\^\S+\s*$", "", x)
        xb = re.sub(r"\[[^\]]*\]", "", xr)     # variant readings stay Pāli: not counted
        yb = re.sub(r"\s*\^\S+\s*$", "", y)
        for fam, pk, st, mode, unless in FAM:
            n = len(re.findall(pk, xb))
            if not n or (unless and re.search(unless, xb)):
                continue
            got = len(re.findall(st, yb))
            STATS[fam] = STATS.get(fam, 0) + n
            if (mode == "req" and got < n) or (mode == "forbid" and got):
                ids = re.findall(r"\^(\S+)\s*$", x)
                print(f"{p.name.split('-')[0].split('.')[0]}:{k}\t{fam}\t{mode} P×{n} M×{got}\t{ids}")
if "--stats" in sys.argv:
    for fam, *_ in FAM:
        print(f"stats\t{STATS.get(fam, 0)}\t{fam}")
