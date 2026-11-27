import sys, re
rows = open(sys.argv[1], encoding="utf-8").read().split("\n[")
for r in rows:
    lines = r.split("\n")
    cnt = lines[0].split("]")[0].lstrip("[")
    m = re.search(r"\[(?:\\+')?([^\]]{0,160})", lines[0][len(cnt)+1:][-400:])
    err = re.findall(r"\[\\*'?([^\[\]]*?)\\*'?\]", lines[0])
    print(cnt, "|", lines[1].strip()[:300] if len(lines) > 1 else "", "||", (err[-1][:120] if err else ""))
