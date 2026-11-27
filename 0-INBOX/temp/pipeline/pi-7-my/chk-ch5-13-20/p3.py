import sys, pathlib, importlib.util, traceback
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m", HERE / "make_ch5-13-20.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for w, n in (("Saññojanagocchakādi", [20,54,1]), ("hetudukaṃ", [20,54,1]), ("Upādānagocchakādi", [69,82,1])):
    r = M.dyads_of(w, n); print("RESULT", w, len(r), r[:3])
    try: print("NAME", M.name_dy(w, r))
    except Exception as e: print("ERR", e)
mm = M.DY_RX.fullmatch("Saññojanagocchakādi"); print("G", mm.groups(), mm[3].startswith("gocchaka"))
import inspect; print(inspect.getsource(M.dyads_of)[:600])
