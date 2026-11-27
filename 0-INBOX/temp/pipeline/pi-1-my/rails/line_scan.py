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
REL_P = (r"(?:(?:^|(?<=[?.] ))(?:Yo|Yaṃ|Yā)(?= )(?! taṃ rūpaṃ)(?! (?:cakkhu|sotaṃ|ghānaṃ|jivhā|kāyo)\b)"
         r"(?! rūpaṃ catunnaṃ)(?! (?:saddo|gandho|raso) catunnaṃ)(?! sā vācā)"
         r"|\b(?:yaṃ evarūpaṃ|yo evarūpo|yā evarūpā|yaṃ etasmiṃ antare|yañca rūpaṃ kammassa katattā uppajjissati))")
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None)
    ("L02 Yo/Yaṃ/yañca = ရှိသမျှ", REL_P, r"ရှိသမျှ", "req", None),
    ("L01 uppanna = ဖြစ်ပေါ်ပြီးသော", rf"(?<![{W}])(?:etth)?uppann(?:aṃ|ā|o|e|ānaṃ)(?![{W}])", r"ဖြစ်ပေါ်ပြီး", "req", None),
    ("L01 uppanna (citta opening)", r"\buppann(?:aṃ|ā) hoti\b", r"ဖြစ်ပေါ်လာသော အချိန်၌", "forbid", None),
    ("L03 ākāsa = ဟင်းလင်းပြင်", r"(?i)ākās", r"ဟင်းလင်းပြင်", "req", None),
    ("L03 ākāsa (old)", r"(?i)ākās", r"ကောင်းကင်", "forbid", None),
    ("L04 paṭiccasamuppāda", r"(?i)paṭiccasamuppād", r"အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ", "req", None),
    ("L04 paṭiccasamuppāda (old)", r"(?i)paṭiccasamuppād", r"အကြောင်းအကျိုး ဆက်စပ်", "forbid", None),
    ("L05 Suññatavāro", r"Suññatavāro", r"ဆိတ်သုဉ်းခြင်း ဖော်ပြချက်", "req", None),
    ("L05 Suññatavāro (old)", r"(?i)suññat", r"ဆိတ်သုဉ်းကြောင်း", "forbid", None),
    ("L06 samāpattivuṭṭhāna", r"samāpattivuṭṭhān", r"ဈာန် ဝင်စားရာမှ ထမြောက်", "req", None),
    ("L07 catukka- / pañcakanaya", r"(?i)(?:catukka|pañcaka)nay", r"ခွဲနည်း", "req", None),
    ("L08 Suddhikaappaṇihitaṃ", r"Suddhikaappaṇihitaṃ", r"တောင့်တမှု မရှိသော ဈာန် သက်သက်", "req", None),
    ("L09 indriyānaṃ paripāko", r"indriyānaṃ paripāko", r"အာရုံခံ အင်္ဂါတို့ ရင့်ရော်", "req", None),
    ("L10 kammassa katattā", r"(?i)kammassa katattā", r"ပြုခဲ့သော ကံကြောင့်", "req",
     r"kammassa katattā (?:upacitattā|bhāvitattā)"),   # the vipāka opening: katattā / upacitattā entries, not the phrase
    ("L10 kammassa katattā (old)", r"(?i)kammassa katattā", r"ကံကို ပြုခဲ့ခြင်းကြောင့်", "forbid", None),
    ("L11 vibhava", r"(?i)vibhava(?!diṭṭh)", r"ဘဝ ပျောက်ကွယ်ခြင်း", "req", None),
    ("L11 vibhava (old)", r"(?i)vibhava", r"ပြတ်စဲခြင်း", "forbid", None),
    ("L12 dhammānaṃ vipākato", r"dhammānaṃ vipākato", r"အကျိုး ဖြစ်သော စိတ်", "req", None),
    ("L13 kāyiko", rf"(?<![{W}])kāyiko(?![{W}])|kāyikavācasiko", r"ကိုယ်ပိုင်းဆိုင်ရာ", "req", None),
    ("L13 vācasiko", rf"(?<![{W}])vācasiko(?![{W}])|kāyikavācasiko", r"နှုတ်ပိုင်းဆိုင်ရာ", "req", None),
    ("L13 kāyiko / vācasiko (old)", r"\bkāyiko\b", r"ကိုယ်ဖြင့် (?:မ)?ကျူးလွန်", "forbid", None),
    ("L14 kodha", r"(?i)kodh", r"အမျက်ဒေါသ", "req", None),
    ("L15 kaṇṇasukhā", r"kaṇṇasukh", r"နား သာယာ", "req", None),
    ("L16 hadayaṅgamā", r"hadayaṅgam", r"နှလုံးသားသို့", "req", None),
    ("L17 bhiyyokamyatā", r"bhiyyokamyatā", r"ပိုမို လိုချင်ခြင်း", "req", None),
    ("L18 bojjhaṅga", r"(?i)bojjhaṅg", r"ဗောဇ္ဈင်", "req", None),
    ("L18 bojjhaṅga (old)", r"(?i)bojjhaṅg", r"သိမြင်ခြင်း၏ အင်္ဂါ", "forbid", None),
    ("L19 Saṃvego", r"(?i)\bsaṃvego", r"သံဝေဂ ရခြင်း", "req", None),
    ("L20 (an)uppādāya", r"\b(?:an)?uppādāya\b", r"ဖြစ်ပေါ်စေရန်", "forbid", None),
    ("L21 pubbenivāsānussati", r"pubbenivāsānussati", r"အဖန်ဖန် အောက်မေ့", "req", None),
    ("L22 samuppannā", rf"(?<![{W}])samuppannā(?![{W}])", r"ဖြစ်ပေါ်လာ", "req", None),
    ("L22 samuppannā (old)", rf"(?<![{W}])a?samuppannā(?![{W}])", r"ကောင်းစွာ (?:မ)?ဖြစ်ပေါ်", "forbid", None),
    ("L23 kusalato / vipākato / kiriyato ca", r"(?:kusalato|vipākato) ca (?:vipākato|kiriyato)",
     r"စိတ်အနက်လည်းကောင်း", "req", None),
    ("L23 … ca (old)", r"(?:kusalato|vipākato) ca (?:vipākato|kiriyato)", r"အဖြစ်လည်းကောင်း", "forbid", None),
    ("L24 rūpañca nibbānañca", rf"(?<![{W}])[Rr]ūpañca nibbānañca", r"ရုပ်လည်း နိဗ္ဗာန်လည်း", "req", None),
    ("L25 kusalahetu", rf"(?<![{W}])(?:a|abyākata)?kusalahet|abyākatahet",
     r"(?:ကုသိုလ်|အကုသိုလ်)၏ အမြစ် (?!ဖြစ်သော)|(?:ကုသိုလ်|အကုသိုလ်)၏ အမြစ်$|သဘောတရားတို့၏ အမြစ်", "forbid",
     r"kusalamūl"),
    ("L25 kusalahetu (subject)", r"(?:alobho|adoso|amoho) kusalahetu", r"ကုသိုလ် အမြစ် ဖြစ်သော", "req", None),
    ("L26 sineho", rf"(?<![{W}])sineho(?![{W}])", r"ချစ်ခင်မှု", "req", r"sinehagataṃ"),   # water: cohesion, other sense
    ("L26 mucchā", rf"(?<![{W}])mucchā(?![{W}])", r"မိန်းမောမှု", "req", None),
    ("L26 santuṭṭhitā", rf"(?<![{W}])santuṭṭhitā(?![{W}])", r"ရောင့်ရဲမှု", "req", None),
    ("L27 domanassa", r"domanassupāyās|abhijjhādomanass", r"စိတ်ဆင်းရဲမှု", "req", None),
    ("L27 domanassa (old)", r"(?i)domanass", r"စိတ်ဆင်းရဲခြင်း", "forbid", None),
    # user-approved termbase change 2026-11-17: bahiddhā (external) = «မိမိ၏ ပြင်ပ၌»; the bases of mastery
    # («ajjhattaṃ arūpasaññī bahiddhā» ပြင်ပ၌) and «ito bahiddhā» (အပြင်ဘက်) are the other two senses
    ("L28 bahiddhā = မိမိ၏ ပြင်ပ၌", r"(?i)(?<![a-zāīūṃṅñṭḍṇḷ])(?:ajjhatta)?bahiddh", r"မိမိ၏ ပြင်ပ၌", "req",
     r"arūpasaññī bahiddhā|[Ii]to bahiddhā"),
    ("L28 bahiddhā (old)", r"(?i)bahiddh", r"သူတစ်ပါး၌", "forbid", None),
    # user-approved termbase change B6 / B7 / B10, 2026-11-17
    ("L36 cittahetuka", r"cittahetuk", r"စိတ်ကို အကြောင်းပြု", "req", None),
    ("L36 cittahetuka (old)", r"cittahetuk", r"စိတ်ကို အမြစ်ပြု", "forbid", None),
    ("L37 byāpajjanā", r"byāpajjanā", r"ဖောက်ပြန်နေခြင်း", "req", None),
    ("L37 byāpajjanā (old)", r"byāpajjanā", r"(?<!မ)ညှဉ်းဆဲလို", "forbid", None),
    ("L38 ucchedadiṭṭhi (old)", r"(?i)ucchedadiṭṭhi|ucchijjissati", r"သေပြီးနောက် ပြတ်စဲ", "forbid", None),
]
for p in sorted(pd.glob("*.md")):
    a = [N(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [N(l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for k, (x, y) in enumerate(zip(a, b), 1):
        xb = re.sub(r"\s*\^\S+\s*$", "", x)
        yb = re.sub(r"\s*\^\S+\s*$", "", y)
        for fam, pk, st, mode, unless in FAM:
            n = len(re.findall(pk, xb))
            if not n or (unless and re.search(unless, xb)):
                continue
            got = len(re.findall(st, yb))
            if (mode == "req" and got < n) or (mode == "forbid" and got):
                ids = re.findall(r"\^(\S+)\s*$", x)
                print(f"{p.name[:-3]}:{k}\t{fam}\t{mode} P×{n} M×{got}\t{ids}")
