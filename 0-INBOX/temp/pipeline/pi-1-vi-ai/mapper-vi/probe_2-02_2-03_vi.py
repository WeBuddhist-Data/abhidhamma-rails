"""Review helper for map_2-02_2-03_vi.py (writes nothing).

usage: python -I -X utf8 probe_2-02_2-03_vi.py lines PART [from_id] [to_id]
           Vietnamese segment lines; a line identical to an earlier one prints as "= <id>"
       python -I -X utf8 probe_2-02_2-03_vi.py kw PART
           keywords that are not in the table (after overrides/context), with their segment ids
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import read_keywords, read_vietnamese  # noqa: E402


def lines(part, a=None, b=None):
    seen = {}
    on = a is None
    for bid, text in read_vietnamese(part).items():
        if bid == a:
            on = True
        if on:
            out = []
            for ln in text.splitlines():
                if ln in seen:
                    out.append(f"   = {seen[ln]}")
                else:
                    out.append("   " + ln)
            print(f"[{bid}]")
            print("\n".join(out))
        for ln in text.splitlines():
            seen.setdefault(ln, bid)
        if bid == b:
            break


def kw(part):
    import importlib.util
    spec = importlib.util.spec_from_file_location("m", HERE / "map_2-02_2-03_vi.py")
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    res = M.resolver_for(part)
    miss = {}
    for bid, kws in read_keywords(part):
        for k in kws:
            try:
                res(bid, k, kws)
            except KeyError:
                miss.setdefault(k, []).append(bid)
    for k, ids in miss.items():
        print(k, len(ids), ids[:6])


if __name__ == "__main__":
    if sys.argv[1] == "lines":
        lines(sys.argv[2], *(sys.argv[3:5]))
    else:
        kw(sys.argv[2])
