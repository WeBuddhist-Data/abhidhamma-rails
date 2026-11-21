import sys, re
R = 'D:/Work/OpenPecha/abhidhamma-rails/AI_translation/'
FILES = {
    'pi1': R + 'vietnamese/pi-1-vietnamese-plain.md',
    'pi2': R + 'vietnamese/pi-2-vietnamese-plain.md',
    'pi3': R + 'vietnamese/pi-3-vietnamese-plain.md',
    'pi4': R + 'vietnamese/pi-4-vietnamese-plain.md',
}
VI5 = R + 'vietnamese/pi-5-vietnamese-plain-rails_split_chapters/'
PI5 = R + 'pali/pi-5_split_chapters/'
texts = {k: open(v, encoding='utf-8').read() for k, v in FILES.items()}
import os
v5 = {f: open(VI5 + f, encoding='utf-8').read() for f in os.listdir(VI5) if f.endswith('.md')}
mode = sys.argv[1]
args = sys.argv[2:]
if mode == 'count':
    for a in args:
        c = {k: t.count(a) for k, t in texts.items()}
        c5 = sum(t.count(a) for t in v5.values())
        print(repr(a), c, 'pi5:', c5)
elif mode == 'ctx':
    a = args[0]
    n = int(args[1]) if len(args) > 1 else 3
    w = int(args[2]) if len(args) > 2 else 120
    for k, t in list(texts.items()) + [('pi5:' + f, t) for f, t in v5.items()]:
        i = 0
        shown = 0
        while shown < n:
            j = t.find(a, i)
            if j < 0:
                break
            print(k, '::', t[max(0, j - w):j + len(a) + w].replace('\n', ' / '))
            i = j + 1
            shown += 1
elif mode == 'pictx':
    # find Pali string contexts in pi-5 Pali chapters, or in a given Pali pi-N file
    a = args[0]
    n = int(args[1]) if len(args) > 1 else 3
    for f in sorted(os.listdir(PI5)):
        t = open(PI5 + f, encoding='utf-8').read()
        i = 0
        shown = 0
        while shown < n:
            j = t.find(a, i)
            if j < 0:
                break
            print(f, '::', t[max(0, j - 100):j + len(a) + 100].replace('\n', ' / '))
            i = j + 1
            shown += 1
