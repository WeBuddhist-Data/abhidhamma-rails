"""Per-line check of pi-2 Burmese chapters 12-14 against the Pāli, plus the pi-1 reuse tests.

usage: python3 -I -X utf8 check_ch12-14.py <pali_file> <burmese_file> [...pairs]
The approved sample checker (check_sample.py) is imported read-only; its tables are EXTENDED in memory here:
  * negations: the privatives of these chapters (adinn-, aver-, abyāpajj-, anant-, agutt-, asaṃvar-, …) and the
    glued double forms (nākusalaṃ, nāsātaṃ, nevasaññānāsaññā = 3 …);
  * numbers: cattāri / catasso / tīṇi / tisso / pañca / channaṃ / catūhi / satta, the jhāna factor counts
    (pañc- / catur- / tiv- / duv-aṅgika), catukkaṃ / pañcakaṃ;
  * lists: every «Yo / Yā / Yaṃ … –» synonym list of a non-pañhāpucchaka line: its Burmese (make_ch12-14.list_my,
    which refuses two items with one Burmese) occurs in the line, in order;
  * variants / editorial notes: as the sample, the two editorial brackets (gaṇanānupubbato …, ayaṃ pāṭho …) apart.
pi-1 REUSE: (a) every Pāli sentence / heading also in pi-1 has pi-1's final Burmese (sample test); (b) every jhāna /
citta opening («Yasmiṃ samaye … , tasmiṃ samaye») whose Pāli is a pi-1 opening contains pi-1's Burmese opening.
"""
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_sample as S  # noqa: E402  (read-only)

_spec = importlib.util.spec_from_file_location("make_ch12_14", HERE / "make_ch12-14.py")
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
M.rebuild_frames()
F = S.F

# ------------------------------------------------------------------ negations (extended)
WB, WE = S.WB, S.WE
_DOUBLE = [(r"arūpāvacarakusal\w*", 1), (r"\w*(?:vacara|uttara)kusal\w*", 0), (r"\w*rūpārūp\w*", 1), (r"neva kusal\w* nākusal\w*", 1), (r"nevasaññ[īā]nāsaññ\w*", 3), (r"nākusal\w*", 2), (r"nāsāt\w*", 2), (r"nā(?=nubyañjan)", 1),
           (r"\w*anatikkam\w*", 1), (r"\w*ānañc\w*", 1), (r"\w*viññāṇañc\w*", 1), (r"\w*ākiñc\w*", 1),
           (r"natthi", 1)]                     # ākāsānañca- / viññāṇañca- (an-anta), ākiñcañña- (a-kiñcana), natthi
_PRIV = ("adinn aver abyāpajj anant akappiy avajj anavajj agutt agopan anārakkh asaṃvar asaṃvut amattaññ asantuṭṭh "
         "appaṭisaṅkh ayonis avītikkam anācār agocar asaṃsaṭṭh ananulomik assaddh appasann anopān anattha ahita "
         "aphāsuk ayogakkhem apilāpan asammusan asithil anikkhitt avūpasam akalyat akammaññ anekaṃs apariyogāh "
         "anattaman anuddhat abyāpann akathaṃkath avikkhep avisāhār avisāhaṭ anākiṇṇ asamphuṭṭh amanasikār ases "
         "akiriy akaraṇ anajjhāpatt anodhis akupp amoh asāt appamañ").split()
S.NEG_PI_RE[:0] = [(re.compile(WB + p, re.I), w) for p, w in _DOUBLE]
S.NEG_PI_RE[len(_DOUBLE):len(_DOUBLE)] = [(re.compile(WB + p + r"\w*", re.I), 1) for p in _PRIV]

# ------------------------------------------------------------------ numbers (extended)
S.NUM_PI_RE += [(re.compile(p, re.I), v) for p, v in [
    (r"cattāri|catasso|catūhi", 4), (r"tīṇi|tisso", 3), (r"pañca|pañcahi|pañcupādānakkhandhā", 5), (r"channaṃ", 6),
    (r"satta", 7), (r"pañcaṅgik\w+", 5), (r"caturaṅgik\w+", 4), (r"tivaṅgik\w+", 3), (r"duvaṅgik\w+", 2),
    (r"catukkaṃ", 4), (r"pañcakaṃ", 5)]]

# ------------------------------------------------------------------ lists (own)
LIST_RE = re.compile(r"(?:^|\? |\. |, )(?:Yo|Yā|Yaṃ|yo|yā) (?:tasmiṃ samaye )?(?P<l>[^–?]+?) – (?:idaṃ|ayaṃ|ime|imā) "
                     r"vuccati")


def list_errs(x, y, pan):
    if pan:
        return [], 0
    errs, n = [], 0
    for m in LIST_RE.finditer(x):
        lst = m["l"]
        if "samaye" in lst:
            continue
        n += 1
        try:
            my = M.list_my(lst)
        except M.Miss as e:
            errs.append(f"list: {e}")
            continue
        if my not in y:
            errs.append("list not found: " + my[:60])
    return errs, n


S.list_errs = lambda x, y: []                  # replaced by the own list test above (per line, see check())
EDN = [re.escape(k) for k in M.EDNOTE]


def check(pali, my):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(a) != len(b):
        return [f"line count {len(a)} vs {len(b)}"], 0
    bad, lists, pan = [], 0, False
    for i, (x, y) in enumerate(zip(a, b)):
        x, y = F.ID_RE.sub("", x), F.ID_RE.sub("", y)
        if x.startswith("#"):
            pan = "Pañhāpucchakaṃ" in x or (pan and not x.startswith("#### "))
        for k, v in M.EDNOTE.items():            # editorial brackets: compared as fixed strings
            if k in x:
                if v not in y:
                    bad.append(f"line {i + 1}: editorial note")
                x, y = x.replace(k, ""), y.replace(v, "")
        errs = []
        if not x.startswith("#") and S.sent_count(x) != y.count(F.END):
            errs.append(f"sentences {S.sent_count(x)}/{y.count(F.END)}")
        nx, ny = S.neg(S.VAR_PI.sub("", x), S.NEG_PI_RE), S.neg(S.VAR_MY.sub("", y), S.NEG_MY_RE)
        if nx != ny:
            errs.append(f"negations {nx}/{ny}")
        if S.nums_pi(S.VAR_PI.sub("", x)) != S.nums_my(y):
            errs.append(f"numbers {S.nums_pi(x)}/{S.nums_my(y)}")
        va, vb = S.VAR_PI.findall(x), S.VAR_MY.findall(y)
        if len(va) != len(vb) or any(t != t2 or F.VAR_KIND.get(t) != k for (t, s), (k, s2, t2) in zip(va, vb)):
            errs.append("variants")
        le, n = list_errs(x.replace("upādinn", "upādiṇṇ"), y, pan and not x.startswith(("Cattāri", "Catasso")))
        lists += n
        errs += le + (S.term_errs(x, y) if pan else []) + S.typo_errs(y)     # «atthi sukhaṃ» (suttanta) is a noun
        if errs:
            bad.append(f"line {i + 1}: " + "; ".join(errs))
    return bad, lists


OPEN_RX = re.compile(r"(?:[Yy]asmiṃ samaye (?P<o>.+?)|(?P<t>Tasseva .+?))(?:, (?=(?:yā |yo )?tasmiṃ samaye)| "
                     r"(?=phasso…pe…))")


def reuse_open(pali, my):
    a = [l for l in pathlib.Path(pali).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in pathlib.Path(my).read_text(encoding="utf-8").splitlines() if l.strip()]
    n = same = 0
    diffs = []
    for i, (x, y) in enumerate(zip(a, b)):
        for m in OPEN_RX.finditer(F.ID_RE.sub("", x)):
            k = M.VAR.sub("", m["o"] or m["t"])
            k = k if k in M.OPEN1 else re.sub(r" \S+ viramantassa$", "", k)     # the citta core of ch14
            k = k if k in M.OPEN1 else re.sub(r" hīnaṃ… .*$", "", k)
            if k in M.OPEN1:
                n += 1
                if M.OPEN1[k] in y:
                    same += 1
                else:
                    diffs.append(f"line {i + 1}: opening «{k[:60]}» not pi-1's")
    return n, same, diffs


if __name__ == "__main__":
    args = sys.argv[1:]
    D = S.pi1_dict()
    total = 0
    for pali, my in zip(args[::2], args[1::2]):
        bad, lists = check(pali, my)
        n, same, diffs = S.reuse(pali, my, D)
        n2, same2, diffs2 = reuse_open(pali, my)
        name = pathlib.Path(my).name
        print(f"{name}: {len(bad)} mismatches ({lists} synonym lists checked); pi-1 reuse {same + same2} / {n + n2} "
              f"identical (sentences / headings {same} / {n}, openings {same2} / {n2})")
        for e in bad[:25] + diffs[:10] + diffs2[:10]:
            print("  " + e)
        total += len(bad) + len([d for d in diffs if "pi-1" in d]) + len(diffs2)
    print("OK" if not total else "MISMATCH")
    sys.exit(1 if total else 0)
