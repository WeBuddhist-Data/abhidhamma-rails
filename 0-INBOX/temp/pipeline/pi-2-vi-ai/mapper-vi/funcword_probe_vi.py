"""Print bare function-word values other than the expected ones (na=không, Yo/Yā/Yaṃ/Ye forms, pada=điều), with the segment's Vietnamese.
usage: python -I -X utf8 funcword_probe_vi.py"""
import pathlib, re, collections, sys

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
D = ROOT / "0-INBOX/temp/pipeline/pi-2-vi-ai/mapper-vi"
VI = ROOT / "AI_translation/vietnamese/pi-2-vietnamese-plain-zeroshot_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
FUNC = {"và", "của", "là", "có", "không", "các", "những", "ở", "trong", "với", "cho", "thì", "mà", "nào", "đã", "đang", "sẽ", "ấy", "này", "được", "bị", "về", "theo", "từ", "đó", "hay", "hoặc", "cũng", "như", "khi", "lúc", "điều"}
EXPECTED = re.compile(r"^(na|y[oaāeṃ]+|ye ye|yaṃ|yā|yo|ye|pad[aāeṃnsū]*)$", re.I)


def segs(p):
    out, cur = {}, []
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID.search(line)
        if m:
            out[m.group(1)] = " ".join(cur)
            cur = []
    return out


cnt = collections.Counter()
for mf in sorted(D.glob("*.mapped.md")):
    part = mf.name[: -len(".mapped.md")]
    vi = segs(VI / f"{part}.md")
    for line in mf.read_text(encoding="utf-8").splitlines():
        sid, body = line[1:].split("] ", 1)
        for k, v in (x.split("=", 1) for x in body.split(", ")):
            if v.strip().lower() in FUNC:
                cnt[(k, v)] += 1
                if not EXPECTED.match(k):
                    print(part, sid, k, "=", v, "|", vi.get(sid, "")[:220])
print(cnt.most_common())
