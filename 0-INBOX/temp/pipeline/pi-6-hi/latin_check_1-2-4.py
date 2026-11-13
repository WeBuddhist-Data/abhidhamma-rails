"""Latin-script words outside variant brackets, double blank lines, CR, 'seed' words, ':-'."""
import re
import sys

t = open(sys.argv[1], encoding="utf-8", newline="").read()
bad = []
for n, line in enumerate(t.split("\n"), 1):
    body = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", line)
    body = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", body)
    words = re.findall(r"[A-Za-zĀāĪīŪūṬṭḌḍṆṇÑñṄṅṂṃḶḷ]+", body)
    if words:
        bad.append((n, words[:5]))
    if re.search(r"\b(seed|unseeded)\b", line, re.I):
        bad.append((n, "seed"))
print("latin/seed problems:", len(bad), bad[:8], "| CR:", "\r" in t, "| double blank:", "\n\n\n" in t,
      "| ':-':", ":-" in t)
