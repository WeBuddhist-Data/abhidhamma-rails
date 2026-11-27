"""Coordinator follow-up 2026-11-22 (item 3): termbase proposals after the bilingual-review fixes.
Writes rails/termbase-proposals-2.tsv (hw|sense_index <TAB> new term <TAB> reason; sense_index 0-based in the termbase
file's order; an index equal to the entry's sense count = a NEW sense appended) and checks every proposal against the
rails text: a replaced sense's new term must occur (adherence_my.occurs) in every rails segment whose keyword list holds
the headword; for an added sense, every such segment must hold one of the entry's terms (old + new) and the new term
must occur in the segments it is proposed for. No ", ", " / ", "; ", «၊» or dash inside a term. Exit 1 on a failure.
usage: python3 -I -X utf8 make_proposals2.py   (read only except the .tsv)"""
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
TB = ROOT / "AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md"
KW = ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
RL = ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters"
OUT = HERE / "termbase-proposals-2.tsv"
_AK = "ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော"
# (headword as in the termbase file, sense index, new term, segments the new term is for, reason)
PROP = [
    ("mātughātako ānantariko", 0, f"အမိကို သတ်သူသည် {_AK}", None,
     "stale phrase entry (also serves Mātughātako ānantariko ^5-877): ānantariko «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော» "
     "(termbase change 2026-11-22, review B6, rails L42); was «… အနန္တရိယကံ ရှိသော»"),
    ("pitughātako ānantariko", 0, f"အဖကို သတ်သူသည် {_AK}", None,
     "stale phrase entry: ānantariko «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော» (change 2026-11-22, B6, L42)"),
    ("saṅghabhedako ānantariko", 0, f"သံဃာကို သင်းခွဲသူသည် {_AK}", None,
     "stale phrase entry (also serves Saṅghabhedako ānantariko ^5-860): ānantariko «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော» "
     "(change 2026-11-22, B6, L42)"),
    ("ruhiruppādako ānantariko", 0, f"ဘုရားရှင်၏ သွေးကို ထွက်စေသူသည် {_AK}", None,
     "stale phrase entry: ānantariko «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော» (change 2026-11-22, B6, L42)"),
    ("Bhagavatā abhisambuddhāni", 0, "မြတ်စွာဘုရား … ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့သော", None,
     "stale phrase entry: abhisambuddhāni «ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့သော» (change 2026-11-22, review A5, "
     "rails F05); was «… ထိုးထွင်း သိတော်မူခဲ့သော»"),
    ("Dukkhaṃ parinipphannaṃ", 0, "ဒုက္ခ … ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော", None,
     "stale phrase entry: review B9 (rails L45), dukkhaññeva parinipphannaṃ «ဒုက္ခသည်သာ ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော» "
     "(dukkhaṃ «ဒုက္ခ»; no doubled «ဆင်းရဲ ဒုက္ခ»)"),
    ("natthika", 0, "ကံ၏ အကျိုး မရှိ", None,
     "review A20 (rails F27): natthikavādā «ကံ၏ အကျိုး မရှိဟု ဆိုသော ဝါဒ ရှိသူ» (akiriyavādā «ပြုခြင်း၏ အကျိုး မရှိဟု …»); "
     "natthika occurs only in ^5-296; was «ဘာမျှ မရှိ»"),
    ("viloketi", 1, "ကြည့်ရှုသည်", ["5-401"],
     "NEW sense (index 1, appended), gloss 'surveys, looks over (all the quarters), in sabbā ca disā viloketi': review "
     "A10 (rails F22) «အရပ် အားလုံးကိုလည်း ကြည့်ရှု၏» ^5-401; sense 0 «ဘေးသို့ ကြည့်သည်» stays (looks aside: ^5-336 "
     "ālokite vilokite, ^5-852): one replaced sense would contradict those two segments"),
    ("ādāna", 1, "ယူခြင်း", ["5-546"],
     "NEW sense (index 1, appended), gloss 'taking, in adinnādāna (compound final)': review B11 (rails F13) «မပေးသည်ကို "
     "ယူခြင်း» ^5-546, = the termbase's ādānaṃ «ယူခြင်း» (in adinnādānaṃ); sense 0 «ကိုင်ခြင်း» stays for "
     "ādānanikkhepanaṃ ^5-293"),
    ("añño", 1, "အခြား", ["5-89", "5-90"],
     "NEW sense (index 1, appended), gloss 'other, in anañño avigato «not other»': review A17 (R203 withdrawn) «အခြား "
     "မဖြစ်ဘဲ မကွယ်ပျောက်ဘဲ» ^5-89 / ^5-90 = the sample ^5-78; sense 0 «တခြားစီ» stays (the approved frame «aññaṃ A "
     "añño B», 14 other segments)"),
]
BAD = re.compile(r", | / |; |၊|[–—-]")


def main():
    raw = {}
    for l in open(TB, encoding="utf-8"):
        m = re.match(r"^(.*?): \{(.*)\}\s*$", N(l.rstrip("\n")))
        if m:
            raw[m.group(1)] = m.group(2)
    tb = A.parse_termbase(TB)
    R = A.segments(RL)
    kw = {}
    for l in open(KW, encoding="utf-8"):
        m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
        if m:
            kw[m.group(1)] = [x.strip().lower() for x in m.group(2).split(", ")]
    err, rows = [], []
    for hw, si, new, only, reason in PROP:
        if hw not in raw:
            err.append(f"{hw}: not a termbase headword")
            continue
        senses = tb[hw.lower()]
        if si > len(senses):
            err.append(f"{hw}: sense index {si} > {len(senses)} senses")
        if BAD.search(new):
            err.append(f"{hw}: delimiter inside the term «{new}»")
        ids = sorted(i for i, k in kw.items() if hw.lower() in k)
        if si < len(senses):                       # replaced sense: the new term in every segment
            terms = senses[:si] + [new] + senses[si + 1:]
            miss = [i for i in ids if not A.occurs(new, R.get(i, "")) and not any(A.occurs(t, R.get(i, "")) for t in terms if t != new)]
            miss_new = [i for i in ids if not A.occurs(new, R.get(i, ""))]
            if len(senses) == 1 and miss_new:
                err.append(f"{hw}: «{new}» missing in {miss_new}")
            if miss:
                err.append(f"{hw}: no term of the entry in {miss}")
            note = f"replaces sense {si} «{senses[si]}»; occurs in {len(ids) - len(miss_new)} of {len(ids)} segments ({' '.join(ids)})"
        else:                                      # added sense
            terms = senses + [new]
            miss = [i for i in ids if not any(A.occurs(t, R.get(i, "")) for t in terms)]
            miss_new = [i for i in (only or []) if not A.occurs(new, R.get(i, ""))]
            if miss or miss_new:
                err.append(f"{hw}: uncovered segments {miss}, new term missing in {miss_new}")
            note = f"adds sense {si}; new term in {' '.join(only)}; every one of the {len(ids)} segments holds a term of the entry"
        rows.append((f"{hw}|{si}", new, reason))
        print(f"{hw}|{si}\t«{new}»\t{note}")
    if err:
        print("\n".join(err))
        sys.exit(1)
    with open(OUT, "w", encoding="utf-8") as f:
        for r in rows:
            f.write("\t".join(r) + "\n")
    print(f"{len(rows)} proposals written to {OUT.name}")


main()
