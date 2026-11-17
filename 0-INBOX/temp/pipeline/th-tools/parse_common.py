"""Shared parsing for the pi-1 alignment: root blocks and translation draft items."""
import re

ID_RE = re.compile(r"\s\^([\w-]+)\s*$")


def parse_root(path):
    """Return the ordered root blocks: dicts with id, kind ('h' or 't'), level, text."""
    text = open(path, encoding="utf-8").read()
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    blocks, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = ID_RE.search(" " + line)
        if line.startswith("#") and m:
            level = len(line) - len(line.lstrip("#"))
            blocks.append({"id": m.group(1), "kind": "h", "level": level,
                           "text": ID_RE.sub("", " " + line).strip().lstrip("#").strip()})
            buf = []
            continue
        buf.append(line)
        if m:
            body = "\n".join(buf)
            body = ID_RE.sub("", " " + body).strip()
            blocks.append({"id": m.group(1), "kind": "t", "level": 0, "text": body})
            buf = []
    return blocks


def parse_draft(path):
    """Return the ordered draft items: dicts with kind ('h', 'p', 'table', 'hr', 'li'), level, text."""
    text = open(path, encoding="utf-8").read()
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    items = []
    for chunk in re.split(r"\n\s*\n", text.strip()):
        chunk = chunk.strip("\n")
        if not chunk.strip():
            continue
        if chunk.strip() == "---" or re.fullmatch(r"#*\s*\**[_\-—=―‗‾\s]{4,}\**\s*", chunk.strip()):
            items.append({"kind": "hr", "level": 0, "text": "---"})  # separator line
        elif chunk.startswith("#"):
            level = len(chunk) - len(chunk.lstrip("#"))
            items.append({"kind": "h", "level": level, "text": chunk.lstrip("#").strip()})
        elif chunk.startswith("|"):
            items.append({"kind": "table", "level": 0, "text": chunk})
        elif chunk.startswith("- "):
            for li in chunk.split("\n- "):
                items.append({"kind": "li", "level": 0, "text": li[2:] if li.startswith("- ") else li})
        else:
            items.append({"kind": "p", "level": 0, "text": chunk})
    return items
