"""One-off patcher of the map-harmonise pass (backups in harmonise-backup/). For every mapping script:
1. its own copy of the presence check (ATTR_FROM … presence()) is replaced by an import of presence_check.py;
2. (the three chapter scripts only) lookup() becomes _lookup() and a wrapper lookup() applies harmonise_rules.apply();
   harmonise_rules.REASONS fill the map-table reasons, harmonise_rules.TABLE_NOTE is appended to the rules text.
map_all.py gets only step 1 (its output must stay byte-identical). Idempotent: a patched script is skipped."""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OLD_HDR = "# presence check: a copy of pi-2's ONE shared presence_check.py (pi-2 map-harmonise decision 3), unchanged\n"
NEW_HDR = ("# presence check: the ONE check shared by all pi-3 mapping scripts (presence_check.py; map-harmonise\n"
           "# decision 3: the documented ending list). Imported, not copied, so every script uses the same form.\n")
IMPORT = ("sys.path.insert(0, str(HERE))\n"
          "from presence_check import ATTR_FROM, VERB_FROM, chunk_present, presence  # noqa: E402,F401\n")
IMPORT_H = "import harmonise_rules  # noqa: E402  (map-harmonise: the book-wide alignments, applied in lookup())\n"
WRAP = '''

_DEPTH = [0]


def lookup(ch, sid, kw, pali, my):
    """map-harmonise: the script's own lookup, then the book-wide alignments of harmonise_rules.py, applied to the
    keyword's final value only (not to the inner lookups of compose / redirect rules, which look other keywords up)."""
    _DEPTH[0] += 1
    try:
        v = _lookup(ch, sid, kw, pali, my)
    finally:
        _DEPTH[0] -= 1
    if _DEPTH[0]:
        return v
    h = harmonise_rules.apply(kw, sid, v, pali, my)
    if h != v:
        SRC[(sid, kw)] = "harmonise"
    return h
'''
REAS = ("for _k, _r in harmonise_rules.REASONS.items():   # map-harmonise reasons (harmonise_rules.py)\n"
        "    REASONS.setdefault(_k, _r)\n"
        "RULES += harmonise_rules.TABLE_NOTE\n\n\n")

for name, chapter in (("map_all.py", False), ("map_ch3-6-8-9.py", True), ("map_ch7-10-11.py", True),
                      ("map_ch12-15.py", True)):
    p = HERE / name
    s = p.read_text(encoding="utf-8")
    if "from presence_check import" in s:
        print("skip (patched)", name)
        continue
    a = s.index(OLD_HDR)
    b = s.index("ATTR_FROM = tuple(")
    c = s.index("\ndef load(ch):")
    body = s[b:c]
    assert body.rstrip().endswith("return True, rules"), name
    imp = IMPORT + (IMPORT_H if chapter else "")
    s = s[:a] + NEW_HDR + s[a + len(OLD_HDR):b] + imp + "\n" + s[c:]
    if chapter:
        assert s.count("\ndef lookup(ch, sid, kw, pali, my):\n") == 1, name
        s = s.replace("\ndef lookup(ch, sid, kw, pali, my):\n", "\ndef _lookup(ch, sid, kw, pali, my):\n")
        i = s.index("\ndef _lookup(ch, sid, kw, pali, my):\n")
        j = s.index("    raise KeyError(kw)\n", i) + len("    raise KeyError(kw)\n")
        s = s[:j] + WRAP + s[j:]
        k = s.index("\ndef prev_any(kw):")
        s = s[:k].rstrip("\n") + "\n\n\n" + REAS.rstrip("\n") + "\n\n" + s[k:]
    p.write_text(s, encoding="utf-8")
    print("patched", name)
