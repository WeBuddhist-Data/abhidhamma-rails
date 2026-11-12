import re, sys
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
CH = ["12-jhanavibhango", "13-appamannavibhango", "15-patisambhidavibhango", "11-maggangavibhango"]

def load(p):
    with open(p, encoding="utf-8") as f:
        raw = f.read()
    return raw

def lines(raw):
    return [l for l in raw.split("\n") if l.strip()]

idre = re.compile(r"\^([0-9a-z\-]+)\s*$")
latin = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")

def strip_brackets(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = re.sub(r"\([^)]*\)", "", s)
    return s

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    for ch in CH:
        pr = load(f"{BASE}\\pali\\pi-2_split_chapters\\{ch}.md")
        hr = load(f"{BASE}\\hindi\\pi-2-hindi-plain-rails_split_chapters\\{ch}.md")
        P, H = lines(pr), lines(hr)
        print(f"=== {ch}: pali {len(P)} hindi {len(H)}")
        if "\n\n\n" in hr.replace("\r", ""):
            print("  DOUBLE BLANK in hindi")
        for i, (p, h) in enumerate(zip(P, H), 1):
            iss = []
            mp, mh = idre.search(p), idre.search(h)
            if (mp and mp.group(1)) != (mh and mh.group(1)):
                iss.append(f"ID {mp and mp.group(1)} vs {mh and mh.group(1)}")
            pb = idre.sub("", p).strip(); hb = idre.sub("", h).strip()
            dp = pb.count("–") + pb.count("—"); dh = hb.count("–") + hb.count("—")
            if dp != dh:
                iss.append(f"dash {dp}/{dh}")
            if "—" in hb:
                iss.append("emdash")
            if '"' in hb or "«" in hb or "»" in hb or "'" in hb:
                iss.append("straight/guillemet quote")
            if hb.count("“") != hb.count("”"):
                iss.append("unbalanced quotes")
            pq = pb.count('"') // 2 + pb.count("“")
            hq = hb.count("“")
            if pq != hq:
                iss.append(f"quotes {pq}/{hq}")
            if not hb.startswith("#"):
                if not re.search(r"[।?]\s*”?$|[।?]”$", hb):
                    iss.append("end:" + hb[-6:])
            lat = latin.findall(strip_brackets(hb))
            if lat:
                iss.append("latin:" + ",".join(lat[:5]))
            pd = re.findall(r"\d+", pb); hd = re.findall(r"[\d०-९]+", hb)
            if pd != hd:
                iss.append(f"digits {pd}/{hd}")
            pe_p = len(re.findall(r"\.\.\.|…", pb)); pe_h = len(re.findall(r"\.\.\.|…", hb))
            if pe_p != pe_h:
                iss.append(f"ellipsis {pe_p}/{pe_h}")
            if "  " in hb:
                iss.append("double space")
            if iss:
                print(f"  L{i} {mp and mp.group(1)}: " + "; ".join(iss))

if __name__ == "__main__":
    main()
