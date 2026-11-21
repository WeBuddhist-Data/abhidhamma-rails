"""r3 review helper: bilingual mechanical checks for pi-3 chapters 8-15 (Vietnamese plain rails).
Read-only. Prints findings to the console only. Never writes any file.
Usage: python -I -X utf8 r3_check.py
"""
import re, sys, unicodedata
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-3_split_chapters"
VDIR = ROOT / r"AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters"
TS = ROOT / r"1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md"
CH = ["8-sattamanayo.md", "9-atthamanayo.md", "10-navamanayo.md", "11-dasamanayo.md",
      "12-ekadasamanayo.md", "13-dvadasamanayo.md", "14-terasamanayo.md", "15-cuddasamanayo.md"]

IDRE = re.compile(r"\^(3-[0-9-]+)\s*$")


def segments(path):
    txt = path.read_text(encoding="utf-8")
    raw = txt
    segs = []
    for block in re.split(r"\n\s*\n", txt.strip("\n")):
        lines = [l for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        m = IDRE.search(lines[-1])
        sid = m.group(1) if m else None
        segs.append((sid, lines))
    return segs, raw


PNUM = {"ekena": 1, "ekāya": 1, "eken": 1, "dvīhi": 2, "dvīh": 2, "tīhi": 3, "catūhi": 4, "pañcahi": 5,
        "chahi": 6, "sattahi": 7, "aṭṭhahi": 8, "dasahi": 10, "dasah": 10, "ekādasahi": 11, "ekādasah": 11,
        "dvādasahi": 12, "dvādasah": 12, "terasahi": 13, "pannarasahi": 15, "soḷasahi": 16,
        "sattarasahi": 17, "aṭṭhārasahi": 18}
PCAT = {"khandhehi": "K", "khandhena": "K", "dhātūhi": "D", "dhātuyā": "D", "āyatanehi": "A", "āyatanena": "A"}

PTOK = re.compile(
    r"\bna kehici khandhehi\b|\bna kehici āyatanehi\b|\bna kāhici dhātūhi\b|\bna kehici dhātūhi\b|"
    r"\bkehici\b|\bNatthi\b|asaṅkhataṃ khandhato ṭhapetvā|"
    r"\b(ekena|ekāya|dvīhi|tīhi|catūhi|pañcahi|chahi|sattahi|aṭṭhahi|dasahi|ekādasahi|dvādasahi|terasahi|pannarasahi|soḷasahi|sattarasahi|aṭṭhārasahi) (khandhehi|khandhena|dhātūhi|dhātuyā|āyatanehi)\b|"
    r"\b(eken|dvīh|dasah|ekādasah|dvādasah)āyatane(?:na|hi)\b|"
    r"\b(asaṅgahitā|saṅgahitā|sampayuttā(?:ti)?|vippayuttā)\b", re.I)

VN = {"một": 1, "hai": 2, "ba": 3, "bốn": 4, "năm": 5, "sáu": 6, "bảy": 7, "tám": 8, "mười": 10,
      "mười một": 11, "mười hai": 12, "mười ba": 13, "mười bốn": 14, "mười lăm": 15, "mười sáu": 16,
      "mười bảy": 17, "mười tám": 18}
VCAT = {"khối": "K", "lĩnh vực nhận biết": "A", "yếu tố": "D"}
VTOK = re.compile(
    r"[Kk]hông có khối nào|không có lĩnh vực nhận biết nào|không có yếu tố nào|một số hiện tượng thuộc|"
    r"Không có\.|ngoại trừ điều không do điều kiện tạo thành|"
    r"\b(mười một|mười hai|mười ba|mười bốn|mười lăm|mười sáu|mười bảy|mười tám|mười|một|hai|ba|bốn|năm|sáu|bảy|tám) (khối|lĩnh vực nhận biết|yếu tố)\b|"
    r"([Kk]hông được gộp vào|[Đđ]ược gộp vào|[Kk]hông gắn liền|[Gg]ắn liền)")
VFILL = re.compile(r"mà (những hiện tượng ấy|chúng) (không gắn liền với|không được gộp vào),?")

TSTOK = re.compile(r"(\d+) (uẩn|u ẩn|xứ|giới)|phần nào|Không có")
TSCAT = {"uẩn": "K", "u ẩn": "K", "xứ": "A", "giới": "D"}


def p_tokens(s):
    out = []
    for m in PTOK.finditer(s):
        t = m.group(0)
        tl = t.lower()
        if tl.startswith("na kehici khandhehi"): out.append("0K")
        elif tl.startswith("na kehici āyatanehi"): out.append("0A")
        elif tl.startswith("na kāhici") or tl.startswith("na kehici dhātūhi"): out.append("0D")
        elif t == "kehici": out.append("k")
        elif t == "Natthi": out.append("NONE")
        elif t.startswith("asaṅkhataṃ"): out.append("EX")
        elif m.group(1): out.append(f"{PNUM[m.group(1).lower()]}{PCAT[m.group(2)]}")
        elif m.group(3): out.append(f"{PNUM[m.group(3).lower()]}A")
        elif m.group(4):
            v = m.group(4).lower()
            out.append({"asaṅgahitā": "vNG", "saṅgahitā": "vG", "vippayuttā": "vV"}.get(v, "vS"))
    return out


def v_tokens(s):
    s = VFILL.sub(lambda m: "" if m.group(0).endswith(",") else m.group(2), s)
    out = []
    for m in VTOK.finditer(s):
        t = m.group(0)
        tl = t.lower()
        if tl == "không có khối nào": out.append("0K")
        elif t == "không có lĩnh vực nhận biết nào": out.append("0A")
        elif t == "không có yếu tố nào": out.append("0D")
        elif t == "một số hiện tượng thuộc": out.append("k")
        elif t == "Không có.": out.append("NONE")
        elif t.startswith("ngoại trừ"): out.append("EX")
        elif m.group(1): out.append(f"{VN[m.group(1)]}{VCAT[m.group(2)]}")
        elif m.group(3):
            v = m.group(3).lower()
            out.append({"không được gộp vào": "vNG", "được gộp vào": "vG", "không gắn liền": "vV"}.get(v, "vS"))
    return out


def p_answer(s):
    cands = [m.start() for m in re.finditer(r"[Tt]e dhammā (?!katihi)", s)]
    cands += [m.start() for m in re.finditer(r"\bNatthi\b", s)]
    return s[min(cands):] if cands else ""


def v_answer(s):
    if "bao nhiêu yếu tố?" in s:
        return s[s.index("bao nhiêu yếu tố?") + len("bao nhiêu yếu tố?"):]
    if "…, " in s:
        return s[s.index("…, ") + 3:]
    if ", thì " in s:
        return s[s.index(", thì ") + 6:]
    return ""


def p_items(s):
    m = re.search(r"ye dhammā (sampayuttā|vippayuttā|khandhasaṅgahena)|ye vippayuttā", s)
    head = s[:m.start()] if m else s
    return len(re.findall(r"…pe…|…|\.\.(?!\.)", head)) + 1, (m.group(0) if m else None)


def v_items(s):
    m = re.search(r"[Nn]hững hiện tượng nào (không được gộp vào cùng với|được gộp vào cùng với|không gắn liền với|gắn liền với) ", s)
    head = s[:m.start()] if m else s
    return len(re.findall(r"…", head)) + 1, (m.group(1) if m else None)


def ts_segments():
    txt = TS.read_text(encoding="utf-8")
    out = {}
    parts = re.split(r"!\[\[[^\]]*#\^(3-[0-9-]+)\]\]", txt)
    for i in range(1, len(parts), 2):
        out[parts[i]] = parts[i + 1].strip()
    return out


def ts_tokens(s):
    out = []
    for m in TSTOK.finditer(s):
        if m.group(1): out.append(f"{m.group(1)}{TSCAT[m.group(2)]}")
        elif m.group(0) == "phần nào": out.append("k")
        else: out.append("NONE")
    return out


def main():
    ts = ts_segments()
    nseg = 0
    for ch in CH:
        ps, praw = segments(PDIR / ch)
        vs, vraw = segments(VDIR / ch)
        print(f"=== {ch}: {len(ps)} Pāli segs, {len(vs)} VI segs")
        if "\r" in vraw: print("  CR present")
        if unicodedata.normalize("NFC", vraw) != vraw: print("  not NFC")
        if re.search(r"\n\s*\n\s*\n", vraw): print("  double blank line")
        if len(ps) != len(vs):
            print("  SEGMENT COUNT MISMATCH"); continue
        for (pid, pl), (vid, vl) in zip(ps, vs):
            nseg += 1
            if pid != vid: print(f"  ID mismatch {pid} vs {vid}")
            if len(pl) != len(vl): print(f"  {pid}: line count {len(pl)} vs {len(vl)}")
            for i, (a, b) in enumerate(zip(pl, vl)):
                if a.count("–") != b.count("–") or a.count("—") != b.count("—"):
                    print(f"  {pid} L{i+1}: dash mismatch")
                for bad, lab in [("….", "'….'"), ('"', "ascii dquote"), (" ,", "space-comma"), (" .", "space-dot"),
                                 (" ;", "space-semicolon"), (" ?", "space-q"), ("  ", "double space"), ("..", "'..'")]:
                    hay = b.replace("…", "") if bad == ".." else b
                    if bad in hay:
                        print(f"  {pid} L{i+1}: {lab}")
                # Latin/Pāli diacritics outside [] brackets
                outside = re.sub(r"\[[^\]]*\]", "", b)
                pw = re.findall(r"\w*[āīūṃṅñṭḍṇḷ]\w*", outside)
                if pw: print(f"  {pid} L{i+1}: Pāli-script words outside brackets: {pw}")
                body = IDRE.sub("", b).rstrip()
                if not b.startswith("#") and body and body[-1] not in ".?;:":
                    print(f"  {pid} L{i+1}: line ends with {body[-1]!r}")
            if pl[0].startswith("#"):
                continue
            P = pl[0]; V = vl[0]
            pa, va = p_tokens(p_answer(P)), v_tokens(v_answer(V))
            def comp(seq):
                return ([x for x in seq if re.match(r"^\d", x)], [x for x in seq if x.startswith("v")],
                        seq.count("k"), seq.count("EX"), seq.count("NONE"))
            if comp(pa) != comp(va):
                print(f"  {pid}: ANSWER MISMATCH\n     P={pa}\n     V={va}")
            pi_, pp = p_items(P); vi_, vp = v_items(V)
            if pi_ != vi_:
                print(f"  {pid}: item count P={pi_} V={vi_}")
            if "-v" in sys.argv:
                print(f"  {pid}: items {pi_}/{vi_} main {pp!r}/{vp!r} ans {comp(pa)}")
            # frame predicates
            pmain = "S" if pp and "sampayuttā" in pp else "V" if pp and "vippayuttā" in pp else "INCL"
            vmain = {"gắn liền với": "S", "không gắn liền với": "V"}.get(vp, "INCL")
            if pmain != vmain:
                print(f"  {pid}: main predicate P={pp} V={vp}")
            if pmain == "INCL":
                pneg = "asaṅgahitā" in P.split(",")[0] or "khandhasaṅgahena asaṅgahitā" in P
                vneg = vp == "không được gộp vào cùng với"
                if pneg != vneg: print(f"  {pid}: inclusion polarity P neg={pneg} V={vp}")
                need = "hay theo cách gộp vào yếu tố" if pneg else "và theo cách gộp vào yếu tố"
                if need not in V: print(f"  {pid}: inclusion-type phrase missing ({need})")
            m2 = re.search(r"\btehi dhammehi (?:\[[^\]]*\] )?ye dhammā (sampayuttā|vippayuttā)", P)
            n2 = re.search(r"những hiện tượng nào (không gắn liền|gắn liền) với các hiện tượng đó", V)
            if bool(m2) != bool(n2):
                print(f"  {pid}: second relative clause presence P={bool(m2)} V={bool(n2)}")
            elif m2:
                if (m2.group(1) == "vippayuttā") != (n2.group(1) == "không gắn liền"):
                    print(f"  {pid}: second relative polarity P={m2.group(1)} V={n2.group(1)}")
            # question verb
            mq = re.search(r"katihi dhātūhi (saṅgahitā|sampayuttā(?:ti)?|vippayuttā)", P)
            nq = re.search(r"(không được gộp vào|được gộp vào|không gắn liền với|gắn liền với) bao nhiêu khối", V)
            if bool(mq) != bool(nq):
                print(f"  {pid}: question presence P={bool(mq)} V={bool(nq)}")
            elif mq:
                ok = {"saṅgahitā": "được gộp vào", "vippayuttā": "không gắn liền với"}.get(mq.group(1), "gắn liền với")
                if nq.group(1) != ok: print(f"  {pid}: question verb P={mq.group(1)} V={nq.group(1)}")
            # Tịnh Sự numbers
            t = ts.get(pid)
            if t is None:
                print(f"  {pid}: no TS segment"); continue
            tn = [x for x in ts_tokens(t) if x != "k"]
            pn = [x for x in pa if re.match(r"^\d", x)]
            tn2 = [x for x in tn if x != "NONE"]
            pn = [x for x in pn if x not in ("0K", "0A", "0D")]
            tn2 = [x for x in tn2 if not x.startswith("0")]
            if pn != tn2:
                print(f"  {pid}: TS numbers differ\n     P={pn}\n     TS={tn2}")
            if pa.count("k") != ts_tokens(t).count("k"):
                print(f"  {pid}: TS kehici count P={pa.count('k')} TS={ts_tokens(t).count('k')}")
    print("segments checked:", nseg)


if __name__ == "__main__":
    main()
