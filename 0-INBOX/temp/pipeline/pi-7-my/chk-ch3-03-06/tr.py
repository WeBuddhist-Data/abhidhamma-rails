import sys, pathlib, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-03-06.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
mk.K.CUR["fix"] = True
d = sys.argv[1]
for line in sys.argv[2:]:
    try:
        print(mk.M3.translate_part(d, line).strip())
    except Exception as e:
        print("ERR", repr(e)[:400])
