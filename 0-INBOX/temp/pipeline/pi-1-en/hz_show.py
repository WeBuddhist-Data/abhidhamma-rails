"""Show aligned Pāli/English non-empty lines. usage: hz_show.py <part-name> [start] [count] | hz_show.py grep <regex-pali> [regex-en] [max]"""
import sys, re, os
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters"
E = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\english\pi-1-english-plain-zeroshot_split_chapters"
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def pairs(part):
    return list(zip(lines(os.path.join(P, part + ".md")), lines(os.path.join(E, part + ".md"))))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "grep":
        rp = re.compile(a[1]); re_ = re.compile(a[2]) if len(a) > 2 and a[2] else None
        mx = int(a[3]) if len(a) > 3 else 40
        n = 0
        for part in PARTS:
            for i, (p, e) in enumerate(pairs(part)):
                if rp.search(p) and (re_ is None or re_.search(e)):
                    n += 1
                    if n <= mx:
                        print(f"== {part}:{i}\nP: {p}\nE: {e}")
        print("total", n)
    else:
        part = [x for x in PARTS if x.startswith(a[0])][0]
        s = int(a[1]) if len(a) > 1 else 0
        c = int(a[2]) if len(a) > 2 else 20
        for i, (p, e) in enumerate(pairs(part)[s:s + c], s):
            print(f"[{i}] P: {p}\n     E: {e}")
