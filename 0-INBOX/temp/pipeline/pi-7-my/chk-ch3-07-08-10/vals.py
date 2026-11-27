import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("mk", H / "make_ch3-07-08-10.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
D, K, F, M = mk.D, mk.K, mk.F, mk.M
for n in "KATABBA VITTH GANETABBA EVAM PANHA NATTHI PARIPUNNA AVASESA SADISANI KAYYA THITA SABBATTHA NANAKARANA ATTHI".split():
    print("K."+n, "=", getattr(K, n, None))
for n in "EVAM_T SAB CAKKA NINNANAKARANA ITARE YAVA_AS ARUPA_N PAVATTE MULA PUCCH EKAYEVA AGGE LABBH DASSET IHA NO_GH KAT VITTH GAN VIBHAJ".split():
    print("D."+n, "=", getattr(D, n, None))
for n in "NINNANA VIBHAJ GAMANA EVAM_THUS".split():
    print("M."+n, "=", getattr(M, n, None))
print("F.SADISA", F.SADISA, "| F.MULAKA", F.MULAKA, "| saṃkhittaṃ", F.NOTES.get("(saṃkhittaṃ)"), "| F.ADI", F.ADI)
print(K.ORDER_N); print(K.ORDER_L)
print({k: v for k, v in K.NOTE_FIXED.items() if len(k) < 40})
