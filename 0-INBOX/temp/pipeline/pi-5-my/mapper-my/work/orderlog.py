"""usage: orderlog.py — every value pali_order (G1 / G2) changes, all three scripts (writes nothing)"""
import sys, pathlib, importlib.util
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
for name in ("map_ch1", "map_ch2-15", "map_ch16-31"):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), D / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    M = m.mapper()
    for ch in m.CHAPTERS:
        if hasattr(m, "CUR"):
            m.CUR["ch"] = ch
        M.map_chapter(ch)
    for (ch, sid, kw), (a, b) in M.ORDER.items():
        print(ch, sid, kw, "|", a, "->", b, sep="\t")
