"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 8: 8-satipatthanakatha.

usage: python -I -X utf8 -B map_8_vi.py                  (writes 8-satipatthanakatha.mapped.md and verifies it)
       python -I -X utf8 -B map_8_vi.py show lo hi        (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T8, text) of map_sample_vi (T8 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import NDE, GAP, build_part, en_ru, lc, present, read_keywords, read_vietnamese, verify  # noqa
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "8-satipatthanakatha"

_ST = "sự tỉnh thức"
_TL = "sự thiết lập tỉnh thức"

T8 = {
    # ---- 5-301 «Có phải tất cả các hiện tượng là các sự thiết lập tỉnh thức không? … là sự tỉnh thức, năng lực tỉnh
    # thức, sức mạnh tỉnh thức, tỉnh thức đúng đắn, chi phần giác ngộ là sự tỉnh thức, con đường duy nhất, dẫn đến sự
    # diệt tận …, sự nhớ lại Đức Phật, … sự nhớ lại sự rộng lượng, sự nhớ lại chư thiên, sự tỉnh thức về hơi thở vào
    # và hơi thở ra, sự nhớ lại sự chết, sự tỉnh thức hướng về thân, sự nhớ lại sự lắng dịu»
    "dhammā satipaṭṭhānā": "hiện tượng là các " + _TL,   # inner «là các» kept (notes-map-6 «quá khứ là các khối»)
    "kāyagatāsati": _ST + " hướng về thân", "kāyagatāsatiṃ": _ST + " hướng về thân",
    "gatā": "hướng về",                            # member of kāyagatāsati
    "ānāpāna": "hơi thở vào và hơi thở ra",        # ānāpānassati «sự tỉnh thức về hơi thở vào và hơi thở ra»
    "cāga": "sự rộng lượng", "devatā": "chư thiên", "upasama": "sự lắng dịu",   # X-ānussati «sự nhớ lại X»
    "ekāyana": "duy nhất", "ekāyano": "duy nhất",  # ekāyanamaggo / ekāyano … maggo «con đường duy nhất»
    "khaya": "sự diệt tận",                        # khayagāmī «dẫn đến sự diệt tận» (notes-map-4)
    "māno": "sự kiêu mạn",                         # the text writes «sự kiêu mạn» (notes-map-2)
    "ottappaṃ": "biết ghê sợ tội lỗi",             # only inside anottappaṃ (notes-map-2, positive part)
    # ---- 5-302 «Chẳng phải sự tỉnh thức lấy tất cả các hiện tượng làm đối tượng mà đứng vững sao? … lấy mọi hiện
    # tượng làm đối tượng … tất cả chúng sinh có sự tỉnh thức được thiết lập, được trang bị sự tỉnh thức, được kết
    # hợp với sự tỉnh thức»
    "ārabbha": "lấy" + GAP + "làm đối tượng",      # no ārammaṇa keyword: «làm đối tượng» renders ārabbha alone
    "santiṭṭhati": "đứng vững",
    "sabbaṃ": "mọi", "dhammaṃ": "hiện tượng",      # Sabbaṃ dhammaṃ «mọi hiện tượng»
    "samohitā": "được kết hợp",
    # ---- 5-303 sutta quotes «… những ai không thọ hưởng sự tỉnh thức hướng về thân thì không thọ hưởng sự bất tử»;
    # «… con đường duy nhất để chúng sinh được thanh lọc, để vượt qua sự sầu muộn và sự than khóc, để làm biến mất
    # sự khó chịu và nỗi buồn, để chứng đắc phương pháp đúng đắn, để tự mình chứng nghiệm Niết-bàn, tức là bốn sự
    # thiết lập tỉnh thức»; «do sự xuất hiện của vị vua chuyển luân, có sự xuất hiện của bảy báu vật …»
    "amataṃ": "sự bất tử", "paribhuñjanti": "thọ hưởng", "paṭilabhanti": "có được", "āsevanti": "thực hành",
    "bahulīkaronti": "làm đi làm lại",
    "visuddhiyā": "được thanh lọc",                # sattānaṃ visuddhiyā «để chúng sinh được thanh lọc» («để» frame)
    "samatikkamāya": "vượt qua", "atthaṅgamāya": "làm biến mất",
    "paridevānaṃ": "sự than khóc",                 # notes-map-4 paridevehi
    "dukkha": "sự khó chịu",                       # dukkhadomanassānaṃ «sự khó chịu và nỗi buồn» (notes-map-4)
    "ñāyassa": "phương pháp đúng đắn",
    "yadidaṃ": "tức là",
    "rañño": "vị vua", "cakkavattissa": "chuyển luân", "rañño cakkavattissa": "vị vua chuyển luân",
    "ratanassa": "báu vật", "ratanānaṃ": "báu vật",
    "cakka": "bánh xe", "assa": "ngựa", "itthi": "người nữ", "maṇi": "ngọc", "gahapati": "gia chủ",
    "pariṇāyaka": "vị cố vấn",                     # «báu vật vị cố vấn» (classifier kept as the text writes it)
    "arahato": "bậc A-la-hán",                     # map_2_vi _ARA
    "sambuddhassa": "bậc Tự Giác Ngộ",             # member of sammāsambuddhassa (pi-1 / pi-3)
    "sammāsambuddhassa": "bậc Tự Giác Ngộ Hoàn Toàn",
    "bojjha": "giác ngộ", "aṅga": "chi phần",      # map_2_vi (bojjhaṅga «chi phần giác ngộ»)
    "balā": "sức mạnh",                            # «các sức mạnh» (map_2_vi)
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value5(kw, kws, T8, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi = read_vietnamese(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
