import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F = X.F
seen = []
orig = X._PREV_UNIT
def spy(u):
    if "ahajātā" in u: seen.append(u[:140])
    return orig(u)
X._PREV_UNIT = spy
X.K.CUR["fix"] = True
t = "Rūpāvacaro dhammo rūpāvacarassa dhammassa kammapaccayena paccayo – sahajātā, nānākkhaṇikā. Sahajātā – rūpāvacarā cetanā sampayuttakānaṃ khandhānaṃ kammapaccayena paccayo; paṭisandhikkhaṇe…pe…. Nānākkhaṇikā – rūpāvacarā cetanā vipākānaṃ rūpāvacarānaṃ khandhānaṃ kammapaccayena paccayo."
print(X.B._engine(t, "rupa"))
print(seen)
print(F.unit_my, X.unit_my)
