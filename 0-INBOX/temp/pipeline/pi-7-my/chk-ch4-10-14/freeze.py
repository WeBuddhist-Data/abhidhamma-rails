"""Development helper (read-only): print the generator's term / name tables of 4-10 … 4-14 as Python literals, for the
checker's frozen copy (pasted by hand, then compared by the checker's T test)."""
import importlib.util
import pathlib
import pprint
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk41014", HERE / "make_ch4-10-14.py")
mk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mk)
X = mk.X
heads = sorted(mk.HEAD_WORLD)
print("DYAD_MY_ADD = " + pprint.pformat({h: [(t, X.dyad_value(h, t)) for _, t, _ in X.DYAD_SURF[h]] for h in heads},
                                        width=118))
extra = {"Mahantaradukaṃ": mk.C3.MAHANTARA, "Piṭṭhidukaṃ": mk.E4.GOCCHAKA["Piṭṭhidukaṃ"]}
print("DUKA_MY_ADD = " + pprint.pformat({**{h: X.DUKA_NAME[h] for h in heads}, **extra}, width=118))
print("GOC_MY_ADD = " + pprint.pformat({"Kilesagocchaka": X.GOC_NAME["Kilesagocchaka"]}, width=118))
for a in ("Micchattattikaṃ", "Sanidassanattikaṃ"):
    print(a, X.TIKA_NAME[a])
