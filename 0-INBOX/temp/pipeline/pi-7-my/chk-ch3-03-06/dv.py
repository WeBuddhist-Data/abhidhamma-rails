import re, sys
for l in open('/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my/chk-ch3-03-06/dev.txt',encoding='utf-8'):
    if l.startswith('['):
        m=re.search(r"\[(\d+)\] SK: (.*)",l); sk=m[2]
        mm=re.search(r"\[\\+'([^\]]*?)\\+'\]",sk)
        print(m[1], (mm[1] if mm else sk[:200])[:int(sys.argv[1]) if len(sys.argv)>1 else 200])
    else: print('     ', l.strip()[:200])
