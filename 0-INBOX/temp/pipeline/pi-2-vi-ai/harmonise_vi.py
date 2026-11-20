"""Consistency (harmonise) pass for the pi-2 Vietnamese plain zero-shot (Vibhaṅga, 19 part files).

Applies fixed old -> new strings (one rule is a function, D10-nhung-gi) to the Vietnamese part files. A rule touches
a Vietnamese line ONLY when the aligned Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli
pattern, and only in the parts listed for it. Line counts, block IDs, heading levels, dashes, variant brackets and
ellipses are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md.
Backup of the pre-pass files: backup-pre-harmonise/ (made once by vi_common.ensure_backup, never overwritten).
Log: harmonise-log.tsv (rule, part, segment, line, old, new).
The pass always reads from the backup, so it is idempotent: rerunning it rebuilds the same output.
Decisions and reasons: harmonise-notes.md. The builders are NOT rerun; harmonise-notes.md lists the builder
constants that would need the same change.

usage: python -I -X utf8 harmonise_vi.py [--dry]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PDIR, VDIR, HERE, BAK, PARTS, PROTECTED_PARTS, PROTECTED_1, ID

R = []  # (id, pali_regex, old, new, kind, parts_prefixes or None); kind: "str" | "rx" | "fn"


def rule(rid, pali, old, new, kind="str", parts=None):
    R.append((rid, pali, old, new, kind, parts))


# =============================================================== decision 1: the source as written
# ^2-171 (ch2, Āyatanavibhaṅga) «kilesasampayuttā ceva no ca na kilesā»: doubled negation, now rendered literally with
# both negations («nhưng không phải là không phải là phiền não»), not as meant.
rule("D1-171-negation", r"no ca na kilesā",
     "Mười lĩnh vực thì không nên nói – rằng “vừa là phiền não vừa gắn liền với phiền não”, hay rằng “gắn liền với phiền não nhưng không phải là phiền não”",
     "Mười lĩnh vực thì không nên nói – rằng “vừa là phiền não vừa gắn liền với phiền não”, hay rằng “gắn liền với phiền não nhưng không phải là không phải là phiền não”",
     parts=["2-"])
# Questions that the Pāli closes with «.» keep «.» (as pi-1 ^1-473 «… là gì.», ^1-1478).
rule("D1-question-dot", r"sabbesaṃ katame cattāro āhārā pātubhavanti\. Kabaḷīkāro",  # ^2-1014
     "bốn loại dưỡng chất nào xuất hiện ở tất cả chúng sinh? Thức ăn",
     "bốn loại dưỡng chất nào xuất hiện ở tất cả chúng sinh. Thức ăn", parts=["18-"])
rule("D1-question-dot", r"^Sabbesaṃ ekasaṅkhāto, āyu bhavati kittako\.$",  # ^2-1023 verse
     "Tuổi thọ của tất cả, khi tính gộp làm một, là bao nhiêu?",
     "Tuổi thọ của tất cả, khi tính gộp làm một, là bao nhiêu.", parts=["18-"])
rule("D1-question-dot", r"atibāḷhaṃ mayi byāvaṭā\. Idānāhaṃ",  # ^2-957 (Ja), same class (added under the rule)
     "“Sao các tôn giả lại quá bận tâm về tôi như vậy? Bây giờ",
     "“Sao các tôn giả lại quá bận tâm về tôi như vậy. Bây giờ", parts=["17-"])

# =============================================================== decision 5: vatthu (ground for X) = «chỗ dựa»
# pi-1 kilesavatthu «chỗ dựa của phiền não» (4-02, 5); pi-2 ch16/17 kilesavatthu, kusītavatthu «chỗ dựa của …».
# pi-1 has no āghātavatthu / virodhavatthu; same compound type (vatthu = ground of X) -> pi-1's «chỗ dựa».
rule("D5-vatthu", r"āghātavatth", "căn cứ của sự oán giận", "chỗ dựa của sự oán giận", parts=["3-", "17-"])
rule("D5-vatthu", r"virodhavatth", "căn cứ của sự chống đối", "chỗ dựa của sự chống đối", parts=["17-"])

# =============================================================== decision 7: sajjha / rajata (ch3 ^2-173)
# Commentary (pi-vibhanga-atthakatha ^2-217): «Sajjhūti rajataṃ … Rajatanti kahāpaṇo»: sajjha = silver
# («bạc», kept), rajata in this list = coin («đồng tiền»). jātarūparajata (ch2 ^2-162, = pi-1 ^1-616) stays «vàng bạc».
rule("D7-rajata", r"pavāḷaṃ rajataṃ jātarūpaṃ", "san hô, bạc, vàng", "san hô, đồng tiền, vàng", parts=["3-"])

# =============================================================== decision 10: identical Pāli, pi-1 wins
# (a) nāma / rūpa members in the ch6 nāmarūpa definitions: pi-1 ^1-1316 / ^1-1317 «phần tinh thần» / «phần vật
# chất» («Ở đây, phần vật chất là gì? … – đó được gọi là phần vật chất»). The compound nāmarūpa keeps pi-1 ^1-1343
# «phần tinh thần và vật chất».
NR = r"Atthi nāmaṃ, atthi rūpaṃ"
rule("D10-namarupa", NR, "Có phần tinh thần, có vật chất.", "Có phần tinh thần, có phần vật chất.", parts=["6-"])
rule("D10-namarupa", NR, "Ở đây, vật chất là gì?", "Ở đây, phần vật chất là gì?", parts=["6-"])
rule("D10-namarupa", NR, "đó được gọi là “vật chất”.", "đó được gọi là “phần vật chất”.", parts=["6-"])
rule("D10-namarupa", NR, "và đây là vật chất.", "và đây là phần vật chất.", parts=["6-"])

# (b) counted plural questions «Tattha katame tayo kusalahetū?»: pi-1 «Ở đây, ba gốc rễ thiện là những gì?» (^1-1060,
# ^1-1064, ^1-1068, ^1-1073, ^1-1077; all nine pi-1 questions that name a number use «là những gì?»). Applied to every
# pi-2 «Tattha katame/katamā/katamāni … <number> …?» question so the frame stays one form (ch10, 16, 17, 18).
NUMW = ("dve tayo tisso tīṇi cattāro catasso cattāri pañca cha satta aṭṭha nava dasa ekādasa dvādasa terasa cuddasa "
        "pannarasa soḷasa sattarasa aṭṭhārasa vīsati ekavīsati bāvīsati").split()
NUMSTEM = r"(?:dv|dvi|ti|catu|pañc|ch|satt|aṭṭh|nav|das|ekādas|dvādas|teras|cuddas|pannaras|soḷas|sattaras|aṭṭhāras|ekavīsat|bāvīsat)"
FUSED = re.compile(NUMSTEM + r"(?:a?kkhandh|āyatan|indriy|dhāt)\w*$")
PQ = re.compile(r"[Tt]attha katam\w*\b[^?]*\?")
VQ = re.compile(r"[Ởở] đây, [^?]*\?")


def counted(q):
    body = re.sub(r"^[Tt]attha katam\w*\s+", "", q).rstrip("?")
    for t in re.split(r"[\s,…]+|pe…", body):
        t = t.strip("“”\"‘’()")
        if t in NUMW or FUSED.match(t):
            return True
    return False


SKIPPED = []
NQ = [0]  # counted Pāli questions seen


def VAR_STRIP(s):
    return re.sub(r"\s*\[[^\]]*\]", "", s)


def mask(s):
    """hide «?» inside variant brackets (same length, so match positions stay valid)"""
    return re.sub(r"\[[^\]]*\]", lambda m: m.group(0).replace("?", "\x00"), s)


def nhung_gi(p, e, where):
    pq = PQ.findall(mask(VAR_STRIP(p)))
    if not any(counted(q) for q in pq):
        return e, 0
    NQ[0] += sum(counted(q) for q in pq)
    em = mask(e)
    vq = list(VQ.finditer(em))
    if len(pq) != len(vq):
        SKIPPED.append((where, f"{len(pq)} Pāli vs {len(vq)} Vietnamese questions"))
        return e, 0
    out, last, n = [], 0, 0
    for q, m in zip(pq, vq):
        if counted(q):
            s = e[m.start():m.end()]
            if s.endswith(" là gì?") and not s.endswith("là những gì?"):
                out.append(e[last:m.start()] + s[:-len(" là gì?")] + " là những gì?")
                last = m.end(); n += 1
            else:
                SKIPPED.append((where, "question does not end in «là gì?»: " + s[-40:]))
    out.append(e[last:])
    return "".join(out), n


rule("D10-nhung-gi", r"[Tt]attha katam", nhung_gi, None, kind="fn")


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    made = vi_common.ensure_backup()
    if made:
        print("backup written:", BAK)
    log = []
    tot = collections.Counter()
    changed = collections.Counter()
    hit = set()
    blocked = []
    comp = [(rid, re.compile(p), old, new, kind, parts) for rid, p, old, new, kind, parts in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("﻿"), part
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of = {}
        cur = []
        for k, li in enumerate(idx):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, kind, parts) in enumerate(comp):
                if parts and not any(part.startswith(x) for x in parts):
                    continue
                if not pr.search(p):
                    continue
                if kind == "fn":
                    e2, n = old(p, e, f"{part}:{k + 1}")
                elif kind == "rx":
                    e2, n = re.subn(old, new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    hit.add(ri)
                    if part in PROTECTED_PARTS or (part.startswith("1-") and k < PROTECTED_1):
                        blocked.append((rid, part, k + 1))
                        continue
                    log.append((rid, part, sid_of.get(k, "?"), k + 1, e, e2))
                    tot[(rid, part)] += n
                    e = e2
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed", e)
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k, "brackets")
                assert e.count("…") == e0.count("…"), (part, k, "ellipsis count")
                assert "—" not in e and ":-" not in e, (part, k)
                el[li] = e
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        if not dry:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tpart\tsegment\tline\told\tnew\n")
            for rid, part, sid, ln, old, new in log:
                f.write(f"{rid}\t{part}\t^{sid}\t{ln}\t{old}\t{new}\n")
    per = collections.defaultdict(dict)
    for (rid, part), n in tot.items():
        per[rid][part.split("-")[0]] = n
    for rid in sorted(per):
        print(f"{rid:18s} total={sum(per[rid].values()):4d} | " + ", ".join(
            f"ch{p}={n}" for p, n in sorted(per[rid].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0)))
    print("lines changed per part:", {p.split('-')[0]: n for p, n in changed.items()}, "total",
          sum(changed.values()), "(dry run)" if dry else "")
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for w, why in SKIPPED:
        print("SKIPPED", w, why)
    print("counted Pāli questions seen (D10-nhung-gi):", NQ[0])
    for ri, r in enumerate(R):
        if ri not in hit:
            print("NO HIT:", r[0], "|", str(r[2])[:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
