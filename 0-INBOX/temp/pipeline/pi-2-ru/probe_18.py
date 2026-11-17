"""Chapter-18 probe: sentence-level Pāli -> Russian map from pi-2 ch1-17 (and pi-1), then report which sentences
of chapter 18 already have a Russian rendering.
usage: python -I -X utf8 probe_18.py [show_missing=1] [dump_json=0]
"""
import glob, json, os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
SPLIT = re.compile(r"(?<=[.?!])\s+(?=[\"(“«„A-ZĀĪŪṬḌÑṆṄṂḶА-ЯЁ])")
ID = re.compile(r"\s*\^[\w-]+\s*$")


def sents(s):
    return [x.strip() for x in SPLIT.split(ID.sub("", s).strip()) if x.strip()]


def build_map(pairs):
    m = {}
    for pd, rd, skip in pairs:
        for p in sorted(glob.glob(os.path.join(ROOT, "pali", pd, "*.md"))):
            name = os.path.basename(p)
            if skip and name.startswith(skip):
                continue
            rp = os.path.join(ROOT, "russian", rd, name)
            if not os.path.exists(rp):
                continue
            pl = open(p, encoding="utf-8").read().split("\n")
            rl = open(rp, encoding="utf-8").read().split("\n")
            if len(pl) != len(rl):
                continue
            for a, b in zip(pl, rl):
                if not a.strip() or a.startswith("#"):
                    continue
                sa, sb = sents(a), sents(b)
                if len(sa) == len(sb):
                    for x, y in zip(sa, sb):
                        m.setdefault(x, y)
    return m


def main():
    show = (sys.argv[1] != "0") if len(sys.argv) > 1 else True
    m = build_map([("pi-2_split_chapters", "pi-2-russian-plain-zeroshot_split_chapters", "18-"),
                   ("pi-1_split_chapters", "pi-1-russian-plain-rails_split_chapters", None)])
    src = open(os.path.join(ROOT, "pali", "pi-2_split_chapters", "18-dhammahadayavibhango.md"), encoding="utf-8").read()
    found, miss = {}, []
    for line in src.split("\n"):
        if not line.strip() or line.startswith("#"):
            continue
        for s in sents(line):
            if s in m:
                found[s] = m[s]
            else:
                miss.append(s)
    print("found", len(found), "missing", len(miss))
    for k, v in found.items():
        print("F|", k, "=>", v)
    if show:
        for s in miss:
            print("M|", s)
    if len(sys.argv) > 2 and sys.argv[2] == "1":
        json.dump(found, open(os.path.join(os.path.dirname(__file__), "probe_18_found.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
