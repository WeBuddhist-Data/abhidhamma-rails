"""read-only helper (g1): segments of chapter CH holding any of the keywords KW…: sid, keywords, Pāli, Burmese (cut to W chars)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
ch = sys.argv[1]; kws = sys.argv[2:]
W = 900
for sid, ks in R.keyword_rows(ch):
    if any(k in ks for k in kws):
        print(f"== ^{sid} KW: {', '.join(ks)}\n PA: {R.pali(ch).get(sid,'')[:W]}\n MY: {R.burmese(ch)[sid][:W]}\n")
