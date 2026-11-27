"""pi-6 phase 1, task 4: the recurring frames check for phase 2.

The 200 most frequent keywords of the WHOLE book (all 44 <ch>.keywords.md); for every use, the value the shared module
gives (map6_rules.Mapper with the module tables only: no chapter table, no CTX) and its presence in that segment's
Burmese (all 44 chapter files). Writes frame-coverage.md. Nothing is mapped or written besides that report.
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 frame_coverage.py
"""
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

TOP = 200


def main():
    uses = collections.Counter()
    where = collections.defaultdict(list)          # kw -> [(ch, sid)]
    for ch in R.CHAPTERS:
        for sid, kws in R.keyword_rows(ch):
            for k in kws:
                uses[k] += 1
                where[k].append((ch, sid))
    top = [k for k, _ in uses.most_common(TOP)]
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
    rows = []
    for k in top:
        vals = collections.Counter()
        ok = 0
        fails = collections.defaultdict(list)      # ch -> [(sid, reason)]
        srcs = collections.Counter()
        for ch, sid in where[k]:
            my, pa = R.burmese(ch).get(sid, ""), R.pali(ch).get(sid, "")
            try:
                v = M.lookup(ch, sid, k, pa, my)
            except KeyError:
                fails[ch].append((sid, "no value"))
                continue
            vals[v] += 1
            srcs[M.SRC.get((sid, k), "?").split(":")[0]] += 1
            if R.presence(v, my)[0]:
                ok += 1
            else:
                fails[ch].append((sid, f"«{v}» not in the text"))
        rows.append((k, uses[k], vals, ok, fails, srcs))
    full = sum(1 for r in rows if r[3] == r[1])
    out = ["# pi-6 phase 1: recurring frames check (the 200 most frequent keywords of the whole book)", "",
           "Written by `frame_coverage.py` with the shared module `map6_rules.py` alone (no chapter table, no per-segment "
           "override): for every use of the keyword in the 44 `*.keywords.md`, the value the module gives in that "
           "segment and its presence in that segment's FINAL Burmese (the presence verifier of the module). "
           "«uses» = keyword uses; «values» = the values given (most frequent first, with uses); «presence» = uses whose "
           "value is in the segment's text; «source» = where the value came from (frame / stock = module tables, verb / "
           "participle / khandha / mula / place = the morphology R2-R5, base = R1, terms = my6-zeroshot-terms, pi-N = a "
           "pi-N value, compose, heading, stem).", "",
           f"**{full} of {len(rows)} keywords reach 100% presence**; "
           f"{sum(r[3] for r in rows)} of {sum(r[1] for r in rows)} uses present.", "",
           "| # | keyword | uses | values (uses) | presence | source | chapters where it fails (why) |",
           "|---|---|---|---|---|---|---|"]
    for i, (k, n, vals, ok, fails, srcs) in enumerate(rows, 1):
        vs = "; ".join(f"{v} ({c})" for v, c in vals.most_common(4)) + (" …" if len(vals) > 4 else "")
        fs = "; ".join(f"{ch} {len(x)}× (e.g. ^{x[0][0]}: {x[0][1]})" for ch, x in sorted(fails.items())) or "-"
        src = ", ".join(f"{s} {c}" for s, c in srcs.most_common(3))
        out.append(f"| {i} | {k} | {n} | {vs} | {ok}/{n} ({100 * ok / n:.0f}%) | {src} | {fs} |")
    tot = ok_all = unm = wrong = 0
    unm_kw, stem_kw = set(), collections.Counter()
    for ch in R.CHAPTERS:
        B, P = R.burmese(ch), R.pali(ch)
        for sid, kws in R.keyword_rows(ch):
            for k in kws:
                tot += 1
                try:
                    v = M.lookup(ch, sid, k, P.get(sid, ""), B.get(sid, ""))
                except KeyError:
                    unm += 1
                    unm_kw.add(k)
                    continue
                if M.SRC.get((sid, k)) == "stem":
                    stem_kw[k] += 1
                if R.presence(v, B.get(sid, ""))[0]:
                    ok_all += 1
                else:
                    wrong += 1
    out += ["", NOTES.format(tot=tot, ok=ok_all, unm=unm, unm_kw=len(unm_kw), wrong=wrong,
                             stem_uses=sum(stem_kw.values()), stem_kw=len(stem_kw))]
    (HERE / "frame-coverage.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("full", full, "of", len(rows), "uses ok", sum(r[3] for r in rows), "of", sum(r[1] for r in rows))
    for k, n, vals, ok, fails, srcs in rows:
        if ok < n:
            print(f"{k} {ok}/{n} {vals.most_common(3)} {[(c, x[:2]) for c, x in list(fails.items())[:3]]}")


NOTES = """## Notes for phase 2

**Module errors found by this check and fixed in `map6_rules.py`** (first run: 179 of 200 at 100%): the moment
phrases had no value (cittassa bhaṅgakkhaṇe / uppādakkhaṇe, bhaṅgakkhaṇe, pavatte: STOCK, harmonise B1 «… ခဏ»
without «၌», «ဘဝ တည်နေစဉ်»); counts + noun took a person classifier from elsewhere in the segment («နှစ်ယောက် …
ခံစားမှု»: compose now joins the noun with the adjacent count, «ခံစားမှု နှစ်ပါး»); the sacca names had no value or a
wrong stem value (maggasaccaṃ «မဂ်နှင့် ပြည့်စုံသော» from S1: family R8 «X သစ္စာ»); the -samaṅgī persons, the
anusaya names in the oblique cases, aggamagga, arahantānaṃ, puthujjanā, nirodhasamāpannānaṃ, pahīno / appahīno,
pacchimacitta (STOCK / R8); persons before a noun («နောက်ဆုံး ဘဝ ရှိသော ယောက်ျား», «အခြား ယောက်ျား»: tuples);
two planes sharing «၌ ရှိသူ» (R5 shared_being), «ကာမဘုံနှင့် ဆိုင်သော» (R5); the «(X-mūlakaṃ)» labels (R4 mulaka);
the contraction nānuseti (R2).

**Genuine context differences** (one keyword, two forms of the text; the module picks the segment's own form, no
action needed): upapajjantānaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» / «ပြန်လည် ဖြစ်ပေါ်ဆဲ» (before another person noun);
uppajjissati «ဖြစ်ပေါ်လိမ့်မည်» / «ဖြစ်ပေါ်မည့်» (relative clause «… ဖြစ်ပေါ်မည့်သူတို့», rule 3); Itaresaṃ «အခြားသူ» /
«အခြား»; Pacchimabhavikānaṃ, pañcavokārānaṃ, arūpāvacarānaṃ «…ရှိသူ» / «…ရှိသော» (before a noun); rūpāvacarānaṃ /
kāmāvacarānaṃ «P၌ ရှိသူ» / «P … ရှိသူ» / «Pနှင့် ဆိုင်သော»; rūpaṃ «ရုပ်» / «အဆင်းအရောင်» (rūpāyatana sense, f_rupam).

**Values from the stem fallback (S1)**: in the top 200 only Aṭṭhamako «အဋ္ဌမ» (51 uses; check the chapter's own word in
phase 2); in the whole book {stem_uses} uses of {stem_kw} keywords: review them in phase 2 (they are present but not checked by eye).

**Whole-book dry run** (all {tot} keyword uses of the 44 files, module only): {ok} present, {unm} uses ({unm_kw}
keywords) without a value, {wrong} with a value not in the text. The groups without a value, for the phase-2 chapter tables: sānusayo /
niranusayo (-ti, -ā) (ch. 7); sacakkhuka / acakkhuka / sasotaka / asotaka / sacittaka / arūpaka persons «မျက်စိ ရှိလျက် /
မရှိဘဲ …» (ch. 3, 4, 10; harmonise table: value «… ရှိသော / မရှိသော» by the ending rule); the X-sampayutta /
X-vippayutta + citta compounds «Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ်» and their moment phrases (ch. 5, 9, 10;
pi-1 rule 3 «…နှင့် ကင်းကွာသော»); avitakkaavicāra / savitakkasavicāra (ch. 6); Abhisametāvīnaṃ / Anabhisametāvīnaṃ
(ch. 5; harmonise A1 «ထင်ထင်ရှားရှား သိမြင်ပြီးသူ»); the cited forms Yassakampi / yassayatthakampi (ch. 3, 5, 6);
caññe (ch. 5), bhaṅgā (ch. 7), aññaṃ, anaññātaññassāmīti (ch. 10; harmonise A2), tesaṃyeva (ch. 6; harmonise B1
«ထိုသူတို့၏ပင်»), Atītānāgataṃ (ch. 8).
"""


if __name__ == "__main__":
    main()
