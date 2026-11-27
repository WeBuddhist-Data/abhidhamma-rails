import re,sys,unicodedata
N=lambda s:unicodedata.normalize("NFC",s)
want=[N(w).lower() for w in sys.argv[1:]]
for l in open("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md",encoding="utf-8"):
    m=re.match(r"^\[([^\]]+)\] (.*)$",N(l.strip()))
    if not m: continue
    ks=[k.strip() for k in m.group(2).split(", ")]
    hit=[k for k in ks if k.lower() in want]
    if hit: print(m.group(1), hit)
