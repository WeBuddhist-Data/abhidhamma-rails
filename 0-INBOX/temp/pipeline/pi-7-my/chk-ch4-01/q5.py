import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
F, D = X.F, X.D
mode = sys.argv[1]
if "nolex" in mode: F.lex = X._LEX0
if "noprep" in mode: D.prep_dyad = X._PREV_PREP
disk = X.ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
X.K.CUR["fix"] = True
D.set_dyad(F, None); D.set_dyad(X.FG, None); X.FG.translate("")
for n in ["1-00-paccaya.md", "1-02-vedanattika.md"]:
    src = (X.PALI / n).read_text(encoding="utf-8-sig")
    try:
        out = F.translate(src)
        print(n, out == (disk / n).read_text(encoding="utf-8"))
    except BaseException as e:
        print(n, "FAIL", str(e)[:200])
