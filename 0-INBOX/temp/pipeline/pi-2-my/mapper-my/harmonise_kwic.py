"""Keyword-in-context: for a keyword, every segment that uses it, with its value and ±W characters of Burmese
around the first chunk of the value (and of the Pāli around the keyword).
usage: python3 -I -X utf8 harmonise_kwic.py KW [W] [VALUE-filter]"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from harmonise_show import segments, MY, PI  # noqa: E402
kw = sys.argv[1]; W = int(sys.argv[2]) if len(sys.argv) > 2 else 60
vf = sys.argv[3] if len(sys.argv) > 3 else None
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name[:-len(".mapped.md")]
    my = pa = None
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1); sid = sid[1:]
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if k[:1].lower() + k[1:] != kw[:1].lower() + kw[1:] or (vf and v != vf):
                continue
            if my is None:
                my = segments(MY / f"{ch}.md"); pa = segments(PI / f"{ch}.md")
            t = my[sid]; p = pa.get(sid, "")
            c = v.split(" … ")[0].split()[0] if v != "(no direct equivalent)" else ""
            c = re.sub("(သော|သည်)$", "", c) or c
            i = t.find(c) if c else -1
            j = p.find(k)
            print(f"{sid:12} {v}\n    MY …{t[max(0, i - W):i + W + len(c)] if i >= 0 else t[:2 * W]}…\n"
                  f"    PA …{p[max(0, j - W):j + W + len(k)] if j >= 0 else p[:2 * W]}…")
