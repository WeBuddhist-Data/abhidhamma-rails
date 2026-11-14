"""Extra checks for Russian rails files against their Pāli.
usage: python -I -X utf8 extra_checks.py <pali> <russian> [<pali> <russian> ...]
Checks: block IDs equal and in order, per-segment line counts, no CR, no double blank lines,
no «ли» word, no Latin letters outside [...] brackets, no ":-", no em dash."""
import re, sys
from pathlib import Path

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(text):
    out, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), len(buf)))
            buf = []
    return out


def check(p, r):
    pt = Path(p).read_text(encoding="utf-8")
    rb = Path(r).read_bytes()
    rt = rb.decode("utf-8")
    errs = []
    sp, sr = segs(pt), segs(rt)
    if [i for i, _ in sp] != [i for i, _ in sr]:
        errs.append("ID order/set differs")
    elif sp != sr:
        errs.append("line counts differ: " + str([i for (i, a), (_, b) in zip(sp, sr) if a != b][:5]))
    if b"\r" in rb:
        errs.append("CR present")
    if "\n\n\n" in rt:
        errs.append("double blank line")
    if re.search(r"(?i)(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", rt):
        errs.append("«ли» found")
    if ":-" in rt or "—" in rt:
        errs.append("':-' or em dash")
    for n, line in enumerate(rt.splitlines(), 1):
        stripped = re.sub(r"\[[^\]]*\]", "", ID.sub("", line))
        if re.search(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]", stripped):
            errs.append(f"Latin outside brackets, line {n}: {stripped[:80]}")
            break
    print(f"{Path(r).name}: {len(sr)} segments; " + ("OK" if not errs else "; ".join(errs)))


if __name__ == "__main__":
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        check(a[i], a[i + 1])
