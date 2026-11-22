"""Probe aligned Pāli / Vietnamese lines of the pi-6 zero-shot.

usage: python -I -X utf8 -B probe_vi.py [--p REGEX] [--v REGEX] [--parts 9-01,9-02] [--max N] [--w WIDTH] [--bak] [--count]
Prints file:block, the Pāli line and the Vietnamese line (cut to WIDTH around the first match).
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common as V


def arg(name, default=None):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


def cut(s, rx, w):
    if len(s) <= w:
        return s
    m = rx.search(s) if rx else None
    a = max(0, (m.start() if m else 0) - w // 3)
    return ("…" if a else "") + s[a:a + w] + ("…" if a + w < len(s) else "")


def main():
    prx = re.compile(arg("--p")) if arg("--p") else None
    vrx = re.compile(arg("--v")) if arg("--v") else None
    parts = arg("--parts")
    mx = int(arg("--max", "40"))
    w = int(arg("--w", "300"))
    if "--bak" in sys.argv:
        V.CUR["vdir"] = V.BAK
    sel = [p for p in V.PARTS if not parts or V.short(p) in parts.split(",")]
    n = 0
    cnt = collections.Counter()
    for part in sel:
        for sid, ps, vs in V.segments(part):
            for i, (p, v) in enumerate(zip(ps, vs)):
                if prx and not prx.search(p):
                    continue
                if vrx and not vrx.search(v):
                    continue
                k = len(vrx.findall(v)) if vrx else 1
                cnt[V.short(part)] += k
                n += 1
                if "--ctx" in sys.argv and vrx:
                    for m in vrx.finditer(v):
                        print(f"{V.short(part)}:{sid}.{i} …{v[max(0, m.start() - w):m.start()]}[[{m.group(0)}]]{v[m.end():m.end() + 40]}…")
                    continue
                if n <= mx and "--count" not in sys.argv:
                    print(f"== {V.short(part)}:{sid}.{i}")
                    print("  P:", cut(p, prx, w))
                    print("  V:", cut(v, vrx or None, w))
    print("lines", n, "per chapter (matches):", dict(cnt))


if __name__ == "__main__":
    main()
