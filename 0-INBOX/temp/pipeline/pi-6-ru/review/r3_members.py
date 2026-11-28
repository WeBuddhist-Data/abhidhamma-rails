"""Compare ordered member sequences (truths / formations) per line, Pali vs Russian."""
import sys, re
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
files = sys.argv[1].split(',')
verbose = len(sys.argv) > 2
PM = [(r'dukkhasacc', 'D'), (r'samudayasacc', 'S'), (r'nirodhasacc', 'N'), (r'maggasacc', 'M'),
      (r'kāyasaṅkhār', 'K'), (r'vacīsaṅkhār', 'V'), (r'cittasaṅkhār', 'C')]
RM = [(r'(?<![а-яё])о страдании', 'D'), (r'(?<![а-яё])о возникновении', 'S'), (r'(?<![а-яё])о прекращении', 'N'), (r'(?<![а-яё])о пути', 'M'),
      (r'телесн\w+ формирующ', 'K'), (r'речев\w+ формирующ', 'V'), (r'формирующ\w+ фактор\w* ума', 'C')]
def seq(s, table):
    s = re.sub(r'\[[^\]]*\]', '', s)
    hits = []
    for rx, t in table:
        for m in re.finditer(rx, s, re.I):
            hits.append((m.start(), t))
    return ''.join(t for _, t in sorted(hits))
n = 0
for f in files:
    pl = open(P + f, encoding='utf-8').read().split('\n')
    rl = open(R + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith("#"):
            continue
        a, b = seq(p, PM), seq(r, RM)
        if a != b:
            n += 1
            print(f'{f}:{i} P={a} R={b}')
            if verbose:
                print('  P', p); print('  R', r)
print('mismatches', n)
