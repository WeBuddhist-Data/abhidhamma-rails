"""Print the termbase entries of every keyword in a range of segments, or of given words.

usage:
  python -I -X utf8 tb_lookup_sample.py ids <id-prefix-or-regex> [...]   (keywords of matching segment IDs)
  python -I -X utf8 tb_lookup_sample.py words <word> [...]               (exact headwords, case-insensitive)
  python -I -X utf8 tb_lookup_sample.py grep <regex>                     (headwords matching regex)
"""
import re, sys, pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation/hindi/pi-6-pali-hindi-termbase-plain.md"


def load_tb():
    tb = {}
    for line in TB.read_text(encoding="utf-8").splitlines():
        if ": {" not in line:
            continue
        w, body = line.split(": {", 1)
        tb[w] = body[:-1]
    return tb


def main():
    mode, args = sys.argv[1], sys.argv[2:]
    tb = load_tb()
    tbl = {k.lower(): (k, v) for k, v in tb.items()}
    if mode == "ids":
        pats = [re.compile(a) for a in args]
        seen = {}
        for line in KW.read_text(encoding="utf-8").splitlines():
            i, body = line.split("] ", 1)
            i = i[1:]
            if not any(p.fullmatch(i) for p in pats):
                continue
            for k in body.split(", "):
                for kk in k.split(" / "):
                    seen.setdefault(kk.lower(), kk)
        for kl in sorted(seen):
            hit = tbl.get(kl)
            print(f"{seen[kl]}: {hit[1] if hit else '-- NOT IN TERMBASE'}")
    elif mode == "words":
        for a in args:
            hit = tbl.get(a.lower())
            print(f"{a}: {hit[1] if hit else '-- NOT IN TERMBASE'}")
    elif mode == "grep":
        p = re.compile(args[0])
        for k, v in tb.items():
            if p.search(k):
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
