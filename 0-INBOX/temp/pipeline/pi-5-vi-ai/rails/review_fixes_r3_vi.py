"""Review fixes, pi-5 Vietnamese rails, part r3 (ch11-15), 2026-11-22.

usage:
  python -I -X utf8 -B review_fixes_r3_vi.py backup
  python -I -X utf8 -B review_fixes_r3_vi.py show <block-id> [...]
  python -I -X utf8 -B review_fixes_r3_vi.py grep <regex> [pi|vi]
  python -I -X utf8 -B review_fixes_r3_vi.py apply [--dry]
"""
import pathlib
import re
import shutil
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
VDIR = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
PDIR = ROOT / "AI_translation/pali/pi-5_split_chapters"
HERE = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails"
BAK = HERE / "backup-pre-review"
LOG = HERE / "review-fixes-log-r3.tsv"
FILES = ["11-tatiyavaggo.md", "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md",
         "15-sattamavaggo.md"]

F11, F12, F13, F14, F15 = FILES
NANU_OLD = ("Chẳng phải đó là sự hiện hữu có tri giác, cõi tái sinh có tri giác… sự có được sự tồn tại cá nhân có tri giác sao?")
NANU_NEW = ("Chẳng phải đó là sự hiện hữu có tri giác, cõi tái sinh có tri giác, nơi cư trú của chúng sinh có tri giác, "
            "vòng luân hồi có tri giác, cách sinh có tri giác, sự có được sự tồn tại cá nhân có tri giác sao?")
VUA_OLD = ("vừa đã tham đắm vừa không tham đắm, vừa đã sân hận vừa không sân hận, vừa đã si mê vừa không si mê, "
           "vừa đã được cắt vừa không được cắt, vừa đã bị phá vỡ vừa không bị phá vỡ, vừa đã được làm vừa không được làm")
VUA_NEW = ("hoặc đã tham đắm hoặc không tham đắm, hoặc đã sân hận hoặc không sân hận, hoặc đã si mê hoặc không si mê, "
           "hoặc đã được cắt hoặc không được cắt, hoặc đã bị phá vỡ hoặc không bị phá vỡ, hoặc đã được làm hoặc không được làm")
RX_NEU_THI = r"RX:Có phải nếu ([^?]*?), thì ([^?]*?) không\?"
RX_VI_NEN = r"Có phải vì \1, nên \2 không?"

RULES = [  # (file, block_id or None, old, new, count, decision)
    # ---- ch11
    (F11, "5-356", "[ở đây, đây là sự phủ nhận nhắm vào phương diện chung",
     "[sự phủ nhận ở đây nhắm vào phương diện chung", 1, "minor (A20)"),
    (F11, "5-366", ", một phần không có giới hạnh được các bậc thánh yêu quý không?",
     ", một phần không được trang bị giới hạnh được các bậc thánh yêu quý không?", 1, "minor (A20)"),
    (F11, "5-367", VUA_OLD, VUA_NEW, 2, "A15"),
    (F11, "5-367", "đang bị phiền não làm ô nhiễm", "đang bị phiền não làm vẩn đục", 1, "A16"),
    (F11, "5-369", "bằng đường sai", "bằng cái không phải là con đường", 3, "minor (A20)"),
    (F11, "5-372", "đứng vững ở phía người phàm phu", "đứng ở phía người phàm phu", 2, "minor (A20)"),
    (F11, None, "tai thuộc cõi trời", "thiên nhĩ", 19, "B6"),
    (F11, "5-382", "nhưng bằng tri giác ấy mà không làm việc của tri giác",
     "nhưng không dùng tri giác ấy để làm việc của tri giác", 2, "minor (A20)"),
    (F11, "5-384", NANU_OLD, NANU_NEW, 1, "A1"),
    (F11, "5-386", "Đối với người thứ tám, không có năm năng lực, mắt.",
     "Đối với người thứ tám, không có năm năng lực; mắt.", 1, "B16"),
    (F11, "5-386", "tri giác giữa các chúng sinh Vô Tưởng, cũng vậy, đỉnh cao của sự hiện hữu.",
     "tri giác giữa các chúng sinh Vô Tưởng, cũng vậy với đỉnh cao của sự hiện hữu.", 1,
     "B16 (no comma inside an item; evameva = «cũng vậy với …» as ch12 ^5-417, ch14 ^5-470)"),
    # ---- ch12
    (F12, "5-387", "ngựa đực và ngựa cái", "ngựa và ngựa cái", 1, "A2"),
    (F12, "5-392", "cái đối tượng của ô nhiễm ấy", "cái là đối tượng của ô nhiễm ấy", 8, "minor (A20)"),
    (F12, "5-396", RX_NEU_THI, RX_VI_NEN, 6, "minor (A20)"),
    (F12, "5-398", "nhưng bằng sự giác ngộ ấy mà không làm việc của sự giác ngộ",
     "nhưng không dùng sự giác ngộ ấy để làm việc của sự giác ngộ", 4, "minor (A20)"),
    (F12, "5-398", "nhưng bằng sự giác ngộ ấy mà không hiểu biết trọn vẹn khổ đau",
     "nhưng không dùng sự giác ngộ ấy để hiểu biết trọn vẹn khổ đau", 4, "minor (A20)"),
    (F12, "5-399", RX_NEU_THI, RX_VI_NEN, 1, "minor (A20)"),
    (F12, "5-402", "báu vật ngựa đực", "báu vật ngựa", 1, "A2"),
    (F12, "5-405", "ấy cần dứt bỏ’", "ấy cần được dứt bỏ’", 1, "minor (A20)"),
    (F12, "5-412", RX_NEU_THI, RX_VI_NEN, 6, "minor (A20)"),
    (F12, "5-417", "người được trang bị các tướng, Bồ-tát đã bước vào sự cố định, đã sống đời sống tu hành trong sạch, "
     "người đang thực hành", "người được trang bị các tướng; Bồ-tát đã bước vào sự cố định, đã sống đời sống tu hành "
     "trong sạch; người đang thực hành", 1, "B16"),
    # ---- ch13
    (F13, None, "bằng thân và an trú", "bằng thân rồi an trú", 7, "A17"),
    (F13, None, "hiểu biết về điều sai lệch", "hiểu biết sai lệch", 16, "A14"),
    # ---- ch14
    (F14, "5-450", "“này các tỳ-khưu, sự sinh làm điều kiện", "“Này các tỳ-khưu, sự sinh làm điều kiện", 1,
     "minor (A20)"),
    (F14, "5-454", "“này các tỳ-khưu, có bốn điều này", "“Này các tỳ-khưu, có bốn điều này", 1, "minor (A20)"),
    # ---- ch15
    (F15, None, "hiện tượng nào là yếu tố đồng hành với tâm", "hiện tượng nào đồng hành với tâm", 4, "minor (A20)"),
    (F15, None, "hiện tượng là yếu tố đồng hành với tâm", "hiện tượng đồng hành với tâm", 13, "minor (A20)"),
    (F15, "5-486", "định tâm không thể đo lường của tâm", "định tâm không thể đo lường", 2, "minor (A20)"),
    (F15, "5-491", "biết ơn, ghi nhớ ơn,\n", "biết ơn, ghi nhớ ơn.\n", 1, "minor (A20)"),
    (F15, "5-501", "Có phải đối với từng người như vậy, không có sự đi đến tận cùng",
     "Có phải như vậy, với quả ấy rồi quả của quả ấy nối tiếp nhau, không có sự đi đến tận cùng", 1, "A18"),
]


def blocks(text):
    """list of (block_id, [lines]) by blank-line paragraphs; id = trailing ^id of the last line."""
    out = []
    for para in text.split("\n\n"):
        ls = [ln for ln in para.split("\n") if ln.strip()]
        if not ls:
            continue
        m = re.search(r"\^(\S+)\s*$", ls[-1])
        out.append((m.group(1) if m else None, ls))
    return out


def backup():
    BAK.mkdir(exist_ok=True)
    for f in FILES:
        dst = BAK / f
        if dst.exists():
            print("exists, kept:", dst.name)
            continue
        shutil.copy2(VDIR / f, dst)
        print("backed up:", dst.name)


def show(ids):
    for f in FILES:
        pb = dict(blocks((PDIR / f).read_text(encoding="utf-8")))
        vb = dict(blocks((VDIR / f).read_text(encoding="utf-8")))
        for bid in ids:
            if bid in pb:
                print(f"=== {f} ^{bid}")
                for i, (p, v) in enumerate(zip(pb[bid], vb.get(bid, []))):
                    print(f"[{i}] PI: {p}")
                    print(f"[{i}] VI: {v}")


def grep(pat, side):
    rx = re.compile(pat)
    for f in FILES:
        d = PDIR if side == "pi" else VDIR
        for bid, ls in blocks((d / f).read_text(encoding="utf-8")):
            for i, ln in enumerate(ls):
                for m in rx.finditer(ln):
                    s = max(0, m.start() - 100)
                    print(f"{f} ^{bid} [{i}]: ...{ln[s:m.end() + 100]}...")


def esc(s):
    return s.replace("\n", "\\n")


def _sub(seg, old, new):
    """plain replace, or regex when old starts with 'RX:'; returns (new_seg, n)."""
    if old.startswith("RX:"):
        return re.subn(old[3:], new, seg)
    return seg.replace(old, new), seg.count(old)


def apply(dry):
    log = ["file\tblock\told\tnew\tdecision"]
    errors = []
    for f in FILES:
        text = (BAK / f).read_text(encoding="utf-8")
        assert "\r" not in text
        before = {k: text.count(k) for k in ("—", ":-", "….", "được được", "là là", "chánh niệm", "  ")}
        for (rf, bid, old, new, cnt, dec) in RULES:
            if rf != f:
                continue
            if bid is None:
                for b, ls in blocks(text):
                    _, k = _sub("\n".join(ls), old, new)
                    for _ in range(k):
                        log.append(f"{f}\t^{b}\t{esc(old)}\t{esc(new)}\t{dec}")
                text, n = _sub(text, old, new)
                if n != cnt:
                    errors.append((f, None, old, n, cnt))
            else:
                paras = text.split("\n\n")
                hit = [i for i, p in enumerate(paras) if re.search(r"\^" + re.escape(bid) + r"\s*$", p.rstrip("\n"))]
                assert len(hit) == 1, (f, bid, hit)
                paras[hit[0]], n = _sub(paras[hit[0]], old, new)
                if n != cnt:
                    errors.append((f, bid, old, n, cnt))
                text = "\n\n".join(paras)
                for _ in range(n):
                    log.append(f"{f}\t^{bid}\t{esc(old)}\t{esc(new)}\t{dec}")
        if errors:
            for e in errors:
                print("COUNT MISMATCH", e)
            if not dry:
                raise SystemExit(1)
            errors = []
        text = unicodedata.normalize("NFC", text)
        for k, v in before.items():
            assert text.count(k) <= v, (f, k, v, text.count(k))
        if not dry:
            (VDIR / f).write_text(text, encoding="utf-8", newline="\n")
        print(f, "done" if not dry else "dry ok")
    if not dry:
        LOG.write_text("\n".join(log) + "\n", encoding="utf-8", newline="\n")
    print("replacements logged:", len(log) - 1)


def main():
    cmd = sys.argv[1]
    if cmd == "backup":
        backup()
    elif cmd == "show":
        show(sys.argv[2:])
    elif cmd == "grep":
        grep(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "vi")
    elif cmd == "apply":
        apply("--dry" in sys.argv)
    elif cmd == "check":
        check()


def check():
    bad = ["—", ":-", "….", "được được", "là là", "chánh niệm", "se" + "ed", "  ", "\r"]
    for f in FILES:
        t = (VDIR / f).read_bytes().decode("utf-8")
        for b in bad:
            if b in t:
                print("FORBIDDEN", f, repr(b), t.count(b))
        assert t == unicodedata.normalize("NFC", t), f
        for (rf, bid, old, new, cnt, dec) in RULES:
            if rf == f and not old.startswith("RX:") and old in t and old not in new:
                print("RESIDUAL", f, repr(old), t.count(old))
        for extra in ("ngựa đực", "tai thuộc cõi trời", "làm nghiệp", "Có phải nếu", "Sakka", "đức Thế Tôn",
                      "người đang nhập thành tựu thiền"):
            if extra in t:
                print("note:", f, repr(extra), t.count(extra))
    print("check done")


if __name__ == "__main__":
    main()
