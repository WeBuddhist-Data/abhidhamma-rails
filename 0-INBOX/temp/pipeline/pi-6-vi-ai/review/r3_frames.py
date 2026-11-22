"""r3: frame consistency. Abstract each Pali sentence and its Vietnamese sentence
(names -> X, persons -> H, places -> L, lists collapsed) and show Pali frames that get
more than one Vietnamese frame. Also checks labels (Ka)->(a), vā pana -> Còn. Console only."""
import re, sys, unicodedata
from collections import defaultdict, Counter
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
import r3_check as C

PNAME = re.compile(r"\b\w*(?:kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay\w*", re.I)
VNAME = re.compile(r"khuynh hướng tiềm ẩn (?:tham đắm dục lạc|tham đắm hiện hữu|ác cảm|kiêu mạn|quan điểm|hoài nghi|vô minh)")

def abst(s, rxs):
    for rx, tag in rxs:
        s = re.sub(rx, tag, s, flags=re.I)
    return s

PI_RX = [(r"\b\w*(?:kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(\w*)", r"X\1"),
         (r"kāmadhātuyā (?:dvīsu|tīsu) vedanāsu|dukkhāya vedanāya|arūpadhātuyā|rūpadhātuyā|a?pariyāpanne|kāmadhātuyā", "L"),
         (r"\b(?:Puthujjan\w*|Anāgāmi\w*|Anāgāmī|Arah\w+|Aṭṭhamak\w*|Aggamaggasamaṅgī|Anāgāmimaggasamaṅgī\w*|\w*maggasamaṅgī\w*)", "H"),
         (r"\b(?:Dvinnaṃ|Tiṇṇaṃ|Catunnaṃ|Dve|Tayo|Cattāro|Tesaññeva|Tasseva|Teva|Sveva) (?:puggal\w+)", "H"),
         ]
VI_RX = [(VNAME.pattern, "X"),
         (r"hai loại cảm giác trong cõi dục lạc|ba loại cảm giác trong cõi dục lạc|cảm giác khó chịu|cõi không hình sắc|cõi hình sắc|những gì không nằm trong các cõi tồn tại|cõi dục lạc", "L"),
         (r"(?:[Bb]ậc |[Nn]gười )?(?:phàm phu|không trở lại|A-la-hán)|[Nn]gười thứ tám|[Nn]gười có được con đường(?: tối thượng| không trở lại)?|(?:[Hh]ai|[Bb]a|[Bb]ốn) hạng người|[Cc]hính (?:những )?hạng người ấy", "H"),
         ]

def collapse(s):
    for _ in range(4):
        s = re.sub(r"X(\w*) ca (?:X\1 ca )+", r"XL\1 ca ", s)
        s = re.sub(r"X(?:, X)* và X", "XL", s)
        s = re.sub(r"L(?:,? (?:ở )?L)+", "LL", s)
        s = re.sub(r"(, cũng (?:không )?(?:có |dứt bỏ |hiểu biết trọn vẹn )?X)(?:, cũng (?:không )?(?:có |dứt bỏ |hiểu biết trọn vẹn )?X)+", r"\1+", s)
        s = re.sub(r"(không (?:có |dứt bỏ |hiểu biết trọn vẹn )?X)\+", r"\1", s)
    return s

def main():
    m = defaultdict(Counter)
    ex = {}
    lab = []
    for fn in C.FILES:
        P, V = C.lines(C.PI + fn), C.lines(C.VI + fn)
        for i, (p, v) in enumerate(zip(P, V)):
            if p.startswith("#"):
                continue
            lp = re.match(r"\((Ka|Kha|Ga|Gha)\)", p)
            lv = re.match(r"\(([a-z])\)", v)
            mp = {"Ka": "a", "Kha": "b", "Ga": "c", "Gha": "d"}
            if (lp and mp[lp.group(1)]) != (lv and lv.group(1)):
                lab.append((fn, i, "LABEL", lp and lp.group(1), lv and lv.group(1)))
            if (" vā pana " in p) != v.lstrip("(ab) ").startswith("Còn"):
                lab.append((fn, i, "VAPANA", " vā pana " in p, v[:30]))
            for a, b in zip(C.split_sent(p), C.split_sent(v)):
                a2 = collapse(abst(re.sub(r"^\(\w+\) ", "", a), PI_RX))
                b2 = collapse(abst(re.sub(r"^\(\w\) ", "", b), VI_RX))
                m[a2][b2] += 1
                ex.setdefault((a2, b2), (fn, i))
    for t in lab:
        print(*t, sep=" | ")
    n = 0
    for a2, cnt in m.items():
        if len(cnt) > 1:
            n += 1
            print("\nPI:", a2)
            for b2, k in cnt.most_common():
                print("   %3d  %s   @%s" % (k, b2, ex[(a2, b2)]))
    print("\nPali frames:", len(m), "with >1 VI frame:", n)

main()
