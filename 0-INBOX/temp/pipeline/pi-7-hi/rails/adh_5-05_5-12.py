"""Termbase adherence limited to the segments of 5-05..5-12 (7-59-* .. 7-66-*); runs the shared checker's code."""
import re, sys
SRC = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\hindi_termbase_adherence.py"
code = open(SRC, encoding="utf-8").read()
code = code.replace("    if i not in seg:\n", "    if i not in seg or not re.match(r'7-(59|6[0-6])-', i):\n")
code = code.replace("print(\"\\n\".join(out[:40]))", "print(\"\\n\".join(out[:200]))")
sys.argv = [SRC, r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7-keywords-by-reference-pali-plain.md",
            r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md",
            r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters"]
exec(compile(code, SRC, "exec"), {"__name__": "__main__", "re": re})
