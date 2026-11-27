import sys, pathlib, re; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.dont_write_bytecode=True
import check_sample as K
a=[l for l in open(sys.argv[1],encoding='utf-8-sig').read().splitlines() if l.strip()]
b=[l for l in open(sys.argv[2],encoding='utf-8').read().splitlines() if l.strip()]
for n in map(int, sys.argv[3:]):
    x,y=K.VAR_PI.sub('',a[n-1]),K.VAR_MY.sub('',b[n-1])
    px=[]; s=x
    for rx,w in K.NEG_PI_RE:
        px += [(m, w) for m in rx.findall(s)]; s=rx.sub(' ',s)
    py=[]; s=y
    for rx,w in K.NEG_MY_RE:
        for m in rx.finditer(s):
            if w: py.append(s[max(0,m.start()-2):m.end()+6])
        s=rx.sub(' ',s)
    print(n, 'PI', px); print(n, 'MY', py)
