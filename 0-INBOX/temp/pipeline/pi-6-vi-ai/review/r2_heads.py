import re, sys, os, collections
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

# (pali regex, viet regex)
PAIRS = [
    (r'asaññasatt', r'vô tưởng'),
    (r'suddhāvās', r'tịnh cư'),
    (r'pañcavokār', r'năm khối'),
    (r'catuvokār', r'bốn khối'),
    (r'ekavokār', r'một khối'),
    (r'puthujjan', r'phàm phu'),
    (r'arahant|arahato', r'a-la-hán'),
    (r'anāgām', r'không trở lại'),
    (r'sakadāgām', r'một lần trở lại'),
    (r'sotāpann', r'nhập dòng'),
    (r'aggamagg', r'con đường tối thượng'),
    (r'nirodhasamāpann', r'thiền chấm dứt|sự chấm dứt'),
    (r'pacchimabhavik', r'kiếp sống cuối cùng'),
    (r'pacchimacitt', r'tâm cuối cùng'),
    (r'upapajjant|upapajjati|upapajjitvā|upapattikkhaṇ', r'tái sinh'),
    (r'cavant|cavati|cutassa|cutānaṃ', r'chết'),
    (r'uppādakkhaṇ', r'khoảnh khắc sinh khởi'),
    (r'bhaṅgakkhaṇ', r'khoảnh khắc tan rã'),
    (r'\bitaresaṃ|\bitarassa', r'\bkhác\b'),
    (r'\bsabbesaṃ', r'tất cả'),
    (r'\babhisametāv', r'(?<!chưa )đã thấu hiểu'),
    (r'anabhisametāv', r'chưa thấu hiểu'),
    (r'āpāyik|apāy', r'cõi khổ'),
    (r'vattamāne', r'đang diễn ra'),
    (r'paṭhamajjhān', r'thiền thứ nhất'),
    (r'dutiyajjhān', r'thiền thứ hai'),
    (r'tatiyajjhān', r'thiền thứ ba'),
    (r'catutthajjhān', r'thiền thứ tư'),
    (r'assāsapassās', r'hơi thở'),
    (r'kāmāvacar|kāmadhāt', r'dục lạc'),
    (r'arūpāvacar|arūpadhāt|\barūp(?!āyatan)', r'không hình sắc'),
    (r'(?<!a)rūpāvacar', r'hình sắc'),
    (r'acakkhuk', r'không có mắt'),
    (r'(?<!a)sacakkhuk', r'(?<!không )có mắt'),
    (r'aghānak', r'không có mũi'),
    (r'saghānak', r'(?<!không )có mũi'),
    (r'asotak', r'không có tai'),
    (r'sasotak', r'(?<!không )có tai'),
    (r'ajivhak', r'không có lưỡi'),
    (r'sajivhak', r'(?<!không )có lưỡi'),
    (r'itthī', r'người nữ'),
    (r'puris', r'người nam'),
    (r'parinibbāy', r'niết-bàn'),
    (r'vedanā', r'cảm giác'),
    (r'avitakk', r'không có sự hướng tâm'),
    (r'(?<!a)savitakk', r'(?<!không )có sự hướng tâm'),
    (r'taṇhāvippayutt', r'không gắn liền với khao khát'),
    (r'maggavippayutt', r'không gắn liền với con đường'),
    (r'kusal', r'thiện'),
    (r'anantarā', r'ngay sau'),
    (r'\baṭṭhamak', r'người thứ tám'),
    (r'paṭilabhi', r'đạt được'),
    (r'dukkhasacc', r'sự thật về khổ đau'),
    (r'samudayasacc', r'sự thật về sự phát sinh'),
    (r'nirodhasacc', r'sự thật về sự chấm dứt'),
    (r'maggasacc', r'sự thật về con đường'),
    (r'kāyasaṅkhār', r'tạo tác bằng thân'),
    (r'vacīsaṅkhār', r'tạo tác bằng lời nói'),
    (r'cittasaṅkhār', r'tạo tác bằng tâm'),
    (r'kāmarāgānusay', r'tham đắm dục lạc'),
    (r'paṭighānusay', r'ác cảm'),
    (r'mānānusay', r'kiêu mạn'),
    (r'diṭṭhānusay', r'quan điểm'),
    (r'vicikicchānusay', r'hoài nghi'),
    (r'bhavarāgānusay', r'tham đắm hiện hữu'),
    (r'avijjānusay', r'vô minh'),
    (r'cakkhāyatan|cakkhudhāt', r'(lĩnh vực|yếu tố) mắt'),
    (r'sotāyatan|sotadhāt', r'(lĩnh vực|yếu tố) tai'),
    (r'ghānāyatan|ghānadhāt', r'(lĩnh vực|yếu tố) mũi'),
    (r'jivhāyatan|jivhādhāt', r'(lĩnh vực|yếu tố) lưỡi'),
    (r'kāyāyatan|kāyadhāt', r'(lĩnh vực|yếu tố) thân'),
    (r'(?<!a)rūpāyatan|(?<!a)rūpadhātu(?!yā)', r'(lĩnh vực|yếu tố) hình sắc'),
    (r'saddāyatan|saddadhāt', r'(lĩnh vực|yếu tố) âm thanh'),
    (r'gandhāyatan|gandhadhāt', r'(lĩnh vực|yếu tố) mùi'),
    (r'rasāyatan|rasadhāt', r'(lĩnh vực|yếu tố) vị'),
    (r'phoṭṭhabbāyatan|phoṭṭhabbadhāt', r'(lĩnh vực|yếu tố) vật xúc chạm'),
    (r'manāyatan|manodhāt', r'(lĩnh vực|yếu tố) ý\b(?! thức)'),
    (r'dhammāyatan|dhammadhāt', r'(lĩnh vực|yếu tố) đối tượng của ý'),
    (r'manoviññāṇadhāt', r'yếu tố ý thức'),
]

only = sys.argv[1:]
cnt = collections.Counter()
for fn in FILES:
    pl = lines(os.path.join(P, fn)); vl = lines(os.path.join(V, fn))
    for li, (a, b) in enumerate(zip(pl, vl)):
        pa = re.sub(r'\[[^\]]*\]', '', a).lower(); vb = re.sub(r'\[[^\]]*\]', '', b).lower()
        bad = []
        for pr, vr in PAIRS:
            if only and pr not in only and not any(o in pr for o in only):
                continue
            np_, nv = len(re.findall(pr, pa)), len(re.findall(vr, vb))
            if np_ != nv:
                bad.append('%s %d/%d' % (pr.split('|')[0][:16], np_, nv))
                cnt[pr.split('|')[0][:16]] += 1
        if bad:
            print('==', fn, 'L%d' % li, '; '.join(bad))
            if os.environ.get('R2V'):
                print('  P:', a); print('  V:', b)
print(cnt)
