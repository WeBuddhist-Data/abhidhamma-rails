import re
import pathlib
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
H = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"
LAT = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")
for f in ["1-02-vedanattika.md", "1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md"]:
    t = (H / f).read_text(encoding="utf-8")
    bad = []
    for i, l in enumerate(t.splitlines(), 1):
        body = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l)
        body = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", body)
        if "??" in body or LAT.search(body) or "—" in body or ":-" in body:
            bad.append((i, (LAT.search(body) or re.search(r"\?\?|—|:-", body)).group(0)))
    print(f, "CR" if "\r" in t else "", "DBL" if "\n\n\n" in t else "", "bad:", bad[:10])
