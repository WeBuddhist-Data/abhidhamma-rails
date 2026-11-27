#!/bin/zsh
# pi-3 Burmese RAILS translation (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»): rebuild every chapter from the zero-shot
# generators + the rails layer, apply the residual rules, and run every check. Model: pi-2-my/rails/regen_rails.sh.
# usage: zsh 0-INBOX/temp/pipeline/pi-3-my/rails/regen_rails.sh   (from anywhere; writes only rails/ and the rails folder)
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
D=0-INBOX/temp/pipeline; G=$D/pi-3-my; R=$G/rails; P1=$D/pi-1-my
S=AI_translation/pali/pi-3_split_chapters
Z=AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters
T=AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters
KW=AI_translation/pali/pi-3-keywords-by-reference-pali-plain.md
TB=AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md
TB_SHA=857bfa8eff945d72eb1a52ec55c452798b34f9d11860322bfe7cc15096f243f3   # termbase/APPROVED.md (locked 2026-11-19)
fail=0
setopt pipefail

echo "== 0. protected inputs (termbase, zero-shot chapters + merged file, generators, my3_formulas, pi-1 / pi-2 final) unchanged"
md5 -r $(awk '{print $2}' $R/protected-md5-before.txt) | diff -q - $R/protected-md5-before.txt >/dev/null \
  && echo "protected md5: unchanged ($(wc -l < $R/protected-md5-before.txt | tr -d ' ') files)" \
  || { echo "FAIL: a protected file changed"; fail=1; }
[[ $(shasum -a 256 $TB | cut -d" " -f1) == $TB_SHA ]] && echo "termbase sha256: recorded lock" || { echo "FAIL: termbase hash"; fail=1; }

echo "== 1. reproduction test (build without the layer = the zero-shot), build (zero-shot generators + rails layer), residual rules"
py $R/build_rails.py --plain $R/plain-test >/dev/null 2>&1 || { echo "FAIL plain build"; fail=1; }
same=0; for f in $Z/*.md; do cmp -s $f $R/plain-test/${f:t} && same=$((same+1)); done
echo "plain build = zero-shot: $same of $(ls $Z/*.md | wc -l | tr -d ' ') files identical"
[[ $same == $(ls $Z/*.md | wc -l | tr -d ' ') ]] || fail=1
rm -rf $R/plain-test
out=$(py $R/build_rails.py 2>&1) || { print -r -- "$out" | grep -v "^wrote" | tail -5; echo "FAIL build"; exit 1; }
print -r -- "$out" | tail -1
py $R/apply_termbase.py || { echo "FAIL apply"; exit 1; }
[[ $(ls $T/*.md | wc -l | tr -d ' ') == 16 ]] && echo "rails folder: 16 files" || { echo "FAIL: rails file count"; fail=1; }

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
py $R/classify_misses.py || { echo "FAIL classify"; fail=1; }
py $R/rails_misses_check.py $R/adherence-rails.txt $R/adherence-classified.tsv || { echo "FAIL adherence"; fail=1; }
py $R/map_vs_termbase.py > $R/map-vs-termbase.txt || { echo "FAIL map vs termbase"; fail=1; }
echo "sense-level: $(head -1 $R/map-vs-termbase.txt)"

echo "== 4. cross-chapter alignment"
py $P1/align_check_my.py $S $Z --all > $R/align-zeroshot.txt
py $P1/align_check_my.py $S $T --all > $R/align-rails.txt
py $P1/align_hidden_my.py $S $T > $R/align-hidden-rails.txt
echo "align: $(head -1 $R/align-rails.txt)"
py $R/align_kept.py || fail=1
echo "hidden: $(tail -1 $R/align-hidden-rails.txt)"
grep -q "unmatched repeated sentences: 0" $R/align-hidden-rails.txt || fail=1

echo "== 5. pi-1 / pi-2 identity (every pi-3 sentence that occurs in pi-1 / pi-2 keeps their final rails Burmese)"
py $R/pi12_identity.py $T > $R/pi12-identity-rails.txt || fail=1
grep "identity" $R/pi12-identity-rails.txt

echo "== 6. per-line scan of the rails families (H1-H4, plural-marker terms)"
py $R/line_scan.py $S $Z > $R/line-scan-zeroshot.txt
py $R/line_scan.py $S $T > $R/line-scan-rails.txt
py $R/line_scan.py $S $T --stats | grep -c "^stats	[1-9]" | read fired
echo "line scan: $(wc -l < $R/line-scan-rails.txt | tr -d ' ') lines left (zero-shot $(wc -l < $R/line-scan-zeroshot.txt | tr -d ' ') flags; $fired of $(py $R/line_scan.py $S $T --stats | grep -c '^stats') families with Pāli hits)"
[[ -s $R/line-scan-rails.txt ]] && fail=1

echo "== 7. lines changed against the zero-shot"
py $R/diff_count.py > $R/lines-changed.txt; tail -1 $R/lines-changed.txt

echo "== 8. rerun stability (outputs against the previous run)"
md5 -r $T/*.md $R/*.tsv $R/*.txt(N) | grep -v "output-md5.txt" > $R/output-md5.new
if [[ -f $R/output-md5.txt ]]; then
  diff -q $R/output-md5.txt $R/output-md5.new >/dev/null && echo "rerun: no byte changed ($(wc -l < $R/output-md5.new | tr -d ' ') files)" \
    || { echo "rerun: outputs differ from the previous run:"; diff $R/output-md5.txt $R/output-md5.new | grep "^[<>]" | head; }
else
  echo "rerun: first run, md5s recorded"
fi
mv $R/output-md5.new $R/output-md5.txt

echo "termbase sha256 $(shasum -a 256 $TB | cut -c1-12) (locked, read only; recorded ${TB_SHA[1,12]})"
[[ $fail == 0 ]] && echo "ALL CHECKS PASSED" || { echo "SOME CHECKS FAILED"; exit 1; }
