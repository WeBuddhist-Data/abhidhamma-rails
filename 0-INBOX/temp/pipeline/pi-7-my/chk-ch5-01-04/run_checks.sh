#!/bin/zsh
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails
PY=/opt/homebrew/Caskroom/miniconda/base/bin/python3
for ch in 5-01-anuloma-tikatika.md 5-02-anuloma-dukaduka.md 5-03-paccaniya-tika.md 5-04-paccaniya-duka.md; do
  echo "== $ch"
  $PY -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-7_split_chapters AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters $ch | tail -1
  $PY -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-7_split_chapters/$ch AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/$ch | tail -1
done
echo "== own check + text check (--pe)"
$PY -I -X utf8 0-INBOX/temp/pipeline/pi-7-my/check_ch5-01-04.py --pe 2>&1 | tail -8
echo "exit $?"
