#!/bin/zsh
# pi-6 Burmese zero-shot (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»): rebuild every chapter from its generator, then run every
# check.   usage: zsh 0-INBOX/temp/pipeline/pi-6-my/regen_zeroshot.sh   (from anywhere)
# The book-wide values of the consistency pass are in my6_formulas.py (blocks marked «harmonise») and in the generators
# (comments «harmonise A… / B…»); log: harmonise-notes.md.
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-6_split_chapters
MY=AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-6-my
P1D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
setopt pipefail

echo "== rebuild (9 generators; make_sample.py --terms rewrites my6-zeroshot-terms.md)"
for g in make_sample make_ch2-02-4-5 make_ch3 make_ch6-8 make_ch7a make_ch7b make_ch9-10a make_ch10b make_ch10c; do
  out=$(py $D/$g.py 2>&1); rc=$?
  if [[ $rc != 0 ]] || print -r -- "$out" | grep -q "MISS\|Miss\|STOP\|bad lines\|Traceback"; then
    echo "FAILED: $g"; print -r -- "$out" | tail -8; fail=1
  fi
done
out=$(py $D/make_sample.py --terms 2>&1) || { echo "FAILED: make_sample --terms"; print -r -- "$out" | tail -5; fail=1; }

echo "== check_chapter_ids / pi-6-mr/check_text_pe.py / pi-4-mr/check_marks.py"
n=0
for f in $PI/*.md; do
  b=${f:t}; n=$((n+1))
  r1=$(py 0-INBOX/temp/pipeline/check_chapter_ids.py $PI $MY $b 2>&1)
  r2=$(py 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py $PI/$b $MY/$b 2>&1)
  r3=$(py 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py $PI/$b $MY/$b 2>&1)
  for r in "$r1" "$r2" "$r3"; do
    if ! print -r -- "$r" | tail -1 | grep -q "OK"; then echo "$b: $r"; fail=1; fi
  done
done
for f in $PI/*.md; do rm -f 0-INBOX/temp/pipeline/pi-6-mr/chk-pe/${f:t}(N); done
echo "($n chapter files checked, chk-pe copies deleted)"

echo "== agents' own checks (0 mismatches, reuse n / n)"
for c in check_sample check_ch2-02-4-5 check_ch3 check_ch6-8 check_ch7a check_ch7b check_ch9-10a check_ch10b check_ch10c; do
  out=$(py $D/$c.py 2>&1); rc=$?
  print -r -- "$c: $(print -r -- "$out" | grep -E "reuse test|^reuse " | tail -1 | cut -c1-110) | $(print -r -- "$out" | grep -i "mismatches" | tail -1)"
  [[ $rc == 0 ]] || { print -r -- "$out" | grep -v "^ *$" | tail -30; fail=1; }
done

echo "== cross-chapter alignment (pi-1-my/align_check_my.py, align_hidden_my.py)"
py $P1D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $P1D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
[[ -f $D/harmonise_align_explained.py ]] && { py $D/harmonise_align_explained.py || fail=1; }

echo "== pi-1 … pi-5 identity (harmonise_pi12345.py)"
mkdir -p $D/scratch
if [[ -f $D/harmonise_pi12345.py ]]; then
  py $D/harmonise_pi12345.py > $D/scratch/pi12345.txt || fail=1; grep "identity" $D/scratch/pi12345.txt
fi

echo "== harmonise scan (one form per item; writes harmonise-table.tsv) and lines changed"
if [[ -f $D/harmonise_scan.py ]]; then
  sc=$(py $D/harmonise_scan.py --table 2>&1) || fail=1
  print -r -- "$sc" | grep -v "^OK " | head -40
fi
[[ -f $D/harmonise_diff.py ]] && py $D/harmonise_diff.py | tail -1

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
