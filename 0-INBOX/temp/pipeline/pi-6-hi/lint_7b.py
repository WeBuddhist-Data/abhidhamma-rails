"""Lint a Hindi file: Latin words outside [...] brackets, double blanks, CR, '@@' markers."""
import re, sys
t = open(sys.argv[1], encoding="utf-8", newline="").read()
errs = []
for n, ln in enumerate(t.split("\n"), 1):
    body = re.sub(r"\[[^\]]*\]", "", ln)
    body = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", body)
    lat = re.findall(r"[A-Za-zĀ-žḀ-ỿ]+", body)
    if lat:
        errs.append(f"{n}: latin {lat[:5]}")
    if "@@" in ln:
        errs.append(f"{n}: untranslated")
    if "  " in ln:
        errs.append(f"{n}: double space")
if "\r" in t:
    errs.append("CR")
if "\n\n\n" in t:
    errs.append("double blank")
print(sys.argv[1].split("\\")[-1], "lint", "OK" if not errs else "ERRORS")
for e in errs[:20]:
    print("  ", e)
