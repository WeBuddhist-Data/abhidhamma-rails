"""Probe for chapter 5 (Aṭṭhakathākaṇḍaṃ): which Pāli lines repeat a 4-0x line verbatim, and the matrix keys.
Writes nothing.  usage: python -I -X utf8 probe_5_vi.py
"""
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402

_spec = importlib.util.spec_from_file_location("build_rails_4_02_4_03_vi", HERE / "build_rails_4-02_4-03_vi.py")
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)
F = G.F
B = G.B
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")

reuse = {}
for part in ("4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"):
    ps = S.segments(S.PALI / part)
    vs = S.segments(S.OUT / part)
    for (a, pl), (b, vl) in zip(ps, vs):
        assert a == b and len(pl) == len(vl)
        for x, y in zip(pl, vl):
            reuse.setdefault(ID.sub("", x), ID.sub("", y))

segs = S.segments(S.PALI / "5-atthakathakandam.md")
n_re = 0
for sid, lines in segs:
    for x in lines:
        x = ID.sub("", x)
        if x in reuse:
            n_re += 1
            print("REUSE", sid, "|", reuse[x][:100])
print("reused lines:", n_re, "of", sum(len(l) for _, l in segs), "segments", len(segs))

qs = set()
for sid, lines in segs:
    for x in lines:
        m = re.match(r"Katame dhammā (.+?)[?.]", x)
        if m:
            qs.add(m.group(1))
for q in sorted(qs):
    print("Q", q, "=>", F.pred(q) if (q in S.PREDS or q in F.PRED_X) else "MISSING")
for k in ("oghā…pe…", "yogā…pe…"):
    pass
print("ARUPA", B.ARUPA)
print("SAB", F.SAB, "| RUPA", G.R.RUPA, "| KAMMA", G.Q.KAMMA, "| NA_KAMMA", G.Q.NA_KAMMA)
print("YANCA", F.YANCA)
print("FN keys", [k for k in S.FN if k in ("vitakko", "vicāro", "pīti", "sukhaṃ", "sammādiṭṭhi")])
print("NAMES upekkha", B.NAMES.get("upekkhā"), "| cittaṃ", B.NAMES.get("cittaṃ"))
print("SPH", F.sph_vi("Kāmāvacarā, arūpāvacarā, apariyāpannā"))
print("QV", F.QV)
for k in ("asaṅkhatā", "sappaccayā", "na hetū sahetukā", "hetū ceva sahetukā ca", "kenaci viññeyyā",
          "dassanena pahātabbā", "niyatā", "aniyatā", "uppādino", "maggādhipatino", "maggahetukā", "anārammaṇā",
          "ajjhattabahiddhā", "savitakkasavicārā"):
    print("P", k, "=>", S.PREDS.get(k))
