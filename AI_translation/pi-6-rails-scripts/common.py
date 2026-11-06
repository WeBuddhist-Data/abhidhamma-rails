"""Shared helpers for the pi-6 rails translation. Run from AI_translation/."""
import re,os
PALI='pali/pi-6_split_chapters/'
ENG='english/pi-6-english-plain-rails_split_chapters/'
def fmt_var(v):
    v=v.replace('evamuparipi','and likewise below')
    def ab(m):
        ps=[x.strip() for x in m.group(1).split('.') if x.strip()]
        return '('+', '.join(x.capitalize()+'.' for x in ps)+')'
    return '[variant: '+re.sub(r'\(([^()]*)\)',ab,v)+']'
def run(f,tr,HD):
    out=[];bad=[]
    for ln,l in enumerate(open(PALI+f,encoding='utf-8').read().split('\n'),1):
        if not l.strip(): out.append(l);continue
        m=re.match(r'^(.*?)( \^\S+)?$',l);body,bid=m.group(1),m.group(2) or ''
        h=re.match(r'^(#+) (.*)$',body)
        try:
            if h: t=f'{h.group(1)} {HD[h.group(2)]}'
            else:
                vs=re.findall(r'\[([^\]]+)\]',body);n=[-1]
                def rp(_):
                    n[0]+=1;return f'⟦{n[0]}⟧'
                t=tr(re.sub(r'\[[^\]]+\]',rp,body))
                for j,v in enumerate(vs): t=t.replace(f'⟦{j}⟧',fmt_var(v))
        except (KeyError,ValueError,TypeError,AttributeError) as e:
            bad.append((ln,repr(e)[:90],body[:200]));t='!!'
        out.append(t+bid)
    return out,bad
def write(f,out):
    os.makedirs(ENG,exist_ok=True)
    open(ENG+f,'w',encoding='utf-8').write('\n'.join(out))
def check(f):
    a=open(PALI+f,encoding='utf-8').read().split('\n');b=open(ENG+f,encoding='utf-8').read().split('\n')
    idf=lambda l:(re.search(r'\^(\S+)\s*$',l) or [None,None])[1]
    bad=[i+1 for i,(x,y) in enumerate(zip(a,b)) if idf(x)!=idf(y) or bool(x.strip())!=bool(y.strip()) or len(re.match(r'#*',x)[0])!=len(re.match(r'#*',y)[0])]
    q=[i+1 for i,(x,y) in enumerate(zip(a,b)) if x.count('?')!=y.count('?')]
    pl=[i+1 for i,l in enumerate(b) if re.search(r'[ṃñṭḍṅ]|⟦|!!|…pe…|…Pe…',re.sub(r'\[variant:.*?\]','',l))]
    print(f,'lines',len(a),len(b),'mismatch',bad[:8],'question-marks',q[:8],'leftover',pl[:8],'ids',sum(1 for l in a if idf(l)))
