import sys
for ch in sys.argv[1:]:
    a=open(f'work/{ch}.prev',encoding='utf-8').read().splitlines(); b=open(f'{ch}.mapped.md',encoding='utf-8').read().splitlines()
    for x,y in zip(a,b):
        if x!=y:
            X=x.split('] ',1)[1].split(', '); Y=y.split('] ',1)[1].split(', ')
            for p,q in zip(X,Y):
                if p!=q: print(ch[:3], x.split(']')[0][1:], p, '=>', q.split('=',1)[1])
