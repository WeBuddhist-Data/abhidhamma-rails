"""List termbase terms with suspicious form: quotes, final case particles / plural markers, ellipsis, Latin, dashes, «၊», «။»."""
import re, pathlib, sys
B = pathlib.Path(__file__).resolve().parents[5]
T = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].endswith(".md") else B / "AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md"
flt = [a for a in sys.argv[1:] if not a.endswith(".md")]
pats = [("quote", r"[“”‘’\"']"), ("case", r"(ကို|၏|၌|တွင်|ဖြင့်|မှ|သည်|အား|နှင့်|သို့)$"), ("plural", r"(များ|တို့)$"),
        ("particle", r"(လည်း|ပင်|သာလျှင်)$"), ("ellipsis-end", r"…$"), ("latin", r"[A-Za-z]"), ("dash", r"[–—-]"),
        ("paren", r"[()\[\]]"), ("pmark", r"[၊။]"), ("sep", r"(, | / |; )")]
for line in T.read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    for i, s in enumerate(body[:-1].split("; ")):
        tag, t = s.rsplit(": ", 1)
        hits = [n for n, p in pats if re.search(p, t)]
        if hits and (not flt or set(hits) & set(flt)):
            print(f"{','.join(hits):12s} {hw}|{i}: {t}    ({tag[:70]})")
