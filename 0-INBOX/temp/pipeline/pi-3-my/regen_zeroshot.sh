#!/bin/zsh
# pi-3 Burmese zero-shot (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»): rebuild every chapter from its generator, then run
# every check.   usage: zsh 0-INBOX/temp/pipeline/pi-3-my/regen_zeroshot.sh   (from anywhere)
# The book-wide values of the consistency pass are in my3_formulas.py (block «consistency pass», install()).
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-3_split_chapters
MY=AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-3-my
P1D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
setopt pipefail

echo "== rebuild (make_sample --terms also rewrites my3-zeroshot-terms.md)"
py $D/make_sample.py --terms > /dev/null || { echo "FAILED: make_sample"; fail=1; }
for g in make_ch3-6-8-9 make_ch7-10-11 make_ch12-15; do
  out=$(py $D/$g.py 2>&1) || { echo "FAILED: $g"; print -r -- "$out" | tail -5; fail=1; }
  if print -r -- "$out" | grep -q "^STOP"; then echo "STOPPED (lines missed): $g"; print -r -- "$out" | grep -A3 "^STOP"; fail=1; fi
done

echo "== check_chapter_ids / pi-6-mr/check_text_pe.py / pi-4-mr/check_marks.py"
for f in $PI/*.md; do
  n=${f:t}
  r1=$(py 0-INBOX/temp/pipeline/check_chapter_ids.py $PI $MY $n 2>&1)
  r2=$(py 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py $PI/$n $MY/$n 2>&1)
  r3=$(py 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py $PI/$n $MY/$n 2>&1)
  for r in "$r1" "$r2" "$r3"; do
    if ! print -r -- "$r" | grep -q "OK"; then echo "$n: $r"; fail=1; fi
  done
done
for f in $PI/*.md; do rm -f 0-INBOX/temp/pipeline/pi-6-mr/chk-pe/${f:t}(N); done
echo "($(ls $PI/*.md | wc -l | tr -d ' ') chapter files checked, chk-pe copies deleted)"

echo "== agents' own checks (0 mismatches, reuse n / n)"
for c in check_sample check_ch3-6-8-9 check_ch7-10-11 check_ch12-15; do
  out=$(py $D/$c.py 2>&1); rc=$?
  print -r -- "$c: $(print -r -- "$out" | tail -1)"
  [[ $rc == 0 ]] || { print -r -- "$out" | grep -A20 "MISMATCHES" | head -20; fail=1; }
done

echo "== cross-chapter alignment (pi-1-my/align_check_my.py, align_hidden_my.py)"
py $P1D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $P1D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
if ! grep -q "with differing Burmese: 0;" $D/align-after.txt; then
  py $D/harmonise_align_kept.py | tail -1 || fail=1
fi
grep -q "unmatched repeated sentences: 0" $D/align-hidden-after.txt || fail=1

echo "== pi-1 / pi-2 identity (harmonise_pi12.py)"
py $D/harmonise_pi12.py > $D/scratch/pi12.txt || fail=1; grep "identity" $D/scratch/pi12.txt

echo "== harmonise scan (one form per item) and lines changed"
sc=$(py $D/harmonise_scan.py --table 2>&1) || fail=1
print -r -- "$sc" | grep -v "^OK " | head -40
py $D/harmonise_diff.py | tail -1

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
