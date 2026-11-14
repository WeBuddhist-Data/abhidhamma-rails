"""Coordinator cleanup of the pi-1 Russian keyword map after the parallel run (2026-11-14). Idempotent; logs to cleanup-log.tsv.

- user rule (sample review): a keyword with no word of its own in the Russian = (no direct equivalent).
  Bare prepositions are not a word of their own: sahagataṃ=с («с восприятием …»), vidhena=по («по два»).
  patho in dvedhāpatho («распутье») and gāho in anekaṃsaggāho: (no direct equivalent), as 4-01 / 4-02 already have.
- identical segments must map identically (crosscheck_map_ru.py): «X ceva X-niyā» pairs take the participle form of ch5;
  hetukā = имеющий корни.
- one value per keyword where the parts only differ in wording of the same Russian: upasampajja viharati, vivicceva kāmehi,
  vivicca, paṭipadaṃ dandha / khippa, asaṅkhatā ca dhātu; Ito = этот (dictionary form).
"""
import pathlib

D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\mapper-ru")
NDE = "(no direct equivalent)"
RULES = {  # keyword -> {old value: new value}
    "sahagataṃ": {"с": NDE},
    "vidhena": {"по": NDE},
    "patho": {"распутье": NDE, "(no direct equivalent)": NDE},
    "gāho": {"прийти": NDE},
    "Ito": {"это": "этот"},
    "hetukā": {"иметь корни": "имеющий корни"},
    "saṃyojanā ceva saṃyojaniyā": {"оковы и подверженный оковам": "являющийся оковами и подверженный оковам"},
    "ganthā ceva ganthaniyā": {"узы и подверженный узам": "являющийся узами и подверженный узам"},
    "nīvaraṇā ceva nīvaraṇiyā": {"помехи и подверженный помехам": "являющийся помехами и подверженный помехам"},
    "upādānā ceva upādāniyā": {"цепляния и служащий объектом цепляния": "являющийся цепляниями и служащий объектом цепляния"},
    "upasampajja viharati": {"входить в … и пребывать в нём": "входить … пребывать"},
    "vivicceva kāmehi": {"полностью уединившись от чувственных удовольствий": "полностью уединиться от чувственных удовольствий"},
    "vivicca": {"уединившись": "уединиться"},
    "paṭipadaṃ dandha": {"способ практики и медленный": "способ практики … медленный"},
    "paṭipadaṃ khippa": {"способ практики и быстрый": "способ практики … быстрый"},
    "asaṅkhatā ca dhātu": {"и необусловленный элемент": "необусловленный элемент"},
}
# 2-04 ^1-425: dvedhāpatho = «распутье»; dvedhā keeps «распутье», patho -> NDE (rule above)

log = []
for p in sorted(D.glob("*.mapped.md")):
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if "] " in line:
            head, body = line.split("] ", 1)
            items = []
            for it in body.split(", "):
                k, v = it.split("=", 1)
                nv = RULES.get(k, {}).get(v, v)
                if nv != v:
                    log.append(f"{p.stem}\t{head[1:]}\t{k}\t{v}\t{nv}")
                items.append(f"{k}={nv}")
            line = head + "] " + ", ".join(items)
        out.append(line)
    p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
(D / "cleanup-log.tsv").write_text("part\tid\tkeyword\told\tnew\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("changes", len(log))
