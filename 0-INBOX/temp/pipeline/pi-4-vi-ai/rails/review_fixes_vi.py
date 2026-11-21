"""Coordinator review fixes, pi-4 Vietnamese rails (Puggalapaññatti), 2026-11-21.

The user approved the review findings r1-r3 ("Apply as recommended", vi-review-fixes-brief.md, decisions 1-11).
Exact string replacements, each rule anchored on its block IDs (or book-wide where the same Pāli recurs), each with an
asserted occurrence count. Always builds from rails/backup-pre-review/ (copied once, never overwritten), so it can be
re-run. Log: rails/review-fixes-log.tsv (file, block id, old, new, decision, n). Stale builder / formula strings:
printed and written to rails/review-fixes-notes.md (section generated below the marker line).
Chapters are NOT rebuilt from their builders.
"""
import collections, pathlib, re, shutil, sys, unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
VDIR = ROOT / "AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters"
RAILS = ROOT / "0-INBOX/temp/pipeline/pi-4-vi-ai/rails"
BAK = RAILS / "backup-pre-review"
PARTS = ["preamble", "1-matika", "2-ekakapuggalapannatti", "3-dukapuggalapannatti", "4-tikapuggalapannatti",
         "5-catukkapuggalapannatti", "6-pancakapuggalapannatti", "7-chakkapuggalapannatti",
         "8-sattakapuggalapannatti", "9-atthakapuggalapannatti", "10-navakapuggalapannatti",
         "11-dasakapuggalapannatti"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

# ------------------------------------------------------------------ backup (once)
BAK.mkdir(exist_ok=True)
for p in PARTS:
    dst = BAK / f"{p}.md"
    if not dst.exists():
        shutil.copyfile(VDIR / f"{p}.md", dst)

# ------------------------------------------------------------------ rules
# (decision, block ids (None = book-wide), old, new, expected total count)
R = []


def rule(dec, ids, old, new, n):
    R.append((dec, None if ids is None else set(ids.split()), old, new, n))


# 1 gotrabhū
rule("1", "4-10", "mà liền sau chúng xảy ra sự đi vào Giáo Pháp cao quý –",
     "mà liền sau chúng, trạng thái cao quý khởi lên –", 1)
# 2 idha niṭṭhā / idha vihāya niṭṭhā (matrix, question, closer); diṭṭheva dhamme and Idhekacco untouched
rule("2", "4-M-16 4-209", "đạt đến đích ở đời này", "đạt đến đích ngay trong cõi này", 3)
rule("2", "4-M-16 4-209", "đạt đến đích sau khi rời khỏi đời này", "đạt đến đích sau khi rời bỏ cõi này", 3)
# 3 heartwood simile ^4-170: pheggu sāraparivāro / sāro phegguparivāro / pheggu phegguparivāro / sāro sāraparivāro
HW = [  # old attribute, tree name, person attribute
    ("không có lõi mà xung quanh có lõi", "cây gỗ xốp mà các cây quanh nó có lõi",
     "không có lõi mà những người quanh mình có lõi"),
    ("có lõi mà xung quanh không có lõi", "cây có lõi mà các cây quanh nó là gỗ xốp",
     "có lõi mà những người quanh mình không có lõi"),
    ("không có lõi và xung quanh không có lõi", "cây gỗ xốp và các cây quanh nó cũng là gỗ xốp",
     "không có lõi và những người quanh mình cũng không có lõi"),
    ("có lõi và xung quanh có lõi", "cây có lõi và các cây quanh nó cũng có lõi",
     "có lõi và những người quanh mình cũng có lõi"),
]
for k, (old, tree, pers) in enumerate(HW):
    rule("3", "4-170", f"Giống như cái cây ấy {old},", f"Giống như cái cây ấy là {tree},", 1)  # simile
    rule("3", "4-170", f"cây {old}", tree, 1)                                                 # list of trees
    # persons: list «Người A, người B, người C, người D», question «… là người X?», «Như vậy là người X.»
    rule("3", "4-170", f"người {old}", f"người {pers}", 2 if k == 0 else 3)
    if k == 0:
        rule("3", "4-170", f"Người {old}", f"Người {pers}", 1)
# 4 kudāssu nāmāhampi … viharissāmī
rule("4", "4-91 4-92 4-93", "“Đến bao giờ tôi cũng sẽ, nhờ sự diệt tận",
     "“Đến bao giờ tôi mới được như vậy: nhờ sự diệt tận", 3)
# 5 pāpa- / kalyāṇamitto purisapuggalo … sampavaṅko
rule("5", "4-124", "nghiêng về phía điều xấu”", "nghiêng về phía người xấu”", 2)
rule("5", "4-126", "nghiêng về phía điều tốt”", "nghiêng về phía người tốt”", 1)
rule("5", "4-124 4-126", "“Con người kết bạn với", "“Người đàn ông này kết bạn với", 3)
# 6 purisa (cakkhumā puriso; purisassa ucchaṅge); «Này ông» ^4-98/99 kept
rule("6", "4-102", "Giống như một người có mắt,", "Giống như một người đàn ông có mắt,", 1)
rule("6", "4-108", "trong vạt áo của một người có đựng", "trong vạt áo của một người đàn ông có đựng", 1)
# 8 names
rule("8", "4-M-7", "Người ngược dòng đi đến cõi Sắc Cứu Cánh", "Người theo dòng đi lên đến cõi Sắc Cứu Cánh", 1)
rule("8", "4-40 4-209", "người ngược dòng đi đến cõi Sắc Cứu Cánh", "người theo dòng đi lên đến cõi Sắc Cứu Cánh", 3)
rule("8", "4-M-10 4-172", "lấy Giáo Pháp làm thước đo", "lấy phẩm hạnh làm thước đo", 3)
rule("8", "4-M-10 4-172", "lòng tin trong sáng nơi Giáo Pháp", "lòng tin trong sáng nơi phẩm hạnh", 3)
# 10 ^4-166 vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati
rule("10", "4-166", "Ở đời này, có người thấy có điều đáng khen và cũng có điều đáng chê.",
     "Ở đời này, về một người nào đó, có điều đáng khen và cũng có điều đáng chê.", 4)
# 11 small fixes
rule("11", "4-M-12 4-22 4-202 4-208", "đạt đến sự toàn tri, và sự làm chủ đối với các sức mạnh",
     "đạt đến sự toàn tri cùng sự làm chủ đối với các sức mạnh", 4)
rule("11", "4-17", "thì kiếp sẽ chưa bị thiêu hủy chừng nào người này chưa tự mình chứng nghiệm thành quả vào dòng.",
     "thì kiếp sẽ không bị thiêu hủy cho đến khi người này tự mình chứng nghiệm thành quả vào dòng.", 1)
# ^4-3..8 and the identical Pāli arūpasahagatānaṃ at ^4-187
rule("11", "4-3 4-4 4-5 4-6 4-7 4-8 4-187", "đi kèm với không hình sắc", "đi kèm với cái không có hình sắc", 10)
rule("11", "4-27 4-28 4-96 4-97 4-208", "Giáo Pháp do Như Lai tuyên bố được người ấy",
     "những điều do Như Lai tuyên bố được người ấy", 6)
rule("11", "4-167", "Kể từ chư thiên Tha Hóa Tự Tại [khác chính tả (Sī., Syā.): paranimmitavasavattideve], "
                    "chư thiên ở cao hơn đó sống nhờ",
     "Chư thiên Tha Hóa Tự Tại [khác chính tả (Sī., Syā.): paranimmitavasavattideve] "
     "và chư thiên ở các cõi cao hơn sống nhờ", 1)
rule("11", "4-114 4-163", "không nằm sẵn nơi người ấy lâu dài suốt một thời gian dài",
     "không âm ỉ trong người ấy lâu", 4)
rule("11", "4-113 4-163", "nằm sẵn nơi người ấy lâu dài suốt một thời gian dài", "âm ỉ trong người ấy rất lâu", 4)
rule("11", "4-164 4-165", "các vị Phật và các đệ tử của các vị Phật", "chư Phật và các đệ tử của Đức Phật", 2)
rule("11", "4-181", "người ấy", "vị ấy", 4)
rule("11", "4-168", "ít thức ăn, thức uống và đồ ăn", "ít lương thực, đồ uống và món ăn", 2)
rule("11", "4-174", "xuống nước đến lần thứ ba vào buổi chiều", "xuống nước ba lần mỗi ngày, lần thứ ba vào buổi chiều", 1)
rule("11", "4-93", "Vì trước đây, khi người ấy chưa được giải thoát, có sự mong cầu được giải thoát, "
                   "thì sự mong cầu ấy đã lắng xuống.",
     "Vì sự mong cầu được giải thoát mà người ấy từng có trước đây, khi chưa được giải thoát, nay đã lắng xuống.", 1)
rule("11", "4-98 4-99", "vì một chút lợi lộc vật chất nhỏ nhặt", "vì chút lợi lộc vật chất", 2)
rule("11", "4-62", "cách cấu tạo câu chữ cần xem xét", "cách cấu tạo của từ này cần được xem xét", 1)
# ^4-94: result first, every clause kept
G = ("khi có được thức ăn thích hợp chứ không phải khi không có được, khi có được thuốc men thích hợp chứ không phải "
     "khi không có được, khi có được người chăm sóc phù hợp chứ không phải khi không có được")
T = ("khi có được dịp thấy Như Lai chứ không phải khi không có được, khi có được dịp nghe Giáo Pháp và Giới Luật do "
     "Như Lai tuyên bố chứ không phải khi không có được")
S = "bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện"
rule("11", "4-94", f"có người bệnh {G}, thì khỏi bệnh ấy. (3)", f"có người bệnh chỉ khỏi bệnh ấy {G}. (3)", 1)
rule("11", "4-94", f"người bệnh nào {G} thì khỏi bệnh ấy, chính vì", f"người bệnh nào chỉ khỏi bệnh ấy {G}, chính vì", 1)
rule("11", "4-94", f"có người {T}, thì {S}. (3)", f"có người chỉ {S}, {T}. (3)", 1)
rule("11", "4-94", f"người nào {T} thì {S}, chính vì", f"người nào chỉ {S}, {T}, chính vì", 1)

# ------------------------------------------------------------------ apply
texts = {p: (BAK / f"{p}.md").read_text(encoding="utf-8") for p in PARTS}
orig = dict(texts)
log = []
hits = collections.Counter()
touched = collections.defaultdict(set)  # (part, line index) -> decisions


def segs(text):
    """split into segments on blank lines, keep the separators; return list of [seg, sid]"""
    out = []
    for s in text.split("\n\n"):
        m = ID.search(s)
        out.append([s, m.group(1) if m else None])
    return out


for ri, (dec, ids, old, new, n) in enumerate(R):
    for p in PARTS:
        ss = segs(texts[p])
        changed = False
        for item in ss:
            s, sid = item
            if ids is not None and sid not in ids:
                continue
            c = s.count(old)
            if c:
                item[0] = s.replace(old, new)
                hits[ri] += c
                changed = True
                log.append(f"{p}.md\t{sid}\t{old}\t{new}\t{dec}\t{c}")
        if changed:
            before = texts[p].split("\n")
            texts[p] = "\n\n".join(x[0] for x in ss)
            for i, (a, b) in enumerate(zip(before, texts[p].split("\n"))):
                if a != b:
                    touched[(p, i)].add(dec)
    assert hits[ri] == n, (dec, old[:60], hits[ri], n)

# ------------------------------------------------------------------ checks
OLD_GONE = ["sự đi vào Giáo Pháp cao quý", "đạt đến đích ở đời này", "rời khỏi đời này", "xung quanh",
            "Đến bao giờ tôi cũng sẽ", "nghiêng về phía điều", "Con người kết bạn", "một người có mắt",
            "vạt áo của một người có", "ngược dòng đi đến", "Giáo Pháp làm thước đo", "nơi Giáo Pháp",
            "có người thấy có điều đáng khen", "sự toàn tri, và sự làm chủ", "chưa bị thiêu hủy",
            "với không hình sắc", "Giáo Pháp do Như Lai", "Kể từ chư thiên", "nằm sẵn", "các vị Phật",
            "thức uống và đồ ăn", "xuống nước đến lần thứ ba", "Vì trước đây, khi người ấy", "nhỏ nhặt",
            "cấu tạo câu chữ", "thì khỏi bệnh ấy", "thì bước vào sự cố định"]
BAD = ["—", ":-", "….", "được được", "là là", "chánh niệm", "seed", "  ", "\r", "\n\n\n"]
problems = []
for p in PARTS:
    t, o = texts[p], orig[p]
    assert t.count("\n") == o.count("\n"), (p, "line count changed")
    ol, tl = o.split("\n"), t.split("\n")
    for i, (a, b) in enumerate(zip(ol, tl)):
        assert ID.findall(a) == ID.findall(b), (p, i)
        assert a.count("–") == b.count("–"), (p, i, "dash count changed")
    assert unicodedata.normalize("NFC", t) == t, (p, "not NFC")
    for s in OLD_GONE:
        if s in t:
            problems.append(f"old string left: {p}: «{s}» x{t.count(s)}")
    for s in BAD:
        if t.count(s) > o.count(s) or (s != "là là" and s in t):
            problems.append(f"bad string: {p}: {s!r} x{t.count(s)} (before x{o.count(s)})")
seg181 = [s for s in texts["5-catukkapuggalapannatti"].split("\n\n") if s.rstrip().endswith("^4-181")][0]
assert "người ấy" not in seg181
assert all(texts[p].count("ngay trong đời này") == orig[p].count("ngay trong đời này") for p in PARTS)
assert all(texts[p].count("Ở đời này, có người") + texts[p].count("ở đời này, có người")
           == orig[p].count("Ở đời này, có người") + orig[p].count("ở đời này, có người")
           - (4 if p == "5-catukkapuggalapannatti" else 0) for p in PARTS)  # only the 4 ^4-166 lines lose it

# ------------------------------------------------------------------ changed lines per chapter / decision
per_ch = collections.Counter()
per_dec = collections.defaultdict(set)
for p in PARTS:
    ol, tl = orig[p].split("\n"), texts[p].split("\n")
    for i, (a, b) in enumerate(zip(ol, tl)):
        if a != b:
            per_ch[p] += 1
            assert touched[(p, i)], (p, i)
for (p, i), decs in touched.items():
    for d in decs:
        per_dec[d].add((p, i))

# ------------------------------------------------------------------ write
if "--dry" not in sys.argv:
    for p in PARTS:
        if texts[p] != (VDIR / f"{p}.md").read_text(encoding="utf-8"):
            (VDIR / f"{p}.md").write_text(texts[p], encoding="utf-8", newline="\n")
    (RAILS / "review-fixes-log.tsv").write_text(
        "file\tblock\told\tnew\tdecision\tn\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")

print("rules", len(R), "occurrences", sum(hits.values()), "log rows", len(log))
print("changed lines per chapter:", dict(per_ch), "total", sum(per_ch.values()))
print("changed lines per decision:", {d: len(v) for d, v in sorted(per_dec.items(), key=lambda kv: int(kv[0]))})
print("problems:", problems or "none")

# ------------------------------------------------------------------ stale builder / formula strings
STALE = ["sự đi vào Giáo Pháp cao quý", "đích ở đời này", "rời khỏi đời này", "xung quanh", "cũng sẽ",
         "nghiêng về phía điều", "Con người", "một người có mắt", "vạt áo của một người", "ngược dòng đi đến",
         "Giáo Pháp làm thước đo", "nơi Giáo Pháp", "thấy có điều đáng khen", "sự toàn tri, và sự làm chủ",
         "chưa bị thiêu hủy", "với không hình sắc", "Giáo Pháp do Như Lai", "Kể từ chư thiên", "nằm sẵn",
         "các vị Phật", "thức uống và đồ ăn", "đến lần thứ ba", "Vì trước đây", "nhỏ nhặt", "cấu tạo câu chữ",
         "thì khỏi bệnh ấy", "thì bước vào sự cố định", "tràn vào người ấy"]
SRC = ["build_rails_sample_vi.py"] + [f"build_rails_{n}_vi.py" for n in range(3, 12)] + ["vi-rails-formulas.md"] \
      + [f"notes-rails-{n}.md" for n in range(3, 12)]
stale = []
for f in SRC:
    fp = RAILS / f
    if not fp.exists():
        continue
    for ln, line in enumerate(fp.read_text(encoding="utf-8").split("\n"), 1):
        for s in STALE:
            if s in line:
                stale.append(f"- {f}:{ln}: «{s}»")
print("stale builder / formula lines:", len(stale))
NOTES = RAILS / "review-fixes-notes.md"
MARK = "<!-- generated by review_fixes_vi.py below this line -->"
head = NOTES.read_text(encoding="utf-8").split(MARK)[0] if NOTES.exists() else "# pi-4 Vietnamese rails: review fixes, notes\n\n"
if "--dry" not in sys.argv:
    NOTES.write_text(head.rstrip("\n") + "\n\n" + MARK + "\n\n## Stale builder / formula strings (not rebuilt; "
                     "update before any rebuild)\n\n" + "\n".join(stale) + "\n", encoding="utf-8", newline="\n")
