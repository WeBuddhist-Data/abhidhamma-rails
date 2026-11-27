#!/bin/zsh
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-5-my
for c in check_sample check_ch2-5 check_ch6-10 check_ch11-12 check_ch13-16 check_ch17-20 check_ch21-25 check_ch26-31; do
  out=$(/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 $c.py 2>&1)
  echo "$c: $(print -r -- "$out" | tail -1)"
  print -r -- "$out" | grep -A8 "MISMATCHES\|Traceback" | head -10 | cut -c1-220
done
