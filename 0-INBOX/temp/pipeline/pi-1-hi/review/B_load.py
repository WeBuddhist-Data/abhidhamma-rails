import re,sys,os,json
ROOT=r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P=os.path.join(ROOT,'pali','pi-1_split_chapters')
H=os.path.join(ROOT,'hindi','pi-1-hindi-plain-rails_split_chapters')
FILES='3-01-rupakandam 3-02-rupakandam 3-03-rupakandam 4-01-nikkhepakandam 4-02-nikkhepakandam 4-03-nikkhepakandam 5-atthakathakandam'.split()
def lines(path):
    return open(path,encoding='utf-8').read().split('\n')
IDRE=re.compile(r'\^([0-9a-z\-]+)\s*$')
def load():
    out=[]
    for f in FILES:
        p=[l for l in lines(os.path.join(P,f+'.md')) if l.strip()]
        h=[l for l in lines(os.path.join(H,f+'.md')) if l.strip()]
        if len(p)!=len(h): print('LINECOUNT',f,len(p),len(h))
        for i,(a,b) in enumerate(zip(p,h)):
            ma=IDRE.search(a); mb=IDRE.search(b)
            out.append(dict(f=f,i=i,id=ma.group(1) if ma else None,hid=mb.group(1) if mb else None,p=a,h=b))
    return out
if __name__=='__main__':
    d=load()
    print(len(d))
    print('withid',sum(1 for x in d if x['id']))
    for x in d:
        if x['id']!=x['hid']: print('IDMISMATCH',x['f'],x['i'],x['id'],x['hid'],x['p'][:60],x['h'][:60])
    for x in d:
        if not x['id']: print('NOID',x['f'],x['i'],x['p'][:100],'||',x['h'][:100])
    for f in FILES:
        t=open(os.path.join(H,f+'.md'),encoding='utf-8').read()
        print(f,'dblblank',len(re.findall(r'\n\s*\n\s*\n',t)))
