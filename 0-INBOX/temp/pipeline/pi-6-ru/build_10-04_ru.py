"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-04-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra paccuppanna: (Ṅa) paccanīkaokāso, (Ca) paccanīkapuggalokāsā).

Nothing new is settled here: every frame comes from the Indriya builders (imported, never edited).
  (Ṅa) places   build_10-02_ru.tr_line(text, IN2_CFG): yattha … tattha … questions, the chained
                "…pe…" questions, place answers «В мире форм: там …» (3-01 ay_place_intro), mūlaka tails.
  (Ca) persons  build_10-03_ru.tr_line(text): yassa yattha … tassa tattha … questions and the person answers
                (10-02 attributes, «У всех, кто умирает», «у существ без восприятия», the moments of
                5-01 / 8 and 10-03 IN_MOMENT_UNITS) with «у них там» (5-01 pv_intro, tattha).
Identical Pāli lines must come out byte-identical with every finished pi-6 chapter (checked below).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-04_ru.py
Import: importlib.import_module("build_10-04_ru")   (importing never writes any file)
"""
import importlib
import pathlib
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

I = importlib.import_module("build_10-01_ru")    # members, headings, mūlaka tails
P2 = importlib.import_module("build_10-02_ru")   # place driver (okāsa), chain questions
P3 = importlib.import_module("build_10-03_ru")   # person / place driver (puggalokāsa): sabbesaṃ, asaññasattānaṃ …
D = I.D
CHAPTER = "10-04-indriyayamaka.md"
PERSON_SECTION = "##### (Ca) paccanīkapuggalokāsā"

IN4_CFG = dict(P2.IN2_CFG)
IN4_CFG.update({"fixed": dict(P2.IN2_CFG["fixed"]), "variant_anchors": dict(P2.IN2_CFG["variant_anchors"])})


def translate_text(src):
    out, persons = [], False
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        if body.startswith(PERSON_SECTION):
            persons = True
        if persons and not body.startswith("#"):
            ru = P3.tr_line(body)
        else:
            ru = P2.tr_line(body, IN4_CFG)
        out.append(ru + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every other finished
    pi-6 chapter (and the sample)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared, files = 0, set()
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
                files.add(f.name)
    return shared, sorted(files)


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(I.A.CROSSBOOK)
    D.check_crossbook(I.CROSSBOOK)
    D.check_crossbook(P2.CROSSBOOK)
    D.check_crossbook(P3.CROSSBOOK)
    I.check_members()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared, files = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")),
          "| lines shared with finished chapters:", shared, files)
    for s in dict.fromkeys(P2.SLIP_LOG + P3.SLIP_LOG + I.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    main()
