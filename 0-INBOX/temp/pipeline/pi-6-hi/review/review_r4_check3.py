import re, sys, collections

PB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
HB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters"
FILES = [f"7-0{i}-anusayayamaka.md" for i in range(1, 7)]


def nonempty(path):
    return [(i, l) for i, l in enumerate(open(path, encoding="utf-8").read().split("\n"), 1) if l.strip()]


def split_p(s):
    return [x for x in re.split(r"(?<=[.?])\s+", s) if x.strip()]


def split_h(s):
    return [x for x in re.split(r"(?<=[।?])\s+", s) if x.strip()]


def strip_id(s):
    return re.sub(r"\s*\^[\d-]+\s*$", "", s)


LAB = [("(Ka)", "(क)"), ("(Kha)", "(ख)"), ("(Ga)", "(ग)"), ("(Gha)", "(घ)"), ("(Ṅa)", "(ङ)"), ("(Ca)", "(च)")]
issues = []
for f in FILES:
    P = nonempty(f"{PB}\\{f}")
    H = nonempty(f"{HB}\\{f}")
    for k, ((pl, p), (hl, h)) in enumerate(zip(P, H)):
        n = k + 1
        for a, b in LAB:
            if p.count(a) + p.count(a.lower()) != h.count(b):
                issues.append((f, n, "LABEL", a))
        if p.startswith("#"):
            continue
        sp, sh = split_p(strip_id(p)), split_h(strip_id(h))
        if len(sp) != len(sh):
            continue
        for j, (a, b) in enumerate(zip(sp, sh)):
            if a.rstrip().endswith("?"):
                continue
            # 'both' construction
            cp = re.split(r",\s*no ca\b", a)
            ch = re.split(r",\s*पर ", b)
            if len(cp) != len(ch):
                issues.append((f, n, "CLAUSES", f"s{j+1} {len(cp)} {len(ch)}", a[:150], b[:200]))
            else:
                for x, y in zip(cp, ch):
                    pb = len(re.findall(r"\bca (?:anuse|nānuse|sānusay|niranusay|pajah|nappajah)|añca (?:pajah|nappajah)", x))
                    exp = pb if pb >= 2 else 0
                    hb2 = len(re.findall(r" भी(?= |।|$)", y))
                    if exp != hb2:
                        issues.append((f, n, "BHI", f"s{j+1} Pca={pb} Hbhi={hb2}", x[:150], y[:200]))
            # pronouns: plural vs singular
            pl_p = len(re.findall(r"\b(?:tesaṃ|te)\b", a))
            pl_h = len(re.findall(r"उनमें|(?<![\u0900-\u097F])वे(?![\u0900-\u097F])", b))
            sg_p = len(re.findall(r"\b(?:tassa|so)\b", a))
            sg_h = len(re.findall(r"उसमें|(?<![\u0900-\u097F])वह(?![\u0900-\u097F])", b))
            if (pl_p > 0 and sg_p == 0 and sg_h > 0) or (sg_p > 0 and pl_p == 0 and pl_h > 0):
                issues.append((f, n, "PRON", f"s{j+1} P pl={pl_p} sg={sg_p} H pl={pl_h} sg={sg_h}", a[:150], b[:200]))
c = collections.Counter(i[2] for i in issues)
print(c)
for i in issues:
    print(*i, sep=" | ")
