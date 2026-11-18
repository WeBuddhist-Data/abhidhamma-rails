"""For each review-fix rule, list the rails builder scripts (and line + first assignment name) that contain the old
wording (or a distinctive fragment of it), so the builders can be updated by hand later.

usage: python -I -X utf8 review_fixes_find_builders.py
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PROBES = [
    ("r1#1", "gốc rễ cần dứt bỏ"),
    ("r1#2", "làm theo quan điểm của mình"),
    ("r1#3", "các bậc thánh mô tả"),
    ("r1#4", "Vật chất."),
    ("r1#4", "đó được gọi là vật chất"),
    ("r2#1", "Quả của nghiệp không xác định về mặt đạo đức"),
    ("r2#3", "Là quả của chính"),
    ("r2#4", "của người đã hiểu biết trọn vẹn là"),
    ("r2#5", "thô lỗ"),
    ("r3#1", "có thể được sáu loại thức nhận biết"),
    ("r3#2", "có loại khi tiếp xúc thì dễ chịu"),
    ("r3#3", "Điều mà là"),
    ("r3#4", "nghiệp đã được tạo:"),
    ("r3#5", "vầng gương"),
    ("r3#5", "gương"),
    ("r3#6", "dáng vẻ"),
    ("r4#1", "phương pháp chia bốn và"),
    ("r4#1", "theo phương pháp chia bốn"),
    ("r4#2", "một loại thức nào đó"),
    ("r4#3", "gắn liền với chúng"),
    ("r4#5", "ở nơi bản thân, riêng từng người"),
    ("r4#6", "người ấy nói lời"),
    ("r4#7", "cõi hình sắc và thuộc cõi không hình sắc"),
    ("r4#8", "đối với"),
    ("r4#9", "Ở nơi"),
    ("r4#10", "tâm làm gốc rễ"),
]
files = sorted(glob.glob(os.path.join(HERE, "build_rails_*.py")))
ASSIGN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=")
for rid, frag in PROBES:
    hits = []
    for f in files:
        lines = open(f, encoding="utf-8").read().splitlines()
        for i, line in enumerate(lines):
            if frag in line:
                name = "?"
                for j in range(i, max(-1, i - 40), -1):
                    m = ASSIGN.match(lines[j])
                    if m:
                        name = m.group(1)
                        break
                    m2 = re.match(r"^\s*def (\w+)", lines[j])
                    if m2:
                        name = "def " + m2.group(1)
                        break
                hits.append(f"{os.path.basename(f)}:{i + 1} [{name}]")
    print(f"{rid} «{frag}»: {len(hits)} hits")
    for h in hits[:12]:
        print("   ", h)
    if len(hits) > 12:
        print("    …", len(hits) - 12, "more")
