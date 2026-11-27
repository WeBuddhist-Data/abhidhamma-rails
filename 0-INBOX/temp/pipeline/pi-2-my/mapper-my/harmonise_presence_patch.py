"""One-off: replace each mapping script's own presence check (ATTR_FROM … presence()) by the shared
presence_check.py (map-harmonise decision 3). Backups of the scripts are in harmonise-backup/."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
NEW = ("# ---- presence check: the ONE check shared by all pi-2 mapping scripts (presence_check.py; map-harmonise\n"
       "# decision 3: the merged, documented ending list). Imported, not copied, so every script uses the same form.\n"
       "sys.path.insert(0, str(HERE))\n"
       "from presence_check import ATTR_FROM, VERB_FROM, chunk_present, presence  # noqa: E402,F401\n\n\n")
for f in sorted(HERE.glob("map_*.py")):
    s = f.read_text(encoding="utf-8")
    if "from presence_check import" in s:
        print(f.name, "already"); continue
    a = s.index("# ---- presence check")
    b = s.index("def load(ch):")
    old = s[a:b]
    assert "def presence(" in old and "def chunk_present(" in old and old.count("\ndef ") == 2, f.name
    f.write_text(s[:a] + NEW + s[b:], encoding="utf-8")
    print(f.name, "patched", len(old.splitlines()), "lines replaced")
