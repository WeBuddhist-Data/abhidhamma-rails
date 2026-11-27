import sys
P = "/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-7_split_chapters/"
D = "/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my/chk-ch3-03-06/dev-"
n, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
pl = [l for l in open(P + n, encoding="utf-8-sig").read().splitlines() if l.strip()]
ml = [l for l in open(D + n, encoding="utf-8").read().splitlines() if l.strip()]
print(len(pl), len(ml))
for i in range(a, min(b, len(pl))):
    if pl[i].startswith("#"): continue
    print(f"[{i+1}] P:", pl[i]); print(f"     M:", ml[i])
