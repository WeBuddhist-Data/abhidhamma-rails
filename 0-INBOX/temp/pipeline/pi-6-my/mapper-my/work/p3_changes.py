"""phase 3: phase3-changes.tsv = every value of the 44 *.mapped.md that differs from the phase-2 files
(work/phase2-mapped, md5 = work/before-phase3-files-md5.txt), with the stage that changed it and its reason."""
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import p3_stage as S

REASON = {
    ("s5-endings", "uppannaṃ"): "M5: mechanic 5 (g2 U4 decided): the verifier ending «Xပြီး မဟုတ်» (perf-neg, presence and "
    "phrase_present) lets the dictionary perfect participle «ဖြစ်ပေါ်ပြီးသော» stand against the text's negated "
    "predicate «… ဖြစ်ပေါ်ပြီး မဟုတ်»; uppannaṃ is «ဖြစ်ပေါ်ပြီးသော» in every segment (was the bare «ဖြစ်ပေါ်ပြီး»)",
    ("s5-endings", "sacchikarittha"): "U4: g3 U4 decided: the verifier ending «neg-verb-sp» (a joined compound verb "
    "against its spaced negative «မျက်မှောက် မပြုခဲ့၊») lets sacchikar- take the joined «မျက်မှောက်ပြု…» everywhere; "
    "g3 W6 (f_sacchi) dropped; the spacing itself is rails item (§A)",
    ("s6b-book", "saraṇaaraṇā"): "U3: g2 U3 decided: «အတွဲ» only where the Pāli keyword itself names the pair (-duka); "
    "saraṇaaraṇā is the two members «ပဋိပက္ခ ရှိသော ပဋိပက္ခ မရှိသော» (the translator's «အတွဲ» goes)",
}
REASON[("s5-endings", "sacchikaritthāti")] = REASON[("s5-endings", "sacchikarittha")]

order = (S.ST / "order.txt").read_text().split()
final = S.read(S.stage_dir(order[-1]))
base = S.read(S.stage_dir("phase2"))
who = {}
for a, b in zip(order, order[1:]):
    for sid, i, k, o, n in S.diff(S.read(S.stage_dir(a)), S.read(S.stage_dir(b))):
        who.setdefault((sid, i), []).append(b)
rows, missing = [], []
for sid, i, k, o, n in S.diff(base, final):
    st = who.get((sid, i), ["?"])
    r = "; ".join(REASON.get((x, k), "?") for x in dict.fromkeys(st))
    if "?" in r:
        missing.append((sid, k, o, n, st))
    rows.append((sid, k, o, n, r))
out = pathlib.Path(__file__).resolve().parent.parent / "phase3-changes.tsv"
out.write_text("segment\tkeyword\told\tnew\treason\n" + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
print("changes", len(rows), "unexplained", len(missing))
for m in missing:
    print("  ?", m)
