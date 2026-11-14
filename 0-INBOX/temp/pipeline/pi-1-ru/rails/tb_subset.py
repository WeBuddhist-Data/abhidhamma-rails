"""Print termbase entries whose key occurs (word-bounded) in the given Pali file(s).
Usage: python -I -X utf8 tb_subset.py out.txt file1 [file2 ...]
Also lists Pali tokens with no exact termbase key."""
import re, sys
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / r"AI_translation\russian\pi-1-pali-russian-termbase-plain.md"


def load_tb():
    d = {}
    for line in TB.read_text(encoding="utf-8").splitlines():
        if ": {" not in line:
            continue
        k, v = line.split(": {", 1)
        d[k.strip()] = v.rstrip("}")
    return d


def main():
    out = Path(sys.argv[1])
    text = "\n".join(Path(f).read_text(encoding="utf-8") for f in sys.argv[2:])
    text = re.sub(r"\^\S+", " ", text)
    low = text.lower()
    tb = load_tb()
    lines = []
    found = set()
    for k, v in tb.items():
        kl = k.lower()
        if re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kl) + r"(?![\wāīūṃṅñṭḍṇḷ])", low):
            lines.append(f"{k}: {v}")
            found.add(kl)
    toks = sorted(set(re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", low)))
    missing = [t for t in toks if t not in found]
    lines.append("\n## TOKENS WITHOUT EXACT KEY")
    lines.append(" ".join(missing))
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(len(lines), "entries;", len(missing), "tokens without key")


if __name__ == "__main__":
    main()
