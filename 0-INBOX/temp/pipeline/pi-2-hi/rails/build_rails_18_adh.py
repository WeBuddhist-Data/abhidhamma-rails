"""Run hindi_termbase_adherence.py restricted to the ch8 and ch18 segment ids (the script itself is not modified).

usage: python -I -X utf8 build_rails_18_adh.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
src = (ROOT / "0-INBOX" / "temp" / "pipeline" / "hindi_termbase_adherence.py").read_text(encoding="utf-8")
MINE = set()
for name in ("8-sammappadhanavibhango.md", "18-dhammahadayavibhango.md"):
    t = (ROOT / "AI_translation" / "pali" / "pi-2_split_chapters" / name).read_text(encoding="utf-8")
    MINE |= set(re.findall(r"\^([0-9A-Za-z-]+)\s*$", t, re.M))
src = src.replace("if i not in seg:", "if i not in seg or i not in MINE:")
src = src.replace("print(\"\\n\".join(out[:40]))", "print(\"\\n\".join(out))")
sys.argv = ["x", str(ROOT / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md"),
            str(ROOT / "AI_translation/hindi/pi-2-pali-hindi-termbase-plain.md"),
            str(ROOT / "AI_translation/hindi/pi-2-hindi-plain-rails_split_chapters")]
exec(compile(src, "adherence", "exec"), {"MINE": MINE, "__name__": "__main__"})
