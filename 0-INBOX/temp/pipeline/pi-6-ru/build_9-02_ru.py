"""Russian plain zero-shot of pi-6 (Yamaka): chapter 9-02-dhammayamaka.md (Dhammayamaka, pavattivāra continued:
the time sections of the uppādavāra and the uppādanirodhavāra).

Every frame comes from build_9-01_ru (DH_CFG, tr(), units_9(), the Dhamma members and moments), which in turn takes
families A / B from build_2-01_ru, the person / place shape from build_7-01_ru, the moments from build_8_ru and the
intros (+ the bhaṅgakkhaṇe units of build_5-02_ru) from build_5-01_ru. None of those files is edited.
NEW here (listed in notes-9-02.md):
  kusalākusalānaṃ bhaṅgakkhaṇe = «в момент распада благих и неблагих явлений» (pi-1 «результатом благих и неблагих
  явлений» for kusalākusalānaṃ dhammānaṃ); the uppādakkhaṇe twin is added for symmetry (not in this chapter).
  Two sub-headings stand as plain lines in the source (^6-9-120, ^6-9-135): rendered as the heading text without '#'.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_9-02_ru.py
Import: M = importlib.import_module("build_9-02_ru")   (importing never writes any file; only __main__ builds)
"""
import contextlib
import importlib
import pathlib
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

N9 = importlib.import_module("build_9-01_ru")
A, C, S = N9.A, N9.C, N9.S

CHAPTER = "9-02-dhammayamaka.md"

# =============================================================================================
# New intro unit: kusalākusalānaṃ bhaṅgakkhaṇe (pi-1 «благих и неблагих явлений»)
# =============================================================================================
KUSALAKUSALA_G = f"{B.ADJ['kusala']['gen_pl']} и {B.ADJ['akusala']['gen_pl']} {N9.DHAMMA_NOUN[2]}"
assert KUSALAKUSALA_G == "благих и неблагих явлений", KUSALAKUSALA_G
UNITS_9_02 = [
    (r"kusalākusalānaṃ bhaṅgakkhaṇe", f"{S.BHANGA} {KUSALAKUSALA_G}", "adv", False),
    (r"kusalākusalānaṃ uppādakkhaṇe", f"{S.UPPADA} {KUSALAKUSALA_G}", "adv", False),
]


@contextlib.contextmanager
def units_9_02():
    """9-01's units_9() plus UNITS_9_02 (restored afterwards)."""
    with N9.units_9():
        old = list(S.ALL_UNITS)
        S.ALL_UNITS[:0] = [u for u in UNITS_9_02 if u not in S.ALL_UNITS]
        try:
            yield
        finally:
            S.ALL_UNITS[:] = old


# =============================================================================================
# Sub-headings that stand as plain lines in the source
# =============================================================================================
def plain_heading(text):
    """'(Ca) paccanīkapuggalokāsā' (plain line) = the heading text of '##### (Ca) paccanīkapuggalokāsā' without '#'."""
    h = N9.heading("##### " + text)
    assert h.startswith("##### "), h
    return h[len("##### "):]


FIXED_9_02 = dict(N9.FIXED_9)
for _t in ("(Ca) paccanīkapuggalokāsā", "(Ga) anulomapuggalokāsā"):
    FIXED_9_02[_t] = plain_heading(_t)

CFG = dict(N9.DH_CFG, fixed=FIXED_9_02)


def translate_text(src, cfg=None, mode="pv"):
    """9-02 continues the pavattivāra: mode "pv" from the first line."""
    cfg = cfg or CFG
    out = []
    with units_9_02():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(N9.tr(body, cfg, mode) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [("1", "благих и неблагих явлений")]


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, inside the chapter and against every finished pi-6 chapter."""
    seen = {}
    names = [p.name for p in sorted(B.OUT_DIR.glob("*.md")) if p.name != CHAPTER and (B.PALI_DIR / p.name).exists()]
    for n in names:
        p = (B.PALI_DIR / n).read_text(encoding="utf-8").split("\n")
        r = (B.OUT_DIR / n).read_text(encoding="utf-8").split("\n")
        if len(p) != len(r):
            continue
        for a, b in zip(p, r):
            pb, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
            seen.setdefault(pb, {}).setdefault(rb, n)
    bad, shared, mine = [], 0, {}
    for a, b in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent inside the chapter: {pb!r}"
        mine[pb] = rb
        if pb.strip() and pb in seen:
            shared += 1
            if rb not in seen[pb]:
                bad.append((pb, rb, seen[pb]))
    if bad:
        raise AssertionError("differs from finished chapters: " + repr(bad[:5]))
    return shared, names


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(S.CROSSBOOK)
    A.check_crossbook(N9.CROSSBOOK)
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared, names = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in N9.SLIP_LOG + S.SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print(f"cross-book asserts OK; per-line checks OK; {shared} lines shared with {len(names)} finished chapters agree")


if __name__ == "__main__":
    main()
