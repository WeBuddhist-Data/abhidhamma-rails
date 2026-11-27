import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
PS = re.compile(r"(?:…\s*pe\s*…\.?|…\.?|[?!]|\.(?=\s|$)|;|–)\s*")
MS = re.compile(r"(?:…|။|၊|–)\s*")
def split(pa, my):
    p = [x for x in PS.split(R.strip_brackets(pa)) if x.strip()]
    m = [x for x in MS.split(re.sub(r"\s*\[[^\]]*\]", "", my)) if x.strip()]
    return p, m
if __name__ == "__main__":
    ch = sys.argv[1]
    my, pa = R.burmese(ch), R.pali(ch)
    good = 0
    for sid in pa:
        p, m = split(pa[sid], my.get(sid, ""))
        good += len(p) == len(m)
        if len(sys.argv) > 2 and len(p) != len(m): print(sid, len(p), len(m))
    print(ch, good, len(pa))
