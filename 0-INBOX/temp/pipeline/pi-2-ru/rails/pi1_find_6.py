"""Chapter 6 helper: for each Pāli substring, print the first pi-1 segment line containing it with the aligned
Russian line (to find the approved pi-1 wording of the shared Abhidhamma passages). Writes pi1-find-6.txt.
usage: python -I -X utf8 pi1_find_6.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails\pi1-find-6.txt")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
PATS = [
    "akusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ diṭṭhigatasampayuttaṃ rūpārammaṇaṃ",
    "somanassasahagataṃ diṭṭhigatasampayuttaṃ sasaṅkhārena",
    "upekkhāsahagataṃ diṭṭhigatasampayuttaṃ",
    "domanassasahagataṃ paṭighasampayuttaṃ",
    "upekkhāsahagataṃ vicikicchāsampayuttaṃ",
    "upekkhāsahagataṃ uddhaccasampayuttaṃ",
    "kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ rūpārammaṇaṃ",
    "ñāṇavippayuttaṃ sasaṅkhārena",
    "rūpūpapattiyā maggaṃ bhāveti vivicceva",
    "arūpūpapattiyā maggaṃ bhāveti sabbaso ākiñcaññāyatanaṃ",
    "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ",
    "kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ",
    "vipākā manodhātu uppannā hoti",
    "vipākā manoviññāṇadhātu uppannā hoti somanassasahagatā",
    "vipākā manoviññāṇadhātu uppannā hoti upekkhāsahagatā",
    "Tasseva rūpāvacarassa kusalassa kammassa",
    "Tasseva arūpāvacarassa",
    "Tasseva lokuttarassa kusalassa jhānassa",
    "manodhātu uppannā hoti kiriyā",
    "manoviññāṇadhātu uppannā hoti kiriyā",
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ",
    "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ",
    "Yaṃ aññāṇaṃ adassanaṃ…pe…",
    "Yā cetanā sañcetanā sañcetayitattaṃ",
    "cittaṃ mano mānasaṃ hadayaṃ",
    "Yo phasso phusanā samphusanā samphusitattaṃ",
    "Yo rāgo sārāgo anunayo",
    "diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ",
    "adhimokkho adhimuccanā tadadhimuttatā",
    "caṇḍikkaṃ asuropo",
    "kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ",
    "uddhaccaṃ avūpasamo cetaso vikkhepo",
    "Yo alobho alubbhanā",
    "Yo adoso adussanā",
    "saddhā saddahanā okappanā abhippasādo",
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ",
    "nissāya manoviññāṇadhātu",
    "āyatanānaṃ ācayo",
    "jāti sañjāti nibbatti",
    "khayo vayo bhedo",
    "jarā jīraṇatā āyuno",
    "phasso hoti…pe… avikkhepo hoti",
    "ime dhammā kusalā",
    "katattā bhāvitattā",
    "tajjācakkhuviññāṇadhātu",
    "tajjāmanodhātu",
    "tajjākāyaviññāṇadhātu",
    "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ",
    "Ṭhapetvā",
    "dhammavicayasambojjhaṅgo maggaṅgaṃ",
    "dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ",
    "pubbeva somanassadomanassānaṃ",
    "kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti upekkhāsahagataṃ ñāṇasampayuttaṃ",
    "Katame dhammā abyākatā? Yasmiṃ samaye kāmāvacarassa",
]


def segs(path):
    out, cur = {}, []
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        cur.append(ln)
        m = ID.search(ln)
        if m:
            out[m.group(1)] = cur
            cur = []
    return out


pdir = ROOT / "pali" / "pi-1_split_chapters"
rdir = ROOT / "russian" / "pi-1-russian-plain-rails_split_chapters"
data = []
for pf in sorted(pdir.glob("*.md")):
    rf = rdir / pf.name
    if rf.exists():
        data.append((pf.name, segs(pf), segs(rf)))
res = []
for pat in PATS:
    found = 0
    for name, P, R in data:
        for sid, pl in P.items():
            for i, ln in enumerate(pl):
                if pat in ln and found < 2:
                    rl = R.get(sid, [])
                    res += [f"######## {pat}", f"== {name} ^{sid} line {i}", "PI: " + ln, "RU: " + (rl[i] if i < len(rl) else "-"), ""]
                    found += 1
    if not found:
        res += [f"######## {pat}", "NOT FOUND", ""]
OUT.write_text("\n".join(res) + "\n", encoding="utf-8", newline="\n")
print("done")
