"""INFLECTION / ARTEFACT rules of classify_misses.py (pi-6 Burmese rails; model pi-5-my/rails/classify_rules.py, read
only): (keyword regex, class, text-form regex that must match the segment, keyword-map forms (tuple) or None, reason,
Pāli check regex (a leading «!» = must NOT match) or None). The first matching rule classifies the row.
The Yamaka is formulaic: every rule is a grammar pattern of one locked term, checked on the segment text and its Pāli.
The agent-noun rule (termbase/APPROVED.md, notes-part5 5e): where the text has the attributive before another person
noun, the miss is INFLECTION, not a change."""
FUT_N = ("ချုပ်ငြိမ်းလိမ့်မည်",)
FUT_U = ("ဖြစ်ပေါ်လိမ့်မည်",)
OTHER = [
    # ---- INFLECTION: the plural verb «…ကြ…» of the future term (Burmese plural subject «သဘောတရားများ / …သူတို့»)
    (r"(?i)nirujjhissanti|nirujjhissantīti", "INFLECTION", r"ချုပ်ငြိမ်းကြလိမ့်မည်", FUT_N,
     "plural «ချုပ်ငြိမ်းကြလိမ့်မည်» of the termbase future «ချုပ်ငြိမ်းလိမ့်မည်» (decision nirujjhissanti|0, the chosen "
     "departure «…လိမ့်မည်»; the plural marker «ကြ» stands between verb and future ending, which the loose test cannot "
     "strip; the keyword map's own value is the term)", r"(?i)nirujjhissant"),
    (r"(?i)uppajjissanti|uppajjissantīti", "INFLECTION", r"ဖြစ်ပေါ်ကြလိမ့်မည်", FUT_U,
     "plural «ဖြစ်ပေါ်ကြလိမ့်မည်» of the termbase future «ဖြစ်ပေါ်လိမ့်မည်» (pi-5 locked Uppajjissati; the plural marker "
     "«ကြ» between verb and future ending; the keyword map's own value is the term)", r"(?i)uppajjissant"),
    # ---- INFLECTION: the future participle in the relative clause «… pacchimacittaṃ uppajjissati» (persons)
    (r"uppajjissati", "INFLECTION", r"နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့်(?:သူ| ကာမဘုံ၌ ရှိသူ)", ("ဖြစ်ပေါ်မည့်",),
     "future participle «… ဖြစ်ပေါ်မည့်သူတို့» of the termbase «ဖြစ်ပေါ်လိမ့်မည်» in the relative clause «yassa cittassa "
     "anantarā … pacchimacittaṃ uppajjissati» (decision uppajjissati|0: «the future participle in a relative clause … "
     "grammar»)", r"pacchimacittaṃ uppajjissati"),
    # ---- INFLECTION: review fix B4 (6-01 / 6-02): the apposition «… ပြုမည့်သူတို့၊ စုတေဆဲ ထိုသူတို့အား» = the attributive
    #      «စုတေဆဲ» of the agent noun before the person noun «ထိုသူတို့» (APPROVED.md key choice 1, agent-noun rule)
    (r"(?i)cavantānaṃ|cavantīnaṃ", "INFLECTION", r"တို့၊ စုတေဆဲ ထို(?:သူ|မိန်းမ)တို့", None,
     "attributive «စုတေဆဲ» before the person noun «ထိုသူတို့» in the apposition «… parinibbāyissanti tesaṃ cavantānaṃ» "
     "(review fix B4, fix-brief.md: no «အနက်»; agent-noun rule, APPROVED.md: the attributive before a person noun is "
     "INFLECTION); B4-ext book-wide (coordinator 2026-11-23): every «… -issanti tesaṃ / tāsaṃ cavant…»", r"(?i)issanti (?:tesaṃ|tāsaṃ) cavant"),
    (r"(?i)upapajjantānaṃ|upapajjantīnaṃ", "INFLECTION", r"တို့၊ ပြန်လည် ဖြစ်ပေါ်ဆဲ ထို(?:သူ|မိန်းမ)တို့", None,
     "attributive «ပြန်လည် ဖြစ်ပေါ်ဆဲ» before the person noun «ထိုသူတို့ / ထိုမိန်းမတို့» in the apposition «… -issanti tesaṃ / "
     "tāsaṃ upapajjant…» (review fix B4-ext, no «အနက်»; agent-noun rule, APPROVED.md)", r"(?i)issanti (?:tesaṃ|tāsaṃ) upapajjant"),
    # ---- INFLECTION: the negative of the joined term stays spaced (§A13, termbase notes-part5 5a / B13)
    (r"(?i)sacchikarissati|sacchikarissanti|sacchikarissatīti|sacchikarittha|sacchikaritthāti", "INFLECTION",
     r"မျက်မှောက် မပြု", None,
     "negative «မျက်မှောက် မပြု…» of the joined termbase «မျက်မှောက်ပြု…» (§A13 decided: positive joined, the negative "
     "stays spaced in the text, B13)", r"(?i)na sacchikar"),
    # ---- INFLECTION: the attributive of the agent noun before another person noun (APPROVED.md key choice 1)
    (r"upapajjantānaṃ", "INFLECTION", r"ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသူ", ("ပြန်လည် ဖြစ်ပေါ်ဆဲ",),
     "attributive «ပြန်လည် ဖြစ်ပေါ်ဆဲ» before the person noun «နောက်ဆုံး ဘဝ ရှိသူတို့» (Pacchimabhavikānaṃ … "
     "upapajjantānaṃ; decision upapajjantānaṃ|0: «…ဆဲ is the attributive before နောက်ဆုံး ဘဝ ရှိသူ (grammar)»)",
     r"(?i)pacchimabhavikānaṃ (?:\w+ ){0,2}upapajjantānaṃ"),
    (r"pañcavokārānaṃ", "INFLECTION", r"အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသော အခြားသူ",
     ("အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသော",),
     "attributive «… ဘဝ၌ ရှိသော» before «အခြားသူတို့» (Itaresaṃ catuvokārānaṃ pañcavokārānaṃ; decision "
     "pañcavokārānaṃ|0: «… ရှိသော is the attributive before အခြားသူ (grammar)»)",
     r"(?i)itaresaṃ catuvokārānaṃ pañcavokārānaṃ"),
    (r"(?i)abhisametāvīnaṃ|anabhisametāvīnaṃ", "INFLECTION",
     r"ထင်ထင်ရှားရှား (?:မ)?သိမြင်(?:ပြီး|ရသေး)သော (?:ပြန်လည် ဖြစ်ပေါ်ဆဲ|စုတေဆဲ)သူ", None,
     "attributive «ထင်ထင်ရှားရှား (မ)သိမြင်(ပြီး / ရသေး)သော» before the person noun «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ / စုတေဆဲသူ» "
     "((an)abhisametāvīnaṃ upapajjantānaṃ / cavantānaṃ; decisions abhisametāvīnaṃ|0 / anabhisametāvīnaṃ|0: «…သော before "
     "another person noun (grammar)»)", r"(?i)abhisametāvīnaṃ (?:upapajjantānaṃ|cavantānaṃ)"),
    (r"(?i)pacchimabhavikānaṃ", "INFLECTION", r"နောက်ဆုံး ဘဝ ရှိသော (?:မိန်းမ|ယောက်ျား)", ("နောက်ဆုံး ဘဝ ရှိသော",),
     "attributive «နောက်ဆုံး ဘဝ ရှိသော» before «မိန်းမတို့ / ယောက်ျားတို့» (Pacchimabhavikānaṃ itthīnaṃ / purisānaṃ; "
     "decision pacchimabhavikānaṃ|0: «… ရှိသော is the attributive before မိန်းမတို့ / ယောက်ျားတို့ (grammar)»)",
     r"(?i)pacchimabhavikānaṃ (?:itthīnaṃ|purisānaṃ)"),
    (r"(?i)itaresaṃ", "INFLECTION", r"အခြား ယောက်ျား", ("အခြား",),
     "attributive «အခြား» before «ယောက်ျားတို့» (Itaresaṃ purisānaṃ; decision itaresaṃ|0: «အခြား is the attributive "
     "before ယောက်ျားတို့ (10-09, grammar)»)", r"(?i)itaresaṃ purisānaṃ"),
]
STALE_SUBS = []      # no stale phrase entry (the termbase was built from this zero-shot's keyword map)
STALE_NO = set()
CONTEXT = []         # no context sense
