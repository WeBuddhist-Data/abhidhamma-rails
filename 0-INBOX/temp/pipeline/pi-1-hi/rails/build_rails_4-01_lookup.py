"""Look up the termbase for every keyword and token of chapter 4-01 (termbase only; Pāli keyword list)."""
import pathlib, re, collections
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
src = (ROOT / "AI_translation/pali/pi-1_split_chapters/4-01-nikkhepakandam.md").read_text(encoding="utf-8")
tb = {}
for line in (ROOT / "AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    if ": {" in line:
        w, b = line.split(": {", 1)
        tb[w] = b[:-1]
tbl = {k.lower(): k for k in tb}
ids = set(re.findall(r"\^([0-9A-Za-z-]+)\s*$", src, re.M))
seen = collections.OrderedDict()
for line in (ROOT / "AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    if i[1:] in ids:
        for k in body.split(", "):
            for kk in k.split(" / "):
                seen.setdefault(kk, 1)
TOK = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")
for t in TOK.findall(src):
    seen.setdefault(t, 1)
hit, miss = [], []
for k in seen:
    kk = tbl.get(k.lower())
    if kk:
        hit.append(f"{kk}: {tb[kk]}")
    else:
        miss.append(k)
out = ROOT / "0-INBOX/temp/pipeline/pi-1-hi/rails/lookup-4-01.txt"
out.write_text("\n".join(hit) + "\n\n=== NOT IN TERMBASE ===\n" + " ".join(miss) + "\n", encoding="utf-8")
print(len(hit), len(miss), len(out.read_text(encoding="utf-8")))
