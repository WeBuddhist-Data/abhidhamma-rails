import sys
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = {'1-02': '1-02-vedanattika.md', '1-03': '1-03-vipakattika.md', '1-04': '1-04-upadinnattika.md',
         '1-05': '1-05-sankilitthattika.md'}
ENG = '\\english\\pi-7-english-plain-zeroshot_split_chapters\\'
# usage: review_r2_show.py 1-03 132 207 ...  (nonempty line numbers; a-b for range); add 'e' to show English
args = sys.argv[1:]
key = args[0]
show_e = 'e' in args
f = FILES[key]
def ne(path):
    try:
        return [l for l in open(path, encoding='utf8').read().split('\n') if l.strip()]
    except FileNotFoundError:
        return []
p = ne(ROOT + '\\pali\\pi-7_split_chapters\\' + f)
h = ne(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + f)
e = ne(ROOT + ENG + f) if show_e else []
nums = []
for a in args[1:]:
    if a == 'e':
        continue
    if '-' in a:
        x, y = a.split('-'); nums += list(range(int(x), int(y) + 1))
    else:
        nums.append(int(a))
for n in nums:
    print('--- L%d' % n)
    print('P:', p[n - 1])
    print('H:', h[n - 1])
    if e:
        print('E:', e[n - 1])
