"""Part 2 helper: for hw=value, print Pali windows around hw and Hindi windows around a probe, for the first n segments.
Usage: python -I -B -X utf8 part2_ctx.py <hw> <value or -> <n> <hindi probe or -> [more quadruples]"""
import io
import os
import re
import sys
import contextlib

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_pi7 as T  # noqa: E402

W = 90


def ids_of(hw, value):
    out = []
    with open(T.MAP, encoding='utf-8-sig') as f:
        for line in f:
            if '] ' not in line:
                continue
            i, body = line.rstrip('\n').split('] ', 1)
            for pair in body.split(', '):
                k, _, v = pair.partition('=')
                if k.lower() == hw.lower() and (value is None or v == value):
                    if i[1:] not in out:
                        out.append(i[1:])
    return out


def win(text, probe):
    i = text.lower().find(probe.lower()) if probe else -1
    if i < 0:
        return None
    return text[max(0, i - W):i + len(probe) + W]


def run(hw, value, n, probe):
    ids = ids_of(hw, value)
    print(f'== {hw}={value}: {len(ids)} segs: {" ".join(ids[:40])}')
    want = ids[:n]
    idre = re.compile(r'\^([0-9A-Za-z-]+)\s*$')
    for name in sorted(os.listdir(T.PDIR)):
        if not name.endswith('.md') or not want:
            continue
        p = T._lines(os.path.join(T.PDIR, name))
        h = T._lines(os.path.join(T.HDIR, name))
        if len(p) != len(h):
            continue
        bp, bh = [], []
        for a, b in zip(p, h):
            bp.append(a)
            bh.append(b)
            m = idre.search(a)
            if m:
                if m.group(1) in want:
                    print(f'--- ^{m.group(1)}')
                    for x, y in zip(bp, bh):
                        px = win(x, hw)
                        if px is None:
                            continue
                        print('P: ' + px)
                        hy = win(y, probe) if probe else None
                        print('H: ' + (hy if hy else y[:2 * W]))
                bp, bh = [], []


if __name__ == '__main__':
    a = sys.argv[1:]
    for k in range(0, len(a), 4):
        run(a[k], None if a[k + 1] == '-' else a[k + 1], int(a[k + 2]), None if a[k + 3] == '-' else a[k + 3])
        print()
