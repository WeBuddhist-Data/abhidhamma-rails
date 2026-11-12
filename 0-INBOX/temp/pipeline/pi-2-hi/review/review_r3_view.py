import sys
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
eng = len(sys.argv) > 4
P = [l for l in open(base + r'\pali\pi-2_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
H = [l for l in open(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
E = [l for l in open(base + r'\english\pi-2-english-plain-zeroshot_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
for i in range(a, min(b, len(P)) + 1):
    print('%d P: %s' % (i, P[i - 1]))
    if eng:
        print('%d E: %s' % (i, E[i - 1]))
    print('%d H: %s' % (i, H[i - 1]))
