import sys, re, glob, os
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-1-russian-plain-rails_split_chapters"
files = sys.argv[1:]
for f in files:
    t = open(os.path.join(base, f), encoding="utf-8").read()
    c1 = len(re.findall(r", – это", t)); c2 = len(re.findall(r"[^,] – это", t))
    print(f, "comma+dash:", c1, "nocomma dash:", c2)
    if len(sys.argv) > 2 and f.startswith("3-"):
        pass
