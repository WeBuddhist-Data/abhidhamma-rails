"""Helper: print Pāli, Burmese and keywords per segment of one chapter.
usage: python3 -I -X utf8 show_seg.py <ch> [first_id_index] [count]"""
import re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-1_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = "\n".join(buf)
            buf = []
    return out


ch = sys.argv[1]
a = int(sys.argv[2]) if len(sys.argv) > 2 else 0
n = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
my, pa = segments(MY / f"{ch}.md"), segments(PI / f"{ch}.md")
rows = [l.split("] ", 1) for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()]
for sid, kws in rows[a:a + n]:
    sid = sid[1:]
    print(f"=== {sid}\nPI: {pa.get(sid, '')}\nMY: {my[sid]}\nKW: {kws}\n")
