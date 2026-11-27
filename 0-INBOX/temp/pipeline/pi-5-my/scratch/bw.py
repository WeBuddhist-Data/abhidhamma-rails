"""scratch: Burmese regex -> counts of context snippets (and chapters). usage: bw.py REGEX [W]"""
import pathlib, re, sys, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
MD = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
rx = re.compile(sys.argv[1]); w = int(sys.argv[2]) if len(sys.argv) > 2 else 25
c = collections.Counter(); ch = collections.defaultdict(set)
for p in MD.glob("*.md"):
    for l in p.read_text(encoding="utf-8").split("\n"):
        for m in rx.finditer(l):
            k = l[max(0, m.start() - w):m.end() + w]; c[k] += 1; ch[k].add(p.name.split("-")[0].split(".")[0])
for k, n in c.most_common(60): print(n, sorted(ch[k], key=lambda x: int(x) if x.isdigit() else 0), k)
