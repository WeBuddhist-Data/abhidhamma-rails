r"""pi-6 Yamaka, Hindi plain zero-shot: Dhātuyamaka (4-dhatuyamaka.md) builder.

usage: python -I -X utf8 build_4_hi.py
Uses the shared engine of build_2_hi (frames of the approved sample + Khandhayamaka frames) with the
eighteen elements added. Lines with ellipses are split at the ellipsis and every piece is translated
by the same frames. Unknown pieces raise an error.
"""
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi"
sys.path.insert(0, HERE)
import build_sample_hi as S  # noqa: E402  (import only)
import build_2_hi as K       # noqa: E402

# ---------------------------------------------------------------- the eighteen elements (pi-2 Hindi)
DHATU = {
    "cakkhudhātu": "आँख का तत्व",
    "sotadhātu": "कान का तत्व",
    "ghānadhātu": "नाक का तत्व",
    "jivhādhātu": "जीभ का तत्व",
    "kāyadhātu": "शरीर का तत्व",
    "rūpadhātu": "दृश्य रूप का तत्व",
    "saddadhātu": "ध्वनि का तत्व",
    "gandhadhātu": "गंध का तत्व",
    "rasadhātu": "स्वाद का तत्व",
    "phoṭṭhabbadhātu": "स्पर्श का तत्व",
    "cakkhuviññāṇadhātu": "आँख की चेतना का तत्व",
    "sotaviññāṇadhātu": "कान की चेतना का तत्व",
    "ghānaviññāṇadhātu": "नाक की चेतना का तत्व",
    "jivhāviññāṇadhātu": "जीभ की चेतना का तत्व",
    "kāyaviññāṇadhātu": "शरीर की चेतना का तत्व",
    "manodhātu": "मन का तत्व",
    "manoviññāṇadhātu": "मन की चेतना का तत्व",
    "dhammadhātu": "मन के विषयों का तत्व",
}
# the bare word of each pair (rendered bare, as rūpaṃ = रूप in the sample)
BARE4 = {
    "cakkhu": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhā": "जीभ", "kāyo": "शरीर",
    "rūpaṃ": "रूप", "saddo": "ध्वनि", "gandho": "गंध", "raso": "रस", "phoṭṭhabbo": "स्पर्श",
    "cakkhuviññāṇaṃ": "आँख की चेतना", "sotaviññāṇaṃ": "कान की चेतना",
    "ghānaviññāṇaṃ": "नाक की चेतना", "jivhāviññāṇaṃ": "जीभ की चेतना",
    "kāyaviññāṇaṃ": "शरीर की चेतना", "mano": "मन", "manoviññāṇaṃ": "मन की चेतना",
    "dhammo": "परिघटना",
}
for k, v in DHATU.items():
    K.ITEMS[k] = (v, False)
    K.OBL[k] = v[:-len(" का तत्व")] + " के तत्व"
for k, v in BARE4.items():
    K.ITEMS[k] = (v, False)
    K.OBL[k] = v
K.ITEMS.update({"dhātu": ("तत्व", False), "dhātū": ("तत्व", True)})
# «… और तत्वों को छोड़कर»: dhātuñca … na ca dhātu/dhātū = the elements
K.OBL.update({"dhātu": "तत्वों", "dhātū": "तत्वों"})
K.set_items()
K.ACC_TO_ITEM["jivha"] = "jivhā"          # source slip "jivha ṭhapetvā" (^6-4-15)
for k in DHATU:
    K.ACC[k + "ṃ"] = K.OBL[k] + " को"
K.KNOWN.update(K.ITEMS)

K.VARIANTS.update({
    "[avaseso kāyo kāyo (syā.)]": "[" + S.VAR_READ + " (Syā.): avaseso kāyo kāyo]",
    "[avaseso kāyo (syā.)]": "[" + S.VAR_READ + " (Syā.): avaseso kāyo]",
    "[avasesā dhātū dhātū (syā.)]": "[" + S.VAR_READ + " (Syā.): avasesā dhātū dhātū]",
})

K.SPECIAL_A.update({
    "Dibbacakkhu paññācakkhu": ("दिव्य आँख और प्रज्ञा की आँख", True),
    "Dibbasotaṃ taṇhāsotaṃ": ("दिव्य कान और तृष्णा का प्रवाह", True),
    "Sīlagandho samādhigandho paññāgandho": ("सदाचार की गंध, एकाग्रता की गंध और प्रज्ञा की गंध", True),
    "Attharaso dhammaraso vimuttiraso": ("अर्थ का रस, शिक्षा का रस और मुक्ति का रस", True),
})
# sota = ear and stream: the pun is kept by naming the Pāli word
K.B_OVERRIDE["Dibbasotaṃ taṇhāsotaṃ"] = "“कान” (सोत)"

DT = S.CHAPTER_TITLES["Dhātuyamakaṃ"]
AT = S.CHAPTER_TITLES["Āyatanayamakaṃ"]
CYCLE = "चक्र पूरा करना चाहिए"                 # cakkaṃ bandhitabbaṃ

K.FIXED.update({
    "(Cakkaṃ bandhitabbaṃ).": f"({CYCLE})।",
    "Āmantā. (Jivhāpi ghānadhātusadisā).": f"{K.AMANTA} (जीभ भी नाक के तत्व के समान है)।",
    "Āmantā. (Saddo ghānasadiso).": f"{K.AMANTA} (ध्वनि नाक के समान है)।",
    "Āmantā. (Phoṭṭhabbo ghānasadiso).": f"{K.AMANTA} (स्पर्श नाक के समान है)।",
})

FIXED4 = {
    "Aṭṭhārasa dhātuyo – " + ", ".join(DHATU) + ".":
        "अठारह तत्व – " + ", ".join(DHATU.values()) + "।",
    "(Kha) dhātū [dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ] sotadhātu?…Pe…":
        "(ख) क्या तत्व [" + S.VAR_SPELL + " (Sī., Ka.): dhātu, दूसरे जोड़ों से मिलाकर देखना चाहिए], "
        + DHATU["sotadhātu"] + " हैं?…",
    "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)":
        f"(जैसे “{AT}” में चक्र पूरा किया गया है, वैसे ही यहाँ भी {CYCLE}।)",
    "Na jivhā… (saṃkhittaṃ [yaṃ saṃkhittaṃ (syā.)], ubhato āmantā).":
        "जीभ नहीं… (संक्षिप्त किया गया है [" + S.VAR_READ + " (Syā.): yaṃ saṃkhittaṃ], दोनों ओर उत्तर “हाँ” है)।",
    "(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti. Cakkaṃ bandhitabbaṃ).":
        f"(जैसे “{AT}” में शब्दावली है, वैसे ही “{DT}” में भी शब्दावली है। {CYCLE})।",
    "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi).":
        f"({CYCLE}, दोनों ओर और बाकी में भी सभी उत्तर “हाँ” हैं)।",
    "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)":
        f"(जैसे “{AT}” की शब्दावली है, वैसे ही “{DT}” की शब्दावली का विस्तार करना चाहिए)",
    "(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).":
        f"(जैसे “{AT}” का विभाजन किया गया है, वैसे ही “{DT}” का भी विभाजन करना चाहिए, उसे उसी के समान बनाना चाहिए)।",
    "Yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānātīti? Āmantā.…Pe… (dhātuyamakaṃ paripuṇṇaṃ peyyālena).":
        K.q_parinna("yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānāti") + "? " + K.AMANTA
        + "… (“" + DT + "” संक्षेप के साथ पूरे हुए)।",
    "Dhātuyamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=DT),
}

PE = r"…(?:[Pp]e…)?"


def piece(c):
    """Translate one piece of an ellipsis line (no ellipsis inside)."""
    core = c.strip()
    if not core:
        return c
    lead = c[:len(c) - len(c.lstrip())]
    trail = c[len(c.rstrip()):]
    return lead + piece_core(core) + trail


def acc_item(a):
    a = K.lc(a)
    if a in K.ACC_TO_ITEM:
        return K.ACC_TO_ITEM[a]
    for cand in (a[:-2] + "o", a[:-2] + "ā", a, a[:-1]):
        if cand in K.ITEMS:
            return cand
    return None


def piece_core(core):
    if core == ".":
        return "।"
    if core in K.FIXED:
        return K.FIXED[core]
    if core in K.SHORT:
        return K.SHORT[core]
    # question with an answer
    if "? " in core:
        q, a = core.split("? ", 1)
        return piece_core(q + "?") + " " + K.answer(a) if K.answer(a) else _fail(core)
    # several sentences: answer sentences, then a question without '?'
    parts = re.split(r"(?<=\.) (?=[A-ZĀĪŪṬḌṆÑṄ(])", core)
    if len(parts) > 1:
        return " ".join(piece_core(p) for p in parts)
    qm = "?" if core.endswith("?") else ""
    q = core[:-1] if qm else core
    if core.endswith(".") and not qm:
        r = K.answer(core)
        return r if r else _fail(core)
    r = K.question(K.lc(q))
    if r:
        return r + qm
    w = K.lc(q)
    if w in K.ITEMS:
        return K.ITEMS[w][0] + qm
    m = re.fullmatch(r"na (\S+)", w)
    if m and m.group(1) in K.ITEMS:
        return K.ITEMS[m.group(1)][0] + " नहीं" + qm
    m = re.fullmatch(r"(\S+) ṭhapetvā", w)
    if m and acc_item(m.group(1)):
        return K.EXCEPT_OF(m.group(1))
    if acc_item(w):
        return K.ITEMS[acc_item(w)][0] + qm
    return _fail(core)


def _fail(core):
    raise ValueError("untranslated piece: " + core)


def tr_body_dh(text):
    if text in FIXED4:
        return FIXED4[text]
    labeled = re.match(r"^\((?:Ka|Kha)\) ", text)
    if labeled:
        m = re.fullmatch(r"(.*\?)(…[Pp]e…\.?)", text)
        if m:
            return K.tr_body(m.group(1)) + "…"
        return K.tr_body(text)
    if "…" not in text and "?" not in text:
        r = K.answer(text)
        if r:
            return r
    toks = re.split(f"({PE})", text)
    return "".join("…" if i % 2 else piece(t) for i, t in enumerate(toks))


def main():
    K.build("4-dhatuyamaka.md", tr_body_dh)
    print("built 4-dhatuyamaka.md")


if __name__ == "__main__":
    main()
