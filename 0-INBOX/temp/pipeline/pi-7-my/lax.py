"""Development helper: import my7_formulas with LAX witnesses and list the failures (read-only)."""
import sys, builtins
sys.dont_write_bytecode = True
src = open(sys.argv[1] if len(sys.argv) > 1 else "my7_formulas.py", encoding="utf-8").read().replace("LAX = False", "LAX = True", 1)
g = {"__file__": __file__.replace("lax.py", "my7_formulas.py"), "__name__": "my7x"}
exec(compile(src, "my7_formulas.py", "exec"), g)
for f in g["WFAIL"]:
    print("FAIL", f)
print(len(g["WITNESS"]), "witnessed")
