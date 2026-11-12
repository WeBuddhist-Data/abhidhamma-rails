import os, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import khuddaka17_f as F, khuddaka17_c as C
D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
corpus = "\n".join(open(os.path.join(D, f), encoding="utf-8-sig").read() for f in os.listdir(D) if f.endswith(".md"))
corpus = re.sub(r"\s*\[[^\]]*\]", "", corpus)
chk = {k: getattr(F, k) for k in ["KODHA_SYN", "MOHA_KNOW", "KAMA_FULL", "BHAVA_FULL", "DITTHI_PE", "INDRIYA_AGUTTA", "INDRIYA_AGUTTA_END", "THINA", "UDDHACCA", "MUTTHASSACCA", "VICIKICCHA_1", "PAPAMITTA_WHO", "DOVACASSA", "AHIRIKA", "ANOTTAPPA", "SILABBATA_Q", "MACCHARIYA_5", "LOLUPPA", "DOSA_2", "MOHA_PE_TAIL", "SASSATO_LOKO_ALL", "VITIKKAMA", "MACCHARIYA_SYN_A"]}
chk["DOSA_1"] = F.DOSA_1.format(s=",")
chk["NATTHI"] = F.NATTHI_DINNAM.format(v="")
for k in ["FEEL_SOM", "FEEL_DOM", "FEEL_UPE"]: chk[k] = getattr(C, k)
for k, v in chk.items():
    print(k, v.rstrip("।") in corpus)
