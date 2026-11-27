import importlib.util, sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("x", HERE / "make_ch5-05-12.py")
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
M=X.M
n="(Paccanīyaṃ vitthāretabbaṃ. Sahajātavārampi paccayavārampi vitthāretabbaṃ. Paccayavārepi hetuyā chabbīsa, ārammaṇe aṭṭhārasa…pe… avigate chabbīsa. Nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paṭiccavārasadisaṃ.)"
body=M.F.pe(n[1:-2])
for snt in re.split(r"\. ", body):
    print(repr(snt), '->', M._sentence(M.F.lc(snt.strip())))
for c in ["hetuyā chabbīsa", "ārammaṇe aṭṭhārasa… avigate chabbīsa"]:
    print(c, X._counts(c))
print(M.note_my(n))
