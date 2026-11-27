# ---- FUNCS-BEGIN
_W = r"(?![a-zāīūṃṅñṭḍṇḷ])"           # end of a Pāli word


def has(*words):
    """True when every Burmese string is in the text."""
    return lambda my: all(w in my for w in words)


def first_in_text(*vals):
    """the candidate whose first « … » part stands earliest in the text (one sense per segment: the first)."""
    def f(kw, pali, my):
        pos = [(my.find(v.split(" … ")[0]), i, v) for i, v in enumerate(vals) if v.split(" … ")[0] in my]
        return min(pos)[2] if pos else vals[-1]
    return f


def if_text(word, value, other="@prior"):
    """value where the text has the Burmese word, else other (default: the pi-1 … pi-4 value present)."""
    return lambda kw, pali, my: value if word in my else other


def by_first_checked(stems, fallbacks):
    """by_first, the value checked against the text: when the first stem's sense is not in the segment's Burmese,
    the first fallback that is (one sense per segment, the text's own word)."""
    def f(kw, pali, my):
        v = first_compound(strip_brackets(pali), stems)
        if v is not None and presence(v, my)[0]:
            return v
        for w in fallbacks:
            if w == "@prior" or presence(w, my)[0]:
                return w
        return fallbacks[-1]
    return f


def f_roman(kw, pali, my):
    """pi-3 M2: a keyword that stands only inside a Roman-script variant bracket has no Burmese."""
    rx = r"(?<![a-zāīūṃṅñṭḍṇḷ])" + re.escape(low(kw)) + _W
    return NONE if not re.search(rx, strip_brackets(pali), flags=re.I) else "@prior"


def f_miccha(kw, pali, my):
    """micchā: the verdict «…ti micchā» = «မှားသည်» (text «…ဟူသည် မှားသည်»), the verdict «idaṃ te micchā» = «အမှား»
    («… သင်၏ အမှား ဖြစ်သည်»), the compound member (micchādiṭṭhi …) = «မှားယွင်းသော» (pi-1 … pi-4); one sense per
    segment, the first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [(r"micchā(?=[a-zāīūṃṅñṭḍṇḷ])", "မှားယွင်းသော"), (r"te micchā" + _W, "အမှား"),
                           (r"micchā" + _W, "မှားသည်")])
    for c in [v, "မှားသည်", "အမှား", "မှားယွင်းသော"]:
        if c and presence(c, my)[0]:
            return c
    return "@prior"


def f_rupa(kw, pali, my):
    """rūpa (compound member), one sense per segment by the first compound (pi-3 / pi-4 f_rupa): the fine-material
    plane «သိမ်မွေ့သော ရုပ်» (rūpāvacara, rūpabhava, rūpadhātuyā as a plane, rūparāga …), the visible object
    «အဆင်းအရောင်» (rūpāyatana, rūpadhātu as an element, rūpasaññā …), matter «ရုပ်» (rūpakkhandha …); checked
    against the text."""
    p = strip_brackets(pali)
    stems = [("rūpāvacar", "သိမ်မွေ့သော ရုပ်"), ("rūpabhav", "သိမ်မွေ့သော ရုပ်"), ("rūpasahagat", "သိမ်မွေ့သော ရုပ်"),
             ("rūparāg", "သိမ်မွေ့သော ရုပ်"), ("rūpūpag", "သိမ်မွေ့သော ရုပ်"), ("rūpadhātuyā", "သိမ်မွေ့သော ရုပ်"),
             ("rūpadhātū", "သိမ်မွေ့သော ရုပ်"), ("rūpī", "သိမ်မွေ့သော ရုပ်"),
             ("rūpāyatan", "အဆင်းအရောင်"), ("rūpadhāt", "အဆင်းအရောင်"), ("rūpasaññ", "အဆင်းအရောင်"),
             ("rūpataṇh", "အဆင်းအရောင်"), ("rūpārammaṇ", "အဆင်းအရောင်"), ("rūpakkhandh", "ရုပ်"), ("rūpa", "ရုပ်")]
    v = first_compound(p, stems)
    if v == "သိမ်မွေ့သော ရုပ်" and "သိမ်မွေ့သော ရုပ်" not in my:
        v = None
    if v == "အဆင်းအရောင်" and "အဆင်းအရောင်" not in my:
        v = None
    if v is not None and presence(v, my)[0]:
        return v
    for c in ("ရုပ်", "အဆင်းအရောင်", "သိမ်မွေ့သော ရုပ်"):
        if c in my:
            return c
    return "@prior"


def f_rupam(kw, pali, my):
    """rūpaṃ: matter «ရုပ်» (the khandha); the seen object «အဆင်းအရောင်» in «rūpaṃ passati / cakkhunā rūpaṃ»
    (pi-5 harmonise B2 F.RUPA_SEEN; pi-2 ^2-517); one sense per segment, the first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [(r"rūpaṃ passat", "အဆင်းအရောင်"), (r"cakkhunā rūpaṃ", "အဆင်းအရောင်"),
                           (r"rūpaṃ disvā", "အဆင်းအရောင်"), (r"rūpa[ṃñm]", "ရုပ်")]) or "ရုပ်"
    if presence(v, my)[0]:
        return v
    return "ရုပ်" if "ရုပ်" in my else "@prior"


_DUKKHA = [("dukkhassant", "ဒုက္ခ"), ("dukkhassa antakiriy", "ဒုက္ခ"), ("dukkhamev", "ဒုက္ခ"),
           ("dukkhasacc", "ဒုက္ခ"), ("dukkhanirodh", "ဒုက္ခ"), ("dukkhasamuday", "ဒုက္ခ"), ("dukkhe" + _W, "ဒုက္ခ"),
           ("dukkhañāṇ", "ဒုက္ခ"), ("dukkhaṃ ariy", "ဒုက္ခ"), ("dukkhadassan", "ဒုက္ခ"),
           ("dukkhaṃ vedan", "နာကျင်သော"), ("dukkhāya vedan", "နာကျင်သော"), ("dukkhā vedan", "နာကျင်သော"),
           ("dukkhavedan", "နာကျင်သော"), ("adukkhamasukh", "နာကျင်"), ("dukkhindriy", "နာကျင်မှု"),
           ("sukhadukkh", "ဆင်းရဲ"), ("āpāyikaṃ dukkh", "ဆင်းရဲ"), ("nerayikaṃ dukkh", "ဆင်းရဲ"),
           ("dukkhudray", "ဆင်းရဲ"), ("dukkhavipāk", "ဆင်းရဲသော"), ("dukkh", "ဆင်းရဲ")]
_SUKHA = [("sukhaṃ vedan", "သာယာသော"), ("sukhā vedan", "သာယာသော"), ("sukhāya vedan", "သာယာသော"),
          ("sukhavedan", "သာယာသော"), ("adukkhamasukh", "သာယာ"), ("sukhindriy", "သာယာမှု"),
          ("sukhasahagat", "သာယာမှု"), ("sukhadukkh", "ချမ်းသာ"), ("dibbaṃ sukh", "ချမ်းသာ"),
          ("mānusakaṃ sukh", "ချမ်းသာ"), ("sukhudray", "ချမ်းသာ"), ("sukhavipāk", "ချမ်းသာသော"),
          ("sukh", "ချမ်းသာ")]


def f_dukkha(kw, pali, my):
    """dukkha, one sense per segment by the first compound (pi-3 f_dukkha with the pi-5 words): the truth / the end of
    suffering «ဒုက္ခ», painful feeling «နာကျင်သော» (adukkhamasukha «နာကျင်»), pain as the opposite of pleasure
    «ဆင်းရဲ» (sukhadukkha, āpāyika dukkha: my5-zeroshot-terms §7 / §8); checked against the text."""
    return by_first_checked(_DUKKHA, ["ဆင်းရဲ", "ဒုက္ခ", "နာကျင်သော", "နာကျင်မှု", "@prior"])(kw, pali, my)


def f_sukha(kw, pali, my):
    """sukha, likewise: pleasant feeling «သာယာသော», happiness «ချမ်းသာ» (dibbaṃ / mānusakaṃ sukhaṃ, sukhadukkha:
    my5-zeroshot-terms), the faculty «သာယာမှု» (pi-1 … pi-4)."""
    return by_first_checked(_SUKHA, ["ချမ်းသာ", "သာယာသော", "သာယာမှု", "@prior"])(kw, pali, my)


def f_anna(kw, pali, my):
    """añña «other»: the text's word «တခြားစီ» (aññaṃ A añño B «Aနှင့် Bသည် တခြားစီ ဖြစ်», pi-1 Aññaṃ), «တခြား»
    (pi-2) where the text has it alone, «အခြား» (anañño «အခြား မဖြစ်ဘဲ», aññatra «မှ အခြား»)."""
    for v in ("တခြားစီ", "တခြား", "အခြား"):
        if v in my:
            return v
    return "@prior"


def f_anna_f(kw, pali, my):
    """aññā: final knowledge «အပြည့်အဝ သိမြင်ခြင်း» (aññindriya, pi-1 … pi-4) or the feminine «other» (f_anna), by the
    first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [("aññindriy", "K"), ("aññātāv", "K"), (r"aññā" + _W, "O"), (r"aññaṃ", "O"),
                           (r"añño", "O")])
    if v == "K" and "အပြည့်အဝ သိမြင်" in my:
        return "အပြည့်အဝ သိမြင်ခြင်း" if "အပြည့်အဝ သိမြင်ခြင်း" in my else "@prior"
    return f_anna(kw, pali, my)


def f_hoti(kw, pali, my):
    """hoti: the copula «ဖြစ်သည်» (pi-4), existence «ရှိသည်» (pi-1 / pi-2) where the text has no «ဖြစ်»."""
    return "ဖြစ်သည်" if "ဖြစ်" in my else "ရှိသည်"


def f_karoti(kw, pali, my):
    """karoti / karonti = «ပြုသည်» (pi-4); only inside a Roman-script variant = (no direct equivalent)."""
    if not re.search(r"(?<![a-zāīūṃṅñṭḍṇḷ])" + low(kw) + _W, strip_brackets(pali), flags=re.I):
        return NONE
    return "ပြုသည်" if presence("ပြုသည်", my)[0] else "@prior"


def f_sassato(kw, pali, my):
    """sassato: the predicate adjective «ထာဝရ တည်မြဲသော» (my5-zeroshot-terms «puggalo sassato»; rule 3); the view
    «… တည်မြဲသည်ဟု / ဟူသော» keeps the pi-1 / pi-2 clause «ထာဝရ တည်မြဲသည်» (rule 4)."""
    if re.search("ထာဝရ တည်မြဲသည်(ဟု|ဟူ)", my) and not re.search("ထာဝရ တည်မြဲသော|ထာဝရ တည်မြဲသူ|ထာဝရ တည်မြဲသလော", my):
        return "ထာဝရ တည်မြဲသည်"
    return "ထာဝရ တည်မြဲသော"


def f_upada(kw, pali, my):
    """upādā: «မှီ၍» (Upādāpaññatti, «upādāya»; absolutive kept, pi-1), the fragment of anupādā(parinibbāna) «စွဲလမ်းမှု
    မရှိဘဲ» = the positive part «စွဲလမ်းမှု» (rule 8)."""
    if re.search(r"anupādā", strip_brackets(pali)) and "စွဲလမ်းမှု" in my and "anupādā" not in kw:
        if not re.search(r"upādāpaññatt|upādāya", strip_brackets(pali), flags=re.I) or "မှီ၍" not in my:
            return "စွဲလမ်းမှု"
    return "မှီ၍" if "မှီ၍" in my else "@prior"


def f_dhatuya(kw, pali, my):
    """dhātuyā (rūpa- / arūpa- / kāmadhātuyā): the plane «ဘုံ» (pi-2 dhātu = ဘုံ) where the text has it, else
    the element «ဓာတ်»."""
    return "ဘုံ" if "ဘုံ" in my and re.search(r"(rūpa|kāma)dhātuyā", pali, flags=re.I) else "ဓာတ်"


FUNCS = {
    "niggaha": lambda kw, pali, my: "ချေပချက်" if "ချေပချက်" in my else (
        "ချုပ်ကိုင်ခြင်း" if "ချုပ်ကိုင်ခြင်း" in my else "@prior"),
    "niggahetabba": pref("ချေပရမည့်", "ချေပရသည်"),
    "roman": f_roman,
    "hevameva": lambda kw, pali, my: NONE if f_roman(kw, pali, my) == NONE else "ဤနည်းအတိုင်းပင်",
    "vata": lambda kw, pali, my: "အမှန်ပင်" if "အမှန်ပင်" in my and re.search(r"vata re|\bvata\b", pali) else "@prior",
    "miccha": f_miccha,
    "tenahi": first_in_text("သို့ဖြစ်လျှင်", "သို့ဖြစ်၍"),
    "puccha": if_text("အမေး", "အမေး", "@prior"),
    "vadi": lambda kw, pali, my: by_sub([("sakavād", "မိမိဘက်"), ("paravād", "တစ်ဖက်သား")], None)(kw, pali, my)
        if re.search(r"sakavād|paravād", pali) and ("မိမိဘက်" in my or "တစ်ဖက်သား" in my)
        else ("ဆိုတော်မူသူ" if "ဆိုတော်မူသူ" in my else "@prior"),
    "atthena": if_text("အနက်", "အနက်"),
    "parama": if_text("အဆုံးစွန်", "အဆုံးစွန်"),
    "saccikattho": literal("အမှန်တကယ် အရာ", "အမှန်တကယ် … အရာ"),
    "attha_thing": lambda kw, pali, my: "အရာ" if "အရာ" in my and "ṭṭh" in pali else (number(kw, my) or "@prior"),
    "suddha": pref("ရိုးရိုး", "သက်သက်"),
    "sabbesu": if_text("အရာအားလုံး", "အရာအားလုံး"),
    "katva": if_text("အကြောင်းပြု", "အကြောင်းပြု၍"),
    "eva": by_first_checked([("attheva", "ပင်"), ("sveva", "ပင်"), ("teneva", "ပင်"), ("tasseva", "ပင်"),
                             ("tatheva", "ပင်"), ("ekova", "သာ"), ("dukkhameva", "သာ")], ["သာ", "ပင်"]),
    "katha": lambda kw, pali, my: next((v for v in ("ဆွေးနွေးချက်", "ဆွေးနွေးခြင်း") if v in my), "@prior"),
    "naya": lambda kw, pali, my: "နည်း" if "နည်း" in my else "@prior",
    "koci": pref("တစ်စုံတစ်ယောက်", "တစ်စုံတစ်ရာ"),
    "yo": lambda kw, pali, my: "အကြင်သူ" if "အကြင်သူ" in my else NONE,
    "yam": lambda kw, pali, my: "အကြင်အရာ" if "အကြင်အရာ" in my else NONE,
    "yena": lambda kw, pali, my: "အကြင်အရာ" if "အကြင်အရာဖြင့်" in my else NONE,
    "anna": f_anna, "anna_f": f_anna_f, "hoti": f_hoti, "upada": f_upada,
    "cavati": lambda kw, pali, my: "စုတေသည်" if "စုတေ" in my else "သေသည်",
    "karoti": f_karoti, "sassato": f_sassato,
    "viraga": lambda kw, pali, my: "ပြယ်ပျောက်" if "ပြယ်ပျောက်တတ်" in my else "@prior",
    "rupam": f_rupam, "rupa": f_rupa, "dukkha": f_dukkha, "sukha": f_sukha, "dhatuya": f_dhatuya,
    "para": by_first_checked([("paracitt", "အခြားသူ"), ("paraṃ lok", "တမလွန်"), ("parasmā lok", "တမလွန်"),
                              ("paraṅkār", "သူတစ်ပါး"), ("paraṃkār", "သူတစ်ပါး"), ("paravād", "တစ်ဖက်သား")],
                             ["@prior"]),
    "hitaya": pref("အကျိုးစီးပွား", "အကျိုး"),
    "sacca": by_first_checked([("saccavād", "မှန်သော"), ("saccato", "အမှန်")], ["@prior"]),
}
# ---- FUNCS-END
