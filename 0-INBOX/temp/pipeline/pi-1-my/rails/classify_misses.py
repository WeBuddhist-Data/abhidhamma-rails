"""Classify every termbase-adherence miss of the pi-1 Burmese zero-shot: GENUINE / INFLECTION / ARTEFACT; and every
miss the rails introduce (a miss of the rails that the zero-shot did not have).

usage: python3 -I -X utf8 classify_misses.py   (after build_rails.py + apply_termbase.py + the rails adherence run)
Inputs: rails/adherence-zeroshot.txt (fixed input), rails/adherence-rails.txt, rails/layer-log.tsv, rails/apply-log.tsv.
Writes rails/adherence-classified.tsv (id, keyword, termbase term, text form, class, reason, ch, src).
  * GENUINE row: its family names a layer patch (Lnn, my_formulas_rails.py) or a residual rule (Rnn, apply_termbase.py)
    that must have been applied in this build (layer-log.tsv / apply-log.tsv), its old-form regex must match the
    zero-shot segment, and the keyword must pass in the rails segment (the same occurrence test as adherence_my.py).
  * INFLECTION / ARTEFACT row: its text-form regex must match the segment (zero-shot; rails for src=rails) and its Pāli
    check, where given, must match the segment's Pāli (a leading «!» means it must NOT match).
Any other row is UNVERIFIED and the run fails (exit 1).
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
import adherence_my as A  # noqa: E402

PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
ZS = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
RL = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
TB = ROOT / "AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md"
OUT = HERE / "adherence-classified.tsv"
N = lambda s: unicodedata.normalize("NFC", s)

PRIV_ARISEN = r"Ye dhammā ajātā abhūtā asañjātā"          # the not-arisen / future lists (1-1042, 1-1045)
NEG_PAH = r"\bna (?:dassanena|bhāvanāya) pahātabbā|neva dassanena na bhāvanāya pahātabbā"

# --- INFLECTION / ARTEFACT families: (keyword regex, class, text-form regex, reason, Pāli check or None)
OTHER = [
    (r"nikkhitta", "ARTEFACT", r"လက်မလွှတ်ခြင်း",
     "privative anikkhittachandatā: the termbase gives the positive member «လက်လွှတ်သော»; the text has the negated "
     "verb «ဆန္ဒကို လက်မလွှတ်ခြင်း» (approved 2-01 synonym list)", r"\banikkhitta"),
    (r"dussanā", "ARTEFACT", r"စိတ်မဆိုးခြင်း",
     "privative adussanā: «စိတ်မဆိုးခြင်း» negates the termbase verb «စိတ်ဆိုးခြင်း» (approved 2-01 list)",
     r"\badussanā"),
    (r"manasikārā", "ARTEFACT", r"နှလုံး မသွင်းခြင်း",
     "privative amanasikārā: «နှလုံး မသွင်းခြင်းကြောင့်», the negation splits the compound verb «နှလုံးသွင်း»",
     r"\bamanasikārā"),
    (r"avasesa", "ARTEFACT", r"အကြွင်းအကျန် မရှိ",
     "privative anavasesa(ppahānāya): «အကြွင်းအကျန် မရှိအောင် ပယ်ရန်», the noun of «ကြွင်းကျန်» with «မရှိ»",
     r"\banavases"),
    (r"jātā|sañjātā|nibbattā|abhinibbattā|pātubhūtā|uṭṭhitā|samuṭṭhitā|uppannā|samuppannā", "ARTEFACT",
     r"မမွေးဖွားသေးသော",
     "privative: the not-arisen / future lists (ajātā … asamuṭṭhitā) negate each member («မ…သေးသော»), as the "
     "approved Mātikā anuppannā «မဖြစ်ပေါ်သေးသော»", PRIV_ARISEN),
    (r"pahātabbā|bhāvanāya pahātabbā", "ARTEFACT", r"ပယ်ရမည် မဟုတ်",
     "«na / neva … pahātabbā» negation: burmese-style «pahātabba = ပယ်ရမည့် (negative ပယ်ရမည် မဟုတ်)»", NEG_PAH),
    (r"sekkhā", "ARTEFACT", r"ကျင့်ကြံမှု ပြီးဆုံးသူ၏",
     "privative asekkhā has its own entry «ကျင့်ကြံမှု ပြီးဆုံးသူ၏», which the text has", r"\basekkhā"),
    (r"patho", "ARTEFACT", r"လမ်း နှစ်ခွ",
     "compound: dvedhāpatho has its own entry «လမ်း နှစ်ခွ», which the text has", r"dvedhāpatho"),
    (r"gāho", "ARTEFACT", r"တစ်ထစ်ချ မယူနိုင်ခြင်း",
     "compound: anekaṃsaggāho has its own entry «တစ်ထစ်ချ မယူနိုင်ခြင်း», which the text has", r"anekaṃsaggāho"),
    (r"kamyatā", "ARTEFACT", r"အလံ ထူလိုခြင်း",
     "compound: ketukamyatā has its own entry «အလံ ထူလိုခြင်း», which the text has", r"ketukamyatā"),
    (r"vacassatā", "ARTEFACT", r"သွန်သင်ချက်ကို နားမထောင်ခြင်း",
     "compound: dovacassatā has its own entry «သွန်သင်ချက်ကို နားမထောင်ခြင်း», which the text has", r"dovacassatā"),
    (r"ñāṇaṃ", "ARTEFACT", r"မသိခြင်း",
     "privative: aññāṇaṃ has its own entry «မသိခြင်း», which the text has", r"\baññāṇaṃ"),
    (r"dhāraṇatā", "ARTEFACT", r"စွဲမှတ် မထားခြင်း",
     "privative adhāraṇatā: «စွဲမှတ် မထားခြင်း» negates «စွဲမှတ်ထားခြင်း»", r"\badhāraṇatā"),
    (r"Dasa|dasa|Ekādasa|ekādasa", "ARTEFACT", r"ဆယ်မျိုး|ဆယ့်တစ်မျိုး",
     "compound with -vidhena (own entry vidhena = «မျိုး»): the count of kinds takes «မျိုး», not the classifier "
     "«ပါး» (decision Ekādasa: «ဆယ့်တစ်» only before «မျိုး»)", r"(?i)\b(?:ekā)?dasavidhena"),
    (r"hetukaṃ", "ARTEFACT", r"စိတ်ကို အကြောင်းပြု",
     "compound: cittahetukaṃ has its own entry «စိတ်ကို အကြောင်းပြုသော» (user-approved B6, 2026-11-17), which the "
     "text has; hetukaṃ «အမြစ်» is the root sense of pahātabbahetukaṃ", r"cittahetuk"),
    (r"para", "ARTEFACT", r"ပရနိမ္မိတဝသဝတ္တီ",
     "proper name: binding rule 1 of APPROVED.md (Paranimmitavasavattī stays «ပရနိမ္မိတဝသဝတ္တီ»)",
     r"(?i)paranimmitavasavatt"),
    (r"Saṃviggassa|saṃviggassa", "INFLECTION", r"သံဝေဂ ရသူ၏",
     "genitive of a person: «သံဝေဂ ရသူ၏» (one who is stirred) = the termbase «သံဝေဂ ရသော» + သူ (person) + ၏; the "
     "attributive alone would need a head noun (approved Mātikā wording)", r"(?i)\bsaṃviggassa\b"),
    (r"kusalato ca vipākato", "ARTEFACT", r"ကုသိုလ်စိတ်အနက်လည်းကောင်း၊ အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း",
     "termbase conflict (doubt 1): the undecided entry «kusalato ca vipākato = ကုသိုလ်အဖြစ်လည်းကောင်း ကံ၏ "
     "အကျိုးအဖြစ်လည်းကောင်း» contradicts the decided kusalato «ကုသိုလ်စိတ်», vipākato «အကျိုး ဖြစ်သော စိတ်» and "
     "«vipākato ca kiriyato = အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း …», which the rails follow (L23)",
     r"kusalato ca vipākato"),
]

# --- GENUINE families: (keyword regex, old-form regex in the zero-shot segment, layer / rule id, what was changed[,
#     Pāli check])
GEN = [
    (r"yaṃ", r"^(?!.*ရှိသမျှ)", "R01|R02", "yaṃ etasmiṃ antare … = «… ရှိသမျှ» (residual rules)",
     r"\byaṃ etasmiṃ antare"),
    (r"Yo|Yaṃ|yo|yaṃ|yañca", r"ထိုအချိန်၌ ရှိသော|အကြင်|^(?!.*ရှိသမျှ)", "L02",
     "relative of the definition list = «… ရှိသမျှ» (decision Yo|0); «ထိုအချိန်၌ ရှိသော A …» / no relative → "
     "«ထိုအချိန်၌ A … ရှိသမျှ –»", r"!\byaṃ etasmiṃ antare"),
    (r"uppannaṃ|uppannā|cittaṃ uppannaṃ|dhātu uppannā|uppanno|uppanne|uppanne hetū|uppannaṃ vicāraṃ|"
     r"uppanno ca vicāro|uppanne vitakkavicāre|uppannaṃ vitakkaṃ", r"ဖြစ်ပေါ်လာသော အချိန်၌|ဖြစ်ပေါ်သော", "L01",
     "uppanna = «ဖြစ်ပေါ်ပြီးသော» (citta-opening formula and the chapter-5 «uppanno / etthuppanne»)"),
    (r"vipākato ca kiriyato|kusalato|kiriyato|vipākato", r"အဖြစ်လည်းကောင်း", "L23",
     "«kusalato ca vipākato ca kiriyato ca» = «ကုသိုလ်စိတ်အနက်လည်းကောင်း၊ အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း၊ "
     "ပြုရုံမျှသာ ဖြစ်သော စိတ်အနက်လည်းကောင်း»"),
    (r"vipākato", r"အကျိုး အဖြစ်ဖြင့်", "L12", "«kusalānaṃ (vā) dhammānaṃ vipākato» = «… အကျိုး ဖြစ်သော စိတ်၌»"),
    (r"ākāsa", r"ကောင်းကင်", "L03", "ākāsa = «ဟင်းလင်းပြင်» in the base of infinite space"),
    (r"Catukkanayo|Pañcakanayo|nayo", r"ပါး နည်း", "L07", "«ဈာန် လေးပါး / ငါးပါး ခွဲနည်း»"),
    (r"Suddhikaappaṇihitaṃ", r"မရှိခြင်း သက်သက်", "L08", "«တောင့်တမှု မရှိသော ဈာန် သက်သက်»"),
    (r"indriyānaṃ", r"စွမ်းရည်တို့ ရင့်ရော်", "L09", "«indriyānaṃ paripāko» = «အာရုံခံ အင်္ဂါတို့ ရင့်ရော်ခြင်း»"),
    (r"samuppannā", r"ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော", "L22", "samuppannā = «ဖြစ်ပေါ်လာသော» in the arisen-states list"),
    (r"kammassa katattā", r"ကံကို ပြုခဲ့ခြင်းကြောင့်", "L10", "«ပြုခဲ့သော ကံကြောင့်»"),
    (r"kāyiko|vācasiko", r"ကိုယ်ဖြင့်|နှုတ်ဖြင့်", "L13", "«ကိုယ်ပိုင်းဆိုင်ရာ / နှုတ်ပိုင်းဆိုင်ရာ (မ)ကျူးလွန်ခြင်း»"),
    (r"kodha", r"ဒေါသနှင့် နီးစပ်", "L14", "kodhasāmantā = «အမျက်ဒေါသနှင့် နီးစပ်သော»"),
    (r"sukhā", r"နားဝင်ချို", "L15", "kaṇṇasukhā = «နား သာယာသော»"),
    (r"hadaya", r"နှလုံးသို့", "L16", "hadayaṅgamā = «နှလုံးသားသို့ ရောက်သော»"),
    (r"kamyatā", r"ပိုမို လိုလား", "L17", "bhiyyokamyatā = «ပိုမို လိုချင်ခြင်း»"),
    (r"bojjhaṅgā", r"သိမြင်ခြင်း၏ အင်္ဂါ", "L18", "«ဗောဇ္ဈင် ခုနစ်ပါး»"),
    (r"Saṃvego", r"သံဝေဂ ဟူသည်", "L19", "Saṃvegoti = «သံဝေဂ ရခြင်း ဟူသည်»"),
    (r"uppādāya|anuppādāya", r"ဖြစ်ပေါ်စေရန်", "L20", "«(မ)ဖြစ်ပေါ်ရန်» (dative, not a causative)"),
    (r"anussati", r"အောက်မေ့နိုင်သော", "L21", "pubbenivāsānussati = «ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော»"),
    (r"vibhava", r"ပြတ်စဲခြင်း", "L11", "vibhavataṇhā = «ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု»"),
    (r"paṭicca|vuccati paṭiccasamuppādakusalatā", r"အကြောင်းအကျိုး ဆက်စပ်", "L04",
     "paṭiccasamuppāda = «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ»"),
    (r"samāpatti", r"ဈာန်မှ ထမြောက်", "L06", "samāpattivuṭṭhānakusalatā = «ဈာန် ဝင်စားရာမှ ထမြောက်ရာ၌ …»"),
    (r"Rūpañca nibbānañca|rūpañca nibbānañca", r"ရုပ်နှင့် နိဗ္ဗာန်", "L24", "«ရုပ်လည်း နိဗ္ဗာန်လည်း»"),
    # user-approved termbase change 2026-11-17 (termbase/APPROVED.md; review B3, B5): the only classification change of
    # the review fixes; the zero-shot misses it creates are fixed by L28
    (r"bahiddhā|dhammā bahiddhā|Bahiddhā dhamme ārabbha|bahiddhā dhammā", r"သူတစ်ပါး၌", "L28",
     "bahiddhā (external, not one's own) = «မိမိ၏ ပြင်ပ၌» (user-approved termbase change 2026-11-17)"),
    # user-approved termbase change B6 / B7 / B10, 2026-11-17 (termbase/APPROVED.md)
    (r"cittahetukaṃ", r"စိတ်ကို အမြစ်ပြု", "L36", "cittahetuka = «စိတ်ကို အကြောင်းပြုသော» (user-approved B6)"),
    (r"byāpajjanā", r"(?<!မ)ညှဉ်းဆဲလိုခြင်း", "L37", "byāpajjanā = «ဖောက်ပြန်နေခြင်း» (user-approved B7)"),
    (r"uccheda|ucchedadiṭṭhi", r"သေပြီးနောက်", "L38",
     "uccheda / ucchedadiṭṭhi without the added «သေပြီးနောက်» (user-approved B10)"),
]


def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8")).splitlines():
            if not l.strip():
                continue
            buf.append(l)
            m = A.ID.search(l)
            if m:
                out[m.group(1)] = (p.name[:-3], " ".join(buf))
                buf = []
    return out


def pali_ok(check, text):
    if check is None:
        return True
    if check.startswith("!"):
        return re.search(check[1:], text) is None
    return re.search(check, text) is not None


def misses(path):
    out = []
    for l in open(path, encoding="utf-8"):
        f = N(l).rstrip("\n").strip().split("\t")
        if len(f) == 3 and f[0][:1].isdigit():
            out.append(tuple(f))
    return out


def applied_ids():
    ids = set()
    for name, col in (("layer-log.tsv", 4), ("apply-log.tsv", 4)):
        for l in open(HERE / name, encoding="utf-8").read().splitlines()[1:]:
            f = l.split("\t")
            m = re.match(r"([LR]\d\d)", f[col]) if len(f) > col else None
            if m:
                ids.add(m.group(1))
    return ids


def main():
    tb = A.parse_termbase(TB)
    P, Z, R = segs(PALI), segs(ZS), segs(RL)
    done = applied_ids()
    zs = misses(HERE / "adherence-zeroshot.txt")
    rl = misses(HERE / "adherence-rails.txt")
    zkeys = {(i, k) for i, k, _ in zs}
    todo = [(r, "zeroshot") for r in zs] + [(r, "rails") for r in rl if (r[0], r[1]) not in zkeys]
    rows, counts, bad = [], {}, 0
    for (i, kw, term), src in todo:
        ch, zt = Z[i]
        rt, pt = R[i][1], P[i][1]
        text = zt if src == "zeroshot" else rt
        row = None
        for rkw, cls, form, reason, pcheck in OTHER:
            if re.fullmatch(rkw, kw):
                fm = re.search(form, text)
                if fm and pali_ok(pcheck, pt):
                    row = (i, kw, term, fm.group(0), cls, reason)
                    break
        if row is None and src == "zeroshot":
            for g in GEN:
                rkw, old, lid, what = g[:4]
                if not re.fullmatch(rkw, kw) or not pali_ok(g[4] if len(g) > 4 else None, pt):
                    continue
                om = re.search(old, zt)
                fixed = any(A.occurs(t, rt) for t in tb.get(kw.lower(), []))
                if om and fixed and any(x in done for x in lid.split("|")):
                    row = (i, kw, term, om.group(0) or "(no relative)", "GENUINE", f"{lid}: {what}")
                    break
        if row is None:
            row = (i, kw, term, "", "UNVERIFIED", "no class")
        bad += row[4] == "UNVERIFIED"
        counts[row[4]] = counts.get(row[4], 0) + 1
        rows.append(row + (ch, src))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("id\tkeyword\ttermbase term\ttext form\tclass\treason\tch\tsrc\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    nz = sum(1 for r in rows if r[7] == "zeroshot")
    print(f"{nz} zero-shot misses + {len(rows) - nz} rails-introduced:",
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for r in rows:
        if r[4] == "UNVERIFIED":
            print("UNVERIFIED", r[0], r[1], r[7])
    sys.exit(1 if bad else 0)


main()
