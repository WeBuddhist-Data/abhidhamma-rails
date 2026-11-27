"""pi-2 rails: every repeated Pāli sentence that align_check_my.py reports with differing Burmese in the RAILS text must
be one of the zero-shot's accepted context differences (pi-2-my/harmonise_align_kept.py, read only: TOPIC = the ch1
approved-sample topic noun, KEPT = the two listed sentences), and the set of differing sentences must be the zero-shot's
(the rails introduce none).
usage: python3 -I -X utf8 align_kept.py   (exit 1 if an unexplained difference is left)"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE.parent))
import harmonise_align_diff as D  # noqa: E402
import harmonise_align_kept as K  # noqa: E402

RL = ROOT / "AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters"
bad_r, bad_z = D.groups(md=RL), D.groups()
topic = kept = 0
left = []
for s, v in bad_r.items():
    vs = list(v)
    diffs = [d for t in vs[1:] for d in K.words(vs[0], t)]
    if diffs and all(x in K.TOPIC and y in K.TOPIC for x, y in diffs):
        topic += 1
    elif s in K.KEPT:
        kept += 1
    else:
        left.append(s)
new = sorted(set(bad_r) - set(bad_z))
print(f"rails align differences: {len(bad_r)} (zero-shot {len(bad_z)}) = topic noun (ch1, no subject in the Pāli): "
      f"{topic}, kept (context): {kept}, unexplained: {len(left)}; new in the rails: {len(new)}")
for s in left + new:
    print("  LEFT:", s[:140])
sys.exit(1 if left or new else 0)
