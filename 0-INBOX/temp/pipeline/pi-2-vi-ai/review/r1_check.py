import re, sys, unicodedata
P = r"AI_translation\pali\pi-2_split_chapters\1-khandhavibhango.md"
V = r"AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\1-khandhavibhango.md"
pl = [l for l in open(P, encoding="utf-8").read().split("\n")]
vraw = open(V, encoding="utf-8").read()
vl = vraw.split("\n")
print("NFC:", unicodedata.is_normalized("NFC", vraw), "CR:", "\r" in vraw, "double blank:", "\n\n\n" in vraw)
print("'….' count:", vraw.count("…."), "'...' count:", vraw.count("..."), "em dash:", vraw.count("—"))
pn = [l for l in pl if l.strip()]
vn = [l for l in vl if l.strip()]
print("nonempty lines", len(pn), len(vn))
def c(s, pat):
    return len(re.findall(pat, s))
for i, (p, v) in enumerate(zip(pn, vn)):
    issues = []
    # siya vs doi khi
    a, b = c(p, r"\bsiyā\b"), c(v, r"đôi khi")
    if a != b: issues.append(f"siyā {a} / đôi khi {b}")
    a, b = c(p, r"vattabb"), c(v, r"không nên nói")
    if a != b: issues.append(f"vattabba {a} / không nên nói {b}")
    a, b = p.count("…pe…"), v.count("…")
    if a != b: issues.append(f"pe {a} / … {b}")
    a, b = p.count("?"), v.count("?")
    if a != b: issues.append(f"? {a} / {b}")
    a, b = c(p, r"(?i)\batthi\b"), c(v, r"(?i)\bcó loại\b")
    if a != b and "atthi" in p: issues.append(f"atthi {a} / có loại {b}")
    a, b = p.count('"') // 2, v.count("“")
    if a != b: issues.append(f'quotes {a} / {b}')
    # Latin words with Pali diacritics outside brackets
    vv = re.sub(r"\[[^\]]*\]", "", v)
    lat = re.findall(r"\b\w*[āīūṃṅñṭḍṇḷ]\w*\b", vv)
    if lat: issues.append(f"pali? {lat[:5]}")
    pid = re.findall(r"\^\S+$", p); vid = re.findall(r"\^\S+$", v)
    if pid != vid: issues.append(f"id {pid} {vid}")
    if issues:
        print(i + 1, pid or "", "; ".join(issues))
