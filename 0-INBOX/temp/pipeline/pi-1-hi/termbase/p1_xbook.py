"""Part-1 helper: headwords of senses-file lines lo..hi whose pi-1 candidates (all senses) share no term with the
same headword in the pi-3/4/5 Hindi termbases. Shows pi-1 senses and the prior entries, for the cross-book table.

usage: python -I -X utf8 p1_xbook.py <lo> <hi>
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\termbase")
import tb_tool_pi1 as tb  # noqa: E402


def main(a):
    lo, hi = int(a[0]), int(a[1])
    pr = tb.prior()
    for hw, ss in tb.senses()[lo - 1:hi]:
        p = pr.get(hw.lower(), [])
        if not p:
            continue
        mine = {c for _, cs in ss for c in cs}
        theirs = {x.split(" = ", 1)[1] for x in p}
        if mine & theirs:
            continue
        print(f"{hw}\t{' ; '.join(t + ': ' + ' / '.join(c) for t, c in ss)}")
        for x in p[:6]:
            print(f"    {x}")


if __name__ == "__main__":
    main(sys.argv[1:])
