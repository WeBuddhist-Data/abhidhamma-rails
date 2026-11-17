"""Scratch for chapters 10-12: print reusable strings from the earlier builders and pi-1 lines by block ID.
Usage: python -I -X utf8 probe_10_12b.py [^1-NNN ...]
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru")
import build_ch1_sample_ru as S
import build_2_3_ru as T
import build_4_5_ru as F
import build_6_ru as G
import build_7_9_ru as Z

if len(sys.argv) > 1:
    for b in sys.argv[1:]:
        print(b, "=>", T.PI1[b], "\n")
    sys.exit()
for name in ("SATI_B", "PANNA_B", "VIRIYA_B", "SAMADHI_B", "SADDHA_B", "JH1", "JH2", "JH3", "JH4", "LOKUTTARA"):
    print("F." + name, "=>", getattr(F, name), "\n")
for name in ("SATI_PE", "PANNA_PE", "VIRIYA_PE", "SAMADHI_PE", "SATI_LOK", "VIP_R", "LOK_R", "VINITA", "VIHARATI", "UPETO_FULL"):
    print("Z." + name, "=>", getattr(Z, name), "\n")
for k, v in G.BODY.items():
    if k.startswith(("Yo rāgo", "Yaṃ cittaṃ")):
        print("G.BODY", k, "=>", v, "\n")
for name in ("VICI", "UDDH", "RAGA", "CITTA", "RUPA_K", "RUPA_V", "LOK_K", "LOK_V", "LOK_V_SUNNA", "RUPA_F", "ARUPA_K",
             "ARUPA_V", "ARUPA_F"):
    print("G." + name, "=>", getattr(G, name), "\n")
print("T.FEEL", T.FEEL, "\n")
print("T.SPACE_EXT", T.SPACE_EXT, "\n")
print("F.FACTOR_BODY keys", list(F.FACTOR_BODY), "\n")
print("S.CHAPTER_TITLES", S.CHAPTER_TITLES)
print("S.SECTION_TITLES", S.SECTION_TITLES)
