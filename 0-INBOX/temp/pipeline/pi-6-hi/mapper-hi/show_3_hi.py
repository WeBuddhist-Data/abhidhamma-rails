"""Show segments of the 3-0x files by id (file found automatically), or only the line pairs (Pāli line i / Hindi
line i) whose Pāli contains a word.
usage: python -I -X utf8 show_3_hi.py id [id ...]            full segments
       python -I -X utf8 show_3_hi.py -w word [max]          line pairs containing word (case-insensitive)"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import HERE, read_keywords, read_hindi, read_pali  # noqa: E402

FILES = [f"3-0{i}-ayatanayamaka" for i in range(1, 7)]
DATA = {f: (read_pali(f), read_hindi(f), dict(read_keywords(f))) for f in FILES}


def mapped(f):
    mp = {}
    p = HERE / f"{f}.mapped.md"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            mp[line.split("] ", 1)[0][1:]] = line
    return mp


if sys.argv[1] == "-w":
    w = sys.argv[2].lower()
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    n = 0
    for f in FILES:
        pi, hi, kw = DATA[f]
        for bid, ptxt in pi.items():
            pl, hl = ptxt.splitlines(), (hi.get(bid) or "").splitlines()
            for i, l in enumerate(pl):
                if w in l.lower():
                    print(f"[{bid}] PI: {l}\n{' ' * (len(bid) + 3)}HI: {hl[i] if i < len(hl) else '??'}"
                          + ("" if len(pl) == len(hl) else f"   (line counts {len(pl)}/{len(hl)})"))
                    n += 1
                    if n >= mx:
                        sys.exit()
else:
    for i in sys.argv[1:]:
        for f in FILES:
            pi, hi, kw = DATA[f]
            if i in hi or i in kw:
                print(f"=== {f} {i}\n--- PI\n{pi.get(i)}\n--- HI\n{hi.get(i)}\n--- KW {kw.get(i)}\n"
                      f"--- MAP {mapped(f).get(i)}\n")
