import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_G10b2_ru as B  # noqa: E402

G45, G10a, G2 = B.G45, B.G10a, B.G2
for p in sys.argv[1:]:
    if p.startswith("L:"):
        print("LINE", B.translate_line(p[2:]))
        continue
    print("UNITS", p, "->", G45.units(p))
    print("INTRO", G45.intro_ru(p))
