// Build step: site menu without Rewards, with NFT (Genesis) after Memes; footer, sitemap and llms.txt get the Genesis page.
const fs = require('fs');
const path = require('path');
function walk(dir, out) {
  for (const name of fs.readdirSync(dir)) {
    if (name === 'node_modules' || name.startsWith('.')) continue;
    const p = path.join(dir, name);
    const st = fs.statSync(p);
    if (st.isDirectory()) walk(p, out);
    else if (name.endsWith('.html')) out.push(p);
  }
  return out;
}
let n = 0;
for (const file of walk('.', [])) {
  let s = fs.readFileSync(file, 'utf8');
  const before = s;
  const isGenesis = path.normalize(file) === path.normalize('genesis/index.html');
  s = s.replace(/<nav aria-label="(Main|Site)">[\s\S]*?<\/nav>/, (nav) => {
    nav = nav.replace(/<a href="\/#rewards"[^>]*>Rewards<\/a>\n?/, '');
    if (!nav.includes('href="/genesis"')) {
      nav = nav.replace(/(<a href="\/memes"[^>]*>Memes<\/a>)/, '$1\n<a href="/genesis"' + (isGenesis ? ' aria-current="page"' : '') + '>NFT</a>');
    }
    return nav;
  });
  if (!s.includes('<li><a href="/genesis">')) {
    s = s.replace('<li><a href="/memes">Meme vault</a></li>', '<li><a href="/memes">Meme vault</a></li><li><a href="/genesis">Genesis NFT</a></li>');
  }
  if (s !== before) { fs.writeFileSync(file, s); n++; }
}
if (fs.existsSync('sitemap.xml')) {
  let x = fs.readFileSync('sitemap.xml', 'utf8');
  if (!x.includes('zfrog.xyz/genesis<')) {
    x = x.replace('</urlset>', '<url><loc>https://www.zfrog.xyz/genesis</loc><lastmod>2026-11-19</lastmod><changefreq>weekly</changefreq><priority>0.9</priority>\n</url>\n</urlset>');
    fs.writeFileSync('sitemap.xml', x);
  }
}
if (fs.existsSync('llms.txt')) {
  let t = fs.readFileSync('llms.txt', 'utf8');
  if (!t.includes('zfrog.xyz/genesis')) {
    const line = '- [ZFROG Genesis NFT](https://www.zfrog.xyz/genesis): the first ZFROG NFT collection, 284 hooded pixel frogs inspired by XCOPY, 100% onchain on Ethereum and minted shielded with Zama FHE. Contract 0x663f2eACeBc10a1Ea7c1Cb83ff328c6f4Ea219E1, trades on OpenSea, launched on Fungo Labs';
    t = t.replace(/(- \[Meme vault\][^\n]*\n)/, '$1' + line + '\n');
    if (!t.includes('zfrog.xyz/genesis')) t += '\n' + line + '\n';
    fs.writeFileSync('llms.txt', t);
  }
}
console.log('nav updated in ' + n + ' pages');
