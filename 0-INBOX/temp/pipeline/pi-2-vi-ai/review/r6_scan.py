import re, unicodedata
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
CH = "17-khuddakavatthuvibhango.md"
P = ROOT + r"\AI_translation\pali\pi-2_split_chapters\\" + CH
V = ROOT + r"\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + CH

raw = open(V, encoding="utf-8").read()
print("CR:", "\r" in raw, "NFC:", unicodedata.normalize("NFC", raw) == raw, "triple-nl:", "\n\n\n" in raw)

def lines(p):
    return [l.rstrip("\n") for l in open(p, encoding="utf-8") if l.strip()]
pl, vl = lines(P), lines(V)
PALI_DIAC = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]")
def strip_brackets(s):
    return re.sub(r"\[[^\]]*\]", "", s)
def ellipses(s):
    s = s.replace("…pe…", "…").replace("... pe ...", "…")
    return s.count("…")
for i, (p, v) in enumerate(zip(pl, vl)):
    issues = []
    if "…." in v or ".." in v.replace("…", ""):
        issues.append("dots")
    if p.count("?") != v.count("?"):
        issues.append(f"? {p.count('?')}/{v.count('?')}")
    if p.count("!") != v.count("!"):
        issues.append(f"! {p.count('!')}/{v.count('!')}")
    dp = re.findall(r"\(\d+\)|\d+", strip_brackets(p))
    dv = re.findall(r"\(\d+\)|\d+", strip_brackets(v))
    if dp != dv:
        issues.append(f"digits {dp[:6]} / {dv[:6]}")
    if PALI_DIAC.search(strip_brackets(v)):
        issues.append("pali-diacritic outside brackets: " + ",".join(sorted(set(re.findall(r"\S*[āīūṃṅñṭḍṇḷ]\S*", strip_brackets(v))))[:5]))
    ep, ev = ellipses(p), ellipses(v)
    if ep != ev:
        issues.append(f"ellipsis {ep}/{ev}")
    if re.search(r" [,.;:?!]", v) or "  " in v:
        issues.append("spacing")
    if v.count("“") != v.count("”") or v.count("‘") != v.count("’"):
        issues.append("quote balance")
    if '"' in v:
        issues.append("straight quote")
    # statement end
    body = re.sub(r"\s*\^[\w-]+$", "", v)
    if not v.startswith("#") and body and body[-1] not in ".?!”…:":
        issues.append("end:" + body[-3:])
    if issues:
        print(i, issues, "|", v[:80])
