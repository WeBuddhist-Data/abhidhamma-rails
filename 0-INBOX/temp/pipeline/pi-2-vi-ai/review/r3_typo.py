import re, unicodedata
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
for ch in ("6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md"):
    P = open(base + r"\pali\pi-2_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
    raw = open(base + r"\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf-8").read()
    V = raw.split("\n")
    print("==", ch, "NFC" if unicodedata.is_normalized("NFC", raw) else "NOT NFC", "CR" if "\r" in raw else "noCR", "double-blank" if "\n\n\n" in raw else "")
    for i, (p, v) in enumerate(zip(P, V)):
        vs = re.sub(r"\s*\^[\w-]+\s*$", "", v)
        if "….":
            if "…." in vs: print(i + 1, "'….'")
        if '"' in vs: print(i + 1, "straight quote")
        # Latin-only words outside brackets
        nob = re.sub(r"\[[^\]]*\]", "", vs)
        lat = [w for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", nob) if re.search(r"[āīūṃṅñṭḍṇḷ]", w)]
        if lat: print(i + 1, "pali-latin:", lat[:5])
        # question marks count
        if p.count("?") != vs.count("?"): print(i + 1, "? count", p.count("?"), vs.count("?"))
        # quote balance
        if vs.count("“") != vs.count("”"): print(i + 1, "unbalanced “”", vs.count("“"), vs.count("”"))
        # pali quotes present vs absent
        pq = p.count('"')
        if pq and pq % 2: print(i + 1, "pali odd quotes", pq, "| vi “", vs.count("“"))
        if pq == 0 and "vuccati " in p and "“" not in vs and p.strip() and not p.startswith("#"):
            print(i + 1, "no quotes in pali (vuccati) and none in vi")
        if (vs.endswith(".") or vs.endswith("?") or vs.endswith("”") or vs.endswith("…") or vs.startswith("#") or not vs) is False:
            print(i + 1, "ending:", vs[-10:])
