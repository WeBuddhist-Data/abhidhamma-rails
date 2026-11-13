"""Run all checks for 5-13..5-20 Hindi; also list Latin words outside variant brackets."""
import re
import subprocess
import sys

R = r"D:\Work\OpenPecha\abhidhamma-rails"
P = R + r"\AI_translation\pali\pi-7_split_chapters"
H = R + r"\AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters"
FILES = ["5-13-anulomapaccaniya-tikatika", "5-14-anulomapaccaniya-dukaduka",
         "5-15-paccaniyanuloma-tika", "5-16-paccaniyanuloma-duka",
         "5-17-paccaniyanuloma-dukatika", "5-18-paccaniyanuloma-tikaduka",
         "5-19-paccaniyanuloma-tikatika", "5-20-paccaniyanuloma-dukaduka"]
LAT = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")
for f in FILES:
    pa, hi = rf"{P}\{f}.md", rf"{H}\{f}.md"
    for cmd in ([sys.executable, "-I", R + r"\0-INBOX\temp\pipeline\check_chapter_ids.py", P, H, f + ".md"],
                [sys.executable, "-I", "-X", "utf8", R + r"\0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py", pa, hi],
                [sys.executable, "-I", "-X", "utf8", R + r"\0-INBOX\temp\pipeline\pi-1-en\dashcheck.py", pa, hi]):
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        print((r.stdout + r.stderr).strip())
    t = open(hi, encoding="utf-8", newline="").read()
    for i, line in enumerate(t.splitlines(), 1):
        body = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", line)
        body = re.sub(r"\[[^\]]*\]", "", body)
        m = LAT.findall(body)
        if m:
            print("  LATIN", f, i, m[:5])
    print("  CR" if "\r" in t else "", "  DOUBLEBLANK" if "\n\n\n" in t else "")
