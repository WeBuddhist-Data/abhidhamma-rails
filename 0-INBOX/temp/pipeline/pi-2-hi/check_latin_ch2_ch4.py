# -*- coding: utf-8 -*-
"""Helper: Latin-script words outside [...] brackets, CR, double blank lines, 'seed' words (chapters 2 and 4)."""
import re, sys
D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters"
for name in sys.argv[1:]:
    raw = open(f"{D}\\{name}", encoding="utf-8", newline="").read()
    bad = []
    for n, line in enumerate(raw.split("\n"), 1):
        body = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
        body = re.sub(r"\[[^\]]*\]", "", body)
        if re.search(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]", body):
            bad.append(n)
    print(name, "latin-outside-brackets lines:", bad[:10], "| CR:", "\r" in raw, "| double blank:", "\n\n\n" in raw,
          "| seed:", bool(re.search(r"seed", raw, re.I)))
