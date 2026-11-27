"""pi-7 Burmese RAILS LAYER: source patches of the zero-shot generators (pi-7-my/make_*.py, my7_formulas.py; read
only), applied in memory by build_rails.py. Model: pi-6-my/rails/my_formulas_rails.py (read only).

PATCHES[file] = [(old, new, count, reason)]: «old» must occur exactly «count» times in that file's source, else the
build stops (a patch that no generator run applies stops it too). A reason names the family, the Pāli, the term /
decision (termbase/decisions-A.tsv) or the §A item (mapper-my/map-harmonise-notes.md; termbase notes-part5 5e).

Import chain (build_rails.py): a patch of my7_formulas / make_sample / an upstream generator reaches every chapter
that imports it, at any depth (my7_formulas -> all; make_ch1-01 -> 2-03-06 … 5-xx; make_ch1-03-05 -> 2-01-02,
2-07-11, 2-03-06 (fallback engine) …; make_ch2-01-02 -> 2-07-11, 4-02-09, 5-01-04 …; make_ch2-07-11 -> 4-02-09,
5-01-04 …; make_ch3-01-02 -> 3-03-06, 3-07-08-10, 3-09, 4-xx, 5-xx; make_ch3-07-08-10 -> 4-01, 4-02-09, 5-xx), so one
shared string changes every instance together (identical Pāli = identical Burmese). Where a word is written as a
literal in several generators, each literal is patched (the counts list every source occurrence, comments included:
a comment that names the old value is updated with it).

The locked termbase (AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md, sha256 faef9155…) differs from the
zero-shot where the coordinator / termbase step decided against the text's form: the avasesa family (coordinator
change before the lock), nānākaraṇa (locked pi-5) and the §A items decided by a term; the families below bring the
text to the term. Single-segment differences are rules in residual_rules.py (apply_termbase.py).
"""

L01 = ("L01 avasesa family = «ကြွင်းကျန်…» (termbase avasesesu / avasesā / Avasesāni «ကြွင်းကျန်သော», coordinator "
       "change before the lock, APPROVED.md: the locked pi-1 / pi-2 / pi-5 / pi-6 term; the substantive «ကြွင်းကျန်သည်တို့» "
       "= pi-6 rails «ကြွင်းကျန်သည်တို့၌လည်း»): zero-shot «ကြွင်းသော / ကြွင်းသည်(တို့)» (30 uses = the 30 Pāli avases-)")
L02 = ("L02 nānākaraṇa family = «ကွဲပြားမှု» (termbase nānākaraṇaṃ «ကွဲပြားမှု», ninnānākaraṇaṃ / ninnānākaraṇā / "
       "ninnānā «ကွဲပြားမှု မရှိ», §A27 decided, locked pi-5: «one noun for nānā(karaṇa)»; nānaṃ / ninnānaṃ of the "
       "notes are the same word): zero-shot «ကွဲပြားချက်» (92 uses) and ninnānaṃ «ကွဲပြားခြင်း မရှိ» (2-01 ^7-U292); "
       "nānattaṃ «ကွဲပြားခြင်း» (1-03 ^7-4-33, another word) is not touched")
L03 = ("L03 §A15 suciṇṇāni = «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု(တို့)» (termbase suciṇṇāni «ကောင်းစွာ ကျင့်ခဲ့ဖူးသော»; the "
       "head noun «အမှု» of 1-01 / 2-03 … 4-01, §A5): zero-shot «ကောင်းစွာ ပြုခဲ့ဖူးသည်တို့» (1-03 … 1-05, 2-01, 2-07, "
       "2-08, 2-10: 21 uses)")
L04 = ("L04 §A16 tadārammaṇatā = «ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်» (termbase tadārammaṇatā «ထိုအာရုံကိုပင် အာရုံပြုသော "
       "အဖြစ်») and §A35 niruddhe = «ချုပ်ငြိမ်းသွားသောအခါ» (termbase niruddhe «ချုပ်ငြိမ်းသွားသော»): the 1-01 frame "
       "«niruddhe vipāko tadārammaṇatā uppajjati» (1-01, 2-05) = the 1-03 … 3-09 form")
L05 = ("L05 §A37 vibhajantena = «ခွဲခြမ်းစိတ်ဖြာလျက်» (termbase, the adverbial participle; = 3-05 ^7-28-52): zero-shot "
       "agent noun «ခွဲခြမ်းစိတ်ဖြာသူသည်» (3-10 ^7-U409)")
L06 = ("L06 §A14 ṭhānāṭhānakosallassa = «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း» (termbase; = 1-01, 2-05, 2-06, "
       "3-02, 4-01): zero-shot «ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု» (1-03 … 1-05, 2-07, 2-10)")
L07 = ("L07 §A19 pavatti = «ဘဝ ဖြစ်စဉ်» (termbase pavattipaṭisandhi «ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ», notes-part5 5e 19; = 2-04, "
       "2-14, 2-15, 3-01, 3-02, 3-09, 4-01): zero-shot «ဘဝ ဖြစ်ဆဲ ကာလ» (2-01, 2-07: 6 uses)")
L08 = ("L08 nillopaṃ = «လုယက်ပစ္စည်း» (termbase nillopaṃ «လုယက်», notes-part5 5g: «nillopaṃ harati» = «လုယက်ပစ္စည်းကို "
       "လုယူသည်» as the pi-5 rails «nillopaṃ hareyya» «လုယက်ပစ္စည်းကို လုယူရာ»): zero-shot «ဥစ္စာကို လုယူ…» (14 uses: "
       "the deeds list, its «-tvā» form and its cut form; the loose test let it pass on the «လုယက်» of gāmaghāta)")
L09 = ("L09 §A8 the act compounds carry their verb, also where «…pe…» cuts the list (termbase uposathakammaṃ «ဥပုသ်ကို "
       "စောင့်ထိန်းသည်», ekāgārikaṃ «အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်», gāmaghātaṃ «ရွာကို ဖျက်ဆီး၍ လုယက်သည်»; notes-part5 "
       "5e 8)")

L10 = ("L10 §A18 / uppanna «ဖြစ်ပေါ်ပြီးသော» before its noun (identical Pāli = identical Burmese; uppanna «ဖြစ်ပေါ်ပြီးသော», "
       "samāpatti «သမာပတ်», utu «ရာသီဥတု» are the locked terms): «uppannaṃ samāpajjati / samāpajjanti» = «ဖြစ်ပေါ်ပြီးသော "
       "သမာပတ်ကို ဝင်စား(ကြ)သည်» (the noun repeated from «anuppannaṃ … samāpattiṃ uppādeti», the majority 12 of 17: the 1-01 "
       "frame, 1-04, 1-05, 2-05, 2-06, 3-02, 4-01), and «uppannaṃ utuṃ upanissāya» = «ဖြစ်ပေါ်ပြီးသော ရာသီဥတုကို အားကြီးစွာ "
       "မှီ၍» (= 2-12 ^7-18-…); zero-shot nominalised «ဖြစ်ပေါ်ပြီးသည်ကို ဝင်စား…» (1-03 ×3, 2-07, 2-10) and «ဖြစ်ပေါ်ပြီးသည်ကို "
       "ရာသီဥတုကို …» (4-02 ^7-36-477). The bare «uppannaṃ» entry stays; the longer phrases come first (lex: longest match)")

PATCHES = {
    "my7_formulas": [
        ("ကြွင်းသ", "ကြွင်းကျန်သ", 1, L01 + ": note «avasesesu na kātabbaṃ» «ကြွင်းကျန်သည်တို့၌ မထည့်ရ» (all chapters)"),
        ('"nillopaṃ harati": "ဥစ္စာကို လုယူသည်"', '"nillopaṃ harati": "လုယက်ပစ္စည်းကို လုယူသည်"', 1,
         L08 + ": the deeds list (all chapters; the cut list of 3-07-08-10 takes the object from it)"),
    ],
    "make_ch1-01": [
        ("ကြွင်းသ", "ကြွင်းကျန်သ", 4, L01 + ": AVASESA, «avasesāni padāni», «avasesesu sabbattha atthi» and the comment"),
        ("ကွဲပြားချက်", "ကွဲပြားမှု", 2, L02 + ": NANAKARANA (1-01 notes; read by 2-03-06 … 4-xx as K.NANAKARANA) and the "
         "comment"),
        ("ချုပ်ငြိမ်းသောအခါ {F.VIPAKA_ADJ} စိတ်သည် ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့် {F.UP}",
         "ချုပ်ငြိမ်းသွားသောအခါ {F.VIPAKA_ADJ} စိတ်သည် ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့် {F.UP}", 1, L04),
        ('"nillopaṃ haritvā": "ဥစ္စာကို လုယူ၍"', '"nillopaṃ haritvā": "လုယက်ပစ္စည်းကို လုယူ၍"', 1,
         L08 + ": the «-tvā» deeds before «tassa paṭighātatthāya»"),
    ],
    "make_ch1-03-05": [
        ('NANAKARANA = new("nānākaraṇaṃ", "ကွဲပြားချက်")', 'NANAKARANA = new("nānākaraṇaṃ", "ကွဲပြားမှု")', 1,
         L02 + ": NANAKARANA of 1-03 … 1-05 (read by 2-01-02, 2-12-17 as G.NANAKARANA)"),
        ('new("suciṇṇāni", "ကောင်းစွာ ပြုခဲ့ဖူးသည်")', 'new("suciṇṇāni", "ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု")', 1,
         L03 + " (the «+» plural gives «…အမှုတို့»)"),
        ('"uppannaṃ": UPPANNA[:-len("သော")] + "သည်",',
         '"uppannaṃ": UPPANNA[:-len("သော")] + "သည်", "uppannaṃ utuṃ": f"{UPPANNA} ရာသီဥတု",', 1,
         L10 + ": «uppannaṃ utuṃ» in the 1-03 … 1-05 lexicon (read by 2-01-02, 2-07-11 and, through 2-03-06's fallback "
         "engine, 3-xx / 4-02-09)"),
        ('"samāpajjati": W("samāpajjati", "ဝင်စား") + "သည်", "samāpajjanti": "ဝင်စားကြသည်"})',
         '"samāpajjati": W("samāpajjati", "ဝင်စား") + "သည်", "samāpajjanti": "ဝင်စားကြသည်"})\n'
         'F.add_lex("x", {"uppannaṃ samāpajjati": f"{UPPANNA} {SAMAPATTI}ကို ဝင်စားသည်",\n'
         '                "uppannaṃ samāpajjanti": f"{UPPANNA} {SAMAPATTI}ကို ဝင်စားကြသည်"})', 1,
         L10 + ": «uppannaṃ samāpajjati / -anti» (the 1-01 phrase entries) in the 1-03 … 1-05 lexicon"),
        ('KOSALLA = new("ṭhānāṭhānakosalla", THANA + "၌ ကျွမ်းကျင်မှု")',
         'KOSALLA = new("ṭhānāṭhānakosalla", "ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း")', 1,
         L06 + " (THANA, the pi-5 witness of ṭhānāṭhānaṃ, stays checked; it is no longer used here)"),
    ],
    "make_ch2-01-02": [
        ("ကြွင်းသ", "ကြွင်းကျန်သ", 3, L01 + ": AVASESA (2-01 … 2-02, read by 2-07-11), «Avasesā sahajātapaccayasadisā» "
         "and the comment"),
        ("{G.NANATTA} {NATTHI}", "{G.NANAKARANA} {NATTHI}", 1, L02 + ": «(Nissayampi ninnānaṃ)» «… ကွဲပြားမှု မရှိ» "
         "(ninnānaṃ = ninnānā, not nānattaṃ)"),
        ('PAVATTI = new("pavatti / pavatte", "ဘဝ ဖြစ်ဆဲ ကာလ")', 'PAVATTI = new("pavatti / pavatte", "ဘဝ ဖြစ်စဉ်")', 1,
         L07),
    ],
    "make_ch2-07-11": [
        ('F.add_lex("na", {"uposathaṃ": F.LEX["uposathakammaṃ karoti"][0].split("ကို")[0],\n'
         '                 "uposathakammaṃ": F.LEX["uposathakammaṃ karoti"][0].split("ကို")[0]})',
         'F.add_lex("na", {"uposathaṃ": "ဥပုသ် စောင့်ထိန်းခြင်း",\n'
         '                 "uposathakammaṃ": "ဥပုသ် စောင့်ထိန်းခြင်း"})', 1,
         L09 + ": the cut «uposathakammaṃ…» / «uposathaṃ…» of 2-07 … 2-11 «ဥပုသ်…» → «ဥပုသ် စောင့်ထိန်းခြင်း…», the form of "
         "the 63 other cut uses (make_ch2-03-06 UPOSATHA, 2-03 … 4-01)"),
    ],
    "make_ch2-12-17": [
        ("ကြွင်းသ", "ကြွင်းကျန်သ", 1, L01 + ": AVASESA_A (2-12 … 2-17)"),
        ("ကွဲပြားချက်", "ကွဲပြားမှု", 1, L02 + ": the comment of NINNANAK (its value is G.NANAKARANA, patched in "
         "make_ch1-03-05)"),
    ],
    "make_ch3-01-02": [
        ("ကြွင်းသ", "ကြွင်းကျန်သ", 5, L01 + ": the 3-01 … 3-02 notes (avasesā pañhā / gaṇanā)"),
        ("ကွဲပြားချက်", "ကွဲပြားမှု", 1, L02 + ": the comment of NINNANAKARANA (its value is K.NANAKARANA, patched in "
         "make_ch1-01)"),
    ],
    "make_ch3-07-08-10": [
        ("ကြွင်းသ", "ကြွင်းကျန်သ", 1, L01 + ": AVAS_O (3-07 … 3-10, read by 4-01)"),
        ("ကွဲပြားချက်", "ကွဲပြားမှု", 1, L02 + ": the comment of a note (its value is NINNANAKARANA)"),
        ('new("vibhajantena", "ခွဲခြမ်းစိတ်ဖြာသူသည်")', 'new("vibhajantena", "ခွဲခြမ်းစိတ်ဖြာလျက်")', 1, L05),
        ('            mod.LEX.setdefault(w, (m[1] if m else full.split(" ")[0], "x"))',
         '            mod.LEX.setdefault(w, (full[:-len("သည်")] if w in ("ekāgārikaṃ", "gāmaghātaṃ")\n'
         '                                   else m[1] if m else full.split(" ")[0], "x"))', 1,
         L09 + ": the deeds cut short by «…pe…» (3-10, 4-01: 6 lists): ekāgārikaṃ «အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်…», "
         "gāmaghātaṃ «ရွာကို ဖျက်ဆီး၍ လုယက်…» (the full deed without its final «သည်», as «ဥပုသ်ကို စောင့်ထိန်း၍…»); the "
         "other members (sandhiṃ, nillopaṃ, paripanthe, paradāraṃ …) are plain objects whose terms the object holds"),
    ],
}
