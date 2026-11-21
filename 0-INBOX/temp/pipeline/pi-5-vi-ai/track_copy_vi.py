"""Track copy for pi-5 Vietnamese plain (2026-11-22).

usage: python -I -X utf8 -B track_copy_vi.py text      -> copy the merged translation into the track folder, add the
                                                         root-text transclusions (pi-3-4/add_transclusions.py), write LF
       python -I -X utf8 -B track_copy_vi.py termbase  -> copy the (aligned) termbase into the track folder, LF
"""
import pathlib, shutil, subprocess, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TRACK = ROOT / "3-TRANSFORMATIONS/Translations/vi-Contemporary-Vietnamese-Abhidhamma"
SRC_TEXT = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain.md"
SRC_TB = ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
ADD = ROOT / "0-INBOX/temp/pipeline/pi-3-4/add_transclusions.py"


def lf(p):
    b = p.read_bytes()
    if b"\r" in b:
        p.write_bytes(b.replace(b"\r\n", b"\n"))
    assert b"\r" not in p.read_bytes()


what = sys.argv[1]
if what == "text":
    dst = TRACK / SRC_TEXT.name
    assert not dst.exists(), f"{dst} exists already; delete it first to redo"
    shutil.copyfile(SRC_TEXT, dst)
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", "-B", str(ADD), str(dst), "1-SOURCES/Text/pi-5.md", str(ROOT)],
                       capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip(), r.stderr.strip())
    assert r.returncode == 0
    lf(dst)
    first = dst.read_text(encoding="utf-8").split("\n", 1)[0]
    assert first == "---", first
    print("track text OK:", dst)
elif what == "termbase":
    dst = TRACK / SRC_TB.name
    shutil.copyfile(SRC_TB, dst)
    lf(dst)
    print("track termbase OK:", dst)
else:
    raise SystemExit(__doc__)
