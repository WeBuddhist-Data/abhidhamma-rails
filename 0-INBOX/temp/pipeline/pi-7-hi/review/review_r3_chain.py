import re, os
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

# chained "… Xpaccayena paccayo" after an ellipsis: verb should agree with the main subject (dhammo -> होती है; dhammā -> होती हैं)
for f in FILES:
    P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f)); H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        m = re.match(r'.*?\b(dhammo|dhammā)\b[^–]*?\bdhammassa\b', p)
        if not m:
            continue
        pl = m.group(1) == 'dhammā'
        exp = 'होती हैं' if pl else 'होती है'
        for c in re.finditer(r'…\s*(?:\([^)]*\)\s*)?((?:पूर्ण निकटता|प्रबल आश्रय|[^\s…]+)-कारण के रूप में कारण (होत\S+ \S+))', h):
            v = c.group(2).rstrip('।…')
            if v != exp:
                print(f'{f[:4]}:{i} pl={pl} chain verb "{v}" | {c.group(1)[:80]}')
