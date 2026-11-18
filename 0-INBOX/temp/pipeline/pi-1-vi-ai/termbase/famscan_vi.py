"""Family scan for the pi-1 Vietnamese termbase: groups one-word headwords by a crude Pāli stem and prints
groups whose chosen terms (decisions applied; nominaliser/classifier words stripped) differ.
usage: python -I -X utf8 famscan_vi.py [min_group_size]"""
import collections, pathlib, re, sys, unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_vi as T

ENDINGS = sorted("""ṃ aṃ ā o e ena assa āya āni ehi esu ānaṃ ānī āyo āhi āsu ī iṃ inā ino ayo uṃ ū ūni unā ussa uno
ato ito tā tāya taṃ ti nti nanti anti ā ca ñca meva eva va pi""".split(), key=len, reverse=True)
STRIP = re.compile(r"\b(sự|các|những|loại|có|niềm|trạng thái|việc|một|đã|được|nào|là)\b\s*")


def stem(hw):
    h = unicodedata.normalize("NFC", hw.lower())
    for _ in range(2):
        for e in ENDINGS:
            if len(h) - len(e) >= 4 and h.endswith(e):
                h = h[: -len(e)]
                break
    return h


def norm(t):
    return re.sub(r"\s+", " ", STRIP.sub("", t)).strip(" …")


def main():
    mn = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    ss, dec = T.senses(), T.decisions()
    groups = collections.defaultdict(list)
    for hw, s in ss:
        if " " in hw:
            continue
        for i, (tag, c) in enumerate(s):
            k = f"{hw}|{i}"
            term = dec[k][0] if k in dec else c[0]
            groups[stem(hw)].append((k, tag, term))
    for st, rows in sorted(groups.items()):
        if len(rows) < mn:
            continue
        terms = {norm(t) for _, _, t in rows}
        if len(terms) > 1:
            print(f"== {st}")
            for k, tag, t in rows:
                print(f"   {k}\t{t}\t[{tag[:70]}]")


if __name__ == "__main__":
    main()
