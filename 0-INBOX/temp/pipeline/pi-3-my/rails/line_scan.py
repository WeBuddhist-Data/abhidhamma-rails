"""Per-line scan of the rails families (stricter than the per-segment adherence check; model pi-2-my/rails/line_scan.py):
a Pāli line holding the family's Pāli form whose Burmese line has fewer termbase forms than the Pāli has hits (req),
or still has a wrong form (forbid). A family may name a Pāli «unless» regex: lines matching it are not scanned for it.
Variant readings in square brackets stay Pāli and are not counted, except for a family marked «raw» (the translated
variant note of ^3-112).
pi-3's one GENUINE family is the review fix F1 (buddho, apply_fixes.py), with F2 (A4, nāmarūpena); the other families
are the four logged text inconsistencies
H1-H4 (mapper-my/map-harmonise-notes.md) as the locked termbase decides them, and the multi-word / plural-marker
terms of the termbase that the loose adherence check (particles «တို့» / «များ» stripped) cannot see.
usage: line_scan.py <pali dir> <burmese dir> [--stats]   (prints one line per failure; nothing = clean; --stats: Pāli hits per family)"""
import pathlib
import re
import sys
import unicodedata

pd, md = map(pathlib.Path, sys.argv[1:3])
STATS = {}
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
W = "a-zA-Zāīūṃṅñṭḍṇḷ"
B = rf"(?<![{W}])"          # Pāli word start
E = rf"(?![{W}])"           # Pāli word end
FAM = [  # (family, Pāli regex, Burmese regex, mode, Pāli «unless» regex or None[, "raw"])
    ("H1 maccu = သေခြင်း (termbase maccu, decision: approved as built)", rf"{B}maccu", r"သေခြင်း", "req", None),
    ("H1 mataṃ = သေခြင်း (termbase mataṃ)", r"jarāmataṃ", r"သေခြင်း", "req", None),
    ("H1 maccu / mataṃ (pi-2 forms)", r"maccu|jarāmataṃ", r"သေဆုံး|သေမင်း", "forbid", None),
    ("H2 pucchake = ဖော်ပြချက် (variant note ^3-112)", r"pañhāpucchake", r"မေးခွန်းများဖြင့် ဖော်ပြချက်", "req", None, "raw"),
    ("H2 pucchakena = မေးခွန်း", r"moghapucchakena", r"မေးခွန်း အချည်းနှီး", "req", None),
    ("H2 pucchakena (other sense)", r"moghapucchakena", r"ဖော်ပြချက်", "forbid", None),
    ("H4 arūpa planes = ရုပ်မရှိသော", r"(?i)arūp(?:āvacar|abhav|ūpapatt)", r"ရုပ်မရှိသော", "req", None),
    ("H4 arūpa planes (spaced)", r"(?i)arūp(?:āvacar|abhav|ūpapatt)", r"ရုပ် မရှိသော", "forbid", None),
    ("H4 arūpa non-material = ရုပ် မဟုတ်သော", r"Arūp(?:akkhandhā|ino|īhi)", r"ရုပ် မဟုတ်သော", "req", None),
    ("H4 arūpa non-material (planes / joined form)", r"Arūp(?:akkhandhā|ino|īhi)", r"ရုပ်မရှိ|ရုပ်မဟုတ်", "forbid", None),
    ("H4 arūpa (wrong forms anywhere)", r"^", r"ရုပ် မရှိသော|ရုပ်မဟုတ်သော", "forbid", None),
    ("T pariyāpanna = ဘဝဘုံတို့၌ အကျုံးဝင်သော", rf"{B}pariyāpann", r"ဘဝဘုံတို့၌ အကျုံးဝင်သော", "req", None),
    ("T apariyāpanna = ဘဝဘုံတို့၌ အကျုံးမဝင်သော", rf"{B}apariyāpann", r"ဘဝဘုံတို့၌ အကျုံးမဝင်သော", "req", None),
    ("T pariyāpanna (plural «များ»)", r"pariyāpann", r"ဘဝဘုံများ", "forbid", None),
    ("T paṭicca = အကြောင်းတို့ကို မှီ၍", rf"{B}[Pp]aṭicca", r"အကြောင်းတို့ကို မှီ၍", "req", None),
    ("T dhammehi vippayuttā (item) = …သဘောတရားများနှင့် ကင်းကွာသော",
     rf"{B}(?!tehi{E})[{W}]+ehi dhammehi ye dhammā vippayuttā", r"သဘောတရားများနှင့် ကင်းကွာသော", "req", None),
    ("T X-ehi dhammehi (item) = …သဘောတရားများနှင့်", rf"{B}(?!tehi{E})[{W}]+ehi dhammehi{E}", r"သဘောတရားများနှင့်", "req", None),
    ("T X-ehi dhammehi (item, «တို့»)", rf"{B}(?!tehi{E})[{W}]+ehi dhammehi{E}", r"(?<!ထို)သဘောတရားတို့နှင့်", "forbid", None),
    ("T Uppannā / Uppannehi (word) = ဖြစ်ပေါ်ပြီးသော", rf"{B}[Uu]ppann(?:ā|ehi){E}", r"ဖြစ်ပေါ်ပြီးသော", "req", None),
    ("T Anuppannā / Anuppannehi = မဖြစ်ပေါ်သေးသော", rf"{B}[Aa]nuppann(?:ā|ehi){E}", r"မဖြစ်ပေါ်သေးသော", "req", None),
    ("T nāmarūpa = စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (binding rule)", r"(?i)nāmarūpa", r"စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "req", None),
    ("F1 subuddho = ကောင်းစွာ နားလည်ပြီး ဖြစ်သည် (termbase buddho|0, review A3 + B3)", rf"{B}subuddho",
     r"ကောင်းစွာ နားလည်ပြီး ဖြစ်သည်", "req", None),
    ("F1 subuddho (old form, anywhere)", r"^", r"နားလည်အပ်", "forbid", None),
    ("F2 nāmarūpena (item) = စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့် (review A4)", rf"{B}nāmarūpena{E}",
     r"စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့်", "req", None),
    ("F2 nāmarūpa pair (old item form, anywhere)", r"^", r"ရုပ်ပိုင်းနှင့်", "forbid", None),
    ("K tehi dhammehi = ထိုသဘောတရားတို့နှင့် (kept: no termbase term decides it; doubt 1)", rf"{B}tehi dhammehi{E}",
     r"ထိုသဘောတရားတို့နှင့်", "req", None),
]
for p in sorted(pd.glob("*.md")):
    a = [N(l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [N(l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for k, (x, y) in enumerate(zip(a, b), 1):
        xr = re.sub(r"\s*\^\S+\s*$", "", x)
        xb = re.sub(r"\[[^\]]*\]", "", xr)     # variant readings stay Pāli: not counted
        yb = re.sub(r"\s*\^\S+\s*$", "", y)
        for fam, pk, st, mode, unless, *raw in FAM:
            xs = xr if raw else xb
            n = len(re.findall(pk, xs))
            if not n or (unless and re.search(unless, xs)):
                continue
            got = len(re.findall(st, yb))
            STATS[fam] = STATS.get(fam, 0) + n
            if (mode == "req" and got < n) or (mode == "forbid" and got):
                ids = re.findall(r"\^(\S+)\s*$", x)
                print(f"{p.name.split('-')[0].split('.')[0]}:{k}\t{fam}\t{mode} P×{n} M×{got}\t{ids}")
if "--stats" in sys.argv:
    for fam, *_ in FAM:
        print(f"stats\t{STATS.get(fam, 0)}\t{fam}")
