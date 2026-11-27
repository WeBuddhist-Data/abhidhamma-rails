import sys, importlib.util, pathlib, re, traceback
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("mk", HERE / "make_ch3-09.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
F, M3 = mk.F, mk.M3
src = (mk.PALI / mk.NAMES[0]).read_text(encoding="utf-8-sig").splitlines()
def dyad_at(n):
    for i in range(n - 1, -1, -1):
        m = re.match(r"^###### (\S+dukaṃ) \^", src[i])
        if m and m[1] in mk.DYAD_OF:
            return mk.DYAD_OF[m[1]]
    return "sarammana"
args = sys.argv[1:]
d = None
for a in args:
    if a.startswith("L"):
        n = int(a[1:]); s = src[n - 1]; dd = dyad_at(n)
    elif a.startswith("D="):
        d = a[2:]; continue
    else:
        s = a; dd = d
    M3.set_dyad(F, dd); M3.set_dyad(mk.FG, dd); mk.FG.translate("")
    M3.chapter_notes(M3.prep(s, dd), dd)
    t = M3.prep(s, dd)
    print("PREP:", t)
    try:
        print("OUT:", F.translate(t))
    except BaseException as e:
        print("ERR:", repr(e)[:1500])
