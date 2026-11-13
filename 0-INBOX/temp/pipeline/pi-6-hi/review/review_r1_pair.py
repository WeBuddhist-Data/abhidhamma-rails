"""r1 review helper: print aligned Pali/Hindi non-empty lines side by side.
usage: python -I -B -X utf8 review_r1_pair.py <file-stem> [start] [end] [--dedupe] [--out file]
(start/end are 1-based non-empty line numbers)
--dedupe: skip a pair whose (Pali, Hindi) text (block ID stripped) was already printed;
          if the same Pali was seen with a DIFFERENT Hindi, print it marked INCONSISTENT."""
import sys, os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PI = os.path.join(ROOT, "pali", "pi-6_split_chapters")
HI = os.path.join(ROOT, "hindi", "pi-6-hindi-plain-rails_split_chapters")
IDRE = re.compile(r"\s*\^[\w-]+\s*$")


def load(path):
    with open(path, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if l.strip()]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dedupe = "--dedupe" in sys.argv
    out = None
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
        args = [a for a in args if a != out]
    stem = args[0]
    p = load(os.path.join(PI, stem + ".md"))
    h = load(os.path.join(HI, stem + ".md"))
    s = int(args[1]) if len(args) > 1 else 1
    e = int(args[2]) if len(args) > 2 else len(p)
    lines = []
    if len(p) != len(h):
        lines.append(f"LINE COUNT MISMATCH {len(p)} {len(h)}")
    seen = {}
    skipped = 0
    for i in range(s - 1, min(e, len(p))):
        pk = IDRE.sub("", p[i])
        hk = IDRE.sub("", h[i]) if i < len(h) else "<none>"
        tag = ""
        if dedupe:
            if pk in seen:
                if hk in seen[pk]:
                    skipped += 1
                    continue
                tag = " [INCONSISTENT vs earlier]"
                seen[pk].add(hk)
            else:
                seen[pk] = {hk}
        lines.append(f"{i+1} P: {p[i]}{tag}")
        lines.append(f"{i+1} H: {h[i] if i < len(h) else '<none>'}")
    lines.append(f"(skipped {skipped} repeated pairs)")
    txt = "\n".join(lines)
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(txt + "\n")
    else:
        print(txt)


if __name__ == "__main__":
    main()
