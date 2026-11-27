"""baseline: the 3-03-06 engine WITHOUT the 3-09 extensions, regenerated in memory and compared (nothing written)"""
import sys, importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("ch30306", HERE / "make_ch3-03-06.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.K.CUR["fix"] = True
m.regress()
