"""Coordinator's read-only lookups for report C."""
import pathlib, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
import hz_common as H
H.CUR["hdir"] = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
seg = {}
for part in H.PARTS:
    for sid, ps, hs in H.segments(part):
        seg[sid] = (part, ps, hs)


def clip(s, key, w=70):
    i = s.find(key)
    return s[max(0, i - w):i + len(key) + w] if i >= 0 else "(no key)"


print("-- 887"); print(seg["1-887"][2][0][:260])
for i in ("1-1124", "1-1143", "1-1222", "1-1264", "1-1271"):
    print("--", i, clip(" ".join(seg[i][2]), "“सदाचार से", 100));
print("-- P 1-1124", clip(" ".join(seg["1-1124"][1]), "sīlena suddhi", 90))
for i in ("1-1105", "1-1122", "1-1144", "1-1181"):
    print("--", i, clip(" ".join(seg[i][2]), "सारी ग़लत दृष्टि", 60))
print("-- 1297", clip(" ".join(seg["1-1297"][2]), "निश्चित", 110)); print("-- 1035", clip(" ".join(seg["1-1035"][2]), "निश्चित", 110))
for i in ("1-1106", "1-1128", "1-1123", "1-1143", "1-1144", "1-1168", "1-1181", "1-1240", "1-1241", "1-1369", "1-1371"):
    print("--", i, clip(" ".join(seg[i][2]), "इस प्रकार", 22))
for i in ("1-1091", "1-1092"):
    print("--", i, " ".join(seg[i][1])[:220]); print("  ", " ".join(seg[i][2])[:300])
print("-- 1101", " ".join(seg["1-1101"][2])[:300])
for i in ("1-934", "1-935", "1-938", "1-939"):
    print("--", i, " ".join(seg[i][2])[:120])
print("-- 1-1310", " ".join(seg["1-1310"][2])[-60:])
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi")
for b in (1, 3, 4, 5):
    for l in (ROOT / f"pi-{b}-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
        if re.match(r"(a?saṃkilesik\w*):", l):
            print(b, l)
