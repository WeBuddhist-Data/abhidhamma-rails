# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 8: 8-satipatthanakatha.md (Satipaṭṭhānakathā,
^5-8-0 … ^5-303).

Imports the approved sample builder (build_sample_vi) for every debate frame, and the finished chapter
builders build_2_vi (kilesa list, satipaṭṭhāna … bojjhaṅga list) and build_4_vi (khayagāmī … asaṃkilesiya)
for identical Pāli; the chapter's own repeated phrases are fixed strings below, so every repeat is
byte-identical. Every string claimed from the pi-1..4 Vietnamese rails is asserted to occur there; the
sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli.

run:  python -I -X utf8 build_8_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (import writes nothing)
import build_4_vi as C4      # noqa: E402  (import writes nothing)

NAME = "8-satipatthanakatha.md"
Q, q, NANU, AM, cap = B.Q, B.q, B.NANU, B.AMANTA, B.cap
NHP = B.NA_HEVAM_PE

# ================================================================ terms
SP = "sự thiết lập tỉnh thức"                 # satipaṭṭhānaṃ / satipaṭṭhānā (sg.) (pi-1, pi-2)
SPS = C2.DEV6[0]                              # satipaṭṭhānā (pl.) = «các sự thiết lập tỉnh thức» (ch2, pi-3)
assert SPS == "các " + SP
ALL = "tất cả các hiện tượng"                 # sabbe dhammā
ALL_SP = f"{ALL} là {SPS}"                    # sabbe dhammā satipaṭṭhānā
SATI = "sự tỉnh thức"                         # sati (core term)
SATI5 = f"{SATI}, năng lực tỉnh thức, sức mạnh tỉnh thức, tỉnh thức đúng đắn, chi phần giác ngộ là {SATI}"
# sati satindriyaṃ satibalaṃ sammāsati satisambojjhaṅgo (pi-1 ^1-290)
SATI4 = f"{SATI}, năng lực tỉnh thức, sức mạnh tỉnh thức, tỉnh thức đúng đắn"   # … sammāsati…pe…
EKAYANA = "con đường duy nhất"                # ekāyanamaggo / ekāyano … maggo (new)
POS = C4.POS                                  # niyyāniko khayagāmī … asaṃkilesiyo (ch4; pi-1 matrix names)
QUAL_ALL = ", ".join(POS[1:])                 # khayagāmī bodhagāmī apacayagāmī anāsavā … asaṃkilesikā
QUAL_PE = f"{', '.join(POS[1:6])}… {POS[-1]}"  # khayagāmī … anāsavaṃ asaṃyojaniyaṃ…pe… asaṃkilesikaṃ
ANUSSATI = [
    "sự nhớ lại Đức Phật",                    # buddhānussati (anussati «sự nhớ lại» pi-1 ^1-14)
    "sự nhớ lại Giáo Pháp",                   # dhammānussati
    "sự nhớ lại Tăng đoàn",                   # saṅghānussati
    "sự nhớ lại giới hạnh",                   # sīlānussati (sīla «giới hạnh» pi-2)
    "sự nhớ lại sự rộng lượng",               # cāgānussati (cāgavant «rộng lượng» pi-1)
    "sự nhớ lại chư thiên",                   # devatānussati
    f"{SATI} về hơi thở vào và hơi thở ra",   # ānāpānassati (new)
    "sự nhớ lại sự chết",                     # maraṇānussati (maraṇa «sự chết» pi-2)
    f"{SATI} hướng về thân",                  # kāyagatāsati (new)
    "sự nhớ lại sự lắng dịu",                 # upasamānussati (new; kept apart from passaddhi «sự an tịnh»)
]
ANU_ALL = ", ".join(ANUSSATI)
ANU_PE = f"{ANUSSATI[-2]}, {ANUSSATI[-1]}"    # …pe… kāyagatāsati upasamānussati
KAYAGATA = ANUSSATI[-2]

AY = B.AYATANA                                # cakkhāyatanaṃ … phoṭṭhabbāyatanaṃ (pi-2)
CAKKHU = AY[0]
KILESA = [C2.R, C2.D, C2.M, C2.MANA, C2.DI, C2.VI, C2.TH, C2.UD, C2.AH, C2.AO]
# rāgo doso moho māno diṭṭhi vicikicchā thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ (ch2; pi-1)
ANOTTAPPA = KILESA[-1]

AND_SATI = "và nó là sự tỉnh thức"            # sā ca satī / tañca satī
AND_NOT = "và nó không phải là sự tỉnh thức"  # sā ca na satī / tañca na satī


def sp_is(x):
    """X satipaṭṭhānaṃ / sati satipaṭṭhānā (singular)"""
    return f"{x} là {SP}"


def sati_is(x, full=True):
    """X sati satindriyaṃ … asaṃkilesikaṃ, X buddhānussati … upasamānussati"""
    if full:
        return f"{x} là {SATI5}, {EKAYANA}, {QUAL_PE}, {x} là {ANU_ALL}"
    return f"{x} là {SATI4}… {ANU_PE}"


ARABBHA_ALL = "lấy tất cả các hiện tượng làm đối tượng"   # sabbe dhamme ārabbha (pi-1 «lấy … làm đối tượng»)
ARABBHA = "lấy mọi hiện tượng làm đối tượng"              # sabbaṃ dhammaṃ ārabbha
STAND = "mà đứng vững"                                     # santiṭṭhati (pi-2 «đứng vững»)
SATI_ST_ALL = f"{SATI} {ARABBHA_ALL} {STAND}"              # sabbe dhamme ārabbha sati santiṭṭhati
SATI_ST = f"{SATI} {ARABBHA} {STAND}"                      # sabbaṃ dhammaṃ ārabbha sati santiṭṭhati


def if_q(x, y):
    """Xti Yti? (sample frame «Có phải nếu X, thì Y không?»)"""
    return f"Có phải nếu {x}, thì {y} không?"


# ================================================================ sutta passages
BHIKKHAVE = "Này các tỳ-khưu,"
AMATA = "sự bất tử"                     # amataṃ (new)
ENJOY = "thọ hưởng"                     # paribhuñjati (new)
SUTTA_AMATA = (f"“{BHIKKHAVE} những ai không {ENJOY} {KAYAGATA} thì không {ENJOY} {AMATA}. "
               f"{BHIKKHAVE} những ai {ENJOY} {KAYAGATA} thì {ENJOY} {AMATA}” [Tăng Chi Bộ Kinh 1.600]")
# "amataṃ te, bhikkhave, na paribhuñjanti ye kāyagatāsatiṃ na paribhuñjanti. Amataṃ te, bhikkhave,
# paribhuñjanti ye kāyagatāsatiṃ paribhuñjantī"ti [a. ni. 1.600]
ALL_BEINGS_KG = (f"tất cả chúng sinh {ENJOY}, có được, thực hành, tu tập, làm đi làm lại {KAYAGATA}")
# sabbe sattā kāyagatāsatiṃ paribhuñjanti paṭilabhanti āsevanti bhāventi bahulīkaronti (pi-2 ^2-522)

SUTTA_EKAYANA = (f"“{BHIKKHAVE} đây là {EKAYANA} để chúng sinh được thanh lọc, để vượt qua sự sầu muộn và sự "
                 "than khóc, để làm biến mất sự khó chịu và nỗi buồn, để chứng đắc phương pháp đúng đắn, để tự "
                 f"mình chứng nghiệm Niết-bàn, tức là bốn {SP}” "
                 "[Trường Bộ Kinh 2.373; Trung Bộ Kinh 1.106; Tương Ưng Bộ Kinh 5.367]")
# "ekāyano ayaṃ, bhikkhave, maggo sattānaṃ visuddhiyā sokaparidevānaṃ samatikkamāya dukkhadomanassānaṃ
# atthaṅgamāya ñāyassa adhigamāya nibbānassa sacchikiriyāya yadidaṃ cattāro satipaṭṭhānā"ti

APPEAR = "có sự xuất hiện của"          # … pātubhāvo hoti (pātubhāva «sự xuất hiện» pi-2)
KING = "do sự xuất hiện của vị vua chuyển luân"                         # rañño cakkavattissa pātubhāvā (pi-2)
TATHAGATA = f"do sự xuất hiện của Như Lai, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"
# Tathāgatassa pātubhāvā arahato sammāsambuddhassa (Như Lai pi-2; epithets = homage wording pi-1)
KATAMESAM = "Bảy điều nào?"             # Katamesaṃ sattannaṃ?
RAT = "báu vật"                          # ratana (new)
BRAT = f"{RAT} chi phần giác ngộ"        # bojjhaṅgaratana
BOJJH = ["sự tỉnh thức", "sự tìm hiểu các hiện tượng", "sự tinh tấn", "sự hân hoan", "sự an tịnh", "định tâm",
         "sự bình thản"]                 # satisambojjhaṅga … upekkhāsambojjhaṅga (pi-2 ^2-466)
SUTTA_RATANA_1 = (f"“{BHIKKHAVE} {KING}, {APPEAR} bảy {RAT}. {KATAMESAM} "
                  f"{cap(APPEAR)} {RAT} bánh xe, {APPEAR} {RAT} voi, {RAT} ngựa… {RAT} ngọc… {RAT} người nữ… "
                  f"{RAT} gia chủ… {APPEAR} {RAT} vị cố vấn. {BHIKKHAVE} {KING}, {APPEAR} bảy {RAT} này.")
# cakka- hatthi- assa- maṇi- itthi- gahapati- pariṇāyakaratana (gahapati «gia chủ» pi-2; rest new)
SUTTA_RATANA_2 = (f"“{BHIKKHAVE} {TATHAGATA}, {APPEAR} bảy {BRAT}. {KATAMESAM} "
                  + ", ".join(f"{cap(APPEAR) if i == 0 else APPEAR} {BRAT} là {b}" for i, b in enumerate(BOJJH))
                  + f". {BHIKKHAVE} {TATHAGATA}, {APPEAR} bảy {BRAT} này” [Tương Ưng Bộ Kinh 5.223]")
ALL_RATANA = f"{TATHAGATA}, {ALL} chính là các {BRAT} là {SATI}"
# Tathāgatassa pātubhāvā arahato sammāsambuddhassa sabbe dhammā satisambojjhaṅgaratanāva honti
REST5 = "… ".join(C2.DEV6[1:])          # sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā (ch2, pi-3)

CROSS = [
    ("sự thiết lập tỉnh thức", 1), ("Bốn sự thiết lập tỉnh thức", 2), (SATI5, 1),
    ("sự nhớ lại", 1), ("sự nhớ lại các đời sống trước", 2), ("Giáo Pháp", 1), ("Tăng đoàn", 2),
    ("giới hạnh", 2), ("rộng lượng", 1), ("chư thiên", 2), ("sự chết", 2), ("Đức Phật", 4),
    ("lấy bất cứ thứ gì làm đối tượng", 1), ("sự tỉnh thức phù hợp với điều ấy đứng vững", 2),
    ("sự tiếp xúc", 1), ("cảm giác", 1), ("tri giác", 1), ("chủ ý", 1), ("tâm", 1),
    ("chúng sinh", 2), ("được trang bị sự tỉnh thức", 2), ("thực hành, tu tập, làm đi làm lại", 2),
    ("có được", 2), ("sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn", 2), ("biến mất", 1),
    ("chứng đắc", 2), ("tự mình chứng nghiệm", 1), ("Niết-bàn", 2), ("vượt qua", 1),
    ("vị vua chuyển luân", 2), ("Như Lai", 2), ("sự xuất hiện", 2), ("bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn", 1),
    ("gia chủ", 2), ("voi", 4), ("ngựa", 4),
    ("chi phần giác ngộ là sự tỉnh thức, chi phần giác ngộ là sự tìm hiểu các hiện tượng, chi phần giác ngộ là sự "
     "tinh tấn, chi phần giác ngộ là sự hân hoan, chi phần giác ngộ là sự an tịnh, chi phần giác ngộ là định tâm, "
     "chi phần giác ngộ là sự bình thản", 2),
    ("sự tham lam, sự sân hận, sự si mê, sự kiêu mạn, quan điểm, sự hoài nghi, sự uể oải, sự xao động, sự "
     "không biết hổ thẹn, sự không biết ghê sợ tội lỗi", 1), ("sự tham đắm", 1),
    ("lĩnh vực âm thanh", 2), ("lĩnh vực vật xúc chạm", 2),
] + [(s, 1) for s in POS[4:]] + [("dẫn đến sự giảm trừ", 1)]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"ch8 cross-book asserts: {len(CROSS)} strings found in pi-1..4 rails")


# ================================================================ build
def build():
    d = B.Doc()
    d.head(3, B.KATHA.format(x=SP), "5-8-0")                                  # Satipaṭṭhānakathā
    rest9 = [*AY[1:10], *KILESA[:-1]]                                         # sotāyatanaṃ … ahirikaṃ
    l5_items = [AY[1], AY[4], AY[5], AY[9], *KILESA[:3]]                      # sotā…pe… kāyā… rūpā…pe… phoṭṭhabbā… rāgo… doso… moho…pe…
    d.seg("5-301",
          f"{Q(ALL_SP)} {AM} Có phải {ALL} là {SATI5}, {EKAYANA}, {QUAL_ALL}, {ALL} là {ANU_ALL} không? {NHP}",
          f"{Q(ALL_SP)} {AM} {Q(sp_is(CAKKHU))} {NHP} {q(sp_is(CAKKHU))} {AM} {Q(sati_is(CAKKHU))} {NHP} "
          f"có phải {'… '.join(rest9)}… {sp_is(ANOTTAPPA)} không? {NHP} {q(sp_is(ANOTTAPPA))} {AM} "
          f"{Q(sati_is(ANOTTAPPA, full=False))} {NHP}",
          f"{Q(sp_is(SATI) + ', ' + AND_SATI)} {AM} {Q(sp_is(CAKKHU) + ', ' + AND_SATI)} {NHP} "
          f"{q(sp_is(SATI) + ', ' + AND_SATI)} {AM} "
          f"Có phải {'… '.join(l5_items)}… {sp_is(ANOTTAPPA)}, {AND_SATI} không? {NHP}",
          f"{Q(sp_is(CAKKHU) + ', ' + AND_NOT)} {AM} {Q(sp_is(SATI) + ', ' + AND_NOT)} {NHP} "
          f"có phải {'… '.join(l5_items)}… {sp_is(ANOTTAPPA)}, {AND_NOT} không? {AM} "
          f"{Q(sp_is(SATI) + ', ' + AND_NOT)} {NHP}")
    phassa = "sự tiếp xúc"                                                    # phasso (pi-1)
    d.seg("5-302",
          f"{B.NA_VATTABBAM_Q(ALL_SP)} {AM} {NANU(SATI_ST_ALL)} {AM} {B.HANCI.format(p=SATI_ST_ALL, q=ALL_SP)}",
          f"{if_q(SATI_ST, ALL_SP)} {AM} {if_q(f'{phassa} {ARABBHA} {STAND}', f'{ALL} là các sự thiết lập tiếp xúc')} "
          f"{NHP}",
          f"{if_q(SATI_ST, ALL_SP)} {AM} "
          f"{if_q(f'{B.VEDANA} {ARABBHA} {STAND}… {B.SANNA} đứng vững… chủ ý đứng vững… tâm đứng vững', f'{ALL} là các sự thiết lập tâm')} "
          f"{NHP}",
          f"{Q(ALL_SP)} {AM} Có phải tất cả chúng sinh có {SATI} được thiết lập, được trang bị {SATI}, được kết hợp "
          f"với {SATI}; nơi tất cả chúng sinh, {SATI} hiện diện không? {NHP}")
    d.seg("5-303",
          f"{Q(ALL_SP)} {AM} {B.NANU_VUTTAM} {SUTTA_AMATA}. {B.ATTHEVA} {AM} {Q(ALL_BEINGS_KG)} {NHP}",
          f"{Q(ALL_SP)} {AM} {B.NANU_VUTTAM} {SUTTA_EKAYANA}! {B.ATTHEVA} Đúng vậy? "
          f"{Q(f'{ALL} là {EKAYANA}')} {NHP}",
          f"{Q(ALL_SP)} {AM} {B.NANU_VUTTAM} {SUTTA_RATANA_1}",
          f"{SUTTA_RATANA_2}. {B.ATTHEVA} {AM} {Q(ALL_RATANA)} {NHP} {q(ALL_SP)} {AM} "
          f"{Q(f'{ALL} là {REST5}')} {NHP}",
          B.KATHA_END.format(x=SP))
    return d.text()


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and "chánh niệm" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
