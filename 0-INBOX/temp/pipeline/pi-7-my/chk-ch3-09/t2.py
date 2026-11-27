import sys, importlib.util, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F, M3 = mk.F, mk.M3
M3.set_dyad(F, "cetasika")
F.translate("")
for fr in ["ahetuke §T§e khandhe ca vatthuñca paṭicca cittasamuṭṭhānaṃ rūpaṃ.", "ahetuke §T§e khandhe ca cittañca paṭicca cittasamuṭṭhānaṃ rūpaṃ.", "§T§e khandhe ca cittañca paṭicca cittasamuṭṭhānaṃ rūpaṃ."]:
    m = F.CLAUSE_RE.match(fr)
    print(m and m.groupdict())
    try:
        print(F.clause(fr, {"T": ["Q"], "C": [], "K": [], "D": [], "V": []}, [0], [0], [0], [0]))
    except Exception as e:
        import traceback; traceback.print_exc(limit=-3)
print([n for n in F.NOUN if n.endswith("ñca")][:20])
