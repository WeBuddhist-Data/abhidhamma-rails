"""List mapped values that pass the presence check only because a dropped «न» may sit between two words
(pi-1 tolerance), i.e. values that may have lost a negation. Unique pairs per file.
usage: python -I -B -X utf8 strictneg_4-15_5-04_hi.py <file> [<file> …]
"""
import collections, pathlib, re, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import read_hindi, present, NDE, DEV  # noqa
sys.path.append(str(HERE.parents[1] / "pi-1-hi" / "mapper-hi"))
from map_common_hi import _norm, _token  # noqa


def strict(value, text):
    t = _norm(text)
    for part in re.split(r" … | / ", value):
        toks = _norm(part).split()
        if not toks:
            continue
        pat = re.compile(f"(?<![{DEV}])" + r"\s+".join(_token(x) for x in toks))
        if not pat.search(t):
            return False
    return True


for f in sys.argv[1:]:
    hi = read_hindi(f)
    seen = collections.Counter()
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, _, rest = line.partition("] ")
        text = hi.get(bid[1:], "")
        for pair in rest.split(", ") if rest else []:
            kw, v = pair.split("=", 1)
            if v == NDE:
                continue
            if present(v, text) and not strict(v, text):
                # try the pronoun / -ाया variants of present() before flagging
                alts = [v.replace("यह", "इस"), v.replace("वह", "उस"), v.replace("कोई", "किसी"),
                        v.replace("ाया", "ाए")]
                if not any(strict(a, text) for a in alts):
                    seen[(kw, v, bid[1:])] += 1
    print("=====", f, len(seen))
    for (kw, v, b), c in sorted(seen.items()):
        print(f"  {b} {kw} = {v}")
