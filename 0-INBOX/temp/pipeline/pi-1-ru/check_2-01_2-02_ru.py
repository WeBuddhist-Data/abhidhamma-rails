"""Extra checks for parts 2-01 / 2-02 (Russian): per-line counts of "–", "—", "?" equal to the Pāli,
no ":-", no CR, no double blank lines, 2-01 starts with the approved sample byte for byte.
usage: python -I -X utf8 check_2-01_2-02_ru.py"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
P = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
R = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters"
bad = 0
for f in ("2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"):
    pl = [l for l in (P / f).read_text(encoding="utf-8").splitlines() if l.strip()]
    rb = (R / f).read_bytes()
    rt = rb.decode("utf-8")
    rl = [l for l in rt.splitlines() if l.strip()]
    errs = []
    if len(pl) != len(rl):
        errs.append(f"line count {len(pl)} != {len(rl)}")
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        for ch in ("–", "—", "?"):
            if p.count(ch) != r.count(ch):
                errs.append(f"line {i}: {ch!r} {p.count(ch)} != {r.count(ch)}")
    if b"\r" in rb or "\n\n\n" in rt or ":-" in rt:
        errs.append("CR / double blank / ':-'")
    if f.startswith("2-01"):
        s = (HERE / "ch2-01-sample.md").read_bytes()
        if not rb.startswith(s):
            errs.append("does not start with ch2-01-sample.md")
    bad += bool(errs)
    print(f, "->", "; ".join(errs[:10]) if errs else "OK")
raise SystemExit(1 if bad else 0)
