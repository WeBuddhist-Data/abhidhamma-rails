"""Part-3 helper: rough lemma groups (single-word headwords, case endings stripped) that touch senses-file lines
lo..hi and carry more than one Hindi term (decision if any, else first candidate). For spotting drift only.

usage: python -I -X utf8 p3_fam.py <lo> <hi>
"""
import collections, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\termbase")
import tb_tool_pi1 as tb  # noqa: E402

ENDS = sorted(["ṃ", "o", "ā", "a", "e", "aṃ", "āni", "ānaṃ", "ena", "assa", "āya", "esu", "ehi", "ato", "ā", "ī", "i",
               "u", "ū", "inaṃ", "ino", "uno", "āsu", "āyo", "iyo", "ūni", "īnaṃ", "ūnaṃ", "isu", "usu", "to"],
              key=len, reverse=True)


def stem(hw):
    w = hw.lower()
    for suf in ("nti", "ñca", "ñceva", "meva", "ti", "ca", "eva"):
        if w.endswith(suf) and len(w) > len(suf) + 3:
            w = w[: -len(suf)]
            break
    for e in ENDS:
        if w.endswith(e) and len(w) > len(e) + 2:
            return w[: -len(e)]
    return w


def main(a):
    lo, hi = int(a[0]), int(a[1])
    ss, dec = tb.senses(), tb.decisions()
    groups = collections.defaultdict(list)
    for n, (hw, s) in enumerate(ss, 1):
        if " " in hw:
            continue
        for i, (tag, c) in enumerate(s):
            k = f"{hw}|{i}"
            t = dec[k][0] if k in dec else c[0]
            groups[stem(hw)].append((n, k, tag, t, len(c)))
    for st, g in sorted(groups.items()):
        if not any(lo <= n <= hi for n, *_ in g):
            continue
        if len({t for *_, t, _ in g}) < 2:
            continue
        print(f"== {st}")
        for n, k, tag, t, nc in g:
            print(f"  {n}\t{k}\t{t}\t[{nc}]\t{tag[:70]}")


if __name__ == "__main__":
    main(sys.argv[1:])
