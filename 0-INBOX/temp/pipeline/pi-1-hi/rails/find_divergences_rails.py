"""Cross-chapter alignment check for the pi-1 Hindi RAILS translation: identical Pāli, differing Hindi.
Reuses ../find_divergences_hi.py (scan_a, scan_items, report) with the Hindi folder pointed at the rails chapters.

usage: python -I -X utf8 find_divergences_rails.py [out.md]   (default: divergences-rails.md, next to this script)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import hz_common
import find_divergences_hi as F

hz_common.CUR["hdir"] = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "divergences-rails.md")
seg, line, clause = F.scan_a()
o1, n1 = F.report(seg, "(a1) whole segments: identical Pāli, differing Hindi")
o2, n2 = F.report(line, "(a2) whole lines: identical Pāli, differing Hindi", minlen=12)
o3, n3 = F.report(clause, "(a3) clauses (sentence parts of lines whose clause counts match)", minlen=12)
o4, n4 = F.report(F.scan_items(), "(a4) comma/dash items of lines whose item counts match (cross-part only)", minlen=6, cross_only=True)
head = ["# pi-1 Hindi rails: divergences", "", f"(a1) segments: {n1}; (a2) lines: {n2}; (a3) clauses: {n3}; (a4) items: {n4}", ""]
open(dest, "w", encoding="utf-8", newline="\n").write("\n".join(head + o1 + o2 + o3 + o4) + "\n")
print("segments", n1, "lines", n2, "clauses", n3, "items", n4, "->", dest)
