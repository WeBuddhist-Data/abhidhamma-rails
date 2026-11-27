import re,glob,os
pat=re.compile(r'အိပ်ရာ နေရာကို (?!အားကြီးစွာ)(\S+?)(သည်|ကို) ')
for f in sorted(glob.glob('burmese/pi-7-burmese-plain-rails_split_chapters/*.md')):
    for i,l in enumerate(open(f,encoding='utf8').read().split('\n'),1):
        for m in pat.finditer(l):
            sid=re.findall(r'\^\S+',l); print(os.path.basename(f),i,sid[-1] if sid else '-',m.group(0))
