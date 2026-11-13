"""Sample helper: run senses_tool_pi7 show and print short windows (Pāli around the headword, Hindi around the value)."""
import io
import os
import re
import sys
import contextlib

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_pi7 as T  # noqa: E402

W = 110


def win(text, probe):
    i = text.lower().find(probe.lower()) if probe else -1
    if i < 0:
        return text[:2 * W]
    return ('…' if i > W else '') + text[max(0, i - W):i + len(probe) + W] + ('…' if i + len(probe) + W < len(text) else '')


def run(hw, value, n):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        T.show(hw, value, n)
    lines = buf.getvalue().splitlines()
    probe = value.split(' … ')[0] if value else None
    out = []
    for l in lines:
        if l.startswith('P: '):
            out.append('P: ' + win(l[3:], hw[:-2] if len(hw) > 4 else hw))
        elif l.startswith('H: '):
            out.append('H: ' + win(l[3:], probe))
        elif l.startswith('  '):
            out.append(l[:300])
        else:
            out.append(l)
    print('\n'.join(out))


if __name__ == '__main__':
    args = sys.argv[1:]
    # triples: hw value n ; value '-' = none
    for k in range(0, len(args), 3):
        v = args[k + 1]
        run(args[k], None if v == '-' else v, int(args[k + 2]))
        print()
