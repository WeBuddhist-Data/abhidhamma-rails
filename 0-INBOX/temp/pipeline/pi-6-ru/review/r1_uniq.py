import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review")
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PA = ["rūpakkhandh", "vedanākkhandh", "vadanākkhandh", "saññākkhandh", "saṅkhārakkhandh", "viññāṇakkhandh"]

def ptempl(s):
    t = re.sub(r"\^[\d-]+", "", s)
    for st in PA:
        t = re.sub(st + r"\w*", "A", t)
    t = re.sub(r"\b(na )?(n?uppajj\w+|nirujjh\w+|parijān\w+)", "V", t)
    return t.strip()

seen = set()
specs = sys.argv[1:]
for spec in specs:
    ch, start = spec.split(":")
    start = int(start)
    p = open(base + r"\pali\pi-6_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
    r = open(base + r"\russian\pi-6-russian-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
    for i, (a, b) in enumerate(zip(p, r)):
        if not a.strip():
            continue
        t = ptempl(a)
        if t in seen:
            continue
        seen.add(t)
        if i + 1 < start:
            continue
        if a.startswith("#"):
            continue
        print(f"{ch[:4]}:{i+1}P: {a}\n{ch[:4]}:{i+1}R: {b}")
