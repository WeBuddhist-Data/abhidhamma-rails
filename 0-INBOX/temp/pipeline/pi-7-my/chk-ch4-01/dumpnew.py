import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("x", H / "make_ch4-01.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
X.K.CUR["fix"] = True
X.F.SLIPS.clear()
txt = X.translate(X.NAMES[0])
out = []
for k, v in X.NEW.items():
    if k.startswith("("):
        continue
    out.append(f"- {k} = {v}")
notes = [f"- {k} = {v}" for k, v in X.NEW.items() if k.startswith("(")]
(H / "chk-ch4-01/new-terms.txt").write_text("\n".join(out), encoding="utf-8")
(H / "chk-ch4-01/new-notes.txt").write_text("\n".join(notes), encoding="utf-8")
print(len(out), "terms;", len(notes), "notes")
print("READ_LOG:", sorted(X.READ_LOG))
print("SLIPS:", sorted(X.F.SLIPS))
print("SUPPLIED:", X.SUPPLIED); print("SLIPS_MINE:", X.SLIPS_MINE)
print("COORD_USED:", sum(X.COORD_USED.values()), "units")
print("COORD_SKIPPED:", X.COORD_SKIPPED)
print("SK_ADD:", len(X.SK_ADD), "SKF_ADD:", len(X.SKF_ADD))
