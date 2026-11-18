"""r3 mechanical checks for chapter 3 (rupakandam) Pali vs our Vietnamese. Prints only; writes nothing.
Usage: python -I -X utf8 r3_check.py [preds|items|typo] <chfile.md> [...]
"""
import re, sys, os, unicodedata
from collections import defaultdict

BASE = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(BASE, r"AI_translation\pali\pi-1_split_chapters")
VDIR = os.path.join(BASE, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
IDRE = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for block in re.split(r"\n\s*\n", txt.strip()):
        lines = [l for l in block.split("\n") if l.strip()]
        m = IDRE.search(lines[-1])
        out.append((m.group(1) if m else None, lines))
    return out, txt


ITEMS = [
    ("cakkhāyatana", "lĩnh vực mắt", "A_eye"), ("sotāyatana", "lĩnh vực tai", "A_ear"),
    ("ghānāyatana", "lĩnh vực mũi", "A_nose"), ("jivhāyatana", "lĩnh vực lưỡi", "A_tongue"),
    ("kāyāyatana", "lĩnh vực thân", "A_body"), ("rūpāyatana", "lĩnh vực hình sắc", "A_vis"),
    ("saddāyatana", "lĩnh vực âm thanh", "A_snd"), ("gandhāyatana", "lĩnh vực mùi", "A_smell"),
    ("rasāyatana", "lĩnh vực vị", "A_taste"), ("phoṭṭhabbāyatana", "lĩnh vực vật xúc chạm", "A_touch"),
    ("itthindriya", "năng lực nữ tính", "I_fem"), ("purisindriya", "năng lực nam tính", "I_masc"),
    ("jīvitindriya", "năng lực sống", "I_life"), ("cakkhundriya", "năng lực mắt", "I_eye"),
    ("sotindriya", "năng lực tai", "I_ear"), ("ghānindriya", "năng lực mũi", "I_nose"),
    ("jivhindriya", "năng lực lưỡi", "I_tongue"), ("kāyindriya", "năng lực thân", "I_body"),
    ("kāyaviññatti", "sự biểu lộ bằng thân", "V_body"), ("vacīviññatti", "sự biểu lộ bằng lời nói", "V_speech"),
    ("ākāsadhātu", "yếu tố không gian", "D_space"), ("āpodhātu", "yếu tố nước", "D_water"),
    ("pathavīdhātu", "yếu tố đất", "D_earth"), ("tejodhātu", "yếu tố lửa", "D_fire"),
    ("vāyodhātu", "yếu tố gió", "D_wind"),
    ("cakkhudhātu", "yếu tố mắt", "D_eye"), ("sotadhātu", "yếu tố tai", "D_ear"), ("ghānadhātu", "yếu tố mũi", "D_nose"),
    ("jivhādhātu", "yếu tố lưỡi", "D_tongue"), ("kāyadhātu", "yếu tố thân", "D_body"),
    ("rūpadhātu", "yếu tố hình sắc", "D_vis"), ("saddadhātu", "yếu tố âm thanh", "D_snd"),
    ("gandhadhātu", "yếu tố mùi", "D_smell"), ("rasadhātu", "yếu tố vị", "D_taste"),
    ("phoṭṭhabbadhātu", "yếu tố vật xúc chạm", "D_touch"),
    ("lahutā", "sự nhẹ nhàng", "L"), ("mudutā", "sự mềm mại", "M"), ("kammaññatā", "sự dễ vận dụng", "K"),
    ("upacayo", "sự tăng trưởng", "UP"), ("santati", "sự liên tục", "SA"), ("jaratā", "sự lão hóa", "J"),
    ("aniccatā", "tính vô thường", "AN"), ("kabaḷīkāro", "thức ăn trong vai trò dưỡng chất", "F"),
]
PRE = re.compile("|".join(sorted((re.escape(p) for p, v, c in ITEMS), key=len, reverse=True)), re.I)
VRE = re.compile("|".join(sorted((re.escape(v) for p, v, c in ITEMS), key=len, reverse=True)), re.I)
P2C = {p: c for p, v, c in ITEMS}
V2C = {v.lower(): c for p, v, c in ITEMS}


def items(ch):
    P, _ = segs(os.path.join(PDIR, ch))
    V, _ = segs(os.path.join(VDIR, ch))
    for (pid, pl), (vid, vl) in zip(P, V):
        for k, (a, b) in enumerate(zip(pl, vl)):
            ps = [P2C[m.group(0).lower()] for m in PRE.finditer(a)]
            vs = [V2C[m.group(0).lower()] for m in VRE.finditer(b)]
            if ps != vs:
                print(f"{ch} ^{pid} L{k}: P={ps}\n    V={vs}")


def preds(chs):
    mp = defaultdict(lambda: defaultdict(list))
    for ch in chs:
        P, _ = segs(os.path.join(PDIR, ch))
        V, _ = segs(os.path.join(VDIR, ch))
        for (pid, pl), (vid, vl) in zip(P, V):
            pa = " ".join(pl); va = " ".join(vl)
            mq = re.search(r"Katamaṃ taṃ rūpaṃ (.*?)[?.] ", pa)
            mc = re.search(r"idaṃ taṃ rūpaṃ (.*?)\.", pa)
            vq = re.search(r"Vật chất nào (.*?)[?.] ", va)
            vc = re.search(r"vật chất này (.*?)\.", va)
            if not mq:
                continue
            q = mq.group(1)
            vqs = vq.group(1) if vq else "<NOQ>"
            vcs = vc.group(1) if vc else "<NOC>"
            mp[q][vqs].append(pid)
            if mc and vc and mc.group(1) == q and vcs != vqs:
                print(f"Q/C MISMATCH ^{pid}: VQ={vqs} | VC={vcs}")
            if mc and mc.group(1) != q:
                print(f"(Pali Q!=C ^{pid}: {q} | {mc.group(1)}) VQ={vqs} | VC={vcs}")
    for q, d in mp.items():
        for v, ids in d.items():
            print(f"{q}  =>  {v}   [{ids[0]}{'..' + ids[-1] if len(ids) > 1 else ''} n={len(ids)}]")


def typo(ch):
    P, ptxt = segs(os.path.join(PDIR, ch))
    V, vtxt = segs(os.path.join(VDIR, ch))
    if "\r" in vtxt: print("CR present")
    if "\n\n\n" in vtxt: print("double blank line")
    if unicodedata.normalize("NFC", vtxt) != vtxt: print("not NFC")
    for bad in ["—", ":-", "….", "..", " ,", " .", " ?", " :", " ;", "\"", "'", "chánh niệm", "  "]:
        n = vtxt.count(bad)
        if n: print(f"contains {bad!r}: {n}")
    if len(P) != len(V): print("SEG COUNT", len(P), len(V))
    for (pid, pl), (vid, vl) in zip(P, V):
        if pid != vid: print("ID", pid, vid)
        if len(pl) != len(vl): print("LINES", pid, len(pl), len(vl))
        for k, (a, b) in enumerate(zip(pl, vl)):
            if a.count("–") != b.count("–"): print(f"DASH ^{pid} L{k} {a.count('–')} vs {b.count('–')}")
            pe = a.count("…pe…") + a.count("…pe …") + a.count("… pe…")
            if pe != b.count("…"): print(f"ELLIPSIS ^{pid} L{k} pe={pe} vi={b.count('…')}")
            if a.count("?") != b.count("?"): print(f"QMARK ^{pid} L{k} {a.count('?')} vs {b.count('?')}")
            if a.count("[") != b.count("["): print(f"BRACKET ^{pid} L{k}")
            # latin words outside brackets
            bb = re.sub(r"\[[^\]]*\]", "", b)
            bb = re.sub(r"\^[0-9A-Za-z-]+", "", bb)
            lat = re.findall(r"\b[a-zA-Zāīūṃṅñṭḍṇḷ]*[āīūṃṅñṭḍṇḷ][a-zA-Zāīūṃṅñṭḍṇḷ]*\b", bb)
            if lat: print(f"LATIN? ^{pid} L{k}: {lat[:5]}")
            # sentence end
            bt = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", b).rstrip()
            if not bt.startswith("#") and not re.search(r"[.?–:]$", bt):
                print(f"END ^{pid} L{k}: ...{bt[-20:]}")
            # negation heuristic
            pn = len(re.findall(r"\b(na|no|neva|nā\w+)\b|\bnārammaṇa", a))
            vn = len(re.findall(r"\bkhông\b", b))
            print_neg = "--neg" in sys.argv
            if print_neg:
                print(f"NEG ^{pid} L{k} P{pn} V{vn}")


if __name__ == "__main__":
    mode = sys.argv[1]
    files = [x for x in sys.argv[2:] if not x.startswith("--")]
    if mode == "items":
        for f in files: items(f)
    elif mode == "preds":
        preds(files)
    elif mode == "typo":
        for f in files:
            print("##", f); typo(f)
