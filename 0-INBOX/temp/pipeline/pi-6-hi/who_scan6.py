"""WHO-phrase scan: answer sentences "<WHO> tesaṃ/tāsaṃ/tattha/tassa … X V" are grouped by the Pāli WHO; the Hindi
WHO is the prefix of the aligned Hindi sentence up to the last «में»/«समय» before the main process verb (the same
extraction harmonise_hi.py B9 uses). Groups whose Hindi WHO differs are reported (exact strings).
Imported by find_divergences_hi.py (section a4); alone: python -I -X utf8 who_scan6.py [--bak]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

SP = re.compile(r"(?<=[.?])\s+(?=[A-ZĀĪŪṬḌṆÑṄa-zāīūṭḍṇñṅ(])")
SH = re.compile(r"(?<=[।?])\s+")
COR = re.compile(r"^(.*)\s+(tesaṃ|tāsaṃ|tattha|tassa)\s+(?!cittassa)")  # greedy: the correlative right before the subject
E = r"(?![ऀ-ॿ])"
VERB = re.compile(r" (उत्पन्न|समाप्त) (भी )?(नहीं )?(होता|होतीं|होती|होते|हुआ|हुईं|हुई|हुए|होगा|होगी|होंगे|होंगी|हो चुका|हो चुकी|हो चुके)" + E)
REL_AFTER = re.compile(r",\s*(उस|उन|उनमें|वे|जिस)" + E)


def who_hi(s):
    m = None
    for mm in VERB.finditer(s):
        if REL_AFTER.match(s, mm.end()):
            continue
        m = mm
        break
    if not m:
        return None
    ends = [x.end() for x in re.finditer(r"(में|समय)(?=[ ,]|$)", s[:m.start()])]
    return s[:ends[-1]] if ends else None


def scan():
    grp = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in C.PARTS:
        if part.startswith(("preamble", "1-", "7-")):
            continue
        for p, h in C.pairs(part):
            if p.startswith("#"):
                continue
            ps = [s for s in SP.split(C.norm(p)) if s]
            hs = [s for s in SH.split(C.norm(h)) if s]
            if len(ps) != len(hs):
                continue
            for a, b in zip(ps, hs):
                if "?" in a or "…" in a or "…" in b:
                    continue
                m = COR.match(a.split(", no ca")[0])
                if not m or len(m.group(1)) < 6 or m.group(1).lower().startswith(("yassa ", "yattha", "no ca")):
                    continue
                w = who_hi(b)
                if not w:
                    continue
                k = re.sub(r"\s+(tesaṃ|tāsaṃ)$", "", m.group(1))
                k = k[0].upper() + k[1:]
                grp[k][w[0].upper() + w[1:]].append(C.short(part))
    out, n = [], 0
    for who, d in sorted(grp.items(), key=lambda kv: -sum(len(v) for v in kv[1].values())):
        if len(d) < 2:
            continue
        n += 1
        out.append(f"### {who}")
        for f, ps in sorted(d.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- [{len(ps)}] {', '.join(sorted(set(ps)))} :: {f[:400]}")
        out.append("")
    return out, n


if __name__ == "__main__":
    if "--bak" in sys.argv:
        C.CUR["hdir"] = C.BAK
    o, n = scan()
    print("\n".join(o))
    print("groups", n)
