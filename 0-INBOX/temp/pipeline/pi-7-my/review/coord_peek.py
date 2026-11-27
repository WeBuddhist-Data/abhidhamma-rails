import re,sys
for spec in sys.argv[1:]:
    f,n=spec.split(':'); n=int(n)
    p=open(f'pali/pi-7_split_chapters/{f}.md',encoding='utf8').read().split('\n')[n-1]
    b=open(f'burmese/pi-7-burmese-plain-rails_split_chapters/{f}.md',encoding='utf8').read().split('\n')[n-1]
    print('==',spec)
    for m in re.finditer(r'senāsan',p): print('  PI:',p[max(0,m.start()-150):m.end()+110])
    for m in re.finditer(r'အိပ်ရာ နေရာကို (စိတ်|မောဟ)သည်',b): print('  MY:',b[max(0,m.start()-100):m.end()+70])
