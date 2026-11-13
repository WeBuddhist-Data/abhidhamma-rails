"""Copy non-empty lines a..b (1-based) of a Pāli file, keeping the blank lines between them exactly."""
import sys


def extract(src, a, b):
    lines = open(src, encoding="utf-8").read().split("\n")
    out, n = [], 0
    started = False
    for ln in lines:
        if ln.strip():
            n += 1
            if n > b:
                break
            if n >= a:
                started = True
                out.append(ln)
        elif started:
            out.append(ln)
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    src, a, b, dst = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    open(dst, "w", encoding="utf-8", newline="\n").write(extract(src, a, b))
