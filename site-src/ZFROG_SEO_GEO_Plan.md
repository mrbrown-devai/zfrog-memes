# ZFROG: SEO and GEO plan

*Last updated 18 Oct 2026. Site: www.zfrog.xyz*

## Goal, honestly framed

Page 1 for bare **"Zama"**, **"FHE"**, **"$ZAMA"**, **"Zama airdrop"** or **"Zama staking"** isn't reachable. zama.org, Wikipedia, Coinbase, CoinGecko, CMC and the exchanges own those results.

The winnable game is the long tail around Zama, and being the source AI answer engines cite for anything ZFROG or frog-related.

| Horizon | Target queries |
|---|---|
| Weeks | ZFROG, $ZFROG, ZFROG contract, Zama memecoin, FROG Mark 1, earn ZAMA by holding, Zama frog / mascot, Zama memes |
| Months | how to buy ZAMA on Solana, bridge ZAMA Solana to Ethereum, how to get shielded on Zama, Zama confidential vaults explained, FHE explained simply |

## Already shipped (18 Oct 2026)

**Homepage**
- New title: "ZFROG ($ZFROG): the Zama-inspired frog memecoin that pays holders in $ZAMA"
- Canonical URL, OG and X share cards, Organization + WebSite JSON-LD (with the contract address and links to our X and Telegram)
- Internal links to the new pages

**New pages**
- **/earn-zama**: how rewards work, how to buy on Raydium, risks, FAQ, and the copycat warning
- **/fhe**: FHE explained by a frog
- **/frog-mark-1**: the origin story, with sources

**/memes**
- Keyword title and description, canonical, JSON-LD

**Site-wide files**
- **robots.txt**: explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended and the other main crawlers
- **sitemap.xml**
- **llms.txt**: a facts sheet for AI engines
- **Custom 404**

**Where things live**
- Site source and build script: GitHub repo `mrbrown-devai/zfrog-memes`, folder `site-src/`
- Share image: `brand/og-home.jpg` in the same repo

## Do this week (only you can)

1. **Google Search Console.**
   - Add `zfrog.xyz` as a Domain property (DNS TXT record at your registrar, or Vercel DNS if the domain uses it).
   - Submit `https://www.zfrog.xyz/sitemap.xml`.
   - Request indexing for /, /earn-zama, /fhe, /frog-mark-1 and /memes.
2. **Bing Webmaster Tools.** Import from Search Console in one click. Bing feeds ChatGPT search and Copilot, so this matters for GEO.
3. **Put zfrog.xyz everywhere the project lives.**
   - X @FrogMark1: bio and pinned post
   - Telegram: channel description and the pinned "single source of truth" post
   - DexScreener token info: website, X and Telegram (paid "Enhanced Token Info")
   - GeckoTerminal and Birdeye token profiles
   - Jupiter strict list or verified tag
4. **Listings.** Apply to CoinGecko, then CoinMarketCap. These rank for "ZFROG" and are the top sources AI engines cite for token facts. Use the exact same one-line description everywhere (see Entity line below).
5. **Push the copycat down.** Another "ZFROG" (`2QbdF…`) shows up first today. The fixes are listings with our contract address, plus the official-contract wording on our site, which is already live.

## GEO: getting cited by ChatGPT, Perplexity, Claude and Google AI Overviews

AI engines quote sources that are consistent, specific and corroborated by third parties.

**Entity line.** Use this exact sentence in every bio, listing, article and press mention:
> $ZFROG is a community memecoin on Solana that pays holders in $ZAMA, named after FROG Mark 1, Zama's first FPGA supercomputer for fully homomorphic encryption. Not affiliated with Zama. Contract: CZ4dvNHa15HybGwBMDaqWhtN4qVpHa9sayBBVrfxoH2T.

**Third-party corroboration** (highest leverage):
- One explainer post on Medium or Mirror, and one Reddit post in r/solana or r/CryptoMoonShots, linking to /frog-mark-1 and /earn-zama
- An X thread version of /fhe that links back to it
- Ask the stonk.fun team to list the zfrog.xyz URL on the ZFROG page

**Answer-first content.**
- Every new page opens with a one-sentence answer to the query it targets.
- Every new page ends with a FAQ.
- Dates and numbers sit next to their sources. AI engines prefer content they can quote verbatim.

**Freshness.**
- Update the "Updated" date and one fact on each guide when Zama ships news.
- Add each new page to sitemap.xml and llms.txt.

**Monthly check.**
- Ask ChatGPT, Perplexity, Claude and Google "What is ZFROG?", "What is FROG Mark 1?" and "Zama memecoin".
- Log who gets cited.
- Fix whatever source they get wrong.

## Content queue (next pages, in order)

1. **/guides/buy-zama-on-solana**: ZAMA on Solana via Sunrise. Official mint `4Zp52a…qeTKh`, Raydium and DFlow.
2. **/guides/shield-tokens-on-zama**: turn the existing X tutorial into a page.
3. **/guides/bridge-zama-solana-ethereum**
4. **/learn/confidential-vaults**: the Morpho vaults, plus the "$68M+ in confidential vaults" stat from Zama's newsletter.
5. **/zfrog**: the character page for ZFROG (Unit 01, created by FROG Mark 1), using renders only and following the brand book IP rules.

**Ride the news.** Publish a short explainer within 24 hours of each Zama milestone: Merkl confidential rewards claims, Developer Program Season 5, the Revolut Learn & Earn campaign, confidential apps on Solana.

## Technical backlog

- **Move the site to a GitHub → Vercel auto-deploy.** Put the media files (hero, machine, swamp and walk videos and posters) in the repo once, then every edit becomes a commit. Today, each deploy has to be pushed through the Vercel API.
- **Serve meme images from zfrog.xyz instead of raw.githubusercontent.com,** so Google Images credits our domain.
- **Per-meme pages (/memes/<id>)** with their own title and description, for image-search long tail.
- **Add an X/Telegram verification meta tag** once Search Console gives you one.

## Brand guardrails for all SEO work

- Never use Zama's logo, wordmark, colors or illustrations.
- Never title anything "Official Zama".
- Use "Zama" only as a description ("inspired by", "named after").
- Keep the not-affiliated line on every page.
- Link to zama.org for official facts.
- Rewards copy says rewards come from the transfer-fee mechanism. It never promises yield.
