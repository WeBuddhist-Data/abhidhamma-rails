#!/bin/zsh
# pi-4 Burmese zero-shot (Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»): rebuild every chapter from its generator,
# then run every check.   usage: zsh 0-INBOX/temp/pipeline/pi-4-my/regen_zeroshot.sh   (from anywhere)
# The book-wide values of the consistency pass are in my4_formulas.py (block «consistency pass (harmonise)»).
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-4_split_chapters
MY=AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-4-my
P1D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
setopt pipefail

echo "== rebuild (make_sample --terms also rewrites my4-zeroshot-terms.md)"
for g in make_sample make_ch3-4 make_ch5 make_ch6-11; do
  if [[ $g == make_sample ]]; then out=$(py $D/$g.py --terms 2>&1); rc=$?; else out=$(py $D/$g.py 2>&1); rc=$?; fi
  if [[ $rc != 0 ]] || print -r -- "$out" | grep -q "^Miss\|STOP\|Traceback"; then
    echo "FAILED: $g"; print -r -- "$out" | tail -5; fail=1
  fi
done

echo "== check_chapter_ids / pi-6-mr/check_text_pe.py / pi-4-mr/check_marks.py"
for f in $PI/*.md; do
  n=${f:t}
  r1=$(py 0-INBOX/temp/pipeline/check_chapter_ids.py $PI $MY $n 2>&1)
  r2=$(py 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py $PI/$n $MY/$n 2>&1)
  r3=$(py 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py $PI/$n $MY/$n 2>&1)
  for r in "$r1" "$r2" "$r3"; do
    if ! print -r -- "$r" | tail -1 | grep -q "OK"; then echo "$n: $r"; fail=1; fi
  done
done
for f in $PI/*.md; do rm -f 0-INBOX/temp/pipeline/pi-6-mr/chk-pe/${f:t}(N); done
echo "($(ls $PI/*.md | wc -l | tr -d ' ') chapter files checked, chk-pe copies deleted)"

echo "== agents' own checks (0 mismatches, reuse n / n, harmonised forms n / n)"
for c in check_sample check_ch3-4 check_ch5 check_ch6-11; do
  out=$(py $D/$c.py 2>&1); rc=$?
  print -r -- "$c: $(print -r -- "$out" | grep '^H\. ' | sed 's/H. harmonised forms (changed on purpose in the consistency pass): /harmonised /') | $(print -r -- "$out" | tail -1)"
  [[ $rc == 0 ]] || { print -r -- "$out" | grep -A20 "MISMATCHES" | head -20; fail=1; }
done

echo "== cross-chapter alignment (pi-1-my/align_check_my.py, align_hidden_my.py)"
py $P1D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $P1D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
grep -q "with differing Burmese: 0;" $D/align-after.txt || fail=1
grep -q "unmatched repeated sentences: 0" $D/align-hidden-after.txt || fail=1

echo "== pi-1 / pi-2 / pi-3 identity (harmonise_pi123.py)"
mkdir -p $D/scratch
py $D/harmonise_pi123.py > $D/scratch/pi123.txt || fail=1; grep "identity" $D/scratch/pi123.txt

echo "== harmonise scan (one form per item; writes harmonise-table.tsv) and lines changed"
sc=$(py $D/harmonise_scan.py --table 2>&1) || fail=1
print -r -- "$sc" | grep -v "^OK " | head -40
py $D/harmonise_diff.py | tail -1

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
