import re, collections, glob
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
c = collections.Counter()
for f in ['10-09', '10-10', '10-11', '10-12', '10-13']:
    h = glob.glob(B + r'\hindi\pi-6-hindi-plain-rails_split_chapters\%s*.md' % f)[0]
    t = open(h, encoding='utf-8').read()
    for m in re.finditer(r'(पूरी तरह|छोड़|अभ्यास|साक्षात्कार|उत्पन्न|निर्वाण|मार्ग प्राप्त|प्राप्त)( नहीं)?(\S*)( \S+)?( \S+)?', t):
        c[m.group(1) + (m.group(2) or '') + m.group(3) + (m.group(4) or '') + (m.group(5) or '')] += 1
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    if 'उत्पन्न' in k and v > 30:
        continue
    print(v, k)
