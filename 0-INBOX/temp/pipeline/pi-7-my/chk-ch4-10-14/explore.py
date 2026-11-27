import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("mk41014", HERE / "make_ch4-10-14.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
X = mk.X
for w in (mk.WC, mk.WE):
    s = X.S(w)
    F, K, D, M = w.F, w.K, w.D, w.M
    print(w.tag, "KAYYA", repr(K.KAYYA), "EVAM", repr(K.EVAM), "SADISA", repr(F.SADISA), "SADISANI", repr(K.SADISANI))
    print(" KAT", repr(s.KAT), "VITTH", repr(s.VITTH), "SAB", repr(s.SAB), "SABB", repr(s.SABB), "DH", repr(s.DH))
    print(" PANHA", repr(getattr(D, "PANHA", None)), "GAMANA", repr(M.GAMANA), "GHATANA", repr(F.GHATANA), "MULAKA", repr(F.MULAKA))
    print(" ADI", repr(F.ADI), "TIKA", F.TIKA, "DUKA", F.DUKA, "ORD", {k: v for k, v in s.ORD.items()})
    print(" vara", s.vara("sahajāta"), "|", s.vara("pañhā"))
    print(" N adhipati", F.N["adhipati"], "AA", s.AA, "SAA", s.SAA)
    for k in ("nayena", "uddharitabbā"):
        pass
    print(" NOTE_ADD imaṃ nānaṃ", getattr(D, "NOTE_ADD", {}).get("imaṃ nānaṃ"), "NINN", getattr(D, "NINNANA", None), "NINK", getattr(D, "NINNANAKARANA", None))
    print(" COUNT", {k: F.COUNT[k] for k in list(F.COUNT)[:12]})
    print(" HLINES keys sample", [k for k in F.HLINES if "Paccayacatukk" in k or "ārammaṇa" in k.lower()][:30])
    print(" LEX kabali", F.LEX.get("kabaḷīkāro āhāro"), F.LEX.get("rūpajīvitindriyaṃ"), F.NOUN.get("kabaḷīkāro"))
    print(" PATHAMA_G", getattr(D, "PATHAMA_GAMANA", None), "IHA", getattr(D, "IHA", None))
print(X.M if hasattr(X,'M') else '')
import inspect
print([n for n in dir(mk.C3.M4) if n.isupper()][:80])
print(mk.C3.M4.NEW.get("nayena"))
