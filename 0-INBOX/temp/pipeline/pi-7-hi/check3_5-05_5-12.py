"""Consistency counts per line (Pāli frame words vs Hindi frame words) and followers of परिघटना."""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]
PAIRS = [(r"\bpaṭicca\b", "पर निर्भर होकर"), (r"\bpaccayā\b", "के कारण"), (r"\buppajjat?i\b|\buppajjanti\b", "उत्पन्न होती"),
         (r"paccayena paccayo", "के रूप में कारण होती"), (r"…pe…|…", "…"), (r"\(", "("),
         (r"[Hh]etupaccayā\b", "मूल-कारण से")]
fol = collections.Counter()
for f in FILES:
    pl = S.nonempty((S.PALI_DIR / f).read_text(encoding="utf-8"))
    hl = S.nonempty((S.HI_DIR / f).read_text(encoding="utf-8"))
    for n, (p, h) in enumerate(zip(pl, hl), 1):
        if p.startswith("#"):
            continue
        for rx, hw in PAIRS:
            a, b = len(re.findall(rx, p)), h.count(hw)
            if a != b:
                print(f"{f} {n}: {rx!r} {a} vs {hw!r} {b}")
        for m in re.finditer(r"परिघटना(?:एँ)?([ ,।…?;)]+\S*)", h):
            fol[m.group(1).strip()] += 1
print(fol.most_common())
