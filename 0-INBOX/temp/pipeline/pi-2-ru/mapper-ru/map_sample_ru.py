"""Build the SAMPLE Pāli->Russian keyword maps for pi-2 (Vibhaṅga): preamble, 1-khandhavibhango.

usage: python -I -X utf8 map_sample_ru.py          (writes the two <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  KH (map_common_pi2_ru.py)  ->  pi-1 CH2 / MATRIX / CORE.
The overrides are the per-segment readings found when comparing each segment's Russian
(see ru-map-conventions-pi2.md).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi2_ru import (CORE, KH, NDE, allowed_for, build_part, hetuko_value, lc,  # noqa: E402,F401
                               present, read_pali, read_russian, value, verify)

PARTS = ["preamble", "1-khandhavibhango"]

# finite-verb frames (text «не устраняется», «не сопровождается»): infinitive, as pi-1 ^1-584
_FINITE = {"pahātabbo": "устраняться", "sahagato": "сопровождаться", "sahagatā": "сопровождаться",
           "upekkhāsahagatā": "сопровождаться невозмутимостью",
           "sukhasahagatā": "сопровождаться счастьем", "pītisahagato": "сопровождаться восторгом"}

OVERRIDES = {
    # ---- 2-33 rūpa ekaka (= pi-1 ^1-584) and the rūpa classifications
    "2-33": {"sahagataṃ": "сопровождаться", "sukha": "счастье", "dukkha": "болезненный",
             "samphassaṃ": "контакт", "asaṃkiliṭṭha": "неомрачённый"},
    # ---- 2-152 / 2-153 pañhāpucchaka
    "2-152": {"pahātabbo": "устраняться", "hetuko": "чьи корни", "gāmī": "ведущий"},
    "2-153": {**_FINITE, "asaṃkiliṭṭho": "не омрачённый"},
}


# Same Pāli fragment, different Russian wording by segment: the first candidate found in the
# segment's Russian wins (checked after reading the segments; the order is the preference).
CHOICES = {
    "upādāniyo": ["служащий объектом цепляния", "служащий его объектом"],   # upādinnupādāniyo only
}


def resolver_for(part):
    ru, pi = read_russian(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if part == "preamble" and lc(kw) in CORE:
            return CORE[lc(kw)]
        if kw == "hetuko":
            return hetuko_value(pi.get(bid, ""))
        if lc(kw) in CHOICES:
            for cand in CHOICES[lc(kw)]:
                if present(cand, ru.get(bid, "")):
                    return cand
            return CHOICES[lc(kw)][0]
        return value(kw, kws)
    return resolve


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolver_for(p))
        verify(p, show=200, allowed=allowed_for(p))
