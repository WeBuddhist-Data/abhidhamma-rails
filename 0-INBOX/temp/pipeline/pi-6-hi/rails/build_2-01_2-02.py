"""Build the Hindi plain RAILS translation of pi-6 2-01-khandhayamaka.md and 2-02-khandhayamaka.md.

2-01: Hindi of Pāli lines 1-638 (to ^6-2-55) copied VERBATIM from sample-1\\2-01-sample.md (user-approved);
      the rest is built here. 2-02: built in full.
Imports build_rails_sample.py read-only (formula constants and builder); adds only the lines it has no formula for.

usage: python -I -X utf8 build_2-01_2-02.py
"""
import sys
import pathlib

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as S  # noqa: E402  (read-only)

PALI = S.PALI_DIR
HI = S.HI_DIR

# ---------------------------------------------------------------------------------------------------------
# Source slips: Pāli sentence as printed -> Pāli read for translation (reported in notes-2-01-2-02.md)
# ---------------------------------------------------------------------------------------------------------
SLIPS = {
    # 2-02 ^6-2-134: "ca" missing before the second verb of a "both" clause
    "Catuvokārā pañcavokārā cavantānaṃ tesaṃ saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati.":
        "Catuvokārā pañcavokārā cavantānaṃ tesaṃ saññākkhandho ca nirujjhissati vedanākkhandho ca nirujjhati.",
    # 2-02 ^6-2-151: stray comma inside a "both" clause
    "tesaṃ tattha rūpakkhandho ca na nirujjhittha, vedanākkhandho ca na nirujjhissati.":
        "tesaṃ tattha rūpakkhandho ca na nirujjhittha vedanākkhandho ca na nirujjhissati.",
    # 2-02 ^6-2-163: "ca" missing after the first subject of a "both" clause
    "tesaṃ tattha rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati.":
        "tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca na nirujjhati.",
    # 2-02 ^6-2-185: "vadanākkhandho" = vedanākkhandho
    "tassa vadanākkhandho nirujjhitthāti?": "tassa vedanākkhandho nirujjhitthāti?",
}

# variant bracket inside a being chain (2-01 ^6-2-87): Pāli bracket -> (Hindi anchor, Hindi bracket)
CHAIN_VARIANTS = {
    " [pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ (sī. syā.)]":
        (S.PACCHIMA_UPAPAJJ, " [पाठभेद (Sī., Syā.): pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ]"),
}

# ---------------------------------------------------------------------------------------------------------
# New lines (no formula in the sample builder). Recurring shapes are listed in notes-2-01-2-02.md.
# ---------------------------------------------------------------------------------------------------------
AGGA = "सर्वोच्च मार्ग से युक्त व्यक्ति"            # Aggamaggasamaṅgī
AGGA_ARAHA_CHHODKAR = f"{AGGA} और अर्हत् को छोड़कर शेष"   # Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā
YE_MAGGAM = "जो मार्ग प्राप्त करेंगे, "               # Ye maggaṃ paṭilabhissanti te
PUTHU = "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, "  # ye ca puthujjanā maggaṃ na paṭilabhissanti te
R = "भौतिक रूप के समूह को"
V = "अनुभूति के समूह को"

NEW_LINES = {
    # 2-02 ^6-2-130
    "Yattha rūpakkhandho na nirujjhati (yatthakaṃ paripuṇṇaṃ kātabbaṃ).":
        "जिस स्थान पर भौतिक रूप का समूह समाप्त नहीं होता (स्थान वाला भाग पूरा करना चाहिए)।",
    # 2-02 ^6-2-185
    "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).":
        "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत का विभाजन किया गया है, वैसे ही यहाँ उसका विभाजन करना चाहिए)।",
    # 2-02 ^6-2-209
    "Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhaṃ na parijānittha. Aggamaggasamaṅgiñca arahantañca "
    "ṭhapetvā avasesā puggalā rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānittha.":
        f"अर्हत् {R} पूरी तरह नहीं समझता, पर उसने {V} पूरी तरह समझा था। "
        f"{AGGA_ARAHA_CHHODKAR} व्यक्ति {R} भी पूरी तरह नहीं समझते और उन्होंने {V} भी पूरी तरह नहीं समझा था।",
    "Aggamaggasamaṅgī vedanākkhandhaṃ na parijānittha, no ca rūpakkhandhaṃ na parijānāti. Aggamaggasamaṅgiñca "
    "arahantañca ṭhapetvā avasesā puggalā vedanākkhandhañca na parijānittha rūpakkhandhañca na parijānanti.":
        f"{AGGA} ने {V} पूरी तरह नहीं समझा था, पर वह {R} पूरी तरह समझता है। "
        f"{AGGA_ARAHA_CHHODKAR} व्यक्तियों ने {V} भी पूरी तरह नहीं समझा था और वे {R} भी पूरी तरह नहीं समझते।",
    # 2-02 ^6-2-210
    "Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānanti, no ca vedanākkhandhaṃ na parijānissanti. Arahā "
    "ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānissanti.":
        f"{YE_MAGGAM}वे {R} पूरी तरह नहीं समझते, पर वे {V} पूरी तरह समझेंगे। "
        f"अर्हत् और {PUTHU}वे {R} भी पूरी तरह नहीं समझते और {V} भी पूरी तरह नहीं समझेंगे।",
    "Aggamaggasamaṅgī vedanākkhandhaṃ na parijānissati, no ca rūpakkhandhaṃ na parijānāti. Arahā ye ca puthujjanā "
    "maggaṃ na paṭilabhissanti te vedanākkhandhañca na parijānissanti rūpakkhandhañca na parijānanti.":
        f"{AGGA} {V} पूरी तरह नहीं समझेगा, पर वह {R} पूरी तरह समझता है। "
        f"अर्हत् और {PUTHU}वे {V} भी पूरी तरह नहीं समझेंगे और {R} भी पूरी तरह नहीं समझते।",
    # 2-02 ^6-2-211
    "Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānittha, no ca vedanākkhandhaṃ na parijānissanti. "
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānittha "
    "vedanākkhandhañca na parijānissanti.":
        f"{YE_MAGGAM}उन्होंने {R} पूरी तरह नहीं समझा था, पर वे {V} पूरी तरह समझेंगे। "
        f"{AGGA} और {PUTHU}उन्होंने {R} भी पूरी तरह नहीं समझा था और वे {V} भी पूरी तरह नहीं समझेंगे।",
    "Arahā vedanākkhandhaṃ na parijānissati, no ca rūpakkhandhaṃ na parijānittha. Aggamaggasamaṅgī ye ca "
    "puthujjanā maggaṃ na paṭilabhissanti te vedanākkhandhañca na parijānissanti rūpakkhandhañca na parijānittha.":
        f"अर्हत् {V} पूरी तरह नहीं समझेगा, पर उसने {R} पूरी तरह समझा था। "
        f"{AGGA} और {PUTHU}वे {V} भी पूरी तरह नहीं समझेंगे और उन्होंने {R} भी पूरी तरह नहीं समझा था।",
}


# harmonise I3 (binding): catuvokārānaṃ pañcavokārānaṃ is ONE chunk «चार या पाँच समूहों वाले अस्तित्व के प्राणियों में»
# in every case form; the sample builder (S.BEINGS) still gives two chunks for the genitive pair.
I3_TWO = f"{S.BEINGS['catuvokārānaṃ']}{S.JOIN_LAST}{S.BEINGS['pañcavokārānaṃ']}"
I3_ONE = f"{S.PLACE_NOUN['catupañcavokāra']} के प्राणियों में"


def my_line(line):
    hi = _my_line(line)
    if "catuvokārānaṃ pañcavokārānaṃ" in line:
        assert I3_TWO in hi, hi
        hi = hi.replace(I3_TWO, I3_ONE)
    return hi


def _my_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    body = line
    if m:
        bid = " " + m.group(1)
        body = line[: m.start()]
    body = body.strip()
    if body in NEW_LINES:
        return NEW_LINES[body] + bid
    for a, b in SLIPS.items():
        body = body.replace(a, b)
    for pv, (anchor, hv) in CHAIN_VARIANTS.items():
        if pv in body:
            hi = S.translate_line(body.replace(pv, ""))
            assert hi.count(anchor) >= 1, hi
            return hi.replace(anchor, anchor + hv, 1) + bid
    if body.startswith("#"):
        return S.translate_line(body + bid)
    return S.translate_line(body) + bid


def my_text(pali_text):
    out, prev_blank = [], True
    for line in pali_text.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(my_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def build():
    # 2-01
    raw = (PALI / "2-01-khandhayamaka.md").read_text(encoding="utf-8")
    lines = raw.splitlines()
    assert lines[S.SAMPLE_2_01_LAST_LINE - 1].rstrip().endswith("^6-2-55")
    sample = (RAILS / "sample-1" / "2-01-sample.md").read_text(encoding="utf-8")
    assert sample.endswith("^6-2-55\n") and "\r" not in sample
    # sanity: the sample builder still gives the sample text (it is copied verbatim either way)
    if S.translate_text("\n".join(lines[: S.SAMPLE_2_01_LAST_LINE]) + "\n") != sample:
        print("NOTE: builder output differs from the sample for lines 1-638; the sample is kept verbatim")
    rest = my_text("\n".join(lines[S.SAMPLE_2_01_LAST_LINE:]) + "\n")
    (HI / "2-01-khandhayamaka.md").write_text(sample + "\n" + rest, encoding="utf-8", newline="\n")
    # 2-02
    raw2 = (PALI / "2-02-khandhayamaka.md").read_text(encoding="utf-8")
    (HI / "2-02-khandhayamaka.md").write_text(my_text(raw2), encoding="utf-8", newline="\n")
    print("built: 2-01-khandhayamaka.md, 2-02-khandhayamaka.md")


if __name__ == "__main__":
    build()
