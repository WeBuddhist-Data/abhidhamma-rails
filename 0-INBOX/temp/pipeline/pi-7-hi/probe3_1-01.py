"""Debug helper for build_1-01_hi: show why count_line fails on given lines, or print translations.

usage: python -I -B -X utf8 probe3_1-01.py count|tr n1 [n2 ...]  or  range a b (route + print Hindi)
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import importlib.util
spec = importlib.util.spec_from_file_location("B", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\build_1-01_hi.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)

mode = sys.argv[1]
if mode == "range":
    ns = range(int(sys.argv[2]), int(sys.argv[3]) + 1)
else:
    ns = [int(x) for x in sys.argv[2:]]
for n in ns:
    try:
        if mode == "count":
            print(n, B.count_line(B.body(n).strip()))
        else:
            print(n, "P:", B.P[n - 1])
            print(n, "H:", B.translate(n))
    except B.Untranslated as e:
        print(n, "ERR", e)
