"""Probe helper for 4-01-kilesagocchaka.
usage: python -I -B -X utf8 probe_4-01_hi.py missing            (unmapped keywords with prior values)
       python -I -B -X utf8 probe_4-01_hi.py ctx kw [n]           (first n segments with kw: Pāli + Hindi)
       python -I -B -X utf8 probe_4-01_hi.py seg id ...           (Pāli + Hindi + keywords of segments)
       python -I -B -X utf8 probe_4-01_hi.py grep "हिंदी" [n]      (Hindi segments containing a string)
"""
import sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import collections
import re
from map_sample_hi import read_keywords, read_hindi, read_pali, prior, lc, PI7, pi7_value
import probe_sample_hi as PS
import importlib.util
_sp = importlib.util.spec_from_file_location("map_4_01_hi", pathlib.Path(__file__).resolve().parent / "map_4-01_hi.py")
M = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(M)

F = "4-01-kilesagocchaka"


def main():
    mode, args = sys.argv[1], sys.argv[2:]
    kwl = read_keywords(F)
    hi, pa = read_hindi(F), read_pali(F)
    if mode == "missing":
        pr = PS.load_prior()
        tab = {**PI7, **M.T}
        miss = collections.Counter()
        for bid, kws in kwl:
            for kw in kws:
                if kw in M.OVR.get(bid, {}):
                    continue
                try:
                    pi7_value(kw, kws, tab, pa.get(bid), hi.get(bid))
                except KeyError:
                    miss[kw] += 1
        for k, c in sorted(miss.items(), key=lambda x: lc(x[0])):
            p = pr.get(lc(k), {})
            top = ", ".join(f"pi{n}:{v}({c2})" for (n, v), c2 in sorted(p.items(), key=lambda x: -x[1])[:3])
            print(f"{k} [{c}] {top}")
    elif mode == "ctx":
        kw, n = args[0], int(args[1]) if len(args) > 1 else 2
        lim = int(args[2]) if len(args) > 2 else 700
        for bid, kws in kwl:
            if kw in kws:
                print("==", bid, "|", ", ".join(kws)[:300])
                p = pa.get(bid, "")
                i = p.find(kw)
                print("PA:", p[max(0, i - 200): i + 300])
                print("HI:", hi.get(bid, "")[:lim])
                n -= 1
                if n == 0:
                    break
    elif mode == "al":                      # aligned pieces: al kw [n]
        kw, n = args[0], int(args[1]) if len(args) > 1 else 1
        for bid, kws in kwl:
            if kw not in kws:
                continue
            p, h = pa.get(bid, ""), hi.get(bid, "")
            pp = re.split(r" – |\. |; |\n", p)
            hh = re.split(r" – |। |; |\n", h)
            flag = "" if len(pp) == len(hh) else f" [pieces {len(pp)}/{len(hh)}]"
            for i, piece in enumerate(pp):
                if re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", piece):
                    print("==", bid, flag)
                    print("  PA:", piece[:400])
                    print("  HI:", hh[i][:400] if i < len(hh) else "?")
                    break
            n -= 1
            if n == 0:
                break
    elif mode == "seg":
        for bid in args:
            print("==", bid)
            print("KW:", ", ".join(dict(kwl).get(bid, [])))
            print("PA:", pa.get(bid))
            print("HI:", hi.get(bid))
    elif mode == "grep":
        s, n = args[0], int(args[1]) if len(args) > 1 else 5
        for bid, t in hi.items():
            i = t.find(s)
            if i >= 0:
                print(bid, "…", t[max(0, i - 150): i + 150])
                n -= 1
                if n == 0:
                    break


if __name__ == "__main__":
    main()
