"""Read-only: compare the keyword tables of the four pi-3 mapping scripts (map-harmonise decision 3: one merged rule
list). Loads each script as a module (nothing is written: the scripts only run under __main__) and prints every
table key that has different values in different scripts / tables, then the shared verse / frame keys."""
import importlib.util, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
SCRIPTS = ["map_all.py", "map_ch3-6-8-9.py", "map_ch7-10-11.py", "map_ch12-15.py"]
vals = collections.defaultdict(lambda: collections.defaultdict(set))
for s in SCRIPTS:
    spec = importlib.util.spec_from_file_location(s[:-3].replace("-", "_"), HERE / s)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for name, t in vars(m).items():
        if name.startswith("T_") and isinstance(t, dict):
            for k, v in t.items():
                vals[k[:1].lower() + k[1:]][v].add(f"{s}:{name}")
        if name == "CTX" and isinstance(t, dict):
            for sid, d in t.items():
                for k, v in d.items():
                    vals[k[:1].lower() + k[1:]][v].add(f"{s}:CTX[{sid}]")
n = 0
for k in sorted(vals):
    if len(vals[k]) > 1:
        n += 1
        print(k, "|", " || ".join(f"{v} <- {sorted(w)}" for v, w in vals[k].items()))
print("keys with >1 table value:", n)
