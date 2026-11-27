"""Consistency pass: explain every repeated Pāli sentence that align_check_my.py still reports with differing Burmese.
A difference is kept only when the Pāli context genuinely differs: the sentence's «-ā» participle (saṅgahitā,
asaṅgahitā, sampayuttā, vippayuttā) agrees with a subject stated earlier in the line, and that subject is a feminine
singular (dhātu, avijjā, vedanā, saññā, …: singular verb, no «ကြ», the sample's rule) in some lines and plural in
others («ကြ»). Checked here: the renderings are identical once «ကြ» is removed, and in every location «ကြ» is
present exactly when the line's subject is not a feminine singular.
usage: python3 -I -X utf8 harmonise_align_kept.py   (exit 1 if a difference is not explained)"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my3_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-3_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPLIT_PI = re.compile(r"(?<=[.?])\s+")
SPLIT_MY = re.compile(r"(?<=[။])\s+")
FSG = re.compile(r"(?:dhātu|avijjā|vedanā|taṇhā|jāti|jarā|appamaññā|saññā|cetanā)$", re.IGNORECASE)
CUT = re.compile(rf"\s(?:{F.COUNTS_RE.pattern}|katihi |asaṅkhataṃ )", re.IGNORECASE)
f = lambda p: [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]  # noqa: E731
seen = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(PD.glob("*.md")):
    for i, (x, y) in enumerate(zip(f(p), f(MD / p.name)), 1):
        xs, ys = SPLIT_PI.split(x.strip()), SPLIT_MY.split(y.strip())
        if len(xs) != len(ys):
            continue
        for s, t in zip(xs, ys):
            if len(s) > 25:
                seen[s][t].append((p.name.split("-")[0].split(".")[0], i, x))
bad = kept = 0
for s, v in seen.items():
    if len(v) < 2:
        continue
    if len({t.replace("ကြ", "") for t in v}) != 1:
        bad += 1
        print("NOT EXPLAINED (differs beyond «ကြ»):", s[:120])
        continue
    for t, locs in v.items():
        for ch, i, line in locs:
            head = CUT.split(line, 1)[0]
            pieces = [z.strip() for z in re.split(r"…pe…|…|(?<=[.?]) ", head)]
            subj = [z for z in pieces if z and not re.search(r"sampayutt|vippayutt|saṅgahit|[Nn]atthi", z)]
            subj = subj[-1] if subj and " ye dhammā" not in line else "te dhammā"     # relative frames: «te dhammā»
            fsg = bool(FSG.search(subj))
            if fsg == ("ကြ" in t):
                bad += 1
                print(f"NOT EXPLAINED {ch}:{i} subject «{subj}» ({'fem. sg' if fsg else 'plural'}) but «{t[-30:]}»")
    kept += 1
    print(f"kept: {s[:90]} — " + "; ".join(
        f"{'plural «ကြ»' if 'ကြ' in t else 'fem. sg subject'} {','.join(f'{c}:{i}' for c, i, _ in l)}"
        for t, l in v.items()))
print(f"differences explained by the subject's number: {kept}; not explained: {bad}")
sys.exit(1 if bad else 0)
