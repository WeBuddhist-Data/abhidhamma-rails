"""Consistency (harmonise) pass for the pi-3 Vietnamese plain zero-shot (Dhātukathā, 16 chapter files).

Exact old -> new string replacements, each scoped to one segment (chapter + block ID) and each with an asserted
count of occurrences in that segment. Line counts, block IDs, heading levels, dashes, variant brackets and
ellipses are never touched (asserted per changed line). The builders are NOT rerun (harmonise-notes.md lists
the builder constants that would need the same change).
Protected (user-approved sample, never changed): preamble.md, 1-uddeso.md, 2-pathamanayo.md.
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


# =============================================================== H1 bare abbreviated instrumental members
# Pāli "Saṃyojanehi… ganthehi… … parāmāsehi dhammehi ye dhammā…" (ch4 ^3-187, ch10 ^3-346) and
# "… ye dhammā… āsavehi… saṃyojanehi… … upādānehi… kilesehi dhammehi ye dhammā…" (ch5 ^3-192).
# One form: every instrumental head gets «đối với» (shared frame «Đối với X, những hiện tượng nào …»); a bare
# member "Xehi…" = «đối với các X…»; "parāmāsehi dhammehi ye dhammā" = «đối với các hiện tượng là sự hiểu sai
# lệch, những hiện tượng nào» as in ch6, 11, 12, 13, 15 (5 chapters).
WHY1 = ("bare instrumental member Xehi… = «đối với các X…» (shared frame: every instrumental head «đối với»); "
        "parāmāsehi dhammehi ye dhammā = ch6/11/12/13/15 form")
OLD1 = "Đối với các xiềng xích… các nút thắt… các dòng lũ… các ách… các chướng ngại… các hiện tượng là sự hiểu sai lệch, những hiện tượng nào…"
NEW1 = ("Đối với các xiềng xích… đối với các nút thắt… đối với các dòng lũ… đối với các ách… đối với các chướng ngại… "
        "đối với các hiện tượng là sự hiểu sai lệch, những hiện tượng nào…")
rule("H1-bare", "4-tatiyanayo", "3-187", OLD1, NEW1, 1, WHY1)
rule("H1-bare", "10-navamanayo", "3-346", OLD1, NEW1, 1, WHY1)
rule("H1-bare", "5-catutthanayo", "3-192",
     "những hiện tượng nào… là ô nhiễm… là xiềng xích… là nút thắt… là dòng lũ… là ách… là chướng ngại… là sự hiểu sai lệch… là sự bám víu… đối với các hiện tượng là phiền não",
     "những hiện tượng nào… đối với các ô nhiễm… đối với các xiềng xích… đối với các nút thắt… đối với các dòng lũ… "
     "đối với các ách… đối với các chướng ngại… đối với các sự hiểu sai lệch… đối với các sự bám víu… đối với các hiện tượng là phiền não",
     1, WHY1)

# =============================================================== H2 closing verses (uddāna)
# Rules: pada = «đề mục» (headings, terms file, ch5/7/11/12/13); a count without padā in the Pāli gets no «mục»
# (as written; ch7/8/10/13 already); antara without duka = «phần xen giữa» (ch7/9/11/15), with duka «bộ đôi xen
# giữa»; tato upari = «tiếp theo đó» (ch10; uddhaṃ ch5 «Tiếp theo»), upari = «tiếp theo»; no word moves to another
# verse line (each Vietnamese verse line renders its own Pāli line); identical Pāli lines ch10 = ch13 take the
# ch13 wording (Pāli word order, «đề mục», gatā «đã được gộp vào»); jīvitaṃ = «sự sống» (pi-1 ^1-19; ch7/11);
# itthipumaṃ = «nữ tính, nam tính» (as written, no indriya); -ti dropped and each line capitalised (all verses).
# ch4 ^3-190
rule("H2-verse", "4-tatiyanayo", "3-190",
     "Ba khối, ba sự thật cũng vậy, và mười sáu năng lực;",
     "Ba khối, các sự thật cũng vậy, và mười sáu năng lực;", 1,
     "as written: «ba» not in the Pāli (tathā saccā)")
rule("H2-verse", "4-tatiyanayo", "3-190",
     "Các mục trong chuỗi điều kiện, mười bốn, rồi thêm mười bốn.",
     "Các đề mục trong chuỗi điều kiện, mười bốn, tiếp theo có mười bốn.", 1,
     "pada = «đề mục»; upari = «tiếp theo» (tato upari «tiếp theo đó»)")
rule("H2-verse", "4-tatiyanayo", "3-190",
     "Có tròn ba mươi mục, trong mười nhóm;",
     "Có tròn ba mươi đề mục, trong mười nhóm, tiếp đến;", 1,
     "pada = «đề mục»; atha stays on its own verse line («tiếp đến»), not moved to line 4")
rule("H2-verse", "4-tatiyanayo", "3-190",
     "Rồi hai mục trong các bộ đôi xen giữa nhỏ [khác chính tả (Sī.): cullantaradukā], tám mục trong các bộ đôi xen giữa lớn.",
     "Hai bộ đôi xen giữa nhỏ [khác chính tả (Sī.): cullantaradukā], tám thuộc phần xen giữa lớn.", 1,
     "atha not moved here; no padā in this line (no «mục»); mahantarā without duka = «phần xen giữa lớn»")
# ch8 ^3-316
rule("H2-verse", "8-sattamanayo", "3-316",
     "Bảy trong các bộ đôi xen giữa, và hai kết hợp với ý;",
     "Bảy trong phần xen giữa, và hai kết hợp với ý;", 1,
     "antarā without duka = «phần xen giữa» (ch7/9/11/15)")
# ch9 ^3-318 and ch15 ^3-518 (identical Pāli verse)
for part, sid in (("9-atthamanayo", "3-318"), ("15-cuddasamanayo", "3-518")):
    rule("H2-verse", part, sid,
         "Lĩnh vực đối tượng của ý, yếu tố đối tượng của ý, rồi năng lực sống, phần tinh thần và vật chất;",
         "Lĩnh vực đối tượng của ý, yếu tố đối tượng của ý, rồi sự sống, phần tinh thần và vật chất;", 1,
         "jīvitaṃ = «sự sống» (pi-1 ^1-19, ch7/11 verse); «năng lực» not in the Pāli")
    rule("H2-verse", part, sid,
         "và hai mục trong các bộ ba thì không tìm thấy.",
         "và hai trong các bộ ba thì không tìm thấy.", 1,
         "no padā in the Pāli line: no «mục»")
    rule("H2-verse", part, sid,
         "Bảy mục trong phần xen giữa thứ nhất, mười mục trong các nhóm;",
         "Bảy trong phần xen giữa thứ nhất, mười trong các nhóm, trong phần xen giữa sau;", 1,
         "no «mục» (no padā); aparante stays on its own verse line")
    rule("H2-verse", part, sid,
         "Mười bốn mục trong phần xen giữa sau, và sáu mục ở phần cuối, như vậy bốn mươi bảy hiện tượng này;",
         "Có mười bốn, và sáu ở phần cuối, như vậy bốn mươi bảy hiện tượng này;", 1,
         "aparante back on line 3; no «mục» (no padā)")
# ch10 ^3-352 = ch13 ^3-447 lines 3-6: ch13 wording
rule("H2-verse", "10-navamanayo", "3-352",
     "Mười hai mục trong chuỗi điều kiện, tiếp theo đó là mười sáu;",
     "Trong phần điều kiện có mười hai đề mục, tiếp theo đó có mười sáu;", 1,
     "identical Pāli ch10 = ch13: paccaye «trong phần điều kiện» (paccaya, not paccayākāra), pada «đề mục»; tato upari «tiếp theo đó»")
rule("H2-verse", "13-dvadasamanayo", "3-447",
     "Trong phần điều kiện có mười hai đề mục, từ đó trở đi có mười sáu;",
     "Trong phần điều kiện có mười hai đề mục, tiếp theo đó có mười sáu;", 1,
     "tato upari = «tiếp theo đó» (ch10; uddhaṃ ch5 «Tiếp theo»)")
rule("H2-verse", "10-navamanayo", "3-352",
     "Tám trong các bộ ba, và cả bốn mươi ba trong các nhóm.",
     "Trong các bộ ba có tám, và trong các nhóm có cả bốn mươi ba.", 1,
     "identical Pāli ch10 = ch13: ch13 wording (Pāli word order)")
rule("H2-verse", "10-navamanayo", "3-352",
     "Bảy trong các bộ đôi xen giữa lớn, sáu mục trong các bộ đôi cuối;",
     "Trong các bộ đôi xen giữa lớn có bảy, trong các bộ đôi cuối có sáu đề mục;", 1,
     "Pāli ch10 = ch13 except the space in piṭṭhi dukesu: ch13 wording, pada «đề mục»")
rule("H2-verse", "10-navamanayo", "3-352",
     "Các mục này được gộp vào phần giải thích đề mục thứ chín.",
     "Những đề mục này đã được gộp vào trong phần giải thích đề mục thứ chín.", 1,
     "identical Pāli ch10 = ch13: ch13 wording (pada «đề mục», gatā «đã được gộp vào»)")
rule("H2-verse", "13-dvadasamanayo", "3-447",
     "Bốn khối ngoài khối vật chất, và cả lĩnh vực ý;",
     "Bốn khối vật chất, và cả lĩnh vực ý;", 1,
     "as written: «ngoài» not in the Pāli (Rūpakkhandhā cattāro); listed for the user")
# ch6 ^3-227 = ch14 ^3-455 line 1 (identical Pāli)
for part, sid in (("6-pancamanayo", "3-227"), ("14-terasamanayo", "3-455")):
    rule("H2-verse", part, sid,
         "năng lực nữ tính, năng lực nam tính, năng lực sống, phần tinh thần và vật chất;",
         "nữ tính, nam tính, sự sống, phần tinh thần và vật chất;", 1,
         "as written: itthipumaṃ jīvitaṃ has no indriya («năng lực» added); jīvitaṃ = «sự sống» (pi-1 ^1-19, ch7/11)")


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


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
            hits[rid] += n
        for k in range(len(idx)):
            e0, e = orig[k], el[idx[k]]
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed")
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k, "brackets")
                assert "—" not in e and ":-" not in e and "…." not in e, (part, k)
                assert "là là" not in e and "được được" not in e, (part, k)
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
        print(f"{rid:10s} replacements={n}")
    print("lines changed per chapter:", {p.split('-')[0]: n for p, n in changed.items()},
          "total", sum(changed.values()), "(dry run)" if dry else "")


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
