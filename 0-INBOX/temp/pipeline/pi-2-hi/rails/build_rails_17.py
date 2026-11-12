"""Builder for chapter 17 (Khuddakavatthuvibhaṅga), Hindi plain rails.

The part modules (build_rails_17_a … _d) hold one Hindi line per non-empty Pāli line, in order. This script
checks every line against its Pāli line (heading level, dash count, '[' count, final '?') and attaches the block
IDs from the Pāli. With fewer Hindi lines than Pāli lines it only checks the prefix and writes nothing.
"""
import importlib
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_17_k as K  # noqa: E402
import build_rails_sample as S  # noqa: E402

CH = "17-khuddakavatthuvibhango.md"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+")


def latin_outside_brackets(s):
    depth, out = 0, []
    for ch in s:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return LATIN.findall("".join(out))


def main():
    pi1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_HI.glob("*.md")))
    for s in K.PI1_STRINGS:
        assert s in pi1, ("not in pi-1 rails Hindi", s[:80])
    hindi = []
    for part in "abcd":
        try:
            m = importlib.import_module(f"build_rails_17_{part}")
        except ModuleNotFoundError:
            break
        hindi += m.LINES
    src = (S.PALI / CH).read_text(encoding="utf-8").splitlines()
    pali = [l for l in src if l.strip()]
    assert len(hindi) <= len(pali), (len(hindi), len(pali))
    errs = []
    out_blocks, cur = [], []
    for i, h in enumerate(hindi):
        p = pali[i]
        assert "^" not in h, (i, h[:60])
        if len(p) - len(p.lstrip("#")) != len(h) - len(h.lstrip("#")):
            errs.append((i, "heading", p[:50], h[:50]))
        if p.count("–") + p.count("—") != h.count("–"):
            errs.append((i, "dash", p.count("–") + p.count("—"), h.count("–"), h[:70]))
        if p.count("[") != h.count("["):
            errs.append((i, "bracket", p[:60]))
        m = ID.search(p)
        pbody = ID.sub("", p)
        if pbody.rstrip().endswith("?") != h.rstrip().endswith("?"):
            errs.append((i, "final ?", h[-40:]))
        lat = latin_outside_brackets(h)
        if lat:
            errs.append((i, "latin", lat[:5]))
        if "—" in h or ":-" in h or "  " in h:
            errs.append((i, "bad char/double space"))
        cur.append(h + (f" ^{m.group(1)}" if m else ""))
        if m:
            out_blocks.append("\n".join(cur))
            cur = []
    for e in errs:
        print("ERR", e)
    print(f"lines {len(hindi)}/{len(pali)}; errors {len(errs)}")
    if len(hindi) == len(pali) and not errs and not cur:
        target = S.OUT / CH
        target.write_text("\n\n".join(out_blocks) + "\n", encoding="utf-8", newline="\n")
        print("wrote", target, len(out_blocks), "segments")
    else:
        print("next Pāli line:", pali[len(hindi)][:120] if len(hindi) < len(pali) else "-")


if __name__ == "__main__":
    main()
