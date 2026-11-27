d = "sanidassana"
X.set_dyad(F, d); X.set_dyad(X.FG, d); X.FG.translate(""); F.translate("")
import traceback
for u in open(HERE / "chk-ch3-01-02/units.txt", encoding="utf-8").read().splitlines():
    p = X.prep(u, d)
    sk, slots = F.slot(F.lc(p))
    print(sk)
    try:
        print(F.pairs_mr(sk, slots))
    except Exception as e:
        traceback.print_exc()
    try:
        print(F.np_my("§T§aṃ cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ".split(), iter(["X"]), ""))
    except Exception as e:
        traceback.print_exc()
