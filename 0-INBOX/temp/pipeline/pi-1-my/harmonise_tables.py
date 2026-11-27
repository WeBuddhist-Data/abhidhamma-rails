"""Consistency pass (Burmese pi-1): the same Pāli key in the generators' tables = the same Burmese.

usage: python3 -I -X utf8 harmonise_tables.py [--all] [--grep REGEX]
Imports each generator (in its own subprocess; extend() / build() called where it exists, nothing is written), dumps
every dict of str -> str / (str, …) it leaves in my_formulas and in its own module, then lists every Pāli key whose
Burmese differs between generators (or between tables). Keys listed in KEEP (genuine sense / grammar differences,
see harmonise-notes.md) are reported separately. Exit 1 if an unexplained difference is left.
"""
import collections, json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
GENS = ["make_sample", "make_ch2-01", "make_ch2-02-03", "make_ch2-04-05", "make_ch3", "make_ch4", "make_ch5"]
DUMP = r'''
import importlib.util, json, sys
sys.path.insert(0, HERE)
import my_formulas as F
spec = importlib.util.spec_from_file_location("gen", HERE + "/" + NAME + ".py")
g = importlib.util.module_from_spec(spec)
sys.argv = [NAME]
spec.loader.exec_module(g)
for fn in ("extend", "build"):
    if hasattr(g, fn) and callable(getattr(g, fn)):
        getattr(g, fn)()
out = {}
for modname, mod in (("F", F), ("G", g)):
    for k, v in vars(mod).items():
        if isinstance(v, dict) and v and not k.startswith("__"):
            d = {}
            for a, b in v.items():
                if isinstance(a, str) and isinstance(b, str):
                    d[a] = b
                elif isinstance(a, str) and isinstance(b, tuple) and b and isinstance(b[0], str):
                    d[a] = b[0]
            if d:
                out[modname + "." + k] = d
print(json.dumps(out, ensure_ascii=False))
'''
py = [sys.executable, "-I", "-X", "utf8", "-c"]
data = {}
for n in GENS:
    code = f"HERE={str(HERE)!r}\nNAME={n!r}\n" + DUMP
    r = subprocess.run(py + [code], capture_output=True, text=True, cwd=str(HERE))
    if r.returncode:
        print("FAILED", n, r.stderr[-800:]); sys.exit(2)
    data[n] = json.loads(r.stdout.strip().splitlines()[-1])
# tables whose keys are not Pāli words of the text (agreement, numbers, labels …) are skipped
SKIP = {"CU_HOTI", "CU_REL", "CU_Q", "CU_DEM", "CU_COP", "NUM", "ORD", "LABEL", "SIGLA", "VAR_KIND", "CU_NUM",
        "NUMW", "NUMMY", "CASE_MY", "COP", "NCOP", "ROLE", "JNUM", "GROUP", "CU_PAIRS", "ORDJ", "AYAT_PI", "INDR_PI",
        "ORG_NOM", "EKA_SPECIAL", "SG", "TEVA_N", "NEW", "OPEN_TABLES", "CHAPTERS", "NUMV", "JPL", "OBJ_NOM",
        "VAR_RE", "PAIRS", "CEVA_SG",
        # tables of derived grammatical forms (predicate / noun-phrase / «with them» / question frames …) of keys that
        # have their plain form in another table: not a second rendering of the key
        "PRED", "ACC2ORG", "ACC2OBJ", "ARM2OBJ", "TEHI_Y", "_IND", "HETU_KIND", "_HETU", "CNT", "KATAME", "IME",
        "OBJ", "UPAJJ", "ALLQ"}
KEEP = {   # Pāli key -> why its tables may hold more than one Burmese (sense or grammar; harmonise-notes.md)
    "atītā": "4-0x list adjective «X ဖြစ်သော» of the noun TERMS value (grammar)",
    "anāgatā": "4-0x list adjective «X ဖြစ်သော» (grammar)", "paccuppannā": "4-0x list adjective (grammar)",
    "nirutti": "4-0x synonym-list noun (the Mātikā string without «ဖြစ်သော»; grammar)",
    "paññatti": "4-0x synonym-list noun (grammar)",
    "niyatā": "4-0x ajjhatta list «restricted to each being» vs Mātikā «fixed in destiny» (sense)",
    "nāmaṃ": "«name» (adhivacana list) vs nāma «mentality» (nāmañca rūpañca) (sense)",
    "rūpa": "visible form (rūpāyatana) / matter / rūpa of nāmarūpa (sense)",
    "rūpaṃ": "visible form / matter / rūpa of nāmarūpa (sense)",
    "sineho": "cohesion of the water element (3-03) vs affection in the greed list (4-0x) (sense)",
    "hetū": "attributive TERMS / plural noun NAMES / ch5 noun (grammar)",
    "kusalaṃ": "«…nti kusalaṃ» (2-05) vs the kusala citta noun of ch5 (grammar)",
    "vipāko": "«…nti vipāko» (2-05) vs the resultant citta noun of ch5 (grammar)",
    "saññaṃ": "accusative «…ကို» in the 4-0x lists (grammar)", "vedanaṃ": "accusative «…ကို» (grammar)",
    "kāmāvacarā": "ch5 FX noun phrase «… သဘောတရားများ» (grammar)", "rūpāvacarā": "ch5 FX noun phrase (grammar)",
    "arūpāvacarā": "ch5 FX noun phrase (grammar)", "apariyāpannā": "ch5 FX noun phrase (grammar)",
}
GREP = re.compile(sys.argv[sys.argv.index("--grep") + 1]) if "--grep" in sys.argv else None
vals = collections.defaultdict(lambda: collections.defaultdict(set))
for n, tabs in data.items():
    for t, d in tabs.items():
        if t.split(".", 1)[1] in SKIP:
            continue
        for k, v in d.items():
            vals[k][v].add(f"{n.replace('make_', '')}:{t}")
bad = {k: v for k, v in vals.items() if len(v) > 1 and k not in KEEP}
if GREP:
    bad = {k: v for k, v in bad.items() if GREP.search(k) or any(GREP.search(m) for m in v)}
print("Pāli keys in the tables:", len(vals), "| with more than one Burmese:", len(bad),
      "| kept (sense / grammar):", sum(1 for k in KEEP if k in vals))
for k, v in sorted(bad.items()):
    print(f"\n{k}")
    for my, where in v.items():
        print(f"   {my[:120]}   <- {', '.join(sorted(where))[:220]}")
sys.exit(1 if bad else 0)
