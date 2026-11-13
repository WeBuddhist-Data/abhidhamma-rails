import sys, glob
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]
f = sys.argv[1]
P = lines(glob.glob(B + r'\pali\pi-6_split_chapters\%s*.md' % f)[0])
H = lines(glob.glob(B + r'\hindi\pi-6-hindi-plain-rails_split_chapters\%s*.md' % f)[0])
E = lines(glob.glob(B + r'\english\pi-6-english-plain-rails_split_chapters\%s*.md' % f)[0])
for a in sys.argv[2:]:
    if '-' in a:
        s, e = map(int, a.split('-'))
    else:
        s = e = int(a)
    for i in range(s, e + 1):
        print('L%d P: %s' % (i, P[i - 1]))
        print('L%d H: %s' % (i, H[i - 1]))
        if '--en' in sys.argv[0:1] or len(E) == len(P):
            pass
        print()
