#!/bin/zsh
# Rebuild the pi-7 Burmese termbase from the raw-*.tsv files and refresh the reports (run from anywhere).
set -e
P=/opt/homebrew/Caskroom/miniconda/base/bin/python3
T=/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my/termbase
B=/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails
cd $B/0-INBOX/temp/pipeline
$P -I -X utf8 $T/build.py
$P -I -X utf8 termbase_assemble.py 7 burmese my plain | tee $T/assemble-out.txt
md5 -q $T/decisions-A.tsv $B/AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md $T/termbase-decisions.md
