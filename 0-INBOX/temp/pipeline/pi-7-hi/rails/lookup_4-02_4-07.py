"""Helper for 4-02..4-07: list distinct Pāli words (not condition forms / numbers) with termbase entries.
usage: python -I -B -X utf8 lookup_4-02_4-07.py [--tb] [words...]"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as S  # noqa: E402

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]
TOK = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")


def load_tb():
    tb = {}
    for line in open(ROOT + r"\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md", encoding="utf-8"):
        line = line.rstrip("\n")
        if ": {" in line:
            w, body = line.split(": {", 1)
            tb[w] = body[:-1]
    return tb


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tb = load_tb()
    ci = {k.lower(): v for k, v in tb.items()}
    if args:
        for w in args:
            print(w, ":", tb.get(w) or ci.get(w.lower()) or "-")
        sys.exit()
    known = set()
    for d in (S.P_ABL, S.P_NABL, S.P_LOC, S.P_NLOC, S.NUM, S.P_NOM):
        known |= {k.lower() for k in d}
    for k in S.KEYS:
        known.add(k + "paccayena")
    seen = {}
    for f in FILES:
        text = open(ROOT + r"\AI_translation\pali\pi-7_split_chapters\\" + f, encoding="utf-8").read()
        text = re.sub(r"\^[0-9A-Za-z-]+", " ", text)
        for t in TOK.findall(text):
            if t.lower() in known:
                continue
            seen[t] = seen.get(t, 0) + 1
    for t, n in seen.items():
        e = tb.get(t) or ci.get(t.lower())
        if "--tb" in sys.argv:
            print(f"{t} ({n}): {e or '-'}")
        else:
            print(f"{t} {n}")
