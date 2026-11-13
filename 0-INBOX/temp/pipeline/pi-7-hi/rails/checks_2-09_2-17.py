"""Run the brief's checks for 2-09 … 2-17 (or the files named): check_chapter_ids, dashcheck, verify_hi,
plus Latin-outside-brackets, double blank lines, CR, «…pe…», «:-».
usage: python -I -B -X utf8 checks_2-09_2-17.py [2-09 …]"""
import re
import subprocess
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = ROOT + r"\0-INBOX\temp\pipeline"
SRC = ROOT + r"\AI_translation\pali\pi-7_split_chapters"
DST = ROOT + r"\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters"
FILES = {
    "2-09": "2-09-hinattika", "2-10": "2-10-micchattaniyatattika", "2-11": "2-11-maggarammanattika",
    "2-12": "2-12-uppannattika", "2-13": "2-13-atitattika", "2-14": "2-14-atitarammanattika",
    "2-15": "2-15-ajjhattattika", "2-16": "2-16-ajjhattarammanattika",
    "2-17": "2-17-sanidassanasappatighattika",
}
for k in (sys.argv[1:] or list(FILES)):
    f = FILES[k] + ".md"
    for cmd in ([sys.executable, "-I", P + r"\check_chapter_ids.py", SRC, DST, f],
                [sys.executable, "-I", "-X", "utf8", P + r"\pi-1-en\dashcheck.py", SRC + "\\" + f, DST + "\\" + f],
                [sys.executable, "-I", "-X", "utf8", P + r"\pi-1-hi\verify_hi.py", SRC + "\\" + f, DST + "\\" + f]):
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        print((r.stdout + r.stderr).strip())
    t = open(DST + "\\" + f, encoding="utf-8", newline="").read()
    noid = re.sub(r"\^[0-9A-Za-z-]+", "", re.sub(r"\[[^\]]*\]", "", t))
    lat = sorted(set(re.findall(r"[A-Za-zāīūṃñṭḍṇḷ]{2,}", noid)))
    print(f"  extra: latin={lat[:10]} CR={chr(13) in t} dbl={chr(10)*3 in t} pe={'…pe…' in t} colon-dash={':-' in t}")
