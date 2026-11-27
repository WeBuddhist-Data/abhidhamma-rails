#!/bin/zsh
# scratch: rebuild all chapters (stop on the first failure), then lines changed + align summaries
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-5-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
for g in make_sample make_ch2-5 make_ch6-10 make_ch11-12 make_ch13-16 make_ch17-20 make_ch21-25 make_ch26-31; do
  out=$(py $g.py 2>&1); rc=$?
  if [[ $rc != 0 ]] || print -r -- "$out" | grep -q "MISS\|CHECK\|Traceback"; then echo "FAILED: $g"; print -r -- "$out" | tail -12; exit 1; fi
done
py harmonise_diff.py | tail -1
R=../../../../AI_translation
py ../pi-1-my/align_check_my.py $R/pali/pi-5_split_chapters $R/burmese/pi-5-burmese-plain-zeroshot_split_chapters --all > scratch/al.txt; head -1 scratch/al.txt
py ../pi-1-my/align_hidden_my.py $R/pali/pi-5_split_chapters $R/burmese/pi-5-burmese-plain-zeroshot_split_chapters > scratch/alh.txt; tail -1 scratch/alh.txt
