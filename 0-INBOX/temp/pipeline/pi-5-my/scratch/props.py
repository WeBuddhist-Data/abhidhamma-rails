"""scratch: after importing every generator chain, list PROP keys with «, » whose clause (stmt) joins with «၍ » but has no «၊»."""
import sys, importlib.util, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
mods = {}
for name in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); mods[name] = m
F = sys.modules["my5_formulas"]
n = 0
for k, cl in F.PROP.items():
    if ", " not in k: continue
    try: s = cl.f("stmt")
    except Exception: continue
    parts = k.count(", ")
    if s.count("၊") < parts and "၍ " in s:
        n += 1; print(k[:110], "\n   ", s[:250])
print(n)
