#!/bin/zsh
# pi-1 Burmese zero-shot (Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»): rebuild every chapter from its generator,
# then run every check.   usage: zsh 0-INBOX/temp/pipeline/pi-1-my/regen_zeroshot.sh   (from anywhere)
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-1_split_chapters
MY=AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
setopt pipefail

echo "== rebuild"
# my-zeroshot-terms.md: make_sample.py --terms writes it (without the 2-01 section), make_ch2-01.py re-completes it
py $D/make_sample.py --terms > /dev/null || { echo "FAILED: make_sample"; fail=1; }
for g in make_ch2-01 make_ch2-02-03 make_ch2-04-05 make_ch3 make_ch4 make_ch5; do
  out=$(py $D/$g.py 2>&1) || { echo "FAILED: $g"; print -r -- "$out" | tail -5; fail=1; }
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
rm -f 0-INBOX/temp/pipeline/pi-6-mr/chk-pe/{preamble,1-matika,2-0?-cittuppadakandam,3-0?-rupakandam,4-0?-nikkhepakandam,5-atthakathakandam}.md(N)
echo "($(ls $PI/*.md | wc -l | tr -d ' ') chapter files checked)"

echo "== no «?», no Zawgyi-range code points"
py $D/harmonise_typo.py $MY || fail=1

echo "== agents' own checks"
pairs() { for n in "$@"; do print -r -- $PI/$n $MY/$n; done; }
run_chk() {
  local c=$1; shift
  local out; out=$(py $D/$c.py ${=$(pairs "$@")} 2>&1); local rc=$?
  print -r -- "$out" | grep -E "OK|mismatch|MISMATCH|Error|error" | sed "s|^.*/||" | head -20
  [[ $rc == 0 ]] || { echo "  -> $c exit $rc"; fail=1; }
}
run_chk check_sample preamble.md 1-matika.md
run_chk check_ch2-01 2-01-cittuppadakandam.md
run_chk check_ch2-02-03 2-02-cittuppadakandam.md 2-03-cittuppadakandam.md
run_chk check_ch2-04-05 2-04-cittuppadakandam.md 2-05-cittuppadakandam.md
run_chk check_ch3 3-01-rupakandam.md 3-02-rupakandam.md 3-03-rupakandam.md
run_chk check_ch4 4-01-nikkhepakandam.md 4-02-nikkhepakandam.md 4-03-nikkhepakandam.md
run_chk check_ch5 5-atthakathakandam.md

echo "== cross-chapter alignment (Burmese copies of pi-4-mr/align_check.py and pi-4-mr/rails/align_hidden.py)"
py $D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
grep -q "with differing Burmese: 0;" $D/align-after.txt || { [[ -f $D/align-kept.txt ]] && py $D/align_kept.py $D/align-after.txt $D/align-kept.txt; } || fail=1
grep -q "unmatched repeated sentences: 0" $D/align-hidden-after.txt || fail=1

echo "== harmonise scan (one form per item)"
[[ -f $D/harmonise_scan.py ]] && { py $D/harmonise_scan.py --table | grep -v "^OK " ; [[ ${pipestatus[1]} == 0 ]] || fail=1; }

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
