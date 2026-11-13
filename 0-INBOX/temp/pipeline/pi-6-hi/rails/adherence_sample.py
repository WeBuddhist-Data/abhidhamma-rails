"""Run hindi_termbase_adherence.py on explicit Hindi files instead of a folder (the sample folder also holds Pāli).

usage: python -I -X utf8 adherence_sample.py <hindi_file>[;<hindi_file>...]
"""
import sys, pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
src = (ROOT / "0-INBOX/temp/pipeline/hindi_termbase_adherence.py").read_text(encoding="utf-8")
old = 'pathlib.Path(rails_dir).glob("*.md")'
assert old in src
src = src.replace(old, '[pathlib.Path(x) for x in rails_dir.split(";")]')
sys.argv = ["adherence", str(ROOT / "AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md"),
            str(ROOT / "AI_translation/hindi/pi-6-pali-hindi-termbase-plain.md"), sys.argv[1]]
exec(compile(src, "hindi_termbase_adherence.py", "exec"), {"__name__": "__main__"})
