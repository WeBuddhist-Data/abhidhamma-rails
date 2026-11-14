# compact family view: for each regex, every matching headword sense with its chosen term (decision, else
# single candidate, else ?a/b). usage: python -I -X utf8 stemscan_ru.py <regex> [<regex> ...]
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\termbase")
import tb_tool_ru as T

dec = T.decisions()
ss = T.senses()
for a in sys.argv[1:]:
    rx = re.compile(a, re.I)
    print(f"=== {a}")
    for hw, s in ss:
        if rx.search(hw):
            for i, (tag, c) in enumerate(s):
                k = f"{hw}|{i}"
                t = dec[k][0] if k in dec else (c[0] if len(c) == 1 else "?" + "/".join(c))
                print(f"  {k}\t{t}\t[{tag[:50]}]")
