import sys
a=[l.split('] ',1) for l in open(sys.argv[1],encoding='utf-8').read().splitlines()]
b=[l.split('] ',1) for l in open(sys.argv[2],encoding='utf-8').read().splitlines()]
assert [x[0] for x in a]==[x[0] for x in b]
bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.rsplit('=',1)[1] for k in y.split(', ')]]
print('lines',len(a),len(b),'english keywords unchanged:',not bad, bad[:5])