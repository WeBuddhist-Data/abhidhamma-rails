"""Read-only: do the pi-3/4/5 root and English translation editions exist on prod, and are the translations aligned?"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7")
from libapi import call  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
ROOTS = {"pi-3": "ygJ9vnhenIaGvUeIfRJ9i", "pi-4": "4bCOP5KnJqlcTxSBZXYA3", "pi-5": "WjnE60LMIzQETFlXoh9Hd"}
EN = {"pi-3": "HLezWU6MhI6FdaGdncgBK", "pi-4": "E9ox1ON9xZVrrjoaE5sHJ", "pi-5": "ugA2G8F1Y9tyebgiDuZ1h"}
for book in ROOTS:
    for kind, eid in (("root", ROOTS[book]), ("english", EN[book])):
        st, meta = call("GET", f"/v2/editions/{eid}")
        title = meta.get("title") if isinstance(meta, dict) else None
        line = f"{book} {kind:8} {eid} -> {st} {title!r}"
        if kind == "english" and st == 200:
            st2, al = call("GET", f"/v2/editions/{eid}/alignments")
            ids = [a.get("id") or a.get("edition_id") for a in al] if isinstance(al, list) else al
            line += f" | aligned-with {st2} {ids}"
        print(line)
