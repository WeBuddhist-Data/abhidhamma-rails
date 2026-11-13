import re, sys
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters"
for i in range(1, 6):
    f = f"{base}\\7-0{i}-anusayayamaka.md"
    b = open(f, "rb").read()
    t = b.decode("utf-8")
    cr = b.count(b"\r")
    dbl = t.count("\n\n\n")
    latin = []
    for ln in t.splitlines():
        ln2 = re.sub(r"\^[0-9A-Za-z-]+", "", ln)
        ln2 = re.sub(r"\[[^\]]*\]", "", ln2)
        latin += re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+", ln2)
    print(f[-22:], "CR", cr, "double-blank", dbl, "latin", sorted(set(latin))[:10], "colon-dash", t.count(":-"))
