import sys, os
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'


def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

# usage: file idx[,idx..] or file a-b
f = sys.argv[1]
P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f))
H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
E = None
if '-e' in sys.argv:
    E = load(os.path.join(B, 'english', 'pi-7-english-plain-zeroshot_split_chapters', f))
idx = []
for part in sys.argv[2].split(','):
    if '-' in part:
        a, b = part.split('-'); idx += list(range(int(a), int(b) + 1))
    else:
        idx.append(int(part))
for i in idx:
    print(f'--- {i}')
    print('P:', P[i - 1])
    print('H:', H[i - 1])
    if E:
        print('E:', E[i - 1])
