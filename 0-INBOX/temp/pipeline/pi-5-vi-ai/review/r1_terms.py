import sys, re, unicodedata
# usage: r1_terms.py term1|term2|...   (counts in pi-1..4 VI and my pi-5 chapters); -c N prints N contexts
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese"
files = {"pi1": BASE + r"\pi-1-vietnamese-plain.md", "pi2": BASE + r"\pi-2-vietnamese-plain.md",
         "pi3": BASE + r"\pi-3-vietnamese-plain.md", "pi4": BASE + r"\pi-4-vietnamese-plain.md",
         "c1": BASE + r"\pi-5-vietnamese-plain-rails_split_chapters\1-puggalakatha.md",
         "c2": BASE + r"\pi-5-vietnamese-plain-rails_split_chapters\2-parihanikatha.md"}
args = sys.argv[1:]
ctx = 0
if args and args[0] == "-c":
    ctx = int(args[1]); args = args[2:]
texts = {k: open(v, encoding="utf8").read() for k, v in files.items()}
for t in " ".join(args).split("|"):
    t = unicodedata.normalize("NFC", t.strip())
    print(t, ":", " ".join("%s=%d" % (k, x.count(t)) for k, x in texts.items()))
    if ctx:
        for k, x in texts.items():
            n = 0
            for m in re.finditer(re.escape(t), x):
                print("   ", k, "...", x[max(0, m.start() - 80):m.end() + 80].replace("\n", " / "))
                n += 1
                if n >= ctx:
                    break
