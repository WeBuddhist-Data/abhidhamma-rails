"""Per-line count comparison of mapped Pali terms vs Vietnamese renderings."""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
only = sys.argv[1].split(",") if len(sys.argv) > 1 and sys.argv[1] != "all" else None
sel = sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] != "any" else None
show = int(sys.argv[3]) if len(sys.argv) > 3 else 5
MAP = [
    ("anagami", r"anāgām", r"không trở lại"),
    ("arahat", r"\barah(?:at|ant|ā)", r"A-la-hán"),
    ("puthujjana", r"puthujjan", r"phàm phu"),
    ("suddhavasa", r"suddhāvās", r"Tịnh Cư"),
    ("asanna", r"asaññasatt", r"Vô Tưởng"),
    ("nirodha", r"nirodhasamāpann", r"thiền chấm dứt"),
    ("itare", r"\bitares", r"\bkhác\b"),
    ("sabbe", r"\bsabbes", r"tất cả"),
    ("upapajj", r"upapajjant|upapajjamān", r"tái sinh"),
    ("cavant", r"\bcavant", r"chết đi"),
    ("cuta", r"\bcutass", r"đã chết đi khỏi"),
    ("pavatte", r"\bpavatte\b", r"trong đời sống"),
    ("uppadakkhana", r"uppādakkhaṇ", r"khoảnh khắc sinh khởi"),
    ("bhangakkhana", r"bhaṅgakkhaṇ", r"khoảnh khắc tan rã"),
    ("pacchima", r"pacchimacitt", r"tâm cuối cùng"),
    ("anantara", r"anantarā", r"ngay sau"),
    ("kamadhatu", r"(?<!na)kāmadhāt|(?<!na)kāmāvacar", r"(?<!không phải là )cõi dục lạc|thuộc dục lạc|cõi dục"),
    ("rupadhatu", r"(?<![an])rūpadhāt|(?<![an])rūpāvacar|(?<![a-z])rūpe\b", r"(?<!không phải là )cõi hình sắc|thuộc hình sắc"),
    ("arupadhatu", r"(?<!na)arūpadhāt|(?<!na)arūpāvacar|\barūpe\b", r"(?<!không phải là )cõi không hình sắc|thuộc không hình sắc"),
    ("catuvokara", r"catuvokār", r"bốn khối"),
    ("pancavokara", r"pañcavokār", r"năm khối"),
    ("ekavokara", r"ekavokār", r"một khối"),
    ("dukkhavedana", r"dukkhāya vedanāya", r"cảm giác khó chịu"),
    ("dvisu", r"dvīsu vedanāsu", r"hai loại cảm giác"),
    ("vattabba", r"vattabb", r"không nên nói"),
    ("bhanga", r"\bbhaṅgā\b", r"phải phân chia"),
    ("kassaci", r"\bkassaci\b", r"một số chúng sinh"),
    ("satteva", r"satteva|pañceva|tayoeva", r"chỉ có"),
    ("dutiye", r"\bdutiye\b", r"thứ hai"),
    ("aggamagga", r"aggamagg", r"con đường tối thượng"),
    ("ahetuka", r"\bahetuk", r"không có gốc rễ"),
    ("sahetuka", r"\bsahetuk", r"(?<!không )có gốc rễ"),
    ("nanasampayutta", r"ñāṇasampayutt", r"gắn liền với hiểu biết"),
    ("nanavippayutta", r"ñāṇavippayutt", r"không gắn liền với hiểu biết"),
    ("somanassena", r"\bsomanassena\b", r"có niềm vui đi kèm"),
    ("upekkhaya", r"\bupekkhāya\b", r"có sự bình thản đi kèm"),
    ("vina", r"\bvinā\b", r"không có [^,]*đi kèm"),
    ("itthi_up", r"itthīnaṃ", r"người nữ"),
    ("purisa_up", r"purisānaṃ", r"người nam"),
    ("vattamane", r"vattamāne", r"đang diễn ra"),
    ("ettha", r"\bettha\b", r"\bở đó\b"),
    ("tattha", r"\btattha\b", r"ở nơi ấy|ở đó"),
]
c = collections.Counter()
shown = collections.Counter()
for f, n, sid, p, v in pairs(only):
    if p.startswith("#"):
        continue
    for name, pr, vr in MAP:
        if sel and name not in sel:
            continue
        a = len(re.findall(pr, p, re.I))
        b = len(re.findall(vr, v))
        if a != b:
            c[(f, name)] += 1
            if shown[name] < show:
                shown[name] += 1
                print(f"{f}:{n} {sid} {name} {a}/{b}\n  P: {p.strip()[:700]}\n  V: {v.strip()[:900]}")
for k, x in sorted(c.items()):
    print(k, x)
