import sys, pathlib, importlib.util, re, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("q", HERE / "make_ch5-01-04.py")
Q = importlib.util.module_from_spec(spec); spec.loader.exec_module(Q)
print("ORDER_L", Q.ORDER_L); print("ORDER_N", Q.K.ORDER_N)
print("HEAD keys", [k for k in Q.F.HEAD][:60])
print({k: v for k, v in Q.WA.F.HLINES.items() if re.search(r"Dhamm(ānuloma|paccanīy)|niṭṭhitaṃ\.$", k) and ("paccan" in k or "Paṭṭhānapakaraṇaṃ" in k)})
P = Q.PALI
heads = collections.OrderedDict()
for n in sorted(p.name for p in P.iterdir() if p.name[:4] in ("5-13","5-14","5-15","5-16","5-17","5-18","5-19","5-20")):
    for l in (P/n).read_text(encoding="utf-8-sig").splitlines():
        if l.startswith("#"):
            h = re.sub(r" \^[\d-]+$", "", l).lstrip("#").strip()
            heads.setdefault(h, n[:4])
for h, n in heads.items():
    a = Q.WA.F.HLINES.get(h); b = Q.WB.F.HLINES.get(h)
    hh = h.strip("*")
    print(n, "KNOWN" if (a or b) else "----", h, "|", a or b or "")
print("GNAME", Q.GNAME)
print("DUKA_NAME", Q.DUKA_NAME)
