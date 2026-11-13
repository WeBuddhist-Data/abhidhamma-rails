import sys, re, os
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
out = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review"
for n in range(7, 12):
    f = "7-%02d-anusayayamaka.md" % n
    P = [l.rstrip("\n") for l in open(os.path.join(base, "pali", "pi-6_split_chapters", f), encoding="utf-8")]
    H = [l.rstrip("\n") for l in open(os.path.join(base, "hindi", "pi-6-hindi-plain-rails_split_chapters", f), encoding="utf-8")]
    Pn = [l for l in P if l.strip()]
    Hn = [l for l in H if l.strip()]
    msgs = []
    if len(Pn) != len(Hn):
        msgs.append("COUNT MISMATCH %d %d" % (len(Pn), len(Hn)))
    # blank line structure
    for i, (a, b) in enumerate(zip(P, H)):
        if bool(a.strip()) != bool(b.strip()):
            msgs.append("blank mismatch raw line %d" % (i + 1))
    for i in range(len(H) - 1):
        if not H[i].strip() and not H[i + 1].strip():
            msgs.append("double blank at raw line %d" % (i + 1))
    with open(os.path.join(out, "review_r5_il_%02d.txt" % n), "w", encoding="utf-8") as o:
        for i, (a, b) in enumerate(zip(Pn, Hn)):
            ida = re.search(r"\^[\w-]+\s*$", a)
            idb = re.search(r"\^[\w-]+\s*$", b)
            if (ida and ida.group().strip()) != (idb and idb.group().strip()):
                msgs.append("ID mismatch line %d: %s / %s" % (i + 1, ida and ida.group(), idb and idb.group()))
            o.write("[%d] P: %s\n[%d] H: %s\n\n" % (i + 1, a, i + 1, b))
    print(f, len(Pn), len(Hn), msgs[:20])
