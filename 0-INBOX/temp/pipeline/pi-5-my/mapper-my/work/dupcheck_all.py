"""phase 3: G5 over the whole book — composed multiword keywords that lost a member (two members with the same
value, or a member value absent from the composed value). usage: dupcheck_all.py"""
import sys, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map5_rules as R
for name in ("map_ch1", "map_ch2-15", "map_ch16-31"):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); M = m.mapper()
    for ch in m.CHAPTERS:
        if hasattr(m, "CUR"):
            m.CUR["ch"] = ch
        my, pa = R.burmese(ch), R.pali(ch)
        for sid, kws in R.keyword_rows(ch):
            for k in kws:
                ws = k.split()
                if len(ws) < 2:
                    continue
                v = M.lookup(ch, sid, k, pa.get(sid, ""), my[sid])
                if M.SRC.get((sid, k)) not in ("compose", "neg"):
                    continue
                vals = []
                for w in ws:
                    if R.low(w) in ("na", "no", "ca", "vā"):
                        continue
                    try:
                        vals.append(M.lookup(ch, sid, w, pa.get(sid, ""), my[sid]))
                    except KeyError:
                        vals.append("?")
                vals = [x for x in vals if x != R.NONE]
                if len(set(vals)) < len(vals) or any(x not in v for x in vals):
                    print(ch, sid, k, "=", v, "|| members:", vals, sep="\t")
