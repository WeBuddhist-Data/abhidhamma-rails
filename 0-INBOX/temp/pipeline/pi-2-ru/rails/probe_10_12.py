"""Probe helper for chapters 10-12: prints strings exported by the earlier builders (reads only, writes nothing).
usage: python -I -X utf8 probe_10_12.py
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
import build_rails_sample_ru as S  # noqa
import build_rails_1_ru as K1  # noqa
import build_rails_2_3_ru as K23  # noqa
import build_rails_4_5_ru as K45  # noqa
import build_rails_6_ru as K6  # noqa

for k, v in K23.FEELING_P1.items():
    print("FEELING", k, "=", v)
print("CORE ākāsa", K23.CORE["ākāsa"])
print("BY_GREAT", K23.BY_GREAT)
print("VITAKKA7", K23.VITAKKA7)
print("SER", K45.SER)
print("DH mano", K23.DH["mano"], "|", K23.DH["manoviññāṇa"])
for key in ["parittārammaṇo", "mahaggatārammaṇo", "appamāṇārammaṇo", "maggārammaṇo", "maggahetuko", "maggādhipati",
            "ajjhattārammaṇo", "nevasekkhanāsekkho", "ācayagāmī", "upādinnupādāniyo", "savitakkasavicāro", "savitakko",
            "savicāro", "sappītiko", "appītiko", "pītisahagato", "sukhasahagato", "upekkhāsahagato", "arūpāvacaro",
            "rūpāvacaro", "pariyāpanno", "sauttaro", "lokiyo", "sāsavo", "upādinno", "hetu", "sahetuko",
            "hetu ceva sahetuko ca", "na hetu sahetuko", "majjhimo", "mahaggato", "sukhāya vedanāya sampayutto",
            "adukkhamasukhāya vedanāya sampayutto", "avitakko", "avicāro", "āsavavippayutto sāsavo"]:
    print(key, "=>", K1.ITEMS.get(key))
print(K1.SUBJ, K1.GROUP_GEN)
print("J1", K6.J1)
print("TASSEVA keys", list(K6.TASSEVA))
print("JHANA keys", list(K6.JHANA))
