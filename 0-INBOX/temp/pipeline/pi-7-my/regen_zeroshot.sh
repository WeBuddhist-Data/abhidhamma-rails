#!/bin/zsh
# pi-7 Burmese zero-shot (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»): rebuild every chapter from its generator in
# dependency order, then run every check.   usage: zsh 0-INBOX/temp/pipeline/pi-7-my/regen_zeroshot.sh [--quick]
# (--quick: skip the --mutate and --regress runs.)  The generators are slow: run it in the background.
# The book-wide values of the consistency pass are in my7_formulas.py and the generators (comments «harmonise H…»);
# log: harmonise-notes.md.
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-7_split_chapters
MY=AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-7-my
P1D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
quick=0; [[ "$1" == "--quick" ]] && quick=1
setopt pipefail

# Import chain (each generator loads the ones on its right in memory; their main blocks never run):
#   make_sample <- my7_formulas
#   1-01 <- sample            1-03-05 <- sample          2-01-02 <- 1-03-05       2-03-06 <- 1-01, 1-03-05
#   2-07-11 <- 2-01-02        2-12-17 <- 2-03-06         3-01-02 <- 2-03-06       3-03-06 <- 3-01-02
#   3-07-08-10 <- 3-01-02     3-09 <- 3-03-06            4-01 <- 3-07-08-10
#   4-02-09 <- 2-07-11, 2-12-17, 3-03-06, 3-07-08-10     4-10-14 <- 3-09, 4-01, 4-02-09    4-15-21 <- 4-10-14
#   5-01-04 <- 2-07-11, 2-12-17, 3-09, 4-01              5-05-12 <- 5-01-04                5-13-20 <- 5-01-04
GENS=(make_sample make_ch1-01 make_ch1-03-05 make_ch2-01-02 make_ch2-03-06 make_ch2-07-11 make_ch2-12-17
      make_ch3-01-02 make_ch3-03-06 make_ch3-07-08-10 make_ch3-09 make_ch4-01 make_ch4-02-09 make_ch4-10-14
      make_ch4-15-21 make_ch5-01-04 make_ch5-05-12 make_ch5-13-20)

echo "== preamble (written by the coordinator: a fixed table)"
py - $MY/preamble.md <<'EOF'
import sys, pathlib
LINES = [
    "ထိုမြတ်စွာဘုရား၊ ရဟန္တာ၊ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်အား ရှိခိုးပါ၏ ^T-1",
    "",
    "# အဘိဓမ္မာပိဋကတွင် ^0",
    "",
    "## အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ ^7-0",
]
pathlib.Path(sys.argv[1]).write_text("\n".join(LINES) + "\n", encoding="utf-8")
EOF

echo "== rebuild (18 generators in dependency order; make_sample.py --terms rewrites my7-zeroshot-terms.md)"
for g in $GENS; do
  t0=$SECONDS
  out=$(py $D/$g.py 2>&1); rc=$?
  if [[ $rc != 0 ]] || print -r -- "$out" | grep -q "MISS\|Miss\|STOP\|unmatched\|bad lines\|Traceback"; then
    echo "FAILED: $g"; print -r -- "$out" | tail -8; fail=1
  else
    echo "  $g: $(print -r -- "$out" | grep -c '^wrote') files ($((SECONDS - t0)) s)"
  fi
done
out=$(py $D/make_sample.py --terms 2>&1) || { echo "FAILED: make_sample --terms"; print -r -- "$out" | tail -5; fail=1; }

if [[ $quick == 0 ]]; then
  echo "== --regress (the upstream outputs regenerate identical in memory)"
  for g in make_ch1-01 make_ch2-03-06 make_ch2-12-17 make_ch3-01-02 make_ch3-03-06 make_ch3-07-08-10 make_ch3-09 make_ch4-01; do
    out=$(py $D/$g.py --regress 2>&1); rc=$?
    print -r -- "  $g --regress: $(print -r -- "$out" | grep -v '^ *$' | tail -1 | cut -c1-150)"
    [[ $rc == 0 ]] || { print -r -- "$out" | tail -12; fail=1; }
  done
fi

echo "== check_chapter_ids / pi-7-my/check_text_pe7.py / pi-4-mr/check_marks.py"
n=0
for f in $PI/*.md; do
  b=${f:t}; n=$((n+1))
  r1=$(py 0-INBOX/temp/pipeline/check_chapter_ids.py $PI $MY $b 2>&1)
  r2=$(py $D/check_text_pe7.py $PI/$b $MY/$b 2>&1)
  r3=$(py 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py $PI/$b $MY/$b 2>&1)
  for r in "$r1" "$r2" "$r3"; do
    if ! print -r -- "$r" | tail -1 | grep -q "OK"; then echo "$b: $r" | head -20; fail=1; fi
  done
done
echo "($n chapter files checked; check_text_pe7 deletes its chk-pe/ copies)"

echo "== agents' own checks (0 mismatches, reuse n / n, mutation)"
CHECKS=(check_sample check_ch1-01 check_ch1-03-05 check_ch2-01-02 check_ch2-03-06 check_ch2-07-11 check_ch2-12-17
        check_ch3-01-02 check_ch3-03-06 check_ch3-07-08-10 check_ch3-09 check_ch4-01 check_ch4-02-09 check_ch4-10-14
        check_ch4-15-21 check_ch5-01-04 check_ch5-05-12 check_ch5-13-20)
for c in $CHECKS; do
  out=$(py $D/$c.py 2>&1); rc=$?
  print -r -- "$c: $(print -r -- "$out" | grep -iE "reuse" | tail -1 | cut -c1-110) | $(print -r -- "$out" | grep -i "mismatch" | tail -1 | cut -c1-90)"
  [[ $rc == 0 ]] || { print -r -- "$out" | grep -v "^ *$" | tail -30; fail=1; }
  if [[ $quick == 0 && $c != check_sample ]]; then
    out=$(py $D/$c.py --mutate 2>&1); rc=$?
    print -r -- "   --mutate: $(print -r -- "$out" | grep -v '^ *$' | tail -1 | cut -c1-120)"
    [[ $rc == 0 ]] || { print -r -- "$out" | tail -12; fail=1; }
  fi
done
if [[ $quick == 0 ]]; then
  for c in check_ch4-10-14 check_ch4-15-21; do
    out=$(py $D/$c.py --regress 2>&1); rc=$?
    print -r -- "  $c --regress: $(print -r -- "$out" | grep -v '^ *$' | tail -1 | cut -c1-150)"
    [[ $rc == 0 ]] || { print -r -- "$out" | tail -12; fail=1; }
  done
fi

echo "== cross-chapter alignment (pi-1-my/align_check_my.py, align_hidden_my.py)"
py $P1D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $P1D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
[[ -f $D/harmonise_align_explained.py ]] && { py $D/harmonise_align_explained.py || fail=1; }

echo "== pi-1 … pi-6 identity (harmonise_pi123456.py)"
if [[ -f $D/harmonise_pi123456.py ]]; then
  py $D/harmonise_pi123456.py > $D/pi123456.txt || fail=1; grep "identity" $D/pi123456.txt
fi

echo "== harmonise scan (one form per item; writes harmonise-table.tsv) and lines changed"
if [[ -f $D/harmonise_scan.py ]]; then
  sc=$(py $D/harmonise_scan.py --table 2>&1) || fail=1
  print -r -- "$sc" | grep -v "^OK " | grep -v "items OK$" | head -40
  print -r -- "$sc" | tail -1
fi
[[ -f $D/harmonise_diff.py ]] && py $D/harmonise_diff.py | tail -1 | cut -c1-2000

echo "== merged file (book order = the pi-7 Pāli folder: preamble, then the chapters in number order)"
py - $PI $MY AI_translation/burmese/pi-7-burmese-plain-zeroshot.md <<'EOF' || fail=1
import sys, pathlib, re
pi, my, out = map(pathlib.Path, sys.argv[1:4])
names = [p.name for p in pi.glob("*.md")]
key = lambda n: (0,) if n == "preamble.md" else (1,) + tuple(int(x) for x in re.findall(r"\d+", n))
order = sorted(names, key=key)
texts = [(my / n).read_text(encoding="utf-8") for n in order]
merged = "\n".join(texts)
out.write_text(merged, encoding="utf-8")
seg = lambda t: len(re.findall(r" \^[0-9A-Za-z-]+\s*$", t, flags=re.M))
s = sum(seg(t) for t in texts)
m = seg(out.read_text(encoding="utf-8"))
print(f"merged {len(order)} files: {m} segments (sum over the chapters {s}) {'OK' if m == s else 'MISMATCH'}")
sys.exit(0 if m == s else 1)
EOF

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
