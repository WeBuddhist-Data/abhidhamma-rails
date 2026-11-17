import re, sys
KOTI = 10**7; SATASAHASSA = 10**5
# (name, human years per divine day, divine years, Pali total, Russian total)
rows = [
    ("catumaharajika", 50, 500, 90*SATASAHASSA, 9_000_000),
    ("tavatimsa", 100, 1000, 3*KOTI + 60*SATASAHASSA, 36_000_000),
    ("yama", 200, 2000, 14*KOTI + 40*SATASAHASSA, 144_000_000),
    ("tusita", 400, 4000, 57*KOTI + 60*SATASAHASSA, 576_000_000),
    ("nimmanarati", 800, 8000, 2*100*KOTI + 30*KOTI + 40*SATASAHASSA, 2_304_000_000),
    ("paranimmita", 1600, 16000, 9*100*KOTI + 21*KOTI + 60*SATASAHASSA, 9_216_000_000),
]
tot = 0
for n, d, y, pali, ru in rows:
    calc = d * 30 * 12 * y
    tot += calc
    print(f"{n:15} calc={calc:>14,} pali={pali:>14,} ru={ru:>14,} {'OK' if calc==pali==ru else 'MISMATCH'}")
verse_pali = 12*100*KOTI + 28*KOTI + 50*SATASAHASSA
verse_ru = 12_000_000_000 + 280_000_000 + 5_000_000
print(f"sum={tot:,} verse_pali={verse_pali:,} verse_ru={verse_ru:,} {'OK' if tot==verse_pali==verse_ru else 'MISMATCH'}")

# Typography scan of the Russian file
ru = open(sys.argv[1], encoding='utf-8').read()
lines = ru.split('\n')
print('double blank:', '\n\n\n' in ru, ' CR:', '\r' in ru, ' em dash:', ru.count('—'))
for i, l in enumerate(lines, 1):
    if re.search(r'\bли\b', l): print('LI', i)
    stripped = re.sub(r'\[[^\]]*\]', '', l)
    stripped = re.sub(r'\^[\w-]+', '', stripped)
    lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', stripped)
    if lat: print('LATIN', i, lat)
    if re.search(r'  ', l): print('DOUBLE SPACE', i)
