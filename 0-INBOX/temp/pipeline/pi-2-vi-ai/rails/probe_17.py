"""probe helper for ch17: print Pāli + Vietnamese lines of a segment (by block id) from pi-2 or pi-1.
usage: python -I -X utf8 probe_17.py <book: 2|1> <file.md> <id> [<id> ...]   (id without caret, e.g. 2-830)
       python -I -X utf8 probe_17.py grep <book> <file.md> <regex>   (Pāli lines matching, with the Vietnamese line)
Reads only the Pāli split chapters and OUR rails outputs (pi-1 / pi-2 Vietnamese rails). Writes nothing."""
import pathlib
import re
import sys

R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
DIRS = {"2": (R / "pali" / "pi-2_split_chapters", R / "vietnamese" / "pi-2-vietnamese-plain-rails_split_chapters"),
        "1": (R / "pali" / "pi-1_split_chapters", R / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters")}


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").split("\n") if ln.strip()]


def main():
    a = sys.argv[1:]
    if a[0] == "find":   # find <regex> [max]: every pi-1 and pi-2 (ch1-16) Pāli line matching, Pāli context + Vietnamese
        rx = re.compile(a[1])
        mx = int(a[2]) if len(a) > 2 else 6
        n = 0
        for book in ("1", "2"):
            pd, vd = DIRS[book]
            for f in sorted(pd.glob("*.md")):
                if book == "2" and f.name.startswith(("17-", "18-")):
                    continue
                vf = vd / f.name
                if not vf.exists():
                    continue
                P, V = lines(f), lines(vf)
                for i, ln in enumerate(P):
                    m = rx.search(ln)
                    if m and n < mx:
                        n += 1
                        print(f"[{book}] {f.name} line {i}: P: …{ln[max(0, m.start() - 120):m.end() + 200]}…")
                        print("V:", V[i] if i < len(V) else "<none>")
                        print()
        return
    if a[0] == "grep":
        pd, vd = DIRS[a[1]]
        P, V = lines(pd / a[2]), lines(vd / a[2])
        rx = re.compile(a[3])
        for i, ln in enumerate(P):
            if rx.search(ln):
                print("P:", ln)
                print("V:", V[i] if i < len(V) else "<none>")
                print()
        return
    pd, vd = DIRS[a[0]]
    P, V = lines(pd / a[1]), lines(vd / a[1])
    for sid in a[2:]:
        end = [i for i, ln in enumerate(P) if ln.endswith("^" + sid)]
        if not end:
            print("no", sid)
            continue
        e = end[0]
        s = e
        while s > 0 and not re.search(r"\^\S+$", P[s - 1]):
            s -= 1
        for i in range(s, e + 1):
            print("P:", P[i])
            print("V:", V[i] if i < len(V) else "<none>")
        print()


if __name__ == "__main__":
    main()
