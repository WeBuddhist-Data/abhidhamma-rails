# read-only helper for the pi-6 Russian termbase (model: pi-2-ru/termbase/crossbook_ru.py).
# usage: python -I -X utf8 -B crossbook_ru.py all     senses whose chosen term is not among the approved pi-1 … pi-5
#                                                      terms for the same headword (prior terms listed under each)
#        python -I -X utf8 -B crossbook_ru.py fam [rx] tag-core groups (tag without the trailing grammar parenthesis and
#                                                      without the particle notes) whose chosen terms differ
import re, sys, collections
sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\termbase")
import tb_tool_ru as T

mode = sys.argv[1] if len(sys.argv) > 1 else "all"
dec = T.decisions()


def chosen(hw, i, c):
    k = f"{hw}|{i}"
    return dec[k][0] if k in dec else (c[0] if len(c) == 1 else "?" + "/".join(c))


if mode == "all":
    pr = T.prior()
    for hw, s in T.senses():
        p = pr.get(hw.lower())
        if not p:
            continue
        terms = {x.split(" = ", 1)[1] for x in p}
        for i, (tag, c) in enumerate(s):
            t = chosen(hw, i, c)
            if t not in terms:
                print(f"{hw}|{i}\t{t}\t[{tag[:70]}]")
                for x in p:
                    print(f"      {x}")
elif mode == "fam":
    rx = re.compile(sys.argv[2], re.I) if len(sys.argv) > 2 else None
    groups = collections.defaultdict(list)
    for hw, ss in T.senses():
        for i, (tag, c) in enumerate(ss):
            core = re.sub(r"\s*\([^()]*\)\s*$", "", tag).strip().lower()
            core = re.sub(r",? (quoted with -ti|with ceva 'both … and'|with ca 'and'|with ca|with pi 'also')"
                          r"( in the chapter on \w+)?$", "", core)
            groups[core].append((f"{hw}|{i}", chosen(hw, i, c)))
    for core, items in sorted(groups.items()):
        if rx and not rx.search(core):
            continue
        if len(items) > 1 and len({t for _, t in items}) > 1:
            print(f"## {core}")
            for k, t in items:
                print(f"   {k}\t{t}")
else:
    sys.exit("usage: crossbook_ru.py all | fam [regex]")
