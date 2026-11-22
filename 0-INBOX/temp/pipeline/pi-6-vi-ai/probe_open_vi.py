"""List the forms in use for the points left open for the termbase stop (harmonise-brief.md point 5):
per Pāli pattern, the Vietnamese candidate counts per chapter (compact).

usage: python -I -X utf8 -B probe_open_vi.py
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common as V

OPEN = [
    ("sakkāya standalone", r"sakkāy", ["tự ngã", "thân kiến"]),
    ("dhātu-section headings", r"dhātupucchā|dhātuvisajjan|Dhātuvisajja", ["theo các yếu tố", "theo các cõi"]),
    ("dhātu as plane in the body", r"\b(?:kāma|rūpa|arūpa)dhātu", ["cõi dục lạc", "cõi hình sắc", "cõi không hình sắc", "yếu tố"]),
    ("Aṭṭhamako", r"(?i)aṭṭhamak", ["Người thứ tám", "người thứ tám"]),
    ("tadekaṭṭhaṃ", r"tadekaṭṭh", ["những gì cùng hiện diện với nó"]),
    ("no ca … nappajahati", r"no ca \w+ (?:[^,.]* )?nappajah", ["vẫn dứt bỏ"]),
    ("no ca … na parijānāti", r"no ca \w+ (?:[^,.]* )?na parijān", ["vẫn hiểu biết trọn vẹn"]),
    ("no ca A ca B ca (neither)", r"no ca \w+ \w+ca \w+ca", ["không có", " và "]),
    ("na vattabbo", r"vattabb", ["không nên nói là", "hay “"]),
    ("kassaci", r"\bkassaci\b", ["ở một số người", "ở một số chúng sinh"]),
    ("bhaṅgā", r"bhaṅgā", ["phải phân chia", "phải phân tích"]),
    ("uppajjittha", r"uppajjittha", ["đã sinh khởi", "đã từng sinh khởi", "chưa từng sinh khởi"]),
    ("uppanna", r"\buppann", ["ở trạng thái đã sinh khởi"]),
    ("piyarūpa / diṭṭhisaññā / dibbacakkhu", r"piyarūp|diṭṭhisaññ|dibbacakkhu|dibbasot|paññācakkhu", ["hiểu theo nghĩa"]),
    ("avasesaṃ sotaṃ na indriyaṃ", r"(?i)avasesaṃ sotaṃ|avasesā sot", ["Tai còn lại", "tai còn lại"]),
    ("itthīnaṃ (beings)", r"\bitthīnaṃ|\bitthiyo\b|\bpurisānaṃ|\bpurisā\b", ["là người nữ", "là người nam", "người nữ", "người nam"]),
    ("ñāṇasampayuttānaṃ", r"ñāṇasampayutt", ["gắn liền với hiểu biết", "có hiểu biết đi kèm"]),
    ("eteneva bhāvena", r"eteneva bhāvena", ["trong chính trạng thái ấy"]),
    ("bhava (katici bhave …)", r"\bbhave\b|\bbhavaṃ\b|\bbhavo\b", ["kiếp sống", "kiếp"]),
    ("anantarā … pacchimacittaṃ uppajjissati (6-01 frame)", r"anantarā \w+ pacchimacittaṃ uppajjissati|anantarā \w+ \w+ pacchimacittaṃ",
     ["Vào tâm mà ngay sau đó", "vào tâm mà ngay sau đó", "ngay sau tâm nào đó"]),
    ("pavatte", r"\bpavatte\b", ["trong đời sống"]),
    ("kāyikaṃ dukkhaṃ", r"(?i)kāyik", ["khổ đau nơi thân", "sự khó chịu nơi thân"]),
    ("anaññātaññassāmīti bare", r"anaññātaññassāmī(?!tindriy)", ["sự biết được điều chưa từng biết"]),
]


def main():
    for name, rx, cands in OPEN:
        rx = re.compile(rx)
        per = []
        for part in V.PARTS:
            c = collections.Counter()
            for p, v in V.pairs(part):
                if not rx.search(p):
                    continue
                c["_l"] += 1
                for cd in cands:
                    c[cd] += v.count(cd)
            if c["_l"]:
                per.append(f"{V.short(part)}: l{c['_l']} " + " ".join(f"«{k}»{n}" for k, n in c.items() if k != "_l" and n))
        print(f"== {name}: " + " | ".join(per))


if __name__ == "__main__":
    main()
