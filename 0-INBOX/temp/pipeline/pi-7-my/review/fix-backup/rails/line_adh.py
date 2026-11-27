"""Inspection helper (read only): line-level adherence. For every keyword of a segment, every Pāli LINE of the segment
holding the keyword as a word (case-insensitive) must hold the term's chunks (adherence_my.occurs) in the Burmese line
of the same number; --unexplained: every line miss must match one of the INF patterns (the same grammar forms as
classify_rules.py: plural «…ကြ…», negative «မျက်မှောက် မပြု», future participle, attributive before a person noun).
usage: line_adh.py <burmese dir> [--rows] [--show KW-REGEX BURMESE-REGEX] [--unexplained]   (run by regen_rails.sh)"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
tb = A.parse_termbase(ROOT / "AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md")
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = pathlib.Path(sys.argv[1])
def seglines(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8-sig")).splitlines():
            if not l.strip(): continue
            buf.append(l)
            m = A.ID.search(l)
            if m: out[m.group(1)] = buf; buf = []
    return out
P, B = seglines(PD), seglines(BD)
BR = re.compile(r"\[[^\]]*\]")
c = collections.Counter(); rows = []
for l in open(ROOT / "AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if not m or m.group(1) not in P: continue
    i = m.group(1)
    for kw in m.group(2).split(", "):
        terms = tb.get(kw.strip().lower())
        if not terms: continue
        rx = re.compile(r"(?<![^\W\d_])" + re.escape(kw.strip()) + r"(?![^\W\d_])", re.I)
        for k, (pl, bl) in enumerate(zip(P[i], B[i])):
            if rx.search(BR.sub("", pl)) and not any(A.occurs(t, bl) for t in terms):
                c[(kw, terms[0])] += 1; rows.append((i, k + 1, kw, terms[0]))
print("line misses", sum(c.values()))
for (kw, t), n in c.most_common(): print(f"{n:5d}\t{kw}\t{t}")
if "--rows" in sys.argv:
    for r in rows: print(*r, sep="\t")
if "--show" in sys.argv:
    kwx = re.compile(sys.argv[sys.argv.index("--show") + 1]); brx = re.compile(N(sys.argv[sys.argv.index("--show") + 2]))
    cc = collections.Counter()
    for i, k, kw, t in rows:
        if kwx.fullmatch(kw):
            cc.update(set(m.group(0) for m in brx.finditer(B[i][k - 1])) or {"NONE " + i})
    for x, n in cc.most_common(): print(f"   {n:4d} {x}")
INF = [(r"(?i)nirujjhissant\w*|uppajjissant\w*|bhāvessanti|parijānissanti|n?appajahissanti|pajahissanti|sacchikariss\w*|sacchikaritth\w*|sacchikaro\w*",
        r"ကြလိမ့်မည်|ကြ[၊။ ]|ကြ$|မျက်မှောက် မပြု|ခဲ့ကြ"),
       (r"(?i)uppajjissati", r"ဖြစ်ပေါ်မည့်သူ|ဖြစ်ပေါ်မည့် ကာမဘုံ၌ ရှိသူ"),   # review fix B2: the beings after the participle
       (r"(?i)upapajjantānaṃ|upapajjantīnaṃ|uppajjantīnaṃ|uppajjantānaṃ", r"ပြန်လည် ဖြစ်ပေါ်ဆဲ (?!သူ)\S"),
       (r"(?i)cavantānaṃ|cavantīnaṃ", r"စုတေဆဲ (?:အခြား|ထို)(?:သူ|မိန်းမ)"),   # review fix B4: «စုတေဆဲ ထိုသူတို့» (attributive before ထိုသူ)
       (r"(?i)pañcavokārānaṃ|kāmāvacarānaṃ", r"ရှိသော အခြားသူ"),
       (r"(?i)pacchimabhavikānaṃ", r"နောက်ဆုံး ဘဝ ရှိသော (မိန်းမ|ယောက်ျား)|ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိ"),
       (r"(?i)itaresaṃ", r"အခြား (မိန်းမ|ယောက်ျား)"),
       (r"(?i)a?n?abhisametāvīnaṃ", r"သိမြင်(ပြီး|ရသေး)သော (ပြန်လည်|စုတေ)")]
if "--unexplained" in sys.argv:
    left = collections.Counter()
    for i, k, kw, t in rows:
        if not any(re.fullmatch(a, kw) and re.search(b, B[i][k - 1]) for a, b in INF):
            left[(kw, t)] += 1
            print("UNEXPLAINED", i, k, kw, t, B[i][k - 1][:300])
    print("unexplained", sum(left.values()), dict(left))
