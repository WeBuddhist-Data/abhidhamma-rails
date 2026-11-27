import sys, time, pathlib, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
t=time.time()
Q = _load("q", "make_ch5-01-04.py"); print("Q", time.time()-t)
X = Q._isolated("x", "make_ch4-02-09.py"); print("X", time.time()-t)
Y = Q._isolated("y", "make_ch4-10-14.py"); print("Y", time.time()-t)
print([k for k in dir(X) if k.isupper()][:80])
print([k for k in dir(Y) if k.isupper()][:80])
