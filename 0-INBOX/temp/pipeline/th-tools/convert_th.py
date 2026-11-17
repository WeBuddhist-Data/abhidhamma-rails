"""Convert the Thai and Vietnamese Dhammasangani PDFs to plain markdown (no block IDs).

Usage: convert_pi1.py <th|vi> <pdf> <out.md> <diagnostics.txt>

Formatting only: page headers, page numbers and the Vietnamese table of contents
are dropped; wrapped lines are re-joined into paragraphs; headings are marked;
the Thai two-column Pali/Thai matrix lines become markdown tables. The wording
of the translation is not changed, apart from the mechanical extraction fixes
listed in the diagnostics file (legacy Thai glyphs, stray spaces inside words).
"""
import os
import re
import sys
import unicodedata

import pypdf

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(__file__))
from thai_pua import fix as fix_pua  # noqa: E402

lang, pdf_path, out_path, diag_path = sys.argv[1:5]
KV_MODE = len(sys.argv) > 5 and sys.argv[5] == "kv"  # Kathavatthu layout
KV_HEAD = re.compile(r"(กถา|จตุกกะ|ปัญจกะ|นิคหะ|วรรค|วรรคที่\s*[๐-๙]+|สาธนะ|สังสันทนะ|ยุตติ|โสธนะ|ปัณณาสก์|วาร|จบ)\s*$")
reader = pypdf.PdfReader(pdf_path)
pages = [(p.extract_text() or "") for p in reader.pages]
diag = {"pages": len(pages)}


def bump(key, n=1):
    diag[key] = diag.get(key, 0) + n


# ---------------------------------------------------------------- Thai
THAI_MN = "ัิ-ฺ็-๎"


def thai_clean(s):
    s = fix_pua(s)
    s = s.replace("ํา", "ำ")  # nikhahit + sara aa -> sara am
    s, n = re.subn(rf" +(?=[{THAI_MN}])", "", s)  # stray space before a combining mark
    bump("th_space_before_mark_removed", n)
    return s


# Thai characters that cannot begin a word (dependent vowels and marks)
THAI_DEPENDENT = set("ะาำๅ") | {chr(c) for c in range(0x0E31, 0x0E3B)} | {chr(c) for c in range(0x0E47, 0x0E4F)}


def next_line(lines, idx):
    for ln in lines[idx + 1:]:
        if ln.strip():
            return ln
    return ""


def convert_th():
    out = []          # list of blocks: ("h", level, text) | ("p", text) | ("table", rows) | ("hr",)
    para = None       # current paragraph text
    para_raw_tail = ""  # raw ending of last joined line (to decide space or no space)
    table = None
    title_lines = []

    def flush():
        nonlocal para, table
        if para is not None:
            out.append(("p", para.strip()))
            para = None
        if table is not None:
            out.append(("table", table))
            table = None

    pending_left = ""
    for pno, text in enumerate(pages):
        lines = thai_clean(text).splitlines()
        if lines and lines[0].strip().startswith("พระอภิธรรมปิฎก เล่ม") and "หน้าที่" in lines[0]:
            lines = lines[1:]
            bump("th_page_headers_removed")
        for idx, raw in enumerate(lines):
            s = raw.strip()
            ind = len(raw) - len(raw.lstrip(" "))
            if not s:
                flush()
                continue
            # Book title block on the first page (three centred lines before the homage)
            if pno == 0 and ind >= 12 and len(title_lines) < 3 and not out and para is None:
                title_lines.append(s)
                continue
            if re.fullmatch(r"-{3,}", s):
                flush()
                out.append(("hr",))
                continue
            m = re.match(r"^(\[[๐-๙]+\])\s{3,}(\S.{0,40})$", s)
            if m and (ind >= 5 or re.match(r"[๐-๙]+(-[๐-๙]+)?\. ", m.group(2))):  # "[๑]      ๑. กุสลติกะ": numbered heading
                flush()
                out.append(("h", 3, f"{m.group(1)} {re.sub(r'\s+', ' ', m.group(2))}"))
                bump("th_headings")
                continue
            if table is not None and ind >= 30 and not re.search(r"\S\s{4,}\S", s) and not re.match(r"[๐-๙]+(-[๐-๙]+)?\. ", s):
                table[-1][1] += s  # wrapped Thai cell, aligned under the right column
                bump("th_table_cell_wraps")
                continue
            # Centred lines that are text, not headings: the homage, a numbered paragraph
            # opening ("[๑] ขันธ์ ๕ คือ"), and the items of a list introduced by "… คือ"
            prev_text = (para if para is not None else (out[-1][1] if out and out[-1][0] == "p" else "")) or ""
            in_list = bool(re.search(r"คือ\s*$", prev_text)) or (out and out[-1][0] == "p" and out[-1][1].startswith("⁣"))
            if ind >= 12 and (s.startswith("ขอนอบน้อม") or re.match(r"^\[[๐-๙]+\]", s)
                              or (in_list and re.match(r"^[๐-๙]+\.\s", s))):
                flush()
                marker = "⁣" if (in_list and re.match(r"^[๐-๙]+\.\s", s)) else ""
                out.append(("p", marker + re.sub(r"\s+", " ", s)))
                bump("th_centred_text_lines")
                continue
            if ind >= 12 and KV_MODE:
                # Kathavatthu: the PDF indents wrapped dialogue lines far enough to look centred.
                # Dialogue lines (ส. / ป.) are text; inside an open paragraph, a centred line is a
                # continuation unless it is a short section name.
                head_like = (len(s) <= 40 and "?" not in s and KV_HEAD.search(s)) or re.match(r"^นิคหะ\s*ที่", s)
                if re.match(r"^[สป]\.\s", s):
                    flush()
                    para, para_raw_tail = s, raw
                    bump("kv_dialogue_lines")
                    continue
                if para is not None and not head_like:
                    joiner = " " if para_raw_tail.endswith(" ") or s.startswith("หรือ") else ""
                    para += joiner + re.sub(r"\s+", " ", s)
                    para_raw_tail = raw
                    bump("kv_continuations")
                    continue
            if ind >= 12:
                flush()
                if s.endswith(("จบ", "จบ.", ".")):  # end lines ("… จบ", "… อย่างนี้.") are text, not headings
                    out.append(("p", s))
                    bump("th_end_markers")
                else:
                    out.append(("h", 3, re.sub(r"\s+", " ", s)))
                    bump("th_headings")
                continue
            gap = re.search(r"\S(\s{4,})\S", s)
            if gap and ind < 12:  # two-column matrix line: Pali | Thai
                left = s[: gap.start(1)].strip()
                right = re.sub(r"\s+", " ", s[gap.end(1):].strip())
                if para is not None:
                    out.append(("p", para.strip()))
                    para = None
                if table is None:
                    table = []
                if pending_left:
                    left = pending_left + left  # Pali cell wrapped onto two lines
                    pending_left = ""
                    bump("th_table_left_wraps")
                table.append([re.sub(r"\s+", " ", left), right])
                bump("th_table_rows")
                continue
            if table is not None and ind == 0 and len(s) < 40:
                nxt = next_line(lines, idx)
                nxt_is_row = bool(re.search(r"\S\s{4,}\S", nxt.strip()))
                if s[0] in THAI_DEPENDENT or not nxt_is_row:
                    table[-1][1] += s  # wrapped Thai cell of the previous row
                    bump("th_table_cell_wraps")
                else:
                    pending_left = s  # head of the next row's Pali cell
                continue
            if table is not None:
                out.append(("table", table))
                table = None
            if ind >= 3 or para is None:
                if para is not None:
                    out.append(("p", para.strip()))
                para = s
            else:
                joiner = " " if para_raw_tail.endswith(" ") else ""
                para += joiner + s
                bump("th_line_joins")
            para_raw_tail = raw
    flush()
    return title_lines, out


# ---------------------------------------------------------------- Vietnamese
def base(ch):
    return unicodedata.normalize("NFD", ch)[0].lower()


VOWELS = set("aeiouy")


def vi_fix_syllables(s):
    """Re-join syllables that the extractor split ("x ứ" -> "xứ"): a vowel-less letter run
    of 1-3 characters can never be a Vietnamese syllable on its own."""
    toks = s.split(" ")
    res = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if (
            i + 1 < len(toks)
            and 1 <= len(t) <= 3
            and t.isalpha()
            and all(base(c) not in VOWELS for c in t)
            and toks[i + 1][:1].isalpha()
            and toks[i + 1][:1].islower()
            and base(toks[i + 1][0]) in VOWELS
        ):
            res.append(t + toks[i + 1])
            bump("vi_split_syllables_rejoined")
            i += 2
            continue
        res.append(t)
        i += 1
    return " ".join(res)


VI_HEAD = [
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


def convert_vi():
    # Body starts on the page with the homage (earlier pages: title page and table of contents)
    start = next(i for i, t in enumerate(pages) if "NAMO TASSA" in t)
    diag["vi_front_pages_skipped"] = start
    lines = []
    for text in pages[start:]:
        ls = text.splitlines()
        while ls and not ls[0].strip():
            ls = ls[1:]
        if ls and (re.match(r"^\s*(\d+\s+)?(Việt dịch|Tạng Vô Tỷ Pháp)", ls[0]) or re.fullmatch(r"\s*\d+\s*", ls[0])):
            ls = ls[1:]
            bump("vi_page_headers_removed")
        lines.extend(ls)
        lines.append("\x00PAGE")  # page boundary: never a paragraph break by itself

    out = []
    para = None
    pending_num = None

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
        bullet = 0xE000 <= ord(s[0]) <= 0xF8FF or s[0] in "•▪●-–"
        body = vi_fix_syllables(re.sub(r"\s+", " ", s[1:].strip() if bullet else s))
        if re.fullmatch(r"-{3,}|~{3,}", s):
            flush()
            out.append(("hr",))
            continue
        if NUM_LINE.match(s):
            flush()
            pending_num = s
            continue
        if bullet:
            flush()
            if pending_num:
                out.append(("p", pending_num))
                pending_num = None
            para = ("li", body)
            bump("vi_list_items")
            continue
        lvl = vi_heading_level(s)
        starts_block = para is None
        if lvl is None and starts_block and len(s) < 70 and not s.startswith("Dứt") and not re.search(r"[.?!:,;]$", s):
            n = nxt_meaningful(i)
            if NUM_LINE.match(n) or vi_heading_level(n):
                lvl = 4
        if lvl and starts_block and len(s) < 90 and pending_num is None:
            out.append(("h", lvl, body))
            bump("vi_headings")
            continue
        if s.startswith("Dứt "):
            flush()
            out.append(("p", body))
            continue
        if para is None:
            text = f"{pending_num} {body}" if pending_num else body
            pending_num = None
            para = ("p", text)
        else:
            para = (para[0], para[1] + " " + body)
            bump("vi_line_joins")
    flush()
    if pending_num:
        out.append(("p", pending_num))
    return out


# ---------------------------------------------------------------- render
def render(blocks):
    md = []
    for b in blocks:
        kind = b[0]
        if kind == "h":
            md.append("#" * b[1] + " " + b[2])
        elif kind == "p":
            md.append(b[1])
        elif kind == "li":
            # consecutive list items stay together (no blank line between)
            if md and md[-1].startswith("- "):
                md[-1] += "\n- " + b[1]
                continue
            md.append("- " + b[1])
        elif kind == "hr":
            md.append("---")
        elif kind == "table":
            rows = ["| Pāli | ไทย |", "|---|---|"] + [f"| {l} | {r} |" for l, r in b[1]]
            md.append("\n".join(rows))
    return "\n\n".join(md) + "\n"


if lang == "th":
    title, blocks = convert_th()
    body = "# " + " ".join(title) + "\n\n" + render(blocks)
    # A Thai word can never start with a dependent vowel or mark, so a space right before
    # one is an extraction or line-join artefact ("คว ามดำรง" -> "ความดำรง").
    body, n = re.subn(r"(?<=[ก-๎]) +(?=[ะาำๅัิ-ฺ็-๎])", "", body)
    bump("th_space_before_dependent_removed", n)
else:
    body = render(convert_vi())

body = body.replace("⁣", "")  # internal list-item marker used during conversion
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(body)
diag["output_chars"] = len(body)
with open(diag_path, "w", encoding="utf-8") as f:
    for k, v in diag.items():
        f.write(f"{k}: {v}\n")
print(diag)
