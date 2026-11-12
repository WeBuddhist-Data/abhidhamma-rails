"""Inventory of Pañhāpucchaka answer clauses (Hindi) that match a regex, with chapters.
usage: hz_pp_clauses.py <hindi-regex> [--bak] [--strip-subj]"""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz_common
from hz_common import PARTS, pairs, short

if "--bak" in sys.argv:
    hz_common.CUR["hdir"] = os.path.join(hz_common.HERE, "backup-pre-harmonise")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
rx = re.compile(args[0])


def pp_lines(part):
    on = False
    for p, h in pairs(part):
        if "kati kusalā" in p:
            on = True
            yield p, h, True
            continue
        if not on or p.startswith("#"):
            continue
        yield p, h, False
        if "Pañhāpucchakaṃ" in p or "niṭṭhit" in p:
            on = False


if __name__ == "__main__":
    inv = collections.defaultdict(collections.Counter)
    for part in PARTS[1:]:
        for p, h, q in pp_lines(part):
            for c in re.split(r"(?<=[।;,?])\s+|…\s*", hz_common.BID.sub("", h)):
                if rx.search(c):
                    inv[c.strip(" ।;,")][short(part)] += 1
    for c, d in sorted(inv.items(), key=lambda kv: (sorted(kv[1])[0], kv[0])):
        print(f"{dict(d)} :: {c}")
