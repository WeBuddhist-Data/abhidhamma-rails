r"""Review fixes, pi-5 Vietnamese rails, part r1 (preamble.md, 1-puggalakatha.md, 2-parihanikatha.md).

User decision 2026-11-22 "Approve as proposed" (review\findings-summary.md A + B; review\findings-r1.md).
Builds from rails\backup-pre-review\<ch>.md (made once, from the chapter as it was before the review fixes),
so it can be re-run. Every rule asserts its occurrence count. Logs to rails\review-fixes-log-r1.tsv.

usage: python -I -X utf8 -B review_fixes_r1_vi.py [--dry]
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
CH = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails"
BACK = RAILS / "backup-pre-review"
LOG = RAILS / "review-fixes-log-r1.tsv"
FILES = ["preamble.md", "1-puggalakatha.md", "2-parihanikatha.md"]
DRY = "--dry" in sys.argv

ID = re.compile(r"\^(\S+)\s*$")

# ch2 ^5-242 … ^5-263: the clause "…, bậc X (na) parihāyati" gets a link word (findings-r1 MINOR, A20).
CH2_RANGE = ["5-%d" % n for n in range(242, 264)]
TOK = r"(dứt bỏ|khổ đau|sự phát sinh|sự chấm dứt|con đường|bốn sự thật|nhiều hơn|vượt trội hơn|giác ngộ|chứng nghiệm)"
SUBJ = r"(bậc (?:(?!khi )[^,;.?…])*?)"

# (file, [block ids], kind, old, new, expected total count, decision)
RULES = [
    # ---- 1-puggalakatha.md (the approved sample chapter)
    ("1-puggalakatha.md", ["5-91", "5-93", "5-227", "5-228"], "str",
     "linh hồn cũng chính là thân thể", "linh hồn và thân thể là một", 6, "B4"),
    ("1-puggalakatha.md", ["5-91"], "str",
     "cùng với sự tạo tác", "cùng với các tạo tác", 1, "minor"),
    ("1-puggalakatha.md", ["5-92"], "str",
     "không có sự tạo tác", "không có các tạo tác", 1, "minor"),
    ("1-puggalakatha.md", ["5-104", "5-105", "5-106"], "re",
     r"(\u201cngười có [^\u201d]*?) đã chấm dứt\u201d", "\\1 ấy đã chấm dứt\u201d", 6, "A9"),
    ("1-puggalakatha.md", ["5-194", "5-196"], "str",
     "yếu tố tai thuộc cõi trời", "yếu tố thiên nhĩ", 2, "B6"),
    ("1-puggalakatha.md", ["5-195"], "str",
     "Ai thi triển thần thông, có phải chính người ấy là người không? Ai không thi triển thần thông, "
     "người ấy không phải là người sao?",
     "Có phải ai thi triển thần thông thì chính người ấy là người không? Có phải ai không thi triển thần "
     "thông thì người ấy không phải là người không?", 1, "A10"),
    ("1-puggalakatha.md", ["5-196"], "str",
     "Ai nghe âm thanh bằng", "Có phải ai nghe âm thanh bằng", 1, "A10"),
    ("1-puggalakatha.md", ["5-196"], "str",
     "tự mình chứng nghiệm sự diệt tận các ô nhiễm, có phải chính người ấy là người không? Ai không tự "
     "mình chứng nghiệm sự diệt tận các ô nhiễm, người ấy không phải là người sao?",
     "tự mình chứng nghiệm sự diệt tận các ô nhiễm thì chính người ấy là người không? Có phải ai không "
     "tự mình chứng nghiệm sự diệt tận các ô nhiễm thì người ấy không phải là người không?", 1, "A10"),
    ("1-puggalakatha.md", ["5-214"], "str",
     "ba đặc tính do điều kiện tạo thành của cái do điều kiện tạo thành",
     "ba đặc tính riêng của cái do điều kiện tạo thành", 1, "minor"),
    ("1-puggalakatha.md", ["5-215"], "str",
     "ba đặc tính không do điều kiện tạo thành của cái không do điều kiện tạo thành",
     "ba đặc tính riêng của cái không do điều kiện tạo thành", 1, "minor"),
    ("1-puggalakatha.md", ["5-227"], "str",
     "Không nên nói như vậy… có phải nếu nhìn không có vật chất, thì linh hồn",
     "Không nên nói như vậy… nhìn không có vật chất. Có phải linh hồn", 1, "minor"),
    ("1-puggalakatha.md", ["5-228"], "str",
     "Không nên nói như vậy… có phải nếu nhìn sau khi ra bên ngoài, thì linh hồn",
     "Không nên nói như vậy… nhìn sau khi ra bên ngoài. Có phải linh hồn", 1, "minor"),
    ("1-puggalakatha.md", ["5-232"], "str",
     "chỉ có khổ đau khi sinh khởi thì sinh khởi", "chỉ có khổ đau khi đang sinh khởi thì sinh khởi", 1,
     "minor"),
    ("1-puggalakatha.md", ["5-234"], "str",
     "trống rỗng tự ngã", "trống rỗng, không có tự ngã", 6, "minor"),
    ("1-puggalakatha.md", ["5-235"], "str",
     "hoàn toàn là một giáo pháp của kẻ ngu si trọn vẹn", "hoàn toàn là lối nghĩ trọn vẹn của kẻ ngu si", 2,
     "minor"),
    # ---- 2-parihanikatha.md
    ("2-parihanikatha.md", CH2_RANGE, "re",
     TOK + ", " + SUBJ + " không sa sút khỏi", "\\1, thì \\2 không sa sút khỏi", 50, "minor"),
    ("2-parihanikatha.md", CH2_RANGE, "re",
     TOK + ", " + SUBJ + " sa sút khỏi", "\\1 mà \\2 vẫn sa sút khỏi", 93, "minor"),
    ("2-parihanikatha.md", ["5-265"], "str",
     "cạm bẫy của dòng lũ đã được nhổ bỏ", "dòng lũ và cạm bẫy đã được nhổ bỏ", 1, "A11"),
    ("2-parihanikatha.md", ["5-268"], "str",
     "đi đến sự tích lũy", "tăng trưởng", 10, "minor"),
]

# strings that must be gone afterwards (whole file)
GONE = {
    "1-puggalakatha.md": ["linh hồn cũng chính là thân thể", "sự tạo tác", "tai thuộc cõi trời",
                          "người ấy không phải là người sao", "đặc tính do điều kiện tạo thành của",
                          "có phải nếu nhìn", "khi sinh khởi thì", "trống rỗng tự ngã", "giáo pháp của kẻ",
                          "đức Thế Tôn"],
    "2-parihanikatha.md": ["cạm bẫy của dòng lũ", "đi đến sự tích lũy"],
    "preamble.md": [],
}


def split(text):
    segs = text.split("\n\n")
    ids = []
    for s in segs:
        m = ID.search(s.rstrip("\n").splitlines()[-1]) if s.strip() else None
        ids.append(m.group(1) if m else None)
    return segs, ids


def main():
    BACK.mkdir(exist_ok=True)
    for f in FILES:
        if not (BACK / f).exists():
            shutil.copyfile(CH / f, BACK / f)
    log = [("file", "block", "old", "new", "decision", "count")]
    bad = []
    for f in FILES:
        src = (BACK / f).read_bytes().decode("utf-8")
        segs, ids = split(src)
        for (rf, blocks, kind, old, new, exp, dec) in RULES:
            if rf != f:
                continue
            total = 0
            for i, sid in enumerate(ids):
                if sid not in blocks:
                    continue
                s = segs[i]
                if kind == "str":
                    n = s.count(old)
                    s2 = s.replace(old, new)
                    if n:
                        log.append((f, "^" + sid, old, new, dec, str(n)))
                else:
                    hits = list(re.finditer(old, s))
                    n = len(hits)
                    for h in hits:
                        log.append((f, "^" + sid, h.group(0), h.expand(new), dec, "1"))
                    s2 = re.sub(old, new, s)
                segs[i] = s2
                total += n
            if total != exp:
                bad.append(f"{f}: rule {old[:50]!r} count {total}, expected {exp}")
        out = "\n\n".join(segs)
        for g in GONE[f]:
            if g in out:
                bad.append(f"{f}: still contains {g!r} x{out.count(g)}")
        if DRY:
            continue
        with open(CH / f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(out)
    if not DRY:
        with open(LOG, "w", encoding="utf-8", newline="\n") as fh:
            for row in log:
                fh.write("\t".join(row) + "\n")
    for b in bad:
        print("PROBLEM", b)
    print("rows", len(log) - 1, "problems", len(bad), "(dry)" if DRY else "(written)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
