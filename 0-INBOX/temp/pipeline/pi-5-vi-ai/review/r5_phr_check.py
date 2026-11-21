"""Coordinator check (2026-11-22): every line of review/r5_phr*.txt must occur in OUR rails chapters (so the phrase
lists hold only our own text). Prints counts only."""
import glob, os

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
V = os.path.join(ROOT, r"AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters")
ours = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(V, "*.md")))
for f in sorted(glob.glob(os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-5-vi-ai\review\r5_phr*.txt"))):
    lines = [l.strip() for l in open(f, encoding="utf-8") if l.strip()]
    miss = [l for l in lines if l not in ours]
    print(os.path.basename(f), "lines", len(lines), "not in our rails", len(miss))
    for l in miss[:5]:
        print("   ", l[:80])
