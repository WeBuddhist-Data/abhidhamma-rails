import re
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = "6-paticcasamuppadavibhango.md"
P = open(base + r"\pali\pi-2_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
V = open(base + r"\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf-8").read().split("\n")
M = {
 "avijjā": "vô minh", "saṅkhārā": "các sự tạo tác", "saṅkhāro": "sự tạo tác", "saṅkhāra": "sự tạo tác",
 "viññāṇaṃ": "thức", "viññāṇa": "thức", "nāmarūpaṃ": "phần tinh thần và vật chất", "nāmarūpa": "phần tinh thần và vật chất",
 "nāmaṃ": "phần tinh thần", "nāma": "phần tinh thần", "saḷāyatanaṃ": "sáu lĩnh vực nhận biết", "saḷāyatana": "sáu lĩnh vực nhận biết",
 "chaṭṭhāyatanaṃ": "lĩnh vực nhận biết thứ sáu", "chaṭṭhāyatana": "lĩnh vực nhận biết thứ sáu",
 "phasso": "sự tiếp xúc", "phassa": "sự tiếp xúc", "vedanā": "cảm giác", "taṇhā": "khao khát",
 "upādānaṃ": "sự bám víu", "upādāna": "sự bám víu", "bhavo": "sự hiện hữu", "bhava": "sự hiện hữu",
 "jāti": "sự sinh", "jarāmaraṇaṃ": "sự lão hóa và sự chết", "adhimokkho": "sự quyết định", "adhimokkha": "sự quyết định",
 "pasādo": "lòng tin trong sáng", "pasāda": "lòng tin trong sáng", "paṭighaṃ": "sự ác cảm", "paṭigha": "sự ác cảm",
 "vicikicchā": "sự hoài nghi", "uddhaccaṃ": "sự xao động", "uddhacca": "sự xao động",
 "kusalamūla": "các gốc rễ thiện", "akusalamūla": "các gốc rễ bất thiện",
}
pp = re.compile(r"\b(\w+?)paccayā(pi)? (\w+)")
vp = re.compile(r"((?:các )?[\wÀ-ỹ ]+?) (cũng )?làm điều kiện cho ((?:các )?[\wÀ-ỹ ]+?)(?= có | gắn | sinh khởi|[,;.:”…]| trong đó|$)")
bad = 0
for i, (p, v) in enumerate(zip(P, V)):
    pl = [(a, bool(b), c) for a, b, c in pp.findall(p)]
    if not pl:
        continue
    exp = []
    for a, b, c in pl:
        a2 = a[0].lower() + a[1:]
        exp.append((M.get(a2, "?" + a2), b, M.get(c, "?" + c)))
    got = []
    for a, b, c in vp.findall(v):
        a = a.strip()
        for pre in ("Vào lúc ấy, ", "vào lúc ấy ", "thì vào lúc ấy ", "Về câu “", "thế nào là “", "Ở đây, thế nào là “"):
            if pre in a:
                a = a.split(pre)[-1]
        a = re.sub(r"^.*?(Vô minh|vô minh)$", r"\1", a)
        got.append((a[0].lower() + a[1:], bool(b), c.strip()))
    # compare loosely: endswith match
    ok = len(exp) == len(got) and all(g[0].endswith(e[0]) and g[1] == e[1] and g[2].startswith(e[2]) for e, g in zip(exp, got))
    if not ok:
        bad += 1
        print("LINE", i + 1)
        print("  exp:", exp)
        print("  got:", got)
print("bad", bad)
