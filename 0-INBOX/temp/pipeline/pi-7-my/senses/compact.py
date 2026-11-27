"""One line per REVIEW headword from rv-review.txt: hw | kept | pi-7 values (count) || binding / Marathi tags.
A leading 'V' marks a heuristic one-lemma group (all value cores share a stem). usage: compact.py rv-review.txt"""
import re, sys
END = ['တော်မူခဲ့သည်', 'တော်မူသည်', 'တော်မူသော', 'တော်မူ', 'ခဲ့သည်', 'ခဲ့သော', 'ခဲ့', 'ပြီးသော', 'ပြီး', 'နေသော', 'နေသည်',
       'နေ', 'သော', 'သည်', 'ခြင်း', 'မှု', 'ချက်', '၍', 'သူ', 'ကြ', 'ရ', '၏', 'ကို', 'ဖြင့်', '၌', 'တွင်', 'များ', 'တို့',
       'ပါ', 'စွာ', 'ဆဲ', 'မည့်', 'ရန်', 'ကုန်', 'နိုင်', 'တတ်', 'စေ', 'အောင်', 'သင့်', 'ထိုက်', 'အပ်', 'ဖွယ်', 'လျှင်']
def core(v):
    v = v.replace('…', '').replace(' ', '')
    ch = True
    while ch:
        ch = False
        for e in END:
            if v.endswith(e) and len(v) > len(e) + 1:
                v = v[:-len(e)]; ch = True
    return v
blocks = open(sys.argv[1], encoding='utf-8').read().split('## ')[1:]
for b in blocks:
    ls = b.rstrip('\n').split('\n')
    hw = ls[0].split('  (')[0]
    kept = ls[0].rsplit('kept=', 1)[1]
    vals = re.findall(r'(?:^|\| )([^=|]+)=(\d+)\[', ls[1].split('pi-7: ', 1)[1])
    cs = [core(v.strip()) for v, _ in vals]
    pre = min(len(c) for c in cs)
    common = 0
    for i in range(pre):
        if len({c[i] for c in cs}) == 1: common += 1
        else: break
    mark = 'V' if common >= 2 and all(c.startswith(cs[0][:common]) for c in cs) else ' '
    ref = ' ## '.join(l.strip() for l in ls[2:])
    print(f"{mark} {hw} [{kept}] " + ' / '.join(f'{v.strip()}={n}' for v, n in vals) + f'  << {ref[:260]}')
