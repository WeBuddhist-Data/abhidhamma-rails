#!/bin/zsh
# pi-6 Burmese RAILS translation (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»): rebuild every chapter from the zero-shot generators
# + the rails layer, apply the residual rules, and run every check.
# Model: pi-5-my/rails/regen_rails.sh (read only).
# usage: zsh 0-INBOX/temp/pipeline/pi-6-my/rails/regen_rails.sh   (from anywhere; writes only rails/ and the rails folder)
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
D=0-INBOX/temp/pipeline; G=$D/pi-6-my; R=$G/rails; P1=$D/pi-1-my
S=AI_translation/pali/pi-6_split_chapters
Z=AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters
T=AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters
KW=AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md
TB=AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md
TB_SHA=847e49cdef8bc8c3f90d2de9f92fd0c6479f60e17a04c8243286b12602a86453   # termbase/APPROVED.md (locked 2026-11-22)
NCH=44
fail=0
setopt pipefail

echo "== 0. protected inputs (termbase, zero-shot chapters + merged file, keyword maps, generators + checks, my6_formulas, regen_zeroshot, notes, harmonise files, termbase decisions, map-harmonise-notes, pi-1 … pi-5 final rails + termbases) unchanged"
md5 -r $(awk '{print $2}' $R/protected-md5-before.txt) | diff -q - $R/protected-md5-before.txt >/dev/null \
  && echo "protected md5: unchanged ($(wc -l < $R/protected-md5-before.txt | tr -d ' ') files)" \
  || { echo "FAIL: a protected file changed"; fail=1; }
[[ $(shasum -a 256 $TB | cut -d" " -f1) == $TB_SHA ]] && echo "termbase sha256: recorded lock" || { echo "FAIL: termbase hash"; fail=1; }

echo "== 1. reproduction test (build without the layer = the zero-shot), build (zero-shot generators + rails layer), residual rules, review fixes"
py $R/build_rails.py --plain $R/plain-test >/dev/null 2>&1 || { echo "FAIL plain build"; fail=1; }
same=0; for f in $Z/*.md; do cmp -s $f $R/plain-test/${f:t} && same=$((same+1)); done
echo "plain build = zero-shot: $same of $(ls $Z/*.md | wc -l | tr -d ' ') files identical"
[[ $same == $(ls $Z/*.md | wc -l | tr -d ' ') ]] || fail=1
rm -rf $R/plain-test
out=$(py $R/build_rails.py 2>&1) || { print -r -- "$out" | tail -5; echo "FAIL build"; exit 1; }
print -r -- "$out" | tail -1
py $R/apply_termbase.py || { echo "FAIL apply"; exit 1; }
out=$(py $R/apply_fixes.py 2>&1) || { print -r -- "$out" | grep -v "^ *[0-9]*  [FQ]\|check:" | tail -8; echo "FAIL fixes"; exit 1; }
print -r -- "$out" | tail -1 | sed 's/^/fixes (review): /'
[[ $(ls $T/*.md | wc -l | tr -d ' ') == $NCH ]] && echo "rails folder: $NCH files" || { echo "FAIL: rails file count"; fail=1; }

echo "== 2. check_chapter_ids / check_text_pe (pi-6-mr wrapper, copies in rails/chk-pe) / pi-4-mr/check_marks.py"
bad=0
for f in $(ls $S | grep '\.md$'); do
  [[ $(py $D/check_chapter_ids.py $S $T $f) == *": OK"* ]] || { echo "ids FAIL $f"; bad=1; }
  py $R/check_text_pe_rails.py $S/$f $T/$f | grep -q "OK" || { echo "text FAIL $f"; bad=1; }
  [[ $(py $D/pi-4-mr/check_marks.py $S/$f $T/$f) == OK ]] || { echo "marks FAIL $f"; bad=1; }
done
rm -rf $R/chk-pe
echo "ids+text+marks over $(ls $S | grep -c '\.md$') files: $([[ $bad == 0 ]] && echo OK || echo FAIL)"
[[ $bad == 0 ]] || fail=1
py $P1/harmonise_typo.py $T >/dev/null && echo "typography (no «?», no Zawgyi range, NFC): OK" || { echo "FAIL typo"; fail=1; }

echo "== 3. termbase adherence: zero-shot input, rails, classification"
py $R/adherence_my.py $KW $TB $Z | diff -q - $R/adherence-zeroshot.txt >/dev/null \
  && echo "zero-shot: $(head -1 $R/adherence-zeroshot.txt) (input file reproduced)" || { echo "FAIL zero-shot input"; fail=1; }
py $R/adherence_my.py $KW $TB $T $R/adherence-rails.txt | sed 's/^/rails: /'
py $R/classify_misses.py > $R/classify-out.txt || fail=1
head -1 $R/classify-out.txt; grep -c "^UNVERIFIED" $R/classify-out.txt | sed 's/^/unverified rows (GENUINE left or unclassified): /'
py $R/rails_misses_check.py $R/adherence-rails.txt $R/adherence-classified.tsv | head -1 || fail=1
la=$(py $R/line_adh.py $T --unexplained | grep -v "^ " | grep -v "^UNEXPLAINED")
echo "line-level adherence (stricter, not required): $(print -r -- "$la" | head -1); $(print -r -- "$la" | tail -1 | cut -d' ' -f1-2) (all inflection patterns)"
[[ $(print -r -- "$la" | tail -1) == "unexplained 0 {}" ]] || { echo "FAIL: line-level miss outside the inflection patterns"; fail=1; }

echo "== 4. cross-chapter alignment"
py $P1/align_check_my.py $S $T --all > $R/align-rails.txt
py $P1/align_hidden_my.py $S $T > $R/align-hidden-rails.txt
echo "align: $(head -1 $R/align-rails.txt)"
echo "hidden: $(tail -1 $R/align-hidden-rails.txt)"
grep -q "with differing Burmese: 0;" $R/align-rails.txt || { echo "FAIL: align_check differing (the zero-shot had 0)"; fail=1; }
grep -q "unmatched repeated sentences: 0" $R/align-hidden-rails.txt || { echo "FAIL: align_hidden unmatched"; fail=1; }
py $R/align_explained.py | head -1 || fail=1

echo "== 5. pi-1 … pi-5 identity (every pi-6 sentence that occurs in pi-1 … pi-5 keeps their final rails Burmese)"
py $R/pi12345_identity.py $T > $R/pi12345-identity-rails.txt || fail=1
grep "identity" $R/pi12345-identity-rails.txt
grep -q "pi-1 identity: 10 / 10 identical, 0 explained; differing: 0" $R/pi12345-identity-rails.txt \
  && grep -q "pi-2 identity: 14 / 14 identical, 0 explained; differing: 0" $R/pi12345-identity-rails.txt \
  && grep -q "pi-3 identity: 10 / 332 identical, 322 explained; differing: 0" $R/pi12345-identity-rails.txt \
  && grep -q "pi-4 identity: 10 / 10 identical, 0 explained; differing: 0" $R/pi12345-identity-rails.txt \
  && grep -q "pi-5 identity: 2791 / 2791 identical, 0 explained; differing: 0" $R/pi12345-identity-rails.txt \
  || { echo "FAIL: identity counts differ from 10/10, 14/14, 10/332 + 322, 10/10, 2791/2791 (the zero-shot)"; fail=1; }

echo "== 6. per-line scan of the rails families"
py $R/line_scan.py $S $Z > $R/line-scan-zeroshot.txt
py $R/line_scan.py $S $T > $R/line-scan-rails.txt
fired=$(py $R/line_scan.py $S $T --stats | grep -c "^stats	[1-9]")
echo "line scan: $(wc -l < $R/line-scan-rails.txt | tr -d ' ') lines left (zero-shot $(wc -l < $R/line-scan-zeroshot.txt | tr -d ' ') flags; $fired of $(py $R/line_scan.py $S $T --stats | grep -c '^stats') families with Pāli hits)"
[[ -s $R/line-scan-rails.txt ]] && fail=1

echo "== 7. lines changed against the zero-shot"
py $R/diff_count.py > $R/lines-changed.txt; tail -1 $R/lines-changed.txt

echo "== 8. rerun stability (outputs against the previous run)"
md5 -r $T/*.md $R/*.tsv $R/*.txt(N) | grep -v "output-md5.txt\|protected-md5-before.txt\|coord-run" > $R/output-md5.new
if [[ -f $R/output-md5.txt ]]; then
  diff -q $R/output-md5.txt $R/output-md5.new >/dev/null && echo "rerun: no byte changed ($(wc -l < $R/output-md5.new | tr -d ' ') files)" \
    || { echo "rerun: outputs differ from the previous run:"; diff $R/output-md5.txt $R/output-md5.new | grep "^[<>]" | head; }
else
  echo "rerun: first run, md5s recorded"
fi
mv $R/output-md5.new $R/output-md5.txt

echo "termbase sha256 $(shasum -a 256 $TB | cut -c1-12) (locked, read only; recorded ${TB_SHA[1,12]})"
[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || { echo "SOME CHECKS FAILED"; exit 1; }
