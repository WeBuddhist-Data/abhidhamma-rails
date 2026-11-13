"""Hand-translated irregular lines of 3-01 / 3-02 (Pāli line without block ID -> Hindi line).
Built from the same strings as build_rails_3-01-3-02.py; abbreviated question lists keep «…» at the Pāli spot."""
IK = "इंद्रिय-क्षेत्र"
Q_AY = "क्या इंद्रिय-क्षेत्र, {} का इंद्रिय-क्षेत्र हैं"            # āyatanā Xāyatanaṃ
Q_NAY = "जो इंद्रिय-क्षेत्र नहीं हैं, क्या वे {} का इंद्रिय-क्षेत्र नहीं हैं"  # nāyatanā na Xāyatanaṃ
NA_CA = "न इंद्रिय-क्षेत्र"                                        # … na ca āyatanā
CH = "{} को छोड़कर"                                                 # X ṭhapetvā
MV = "मन के विषयों"

OVERRIDES = {
    # 3-01 ^6-3-12
    "Āyatanā ghānāyatananti…pe… āyatanā dhammāyatananti?":
        f"{Q_AY.format('नाक')}… {Q_AY.format(MV)}?",
    "Sotaṃ sotāyatananti?…Pe… avasesā āyatanā na dhammāyatanaṃ…pe….":
        f"क्या कान, कान का इंद्रिय-क्षेत्र है?… शेष इंद्रिय-क्षेत्र, {MV} का इंद्रिय-क्षेत्र नहीं हैं…।",
    "Āyatanā sotāyatananti…pe… āyatanā manāyatananti?":
        f"{Q_AY.format('कान')}… {Q_AY.format('मन')}?",
    # 3-01 ^6-3-13
    "Nāyatanā na cakkhāyatanaṃ…pe… nāyatanā na dhammāyatananti? Āmantā.":
        f"{Q_NAY.format('आँख')}… {Q_NAY.format(MV)}? हाँ।",
    "Na ghānaṃ na ghānāyatanaṃ…pe… nāyatanā na dhammāyatananti?":
        f"जो नाक नहीं है, क्या वह नाक का इंद्रिय-क्षेत्र नहीं है… {Q_NAY.format(MV)}?",
    "Nāyatanā na sotāyatanaṃ…pe… nāyatanā na manāyatananti? Āmantā.":
        f"{Q_NAY.format('कान')}… {Q_NAY.format('मन')}? हाँ।",
    # 3-01 ^6-3-14
    "Āmantā.…Pe… ghānaṃ… jivhā… kāyo… rūpaṃ… saddo… gandho… raso… phoṭṭhabbo… mano… dhammo āyatananti?":
        "हाँ।… क्या नाक… जीभ… शरीर… रूप… ध्वनि… गंध… स्वाद… स्पर्श… मन… परिघटना, इंद्रिय-क्षेत्र है?",
    # 3-01 ^6-3-15
    "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā.":
        f"{CH.format('कान')}… {CH.format('नाक')}… {CH.format('जीभ')}… {NA_CA}।",
    "Rūpaṃ ṭhapetvā…pe… saddaṃ ṭhapetvā…pe… gandhaṃ ṭhapetvā…pe… rasaṃ ṭhapetvā…pe… phoṭṭhabbaṃ ṭhapetvā…pe… "
    "na ca āyatanā. Nāyatanā na phoṭṭhabbāyatananti? Āmantā.":
        f"{CH.format('रूप')}… {CH.format('ध्वनि')}… {CH.format('गंध')}… {CH.format('स्वाद')}… "
        f"{CH.format('स्पर्श')}… {NA_CA}। {Q_NAY.format('स्पर्श')}? हाँ।",
    # 3-01 ^6-3-16
    "Āyatanā ghānāyatanaṃ…pe… āyatanā dhammāyatananti?":
        f"{Q_AY.format('नाक')}… {Q_AY.format(MV)}?",
    "Āyatanā cakkhāyatananti?…Pe… na cakkhāyatanaṃ…pe…. Āyatanā dhammāyatananti?…Pe… na dhammāyatanaṃ.":
        f"{Q_AY.format('आँख')}?… आँख का इंद्रिय-क्षेत्र नहीं हैं…। {Q_AY.format(MV)}?… "
        f"{MV} का इंद्रिय-क्षेत्र नहीं हैं।",
    "Āyatanā cakkhāyatananti?…Pe… āyatanā dhammāyatananti? …Pe… na dhammāyatanaṃ…pe….":
        f"{Q_AY.format('आँख')}?… {Q_AY.format(MV)}? … {MV} का इंद्रिय-क्षेत्र नहीं हैं…।",
    "Āyatanā cakkhāyatanaṃ…pe… āyatanā manāyatananti?":
        f"{Q_AY.format('आँख')}… {Q_AY.format('मन')}?",
    # 3-01 ^6-3-17
    "Nāyatanā na ghānāyatanaṃ…pe… nāyatanā na dhammāyatananti?":
        f"{Q_NAY.format('नाक')}… {Q_NAY.format(MV)}?",
    "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā. Nāyatanā na dhammāyatananti? Āmantā.":
        f"{CH.format('कान')}… {CH.format('नाक')}… {CH.format('जीभ')}… {NA_CA}। {Q_NAY.format(MV)}? हाँ।",
}
