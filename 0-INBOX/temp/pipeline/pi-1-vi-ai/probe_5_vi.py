"""Print the earlier Vietnamese strings that part 5 reuses (read-only helper; writes nothing)."""
import importlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
H = importlib.import_module("build_4-02_4-03_vi")
G, M, C, R, X, B, E, F = H.G, H.M, H.C, H.R, H.X, H.B, H.E, H.F

for name in ("RF", "ALL_RF", "KIND", "MAHA4", "SPHERES", "KHANDHAS", "ASANKHATA_DHATU"):
    print("R." + name, "=", repr(getattr(R, name, None)))
for k in ("cakkhāyatanaṃ", "rūpāyatanaṃ", "phoṭṭhabbāyatanaṃ", "kāyaviññatti", "vacīviññatti", "kabaḷīkāro āhāro"):
    print("R.N", k, "=", repr(R.N.get(k)))
print("X.QUALS kammassa =", repr(X.QUALS["kammassa katattā"]), "|", repr(X.QUALS["na kammassa katattā"]))
print("X.EXTRA anid =", repr(X.EXTRA["anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ"]))
print("X.ANY_OTHER =", repr(X.ANY_OTHER))
print("X.QUALS cittaja =", repr(X.QUALS["cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ"]))
print("B.NANA =", repr(B.NANA), "| manāyatanaṃ", repr(B.NAME["manāyatanaṃ"]), "| dhammāyatanaṃ", repr(B.NAME["dhammāyatanaṃ"]))
print("E.EYE..", E.EYE, E.EAR, E.NOSE, E.TONGUE, E.BODY)
print("F.KIRIYA_V =", repr(F.KIRIYA_V))
for n in ("MAGGA4", "MAGGA3", "ARIYAMAGGA", "SPHERE", "KATATTA", "NA_KATATTA", "ANID", "MAHA", "AY_PE", "VICI",
          "SILA_N", "IDAM", "ASAVA", "FETTER_GEN", "GANTHA_GEN", "FEEL", "PITI", "SUKHA", "UPEKKHA", "VIT", "VIC",
          "ROOTS_K", "ROOTS_A", "ROOT_K", "ROOT_A", "ROOT_AB", "END_TIKA", "TL", "K"):
    print("G." + n, "=", repr(getattr(G, n)))
for n in ("NIV", "UPA", "KIL", "DP", "AKASA", "NEVA", "TAM", "KH3V", "THINA", "UDDHACCA", "KUKKUCCA"):
    print("H." + n, "=", repr(getattr(H, n)))
txt2 = (B.OUT_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8")
for w in ("lĩnh vực thức vô tận", "lĩnh vực không có gì cả", "tầng thiền thứ tư", "phương pháp chia năm",
          "Bốn tầng thiền không hình sắc", "Tâm thiện thuộc ba cõi"):
    print(w, w in txt2)
P = dict(H.pali_segments(H.PARTS[0]))
V = dict(H.build_402(P))
for b in ("1-1198", "1-1200", "1-1201", "1-1213", "1-1214", "1-1215", "1-1288", "1-1290", "1-1292"):
    print(b, V[b])
V1 = dict(G.SEGMENTS)
for b in ("1-1023", "1-1024", "1-1102", "1-1118", "1-1140"):
    print(b, V1[b])
