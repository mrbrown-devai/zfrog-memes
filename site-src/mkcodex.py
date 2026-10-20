"""Builds pages/codex.html from the Pond Codex markdown (claude/ZFROG_Pond_Codex.md)."""
import json, re, sys
RAW = 'https://raw.githubusercontent.com/mrbrown-devai/zfrog-memes/main/codex/'
PDF = RAW + 'ZFROG_Pond_Codex.pdf'
SRC = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/docs/ZFROG_Pond_Codex.md'
DISC = '<p class="callout"><strong>Not Zama.</strong> $ZFROG is an independent community memecoin. The Pond Codex is fan lore. It is not affiliated with, endorsed by or sponsored by Zama. For official Zama information, go to <a href="https://www.zama.org" rel="noopener">zama.org</a>.</p>'

# chapter number -> (image, width, height, caption, alt)
PLATES = {
    'I': ('01', 1200, 675, 'Plate 01 · Surveillance room', 'ZFROG at a desk facing a tunnel of surveillance screens'),
    'II': ('02', 1200, 800, 'Plate 02 · Cooking up something', 'ZFROG writing by candlelight with a burning quill'),
    'III': ('03', 1200, 1200, 'Plate 03 · Incubated', 'ZFROG tucked under a blue blanket, only his eyes and mask showing'),
    'IV': ('04', 1200, 800, 'Plate 04 · Behind the curtain', 'ZFROG peeking from behind a dark curtain'),
    'V': ('05', 1200, 1499, 'Plate 05 · The final boss', 'A giant ZFROG towering over a small figure in a misty wasteland'),
    'VI': ('06', 1200, 800, 'Plate 06 · The ripple-grammar', 'Two ZFROGs facing each other across a galaxy, linked by a line of light'),
    'VII': ('07', 1200, 1200, 'Plate 07 · Interpose', 'ZFROG reaching toward the camera with a gloved hand'),
    'VIII': ('08', 1200, 1499, 'Plate 08 · The pot', 'ZFROG in an apron tossing fried rice in a wok'),
    'IX': ('09', 1200, 1200, 'Plate 09 · The night shift', 'ZFROG asleep at his desk while a ghostly ZFROG keeps watch'),
    'X': ('10', 1200, 1200, 'Plate 10 · Peephole', 'ZFROG seen through a door peephole'),
    'XI': ('11', 1200, 675, 'Plate 11 · Same Pond', 'ZFROG in a holiday selfie with three people on a boat'),
    'XII': ('12', 1200, 1200, 'Plate 12 · Lore night', 'ZFROG in a cinema seat with a bucket of popcorn'),
    'XIII': ('13', 1200, 1499, 'Plate 13 · Rain watch', 'ZFROG looking up into heavy rain at night'),
    'Appendix': ('appendix', 1200, 800, 'Plate 14 · The canon', 'ZFROG puzzling over a long redacted scroll'),
}


def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    return t


def slug(num):
    return 'appendix' if num == 'Appendix' else 'ch-' + num.lower()


md = open(SRC, encoding='utf-8').read()
chapters = re.split(r'^## ', md, flags=re.M)[1:]
toc, sections = [], []
for ch in chapters:
    head, _, text = ch.partition('\n')
    text = text.split('\n---')[0].strip()
    num, _, name = head.partition('. ')
    sid = slug(num)
    label = 'Appendix' if num == 'Appendix' else 'Chapter ' + num
    toc.append(f'<li><a href="#{sid}"><span>{num if num != "Appendix" else "App."}</span>{inline(name)}</a></li>')
    paras = [p.strip() for p in text.split('\n\n') if p.strip()]
    img, w, h, cap, alt = PLATES[num]
    tall = ' tall' if h > w else ''
    plate = (f'<figure class="plate{tall}"><img src="{RAW}{img}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy">'
             f'<figcaption>{cap}</figcaption></figure>')
    if num == 'V':
        body = '<div class="creed">' + ''.join(f'<p>{inline(p)}</p>' for p in paras) + '</div>'
    else:
        body = ''.join(f'<p>{inline(p)}</p>' for p in paras)
    sections.append(f'<section class="chapter" id="{sid}"><span class="eyebrow">{label}</span>\n<h2>{inline(name)}</h2>\n{plate}\n{body}</section>')

intro = f'''<p>The Pond Codex is the lore of ZFROG: where the frog comes from, what he believes, and the watched city he was made to resist. FROG Mark 1, Zama's first FPGA supercomputer, is his creator. The Brothers are the weather of surveillance. The Hooded are everyone who holds. Read it once, then keep it open while you write, draw or shoot anything in the pond.</p>
<div class="cta-row"><a class="btn btn-primary chip" href="{PDF}" target="_blank" rel="noopener">Download the Codex (PDF)</a><a class="btn btn-ghost chip" href="#ch-v">Skip to the creed</a></div>
<nav class="toc" aria-label="Chapters"><span class="eyebrow">Contents</span><ol>{''.join(toc)}</ol></nav>
'''
outro = f'''<p class="codex-end"><em>End of the second codex. The pond does not close.</em></p>
<div class="cta-row"><a class="btn btn-primary chip" href="{PDF}" target="_blank" rel="noopener">Download the Codex (PDF)</a><a class="btn btn-ghost chip" href="/frog-mark-1">The real FROG Mark 1</a></div>
''' + DISC

meta = dict(order=4, slug='codex', crumb='The Pond Codex', eyebrow='Lore',
            title='The Pond Codex: the lore of ZFROG, born of FROG Mark 1 | ZFROG',
            description='The lore of ZFROG: a hooded frog created by FROG Mark 1, Zama\'s first FPGA supercomputer, raised to fight for privacy in a watched city. Read online or download the PDF.',
            h1='The Pond <em>Codex.</em>', h1_plain='The Pond Codex: the ZFROG lore',
            lede='Born of FROG Mark 1. Kept by the Hooded. Raised against the Brothers. Privacy is not a right. Privacy is a fight.',
            hero_img=RAW + 'cover.webp', hero_alt='ZFROG peeking over an ancient book of encryption diagrams', hero_w=1200, hero_h=800,
            image=RAW + 'og-codex.jpg', schema_type='Article',
            about=['ZFROG', 'FROG Mark 1', 'Zama', 'Privacy', 'Fully homomorphic encryption', 'Lore'],
            faq=[
                ('Who created ZFROG?', 'In the lore, FROG Mark 1, Zama\'s first FPGA supercomputer, created ZFROG. Rand built the machine. Zama made the machine, never the frog.'),
                ('Is the main character called Mark?', 'No. The main character is ZFROG, Unit 01. FROG Mark 1 is the machine that created him, and ZFROG Mark 1 is the name of the ZFROG agent.'),
                ('Is the Pond Codex official Zama lore?', 'No. It is community lore written for $ZFROG, an independent memecoin that is not affiliated with Zama.'),
                ('Can I write, draw or film in the pond?', 'Yes. Read the appendix for the canon: names, objects, words and the rules of ZFROG\'s voice. Post what you make in the ZFROG Telegram.'),
            ])
body = intro + '\n'.join(sections) + '\n' + outro
with open('pages/codex.html', 'w', encoding='utf-8') as f:
    f.write(json.dumps(meta, ensure_ascii=False) + '\n' + body)
print('codex ok', len(body))
