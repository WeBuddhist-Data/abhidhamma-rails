# r1 reviewer helper: find Pali patterns in pi-1/2/3 split chapters and print the aligned
# Vietnamese line (our approved translation) to the console. Writes nothing.
# usage: python -I -X utf8 r1_xbook.py "<pali regex>" ["<vi regex for snippet>"] [maxhits]
import sys, re, os, glob
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
pat = re.compile(sys.argv[1])
vpat = re.compile(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else None
maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 3
books = sys.argv[4].split(',') if len(sys.argv) > 4 else ['1', '2', '3']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

hits = 0
for n in books:
    pdir = os.path.join(ROOT, 'pali', f'pi-{n}_split_chapters')
    vdir = os.path.join(ROOT, 'vietnamese', f'pi-{n}-vietnamese-plain-rails_split_chapters')
    for pf in sorted(glob.glob(os.path.join(pdir, '*.md'))):
        vf = os.path.join(vdir, os.path.basename(pf))
        if not os.path.exists(vf):
            continue
        pl, vl = lines(pf), lines(vf)
        for i, l in enumerate(pl):
            m = pat.search(l)
            if not m:
                continue
            v = vl[i] if i < len(vl) else '<<no line>>'
            s = max(0, m.start() - 60)
            print(f'== pi-{n} {os.path.basename(pf)} line{i}')
            print('  P:', l[s:m.end() + 120])
            if vpat:
                vm = vpat.search(v)
                if vm:
                    vs = max(0, vm.start() - 120)
                    print('  V:', v[vs:vm.end() + 200])
                else:
                    print('  V(no vi match):', v[:int(os.environ.get('R1W', '300'))])
            else:
                print('  V:', v[:int(os.environ.get('R1W', '500'))])
            hits += 1
            if hits >= maxhits:
                sys.exit(0)
print('hits', hits)
