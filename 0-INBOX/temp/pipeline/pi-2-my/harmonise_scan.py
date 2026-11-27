"""Consistency pass (pi-2 Burmese): every item of harmonise-todo.md (and every drift the scans found), before vs now.
For each item: the lines whose Pāli matches `pali` are taken (so an item is only counted where the Pāli line has it);
in their Burmese, the uses of the chosen form and of every other form are counted, in the chapter files before the
pass (harmonise-backup/chapters-before/) and now. An item fails if an other form is left now.
usage: python3 -I -X utf8 harmonise_scan.py [--table]   (--table also writes harmonise-table.tsv)"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-2_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters-before"

# (item, Pāli regex on the line, chosen Burmese (regex), [other forms (regex)], kind)
# kind: A = source slip (translated as written), B = term drift, F = frame / punctuation
ITEMS = [
    # ---- A: source slips
    ("^2-171 «saṃyojanañceva saṃyojaniya\"ntipi» (ca missing, as written)", r'"saṃyojanañceva saṃyojaniya"ntipi',
     r"“နှောင်ကြိုးလည်း ဖြစ်၊ နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော", [r"“နှောင်ကြိုးလည်း ဖြစ်၊ နှောင်ကြိုး၏ အာရုံလည်း"], "A"),
    ("^2-171 «upādāniyañceva upādānasampayuttañcā» (not upādānañceva)", r'"upādāniyañceva upādānasampayuttañcā"',
     r"“စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်၊ စွဲလမ်းမှုနှင့်လည်း", [r"“စွဲလမ်းမှုလည်း ဖြစ်၊ စွဲလမ်းမှုနှင့်လည်း"], "A"),
    ("^2-171 «siyā upādānasampayuttaupādāniyā» (not -vippayutta-)", r"siyā upādānasampayuttaupādāniyā",
     r"တစ်ခါတစ်ရံ စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော သဘောတရားများအနက်",
     [r"နှစ်ပါးသည် တစ်ခါတစ်ရံ စွဲလမ်းမှုနှင့် ကင်းကွာသော"], "A"),
    ("^2-171 «kilesasampayuttā ceva no ca na kilesā» (double negative)", r"no ca na kilesā",
     r"ကိလေသာ မဟုတ်သည် မဟုတ်သော", [r"ယှဉ်တွဲသော်လည်း ကိလေသာ မဟုတ်သော"], "A"),
    ("^2-184 «atthi hetu, atthi ahetu» (a-hetu, not na hetu)", r"atthi hetu, atthi ahetu\.",
     r"အမြစ် မဟုတ်သော ပြုပြင်ဖန်တီးမှု ရှိသည်", [], "A"),
    ("^2-188 parāmāsa quote: one quotation, no «ti» after it", r'"parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā',
     r"သဘောတရားများဟု မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော်လည်း", [r"သဘောတရားများ” ဖြစ်ကြသည်"], "A"),
    ("^2-206 Dukaṃ «Dve saccā nīvaraṇiyā dve saccā …» (stop missing: no «၊» added)",
     r"Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā", r"ဖြစ်ကြသည် သစ္စာ နှစ်ပါးသည် အတားအဆီး၏ အာရုံ မဖြစ်",
     [r"ဖြစ်ကြသည်၊ သစ္စာ နှစ်ပါးသည် အတားအဆီး၏ အာရုံ မဖြစ်"], "A"),
    ("^2-206 Dukaṃ «Dukkhasaccaṃ siyā ajjhattaṃ» (not ajjhattikaṃ)", r"Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ",
     r"ဒုက္ခ သစ္စာသည် တစ်ခါတစ်ရံ မိမိ၌ ရှိသော", [r"ဒုက္ခ သစ္စာသည် တစ်ခါတစ်ရံ အတွင်းပိုင်း"], "A"),
    ("^2-223 «siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ» / ch7 «Siyā vipākā siyā …» (no «၊» added)",
     r"siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ|Siyā vipākā siyā vipākadhammadhammā\.",
     r"(?:ဖြစ်သည်|ဖြစ်ကြသည်) တစ်ခါတစ်ရံ", [r"အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော သဘောတရား ဖြစ်သည်၊ တစ်ခါတစ်ရံ ကြီးမြတ်",
                                       r"ကံ၏ အကျိုး ဖြစ်သော သဘောတရားများ ဖြစ်ကြသည်၊ တစ်ခါတစ်ရံ အကျိုး ပေးတတ်"], "A"),
    ("^2-711 «kāmāvacare kusalaṃ cittaṃ» (locative, as written)", r"kāmāvacare kusalaṃ cittaṃ",
     r"ကာမဘုံ၌ ကုသိုလ်စိတ်သည်", [r"မွန်မြတ်သော ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်စိတ်သည်"], "A"),
    ("^2-974 / ^2-976 taṇhāvicarita «… vā yathā so …» (comma missing: no «၊» added)", r"[^,] vā yathā so ",
     r"ဟုဖြစ်စေ ထိုသူ", [r"(?<=ဖြစ်၏)ဟုဖြစ်စေ၊ ထိုသူ သူဆင်းရဲမျိုး", r"မင်းမျိုး မဟုတ်ဟုဖြစ်စေ၊ ထိုသူ ပုဏ္ဏား"], "A"),
    ("^2-1039 «siyā dukkhamasukhāya» (as written, a- missing)", r"siyā dukkhamasukhāya",
     r"တစ်ခါတစ်ရံ နာကျင် မသာယာသော", [r"မောဟသည် .* တစ်ခါတစ်ရံ မနာကျင် မသာယာသော"], "A"),
    # ---- B: the suttanta definitions (ch4 = ch6)
    ("sattanikāya (jāti / jarā / maraṇa)", r"sattanikāy", r"သတ္တဝါ အမျိုးအစား", [r"သတ္တဝါ အပေါင်း"], "B"),
    ("abhinibbatti (jāti list)", r"jāti sañjāti okkanti abhinibbatti", r"ထင်ရှားစွာ ပေါ်ထွက်ခြင်း",
     [r"ထင်ရှား ဖြစ်ခြင်း"], "B"),
    ("khandhānaṃ pātubhāvo (jāti list)", r"khandhānaṃ pātubhāvo", r"အစုအဝေးတို့၏ ထင်ရှား လာခြင်း",
     [r"အစုအဝေးတို့ ပေါ်ထွက်ခြင်း"], "B"),
    ("X-byasanena vā phuṭṭhassa (soka / parideva / upāyāsa)", r"byasanena vā phuṭṭhassa",
     r"ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ", [r"ပျက်စီးခြင်းနှင့်ဖြစ်စေ တွေ့ကြုံရသူ၏"], "B"),
    ("aññataraññatarena byasanena samannāgatassa", r"byasanena samannāgatassa",
     r"ပျက်စီးခြင်းနှင့် ကြုံတွေ့နေရသူ၏", [r"ပျက်စီးခြင်းနှင့် ပြည့်စုံသူ၏"], "B"),
    ("aññataraññatarena dukkhadhammena phuṭṭhassa", r"dukkhadhammena phuṭṭhassa",
     r"ဆင်းရဲဖွယ်ရာဖြင့် ထိခိုက်ခံရသူ၏", [r"ဆင်းရဲဖွယ် အကြောင်းနှင့် တွေ့ကြုံရသူ၏"], "B"),
    ("antoparisoko", r"antoparisoko", r"အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း", [r"အတွင်း၌ အလွန် စိုးရိမ်ခြင်း"], "B"),
    ("vācā palāpo vippalāpo lālappo … (one item per word)", r"vācā palāpo vippalāpo",
     r"စကား၊ ပေါက်ကရ ပြောခြင်း၊ ကမောက်ကမ ပြောခြင်း၊ မြည်တမ်းခြင်း",
     [r"စကား ပေါက်ကရ ပြောခြင်း", r"ညည်းတွား"], "B"),
    ("«… phuṭṭhassa X Y – ayaṃ vuccati» without a relative: no «ရှိသမျှ»", r"phuṭṭhassa (?:soko|ādevo|āyāso)",
     r"(?:ငြောင့်|အဖြစ်) – ဤသည်ကို", [r"(?:ငြောင့်|အဖြစ်) ရှိသမျှ – ဤသည်ကို"], "B"),
    ("saṅgati / samāgamo / samodhānaṃ", r"saṅgati|samāgamo|samodhānaṃ", r"စုဝေးခြင်း",
     [r"ဆုံတွေ့ခြင်း", r"ပေါင်းဆုံခြင်း"], "B"),
    # ---- B: the todo list
    ("upapatti / upapattibhava (noun)", r"upapatti", r"ပြန်လည် ဖြစ်ပေါ်", [r"ပဋိသန္ဓေ"], "B"),
    ("adhimokkha", r"adhimokkh", r"ဆုံးဖြတ်မှု", [r"ဆုံးဖြတ်ချက်"], "B"),
    ("samudayasaccaṃ (as written)", r"[Ss]amudayasacc", r"(?<!ဒုက္ခ )ဖြစ်ပေါ်ခြင်း သစ္စာ", [r"ဒုက္ခ ဖြစ်ပေါ်ခြင်း သစ္စာ"], "B"),
    ("nirodhasaccaṃ (as written)", r"[Nn]irodhasacc", r"(?<!ဒုက္ခ )ချုပ်ငြိမ်းခြင်း သစ္စာ",
     [r"ဒုက္ခ ချုပ်ငြိမ်းခြင်း သစ္စာ"], "B"),
    ("upādānakkhandha", r"upādānakkhandh", r"စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော",
     [r"စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော အစုအဝေး ငါးပါး"], "B"),
    ("tathāgato paraṃ maraṇā (the ten views = pi-1)", r"tathāgato paraṃ maraṇā", r"မြတ်စွာဘုရားသည် သေပြီးနောက်",
     [r"တထာဂတ"], "B"),
    ("sassato loko … (the ten views = pi-1)", r"[Ss]assato loko", r"လောကသည် ထာဝရ တည်မြဲသည်",
     [r"လောကသည် မြဲ၏", r"အသက်ကောင်သည်"], "B"),
    ("«X\"ti vā» in the views (pi-1 frame)", r"[Ss]assato loko\"?ti vā", r"ဟူ၍ဖြစ်စေ",
     [r"(?:တည်မြဲသည်|မတည်မြဲ|မြဲ၏|မမြဲ)”?ဟုဖြစ်စေ"], "B"),
    ("the editors' «(?)»", r"\(\?\)", r"အမည်မသိ မူ", [r"ရင်းမြစ် မသေချာ"], "B"),
    ("bhavadiṭṭhi / vibhavadiṭṭhi … (pi-1 suttantika names)", r"bhavadiṭṭhi|sassatadiṭṭhi|pubbantānudiṭṭhi",
     r"ဟူသော အယူ", [r"ဘဝဆိုင်ရာ အယူ", r"ပျောက်ကွယ်ခြင်းဆိုင်ရာ အယူ", r"(?<!တည်)မြဲသည်ဟူသော အယူ",
                   r"(?<!စဲသွား)ပြတ်သည်ဟူသော အယူ", r"ကာလကို အစွဲပြုသော အယူ"], "B"),
    # ---- B: drift found by the scans (align_check, harmonise_lists, harmonise_tables)
    ("nekkhamma- / abyāpāda- / avihiṃsāsaṅkappo", r"[Nn]ekkhammasaṅkappo, abyāpādasaṅkappo",
     r"ခြင်းဆိုင်ရာ ကြံစည်မှု", [r"ခြင်းကို ကြံစည်မှု", r"ညှဉ်းဆဲလိုစိတ် မရှိခြင်း"], "B"),
    ("musāvāda", r"[Mm]usāvād", r"မုသား ပြောခြင်း", [r"မုသားစကား", r"မုသာ ပြောခြင်း"], "B"),
    ("pisuṇā vācā", r"pisuṇ", r"ကုန်းတိုက်သော စကား", [r"ကုန်းချော"], "B"),
    ("samphappalāpa", r"samphappalāp", r"အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", [r"အကျိုးမဲ့ စကား", r"အကျိုးမဲ့ ပြောခြင်း"], "B"),
    ("adinnādāna", r"adinnādān", r"မပေးသည်ကို ယူခြင်း", [r"မပေးသောအရာကို ယူခြင်း"], "B"),
    ("sammāājīvena jīvikaṃ kappeti", r"sammāājīvena jīvikaṃ kappeti", r"အသက်မွေး၏", [r"အသက် မွေး၏"], "B"),
    ("kāyiko / vācasiko (a)vītikkamo", r"vītikkamo", r"ပိုင်းဆိုင်ရာ (?:မ)?ကျူးလွန်ခြင်း",
     [r"(?:ကိုယ်|နှုတ်|ကိုယ်နှုတ်)ဖြင့် (?:မ)?ကျူးလွန်ခြင်း"], "B"),
    ("X vā cittaṃ \"X citta\"nti pajānāti (the sixteen states)", r'citta"nti pajānāti|paricca pajānāti',
     r"ကွဲပြားစွာ သိ၏", [r"”ဟု သိသည်", r"ပိုင်းခြား၍ သိသည်", r"တွန့်ဆုတ်သော စိတ်", r"ပျံ့လွင့်သော စိတ်"], "B"),
    ("mettā- / karuṇā- … cetovimutti", r"cetovimutti", r"စိတ်လွတ်မြောက်မှု", [r"စိတ် လွတ်မြောက်ခြင်း"], "B"),
    ("khīraṃ / sappi (pi-1 names)", r"khīraṃ dadhi sappi", r"နွားနို့၊ နို့ချဉ်၊ ထောပတ်ကြည်", [r"ထောပတ်ဆီ", r"၊ နို့၊"], "B"),
    ("gehasitaṃ cetasikaṃ sātaṃ … (pi-1 feeling synonyms)", r"gehasitaṃ cetasikaṃ",
     r"စိတ်ပိုင်းဆိုင်ရာ", [r"စိတ်၌ ဖြစ်သော", r"ချမ်းသာ သာယာစွာ", r"မချမ်းသာ နာကျင်"], "B"),
    # ---- F: frames
    ("multi-citta opening «Q…pe… Q sasaṅkhārena…pe…» (no «၊» before the adverb; objects first)",
     r"cittaṃ uppannaṃ hoti \S+ \S+ sasaṅkhārena…pe…", r"(?:ယှဉ်တွဲသော|ကင်းကွာသော) တိုက်တွန်းမှုဖြင့်",
     [r"(?:ယှဉ်တွဲသော|ကင်းကွာသော)၊ တိုက်တွန်းမှုဖြင့်", r"နည်း။ (?:ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်စိတ်|အကုသိုလ်စိတ်)သည် "
      r"(?:ဝမ်းမြောက်|ဥပေက္ခာ)"], "F"),
]
# items checked and kept (a genuine sense / context difference, or already one form): (item, note)
CHECKED = [
    ("cuti", "«စုတေခြင်း» in both maraṇa lists (ch4, ch6: one form already); pi-1 cuti «သေခြင်း» (cutūpapāta) kept in ch16 "
             "«သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်း»: in the maraṇa list «သေခြင်း» is maraṇaṃ, two synonyms may not share it"),
    ("dukkhaṃ (label of the kāyika dukkha definition)", "ch4 / ch6 «ကိုယ်ဆင်းရဲခြင်း» (the dukkha of «soka-parideva-"
     "dukkha-…», pi-1 final) vs ch12 «နာကျင်မှု» (the dukkha of «dukkhassa ca pahānā», pi-1 final): context"),
    ("rūpasaññā", "jhāna formula «ရုပ်ဟု မှတ်သိမှု» (ch12, ch16, ch17) vs the six-object list «အဆင်းအရောင်ဟု မှတ်သိမှု»: sense"),
    ("rūpataṇhā", "six-object list «အဆင်းအရောင်ကို တပ်မက်မှု» vs kāma/rūpa/arūpa-taṇhā «သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု»: sense"),
    ("kāyopi passambhati", "ch10 «ကိုယ်လည်း ငြိမ်းအေး၏» kept: no identical pi-1 sentence; pi-1 termbase kāyo «ကိုယ်»; the "
     "«စိတ်၏ အဖော်တို့» of pi-1 kāyapassaddhi is that compound's own definition (^1-320), not stated here"),
    ("idha", "«ဤသာသနာ၌» (a monk / disciple; pi-1 ^1-1377) vs «ဤလောက၌» (anyone; pi-1 Idhekacco): sense"),
    ("hadayaṃ", "the organ in the body list «နှလုံး» vs the citta synonym «နှလုံးသား» (pi-1): sense"),
    ("attha (ch15)", "«အကျိုးအနက်» kept for atthapaṭisambhidā (the Pāli does not split result / meaning; one compound "
                     "covers both); «atthaṃ carati» (benefit) «အကျိုး» in ch17: sense"),
    ("na vattabbā A-tipi, B-tipi", "frame «… ဟု(လည်းကောင်း) … ခေါ်ဆို၍ မရ» everywhere; quotes and dash follow the Pāli "
                                   "per line (check_marks OK on 19 files): one frame already"),
    ("saṅkhārapaccayā viññāṇaṃ", "6:10 suttanta (saṅkhārā plural, pi-1 4-03) vs abhidhamma (saṅkhāro): context"),
    ("chapter titles «X ကို ခွဲခြမ်းစိတ်ဖြာခြင်း»", "one pattern in 18 titles and colophons; the ch15 note names ch3 "
                                                 "«“ဓာတ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း”၌ကား» = ch3's title"),
    ("headings / colophons", "Suttantabhājanīyaṃ, Abhidhammabhājanīyaṃ, Pañhāpucchakaṃ, -niddeso, -mātikā, Catukkaṃ / "
                             "Pañcakaṃ (5 + 5 lines), X niṭṭhito: every Pāli heading has one Burmese (372 headings)"),
    ("^2-245 upādānasampayuttaṃ (for taṇhāsampayuttaṃ)", "as written «စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော စွဲလမ်းမှု» already"),
    ("^2-517 «Ñatvādhikaraṇamenaṃ»", "the sentence differs from pi-1's «Yatvādhikaraṇamenaṃ manindriyaṃ …» in one letter "
     "only (the same formula word): spelling slip, pi-1's Burmese kept"),
    ("^2-576 «santā hoti», ^2-717 «na hetu sahetūkā», «bhāvanāyapahātabbā»", "as written (singular kept; ū / joined: spelling)"),
    ("^2-933 bhavantattaṃ, ^2-273 abhinibbati, ^2-277 akusamūlaṃ, jīvhindriyampetaṃ, Sattadhātuyo, «micchā ājīvā», "
     "^2-688 muditāyatanā, ^2-508 ākiñcāyatanaṃ, ^2-749 apaṭighā, ^2-753 anuppādinn- / ajjhatā, stray spaces",
     "spelling slips (one letter, joined / split word, stray space): the intended word kept (allowed by the rule)"),
    ("^2-974 (7) «– evaṃ bhavissanti hoti»", "as written: one «evaṃ» rendered once («ငါ ထိုနည်းတူ ဖြစ်လိမ့်မည်ဟု ဖြစ်သည်»)"),
    ("^2-777 «upariṭṭhimā … arahattaphale»", "the ending of the adjective is not visible in the Burmese attributive: same"),
    ("ch10 ^2-478 stray «yo»", "a relative pronoun without its clause; not rendered (no Burmese word for it), logged"),
]


def lines(md):
    """(chapter, Pāli, Burmese) units: the sentences of a line when Pāli and Burmese split evenly, else the line."""
    out = []
    for p in sorted(PD.glob("*.md")):
        ch = p.name.split("-")[0].split(".")[0]
        P = p.read_text(encoding="utf-8-sig").split("\n")
        M = (md / p.name).read_text(encoding="utf-8").split("\n")
        for x, y in zip(P, M):
            if not x.strip():
                continue
            xs, ys = re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", x), re.split(r"(?<=။) ", y)
            out += [(ch, a, b) for a, b in zip(xs, ys)] if len(xs) == len(ys) else [(ch, x, y)]
    return out


def count(ls, item):
    _, prx, ch, others, _ = item
    prx, chr_ = re.compile(prx), re.compile(ch)
    c, o, where = 0, collections.Counter(), collections.Counter()
    for chn, x, y in ls:
        if prx.search(x):
            c += len(chr_.findall(y))
            for r in others:
                k = len(re.findall(r, y))
                if k:
                    o[r] += k
                    where[chn] += k
    return c, o, where


def main(argv):
    before, now = lines(BEFORE), lines(NOW)
    rows, left = [], 0
    for it in ITEMS:
        cb, ob, wb = count(before, it)
        cn, on, wn = count(now, it)
        lft = sum(on.values())
        left += lft
        status = "LEFT" if lft else "OK  "
        print(f"{status} [{it[4]}] {it[0]}: chosen {cb} -> {cn}; other forms {sum(ob.values())} -> {lft}")
        rows.append((it[0], it[2].replace("(?<!ဒုက္ခ )", ""), "; ".join(f"{r} ({n})" for r, n in ob.items()) or "-",
                     ", ".join(sorted(wb, key=lambda c: int(c) if c.isdigit() else 0)) or "-", it[4]))
    print(f"items: {len(ITEMS)} changed / aligned, {len(CHECKED)} checked and kept; other forms left: {left}")
    if "--table" in argv:
        out = ["Pāli item\tchosen Burmese\tother forms before (uses)\tchapters changed\tkind"]
        out += ["\t".join(r) for r in rows]
        out += [f"{k}\t(kept)\t{v}\t-\tCHECKED" for k, v in CHECKED]
        (HERE / "harmonise-table.tsv").write_text("\n".join(out) + "\n", encoding="utf-8")
    return left


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
