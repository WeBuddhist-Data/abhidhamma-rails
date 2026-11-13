import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r4_check import PB, HB, FILES, nonempty, split_p, split_h, seq, P_TEND, H_TEND, p_neg, h_neg

DEV = r"\u0900-\u097F"
issues = []
stats = collections.Counter()


def strip_id(s):
    return re.sub(r"\s*\^[\d-]+\s*$", "", s)


for f in FILES:
    P = nonempty(f"{PB}\\{f}")
    H = nonempty(f"{HB}\\{f}")
    for k, ((pl, p), (hl, h)) in enumerate(zip(P, H)):
        n = k + 1
        if p.startswith("#"):
            continue
        sp, sh = split_p(strip_id(p)), split_h(strip_id(h))
        if len(sp) != len(sh):
            continue
        for j, (a, b) in enumerate(zip(sp, sh)):
            # verb lexeme counts
            pa = len(re.findall(r"\banuse(?:t|nt)|\bnānuse|\banusant", a))
            ha = len(re.findall(r"सोई", b))
            ps = len(re.findall(r"sānusay", a)); hs = len(re.findall(r"प्रवृत्ति(?:यों)? वाल", b))
            pn = len(re.findall(r"niranusay", a)); hn = len(re.findall(r"मुक्त", b))
            pp = len(re.findall(r"pajah", a)); hp = len(re.findall(r"छोड़(?!कर)", b)) - len(re.findall(r"साथ रहने", b)) * 0
            pt = len(re.findall(r"ṭhapetvā", a)); ht = len(re.findall(r"छोड़कर", b))
            for name, x, y in (("anuseti", pa, ha), ("sanusaya", ps, hs), ("niranusaya", pn, hn), ("pajahati", pp, hp), ("thapetva", pt, ht)):
                if x != y:
                    issues.append((f, n, name, f"s{j+1} P={x} H={y}", a[:120], b[:160]))
            # question frames
            q = a.rstrip().endswith("?")
            if q:
                fp = []
                if re.search(r"\byassa\b", a, re.I): fp.append("person-loc")
                if re.search(r"\byo\b", a, re.I): fp.append("person-nom")
                if re.search(r"\byattha\b", a, re.I): fp.append("place-loc")
                if re.search(r"\byato\b", a, re.I): fp.append("place-abl")
                fh = []
                if "जिस व्यक्ति में" in b: fh.append("person-loc")
                if "जो व्यक्ति" in b: fh.append("person-nom")
                if "जिस स्थान पर" in b: fh.append("place-pa")
                if "जिस स्थान से" in b: fh.append("place-se")
                stats[(f, tuple(fp), tuple(fh))] += 1
                if ("vā pana" in a) != b.startswith(("और ", "(ख) और ")) :
                    issues.append((f, n, "vapana", f"s{j+1}", a[:80], b[:80]))
            # no ca tattha/tato -> पर वहाँ
            if re.search(r"no ca (?:tattha|tato|so tato|tassa tattha|tesaṃ tattha|te tato)", a) and "वहाँ" not in b.split("पर ")[-1] if "पर " in b else False:
                issues.append((f, n, "noca-place", f"s{j+1}", a[:100], b[:100]))
            # agreement: anuseti family
            # split hindi by verb occurrences
            segs = re.split(r"(सोई (?:नहीं )?रहती(?:ं)?(?: हैं| है)?)", b)
            for idx in range(1, len(segs), 2):
                pre = segs[idx - 1]
                verb = segs[idx]
                # tendencies since previous verb
                names = seq(pre, H_TEND)
                cnt = len(names)
                if "…" in pre and cnt >= 2:
                    cnt -= pre.count("…")
                plural = verb.endswith("हैं") or verb.endswith("रहतीं")
                if cnt >= 2 and not plural:
                    issues.append((f, n, "agree-sg-for-pl", f"s{j+1}", verb, pre[-100:]))
                if cnt == 1 and plural:
                    issues.append((f, n, "agree-pl-for-sg", f"s{j+1}", verb, pre[-100:]))
            # plural persons
            ppl = len(re.findall(r"\b(?:sānusayā|niranusayā|pajahanti|nappajahanti)\b", a))
            hpl = len(re.findall(r"(?:वाले|मुक्त(?: भी| नहीं)? हैं|छोड़ते)", b.replace("फिर न लौटने वाले", "")))
            if ppl != hpl:
                issues.append((f, n, "person-number", f"s{j+1} P={ppl} H={hpl}", a[:120], b[:160]))

for key, v in sorted(stats.items()):
    print("FRAME", key, v)
c = collections.Counter(i[2] for i in issues)
print(c)
for i in issues:
    print(*i, sep=" | ")
