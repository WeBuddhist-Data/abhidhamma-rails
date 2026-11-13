import sys, os
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
H = os.path.join(ROOT, 'hindi', 'pi-6-hindi-plain-rails_split_chapters')

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

def load(fn):
    return lines(os.path.join(P, fn)), lines(os.path.join(H, fn))

if __name__ == '__main__':
    fn = sys.argv[1]
    a, b = int(sys.argv[2]), int(sys.argv[3])
    pl, hl = load(fn)
    out = []
    for i in range(a - 1, min(b, len(pl))):
        out.append(f'{i+1} P: {pl[i]}')
        out.append(f'{i+1} H: {hl[i]}')
    sys.stdout.write('\n'.join(out) + '\n')
