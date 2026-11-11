import pathlib, sys
sys.argv = ["x"]
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
sys.path.insert(0, str(B / "AI_translation/skills/scripts"))
from split_chapters import strip_frontmatter
for n in (3, 4):
    fm, _ = strip_frontmatter((B / f"1-SOURCES/Text/pi-{n}.md").read_text(encoding="utf-8"))
    (B / f"AI_translation/pali/pi-{n}_split_chapters/frontmatter.txt").write_text(fm + "\n", encoding="utf-8")
    print(n, "frontmatter.txt written")
