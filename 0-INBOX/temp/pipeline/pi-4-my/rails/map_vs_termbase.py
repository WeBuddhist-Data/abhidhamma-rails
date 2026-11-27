"""pi-4 rails, sense-level cross-check (stricter than the loose adherence test): every value of the zero-shot keyword
map (the zero-shot's own form of each keyword in each segment) must be a term of that keyword's termbase entry, or
else be explained here, one of:
  FIXED  (family Lnn): the rails segment now has the termbase term (adherence_my.occurs) and no longer the old form;
  STALE  : the termbase term itself is already in the zero-shot segment (the map was built before the consistency
           pass, or took a neighbouring word: sambuddho «… ဘုရား» where the text has «… ဘုရားရှင်»; kantā
           «ချစ်ခင်ဖွယ်ကောင်းသော» is pemanīyā's word next to bahujanakantā «လူအများ နှစ်သက်သော»);
  KEPT   (reason): a person-type NAME (binding), a privative fragment, another grammatical form, an approved rails-step
           note, or a sense the term does not cover (a termbase doubt) — the old form must still be in the rails segment;
  «(no direct equivalent)» of a keyword without an entry.
Anything else is a difference the loose test could hide, and the run fails. Model: pi-3-my/rails/map_vs_termbase.py.
usage: python3 -I -X utf8 map_vs_termbase.py   (after the rails build; exit 1 on an unexplained or unverified value)"""
import collections
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
TB = ROOT / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md"
KMAP = ROOT / "AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md"
Z = A.segments(ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters")
R = A.segments(ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters")
tb = A.parse_termbase(TB)

FIXED = {  # (keyword, zero-shot form) -> family (my_formulas_rails.py)
    ("ṭhito", "တည်သော"): "L01",
    ("suṇāti", "ကြားရသည်"): "L03", ("suṇāti", "ကြားနာသည်"): "L03", ("sutvā", "ကြားနာ၍"): "L03",
    ("suṇato", "ကြားနာသော"): "L03",
    ("desenti", "ဟောကြားသည်"): "L04", ("bhikkhū desenti", "ရဟန်း … ဟောကြားသည်"): "L04",
    ("desetabbo", "ဟောကြားရမည့်"): "L04",
    ("pakāsenti", "ထုတ်ဖော် ပြသည်"): "L05", ("brahmacariyaṃ pakāsenti", "မြင့်မြတ်သော အကျင့်ကို ထုတ်ဖော် ပြသည်"): "L05",
    ("dīgharattaṃ", "ကြာမြင့်စွာ"): "L06",
    ("dubbaṇṇo", "အဆင်း ညှိုးသော"): "L07", ("dubbaṇṇatāya", "အဆင်း ညှိုးခြင်း"): "L07",
    ("senāsana", "ကျောင်းအိပ်ရာနေရာ"): "L08",
    ("purisapuggalo", "လူ ပုဂ္ဂိုလ်"): "L09",
    ("bhogaṃ", "စည်းစိမ်ဥစ္စာ"): "L10",
    ("vāco", "ပြောတတ်သော"): "L11",
    ("abhisamayo", "ထိုးဖောက် သိမြင်ခြင်း"): "L12",
    ("puggalassa abhisamayo", "ပုဂ္ဂိုလ် … ထိုးဖောက် သိမြင်ခြင်း"): "L12",
    ("atthe", "အနက်"): "L13", ("atthaṃ", "အနက်"): "L13", ("attha", "အနက်"): "L13",
    ("byañjanaṃ", "သဒ္ဒါ"): "L14",
    ("paṭipannānaṃ", "ကျင့်သော"): "L15", ("duppaṭipannānaṃ", "ဆိုးစွာ ကျင့်သော"): "L15",
    ("micchāpaṭipannānaṃ", "မှားယွင်းစွာ ကျင့်သော"): "L15", ("sammāpaṭipannā", "မှန်ကန်စွာ ကျင့်သော"): "L15",
    ("sammāpaṭipannānaṃ", "မှန်ကန်စွာ ကျင့်သော"): "L15", ("paṭipanno", "ကျင့်သော"): "L15",
    ("abhirūpo", "ရုပ်ချောသော"): "L16", ("dassanīyo", "ရှုချင်ဖွယ် ဖြစ်သော"): "L16",
    ("pāsādiko", "ကြည်ညိုဖွယ် ဖြစ်သော"): "L16",
    ("kasira", "ခက်ခဲသော"): "L17", ("kasirena", "ခက်ခဲစွာ"): "L17",
    ("ābādho", "ရောဂါ"): "L18",
    ("ajinaṃ", "သားရေ"): "L19",
    ("sappi", "ထောပတ်"): "L20",
    ("rūpa", "အဆင်း"): "L21",
    ("raja", "မြူမှုန်"): "L22",
    ("ekanta", "စင်စစ်"): "L23",
    ("nikati", "စဉ်းလဲခြင်း"): "L24",
    ("pamāda", "မေ့လျော့ခြင်း"): "L25",
    ("narassa", "လူ"): "F03", ("sāci", "ကောက်ကျစ်သော"): "F05",   # review fixes, termbase change 2026-11-20
}
# the old form (regex) that must be gone from the rails segment, where the map value is not itself a plain substring
GONE = {("ṭhito", "တည်သော"): "၌ တည်သော", ("vāco", "ပြောတတ်သော"): "ပြောတတ်", ("rūpa", "အဆင်း"): "အဆင်းတူ",
        ("sappi", "ထောပတ်"): "ထောပတ်နှင့်", ("ajinaṃ", "သားရေ"): "ကြမ်းသော သားရေ", ("ābādho", "ရောဂါ"): "ပုကွသူ၊ ရောဂါ",
        ("atthe", "အနက်"): "အနက်ကို", ("atthaṃ", "အနက်"): "အနက် ပြည့်စုံ", ("attha", "အနက်"): "အနက်ကို",
        ("paṭipanno", "ကျင့်သော"): "ကျင့်သူ", ("abhirūpo", "ရုပ်ချောသော"): "ရုပ်ချော",
        ("dassanīyo", "ရှုချင်ဖွယ် ဖြစ်သော"): "ရှုချင်ဖွယ် ဖြစ်", ("pāsādiko", "ကြည်ညိုဖွယ် ဖြစ်သော"): "ကြည်ညိုဖွယ် ဖြစ်",
        ("pamāda", "မေ့လျော့ခြင်း"): "မေ့လျော့ခြင်း၏ အကြောင်း",
        ("narassa", "လူ"): "လူ၏ အရှေ့ဘက်", ("sāci", "ကောက်ကျစ်သော"): "ကောက်ကျစ်သော နည်းလမ်း",
        **{(k, v): "ကျင့်(?:သော|သူ)" for k, v in (("paṭipannānaṃ", "ကျင့်သော"), ("duppaṭipannānaṃ", "ဆိုးစွာ ကျင့်သော"),
                                              ("micchāpaṭipannānaṃ", "မှားယွင်းစွာ ကျင့်သော"),
                                              ("sammāpaṭipannā", "မှန်ကန်စွာ ကျင့်သော"),
                                              ("sammāpaṭipannānaṃ", "မှန်ကန်စွာ ကျင့်သော"))}}
STALE = {("sambuddho", "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရား"), ("samannāgatā", "ပြည့်စုံသော"),
         ("upakkilese", "အညစ်အကြေး"), ("vūpasanta", "ကောင်းစွာ ငြိမ်သက်သော"), ("kantā", "ချစ်ခင်ဖွယ်ကောင်းသော"),
         ("ārāmo", "နှစ်သက်သော")}
KEPT = {  # (keyword, zero-shot form) -> reason
    ("niyato", "လမ်းကြောင်း ကျိန်းသေသူ"): "person-type NAME (binding; decision niyato|0)",
    ("Niyato", "လမ်းကြောင်း ကျိန်းသေသူ"): "person-type NAME (binding; decision niyato|0)",
    ("sampajāno", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ရှိသူ"): "person-type NAME (binding; decision sampajāno|0); ^4-182 «sato sampajāno» has the term as «… ဆင်ခြင်သိမြင်လျက်»",
    ("bhabba", "ထိန်းနိုင်သော"): "person-type NAMES cetanābhabbo / anurakkhaṇābhabbo (binding; decision bhabba|0)",
    ("vigata", "ကင်းပြီးသော"): "inside a person-type NAME (binding; decision vigata|0)",
    ("gāmī", "လိုက်သွားသော"): "person-type NAME anusotagāmī (binding; decision gāmī|0)",
    ("Puggalapaññatti", "ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း"): "the approved book title (^4-0)",
    ("puggalapaññatti", "ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း"): "the approved book title (colophon ^4-209)",
    ("paññatti", "သတ်မှတ်ဖော်ပြခြင်း"): "inside the approved book title (^4-0)",
    ("pahīnāni", "ပယ်ရသော"): "privative fragment of appahīn- «မပယ်ရသေး» (decision)",
    ("pahīnā", "ပယ်ရသော"): "privative fragment of appahīn- «မပယ်ရသေး» (decision)",
    ("pahīno", "ပယ်ရသော"): "privative fragment of appahīn- «မပယ်ရသေး» (decision)",
    ("pahīnaṃ", "ပယ်ရသော"): "privative fragment of appahīn- «မပယ်ရသေး» (decision)",
    ("manasi", "နှလုံး"): "fragment before the negated verb «နှလုံး မသွင်း» (decision manasi|0)",
    ("ñāṇaṃ", "သိခြင်း"): "positive part of aññāṇaṃ «မသိခြင်း» (decision ñāṇaṃ|0)",
    ("pameyyo", "ချိန်ဆ၍ ရနိုင်သော"): "positive part of appameyyo «ချိန်ဆ၍ မရနိုင်သူ» (own entry)",
    ("dukkha", "နာကျင်သော"): "dukkhasamphassa, the cloth (decision dukkha|0)",
    ("sukha", "သာယာသော"): "sukhasamphassa, the cloth (decision sukha|0)",
    ("sammā", "မှန်ကန်စွာ"): "the adverb in sammāpaṭipannā (decision sammā|0)",
    ("anussati", "အောက်မေ့နိုင်သော"): "inside pubbenivāsānussatiñāṇa (decision anussati|0)",
    ("nirodha", "ချုပ်ငြိမ်း"): "inside dukkhanirodhagāminī «… ချုပ်ငြိမ်းရာ» (grammar, decision nirodha|0)",
    ("dukkhanirodha", "ဒုက္ခ ချုပ်ငြိမ်းရာ"): "inside dukkhanirodhagāminī (grammar)",
    ("phāsu", "ချမ်းသာ"): "predicate «… ချမ်းသာ ဖြစ်လိမ့်မည်» (INFLECTION row)",
    ("kārī", "ပြုလေ့ရှိသော"): "sampajānakārī, own entry",
    ("para", "ပရ"): "proper name Paranimmita",
    ("vaṇṇa", "ချီးမွမ်း"): "spoken praise, own phrase entries (decision vaṇṇa|0)",
    ("gilāna", "လူနာ"): "the sick person gilāno «လူနာ» (decision gilāna|0, H11)",
    ("evaṃ", "ဤနည်းတူ"): "the bracket note evamuparipi / evaṃ (decision evaṃ|0)",
    ("evameva", "ဤနည်းတူ"): "the bracket note «… evameva» (decision evameva|0)",
    ("phalaṃ", "အကျိုး"): "approved rails-step note: mahapphalaṃ ^4-116 / ^4-117 «အကျိုး»",
    ("indriyānaṃ", "စွမ်းရည်"): "approved rails-step note: ^4-M-6 the 22 faculties «စွမ်းရည်»",
    ("attanā", "မိမိကိုယ်"): "X-bhūtena attanā (doubt 2)",
    ("vācāya", "စကား"): "pisuṇāya / pharusāya vācāya, the speech itself (doubt 3)",
    ("gahapati", "သူကြွယ်"): "the householder himself (doubt 1)",
    ("eva", "ပင်"): "the identifying emphatic «ပင်» (doubt 7)",
    ("pāpa", "ယုတ်မာသော"): "pāpadhammo / pāpiccho: their own word «ယုတ်မာသော» (entries pāpadhammo, pāpakā; "
                           "decision pāpa|0: «ဆိုး» is the member of pāpamittatā)",
}
# the rails form a KEPT value must still have, where it is not the map value itself (negative / agent forms)
KEPT_FORM = {("sampajāno", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ရှိသူ"): r"ကောင်းစွာ ဆင်ခြင်သိမြင်(?:ခြင်း (?:မ)?ရှိသူ|လျက်)",
             ("pameyyo", "ချိန်ဆ၍ ရနိုင်သော"): r"ချိန်ဆ၍ မရနိုင်သူ"}
# the rails form of a FIXED value, where the termbase form is not literally in the segment (finite ending)
FIXED_FORM = {("desetabbo", "ဟောကြားရမည့်"): r"တရား ဟောရမည်"}
EXACT_FREE = {"(no direct equivalent)"}  # the KEPT check of these: the keyword has no Burmese word of its own


def stem_gone(key, rseg):
    g = GONE.get(key) or re.escape(re.sub(r"(?:သည်|သော|၍)$", "", key[1]).replace("… ", ""))
    return re.search(g, rseg) is None


def term_in(terms, seg):
    """the termbase term itself (its pieces around «…») occurs in the segment."""
    return any(all(p.strip() in seg for p in t.split("…")) for t in terms)


n, c, bad, fixed_fams = 0, collections.Counter(), [], collections.Counter()
for l in open(KMAP, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if not m:
        continue
    i = m.group(1)
    for x in m.group(2).split(", "):
        if "=" not in x:
            continue
        k, v = x.split("=", 1)
        n += 1
        t = tb.get(k.lower())
        if t is not None and v in t:
            continue
        key = (k, v)
        if t is None and v.startswith("(no direct"):
            c["no entry, (no direct equivalent)"] += 1
        elif key in FIXED:
            if (any(A.occurs(tt, R[i]) for tt in t) or re.search(FIXED_FORM.get(key, "^$"), R[i])) and stem_gone(key, R[i]):
                c[f"FIXED {FIXED[key]} {k}: «{v}»"] += 1
                fixed_fams[FIXED[key]] += 1
            else:
                bad.append(f"NOT FIXED {i} {k}={v} | termbase: {' | '.join(t)}")
        elif key in STALE:
            if term_in(t, Z[i]) or any(A.occurs(tt, Z[i]) for tt in t):
                c[f"STALE map value {k}: «{v}» (the text has the term)"] += 1
            else:
                bad.append(f"NOT STALE {i} {k}={v}")
        elif key in KEPT:
            if v in EXACT_FREE or re.search(KEPT_FORM.get(key) or re.escape(re.sub(r"(?:သည်|သော)$", "", v)), R[i]):
                c[f"KEPT {k}: «{v}» — {KEPT[key]}"] += 1
            else:
                bad.append(f"KEPT form gone {i} {k}={v}")
        elif t is not None and v in EXACT_FREE and (k, v) in {("sambuddho", v), ("gāmī", v), ("bhūta", v), ("aggaṃ", v)}:
            c[f"KEPT {k}: «{v}» — no word of its own here (paccekasambuddho / akaniṭṭhagāmī NAME / pāṇabhūta … / rajagga)"] += 1
        else:
            bad.append(f"UNEXPLAINED {i} {k}={v} | termbase: {' | '.join(t or ['(no entry)'])}")
print(f"keyword-map values: {n}; = a termbase term: {n - sum(c.values()) - len(bad)}; explained: {sum(c.values())} "
      f"(FIXED {sum(v for k, v in c.items() if k.startswith('FIXED'))}, STALE "
      f"{sum(v for k, v in c.items() if k.startswith('STALE'))}, KEPT {sum(v for k, v in c.items() if k.startswith('KEPT'))}, "
      f"no entry {c['no entry, (no direct equivalent)']}); unexplained or unverified: {len(bad)}")
for k, v in sorted(c.items()):
    print(f"   {v}\t{k}")
for b in bad:
    print(b)
sys.exit(1 if bad else 0)
