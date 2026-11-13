import re, os
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
N = {"kāma": "इंद्रिय-सुखों के लोक", "rūpa": "सूक्ष्म भौतिक लोक", "arūpa": "अभौतिक लोक"}

def lines(path):
    return [l.rstrip("\n") for l in open(path, encoding="utf-8") if l.strip()]

def realms(s, case):
    # returns (neg, [realms]) for a chunk like "Na kāmadhātuyā na arūpadhātuyā"
    toks = re.findall(r"(?i)(na )?(kāma|rūpa|arūpa)dhātu" + case, s)
    neg = any(t[0] for t in toks)
    return neg, [t[1].lower() for t in toks]

def expect(neg, rs, tail):
    if not neg:
        assert len(rs) == 1
        return N[rs[0]] + tail[0]
    if len(rs) == 1:
        return N[rs[0]] + " से भिन्न लोक" + tail[1]
    return N[rs[0]] + " और " + N[rs[1]] + " से भिन्न लोक" + tail[1]

rep = []
cnt = 0
for f, start in (("7-10-anusayayamaka.md", "dhātupucchāvāro"), ("7-11-anusayayamaka.md", "")):
    P = lines(os.path.join(base, "pali", "pi-6_split_chapters", f))
    H = lines(os.path.join(base, "hindi", "pi-6-hindi-plain-rails_split_chapters", f))
    on = start == ""
    for i, (p, h) in enumerate(zip(P, H), 1):
        if start and start in p:
            on = True
            continue
        if not on or p.startswith("#"):
            continue
        # each Pali sentence begins with a cuti phrase
        psents = re.findall(r"((?:Na |na )?(?:Kāma|Rūpa|Arūpa|kāma|rūpa|arūpa)dhātuyā(?: na (?:kāma|rūpa|arūpa)dhātuyā)? cutassa (?:(?:na )?(?:kāma|rūpa|arūpa)dhātu(?:ṃ|yā) ?){1,2})", p)
        if not psents:
            continue
        pos = 0
        for ps in psents:
            cnt += 1
            cut, upp = ps.split(" cutassa ")
            cneg, crs = realms(cut, "yā")
            uneg, urs = realms(upp, "(?:ṃ|yā)")
            ec = expect(cneg, crs, (" से मरकर", " से मरकर"))
            eu = expect(uneg, urs, (" में", " में"))
            target = ec + " " + eu
            j = h.find(target, pos)
            if j < 0:
                rep.append((f[:4], i, ps, target))
            else:
                pos = j + len(target)
        # numbers per Pali sentence are checked in review_r5_check.py
for r in rep:
    print(*r, sep=" | ")
print("dhatu chains checked", cnt, "flags", len(rep))
