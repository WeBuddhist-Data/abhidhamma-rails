"""Wikipedia pageviews per language edition for Abhidhamma-related articles.

Resolves each English article to its Wikidata item, follows sitelinks to every
target language edition, then sums monthly user pageviews (Nov 2025 - Oct 2026).
"""
import json, sys, time, urllib.parse, urllib.request

UA = "abhidhamma-rails-language-research/0.1 (https://github.com/OpenPecha)"
START, END = "20251101", "20261031"

TOPICS = {
    "abhidhamma": "Abhidhamma Piṭaka",
    "abhidharma": "Abhidharma",
    "pali_canon": "Pali Canon",
    "theravada": "Theravada",
    "buddhism": "Buddhism",
}
# our language code -> wikipedia db prefix
LANGS = {
    "en": "en", "bo": "bo", "fr": "fr", "hi": "hi", "ja": "ja", "lzh": "zh-classical",
    "mn": "mn", "mr": "mr", "ne": "ne", "ru": "ru", "sa": "sa", "th": "th",
    "vi": "vi", "zh": "zh",
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(2 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def sitelinks(en_title):
    url = ("https://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&format=json"
           "&props=sitelinks&redirects=yes&titles=" + urllib.parse.quote(en_title))
    data = get(url)
    ent = next(iter(data["entities"].values()))
    return ent.get("id"), {k: v["title"] for k, v in ent.get("sitelinks", {}).items()}


def views(project, title):
    t = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}.wikipedia/"
           f"all-access/user/{t}/monthly/{START}00/{END}00")
    data = get(url)
    if not data:
        return 0
    return sum(i["views"] for i in data.get("items", []))


out = {"window": f"{START}-{END}", "topics": {}}
for key, en_title in TOPICS.items():
    qid, links = sitelinks(en_title)
    row = {"wikidata": qid, "langs": {}}
    for code, wp in LANGS.items():
        site = wp.replace("-", "_") + "wiki"
        title = links.get(site)
        row["langs"][code] = {"title": title, "views": views(wp, title) if title else None}
        time.sleep(0.1)
    out["topics"][key] = row
    print(key, qid, {c: v["views"] for c, v in row["langs"].items()}, file=sys.stderr)

json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
