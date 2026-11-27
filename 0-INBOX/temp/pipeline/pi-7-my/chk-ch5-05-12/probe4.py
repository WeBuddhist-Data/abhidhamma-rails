import importlib.util, sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("x", HERE / "make_ch5-05-12.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
PALI = X.PALI
seen=set()
for n in X.NAMES:
    src=(PALI/n).read_text(encoding='utf-8-sig')
    rx = X.PH_T if n.startswith('5-09') else X.PH_D if n.startswith('5-10') else X.PH_X
    for m in rx.finditer(src):
        words = [m[2], m[3]] if rx is X.PH_X else [m[2] if rx is X.PH_D else m[1]]
        for w in words:
            if w in seen: continue
            seen.add(w)
            try:
                k,h,nm = X.side(w) if rx is not X.PH_T else ('t',[X.M.triad_of(w)],'')
                print(n[:4], w, '|', k, len(h), h[0], h[-1], '|', nm)
            except Exception as e:
                print(n[:4], w, 'ERROR', repr(e))
