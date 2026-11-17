# cross-book view for pi-2: senses whose chosen term differs from the approved pi-1 Russian termbase term for the
# same headword with the SAME sense tag (mode "pi1"), or from every term pi-1/3/4/5 give the headword (mode "all").
# usage: python -I -X utf8 crossbook_ru.py [pi1|all]
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\termbase")
import tb_tool_ru as T

mode = sys.argv[1] if len(sys.argv) > 1 else "pi1"
dec = T.decisions()
pi1 = {}
for l in T.PRIOR[1].read_text(encoding="utf-8").splitlines():
    if ": {" in l:
        hw, ss = T.parse(l)
        for tag, c in ss:
            pi1[(hw.lower(), tag)] = c[0]
pr = T.prior()
for hw, s in T.senses():
    for i, (tag, c) in enumerate(s):
        k = f"{hw}|{i}"
        t = dec[k][0] if k in dec else c[0]
        if mode == "pi1":
            p = pi1.get((hw.lower(), tag))
            if p is not None and p != t:
                print(f"{k}\t{t}\tpi-1: {p}\t[{tag[:70]}]")
        elif mode == "agree":
            p = [x for x in pr.get(hw.lower(), []) if not x.startswith("pi-1 ")]
            books = {x.split(" ", 1)[0] for x in p}
            terms = {x.split(" = ", 1)[1] for x in p}
            if len(s) == 1 and len(books) >= 2 and len(terms) == 1 and t not in terms:
                print(f"{k}\t{t}\t{'/'.join(sorted(books))}: {terms.pop()}\t[{tag[:60]}]")
        else:
            p = pr.get(hw.lower())
            if p and t not in {x.split(' = ', 1)[1] for x in p}:
                print(f"{k}\t{t}\t[{tag[:60]}]")
                for x in p:
                    print(f"      {x}")
