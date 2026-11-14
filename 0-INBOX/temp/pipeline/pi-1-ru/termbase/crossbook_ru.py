# cross-book view: pi-1 headwords whose chosen term is not among the terms the pi-3/4/5 Russian termbases give
# the same headword. usage: python -I -X utf8 crossbook_ru.py
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\termbase")
import tb_tool_ru as T

dec = T.decisions()
pr = T.prior()
for hw, s in T.senses():
    p = pr.get(hw.lower())
    if not p:
        continue
    pterms = {x.split(" = ", 1)[1] for x in p}
    for i, (tag, c) in enumerate(s):
        k = f"{hw}|{i}"
        t = dec[k][0] if k in dec else c[0]
        if t not in pterms:
            print(f"{k}\t{t}\t[{tag[:60]}]")
            for x in p:
                print(f"      {x}")
