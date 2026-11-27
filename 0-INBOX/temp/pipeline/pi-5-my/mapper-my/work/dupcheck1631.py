"""multiword keywords whose composed value lost a member (two members with the same value, or a member value absent)."""
import sys, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map5_rules as R
spec = importlib.util.spec_from_file_location("m1631", HERE / "map_ch16-31.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
for ch in m.CHAPTERS:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for k in kws:
            ws = k.split()
            if len(ws) < 2: continue
            v = M.lookup(ch, sid, k, pa.get(sid, ""), my[sid])
            if M.SRC.get((sid, k)) not in ("compose", "neg"): continue
            vals = []
            for w in ws:
                if R.low(w) in ("na", "no", "ca", "vā"): continue
                try: vals.append(M.lookup(ch, sid, w, pa.get(sid, ""), my[sid]))
                except KeyError: vals.append("?")
            vals = [x for x in vals if x != R.NONE]
            if len(set(vals)) < len(vals) or any(x not in v for x in vals):
                print(ch[:3], sid, k, "=", v, "|| members:", vals)
