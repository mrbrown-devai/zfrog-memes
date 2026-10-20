"""One header and one footer for every page of zfrog.xyz."""
import re
CA = 'CZ4dvNHa15HybGwBMDaqWhtN4qVpHa9sayBBVrfxoH2T'
RAW = 'https://raw.githubusercontent.com/mrbrown-devai/zfrog-memes/main/'
BUY = f'https://raydium.io/swap/?inputMint=sol&amp;outputMint={CA}'
NAV = [('/#rewards', 'Rewards', 'home'), ('/earn-zama', 'Earn $ZAMA', 'earn-zama'), ('/fhe', 'FHE explained', 'fhe'),
       ('/frog-mark-1', 'FROG Mark 1', 'frog-mark-1'), ('/codex', 'Lore', 'codex'), ('/agent', 'Agent', 'agent'), ('/memes', 'Memes', 'memes')]

CHROME_CSS = '''header.nav.sf{position:sticky;top:0;z-index:40;background:color-mix(in srgb,#07070a 88%,transparent);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid #2c2c17}
header.sf .wrap{display:flex;align-items:center;gap:24px;min-height:68px;max-width:1180px;margin-inline:auto;padding-inline:clamp(16px,4vw,48px)}
header.sf .brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:700 22px/1 "Chakra Petch","Arial Narrow",system-ui,sans-serif;letter-spacing:.02em;color:#f1eee0}
header.sf .brand img{width:42px;height:42px;object-fit:cover;border:1px solid #f7d417;box-shadow:0 0 14px color-mix(in srgb,#f7d417 35%,transparent);clip-path:polygon(7px 0,calc(100% - 7px) 0,100% 7px,100% calc(100% - 7px),calc(100% - 7px) 100%,7px 100%,0 calc(100% - 7px),0 7px)}
header.sf nav{display:flex;gap:22px;margin-left:auto;font:500 15px/1 "Chakra Petch","Arial Narrow",system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase}
header.sf nav a{text-decoration:none;color:#a29f8a;white-space:nowrap;padding:6px 0}
header.sf nav a:hover,header.sf nav a[aria-current]{color:#f1eee0}
header.sf nav a[aria-current]{box-shadow:0 2px 0 #f7d417}
header.sf .sf-buy{display:inline-flex;align-items:center;justify-content:center;font:700 15px/1 "Chakra Petch","Arial Narrow",system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;padding:15px 22px;background:#f7d417;color:#07070a;clip-path:polygon(9px 0,calc(100% - 9px) 0,100% 9px,100% calc(100% - 9px),calc(100% - 9px) 100%,9px 100%,0 calc(100% - 9px),0 9px)}
header.sf .sf-buy:hover{background:#fff27a}
.bar{top:69px}
@media (max-width:980px){header.sf .wrap{flex-wrap:wrap;gap:10px 16px;padding-block:10px 0;min-height:0}
header.sf .sf-buy{margin-left:auto;padding:12px 16px;font-size:13px}
header.sf nav{display:flex;order:3;width:100%;margin:0;gap:20px;overflow-x:auto;scrollbar-width:none;padding:6px 0 12px;font-size:14px}
header.sf nav::-webkit-scrollbar{display:none}
.bar{top:107px}}
footer.sf{border-top:1px solid #2c2c17;padding-block:48px 40px;font:400 15px/1.5 "Barlow",system-ui,sans-serif;color:#a29f8a;background:#07070a}
footer.sf .wrap{display:grid;gap:32px;max-width:1180px;margin-inline:auto;padding-inline:clamp(16px,4vw,48px)}
footer.sf .sf-top{display:grid;grid-template-columns:1.3fr repeat(3,1fr);gap:28px 40px}
footer.sf .brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:700 22px/1 "Chakra Petch","Arial Narrow",system-ui,sans-serif;color:#f1eee0}
footer.sf .brand img{width:42px;height:42px;object-fit:cover;border:1px solid #f7d417;clip-path:polygon(7px 0,calc(100% - 7px) 0,100% 7px,100% calc(100% - 7px),calc(100% - 7px) 100%,7px 100%,0 calc(100% - 7px),0 7px)}
footer.sf .tag{margin:14px 0 0;font:600 15px/1.3 "Chakra Petch",system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#f1eee0}
footer.sf h2{margin:0 0 14px;font:600 12px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.16em;text-transform:uppercase;color:#f7d417}
footer.sf ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
footer.sf a{color:#f1eee0;text-decoration:none;font:500 15px/1.3 "Barlow",system-ui,sans-serif}
footer.sf a:hover{color:#f7d417}
footer.sf code{display:block;margin-top:12px;font:400 12px/1.5 "JetBrains Mono",ui-monospace,monospace;color:#a29f8a;overflow-wrap:anywhere}
footer.sf .sf-legal{border-top:1px dashed #2c2c17;padding-top:20px;margin:0;font-size:13px;line-height:1.6;max-width:90ch}
footer.sf .sf-legal a{font:inherit;color:#f1eee0;text-decoration:underline}
@media (max-width:860px){footer.sf .sf-top{grid-template-columns:1fr 1fr}}
@media (max-width:480px){footer.sf .sf-top{grid-template-columns:1fr}}
'''
CSS = '<link rel="stylesheet" href="/assets/chrome.css">'


def header(current):
    cur = ' aria-current="page"'
    links = '\n'.join('<a href="%s"%s>%s</a>' % (h, cur if key == current and current != 'home' else '', t) for h, t, key in NAV)
    return f'''<header class="nav sf">
<div class="wrap">
<a class="brand" href="/" aria-label="ZFROG home"><img src="/media/logo.jpg" alt="" width="42" height="42">ZFROG</a>
<nav aria-label="Main">
{links}
</nav>
<a class="sf-buy" href="{BUY}" target="_blank" rel="noopener">Get $ZFROG</a>
</div>
</header>'''


FOOTER = f'''<footer class="sf">
<div class="wrap">
<div class="sf-top">
<div><a class="brand" href="/"><img src="/media/logo.jpg" alt="" width="42" height="42" loading="lazy">ZFROG</a><p class="tag">Made of memes. Powered by privacy.</p></div>
<nav aria-label="Explore"><h2>Explore</h2><ul>
<li><a href="/">Home</a></li><li><a href="/#rewards">Live rewards</a></li><li><a href="/earn-zama">Earn $ZAMA</a></li><li><a href="/fhe">FHE explained</a></li><li><a href="/frog-mark-1">FROG Mark 1</a></li><li><a href="/codex">The Pond Codex</a></li><li><a href="/agent">ZFROG Mark 1 agent</a></li><li><a href="/memes">Meme vault</a></li>
</ul></nav>
<nav aria-label="Community"><h2>Community</h2><ul>
<li><a href="https://x.com/FrogMark1" target="_blank" rel="noopener">X @FrogMark1</a></li><li><a href="https://t.me/ZFROGPortal" target="_blank" rel="noopener">Telegram</a></li><li><a href="https://t.me/addstickers/zfrog" target="_blank" rel="noopener">Sticker pack</a></li><li><a href="{RAW}brand/ZFROG_Brand_Book.pdf" target="_blank" rel="noopener">Brand book (PDF)</a></li><li><a href="{RAW}codex/ZFROG_Pond_Codex.pdf" target="_blank" rel="noopener">Pond Codex (PDF)</a></li>
</ul></nav>
<nav aria-label="Token"><h2>$ZFROG</h2><ul>
<li><a href="{BUY}" target="_blank" rel="noopener">Buy on Raydium</a></li><li><a href="https://dexscreener.com/solana/fpbmde3afu8ytcqs8vgh7zep7gsepfewx4hqcnduyoj1" target="_blank" rel="noopener">Chart on Dexscreener</a></li><li><a href="https://solscan.io/token/{CA}" target="_blank" rel="noopener">Contract on Solscan</a></li>
</ul><code>{CA}</code></nav>
</div>
<p class="sf-legal">$ZFROG is a community memecoin with no intrinsic value and no expectation of financial return. It is not affiliated with, endorsed by or operated by Zama. For official Zama information go to <a href="https://www.zama.org" rel="noopener">zama.org</a>. Crypto assets are highly volatile and you can lose everything you put in. Nothing on this site is financial advice. © 2026 ZFROG.</p>
</div>
</footer>'''


def unify(html, current):
    n_h = len(re.findall(r'<header class="nav">.*?</header>', html, flags=re.S))
    n_f = len(re.findall(r'<footer>.*?</footer>', html, flags=re.S))
    assert n_h <= 1 and n_f <= 1, (current, n_h, n_f)
    if n_h:
        html = re.sub(r'<header class="nav">.*?</header>', lambda m: CSS + '\n' + header(current), html, count=1, flags=re.S)
    else:  # 404
        html = html.replace('<main', CSS + '\n' + header(current) + '\n<main', 1)
    if n_f:
        html = re.sub(r'<footer>.*?</footer>', lambda m: FOOTER, html, count=1, flags=re.S)
    else:
        html = html.replace('</html>', FOOTER + '\n</html>', 1)
    return html
