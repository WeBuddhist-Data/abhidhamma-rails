"""Consistency pass (pi-3 Burmese, Dhātukathā): every item of harmonise-todo.md, before vs now.
For each item the lines whose Pāli matches `pali` are taken (an item is counted only where the Pāli line has it;
«VERSE» = the summary-verse lines, my3_formulas.VERSES); in their Burmese the uses of the chosen form and of every
other form are counted, in the chapter files before the pass (harmonise-backup/chapters/) and now. An item fails if an
other form is left now, or if a line that has the Pāli item lacks the chosen form now.
usage: python3 -I -X utf8 harmonise_scan.py [--table]   (--table also writes harmonise-table.tsv)"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my3_formulas as F  # noqa: E402

F.install()
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-3_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters"
T = lambda k: F.subject(k)[0][:-len(" " + F.DHP)]          # noqa: E731  a pi-1 term without «သဘောတရားများ»
E = re.escape

# (item, Pāli regex on the line or "VERSE", chosen Burmese (regex), [other forms (regex)], kind)
# kind: A = source as written, B = term / frame drift, R = rule kept (verified, nothing to change)
ITEMS = [
    # ---- Part A: the source as written
    ("A1 ^3-413 «… dhātusaṅgahena saṅgahitā te dhammā» (no mark: no «၊»)", r"dhātusaṅgahena saṅgahitā te dhammā",
     r"အကျုံးဝင်သော သဘောတရားများ ထိုသဘောတရားများသည်", [r"အကျုံးဝင်သော သဘောတရားများ၊ ထိုသဘောတရားများသည်"], "A"),
    ("A1 ^3-225 «… asaṅgahitā tehi dhammehi» (no mark: no «၊», kept)", r"asaṅgahitā tehi dhammehi",
     r"အကျုံးမဝင်သော သဘောတရားများ ထိုသဘောတရားတို့နှင့်", [r"အကျုံးမဝင်သော သဘောတရားများ၊ ထိုသဘောတရားတို့နှင့်"], "A"),
    ("A2 ^3-269 «Dassanena pahātabbā dhammā bhāvanāya …» (no mark: no «၊», no «…»)",
     r"Dassanena pahātabbā dhammā bhāvanāya", r"ပယ်ရမည့် သဘောတရားများသည် ဘာဝနာ",
     [r"ပယ်ရမည့် သဘောတရားများသည်၊ ဘာဝနာ", r"ပယ်ရမည့် သဘောတရားများသည်… ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် သဘောတရားများသည်… သစ္စာ"],
     "A"),
    ("A3 a space before «…» in the Pāli (typography: «X…» in every generator)", r" …", r"[^ ]…", [r" …"], "R"),
    ("A4 ^3-357 «..» kept as written", r"ye dhammā\.\. ", r"နှင့်\.\. ", [], "R"),
    ("A4 ^3-287 «… aparāmaṭṭhā dhammā sampayuttāti?» (question words elided, no «…pe…»: as written)",
     r"aparāmaṭṭhā dhammā sampayuttāti\?", r"မဖြစ်နိုင်သော သဘောတရားများသည် ယှဉ်တွဲကြသနည်း",
     [r"မဖြစ်နိုင်သော သဘောတရားများသည်… ယှဉ်တွဲကြသနည်း"], "R"),
    ("A4 ^3-298 «… pahātabbahetukā dhammā… sampayuttāti?» (as written)", r"pahātabbahetukā dhammā… sampayuttāti\?",
     r"သဘောတရားများသည်… ယှဉ်တွဲကြသနည်း", [], "R"),
    ("A5 ^3-189 «Cittasahabhūmi» (slip) = cittasahabhuno (pi-1)", r"Cittasahabhūmi",
     E(T("cittasahabhuno dhammā")), [], "R"),
    ("A5 ^3-210 «paccupannārammaṇehi» (slip) = paccuppannārammaṇā (pi-1)", r"paccupannārammaṇehi",
     E(T("paccuppannārammaṇā dhammā")), [], "R"),
    ("A5 ^3-213 / ^3-279 «na hetusahetuka-» (one word) = na hetū sahetukā (pi-1)", r"na hetusahetuk",
     E(T("na hetū sahetukā dhammā")), [], "R"),
    ("A5 «na hetuahetukehi» (one word) = na hetū ahetukā (pi-1)", r"na hetuahetuk",
     E(T("na hetū ahetukā dhammā")), [], "R"),
    ("A5 ^3-454 «dhātusaṅgena» (slip) = dhātusaṅgahena", r"dhātusaṅgena", r"ဓာတ် အကျုံးဝင်ခြင်းဖြင့်", [], "R"),
    ("A5 anupādinnupādāniya- = pi-1 anupādiṇṇupādāniyā", r"[Aa]nupādinnupādāniy",
     E(T("anupādiṇṇupādāniyā dhammā")), [], "R"),
    ("A5 anupādinnaanupādāniya- = pi-1 anupādiṇṇaanupādāniyā", r"[Aa]nupādinnaanupādāniy",
     E(T("anupādiṇṇaanupādāniyā dhammā")), [], "R"),
    ("A5 anupādinnā / -ehi = pi-1 anupādiṇṇā", r"[Aa]nupādinn(?:ā|ehi)\b", E(T("anupādiṇṇā dhammā")), [], "R"),
    # ---- B1 verb number (the Pāli number; «-ā» after a feminine singular subject = singular: the sample)
    ("B1 singular participle «-o(ti)?» question: no «ကြ»", r"(?:sampayutt|vippayutt)oti?\?",
     r"(?:ယှဉ်တွဲ|ကင်းကွာ)သနည်း", [], "R"),
    ("B1 «te dhammā … sampayuttā(ti) / vippayuttā?» (plural): «ကြသနည်း»",
     r"te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi (?:sampayutt|vippayutt)ā(?:ti)?\?",
     r"မည်မျှတို့နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)ကြသနည်း", [r"ထိုသဘောတရားများသည် [^။]*မည်မျှတို့နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)သနည်း"], "R"),
    # ---- B2 kehici / na kehici
    ("B2 kehici = «… (တို့)၏ အချို့နှင့် V»", r"(?<!na )kehici (?:sampayutt|vippayutt)", r"၏ အချို့နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)",
     [r"အချို့ကို", r"တချို့", r"အချို့တို့"], "R"),
    ("B2 na kehici … = «V-ရာ X၊ Y မရှိ» (the sample's zero run)", r"na kehici|na kāhici",
     r"ရာ (?:အစုအဝေး|အာရုံခံ နယ်ပယ်|ဓာတ်)(?:၊ (?:အာရုံခံ နယ်ပယ်|ဓာတ်))* မရှိ", [r"မည်သည့်", r"တစ်ပါးမျှ"], "R"),
    # ---- B3 relative-clause frames
    ("B3 «X-ena ye dhammā…» (verb elided) = «Xနှင့်…» (the relative said once, where the verb is)",
     "CHUNK", r"နှင့်(?: \[[^\]]+\])?$", [r"(?:ယှဉ်တွဲ|ကင်းကွာ)သော သဘောတရားများ$"], "B"),
    ("B3 «X-ena ye dhammā sampayuttā / vippayuttā» = «Xနှင့် Vသော သဘောတရားများ»", r"ye dhammā (?:sampayuttā|vippayuttā)",
     r"နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)သော သဘောတရားများ", [], "R"),
    ("B3 khandhasaṅgahena (a)saṅgahitā … = «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံး(မ)ဝင်၊ …သော သဘောတရားများ»",
     r"khandhasaṅgahena a?saṅgahitā", r"အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံးမ?ဝင်၊ အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့်",
     [r"အစုအဝေး အကျုံးဝင်မှု", r"အစုအဝေးဖြင့် အကျုံး"], "R"),
    ("B3 tehi dhammehi ye dhammā = «ထိုသဘောတရားတို့နှင့်» (pi-1 ^1-1115)", r"(?<![\w])tehi dhammehi ye dhammā",
     E(F.TEHI), [r"ထိုသဘောတရားများနှင့်"], "R"),
    ("B3 te dhammā = «ထိုသဘောတရားများသည်» (pi-1 ^1-1091)", r"(?<!ye )[Tt]e dhammā", E(F.TE + F.SUBJ_MARK),
     [r"ထိုတရားများ", r"ယင်းသဘောတရား"], "R"),
    ("B3 Natthi = «မရှိ။» (pi-1 ^1-1221)", r"Natthi[.?]", r"(?:^| )မရှိ။", [r"မရှိပါ"], "R"),
    # ---- B4 saṅkhāra number
    ("B4 avijjāpaccayā saṅkhārena (sg) = «… ပြုပြင်ဖန်တီးမှု» (pi-2 ^2-249)", r"avijjāpaccayā saṅkhārena",
     r"မသိမှုကြောင့် ဖြစ်သော ပြုပြင်ဖန်တီးမှုနှင့်", [r"မသိမှုကြောင့် ဖြစ်သော ပြုပြင်ဖန်တီးမှုများနှင့်"], "R"),
    ("B4 avijjāpaccayā saṅkhārā / -ehi (pl) = «… ပြုပြင်ဖန်တီးမှုများ» (sample, pi-2 ^2-227)",
     r"[Aa]vijjāpaccayā saṅkhār(?:ā|ehi)", r"မသိမှုကြောင့် ဖြစ်သော ပြုပြင်ဖန်တီးမှုများ",
     [r"မသိမှုကြောင့် ဖြစ်သော ပြုပြင်ဖန်တီးမှု(?!များ)"], "R"),
    ("B4 saṅkhārapaccayā viññāṇa- = «ပြုပြင်ဖန်တီးမှုများကြောင့် ဖြစ်သော သိစိတ်» (sample, pi-2 ^2-227)",
     r"[Ss]aṅkhārapaccayā viññāṇ", r"ပြုပြင်ဖန်တီးမှုများကြောင့် ဖြစ်သော သိစိတ်", [r"ပြုပြင်ဖန်တီးမှုကြောင့်"], "R"),
    # ---- B5 the summary verses
    ("B5 verse locatives (-e / -esu / -su, ettha) = «တွင်» (the sample's IN)", "VERSE", r"တွင်", [r"၌"], "B"),
    ("B5 padā with a number = «ပုဒ် N-ပါး» (classifier ပါး, as the sample)", "VERSE", r"ပုဒ် [က-႟]+ပါး",
     [r"(?<!ပုဒ် )(?<= )[က-႟]+ပုဒ်(?:[၊။]|ကို|လည်း)"], "B"),
    ("B5 a count without padā = «N-ပါး»", r"tikesvekūnavīsati|Mahantare pannarasa|Gocchakesu ca paññāsa",
     r"[က-႟]+ပါး", [r"ဆယ့်ကိုးပုဒ်", r"ဆယ့်ငါးပုဒ်", r"ငါးဆယ်ပုဒ်"], "B"),
    ("B5 gocchaka = «အစု» (pi-1 Hetugocchakaṃ)", r"gocchak|Gocchak", r"အစု", [], "R"),
    ("B5 cūḷantare / mahantare (no duka) = «ကြားညှပ် အစုငယ် / အစုကြီး»", r"(?:cūḷ|Mah)antare ",
     r"ကြားညှပ် အစု(?:ငယ်|ကြီး)တွင်", [r"ကြားညှပ် နှစ်မျိုးတွဲ အစု(?:ငယ်|ကြီး)တွင် (?:ဆယ့်ငါး|ရှစ်)"], "B"),
    ("B5 Mahantaraduka / cūḷantaradukā / Piṭṭhiduka = the pi-1 headings", r"Mahantaraduke|cūḷantaradukā|piṭṭhi ?dukesu",
     r"ကြားညှပ် နှစ်မျိုးတွဲ အစု(?:ငယ်|ကြီး)|နောက်ဆုံး နှစ်မျိုးတွဲများ", [], "R"),
    ("B5 mahantarā (no duka) = «ကြားညှပ် အစုကြီး»", r"mahantarāti", r"ရှစ်ပါးသည် ကြားညှပ် အစုကြီး",
     [r"ရှစ်ပါးသည် ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး"], "B"),
    ("B5 Sattantarā (no duka) = «ကြားညှပ်တို့မှ»", r"Sattantarā", r"ကြားညှပ်တို့မှ", [r"ကြားညှပ် နှစ်မျိုးတွဲတို့မှ"], "B"),
    ("B5 Paṭhamantare / aparante = «ပထမ ကြားညှပ်» / «နောက် ကြားညှပ်» (no gocchaka)", r"Paṭhamantare",
     r"ပထမ ကြားညှပ်တွင် .* နောက် ကြားညှပ်တွင်", [r"ကြားညှပ် အစုတွင်", r"နောက်ပိုင်း ကြားညှပ်"], "B"),
    ("B5 paccayākāre = «အကြောင်းတို့၏ အခြင်းအရာတွင်»", r"paccayākāre", r"အကြောင်းတို့၏ အခြင်းအရာတွင်", [], "R"),
    ("B5 paccaye = «အကြောင်း အပိုင်းတွင်»", r"Paccaye ", r"အကြောင်း အပိုင်းတွင်",
     [r"အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ၌", r"အကြောင်း အပိုင်း၌"], "B"),
    ("B5 paṭicca(padā) = «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ» (pi-2)", r"paṭicca", r"အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ", [], "R"),
    ("B5 upari / uddhaṃ = «အထက်တွင်», tato upari = «ထို့အထက်တွင်»", r"VERSE:[Uu]ddhaṃ|(?<![a-z])upari|sūpari",
     r"အထက်တွင်", [r"အထက်ပိုင်း၌", r"အထက်၌", r"ထို့အထက်တွင် နောက်ထပ်"], "B"),
    ("B5 tato pare = «ထို့နောက်တွင်»", r"tato pare", r"ထို့နောက်တွင်", [], "R"),
    ("B5 puna / punadeva = «တဖန်»", r"\b[Pp]una", r"တဖန်", [r"နောက်ထပ်"], "B"),
    ("B5 atha = «ထို့နောက်»", r"\batha\b|dasasvatha", r"ထို့နောက်", [r"တို့၌မူ"], "B"),
    ("B5 numbers 30 / 43 / 47 = «သုံးဆယ်» / «လေးဆယ့်သုံး» / «လေးဆယ့်ခုနစ်» (one word with «ပါး» / «မျိုး»)",
     r"tiṃsa|tecattālīsa|sattacattālīsa", r"(?:သုံးဆယ်|လေးဆယ့်သုံး|လေးဆယ့်ခုနစ်)(?:ပါး|မျိုး)",
     [r"သုံးဆယ် မျိုး", r"သုံးဆယ် အပြည့်"], "B"),
    ("B5 na labbhati (sg) = «မတွေ့ရ»", r"labbhatīti", r"မတွေ့ရ။", [], "R"),
    ("B5 na labbhare / na labbhanti (pl) = «မတွေ့ရကြ»", r"labbh(?:are|anti)", r"မတွေ့ရကြ", [r"မတွေ့ရ(?!ကြ)"], "B"),
    ("B5 jīvitaṃ (verse) = «အသက်» (pi-2 termbase)", r"jīvitaṃ", r"အသက်", [], "R"),
    ("B5 mahābhavā = «ဘဝကြီး»", r"mahābhavā", r"ဘဝကြီး", [], "R"),
    ("B5 maccurūpaṃ: rūpaṃ = the term «ရုပ် ဖြစ်သော သဘောတရား» (as the neighbouring terms)", r"maccurūpaṃ",
     r"သေခြင်း၊ ရုပ် ဖြစ်သော သဘောတရား", [r"သေခြင်း၊ ရုပ်၊"], "B"),
    ("B5 ^3-227 / ^3-455 «… dve, visayo … esanayo subuddho»: one literal treatment",
     r"esanayo subuddho", r"နှစ်ပါး၊ အပိုင်းအခြား(?: \[[^\]]+\])?၊ ဤခွဲနည်းကို ကောင်းစွာ နားလည်အပ်သည်",
     [r"နယ်ပယ်နှင့်တကွ", r"နားလည်ပြီ", r"သိမြင်အပ်", r"ဟူသော နှစ်ပါးသည်"], "B"),
    ("B5 manāyatanameva ca = «၊ မနော အာရုံခံ နယ်ပယ်လည်း»", r"manāyatanameva ca", r"လေးပါး၊ မနော အာရုံခံ နယ်ပယ်လည်း",
     [r"လေးပါးနှင့် မနော"], "B"),
    ("B5 verse verbs (honti …) = «…သည်» (no «၏» ending)", "VERSE", r"(?:ရှိ|ဖြစ်)သည်|(?<!ရှိ)(?<!ဖြစ်)",
     [r"(?:ရှိ|ဖြစ်)၏"], "B"),
    ("B5 no verb added after «… ca» («…လည်း။»)", r"tecattālīsameva ca\.|moghapucchakena cāti", r"လည်း။",
     [r"လည်း ဖြစ်သည်"], "B"),
    ("B5 samuccheda = «ပိုင်းဖြတ်ခြင်း»", r"Samucchede", r"ပိုင်းဖြတ်ခြင်းတွင်", [r"ပိုင်းခြားမှု"], "B"),
    ("B5 moghapucchakena = «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်»", r"moghapucchakena", r"မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်",
     [r"အချည်းနှီး မေးခွန်း"], "B"),
    ("B5 matthake = «အဆုံးတွင်»", r"matthake", r"အဆုံးတွင်", [r"အဆုံးပိုင်း", r"အဆုံး၌"], "B"),
    ("B5 iccete … dhammā = «ဤသို့ ဤသဘောတရား N-ပါးတို့သည်» (counted noun without «များ»)", r"iccete",
     r"ဤသို့ ဤသဘောတရား လေးဆယ့်ခုနစ်ပါး", [r"ဤသဘောတရားများ လေးဆယ့်"], "B"),
    # ---- B6 headings and colophons
    ("B6 Khandhādi = «အစုအဝေး စသည်»", r"^#+ Khandhādi", r"အစုအဝေး စသည်", [], "R"),
    ("B6 Saccādi = «သစ္စာ စသည်»", r"^#+ Saccādi", r"သစ္စာ စသည်", [], "R"),
    ("B6 Phassādisattakaṃ = «တွေ့ထိမှု စသည့် ခုနစ်မျိုးတွဲ»", r"Phassādisattakaṃ", r"တွေ့ထိမှု စသည့် ခုနစ်မျိုးတွဲ", [], "R"),
    ("B6 Tikaṃ / Dukaṃ = pi-2", r"^#+ (?:Tikaṃ|Dukaṃ)$", r"^#+ (?:သုံးမျိုးတွဲ|နှစ်မျိုးတွဲ)$", [], "R"),
    ("B6 (X-mūlakaṃ.) = «(X-ကို အခြေခံသော ခွဲနည်း။)» (pi-2)", r"mūlakaṃ\.\)", r"ကို အခြေခံသော ခွဲနည်း။\)", [], "R"),
    ("B6 book colophon = «“…” ကျမ်း ပြီးဆုံးပြီ။» (pi-1 / pi-2)", r"Dhātukathāpakaraṇaṃ niṭṭhitaṃ",
     r"“ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း” ကျမ်း ပြီးဆုံးပြီ။", [], "R"),
    # ---- B7 bare items, elided questions
    ("B7 bare instrumental items «Saṃyojanehi…» = «နှောင်ကြိုး ဖြစ်သော…» (as ch4 / ch5: no «သဘောတရားများနှင့်»)",
     r"(?<![a-z])[Ss]aṃyojanehi ?…", r"နှောင်ကြိုး ဖြစ်သော…", [r"နှောင်ကြိုး ဖြစ်သော သဘောတရားများနှင့်… အထုံး ဖြစ်သော သဘောတရား"],
     "B"),
    ("B7 elided question «…(pe…) sampayuttāti?» = «… V(ကြ)သနည်း» (the sample's particle)",
     r"…(?:pe…)? ?(?:sampayutt|vippayutt)\w*\?", r"…(?: |)(?:ယှဉ်တွဲ|ကင်းကွာ)(?:ကြ)?သနည်း", [r"သလော"], "R"),
    # ---- B8 sigla
    ("B8 (bahūsu) = «(Bahūsu)» (pi-1 / pi-2 final, Roman like the other sigla)", r"\(bahūsu\)", r"\(Bahūsu\)",
     [r"မူ အများ"], "B"),
    ("B8 (?) = «(အမည်မသိ မူ)» (pi-2 ^2-924)", r"\(\?\)", r"\(အမည်မသိ မူ\)", [], "R"),
    ("B8 (sī.) (syā.) (ka.) (pī.) = Sī. Syā. Ka. Pī. (pi-1)", r"\((?:sī|syā|pī)\.", r"\((?:Sī|Syā|Pī)\.", [], "R"),
]

ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def pairs(md):
    for p in sorted(PD.glob("*.md")):
        ch = p.name.split("-")[0].split(".")[0]
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            yield ch, x, y


def chunks(md):
    """«CHUNK»: the chain items «… ye dhammā» whose verb is elided (Pāli chunk before «…» / «..»), paired with the
    Burmese chunk before «…» / «..» (lines and sentences that split evenly)."""
    for ch, x, y in pairs(md):
        xs, ys = re.split(r"(?<=[.?])\s+", x.strip()), re.split(r"(?<=။)\s+", y.strip())
        if len(xs) != len(ys):
            continue
        for s, t in zip(xs, ys):
            a = re.split(r"…pe…|…Pe…|…|\.\.(?= )", s)
            b = re.split(r"…|\.\.(?= )", t)
            if len(a) != len(b):
                continue
            for c, d in zip(a[:-1], b[:-1]):
                if re.search(r"(?<![\w])ye dhammā$", re.sub(r" ?\[[^\]]*\]", "", c.strip(" ,"))):
                    yield ch, c, d.strip(" ၊")


def count(md, pali, chosen, others):
    nl = nc = miss = 0
    no = [0] * len(others)
    chs = [set() for _ in others]
    src = chunks(md) if pali == "CHUNK" else pairs(md)
    for ch, x, y in src:
        if pali == "CHUNK":
            pass
        elif pali == "VERSE":
            if x not in F.VERSES:
                continue
        elif pali.startswith("VERSE:"):
            if x not in F.VERSES or not re.search(pali[6:], x):
                continue
        elif not re.search(pali, x):
            continue
        nl += 1
        c = len(re.findall(chosen, y)) if chosen else 0
        nc += c
        miss += c == 0
        for i, o in enumerate(others):
            k = len(re.findall(o, y))
            no[i] += k
            if k:
                chs[i].add(ch)
    return nl, nc, miss, no, chs


def main(argv):
    rows, fails = [], 0
    for item, pali, chosen, others, kind in ITEMS:
        nl, nc0, _, no0, ch0 = count(BEFORE, pali, chosen, others)
        nl1, nc1, miss1, no1, _ = count(NOW, pali, chosen, others)
        left = sum(no1)
        bad = left or not nl1 or (miss1 and pali != "VERSE")
        unit = "chain items" if pali == "CHUNK" else "lines"
        fails += bool(bad)
        chs = sorted(set().union(*ch0), key=lambda c: int(c) if c.isdigit() else 0) if others else []
        print(f"{'FAIL' if bad else 'OK  '} {item}: {nl1} {unit}; chosen {nc0} -> {nc1}"
              + (f"; other forms {sum(no0)} -> {left}" if others else "") + (f"; {miss1} lines without it" if miss1 and pali != "VERSE" else ""))
        rows.append((item, chosen, "; ".join(f"{o} ({n})" for o, n in zip(others, no0) if n) or "-",
                     ", ".join(chs) or "-", kind))
    if "--table" in argv:
        with open(HERE / "harmonise-table.tsv", "w", encoding="utf-8") as fh:
            fh.write("Pāli item\tchosen Burmese\tother forms before (uses)\tchapters changed\tkind\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")
    print(f"{len(ITEMS) - fails} / {len(ITEMS)} items OK")
    return fails


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
