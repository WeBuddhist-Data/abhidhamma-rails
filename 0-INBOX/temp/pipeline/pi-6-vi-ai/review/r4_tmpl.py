"""Template-level consistency: abstract term names and compare frames."""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
show = int(sys.argv[1]) if len(sys.argv) > 1 else 10
PT = [r"kāmarāgānusay\w*", r"paṭighānusay\w*", r"mānānusay\w*", r"diṭṭhānusay\w*", r"vicikicchānusay\w*",
      r"bhavarāgānusay\w*", r"avijjānusay\w*",
      r"\b(?:a)?kusal(?:ā|a|aṃ|ānaṃ|e)\b", r"\babyākat(?:ā|a|aṃ)\b",
      r"\b\w+indriy\w*"]
VT = ["khuynh hướng tiềm ẩn tham đắm dục lạc", "khuynh hướng tiềm ẩn ác cảm", "khuynh hướng tiềm ẩn kiêu mạn",
      "khuynh hướng tiềm ẩn quan điểm", "khuynh hướng tiềm ẩn hoài nghi", "khuynh hướng tiềm ẩn tham đắm hiện hữu",
      "khuynh hướng tiềm ẩn vô minh",
      "không xác định về mặt đạo đức", "bất thiện", "thiện",
      r"năng lực của người đã hiểu biết trọn vẹn", r"năng lực biết được điều chưa từng biết",
      r"năng lực (?:mắt|tai|mũi|lưỡi|thân|ý|nữ tính|nam tính|sống|dễ chịu|khó chịu|niềm vui|nỗi buồn|bình thản|niềm tin|tinh tấn|tỉnh thức|định tâm|trí tuệ|hiểu biết trọn vẹn)"]


def np_(s):
    s = re.sub(r"\s*\^[0-9a-z-]+\s*$", "", s.strip())
    for pt in PT:
        s = re.sub(pt, "§", s)
    s = re.sub(r"§ ca\b", "§", s)
    return s.lower()


def nv(s):
    s = re.sub(r"\s*\^[0-9a-z-]+\s*$", "", s.strip())
    for vt in VT:
        s = re.sub(vt, "§", s)
    return s


groups = collections.defaultdict(collections.Counter)
where = {}
for f, n, sid, p, v in pairs():
    if p.startswith("#"):
        continue
    k = np_(p)
    vv = nv(v)
    groups[k][vv] += 1
    where.setdefault((k, vv), f"{f}:{n} {sid}")
bad = [(k, c) for k, c in groups.items() if len(c) > 1]
print("groups", len(groups), "inconsistent", len(bad))
for k, c in sorted(bad, key=lambda x: -sum(x[1].values()))[:show]:
    print("P:", k[:250])
    for vv, x in c.most_common(4):
        print(f"   {x}x {where[(k, vv)]} V: {vv[:300]}")
