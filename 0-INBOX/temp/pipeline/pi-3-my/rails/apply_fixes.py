"""pi-3 Burmese rails: the bilingual-review fixes (review/report-A.md, review/report-B.md; decisions in
review/fix-brief.md, results and the KEEP items in review/fix-notes.md). Model: pi-2-my/rails/apply_fixes.py.
Neither fix changes a repeated formula (one verse line in two chapters; one keyword in two lists), so the rails layer
(my_formulas_rails.py) stays empty and both are explicit rules here.

usage: python3 -I -X utf8 apply_fixes.py
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Reads and rewrites AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters.

Every fix is an explicit rule, applied line by line (Pāli and Burmese lines are aligned inside each segment):
  - scope: a list of segment IDs;
  - trigger: a regex the aligned Pāli line must match, else the line is not touched;
  - change: a list of exact Burmese old → new pairs;
  - expected replacement count over the whole book: the run fails (and writes nothing) if the count differs.
Book-wide checks (main): F2's count = every «nāmarūpena» of the Pāli (found by script, not by the ID list), and no
Burmese line keeps the old form; F1 keeps each line's «[» / «…» / «–» counts.
Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule); line = line number in the chapter file.
Deterministic: no randomness, files and rules in fixed order.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

_END_OLD = "၊ ဤခွဲနည်းကို ကောင်းစွာ နားလည်အပ်သည်။"
_END_NEW = "နှင့်တကွ ဤခွဲနည်းကို ကောင်းစွာ နားလည်ပြီး ဖြစ်သည်။"
_VAR = " [ပါဌ်ကွဲ (Syā.): dvevīsati]"
_NR_OLD = "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းနှင့်"
_NR_NEW = "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့်"

# (rule, segment ids, Pāli trigger regex, [(old, new)], expected)
RULES = [
    ("F1 A3+B3 summary verse «… visayo esanayo subuddho» (^3-227, ^3-455): «အပိုင်းအခြား» joined to the method, subuddho "
     "= «ကောင်းစွာ နားလည်ပြီး ဖြစ်သည်» (termbase buddho|0 «နားလည်ပြီးသော», changed 2026-11-19); at ^3-227 the variant "
     "bracket stays right after its word",
     ["3-227", "3-455"], r"\bvisayo (?:\[dvevīsati \(syā\.\)\] )?esanayo subuddho",
     [("နှစ်ပါး၊ အပိုင်းအခြား" + _VAR + _END_OLD, "နှစ်ပါး၊ အပိုင်းအခြား" + _VAR + _END_NEW),
      ("နှစ်ပါး၊ အပိုင်းအခြား" + _END_OLD, "နှစ်ပါး၊ အပိုင်းအခြား" + _END_NEW)], 2),
    ("F2 A4 nāmarūpena (item) = «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းတို့နှင့်» (the pair as one item; termbase nāmarūpa "
     "«စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း» kept)",
     ["3-202", "3-449"], r"\bnāmarūpena\b", [(_NR_OLD, _NR_NEW)], 2),
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


def marks(s):
    return s.count("["), s.count("…"), s.count("–")


def main():
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: (PALI / f).read_text(encoding="utf-8").split("\n") for f in files}
    text = {f: (OUT / f).read_text(encoding="utf-8").split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    log, errors, counts = [], [], {}
    for rule, ids, trig, pairs, expect in RULES:
        trig_re = re.compile(trig)
        done, found = 0, set()
        for f in files:
            for i, pidx in pseg[f]:
                if i not in ids:
                    continue
                found.add(i)
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule[:12]}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    np_ = len(trig_re.findall(pali[f][pk]))
                    if not np_:
                        continue
                    before, got = text[f][mk], 0
                    for old, new in pairs:
                        n = text[f][mk].count(old)
                        if n:
                            text[f][mk] = text[f][mk].replace(old, new)
                            got += n
                            log += [(f[:-3], i, str(mk + 1), old, new, rule)] * n
                    if got != np_:
                        errors.append(f"{rule[:12]}: {f[:-3]} {i} line {mk + 1}: {got} replacements, Pāli {np_}")
                    if marks(before) != marks(text[f][mk]):
                        errors.append(f"{rule[:12]}: {f[:-3]} {i} line {mk + 1}: «[» / «…» / «–» counts changed")
                    done += got
        if found != set(ids):
            errors.append(f"{rule[:12]}: segments not found: {sorted(set(ids) - found)}")
        counts[rule] = done
        if done != expect:
            errors.append(f"{rule[:12]}: {done} replacements, expected {expect}")
    # F2 found by script: every Pāli «nāmarūpena» is in the rule's scope, and no Burmese line keeps the old form
    n_pali = sum(len(re.findall(r"\bnāmarūpena\b", l)) for f in files for l in pali[f])
    if n_pali != counts[RULES[1][0]]:
        errors.append(f"F2: Pāli has {n_pali} «nāmarūpena», {counts[RULES[1][0]]} replaced")
    left = [f"{f[:-3]}:{k + 1}" for f in files for k, l in enumerate(text[f]) if "ရုပ်ပိုင်းနှင့်" in l]
    if left:
        errors.append(f"F2: «ရုပ်ပိုင်းနှင့်» left on {left}")
    left = [f"{f[:-3]}:{k + 1}" for f in files for k, l in enumerate(text[f]) if "နားလည်အပ်" in l]
    if left:
        errors.append(f"F1: «နားလည်အပ်» left on {left}")
    for rule, n in counts.items():
        print(f"{n:6d}  {rule[:110]}")
    if errors:
        print("\n".join(errors))
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
