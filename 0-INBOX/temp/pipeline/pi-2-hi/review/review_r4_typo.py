import re, io, sys, collections
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\\'
for ch in sys.argv[1:]:
    L = [l.rstrip('\n') for l in io.open(base + ch, encoding='utf8')]
    ne = [l for l in L if l.strip()]
    words = collections.Counter(w for l in ne for w in re.findall(r'[\u0900-\u097F]+', l))
    print('==', ch)
    for i, l in enumerate(ne, 1):
        for w in re.findall(r'[\u0900-\u097F]+', l):
            for suf in ('के', 'की', 'का', 'को', 'में', 'से', 'ने'):
                if w.endswith(suf) and len(w) > len(suf) + 1:
                    stem = w[:-len(suf)]
                    if words.get(stem, 0) >= 3 and words.get(w, 0) < 5:
                        print(i, 'GLUE?', w)
        # Hindi quote ending without danda when followed by space+text
        for m in re.finditer(r'([^\s।?!])”(\s+)(\S+)', l):
            print(i, 'QUOTE-END', l[max(0, m.start()-15):m.end()+5])
        if re.search(r'[\.]\s*\^|[\u0900-\u097F]\.(\s|$)', l):
            print(i, 'LATINDOT')
