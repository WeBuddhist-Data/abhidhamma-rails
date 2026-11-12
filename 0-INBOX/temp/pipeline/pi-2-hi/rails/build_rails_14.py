"""Builder: pi-2 chapter 14 (Sikkhāpadavibhaṅga), Hindi rails, plain audience.

usage: python -I -X utf8 build_rails_14.py
Imports build_rails_sample (read-only constants and emit), build_rails_15_citta, build_rails_3_panha.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402
import build_rails_15_citta as C  # noqa: E402
import build_rails_3_panha as P  # noqa: E402

CH = "14-sikkhapadavibhango.md"
TITLE = "प्रशिक्षण के नियमों का विश्लेषण"
VER = "दूर रहने"  # precept phrases: termbase phrase entries (… से दूर रहना / दूर रहने का प्रशिक्षण-नियम)
ABL = {  # the five abstentions, ablative member (… से)
    "pana": "जीव-हत्या से",
    "adinna": "बिना दी गई चीज़ लेने से",
    "kama": "इंद्रिय-सुखों में दुराचार से",
    "musa": "झूठ बोलने से",
    "sura": "लापरवाही का कारण बनने वाली शराब, मदिरा और नशीली चीज़ों से",
}
ORDER = ["pana", "adinna", "kama", "musa", "sura"]


def name(k):
    return f"{ABL[k]} {VER} का प्रशिक्षण-नियम"


FIVE = "पाँच प्रशिक्षण-नियम – " + ", ".join(name(k) for k in ORDER) + "।"


def q(k):
    return f"यहाँ {name(k)} क्या है?"


Q_MULTI = "यहाँ " + "… ".join(name(k) for k in ORDER[1:]) + " क्या है?"


def head(k, desc):
    """Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti <desc> <X> viramantassa"""
    return f"जिस समय {ABL[k]} विरत रहने वाले व्यक्ति में {C.KAMA_KUSALA} {C.UPP}, जो {desc} होता है"


def called(k):
    return f"यह “{name(k)}” कहा जाता है।"


def arati(k):
    return (f"उस समय जो {ABL[k]} दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, "
            f"दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना है – {called(k)}")


AV_VER = "शेष परिघटनाएँ बचने से जुड़ी हैं।"  # veramaṇiyā on its own = बचना
AV_CET = "शेष परिघटनाएँ इरादे से जुड़ी हैं।"


def cetana(k):
    return f"उस समय जो इरादा, इरादा करना, इरादा कर चुका होना है – {called(k)}"


def phassa(k, yo=True):
    if yo:
        return f"उस समय जो संपर्क… तत्परता, भटकाव का अभाव है – {called(k)}"
    return f"उस समय संपर्क… तत्परता, भटकाव का अभाव – {called(k)}"


def tail(k):
    """Avasesā dhammā veramaṇiyā sampayuttā…pe… avasesā dhammā cetanāya sampayuttā…pe… phasso…pe… paggāho avikkhepo – idaṃ vuccati …"""
    return f"{AV_VER[:-1]}… {AV_CET[:-1]}… संपर्क… तत्परता, भटकाव का अभाव – {called(k)}"


D1 = C.q2(C.SN, C.NS)                       # somanassasahagataṃ ñāṇasampayuttaṃ
D_LAST = C.q3(C.UP, C.NVP, C.SAS)           # upekkhāsahagataṃ ñāṇavippayuttaṃ sasaṅkhārena
D8 = C.CHAIN8                               # sasaṅkhārena…pe… upekkhāsahagataṃ ñāṇavippayuttaṃ sasaṅkhārena
ADH4 = ["chanda", "viriya", "citta", "vimamsa"]
ADH3 = ["chanda", "viriya", "citta"]
D_HINA = f"{C.q3(C.SN, C.NS, C.HINA)}… {C.hina_chain(ADH4)}"
D8_HINA = "… ".join(C.CHAIN8_LIST[:-1] + [f"{C.UP}, {C.NVP}, {C.SAS} और {C.HINA}"]) + "… " + C.hina_chain(ADH3)
# ^2-711: "…cittādhipateyyaṃ hīnaṃ… majjhimaṃ paṇītaṃ" (no ellipsis between the last two)
D8_HINA_711 = D8_HINA[: -len("मध्यम… उत्तम")] + "मध्यम, उत्तम"
assert D8_HINA.endswith("मध्यम… उत्तम")

SIKKHA_Q = "कौन-सी परिघटनाएँ प्रशिक्षण हैं?"
IME_SIKKHA = "ये परिघटनाएँ प्रशिक्षण हैं।"

PANHA_Q = ("पाँच प्रशिक्षण-नियमों में से कितने हितकर हैं, कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… "
           "कितने संघर्ष वाले हैं, कितने संघर्ष से रहित?")
DEFAULT = P.Subj("पाँचों", "इन पाँचों", True)


def build(pali):
    lines = {sid: [S.ID.sub("", x).rstrip() for x in pl] for sid, pl in S.segs_of_lines(pali)}
    h = {}
    h["2-14-0"] = [f"### {TITLE}"]
    h["2-14-1-0"] = [f"#### {S.ABHI_BH}"]
    h["2-703"] = [FIVE]
    k = "pana"
    h["2-704"] = [f"{q(k)} {head(k, D1)}, {arati(k)} {AV_VER}",
                  f"{q(k)} {head(k, D1)}, {cetana(k)} {AV_CET}",
                  f"{q(k)} {head(k, D1)}, {phassa(k)}",
                  f"{q(k)} {head(k, D8)}, {arati(k)} {AV_VER}"]
    h["2-705"] = [f"{q(k)} {head(k, D_LAST)}, {cetana(k)} {AV_CET}",
                  f"{q(k)} {head(k, D_LAST)}, {phassa(k, yo=False)}"]
    k = "sura"
    h["2-706"] = [f"{Q_MULTI} {head(k, D1)}, {arati(k)} {AV_VER}",
                  f"{q(k)} {head(k, D1)}, {cetana(k)} {AV_CET}",
                  f"{q(k)} {head(k, D1)}, {phassa(k)}",
                  f"{q(k)} {head(k, D8)}, {arati(k)} {AV_VER}"]
    h["2-707"] = [f"{q(k)} {head(k, D_LAST)}, {cetana(k)} {AV_CET}",
                  f"{q(k)} {head(k, D_LAST)}, {phassa(k)}"]
    h["2-708"] = [FIVE]
    k = "pana"
    h["2-709"] = [f"{q(k)} {head(k, D_HINA)}, {arati(k)} {AV_VER}",
                  f"{q(k)} {head(k, D_HINA)}, {cetana(k)} {AV_CET}",
                  f"{q(k)} {head(k, D_HINA)}, {phassa(k)}",
                  f"{q(k)} {head(k, D8_HINA)}, {arati(k)} {tail(k)}"]
    k = "sura"
    h["2-710"] = [f"{Q_MULTI} {head(k, D_HINA)}, {arati(k)} {tail(k)}"]
    h["2-711"] = [f"{q(k)} {head(k, D8_HINA_711)}, {arati(k)} {tail(k)}"]
    h["2-712"] = [f"{SIKKHA_Q} {C.kusala_head(D1)} {C.OBJ_ALL}, {C.PHASSA_PE}। {IME_SIKKHA}",
                  f"{SIKKHA_Q} {C.kusala_head(D8)} {C.OBJ_ALL}, {C.PHASSA_PE}। {IME_SIKKHA}"]
    path = (f"{C.RUPUPAPATTI}… {C.ARUPUPAPATTI[len('जिस समय '):]}… {C.LOKUTTARA[len('जिस समय '):]}, "
            f"{C.JHANA1_PATH}, {C.PHASSA_PE}। {IME_SIKKHA}")
    h["2-713"] = [f"{SIKKHA_Q} {path}", f"{S.ABHI_BH}।"]
    h["2-14-2-0"] = [f"#### {S.PANHA}"]
    h["2-714"] = [FIVE]
    h["2-715"] = [PANHA_Q]
    h["2-14-2-1-0"] = ["##### तीन-तीन के वर्गीकरण"]
    t = lines["2-716"]
    h["2-716"] = [P.render_line(t[0], DEFAULT), P.render_line(t[1], DEFAULT)]
    h["2-14-2-2-0"] = ["##### दो-दो के वर्गीकरण"]
    d = lines["2-717"]
    h["2-717"] = [P.render_line(d[0], DEFAULT, fixes=[("Na hetū sahetukā, hetusampayuttā.",
                                                        "Na hetū, sahetukā, hetusampayuttā.")]),
                  P.render_line(d[1], DEFAULT, fixes=[("Āsavavippayuttā sāsavā", "āsavavippayuttasāsavā")]),
                  P.render_line(d[2], DEFAULT),
                  f"{S.PANHA}।", f"{TITLE} {S.DONE}।"]
    return h


def strip_ids(pl):
    return [S.ID.sub("", x).rstrip() for x in pl]


if __name__ == "__main__":
    pali = (S.PALI / CH).read_text(encoding="utf-8").splitlines()
    h = build(pali)
    S.emit(pali, h, S.OUT / CH)
