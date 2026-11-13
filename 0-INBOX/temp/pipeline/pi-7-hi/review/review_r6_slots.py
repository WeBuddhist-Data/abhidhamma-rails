import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *
from review_r6_cond import pali_conds, hindi_conds

REL_P = re.compile(r"^(?P<x>.+?) dhamm(?:aṃ|e) (?P<v>paṭicca|paccayā|saṃsaṭṭho|saṃsaṭṭhā) (?P<y>.+?) dhamm(?:o|ā) uppajj\w+ (?P<c>\S+?)[\s.…]")
PAN_P = re.compile(r"^(?P<x>.+?) dhamm(?:o|ā) (?P<y>.+?) dhammassa (?P<c>\w+?)paccayena paccayo")
VH = {"paṭicca": " पर निर्भर होकर ", "paccayā": " के कारण ", "saṃsaṭṭho": " से घुल-मिलकर ", "saṃsaṭṭhā": " से घुल-मिलकर "}

def main_clause(t):
    return re.split(r" – ", IDRE.sub("", t), maxsplit=1)[0] + " "

def norm_y_h(y):
    return y

table = collections.defaultdict(lambda: collections.defaultdict(list))
problems = []
nrel = 0
for fi, f in enumerate(FILES):
    for r in pairs(f):
        p = main_clause(r["p"]); h = main_clause(r["h"])
        tag = f"{fi}|{r['id']}|k{r['k']}"
        m = REL_P.match(p)
        if m:
            nrel += 1
            v = m.group("v"); sep = VH[v]
            if sep not in h:
                problems.append((tag, "verb marker missing", p[:120], h[:160])); continue
            hx, rest = h.split(sep, 1)
            mm = re.match(r"(?P<y>.+?) (?:" + "|".join(["मूल", "विषय", "प्रधानता", "पूर्ण निकटता", "निकटता", "सह-उत्पत्ति", "परस्पर", "प्रबल आश्रय", "आश्रय", "पूर्व-उत्पत्ति", "पश्चात्-उत्पत्ति", "पुनरावृत्ति", "कर्म-फल", "कर्म", "आहार", "क्षमता", "ध्यान", "मार्ग", "जुड़ाव", "अलगाव", "अनुपस्थिति", "उपस्थिति", "अविलीनता", "विलीनता"]) + r")-कारण", rest)
            if not mm:
                problems.append((tag, "no cond after y", p[:120], h[:160])); continue
            hy = mm.group("y")
            table["X:" + m.group("x").lower()][hx].append(tag)
            table["Y:" + m.group("y").lower()][hy].append(tag)
            # plural agreement: uppajjanti <-> होती हैं
            pl_p = "uppajjanti" in p
            pl_h = bool(re.search(r"उत्पन्न होती हैं|उत्पन्न होते हैं", h))
            if pl_p != pl_h:
                problems.append((tag, "verb number", p[-60:], h[-80:]))
            continue
        m = PAN_P.match(p)
        if m:
            nrel += 1
            mh = re.match(r"^(?P<x>.+?परिघटना(?:एँ)?), (?P<y>.+?) के लिए (?P<c>.+?) के रूप में कारण (?P<v>होती हैं|होती है|होते हैं|होता है)", h)
            if not mh:
                problems.append((tag, "panha H parse", p[:120], h[:200])); continue
            table["PX:" + m.group("x").lower()][mh.group("x")].append(tag)
            table["PY:" + m.group("y").lower()][mh.group("y")].append(tag)
            pl_p = m.group(0).find("dhammā ") >= 0
            pl_h = mh.group("v") == "होती हैं"
            if pl_p != pl_h:
                problems.append((tag, "panha verb number", m.group(0)[:80], mh.group(0)[-60:]))
for pr in problems:
    print(" | ".join(pr))
print("relation lines:", nrel)
out = []
for k in sorted(table):
    d = table[k]
    out.append(f"{k}  [{sum(len(v) for v in d.values())}]")
    for hk, tags in sorted(d.items(), key=lambda x: -len(x[1])):
        out.append(f"     {len(tags):4d}  {hk}   e.g. {tags[0]}" + ("" if len(d) == 1 else "  ALL:" + ",".join(tags[:12])))
open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\r6_slots.txt", "w", encoding="utf-8").write("\n".join(out))
print("distinct pali slots", len(table), "multi-rendered", sum(1 for k in table if len(table[k]) > 1))


