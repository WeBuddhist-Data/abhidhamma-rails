"""Debug helper 4 for build_1-01_hi: inspect characters and matching rules."""
import re, unicodedata
import importlib.util
spec = importlib.util.spec_from_file_location("B", r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\build_1-01_hi.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
s = unicodedata.normalize("NFC", B.body(1311)).replace("…pe…", "…")
pat = [r for r, h in B.PN_RULES if "īlaṃ…" in r.pattern][0].pattern
print([hex(ord(c)) for c in pat[30:]])
i = s.find("paññaṃ upanis")
print([hex(ord(c)) for c in s[i:i + 20]])
