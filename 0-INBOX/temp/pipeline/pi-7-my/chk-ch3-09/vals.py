import sys, importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
M3, M4, M, K, F = mk.M3, mk.M4, mk.M, mk.K, mk.F
for mod, names in ((M3, "KAT VITTH GAN VIBHAJ EVAM_T PANHA NATTHI PARIP AVAS SAB MAHAB NIYAM PAV_PS NINNANA YAVA_AS IHA NO_GH NINNANAKARANA IMINA ARUPA_N MULA PUCCH EKASADISA EKAYEVA ITARE VAJJ CHADD DASSET LABBH AGGE PAVATTE ANUL_MATIKA SUDDHAKE PATICCA_V AJJH BAHIRA KABALI RJIVIT JIVIT CAKKA PATHAMA_GAMANA"),
                   (M4, "GARUK AVAJ_VUTTH ASSADANA VIBHAJANA PARIVATT NA_KAT SEKHA"),
                   (M, "GAMANA SABBE MAHABHUTA EVAM_THUS VIBHAJ AJJHATTIKA"),
                   (K, "KATABBA VITTH GANETABBA PANHA NATTHI PARIPUNNA AVASESA NANAKARANA KAYYA EVAM SADISANI SABBATTHA THITA ASANNA BAHIRA"),
                   (F, "SADISA MULAKA PADA ADI GHATANA PATISANDHI LAKAUNG KATATTARUPA VATTHU KHANDHA DHAMMA DUKA")):
    for n in names.split():
        print(mod.__name__, n, "=", repr(getattr(mod, n, "??")))
print("NOTE_ADD3", {k: v for k, v in list(M3.NOTE_ADD.items())})
print("NEWS", dict(M3.NEW))
print("NEW4", dict(M4.NEW))
print("S.GANANA", mk.S.GANANA, "ORDER_N", K.ORDER_N, "ORDER_L", K.ORDER_L)
