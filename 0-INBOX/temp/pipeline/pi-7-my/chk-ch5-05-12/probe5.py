import importlib.util, sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m5", HERE / "make_ch5-01-04.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
F=M.WA.F
print({k:v for k,v in F.COUNT.items() if 'vīs' in k or 'bīs' in k})
for w in (M.WA, M.WB):
  for mod in (w.F, w.FG):
    for name in dir(mod):
        obj=getattr(mod,name)
        if isinstance(obj,dict):
            for k,v in obj.items():
                if isinstance(k,str) and re.search(r"kusalākusal|vipākābyākataṃ kiriyābyākataṃ|sukhavedanā|mahābhūtā natthi|ārammaṇaṃ natthi|cittasamuṭṭhānameva", k):
                    print(w.tag, mod.__name__, name, repr(k)[:120], '=', repr(v)[:200])
print(F.SIGLA.get('?'), F.variant("nevasaññānāsaññāyatanassa (?)"))
