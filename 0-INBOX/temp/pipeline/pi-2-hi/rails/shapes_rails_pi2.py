"""Count Hindi shapes (regex matches) per chapter on lines whose aligned Pāli matches a regex.

usage: python -I -X utf8 shapes_rails_pi2.py <pali-regex> <hindi-regex> [--pi1] [--top N] [--bak]
"""
import collections, os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = ROOT + r"\AI_translation\pali\pi-2_split_chapters"
HDIR = ROOT + r"\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
BAK = ROOT + r"\0-INBOX\temp\pipeline\pi-2-hi\rails\backup-pre-align"
PI1P = ROOT + r"\AI_translation\pali\pi-1_split_chapters"
PI1H = ROOT + r"\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def main():
    a = sys.argv[1:]
    pi1 = "--pi1" in a
    top = int(a[a.index("--top") + 1]) if "--top" in a else 40
    hd = BAK if "--bak" in a else HDIR
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and not (i > 0 and a[i - 1] == "--top")]
    prx, hrx = re.compile(pos[0]), re.compile(pos[1])
    pd, hd = (PI1P, PI1H) if pi1 else (PDIR, hd)
    tot = collections.Counter()
    per = collections.defaultdict(collections.Counter)
    for f in sorted(os.listdir(pd)):
        if not f.endswith(".md") or not os.path.exists(os.path.join(hd, f)):
            continue
        tag = f.split("-")[0] if not pi1 else f[:-3]
        for p, h in zip(lines(os.path.join(pd, f)), lines(os.path.join(hd, f))):
            if prx.search(p):
                for m in hrx.finditer(h):
                    s = m.group(1) if m.groups() else m.group(0)
                    tot[s] += 1
                    per[s][tag] += 1
    for s, n in tot.most_common(top):
        print(f"{n:5d}  {s}   [{', '.join(f'{k}:{v}' for k, v in sorted(per[s].items(), key=lambda kv: -kv[1]))}]")


if __name__ == "__main__":
    main()
