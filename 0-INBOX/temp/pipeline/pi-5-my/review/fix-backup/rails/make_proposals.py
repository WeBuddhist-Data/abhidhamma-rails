"""Write rails/termbase-proposals.tsv (coordinator request 2026-11-22): one line per sense «hw|sense_index<TAB>new
term<TAB>reason», sense_index 0-based in the termbase order. (a) every STALE phrase entry of adherence-classified.tsv:
the new term is the phrase with the layer's / rules' member changes applied (the rails wording); (b) sikkhāya.
Every proposed term is checked: no «, » « / » «; » «၊» or dash, and it must occur (adherence_my.occurs) in every rails
segment whose keyword list has the headword. Exit 1 on a failed check.
usage: python3 -I -X utf8 make_proposals.py"""
import collections
import difflib
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
senses = {}
for l in open(TB, encoding="utf-8"):
    m = re.match(r"^(.*?): \{(.*)\}\s*$", N(l.rstrip("\n")))
    if not m:
        continue
    out, cur = [], ""
    for part in m.group(2).split("; "):
        cur = part if not cur else cur + "; " + part
        if ": " in cur:
            out.append(N(cur.rsplit(": ", 1)[1]).strip())
            cur = ""
    senses[m.group(1)] = out
R = A.segments(ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters")
segs_of = collections.defaultdict(list)
for l in open(ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m and m.group(1) in R:
        for kw in m.group(2).split(", "):
            segs_of[kw.strip().lower()].append(m.group(1))
props = {}
for l in open(HERE / "adherence-classified.tsv", encoding="utf-8"):
    f = N(l).rstrip("\n").split("\t")
    if len(f) < 8 or not f[5].startswith("STALE"):
        continue
    kw, old, new = f[1], f[2], f[3]
    hw = next((h for h in senses if h.lower() == kw.lower()), None)
    k = max(range(len(senses[hw])), key=lambda j: difflib.SequenceMatcher(None, senses[hw][j], new).ratio())
    props.setdefault((hw, k), set()).add(new)
OVERRIDE = {  # stale phrases whose automatic member change missed a word: the rails wording, by hand
    "Asañcicca voropetvā": "မရည်ရွယ်ဘဲ … အသက်မှ ချ၍",
    "sabyābajjhaṃ abyābajjhaṃ": "ဆင်းရဲစေတတ်သော … ညှဉ်းဆဲမှု ကင်းသော",
    "rūpārūpadhātu": "သိမ်မွေ့သော ရုပ်ဘုံ … ရုပ်မရှိသော ဘုံ",
    "Rūpārūpadhātupariyāpannakathā": "သိမ်မွေ့သော ရုပ်ဘုံ … ရုပ်မရှိသော ဘုံ၌ အကျုံးဝင်ခြင်းအကြောင်း ဆွေးနွေးချက်",
}
rows, bad = [], 0
for (hw, k), news in sorted(props.items(), key=lambda x: (x[0][0].lower(), x[0][1])):
    new = OVERRIDE.get(hw) or (sorted(news, key=len)[-1] if len(news) > 1 else next(iter(news)))
    rows.append((hw, k, new, f"(a) stale phrase entry: «{senses[hw][k]}» copies the zero-shot wording of a member word "
                 "that a locked decision changes; the new term is the rails wording (notes-rails.md, termbase doubt 1)"))
hw = next(h for h in senses if h.lower() == "voropetvā")
rows.append((hw, 0, "ချ၍", "(c) §A29: jīvitā voropetvā «အသက်မှ ချ၍» (mātaraṃ jīvitā|0 renders both words; = voropitā "
             "«ချခံရသော», jīvitā voropitā «အသက်မှ ချခံရသော», pi-2 locked); «သတ်၍» leaves jīvitā unrendered"))
hw = next(h for h in senses if h.lower() == "sikkhāya")
rows.append((hw, 0, "သိက္ခာ", "(b) one word for the training: sikkhā / sikkhaṃ / sikkhāyo «သိက္ခာ» (pi-2 / pi-4 locked; "
             "pi-5 sikkhā «သိက္ခာ»); sikkhāya «ကျင့်စဉ်» (pi-1 / pi-2) splits the same word; ^5-648 «sikkhaṃ "
             "paccakkhāya»-type use reads «သိက္ခာ»"))
with open(HERE / "termbase-proposals.tsv", "w", encoding="utf-8") as fh:
    for hw, k, new, why in rows:
        if re.search(r", | / |; |၊|[–—-]", new):
            print("BAD separator", hw, new); bad += 1
        miss = [i for i in segs_of.get(hw.lower(), []) if not A.occurs(new, R[i])]
        if miss:
            print("NOT IN SEGMENT", hw, new, miss[:5]); bad += 1
        fh.write(f"{hw}|{k}\t{new}\t{why}\n")
kinds = collections.Counter(r[3][:3] for r in rows)
print(f"{len(rows)} proposals: " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())) + f"; {bad} failed checks")
sys.exit(1 if bad else 0)
