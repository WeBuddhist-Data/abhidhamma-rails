import re, pathlib
H = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
nb = lambda p: [l for l in p.read_text(encoding="utf-8").replace("\r\n","\n").split("\n") if l.strip()]
o = nb(H / "0-INBOX/temp/pipeline/split-sync/backup-pre-sync/pi-2_split_chapters/16-nanavibhango.md")
e = nb(H / "AI_translation/english/pi-2-english-plain-zeroshot_split_chapters/16-nanavibhango.md")
segs = lambda ls: [(m.group(1), k) for k, l in enumerate(ls) if (m := ID.search(l))]
so, se = segs(o), segs(e)
print(len(so), len(se), [x[0] for x in so] == [x[0] for x in se])
prev_o = prev_e = -1
for (io, ko), (ie, ke) in zip(so, se):
    if ko - prev_o != ke - prev_e:
        print("segment", io, "pali lines", ko - prev_o, "en lines", ke - prev_e)
        for l in o[prev_o+1:ko+1]: print("  P:", l[:110])
        for l in e[prev_e+1:ke+1]: print("  E:", l[:110])
        break
    prev_o, prev_e = ko, ke
