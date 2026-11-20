import re, sys, unicodedata
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\18-dhammahadayavibhango.md"
V = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\18-dhammahadayavibhango.md"
p = open(P, encoding="utf-8").read().split("\n")
v = open(V, encoding="utf-8").read().split("\n")
print("lines", len(p), len(v))
vt = "\n".join(v)
print("CR", "\r" in vt, "NFC", unicodedata.is_normalized("NFC", vt), "triple-nl", "\n\n\n" in vt)
print("ellipsis-dot", vt.count("…."), "emdash", vt.count("—"), "ascii-quote", vt.count('"'))
ids = 0
for i, (a, b) in enumerate(zip(p, v), 1):
    if bool(a.strip()) != bool(b.strip()):
        print("blank mismatch", i)
    ia = re.findall(r"\^[\d-]+$", a); ib = re.findall(r"\^[\d-]+$", b)
    if ia != ib:
        print("ID mismatch", i, ia, ib)
    if ia and not ia[0].endswith("-0"):
        ids += 1
    if a.count("–") != b.count("–"):
        print("dash", i, a.count("–"), b.count("–"))
    # end punctuation
    ea = re.sub(r"\s*\^[\d-]+$", "", a).rstrip()
    eb = re.sub(r"\s*\^[\d-]+$", "", b).rstrip()
    if ea and not ea.startswith("#"):
        if ea[-1] != eb[-1]:
            print("endpunct", i, repr(ea[-3:]), repr(eb[-3:]))
    # question count
    if ea.count("?") != eb.count("?"):
        print("qcount", i, ea.count("?"), eb.count("?"))
    # ellipsis count
    ca = ea.count("…pe…") + ea.count("…") - 2 * ea.count("…pe…")
    cb = eb.count("…")
    if ca != cb:
        print("ellipsis", i, ca, cb)
    # siyā vs đôi khi
    sa = len(re.findall(r"\bsiyā\b", ea)); sb = eb.count("đôi khi")
    if sa != sb:
        print("siya", i, sa, sb)
    # na vattabb
    na = len(re.findall(r"vattabb", ea)); nb = eb.count("không nên nói")
    if na != nb:
        print("navattabba", i, na, nb)
    # latin words in vi (outside brackets)
    s = re.sub(r"\[[^\]]*\]", "", eb)
    lat = re.findall(r"[a-zA-Z]*[āīūṃṅñṭḍṇḷ][a-zA-Zāīūṃṅñṭḍṇḷ]*", s)
    if lat:
        print("latin", i, lat)
print("content segments", ids)
