"""pi-6 Burmese RAILS LAYER: source patches of the zero-shot generators (pi-6-my/make_*.py, my6_formulas.py; read
only), applied in memory by build_rails.py. Model: pi-5-my/rails/my_formulas_rails.py (read only).

PATCHES[file] = [(old, new, count, reason)]: «old» must occur exactly «count» times in that file's source, else the
build stops. A reason names the family, the Pāli, the term / decision or the §A item (mapper-my/map-harmonise-notes.md).

The termbase (AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md, sha256 847e49cd…, LOCKED) was built from this
zero-shot's keyword map, so the adherence run of the zero-shot has no GENUINE miss (333 rows, all INFLECTION:
rails/adherence-classified.tsv); the layer holds the §A text item that no term decides and that a single shared
string fixes everywhere (identical Pāli = identical Burmese).

L01 §A1 «yassa cittassa anantarā» (map-harmonise §A 1; termbase notes-part5 5d: left for the rails step).
    The zero-shot has two Burmese forms of the one Pāli phrase: the correlative «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (5-01 …
    5-03, 9-01 … 9-03, 10-09 … 10-11; 166 places) and «မိမိ စိတ်၏ ချက်ချင်း နောက်၌» («one's own mind»; 6-01, 6-02,
    10-05 … 10-07, 10-12; 92 places). The Pāli is the same phrase in every place: yassa is the relative pronoun in
    agreement with cittassa («immediately after which mind»), whatever the main clause's subject is (the last mind
    «… pacchimacittaṃ uppajjissati» or the persons «… aggamaggaṃ paṭilabhissanti»), and the Pāli has no word for
    «own» (မိမိ). The rails take the one rendering that reads the Pāli as written, the majority correlative
    «အကြင်စိတ်၏ ချက်ချင်း နောက်၌», already used without a following «ထိုစိတ်၏» in the persons frames of ch. 5 / 9 / 10-09 …
    10-11 («အကြင်စိတ်၏ ချက်ချင်း နောက်၌ အမြတ်ဆုံး မဂ်ကို ရရှိမည့်သူတို့»). cittassa «စိတ်» and anantarā «ချက်ချင်း နောက်»
    (locked terms) are unchanged. Three generator strings build the 92 places: make_ch6-8 OWN_MIND (6-01 / 6-02),
    make_ch10b OWN_CITTA (10-05 … 10-07), make_ch10c OWN_MIND (10-12).
"""

A1 = ("L01 §A1 yassa cittassa anantarā = «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (one rendering of the one Pāli phrase; "
      "the correlative yassa … cittassa as written, no «မိမိ» (own) in the Pāli; = 5-01 … 5-03, 9-01 … 9-03, 10-09 … 10-11)")

PATCHES = {
    "make_ch6-8": [
        ('OWN_MIND = new("yassa cittassa anantarā", "မိမိ စိတ်")', 'OWN_MIND = new("yassa cittassa anantarā", "အကြင်စိတ်")',
         1, A1 + ": 6-01 / 6-02 (61 places)"),
    ],
    "make_ch10b": [
        ('OWN_CITTA = f"မိမိ {CITTA}၏"', 'OWN_CITTA = f"အကြင်{CITTA}၏"', 1, A1 + ": 10-05 … 10-07 (24 places)"),
    ],
    "make_ch10c": [
        ('OWN_MIND = "မိမိ စိတ်"', 'OWN_MIND = "အကြင်စိတ်"', 1, A1 + ": 10-12 (7 places)"),
    ],
}
