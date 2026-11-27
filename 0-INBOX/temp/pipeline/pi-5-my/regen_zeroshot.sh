#!/bin/zsh
# pi-5 Burmese zero-shot (Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»): rebuild every chapter from its
# generator, then run every check.   usage: zsh 0-INBOX/temp/pipeline/pi-5-my/regen_zeroshot.sh   (from anywhere)
# The book-wide values of the consistency pass are in my5_formulas.py (blocks marked «harmonise») and in the generators
# (comments «harmonise A… / B…»); log: harmonise-notes.md.
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
PI=AI_translation/pali/pi-5_split_chapters
MY=AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters
D=0-INBOX/temp/pipeline/pi-5-my
P1D=0-INBOX/temp/pipeline/pi-1-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
fail=0
setopt pipefail

echo "== rebuild (8 generators; terms_my5.py rewrites my5-zeroshot-terms.md)"
for g in make_sample make_ch2-5 make_ch6-10 make_ch11-12 make_ch13-16 make_ch17-20 make_ch21-25 make_ch26-31 terms_my5; do
  out=$(py $D/$g.py 2>&1); rc=$?
  if [[ $rc != 0 ]] || print -r -- "$out" | grep -q "MISS\|CHECK\|STOP\|Traceback"; then
    echo "FAILED: $g"; print -r -- "$out" | tail -8; fail=1
  fi
done

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
for c in check_sample check_ch2-5 check_ch6-10 check_ch11-12 check_ch13-16 check_ch17-20 check_ch21-25 check_ch26-31; do
  out=$(py $D/$c.py 2>&1); rc=$?
  print -r -- "$c: $(print -r -- "$out" | tail -1)"
  [[ $rc == 0 ]] && print -r -- "$out" | tail -1 | grep -q "^OK: 0 mismatches" || { print -r -- "$out" | grep -v "^ *$" | grep -B2 -A12 -i "mismatch" | head -30; fail=1; }
done

echo "== cross-chapter alignment (pi-1-my/align_check_my.py, align_hidden_my.py)"
py $P1D/align_check_my.py $PI $MY --all > $D/align-after.txt
py $P1D/align_hidden_my.py $PI $MY > $D/align-hidden-after.txt
head -1 $D/align-after.txt
tail -1 $D/align-hidden-after.txt
py $D/harmonise_align_explained.py || fail=1

echo "== pi-1 … pi-4 identity (harmonise_pi1234.py)"
mkdir -p $D/scratch
py $D/harmonise_pi1234.py > $D/scratch/pi1234.txt || fail=1; grep "identity" $D/scratch/pi1234.txt

echo "== harmonise scan (one form per item; writes harmonise-table.tsv) and lines changed"
sc=$(py $D/harmonise_scan.py --table 2>&1) || fail=1
print -r -- "$sc" | grep -v "^OK " | head -40
py $D/harmonise_diff.py | tail -1

[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
