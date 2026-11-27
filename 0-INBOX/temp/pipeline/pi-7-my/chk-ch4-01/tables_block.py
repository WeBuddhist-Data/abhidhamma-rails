# dyad terms (the pi-1 Mātikā values ^1-M2-75 … ^1-M2-100, typed here again; two NEW for the eighth kilesa dyad)
_K = "ကိလေသာ"
TERMS_MY = {
    "kil1": {"kilesa": f"{_K} ဖြစ်သော", "nokilesa": f"{_K} မဟုတ်သော"},
    "kil2": {"saṃkilesika": f"{_K}၏ အာရုံ ဖြစ်နိုင်သော", "asaṃkilesika": f"{_K}၏ အာရုံ မဖြစ်နိုင်သော"},
    "kilS": {"saṃkiliṭṭha": f"{_K}ဖြင့် ညစ်နွမ်းသော", "asaṃkiliṭṭha": f"{_K}ဖြင့် မညစ်နွမ်းသော"},
    "kilP": {"kilesasampayutta": f"{_K}နှင့် ယှဉ်တွဲသော", "kilesavippayutta": f"{_K}နှင့် ကင်းကွာသော"},
    "kil4": {"kilesa ceva saṃkilesika": f"{_K}လည်း ဖြစ်၊ {_K}၏ အာရုံလည်း ဖြစ်နိုင်သော",
             "saṃkilesika ceva no ca kilesa": f"{_K}၏ အာရုံ ဖြစ်နိုင်သော်လည်း {_K} မဟုတ်သော"},
    "kilB": {"kilesa ceva saṃkiliṭṭha": f"{_K}လည်း ဖြစ်၊ {_K}ဖြင့်လည်း ညစ်နွမ်းသော",
             "saṃkiliṭṭha ceva no ca kilesa": f"{_K}ဖြင့် ညစ်နွမ်းသော်လည်း {_K} မဟုတ်သော"},
    "kil5": {"kilesa ceva kilesasampayutta": f"{_K}လည်း ဖြစ်၊ {_K}နှင့်လည်း ယှဉ်တွဲသော",
             "kilesasampayutta ceva no ca kilesa": f"{_K}နှင့် ယှဉ်တွဲသော်လည်း {_K} မဟုတ်သော"},
    "kil6": {"kilesavippayutta saṃkilesika": f"{_K}နှင့် ကင်းကွာသော်လည်း {_K}၏ အာရုံ ဖြစ်နိုင်သော",
             "kilesavippayutta asaṃkilesika": f"{_K}နှင့် ကင်းကွာ၊ {_K}၏ အာရုံ မဖြစ်နိုင်သော"},
    "dass": {"dassanena pahātabba": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့်",
             "nadassanena pahātabba": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော"},
    "bhav": {"bhāvanāya pahātabba": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်",
             "nabhāvanāya pahātabba": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော"},
    "dassh": {"dassanena pahātabbahetuka": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
              "nadassanena pahātabbahetuka": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော"},
    "bhavh": {"bhāvanāya pahātabbahetuka": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
              "nabhāvanāya pahātabbahetuka": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော"},
    "vitakka": {"savitakka": "စတင်ကြံစည်မှု ရှိသော", "avitakka": "စတင်ကြံစည်မှု မရှိသော"},
    "vicara": {"savicāra": "ဆက်လက်သုံးသပ်မှု ရှိသော", "avicāra": "ဆက်လက်သုံးသပ်မှု မရှိသော"},
    "sappitika": {"sappītika": "ပီတိ ရှိသော", "appītika": "ပီတိ မရှိသော"},
    "piti": {"pītisahagata": "ပီတိနှင့်အတူ ဖြစ်သော", "napītisahagata": "ပီတိနှင့်အတူ ဖြစ်သည် မဟုတ်သော"},
    "sukha": {"sukhasahagata": "သာယာမှုနှင့်အတူ ဖြစ်သော", "nasukhasahagata": "သာယာမှုနှင့်အတူ ဖြစ်သည် မဟုတ်သော"},
    "upekkha": {"upekkhāsahagata": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
                "naupekkhāsahagata": "ဥပေက္ခာနှင့်အတူ ဖြစ်သည် မဟုတ်သော"},
    "kama": {"kāmāvacara": "ကာမဘုံနှင့် ဆိုင်သော", "nakāmāvacara": "ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော"},
    "rupa": {"rūpāvacara": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "narūpāvacara": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည် မဟုတ်သော"},
    "arupa": {"arūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "naarūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော"},
    "pariyapanna": {"pariyāpanna": "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "apariyāpanna": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော"},
    "niyyanika": {"niyyānika": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "aniyyānika": "လွတ်မြောက်ရာသို့ မပို့ဆောင်သော"},
    "niyata": {"niyata": "ကျိန်းသေသော", "aniyata": "မကျိန်းသေသော"},
    "sauttara": {"sauttara": "ထိုထက် သာလွန်သည် ရှိသေးသော", "anuttara": "ထိုထက် သာလွန်သည် မရှိသော"},
    "sarana": {"saraṇa": "ပဋိပက္ခ ရှိသော", "araṇa": "ပဋိပက္ခ မရှိသော"},
}
_E = r"(?:o|aṃ|assa|ā|ānaṃ|añca|e)"
_ND = r"(?!aduk)\w*"                          # not a dyad name («savitakkadukaṃ»)


def _cap(w):
    return f"[{w[0].upper()}{w[0]}]" + w[1:]


# Pāli regexes of the terms of each dyad (raw Pāli, variants removed), longer forms first
TERM_PI = {
    "kil1": [(r"[Kk]iles" + _E + r"(?= (?:ca )?(?:[Nn]okiles\w*(?: ca)? )?(?:dhamm|hetū?(?!\w)))|[Kk]ilesādhipati",
              "kilesa"), (r"[Nn]okiles\w*", "nokilesa")],
    "kil2": [(r"[Aa]saṃkilesik\w*", "asaṃkilesika"), (r"[Ss]aṃkilesik" + _ND, "saṃkilesika")],
    "kilS": [(r"[Aa]saṃkiliṭṭh\w*", "asaṃkiliṭṭha"), (r"[Ss]aṃkiliṭṭh" + _ND, "saṃkiliṭṭha")],
    "kilP": [(r"[Kk]ilesasampayutt" + _ND, "kilesasampayutta"), (r"[Kk]ilesavippayutt\w*", "kilesavippayutta")],
    "kil4": [(r"[Kk]iles\w*?(?:ñceva| ceva) saṃkilesik\w*?(?:ñca| ca(?!\w))", "kilesa ceva saṃkilesika"),
             (r"[Ss]aṃkilesik\w*?(?:ñceva| ceva) no ca kiles\w*", "saṃkilesika ceva no ca kilesa")],
    "kilB": [(r"[Kk]iles\w*?(?:ñceva| ceva) saṃkiliṭṭh\w*?(?:ñca| ca(?!\w))", "kilesa ceva saṃkiliṭṭha"),
             (r"[Ss]aṃkiliṭṭh\w*?(?:ñceva| ceva) no ca kiles\w*", "saṃkiliṭṭha ceva no ca kilesa")],
    "kil5": [(r"[Kk]iles\w*?(?:ñceva| ceva) kilesasampayutt\w*?(?:ñca| ca(?!\w))", "kilesa ceva kilesasampayutta"),
             (r"[Kk]ilesasampayutt\w*?(?:ñceva| ceva) no ca kiles\w*", "kilesasampayutta ceva no ca kilesa")],
    "kil6": [(r"[Kk]ilesavippayutt\w* asaṃkilesik\w*", "kilesavippayutta asaṃkilesika"),
             (r"[Kk]ilesavippayutt\w* saṃkilesik\w*", "kilesavippayutta saṃkilesika")],
}
_PLAIN = {  # dyad -> [(stem regex, key)] for the piṭṭhiduka (a term is any form of its stem; not a dyad name)
    "dass": [("[Nn]adassanena pahātabb", "nadassanena pahātabba"), ("[Dd]assanena pahātabb", "dassanena pahātabba")],
    "bhav": [("[Nn]abhāvanāya pahātabb", "nabhāvanāya pahātabba"), ("[Bb]hāvanāya pahātabb", "bhāvanāya pahātabba")],
    "dassh": [("[Nn]adassanena pahātabbahetuk", "nadassanena pahātabbahetuka"),
              ("[Dd]assanena pahātabbahetuk", "dassanena pahātabbahetuka")],
    "bhavh": [("[Nn]abhāvanāya pahātabbahetuk", "nabhāvanāya pahātabbahetuka"),
              ("[Bb]hāvanāya pahātabbahetuk", "bhāvanāya pahātabbahetuka")],
    "vitakka": [("[Ss]avitakk", "savitakka"), ("[Aa]vitakk", "avitakka")],
    "vicara": [("[Ss]avicār", "savicāra"), ("[Aa]vicār", "avicāra")],
    "sappitika": [("[Ss]appītik", "sappītika"), ("[Aa]ppītik", "appītika")],
    "piti": [("[Nn]apītisahagat", "napītisahagata"), ("[Pp]ītisahagat", "pītisahagata")],
    "sukha": [("[Nn]asukhasahagat", "nasukhasahagata"), ("[Ss]ukhasahagat", "sukhasahagata")],
    "upekkha": [("[Nn]aupekkhāsahagat", "naupekkhāsahagata"), ("[Uu]pekkhāsahagat", "upekkhāsahagata")],
    "kama": [("[Nn]akāmāvacar", "nakāmāvacara"), ("[Kk]āmāvacar", "kāmāvacara")],
    "rupa": [("[Nn]arūpāvacar", "narūpāvacara"), ("[Rr]ūpāvacar", "rūpāvacara")],
    "arupa": [("[Nn]aarūpāvacar", "naarūpāvacara"), ("[Aa]rūpāvacar", "arūpāvacara")],
    "pariyapanna": [("[Aa]pariyāpann", "apariyāpanna"), ("[Pp]ariyāpann", "pariyāpanna")],
    "niyyanika": [("[Aa]niyyānik", "aniyyānika"), ("[Nn]iyyānik", "niyyānika")],
    "niyata": [("[Aa]niyat", "aniyata"), ("[Nn]iyat", "niyata")],
    "sauttara": [("[Ss]auttar", "sauttara"), ("[Aa]nuttar", "anuttara")],
    "sarana": [("[Ss]araṇ", "saraṇa"), ("[Aa]raṇ", "araṇa")],
}
for _d, _rx in _PLAIN.items():
    TERM_PI[_d] = [(st + _ND, k) for st, k in _rx]
# the dyads whose terms are named in each other's parts (a sentence or note of a sister dyad): a line is read with the
# terms of its whole family (Pāli and Burmese alike)
FAMILY = [("dass", "bhav", "dassh", "bhavh"), ("vitakka", "vicara"), ("sappitika", "piti", "sukha", "upekkha"),
          ("kama", "rupa", "arupa")]
FAM = {d: f for f in FAMILY for d in f}
assert all(k in TERMS_MY[d] for d, rxs in TERM_PI.items() for _, k in rxs)
# Burmese strings that contain a term value but are not that term (masked before the term count)
MY_MASK = ["မှားယွင်းမှု၌ ကျိန်းသေသော"]                                # micchattaniyata (2-10)
# dyad names (headings, colophons, inside notes): Pāli stem -> Burmese (NEW names, typed here again)
_AR, _KS = "၏ အာရုံ ဖြစ်နိုင်ခြင်း", "ဖြင့် ညစ်နွမ်းခြင်း"
_DN = "နှစ်မျိုးတွဲ"
NAMES_MY = {"lokiyaduk": f"လောကနှင့် သက်ဆိုင်ခြင်း {_DN}",
            "kilesaduk": f"{_K} {_DN}", "saṃkilesikaduk": f"{_K}{_AR} {_DN}", "saṃkiliṭṭhaduk": f"{_K}{_KS} {_DN}",
            "kilesasampayuttaduk": f"{_K}နှင့် ယှဉ်တွဲခြင်း {_DN}",
            "kilesasaṃkilesikaduk": f"{_K} ဖြစ်ခြင်းနှင့် {_K}{_AR} {_DN}",
            "kilesasaṃkiliṭṭhaduk": f"{_K} ဖြစ်ခြင်းနှင့် {_K}{_KS} {_DN}",
            "kilesakilesasampayuttaduk": f"{_K} ဖြစ်ခြင်းနှင့် {_K}နှင့် ယှဉ်တွဲခြင်း {_DN}",
            "kilesavippayuttasaṃkilesikaduk": f"{_K}နှင့် ကင်းကွာခြင်းနှင့် {_K}{_AR} {_DN}",
            "dassanenapahātabbaduk": f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း {_DN}",
            "bhāvanāyapahātabbaduk": f"ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း {_DN}",
            "dassanenapahātabbahetukaduk": f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် {_DN}",
            "bhāvanāyapahātabbahetukaduk": f"ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် {_DN}",
            "savitakkaduk": f"စတင်ကြံစည်မှု ရှိခြင်း {_DN}", "savicāraduk": f"ဆက်လက်သုံးသပ်မှု ရှိခြင်း {_DN}",
            "sappītikaduk": f"ပီတိ ရှိခြင်း {_DN}", "pītisahagataduk": f"ပီတိနှင့်အတူ ဖြစ်ခြင်း {_DN}",
            "sukhasahagataduk": f"သာယာမှုနှင့်အတူ ဖြစ်ခြင်း {_DN}",
            "upekkhāsahagataduk": f"ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း {_DN}",
            "kāmāvacaraduk": f"ကာမဘုံနှင့် ဆိုင်ခြင်း {_DN}", "rūpāvacaraduk": f"သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း {_DN}",
            "arūpāvacaraduk": f"ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း {_DN}",
            "pariyāpannaduk": f"ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း {_DN}",
            "niyyānikaduk": f"လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း {_DN}", "niyataduk": f"ကျိန်းသေခြင်း {_DN}",
            "sauttaraduk": f"ထိုထက် သာလွန်သည် ရှိခြင်း {_DN}", "saraṇaduk": f"ပဋိပက္ခ ရှိခြင်း {_DN}",
            # as written inside the notes: «dassanaduka» (the dassanena pahātabba dyad), «arūpaduka»
            "dassanaduk": f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း {_DN}", "arūpaduk": f"ရုပ်မရှိသော ဘုံ {_DN}"}
# names written with a space or before a compound member (regex -> NAMES_MY key)
NAME_REF = {r"dassanena pahātabbahetukaduk(?=a)": "dassanenapahātabbahetukaduk",
            r"sappītikaduk(?=apaccayavāra)": "sappītikaduk"}
_DUKA_HEAD = ["Kilesadukaṃ", "Saṃkilesikadukaṃ", "Saṃkiliṭṭhadukaṃ", "Kilesasampayuttadukaṃ", "Kilesasaṃkilesikadukaṃ",
              "Kilesasaṃkiliṭṭhadukaṃ", "Kilesakilesasampayuttadukaṃ", "Kilesavippayuttasaṃkilesikadukaṃ",
              "Dassanenapahātabbadukaṃ", "Bhāvanāyapahātabbadukaṃ", "Dassanenapahātabbahetukadukaṃ",
              "Bhāvanāyapahātabbahetukadukaṃ", "Savitakkadukaṃ", "Savicāradukaṃ", "Sappītikadukaṃ", "Pītisahagatadukaṃ",
              "Sukhasahagatadukaṃ", "Upekkhāsahagatadukaṃ", "Kāmāvacaradukaṃ", "Rūpāvacaradukaṃ", "Arūpāvacaradukaṃ",
              "Pariyāpannadukaṃ", "Niyyānikadukaṃ", "Niyatadukaṃ", "Sauttaradukaṃ", "Saraṇadukaṃ"]
DYAD_HEAD = dict(zip(_DUKA_HEAD, ["kil1", "kil2", "kilS", "kilP", "kil4", "kilB", "kil5", "kil6", "dass", "bhav",
                                  "dassh", "bhavh", "vitakka", "vicara", "sappitika", "piti", "sukha", "upekkha",
                                  "kama", "rupa", "arupa", "pariyapanna", "niyyanika", "niyata", "sauttara", "sarana"]))
