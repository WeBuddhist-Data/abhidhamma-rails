"""Convert a Vietnamese Tịnh Sự Abhidhamma PDF (Word export) to plain markdown (no block IDs).

Usage: convert_vi.py <pdf> <out.md> <diagnostics.txt> [--keep-footnotes] [--start-page N]

Formatting only: title page, table of contents, running headers and page numbers are dropped;
wrapped lines are re-joined into paragraphs; headings are marked; bullet glyphs become list
items. Translator footnotes are dropped (user decision 2026-11-17: the Vietnamese is a
verification reference only), both the note text at the foot of the page and the marker digits
glued to the word they annotate; --keep-footnotes keeps them (for the raw copy).
"""
import re
import sys
import unicodedata

import pypdf

sys.stdout.reconfigure(encoding="utf-8")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
pdf_path, out_path, diag_path = args[:3]
KEEP_FN = "--keep-footnotes" in sys.argv
START = None
if "--start-page" in sys.argv:
    START = int(sys.argv[sys.argv.index("--start-page") + 1])
    args = [a for a in args if a != str(START)]
reader = pypdf.PdfReader(pdf_path)
pages = [(p.extract_text() or "") for p in reader.pages]
diag = {"pages": len(pages)}


def bump(key, n=1):
    diag[key] = diag.get(key, 0) + n


# ---------------------------------------------------------------- syllable repair
def base(ch):
    return unicodedata.normalize("NFD", ch)[0].lower()


VOWELS = set("aeiouy")


def vi_fix_syllables(s):
    """Re-join syllables split by the extractor ("x ứ" -> "xứ"): a vowel-less letter run of
    1-3 characters can never be a Vietnamese syllable on its own."""
    toks = s.split(" ")
    res, i = [], 0
    while i < len(toks):
        t = toks[i]
        if (i + 1 < len(toks) and 1 <= len(t) <= 3 and t.isalpha() and all(base(c) not in VOWELS for c in t)
                and toks[i + 1][:1].isalpha() and toks[i + 1][:1].islower() and base(toks[i + 1][0]) in VOWELS):
            res.append(t + toks[i + 1])
            bump("split_syllables_rejoined")
            i += 2
            continue
        res.append(t)
        i += 1
    return " ".join(res)


# ---------------------------------------------------------------- page cleaning
HEADER = re.compile(r"^\s*(\d+\s+)?(Việt [dD]ịch|Tạng Vô Tỷ Pháp|Tạng Diệu Pháp)|^\s*\d+\s*$", re.I)
MARKER = re.compile(r"(?<=[^\W\d_\s])(\d{1,2})(?=[\s,.;:!?)\]\"”']|$)")
fn_next = [1]  # number of the next translator footnote


def clean_page(text):
    # NFC: some PDFs give decomposed Vietnamese letters ("PHẦN"), which defeats the patterns
    ls = [unicodedata.normalize("NFC", ln) for ln in text.splitlines()]
    while ls and not ls[0].strip():
        ls = ls[1:]
    # running header (and a page number on its own line) at the top
    while ls and HEADER.match(ls[0]):
        ls = ls[1:]
        bump("page_headers_removed")
    if KEEP_FN:
        return ls
    # footnotes: markers glued to a word in the body, notes "N text" at the foot of the page
    marks = set()
    for ln in ls:
        for m in MARKER.finditer(ln):
            marks.add(m.group(1))
    # footnotes are numbered in sequence through the book: the next number is a note too,
    # even when its marker is not glued to a word on this page
    marks.add(str(fn_next[0]))
    cut = None
    for k in range(len(ls) - 1, max(-1, len(ls) - 15), -1):
        m = re.match(r"^\s*(\d{1,2})\s+[^\W\d_]", ls[k])
        if m and m.group(1) in marks and (k == 0 or not ls[k - 1].strip() or k > len(ls) - 6):
            cut = k
    if cut is not None:
        nums = [int(x) for x in re.findall(r"(?:^|\s)(\d{1,2})\s+[^\W\d_]", " ".join(ls[cut:]))]
        fn_next[0] = max([fn_next[0] - 1] + [n for n in nums if n < fn_next[0] + 5]) + 1
        bump("footnote_lines_removed", len(ls) - cut)
        ls = ls[:cut]
    out = []
    for ln in ls:
        new, n = MARKER.subn("", ln)
        bump("footnote_markers_removed", n)
        out.append(new)
    return out


# ---------------------------------------------------------------- structure
VI_HEAD = [
    (re.compile(r"^PHẦN [IVXL]+(\s*[-–.:]|\s+[A-ZĐÀ-Ỹ]|\s*$)"), 2),  # "PHẦN I - UẨN …", "PHẦN I XIỂN MINH …", "PHẦN I"
    (re.compile(r"^(ĐẠI )?PHẨM THỨ [A-ZĐÀ-Ỹ ]+$"), 2),  # Kathāvatthu vaggas: "PHẨM THỨ HAI"
    (re.compile(r"^[A-H]\.\s+\S"), 3),  # "A. UẨN PHÂN TÍCH PHẦN PHÂN THEO KINH"
    (re.compile(r"^(Xiển minh|Đầu đề) phần \S+$"), 4),  # Puggalapaññatti: "Xiển minh phần tam"
    (re.compile(r"^Phần [A-Z]\.", re.I), 2),
    (re.compile(r"^[IVX]+\.\s"), 3),
    (re.compile(r"^\d+\.\d+\)\s"), 5),
    (re.compile(r"^\d+\)\s"), 4),
    (re.compile(r"^[a-zđ]\)\s"), 6),
]
NUM_LINE = re.compile(r"^\d{1,4}\.?$")  # the source occasionally drops the dot (e.g. "806")


def vi_heading_level(s):
    for rx, lvl in VI_HEAD:
        if rx.match(s):
            return lvl
    return None


def convert():
    # The body starts at the homage: "NAMO TASSA …" (Pāli) or, in books without it, the
    # Vietnamese "CUNG KÍNH ĐỨC THẾ TÔN …"; lines before it on that page (book title) are dropped.
    if START is not None:
        start = START
    else:
        start = next((i for i, t in enumerate(pages) if "NAMO TASSA" in t.upper()), None)
        if start is None:
            start = next(i for i, t in enumerate(pages) if i > 1 and "CUNG K" in t.upper() and "THẾ TÔN" in t.upper())
    diag["front_pages_skipped"] = start
    lines = []
    for n, text in enumerate(pages[start:]):
        pl = clean_page(text)
        if n == 0:
            k = next((j for j, ln in enumerate(pl) if "NAMO TASSA" in ln.upper() or ("CUNG K" in ln.upper() and "THẾ TÔN" in ln.upper())), 0)
            diag["title_lines_dropped"] = k
            pl = pl[k:]
        lines.extend(pl)
        lines.append("\x00PAGE")  # page boundary: never a paragraph break by itself

    out, para, pending_num = [], None, None
    last_num = [0]  # last paragraph number seen

    def flush():
        nonlocal para
        if para is not None:
            out.append(para)
            para = None

    def nxt_meaningful(i):
        for j in range(i + 1, len(lines)):
            if lines[j] != "\x00PAGE" and lines[j].strip():
                return lines[j].strip()
        return ""

    for i, raw in enumerate(lines):
        if raw == "\x00PAGE":
            continue
        s = raw.strip()
        if not s:
            flush()
            continue
        if all(0xE000 <= ord(c) <= 0xF8FF or c.isspace() for c in s):
            # a row of symbol-font glyphs (e.g. U+F068 x 3): a decorative separator
            flush()
            out.append(("hr",))
            bump("glyph_separators")
            continue
        bullet = 0xE000 <= ord(s[0]) <= 0xF8FF or (s[0] in "•▪●-–" and not re.fullmatch(r"[-~–]+", s))
        body = vi_fix_syllables(re.sub(r"\s+", " ", s[1:].strip() if bullet else s))
        if re.fullmatch(r"[-~]{2,}", s):
            flush()
            out.append(("hr",))
            continue
        if NUM_LINE.match(s):
            flush()
            pending_num = s
            n_ = int(s.rstrip("."))
            if last_num[0] < n_ <= last_num[0] + 6:
                last_num[0] = n_
            elif n_ == 1:
                last_num[0] = 1  # numbering restarts (second book in the volume)
            continue
        if bullet:
            flush()
            if pending_num:
                out.append(("p", pending_num))
                pending_num = None
            para = ("li", body)
            bump("list_items")
            continue
        lvl = vi_heading_level(s)
        if lvl and s.rstrip().endswith("?"):
            lvl = None  # "2) Thọ uẩn đó ra sao?": a numbered question, not a heading
        if (para is None and out and out[-1][0] == "h" and re.fullmatch(r"PHẦN [IVXL]+", out[-1][2])
                and body.upper() == body and len(body) < 90):
            # "PHẦN I" on one line, its title "XIỂN MINH CÂU …" (capitals) on the next
            out[-1] = ("h", out[-1][1], out[-1][2] + " " + body)
            bump("chapter_titles_joined")
            continue
        if (para is None and out and out[-1][0] == "h" and out[-1][2].startswith("Xiển minh phần")
                and re.fullmatch(r"\S+ chủng nhân", body)):
            # "Xiển minh phần tam" / "Tam chủng nhân" (three kinds of persons): one heading
            out[-1] = ("h", out[-1][1], out[-1][2] + " " + body)
            bump("heading_subtitles_joined")
            continue
        if para is None and out and out[-1][0] == "h" and re.fullmatch(r"\([^()]{3,60}\)", body):
            # "(Dhātuvibhaṅga)" printed under a chapter heading: part of that heading
            out[-1] = ("h", out[-1][1], out[-1][2] + " " + body)
            bump("heading_subtitles_joined")
            continue
        if re.match(r"^(Đầy đủ|Hoàn bị|Hoàn thành|Hoàn tất|Dứt|Hết [Pp]hẩm|Rồi [Pp]hẩm|Mùa an cư)", body):
            # chapter end lines ("Đầy đủ Uẩn phân tích") and the translator's dating line: text
            flush()
            out.append(("p", body))
            bump("end_lines")
            continue
        if lvl == 2 and para is not None and len(s) < 90 and pending_num is None:
            # a chapter title ("PHẦN I XIỂN MINH …") printed right under a line of text, with
            # no blank line between: it still starts a heading
            flush()
            bump("chapter_titles_after_text")
        starts_block = para is None
        if lvl is None and starts_block and len(s) < 70 and not s.startswith("Dứt") and not re.search(r"[.?!:,;]$", s):
            n = nxt_meaningful(i)
            if NUM_LINE.match(n) or vi_heading_level(n):
                lvl = 4
        if lvl and starts_block and len(s) < 90 and pending_num is None:
            out.append(("h", lvl, body))
            bump("headings")
            continue
        if s.startswith("Dứt "):
            flush()
            out.append(("p", body))
            continue
        mnum = re.match(r"^(\d{1,4})\.\s+\S", s)
        if para is not None and mnum and last_num[0] < int(mnum.group(1)) <= last_num[0] + 3:
            # the next paragraph number at the start of a line opens a new paragraph, even with
            # no blank line before it (vi-3: "2. Sắc uẩn …" followed directly by "3. …")
            flush()
            bump("numbered_paragraph_breaks")
        if mnum and last_num[0] < int(mnum.group(1)) <= last_num[0] + 3:
            last_num[0] = int(mnum.group(1))
        if para is None:
            text = f"{pending_num} {body}" if pending_num else body
            pending_num = None
            para = ("p", text)
        else:
            para = (para[0], para[1] + " " + body)
            bump("line_joins")
    flush()
    if pending_num:
        out.append(("p", pending_num))
    return out


def render(blocks):
    md = []
    for b in blocks:
        if b[0] == "h":
            md.append("#" * b[1] + " " + b[2])
        elif b[0] == "p":
            md.append(b[1])
        elif b[0] == "li":
            if md and md[-1].startswith("- "):
                md[-1] += "\n- " + b[1]
                continue
            md.append("- " + b[1])
        elif b[0] == "hr":
            md.append("---")
    return "\n\n".join(md) + "\n"


body = render(convert())
open(out_path, "w", encoding="utf-8", newline="\n").write(body)
diag["output_chars"] = len(body)
open(diag_path, "w", encoding="utf-8").write("".join(f"{k}: {v}\n" for k, v in diag.items()))
print(diag)
