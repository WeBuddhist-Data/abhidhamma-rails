"""Compact view for part 2 decisions: runs senses_tool_pi1.show and prints only short snippets
around the headword (Pāli) and the value (Hindi). Usage: snip_part2.py hw value [maxsegs]"""
import io
import contextlib
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_pi1 as T

hw, val = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 3
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    T.show(hw, val, n)
probe = val.split(' … ')[0]
for line in buf.getvalue().splitlines():
    if line.startswith('P: '):
        s = line[3:]
        i = s.lower().find(hw.lower())
        print('  P: …' + s[max(0, i - 70):i + len(hw) + 70] + '…')
    elif line.startswith('H: '):
        s = line[3:]
        i = s.find(probe)
        print('  H: …' + s[max(0, i - 70):i + len(probe) + 70] + '…')
    else:
        print(line[:400])
