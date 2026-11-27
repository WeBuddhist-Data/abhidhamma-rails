import re,glob,os
pat=re.compile(r'အိပ်ရာ နေရာ(၊ |လည်းကောင်း၊ |ကို )(မောဟ|စိတ်)(သည်|လည်းကောင်း)')
for f in sorted(glob.glob('burmese/pi-7-burmese-plain-rails_split_chapters/*.md')):
    pf='pali/pi-7_split_chapters/'+os.path.basename(f)
    B=open(f,encoding='utf8').read().split('\n'); P=open(pf,encoding='utf8').read().split('\n')
    for i,l in enumerate(B,1):
        for m in pat.finditer(l):
            p=P[i-1]; pm=[p[max(0,x.start()-25):x.end()+40] for x in re.finditer(r'senāsanaṃ (moho|cittaṃ) (?!upanissāya)',p)]
            print(os.path.basename(f)[:20],i,repr(m.group(0)),'|',l[m.end():m.end()+45],'|',pm)
