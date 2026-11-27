"""pi-6 Burmese RAILS LAYER: source patches of the zero-shot generators (pi-6-my/make_*.py, my6_formulas.py; read
only), applied in memory by build_rails.py. Model: pi-5-my/rails/my_formulas_rails.py (read only).

PATCHES[file] = [(old, new, count, reason)]: «old» must occur exactly «count» times in that file's source, else the
build stops. A reason names the family, the Pāli, the term / decision or the §A item (mapper-my/map-harmonise-notes.md).

The termbase (AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md, sha256 847e49cd…, LOCKED) was built from this
zero-shot's keyword map, so the adherence run of the zero-shot has no GENUINE miss (333 rows, all INFLECTION:
rails/adherence-classified.tsv); the layer holds the §A text item that no term decides and that a single shared
string fixes everywhere (identical Pāli = identical Burmese).

L01 §A1 «yassa cittassa anantarā» (map-harmonise §A 1; termbase notes-part5 5d: left for the rails step).
    The zero-shot has two Burmese forms of the one Pāli phrase: the correlative «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (5-01 …
    5-03, 9-01 … 9-03, 10-09 … 10-11; 166 places) and «မိမိ စိတ်၏ ချက်ချင်း နောက်၌» («one's own mind»; 6-01, 6-02,
    10-05 … 10-07, 10-12; 92 places). The Pāli is the same phrase in every place: yassa is the relative pronoun in
    agreement with cittassa («immediately after which mind»), whatever the main clause's subject is (the last mind
    «… pacchimacittaṃ uppajjissati» or the persons «… aggamaggaṃ paṭilabhissanti»), and the Pāli has no word for
    «own» (မိမိ). The rails take the one rendering that reads the Pāli as written, the majority correlative
    «အကြင်စိတ်၏ ချက်ချင်း နောက်၌», already used without a following «ထိုစိတ်၏» in the persons frames of ch. 5 / 9 / 10-09 …
    10-11 («အကြင်စိတ်၏ ချက်ချင်း နောက်၌ အမြတ်ဆုံး မဂ်ကို ရရှိမည့်သူတို့»). cittassa «စိတ်» and anantarā «ချက်ချင်း နောက်»
    (locked terms) are unchanged. Three generator strings build the 92 places: make_ch6-8 OWN_MIND (6-01 / 6-02),
    make_ch10b OWN_CITTA (10-05 … 10-07), make_ch10c OWN_MIND (10-12).
"""

A1 = ("L01 §A1 yassa cittassa anantarā = «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (one rendering of the one Pāli phrase; "
      "the correlative yassa … cittassa as written, no «မိမိ» (own) in the Pāli; = 5-01 … 5-03, 9-01 … 9-03, 10-09 … 10-11)")

PATCHES = {
    "make_ch6-8": [
        ('OWN_MIND = new("yassa cittassa anantarā", "မိမိ စိတ်")', 'OWN_MIND = new("yassa cittassa anantarā", "အကြင်စိတ်")',
         1, A1 + ": 6-01 / 6-02 (61 places)"),
    ],
    "make_ch10b": [
        ('OWN_CITTA = f"မိမိ {CITTA}၏"', 'OWN_CITTA = f"အကြင်{CITTA}၏"', 1, A1 + ": 10-05 … 10-07 (24 places)"),
    ],
    "make_ch10c": [
        ('OWN_MIND = "မိမိ စိတ်"', 'OWN_MIND = "အကြင်စိတ်"', 1, A1 + ": 10-12 (7 places)"),
    ],
}

# ===================================================================================================================
# Review fixes 2026-11-22 (review/report-A.md, report-B.md, report-C.md; decisions review/fix-brief.md; results
# review/fix-notes.md). Families L02 …; each patch names its fix ID.
# ===================================================================================================================
C1 = ("L02 C1 «S ṭhapetvā avaseso / avasesaṃ / avasesā N, na S.» keeps its head noun N: «Sကို ချန်ထား၍၊ ကြွင်းကျန်သော "
      "Nသည် N ဖြစ်သည်၊ S မဟုတ်။» (the remaining N, not «the remaining thing(s)», which said that everything else is N); "
      "number from N's own term (avasesā upekkhā = «ကြွင်းကျန်သော ဥပေက္ခာသည်», as «Avasesā upekkhā na indriyaṃ» "
      "^6-10-140; avasesā saṅkhārā plural); = «Avasesaṃ sotaṃ / Avaseso kāyo na indriyaṃ» «ကြွင်းကျန်သော နား / ကိုယ်»")


def _add(name, *entries):
    PATCHES.setdefault(name, []).extend(entries)


_add("make_ch9-10a",
     ('        sub, pl = av_subj(m["av"], m["k"])\n        sep = C',
      '        sub, pl = av_subj(m["av"], m["k"] or m["a"])\n        sep = C', 1, C1 + ": 10-01 (Y1 / Y1C frame)"))
_add("make_ch2-02-4-5",
     ('        sub, pl = av_subj(m["av"], m["k"])\n        return f"{F.leave(S)} {sub}သည် {A[0]}',
      '        sub, pl = av_subj(m["av"], m["k"] or m["a"])\n        return f"{F.leave(S)} {sub}သည် {A[0]}', 1,
      C1 + ": 4, 5-01 (Y1 frame)"),
     ('        A, B = T(m["a"])[0], T(m["b"])[0]\n        lv = ',
      '        A, B = T(m["a"])[0], T(m["b"])[0]\n        if m.re is XS:\n            sub, pl = f"{F.AVASESA} {A}", T(m["a"])[1]\n'
      '        lv = ', 1, C1 + ": 5-01 (XS frame, Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ)"))
_add("make_ch3",
     ('        n, pl = avas_noun(m["av"])\n        return f"{leave(S)} {n}သည် {A[0]}',
      '        n, pl = f"{F.AVASESA} {A[0]}", A[1]\n        return f"{leave(S)} {n}သည် {A[0]}', 1, C1 + ": 3-01 (P1B frame)"))
_add("my6_formulas",
     ("        return (f\"{leave(S)} {AVASESA_N}သည် {A[0]}{m['v'] or ''} {BE}ကြသည်{C} {isnt(B[0], True)}{END}\")",
      "        return (f\"{leave(S)} {AVASESA} {A[0]}သည် {A[0]}{m['v'] or ''} {BE}{ko(A)}သည်{C} {isnt(B[0], A[1])}{END}\")",
      1, C1 + ": 2-01 (P1B frame, avasesā saṅkhārā)"))

B2 = ("L03 B2 «yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati»: the genitive plural kāmāvacarānaṃ "
      "names the beings (termbase kāmāvacarānaṃ, beings sense; = «ကာမဘုံ၌ ရှိသူတို့» elsewhere in the same sentences): "
      "«အကြင်စိတ်၏ ချက်ချင်း နောက်၌ နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ကာမဘုံ၌ ရှိသူတို့» (was «… ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး "
      "စိတ် ဖြစ်ပေါ်မည့်သူတို့»); the frame has no rūpāvacarānaṃ / arūpāvacarānaṃ (script: 24 lines, all kāmāvacarānaṃ)")
B4 = ("L04 B4 «… ye ca … upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ» in the 6-01 / 6-02 frame: the apposition "
      "without «အနက်» (among), «… ပရိနိဗ္ဗာန် ပြုမည့်သူတို့၊ စုတေဆဲ ထိုသူတို့အား» (tesaṃ picks up every group)")
_add("make_ch6-8",
     ('        obj = REL_OBJ[tl[i + 3]]\n        v = F.V(toks[i + 5], "attr")\n',
      '        v = F.V(toks[i + 5], "attr")\n        if tl[i + 3] == "kāmāvacarānaṃ":\n'
      '            return f"{OWN_MIND}{ANANTARA} {PACCHIMA_CITTA} {v} {F._one_group([toks[i + 3]])}", i + 6\n'
      '        obj = REL_OBJ[tl[i + 3]]\n', 1, B2 + ": 6-01 / 6-02"),
     ("                out += f\"{AMONG} {F.PART['cavantānaṃ'][0]}{F.THEM}\"",
      "                out += f\"{C} {F.PART['cavantānaṃ'][0]} ထို{F.THEM}\"", 1, B4 + ": 6-01 / 6-02"))

A1R = ("L05 A1 the rūpa word-play «Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho» (and the paccanīka «… na rūpakkhandho, "
       "rūpaṃ»): rūpaṃ = «“ရူပ” (ရုပ် သို့မဟုတ် သဘော)», as the sota word-play «“သောတ” (နား သို့မဟုတ် ရေစီး)»; the "
       "quote marks a Pāli word being mentioned (kept kind of the quote rule)")
_RUPA = "(\"“ရူပ” (ရုပ် သို့မဟုတ် သဘော)\" if m['s'] == 'Piyarūpaṃ sātarūpaṃ' and m['a'] == 'rūpaṃ' else A[0])"
_add("my6_formulas",
     ("        return f\"{SPECIAL_SUBJ[m['s']]}သည် {is_(A[0], False)}{C} {isnt(B[0], False)}{END}\"",
      "        return f\"{SPECIAL_SUBJ[m['s']]}သည် {is_(" + _RUPA + ", False)}{C} {isnt(B[0], False)}{END}\"", 1,
      A1R + ": 2-01 P1 frame (^6-2-26, ^6-2-28)"),
     ("        return f\"{SPECIAL_SUBJ[m['s']]}သည် {isnt(B[0], False)}{C} {is_(A[0], False)}{END}\"",
      "        return f\"{SPECIAL_SUBJ[m['s']]}သည် {isnt(B[0], False)}{C} {is_(" + _RUPA + ", False)}{END}\"", 1,
      A1R + ": 2-01 P4 frame (^6-2-27)"))

B1 = ("L06 B1 the dhātu / vedanā lists ending in apariyāpanne: «၊» before the apariyāpanna item instead of «နှင့်» "
      "(«… ရုပ်ဘုံ၊ ရုပ်မရှိသော ဘုံ၊ ဘဝဘုံတို့၌ အကျုံးမဝင်သော အရာ», «နာကျင်သော ခံစားမှု၊ ဘဝဘုံတို့၌ …»; = the two places "
      "in 7-06 / 7-08 that already had «၊»), so the list does not read as «A and B» inside the apariyāpanna scope")
_add("make_ch7a",
     ('    return f"{C} ".join(its[:-1]) + f"{AND} " + its[-1]',
      '    return f"{C} ".join(its[:-1]) + (f"{C} " if keys[-1] == ("apariyāpanne",) else f"{AND} ") + its[-1]', 1,
      B1 + ": places_my (7-01 … 7-11, also through make_ch7b)"))
_add("make_ch7b",
     ('        k = f"{PLACE_KT}{F.AND} {PLACE_AP}"', '        k = f"{PLACE_KT}{F.C} {PLACE_AP}"', 1,
      B1 + ": the harmonise A4 «,» line (7-08) now already has «၊» from places_my"))

A2 = ("L07 A2 / B6 / C5 bare Sabbesaṃ before a moment = «သူအားလုံးတို့၏ …» (one word, no stray space; was «သူ အားလုံးတို့၏»; "
      "the participle form «…ဆဲသူ အားလုံးတို့» is not this rendering and stays; «သူ အားလုံးတို့» does not occur in pi-1 … pi-5)")
for _g, _w in (("make_ch2-02-4-5", "5-01 … 5-03"), ("make_ch6-8", "6-01, 6-02, 8"), ("make_ch9-10a", "9-01 … 10-04"),
               ("make_ch10b", "10-05 … 10-09"), ("make_ch10c", "10-10 … 10-13")):
    _add(_g, ('f"{F.ALL_OF}၏ "', 'f"{F.ALL_OF.replace(\' \', \'\')}၏ "', 1, A2 + ": " + _w))

C6 = ("L08 C6 «yassa cittassa anantarā (X-)pacchimacittaṃ uppajjissati tassa cittassa …kkhaṇe»: the relative verb is "
      "attributive, «… နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့် ထိုစိတ်၏ …» (was the finite «… ဖြစ်ပေါ်လိမ့်မည်၊ ထိုစိတ်၏ …», which reads "
      "as an assertion); = the 5-xx / 9-xx relative «… ရရှိမည့်»")
_add("make_ch10b",
     ("        my = (f\"{YASSA_CITTA[0]} {ANANTARA} {ACC_CITTA[toks[j + 3]]} {F.V(v, 'cl')}{C} \"",
      "        my = (f\"{YASSA_CITTA[0]} {ANANTARA} {ACC_CITTA[toks[j + 3]]} {F.V(v, 'attr')} \"", 1, C6 + ": 10-09"))
_add("make_ch10c",
     ('        v = F.V(toks[j + 4], "cl")\n', '        v = F.V(toks[j + 4], "attr")\n', 1, C6 + ": 10-10, 10-11"),
     ("{x}{PACCHIMA} {CITTA} {v}{C} {TAM_CITTA}၏", "{x}{PACCHIMA} {CITTA} {v} {TAM_CITTA}၏", 1, C6 + ": 10-10, 10-11"))

A4 = ("L09 A4 cakkaṃ bandhitabbaṃ = «လှည့်ပတ်ခြင်းကို ဖွဲ့ရမည်» without the added «အပြည့်အစုံ» (fully; no Pāli word), in every "
      "note that has it (= «… လှည့်ပတ်ခြင်းကို ဖွဲ့ထားသကဲ့သို့» ^6-4-4, «လှည့်ပတ်ခြင်းကို ဖွဲ့သောအခါ» ^6-3-13)")
_add("make_ch2-02-4-5",
     ('CAKKA_B = new("cakkaṃ bandhitabbaṃ", f"{F.CAKKA}ကို အပြည့်အစုံ ဖွဲ့ရမည်")',
      'CAKKA_B = new("cakkaṃ bandhitabbaṃ", f"{F.CAKKA}ကို ဖွဲ့ရမည်")', 1, A4 + ": 4 (CAKKA_B)"))
_add("make_ch3",
     ('CAKKA_BIND = f"{F.CAKKA}ကို အပြည့်အစုံ ဖွဲ့ရမည်"', 'CAKKA_BIND = f"{F.CAKKA}ကို ဖွဲ့ရမည်"', 1, A4 + ": 3-01 (CAKKA_BIND)"),
     ('ကို မရောထွေးစေဘဲ အပြည့်အစုံ ဖွဲ့ရမည်)"', 'ကို မရောထွေးစေဘဲ ဖွဲ့ရမည်)"', 1, A4 + ": ^6-3-12 (Ekekapadamūlakaṃ …)"))
