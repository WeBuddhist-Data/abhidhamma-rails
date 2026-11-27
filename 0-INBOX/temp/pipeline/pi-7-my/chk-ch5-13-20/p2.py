import sys, pathlib, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("q", HERE / "make_ch5-01-04.py")
Q = importlib.util.module_from_spec(spec); spec.loader.exec_module(Q)
for n, l in [("hetu", Q._HETU_CL), ("cula", Q._CULA), ("maha", Q._MAHA), ("kil", Q._KIL), ("pit", Q._PITTHI)] + [(c, Q._CLUSTER_HEADS[c]) for c in Q._CLUSTER_HEADS]:
    print(n, len(l), l)
print(len(Q.DYAD_TERMS))
