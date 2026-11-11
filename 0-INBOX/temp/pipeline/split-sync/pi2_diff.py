import re, pathlib, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\split-sync")
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
TR = re.compile(r"^\s*!\[\[.*\]\]\s*$")
root = (B / "1-SOURCES/Text/pi-2.md").read_text(encoding="utf-8").replace("\r\n", "\n")
body = root.split("\n---", 1)[1] if root.startswith("---") else root
rl = [l for l in body.split("\n")[1:] if l.strip() and not TR.match(l)]
sd = B / "AI_translation/pali/pi-2_split_chapters"
pre = (sd / "preamble.md").read_text(encoding="utf-8").replace("\r\n", "\n")
print("SPLIT preamble:", pre[:400])
print("ROOT head:", rl[:6])
files = sorted((p for p in sd.glob("*.md") if p.stem != "preamble"), key=lambda p: int(p.stem.split("-")[0]))
sl = [l for p in [sd / "preamble.md"] + files for l in p.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n") if l.strip()]
print("nonblank lines split", len(sl), "root", len(rl))
sid = [m.group(1) for l in sl if (m := ID.search(l))]
rid = [m.group(1) for l in rl if (m := ID.search(l))]
print("ids split", len(sid), "root", len(rid), "same order:", sid == rid)
if sid != rid:
    import difflib
    print([d for d in difflib.unified_diff(sid, rid, n=0, lineterm="")][:20])
strip = lambda l: re.sub(r"^\d+\. ", "", l)
d = [(a, b) for a, b in zip(sl, rl) if strip(a) != b]
print("lines differing after dropping leading 'N. ':", len(d))
for a, b in d[:8]:
    print("  S:", a[:150]); print("  R:", b[:150])
print("split lines with leading number:", sum(1 for l in sl if re.match(r"\d+\. ", l)), "root:", sum(1 for l in rl if re.match(r"\d+\. ", l)))
