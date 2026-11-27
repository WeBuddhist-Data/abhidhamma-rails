"""scratch: list every failing unit / part of a chapter (all units, not only the first per line)."""
import sys, pathlib, re, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import make_sample  # noqa: registers the chapter tables
F = make_sample.F
name = sys.argv[1] if len(sys.argv) > 1 else "1-puggalakatha.md"
src = (make_sample.PALI / name).read_text(encoding="utf-8")
cnt = collections.Counter()
for line in src.splitlines():
    if not line.strip():
        continue
    m = F.ID_RE.search(line)
    body = (line[:m.start()] if m else line).strip()
    if F.HEAD_RE.fullmatch(body):
        try: F.line_my(body)
        except F.Miss as e: cnt["HEAD " + body] += 1
        continue
    clean = F.BR_RE.sub("", body)
    key = F.norm_pe(F.strip_q(clean))
    if key in F.LINES or key.rstrip(".") in F.COLO:
        continue
    if any(rx.fullmatch(key) for rx, fn in F.LINE_FRAMES):
        try: F.line_my(body); continue
        except F.Miss as e: cnt["LINEFRAME " + str(e)] += 1; continue
    for a, b in F.split_sents(clean):
        u = F.strip_q(clean[a:b].strip())
        try:
            F.unit_my(u)
        except F.Miss as e:
            # find the deepest message by trying the generic frames directly
            msg = str(e)
            for rx, fn in F.FRAMES:
                mm = rx.fullmatch(F.norm_pe(u))
                if mm:
                    try: fn(mm)
                    except F.Miss as e2:
                        msg = str(e2); break
            cnt[msg] += 1
for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
    print(v, k)
print(len(cnt), "distinct")
