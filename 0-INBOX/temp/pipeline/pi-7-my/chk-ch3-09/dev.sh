cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 make_ch3-09.py --dev $3 2>&1 | tail -3
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 -c "
import sys
t=open('chk-ch3-09/dev.txt',encoding='utf-8').read().split('\n[')
n=int(sys.argv[1]); w=int(sys.argv[2])
for b in t[:n]:
  l=b.split('\n')
  s=l[0].replace(chr(92),'')
  i=s.find('[',8)
  print(s[:w], '||', s[i:i+160] if i>0 else '')
  print('   ',l[1][:w] if len(l)>1 else '')
" "$1" "$2"
