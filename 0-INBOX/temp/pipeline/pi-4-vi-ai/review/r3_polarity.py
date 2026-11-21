# r3 helper: per-line negation counts, Pali vs our Vietnamese (console only)
import re, sys
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-4_split_chapters" + "\\"
V = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters" + "\\"
chs = sys.argv[1:]
def strip_br(s):
    return re.sub(r"\[[^\]]*\]", "", s)
pneg = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(na|no|neva|nāpi|nopi|naheva|nayidaṃ|nappajānāti|nappavaḍḍhanti|nārabhati|nānubyañjanaggāhī|nāparaṃ|nābhihaṭaṃ|naehibhaddantiko|natiṭṭhabhaddantiko)(?![\wāīūṃṅñṭḍṇḷ])")
vneg = re.compile(r"(?<!\w)(không|chưa|chẳng)(?!\w)")
for ch in chs:
    pl = [l for l in open(P + ch, encoding="utf-8").read().split("\n") if l.strip()]
    vl = [l for l in open(V + ch, encoding="utf-8").read().split("\n") if l.strip()]
    print("=====", ch, len(pl), len(vl))
    for i, (a, b) in enumerate(zip(pl, vl)):
        a2 = strip_br(a); b2 = strip_br(b)
        pn = len(pneg.findall(a2)); vn = len(vneg.findall(b2))
        ida = re.findall(r"\^[\w-]+$", a.strip()); idb = re.findall(r"\^[\w-]+$", b.strip())
        flag = "" if pn == vn else "  <-- diff"
        if ida != idb: flag += "  <-- ID MISMATCH"
        print(f"{i+1:3d} {ida[0] if ida else '':12s} pi_neg={pn:2d} vi_neg={vn:2d}{flag}")
