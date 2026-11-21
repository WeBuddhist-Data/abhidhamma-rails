"""Coordinator cross-part alignment after the five review-fix parts (2026-11-22).

Identical Pāli must read identically. Two fixes were applied in one part but the same Pāli also occurs in another:
- dānaṃ … dukkhudrayaṃ dukkhavipākaṃ / sukhudrayaṃ sukhavipākaṃ: ch10 (r2 minor fix) «đưa đến khổ đau, có quả trổ là khổ đau» /
  «đưa đến hạnh phúc, có quả trổ là hạnh phúc"; ch15 still had the feeling words.
- "… tasmā sataṃ dhammo asabbhi ārakā": ch18 / ch21 (r4 minor fix) «giáo pháp của người hiền thiện ở xa kẻ không hiền thiện»;
  ch15 ^5-491 and ch27 ^5-830 still had «bản chất».
Applied to the current files (after the part scripts), with asserted counts; pre-fix copies in rails/backup-pre-coord/;
log rails/review-fixes-log-coord.tsv. Re-runnable: it builds from backup-pre-coord/.
"""
import pathlib, re, shutil

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
V = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
D = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails"
B = D / "backup-pre-coord"
B.mkdir(exist_ok=True)

RULES = {
    "15-sattamavaggo.md": [
        ("đưa đến sự khó chịu, có quả trổ khó chịu", "đưa đến khổ đau, có quả trổ là khổ đau", None, "align ch10 (dukkhudraya)"),
        ("đưa đến sự dễ chịu, có quả trổ dễ chịu", "đưa đến hạnh phúc, có quả trổ là hạnh phúc", None, "align ch10 (sukhudraya)"),
        ("bản chất của người hiền thiện ở xa kẻ không hiền thiện", "giáo pháp của người hiền thiện ở xa kẻ không hiền thiện", 1, "align ch18 / ch21 (sataṃ dhammo asabbhi ārakā)"),
        ("thuộc về cõi trời, có quả trổ dễ chịu", "thuộc về cõi trời, có quả trổ là hạnh phúc", 4, "user 2026-11-22 «Yes, align them»: merit formula sukhavipāka (bare) = the udraya formula"),
        ("bản chất của người hiền thiện và bản chất của kẻ không hiền thiện", "giáo pháp của người hiền thiện và giáo pháp của kẻ không hiền thiện", 2, "user 2026-11-22: AN 4.47 satañca dhammo asatañca dhammo «giáo pháp» in the whole sutta (commentary: bodhipakkhiya / 62 views)"),
    ],
    "10-dutiyavaggo.md": [
        ("Chẳng phải “cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15],” Đức Thế Tôn đã nói, “tất cả các tạo tác đều vô thường” [Kinh Pháp Cú 277; Trung Bộ Kinh 1.356] sao?",
         "Chẳng phải Đức Thế Tôn đã nói rằng “cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15],” và đã nói “tất cả các tạo tác đều vô thường” [Kinh Pháp Cú 277; Trung Bộ Kinh 1.356] sao?",
         1, "user 2026-11-22: A6 wording at ^5-338 (quotes kept as the Pāli has them)"),
        ("Nếu “cái gì vô thường thì cái ấy là khổ đau,” Đức Thế Tôn đã nói, “tất cả các tạo tác đều vô thường,” thì",
         "Nếu Đức Thế Tôn đã nói rằng “cái gì vô thường thì cái ấy là khổ đau,” và đã nói “tất cả các tạo tác đều vô thường,” thì",
         1, "user 2026-11-22: A6 wording at ^5-338 (Hañci clause)"),
    ],
    "1-puggalakatha.md": [
        ("đưa đến sự khó chịu, có quả trổ khó chịu", "đưa đến khổ đau, có quả trổ là khổ đau", None, "user 2026-11-22 «Yes, align them»: sample, dukkhudraya dukkhavipāka (kamma) = ch10 / ch15 / ch16"),
        ("đưa đến sự dễ chịu, có quả trổ dễ chịu", "đưa đến hạnh phúc, có quả trổ là hạnh phúc", None, "user 2026-11-22 «Yes, align them»: sample, sukhudraya sukhavipāka (kamma) = ch10 / ch15 / ch16"),
    ],
    "19-ekadasamavaggo.md": [
        ("có quả trổ khó chịu", "có quả trổ là khổ đau", 1, "user 2026-11-22 «Yes, align them»: dukkhavipāka (bare) = the udraya formula"),
    ],
    "16-atthamavaggo.md": [
        ("đưa đến sự khó chịu, có quả trổ khó chịu", "đưa đến khổ đau, có quả trổ là khổ đau", 3, "align ch10 / ch15 (dukkhudrayaṃ dukkhavipākaṃ, AN 10 kamma sutta; found by the termbase alignment)"),
        ("đưa đến sự dễ chịu, có quả trổ dễ chịu", "đưa đến hạnh phúc, có quả trổ là hạnh phúc", 3, "align ch10 / ch15 (sukhudrayaṃ sukhavipākaṃ)"),
    ],
    "27-ekunavisatimavaggo.md": [
        ("bản chất của người hiền thiện ở xa kẻ không hiền thiện", "giáo pháp của người hiền thiện ở xa kẻ không hiền thiện", 1, "align ch18 / ch21 (sataṃ dhammo asabbhi ārakā)"),
    ],
}

log = []
for fn, rules in RULES.items():
    bak = B / fn
    if not bak.exists():
        shutil.copyfile(V / fn, bak)
    lines = bak.read_text(encoding="utf-8").split("\n")
    for old, new, want, why in rules:
        n = 0
        for i, l in enumerate(lines):
            c = l.count(old)
            if c:
                n += c
                lines[i] = l.replace(old, new)
                sid = re.search(r"\^([0-9A-Za-z-]+)\s*$", l)
                log.append(f"{fn}\t{sid.group(1) if sid else 'L' + str(i + 1)}\t{old} -> {new}\t{why}")
        assert n > 0 and (want is None or n == want), (fn, old, n)
        print(fn, "|", old[:40], "->", n)
    out = "\n".join(lines)
    (V / fn).write_text(out, encoding="utf-8", newline="\n")
(D / "review-fixes-log-coord.tsv").write_text("\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("log rows", len(log))
