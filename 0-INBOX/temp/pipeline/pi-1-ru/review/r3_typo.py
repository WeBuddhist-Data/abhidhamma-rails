import re, os
B = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-1-russian-plain-rails_split_chapters"
for f in ["3-01-rupakandam.md", "3-02-rupakandam.md", "3-03-rupakandam.md"]:
    t = open(os.path.join(B, f), encoding="utf-8").read()
    print(f, "CR:", "\r" in t, "double blank:", "\n\n\n" in t, "em:", t.count("—"), "quotes\":", t.count('"'))
    for i, l in enumerate(t.split("\n")):
        if re.search(r"\bли\b", l):
            print(" li", i + 1)
        s = re.sub(r"\[[^\]]*\]", "", l)
        s = re.sub(r"\^[\w-]+", "", s)
        lat = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", s)
        if lat:
            print(" latin", i + 1, lat[:5])
        if l.strip() and not l.startswith("#"):
            body = re.sub(r"\s*\^[\w-]+\s*$", "", l).rstrip()
            if body and body[-1] not in ".?–:":
                print(" end", i + 1, repr(body[-20:]))
        if re.search(r"(\b[а-яё]{3,}\b) \1\b", l, re.I):
            print(" rep", i + 1, re.search(r"(\b[а-яё]{3,}\b) \1\b", l, re.I).group(0))
        if "…" in l and re.search(r"\.\.\.", l):
            print(" dots", i + 1)
