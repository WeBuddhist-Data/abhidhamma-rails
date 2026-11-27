"""unmapped keywords grouped by Pāli clause: the clause, its best-matching Burmese clause, then «kw[uses]=cand¦cand».
args: CH [multi]"""
import sys, collections, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "work"))
import map5_rules as R
import cand215 as C
PS = re.compile(r"(?:…\s*pe\s*…\.?|…\.?|[?!;]|\.(?=\s|$)|–)\s*")
MS = re.compile(r"(?:…|။|–)\s*")


def split_cands(k, my):
    kl = R.low(k); out = []
    for i in range(3, len(kl) - 2):
        a, b = kl[:i], kl[i:]
        ca = [v for v, _ in C.stem_cands(a).most_common(8)]
        cb = [v for v, _ in C.stem_cands(b).most_common(8)]
        for x in ca:
            for y in cb:
                for j in ("", " "):
                    v = x + j + y
                    if v in my and v not in out:
                        out.append(v)
    return out


def main():
    ch = sys.argv[1]
    multi = "multi" in sys.argv
    lines, problems, unmapped, nne = C.M.map_chapter(ch)
    my, pa = R.burmese(ch), R.pali(ch)
    segmap = {}
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        segmap[sid] = dict(kv.split("=", 1) for kv in rest.split(", "))
    seen = collections.OrderedDict()
    for sid, k in unmapped:
        seen.setdefault(k, []).append(sid)
    groups = collections.OrderedDict()
    for k, sids in seen.items():
        if (" " in k) != multi:
            continue
        cands = [v for v, c in C.stem_cands(k).most_common(40) if all(C.ok(v, my[s]) for s in sids)]
        if not cands and " " not in k:
            cands = split_cands(k, my[sids[0]])
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
        groups.setdefault((pc[:130], best[:200]), []).append(f"{k}[{len(sids)}{'' if len(sids) > 1 else ' ' + sid}]=" + "¦".join(cands[:3]))
    print("##", ch, len(seen), "keywords,", len(unmapped), "uses")
    for (pc, best), ks in groups.items():
        print("P:", pc); print("M:", best); print("   " + "; ".join(ks))


if __name__ == "__main__":
    main()
