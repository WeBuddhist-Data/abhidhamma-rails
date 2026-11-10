"""Re-upload the pi-4 English translation in place on prod (same edition_id), "outline" -> "matrix" (2026-11-10).

usage: python -I -X utf8 reupload_pi4_english.py dry|apply
  0. back up live content, segments, TOC and alignment pairs to 0-INBOX/pi-4-english-backup-2026-11-10/;
     pre-check: live content == the committed parser output (git HEAD); no other span annotations
  1. delete the alignment translation -> root (backed up; re-put in step 5)
  2. delete the TOC(s) and the segmentation
  3. replace the whole content, post the new segmentation and TOC
  4. verify content, segments (reference, type, lines) and one TOC; write the new toc_id into the track file
  5. put the alignment from the rebuilt alignment.json and verify every pair by reference
No segment-id map (user, 2026-11-10). Stops at the first failed call.
"""
import json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7")
from libapi import call, get_all  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
MODE = sys.argv[1]
assert MODE in ("dry", "apply")
REPO = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
GIT = r"C:\Users\Uzumaki Sither\AppData\Local\GitHubDesktop\app-3.6.10\resources\app\git\cmd\git.exe"
EID, ROOT = "E9ox1ON9xZVrrjoaE5sHJ", "4bCOP5KnJqlcTxSBZXYA3"
NAME = "pi-4-english-plain"
OUT = REPO / f"4-SYSTEM/scripts/parser-root-text/output/{NAME}"
MD = REPO / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-4-english-plain.md"
BK = REPO / "0-INBOX/pi-4-english-backup-2026-11-10"
ed = json.load(open(OUT / f"{NAME}.edition.json", encoding="utf-8"))
toc_local = json.load(open(OUT / f"{NAME}.toc.json", encoding="utf-8"))
al = json.load(open(OUT / f"{NAME}.alignment.json", encoding="utf-8"))["alignments"]
r = subprocess.run([GIT, "show", f"HEAD:4-SYSTEM/scripts/parser-root-text/output/{NAME}/{NAME}.edition.json"],
                   cwd=REPO, capture_output=True)
committed = json.loads(r.stdout.decode("utf-8"))["content"]


def must(st, body, what, ok=(200, 201, 204)):
    print(f"   {what}: {st}")
    if st not in ok:
        raise SystemExit(f"STOP: {what} failed: {st} {str(body)[:600]}")
    return body


def write(method, path, payload=None, what=""):
    if MODE == "dry":
        size = len(json.dumps(payload, ensure_ascii=False)) if payload is not None else 0
        print(f"   [dry] {method} {path} ({size} bytes) — {what}")
        return {}
    st, body = call(method, path, payload)
    return must(st, body, f"{method} {path} — {what}")


def text_of(x):
    return x if isinstance(x, str) else x.get("content")


print(f"== {NAME} ({EID}) — {MODE}")
# 0. backup + pre-checks
st, live = call("GET", f"/v2/editions/{EID}/content")
must(st, live, "GET content", ok=(200,))
live_text = text_of(live)
st, live_segs = get_all(f"/v2/editions/{EID}/segmentation/segments", limit=500)
must(st, live_segs, "GET segments", ok=(200,))
st, tocs = call("GET", f"/v2/editions/{EID}/table-of-contents")
must(st, tocs, "GET toc", ok=(200,))
st, pairs = get_all(f"/v2/editions/{EID}/alignments/{ROOT}", limit=500)
must(st, pairs, "GET alignment pairs", ok=(200,))
BK.mkdir(parents=True, exist_ok=True)
for fname, data in (("content.json", live), ("segments.json", live_segs), ("toc.json", tocs), ("alignment.json", pairs)):
    p = BK / fname
    if not p.exists():  # keep the first (pre-change) backup on re-runs
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"   backup in {BK.relative_to(REPO)}: {len(live_segs)} segments, {len(tocs)} TOC, {len(pairs)} alignment pairs")
already = live_text == ed["content"]
print(f"   live content == committed output: {live_text == committed}; == new output: {already}")
if not (live_text == committed or already):
    raise SystemExit("STOP: live content differs from both the committed and the new output")
for kind in ("pagination", "bibliographic", "durchens", "yigchungs"):
    st, ann = call("GET", f"/v2/editions/{EID}/{kind}")
    n = len(ann) if isinstance(ann, list) else (len(ann.get("items", [])) if isinstance(ann, dict) else "?")
    if st == 200 and n not in (0, "?"):
        raise SystemExit(f"STOP: edition has {n} {kind} annotation(s)")
toc_ids = [t["id"] for t in tocs] if isinstance(tocs, list) else []

new_toc_id = toc_ids[0] if toc_ids else None
if not already:
    # 1. alignment out
    if pairs:
        write("DELETE", f"/v2/editions/{EID}/alignments/{ROOT}", None, f"old alignment ({len(pairs)} pairs, backed up)")
    # 2. TOC + segmentation out
    for t in toc_ids:
        write("DELETE", f"/v2/table-of-contents/{t}", None, "old TOC")
    if live_segs:
        write("DELETE", f"/v2/editions/{EID}/segmentation", None, "old segmentation")
    # 3. content, segmentation, TOC in
    write("PATCH", f"/v2/editions/{EID}/content",
          {"type": "replace", "start": 0, "end": len(live_text), "text": ed["content"]}, "replace whole content")
    seg_payload = {"segments": [{"lines": s["lines"], "type": s["type"], "reference": s["reference"]}
                                for s in ed["segmentation"]["segments"]]}
    write("POST", f"/v2/editions/{EID}/segmentation", seg_payload, f"new segmentation ({len(seg_payload['segments'])})")
    body = write("POST", f"/v2/editions/{EID}/table-of-contents", {"sections": toc_local["sections"]}, "new TOC")
    new_toc_id = body.get("id") if isinstance(body, dict) else None
else:
    print("   content already new; content/TOC/segmentation steps skipped")

if MODE == "dry":
    print(f"   [dry] PUT /v2/editions/{EID}/alignments/{ROOT} ({len(al)} pairs)")
    print("   dry run done")
    sys.exit()

# 4. verify + toc_id
st, live = call("GET", f"/v2/editions/{EID}/content")
lt = text_of(live)
st, ns = get_all(f"/v2/editions/{EID}/segmentation/segments", limit=500)
loc = [(s["reference"], s["type"], s["lines"]) for s in ed["segmentation"]["segments"]]
liv = [(s.get("reference"), s.get("type"), s["lines"]) for s in ns]
st, tocs = call("GET", f"/v2/editions/{EID}/table-of-contents")
toc_ok = isinstance(tocs, list) and len(tocs) == 1
new_toc_id = tocs[0]["id"] if toc_ok else new_toc_id
print(f"   VERIFY content == local: {lt == ed['content']}; segments == local: {liv == loc} ({len(ns)}); one TOC: {toc_ok} ({new_toc_id})")
if not (lt == ed["content"] and liv == loc and toc_ok):
    raise SystemExit("STOP: verification failed")
t = MD.read_bytes().decode("utf-8")
t2, n = re.subn(r"(?m)^toc_id:[ \t]*\S+", f"toc_id: {new_toc_id}", t, count=1)
if n and t2 != t:
    MD.write_bytes(t2.encode("utf-8"))
print(f"   frontmatter toc_id -> {new_toc_id} ({'updated' if n else 'NO toc_id line'})")

# 5. alignment back
st, cur = call("GET", f"/v2/editions/{EID}/alignments/{ROOT}?offset=0&limit=1")
if isinstance(cur, dict) and cur.get("items"):
    write("DELETE", f"/v2/editions/{EID}/alignments/{ROOT}", None, "stale alignment")
write("PUT", f"/v2/editions/{EID}/alignments/{ROOT}", {"alignments": al}, f"alignment {len(al)} pairs")
st, items = get_all(f"/v2/editions/{EID}/alignments/{ROOT}", limit=500)
got = sorted((x["source_segment"]["reference"], x["target_segment"]["reference"]) for x in items)
want = sorted((a["source_segment_reference"], a["target_segment_reference"]) for a in al)
print(f"   VERIFY alignment pairs == local: {got == want} ({len(got)})")
if got != want:
    raise SystemExit("STOP: alignment verification failed")
print("   done")
