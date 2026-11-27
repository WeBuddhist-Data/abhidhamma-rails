import traceback
d = sys.argv[2] if len(sys.argv) > 2 else "hetu"
X.set_dyad(F, d); X.set_dyad(X.FG, d); X.FG.translate(""); F.translate("")
for u in open(sys.argv[3] if len(sys.argv) > 3 else HERE / "chk-ch3-01-02/units.txt", encoding="utf-8").read().splitlines():
    if not u.strip(): continue
    p = X.prep(u, d)
    try:
        print("OK ", F.unit_my(p))
    except Exception as e:
        print("ERR", p, "\n   ", repr(e)[:300])
    print("   F.np:", end=" ")
    print()
