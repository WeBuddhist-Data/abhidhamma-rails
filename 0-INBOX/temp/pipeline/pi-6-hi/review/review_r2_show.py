import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r2_align import pairs
# usage: review_r2_show.py <fileno> <from_nonempty> <to_nonempty>  (1-based, inclusive)
f = f"3-0{sys.argv[1]}-ayatanayamaka.md"
P, H = pairs(f)
a, b = int(sys.argv[2]), int(sys.argv[3])
for k in range(a - 1, min(b, len(P))):
    print(f"#{k+1} L{H[k][0]}")
    print("  P:", P[k][1])
    print("  H:", H[k][1])
