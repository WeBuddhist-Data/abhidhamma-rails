# dyad terms (the pi-1 Mātikā values ^1-M2-55 … ^1-M2-68, typed here again) and their Pāli regexes (raw Pāli)
TERMS_MY = {
    "sarammana": {"S": "အာရုံ ရှိသော", "aS": "အာရုံ မရှိသော"},
    "citta": {"C": "စိတ် ဖြစ်သော", "noC": "စိတ် မဟုတ်သော"},
    "cetasika": {"Ce": "စိတ်၏ အဖော် ဖြစ်သော", "aCe": "စိတ်၏ အဖော် မဟုတ်သော"},
    "cittasamp": {"Csamp": "စိတ်နှင့် ယှဉ်တွဲသော", "Cvipp": "စိတ်နှင့် ကင်းကွာသော"},
    "cittasams": {"Csams": "စိတ်နှင့် ရောနှောသော", "Cvisams": "စိတ်နှင့် မရောနှောသော"},
    "cittasamu": {"Csamu": "စိတ်မှ ဖြစ်ပေါ်လာသော", "noCsamu": "စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော"},
    "cittasaha": {"Csaha": "စိတ်နှင့်အတူ တည်ရှိသော", "noCsaha": "စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော"},
    "cittanu": {"Canu": "စိတ်နောက်သို့ လိုက်ပါသော", "noCanu": "စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော"},
    "css": {"Css": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော", "noCss": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော"},
    "csssaha": {"Csssaha": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသော",
                "noCsssaha": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော"},
    "cssanu": {"Cssanu": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော",
               "noCssanu": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော"},
    "ajjhattika": {"A": "အတွင်းပိုင်း", "B": "ပြင်ပ"},
    "upada": {"U": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော", "noU": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော"},
    "upadinna": {"Ud": "ကံကြောင့် ဖြစ်သော", "aUd": "ကံကြောင့် မဖြစ်သော"},
}
_E = r"(?:o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena|ādhipati|acittasamaṅgissa|asamaṅgissa|amūlak\w*)"
_NOT_NAME = r"(?!\w*(?:duk|gaman))"
_U = r"(?:ū|uṃ|uñca|ussa|ūnaṃ|ūnañca|uno|u)(?!\w)"
_I = r"(?:ī|iṃ|iñca|issa|īnaṃ|īnañca|ino|i)(?!\w)"
_CSS = "cittasaṃsaṭṭhasamuṭṭhān"
TERM_PI = {
    "sarammana": [(r"[Ss]ārammaṇ" + _E + r"(?!\w)", "S"), (r"[Aa]nārammaṇ" + _E + r"(?!\w)", "aS")],
    "citta": [(r"[Cc]itt" + _E + r"(?= (?:ca )?(?:[Nn]ocitt\w*(?: ca)? )?(?:dhamm|…))", "C"),
              (r"[Nn]ocitt" + _E + r"(?!\w)", "noC")],
    "cetasika": [(r"[Cc]etasik" + _E + r"(?!\w)", "Ce"), (r"[Aa]cetasik" + _E + r"(?!\w)", "aCe")],
    "cittasamp": [(r"[Cc]ittasampayutt(?:ak)?" + _E + r"(?!\w)", "Csamp"), (r"[Cc]ittavippayutt" + _E + r"(?!\w)", "Cvipp")],
    "cittasams": [(r"[Cc]ittasaṃsaṭṭh" + _E + r"(?!\w)", "Csams"), (r"[Cc]ittavisaṃsaṭṭh" + _E + r"(?!\w)", "Cvisams")],
    "cittasamu": [(r"[Cc]ittasamuṭṭhān" + _E + r"(?!\w)", "Csamu"), (r"[Nn]ocittasamuṭṭhān" + _E + r"(?!\w)", "noCsamu")],
    "cittasaha": [(r"[Cc]ittasahabh" + _NOT_NAME + _U, "Csaha"), (r"[Nn]ocittasahabh" + _U, "noCsaha")],
    "cittanu": [(r"[Cc]ittānuparivatt" + _NOT_NAME + _I, "Canu"), (r"[Nn]ocittānuparivatt" + _I, "noCanu")],
    "css": [(r"[Cc]" + _CSS[1:] + _E + r"(?!\w)", "Css"), (r"[Nn]o" + _CSS + _E + r"(?!\w)", "noCss")],
    "csssaha": [(r"[Cc]" + _CSS[1:] + r"asahabh" + _NOT_NAME + _U, "Csssaha"),
                (r"[Nn]o" + _CSS + r"asahabh" + _U, "noCsssaha")],
    "cssanu": [(r"[Cc]" + _CSS[1:] + r"ānuparivatt" + _NOT_NAME + _I, "Cssanu"),
               (r"[Nn]o" + _CSS + r"ānuparivatt" + _I, "noCssanu")],
    "ajjhattika": [(r"[Aa]jjhattik" + _E + r"(?!\w)", "A"), (r"[Bb]āhir" + _E + r"(?!\w)", "B")],
    "upada": [(r"[Uu]pādā(?:dhipati|cittasamaṅgissa|mūlak\w*)?(?!\w)", "U"),
              (r"[Nn]o ?upādā(?:dhipati|cittasamaṅgissa|mūlak\w*)?(?!\w)", "noU")],
    "upadinna": [(r"[Uu]pādinn" + _E + r"(?!\w)", "Ud"), (r"[Aa]nupādinn" + _E + r"(?!\w)", "aUd")],
}
DYAD_HEAD = {"Sārammaṇadukaṃ": "sarammana", "Cittadukaṃ": "citta", "Cetasikadukaṃ": "cetasika",
             "Cittasampayuttadukaṃ": "cittasamp", "Cittasaṃsaṭṭhadukaṃ": "cittasams",
             "Cittasamuṭṭhānadukaṃ": "cittasamu", "Cittasahabhūdukaṃ": "cittasaha",
             "Cittānuparivattidukaṃ": "cittanu", "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ": "css",
             "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ": "csssaha",
             "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ": "cssanu", "Ajjhattikadukaṃ": "ajjhattika",
             "Upādādukaṃ": "upada", "Upādinnadukaṃ": "upadinna"}
_DU = "နှစ်မျိုးတွဲ"
NAMES_MY = {
    "sārammaṇaduk": f"အာရုံ ရှိခြင်း {_DU}", "cittaduk": f"စိတ် ဖြစ်ခြင်း {_DU}",
    "cetasikaduk": f"စိတ်၏ အဖော် ဖြစ်ခြင်း {_DU}", "cittasampayuttaduk": f"စိတ်နှင့် ယှဉ်တွဲခြင်း {_DU}",
    "cittasaṃsaṭṭhaduk": f"စိတ်နှင့် ရောနှောခြင်း {_DU}", "cittasamuṭṭhānaduk": f"စိတ်မှ ဖြစ်ပေါ်လာခြင်း {_DU}",
    "cittasahabhūduk": f"စိတ်နှင့်အတူ တည်ရှိခြင်း {_DU}", "cittānuparivattiduk": f"စိတ်နောက်သို့ လိုက်ပါခြင်း {_DU}",
    "cittasaṃsaṭṭhasamuṭṭhānaduk": f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း {_DU}",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūduk": f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိခြင်း {_DU}",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattiduk":
        f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါခြင်း {_DU}",
    "ajjhattikaduk": f"အတွင်းပိုင်း ဖြစ်ခြင်း {_DU}", "upādāduk": f"မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း {_DU}",
    "upādinnaduk": f"ကံကြောင့် ဖြစ်ခြင်း {_DU}",
    "mahantaraduk": "ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး",
}
# dyad names inside notes in other forms («-dukasadisaṃ», «-duke», «-gamana-»)
NAME_REF = {"cittasaṃsaṭṭhasamuṭṭhānadukasadis": "cittasaṃsaṭṭhasamuṭṭhānaduk",
            "cittasamuṭṭhānadukasadis": "cittasamuṭṭhānaduk", "cittasamuṭṭhānaduke": "cittasamuṭṭhānaduk",
            "cittasahabhūdukasadis": "cittasahabhūduk", "cittasahabhūduke": "cittasahabhūduk",
            "cittasahabhūgamanasadis": "cittasahabhūduk"}
