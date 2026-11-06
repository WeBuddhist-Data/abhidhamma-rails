"""Build the pi-6 track copy from the merged English, in the same format as pi-4 and pi-5.

Run from the project root (abhidhamma-rails/). It adds the track's frontmatter fields and one
root transclusion before every content block; headings get none.

Then run the linter and the parser on the track copy. Re-running this replaces the track copy,
so copy text_id, edition_id and toc_id back into its frontmatter after any rebuild.
"""
import re

SOURCE = 'AI_translation/english/pi-6-english-plain.md'
ROOT_TEXT = '1-SOURCES/Text/pi-6.md'
TRACK = '3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-6-english-plain.md'


def main():
    with open(SOURCE, encoding='utf-8') as fh:
        text = fh.read()
    match = re.match(r'---\n(.*?)\n---\n', text, re.S)
    frontmatter, body = match[1], text[match.end():]

    # Same fields and order as the pi-4 and pi-5 track copies.
    frontmatter = frontmatter.replace(
        'source_title: Yamakapāḷi\n',
        'source_title: Yamakapāḷi\n'
        f'root_text: {ROOT_TEXT}\n'
        'category_id: MZUUxphQ0yFwLBon3Vng8\n'
        'license: public\n'
        'source: https://webuddhist.com\n',
    )
    frontmatter = re.sub(r'^(?:termbase_variant|source_file):.*\n', '', frontmatter, flags=re.M)

    out = []
    for para in re.split(r'\n\s*\n', body.strip('\n')):
        block_id = re.search(r'\^(\S+)\s*$', para)[1]
        if not para.startswith('#'):
            out.append(f'![[{ROOT_TEXT}#^{block_id}]]')
        out.append(para)

    with open(TRACK, 'w', encoding='utf-8') as fh:
        fh.write('---\n' + frontmatter + '\n---\n\n' + '\n\n'.join(out) + '\n')
    print(f'Wrote {TRACK}: {len(out)} paragraphs')


if __name__ == '__main__':
    main()
