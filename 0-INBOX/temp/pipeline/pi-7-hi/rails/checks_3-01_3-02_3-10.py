"""Extra checks for 3-01, 3-02, 3-10: double blank lines, CR, Latin outside [..] brackets, ⟦ markers, em/en dashes."""
import re, os

D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters"
for f in ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]:
    raw = open(os.path.join(D, f), "rb").read()
    t = raw.decode("utf-8")
    bad = []
    if b"\r" in raw:
        bad.append("CR")
    if "\n\n\n" in t:
        bad.append("double blank")
    if "⟦" in t:
        bad.append("unknown marker")
    lat = []
    for i, ln in enumerate(t.split("\n"), 1):
        s = re.sub(r"\[[^\]]*\]", "", ln)
        s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
        w = re.findall(r"[A-Za-zĀāĪīŪūṂṃÑñṬṭḌḍṆṇḶḷ]{2,}", s)
        if w:
            lat.append((i, w[:4]))
    print(f, "issues:", bad or "none", "| latin lines:", len(lat), lat[:5], "| em/en dash:", t.count("—"), t.count("–"))
