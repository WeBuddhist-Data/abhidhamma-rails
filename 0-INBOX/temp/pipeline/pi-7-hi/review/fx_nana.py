"""nānākkhaṇikā fragments: Pāli «… cetanā vipākānaṃ … paccayo» vs Hindi «इरादा … के लिए» shapes."""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
out = open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\fx_out.txt", "w", encoding="utf-8")
shape = collections.Counter()
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        if "cetanā vipāk" not in p:
            continue
        pf = re.findall(r"cetanā vipāk[^.;]*?kammapaccayena", p)
        hf = re.findall(r"इरादा[^।;]*?कर्म-फल रूपी[^।;]*?के लिए", h)
        for x in pf:
            out.write(f"{part[:4]}:{i+1} P: {x}\n")
        for x in hf:
            s = re.sub(r"इरादा (.*?)कर्म-फल रूपी", lambda m: "इरादा <" + m.group(1) + ">कर्म-फल रूपी", x)
            out.write(f"{part[:4]}:{i+1} H: {s}\n")
            k = re.sub(r"[^\s,]+", "w", x)
            shape[("," in x.split("कर्म-फल रूपी")[1][:3], x.startswith("इरादा कर्म-फल"), x.startswith("इरादा, "))] += 1
print(shape)
