"""User decision 2026-11-14 on the pi-1 Russian map sample: a keyword whose 'positive part' is not a real
Russian word, or that has no word of its own in the Russian, gets (no direct equivalent).
Applies to the approved sample parts; idempotent.
"""
import pathlib

D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\mapper-ru")
FIX = {
    "nikkhitta=отступный": "nikkhitta=(no direct equivalent)",
    "santuṭṭhitā=насытность": "santuṭṭhitā=(no direct equivalent)",
    "ṭhānesu=то что": "ṭhānesu=(no direct equivalent)",
}
n = 0
for p in sorted(D.glob("*.mapped.md")):
    lines = p.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if "] " in line:
            head, body = line.split("] ", 1)
            items = [FIX.get(k, k) for k in body.split(", ")]
            n += sum(1 for a, b in zip(body.split(", "), items) if a != b)
            line = head + "] " + ", ".join(items)
        out.append(line)
    p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("replaced", n)
