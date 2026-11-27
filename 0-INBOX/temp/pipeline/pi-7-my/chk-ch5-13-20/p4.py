import sys, pathlib, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m", HERE / "make_ch5-13-20.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
Q = M.Q; K = Q.K; F = Q.F
for n in ("SADISA", "SABBATTHA", "VITTH", "EVAM", "GANETABBA", "NATTHI", "PANHA"):
    print(n, repr(getattr(K, n, None)))
print("DHAMMA", repr(F.DHAMMA), "PADA", F.PADA, "MULAKA", repr(getattr(F, "MULAKA", None)))
for a in ("saṅkhat","sappaccay","asaṅkhat","appaccay","sahetuk","ahetuk","lokiy","uppād","anuppann","anāgat","atīt","anupādinnupādāniy","sanidassanasappaṭigh","anidassanasappaṭigh","anidassanaappaṭigh","akusal","abyākat","kusal","nakusal","naakusal","naabyākat","nahet","nanahet","nasahetuk","naanidassanasappaṭigh","naanidassanaappaṭigh","naappaccay","nasaṅkhat","nasappaccay","nakenaci viññeyy","nasāsav","naāsavasampayutt","naāsav","naanāsav","āsavavippayutt","nasāsav","adukkhamasukhāya vedanāya sampayutt","dukkhāya vedanāya sampayutt","nadukkhāya vedanāya sampayutt","bahiddh","nabahiddh","ajjhattabahiddhārammaṇ","apariyāpann","nanoāsav","noāsav","āsav"):
    print(a, Q.ATOM.get(a))
print(F.COUNT)
print([k for k in F.NOTES][:80])
print(K.vara("paṭicca"), K.vara("pañhā"))
print(F.HEAD.get("Pañhāvāro"), F.HEAD.get("Paṭiccavāro"))
print({k: v for k, v in F.HLINES.items() if "vārādi" in k or "Paccayavār" in k})
