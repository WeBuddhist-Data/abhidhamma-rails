import sys, importlib.util, pathlib, json
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F, D = X.F, X.D
snap, snapg = json.loads((H / "chk-ch4-01/snapB.json").read_text())
diffs = []
for mod, sn in ((F, snap), (X.FG, snapg)):
    for n, tab in sn.items():
        cur = getattr(mod, n)
        for k in cur:
            if k not in tab: diffs.append((mod, n, k, "added"))
            elif repr(cur[k]) != tab[k]: diffs.append((mod, n, k, "changed"))
print(len(diffs), "diffs;", [ (n,k,w) for _, n, k, w in diffs if w == "changed"][:40])
disk = X.ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
X.K.CUR["fix"] = True
def run():
    D.set_dyad(F, None); D.set_dyad(X.FG, None); X.FG.translate("")
    src = (X.PALI / "1-00-paccaya.md").read_text(encoding="utf-8-sig")
    try:
        return F.translate(src) == (disk / "1-00-paccaya.md").read_text(encoding="utf-8")
    except BaseException:
        return None
# remove added/changed entries per table and test
import copy
for target in ("LEX", "FIXED", "QUAL", "NOUN", "SK", "SKF", "NOTES", "HLINES"):
    saved = []
    for mod, n, k, w in diffs:
        if n == target:
            saved.append((mod, n, k, getattr(mod, n)[k]))
            tab = (snap if mod is F else snapg).get(n, {})
            if w == "added": del getattr(mod, n)[k]
    r = run()
    print(target, "removed ->", r)
    for mod, n, k, v in saved:
        getattr(mod, n)[k] = v
