import sys, pathlib, importlib.util, re, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m", HERE / "make_ch5-13-20.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
Q = M.Q
N = collections.OrderedDict()
for n in M.NAMES:
    for l in (M.PALI / n).read_text(encoding="utf-8-sig").splitlines():
        for m in re.finditer(r"\([^()]*\)", l):
            k = m[0]
            if re.fullmatch(r"\(\d+\)", k): continue
            N.setdefault(k, (n[:4], l))
for k, (n, l) in N.items():
    if k in Q.WA.F.NOTES or Q.F.lc(k) in Q.WA.F.NOTES or k in Q.WB.F.NOTES or Q.F.lc(k) in Q.WB.F.NOTES:
        print("ENGINE", k, "=", Q.WA.F.NOTES.get(k) or Q.WA.F.NOTES.get(Q.F.lc(k)) or Q.WB.F.NOTES.get(k) or Q.WB.F.NOTES.get(Q.F.lc(k))); continue
    r = Q.note_my(k)
    if r: print("Q", k, "=", r); continue
    print("TODO", n, k, "|", l[:300])
