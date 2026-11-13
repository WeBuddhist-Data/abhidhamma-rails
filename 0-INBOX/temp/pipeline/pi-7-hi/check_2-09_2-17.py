"""Extra checks for 2-09..2-17 Hindi: Latin residue, em dash / ':-', CR, double blank lines, unresolved markers."""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_sample_hi as S  # noqa: E402

LATIN = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")
names = sorted(p.name for p in S.HI_DIR.glob("2-*.md") if "2-09" <= p.name[:4] <= "2-17")
bad = 0
for n in names:
    t = (S.HI_DIR / n).read_text(encoding="utf-8")
    errs = []
    for i, l in enumerate(t.split("\n"), 1):
        body = S.ID_RX.sub("", l)
        if LATIN.search(body):
            errs.append(f"{i}: Latin {LATIN.search(body).group(0)}")
        if "—" in l or ":-" in l:
            errs.append(f"{i}: em dash or :-")
        if re.search("[-]", l):
            errs.append(f"{i}: marker left")
        if "  " in l or " ," in l or " ।" in l:
            errs.append(f"{i}: spacing")
    if "\r" in t or "\n\n\n" in t:
        errs.append("CR or double blank line")
    print(n, "OK" if not errs else errs[:10])
    bad += bool(errs)
sys.exit(1 if bad else 0)
