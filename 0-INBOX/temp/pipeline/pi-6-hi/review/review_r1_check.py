"""r1 review: automated per-line checks (polarity, tense, items, beings, typography).
usage: python -I -B -X utf8 review_r1_check.py <stem> [<stem> ...]"""
import sys, os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PI = os.path.join(ROOT, "pali", "pi-6_split_chapters")
HI = os.path.join(ROOT, "hindi", "pi-6-hindi-plain-rails_split_chapters")
IDRE = re.compile(r"\s*\^([\w-]+)\s*$")


def load_raw(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def nonempty(txt):
    return [l for l in txt.split("\n") if l.strip()]


# ---------- polarity ----------
def pali_neg(line):
    l = line.lower()
    n = 0
    n += len(re.findall(r"\bna\b", l))
    n += len(re.findall(r"\bno\b", l))
    n += len(re.findall(r"\bnuppajj", l))
    n += len(re.findall(r"\bnatthi\b", l))
    # flip rule: "no ca ... (na|nuppajj...)" inside a clause -> both cancel
    for m in re.finditer(r"\bno ca\b([^.,;?]*)", l):
        seg = m.group(1)
        if re.search(r"\bna\b|\bnuppajj", seg):
            n -= 2
    return n


def hindi_neg(line):
    return len(re.findall(r"(?<![\u0900-\u0963\u0966-\u097F])(?:न|नहीं)(?![\u0900-\u0963\u0966-\u097F])", line))


# ---------- tense ----------
def pali_tense(line):
    l = line.lower()
    past = len(re.findall(r"(?:uppajj|nirujjh|parijān)i?(?:tth[aā]|atth[aā])", l))
    fut = len(re.findall(r"(?<!आ)"+r"(?:uppajj|nirujjh|parijān|parinibbāy|paṭilabh)issa", l))
    pres = len(re.findall(r"(?:uppajj|nirujjh)at[iī]|parijān(?:āt[iī]|anti)|parinibbantānaṃ", l))
    return past, fut, pres


def hindi_tense(line):
    past = len(re.findall(r"(?<![\u0900-\u0963\u0966-\u097F])(?:था|थी|थे|थीं)(?![\u0900-\u0963\u0966-\u097F])", line))
    fut = len(re.findall(r"(?<!आ)"+r"[\u0900-\u097F]*(?:गा|गी|गे)(?![\u0900-\u0963\u0966-\u097F])", line))
    pres = len(re.findall(r"(?<![\u0900-\u0963\u0966-\u097F])(?:होता|होती|होते|समझता|समझते|पाने)(?![\u0900-\u0963\u0966-\u097F])", line))
    return past, fut, pres


# ---------- items ----------
P_ITEMS = [
    ("rupak", r"rūpakkhandh"), ("vedk", r"vedanākkhandh|vadanākkhandh"), ("sank", r"saññākkhandh"),
    ("sakk", r"saṅkhārakkhandh"), ("vink", r"viññāṇakkhandh"),
    ("cvd", r"cakkhuviññāṇadhāt"), ("svd", r"sotaviññāṇadhāt"), ("gvd", r"ghānaviññāṇadhāt"),
    ("jvd", r"jivhāviññāṇadhāt"), ("kvd", r"kāyaviññāṇadhāt"), ("mvd", r"manoviññāṇadhāt"),
    ("cd", r"(?<!viññāṇa)(?<![a-zāīūṃñṅṭḍṇḷ])cakkhudhāt"), ("sd", r"(?<![a-zāīūṃñṅṭḍṇḷ])sotadhāt"),
    ("gd", r"(?<![a-zāīūṃñṅṭḍṇḷ])ghānadhāt"), ("jd", r"(?<![a-zāīūṃñṅṭḍṇḷ])jivhādhāt"),
    ("kd", r"(?<![a-zāīūṃñṅṭḍṇḷ])kāyadhāt"), ("rd", r"(?<![a-zāīūṃñṅṭḍṇḷ])rūpadhāt"),
    ("md", r"(?<![a-zāīūṃñṅṭḍṇḷ])manodhāt"), ("dd", r"dhammadhāt"),
]
H_ITEMS = [
    ("rupak", r"भौतिक रूप (?:का|के) समूह"), ("vedk", r"अनुभूति (?:का|के) समूह"), ("sank", r"पहचान (?:का|के) समूह"),
    ("sakk", r"मानसिक रचनाओं (?:का|के) समूह"), ("vink", r"चेतना (?:का|के) समूह"),
    ("cvd", r"आँख की चेतना (?:का|के) तत्व"), ("svd", r"कान की चेतना (?:का|के) तत्व"), ("gvd", r"नाक की चेतना (?:का|के) तत्व"),
    ("jvd", r"जीभ की चेतना (?:का|के) तत्व"), ("kvd", r"शरीर की चेतना (?:का|के) तत्व"), ("mvd", r"मन की चेतना (?:का|के) तत्व"),
    ("cd", r"आँख (?:का|के) तत्व"), ("sd", r"कान (?:का|के) तत्व"), ("gd", r"नाक (?:का|के) तत्व"),
    ("jd", r"जीभ (?:का|के) तत्व"), ("kd", r"शरीर (?:का|के) तत्व"), ("rd", r"दृश्य रूप (?:का|के) तत्व"),
    ("md", r"(?<!की )मन (?:का|के) तत्व"), ("dd", r"मन के विषयों (?:का|के) तत्व"),
]


def seq(line, table):
    hits = []
    for name, rx in table:
        for m in re.finditer(rx, line):
            hits.append((m.start(), name))
    hits.sort()
    # drop nested duplicates: a हिंदी 'आँख की चेतना का तत्व' also matches nothing else since cd needs 'आँख का/के'
    return [h[1] for h in hits]


# ---------- beings ----------
P_BEINGS = [
    ("asanna", r"asaññasatt"), ("panca", r"pañcavokār"), ("catu", r"catuvokār"), ("arupa", r"\barūp"),
    ("suddha", r"suddhāvās"), ("cav", r"cavantānaṃ"), ("upa", r"upapajjantānaṃ"),
    ("parinb", r"parinibbantānaṃ"), ("parinbF", r"parinibbāyissanti"), ("pacch", r"pacchimabhavik"),
    ("itare", r"itaresaṃ"), ("sabbe", r"sabbesaṃ"),
]
H_BEINGS = [
    ("asanna", r"पहचान-रहित"), ("panca", r"पाँच समूहों"), ("catu", r"चार या पाँच|चार समूहों"), ("arupa", r"अभौतिक"),
    ("suddha", r"शुद्ध निवास"), ("cav", r"मरने वालों"), ("upa", r"जन्म लेने वालों|जन्म लेकर"),
    ("parinb", r"पूर्ण निर्वाण पाने वालों"), ("parinbF", r"पूर्ण निर्वाण पाएँगे"), ("pacch", r"अंतिम जन्म"),
    ("itare", r"बाकी"), ("sabbe", r"सभी"),
]


def count_table(line, table, lower=True):
    s = line.lower() if lower else line
    return {n: len(re.findall(rx, s)) for n, rx in table}


def main():
    total_lines = 0
    total_segments = 0
    for stem in sys.argv[1:]:
        praw = load_raw(os.path.join(PI, stem + ".md"))
        hraw = load_raw(os.path.join(HI, stem + ".md"))
        p = nonempty(praw)
        h = nonempty(hraw)
        print(f"===== {stem}: {len(p)} / {len(h)} non-empty lines")
        if "\n\n\n" in hraw:
            print("  DOUBLE BLANK LINE present")
        segs = sum(1 for l in p if IDRE.search(l))
        total_segments += segs
        total_lines += len(p)
        # current block id for each line
        ids = []
        pending = []
        for i, l in enumerate(p):
            pending.append(i)
            m = IDRE.search(l)
            if m:
                for j in pending:
                    ids.append(m.group(1))
                pending = []
        ids += ["(none)"] * len(pending)
        for i, (pl, hl) in enumerate(zip(p, h)):
            issues = []
            pm, hm = IDRE.search(pl), IDRE.search(hl)
            if (pm.group(1) if pm else None) != (hm.group(1) if hm else None):
                issues.append(f"ID {pm and pm.group(1)} vs {hm and hm.group(1)}")
            pb, hb = IDRE.sub("", pl), IDRE.sub("", hl)
            if pb.startswith("#"):
                if pb.split(" ")[0] != hb.split(" ")[0]:
                    issues.append("heading level")
                if issues:
                    print(f"  {ids[i]} L{i+1}: {'; '.join(issues)}")
                continue
            # polarity
            pn, hn = pali_neg(pb), hindi_neg(hb)
            if pn != hn:
                issues.append(f"NEG p={pn} h={hn}")
            # tense
            pt, ht = pali_tense(pb), hindi_tense(hb)
            if pt[0] != ht[0] or pt[1] != ht[1]:
                issues.append(f"TENSE past p{pt[0]}/h{ht[0]} fut p{pt[1]}/h{ht[1]}")
            # items
            ps, hs = seq(pb.lower(), P_ITEMS), seq(hb, H_ITEMS)
            if ps != hs:
                issues.append(f"ITEMS p={ps} h={hs}")
            # beings
            pc, hc = count_table(pb, P_BEINGS), count_table(hb, H_BEINGS, lower=False)
            # catuvokāra+pañcavokāra pair rendered as 'चार या पाँच' (one पाँच समूहों)
            pairs = len(re.findall(r"catuvokār\w*\s+pañcavokār", pb.lower()))
            pc["panca"] -= pairs
            # 'catuvokāraṃ pañcavokāraṃ upapajjantānaṃ' is one chunk anyway
            diffs = {k: (pc[k], hc[k]) for k in pc if pc[k] != hc[k]}
            if diffs:
                issues.append(f"BEINGS {diffs}")
            # typography
            pd, hd = pb.count("–") + pb.count("—"), hb.count("–") + hb.count("—")
            if pd != hd:
                issues.append(f"DASH p{pd} h{hd}")
            if re.search(r"[A-Za-zāīūṃñṅṭḍṇḷ]{3,}", re.sub(r"\[[^\]]*\]", "", hb)):
                issues.append("LATIN outside brackets")
            if '"' in hb or "'" in hb:
                issues.append("straight quote")
            if "  " in hb:
                issues.append("double space")
            if re.search(r"\s[।?,]", hb):
                issues.append("space before punct")
            if hb.count("?") != pb.count("?"):
                issues.append(f"QMARK p{pb.count('?')} h{hb.count('?')}")
            if hb.rstrip().endswith(".") or re.search(r"[\u0900-\u097F]\.(\s|$)", hb):
                issues.append("Latin full stop")
            if hb.count("(क)") + hb.count("(ख)") != pb.count("(Ka)") + pb.count("(Kha)"):
                issues.append("KA/KHA label count")
            if issues:
                print(f"  {ids[i]} L{i+1}: {'; '.join(issues)}")
                print(f"      P: {pb[:220]}")
                print(f"      H: {hb[:220]}")
    print(f"TOTAL non-empty lines {total_lines}, segments (block IDs) {total_segments}")


if __name__ == "__main__":
    main()
