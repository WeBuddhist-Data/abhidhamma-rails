"""Coordinator-delegated rails consistency fix, pi-5 Vietnamese (2026-11-21): where identical Pāli reads differently
across the finished rails chapters, align it by the precedence of consistency-brief.md (termbase / APPROVED.md >
pi-1 … pi-4 rails > the approved sample (preamble, 1-puggalakatha) and vi-rails-formulas.md > the earlier chapter).
The sample is never changed. Explicit (file, old, new, count) replacements, asserted; each run starts again from the
pre-fix copies in rails/consistency/ (made once, never overwritten), so it can be re-run safely; it rewrites
rails/consistency-log.tsv (file, block id, old -> new, reason). See consistency-notes.md.

usage: python -I -X utf8 -B consistency_fix_vi.py [--dry]
"""
import pathlib
import re
import shutil
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
VDIR = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
HERE = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails"
BAK = HERE / "consistency"
LOG = HERE / "consistency-log.tsv"
PROTECTED = {"preamble.md", "1-puggalakatha.md"}

# reasons
R_ETA = "etadavoca = «đã nói (với Y) điều này sao –» (sample ^5-234, ch12, ch25)"
R_UDA = "udā. citation = «Kinh Phật Tự Thuyết» (ch10 ×5, ch19, ch20; formulas: Kinh … for every collection)"
R_UPP = "buddho loke uppajjati = «xuất hiện» (termbase sambuddhā uppajjanti; pi-4 tathāgato loke uppajjati; ch3, ch16)"
R_IDHA_CAP = "sutta quote opening “idha, bhikkhave …” capitalised (sample, ch15, ch18, ch20, ch21, ch26, ch27)"
R_IDHA_EKACCO = "idha … ekacco = «Ở đời này, … có người» (pi-1 idhekacco, pi-4, sample ^5-236, ch15 ^5-481, ch27)"
R_PUNNA = "Puṇṇa (MN 57, same person as ch22 ^5-707; not in termbase) = «Pun-na» (earlier chapter ch22)"
R_MAGGA = "maggo phalaṃ nibbānaṃ … bojjhaṅgoti? = «Có phải là con đường, …» (earlier chapter ch10; ch12, ch22)"
R_SAMAP = "X-viññāṇasamaṅgī samāpannoti? = «… là người đang nhập» (termbase Samāpanno; earlier chapter ch19 ^5-616)"
R_PATIS = "dhammappaṭisaraṇo = «chỗ nương tựa về Giáo Pháp» (earlier chapter ch11; ch26)"
R_KHANDHA = "katamakkhandhapariyāpanna(nti/oti)? = «Nó nằm trong khối nào?» (earlier chapter ch16 ^5-542, ^5-543)"
R_NIRODHA = "na nirodhaṃ samāpannoti? = «Có phải đó không phải là người đang nhập sự chấm dứt không?» (earlier chapter ch16 ^5-542)"
R_ESIYA = ("samāpattesiyo … ekārammaṇoti = ch22 ^5-703 order «…, với tâm … mà nó đi kèm, …, có cùng một đối tượng» "
           "(earlier chapter); ^5-768/769 neuter forms of the same frame aligned too")
R_PANIDHI = "sāva X uppādāya āvaṭṭanā…pe… paṇidhi = «… sự mong cầu ấy là để X sinh khởi» (earlier chapter ch22)"
R_BODHI = ("satipaṭṭhānā… sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā (plural list) = «các …» on every member "
           "(earlier chapters ch2, ch8, ch10, ch11, ch20)")
R_AN = "[aṅguttaranikāye] = «[trong Tăng Chi Bộ Kinh]» (earlier chapter ch3, ^5-278 segment)"

R = [  # (file, old, new, count, reason)
    ("5-sabbamatthitikatha.md", "đã nói với Đức Thế Tôn thế này sao –", "đã nói với Đức Thế Tôn điều này sao –", 1, R_ETA),
    ("5-sabbamatthitikatha.md", "tôn giả Nan-đa-ka đã nói thế này sao –", "tôn giả Nan-đa-ka đã nói điều này sao –", 1, R_ETA),
    ("5-sabbamatthitikatha.md", "[Tăng Chi Bộ Kinh]", "[trong Tăng Chi Bộ Kinh]", 1, R_AN),
    ("10-dutiyavaggo.md", "đã nói với các tỳ-khưu thế này sao –", "đã nói với các tỳ-khưu điều này sao –", 1, R_ETA),
    ("11-tatiyavaggo.md", "tôn giả Xá-lợi-phất đã nói thế này sao –", "tôn giả Xá-lợi-phất đã nói điều này sao –", 1, R_ETA),
    ("11-tatiyavaggo.md", "Có phải đó là con đường, thành quả, Niết-bàn", "Có phải là con đường, thành quả, Niết-bàn", None, R_MAGGA),
    ("11-tatiyavaggo.md", "có phải đó là con đường, thành quả, Niết-bàn", "có phải là con đường, thành quả, Niết-bàn", None, R_MAGGA),
    ("13-pancamavaggo.md", "; Phật Tự Thuyết 76]", "; Kinh Phật Tự Thuyết 76]", 1, R_UDA),
    ("13-pancamavaggo.md", "chỗ nương tựa của Giáo Pháp", "chỗ nương tựa về Giáo Pháp", 1, R_PATIS),
    ("13-pancamavaggo.md",
     "có sự thiết lập tỉnh thức… nỗ lực đúng đắn… nền tảng thần thông… năng lực… sức mạnh… chi phần giác ngộ để đi đến sự cố định",
     "có các sự thiết lập tỉnh thức… các nỗ lực đúng đắn… các nền tảng thần thông… các năng lực… các sức mạnh… các chi phần giác ngộ để đi đến sự cố định",
     1, R_BODHI),
    ("13-pancamavaggo.md",  # ^5-429 natthi satipaṭṭhānā…pe… bojjhaṅgā (plural), the negative of the line above
     "không có sự thiết lập tỉnh thức… chi phần giác ngộ để đi đến sự cố định",
     "không có các sự thiết lập tỉnh thức… các chi phần giác ngộ để đi đến sự cố định", 1, R_BODHI),
    ("13-pancamavaggo.md", "không có chi phần giác ngộ để đi đến sự cố định",
     "không có các chi phần giác ngộ để đi đến sự cố định", 1, R_BODHI),
    ("17-navamavaggo.md", "“ở đây, này các tỳ-khưu, vị tỳ-khưu sống quán sát", "“Ở đây, này các tỳ-khưu, vị tỳ-khưu sống quán sát", 1, R_IDHA_CAP),
    ("17-navamavaggo.md", "Nằm trong khối nào?", "Nó nằm trong khối nào?", 3, R_KHANDHA),
    ("19-ekadasamavaggo.md", "Nằm trong khối nào?", "Nó nằm trong khối nào?", 3, R_KHANDHA),
    ("21-terasamavaggo.md", "Đức Phật sinh khởi ở thế gian", "Đức Phật xuất hiện ở thế gian", 1, R_UPP),
    ("22-cuddasamavaggo.md", "[Tăng Chi Bộ Kinh]", "[trong Tăng Chi Bộ Kinh]", 1, R_AN),
    ("23-pannarasamavaggo.md", "“Ở đây, này Phú-lâu-na, có người", "“Ở đời này, này Pun-na, có người", 1,
     R_IDHA_EKACCO + "; " + R_PUNNA),
    ("23-pannarasamavaggo.md", "Có phải đó là con đường, thành quả, Niết-bàn", "Có phải là con đường, thành quả, Niết-bàn", None, R_MAGGA),
    ("23-pannarasamavaggo.md", "có phải đó là con đường, thành quả, Niết-bàn", "có phải là con đường, thành quả, Niết-bàn", None, R_MAGGA),
    ("23-pannarasamavaggo.md", "Có phải người ấy không phải là người đang nhập sự chấm dứt không?",
     "Có phải đó không phải là người đang nhập sự chấm dứt không?", 1, R_NIRODHA),
    ("24-solasamavaggo.md",
     ", đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng một sự sinh khởi, có cùng một sự chấm dứt, có cùng một chỗ dựa, "
     "có cùng một đối tượng với tâm tìm cầu sự thành tựu thiền, với tâm tìm cầu sự tái sinh, với tâm an trú trong hạnh phúc "
     "ngay trong đời này không?",
     ", với tâm tìm cầu sự thành tựu thiền, với tâm tìm cầu sự tái sinh, với tâm an trú trong hạnh phúc ngay trong đời này "
     "mà nó đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng một sự sinh khởi, có cùng một sự chấm dứt, có cùng một chỗ dựa, "
     "có cùng một đối tượng không?",
     4, R_ESIYA),
    ("24-solasamavaggo.md",
     ", không đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng một sự sinh khởi, có cùng một sự chấm dứt, có cùng một chỗ dựa, "
     "có cùng một đối tượng với tâm tìm cầu sự thành tựu thiền, không với tâm tìm cầu sự tái sinh, không với tâm an trú "
     "trong hạnh phúc ngay trong đời này",
     ", không phải với tâm tìm cầu sự thành tựu thiền, không phải với tâm tìm cầu sự tái sinh, không phải với tâm an trú "
     "trong hạnh phúc ngay trong đời này mà nó đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng một sự sinh khởi, có cùng một "
     "sự chấm dứt, có cùng một chỗ dựa, có cùng một đối tượng",
     2, R_ESIYA),
    ("24-solasamavaggo.md",
     ", không… có cùng một chỗ dựa, có cùng một đối tượng với tâm tìm cầu sự thành tựu thiền",
     ", không phải với tâm tìm cầu sự thành tựu thiền… có cùng một chỗ dựa, có cùng một đối tượng",
     3, R_ESIYA),
    ("24-solasamavaggo.md",
     ", không… có cùng một đối tượng với tâm tìm cầu sự thành tựu thiền",
     ", không phải với tâm tìm cầu sự thành tựu thiền… có cùng một đối tượng",
     2, R_ESIYA),
    ("24-solasamavaggo.md", "tôn giả Ưu-đà-di đã nói thế này sao –", "tôn giả Ưu-đà-di đã nói điều này sao –", 1, R_ETA),
    ("26-attharasamavaggo.md", "sự mong cầu ấy để ", "sự mong cầu ấy là để ", 6, R_PANIDHI),
    ("26-attharasamavaggo.md", "Có phải người có được thức qua tai là người đang nhập thành tựu thiền không?",
     "Có phải người có được thức qua tai là người đang nhập không?", 1, R_SAMAP),
    ("29-ekavisatimavaggo.md",  # ^5-878 (L30 satipaṭṭhānato … ablative list, singular «xét về …», is not this frame)
     "nỗ lực đúng đắn… nền tảng thần thông… năng lực… sức mạnh… chi phần giác ngộ đã được làm mới",
     "các nỗ lực đúng đắn… các nền tảng thần thông… các năng lực… các sức mạnh… các chi phần giác ngộ đã được làm mới",
     1, R_BODHI),
    ("29-ekavisatimavaggo.md",
     "nỗ lực đúng đắn… nền tảng thần thông… năng lực… sức mạnh… chi phần giác ngộ không?",
     "các nỗ lực đúng đắn… các nền tảng thần thông… các năng lực… các sức mạnh… các chi phần giác ngộ không?",
     2, R_BODHI),
    ("30-bavisatimavaggo.md", "tôn giả Xá-lợi-phất đã nói thế này sao –", "tôn giả Xá-lợi-phất đã nói điều này sao –", 2, R_ETA),
]
# counts that depend on the file (checked by the dry run, then fixed here)
COUNTS = {("11-tatiyavaggo.md", "Có phải đó là con đường, thành quả, Niết-bàn"): 2,
          ("11-tatiyavaggo.md", "có phải đó là con đường, thành quả, Niết-bàn"): 0,
          ("23-pannarasamavaggo.md", "Có phải đó là con đường, thành quả, Niết-bàn"): 3,
          ("23-pannarasamavaggo.md", "có phải đó là con đường, thành quả, Niết-bàn"): 0}

ID = re.compile(r"\^([\w-]+)\s*$")


def seg_id(lines, i):
    for j in range(i, len(lines)):
        m = ID.search(lines[j])
        if m:
            return m.group(1)
    return "?"


def short(s, n=90):
    return s if len(s) <= n else s[:n] + "…"


def main():
    dry = "--dry" in sys.argv
    files = sorted({f for f, *_ in R})
    assert not PROTECTED & set(files), "the approved sample is never changed"
    if not dry:
        BAK.mkdir(exist_ok=True)
        for f in files:
            b = BAK / (f[:-3] + ".pre-fix.md")
            if not b.exists():
                shutil.copyfile(VDIR / f, b)
    log = []
    for f in files:
        src = (BAK / (f[:-3] + ".pre-fix.md")) if not dry and (BAK / (f[:-3] + ".pre-fix.md")).exists() else VDIR / f
        text = src.read_text(encoding="utf-8")
        assert "\r" not in text
        lines = text.split("\n")
        for (ff, old, new, n, why) in R:
            if ff != f:
                continue
            n = COUNTS.get((ff, old), n)
            got = sum(l.count(old) for l in lines)
            if dry:
                print(f"{f}\t{got}\t(expected {n})\t{short(old, 60)}")
                continue
            assert got == n, (f, old, got, n)
            for i, l in enumerate(lines):
                if old in l:
                    k = l.count(old)
                    lines[i] = l.replace(old, new)
                    for _ in range(k):
                        log.append(f"{f}\t{seg_id(lines, i)}\t{short(old)} -> {short(new)}\t{why}")
        if dry:
            continue
        out = unicodedata.normalize("NFC", "\n".join(lines))
        for bad in ("các các", "là là", "được được", "….", ".…", ":-", "chánh niệm"):
            assert out.count(bad) == text.count(bad), (f, bad)
        (VDIR / f).write_text(out, encoding="utf-8", newline="\n")
    if not dry:
        LOG.write_text("file\tblock\told -> new\treason\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")
        per = {}
        for row in log:
            per[row.split("\t")[0]] = per.get(row.split("\t")[0], 0) + 1
        for f in files:
            print(f, per.get(f, 0))
        print("total", len(log))


if __name__ == "__main__":
    main()
