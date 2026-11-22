"""Print the member tables of the frame-setter / yamaka builders (import only; importing writes nothing)."""
import os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

for mod, names in [("build_2-01_vi", ["KHANDHA_STEM", "MEMBER"]), ("build_3-01_vi", ["BASE", "BARE", "MEMBER"]),
                   ("build_4_vi", ["ELEMENT", "MEMBER", "VINNANA"]), ("build_5-01_vi", ["SACCA_STEM", "MEMBER"]),
                   ("build_6-01_vi", ["MEMBER"]), ("build_7-01_vi", ["TENDENCY_VI", "ANUSAYA_PL"]),
                   ("build_9-01_vi", ["CATS"]), ("build_10-01_vi", ["FACULTY_VI", "BARE_VI", "MEMBER"])]:
    m = importlib.import_module(mod)
    for n in names:
        print(f"== {mod}.{n}:", repr(getattr(m, n, None))[:3000])
