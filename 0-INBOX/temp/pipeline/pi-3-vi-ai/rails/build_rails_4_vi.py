"""Builder for the Vietnamese rails of pi-3 chapter 4 (Tatiyanayo, ^3-179 .. ^3-190), plain audience.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters/4-tatiyanayo.md

Translated from the Pāli (AI_translation/pali/pi-3_split_chapters/4-tatiyanayo.md) with the locked termbase and the
approved formulas (rails/vi-rails-formulas.md, incl. the ch3-15 frames approved 2026-11-20). All shared strings are
imported from build_rails_sample_vi (read-only); the ch4 frame is asserted against the formulas file, and the
pi-1 strings reused here are asserted against the pi-1 rails. New strings: notes-rails-4.md.

usage: python -I -X utf8 build_rails_4_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "4-tatiyanayo.md"

# ------------------------------------------------------------------ frame pieces (approved ch3-15 formulas)
WHICH = "những hiện tượng nào"                     # ye dhammā
WITH = "cùng với"                                  # X-ena (instrumental of the reference item)
BY_K = "theo cách gộp vào khối"                    # khandhasaṅgahena
BY_A = "theo cách gộp vào lĩnh vực nhận biết"      # āyatanasaṅgahena
BY_D = "theo cách gộp vào yếu tố"                  # dhātusaṅgahena
THOSE = "những hiện tượng ấy"                      # te dhammā


def rel_clause(x_vi, pron):
	"""Xena ye dhammā khandhasaṅgahena asaṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā"""
	return (f"{WHICH} {S.OUT_} {WITH} {x_vi} {BY_K}, {S.BUT} {S.IN} {WITH} {pron} {BY_A} và {BY_D}")


def answer(asx, nums):
	"""te dhammā [asaṅkhataṃ khandhato ṭhapetvā] N … saṅgahitā"""
	head = f"{THOSE}, {S.ASANKHATA}," if asx else THOSE
	return f"{head} {S.answer_in(nums)}"


# ------------------------------------------------------------------ reference items in the instrumental
INSTR = {  # instrumental Pāli -> nominative key of S.NAMES (formula: names unchanged)
	"vedanākkhandhena": "vedanākkhandho", "saññākkhandhena": "saññākkhandho",
	"saṅkhārakkhandhena": "saṅkhārakkhandho",
	"samudayasaccena": "samudayasaccaṃ", "maggasaccena": "maggasaccaṃ", "nirodhasaccena": "nirodhasaccaṃ",
	"jīvitindriyena": "jīvitindriyaṃ", "itthindriyena": "itthindriyaṃ", "purisindriyena": "purisindriyaṃ",
	"sukhindriyena": "sukhindriyaṃ", "dukkhindriyena": "dukkhindriyaṃ", "somanassindriyena": "somanassindriyaṃ",
	"domanassindriyena": "domanassindriyaṃ", "upekkhindriyena": "upekkhindriyaṃ",
	"saddhindriyena": "saddhindriyaṃ", "vīriyindriyena": "vīriyindriyaṃ", "satindriyena": "satindriyaṃ",
	"samādhindriyena": "samādhindriyaṃ", "paññindriyena": "paññindriyaṃ",
	"anaññātaññassāmītindriyena": "anaññātaññassāmītindriyaṃ", "aññindriyena": "aññindriyaṃ",
	"aññātāvindriyena": "aññātāvindriyaṃ",
	"avijjāya": "avijjā",
	"avijjāpaccayā saṅkhārena": "avijjāpaccayā saṅkhārā",       # sg. saṅkhārena: name unchanged (reported)
	"saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
	"phassapaccayā vedanāya": "phassapaccayā vedanā",
	"vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
	"taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
	"jātiyā": "jāti", "jarāya": "jarā", "maraṇena": "maraṇaṃ", "jhānena": "jhānaṃ",
	"sokena": "soko", "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ", "upāyāsena": "upāyāso",
	"satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ", "appamaññāya": "appamaññā",
	"pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
	"sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
	"phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā",
	"adhimokkhena": "adhimokkho", "manasikārena": "manasikāro",
}
INSTR_VI = {k: S.NAMES[v] for k, v in INSTR.items()}
# kammabhavena [upādānapaccayā kammabhavena (syā.)]: name of «kammabhavo», variant kept in Pāli (Syā. only here)
INSTR_VI["kammabhavena [upādānapaccayā kammabhavena (syā.)]"] = (
	"sự hiện hữu dưới dạng nghiệp " + S.reading("Syā.", "upādānapaccayā kammabhavena"))

ATTR = {  # X-ehi dhammehi -> key of S.DHAMMA_ATTR («các hiện tượng X», unchanged)
	"hetūhi": "hetū", "hetūhi ceva sahetukehi ca": "hetū ceva sahetukā ca",
	"hetūhi ceva hetusampayuttehi ca": "hetū ceva hetusampayuttā ca",
	"appaccayehi": "appaccayā", "asaṅkhatehi": "asaṅkhatā",
	"āsavehi": "āsavā", "āsavehi ceva sāsavehi ca": "āsavā ceva sāsavā ca",
	"āsavehi ceva āsavasampayuttehi ca": "āsavā ceva āsavasampayuttā ca",
	"parāmāsehi": "parāmāsā", "parāmāsehi ceva parāmaṭṭhehi ca": "parāmāsā ceva parāmaṭṭhā ca",
	"cetasikehi": "cetasikā", "cittasampayuttehi": "cittasampayuttā", "cittasaṃsaṭṭhehi": "cittasaṃsaṭṭhā",
	"cittasaṃsaṭṭhasamuṭṭhānehi": "cittasaṃsaṭṭhasamuṭṭhānā",
	"cittasaṃsaṭṭhasamuṭṭhānasahabhūhi": "cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
	"cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
	"cittasahabhūmi": "cittasahabhuno",          # ^3-189 «Cittasahabhūmi»: slip for cittasahabhūhi (reported)
	"cittānuparivattīhi": "cittānuparivattino",
	"upādānehi": "upādānā", "kilesehi": "kilesā",
	"kilesehi ceva saṃkilesikehi ca": "kilesā ceva saṃkilesikā ca",
	"kilesehi ceva saṃkiliṭṭhehi ca": "kilesā ceva saṃkiliṭṭhā ca",
	"kilesehi ceva kilesasampayuttehi ca": "kilesā ceva kilesasampayuttā ca",
}

# ^3-187: bare instrumental nouns with neither «dhammehi» nor «ye dhammā»; rendered «cùng với các X…»
# exactly as ch5 (5-catutthanayo.md ^3-192) renders the identical Pāli «saṃyojanehi… ganthehi…».
# Coordinator fix 2026-11-20 (rails consistency): was «các hiện tượng là X», which adds words the Pāli lacks.
BARE = {"saṃyojanehi": "các xiềng xích", "ganthehi": "các nút thắt", "oghehi": "các dòng lũ",
	"yogehi": "các ách", "nīvaraṇehi": "các chướng ngại"}


def ref_vi(p):
	"""Instrumental reference item (without «ye dhammā») -> (Vietnamese, plural?)."""
	k = p[0].lower() + p[1:]
	if k.endswith(" dhammehi"):
		return f"{S.DHAMMA_N} {S.DHAMMA_ATTR[ATTR[k[: -len(' dhammehi')]]]}", True
	return INSTR_VI[k], False


# ------------------------------------------------------------------ segment grammar
PRED = "khandhasaṅgahena asaṅgahitā āyatanasaṅgahena saṅgahitā dhātusaṅgahena saṅgahitā"
Q_FULL = ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? Te dhammā "
SEG = re.compile(r"^(?P<subj>.*) ye dhammā " + re.escape(PRED)
                 + r"(?P<mid>" + re.escape(Q_FULL) + r"|…pe… te dhammā |… te dhammā )"
                 + r"(?P<asx>asaṅkhataṃ khandhato ṭhapetvā )?(?P<cnt>" + S.CNT + r") saṅgahitā\.$")


def content_line(p):
	m = SEG.match(p)
	if not m:
		raise ValueError(f"unparsed: {p}")
	items = [x.strip() for x in m.group("subj").split("…")]
	assert all(items), p
	parts = []
	for it in items[:-1]:
		if it.endswith(" ye dhammā"):               # Xena ye dhammā…
			x_vi, _ = ref_vi(it[: -len(" ye dhammā")])
			parts.append(f"{WHICH} {WITH} {x_vi}")
		else:                                        # Saṃyojanehi … ganthehi… (bare noun)
			parts.append(f"{WITH} {BARE[it[0].lower() + it[1:]]}")
	x_vi, plural = ref_vi(items[-1])
	pron = S.PRON["ā"] if plural else S.PRON["o"]
	parts.append(rel_clause(x_vi, pron))
	subj = S.cap("… ".join(parts))
	nums = S.parse_counts(m.group("cnt"))
	ans = answer(bool(m.group("asx")), nums)
	if m.group("mid") == Q_FULL:
		return f"{subj}, {S.THEN} {THOSE} {S.Q_IN} {S.cap(ans)}."
	return f"{subj}…, {ans}."                       # …pe… / … te dhammā


# ------------------------------------------------------------------ summary verse (^3-190, lines 2-5)
VERSE = {
	"Tayo khandhā tathā saccā, indriyāni ca soḷasa;":
		"Ba khối, các sự thật cũng vậy, và mười sáu năng lực;",
	"Padāni paccayākāre, cuddasūpari cuddasa.":
		"Các đề mục trong chuỗi điều kiện là mười bốn, tiếp theo là mười bốn.",
	"Samatiṃsa padā honti, gocchakesu dasasvatha;":
		"Rồi trong mười nhóm có tròn ba mươi đề mục;",
	"Duve cūḷantaradukā [cullantaradukā (sī.)], aṭṭha honti mahantarāti.":
		"Hai bộ đôi xen giữa nhỏ " + S.spell("Sī.", "cullantaradukā") + ", có tám bộ đôi xen giữa lớn.",
}
PI1_REUSE = ["bộ đôi xen giữa nhỏ", "bộ đôi xen giữa lớn"]   # Cūḷantaradukaṃ / Mahantaradukaṃ (pi-1 matrix)


def translate_segment(lines):
	out = []
	for ln in lines:
		if ln.startswith("#"):
			out.append(S.heading_vi(ln))
		elif ln in S.CLOSINGS:
			out.append(S.CLOSINGS[ln])
		elif ln in VERSE:
			out.append(VERSE[ln])
		else:
			out.append(content_line(ln))
	return out


def render():
	blocks = []
	for lines, bid in S.pali_segments(S.PALI / NAME):
		vi = translate_segment(lines)
		assert len(vi) == len(lines), bid
		vi[-1] = f"{vi[-1]} ^{bid}"
		blocks.append("\n".join(vi))
	return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


# ------------------------------------------------------------------ checks
def check_formula():
	"""The full ch4 frame must equal the approved formula (with X / N filled in)."""
	txt = (S.RAILS / "vi-rails-formulas.md").read_text(encoding="utf-8")
	line = next(ln for ln in txt.splitlines() if "saṅgahitā. (ch4) = " in ln)
	f = line.split(" = ", 1)[1].replace(" (proposed for ch3-15)", "")
	f = f.replace("N khối, N lĩnh vực nhận biết và N yếu tố", "ba khối, một lĩnh vực nhận biết và một yếu tố")
	got = (f"{S.cap(rel_clause('X', 'nó'))}, {S.THEN} {THOSE} {S.Q_IN} "
	       f"{S.cap(answer(True, (3, 1, 1)))}.")
	assert got == f, f"frame differs:\n{got}\n{f}"


def check_pi1():
	t1 = "\n".join(p.read_text(encoding="utf-8") for p in sorted(S.PI1_DIR.glob("*.md"))).lower()
	missing = [s for s in PI1_REUSE if s not in t1]
	assert not missing, missing


if __name__ == "__main__":
	n_reuse = S.check_reuse()
	check_formula()
	check_pi1()
	txt = render()
	assert "được được" not in txt and "là là" not in txt and "…." not in txt
	n = S.check_against_pali(txt, S.PALI / NAME)
	(S.OUT / NAME).write_text(txt, encoding="utf-8", newline="\n")
	print(f"{NAME}: {n} segments; {n_reuse} sample pi-1/pi-2 strings + {len(PI1_REUSE)} pi-1 strings asserted")
