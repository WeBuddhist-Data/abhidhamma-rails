"""Consistency pass (pi-7 Burmese, Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»): every item of harmonise-todo.md
(H1 … H24), before vs now. For each item the lines whose Pāli matches `pali` are taken (an item is counted only where
the Pāli line has it); in their Burmese the uses of the chosen form and of every other form are counted, in the chapter
files before the pass (harmonise-backup/chapters/) and now. An item fails if an other form is left now, or if a line
that has the Pāli item lacks the chosen form now. One book-wide test runs as a function: headings / colophons
(identical Pāli = identical Burmese). Model: pi-6-my/harmonise_scan.py (read only).
usage: python3 -I -X utf8 harmonise_scan.py [--table]   (--table also writes harmonise-table.tsv:
       Pāli<TAB>chosen Burmese<TAB>other forms (uses before)<TAB>chapters with an other form before)"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
VA = r"(?:\{[^}]*\})"

# (item, Pāli label for the table, Pāli regex on the line, chosen Burmese (regex), [other forms (regex)], kind)
# kind: B = term / frame drift (changed), R = rule verified (kept)
ITEMS = [
    ("H1 «Anulomaṃ.» closing the positive order", "Anulomaṃ. (a whole line)", r"^Anulomaṃ\.$",
     r"^အဟုတ်ပြ ပုံစံ။$", [r"^လျော်ညီခြင်း စိတ်။$"], "B"),
    ("H1 the mind moment «anulomaṃ» inside a sentence keeps «လျော်ညီခြင်း စိတ်»", "anulomaṃ gotrabhussa…",
     r"[Aa]nulomaṃ gotrabhussa", r"လျော်ညီခြင်း စိတ်သည် အနွယ် ပြောင်းခြင်း", [], "R"),
    ("H2 a noun before «ārabbha / garuṃ katvā» (no stray «သည်»)", "Uddhaccaṃ / Domanassaṃ ārabbha, … jhānaṃ garuṃ katvā",
     r"(?:[Uu]ddhaccaṃ|[Dd]omanassaṃ) ārabbha|jhānaṃ garuṃ katvā|ñāṇaṃ garuṃ katvā",
     r"(?:မှု|ဈာန်|ဉာဏ်)ကို (?:အာရုံပြု|လေးစား)", [r"(?:မှု|ဈာန်|ဉာဏ်)သည်ကို"], "B"),
    ("H3 asaññasattānaṃ (possessive genitive)", "asaññasattānaṃ", r"[Aa]saññasattānaṃ", r"အသညသတ်တို့၏",
     [r"အသညသတ်တို့၌"], "B"),
    ("H4 tassa paṭighātatthāya", "tassa paṭighātatthāya", r"tassa paṭighātatthāya", r"ထိုအမှုကို ချေဖျက်ရန်",
     [r"ပယ်ဖျက်ရန်အတွက်"], "B"),
    ("H5 the heinous deeds (pi-5)", "mātughāti- / pitughāti- / arahantaghāti- / ruhiruppāda- / saṅghabhedakammaṃ",
     r"(?:mātughāti|pitughāti|arahantaghāti|ruhiruppāda|saṅghabheda)kamm",
     r"(?:သတ်|ထွက်စေ|သင်းခွဲ)ခြင်း ကံ", [r"သတ်သော ကံ", r"ထွက်စေသော ကံ", r"ဖြိုခွဲသော ကံ"], "B"),
    ("H6 two terms on one noun stacked «A၊ B N» (2-08 «appamāṇārammaṇe paritte khandhe», compounds)",
     "parittārammaṇe paritte khandhe …, parittārammaṇaparittacittasamaṅgissa …",
     r"(?:paritt|mahaggat|appamāṇ)ārammaṇ(?:e|ā|a)(?: |)(?:paritt|mahaggat|appamāṇ)(?:e|ā|a)",
     r"အာရုံပြုသော၊ (?:အကန့်အသတ်|ကြီးမြတ်|အတိုင်းအဆ)",
     [r"အာရုံပြုသော (?:အကန့်အသတ် ရှိသော|ကြီးမြတ်သော|အတိုင်းအဆ မရှိသော)"], "B"),
    ("H6 pīti + sukha on one aggregate «A၊ B N» (2-01 … 2-02)", "pītisahagatā ca sukhasahagatā ca tayo khandhā",
     r"pītisahagatā ca sukhasahagatā ca tayo khandhā", r"ပီတိနှင့်အတူ ဖြစ်သော၊ သာယာမှုနှင့်အတူ ဖြစ်သော အစုအဝေး",
     [], "R"),
    ("H7 / H17 kamma-kind label «Sahajātā –» in a kamma line", "… kammapaccayena paccayo – sahajātā … Sahajātā –",
     r"kammapaccayena.*Sahajātā – .*nānākkhaṇik|kammapaccayena.*nānākkhaṇik.*Sahajātā – ",
     r"အတူ ပေါ်ပေါက်သည့် ကံ – ", [r"(?:^|[။၊] )အတူ ပေါ်ပေါက်ခြင်း – "], "B"),
    ("H9 sekkhā vā puthujjanā vā (pi-1 «vā … vā»)", "sekkhā vā puthujjanā vā", r"[Ss]ekkhā vā puthujjanā vā",
     r"ကျင့်ကြံဆဲသူတို့ဖြစ်စေ၊ ပုထုဇဉ်တို့ဖြစ်စေ", [r"သော်လည်းကောင်း၊ ပုထုဇဉ်"], "B"),
    ("H10 anumajjantena", "anumajjantena", r"anumajjantena", r"ပြန်လည် စိစစ်လျက်", [r"အစဉ်လိုက် သုံးသပ်လျက်"], "B"),
    ("H11 / H9 «X Y-assa…pe…» = conditioning / conditioned (not one list)",
     "rūpāyatanaṃ cakkhuviññāṇassa…pe…, cakkhāyatanaṃ cakkhuviññāṇassa…pe…, kabaḷīkāro āhāro imassa kāyassa…pe…",
     r"[Rr]ūpāyatanaṃ cakkhuviññāṇassa…|[Cc]akkhāyatanaṃ cakkhuviññāṇassa…|[Kk]abaḷīkāro āhāro imassa kāyassa…",
     r"(?:နယ်ပယ်|အာဟာရ)သည် (?:မျက်စိ သိစိတ်|ဤကိုယ်)အား…",
     [r"နယ်ပယ်၊ မျက်စိ သိစိတ်တို့အား…", r"အာဟာရ၊ ဤကိုယ်တို့အား…"], "B"),
    ("H12 dve mahābhūtā", "dve mahābhūtā", r"dve mahābhūtā", r"မူလဓာတ်ကြီး နှစ်ပါး", [r"နှစ်ခု မူလဓာတ်ကြီး"], "R"),
    ("H14 «evaṃ gaṇetabbaṃ» without «yathā»", "(… evaṃ gaṇetabbaṃ)", r"\(evaṃ ga[ṇ][ea]tabbaṃ\)",
     r"\(ဤသို့ ရေတွက်ရမည်\)", [r"\(ထိုနည်းတူ ရေတွက်ရမည်\)"], "B"),
    ("H14 «evaṃ vitthāretabbaṃ» without «yathā» after a vāra list", "(Sahajātavārampi…pe… pañhāvārampi evaṃ vitthāretabbaṃ)",
     r"pañhāvārampi evaṃ vitthāretabbaṃ", r"ကိုလည်း ဤသို့ အကျယ် ချဲ့ရမည်", [r"ဖော်ပြချက်လည်း ထိုနည်းတူ အကျယ်"], "B"),
    ("H15 the sixth-dyad terms (3-03-06 = 3-07-08-10)", "X-vippayutto X-iyo / X-vippayutto noX-iyo",
     r"(?<![a-z])(?:[Āā]sava|[Ss]aññojana|[Gg]antha|[Oo]gha|[Yy]oga|[Nn]īvaraṇa|[Pp]arāmāsa|[Uu]pādāna|[Kk]ilesa)vippayutt"
     r"(?:o|aṃ|ā|ena|assa|āya|e|ānaṃ) (?:sāsav|anāsav|saññojaniy|asaññojaniy|ganthaniy|aganthaniy|oghaniy|anoghaniy|"
     r"yoganiy|ayoganiy|nīvaraṇiy|anīvaraṇiy|parāmaṭṭh|aparāmaṭṭh|upādāniy|anupādāniy|saṃkilesik|asaṃkilesik)",
     r"နှင့် ကင်းကွာ(?:သော်လည်း|၊) ", [], "R"),
    ("H16 ajjhattika attributive (locked «အတွင်းပိုင်း»)", "ajjhattikā mahābhūtā / indriyā, ajjhattikabāhirā",
     r"ajjhattik(?:ā mahābhūt|ā indriy|aṃ mahābhūt|abāhirā mahābhūt)", r"အတွင်းပိုင်း(?:၊)? (?:မူလဓာတ်ကြီး|စွမ်းရည်|ပြင်ပ)",
     [r"အတွင်းပိုင်း ဖြစ်သော"], "B"),
    ("H16 3-02 ^565 «eko khandho ca cakkhāyatanañca tiṇṇannaṃ khandhānaṃ…» (subject + recipient)",
     "eko khandho ca cakkhāyatanañca tiṇṇannaṃ khandhānaṃ…",
     r"eko khandho ca cakkhāyatanañca tiṇṇannaṃ khandhānaṃ…", r"နယ်ပယ်လည်းကောင်း အစုအဝေး သုံးပါးတို့အား…",
     [r"နယ်ပယ်အားလည်းကောင်း၊ အစုအဝေး သုံးပါးတို့အားလည်းကောင်း"], "B"),
    ("H18 chandarāga (locked pi-2)", "chandarāgo", r"chandarāg", r"လိုလားမှု ရာဂ", [r"ဆန္ဒရာဂ"], "B"),
    ("H19 a bare «X-sadisa» (no «paccaya») = the bare name", "sahajātasadisaṃ / purejātasadisaṃ / ārammaṇasadisā …",
     r"(?<![a-z])(?:anuloma|paṭiccavāre |paccayavāre |tīṇi |)(?:sahajāta|purejāta|pacchājāta|ārammaṇa|sampayutta)sadis",
     r"(?:ပေါ်ပေါက်ခြင်း|ဖြစ်ပေါ်ခြင်း|အာရုံ|ယှဉ်တွဲခြင်း)နှင့် တူ",
     [r"(?:အတူ ပေါ်ပေါက်ခြင်း|ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း|နောက်မှ ဖြစ်ပေါ်ခြင်း|အာရုံ|ယှဉ်တွဲခြင်း)ဟူသော အကြောင်းနှင့် တူ"
      r"(?=[^()]*\))(?![^()]*paccaya)"], "B"),
    ("H20 a vāra list before «vitthāretabba» (object «ကိုလည်း»)", "(Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ)",
     r"\(?Sahajātavārampi…pe… (?:pañha|sampayutta)vārampi (?:paṭiccavārasadisaṃ )?(?:evaṃ )?vitthāretabbaṃ",
     r"ဖော်ပြချက်ကိုလည်း", [r"ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… (?:ပြဿနာ|ယှဉ်တွဲခြင်း)အလိုက် ဖော်ပြချက်လည်း"], "B"),
    ("H20 labbhati", "labbhati / labbhanti (positive)", r"(?<!na )labbhat?i(?!ya)", r"တွေ့ရ", [r"ကံကို ရသည်"], "B"),
    ("H22 heṭṭhā (earlier in the text, pi-6 «ရှေ့၌»)", "heṭṭhā", r"heṭṭhā", r"\(ရှေ့", [r"\(အထက်"], "B"),
    ("H23 {hetuyā aṭṭha?} kept as an uncertain variant", "{hetuyā aṭṭha?}", r"\{hetuyā aṭṭha\?\}",
     r"\{ပါဌ်ကွဲ \(\(မသေချာ\)\): hetuyā aṭṭha\}", [r"\{အမြစ်ဟူသော အကြောင်း၌ ရှစ်ခု"], "B"),
    ("H23 piṭṭhi «နောက်ဆုံး» / antima «အဆုံးသတ်» kept apart", "Piṭṭhidukaṃ … / Antimadukaṃ",
     r"[Pp]iṭṭhiduk|Antimaduk", r"နောက်ဆုံး နှစ်မျိုးတွဲ|အဆုံးသတ် နှစ်မျိုးတွဲ", [], "R"),
    ("H24 «…paṭiccavārasadisaṃ» (singular) «…နှင့် တူသည်»", "(Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ)",
     r"sampayuttavārampi paṭiccavārasadisaṃ(?! vitthār| evaṃ)", r"ဖော်ပြချက်နှင့် တူသည်", [r"ဖော်ပြချက်နှင့် တူကြသည်"], "B"),
    ("H24 «yathā kusalattike pañhāvāraṃ, evaṃ …»", "Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ",
     r"[Yy]athā kusalattike pañhāvāraṃ,? evaṃ", r"ပြဿနာအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ",
     [r"ပြဿနာအလိုက် ဖော်ပြချက်အတိုင်း ထိုနည်းတူ"], "B"),
    ("align: the formless-base minds (1-01 form)", "ākāsānañcāyatanakusalaṃ …",
     r"(?:ākāsānañc|viññāṇañc|ākiñcaññ|nevasaññānāsaññ)āyatana(?:kusal|kiriy|vipāk)",
     r"နယ်ပယ် (?:ကုသိုလ်|ပြုရုံမျှသာ|ကံ၏ အကျိုး)", [r"နယ်ပယ်နှင့် ဆိုင်သော"], "B"),
    ("align: «yathā … evaṃ kātabbaṃ ninnānākaraṇaṃ» (no Pāli «,»: no «၊»)",
     "(Yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.)",
     r"evaṃ kātabbaṃ ninnānākaraṇaṃ", r"ထိုနည်းတူ ကွဲပြားချက် မရှိ ပြုရမည်", [r"ပြုရမည်၊ ကွဲပြားချက် မရှိ"], "B"),
]


def clean(rx):
    """a readable form of a regex for the table («(?:A|B)» -> «A / B», no anchors / look-arounds)"""
    rx = re.sub(r"\(\?[=!<][^()]*(?:\([^()]*\)[^()]*)*\)", "", rx)
    rx = rx.replace("(?:", "(").replace("\\", "").strip("^$")
    rx = re.sub(r"\(([^()|]*\|[^()]*)\)", lambda m: "[" + m[1].replace("|", " / ") + "]", rx)
    return rx.replace("[။၊] ", "").replace("(^", "(")


def heading_test(md):
    """headings and colophon lines: identical Pāli = identical Burmese."""
    D = collections.defaultdict(set)
    for p in sorted(PD.glob("*.md")):
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            if x.startswith("#") or re.search(r"(?:niṭṭhito|niṭṭhitaṃ|niṭṭhitā|anulomaṃ|vāro)\.$", x):
                D[re.sub(r"^#+ ", "", x)].add(re.sub(r"^#+ ", "", y))
    bad = [f"{k}: {sorted(v)}" for k, v in D.items() if len(v) > 1]
    return len(D), bad


def pairs(md):
    for p in sorted(PD.glob("*.md")):
        ch = p.name[:4] if p.name[0].isdigit() else p.name[:-3]
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            yield ch, re.sub(VA, "", x) if "aṭṭha?" not in x else x, y


def count(md, pali, chosen, others):
    nl = nc = miss = 0
    no = [0] * len(others)
    chs = [set() for _ in others]
    for ch, x, y in pairs(md):
        if not re.search(pali, x):
            continue
        nl += 1
        c = len(re.findall(chosen, y))
        nc += c
        miss += c == 0
        for i, o in enumerate(others):
            k = len(re.findall(o, y))
            no[i] += k
            if k:
                chs[i].add(ch)
    return nl, nc, miss, no, chs


def main(argv):
    rows, fails = [], 0
    for item, label, pali, chosen, others, kind in ITEMS:
        nl, nc0, _, no0, ch0 = count(BEFORE, pali, chosen, others)
        nl1, nc1, miss1, no1, _ = count(NOW, pali, chosen, others)
        left = sum(no1)
        bad = left or not nl1 or miss1
        fails += bool(bad)
        chs = sorted(set().union(*ch0)) if others else []
        print(f"{'FAIL' if bad else 'OK  '} {item}: {nl1} lines; chosen {nc0} -> {nc1}"
              + (f"; other forms {sum(no0)} -> {left}" if others else "")
              + (f"; {miss1} lines without it" if miss1 else ""))
        rows.append((label, clean(chosen),
                     "; ".join(f"{clean(o)} ({n})" for o, n in zip(others, no0) if n) or "-",
                     ", ".join(chs) or "-"))
    n0, b0 = heading_test(BEFORE)
    n1, b1 = heading_test(NOW)
    fails += bool(b1)
    print(f"{'FAIL' if b1 else 'OK  '} headings / colophons: identical Pāli = identical Burmese: {n1} units; "
          f"differing {len(b0)} -> {len(b1)}")
    for b in b1[:12]:
        print("      ", b[:220])
    rows.append(("(every heading / colophon)", "one Burmese each", f"differing before: {len(b0)}", "-"))
    if "--table" in argv:
        with open(HERE / "harmonise-table.tsv", "w", encoding="utf-8") as fh:
            fh.write("Pāli\tchosen Burmese\tother forms (uses before the pass)\tchapters\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")
    print(f"{len(ITEMS) + 1 - fails} / {len(ITEMS) + 1} items OK")
    return fails


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
