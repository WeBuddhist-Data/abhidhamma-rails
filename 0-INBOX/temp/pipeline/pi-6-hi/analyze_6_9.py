r"""Helper for 6-01/6-02/9-01/9-02/9-03: list distinct line templates and answer prefixes."""
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
FILES = sys.argv[1:] or ["6-01-sankharayamaka.md", "6-02-sankharayamaka.md",
                         "9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md"]
ID_RE = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

ITEMS = r"(?:kāyasaṅkhāro|vacīsaṅkhāro|cittasaṅkhāro|kusalā dhammā|akusalā dhammā|abyākatā dhammā|kusalā ca dhammā|akusalā ca dhammā|abyākatā ca dhammā|kāyasaṅkhāro ca|vacīsaṅkhāro ca|cittasaṅkhāro ca)"
prefixes = Counter()
templates = Counter()
for f in FILES:
    for line in (PALI / f).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        t = ID_RE.sub("", line)
        for s in re.split(r"(?<=\.) ", t):
            m = re.match(rf"^(.*?) (tesaṃ tattha|tesaṃ|tattha) {ITEMS} ", s)
            if m and not s.startswith("("):
                prefixes[m.group(1)] += 1
        n = re.sub(r"\b(kāya|vacī|citta)saṅkhāro", "S", t)
        n = re.sub(r"\b(kusalā|akusalā|abyākatā)\b", "K", n)
        n = re.sub(r"\b(n|na )?(uppajj|nirujjh)\w*", "V", n)
        templates[n] += 1
mode = "t"
if mode == "t":
    Q = re.compile(r"^\((?:Ka|Kha)\) (yassa|yattha)( vā pana)?( yattha)? S V (tassa tattha|tassa|tattha) S V\?( (Āmantā|No|Natthi|V)\.)?$")
    Q2 = re.compile(r"^\((?:Ka|Kha)\) (yassa|yattha)( vā pana)?( yattha)? K dhammā V (tassa tattha|tassa|tattha) K dhammā V\?( (Āmantā|No|Natthi|V)\.)?$")
    A = re.compile(r"^.*? (tesaṃ tattha|tesaṃ|tattha) (S|K dhammā) V, no ca (tesaṃ tattha|tesaṃ|tattha) (S|K dhammā) V\. .*? (tesaṃ tattha|tesaṃ|tattha) (S ca|K ca dhammā) V (S ca|K ca dhammā) V\.$")
    for tpl, c in templates.items():
        if Q.match(tpl) or Q2.match(tpl) or A.match(tpl):
            continue
        print(c, "|", tpl)
if mode == "p":
    for p, c in sorted(prefixes.items()):
        print(c, "|", p)
