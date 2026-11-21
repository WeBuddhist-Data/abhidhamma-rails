"""Coordinator check (pi-5): the brief's structural verifier + the presence check for the given parts, and a check that
the approved pi-1 / pi-2 / pi-3 / pi-4 mapped files are byte-identical before and after the pi-5 modules are imported.

Usage: python -I -X utf8 check_parts_vi.py <part> [<part> ...]

Presence-check exceptions are the ALLOWED dicts ({(id, keyword): reason}) of the part scripts in this folder
(map_*_vi.py; imported only, they build nothing). The presence check is map_common_vi.present (pi-5: translated
editorial brackets and variant labels count as text, the Pāli of a variant bracket does not)."""
import hashlib
import importlib.util
import pathlib
import sys

sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parent
PIPE = D.parents[1]


def _hashes():
    out = {}
    for n in (1, 2, 3, 4):
        for f in sorted((PIPE / f"pi-{n}-vi-ai" / "mapper-vi").glob("*.mapped.md")):
            out[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


BEFORE = _hashes()
sys.path.insert(0, str(D))
import map_common_vi as m  # noqa: E402

allowed = {}
for f in sorted(D.glob("map_*_vi.py")):
    if f.name == "map_common_vi.py":
        continue
    spec = importlib.util.spec_from_file_location("pi5_" + f.stem.replace("-", "_"), f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    allowed.update(getattr(mod, "ALLOWED", {}))

for ch in sys.argv[1:]:
    a = [l.split('] ', 1) for l in (D / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines() if l.strip()]
    b = [l.split('] ', 1) for l in (D / f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines() if l.strip()]
    assert [x[0] for x in a] == [x[0] for x in b], ch
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(', ')] != [k.split('=', 1)[0] for k in y.split(', ')]]
    nde = sum(y.count('=(no direct equivalent)') for _, y in b)
    raw = (D / f'{ch}.mapped.md').read_bytes()
    print(ch, 'lines', len(a), 'bad', bad, 'NDE', nde, '| CR', raw.count(b'\r'))
    m.verify(ch, allowed)

AFTER = _hashes()
changed = [p for p in BEFORE if AFTER.get(p) != BEFORE[p]]
print("pi-1 / pi-2 / pi-3 / pi-4 mapped files:", len(BEFORE), "hashed;",
      "unchanged" if not changed and AFTER.keys() == BEFORE.keys() else f"CHANGED {changed}")
