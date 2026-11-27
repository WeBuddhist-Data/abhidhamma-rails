# list of protected files (md5 recorded before any rails work); run from the vault root. Model: pi-6-my/rails/protected_list.py
import os
G='0-INBOX/temp/pipeline/pi-7-my'
B='AI_translation/burmese'
out=[]
for d in [B+'/pi-7-burmese-plain-zeroshot_split_chapters']+[B+'/pi-%d-burmese-plain-rails_split_chapters'%i for i in range(1,7)]:
    out+=[d+'/'+f for f in sorted(os.listdir(d)) if f.endswith('.md')]
out+=[B+'/pi-7-burmese-plain-zeroshot.md',B+'/pi-7-keywords-by-reference-pali-burmese-plain.md',B+'/pi-7-pali-burmese-termbase-plain.md',
      'AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md']
out+=[B+'/pi-%d-pali-burmese-termbase-plain.md'%i for i in range(1,7)]
for f in sorted(os.listdir(G)):
    if (f.startswith(('make_','check_','notes-','harmonise')) and f.endswith(('.py','.md'))) or f in ('my7_formulas.py','regen_zeroshot.sh','my7-zeroshot-terms.md'):
        out.append(G+'/'+f)
out+=[G+'/termbase/'+f for f in ('APPROVED.md','decisions-A.tsv','termbase-decisions.md','notes-part5.txt')]
out+=[G+'/mapper-my/map-harmonise-notes.md']
for f in out: assert os.path.isfile(f),f
print(' '.join(out))
