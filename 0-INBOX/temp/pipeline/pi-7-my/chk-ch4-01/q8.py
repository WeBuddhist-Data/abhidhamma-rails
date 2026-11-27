import sys, importlib.util, pathlib, json
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F, D = X.F, X.D
snap, snapg = json.loads((H / "chk-ch4-01/snapB.json").read_text())
adds = [(m, k) for m, sn in ((F, snap), (X.FG, snapg)) for k in getattr(m, "FIXED") if k not in sn["FIXED"]]
print(len(adds), sorted({k for _, k in adds}))
disk = X.ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
X.K.CUR["fix"] = True
def run():
    D.set_dyad(F, None); D.set_dyad(X.FG, None); X.FG.translate("")
    src = (X.PALI / "1-00-paccaya.md").read_text(encoding="utf-8-sig")
    try:
        return F.translate(src) == (disk / "1-00-paccaya.md").read_text(encoding="utf-8")
    except BaseException:
        return None
keys = sorted({k for _, k in adds})
for k in keys:
    saved = [(m, m.FIXED[k]) for m, kk in adds if kk == k]
    for m, _ in saved: del m.FIXED[k]
    r = run()
    for m, v in saved: m.FIXED[k] = v
    if r: print("culprit:", k)
