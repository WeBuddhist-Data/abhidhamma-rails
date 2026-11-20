import sys
# usage: r6_grep.py <which> <substring> [maxhits] [context_chars]
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
FILES = {
    "pi1v": ROOT + r"\AI_translation\vietnamese\pi-1-vietnamese-plain.md",
    "pi1p": ROOT + r"\AI_translation\pali\pi-1.md",
    "v": ROOT + r"\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\17-khuddakavatthuvibhango.md",
    "p": ROOT + r"\AI_translation\pali\pi-2_split_chapters\17-khuddakavatthuvibhango.md",
    "en": ROOT + r"\AI_translation\english\pi-2-english-plain-rails_split_chapters\17-khuddakavatthuvibhango.md",
    "ru": ROOT + r"\AI_translation\russian\pi-2-russian-plain-rails_split_chapters\17-khuddakavatthuvibhango.md",
    "att": ROOT + r"\1-SOURCES\Commentaries\pi-vibhanga-atthakatha.md",
    "ts": ROOT + r"\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md",
}
which, sub = sys.argv[1], sys.argv[2]
maxh = int(sys.argv[3]) if len(sys.argv) > 3 else 5
ctx = int(sys.argv[4]) if len(sys.argv) > 4 else 0
n = 0
with open(FILES[which], encoding="utf-8") as f:
    for i, l in enumerate(f, 1):
        if sub in l:
            l = l.rstrip("\n")
            if ctx:
                k = l.find(sub)
                l = l[max(0, k - ctx):k + len(sub) + ctx]
            print(f"{i}: {l}")
            n += 1
            if n >= maxh:
                break
