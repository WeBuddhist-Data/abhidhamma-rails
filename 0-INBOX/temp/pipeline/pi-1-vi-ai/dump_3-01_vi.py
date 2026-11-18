"""Helper for part 3-01: print the earlier Vietnamese strings the 3-01 builder reuses (read-only)."""
import importlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402
import build_ch2_01_sample_vi as C  # noqa: E402
B = importlib.import_module("build_2-01_2-02_vi")
D = importlib.import_module("build_2-03_vi")
E = importlib.import_module("build_2-04_vi")
F = importlib.import_module("build_2-05_vi")

KEYS = [("1-M1-1", "c"), ("1-M2-1", "b"), ("1-M2-2", "b"), ("1-M2-3", "b"), ("1-M2-7", "a"), ("1-M2-8", "a"),
        ("1-M2-11", "a"), ("1-M2-12", "a"), ("1-M2-15", "a"), ("1-M2-21", "a"), ("1-M2-27", "a"),
        ("1-M2-33", "a"), ("1-M2-39", "a"), ("1-M2-45", "a"), ("1-M2-51", "a"), ("1-M2-70", "a"),
        ("1-M2-76", "a"), ("1-M2-55", "b"), ("1-M2-57", "b"), ("1-M2-58", "b"), ("1-M1-3", "c"),
        ("1-M1-5", "b"), ("1-M1-6", "a"), ("1-M1-6", "b"), ("1-M1-6", "c"), ("1-M2-90", "b"), ("1-M2-91", "b"),
        ("1-M2-92", "b"), ("1-M1-8", "c"), ("1-M1-9", "c"), ("1-M1-10", "c"), ("1-M1-11", "c"),
        ("1-M1-12", "a"), ("1-M2-93", "a"), ("1-M2-94", "b"), ("1-M2-95", "b"), ("1-M2-96", "a"),
        ("1-M2-96", "b"), ("1-M1-15", "c"), ("1-M2-97", "b"), ("1-M1-17", "a"), ("1-M2-67", "a"),
        ("1-M2-67", "b"), ("1-M2-68", "a"), ("1-M2-68", "b"), ("1-M1-4", "a"), ("1-M1-4", "b"), ("1-M2-9", "a"),
        ("1-M2-9", "b"), ("1-M2-10", "a"), ("1-M2-10", "b"), ("1-M2-60", "a"), ("1-M2-60", "b"),
        ("1-M2-61", "a"), ("1-M2-61", "b"), ("1-M2-62", "a"), ("1-M2-62", "b"), ("1-M2-66", "a"),
        ("1-M2-66", "b"), ("1-M1-22", "c"), ("1-M2-13", "a"), ("1-M2-1", "a")]
for k in KEYS:
    print(k, "| BARE:", M.BARE[k], "| PRED:", M.PRED[k])
print()
for k in ["vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho", "dhammāyatanaṃ",
          "manāyatanaṃ", "jīvitindriyaṃ", "manodhātu", "manoviññāṇadhātu", "cakkhuviññāṇadhātu", "dhammadhātu",
          "kabaḷīkāro āhāro", "phassāhāro", "sukhindriyaṃ", "manindriyaṃ"]:
    print(k, "=", B.NAME.get(k))
print()
for k, v in B.PH.items():
    if any(w in k for w in ("vipāk", "kāmāvacar", "rūpāvacar", "apariyāpann", "kusal", "phoṭṭhabb", "rūpārammaṇ")):
        print("PH", k, "=", v)
print(F.KIRIYA_V)
print(E.RESULT_KAMA)
