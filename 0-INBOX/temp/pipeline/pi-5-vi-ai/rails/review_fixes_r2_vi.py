r"""Review fixes, pi-5 Vietnamese rails, part r2 (3-brahmacariyakatha.md … 10-dutiyavaggo.md).

User decision 2026-11-22 "Approve as proposed" (review\findings-summary.md A + B; review\findings-r2.md).
Builds from rails\backup-pre-review\<ch>.md (copied once from the chapter as it was before the review fixes,
never overwritten), so it can be re-run. Every rule is scoped to the listed block-ID segments and asserts its
occurrence count. Logs to rails\review-fixes-log-r2.tsv; then runs the residue / typography checks.

usage: python -I -X utf8 -B review_fixes_r2_vi.py [--dry]
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
CH = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails"
BACK = RAILS / "backup-pre-review"
LOG = RAILS / "review-fixes-log-r2.tsv"
FILES = ["3-brahmacariyakatha.md", "4-jahatikatha.md", "5-sabbamatthitikatha.md",
         "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md", "8-satipatthanakatha.md",
         "9-hevatthikatha.md", "10-dutiyavaggo.md"]
DRY = "--dry" in sys.argv

ID = re.compile(r"\^(\S+)\s*$")
LQ, RQ = "\u201c", "\u201d"
VERSE_OLD = "Hoặc bất cứ giới hạnh và nghi thức nào có;"
VERSE_NEW = "Và cả giới hạnh và nghi thức, bất cứ điều gì còn có;"
SAMA = ["5-%d" % n for n in range(326, 334)]
SADH = ["5-312", "5-316", "5-320", "5-324"]

# (file, [block ids], kind, old, new, expected total count, decision)
RULES = [
    # ---- 3-brahmacariyakatha.md
    ("3-brahmacariyakatha.md", ["5-274"], "str",
     "một phần không có giới hạnh được các bậc thánh yêu quý",
     "một phần không được trang bị giới hạnh được các bậc thánh yêu quý", 4, "minor"),
    ("3-brahmacariyakatha.md", ["5-274"], "str",
     "một phần có giới hạnh được các bậc thánh yêu quý",
     "một phần được trang bị giới hạnh được các bậc thánh yêu quý", 2, "minor"),
    ("3-brahmacariyakatha.md", ["5-276"], "str",
     "dứt bỏ cái gì? Và dứt bỏ các phiền não cùng hiện diện với chúng.",
     "dứt bỏ cái gì? Dứt bỏ cả các phiền não cùng hiện diện với chúng.", 1, "minor"),
    ("3-brahmacariyakatha.md", ["5-278"], "str", VERSE_OLD, VERSE_NEW, 1, "minor"),
    # ---- 5-sabbamatthitikatha.md
    ("5-sabbamatthitikatha.md", ["5-288"], "str",
     "không là rồi không trở thành, không là rồi không trở thành",
     "chưa có thì không có, chưa có thì không có", 3, "minor"),
    ("5-sabbamatthitikatha.md", ["5-288"], "str",
     "là rồi trở thành, là rồi trở thành", "đã có rồi lại có, đã có rồi lại có", 6, "minor"),
    ("5-sabbamatthitikatha.md", ["5-295"], "str",
     "Có phải hiện tại tồn tại không, đúng vậy.", "Có phải hiện tại tồn tại không? Đúng vậy.", 1, "B10"),
    ("5-sabbamatthitikatha.md", ["5-296"], "str",
     "có thể mô tả được không. Bạch Thế Tôn", "có thể mô tả được không? Bạch Thế Tôn", 1, "minor"),
    ("5-sabbamatthitikatha.md", ["5-296"], "str",
     "có thể mô tả được không" + RQ + ".", "có thể mô tả được không?" + RQ, 1, "minor"),
    # ---- 6-atitakkhandhadikatha.md
    ("6-atitakkhandhadikatha.md", ["5-298"], "str",
     "thuộc quá khứ và tương lai, và những điều này không tồn tại",
     "thuộc quá khứ và tương lai, những điều ấy không tồn tại", 4, "minor"),
    ("6-atitakkhandhadikatha.md", ["5-298"], "str",
     "phạm vi của tên gọi, sự định danh…", "phạm vi của tên gọi, phạm vi của sự định danh…", 1, "minor"),
    # ---- 7-ekaccam-atthitikatha.md (uppādino «có tính chất sinh khởi»; uppajjissanti stays «sẽ sinh khởi»)
    ("7-ekaccam-atthitikatha.md", ["5-300"], "str",
     "thuộc tương lai sẽ sinh khởi thì sẽ sinh khởi",
     "thuộc tương lai có tính chất sinh khởi sẽ sinh khởi", 3, "B8"),
    ("7-ekaccam-atthitikatha.md", ["5-300"], "str",
     "thuộc tương lai sẽ không sinh khởi", "thuộc tương lai không có tính chất sinh khởi", 6, "B8"),
    ("7-ekaccam-atthitikatha.md", ["5-300"], "str",
     "thuộc tương lai sẽ sinh khởi", "thuộc tương lai có tính chất sinh khởi", 12, "B8"),
    # ---- 8-satipatthanakatha.md
    ("8-satipatthanakatha.md", ["5-303"], "str", "báu vật ngựa đực", "báu vật ngựa", 1, "A2"),
    # ---- 10-dutiyavaggo.md
    ("10-dutiyavaggo.md", ["5-308"], "str",
     "Bởi vì chúng tôi sẽ khiến vị ấy rơi vào sự phân vân.",
     "Vì họ có ý: " + LQ + "Nào, chúng ta sẽ khiến vị ấy rơi vào sự phân vân" + RQ + ".", 1, "A8/B7"),
    ("10-dutiyavaggo.md", SADH, "str",
     "thông thạo các hiện tượng của mình", "thông thạo lĩnh vực của riêng mình", 39, "A7"),
    ("10-dutiyavaggo.md", SADH, "str",
     "thông thạo các hiện tượng của người khác", "thông thạo cả các lĩnh vực khác", 39, "A7"),
    ("10-dutiyavaggo.md", ["5-317", "5-346"], "str", VERSE_OLD, VERSE_NEW, 2, "minor"),
    ("10-dutiyavaggo.md", SAMA, "str", "người đang nhập thành tựu thiền", "người đang nhập thiền", 6, "A19"),
    ("10-dutiyavaggo.md", SAMA, "re",
     r"người đang nhập(?! (?:thiền|tầng thiền|đề mục|lĩnh vực|sự chấm dứt))", "người đang nhập thiền", 41, "A19"),
    ("10-dutiyavaggo.md", ["5-333"], "str", "đứng vững ở cõi Phạm Thiên", "đứng ở cõi Phạm Thiên", 1, "minor"),
    ("10-dutiyavaggo.md", ["5-338"], "str",
     "đưa đến sự khó chịu, có quả trổ khó chịu", "đưa đến khổ đau, có quả trổ là khổ đau", 2, "minor"),
    ("10-dutiyavaggo.md", ["5-338"], "str",
     "đưa đến sự dễ chịu, có quả trổ dễ chịu", "đưa đến hạnh phúc, có quả trổ là hạnh phúc", 4, "minor"),
    ("10-dutiyavaggo.md", ["5-339"], "str", "dần dần ", "theo tuần tự ", 12, "minor"),
    ("10-dutiyavaggo.md", ["5-340"], "str",
     "một phần tư không có giới hạnh được các bậc thánh yêu quý",
     "một phần tư không được trang bị giới hạnh được các bậc thánh yêu quý", 2, "minor"),
    ("10-dutiyavaggo.md", ["5-346"], "str",
     "dốc xuống tuần tự, không đột ngột là vực thẳm;",
     "dốc xuống tuần tự, chứ không đột ngột dốc thẳng xuống như vực;", 1, "minor"),
    ("10-dutiyavaggo.md", ["5-346"], "str",
     "cách thực hành tuần tự, không đột ngột là sự thấu triệt hiểu biết trọn vẹn",
     "cách thực hành tuần tự, chứ không đột ngột có sự thấu triệt hiểu biết trọn vẹn", 1, "minor"),
    ("10-dutiyavaggo.md", ["5-352"], "str",
     "khi nói về đường sai, thì là đường sai",
     "khi nói về điều không phải con đường, thì là điều không phải con đường", 1, "minor"),
    ("10-dutiyavaggo.md", ["5-352"], "str",
     "khi nói về điều phi vật chất, thì là điều phi vật chất",
     "khi nói về điều không phải vật chất, thì là điều không phải vật chất", 1, "minor"),
]

# strings that must be gone afterwards (file -> list); regexes allowed with prefix "re:"
RESIDUE = {
    "3-brahmacariyakatha.md": ["không có giới hạnh được các bậc thánh", "một phần có giới hạnh",
                               "? Và dứt bỏ", "Hoặc bất cứ giới hạnh"],
    "5-sabbamatthitikatha.md": ["là rồi trở thành", "không, đúng vậy", "mô tả được không."],
    "6-atitakkhandhadikatha.md": ["những điều này không tồn tại", "tên gọi, sự định danh"],
    "7-ekaccam-atthitikatha.md": ["sẽ sinh khởi thì sẽ sinh khởi", "tương lai sẽ không sinh khởi",
                                  "tương lai sẽ sinh khởi"],
    "8-satipatthanakatha.md": ["đực"],
    "10-dutiyavaggo.md": ["chúng tôi", "thông thạo các hiện tượng", "Hoặc bất cứ giới hạnh",
                          "re:người đang nhập(?! (?:thiền|tầng thiền|đề mục|lĩnh vực|sự chấm dứt))",
                          "thành tựu thiền với", "thành tựu thiền thuộc", "đứng vững ở cõi Phạm Thiên",
                          "quả trổ khó chịu", "quả trổ dễ chịu", "dần dần tu tập", "dần dần tự mình",
                          "không có giới hạnh được các bậc thánh", "không đột ngột là", "đường sai, thì",
                          "điều phi vật chất"],
}
COMMON_BAD = ["—", ":-", "….", "được được", "là là", "chánh niệm", "seed", "  ", "\r",
              "ngựa đực", "làm nghiệp", "tai thuộc cõi trời", "đức Thế Tôn", "Sakka"]


def seg_ids(lines):
    """block id of the segment each line belongs to (the next id at or after it)."""
    out, pending = [None] * len(lines), []
    for i, ln in enumerate(lines):
        pending.append(i)
        m = ID.search(ln)
        if m:
            for j in pending:
                out[j] = m.group(1)
            pending = []
    return out


def main():
    BACK.mkdir(exist_ok=True)
    for f in FILES:
        if not (BACK / f).exists():
            shutil.copyfile(CH / f, BACK / f)
    texts = {f: (BACK / f).read_text(encoding="utf-8") for f in FILES}
    log = []
    bad = 0
    for f, ids, kind, old, new, exp, dec in RULES:
        lines = texts[f].split("\n")
        sids = seg_ids(lines)
        total = 0
        for i, ln in enumerate(lines):
            if sids[i] not in ids:
                continue
            if kind == "str":
                n = ln.count(old)
                if n:
                    lines[i] = ln.replace(old, new)
            else:
                lines[i], n = re.subn(old, new, ln)
            if n:
                total += n
                log.append((f, sids[i], str(n), old, new, dec))
        if total != exp:
            print(f"COUNT MISMATCH {f} {ids[0]}…: {old[:50]!r} found {total}, expected {exp}")
            bad += 1
        texts[f] = "\n".join(lines)
    if bad:
        sys.exit("aborted, nothing written")
    # residue + typography checks
    probs = []
    for f in FILES:
        t = texts[f]
        for s in RESIDUE.get(f, []):
            hit = re.search(s[3:], t) if s.startswith("re:") else (s in t)
            if hit:
                probs.append(f"{f}: residue {s!r}")
        for s in COMMON_BAD:
            if s in t:
                probs.append(f"{f}: bad string {s!r}")
    for p in probs:
        print("PROBLEM", p)
    changed = {f: sum(1 for a, b in zip((BACK / f).read_text(encoding="utf-8").split("\n"), texts[f].split("\n"))
                      if a != b) for f in FILES}
    for f in FILES:
        print(f"{f}: {changed[f]} lines changed")
    per_dec = {}
    for row in log:
        per_dec[row[5]] = per_dec.get(row[5], 0) + int(row[2])
    print("replacements per decision:", per_dec)
    if DRY:
        print("dry run: nothing written")
        return
    for f in FILES:
        with open(CH / f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(texts[f])
    with open(LOG, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("file\tblock_id\tcount\told\tnew\tdecision\n")
        for row in log:
            fh.write("\t".join(row) + "\n")
    print("written", len(log), "log rows")


if __name__ == "__main__":
    main()
