"""List chapter-5 segments (and sentences) whose Pali is identical to a segment / sentence of an earlier
chapter that already has a Russian rails translation. Read-only helper for build_rails_5_ru.py.
usage: python -I -X utf8 reuse_5.py"""
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402

PREV = ["2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md", "2-03-cittuppadakandam.md",
        "2-04-cittuppadakandam.md", "2-05-cittuppadakandam.md", "3-01-rupakandam.md", "3-02-rupakandam.md",
        "3-03-rupakandam.md", "4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"]
STRIP = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def body(lines):
    return "\n".join(STRIP.sub("", x) for x in lines)


def main():
    seen = {}
    for ch in PREV:
        for sid, pl in S.segments(S.PALI / ch):
            seen.setdefault(body(pl), (ch, sid))
    for sid, pl in S.segments(S.PALI / "5-atthakathakandam.md"):
        b = body(pl)
        if b in seen:
            print("SEG", sid, "=", seen[b])
            continue
        # answer bodies: «Katame dhammā X? BODY – ime dhammā X.»
        m = re.match(r"Katame dhammā (.+?)\? (.+?) – ime dhammā \1\.$", b)
        if m:
            for k, (ch, s2) in seen.items():
                if k.endswith(f"? {m.group(2)} – ime dhammā {m.group(1)}."):
                    print("BODY", sid, "=", ch, s2)
                    break


if __name__ == "__main__":
    main()
