"""pi-6 Burmese keyword mapping, PHASE 2, group G2: 6-01 / 6-02 sankharayamaka, 7-01 … 7-11 anusayayamaka, 8-cittayamaka.

Imports the shared module map6_rules.py; since phase 3 the group rules are book-wide in the module and this script
holds only the per-segment rules (CTX) of the group. Writes <ch>.mapped.md for each chapter in chapter order and prints the three checks per chapter.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g2.py
"""
import sys
import re
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

GROUP = ["6-01-sankharayamaka", "6-02-sankharayamaka"] + [f"7-{i:02d}-anusayayamaka" for i in range(1, 12)] + \
        ["8-cittayamaka"]

# phase 3: the chapter tables T6 / T7 / T8, the context functions f_plane_adj / f_vara and the rules V1-V7, O1-O9 are
# now book-wide in map6_rules.py (BOOK, book_auto(), title_value(), mechanics 1-5). Only the forms of ONE segment stay
# here, as per-segment rules (sid -> {kw: value}); notes-g2.md, map-harmonise-notes.md §D.
TABLES = {}
CTX = {
    "6-6-16-5-0": {"paccanīkaokāsā": "နေရာအလိုက် အငြင်းပြ ပုံစံ"},          # the slip of paccanīkaokāso (T4)
    "6-7-1": {"Sattānusayā": "ကိန်းအောင်းခြင်း ခုနစ်ပါး"},                 # count + noun, the text's classifier
    "6-7-197": {"Pajahanāvāre": "ပယ်ခြင်းအလိုက် ဖော်ပြချက်"},              # the slip of Pajahanavāre (V1)
    # the dhātu headings in a body line (R6 / rule 7: the text's whole name)
    "6-7-340": {"Dhātupucchāvāro": "ဘုံများအကြောင်း အမေး ဖော်ပြချက်"},
    "6-7-349": {"Dhātuvisajjavāro": "ဘုံများအကြောင်း အဖြေ ဖော်ပြချက်",     # (slip of Dhātuvisajjanāvāro)
                "upapattināma": "ပြန်လည် ဖြစ်ပေါ်ခြင်း"},                   # «… upapatti nāma natthi» «… ဖြစ်ပေါ်ခြင်း ဟူ၍»
    "6-8-82": {"Atikkantakālavāro": "ကာလ ကျော်လွန်ပြီးခြင်း ဖော်ပြချက်"},  # the heading standing in a body line
    "6-8-113": {"cittake": "စိတ် အပိုင်း"},                              # the cited section «“အကြင်သူအား စိတ်” အပိုင်း» (V3)
    "6-8-114": {"sarāgacittassa uppādakkhaṇe": "ရာဂ ရှိသော စိတ်၏ ဖြစ်ခြင်း ခဏ"},   # pi-2 sarāga «ရာဂ ရှိသော» (V4)
    "6-8-115": {"Pacchimakusalacittassa": "နောက်ဆုံး ကုသိုလ်စိတ်"},
}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, R.BOOK]))


def s1_review(M):
    """S1 review: every use that the module ALONE (no group table) maps by the stem fallback, compared with the final
    value: kept (same value) or corrected (a group table / context function gives another value)."""
    M0 = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.BOOK]))
    kept, corr = collections.Counter(), collections.Counter()
    for ch in GROUP:
        pa, my = R.pali(ch), R.burmese(ch)
        final = {}
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            final[sid] = [kv.split("=", 1) for kv in rest.split(", ")]
        for sid, kws in R.keyword_rows(ch):
            for i, kw in enumerate(kws):
                try:
                    v0 = M0.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    continue
                if M0.SRC.get((sid, kw)) != "stem":
                    continue
                v = final[sid][i][1]
                (kept if v == v0 else corr)[(ch, kw, v0, v)] += 1
    return kept, corr


def prior_diffs():
    """uses whose final value differs from every pi-1 … pi-5 value of the keyword (or of its base form, R1)."""
    same = new = 0
    diffs = collections.defaultdict(collections.Counter)
    for ch in GROUP:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l[1:].split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if not pv:
                    new += 1
                elif v in pv:
                    same += 1
                else:
                    diffs[(k, v)][pv.most_common(1)[0][0]] += 1
    return same, new, diffs


def main():
    M = mapper()
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    for ch in GROUP:
        if only and not any(ch.startswith(o) for o in only):
            continue
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        rules = collections.Counter(r for _, _, _, r in ruled)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ending-rule chunks {dict(rules)}")
        if "-v" in sys.argv:
            for x in unmapped:
                print("   UNMAPPED", x)
            for x in fails:
                print("   FAIL", x)
            for x in punct:
                print("   PUNCT", x)
    if "--report" in sys.argv:
        kept, corr = s1_review(M)
        print(f"S1 (module alone): uses {sum(kept.values()) + sum(corr.values())}, kept {sum(kept.values())} "
              f"({len(kept)} pairs), corrected {sum(corr.values())} ({len(corr)} pairs)")
        for (ch, k, v0, v), c in sorted(corr.items()):
            print(f"   CORR {ch} {k}: {v0} -> {v} ({c})")
        for (ch, k, v0, v), c in sorted(kept.items()):
            print(f"   KEPT {ch} {k}: {v0} ({c})")
        same, new, diffs = prior_diffs()
        print(f"prior: same {same} new {new} diff {sum(sum(c.values()) for c in diffs.values())} ({len(diffs)} pairs)")
        for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
            print(f"   DIFF {k} = {v}   prior {dict(c)}")
    return M


if __name__ == "__main__":
    main()
