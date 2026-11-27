import sys, pathlib, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-03-06.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
role = sys.argv[1]
for ph in sys.argv[2:]:
    try: print(ph, "=>", mk.F.np_my(ph.split(), iter([]), role))
    except Exception as e: print(ph, "ERR", repr(e))
