"""Part B helper: compare answer-type sequences per block, Pali vs Tinh Su (console only)."""
import sys, re, unicodedata, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import PDIR, FILES, load
TS = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md"
show = int(sys.argv[1]) if len(sys.argv) > 1 else 0
files = sys.argv[2].split(",") if len(sys.argv) > 2 else FILES


def blocks_text(text):
    d = {}
    for b in re.split(r"\n\s*\n", text):
        m = re.search(r"\^([0-9a-z-]+)\s*$", b.strip())
        if m:
            d[m.group(1)] = b.strip()
    return d


with open(TS, encoding="utf-8") as fh:
    tsb = blocks_text(unicodedata.normalize("NFC", fh.read()))


def pcodes(b):
    b = re.sub(r"^#.*$", "", b, flags=re.M)
    parts = b.split("?")[1:]
    out = []
    for s in parts:
        s = s.strip()
        s = re.sub(r"^\(?[A-Za-z]+\)?\s", lambda m: m.group(0) if False else m.group(0), s)
        if re.match(r"Āmantā", s):
            out.append("Y")
        elif re.match(r"No\b", s):
            out.append("N")
        elif re.match(r"Natthi", s):
            out.append("X")
        elif re.match(r"(\(\w+\)\s*)?(yassa|yattha|yaṃ|yo|yā|ye|kāmadhātuyā|na |kati|$)", s, re.I) or s == "":
            out.append("-")
        else:
            out.append("P")
    return out


def tcodes(b):
    parts = re.split(r"phải chăng\s*\?|\?", b)[1:]
    out = []
    for s in parts:
        s = s.strip()
        s = re.sub(r"^\d+\.\s*", "", s)
        if re.match(r"Phải rồi|Phải\b", s):
            out.append("Y")
        elif re.match(r"Không phải|Không\.|Chẳng phải\.", s):
            out.append("N")
        elif re.match(r"Không có", s):
            out.append("X")
        elif s == "" or re.match(r"(Hay là|Người nào|Pháp|Tâm|Cõi nào|Nơi nào|Với người|\^)", s) or s.startswith("^"):
            out.append("-")
        else:
            out.append("P")
    return out


stat = collections.Counter()
k = 0
for f in files:
    P = "\n".join(load(PDIR, f))
    pb = blocks_text(P)
    for bid, b in pb.items():
        if bid.endswith("-0") and b.startswith("#"):
            continue
        t = tsb.get(bid)
        if t is None:
            stat["ts_missing"] += 1
            continue
        a, c = pcodes(b), tcodes(t)
        a2 = [x for x in a if x != "-"]
        c2 = [x for x in c if x != "-"]
        if a2 == c2:
            stat["same"] += 1
        else:
            stat["diff"] += 1
            if k < show:
                k += 1
                print(f"{f} {bid}\n  P: {''.join(a2)}\n  T: {''.join(c2)}")
print(stat)
