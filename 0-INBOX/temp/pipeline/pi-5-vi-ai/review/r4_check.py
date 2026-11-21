"""r4 mechanical checks: Pali vs Vietnamese, line by line, for given chapters.
Usage: python -I -X utf8 -B r4_check.py <ch1.md> [<ch2.md> ...]
Prints only mismatches. Writes nothing.
"""
import re
import sys
import unicodedata

BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PDIR = BASE + r"\pali\pi-5_split_chapters"
VDIR = BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"


def lines(path):
    with open(path, encoding="utf-8") as f:
        t = f.read()
    return t, [l for l in t.split("\n") if l.strip()]


def cnt(pat, s, flags=re.I):
    return len(re.findall(pat, s, flags))


def strip_brackets(s):
    return re.sub(r"\[[^\]]*\]", "", s)


def pali_counts(p):
    q = strip_brackets(p)
    pe = q.replace("…pe…", "\u2026")
    return {
        "amanta": cnt(r"āmantā", q),
        "nahevam": cnt(r"na hevaṃ vattabbe", q),
        "q": q.count("?"),
        "dash": p.count("–") + p.count("—"),
        "ell": pe.count("\u2026"),
        "nanu": cnt(r"\bnanu\b", q),
        "hanci": cnt(r"\bhañci\b", q),
        "nocavata": cnt(r"no ca vata re vattabbe|no vata re vattabbe", q),
        "tenavata": cnt(r"tena vata re vattabbe", q),
        "tenahi_na": cnt(r"tena hi na vattabba", q),
        "tenahi": cnt(r"tena hi\b", q),
        "sutta": cnt(r"attheva suttanto", q),
        "nittha": cnt(r"niṭṭhit", q),
    }


def vi_counts(v):
    q = strip_brackets(v)
    return {
        "amanta": cnt(r"đúng vậy", q),
        "nahevam": cnt(r"không nên nói như vậy", q),
        "q": q.count("?"),
        "dash": v.count("–") + v.count("—"),
        "ell": q.count("\u2026"),
        "nanu": cnt(r"chẳng phải", q),
        "hanci": cnt(r"\bnếu\b", q),
        "nocavata": cnt(r"chắc chắn không nên nói", q),
        "tenavata": cnt(r"chắc chắn nên nói", q),
        "tenahi_na": cnt(r"vậy thì không nên nói", q),
        "tenahi": cnt(r"vậy thì", q),
        "sutta": cnt(r"có bài kinh như vậy thật không", q),
        "nittha": cnt(r"đã hoàn tất", q),
    }


def main():
    for ch in sys.argv[1:]:
        pt, pl = lines(PDIR + "\\" + ch)
        vt, vl = lines(VDIR + "\\" + ch)
        print("=" * 20, ch, "P lines", len(pl), "V lines", len(vl))
        if unicodedata.normalize("NFC", vt) != vt:
            print("  NOT NFC")
        if "\r" in vt:
            print("  CR present")
        if "\n\n\n" in vt:
            print("  double blank")
        for bad in ["«", "»", "….", "\"", "—", ":-", " ?", " .", " ,"]:
            if bad in strip_brackets(vt):
                for i, l in enumerate(vl):
                    if bad in strip_brackets(l):
                        print("  typo %r line %d: ...%s" % (bad, i + 1, l[max(0, l.find(bad) - 40):l.find(bad) + 20]))
        cur = ""
        for i, (p, v) in enumerate(zip(pl, vl)):
            m = re.search(r"\^(\S+)\s*$", p)
            mv = re.search(r"\^(\S+)\s*$", v)
            if m:
                cur = m.group(1)
            if (m and not mv) or (mv and not m) or (m and mv and m.group(1) != mv.group(1)):
                print("  ID mismatch line", i + 1, m and m.group(1), mv and mv.group(1))
            if p.startswith("#") != v.startswith("#") or (p.startswith("#") and p.split(" ")[0] != v.split(" ")[0]):
                print("  heading level mismatch line", i + 1)
            pc, vc = pali_counts(p), vi_counts(v)
            diffs = []
            for k in pc:
                a, b = pc[k], vc[k]
                if k == "tenahi":
                    a = a - pc["tenahi_na"]
                    b = b - vc["tenahi_na"]
                if k == "hanci":
                    if b < a:
                        diffs.append("%s P%d V%d" % (k, a, b))
                    continue
                if a != b:
                    diffs.append("%s P%d V%d" % (k, a, b))
            if diffs:
                print("  L%d [%s] %s" % (i + 1, cur, "; ".join(diffs)))
            # latin leftovers in vi (outside brackets)
            lat = re.findall(r"\b[a-zāīūṃṅñṭḍṇḷ]*[āīūṃṅñṭḍṇḷ][a-zāīūṃṅñṭḍṇḷ]*\b", strip_brackets(v), re.I)
            if lat:
                print("  L%d [%s] pali-like words: %s" % (i + 1, cur, lat[:8]))


main()
