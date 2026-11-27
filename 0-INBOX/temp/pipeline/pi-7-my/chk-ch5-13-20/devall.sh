cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my
for c in 5-13 5-14 5-15 5-16 5-17 5-18 5-19 5-20; do
  /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 make_ch5-13-20.py $c --dev > chk-ch5-13-20/log-$c.txt 2>&1 &
done
wait
for c in 5-13 5-14 5-15 5-16 5-17 5-18 5-19 5-20; do echo "$c: $(tail -1 chk-ch5-13-20/log-$c.txt)"; done
