cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my
for c in "$@"; do
  /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 make_ch5-13-20.py $c > chk-ch5-13-20/run-$c.txt 2>&1 &
done
wait
for c in "$@"; do echo "$c: $(tail -1 chk-ch5-13-20/run-$c.txt)"; done
