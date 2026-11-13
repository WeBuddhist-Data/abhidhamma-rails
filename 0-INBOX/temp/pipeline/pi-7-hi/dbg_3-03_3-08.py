import sys, re, importlib.util
spec = importlib.util.spec_from_file_location("B", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\build_3-03_3-08_hi.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
g, s = sys.argv[1], sys.argv[2]
B.FILE_STATE.clear()
if "--units" in sys.argv:
    for u in B.first_units(B.tokenize(s), g):
        print(u.get("t"), u.get("w"), u.get("kind"), u.get("s", ""))
print(B.body_line(s, g))
