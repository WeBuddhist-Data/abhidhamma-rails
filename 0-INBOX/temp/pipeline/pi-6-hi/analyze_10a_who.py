r"""Helper: list the distinct being/place phrases (the part before tesaṃ/tāsaṃ/tattha) in the answers of 10-01..10-06,
and the other answer sentences that do not fit the 'WHO LOC X V, no ca ...' / 'WHO LOC X ca V Y ca V' frames."""
import pathlib, re, sys, collections
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
FILES = sys.argv[1:] or [f"10-{i:02d}-indriyayamaka.md" for i in range(1, 7)]
who = collections.Counter()
other = collections.Counter()
for f in FILES:
    for l in (P / f).read_text(encoding="utf-8").splitlines():
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l).strip()
        if not t or t.startswith("#"):
            continue
        if t.startswith("("):
            if "? " not in t:
                continue
            t = t.split("? ", 1)[1]
        for s in re.split(r"(?<=\.) ", t):
            m = re.match(r"^(.*?) (tesaṃ|tāsaṃ|tattha)\b", s)
            if m and "no ca" in s or m and re.search(r" ca (?:na )?\S+ \S+ ca (?:na )?\S+\.$|\S+ ca (?:na )?\S+ \S+ ca (?:na )?\S+\.$", s):
                who[m.group(1)] += 1
            else:
                other[s] += 1
out = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-hi" / "who-10a.txt"
with out.open("w", encoding="utf-8") as fh:
    fh.write("## WHO\n")
    for k, v in sorted(who.items(), key=lambda x: x[0]):
        fh.write(f"{v}\t{k}\n")
    fh.write("## OTHER\n")
    for k, v in sorted(other.items(), key=lambda x: -x[1]):
        fh.write(f"{v}\t{k}\n")
print(len(who), len(other))
