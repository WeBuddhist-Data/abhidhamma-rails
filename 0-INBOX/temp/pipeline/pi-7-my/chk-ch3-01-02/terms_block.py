# dyad terms (the pi-1 Mātikā values ^1-M2-1 … ^1-M2-13, typed here again; two NEW for the nahetu-sahetuka dyad)
TERMS_MY = {
    "hetu": {"hetu": "အမြစ် ဖြစ်သော", "nahetu": "အမြစ် မဟုတ်သော"},
    "sahetuka": {"sahetuka": "အမြစ် ရှိသော", "ahetuka": "အမြစ် မရှိသော"},
    "hetusamp": {"hetusampayutta": "အမြစ်နှင့် ယှဉ်တွဲသော", "hetuvippayutta": "အမြစ်နှင့် ကင်းကွာသော"},
    "hetusahetuka": {"hetu ceva sahetuka": "အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော",
                     "sahetuka ceva na ca hetu": "အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော"},
    "hetuhetusamp": {"hetu ceva hetusampayutta": "အမြစ်လည်း ဖြစ်၊ အမြစ်နှင့်လည်း ယှဉ်တွဲသော",
                     "hetusampayutta ceva na ca hetu": "အမြစ်နှင့် ယှဉ်တွဲသော်လည်း အမြစ် မဟုတ်သော"},
    "nahetusahetuka": {"nahetu sahetuka": "အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော",
                       "nahetu ahetuka": "အမြစ်လည်း မဟုတ်၊ အမြစ်လည်း မရှိသော"},
    "sappaccaya": {"sappaccaya": "အကြောင်း ရှိသော", "appaccaya": "အကြောင်း မရှိသော"},
    "sankhata": {"saṅkhata": "ပြုပြင်ဖန်တီးထားသော", "asaṅkhata": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော"},
    "sanidassana": {"sanidassana": "မြင်နိုင်သော", "anidassana": "မမြင်နိုင်သော"},
    "sappatigha": {"sappaṭigha": "ထိခိုက်မှု ရှိသော", "appaṭigha": "ထိခိုက်မှု မရှိသော"},
    "rupi": {"rūpī": "ရုပ် ဖြစ်သော", "arūpī": "ရုပ် မဟုတ်သော"},
    "lokiya": {"lokiya": "လောကနှင့် သက်ဆိုင်သော", "lokuttara": "လောကကို ကျော်လွန်သော"},
    "kenaci": {"kenaci viññeyya": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော",
               "kenaci naviññeyya": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော"},
}
_A = r"(?:aṃ|o|ā|ānaṃ|ānañca|añca|assa|e|ena|āya|ādhipati|acittasamaṅgissa|amūlak\w*|ā ca|o ca|e ca)"
_U = r"(?:ūnaṃ|uñca|ussa|unā|uṃ|ū|u)"
_I = r"(?:ī|iṃ|iñca|issa|ino|īnaṃ|inā|icittasamaṅgissa)"
_NOT_NAME = r"(?!\w*dukaṃ)"
# Pāli regexes of the terms of each dyad (raw Pāli, variants removed), in the order of TERMS_MY; the first regex that
# matches at a position wins (longer forms first)
TERM_PI = {
    "hetu": [(r"[Hh]et" + _U + r"(?= (?:ca )?(?:[Nn]ahet\w*(?: ca)? )?dhamm)", "hetu"),
             (r"[Nn]ahet(?:ūnaṃ|uñca|ussa|unā|uṃ|ū|ucittasamaṅgissa|umūlak\w*|u)(?!\w)", "nahetu")],
    "sahetuka": [(r"[Ss]ahetuk" + _NOT_NAME + r"\w*", "sahetuka"), (r"[Aa]hetuk\w*", "ahetuka")],
    "hetusamp": [(r"[Hh]etusampayutt" + _NOT_NAME + r"\w*", "hetusampayutta"),
                 (r"[Hh]etuvippayutt\w*", "hetuvippayutta")],
    "hetusahetuka": [(r"[Hh]et\w*(?:ñceva| ceva) sahetuk\w*?(?:ñca| ca(?!\w)|(?=ādhipati))(?:ādhipati)?",
                      "hetu ceva sahetuka"),
                     (r"[Ss]ahetuk\w*?(?:ñceva| ceva) na ca het\w*", "sahetuka ceva na ca hetu")],
    "hetuhetusamp": [(r"[Hh]et\w*(?:ñceva| ceva) hetusampayutt\w*?(?:ñca| ca(?!\w))", "hetu ceva hetusampayutta"),
                     (r"[Hh]etusampayutt\w*?(?:ñceva| ceva) na ca het\w*", "hetusampayutta ceva na ca hetu")],
    "nahetusahetuka": [(r"[Nn]ahet\w* sahetuk\w*|[Nn]ahetusahetuk" + _NOT_NAME + r"\w*", "nahetu sahetuka"),
                       (r"[Nn]ahet\w* ahetuk\w*|[Nn]ahetuahetuk\w*", "nahetu ahetuka")],
    "sappaccaya": [(r"[Ss]appaccay" + _NOT_NAME + r"(?!agaṇan)\w*", "sappaccaya"), (r"[Aa]ppaccay\w*", "appaccaya")],
    "sankhata": [(r"[Ss]aṅkhat" + _NOT_NAME + r"\w*", "saṅkhata"), (r"[Aa]saṅkhat\w*", "asaṅkhata")],
    "sanidassana": [(r"[Ss]anidassan" + _NOT_NAME + r"\w*", "sanidassana"), (r"[Aa]nidassan\w*", "anidassana")],
    "sappatigha": [(r"[Ss]appaṭigh" + _NOT_NAME + r"\w*", "sappaṭigha"), (r"[Aa]ppaṭigh\w*", "appaṭigha")],
    "rupi": [(r"[Aa]rūp" + _I + r"(?!\w)", "arūpī"), (r"[Rr]ūp" + _I + r"(?!\w)", "rūpī")],
    "lokiya": [(r"[Ll]okiy" + _NOT_NAME + r"\w*", "lokiya"), (r"[Ll]okuttar\w*", "lokuttara")],
    "kenaci": [(r"[Kk]enaci na ?viññeyy\w*", "kenaci naviññeyya"), (r"[Kk]enaci viññeyy" + _NOT_NAME + r"\w*",
                                                                     "kenaci viññeyya")],
}
# dyad names (headings, colophons, inside notes): Pāli -> Burmese (NEW names, typed here again)
NAMES_MY = {"hetuduk": "အမြစ် နှစ်မျိုးတွဲ", "sahetukaduk": "အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ",
            "hetusampayuttaduk": "အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ",
            "hetusahetukaduk": "အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ",
            "hetuhetusampayuttaduk": "အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ",
            "nahetusahetukaduk": "အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ",
            "sappaccayaduk": "အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ", "saṅkhataduk": "ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲ",
            "sanidassanaduk": "မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ", "sappaṭighaduk": "ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ",
            "rūpīduk": "ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ", "lokiyaduk": "လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ",
            "kenaciviññeyyaduk": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ"}
NAME_REF = {"sappaccayagaṇan": "sappaccayaduk"}       # a dyad named inside a note
DYAD_HEAD = {"Hetudukaṃ": "hetu", "Sahetukadukaṃ": "sahetuka", "Hetusampayuttadukaṃ": "hetusamp",
             "Hetusahetukadukaṃ": "hetusahetuka", "Hetuhetusampayuttadukaṃ": "hetuhetusamp",
             "Nahetusahetukadukaṃ": "nahetusahetuka", "Sappaccayadukaṃ": "sappaccaya", "Saṅkhatadukaṃ": "sankhata",
             "Sanidassanadukaṃ": "sanidassana", "Sappaṭighadukaṃ": "sappatigha", "Rūpīdukaṃ": "rupi",
             "Lokiyadukaṃ": "lokiya", "Kenaciviññeyyadukaṃ": "kenaci"}
