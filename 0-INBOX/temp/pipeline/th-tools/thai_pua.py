"""Map legacy Thai font private-use glyphs (U+F700-U+F71A) back to standard Unicode.

Word-era Thai fonts draw shifted/low variants of vowels and tone marks as
private-use glyphs; text extraction then returns those code points instead of
the real characters. This is the standard Microsoft/Apple Thai PUA layout.
"""

THAI_PUA = {
    0xF700: "ฐ",  # tho than without descender
    0xF701: "ิ",  # sara i (left-shifted)
    0xF702: "ี",  # sara ii
    0xF703: "ึ",  # sara ue
    0xF704: "ื",  # sara uee
    0xF705: "่",  # mai ek (low-left)
    0xF706: "้",  # mai tho
    0xF707: "๊",  # mai tri
    0xF708: "๋",  # mai chattawa
    0xF709: "์",  # thanthakhat
    0xF70A: "่",  # mai ek (low)
    0xF70B: "้",  # mai tho
    0xF70C: "๊",  # mai tri
    0xF70D: "๋",  # mai chattawa
    0xF70E: "์",  # thanthakhat
    0xF70F: "ญ",  # yo ying without descender
    0xF710: "ั",  # mai han-akat (left)
    0xF711: "ํ",  # nikhahit (left)
    0xF712: "็",  # maitaikhu (left)
    0xF713: "่",  # mai ek (left)
    0xF714: "้",  # mai tho (left)
    0xF715: "๊",  # mai tri (left)
    0xF716: "๋",  # mai chattawa (left)
    0xF717: "์",  # thanthakhat (left)
    0xF718: "ุ",  # sara u (low)
    0xF719: "ู",  # sara uu (low)
    0xF71A: "ฺ",  # phinthu (low)
}

TABLE = str.maketrans(THAI_PUA)


def fix(text: str) -> str:
    return text.translate(TABLE)
