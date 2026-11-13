"""Helper for the pi-7 sample: prior Hindi values (pi-1..6 maps) and English pi-7 map lines.
usage: python -I -B -X utf8 probe_sample_hi.py prior kw1 kw2 ...
       python -I -B -X utf8 probe_sample_hi.py en id1 id2 ...
       python -I -B -X utf8 probe_sample_hi.py uniq <file>     (unique keywords of a keyword file with prior values)
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
HI = ROOT / "AI_translation" / "hindi"
EN = ROOT / "AI_translation" / "english" / "pi-7-keywords-by-reference-pali-english-plain.md"


def lc(k):
    return k[:1].lower() + k[1:]


def load_prior():
    pr = collections.defaultdict(collections.Counter)
    for n in range(1, 7):
        p = HI / f"pi-{n}-keywords-by-reference-pali-hindi-plain.md"
        for line in p.read_text(encoding="utf-8").splitlines():
            if "] " in line:
                for pair in line.split("] ", 1)[1].split(", "):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        pr[lc(k.strip())][(n, v)] += 1
    return pr


def main():
    mode, args = sys.argv[1], sys.argv[2:]
    if mode == "prior":
        pr = load_prior()
        for k in args:
            print(k, "->", dict(pr.get(lc(k), {})) or "-")
    elif mode == "en":
        want = set(args)
        for line in EN.read_text(encoding="utf-8").splitlines():
            if line.split("] ", 1)[0][1:] in want:
                print(line)
    elif mode == "uniq":
        pr = load_prior()
        seen = collections.Counter()
        for line in (HERE / f"{args[0]}.keywords.md").read_text(encoding="utf-8").splitlines():
            if "] " in line:
                for k in line.split("] ", 1)[1].split(", "):
                    seen[k.strip()] += 1
        for k, c in sorted(seen.items(), key=lambda x: lc(x[0])):
            p = pr.get(lc(k), {})
            top = ", ".join(f"pi{n}:{v}({c2})" for (n, v), c2 in sorted(p.items(), key=lambda x: -x[1])[:4])
            print(f"{k} [{c}] {top}")


if __name__ == "__main__":
    main()
