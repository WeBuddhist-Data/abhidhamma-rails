"""pi-4 Burmese rails, residual single cases: explicit rules applied to the chapters build_rails.py has just written.
Model: pi-3-my/rails/apply_termbase.py, pi-2-my/rails/apply_termbase.py (read only).

usage: python3 -I -X utf8 apply_termbase.py   (run right after build_rails.py; regen_rails.sh does both)
A rule fires only in the segment IDs it names, and only when that segment's Pāli holds the rule's keyword regex; each
rule states how many replacements it must make over all its segments, else the run fails and nothing is written.
Every replacement is logged in rails/apply-log.tsv (ch, id, old, new, rule). The zero-shot files are never touched.
pi-4 result: no residual single case: every GENUINE difference and every logged text inconsistency that the locked
termbase decides is a source patch of the layer (my_formulas_rails.py L01 … L25, see notes-rails.md), so RULES is empty.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters"
LOG = HERE / "apply-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
# (rule, Pāli keyword regex, segment ids, old, new, replacements expected over all ids)
RULES = []


def seg_ranges(lines):
    """id -> (first line index, last line index) of its segment."""
    out, start = {}, None
    for k, l in enumerate(lines):
        if not l.strip():
            continue
        if start is None:
            start = k
        m = ID.search(l)
        if m:
            out[m.group(1)] = (start, k)
            start = None
    return out


def main():
    where, pali_seg = {}, {}
    for p in sorted(PALI.glob("*.md")):
        pl = p.read_text(encoding="utf-8-sig").splitlines()
        for i, (a, b) in seg_ranges(pl).items():
            where[i] = p.name
            pali_seg[i] = " ".join(pl[a:b + 1])
    texts = {p.name: p.read_text(encoding="utf-8").split("\n") for p in sorted(OUT.glob("*.md"))}
    log, errors, touched = [], [], set()
    for rule, kw, ids, old, new, expect in RULES:
        done = 0
        for i in ids:
            ch = where.get(i)
            if ch is None or ch not in texts:
                errors.append(f"{rule}: no segment {i}")
                continue
            if not re.search(kw, pali_seg[i]):
                errors.append(f"{rule}: Pāli of {i} lacks keyword {kw}")
                continue
            lines = texts[ch]
            a, b = seg_ranges(lines)[i]
            for k in range(a, b + 1):
                n = lines[k].count(old)
                if n:
                    lines[k] = lines[k].replace(old, new)
                    done += n
                    touched.add(ch)
                    log += [(ch[:-3], i, old, new, rule)] * n
        if done != expect:
            errors.append(f"{rule}: {done} replacements, expected {expect}")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    for name in sorted(touched):
        (OUT / name).write_text("\n".join(texts[name]), encoding="utf-8")
    with open(LOG, "w", encoding="utf-8") as f:
        f.write("ch\tid\told\tnew\trule\n")
        for row in log:
            f.write("\t".join(row) + "\n")
    print(f"{len(RULES)} rule entries; {len(log)} replacements")


main()
