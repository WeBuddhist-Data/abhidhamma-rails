"""Extra checks for parts 2-01 / 2-02: true dash counts (– and —) per line, forbidden strings,
CR, double blank lines, sample prefix (2-01)."""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
P = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
E = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
ok = True
for name in sys.argv[1:]:
    pb, eb = (P / name).read_bytes(), (E / name).read_bytes()
    pt, et = pb.decode("utf-8"), eb.decode("utf-8")
    pl = [l for l in pt.splitlines() if l.strip()]
    el = [l for l in et.splitlines() if l.strip()]
    c = lambda t: (t.count("–"), t.count("—"))
    bad = [i for i, (a, b) in enumerate(zip(pl, el)) if c(a) != c(b)]
    q = lambda t: t.count("?")
    badq = [i for i, (a, b) in enumerate(zip(pl, el)) if q(a) != q(b)]
    probs = []
    if len(pl) != len(el):
        probs.append(f"line count {len(pl)} vs {len(el)}")
    if bad:
        probs.append(f"dash mismatches {len(bad)} {bad[:5]}")
    if badq:
        probs.append(f"'?' mismatches {len(badq)} {badq[:5]}")
    if b"\r" in eb:
        probs.append("CR present")
    if "\n\n\n" in et:
        probs.append("double blank line")
    for s in (":-", "outline", "Outline", "neutral", "Dhamma "):
        if s in et:
            probs.append(f"forbidden {s!r}")
    if et.count("—") > pt.count("—"):
        probs.append("em dash added")
    if name.startswith("2-01"):
        sample = (HERE / "ch2-01-sample.md").read_text(encoding="utf-8")
        if not et.startswith(sample):
            probs.append("sample prefix differs")
    print(name, "lines", len(pl), len(el), "dashes(pali/en)", sum(map(sum, map(c, pl))), sum(map(sum, map(c, el))),
          "OK" if not probs else "PROBLEMS: " + "; ".join(probs))
    ok &= not probs
sys.exit(0 if ok else 1)
