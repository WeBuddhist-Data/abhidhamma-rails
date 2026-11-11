import pathlib,re
R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails/AI_translation/hindi/pi-1-hindi-plain-rails_split_chapters")
want = {"3-02-rupakandam.md":["1-636","1-641","1-642","1-643","1-644","1-651","1-652","1-680","1-696","1-728","1-729"],
"3-03-rupakandam.md":["1-750","1-765","1-786","1-789","1-810","1-858","1-882","1-884","1-885","1-895","1-902","1-904","1-945","1-953","1-966","1-967","1-969","1-974","1-983","1-984","1-984"]}
for f,ids in want.items():
    t=(R/f).read_text(encoding="utf-8")
    for b in t.split("\n\n"):
        m=re.search(r"\^([0-9A-Za-z-]+)\s*$",b)
        if m and m.group(1) in ids: print(b[:520]); print()
    print("bad:", [x for x in ("seed","—",":-") if x in t], "dbl:", "\n\n\n" in t)
