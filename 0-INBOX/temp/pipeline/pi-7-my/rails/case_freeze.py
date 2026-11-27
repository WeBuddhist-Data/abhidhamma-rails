"""pi-7 rails fix round, helper (not part of the checks): freeze the reviewed case proposals (case-proposals.tsv,
written by case_propose.py from the PRE-FIX rails backup) into the data module case_fixes.py read by apply_fixes.py.
EXCLUDE lists the proposals that are wrong (the hand rules of apply_fixes.py cover those units).
Each frozen row: (rule, Pāli trigger regex built from the Pāli unit, old Burmese unit core, new, count)."""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
EXCLUDE = [
    # a genitive modifier rendered as an extra recipient, not a subject (hand rule M16 «…တို့၏»)
    ("K2", "Maggo sekkhānaṃ"), ("K2", "maggo sekkhānaṃ"),
    # the K1 «နိဗ္ဗာန်ကို → သည်» row is right; the K2 row of the same unit is not
    ("K2", "nibbānaṃ gotrabhussa vitakkassa ca"),
    # the subject is the comma list «patthanā, …» / «…, kāyikaṃ dukkhaṃ,» / «…, anattānupassanā,»: hand rules
    ("K2", "patthanā, kāyikassa sukhassa"), ("K3", "kāyikaṃ dukkhaṃ, mahaggatārammaṇāya"),
    ("K3", "anattānupassanā, ajjhattārammaṇāya"),
    # source oddity, kept (fix-notes: «Sekkhā phalasamāpattiyā kāyikassa sukhassa»)
    ("K2", "Sekkhā phalasamāpattiyā"),
    # C1: hand rule M07
    ("K3", "uppannā hetū sampayuttakānaṃ hetūnaṃ"), ("K2", "anuppannā hetū"), ("K2", "uppādī hetū"),
    # 3-09 ^7-32-…: the subject made a co-subject; hand rule M14
    ("K4", "rūpāyatanaṃ cakkhuviññāṇassa ca sampayuttakānañca"),
]
SEP = r"(?:\s|…pe…|…|[,.;()–]|\{[^}]*\})+(?:(?:na|pi|kesañci|aññamaññaṃ|kiñci kāle)(?:\s|…pe…|…|[,.;()–])+)?"


def trigger(unit):
    unit = re.sub(r"\{[^}]*\}", " ", unit)
    ws = [w.replace("…pe…", "").strip("…,.;()") for w in unit.split()]
    ws = [w for w in ws if w and not w.startswith("{")]
    return r"\b" + SEP.join(re.escape(w) for w in ws) + r"\b"


counts = {}
cf = HERE / "dev-case-counts.tsv"
if cf.exists():                     # the replacements each row makes in the pre-fix rails, in rule order
    for l in cf.read_text(encoding="utf-8").split("\n"):
        if l:
            k, v = l.split("\t")
            counts[int(k.split(".")[1])] = int(v)
rows = []
for l in (HERE / "case-proposals.tsv").read_text(encoding="utf-8").split("\n")[1:]:
    if not l:
        continue
    rule, n, pu, old, new = l.split("\t")
    if any(rule == r and pu.startswith(p) for r, p in EXCLUDE):
        continue
    rows.append((rule, trigger(pu), old, new, int(n)))
if counts:                          # keep only the rows that change the text; their exact counts are the expectation
    rows = [(r[0], r[1], r[2], r[3], counts[i]) for i, r in enumerate(rows) if counts.get(i)]
with open(HERE / "case_fixes.py", "w", encoding="utf-8") as fh:
    fh.write('"""pi-7 rails fix round: the frozen case fixes K1 … K5 (written by case_freeze.py from case-proposals.tsv;\n'
             'reviewed by hand). Row = (rule, Pāli trigger regex, old Burmese, new Burmese, replacements in the pre-fix\n'
             'rails). K1 subject «…ကို» -> «…သည်»; K2 subject written as the first recipient -> «…သည်»; K3 subject joined\n'
             'to the recipients by «၊» -> «…သည်»; K4 «၊» after the last co-subject dropped; K5 recipients written\n'
             '«…လည်းကောင်း» without «အား» -> «…အားလည်းကောင်း»."""\n\nCASE = [\n')
    for r in rows:
        fh.write(f"    {r!r},\n")
    fh.write("]\n")
print(len(rows), "rows frozen")
