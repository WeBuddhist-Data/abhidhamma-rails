import sys, re
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
P = BASE + r"\pali\pi-6_split_chapters\\"
H = BASE + r"\hindi\pi-6-hindi-plain-rails_split_chapters\\"

def lines(path):
    with open(path, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if l.strip()]

def load(fn):
    return lines(P + fn), lines(H + fn)

if __name__ == "__main__":
    fn = sys.argv[1]
    a = int(sys.argv[2]); b = int(sys.argv[3])
    p, h = load(fn)
    for i in range(a - 1, min(b, len(p))):
        print(f"{i+1} P: {p[i]}")
        print(f"{i+1} H: {h[i]}")
