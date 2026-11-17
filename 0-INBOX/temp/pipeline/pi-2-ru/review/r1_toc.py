import sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load
ch = sys.argv[1]
p, r, pt, rt = load(ch)
for i, ((pid, pl), (rid, rl)) in enumerate(zip(p, r)):
    pl_len = sum(len(x) for x in pl)
    rl_len = sum(len(x) for x in rl)
    head = pl[0][:70]
    print(i, pid, len(pl), pl_len, rl_len, round(rl_len / max(pl_len, 1), 2), '|', head)
