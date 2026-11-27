"""Consistency pass (pi-2 Burmese): the synonym tables / lists in the OUTPUT. For every sentence of every chapter, the part
before « – » (or the whole sentence) is split into list items: the Pāli at «, » (or, without commas, at spaces) and the
Burmese at «၊ »; when both give the same number (>= 3) of items they are paired. The same Pāli item must have the same
Burmese item everywhere (case endings of the Burmese item - ကို / ၏ / ဖြင့် … - are compared too: a difference there
is listed, so grammar differences show up and are judged by hand). Also: within one list, two Pāli synonyms must not
share one Burmese item.
usage: python3 -I -X utf8 harmonise_lists.py [-v] [--grep REGEX] [--keep]   (exit 1 if an unexplained item is left)"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-2_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
BR = re.compile(r"\s*\[[^\]]*\]")
f = lambda p: [ID.sub("", l).strip() for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
PSPLIT = re.compile(r"(?<=[.?])(?:\"|”)? (?=\S)")
BSPLIT = re.compile(r"(?<=။) ")
REL = re.compile(r"^(?:Yo|Yā|Yaṃ|Ye|Yāni|yo|yā|yaṃ) ")
TAIL_MY = re.compile(r"\s*(?:ရှိသမျှ|ဟူသော|တို့|။)+$")
END_ITEM = re.compile(r"(ဖြစ်စေ|လည်း)$")
# grammar, not vocabulary: the predicate of a pañhāpucchaka item follows its subject (number; ch16 «ပညာ» = the subject
# paññā the Pāli predicate agrees with), and «… ဖြစ်သည်» / «… ရှိသည်» closes an item that is a statement
GRAMMAR = [(re.compile(r" (?:သဘောတရား|ပညာ)(?:များ)?(?=ဟု| ဖြစ်| ခေါ်|$)"), " N"), (re.compile(r" ဖြစ်(?:ကြ)?သည်$"), ""),
           (re.compile(r" ရှိသည်$"), "")]

# Pāli items with more than one Burmese that are genuine sense / grammar differences (harmonise-notes.md)
KEEP = {
    "rūpataṇhā": "sense: craving for visible forms in the six-object list «rūpataṇhā saddataṇhā …» (ch6, ch17 "
                 "«အဆင်းအရောင်ကို တပ်မက်မှု») vs craving for fine-material existence in «kāmataṇhā rūpataṇhā "
                 "arūpataṇhā» (ch17 «သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု»)",
}


def items(s, t):
    s = s.split(" – ")[0] if " – " in s else s
    t = t.split(" – ")[0] if " – " in t else t
    s = REL.sub("", BR.sub("", s)).rstrip(".?")
    t = TAIL_MY.sub("", BR.sub("", t))
    ys = [y.strip() for y in t.split("၊ ")]
    xs = [x.strip(" \"") for x in (s.split(", ") if ", " in s else s.split(" "))]
    if len(xs) != len(ys) or len(xs) < 3:
        return []
    return list(zip(xs, ys))


def scan():
    tab = collections.defaultdict(lambda: collections.defaultdict(list))
    shared = []
    for p in sorted(PD.glob("*.md")):
        ch = p.name.split("-")[0].split(".")[0]
        for i, (x, y) in enumerate(zip(f(p), f(MD / p.name)), 1):
            xs, ys = PSPLIT.split(x), BSPLIT.split(y)
            if len(xs) != len(ys):
                continue
            for s, t in zip(xs, ys):
                pr = items(s, t)
                seen = {}
                for a, b in pr:
                    a = a.lower().replace("…pe…", "").strip()
                    b = END_ITEM.sub("", b.replace("…", "").strip())
                    for rx, rep in GRAMMAR:
                        b = rx.sub(rep, b)
                    if not a or not b or a.startswith("atthi "):    # «atthi X»: the subject is the section's topic
                        continue
                    tab[a][b].append(f"{ch}:{i}")
                    if b in seen and seen[b] != a:
                        shared.append((f"{ch}:{i}", seen[b], a, b))
                    seen[b] = a
    return tab, shared


if __name__ == "__main__":
    tab, shared = scan()
    grep = re.compile(sys.argv[sys.argv.index("--grep") + 1]) if "--grep" in sys.argv else None
    bad = {k: v for k, v in tab.items() if len(v) > 1 and k not in KEEP}
    if grep:
        bad = {k: v for k, v in bad.items() if grep.search(k)}
    print(f"Pāli list items: {len(tab)}; with more than one Burmese: {len(bad)} (kept: "
          f"{sum(1 for k in KEEP if k in tab and len(tab[k]) > 1)}); shared Burmese inside one list: {len(shared)}")
    for k, v in sorted(bad.items()):
        print(f"\n{k}")
        for t, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            print(f"   {len(locs):3} {t[:110]}   {locs[:6]}")
    if "--keep" in sys.argv:
        for k in KEEP:
            if k in tab:
                print(f"KEPT {k}: {dict((t, len(l)) for t, l in tab[k].items())} – {KEEP[k]}")
    for loc, a, b, t in shared:
        print(f"SHARED {loc}: «{a}» and «{b}» = «{t}»")
    sys.exit(1 if bad or shared else 0)
