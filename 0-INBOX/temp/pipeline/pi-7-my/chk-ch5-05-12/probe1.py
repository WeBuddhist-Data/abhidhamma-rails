import importlib.util, sys, pathlib, time
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
t=time.time()
spec = importlib.util.spec_from_file_location("m5", HERE / "make_ch5-01-04.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
print("load", time.time()-t)
K=M.WA.K
print(K.ORDER_L); print(K.ORDER_N)
print({k:v for k,v in M.F.HEAD.items()})
for k,v in M.WA.F.HLINES.items():
    if 'nulomapacc' in k or 'Paccanīy' in k or 'paccanīy' in k: print(repr(k),'=',v)
