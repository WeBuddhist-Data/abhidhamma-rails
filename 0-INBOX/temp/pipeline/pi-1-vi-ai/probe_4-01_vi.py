"""Helper for part 4-01: prints the earlier Vietnamese strings that 4-01 reuses (nothing is written)."""
import importlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402
import build_ch2_01_sample_vi as C  # noqa: E402
R = importlib.import_module("build_3-01_vi")
X = importlib.import_module("build_3-02_3-03_vi")
D, E, F = R.D, R.E, R.F

print("UDDESO_V:", R.UDDESO_V)
print("SPHERES:", R.SPHERES)
print("KHANDHAS:", R.KHANDHAS)
print("ASD:", R.ASANKHATA_DHATU)
print("EKAKA_HEAD_V:", R.EKAKA_HEAD_V)
print("ANID:", X.EXTRA["anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ"])
print("QUALS:", X.QUALS["kammassa katattā"], "|", X.QUALS["na kammassa katattā"])
print("KIRIYA_V:", F.KIRIYA_V)
print("MAGGA:", D.MAGGA, "|", D.TOKENS["dhammavicayasambojjhaṅgo"])
for k in ("rūpakkhandho", "vedanākkhandho", "dhammāyatanaṃ", "lobho", "doso", "moho", "abhijjhā", "byāpādo",
          "vicikicchā", "micchādiṭṭhi"):
    print(k, "=", D.B.NAME.get(k))
print("W_LOBHA", E.W_LOBHA)
print("W_DOSA", E.W_DOSA)
print("W_MOHA", E.W_MOHA)
print("W_DITTHI", E.W_DITTHI)
print("W_VICI", E.W_VICIKICCHA)
print("ADOSA WL", C.WL["adoso"])
for k in [("1-M1-2", l) for l in "abc"] + [("1-M1-6", l) for l in "abc"] + [("1-M1-9", l) for l in "abc"] + \
        [("1-M1-10", "c"), ("1-M1-12", "a"), ("1-M1-16", "b"), ("1-M2-4", "a"), ("1-M2-5", "a"), ("1-M2-13", "a"),
         ("1-M2-13", "b"), ("1-M2-15", "a"), ("1-M2-17", "a"), ("1-M2-18", "a"), ("1-M2-21", "a"),
         ("1-M2-23", "a"), ("1-M2-24", "a"), ("1-M2-27", "a"), ("1-M2-29", "a"), ("1-M2-30", "a"),
         ("1-M2-93", "a"), ("1-M2-96", "b")]:
    print(k, "PRED:", M.PRED[k], "| BARE:", M.BARE[k])
s = ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
     "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
     "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
     "amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ")
try:
    print("COMPOSE:", D.compose(s))
except Exception as e:  # noqa: BLE001
    print("compose failed", e)
