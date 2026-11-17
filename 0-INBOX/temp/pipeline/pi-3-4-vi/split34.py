"""Split the converted Vietnamese volume (Dhātukathā + Puggalapaññatti) into two drafts.

The Dhātukathā ends with "HOÀN BỊ BỘ NGUYÊN CHẤT NGỮ" and its dedication ("Chia phước …
Dương lịch 1975"); the Puggalapaññatti title page ("BỘ THỨ TƯ …", printed right after the
dedication) and its book title are dropped; the Puggalapaññatti starts at its own homage.

Usage: split34.py <vi-34-draft.md> <vi-3-draft.md> <vi-4-draft.md>
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
src, out3, out4 = sys.argv[1:4]
s = open(src, encoding="utf-8").read()
cut = s.index("BỘ NHÂN CHẾ ĐỊNH (Puggalapaññatti)")
dt, pp = s[:cut], s[cut:]
end = dt.index("BỘ THỨ TƯ", dt.index("HOÀN BỊ BỘ NGUYÊN CHẤT NGỮ"))
dt = dt[:end].rstrip() + "\n"
pp = pp[pp.index("CUNG K"):]
open(out3, "w", encoding="utf-8", newline="\n").write(dt)
open(out4, "w", encoding="utf-8", newline="\n").write(pp)
print("vi-3 ends:", repr(dt[-90:]))
print("vi-4 starts:", repr(pp[:90]))
