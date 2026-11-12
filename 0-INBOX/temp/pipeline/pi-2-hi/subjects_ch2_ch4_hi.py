# -*- coding: utf-8 -*-
"""Subjects and the few hand-assembled sentences of the Pañhāpucchaka of chapters 2 and 4 (built from matrix strings)."""
import re
import matrix_ch2_ch4_hi as M

ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
K = "इंद्रिय-क्षेत्र"
NUM = {"Dasa": "दस", "Dv": "दो", "Pañc": "पाँच", "Cattāro": "चार", "Ekādas": "ग्यारह", "Nav": "नौ", "Ch": "छह"}


def _pl(n):
    return M.Subj(f"{n} {K}", f"{n} {K}ों", True)


def _sg(owner):
    return M.Subj(f"{owner} का {K}", f"{owner} के {K}", False)


SUBJ_AYATANA = sorted([
    ("Dasāyatanā", _pl("दस")), ("Dvāyatanā", _pl("दो")), ("Pañcāyatanā", _pl("पाँच")),
    ("Cattāro āyatanā", _pl("चार")), ("Ekādasāyatanā", _pl("ग्यारह")), ("Navāyatanā", _pl("नौ")),
    ("Chāyatanā", _pl("छह")),
    ("Manāyatanaṃ", _sg("मन")), ("Dhammāyatanaṃ", _sg("मन के विषयों")),
    ("Rūpāyatanaṃ", _sg("दृश्य रूप")), ("Saddāyatanaṃ", _sg("ध्वनि")),
], key=lambda x: -len(x[0]))

S = "सत्य"
SUBJ_SACCA = sorted([
    ("Dukkhasaccaṃ", M.Subj(f"दुःख का {S}", f"दुःख के {S}", False)),
    ("Samudayasaccaṃ", M.Subj(f"उत्पत्ति का {S}", f"उत्पत्ति के {S}", False)),
    ("Nirodhasaccaṃ", M.Subj(f"दुःख के अंत का {S}", f"दुःख के अंत के {S}", False)),
    ("Maggasaccaṃ", M.Subj(f"मार्ग का {S}", f"मार्ग के {S}", False)),
    ("Dve saccā", M.Subj(f"दो {S}", f"दो {S}ों", True)),
    ("Tīṇi saccāni", M.Subj(f"तीन {S}", f"तीन {S}ों", True)),
], key=lambda x: -len(x[0]))


def _f(key, pl):
    sg, p, _ = M.lookup(key)
    return p if pl else sg


# "…pe…" chains of the cluster heads (no/… ogha, yoga, nīvaraṇa)
OVR_AYATANA = {
    "Ekādasāyatanā no oghā…pe… no yogā…pe… no nīvaraṇā":
        f"ग्यारह {K} {_f('oghā', True)} नहीं हैं… {_f('yogā', True)} नहीं हैं… {_f('nīvaraṇā', True)} नहीं हैं।",
}
OVR_SACCA = {
    "Samudayasaccaṃ ogho…pe… yogo…pe… nīvaraṇaṃ":
        f"उत्पत्ति का {S} {_f('ogho', False)} है… {_f('yogo', False)} है… {_f('nīvaraṇaṃ', False)} है।",
    # the Pāli has no full stop between the two statements (as written)
    "Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā":
        f"दो {S} {_f('nīvaraṇiyā', True)} हैं, दो {S} {_f('anīvaraṇiyā', True)} हैं।",
}
