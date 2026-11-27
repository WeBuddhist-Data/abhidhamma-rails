"""Build the Burmese pi-N merged file and track copy, the same way as the Marathi / Hindi tracks.

usage: python -I -X utf8 burmese_publish.py N [N ...]

For each book N:
 1. pi-N-my/my-frontmatter.yaml: the library IDs (category, text, edition, translator) and the
    book facts copied from pi-N-mr/mr-frontmatter.yaml; the language fields made Burmese.
 2. merge_rails.py -> AI_translation/burmese/pi-N-burmese-plain.md (re-verified against the Pāli split).
 3. Track copy 3-TRANSFORMATIONS/Translations/my-Contemporary-Burmese-Abhidhamma/pi-N-burmese-plain.md:
    add_transclusions.py copies each root-text transclusion line from the Marathi track copy
    to the block with the same segment ID; then verify_transclusions.py checks it independently,
    and the transclusion list must equal the Marathi one.
 4. The termbase copied byte for byte into the track folder.
Nothing is uploaded anywhere.
"""
import datetime, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PIPE = ROOT / "0-INBOX/temp/pipeline"
PY = "/opt/homebrew/Caskroom/miniconda/base/bin/python3"
TRACK = ROOT / "3-TRANSFORMATIONS/Translations/my-Contemporary-Burmese-Abhidhamma"
MR_TRACK = ROOT / "3-TRANSFORMATIONS/Translations/mr-Contemporary-Marathi-Abhidhamma"
MY = ROOT / "AI_translation/burmese"
SUFFIX = " - ရိုးရှင်းသော မြန်မာ"
KEEP = ["translator", "source_title", "root_text", "category_id", "license", "source", "source_split",
        "source_text_id", "source_edition_id", "translation_of", "segment_ids", "chapters"]

APPROACH = ("zero-shot built by generator scripts from shared formula frames (sample first, remaining files in "
            "parallel), then a book-wide consistency pass; rails = the harmonised text with the locked termbase "
            "applied by an audited rule script (0 genuine termbase misses); identical Pāli kept as identical "
            "Burmese within the book and with the earlier Burmese books; independent bilingual review with fixes "
            "applied; translated from the Pāli only, no existing Burmese translation, nissaya or web source used; "
            "dashes only where the Pāli has them")
APPROACH_1 = APPROACH + ("; afterwards a meaning-only comparison of part of the book with the Religious Affairs "
                         "Burmese translation (copyrighted, post-translation reference only, no wording used, its "
                         "findings not applied)")


def run(*args):
    r = subprocess.run([PY, "-I", "-X", "utf8", *map(str, args)], capture_output=True, text=True, cwd=ROOT)
    out = (r.stdout + r.stderr).strip()
    if r.returncode:
        sys.exit(f"FAILED: {' '.join(map(str, args))}\n{out}")
    return out


def fm_value(text, key):
    m = re.search(rf"^{key}: (.*)$", text, re.M)
    if not m:
        sys.exit(f"missing {key}")
    return m.group(1)


def trans_lines(p):
    return [l for l in p.read_text(encoding="utf-8").split("\n") if l.startswith("![[")]


def book(n):
    mr = (PIPE / f"pi-{n}-mr/mr-frontmatter.yaml").read_text(encoding="utf-8")
    rails = MY / f"pi-{n}-burmese-plain-rails_split_chapters"
    heading = None
    for p in sorted(rails.glob("*.md")):
        m = re.search(rf"^## (.+) \^{n}-0$", p.read_text(encoding="utf-8"), re.M)
        if m:
            heading = m.group(1); break
    if not heading:
        sys.exit(f"pi-{n}: book heading ^{n}-0 not found")
    approved = re.search(r"20\d\d-\d\d-\d\d", (PIPE / f"pi-{n}-my/termbase/APPROVED.md").read_text(encoding="utf-8")).group(0)
    generated = datetime.date.fromtimestamp(max(p.stat().st_mtime for p in rails.glob("*.md"))).isoformat()
    v = {k: fm_value(mr, k) for k in KEEP}
    lines = ["---", f"title: {heading}{SUFFIX}", f"translator: {v['translator']}"]
    for k in KEEP[1:10]:
        lines.append(f"{k}: {v[k]}")
    lines += [
        "language: Burmese", "lang_tag: my", "file_type: translation",
        "audience_profile: AI_translation/audience_profile/plain.md",
        f"termbase: AI_translation/burmese/pi-{n}-pali-burmese-termbase-plain.md",
        f"termbase_approved: {approved}",
        f'pipeline: "zeroshot-translator -> keyword-equivalence-mapper (Pāli keywords from AI_translation/pali/pi-{n}-keywords-by-reference-pali-plain.md; keyword extraction skipped) -> word-sense-grouper -> termbase-builder -> rails-verse-translator"',
        f'approach: "{APPROACH_1 if n == 1 else APPROACH}"',
        f"zeroshot_split: AI_translation/burmese/pi-{n}-burmese-plain-zeroshot_split_chapters",
        f"keyword_map: AI_translation/burmese/pi-{n}-keywords-by-reference-pali-burmese-plain.md",
        f"senses: AI_translation/burmese/pi-{n}-pali-word-burmese-senses-plain.md",
        f"segment_ids: {v['segment_ids']}", f"chapters: {v['chapters']}",
        f"split_chapters: AI_translation/burmese/pi-{n}-burmese-plain-rails_split_chapters",
        f"generated: {generated}", "status: draft", "---"]
    fm = PIPE / f"pi-{n}-my/my-frontmatter.yaml"
    fm.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    merged = MY / f"pi-{n}-burmese-plain.md"
    out = run(PIPE / "merge_rails.py", ROOT / f"AI_translation/pali/pi-{n}_split_chapters", rails, fm, merged)
    nseg = sum(1 for l in merged.read_text(encoding="utf-8").split("\n") if re.search(r"\^[0-9A-Za-z-]+\s*$", l))

    TRACK.mkdir(parents=True, exist_ok=True)
    tr = TRACK / f"pi-{n}-burmese-plain.md"
    mr_tr = MR_TRACK / f"pi-{n}-marathi-plain.md"
    run(ROOT / "AI_translation/skills/scripts/add_transclusions.py", mr_tr, merged, "-o", tr)
    # the frontmatter's segment_ids line names the last ID, so the tool also puts that transclusion
    # above the frontmatter; drop it there when the same line also stands in the body
    t = tr.read_text(encoding="utf-8").split("\n")
    k = t.index("---")
    head, rest = t[:k], t[k:]
    if any(l.strip() and not (l.startswith("![[") and l in rest) for l in head):
        sys.exit(f"pi-{n}: unexpected lines above the frontmatter: {head}")
    if head:
        tr.write_text("\n".join(rest), encoding="utf-8", newline="\n")
    ver = [l for l in run(PIPE / "pi-3-4/verify_transclusions.py", tr, ROOT, 0).splitlines() if l.strip()][-1]
    if "ALL OK" not in ver:
        sys.exit(f"pi-{n}: verify_transclusions: {ver}")
    if ": OK;" not in out:
        sys.exit(f"pi-{n}: merge_rails: {out}")
    a, b = trans_lines(tr), trans_lines(mr_tr)
    if a != b:
        sys.exit(f"pi-{n}: transclusions differ from the Marathi track ({len(a)} vs {len(b)})")
    if not tr.read_text(encoding="utf-8").startswith("---\n"):
        sys.exit(f"pi-{n}: track copy does not start with frontmatter")
    tb = MY / f"pi-{n}-pali-burmese-termbase-plain.md"
    shutil.copyfile(tb, TRACK / tb.name)
    print(f"pi-{n}: title «{heading}{SUFFIX}»; merged {nseg} segments; merge: {out.splitlines()[-1] if out else 'OK'}; "
          f"transclusions {len(a)} (= Marathi); verify: {ver}")


for n in map(int, sys.argv[1:]):
    book(n)
