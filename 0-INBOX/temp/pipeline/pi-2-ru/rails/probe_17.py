"""Chapter 17 helper: print the earlier builders' strings that chapter 17 reuses (reference only, writes nothing).
usage: python -I -X utf8 probe_17.py
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
import build_rails_sample_ru as S   # noqa: E402
import build_rails_1_ru as K1       # noqa: E402
import build_rails_2_3_ru as K23    # noqa: E402
import build_rails_4_5_ru as K45    # noqa: E402
import build_rails_6_ru as K6       # noqa: E402
import build_rails_7_9_ru as K79    # noqa: E402
import build_rails_10_12_ru as K10  # noqa: E402
import build_rails_13_15_ru as K1315  # noqa: E402
import build_rails_16_ru as K16     # noqa: E402

names = {
    "S": ["CH_TITLE", "DONE", "NUMW"],
    "K6": ["RAGA7", "DITTHI16", "VICIKICCHA", "UDDHACCA", "MOHA_PE", "NOT_KNOW4", "SOKA5" if hasattr(K6, "SOKA5") else "TENA"],
    "K23": ["MOHA_P1", "VITAKKA7", "DOSA_LIST", "CONNECTED", "MICCHA", "LISTS"],
    "K45": ["SOKA5", "PATH8", "JHANA1_P1", "JHANA2", "JHANA3_P1", "JHANA4_P1", "IND", "MARANA_LIST", "SER", "OBJ_GEN"],
    "K10": ["BYAPADA_P1", "THINA_P1", "MIDDHA_P1", "UDDHACCA_P1", "KUKKUCCA_A", "KUKKUCCA_B", "VICIKICCHA",
            "P1_1352", "P1_1353", "SEVEN", "SEVEN_LIST", "NOBLE8", "EIGHT_LIST", "FIVE_LIST", "JH", "ARUPA1", "ARUPA2",
            "ARUPA3", "ARUPA4", "J_PE", "J_INTO"],
    "K79": ["SATIP4", "SAMMAP4", "IDDHIP4"],
    "K16": ["TEN_VIEWS", "RIGHT_VIEW", "HAPPY", "WOE", "AFTER_DEATH", "CONDUCT", "GATI", "ORD", "SMALL"],
}
mods = {"S": S, "K6": K6, "K23": K23, "K45": K45, "K10": K10, "K79": K79, "K16": K16}
for m, ns in names.items():
    for n in ns:
        v = getattr(mods[m], n, "<missing>")
        print(f"== {m}.{n} = {v!r}")
