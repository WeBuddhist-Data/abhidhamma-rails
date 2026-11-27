#!/bin/zsh
# pi-2 Burmese zero-shot (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»): rebuild every chapter from its generator, then run every check.
# usage: zsh 0-INBOX/temp/pipeline/pi-2-my/regen_zeroshot.sh   (from anywhere)
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-2_split_chapters
MY=AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-2-my
P1D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
setopt pipefail

echo "== rebuild (the generators; the consistency-pass values are in my2_formulas.py, block «consistency pass»)"
py $D/make_sample.py --terms > /dev/null || { echo "FAILED: make_sample"; fail=1; }
for g in make_ch2-4 make_ch5-7-11 make_ch6 make_ch12-14 make_ch15-16 make_ch17 make_ch18; do
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
echo "($(ls $PI/*.md | wc -l | tr -d ' ') chapter files checked)"

echo "== agents' own checks"
pairs() { for n in "$@"; do print -r -- $PI/$n $MY/$n; done; }
run_chk() {                       # run_chk <check> <args...> : prints the OK / mismatch / reuse lines
  local c=$1; shift
  local out; out=$(py $D/$c.py "$@" 2>&1); local rc=$?
  print -r -- "$out" | grep -E "OK|mismatch|MISMATCH|Error|error|reuse|identical" | sed -E "s|[^ ]*/([^/ ]+\.md)|\1|g" | head -12
  [[ $rc == 0 ]] || { echo "  -> $c exit $rc"; fail=1; }
}
run_chk check_sample ${=$(pairs preamble.md 1-khandhavibhango.md)}
run_chk check_ch2-4 ${=$(pairs 2-ayatanavibhango.md 3-dhatuvibhango.md 4-saccavibhango.md)}
run_chk check_ch5-7-11
run_chk check_ch6 ${=$(pairs 6-paticcasamuppadavibhango.md)}
run_chk check_ch12-14 ${=$(pairs 12-jhanavibhango.md 13-appamannavibhango.md 14-sikkhapadavibhango.md)}
run_chk check_ch15-16 ${=$(pairs 15-patisambhidavibhango.md 16-nanavibhango.md)}
run_chk check_ch17 ${=$(pairs 17-khuddakavatthuvibhango.md)}
run_chk check_ch18 ${=$(pairs 18-dhammahadayavibhango.md)}

echo "== cross-chapter alignment (pi-1-my/align_check_my.py, align_hidden_my.py)"
py $P1D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $P1D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
if ! grep -q "with differing Burmese: 0;" $D/align-after.txt; then
  if [[ -f $D/harmonise_align_kept.py ]]; then py $D/harmonise_align_kept.py || fail=1; else fail=1; fi
fi
grep -q "unmatched repeated sentences: 0" $D/align-hidden-after.txt || fail=1

echo "== pi-1 identity (harmonise_pi1.py)"
py $D/harmonise_pi1.py > $D/scratch/pi1.txt || fail=1; head -1 $D/scratch/pi1.txt

echo "== harmonise scans (one form per item)"
py $D/harmonise_lists.py > $D/scratch/lists.txt; r=$?; head -1 $D/scratch/lists.txt; [[ $r == 0 ]] || fail=1
sc=$(py $D/harmonise_scan.py --table 2>&1) || fail=1
print -r -- "$sc" | grep -v "^OK " | head -40
py $D/harmonise_diff.py | tail -1

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
