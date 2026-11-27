"""Per-line scan of the GENUINE keyword families (stricter than the per-segment adherence check): a Pāli line holding
the family's Pāli form whose Burmese line has fewer termbase forms than the Pāli has hits (req), or still has the
old form (forbid). A family may name a Pāli «unless» regex: lines matching it are not scanned for that family.
usage: line_scan.py <pali dir> <burmese dir>     (prints one line per failure; nothing = clean)"""
import pathlib
import re
import sys
import unicodedata

pd, md = map(pathlib.Path, sys.argv[1:3])
N = lambda s: unicodedata.normalize("NFC", s)
W = "a-zA-Zāīūṃṅñṭḍṇḷ"
B = rf"(?<![{W}])"          # Pāli word start
E = rf"(?![{W}])"           # Pāli word end
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None)
    ("L01 avasesā = ကြွင်းကျန်သော", rf"{B}[Aa]vasesā(?:naṃ)?{E}", r"ကြွင်းကျန်သော", "req", None),
    ("L01 avasesā (old)", rf"{B}[Aa]vasesā(?:naṃ)?{E}", r"ကြွင်းသော", "forbid", None),
    ("L02 niddeso (heading) = အကျယ် ဖော်ပြချက်", r"niddeso", r"အကျယ် ဖော်ပြချက်", "req", None),
    ("L02 niddeso (old)", r"niddeso", r"ဖွင့်ဆိုချက်", "forbid", None),
    ("L03 pihakaṃ = သရက်ရွက်", rf"{B}pihakaṃ{E}", r"သရက်ရွက်", "req", None),
    ("L03 mutta (urine) = ဆီး", r'lasikā mutta"nti', r"အစေး၊ ဆီး ရှိ၏", "req", None),
    ("L04 viharati glosses", r"[Ii]riyati vattati pāleti yapeti yāpeti carati viharati",
     r"လှုပ်ရှား၏၊ လည်ပတ်၏၊ စောင့်ရှောက်၏၊ မျှတ၏၊ မျှတစေ၏၊ ကျင်လည်၏၊ နေ၏", "req", None),
    ("L05 paṭilābho = ရရှိခြင်း", rf"{B}lābho paṭilābho{E}", r"ရခြင်း၊ ရရှိခြင်း", "req", None),
    ("L05 upasampadā = ဝင်စားခြင်း", rf"{B}sacchikiriyā upasampadā{E}", r"မျက်မှောက်ပြုခြင်း၊ ဝင်စားခြင်း", "req", None),
    ("L05 paṭilābho (old)", rf"{B}paṭilābho{E}", r"ထပ်မံ ရခြင်း|ပြန်လည် ရခြင်း", "forbid", None),
    ("L06 upekkhā synonyms", r"upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa",
     r"ဥပေက္ခာ၊ ဥပေက္ခာဖြင့် ရှုခြင်း၊ ဥပေက္ခာဖြင့် လွန်စွာ ရှုခြင်း၊ စိတ်၏ အလယ်၌ တည်ခြင်း", "req", None),
    ("L07 dānamayā … bhāvanāmayā", r"dānamayā sīlamayā bhāvanāmayā",
     r"ပေးလှူခြင်းမှ ဖြစ်သော၊ သီလမှ ဖြစ်သော၊ ဘာဝနာ ပွားများခြင်းမှ ဖြစ်သော", "req", None),
    ("L08 santā … byantīkatā", r"santā hoti samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā "
     r"visositā byantīkatā|santā honti samitā vūpasantā",
     r"ငြိမ်းပြီး၊ ငြိမ်သက်ပြီး၊ ကောင်းစွာ ငြိမ်သက်ပြီး၊ ကွယ်ပျောက်ပြီး၊ လုံးဝ ကွယ်ပျောက်ပြီး၊ ချုပ်ငြိမ်းစေပြီး၊ "
     r"အပြီးတိုင် ချုပ်ငြိမ်းစေပြီး၊ ခြောက်ခန်းစေပြီး၊ လုံးဝ ခြောက်ခန်းစေပြီး၊ အဆုံးသတ်ပြီး ဖြစ်", "req", None),
    ("L08 santā (old)", r"santā hon?ti samitā", r"သွားသည်", "forbid", None),
    ("L08 jātā … pātubhūtā", r"jātā honti sañjātā nibbattā abhinibbattā pātubhūtā",
     r"မွေးဖွားပြီး၊ ကောင်းစွာ မွေးဖွားပြီး၊ ပေါ်ထွက်ပြီး၊ ထင်ရှားစွာ ပေါ်ထွက်ပြီး၊ ထင်ရှားလာပြီး ဖြစ်ကြ၏", "req", None),
    ("L08 sahajātaṃ", r"sahagataṃ hoti sahajātaṃ", r"အတူ မွေးဖွားပြီး ဖြစ်၏", "req", None),
    ("L09 upeto … samannāgato", r"upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato",
     r"ယှဉ်သူ၊ ကောင်းစွာ ယှဉ်သူ၊ ချဉ်းကပ်သူ၊ ကောင်းစွာ ချဉ်းကပ်သူ၊ ရောက်ရှိသူ၊ ပြည့်စုံသူ၊ အပြည့်အဝ ပြည့်စုံသူ ဖြစ်၏",
     "req", None),
    ("L09 samannāgat (old)", r"samannāgat", r"အညီအညွတ်", "forbid", None),
    ("L10 sakkāra = အရိုအသေ ပြုခံရမှု", r"(?i)sakkār", r"အရိုအသေ ပြုခံရမှု", "req", r"(?i)sakkārasilokasannissit|sakkacc"),
    ("L10 sakkāra (old)", r"(?i)sakkār", r"အပူဇော်ခံရခြင်း", "forbid", None),
    ("L10 paṭibhāna (old)", r"paṭibhān", r"လျင်မြန်သော ဉာဏ်", "forbid", None),
    ("L20 mātā / pitā", rf"{B}mātā vā pitā vā{E}", r"အမိ ဖြစ်စေ၊ အဖ ဖြစ်စေ", "req", None),
    ("L20 anattha (old)", r"(?i)anattha", r"အကျိုးမဲ့ကို|အကျိုး မရှိခြင်းကို", "forbid", None),
    ("L21 asesavirāganirodho", r"asesavirāganirodho", r"အကြွင်းအကျန် မရှိ ပြယ်ပျောက် ချုပ်ငြိမ်းခြင်း", "req", None),
    ("L22 sammāsati formula (ch4)", r"kāye kāyānupassī viharati ātāpī sampajāno satimā, vineyya",
     r"ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက်၊ ထက်သန်သော လုံ့လ ရှိသူ", "req", None),
    ("L23 pariyantaṃ karitvā", r"avīcinirayaṃ pariyantaṃ karitvā", r"အဆုံးအစွန် ပြု၍", "req", None),
    ("L24 niruddhasamanantarā", r"niruddhasamanantarā", r"ချုပ်ငြိမ်းပြီးသည့် ချက်ချင်း နောက်၌", "req", None),
    ("L25 āvaṭṭanā … manasikāro", r"āvaṭṭanā (?:anāvaṭṭanā )?ābhogo samannāhāro manasikāro|natthi āvaṭṭanā vā ābhogo vā",
     r"စိတ်ကို လှည့်ဆောင်ခြင်း.*စိတ်ညွတ်ခြင်း.*စိတ်ကို ဆောင်ခြင်း.*နှလုံးသွင်းခြင်း", "req", None),
    ("L25 samannāhāro (old)", r"samannāhār", r"အာရုံသို့ စိတ်ညွတ်ခြင်း|ပထမ နှလုံးသွင်းခြင်း", "forbid", None),
    ("L28 bhajati sambhajati sevati", r"bhajati sambhajati sevati nisevati saṃsevati",
     r"ဆည်းကပ်၏၊ ကောင်းစွာ မှီဝဲ၏၊ မှီဝဲ၏၊ အမြဲ ဆည်းကပ်၏၊ ကောင်းစွာ ဆည်းကပ်၏", "req", None),
    ("L30 the wrong-livelihood list", r"veḷudānena vā pattadānena", r"အရွက်ကို ပေးလှူခြင်း", "req", None),
    ("L33 āsevati bhāveti bahulīkaroti", rf"{B}āsevati bhāveti bahulīkaroti{E}", r"အလေ့အကျင့် ပြု၏၊ ပွားများ၏၊ အကြိမ်ကြိမ် ပြု၏",
     "req", None),
    ("L35 samāpannassa (arūpa)", r"āyatanaṃ samāpannassa vā upapannassa", r"နယ်ပယ် ဈာန်ကို ဝင်စားသူ", "req", None),
    ("L38 2-745 uppannā hoti", r"manoviññāṇadhātu uppannā hoti kiriyā", r"ဖြစ်ပေါ်ပြီး", "req", None),
    ("L41 pajānāti (Tathāgata)", r"pajānāti", r"(?<!ကွဲပြားစွာ )သိတော်မူသည်", "forbid", None),
    ("L51 nikkhitta (old)", rf"{B}nikkhitta", r"(?<!မ)ချထား", "forbid", None),
    ("L53 ārabbha (old)", rf"{B}ārabbha{E}", r"အစွဲပြု၍", "forbid", None),
    ("L54 nānattasaññā", r"nānattasaññ", r"အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှု", "req", None),
    ("L56 macchariya list", r"kulamacchariyaṃ, lābhamacchariyaṃ, vaṇṇamacchariyaṃ",
     r"ကိုးကွယ်သော အိမ်ကို ဝန်တိုမှု၊ လာဘ်ကို ဝန်တိုမှု၊ ဂုဏ်သတင်းကို ဝန်တိုမှု", "req", None),
    ("L57 saṅga (old)", r"saṅg[oā]", r"တွယ်ငြိမှု", "forbid", None),
    ("L58 vatthu (old)", r"(?:kilesa|virodha|āghāta|kusīta)vatthu", r"အကြောင်းရင်း|၏ အကြောင်း", "forbid", None),
    ("L62 sassatavādā", r"sassatavādā", r"ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ", "req", None),
    ("L62 ucchedavādā", r"ucchedavādā", r"ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ", "req", None),
    ("L63 ajjhattikassa / bāhirassa upādāya", r"(?i)(?:ajjhattikassa|bāhirassa) upādāya", r"(?:အတွင်းပိုင်း|ပြင်ပ)ကို မှီ၍",
     "req", None),
    ("L63 (old)", r"(?i)(?:ajjhattikassa|bāhirassa) upādāya", r"(?:အတွင်း|အပြင်)ကို မှီ၍", "forbid", None),
    ("L66 maggo (road)", r"maggo gantabbo|maggo gato|[Mm]aggaṃ kho pana", r"ခရီး", "forbid", None),
    ("R01 uparito", r"uparito paranimmitavasavattī", r"အထက်ဘက်တွင် ပရနိမ္မိတဝသဝတ္တီ", "req", None),
]
for p in sorted(pd.glob("*.md")):
    a = [N(l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [N(l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for k, (x, y) in enumerate(zip(a, b), 1):
        xb = re.sub(r"\[[^\]]*\]", "", re.sub(r"\s*\^\S+\s*$", "", x))     # variant readings stay Pāli: not counted
        yb = re.sub(r"\s*\^\S+\s*$", "", y)
        for fam, pk, st, mode, unless in FAM:
            n = len(re.findall(pk, xb))
            if not n or (unless and re.search(unless, xb)):
                continue
            got = len(re.findall(st, yb))
            if (mode == "req" and got < n) or (mode == "forbid" and got):
                ids = re.findall(r"\^(\S+)\s*$", x)
                print(f"{p.name.split('-')[0].split('.')[0]}:{k}\t{fam}\t{mode} P×{n} M×{got}\t{ids}")
