"""Print the termbase entries for every keyword of this chapter's segments, and any
further termbase key that appears as a word of the chapter or begins with a listed stem."""
import re, sys, pathlib
R = pathlib.Path(r'D:\Work\OpenPecha\abhidhamma-rails')
tb = {}
for l in (R / 'AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md').read_text(encoding='utf-8').splitlines():
    k, b = l.split(': {', 1)
    tb[k] = b[:-1]
ci = {k.lower(): k for k in tb}
src = (R / 'AI_translation/pali/pi-1_split_chapters/3-01-rupakandam.md').read_text(encoding='utf-8')
ids = set(re.findall(r'\^([0-9A-Za-z-]+)\s*$', src, re.M))
seen = {}
for l in (R / 'AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md').read_text(encoding='utf-8').splitlines():
    i, body = l.split('] ', 1)
    if i[1:] in ids:
        for k in body.split(', '):
            for kk in k.split(' / '):
                seen.setdefault(kk, i[1:])
print('=== keywords of chapter', len(seen))
for k, i in seen.items():
    kk = ci.get(k.lower())
    print(f'{i}\t{k}\t{tb[kk] if kk else "##MISSING"}')
words = {w.lower() for w in re.findall(r"[^\W\d_]+", src)}
print('=== other termbase keys that are words in chapter')
for k in tb:
    if k.lower() in words and k not in seen:
        print(f'{k}\t{tb[k]}')
if len(sys.argv) > 1:
    print('=== stem search')
    for s in sys.argv[1].split(','):
        for k in tb:
            if s.lower() in k.lower():
                print(f'[{s}] {k}\t{tb[k]}')
