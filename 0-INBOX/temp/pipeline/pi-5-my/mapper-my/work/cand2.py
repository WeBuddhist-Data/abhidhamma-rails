"""compact candidates for unmapped keywords: kw | uses | candidates | Pāli clause | best-matching Burmese clause
(the Burmese clause with the most values of the clause's other mapped words). args: CH [multi] [sid-filter]"""
import sys, collections, pathlib, importlib.util, re
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "work"))
import map5_rules as R
import cand215 as C   # noqa  (reuses POOL / stem_cands; cand215 runs only with argv? guard below)
PS = re.compile(r"(?:…\s*pe\s*…\.?|…\.?|[?!;]|\.(?=\s|$)|–)\s*")
MS = re.compile(r"(?:…|။|–)\s*")


def main():
    ch = sys.argv[1]
    multi = "multi" in sys.argv
    filt = [a for a in sys.argv[2:] if a != "multi"]
    lines, problems, unmapped, nne = C.M.map_chapter(ch)
    my, pa = R.burmese(ch), R.pali(ch)
    segmap = {}
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        segmap[sid] = dict(kv.split("=", 1) for kv in rest.split(", "))
    seen = collections.OrderedDict()
    for sid, k in unmapped:
        seen.setdefault(k, []).append(sid)
    print("##", ch, len(seen), "keywords,", len(unmapped), "uses")
    for k, sids in seen.items():
        if (" " in k) != multi:
            continue
        if filt and not any(s in filt for s in sids):
            continue
        cands = [v for v, c in C.stem_cands(k).most_common(40) if all(C.ok(v, my[s]) for s in sids)]
        sid = sids[0]
        pcl = [x for x in PS.split(R.strip_brackets(pa.get(sid, ""))) if x.strip()]
        mcl = [x for x in MS.split(re.sub(r"\s*\[[^\]]*\]", "", my[sid])) if x.strip()]
        key = R.low(k.split()[0]).lower(); key = key[:max(4, len(key) - 2)]
        pi_ = next((i for i, x in enumerate(pcl) if key in x.lower()), 0)
        pc = pcl[pi_] if pcl else ""
        tp = sum(len(x) for x in pcl) or 1; tm = sum(len(x) for x in mcl) or 1
        fp = (sum(len(x) for x in pcl[:pi_]) + len(pc) / 2) / tp
        words = re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", pc)
        vals = [segmap[sid].get(w) for w in words]
        vals = [v.split(" … ")[0].split()[0] for v in vals if v and v not in ("?", R.NONE)]
        def score(j):
            m = mcl[j]
            fm = (sum(len(x) for x in mcl[:j]) + len(m) / 2) / tm
            return sum(v[:-3] in m if v.endswith(("သော", "သည်")) else v in m for v in vals) * 10 - abs(fp - fm) * 40
        best = mcl[max(range(len(mcl)), key=score)] if mcl else ""
        strong = cands and "ctx" not in sys.argv
        print(f"{k} |{len(sids)}| {' ¦ '.join(cands[:4])}" + ("" if strong else f"\n    P: {pc[:110]}\n    M: {best[:170]}"))


if __name__ == "__main__":
    main()
