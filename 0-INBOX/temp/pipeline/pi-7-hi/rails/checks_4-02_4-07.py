"""Extra brief checks for 4-02..4-07 outputs: double blank lines, CR, Latin outside brackets, ':-', '…pe…',
ASCII quotes, dash totals, and identical-Pāli-line -> identical-Hindi consistency (no files written)."""
import collections
import re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]
pairs = collections.defaultdict(set)
for f in FILES:
    t = open(ROOT + r"\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\\" + f, encoding="utf-8",
             newline="").read()
    p = open(ROOT + r"\AI_translation\pali\pi-7_split_chapters\\" + f, encoding="utf-8").read()
    nob = re.sub(r"\[[^\]]*\]", "", re.sub(r"\^[0-9A-Za-z-]+", "", t))
    latin = re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", nob)
    print(f, "| double blank:", "\n\n\n" in t, "| CR:", "\r" in t, "| ':-':", ":-" in t, "| pe:", "pe…" in t,
          "| ascii quote:", '"' in t, "| latin:", collections.Counter(latin).most_common(5),
          "| dashes hi/pi:", t.count("–") + t.count("—"), p.count("–") + p.count("—"),
          "| ।। :", "।।" in t, "| '!!':", "!!" in t)
    pl = [x for x in p.split("\n") if x.strip()]
    hl = [x for x in t.split("\n") if x.strip()]
    for a, b in zip(pl, hl):
        a = re.sub(r" \^[0-9A-Za-z-]+$", "", a)
        b = re.sub(r" \^[0-9A-Za-z-]+$", "", b)
        if not a.startswith("#"):
            pairs[a].add(b)
bad = {k: v for k, v in pairs.items() if len(v) > 1}
print("identical Pāli lines with differing Hindi:", len(bad))
for k, v in list(bad.items())[:5]:
    print(" P:", k)
    for x in v:
        print("   H:", x)
