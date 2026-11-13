r"""Alignment pass for the pi-6 Hindi rails: make phrases that drifted between parallel agents uniform.

usage: python -I -B -X utf8 align_rails_pi6.py [--dry]
Backs up each touched file once to backup-pre-align\, applies the rules, logs per rule/file counts to align-log.tsv.
Decisions (majority form across the book; see run-reports.md):
  R1 na itthīnaṃ / na purisānaṃ = «स्त्रियों / पुरुषों से भिन्न» (10-02, 10-08..10-11) over «स्त्री / पुरुष न होने वाले» (10-03/04)
  R2 Anusaya cycle labels «(एक मूल पर आधारित)», «(दो … छह मूलों पर आधारित)» (7-03..7-10) over «(एक … छह पर आधारित)» (7-01/02)
  R3 Dve/Tayo/Cattāro puggalā = «दो/तीन/चार व्यक्ति» (7-01/02, 7-05.., 9-03, 10-13) over «… प्रकार के व्यक्ति» (7-03/04)
  R4 sabbattha = «सब जगह» (3-04, 7-04) over «सभी स्थानों पर» (7-02, 7-08) and «सभी स्थानों से» (7-06 → «सब जगह से»)
  R5 (Yassakampi yassayatthakampi sadisaṃ) = «… भाग भी समान हैं)» (3-05, 6-02) over «… समान है)» (5-02)
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
H = ROOT / "AI_translation/hindi/pi-6-hindi-plain-rails_split_chapters"
D = pathlib.Path(__file__).parent
BAK = D / "backup-pre-align"
DRY = "--dry" in sys.argv
NUM = {"दो", "तीन", "चार", "पाँच", "छह"}

RULES = [
    ("R1", ("10-03", "10-04"), r"स्त्री न होने वाले", "स्त्रियों से भिन्न"),
    ("R1", ("10-03", "10-04"), r"पुरुष न होने वाले", "पुरुषों से भिन्न"),
    ("R2", ("7-01", "7-02"), r"\(एक पर आधारित\)", "(एक मूल पर आधारित)"),
    ("R2", ("7-01", "7-02"), r"\((दो|तीन|चार|पाँच|छह) पर आधारित\)", r"(\1 मूलों पर आधारित)"),
    ("R3", ("7-03", "7-04"), r"प्रकार के व्यक्ति", "व्यक्ति"),
    ("R4", ("7-02", "7-08"), r"सभी स्थानों पर", "सब जगह"),
    ("R4", ("7-06",), r"सभी स्थानों से", "सब जगह से"),
    ("R5", ("5-02",), r"स्थान वाला भाग भी समान है\)", "स्थान वाला भाग भी समान हैं)"),
]

log = []
for f in sorted(H.glob("*.md")):
    text = f.read_text(encoding="utf-8")
    new = text
    for rid, prefixes, pat, rep in RULES:
        if not f.name.startswith(tuple(p + "-" for p in prefixes)):
            continue
        new, n = re.subn(pat, rep, new)
        if n:
            log.append((rid, f.name, pat, rep, n))
    if new != text and not DRY:
        BAK.mkdir(exist_ok=True)
        if not (BAK / f.name).exists():
            shutil.copy2(f, BAK / f.name)
        f.write_text(new, encoding="utf-8", newline="\n")

if not DRY:
    (D / "align-log.tsv").write_text(
        "rule\tfile\tpattern\treplacement\tcount\n" + "\n".join("\t".join(map(str, r)) for r in log) + "\n",
        encoding="utf-8", newline="\n")
for r in log:
    print(*r, sep="\t")
print("total", sum(r[4] for r in log), "(dry)" if DRY else "")
