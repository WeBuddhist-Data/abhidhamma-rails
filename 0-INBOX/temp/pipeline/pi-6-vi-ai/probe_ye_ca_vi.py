"""Probe: «ye ca [itthiyo / purisā] somanassena / upekkhāya [<plane>ṃ] upapajjitvā parinibbāyissanti [tesaṃ X]» Pāli
phrases and the Vietnamese «và những người … Niết-bàn trọn vẹn» phrases in the same line, grouped per Pāli phrase.

usage: python -I -X utf8 -B probe_ye_ca_vi.py [--bak]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common as V

PP = re.compile(r"ye ca (?:\w+ )?(?:somanassena|upekkhāya|vinā \w+)(?: \w+)? upapajjitvā parinibbāyissanti(?: tesaṃ \w+ānaṃ)?|"
                r"ye ca (?:\w+ )?\w+ (?:somanassena|upekkhāya) upapajjitvā parinibbāyissanti(?: tesaṃ \w+ānaṃ)?")
PV = re.compile(r"(?:và|, )những (?:người|người nam|người nữ)[^,.]*? mà sau khi tái sinh[^,.]*?Niết-bàn trọn vẹn")


def main():
    if "--bak" in sys.argv:
        V.CUR["vdir"] = V.BAK
    g = collections.defaultdict(lambda: collections.defaultdict(set))
    for part in V.PARTS:
        for sid, ps, vs in V.segments(part):
            for p, v in zip(ps, vs):
                a = sorted(set(m.group(0) for m in PP.finditer(p)))
                b = sorted(set(m.group(0) for m in PV.finditer(v)))
                if a:
                    g[" | ".join(a)][" | ".join(b)].add(V.short(part))
    for k in sorted(g):
        print("P:", k)
        for vv, chs in g[k].items():
            print("   ", sorted(chs, key=lambda x: (len(x), x)), "::", vv[:400])


if __name__ == "__main__":
    main()
