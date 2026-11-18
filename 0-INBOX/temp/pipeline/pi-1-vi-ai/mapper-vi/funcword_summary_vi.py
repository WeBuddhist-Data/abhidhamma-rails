"""Count keyword=value pairs whose value is a bare Vietnamese function word (read-only)."""
import collections
import pathlib

D = pathlib.Path(__file__).resolve().parent
FUNC = {"và", "của", "là", "có", "không", "các", "những", "ở", "trong", "với", "cho", "thì", "mà", "nào",
        "đã", "đang", "sẽ", "ấy", "này", "được", "bị", "về", "theo", "từ", "đó", "hay", "hoặc", "cũng",
        "như", "khi", "lúc", "điều"}
cnt = collections.Counter()
for f in sorted(D.glob("*.mapped.md")):
    for line in f.read_text(encoding="utf-8").splitlines():
        for p in line.split("] ", 1)[1].split(", "):
            k, v = p.split("=", 1)
            if v.strip().lower() in FUNC:
                cnt[(k, v)] += 1
for (k, v), n in sorted(cnt.items(), key=lambda x: -x[1]):
    print(n, k, "=", v)
