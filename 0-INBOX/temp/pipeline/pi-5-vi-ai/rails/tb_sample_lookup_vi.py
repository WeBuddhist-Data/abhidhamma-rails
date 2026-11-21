"""Helper: for the pi-5 sample (preamble, 1-puggalakatha) list every keyword of the Pāli keyword map once
(first segment where it occurs) with its locked Vietnamese termbase entry.

usage: python -I -X utf8 -B tb_sample_lookup_vi.py [--from ID] [--to ID]
       python -I -X utf8 -B tb_sample_lookup_vi.py --word <regex>   (grep the termbase headwords)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"


def termbase():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb[ln.split(": {", 1)[0]] = ln
    return tb


def main():
    args = sys.argv[1:]
    tb = termbase()
    if args and args[0] == "--word":
        pat = re.compile(args[1], re.I)
        for h, ln in tb.items():
            if pat.search(h):
                print(ln)
        return
    lo = args[args.index("--from") + 1] if "--from" in args else None
    hi = args[args.index("--to") + 1] if "--to" in args else None
    tbl = {k.lower(): v for k, v in tb.items()}
    seen = set()
    on = lo is None
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        if not (i in ("0", "T-1") or i.startswith("5-")):
            continue
        if i.startswith("5-") and not (re.fullmatch(r"5-\d+", i) and int(i[2:]) <= 238 or i.startswith("5-1-") or i == "5-0"):
            continue
        if not on and i == lo:
            on = True
        if not on:
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                e = tb.get(kk) or tbl.get(kk.lower())
                print(f"[{i}] {e if e else kk + ': <NOT IN TERMBASE>'}")
        if hi and i == hi:
            break


if __name__ == "__main__":
    main()
