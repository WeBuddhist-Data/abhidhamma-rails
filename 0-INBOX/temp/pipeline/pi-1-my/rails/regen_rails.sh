#!/bin/zsh
# pi-1 Burmese RAILS translation (Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»): rebuild every chapter from the
# zero-shot generators + the rails layer, apply the residual rules and the bilingual-review fixes, and run every check.
# usage: zsh 0-INBOX/temp/pipeline/pi-1-my/rails/regen_rails.sh   (from anywhere; writes only rails/ and the rails folder)
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
D=0-INBOX/temp/pipeline; G=$D/pi-1-my; R=$G/rails
S=AI_translation/pali/pi-1_split_chapters
Z=AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters
T=AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters
KW=AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md
TB=AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md
TB_SHA=3c8cc8d0654cfc94d1b337859305056d06c308b10693dd44f07e3beb821a9972   # termbase/APPROVED.md (B6/B7/B10 change 2026-11-17)
fail=0
setopt pipefail

echo "== 0. protected inputs (termbase, zero-shot chapters, generators) unchanged"
md5 -r $(awk '{print $2}' $R/protected-md5-before.txt) | diff -q - $R/protected-md5-before.txt >/dev/null \
  && echo "protected md5: unchanged ($(wc -l < $R/protected-md5-before.txt | tr -d ' ') files)" \
  || { echo "FAIL: a protected file changed"; fail=1; }

[[ $(shasum -a 256 $TB | cut -d" " -f1) == $TB_SHA ]] && echo "termbase sha256: recorded lock" || { echo "FAIL: termbase hash"; fail=1; }

echo "== 1. build (zero-shot generators + rails layer), residual rules, review fixes"
out=$(py $R/build_rails.py 2>&1) || { print -r -- "$out" | tail -5; echo "FAIL build"; exit 1; }
print -r -- "$out" | tail -1
py $R/apply_termbase.py || { echo "FAIL apply"; exit 1; }
fx=$(py $R/apply_fixes.py) || { print -r -- "$fx"; echo "FAIL fixes"; exit 1; }
echo "review fixes (rails/fixes-log.tsv): $(print -r -- "$fx" | tail -1)"

echo "== 2. check_chapter_ids / pi-6-mr/check_text_pe.py / pi-4-mr/check_marks.py"
bad=0
for f in $(ls $S | grep '\.md$'); do
  [[ $(py $D/check_chapter_ids.py $S $T $f) == *": OK"* ]] || { echo "ids FAIL $f"; bad=1; }
  py $D/pi-6-mr/check_text_pe.py $S/$f $T/$f | grep -q "OK" || { echo "text FAIL $f"; bad=1; }
  [[ $(py $D/pi-4-mr/check_marks.py $S/$f $T/$f) == OK ]] || { echo "marks FAIL $f"; bad=1; }
  rm -f $D/pi-6-mr/chk-pe/$f
done
echo "ids+text+marks over $(ls $S | grep -c '\.md$') chapters: $([[ $bad == 0 ]] && echo OK || echo FAIL)"
[[ $bad == 0 ]] || fail=1
py $G/harmonise_typo.py $T >/dev/null && echo "typography (no «?», no Zawgyi range, NFC): OK" || { echo "FAIL typo"; fail=1; }

echo "== 3. termbase adherence: zero-shot input, rails, classification"
py $R/adherence_my.py $KW $TB $Z | diff -q - $R/adherence-zeroshot.txt >/dev/null \
  && echo "zero-shot: $(head -1 $R/adherence-zeroshot.txt) (input file reproduced)" || { echo "FAIL zero-shot input"; fail=1; }
py $R/adherence_my.py $KW $TB $T $R/adherence-rails.txt | sed 's/^/rails: /'
py $R/classify_misses.py || { echo "FAIL classify"; fail=1; }
py $R/rails_misses_check.py $R/adherence-rails.txt $R/adherence-classified.tsv || { echo "FAIL adherence"; fail=1; }

echo "== 4. cross-chapter alignment"
py $G/align_check_my.py $S $T --all > $R/align-rails.txt
py $G/align_hidden_my.py $S $T > $R/align-hidden-rails.txt
echo "align: $(head -1 $R/align-rails.txt)"
echo "hidden: $(tail -1 $R/align-hidden-rails.txt)"
grep -q "with differing Burmese: 0;" $R/align-rails.txt || fail=1
grep -q "unmatched repeated sentences: 0" $R/align-hidden-rails.txt || fail=1

echo "== 5. per-line scan of the GENUINE families"
py $R/line_scan.py $S $Z > $R/line-scan-zeroshot.txt
py $R/line_scan.py $S $T > $R/line-scan-rails.txt
echo "line scan: $(wc -l < $R/line-scan-rails.txt | tr -d ' ') lines left (zero-shot $(wc -l < $R/line-scan-zeroshot.txt | tr -d ' ') flags)"
[[ -s $R/line-scan-rails.txt ]] && fail=1

echo "== 6. lines changed against the zero-shot"
py $R/diff_count.py | tail -1

echo "termbase sha256 $(shasum -a 256 $TB | cut -c1-12) (locked, read only; recorded ${TB_SHA[1,12]})"
[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || { echo "SOME CHECKS FAILED"; exit 1; }
