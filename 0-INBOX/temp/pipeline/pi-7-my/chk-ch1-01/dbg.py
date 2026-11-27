import importlib.util, pathlib, sys, traceback
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("ch101", HERE / "make_ch1-01.py")
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
F = K.F
F.CLAUSE_RE, F.PANHA_RE = F._clause_re(), F._panha_re()
import re
F.GHATANA_RE = re.compile(r"(?P<c>[\wāīūṃṅñṭḍṇḷ][\wāīūṃṅñṭḍṇḷ -]*?)(?:nti|īti) (?P<n>" + F._CNT_ALT + r")(?P<end>[. ]|$)")
for a in sys.argv[1:]:
    if a.startswith("@"):
        try:
            print(K.note_clause(a[1:]))
        except Exception:
            traceback.print_exc()
        continue
    try:
        print(F.body_my(a))
    except Exception as e:
        traceback.print_exc()
