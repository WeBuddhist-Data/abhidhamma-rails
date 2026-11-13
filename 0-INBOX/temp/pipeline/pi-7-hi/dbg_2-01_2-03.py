import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import importlib.util
spec = importlib.util.spec_from_file_location("B", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\build_2-01_2-03_hi.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
for s in sys.argv[1:]:
    k, sl = B.normalize(s)
    print(repr(k), [getattr(x, "case", getattr(x, "kind", None)) for x in sl])
    print(B._tokens(k, sl))
    print(B.lookup(s))
