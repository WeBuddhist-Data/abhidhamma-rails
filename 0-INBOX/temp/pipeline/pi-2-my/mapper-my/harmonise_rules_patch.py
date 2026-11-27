"""One-off: make the seven chapter scripts apply harmonise_rules.py in lookup() (map-harmonise decisions 2-4).
map_all.py (the approved sample) is not patched. Backups of the scripts are in harmonise-backup/."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
OLD = """    if v is None:
        raise KeyError(kw)
    SRC[(sid, kw)] = src
    return v
"""
NEW = """    if v is None:
        raise KeyError(kw)
    h = harmonise_rules.apply(kw, sid, v, my)      # map-harmonise: book-wide alignments (harmonise_rules.py)
    if h != v:
        v, src = h, "harmonise"
    SRC[(sid, kw)] = src
    return v
"""
IMP = "from presence_check import ATTR_FROM, VERB_FROM, chunk_present, presence  # noqa: E402,F401\n"
IMP2 = IMP + "import harmonise_rules  # noqa: E402  (map-harmonise: the book-wide alignments, applied in lookup())\n"
for f in sorted(HERE.glob("map_*.py")):
    if f.name == "map_all.py":
        continue
    s = f.read_text(encoding="utf-8")
    if "harmonise_rules.apply" in s:
        print(f.name, "already"); continue
    assert s.count(OLD) == 1 and s.count(IMP) == 1 and s.count("\n\ndef pi1_vals") == 1, f.name
    s = s.replace(OLD, NEW).replace(IMP, IMP2)
    s = s.replace("\n\ndef pi1_vals", "\nfor _k, _r in harmonise_rules.REASONS.items():\n    REASONS.setdefault(_k, _r)\n\n\ndef pi1_vals")
    f.write_text(s, encoding="utf-8")
    print(f.name, "patched")
