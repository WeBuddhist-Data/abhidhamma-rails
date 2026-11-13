"""Segments whose Pāli has «cakkhunā rūpaṃ» (the visible object): rūpaṃ keyword count, Pāli rūpaṃ count, values."""
import sys, pathlib, re
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
for f in sys.argv[1:]:
    pa, hi = read_pali(f), read_hindi(f)
    mp = {}
    for l in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        b, _, r = l.partition("] ")
        mp[b[1:]] = [p.split("=", 1) for p in r.split(", ")] if r else []
    for b, prs in mp.items():
        p = pa.get(b, "")
        if "cakkhunā rūpaṃ" in p or "cakkhunā rūpa" in p:
            vals = [v for k, v in prs if k == "rūpaṃ"]
            print(f[:4], b, "Pāli rūpaṃ:", len(re.findall(r"\brūpaṃ\b", p)), "| cakkhunā rūpaṃ:",
                  p.count("cakkhunā rūpaṃ"), "| kw:", vals, "| HI भौतिक रूप:", hi.get(b, "").count("भौतिक रूप"))
