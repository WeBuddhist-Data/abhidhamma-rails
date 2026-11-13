"""Extra checks for 5-05..5-12 Hindi: double blank lines, CR, Latin outside brackets, leftover '@@'."""
import os, re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
OUT = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]
for f in FILES:
    raw = open(os.path.join(OUT, f), "rb").read()
    txt = raw.decode("utf-8")
    probs = []
    if b"\r" in raw:
        probs.append("CR")
    if "\n\n\n" in txt:
        probs.append("double blank")
    if "@@" in txt:
        probs.append("@@")
    for i, ln in enumerate(txt.split("\n"), 1):
        body = re.sub(r" \^[0-9A-Za-z-]+$", "", ln)
        body = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद)[^\]]*\]", "", body)
        lat = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}", body)
        if lat:
            probs.append(f"latin L{i}: {lat[:4]}")
        if re.search(r"[—]|:-", body):
            probs.append(f"dash L{i}")
    print(f, "OK" if not probs else probs[:12])
