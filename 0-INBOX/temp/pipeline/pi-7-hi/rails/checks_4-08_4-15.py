"""Run the brief's checks on 4-08 .. 4-15 and summarise (ids, dashes, verify_hi, blank lines, CR, Latin).
usage: python -I -B -X utf8 checks_4-08_4-15.py
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
PALI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-rails_split_chapters"
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline"
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md", "4-13-dukatika-dassanenapahatabbaduka.md",
         "4-14-dukatika-saranaduka.md", "4-15-tikaduka-hetuduka.md"]


def run(args):
    r = subprocess.run([sys.executable, "-I", "-X", "utf8"] + [str(a) for a in args], capture_output=True, text=True,
                       encoding="utf-8", cwd=ROOT)
    return (r.stdout + r.stderr).strip()


for f in FILES:
    print("=" * 20, f)
    print(run([PIPE / "check_chapter_ids.py", PALI, HI, f])[-600:])
    print(run([PIPE / "pi-1-en" / "dashcheck.py", PALI / f, HI / f])[-600:])
    v = run([PIPE / "pi-1-hi" / "verify_hi.py", PALI / f, HI / f])
    print("verify_hi:", v[-1500:])
    raw = (HI / f).read_bytes().decode("utf-8")
    segs = len(re.findall(r" \^[0-9A-Za-z-]+$", raw, re.M))
    print("segments:", segs, "| CR:", "\r" in raw, "| double blank:", "\n\n\n" in raw)
    lat = [ln for ln in raw.splitlines() if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r" \^[0-9A-Za-z-]+$", "", ln))]
    print("Latin lines:", len(lat), lat[:3])
