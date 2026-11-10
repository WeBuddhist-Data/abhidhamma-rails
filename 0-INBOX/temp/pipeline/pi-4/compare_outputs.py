"""Compare the rebuilt pi-4 English parser outputs with the committed (git HEAD) ones."""
import json, subprocess, sys, difflib
sys.stdout.reconfigure(encoding="utf-8")
REPO = r"D:\Work\OpenPecha\abhidhamma-rails"
GIT = r"C:\Users\Uzumaki Sither\AppData\Local\GitHubDesktop\app-3.6.10\resources\app\git\cmd\git.exe"
D = "4-SYSTEM/scripts/parser-root-text/output/pi-4-english-plain/pi-4-english-plain"


def old(ext):
    r = subprocess.run([GIT, "show", f"HEAD:{D}.{ext}.json"], cwd=REPO, capture_output=True)
    return json.loads(r.stdout.decode("utf-8"))


def new(ext):
    return json.load(open(f"{REPO}/{D}.{ext}.json", encoding="utf-8"))


eo, en = old("edition"), new("edition")
co, cn = eo["content"], en["content"]
p = 0
while p < min(len(co), len(cn)) and co[p] == cn[p]:
    p += 1
s = 0
while s < min(len(co), len(cn)) - p and co[-1 - s] == cn[-1 - s]:
    s += 1
print("content lengths", len(co), len(cn), "| differing middle:", repr(co[p:len(co) - s]), "->", repr(cn[p:len(cn) - s]),
      "| context:", repr(co[max(0, p - 40):p]))
so, sn = eo["segmentation"]["segments"], en["segmentation"]["segments"]
print("segments", len(so), len(sn), "refs/types equal:",
      [(s["reference"], s["type"]) for s in so] == [(s["reference"], s["type"]) for s in sn])
changed = [s["reference"] for s, t in zip(so, sn) if co[s["lines"][0]["start"]:s["lines"][-1]["end"]] != cn[t["lines"][0]["start"]:t["lines"][-1]["end"]]] if "lines" in so[0] and isinstance(so[0]["lines"], list) and isinstance(so[0]["lines"][0], dict) else "n/a"
print("segments whose text changed:", changed)
for k in eo:
    if k not in ("content", "segmentation") and eo[k] != en[k]:
        print("edition field differs:", k)


def titles(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "title":
                out.append(json.dumps(v, ensure_ascii=False))
            else:
                titles(v, out)
    elif isinstance(node, list):
        for v in node:
            titles(v, out)
    return out


to, tn = titles(old("toc"), []), titles(new("toc"), [])
print("toc titles", len(to), len(tn))
for a, b in zip(to, tn):
    if a != b:
        print("  ", a, "->", b)
ao, an = old("alignment"), new("alignment")
print("alignment equal:", ao == an)
