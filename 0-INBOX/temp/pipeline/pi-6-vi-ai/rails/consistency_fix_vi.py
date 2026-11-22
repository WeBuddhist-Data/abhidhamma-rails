"""Coordinator-delegated rails consistency fix, pi-6 Vietnamese (Yamaka, 2026-11-22): where identical Pāli reads
differently across the finished rails chapters, align it by the precedence of consistency-brief.md (termbase /
APPROVED.md and the user decisions in rails-coordinator-rules.md > pi-1 … pi-5 rails > the approved sample (preamble,
1-mulayamaka) and vi-rails-formulas.md > the family setter, then the earlier chapter), and settle the coordinator's
known clashes. The sample is never changed. Explicit (file, old, new, count, reason) replacements, asserted; each run
starts again from the pre-fix copies in rails/consistency/ (made once, never overwritten), so it can be re-run safely;
it rewrites rails/consistency-log.tsv (file, block id, old -> new, reason). See consistency-notes.md.

Adapted from pi-5-vi-ai/rails/consistency_fix_vi.py (pi-5 files untouched).

usage: python -I -X utf8 -B consistency_fix_vi.py [--dry]
"""
import pathlib
import re
import shutil
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
VDIR = ROOT / "AI_translation/vietnamese/pi-6-vietnamese-plain-rails_split_chapters"
HERE = ROOT / "0-INBOX/temp/pipeline/pi-6-vi-ai/rails"
BAK = HERE / "consistency"
LOG = HERE / "consistency-log.tsv"
PROTECTED = {"preamble.md", "1-mulayamaka.md"}

# ---------------------------------------------------------------------------------------------------------------
# reasons
# ---------------------------------------------------------------------------------------------------------------
R_RUN_IN = ("clash 1: a run of groups joined flat with one run-level «và»; the inner plane / jhāna list «X và Y» is "
            "kept (flattening would read the next group as one more place after «trong» / «vào» or as an object of "
            "«nhập»), so the outer item is joined with «, và …» (coordinator rule, 3-02 / 3-03 / 10-07)")
R_RUN_FLAT = ("clash 1: nested plane-being run inside a longer run joined flat «A, B và C» with each being group "
              "spelled out (3-02 notes: Kāmāvacarā cavantānaṃ … rūpāvacarānaṃ arūpāvacarānaṃ = «…, chúng sinh trong "
              "cõi hình sắc và chúng sinh trong cõi không hình sắc»; 6-01 ^6-6-32); 10-06 / 10-07 same Pāli")
R_VIBH = ("clash 2: vibhajitabbaṃ «cũng nên phân tích như vậy» (pi-2 1-khandhavibhango «…, ở đây cũng nên phân tích "
          "như vậy»; 2-02, 3-06, 5-02, 5-03, 6-01, 6-02)")
R_PUCCHA = ("clash 2: (atītā / anāgatā / paccuppannātītā …) pucchā «các câu hỏi về …» (family setter 5-02 in "
            "rails-coordinator-rules.md; 5-02, 5-03, 6-01, 6-02)")
R_ANUP = ("clash 2: anulomampi paccanīkampi «cả chiều thuận lẫn chiều nghịch» (5-02 ^6-5-96, 5-03 ^6-5-164, 6-01 "
          "^6-6-87, 6-02 ^6-6-147 / 158); inside a «ở cả … lẫn …» list «ở cả chiều thuận lẫn chiều nghịch» (5-02 "
          "^6-5-153, same Pāli run yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi)")
R_SADIS = ("clash 2: (Yassa yatthakampi / Yassayatthakampi) sadisaṃ vitthāretabbaṃ, one subject: «… cũng nên được "
           "trình bày chi tiết giống như vậy» (family setter 3-04 ^6-3-125: sadisaṃ with one subject «giống như "
           "vậy»; the Pāli differs only in spacing)")

A = "và cõi không hình sắc"
R = [  # (file, old, new, count, reason)
    # ---- clash 1: nested runs -------------------------------------------------------------------------------------
    ("3-03-ayatanayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("3-03-ayatanayamaka.md", f"cõi hình sắc {A} và chúng sinh Vô Tưởng", f"cõi hình sắc {A}, và chúng sinh Vô Tưởng", None, R_RUN_IN),
    ("3-04-ayatanayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("3-05-ayatanayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("3-05-ayatanayamaka.md", f"cõi hình sắc {A} và chúng sinh Vô Tưởng", f"cõi hình sắc {A}, và chúng sinh Vô Tưởng", None, R_RUN_IN),
    ("3-06-ayatanayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("6-01-sankharayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("6-01-sankharayamaka.md", "tầng thiền thứ hai và tầng thiền thứ ba và chúng sinh",
     "tầng thiền thứ hai và tầng thiền thứ ba, và chúng sinh", None, R_RUN_IN),
    ("6-01-sankharayamaka.md", "tầng thiền thứ ba và tầng thiền thứ tư và chúng sinh",
     "tầng thiền thứ ba và tầng thiền thứ tư, và chúng sinh", None, R_RUN_IN),
    ("6-02-sankharayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("6-02-sankharayamaka.md", "tầng thiền thứ hai và tầng thiền thứ ba và chúng sinh",
     "tầng thiền thứ hai và tầng thiền thứ ba, và chúng sinh", None, R_RUN_IN),
    ("10-06-indriyayamaka.md", f"Ở chúng sinh trong cõi hình sắc {A} và những người n",
     "Ở chúng sinh trong cõi hình sắc, chúng sinh trong cõi không hình sắc và những người n", None, R_RUN_FLAT),
    ("10-07-indriyayamaka.md", f"Ở chúng sinh trong cõi hình sắc {A} và những người n",
     "Ở chúng sinh trong cõi hình sắc, chúng sinh trong cõi không hình sắc và những người n", None, R_RUN_FLAT),
    ("10-10-indriyayamaka.md", f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A}, và những người nào", None, R_RUN_IN),
    ("10-11-indriyayamaka.md", f"cõi hình sắc {A} và chúng sinh Vô Tưởng", f"cõi hình sắc {A}, và chúng sinh Vô Tưởng", None, R_RUN_IN),
    ("10-12-indriyayamaka.md", f"cõi hình sắc {A} và chúng sinh Vô Tưởng", f"cõi hình sắc {A}, và chúng sinh Vô Tưởng", None, R_RUN_IN),
    # ---- clash 2: editorial notes ---------------------------------------------------------------------------------
    ("4-dhatuyamaka.md", "“Các cặp câu hỏi về các yếu tố” cũng nên được phân tích như vậy",
     "“Các cặp câu hỏi về các yếu tố” cũng nên phân tích như vậy", 1, R_VIBH),
    ("3-04-ayatanayamaka.md",
     "câu hỏi về quá khứ theo chiều thuận và chiều nghịch [dị bản (Sī., Syā., Ka.): paccaniyampi] đều giống nhau.)",
     "các câu hỏi về quá khứ, cả chiều thuận lẫn chiều nghịch [dị bản (Sī., Syā., Ka.): paccaniyampi], đều giống nhau.)",
     1, R_PUCCHA + "; " + R_ANUP),
    ("3-04-ayatanayamaka.md", "(Như trong mục về sự sinh khởi, câu hỏi về tương lai",
     "(Như trong mục về sự sinh khởi, các câu hỏi về tương lai", 1, R_PUCCHA),
    ("3-05-ayatanayamaka.md",
     "(Câu hỏi về quá khứ ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt, theo chiều thuận và chiều "
     "nghịch đều giống nhau)",
     "(Các câu hỏi về quá khứ ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt, cả chiều thuận lẫn chiều "
     "nghịch đều giống nhau)", 1, R_PUCCHA + "; " + R_ANUP),
    ("3-06-ayatanayamaka.md",
     "(Câu hỏi về hiện tại và quá khứ như đã được phân tích trong mục về sự sinh khởi, ở sự sinh khởi và sự chấm dứt, "
     "câu hỏi về hiện tại và quá khứ theo chiều thuận và chiều nghịch cũng nên phân tích như vậy",
     "(Các câu hỏi về hiện tại và quá khứ như đã được phân tích trong mục về sự sinh khởi, ở sự sinh khởi và sự chấm "
     "dứt, các câu hỏi về hiện tại và quá khứ, cả chiều thuận lẫn chiều nghịch, cũng nên phân tích như vậy",
     1, R_PUCCHA + "; " + R_ANUP + " (= 6-02 ^6-6-147)"),
    ("3-06-ayatanayamaka.md",
     "(Câu hỏi về quá khứ và tương lai [dị bản (Syā.): atītenānāgatā] ở cả phần về người, phần về nơi chốn lẫn phần về "
     "người và nơi chốn, theo chiều thuận và chiều nghịch, như đã",
     "(Các câu hỏi về quá khứ và tương lai [dị bản (Syā.): atītenānāgatā] ở cả phần về người, phần về nơi chốn lẫn "
     "phần về người và nơi chốn, ở cả chiều thuận lẫn chiều nghịch, như đã", 1, R_PUCCHA + "; " + R_ANUP),
    ("3-06-ayatanayamaka.md", ", câu hỏi về quá khứ và tương lai cũng nên phân tích như vậy.)",
     ", các câu hỏi về quá khứ và tương lai cũng nên phân tích như vậy.)", 1, R_PUCCHA),
    ("5-02-saccayamaka.md", "(Phần về người và nơi chốn cũng nên được trình bày chi tiết giống nhau)",
     "(Phần về người và nơi chốn cũng nên được trình bày chi tiết giống như vậy)", 1, R_SADIS),
]
# counts of the clash-1 strings (taken from the dry run, then fixed here so that any drift fails)
_NN, _CV = f"cõi hình sắc {A} và những người nào", f"cõi hình sắc {A} và chúng sinh Vô Tưởng"
_J2, _J4 = "tầng thiền thứ hai và tầng thiền thứ ba và chúng sinh", "tầng thiền thứ ba và tầng thiền thứ tư và chúng sinh"
_FL = f"Ở chúng sinh trong cõi hình sắc {A} và những người n"
COUNTS = {("3-03-ayatanayamaka.md", _NN): 2, ("3-03-ayatanayamaka.md", _CV): 4,
          ("3-04-ayatanayamaka.md", _NN): 2,
          ("3-05-ayatanayamaka.md", _NN): 1, ("3-05-ayatanayamaka.md", _CV): 4,
          ("3-06-ayatanayamaka.md", _NN): 2,
          ("6-01-sankharayamaka.md", _NN): 4, ("6-01-sankharayamaka.md", _J2): 4, ("6-01-sankharayamaka.md", _J4): 2,
          ("6-02-sankharayamaka.md", _NN): 8, ("6-02-sankharayamaka.md", _J2): 4,
          ("10-06-indriyayamaka.md", _FL): 6, ("10-07-indriyayamaka.md", _FL): 6,
          ("10-10-indriyayamaka.md", _NN): 12, ("10-11-indriyayamaka.md", _CV): 6, ("10-12-indriyayamaka.md", _CV): 12}

ID = re.compile(r"\^([\w-]+)\s*$")
BAD = ("—", "–", "….", ".…", ":-", "là là", "được được", "chánh niệm", "vẫn đã", "Vào tâm mà ngay sau đó", ", ,",
       " và và ", ",,")


def seg_id(lines, i):
    for j in range(i, len(lines)):
        m = ID.search(lines[j])
        if m:
            return m.group(1)
    return "?"


def short(s, n=110):
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
        b = BAK / (f[:-3] + ".pre-fix.md")
        src = b if b.exists() else VDIR / f
        text = src.read_text(encoding="utf-8")
        assert "\r" not in text and text == unicodedata.normalize("NFC", text)
        lines = text.split("\n")
        for (ff, old, new, n, why) in R:
            if ff != f:
                continue
            n = COUNTS.get((ff, old), n)
            got = sum(l.count(old) for l in lines)
            if dry:
                print(f"{f}\t{got}\t(expected {n})\t{short(old, 70)}")
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
        for bad in BAD:
            assert out.count(bad) == text.count(bad), (f, bad)
        assert out.count("\n") == text.count("\n")
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
