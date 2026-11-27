"""pi-6 Burmese keyword mapping, PHASE 1: preamble, 1-mulayamaka, 2-01-khandhayamaka.

Uses the shared module map6_rules.py (side-effect free). Writes <ch>.mapped.md for the three sample chapters, runs the
verifier (keyword preservation, presence, punctuation) and prints the numbers of map-table.md.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_sample.py [--table]
"""
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

# chapter tables: only what the module does not settle (see map-table.md)
T_PRE = {}
T_CH1 = {}
T_CH2 = {}
TABLES = {"preamble": T_PRE, "1-mulayamaka": T_CH1, "2-01-khandhayamaka": T_CH2}
# per-segment overrides (sid -> {kw: value})
CTX = {}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, T_CH1, T_CH2]))


def run(write=True):
    M = mapper()
    out = {}
    for ch in R.SAMPLE:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        out[ch] = (lines, problems, unmapped, nne)
        if write:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return M, out


def compare_prior(M):
    """uses whose value equals / differs from a pi-1 … pi-5 value of the same keyword (or its base form)."""
    same = new = diff = 0
    diffs = collections.defaultdict(collections.Counter)
    for ch in R.SAMPLE:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
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
                    diff += 1
                    diffs[(k, v)][pv.most_common(1)[0][0]] += 1
    return same, new, diff, diffs


REASONS = {
    "nāmā": "rule 11 (sense): nāma = mentality «စိတ်ပိုင်း» (pi-1 nāma ^1-M2-109, my6-zeroshot-terms §7); pi-5 «အမည်» is 'name' and not in the segment",
    "anulomaṃ": "approved sample departure 2 (notes-sample): the Yamaka sense «အဟုတ်ပြ ပုံစံ» (affirmative form); pi-5 «အစဉ်အတိုင်း» is the debate order and not in the segment",
    "paccanīkaṃ": "as anulomaṃ: «အငြင်းပြ ပုံစံ» (negated form); pi-5 «ပြောင်းပြန်» not in the segment",
    "arūpaṃ": "rule 11 (sense): the plane «ရုပ်မရှိသော ဘုံ» (pi-5 arūpe, my6-zeroshot-terms §6); pi-2 / pi-5 «ရုပ် မဟုတ်သော» is the adjective 'non-material', not in the segment",
    "arūpā": "rule 11 (sense) / R5: the ablative of the plane «ရုပ်မရှိသော ဘုံမှ» (Arūpā cavantānaṃ); pi-2 «ရုပ် မဟုတ်သော» is the adjective 'non-material', not in the segment",
    "ekamūlakaṃ": "the pi-6 text's word «တူညီသော အမြစ်ကို အခြေခံ» (eka = the same root, notes-sample); pi-3 «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā ekamūlaka) is not in the segment",
    "paccayo": "the hetuvāra list gives each of the ten synonyms its own word (notes-sample departure 1): paccaya «အထောက်အပံ့» (pi-1 ^1-1344); pi-5 «အကြောင်း» is hetu's word in the same verse",
    "sambhavo": "the hetuvāra word «ဖြစ်တည်ရာ» (NEW in the pi-6 text); pi-2 «ဖြစ်ပေါ်လာသော» not in the segment",
    "kusalahetū": "approved sample departure 1: hetu «အကြောင်း» in the hetuvāra list; pi-1 / pi-2 «ကုသိုလ် အမြစ်» not in the segment",
    "viññāṇañca": "R1: viññāṇaṃ + ca «သိစိတ်»; the pi-1 / pi-5 key viññāṇañca is the homograph of viññāṇañc(āyatana) «အဆုံး မရှိသော သိစိတ်», not in the segment",
    "nāmapaccayā": "the hetuvāra predicate «စိတ်ပိုင်း၏ အထောက်အပံ့» (X-paccayā = having X as support); pi-2 «စိတ်ပိုင်းကြောင့်» is the paṭiccasamuppāda ablative and not in the segment",
}


def reason(k):
    for key in [k] + R.base_forms(k) + [R.low(k)] + [R.low(b) for b in R.base_forms(k)]:
        if key in REASONS or R.low(key) in REASONS:
            return REASONS.get(key) or REASONS[R.low(key)]
    return "?"


def write_table(M, out, same, new, diff, diffs):
    """map-table.md: numbers, rules, the keyword -> Burmese table of the sample (written from the mapped files)."""
    L = [HEAD, "## Numbers", ""]
    for ch in R.SAMPLE:
        n, bad, fails, punct, ruled = R.verify_file(ch)
        L.append(f"- `{ch}.mapped.md`: {n} lines, keyword preservation `bad {bad}`, presence failures {len(fails)}, "
                 f"«, » / «၊» / « / » in a value {len(punct)}, (no direct equivalent) {out[ch][3]}, chunks matched by an "
                 f"ending rule {len(ruled)}.")
    pairs = collections.Counter()
    src = {}
    for ch in R.SAMPLE:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                pairs[(k, v)] += 1
                src.setdefault((k, v), M.SRC.get((sid, k), "?"))
    srcs = collections.Counter()
    for (k, v), c in pairs.items():
        srcs[src[(k, v)].split(":")[0]] += c
    tot = same + new + diff
    same_kw = len({k for (k, v) in pairs if v in R.prev_vals(k) or any(v in R.prev_vals(b) for b in R.base_forms(k))})
    L += [f"- Keyword uses {tot}: the same value as a pi-1 … pi-5 mapping of that keyword (or of its base form, R1) "
          f"{same} (in {same_kw} keywords); a keyword that pi-1 … pi-5 never mapped {new}; a value different from "
          f"pi-1 … pi-5 {diff} (in {len(diffs)} keyword / value pairs, listed below with the reason).",
          "- Source of the values (uses): " + ", ".join(f"{x} {c}" for x, c in srcs.most_common()) +
          " (frame / stock = the module tables; "
          "verb / khandha / mula / place / family = the morphology R2-R5, R8; base = R1 on a table value; terms = "
          "my6-zeroshot-terms; compose = members joined (Q3); heading = R6; title = rule 7).", "", RULES,
          "## Values different from pi-1 … pi-5 (same keyword)", "",
          "| keyword = pi-6 value | pi-1 … pi-5 value (uses here) | reason |", "|---|---|---|"]
    for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
        L.append(f"| {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()) + f" | {reason(k)} |")
    rk = collections.Counter()
    ex = {}
    for ch in R.SAMPLE:
        for sid, k, c, r in R.verify_file(ch)[4]:
            rk[r] += 1
            ex.setdefault(r, f"^{sid} {k}: «{c}»")
    L += ["", "## Presence: chunks matched by an ending rule (no other exception)", "",
          "Every chunk of every value stands in its segment's Burmese, literally or by one of the approved ending rules "
          "of the verifier (pi-1 rules 3 / 4 / 8, pi-2 N11, pi-3 M7, pi-4 P3 / A2, pi-5 Q1): no presence failure and no "
          "exception outside these rules.", "", "| rule | chunks | example |", "|---|---|---|"]
    for r, c in rk.most_common():
        L.append(f"| {r} | {c} | {ex[r]} |")
    L += ["", "## Keyword → Burmese (sample chapters; uses; source)", "",
          "| keyword | Burmese | uses | source |", "|---|---|---|---|"]
    for (k, v), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
        L.append(f"| {k} | {v} | {c} | {src[(k, v)]} |")
    (HERE / "map-table.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    M, out = run()
    for ch in R.SAMPLE:
        lines, problems, unmapped, nne = out[ch]
        n, bad, fails, punct, ruled = R.verify_file(ch)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)}")
        for x in unmapped[:40]:
            print("   UNMAPPED", x)
        for x in fails[:40]:
            print("   FAIL", x)
        for x in punct[:10]:
            print("   PUNCT", x)
    src = collections.Counter(M.SRC.values())
    print("sources", src.most_common())
    same, new, diff, diffs = compare_prior(M)
    print("same", same, "new", new, "diff", diff)
    if "--table" in sys.argv:
        write_table(M, out, same, new, diff, diffs)
    if "--diff" in sys.argv:
        for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
            print(f"   {k} = {v}   prior {dict(c)}")


from map_sample_text import HEAD, RULES   # noqa: E402  (the prose of map-table.md)

if __name__ == "__main__":
    main()
