"""Survey helper for 4-02..4-07: print lines / sentences that are not plain frames or counts."""
import collections
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as S  # noqa: E402

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]
PAT = re.compile(r"^(?:Siyā )?(.+?) dhammaṃ paṭicca (.+?) (?:dhammo uppajjati|dhammā uppajjanti) ")
PAN = re.compile(r"^(.+?) (?:dhammo|dhammā) (.+?) dhammassa \w+paccayena paccayo")

notes = collections.Counter()
other = collections.Counter()
heads = collections.Counter()
items = collections.Counter()
tails = collections.Counter()
for f in FILES:
    for ln in open(ROOT + r"\AI_translation\pali\pi-7_split_chapters\\" + f, encoding="utf-8"):
        ln = re.sub(r" \^[0-9A-Za-z-]+\s*$", "", ln.rstrip("\n"))
        if not ln.strip():
            continue
        if ln.startswith("#"):
            heads[re.sub(r"^#+ \*?(\d+-\d+\.? )?", "", ln).rstrip("*")] += 1
            continue
        for n in re.findall(r"\(([^()]*[^\d()][^()]*)\)", ln):
            notes[n] += 1
        body = re.sub(r" ?\(([^()]*)\)", "", ln)
        lb = S.lower_initials(body).strip()
        if not lb or S.is_count(lb.rstrip(". ")) or S.is_count(lb):
            continue
        for sent in re.split(r"(?<=\.) (?=[A-Z…])", body):
            m = PAT.match(sent) or PAN.match(sent)
            if m:
                items[m.group(1)] += 1
                items[m.group(2)] += 1
                tail = sent[m.end():] if PAT.match(sent) else sent[m.start(2) + len(m.group(2)):]
                tails[re.sub(r"\b(ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava)\b", "N", tail)] += 1
                continue
            other[sent] += 1
what = sys.argv[1] if len(sys.argv) > 1 else "other"
d = {"notes": notes, "other": other, "heads": heads, "items": items, "tails": tails}[what]
for k, v in d.items():
    print(v, k)
