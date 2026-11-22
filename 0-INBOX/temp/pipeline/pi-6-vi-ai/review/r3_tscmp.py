"""r3: content-level comparison of our Vietnamese with Tinh Su for 6-7-36..6-7-263.
Questions are keyed by (verb kind, frame, question polarity, names); answers are reduced to
type + per-sentence (name, polarity) sets. TS block IDs are not trusted (misaligned in part),
so matching is by question key, in order. Console only, nothing is written."""
import re, sys, unicodedata
from collections import defaultdict
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
import r3_check as C

TS = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md"
IDR = re.compile(r"\s*\^(6-7-[0-9-]+)\s*$")

def norm_ts(s):
    for a, b in (("nhu ế", "nhuế"), ("ki ến", "kiến"), ("thư ợng", "thượng"), ("ngư ời", "người"),
                 ("gi ới", "giới"), ("Không Phải", "Không phải")):
        s = s.replace(a, b)
    return s

TSN = [("K", "dục ái"), ("P", "phẫn nhuế"), ("M", "ngã mạn"), ("D", "tà kiến"), ("V", "hoài nghi"),
       ("B", "hữu ái"), ("A", "vô minh")]
VN = [("K", "tham đắm dục lạc"), ("B", "tham đắm hiện hữu"), ("P", "ác cảm"), ("M", "kiêu mạn"),
      ("D", "quan điểm"), ("V", "hoài nghi"), ("A", "vô minh")]

def names(s, table):
    hits = []
    for t, w in table:
        for m in re.finditer(re.escape(w), s, flags=re.I):
            hits.append((m.start(), m.end(), t))
    hits.sort()
    return hits

VERB_TS = {"anusaya": r"(chẳng phải |chẳng |không )?ngủ theo",
           "sanusaya": r"(phi |chẳng phải |không )?tự y",
           "pajahana": r"(chẳng phải |chẳng |không )?đang trừ",
           "pariñña": r"(phi |chẳng phải |không )?đạt trừ"}
VERB_VI = {"anusaya": r"(không |vẫn |cũng )?nằm sẵn",
           "sanusaya": r"(không |vẫn |cũng )?có khuynh hướng",
           "pajahana": r"(không |vẫn |cũng )?dứt bỏ",
           "pariñña": r"(không |vẫn |cũng )?hiểu biết trọn vẹn"}
NEGW = ("không ", "chẳng phải ", "chẳng ", "phi ")

def verbs(s, rx):
    return [(m.start(), "N" if (m.group(1) or "") in NEGW else "P") for m in re.finditer(rx, s)]

def name_pol(s, kind, table, vrx):
    ns = names(s, table)
    vs = verbs(s, vrx)
    out = []
    for st, en, t in ns:
        if kind == "anusaya":
            f = [p for pos, p in vs if pos >= en]
            out.append((t, f[0] if f else "?"))
        else:
            b = [p for pos, p in vs if pos < st]
            out.append((t, b[-1] if b else "?"))
    return out

def frame(q, ts):
    q = q.lower()
    if ts:
        pl = re.search(r"người nào,? (?:cõi|chỗ|nơi) nào", q)
        if pl:
            return "PL"
        if "người nào" in q:
            return "P"
        return "L"
    if "người nào" in q and "nơi nào" in q:
        return "PL"
    if "người nào" in q:
        return "P"
    return "L"

def qkey(q, kind, ts):
    table = TSN if ts else VN
    vrx = (VERB_TS if ts else VERB_VI)[kind]
    sp = re.split(r"\bth(?:ì|ời)\b", q, maxsplit=1)
    c1 = sp[0]
    c2 = sp[1] if len(sp) > 1 else ""
    n1 = tuple(sorted(set(t for _, _, t in names(c1, table))))
    n2 = [t for _, _, t in names(c2, table)]
    v = verbs(q, vrx)
    return (kind, frame(q, ts), v[0][1] if v else "?", n1, n2[-1] if n2 else "?")

def atype(a, ts):
    a = a.strip()
    if ts:
        if a.startswith("Phải rồi"):
            return "YES"
        if a.startswith("Không phải"):
            return "NO"
        if a.startswith("Không có"):
            return "NONE"
        if a.startswith("Chỉ trừ phần đồng") or a.startswith("Chỉ đạt trừ phần đồng") or "phần đồng" in a and len(a) < 40:
            return "TE"
        return "PART"
    if a.startswith("Đúng vậy"):
        return "YES"
    if re.match(r"Không\.", a):
        return "NO"
    if a.startswith("Không có."):
        return "NONE"
    if "những gì cùng hiện diện với nó" in a and len(a) < 70:
        return "TE"
    return "PART"

def kind_from(text, ts, cur):
    if ts:
        if "tự y" in text:
            return "sanusaya"
        if "đạt trừ" in text:
            return "pariñña"
        if "đang trừ" in text:
            return "pajahana"
        if "ngủ theo" in text:
            return "anusaya"
        return cur
    if "nằm sẵn" in text:
        return "anusaya"
    if "có khuynh hướng" in text:
        return "sanusaya"
    if "hiểu biết trọn vẹn" in text:
        return "pariñña"
    if "dứt bỏ" in text:
        return "pajahana"
    return cur

def parse(stream, ts):
    """stream: list of (id, text). returns list of (id, key, atype, answer-sig, question, answer)."""
    sents = []
    for bid, text in stream:
        text = re.sub(r"^\(\w\)\s*", "", text)
        text = re.sub(r"^\d+\.\s*", "", text)
        for s in re.split(r"(?<=\?)\s+|(?<=[^.…]\.)\s+", text):
            if s.strip():
                sents.append((bid, s.strip()))
    out = []
    i = 0
    kind = None
    while i < len(sents):
        bid, s = sents[i]
        if s.endswith("?") or s.endswith("? …") :
            kind = kind_from(s, ts, kind)
            ans = []
            j = i + 1
            while j < len(sents) and not sents[j][1].endswith("?"):
                if re.match(r"^(\d+\.|\(|#|!\[\[)", sents[j][1]):
                    j += 1
                    continue
                ans.append(sents[j][1])
                j += 1
            a = " ".join(ans)
            # answers may sit after '?' in the same sentence chunk
            k = qkey(s, kind, ts)
            t = atype(a, ts) if a else "?"
            table = TSN if ts else VN
            vrx = (VERB_TS if ts else VERB_VI)[kind]
            sig = tuple(sorted(set(tuple(sorted(set(name_pol(x, kind, table, vrx)))) for x in ans))) if t == "PART" else ()
            out.append((bid, k, t, sig, s, a))
            i = j
        else:
            i += 1
    return out

def ts_stream():
    with open(TS, encoding="utf-8") as f:
        L = [norm_ts(unicodedata.normalize("NFC", l.rstrip("\n"))) for l in f]
    start = next(i for i, l in enumerate(L) if l.rstrip().endswith("^6-7-3-0"))
    end = next(i for i, l in enumerate(L) if l.rstrip().endswith("^6-7-263"))
    stream, buf = [], []
    for l in L[start:end + 1]:
        if not l.strip():
            continue
        m = IDR.search(l)
        buf.append(IDR.sub("", l))
        if m:
            for b in buf:
                stream.append((m.group(1), b))
            buf = []
    # join '...' line breaks: TS splits a question across two lines after '...'
    joined = []
    for bid, t in stream:
        if joined and joined[-1][1].endswith("...") and not re.match(r"^\d+\.", t):
            joined[-1] = (bid, joined[-1][1] + " " + t)
        else:
            joined.append((bid, t))
    return joined

def our_stream():
    stream = []
    for fn in C.FILES:
        V = C.lines(C.VI + fn)
        buf = []
        for l in V:
            m = C.ID_RE.search(l)
            buf.append(C.ID_RE.sub("", l))
            if m:
                for b in buf:
                    stream.append((m.group(1), b))
                buf = []
    return stream

def main():
    T = parse(ts_stream(), True)
    O = parse(our_stream(), False)
    tq = defaultdict(list)
    for r in T:
        tq[r[1]].append(r)
    used = defaultdict(int)
    nm = 0
    diff = []
    nomatch = []
    for r in O:
        lst = tq.get(r[1], [])
        k = used[r[1]]
        if k >= len(lst):
            nomatch.append(r)
            continue
        used[r[1]] += 1
        t = lst[k]
        nm += 1
        clean = lambda sig: set(x for x in sig if x and not any(p == "?" for _, p in x))
        same = (r[2] == t[2]) and (r[2] != "PART" or clean(r[3]) == clean(t[3]))
        if not same:
            diff.append((r, t))
    if "-c" in sys.argv:
        for r, t in diff:
            if r[2] != t[2]:
                print("TYPE  ours %s %s=%s | TS %s %s" % (r[0], r[1], r[2], t[0], t[2]))
                continue
            o, s = clean(r[3]), clean(t[3])
            print("PART  ours %s %s | TS %s | ours-only %s | ts-only %s" % (
                r[0], r[1][1:], t[0], sorted(o - s), sorted(s - o)))
        return
    print("ours Q:", len(O), "TS Q:", len(T), "matched:", nm, "diff:", len(diff), "unmatched ours:", len(nomatch))
    show = "-v" in sys.argv
    for r, t in diff:
        print("\nOURS %s %s %s | TS %s %s" % (r[0], r[1], r[2], t[0], t[2]))
        print("  ours sig:", r[3])
        print("  ts   sig:", t[3])
        if show:
            print("  OQ:", r[4]); print("  OA:", r[5][:600])
            print("  TQ:", t[4]); print("  TA:", t[5][:600])
    if "-u" in sys.argv:
        for r in nomatch:
            print("UNMATCHED", r[0], r[1], r[2])

main()
