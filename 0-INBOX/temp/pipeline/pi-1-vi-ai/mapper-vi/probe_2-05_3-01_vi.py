"""Review helper for map_2-05_3-01_vi.py (writes nothing).

usage: python -I -X utf8 probe_2-05_3-01_vi.py lines PART [from_id] [to_id]
           Vietnamese segment lines; a line identical to an earlier one prints as "= <id>"
       python -I -X utf8 probe_2-05_3-01_vi.py pali PART [from_id] [to_id]
           Pāli segment lines (same dedup)
       python -I -X utf8 probe_2-05_3-01_vi.py kw PART
           keywords the current resolver cannot map, with their segment ids
       python -I -X utf8 probe_2-05_3-01_vi.py miss PART
           keyword=value pairs whose value is not found in the segment's Vietnamese
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import present, read_keywords, read_pali, read_vietnamese  # noqa: E402


def _show(segs, a=None, b=None):
    seen = {}
    on = a is None
    for bid, text in segs.items():
        if bid == a:
            on = True
        if on:
            print(f"[{bid}]")
            for ln in text.splitlines():
                print(f"   = {seen[ln]}" if ln in seen else "   " + ln)
        for ln in text.splitlines():
            seen.setdefault(ln, bid)
        if bid == b:
            break


def _resolver(part):
    spec = importlib.util.spec_from_file_location("m", HERE / "map_2-05_3-01_vi.py")
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    return M.resolver_for(part)


def kw(part):
    res = _resolver(part)
    miss = {}
    for bid, kws in read_keywords(part):
        for k in kws:
            try:
                res(bid, k, kws)
            except KeyError:
                miss.setdefault(k, []).append(bid)
    for k, ids in miss.items():
        print(k, len(ids), ids[:8])


def miss(part):
    res = _resolver(part)
    vi = read_vietnamese(part)
    out = {}
    for bid, kws in read_keywords(part):
        for k in kws:
            try:
                v = res(bid, k, kws)
            except KeyError:
                continue
            if not present(v, vi.get(bid, "")):
                out.setdefault((k, v), []).append(bid)
    for (k, v), ids in out.items():
        print(f"{k}={v}", len(ids), ids[:8])


if __name__ == "__main__":
    cmd, part = sys.argv[1], sys.argv[2]
    if cmd == "lines":
        _show(read_vietnamese(part), *(sys.argv[3:5]))
    elif cmd == "pali":
        _show(read_pali(part), *(sys.argv[3:5]))
    elif cmd == "kw":
        kw(part)
    else:
        miss(part)
