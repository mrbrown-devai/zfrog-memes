#!/usr/bin/env python3
"""Build the zfrog.xyz static site (SEO pass).

Inputs:  ../v2/index.html, ../v2/memes_orig.html (the live sources),
         pages/*.html (body fragments for new pages, first line = JSON meta),
         memes.json (from the zfrog-memes repo).
Output:  out/ (index.html, memes/index.html, <slug>/index.html, robots.txt, sitemap.xml, 404.html)
"""
import html, json, os, re, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'live')
OUT = os.path.join(HERE, 'out')
SITE = 'https://www.zfrog.xyz'
RAW = 'https://raw.githubusercontent.com/mrbrown-devai/zfrog-memes/main/'
OG_HOME = RAW + 'brand/og-home.jpg'
CA = 'CZ4dvNHa15HybGwBMDaqWhtN4qVpHa9sayBBVrfxoH2T'
TODAY = datetime.date.today().isoformat()
SAME_AS = ['https://x.com/FrogMark1', 'https://t.me/ZFROGPortal',
           'https://dexscreener.com/solana/fpbmde3afu8ytcqs8vgh7zep7gsepfewx4hqcnduyoj1',
           'https://solscan.io/token/' + CA]


def esc(s):
    return html.escape(s, quote=True)


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'


def social(title, desc, url, image, w=1200, h=630, typ='website'):
    return '\n'.join([
        f'<link rel="canonical" href="{url}">',
        f'<meta property="og:type" content="{typ}">',
        '<meta property="og:site_name" content="ZFROG">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{image}">',
        f'<meta property="og:image:width" content="{w}">',
        f'<meta property="og:image:height" content="{h}">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:site" content="@FrogMark1">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{image}">',
        '<meta name="theme-color" content="#07070a">',
    ])


ORG = {
    '@type': 'Organization', '@id': SITE + '/#org', 'name': 'ZFROG', 'url': SITE + '/',
    'logo': SITE + '/media/logo.jpg',
    'description': '$ZFROG is a community memecoin on Solana that rewards holders in $ZAMA. '
                   'Its main character, ZFROG, was born from FROG Mark 1, Zama\'s first FPGA supercomputer for fully homomorphic encryption. '
                   'Not affiliated with Zama. Official contract: ' + CA,
    'sameAs': SAME_AS,
}
WEBSITE = {'@type': 'WebSite', '@id': SITE + '/#site', 'name': 'ZFROG', 'url': SITE + '/',
           'publisher': {'@id': SITE + '/#org'}, 'inLanguage': 'en'}


def crumbs(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]}


def sub(s, old, new, count=1):
    assert s.count(old) == count, (old[:80], s.count(old))
    return s.replace(old, new)


# ---------------------------------------------------------------- pages config
PAGES = []  # filled from pages/*.html


def load_pages():
    d = os.path.join(HERE, 'pages')
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.html'):
            continue
        raw = open(os.path.join(d, fn), encoding='utf-8').read()
        meta_line, body = raw.split('\n', 1)
        meta = json.loads(meta_line)
        meta['body'] = body
        PAGES.append(meta)
    PAGES.sort(key=lambda p: p.get('order', 99))


NAV_LINKS = [('/earn-zama', 'Earn $ZAMA'), ('/fhe', 'FHE explained'), ('/frog-mark-1', 'FROG Mark 1'), ('/codex', 'Lore'), ('/agent', 'Agent'), ('/memes', 'Memes')]


CODEX_RAW = RAW + 'codex/'
CODEX_BLOCK = f'''  <section id="codex" style="padding-top:0">
    <div class="wrap book">
      <a class="book-cover chip" href="/codex"><img src="{CODEX_RAW}cover.webp" alt="Cover of the Pond Codex: ZFROG peeking over an ancient book" loading="lazy" width="1200" height="800"></a>
      <div class="head">
        <span class="eyebrow">The Pond Codex</span>
        <h2>Privacy is not a right. <em>It is a fight.</em></h2>
        <p>The lore of ZFROG in thirteen chapters: the watched city, FROG Mark 1, the birth on the lily, the creed, the Brothers and the Hooded. Read it online or take the PDF with you.</p>
        <div class="cta-row">
          <a class="btn btn-primary chip" href="/codex">Read the Codex</a>
          <a class="btn btn-ghost chip" href="{CODEX_RAW}ZFROG_Pond_Codex.pdf" target="_blank" rel="noopener">Download the PDF</a>
        </div>
        <p class="book-meta">PDF · 16 pages · 3.6 MB · Second edition, Oct 2026</p>
      </div>
    </div>
  </section>
'''

# ---------------------------------------------------------------- homepage
def build_home():
    s = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()
    title = 'ZFROG ($ZFROG): Hold the Frog, Earn $ZAMA on Solana'
    desc = ('Hold $ZFROG on Solana, earn $ZAMA automatically. The hooded frog born from FROG Mark 1, '
            "Zama's FPGA supercomputer for FHE. Community memecoin, not affiliated with Zama.")
    s = sub(s, '<meta name="description" content="Hold $ZFROG. Earn $ZAMA. The hooded frog guarding Zama\'s first FPGA supercomputer.">',
            f'<meta name="description" content="{esc(desc)}">')
    s = sub(s, '<title>ZFROG</title>', f'<title>{esc(title)}</title>\n' + social(title, desc, SITE + '/', OG_HOME) + '\n' + ld({
        '@context': 'https://schema.org', '@graph': [ORG, WEBSITE, {
            '@type': 'WebPage', '@id': SITE + '/#home', 'url': SITE + '/', 'name': title, 'description': desc,
            'isPartOf': {'@id': SITE + '/#site'}, 'about': {'@id': SITE + '/#org'},
            'primaryImageOfPage': OG_HOME}]}))
    s = sub(s, '<link rel="icon" href="media/logo.jpg">', '<link rel="icon" href="/media/logo.jpg">\n<link rel="apple-touch-icon" href="/media/logo.jpg">')
    # nav: add the new pages (Memes already there)
    s = sub(s, '      <a href="#machine">The machine</a>\n      <a href="/memes">Memes</a>',
            '      <a href="/earn-zama">Earn $ZAMA</a>\n      <a href="/fhe">FHE explained</a>\n      <a href="/memes">Memes</a>')
    s = sub(s, '      <a href="#how">How it works</a>\n', '')
    # internal links from body copy
    s = sub(s, '<div class="cta-row"><a class="btn btn-ghost chip" href="https://x.com/randhindi/status/1938010202235687040" target="_blank" rel="noopener">See the original post</a></div>',
            '<div class="cta-row"><a class="btn btn-primary chip" href="/frog-mark-1">The full FROG Mark 1 story</a><a class="btn btn-ghost chip" href="https://x.com/randhindi/status/1938010202235687040" target="_blank" rel="noopener">See the original post</a></div>')
    s = sub(s, '<p>Every trade feeds the pot. The pot turns into $ZAMA. The $ZAMA lands in holders\' wallets on its own.</p>',
            '<p>Every trade feeds the pot. The pot turns into $ZAMA. The $ZAMA lands in holders\' wallets on its own. <a href="/earn-zama">Full rewards guide</a>.</p>')
    s = sub(s, 'which means computing on data without ever decrypting it.</p>',
            'which means computing on data without ever decrypting it. New to it? <a href="/fhe">FHE explained by a frog</a>.</p>')
    # footer: guides
    s = sub(s, '        <a href="/memes">Memes</a>\n        <a href="#brandbook">Brand book</a>',
            '        <a href="/earn-zama">Earn $ZAMA</a>\n        <a href="/fhe">FHE explained</a>\n        <a href="/frog-mark-1">FROG Mark 1</a>\n        <a href="/memes">Memes</a>\n        <a href="#brandbook">Brand book</a>')
    # official-contract clarity (other ZFROG tokens exist)
    s = sub(s, '      <div class="ca chip" role="group" aria-label="Contract address">',
            '      <div class="ca chip" role="group" aria-label="Official $ZFROG contract address on Solana">')
    # character naming: the hero is ZFROG; FROG Mark 1 is his creator
    # Pond Codex: nav, footer, lore CTA, codex block before the brand book
    s = sub(s, '      <a href="/fhe">FHE explained</a>\n      <a href="/memes">Memes</a>',
            '      <a href="/fhe">FHE explained</a>\n      <a href="/codex">Lore</a>\n      <a href="/memes">Memes</a>')
    s = sub(s, '        <a href="/frog-mark-1">FROG Mark 1</a>\n        <a href="/memes">Memes</a>',
            '        <a href="/frog-mark-1">FROG Mark 1</a>\n        <a href="/codex">The Pond Codex</a>\n        <a href="/memes">Memes</a>')
    s = sub(s, '        <span class="eyebrow">Lore</span>\n        <h2>Tales from <em>the swamp.</em></h2>\n      </div>',
            '        <span class="eyebrow">Lore</span>\n        <h2>Tales from <em>the swamp.</em></h2>\n        <p>Every episode comes from the Pond Codex, the full story of ZFROG. <a href="/codex">Read the Codex</a>.</p>\n      </div>')
    s = sub(s, '  <section id="brandbook" style="padding-top:0">', CODEX_BLOCK + '\n  <section id="brandbook" style="padding-top:0">')
    s = sub(s, 'alt="Cover of the ZFROG brand book: Mark, the hooded frog, next to the ZFROG wordmark"',
            'alt="Cover of the ZFROG brand book: ZFROG, the hooded frog, next to the ZFROG wordmark"')
    s = sub(s, "Mark's character sheet", "ZFROG's character sheet")
    s = sub(s, '<figcaption>Unit 01 · FROG Mark 1</figcaption>', '<figcaption>ZFROG · Unit 01</figcaption>')
    s = sub(s, "<p class=\"lede\">The hooded frog guarding Zama's first FPGA supercomputer.",
            "<p class=\"lede\">The hooded frog born from FROG Mark 1, Zama's first FPGA supercomputer.")
    return s


# ---------------------------------------------------------------- memes page
def build_memes(memes):
    s = open(os.path.join(SRC, 'memes_orig.html'), encoding='utf-8').read()
    n = len(memes['memes'])
    title = 'ZFROG Memes: Zama, FHE and privacy memes to steal and share'
    desc = (f'{n} free ZFROG memes about Zama, FHE, shielded tokens and online privacy. '
            'Filter, search, download or send straight to Telegram. ZRIBBIT.')
    url = SITE + '/memes'
    s = sub(s, '<title>ZFROG Memes</title>', f'<title>{esc(title)}</title>')
    s = sub(s, '<meta name="description" content="Every ZFROG meme in one place. Grab one, drop it in the chat. ZRIBBIT.">',
            f'<meta name="description" content="{esc(desc)}">\n<link rel="canonical" href="{url}">\n<meta name="theme-color" content="#07070a">')
    s = sub(s, '<meta property="og:url" content="https://zfrog.xyz/memes">', f'<meta property="og:url" content="{url}">')
    s = sub(s, 'var PAGE = \'https://zfrog.xyz/memes\';', f"var PAGE = '{url}';")
    cats = {c['id']: c['label'] for c in memes['categories']}
    items = []
    cards = []
    for i, m in enumerate(memes['memes']):
        img = RAW + m['file']
        cap = m.get('caption') or m['title']
        items.append({'@type': 'ImageObject', 'name': m['title'], 'caption': cap, 'contentUrl': img})
        # static, crawlable cards; the script replaces them on load
        cards.append(f'<a class="card chip" href="#{esc(m["id"])}"><img src="{RAW + m.get("thumb", m["file"])}" alt="{esc(cap)}" loading="{"eager" if i < 8 else "lazy"}" width="640" height="640"><span class="meta"><span>{esc(cats.get(m["category"], m["category"]))}</span><strong>{esc(m["title"])}</strong></span></a>')
    graph = {'@context': 'https://schema.org', '@graph': [ORG, WEBSITE, {
        '@type': ['CollectionPage', 'ImageGallery'], '@id': url, 'url': url, 'name': title, 'description': desc,
        'isPartOf': {'@id': SITE + '/#site'}, 'about': ['Zama', 'Fully homomorphic encryption', 'Privacy', 'Memes'],
        'numberOfItems': n},
        crumbs([('Home', SITE + '/'), ('Memes', url)])]}
    s = sub(s, '<link rel="icon" href="/media/logo.jpg">', '<link rel="icon" href="/media/logo.jpg">\n' + ld(graph))
    s = sub(s, '<p>Every ZFROG meme in one place. Tap one, <b>send it straight to Telegram</b> or save it. ZRIBBIT.</p>',
            '<p>Every ZFROG meme in one place: Zama news, FHE and privacy jokes, frog lore. Tap one, <b>send it straight to Telegram</b> or save it. ZRIBBIT.</p>')
    s = sub(s, '<span id="count">··</span>', f'<span id="count">{n}</span>')
    s = sub(s, '<a href="/#how">How it works</a>\n<a href="/memes" aria-current="page">Memes</a>',
            '<a href="/earn-zama">Earn $ZAMA</a>\n<a href="/fhe">FHE explained</a>\n<a href="/memes" aria-current="page">Memes</a>')
    s = sub(s, '<a href="/">Home</a>\n<a href="https://t.me/ZFROGPortal"',
            '<a href="/">Home</a>\n<a href="/earn-zama">Earn $ZAMA</a>\n<a href="/fhe">FHE explained</a>\n<a href="/frog-mark-1">FROG Mark 1</a>\n<a href="https://t.me/ZFROGPortal"')
    return s


# ---------------------------------------------------------------- article pages
ARTICLE_CSS = open(os.path.join(HERE, 'article.css'), encoding='utf-8').read()


def build_article(p):
    url = SITE + '/' + p['slug']
    nav = '\n'.join(f'<a href="{h}"{" aria-current=\"page\"" if h == "/" + p["slug"] else ""}>{t}</a>' for h, t in NAV_LINKS)
    related = [q for q in PAGES if q['slug'] != p['slug']]
    rel_html = ''.join(f'<a class="rel chip" href="/{q["slug"]}"><span class="eyebrow">{esc(q["eyebrow"])}</span><strong>{esc(q["h1_plain"])}</strong></a>' for q in related)
    rel_html += '<a class="rel chip" href="/memes"><span class="eyebrow">Meme vault</span><strong>Steal these memes</strong></a>'
    graph = [ORG, WEBSITE, {
        '@type': p.get('schema_type', 'Article'), '@id': url + '#article', 'headline': p['h1_plain'],
        'description': p['description'], 'url': url, 'mainEntityOfPage': url, 'image': p.get('image', OG_HOME),
        'datePublished': p.get('published', TODAY), 'dateModified': TODAY, 'inLanguage': 'en',
        'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'},
        'about': p.get('about', [])}, crumbs([('Home', SITE + '/'), (p['crumb'], url)])]
    if p.get('faq'):
        graph.append({'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in p['faq']]})
    if p.get('howto'):
        graph.append(p['howto'])
    faq_html = ''
    if p.get('faq'):
        faq_html = '<section class="faq" id="faq"><h2>FAQ</h2>' + ''.join(
            f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in p['faq']) + '</section>'
    return f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['description'])}">
{social(p['title'], p['description'], url, p.get('image', OG_HOME), typ='article')}
<link rel="icon" href="/media/logo.jpg">
<link rel="apple-touch-icon" href="/media/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Barlow:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{ld({'@context': 'https://schema.org', '@graph': graph})}
<header class="nav">
<div class="wrap">
<a class="brand" href="/" aria-label="ZFROG home"><img src="/media/logo.jpg" alt="" width="42" height="42">ZFROG</a>
<nav aria-label="Site">
{nav}
</nav>
<a class="btn btn-primary chip" href="https://raydium.io/swap/?inputMint=sol&amp;outputMint={CA}" target="_blank" rel="noopener">Get $ZFROG</a>
</div>
</header>
<main>
<article class="wrap art">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">/</span> <span>{esc(p['crumb'])}</span></nav>
<header class="art-head">
<span class="eyebrow">{esc(p['eyebrow'])}</span>
<h1>{p['h1']}</h1>
<p class="lede">{p['lede']}</p>
<p class="byline">By the ZFROG pond · Updated <time datetime="{TODAY}">{datetime.date.today().strftime('%-d %b %Y')}</time></p>
</header>
{('<figure class="hero-img chip"><img src="' + p['hero_img'] + '" alt="' + esc(p['hero_alt']) + '" width="' + str(p.get('hero_w', 1200)) + '" height="' + str(p.get('hero_h', 675)) + '" fetchpriority="high"></figure>') if p.get('hero_img') else ''}
<div class="prose">
{p['body']}
</div>
{faq_html}
<aside class="cta chip">
<div><h2>Hold the frog. <em>Earn $ZAMA.</em></h2><p>Official $ZFROG contract on Solana: <code>{CA}</code></p></div>
<div class="cta-row"><a class="btn btn-primary chip" href="https://raydium.io/swap/?inputMint=sol&amp;outputMint={CA}" target="_blank" rel="noopener">Buy on Raydium</a><a class="btn btn-ghost chip" href="https://t.me/ZFROGPortal" target="_blank" rel="noopener">Join the Telegram</a></div>
</aside>
<section class="related"><h2>Keep digging</h2><div class="rel-grid">{rel_html}</div></section>
</article>
</main>
<footer>
<div class="wrap">
<div class="foot-top">
<a class="brand" href="/"><img src="/media/logo.jpg" alt="" width="42" height="42">ZFROG</a>
<div class="foot-links">
<a href="/earn-zama">Earn $ZAMA</a><a href="/fhe">FHE explained</a><a href="/frog-mark-1">FROG Mark 1</a><a href="/codex">The Pond Codex</a><a href="/memes">Memes</a><a href="https://t.me/ZFROGPortal" target="_blank" rel="noopener">Telegram</a><a href="https://x.com/FrogMark1" target="_blank" rel="noopener">X</a>
</div>
</div>
<p class="disclaimer">$ZFROG is a community memecoin with no intrinsic value and no expectation of financial return. It is not affiliated with, endorsed by or operated by Zama. For official Zama information go to <a href="https://www.zama.org" rel="noopener">zama.org</a>. Crypto assets are highly volatile and you can lose everything you put in. Nothing on this site is financial advice. © 2026 ZFROG.</p>
</div>
</footer>
</html>
'''


def build_404():
    p = {'title': 'Lost in the swamp · ZFROG', 'description': 'This page sank to the bottom of the pond.'}
    links = ''.join(f'<a class="btn btn-ghost chip" href="{h}">{t}</a>' for h, t in [('/', 'Home')] + NAV_LINKS)
    return f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/media/logo.jpg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Barlow:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<style>.lost{{min-height:70vh;display:grid;align-content:center;gap:22px;padding-block:80px}}
.lost h1{{font-size:clamp(48px,9vw,120px);text-transform:uppercase}}</style>
<main class="wrap lost"><span class="eyebrow">404</span><h1>Lost in <em>the swamp.</em></h1><p class="lede">This page sank to the bottom of the pond. Try one of these.</p><div class="cta-row">{links}</div></main>
</html>
'''


def main():
    load_pages()
    memes = json.load(open(os.path.join(HERE, 'memes.json'), encoding='utf-8'))
    os.makedirs(OUT, exist_ok=True)
    files = {'index.html': build_home(), 'memes/index.html': build_memes(memes), '404.html': build_404()}
    for p in PAGES:
        files[p['slug'] + '/index.html'] = build_article(p)
    files['breakpoint/index.html'] = open(os.path.join(HERE, 'breakpoint.html'), encoding='utf-8').read()
    from chrome import unify
    for rel in list(files):
        key = 'home' if rel == 'index.html' else ('404' if rel == '404.html' else rel.split('/')[0])
        files[rel] = unify(files[rel], key)
    files['assets/site.css'] = ARTICLE_CSS
    from chrome import CHROME_CSS
    files['assets/chrome.css'] = CHROME_CSS
    bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'Googlebot']
    files['robots.txt'] = ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) + f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n'
    files['llms.txt'] = open(os.path.join(HERE, 'llms.txt'), encoding='utf-8').read()
    urls = [('/', '1.0', 'daily'), ('/memes', '0.8', 'daily')] + [('/' + p['slug'], '0.9', 'weekly') for p in PAGES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, pr, cf in urls:
        sm.append(f'<url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority>')
        sm.append('</url>')
    sm.append('</urlset>')
    files['sitemap.xml'] = '\n'.join(sm) + '\n'
    for rel, content in files.items():
        path = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{len(content.encode()):>8}  {rel}')


if __name__ == '__main__':
    main()
