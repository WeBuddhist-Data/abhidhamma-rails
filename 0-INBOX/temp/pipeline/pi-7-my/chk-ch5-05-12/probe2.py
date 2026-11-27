import importlib.util, sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m5", HERE / "make_ch5-01-04.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for w in (M.WA, M.WB):
  for k,v in w.F.HLINES.items():
    if re.search(r"ādi|gocchak|ttikāni|dukāni|Dvi|Cha", k) and not k.startswith(('*','1-','Paṭicca')): print(w.tag, repr(k),'=',v)
print(sorted(M.GNAME.items()))
print(M.DUKA_NAME.get("Hetudukaṃ"), M.TIKA_NAME["Kusalattikaṃ"])
print(sorted(M.HL.items())[:5])
