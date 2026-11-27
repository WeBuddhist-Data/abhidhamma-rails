import importlib.util, sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m5", HERE / "make_ch5-01-04.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for h in M.DYAD_TERMS: print(h, '|', M.DUKA_NAME.get(h), '|', M.DYAD_TERMS[h])
for t in M.TRIADS: print(t, '|', M.TIKA_NAME[t])
print(M.F.ADI, M.F.PADA, M.TIKA, M.DUKA)
