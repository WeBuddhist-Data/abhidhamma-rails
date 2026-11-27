"""pi-1 Burmese rails: the bilingual-review fixes that cannot be one source string of the rails layer (review/report-A.md,
review/report-B.md; decisions in review/fix-brief.md, results and the items not applied in review/fix-notes.md).
The fixes that change a repeated formula or term are rails-layer patches (my_formulas_rails.py, L28 … L35).

usage: python3 -I -X utf8 apply_fixes.py
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Reads and rewrites AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters.

Every fix is an explicit rule, applied line by line (Pāli and Burmese lines are aligned inside each segment):
  - scope: a list of segment IDs, or chapter-name prefixes (None = all 14 chapters);
  - trigger: a regex the aligned Pāli line must match, else the line is not touched;
  - change: exact Burmese old → new, or a pattern function (F1) that rebuilds the old Burmese run from the Pāli items
    and fails unless it is found exactly once on the line;
  - expected replacement count over the whole book: the run fails (and writes nothing) if the count differs.
Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule); line = line number in the chapter file.
Deterministic: no randomness, files and rules in fixed order.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
COMMA = "၊ "

# ---------------------------------------------------------------- F1 (B8): the bhūmi locative frame
# «X-bhūmiyaṃ kāmāvacare, rūpāvacare, …» (4-01 with «,», 4-02 without): the plane items are locatives of a noun
# (the mind of that plane). Zero-shot / rails: «… ကာမဘုံနှင့် ဆိုင်သည်၌၊ … ဆိုင်သည်၌၊» (a double locative without a
# noun) → «… ကာမဘုံနှင့် ဆိုင်သော စိတ်၊ … စိတ်တို့၌၊» (one item: «… စိတ်၌၊»).
F1_ITEM = {"kāmāvacare": "ကာမဘုံနှင့် ဆိုင်", "rūpāvacare": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်",
           "arūpāvacare": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်", "apariyāpanne": "ဘဝဘုံတို့၌ အကျုံးမဝင်"}
F1_P = re.compile(r"bhūmiyaṃ((?:,? (?:kāmāvacare|rūpāvacare|arūpāvacare|apariyāpanne)(?![\w]))+)")


def f1(p, m):
    pm = F1_P.search(p)
    items = re.findall(r"kāmāvacare|rūpāvacare|arūpāvacare|apariyāpanne", pm.group(1))
    stems = [F1_ITEM[x] for x in items]
    old = COMMA.join(s + "သည်၌" for s in stems) + COMMA
    new = COMMA.join(s + "သော စိတ်" for s in stems) + ("တို့၌" if len(stems) > 1 else "၌") + COMMA
    if m.count(old) != 1:
        raise ValueError(f"F1: {len(items)} plane items, old run found {m.count(old)}×")
    return m.replace(old, new), [(old, new)]


# ---------------------------------------------------------------- the rules, in order
# (rule, scope ids | None, chapter prefixes | None, Pāli trigger regex, change, expected)
#   change: ("s", old, new) exact | ("f", function)
_TAN = "တပ်မက်မှု"
RULES = [
    ("F1 B8 bhūmi frame «X-bhūmiyaṃ kāmāvacare …» = «… ဆိုင်သော စိတ်၊ … စိတ်တို့၌»", None, ("4-",), F1_P.pattern,
     ("f", f1), 21),
    ("F2 B1 lobha list: 1st rūpataṇhā = fine-material existence, 2nd = visible form", None, ("4-",),
     r"rūpataṇhā arūpataṇhā nirodhataṇhā rūpataṇhā saddataṇhā",
     ("s", f"ရုပ်ကို {_TAN}၊ ရုပ်မရှိသော ဘဝကို {_TAN}၊ ချုပ်ငြိမ်းခြင်းကို {_TAN}၊ ရုပ်ကို {_TAN}၊ အသံကို {_TAN}",
      f"သိမ်မွေ့သော ရုပ်ဘဝကို {_TAN}၊ ရုပ်မရှိသော ဘဝကို {_TAN}၊ ချုပ်ငြိမ်းခြင်းကို {_TAN}၊ "
      f"အဆင်းအရောင်ကို {_TAN}၊ အသံကို {_TAN}"), 3),
    ("F3 B2 ^1-1387 «… kiriyato ca pañca» = «… ငါးပါး» (no added «စီ»; the Pāli as written)", ["1-1387"], None,
     r"kāmāvacarakusalassa vipākato ca kiriyato ca pañca,",
     ("s", "ပြုရုံမျှသာ ဖြစ်သော စိတ်အနက်လည်းကောင်း ငါးပါးစီ၊", "ပြုရုံမျှသာ ဖြစ်သော စိတ်အနက်လည်းကောင်း ငါးပါး၊"), 1),
]


def segs(lines):
    """[(id, [line indexes])] in file order."""
    out, buf = [], []
    for k, l in enumerate(lines):
        if not l.strip():
            continue
        buf.append(k)
        m = ID.search(l)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return out


def main():
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: (PALI / f).read_text(encoding="utf-8").split("\n") for f in files}
    text = {f: (OUT / f).read_text(encoding="utf-8").split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    log, errors, counts = [], [], {}
    for rule, ids, chs, trig, change, expect in RULES:
        trig_re = re.compile(trig)
        done = 0
        for f in files:
            if chs and not f.startswith(chs):
                continue
            for i, pidx in pseg[f]:
                if ids is not None and i not in ids:
                    continue
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    p, m = pali[f][pk], text[f][mk]
                    if not trig_re.search(p):
                        continue
                    try:
                        if change[0] == "s":
                            n = m.count(change[1])
                            ch = [(change[1], change[2])] * n
                            m = m.replace(change[1], change[2])
                        else:
                            m, ch = change[1](p, m)
                    except ValueError as e:
                        errors.append(f"{rule}: {f[:-3]} {i} line {mk + 1}: {e}")
                        continue
                    if ch:
                        text[f][mk] = m
                        done += len(ch)
                        log += [(f[:-3], i, str(mk + 1), o, n_, rule) for o, n_ in ch]
        counts[rule] = done
        if done != expect:
            errors.append(f"{rule}: {done} replacements, expected {expect}")
    for rule, n in counts.items():
        print(f"{n:6d}  {rule}")
    if errors:
        print("\n".join(errors[:60]))
        print(f"{len(errors)} errors")
        sys.exit(1)
    for f in files:
        (OUT / f).write_text("\n".join(text[f]), encoding="utf-8")
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write("ch\tid\tline\told\tnew\trule\n")
        for row in log:
            fh.write("\t".join(row) + "\n")
    print(f"{len(RULES)} rules; {len(log)} replacements; {len({(r[0], r[2]) for r in log})} lines changed")


main()
