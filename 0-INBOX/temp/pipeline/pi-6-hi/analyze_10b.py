r"""Helper: shape catalogue of 10-07..10-13 indriyayamaka Pali lines."""
import pathlib, re, sys, collections
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
FILES = [f"10-{i:02d}-indriyayamaka.md" for i in range(7, 14)]
IND = r"(?:cakkhu|sot|ghān|jivh|kāy|man|itth|puris|jīvit|sukh|dukkh|somanass|domanass|upekkh|saddh|vīriy|sat|samādh|paññ|anaññātaññassāmīt|aññ|aññātāv)indriy(?:aṃ|añca|ā|āni|ānañca|ānaṃ|anti|añceva)"
VERB = r"(?:na |n)?(?:uppajj|nirujjh)(?:ati|ittha|issati|issatīti|atīti|itthāti|anti)"
mode = sys.argv[1] if len(sys.argv) > 1 else "shapes"
cnt = collections.Counter()
ex = {}
for f in FILES:
    for l in (P / f).read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l)
        if mode == "heads":
            if t.startswith("#") or re.search(r"\(\w+mūlakaṃ\)|niṭṭhit", t):
                print(f, t[:150])
            continue
        if mode == "who":
            for m in re.finditer(r"(?:^|(?<=[.?] ))([^.?]*?) (tesaṃ|tāsaṃ)( tattha)? \S+ (?:na |n)?\S+(?:,| \S+ca)", t):
                cnt[m.group(1)] += 1
                ex.setdefault(m.group(1), f)
            continue
        s = re.sub(IND, "I", t)
        s = re.sub(VERB, "V", s)
        for sent in re.split(r"(?<=[.?]) ", s):
            sent = re.sub(r"^\((Ka|Kha)\) ", "", sent)
            cnt[sent] += 1
            ex.setdefault(sent, f)
for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
    print(v, ex[k], k)
