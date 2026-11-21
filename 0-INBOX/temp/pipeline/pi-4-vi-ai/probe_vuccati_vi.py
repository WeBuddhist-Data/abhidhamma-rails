"""Probe: the naming frame «ayaṃ vuccati puggalo X» / «ime vuccanti puggalā X» / «… vuccati X» per chapter.
Classifies each Pāli occurrence by (dash before it?, quotes around the name?) and the Vietnamese clause found in
the aligned sentence (or, when sentences do not align, the n-th naming clause of the line).

usage: python -I -X utf8 probe_vuccati_vi.py [--bak] [--list]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments, short, norm

if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
P = re.compile(r'(–\s*)?\b([Aa]yaṃ|[Ii]daṃ|[Ii]me|[Ii]māni|[Tt]e|[Ss]o)\s+vucca(?:ti|nti)\s*(puggal[oā]\s*)?("[^"]*"|[^.;?]*)')
V = re.compile(r'(–\s*)?((?:[Nn]hững người này|[Nn]gười này|[Đđ]ó|[Đđ]iều này|[Nn]hững hiện tượng này|[Hh]ọ)'
               r' được gọi là|là) (“[^”]*”|[^.;?]*)')
stats = collections.Counter()
rows = []
for part in PARTS:
    for sid, ps, vs in segments(part):
        for i, (p, v) in enumerate(zip(ps, vs)):
            mp = list(P.finditer(p))
            if not mp:
                continue
            mv = [m for m in V.finditer(v) if "được gọi là" in m.group(2)]
            for k, m in enumerate(mp):
                dash = bool(m.group(1))
                quoted = m.group(4).startswith('"')
                person = bool(m.group(3))
                vm = mv[k] if k < len(mv) else None
                vform = "—none—"
                if vm:
                    vform = ("–" if vm.group(1) else "") + vm.group(2) + (" “…”" if vm.group(3).startswith("“") else " (no quotes)")
                key = (short(part), "dash" if dash else "nodash", "quoted" if quoted else "plain",
                       "person" if person else "thing", vform)
                stats[key] += 1
                rows.append((f"{short(part)}:{sid}.{i+1}", m.group(0)[:90], vm.group(0)[:90] if vm else "—none—"))
for k, n in sorted(stats.items(), key=lambda kv: (len(kv[0][0]), kv[0])):
    print(n, *k)
if "--list" in sys.argv:
    for r in rows:
        print(*r, sep=" | ")
