import sys, re, importlib.util, pathlib
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-01-02.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F = X.F
exec(open(sys.argv[1], encoding="utf-8").read())
