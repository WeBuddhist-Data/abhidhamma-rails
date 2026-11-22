"""r3: list TS / our questions for a given key, to debug r3_tscmp matching. Console only.
usage: r3_tskey.py kind frame pol n1(comma) n2"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
sys.argv, args = [sys.argv[0]], sys.argv[1:]
import importlib.util
spec = importlib.util.spec_from_file_location("cmp", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review\r3_tscmp.py")
src = open(spec.origin, encoding="utf-8").read().replace("\nmain()\n", "\n")
ns = {}
exec(compile(src, spec.origin, "exec"), ns)
key = (args[0], args[1], args[2], tuple(args[3].split(",")), args[4])
for lab, ts, stream in (("TS", True, ns["ts_stream"]()), ("OURS", False, ns["our_stream"]())):
    for r in ns["parse"](stream, ts):
        if r[1] == key:
            print(lab, r[0], r[2], "|", r[4][:160], "||", r[5][:200])
