import glob, re, sys
sys.stdout.reconfigure(encoding="utf-8")
root = sys.argv[1]
files = (glob.glob(root + r"\1-SOURCES\Translations\Thai\th-*-thai_tipitaka.md") + [root + r"\1-SOURCES\Translations\Vietnamese\vi-1-tinh_su.md"]
         + glob.glob(root + r"\0-INBOX\raw-data\th-*-raw.md") + [root + r"\0-INBOX\raw-data\vi-1-tinh_su-raw.md"]
         + glob.glob(root + r"\0-INBOX\temp\pipeline\*\*-fm*.txt"))
pat = re.compile(r'^title: "([^"(]+?)\s*\([^)]*\),\s*(?:Thai|Vietnamese) translation[^"]*"$', re.M)
for f in files:
    s = open(f, encoding="utf-8").read()
    s2, n = pat.subn(lambda m: f'title: "{m.group(1).strip()}"', s, count=1)
    if n:
        with open(f, "w", encoding="utf-8", newline="") as fh:
            fh.write(s2)
    print(n, f.split("\\")[-1])
t = root + r"\0-INBOX\temp\pipeline\th-tools\make_fm_th.py"
s = open(t, encoding="utf-8").read()
s2 = s.replace('title: "{th_title} ({pi_title}), Thai translation"', 'title: "{th_title}"')
with open(t, "w", encoding="utf-8", newline="") as fh:
    fh.write(s2)
print("template updated:", s != s2)