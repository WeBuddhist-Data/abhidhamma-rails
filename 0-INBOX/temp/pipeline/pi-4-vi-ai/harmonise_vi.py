"""Consistency (harmonise) pass for the pi-4 Vietnamese plain zero-shot (Puggalapaññatti, 12 chapter files).

Adapted from pi-3-vi-ai/harmonise_vi.py (pi-3 files untouched).
Exact old -> new string replacements, each scoped to one segment (chapter + block ID) and each with an asserted
count of occurrences in that segment. Line counts, block IDs, heading levels, dashes and ellipses are never
touched (asserted per changed line); variant brackets are asserted unchanged except by the bracket rules (HB*),
which may only change a label or separator inside a bracket (bracket count and every Pāli word asserted equal).
The builders are NOT rerun (harmonise-notes.md lists the builder constants that would need the same change).
Protected (user-approved sample, not named by harmonise-brief.md for any change): preamble.md, 1-matika.md,
2-ekakapuggalapannatti.md.
Backup of the pre-pass files: backup-pre-harmonise/ (made once by vi_common.ensure_backup, never overwritten).
The pass always reads from the backup, so it is idempotent: rerunning it rebuilds the same output.
Log: harmonise-log.tsv (rule, file, block id, line, old, new, reason). Decisions: harmonise-notes.md.

usage: python -I -X utf8 harmonise_vi.py [--dry]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PDIR, VDIR, HERE, BAK, PARTS, PROTECTED_PARTS, ID

R = []  # (rid, part, sid, old, new, count, reason)


def rule(rid, part, sid, old, new, n, reason):
    assert part in PARTS, part
    R.append((rid, part, sid, old, new, n, reason))


CH3, CH4, CH5, CH6 = "3-dukapuggalapannatti", "4-tikapuggalapannatti", "5-catukkapuggalapannatti", "6-pancakapuggalapannatti"
CH7, CH8 = "7-chakkapuggalapannatti", "8-sattakapuggalapannatti"

# =============================================================== H1 Kathañca puggalo X hoti?
# One form = the majority «Người như thế nào là X?» (ch5, 68 questions; ch6 5 «Thế nào là X?», ch8 7 «Và như thế
# nào là X?»). It keeps puggalo («Người») and kathaṃ («như thế nào») and stays distinct from the sample's
# Katamo ca puggalo X? = «Thế nào là X?»; ca is not rendered (as in the sample's Katamo ca). Answer «Như vậy là X.»
# is already uniform (ch5 64, ch6 5, ch8 7).
WHY1 = "Kathañca puggalo X hoti? = «Người như thế nào là X?» (ch5 majority, 68 of 80; distinct from Katamo ca = «Thế nào là»)"
rule("H1-kathanca", CH6, "4-192", "Thế nào là ", "Người như thế nào là ", 5, WHY1)
rule("H1-kathanca", CH8, "4-203", "Và như thế nào là ", "Người như thế nào là ", 7, WHY1)

# =============================================================== H2 samāhite citte … abhininnāmeti (ch5 ×3, ch6 ×1)
# Adjectives: ch5 wording (3 of 4 occurrences). abhininnāmeti: ch6 «dẫn tâm» in all four, because «hướng tâm» is the
# core term for vitakka («sự hướng tâm», pi-1 core list) in the jhāna formula of the same passages (ch5 ^4-183,
# ch6 ^4-198).
rule("H2-samahite", CH6, "4-198",
     "trong sạch, sáng tỏ, không vết nhơ, đã lìa những thứ làm vẩn đục, mềm mại, dễ vận dụng, vững vàng, đạt đến trạng thái bất động, vị ấy dẫn tâm",
     "trong sạch, trong sáng, không còn vết nhơ, đã lìa các thứ làm vẩn đục, trở nên mềm dẻo, dễ vận dụng, vững vàng, đạt đến sự bất động, vị ấy dẫn tâm",
     1, "identical Pāli: ch5 adjectives (3 of 4 occurrences)")
for sid in ("4-183", "4-184", "4-185"):
    rule("H2-samahite", CH5, sid, "đạt đến sự bất động, vị ấy hướng tâm đến", "đạt đến sự bất động, vị ấy dẫn tâm đến", 1,
         "abhininnāmeti = «dẫn tâm» (ch6): «hướng tâm» is vitakka («sự hướng tâm», core term) in the same passage")

# =============================================================== H3 rest of the āsavakkhaya passage (ch5 ^4-185 = ch6 ^4-198)
rule("H3-asava", CH5, "4-185", "tâm được giải thoát khỏi ô nhiễm", "tâm được giải thoát khỏi cả ô nhiễm", 3,
     "as written: kāmāsavāpi / bhavāsavāpi / avijjāsavāpi (-pi = «cả», ch6)")
rule("H3-asava", CH6, "4-198",
     "Khi đã được giải thoát, có sự hiểu biết: “Đã được giải thoát”.",
     "Khi tâm đã được giải thoát, có sự hiểu biết rằng đã được giải thoát.", 1,
     "vimuttasmiṃ vimuttamiti = ch5 form: iti = «rằng» (the Pāli has no quotation marks here); «tâm» = the cittaṃ of the preceding sentence")
rule("H3-asava", CH5, "4-185",
     "“Sự sinh đã diệt tận, đời sống tu hành trong sạch đã được sống trọn, việc cần làm đã làm xong, không còn trở lại trạng thái này nữa”",
     "“Sự sinh đã được diệt tận, đời sống tu hành trong sạch đã được sống trọn, việc cần làm đã được làm xong, không còn gì khác cho trạng thái này nữa”",
     1, "khīṇā jāti … nāparaṃ itthattāya = ch6 form: as written (nāparaṃ itthattāya has no «trở lại»)")

# =============================================================== H4 samannāgata / the beauty formula (ch5 ^4-168 = ch6 ^4-194, ^4-195)
# Rule: samannāgata = «được trang bị» for a quality or attainment one is endowed with (beauty included);
# «mang» only for bad states, obstructions and conduct / kamma (terms file; pi-2 ^2-826, ^2-830). «sở hữu» dropped.
# Rest of the formula: abhirūpa dassanīya pāsādika = ch5 «đẹp đẽ, dễ nhìn, đáng mến» (pāsādika «đáng mến» 14 of 17
# in pi-4); vaṇṇapokkharatā = pi-2 «vẻ đẹp dung mạo» (pi-2 Khuddakavatthuvibhaṅga, the seyyohamasmīti māno lines); paramāya = ch5 «tuyệt vời».
NEWB = "đẹp đẽ, dễ nhìn, đáng mến, được trang bị vẻ đẹp dung mạo tuyệt vời"
WHYB = ("samannāgata = «được trang bị» (quality possessed); identical Pāli ch5 = ch6; pāsādika «đáng mến» (pi-4 majority); "
        "vaṇṇapokkharatā = pi-2 «vẻ đẹp dung mạo»")
rule("H4-beauty", CH5, "4-168", "đẹp đẽ, dễ nhìn, đáng mến, mang vẻ đẹp tuyệt vời của nước da", NEWB, 2, WHYB)
rule("H4-beauty", CH6, "4-194", "xinh đẹp, dễ nhìn, dễ mến, sở hữu vẻ đẹp tuyệt hảo của dung sắc", NEWB, 1, WHYB)
rule("H4-beauty", CH6, "4-195", "xinh đẹp, dễ nhìn, dễ mến, sở hữu vẻ đẹp tuyệt hảo của dung sắc", NEWB, 2, WHYB)

# =============================================================== H5 Seyyathāpi so X …, tathūpamo ayaṃ puggalo
# «Như X ấy …, người này cũng giống như thế.» in ch4 (6) and ch5 (28); ch6 opened with «Giống như» (5).
for sid in ("4-194", "4-195", "4-196", "4-197", "4-198"):
    rule("H5-seyyatha", CH6, sid, "Giống như chiến binh ấy", "Như chiến binh ấy", 1,
         "Seyyathāpi so X …, tathūpamo ayaṃ puggalo = «Như X ấy …, người này cũng giống như thế» (ch4/ch5, 34 of 39)")

# =============================================================== H6 so / assa / esa by referent: a bhikkhu = «vị ấy»
# Cloth similes (ch4 ^4-116, ^4-117): the person is introduced as navo / majjhimo / thero bhikkhu; the thera lines
# already have «vị ấy» (So kupito «Vị ấy nổi giận»), the nava / majjhima lines had «người ấy». tathūpamo ayaṃ puggalo
# keeps «người này» (puggalo).
WHY6 = "referent is a bhikkhu (navo / majjhimo / thero bhikkhu) = «vị ấy», as in the thera lines of the same simile and ch5/ch6"
for sid, nhan in (("4-116", 2), ("4-117", 1)):
    rule("H6-referent", CH4, sid, "của người ấy", "của vị ấy", 6, WHY6)
    rule("H6-referent", CH4, sid, "thân cận người ấy và noi theo gương người ấy", "thân cận vị ấy và noi theo gương vị ấy", 2, WHY6)
    rule("H6-referent", CH4, sid, "Người ấy nhận", "Vị ấy nhận", nhan, WHY6)
rule("H6-referent", CH4, "4-117", "Người ấy [dị bản (mọi bản): yesaṃ kho pana", "Vị ấy [dị bản (mọi bản): yesaṃ kho pana", 1, WHY6)

# =============================================================== H7 ^4-176 puratthimena narassa (as written)
rule("H7-narassa", CH5, "4-176", "ở phía đông thành phố", "ở phía đông của một người", 1,
     "as written: narassa = 'of a man / of a person' (user rule); the agent had read nagarassa (commentary lemma "
     "«Puratthimena nagarassāti», English / Russian rails «east of the city»); listed for the user")

# =============================================================== HB variant-bracket labels / separators
# Two variants of the same kind in one bracket: the label once, the second variant with its sigla only, as in pi-1 /
# pi-2 («[dị bản (Syā.): upariṭṭhime; (Ka.): upariṭṭhimaṃ]», «[khác chính tả (Sī.): nijigiṃsanatā; (Syā.):
# jigiṃsanatā]») and ch3 ^4-47, ch6 ^4-193; variants of different kinds keep a label each (pi-1 «[khác chính tả (Sī.):
# na hetū sahetukehi; dị bản (Syā., Ka.): …]», ch4 ^4-111, ch5 ^4-176). An "evaṃ …" note appended to a
# variant (evamuparipi, evaṃ tīsu ṭhānesupi, evaṃ … -nidd-esepi) follows a comma, as in pi-2 («[khác chính tả (Syā.):
# gaṇanānupubbato, cũng vậy ở các chỗ sau]» ^2-568; ch7 ^4-202, ch8 ^4-203); any other note (padasiddhi cintetabbā,
# … pana sameti, aṭṭhakathā oloketabbā) follows «;» (pi-2 «…, cũng vậy ở các chỗ sau; nên xem chú giải»; ch3 ^4-62,
# ch4 ^4-117).
rule("HB-label", CH4, "4-107", "[dị bản (Sī.): gato; dị bản (Syā.): gantvā]", "[dị bản (Sī.): gato; (Syā.): gantvā]", 1,
     "same-kind second variant: label once (pi-1/pi-2 form; ch3, ch6)")
rule("HB-label", CH5, "4-189", "; dị bản (Ka.): na dhammamaññāya dhammānudhammappaṭipanno]",
     "; (Ka.): na dhammamaññāya dhammānudhammappaṭipanno]", 1,
     "same-kind second variant: label once (pi-1/pi-2 form; ch3, ch6)")
rule("HB-sep", CH3, "4-51", "kakkhaḷatā kakkhaḷiyaṃ; cũng vậy trong phần", "kakkhaḷatā kakkhaḷiyaṃ, cũng vậy trong phần", 1,
     "evaṃ … note after a comma (pi-2 evamuparipi form; ch7, ch8)")


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


LATIN = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")


def bracket_pali(b):
    """the Pāli words (no diacritic-free Vietnamese) inside a bracket: lowercase words with Pāli letters or sigla"""
    return [w for w in LATIN.findall(b) if re.search(r"[āīūṃṅñṭḍṇḷ]", w)]


def main(dry=False):
    if vi_common.ensure_backup():
        print("backup written:", BAK)
    by_part = collections.defaultdict(list)
    for r in R:
        assert r[1] not in PROTECTED_PARTS, r
        by_part[r[1]].append(r)
    log, changed, hits = [], collections.Counter(), collections.Counter()
    for part in PARTS:
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("﻿"), part
        if part not in by_part:
            if not dry:
                open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(text)
            continue
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of, cur = {}, []
        for k in range(len(idx)):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        orig = {k: el[idx[k]] for k in range(len(idx))}
        brule = collections.defaultdict(bool)
        for ri, (rid, _, sid, old, new, n, why) in enumerate(by_part[part]):
            ks = [k for k in range(len(idx)) if sid_of.get(k) == sid]
            assert ks, (part, sid)
            got = sum(el[idx[k]].count(old) for k in ks)
            assert got == n, (rid, part, sid, f"expected {n}, found {got}", old)
            for k in ks:
                e = el[idx[k]]
                if old in e:
                    e2 = e.replace(old, new)
                    log.append((rid, part, sid, k + 1, old, new, why))
                    el[idx[k]] = e2
                    if rid.startswith("HB"):
                        brule[k] = True
            hits[rid] += n
        for k in range(len(idx)):
            e0, e = orig[k], el[idx[k]]
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed")
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                b0, b1 = re.findall(r"\[[^\]]*\]", e0), re.findall(r"\[[^\]]*\]", e)
                if brule[k]:
                    assert len(b0) == len(b1), (part, k, "bracket count")
                    assert [bracket_pali(x) for x in b0] == [bracket_pali(x) for x in b1], (part, k, "bracket Pāli")
                else:
                    assert b0 == b1, (part, k, "brackets")
                assert e.count("…") == e0.count("…"), (part, k, "ellipsis")
                assert "—" not in e and ":-" not in e and "…." not in e, (part, k)
                assert "là là" not in e and "được được" not in e and "chánh niệm" not in e, (part, k)
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        if not dry:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tfile\tblock\tline\told\tnew\treason\n")
            for rid, part, sid, ln, old, new, why in log:
                f.write(f"{rid}\t{part}.md\t^{sid}\t{ln}\t{old}\t{new}\t{why}\n")
    for rid, n in sorted(hits.items()):
        print(f"{rid:12s} replacements={n}")
    print("lines changed per chapter:", {p.split('-')[0]: n for p, n in changed.items()},
          "total", sum(changed.values()), "(dry run)" if dry else "")


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
