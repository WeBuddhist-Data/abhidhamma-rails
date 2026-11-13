"""Helper for 1-02..1-05: non-count clause patterns (items as placeholders).
usage: python -I -B -X utf8 analyze2_1-02_1-05.py <stem|all> [min]"""
import collections
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as S  # noqa: E402
import importlib.util  # noqa: E402
_sp = importlib.util.spec_from_file_location(
    "an", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails\analyze_1-02_1-05.py")
_an = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(_an)
ITEMS, FILES, lines = _an.ITEMS, _an.FILES, _an.lines

if __name__ == "__main__":
    stem = sys.argv[1]
    mn = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    stems = FILES if stem == "all" else [stem]
    c = collections.Counter()
    for s in stems:
        for ln in lines(s):
            if ln.startswith("#"):
                c["H| " + ln.lstrip("# ")] += 1
                continue
            t = ln
            for rx, ph in ITEMS:
                t = re.sub(rx, ph, t)
            for piece in re.split(r" – |; |\. |\.$|…pe…|…|, | \(\d+\)", t):
                piece = piece.strip()
                if not piece:
                    continue
                low = S.lower_initials(piece)
                if S.is_count(low) or S.is_count(low.split(" (")[0]):
                    continue
                c[piece] += 1
    for k, v in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])):
        if v >= mn:
            print(v, k)
