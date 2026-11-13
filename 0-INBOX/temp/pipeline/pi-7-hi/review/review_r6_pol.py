import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *
ITEMS = r"(?:āsav|saññojan|ganth|nīvaraṇ|parāmās|ogh|yog)"
res = collections.Counter(); out = []
for fi, f in enumerate(FILES):
    for r in pairs(f):
        p = re.sub(r"\{[^}]*\}", "", IDRE.sub("", r["p"])).lower()
        h = IDRE.sub("", r["h"])
        tag = f"{fi}|{r['id']}|k{r['k']}"
        # negated items: no+item, "ceva no ca item", a+item (anāsava etc.)
        pn = len(re.findall(r"\bno" + ITEMS, p)) + len(re.findall(r"no ca " + ITEMS, p)) + len(re.findall(r"\ba(?:n)?" + ITEMS + r"(?:iy|aniy)?", p)) + len(re.findall(r"\baparāmaṭṭh", p))
        hn = len(re.findall(r"न होने वाल|न बनने वाल", h))
        # sampayutta / vippayutta with items
        ps = len(re.findall(ITEMS + r"\w*sampayutt", p)) - len(re.findall(r"vippayutt" , "")); pv = len(re.findall(ITEMS + r"\w*vippayutt|diṭṭhigatavippayutt", p))
        hs = len(re.findall(r"से जुड़", h)); hv = len(re.findall(r"से अलग", h))
        # bare "sampayuttak" (associated) -> जुड़े हुए
        pb = len(re.findall(r"(?<![a-zāīūṃṅñṭḍṇḷ])sampayuttak", p))
        hb = len(re.findall(r"जुड़े हुए|जुड़ा हुआ|जुड़ी हुई", h))
        for name, a, b in (("neg", pn, hn), ("samp", ps, hs), ("vipp", pv, hv), ("bareassoc", pb, hb)):
            if a != b:
                res[name] += 1; out.append((name, tag, a, b))
print(res)
for o in out:
    print(o)
