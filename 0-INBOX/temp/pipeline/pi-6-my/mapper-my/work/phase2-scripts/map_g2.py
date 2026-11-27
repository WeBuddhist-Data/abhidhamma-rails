"""pi-6 Burmese keyword mapping, PHASE 2, group G2: 6-01 / 6-02 sankharayamaka, 7-01 … 7-11 anusayayamaka, 8-cittayamaka.

Imports the shared module map6_rules.py (NOT edited); holds only the chapter tables and the new context functions of
this group. Writes <ch>.mapped.md for each chapter in chapter order and prints the three checks per chapter.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g2.py
"""
import sys
import re
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

GROUP = ["6-01-sankharayamaka", "6-02-sankharayamaka"] + [f"7-{i:02d}-anusayayamaka" for i in range(1, 12)] + \
        ["8-cittayamaka"]

# the vitakka / vicāra qualifiers (pi-1 ^1-M1-6 savitakkasavicāra «… ရှိသော», pi-1 ^1-1401 avitakkaavicāra «…လည်း
# မရှိ၊ …လည်း မရှိသော»; rule 6: the «၊» inside the term goes, as abyākata)
SV = "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိ"
AV = "စတင်ကြံစည်မှုလည်း မရှိ ဆက်လက်သုံးသပ်မှုလည်း မရှိ"
KS = "ကိုယ်၏ ပြုပြင်ဖန်တီးမှု"

# ---- new context functions of this group
def f_plane_adj(kw, pali, my):
    """R5 (group fix, O2): a plane genitive plural before «pacchimacittaṃ» («yassa cittassa anantarā kāmāvacarānaṃ
    pacchimacittaṃ», the keyword's own case: «Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe» is the beings) is the text's adjective «Pနှင့် ဆိုင်သော» (harmonise A2); the module's shared_being would join
    the plane to a «…၌ ရှိသူ» of ANOTHER plane later in the clause («ကာမဘုံ … ရှိသူ»). Elsewhere the module value."""
    base = R.place_cands(kw)
    m = re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])( pacchimacittaṃ)?", R.strip_brackets(pali))
    if base and m and m.group(1):        # one sense per segment: the sense of the keyword's FIRST occurrence
        p = base[-1]
        if p + "နှင့် ဆိုင်သော" in my:
            return p + "နှင့် ဆိုင်သော"
    v = R.morph_value(kw, pali, my)[0]
    return v if v else "@prior"


# R6 in a body line (group rule V1): a vāra name in any case «X-vāro / -vāre / -vārepi / -vāraṃ / -vārena» = «Xအလိုက်
# ဖော်ပြချက်» (the heading form of the zero-shot notes ch6-8 / ch7a / ch7b; rule 1: the case particle «၌ / ကို / နှင့်»
# goes, Q4: api «လည်း» goes); a heading line keeps the heading rule's whole part.
VARA = [("uppādavāranirodha", "ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် ချုပ်ငြိမ်းခြင်း"),
        ("uppādanirodha", "ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်း"), ("uppāda", "ဖြစ်ပေါ်ခြင်း"), ("nirodha", "ချုပ်ငြိမ်းခြင်း"),
        ("uppajjana", "ဖြစ်ပေါ်ခြင်း"), ("pariññā", "ပိုင်းခြား သိခြင်း"), ("pahīna", "ပယ်ပြီး ဖြစ်ခြင်း"),
        ("pajahana", "ပယ်ခြင်း"), ("sānusaya", "ကိန်းအောင်းခြင်း ရှိသူ"), ("anusaya", "ကိန်းအောင်းခြင်း"),
        ("uppattiṭṭhāna", "ဖြစ်ပေါ်ရာ နေရာ"), ("puggala", "ပုဂ္ဂိုလ်"), ("dhamma", "သဘောတရား"),
        ("puggaladhamma", "ပုဂ္ဂိုလ်နှင့် သဘောတရား"), ("paṇṇatti", "သတ်မှတ်ချက်"), ("pavatti", "ဖြစ်ပျက်ခြင်း")]
_VARA = re.compile(r"^(\w+?)vār(o|e|epi|aṃ|ena|a|ampi)$")


def vara_value(kw):
    m = _VARA.match(R.low(kw))
    if not m:
        return None
    for st, my in sorted(VARA, key=lambda x: -len(x[0])):
        if m.group(1) == st:
            return my + "အလိုက် ဖော်ပြချက်"
    return None


def f_vara(kw, pali, my):
    if pali.lstrip().startswith("#"):
        h = R.heading_value(kw, pali, my)
        if h:
            return h
    v = vara_value(kw)
    if v and (R.phrase_ok(v, my) or R.phrase_ok(v, R.flat(my))):
        return v
    h = R.heading_value(kw, pali, my)
    return h if h else "@prior"


FUNCS = {"plane_adj": f_plane_adj, "vara": f_vara}
PLANE_ADJ = {k: "@plane_adj" for k in ("kāmāvacarānaṃ", "rūpāvacarānaṃ", "arūpāvacarānaṃ")}

# ---- ch. 6 Saṅkhārayamaka
T6 = {
    **PLANE_ADJ,
    # kāyasaṅkhāra = the text's «ကိုယ်၏ ပြုပြင်ဖန်တီးမှု» (pi-5 ^5-458 rails, as vacī- / cittasaṅkhāra «နှုတ်၏ / စိတ်၏»);
    # the pi-2 / pi-5 key value «ကိုယ် ပြုပြင်ဖန်တီးမှု» is not a phrase of any pi-6 segment (module override O1)
    "kāyasaṅkhāro": KS, "kāyasaṅkhāraṃ": KS, "kāyasaṅkhārassa": KS, "kāyasaṅkhārā": KS,
    "vaciṃ": "နှုတ်",                                             # Vaciñca (R1) = vacī «နှုတ်» (pi-5)
    # the okāsa / person leads (my6-zeroshot-terms §5: yattha «အကြင်နေရာ၌», rule 1: the final «၌» goes)
    "Yattha": "အကြင်နေရာ", "Yassa yattha": "အကြင်သူအား အကြင်နေရာ",
    # the cited sections of the editorial notes «(Yassakampi yassayatthakampi sadisaṃ)» = «(“အကြင်သူအား” အပိုင်းလည်း၊
    # “အကြင်သူအား အကြင်နေရာ၌” အပိုင်းလည်း …)»: the quoted lead + «အပိုင်း» (-ka); api «လည်း» goes (Q4), the final «၌»
    # of the locative yassayatthake goes (rule 1); the quoted lead keeps its own particles
    "Yassakampi": "အကြင်သူအား အပိုင်း", "yassakampi": "အကြင်သူအား အပိုင်း",
    "yassayatthakampi": "အကြင်သူအား အကြင်နေရာ၌ အပိုင်း", "yassayatthake": "အကြင်သူအား အကြင်နေရာ၌ အပိုင်း",
    "Yatthakampi": "အကြင်နေရာ၌ အပိုင်း",
    "tesaṃyeva": "ထိုသူ",                                         # R1: = tesaṃ «ထိုသူ» (pi-4 / pi-5 tassa); eva «ပင်» goes
    # vitakka / vicāra
    "avitakkaavicāraṃ": AV + "သော", "Avitakkaavicāraṃ": AV + "သော",
    "avitakkaavicāracittassa uppādakkhaṇe": AV + "သော စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "avitakkaavicāracittassa bhaṅgakkhaṇe": AV + "သော စိတ်၏ ပြိုပျက်ခြင်း ခဏ",
    "Savitakkasavicārapacchimacittassa uppādakkhaṇe": SV + "သော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "Savitakkasavicārapacchimacittassa bhaṅgakkhaṇe": SV + "သော နောက်ဆုံး စိတ်၏ ပြိုပျက်ခြင်း ခဏ",
    "avitakkaavicārapacchimacittasamaṅgīnaṃ": AV + "သော နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ",
    "Savitakkasavicārabhūmiyaṃ": SV + "ရာ အဆင့်", "Avitakkaavicārabhūmiyaṃ": AV + "ရာ အဆင့်",   # pi-1 sukhabhūmiyaṃ «…ရာ အဆင့်»
    # headings and colophons standing in a body line (R6 reads only heading lines)
    "paccanīkaokāsā": "နေရာအလိုက် အငြင်းပြ ပုံစံ",                 # the slip of paccanīkaokāso (zero-shot notes)
    "Savitakkasavicārapacchimacittassa": SV + "သော နောက်ဆုံး စိတ်", "Avitakkaavicārapacchimacittassa": AV + "သော နောက်ဆုံး စိတ်",
    "Avitakkaavicārapacchimacittassa bhaṅgakkhaṇe": AV + "သော နောက်ဆုံး စိတ်၏ ပြိုပျက်ခြင်း ခဏ",
    "Avitakkaavicārapacchimacittassa uppādakkhaṇe": AV + "သော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "yatthakānaṃ": "အကြင်နေရာ၌ အပိုင်း",                         # «(itaresaṃ yatthakānaṃ sadisaṃ)» «“အကြင်နေရာ၌” အပိုင်းတို့»
    # chapter titles cited in a note (rule 7: the approved title whole; the locative «၌» goes, rule 1)
    "khandhayamake": "အစုအဝေးများကို အတွဲလိုက် မေးဖြေခြင်း", "saṅkhārayamakepi": "ပြုပြင်ဖန်တီးမှုများကို အတွဲလိုက် မေးဖြေခြင်း",
    # persons: samāpannānaṃ = the agent noun «… ဝင်စားနေသူ» (pi-4 P6; «ဈာန်ကို ဝင်စားနေသူတို့»), its attributive before a noun
    "samāpannānaṃ": ("ဝင်စားနေသူ", "ဝင်စားနေသော"),
}
# ---- ch. 7 Anusayayamaka
PAT = "အငြင်းပြ ပုံစံ"
T7 = {
    "kāmārāgānusayo": "ကာမရာဂ ကိန်းအောင်းခြင်း",               # the source slip (kāmā-) of kāmarāgānusayo (R8)
    "Sattānusayā": "ကိန်းအောင်းခြင်း ခုနစ်ပါး",
    "Pajahanāvāre": "ပယ်ခြင်းအလိုက် ဖော်ပြချက်",                 # the source slip of Pajahanavāre (V1)                   # count + noun with the text's classifier (pi-1 decision 5)
    # paṭiloma = paccanīka «အငြင်းပြ ပုံစံ» (the Yamaka negated form, approved sample departure 2; zero-shot notes ch7a)
    "paṭilomaṃ": PAT, "paṭilomapuggalo": "ပုဂ္ဂိုလ်အလိုက် " + PAT, "paṭilomaokāso": "နေရာအလိုက် " + PAT,
    "paṭilomapuggalokāsā": "ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် " + PAT,
    # sa-anusaya / nir-anusaya persons (group rule V2): the agent noun «ကိန်းအောင်းခြင်း ရှိသူ / မရှိသူ» (pi-4 P6; the
    # zero-shot notes ch7a, pi-5 ^5-606 «ကိန်းအောင်းခြင်း ရှိသူ»); the anusaya named in the instrumental keeps its own
    # value «X ကိန်းအောင်းခြင်း» (R8), so the word «ကိန်းအောင်းခြင်း» stands in both values (the anusaya element of
    # sa-anusaya); the plural «များ» and the copula go (rules 1 / 2)
    # dhātupucchā / -visajjanā (7-10, 7-11): bhaṅgā (a predicate adjective, «kati anusayā bhaṅgā?» «… မည်မျှ
    # ပြိုပျက်ကြသနည်း», «anusayā bhaṅgā natthi» «ပြိုပျက်သော ကိန်းအောင်းခြင်း မရှိ») = rule 3 «ပြိုပျက်သော» (the text's
    # «ပြိုပျက်ကြ…» by the ending rule); the colophons in a body line (R6); the «na»-plane labels = the text's whole label
    # as an adjective (R4 mūlaka: «(ကာမဘုံ မဟုတ်သော ဘုံကို အခြေခံ၍)» = … အခြေခံသော; rule 6: the «၊» goes)
    "bhaṅgā": "ပြိုပျက်သော",
    # pahīnā = pahīno «ပယ်ပြီးသော» (STOCK, pi-4 / pi-5; the text's «… ပယ်ပြီး ဖြစ်»); the pi-4 «ပယ်ရသော» would match the
    # negative «မပယ်ရသေး» by the ending rule (module override O4)
    "pahīnā": "ပယ်ပြီးသော", "appahīnā": "မပယ်ရသေးသော",
    # «heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati» «အောက်၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူသည်»: a person, the agent noun (P6;
    # the module's -amāno «thing» form «…ဆဲ» is the bare participle; module override O3)
    "upapajjamāno": ("ပြန်လည် ဖြစ်ပေါ်ဆဲသူ", "ပြန်လည် ဖြစ်ပေါ်ဆဲ"),
    "Dhātupucchāvāro": "ဘုံများအကြောင်း အမေး ဖော်ပြချက်", "Dhātuvisajjavāro": "ဘုံများအကြောင်း အဖြေ ဖော်ပြချက်",
    "kāmadhātuṃyeva": "ကာမဘုံ",                                   # R1 (eva «ပင်» goes; «ကာမဘုံ၌ပင်», rule 1)
    "upapattināma": "ပြန်လည် ဖြစ်ပေါ်ခြင်း",                      # «… upapatti nāma natthi» «ပြန်လည် ဖြစ်ပေါ်ခြင်း ဟူ၍ မရှိ»
    "Nakāmadhātumūlakaṃ": "ကာမဘုံ မဟုတ်သော ဘုံကို အခြေခံသော",
    "Narūpadhātumūlakaṃ": "သိမ်မွေ့သော ရုပ်ဘုံ မဟုတ်သော ဘုံကို အခြေခံသော",
    "Naarūpadhātumūlakaṃ": "ရုပ်မရှိသော ဘုံ မဟုတ်သော ဘုံကို အခြေခံသော",
    "Nakāmanaarūpadhātumūlakaṃ": "ကာမဘုံလည်း မဟုတ် ရုပ်မရှိသော ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံသော",
    "Narūpanaarūpadhātumūlakaṃ": "သိမ်မွေ့သော ရုပ်ဘုံလည်း မဟုတ် ရုပ်မရှိသော ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံသော",
    "Nakāmanarūpadhātumūlakaṃ": "ကာမဘုံလည်း မဟုတ် သိမ်မွေ့သော ရုပ်ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံသော",
    "sānusayo": "ကိန်းအောင်းခြင်း ရှိသူ", "sānusayā": "ကိန်းအောင်းခြင်း ရှိသူ",
    "niranusayo": "ကိန်းအောင်းခြင်း မရှိသူ", "niranusayā": "ကိန်းအောင်းခြင်း မရှိသူ",
}
# ---- ch. 8 Cittayamaka
T8 = {
    **PLANE_ADJ,
    # «Atītānāgataṃ cittaṃ» «အတိတ် စိတ်နှင့် အနာဂတ် စိတ်»: the dvandva's two members around the repeated «စိတ်» (cittaṃ
    # has its own keyword): rule 10 « … »
    "Atītānāgataṃ": "အတိတ် … အနာဂတ်",
    # uppannaṃ = the perfect participle «ဖြစ်ပေါ်ပြီးသော» (pi-2; the text's «ဖြစ်ပေါ်ပြီး ဖြစ် / မဟုတ်»); the pi-1 «ဖြစ်ပေါ်သော»
    # is found only inside the concessive «ဖြစ်ပေါ်သော်လည်း» of uppajjati (module override O5); where the text has the
    # participle only before «မဟုတ်» («no ca tassa cittaṃ uppannaṃ» «… ဖြစ်ပေါ်ပြီး မဟုတ်»), the text's form «ဖြစ်ပေါ်ပြီး»
    "uppannaṃ": ("ဖြစ်ပေါ်ပြီးသော", "ဖြစ်ပေါ်ပြီး"),
    # headings (rule 7 / R6: the text's whole part; the hyphenated heading «Uppajjamāna-nanirodhavāro» is keyed as two
    # parts, «ဖြစ်ပေါ်ဆဲ အရာနှင့် | မချုပ်ငြိမ်းခြင်း ဖော်ပြချက်»)
    "nanirodhavāro": "မချုပ်ငြိမ်းခြင်း ဖော်ပြချက်",
    "Suddhacittasāmaññaṃ": "ရိုးရိုး စိတ် အထွေထွေ", "Suddhacittasāmañña": "ရိုးရိုး စိတ် အထွေထွေ",
    "Suttantacittamissakaviseso": "သုတ္တန်လာ စိတ်များကို ရောစပ်သော ထူးခြားချက်",
    "Abhidhammacittamissakaviseso": "အဘိဓမ္မာလာ စိတ်များကို ရောစပ်သော ထူးခြားချက်",
    "Atikkantakālavāro": "ကာလ ကျော်လွန်ပြီးခြင်း ဖော်ပြချက်",     # the heading standing in a body line (^6-8-82)
    # «yāva saraṇaaraṇā» «“ပဋိပက္ခ ရှိသော” “ပဋိပက္ခ မရှိသော” အတွဲ တိုင်အောင်»: the dvandva = its two members + «အတွဲ»
    # (pi-1 ^1-M2-100 saraṇa / araṇa); the quotation marks and «တိုင်အောင်» (yāva) go
    "saraṇaaraṇā": "ပဋိပက္ခ ရှိသော ပဋိပက္ခ မရှိသော အတွဲ",
    # moment / person phrases of the citta qualifiers (pi-2 ^2-365 sarāga «ရာဂ ရှိသော»; pacchima «နောက်ဆုံး»)
    "Sarāgapacchimacittassa uppādakkhaṇe": "ရာဂ ရှိသော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "sarāgacittassa uppādakkhaṇe": "ရာဂ ရှိသော စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "Pacchimakusalacittassa": "နောက်ဆုံး ကုသိုလ်စိတ်",
    # the cited sections «(Yassa cittake …, yaṃ cittake ca yassa yaṃ cittake ca …)» «“အကြင်သူအား စိတ်” အပိုင်း»: as
    # yassaka (ch. 6): the word + «အပိုင်း» (-ka); the chapter titles cited in a note (rule 7)
    "cittake": "စိတ် အပိုင်း",
    "dhammayamakanti": "သဘောတရားများကို အတွဲလိုက် မေးဖြေခြင်း",
}
# every vāra keyword of the group's chapters goes through f_vara (unless a table has it)
for _ch in GROUP:
    _t = T6 if _ch.startswith("6-") else T7 if _ch.startswith("7-") else T8
    for _sid, _kws in R.keyword_rows(_ch):
        for _k in _kws:
            if vara_value(_k) and _k not in _t:
                _t[_k] = "@vara"
TABLES = {ch: (T6 if ch.startswith("6-") else T7 if ch.startswith("7-") else T8) for ch in GROUP}
CTX = {}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS, stem=R.make_stem([R.FRAME, R.STOCK, T6, T7, T8]))


def s1_review(M):
    """S1 review: every use that the module ALONE (no group table) maps by the stem fallback, compared with the final
    value: kept (same value) or corrected (a group table / context function gives another value)."""
    M0 = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
    kept, corr = collections.Counter(), collections.Counter()
    for ch in GROUP:
        pa, my = R.pali(ch), R.burmese(ch)
        final = {}
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            final[sid] = [kv.split("=", 1) for kv in rest.split(", ")]
        for sid, kws in R.keyword_rows(ch):
            for i, kw in enumerate(kws):
                try:
                    v0 = M0.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    continue
                if M0.SRC.get((sid, kw)) != "stem":
                    continue
                v = final[sid][i][1]
                (kept if v == v0 else corr)[(ch, kw, v0, v)] += 1
    return kept, corr


def prior_diffs():
    """uses whose final value differs from every pi-1 … pi-5 value of the keyword (or of its base form, R1)."""
    same = new = 0
    diffs = collections.defaultdict(collections.Counter)
    for ch in GROUP:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l[1:].split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if not pv:
                    new += 1
                elif v in pv:
                    same += 1
                else:
                    diffs[(k, v)][pv.most_common(1)[0][0]] += 1
    return same, new, diffs


def main():
    M = mapper()
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    for ch in GROUP:
        if only and not any(ch.startswith(o) for o in only):
            continue
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        rules = collections.Counter(r for _, _, _, r in ruled)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ending-rule chunks {dict(rules)}")
        if "-v" in sys.argv:
            for x in unmapped:
                print("   UNMAPPED", x)
            for x in fails:
                print("   FAIL", x)
            for x in punct:
                print("   PUNCT", x)
    if "--report" in sys.argv:
        kept, corr = s1_review(M)
        print(f"S1 (module alone): uses {sum(kept.values()) + sum(corr.values())}, kept {sum(kept.values())} "
              f"({len(kept)} pairs), corrected {sum(corr.values())} ({len(corr)} pairs)")
        for (ch, k, v0, v), c in sorted(corr.items()):
            print(f"   CORR {ch} {k}: {v0} -> {v} ({c})")
        for (ch, k, v0, v), c in sorted(kept.items()):
            print(f"   KEPT {ch} {k}: {v0} ({c})")
        same, new, diffs = prior_diffs()
        print(f"prior: same {same} new {new} diff {sum(sum(c.values()) for c in diffs.values())} ({len(diffs)} pairs)")
        for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
            print(f"   DIFF {k} = {v}   prior {dict(c)}")
    return M


if __name__ == "__main__":
    main()
