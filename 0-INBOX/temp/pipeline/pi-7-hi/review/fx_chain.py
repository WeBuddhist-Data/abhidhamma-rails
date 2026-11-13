"""Abbreviated condition chains: list every condition-only unit («…X-कारण के रूप में कारण <verb>») whose verb
differs from the agreement of the nearest preceding formula head («… परिघटना(एँ), … के लिए …-कारण के रूप में कारण
होती है/हैं»). Shows the previous unit's tail (Hindi + Pāli)."""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
out = open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\fx_out.txt", "w", encoding="utf-8")
VERB = r"(होती हैं|होते हैं|होता है|होती है)"
HEAD = re.compile(r"परिघटना(एँ)?, [^।–]*? के लिए [^\s।]+ के रूप में कारण (होती हैं|होती है)")
LINK = re.compile(r"^\s*([^\s…]+-कारण) के रूप में कारण " + VERB)
PLINK = re.compile(r"^\s*\w+paccayena paccayo")
cnt = collections.Counter()
for part in C.PARTS:
    head = None
    for i, (p, h) in enumerate(C.pairs(part)):
        if h.startswith("#"):
            head = None
            continue
        units = h.split("…")
        punits = re.split(r"…(?:pe…)?", p)
        plinks = sum(1 for u in punits if PLINK.match(u))
        hl = 0
        for j, u in enumerate(units):
            m = LINK.match(u)
            if m:
                hl += 1
                if head and m.group(2) != head:
                    prev = units[j - 1][-45:] if j else "<line start>"
                    ok = "KEEP?" if j and not re.search(VERB, units[j - 1]) and not HEAD.search(units[j - 1]) else "FIX"
                    cnt[(ok, m.group(2), head)] += 1
                    out.write(f"{part[:4]}:{i+1}\t{ok}\t{m.group(1)} {m.group(2)} -> {head}\tprev: {prev}\n")
            for hm in HEAD.finditer(u):
                head = hm.group(2)
        if hl != plinks:
            out.write(f"{part[:4]}:{i+1}\tCOUNT hindi links {hl} pali links {plinks}\n")
for k, v in cnt.most_common():
    print(k, v)
