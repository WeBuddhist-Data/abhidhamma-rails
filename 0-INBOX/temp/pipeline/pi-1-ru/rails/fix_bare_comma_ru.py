"""Punctuation sweep (coordinator, 2026-11-14): «X, – это …» -> «X – это …» where X (the answer before the Pāli dash)
has no comma of its own, i.e. a plain noun phrase or a «…» list, with no participial phrase or clause to close.
Only 3-02 and 3-03 have the pattern (4-01 … 5 were built with the rule). Run after any rebuild of
build_rails_3-02_3-03_ru.py. Dashes and line counts are unchanged; logs to fix-bare-comma-log.tsv.
"""
import pathlib, re

R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-1-russian-plain-rails_split_chapters")
LOG = pathlib.Path(__file__).with_name("fix-bare-comma-log.tsv")
PAT = re.compile(r"(^|\? )([^,?.]+), – это")
log = []
for p in sorted(R.glob("*.md")):
    lines = p.read_text(encoding="utf-8").split("\n")
    out = []
    for i, line in enumerate(lines, 1):
        new = PAT.sub(lambda m: f"{m.group(1)}{m.group(2)} – это", line)
        if new != line:
            log.append(f"{p.name}\t{i}\t{line[:120]}")
        out.append(new)
    if out != lines:
        p.write_text("\n".join(out), encoding="utf-8", newline="\n")
LOG.write_text("file\tline\tbefore\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("lines changed:", len(log))
