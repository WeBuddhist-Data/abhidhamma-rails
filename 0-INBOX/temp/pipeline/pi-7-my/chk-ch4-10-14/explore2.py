import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk41014", HERE / "make_ch4-10-14.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
X = mk.X
w = mk.WE
F, K, D = w.F, w.K, w.D
print("EVAM_T", D.EVAM_T, "| PANHA", D.PANHA, "| IHA", D.IHA, "| KABALI", getattr(D, "KABALI", None), "| RJIVIT", getattr(D, "RJIVIT", None))
print("ORDER_L", getattr(K, "ORDER_L", None))
print("cond loc neg", F.cond("hetu", "loc", True), "|", F.cond("jhāna", "loc", True), "|", F.cond("indriya", "loc", False))
print("cond n neg", F.cond("hetu", "n", True))
for k in ("ārammaṇapurejātaṃ", "vatthupurejātaṃ", "ārammaṇapurejāto", "kusalākusale"):
    print(k, F.LEX.get(k), F.FIXED.get(k))
print("heading", F.heading("*Hetu-ārammaṇapaccayā*"))
try:
    print("heading3", F.heading("*Hetu-ārammaṇa-adhipatipaccayā*"))
except Exception as e:
    print("heading3 ERR", e)
print("GROUP", F.GROUP, "PACCAYA", F.PACCAYA)
print("translate count:", F.translate("Hetuyā cha, ārammaṇe cha, indriye jhāne cha."))
print("finished", F.finished("X"))
print(F.HLINES.get("Dhammānulome dukatikapaṭṭhānaṃ"))
