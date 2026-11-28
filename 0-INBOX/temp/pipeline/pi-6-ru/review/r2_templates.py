"""r2: collapse lines into templates (members -> X) and print unique Russian templates per file with a Pāli sample."""
import re, sys, os, collections
PD = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
RD = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters"

RMEM = r"сфер\w*\s+(глаза|уха|носа|языка|тела|видимых\s+форм|звуков|запахов|вкусов|осязаемого|объектов\s+ума|ума)"
PMEM = r"(cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatan\w*"
RATTR = r"(с|без) (глазом|глаза|ухом|уха|носом|носа|видимой формой|видимой формы|умом|ума)"
PATTR = r"(?<![a-zā])(sa|a)(cakkhuk|sotak|ghānak|rūpak|cittak)\w*"

def lines(path):
    return [l for l in open(path, encoding="utf-8").read().split("\n") if l.strip()]

seen = collections.OrderedDict()
for f in sys.argv[1:]:
    pl = lines(os.path.join(PD, f)); rl = lines(os.path.join(RD, f))
    for i, (p, r) in enumerate(zip(pl, rl)):
        tr = re.sub(r"\^[\d-]+", "", r)
        tr = re.sub(RMEM, "X", tr, flags=re.I)
        tr = re.sub(RATTR, r"\1 A", tr, flags=re.I)
        tr = re.sub(r"\((На основе) X\)", r"(\1 X)", tr)
        tr = re.sub(r"(?<![а-яё])(возникает|возникала|возникнет|прекращается|прекращалась|прекратится)(?![а-яё])", "V", tr)
        tr = re.sub(r"^\((а|б)\) ", "", tr)
        key = tr.strip()
        if key not in seen:
            seen[key] = [f"{f[:4]}:L{i+1}", p, r, 0]
        seen[key][3] += 1
full = "--full" in os.environ.get("R2MODE", "")
for k, (loc, p, r, n) in seen.items():
    if full:
        print(f"[{loc} x{n}]"); print("  P:", p); print("  R:", r)
    else:
        print(f"{loc} x{n}: {k}")
print("unique:", len(seen))
