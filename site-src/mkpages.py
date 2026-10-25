import json, os
RAW='https://raw.githubusercontent.com/mrbrown-devai/zfrog-memes/main/'
CA='CZ4dvNHa15HybGwBMDaqWhtN4qVpHa9sayBBVrfxoH2T'
ZM='4Zp52aF4hZi9fzH19xpbWKYKQvgLyCN67KFbrQDqeTKh'
DISC='<p class="callout"><strong>Not Zama.</strong> $ZFROG is an independent community memecoin. It is not affiliated with, endorsed by or sponsored by Zama. For official Zama information, go to <a href="https://www.zama.org" rel="noopener">zama.org</a>.</p>'
pages=[]

# ---------------- /earn-zama
pages.append(dict(order=1, slug='earn-zama', published='2026-10-18', crumb='Earn $ZAMA', eyebrow='Rewards guide',
 title='Earn $ZAMA by Holding $ZFROG on Solana | ZFROG',
 description='Hold at least $20 of $ZFROG on Solana and get $ZAMA sent to your wallet automatically. How the rewards work, how to buy on Raydium, and the risks.',
 h1='Earn $ZAMA by <em>holding $ZFROG.</em>', h1_plain='Earn $ZAMA by holding $ZFROG',
 lede='Hold the frog. Get $ZAMA. Nothing to claim, nothing to stake, nothing to lock.',
 hero_img='/media/portrait.jpg', hero_alt='ZFROG, the hooded frog, in a rain-soaked alley', schema_type='Article',
 about=['$ZFROG','$ZAMA','Zama','Solana','Raydium','stonk.fun'],
 faq=[
  ('How do I earn $ZAMA with $ZFROG?','Hold at least $20 worth of $ZFROG in a Solana wallet. $ZAMA from the reward pot is sent to you automatically, in proportion to your holdings.'),
  ('Do I need to claim or stake anything?','No. Distribution is automatic. There is nothing to claim and nothing to lock.'),
  ('Where does the $ZAMA come from?','From the 3% transfer tax on $ZFROG. 2.5% of that tax (0.075% of each transfer) covers network and operating costs. The other 2.925% is swapped to $ZAMA by stonk.fun and sent to holders.'),
  ('How much of the 3% tax goes to holders?','2.925%. 3% is collected on every transfer, 2.5% of that 3% (0.075%) pays network and operating costs, and 3% minus 0.075% = 2.925% is paid in $ZAMA to wallets holding at least $20 of $ZFROG. On a $1,000 trade that is $29.25 for holders.'),
  ('What is the official $ZFROG contract address?',f'{CA} on Solana. Ignore any other token using the ZFROG name.'),
  ('Which wallets work?','Any Solana wallet that supports Token-2022 tokens, including Phantom, Solflare and Backpack.'),
  ('Why does Raydium show a warning?','$ZFROG uses the Token-2022 standard. Raydium asks you to confirm before trading any Token-2022 token, and you add it by pasting the contract address.'),
  ('Is $ZFROG a Zama token?','No. It is an independent community memecoin named after FROG Mark 1, Zama\'s FPGA supercomputer. It is not affiliated with Zama.'),
  ('What can I do with the $ZAMA I earn?','Bridge it from Solana to Ethereum with Zama\'s official bridge, then shield it, swap cZAMA to cUSDT, earn yield on cUSDT, or stake $ZAMA with an operator. The 5-step guide is on this page.'),
  ('Do I need ETH to bridge $ZAMA to Ethereum?','Yes. Keep a little ETH in your Ethereum wallet for gas, and a little SOL on Solana for the bridge transaction.'),
 ],
 body=f'''<h2>How the rewards work</h2>
<p>$ZFROG is a Solana Token-2022 token with a transfer fee built in. Here is the loop:</p>
<ol>
<li><strong>3% is withheld on every transfer.</strong> Buys, sells and wallet-to-wallet moves all count. This uses Solana's <a href="https://solana.com/docs/tokens/extensions/transfer-fees" rel="noopener">Token-2022 transfer fee extension</a>.</li>
<li><strong>2.5% of that 3% covers network and operating costs.</strong> That is 0.075% of each transfer, not 2.5 points.</li>
<li><strong>The other 2.925% goes into the reward pot.</strong> That is what holders receive.</li>
<li><strong>stonk.fun swaps the pot into $ZAMA.</strong></li>
<li><strong>$ZAMA is sent automatically,</strong> pro rata, to every wallet holding at least <strong>$20 of $ZFROG</strong>.</li>
</ol>
<p>No staking. No claim button. No lockup. If your wallet holds the minimum, $ZAMA shows up. More volume in the swamp means a bigger pot. The live total paid to holders is on the <a href="/#rewards">homepage counter</a>.</p>
<h3>Where the 3% goes</h3>
<div class="tablewrap"><table>
<tr><th></th><th>Share of each transfer</th><th>On a $1,000 trade</th></tr>
<tr><th>Transfer tax collected</th><td>3%</td><td>$30.00</td></tr>
<tr><th>Network and operating costs (2.5% of the tax)</th><td>0.075%</td><td>$0.75</td></tr>
<tr><th>Paid to holders in $ZAMA</th><td>2.925%</td><td>$29.25</td></tr>
</table></div>
<p>To receive your share, hold at least <strong>$20 of $ZFROG</strong>. The $ZAMA is split pro rata between every eligible wallet.</p>
<div class="tablewrap"><table>
<tr><th>Chain</th><td>Solana</td></tr>
<tr><th>Official $ZFROG contract</th><td><code>{CA}</code></td></tr>
<tr><th>Launched</th><td>3 October 2026</td></tr>
<tr><th>Main pool</th><td>Raydium</td></tr>
<tr><th>Reward token</th><td>$ZAMA (official Solana mint <code>{ZM}</code>)</td></tr>
<tr><th>Transfer tax</th><td>3% (2.925% to holders, 0.075% to costs)</td></tr>
<tr><th>Minimum to earn</th><td>$20 of $ZFROG</td></tr>
</table></div>
<h2>How to buy $ZFROG on Raydium</h2>
<ol>
<li><strong>Get a Solana wallet.</strong> Phantom, Solflare or Backpack all work. Write your seed phrase down offline and never share it.</li>
<li><strong>Fund it with SOL.</strong> Buy SOL on an exchange and withdraw it to your wallet. Keep a little extra for network fees.</li>
<li><strong>Open Raydium.</strong> Type raydium.io yourself or use your wallet's in-app browser. Fake Raydium sites exist.</li>
<li><strong>Connect your wallet.</strong></li>
<li><strong>Paste the contract address</strong> <code>{CA}</code> into the token field. Raydium does not list Token-2022 tokens by name search.</li>
<li><strong>Accept the Token-2022 notice.</strong> Raydium shows a risk prompt for Token-2022 tokens. Confirm it to unlock the pool.</li>
<li><strong>Swap SOL for $ZFROG.</strong> The 3% transfer fee comes off what lands in your wallet.</li>
<li><strong>Hold at least $20 worth.</strong> You are in the pond.</li>
</ol>
<p><a class="btn btn-primary chip" href="https://raydium.io/swap/?inputMint=sol&amp;outputMint={CA}" target="_blank" rel="noopener">Open $ZFROG on Raydium</a></p>
<blockquote><strong>Watch out for copycats.</strong> At least one other Solana token uses the ZFROG name (<code>2QbdFYSVpksupj1BnAwgn7xs5RQi5AHm3Wk1kFn2yqvK</code>). It is not us. Always match the full contract address above.</blockquote>
<h2 id="shielded">What to do with your $ZAMA: get fully shielded</h2>
<p>Your $ZFROG earns $ZAMA on Solana. That is half the stack. To shield, swap, earn and stake, $ZAMA has to be on Ethereum for now. Five steps, one Ethereum wallet. Each step has a short video on <a href="https://x.com/FrogMark1/status/2109340658666221591" target="_blank" rel="noopener">our X series</a>.</p>
<ol class="steps-guide">
<li><strong>Bridge $ZAMA from Solana to Ethereum.</strong> Open <a href="https://bridge.zama.org" rel="noopener">bridge.zama.org</a>, connect your Solana wallet and your Ethereum wallet, and send your $ZAMA across. Keep some SOL for the Solana side and some ETH for gas on Ethereum. <a href="https://x.com/FrogMark1/status/2107203182447198533" target="_blank" rel="noopener">Watch step 1</a>.</li>
<li><strong>Shield (and unshield) $ZAMA.</strong> In the <a href="https://app.zama.org" rel="noopener">Zama App</a>, Shield turns $ZAMA into cZAMA, a confidential balance only you can read. Unshield brings it back to a public balance when you need it. Same wallet, two states. <a href="https://x.com/FrogMark1/status/2107569388794658872" target="_blank" rel="noopener">Watch step 2</a>.</li>
<li><strong>Swap cZAMA to cUSDT.</strong> Still in the <a href="https://app.zama.org" rel="noopener">Zama App</a>, swap without leaving the confidential state. Amounts and balances stay encrypted. Private in, private out. <a href="https://x.com/FrogMark1/status/2108318923355455653" target="_blank" rel="noopener">Watch step 3</a>.</li>
<li><strong>Earn yield with cUSDT.</strong> On <a href="https://app.zama.org/earn" rel="noopener">app.zama.org/earn</a>, deposit cUSDT and earn yield on Ethereum, with amounts still encrypted. <a href="https://x.com/FrogMark1/status/2108707055099932719" target="_blank" rel="noopener">Watch step 4</a>.</li>
<li><strong>Stake $ZAMA.</strong> On <a href="https://staking.zama.org" rel="noopener">staking.zama.org</a>, delegate $ZAMA to an operator to help secure the protocol and earn staking rewards. Staking uses regular (non-confidential) $ZAMA, so unshield first if needed. <a href="https://x.com/FrogMark1/status/2109315114369163325" target="_blank" rel="noopener">Watch step 5</a>.</li>
</ol>
<p>Type these addresses yourself and check the domain is <code>zama.org</code>. Yield and staking rewards are set by those protocols, not by ZFROG, and are never guaranteed. Bridging, swaps and deposits each cost network fees.</p>
<h2>Risks</h2>
<p>Read this before you buy.</p>
<ul>
<li><strong>Memecoins are very risky.</strong> The price can go toward zero. Only put in what you can afford to lose.</li>
<li><strong>Rewards are not guaranteed.</strong> They depend on trading volume, the $ZAMA price and the stonk.fun mechanism working as intended.</li>
<li><strong>The 3% fee hits every transfer.</strong> Flipping in and out costs you each time.</li>
<li><strong>The $20 minimum moves with price.</strong> If $ZFROG drops, your bag can fall under the line and stop earning until you top up.</li>
<li><strong>Third-party risk.</strong> Raydium, stonk.fun and Solana are outside our control.</li>
<li><strong>Exchange wallets may not count.</strong> Rewards go to onchain holder wallets. Keep your $ZFROG in your own wallet.</li>
<li><strong>Scams.</strong> We never DM first, never ask for your seed phrase and never ask you to "validate" a wallet.</li>
</ul>
<h2>What is $ZAMA, anyway?</h2>
<p>$ZAMA is the token of the Zama Confidential Blockchain Protocol, which uses fully homomorphic encryption to keep balances and transfers private on public chains. It pays protocol fees and secures the network through staking. It has traded since 2 February 2026 and lives on Ethereum, BNB Chain and Solana. New to all this? Start with <a href="/fhe">FHE explained by a frog</a>.</p>
{DISC}'''))

# ---------------- /fhe
pages.append(dict(order=2, slug='fhe', published='2026-10-18', crumb='FHE explained', eyebrow='Learn',
 title='FHE Explained by a Frog: an Unofficial Guide to Zama FHE | ZFROG',
 description='What is fully homomorphic encryption? A plain-language guide to FHE, how Zama uses it onchain, why it needs serious hardware and where $ZAMA fits.',
 h1='FHE explained <em>(by a frog).</em>', h1_plain='FHE explained (by a frog)',
 lede='ZFROG here. Unit 01. I live in the swamp and I compute on things I cannot see. Let me explain how.',
 hero_img=RAW+'memes/lore/reading-the-ancient-book.jpg', hero_alt='ZFROG the hooded frog peeking over an ancient book of encryption diagrams', hero_w=1536, hero_h=1024,
 schema_type='Article', about=['Fully homomorphic encryption','FHE','Zama','FHEVM','TFHE','Confidential tokens','ERC-7984'],
 faq=[
  ('What is FHE in one sentence?','Encryption that lets you compute on data while it stays encrypted, so whoever processes it never sees it.'),
  ('Is FHE the same as zero-knowledge proofs?','No. ZK proves a statement is true without revealing the data. FHE computes on hidden data. Zama uses both: ZK proofs check encrypted inputs.'),
  ('Who invented FHE?','Craig Gentry published the first plausible fully homomorphic scheme in 2009. Zama builds on TFHE, published in 2016.'),
  ('Does Zama have its own blockchain?','No. Zama is a confidentiality layer on top of existing chains. Its Gateway runs on a dedicated Arbitrum rollup.'),
  ('Which chains does Zama support?','Confidential apps run on Ethereum mainnet. $ZAMA itself can be bridged across Ethereum, BNB Chain and Solana. Zama has said confidential apps on more chains are coming.'),
  ('Why is FHE slow?','Ciphertexts are large and bootstrapping is compute-heavy. That is why Zama is moving from CPUs to GPUs, FPGAs and eventually dedicated ASICs.'),
  ('Is FHE quantum-safe?','Zama describes FHE as already post-quantum, because it is built on lattice problems rather than the math quantum computers threaten.'),
 ],
 body='''<h2>What is fully homomorphic encryption?</h2>
<p>Normal encryption is a locked box. You can store it and send it. But to do anything with what is inside, you have to open it, and the moment you open it, whoever is doing the work sees everything.</p>
<p>Fully homomorphic encryption (FHE) changes that. You can run computations on encrypted data <strong>without decrypting it</strong>. The result stays encrypted. Only the key holder can read it, and it matches what you would get from doing the same math on the raw data.</p>
<blockquote>Lock the box. Do math on the box. Open the box. The right answer is inside. Nobody in the middle saw a thing.</blockquote>
<h2>A 30-second history</h2>
<p>Cryptographers chased this idea for decades. In 2009 Craig Gentry published the first plausible fully homomorphic scheme, built on lattice-based cryptography.</p>
<p>The catch was noise. Every operation on a ciphertext adds a little, and too much makes the data unreadable. Gentry's fix was <strong>bootstrapping</strong>: the scheme runs its own decryption circuit while the data stays encrypted, producing a fresh, low-noise ciphertext. Refresh often enough and you can compute forever.</p>
<p>In 2016, Ilaria Chillotti, Nicolas Gama, Mariya Georgieva and Malika Izabachène published <strong>TFHE</strong>, a scheme with much faster bootstrapping. TFHE is the family Zama builds on, through its TFHE-rs library.</p>
<h2>Why FHE matters onchain</h2>
<p>Public blockchains are glass houses. Every balance, trade and salary payment is visible to anyone with a block explorer. Fine for memes. Fatal for most real finance.</p>
<p>FHE lets a public chain stay verifiable and get privacy too:</p>
<ul>
<li><strong>Confidential balances.</strong> Your token balance is encrypted onchain.</li>
<li><strong>Private transfers.</strong> Amounts stay hidden while the contract still checks you can afford them.</li>
<li><strong>Sealed-bid auctions, private voting, payroll.</strong> Logic runs on data nobody can peek at.</li>
<li><strong>Selective disclosure.</strong> You choose who can decrypt, such as an auditor.</li>
</ul>
<h2>How does Zama work?</h2>
<p>Zama builds the <strong>Zama Confidential Blockchain Protocol</strong>. It is not a new L1 or L2. It is a confidentiality layer that plugs into chains that already exist.</p>
<ul>
<li><strong>FHEVM library.</strong> Developers write confidential smart contracts in plain Solidity.</li>
<li><strong>Symbolic execution.</strong> The host chain does not run the heavy FHE math. It stores pointers and emits events.</li>
<li><strong>Coprocessors.</strong> Offchain operators pick up those events, run the FHE computations in parallel and store the ciphertexts.</li>
<li><strong>Gateway.</strong> Coordinates input checks, decryption and bridging, on a dedicated Arbitrum rollup.</li>
<li><strong>Threshold key management.</strong> The decryption key is split across 13 MPC nodes, and a threshold of them (9 of 13 in Zama's docs) must cooperate to decrypt. Nothing is decrypted unless the contract allows it.</li>
<li><strong>Access control.</strong> Tracks who may compute on or decrypt each ciphertext.</li>
</ul>
<p>Source: the <a href="https://docs.zama.org/protocol/zama-protocol-litepaper" rel="noopener">Zama Protocol litepaper</a>.</p>
<h2>Confidential tokens and shielding</h2>
<p>The flagship use case is the confidential token. Zama and OpenZeppelin implemented <strong>ERC-7984</strong>, a confidential version of the ERC-20 standard. Balances and transfer amounts are encrypted with FHE, so even the smart contract does not know your balance.</p>
<p>You <strong>shield</strong> a regular token by wrapping it into its confidential version. The amount is visible going in and encrypted after that. <strong>Unshielding</strong> takes an explicit decryption step. Official wrappers are live on Ethereum for tokens including USDC, USDT, WETH and ZAMA, and the Zama App has Shield and Unshield built in.</p>
<h2>Why FHE needs serious hardware</h2>
<p>FHE is heavy. Bootstrapping on a CPU is slow, and slow means low throughput. Zama's litepaper lays out the roadmap:</p>
<div class="tablewrap"><table>
<tr><th>Hardware</th><th>Throughput per chain</th></tr>
<tr><td>CPU (today)</td><td>20+ TPS</td></tr>
<tr><td>GPU</td><td>Zama has shown up to about 1,000 TPS on GPUs</td></tr>
<tr><td>FPGA and ASIC</td><td>The longer-term target: thousands of TPS and more, on dedicated FHE hardware</td></tr>
</table></div>
<p>In May 2025 Zama open-sourced the <strong>HPU</strong> (Homomorphic Processing Unit), an FHE processor running on an AMD V80 FPGA board, at about 13,000 programmable bootstraps per second for about 200W. That is the family of hardware my creator, FROG Mark 1, comes from. The whole story is on the <a href="/frog-mark-1">FROG Mark 1 page</a>.</p>
<blockquote>Compute without looking. Protect without collecting. <a href="/codex#ch-v">From the Pond Codex</a>.</blockquote>
<h2>Where does $ZAMA fit?</h2>
<p>$ZAMA is the protocol token:</p>
<ul>
<li><strong>Fees.</strong> Encryption, decryption, proof verification and bridging are priced in USD and paid in $ZAMA. Apps can pay on your behalf, so users do not have to hold it.</li>
<li><strong>Staking.</strong> Operators and delegators stake $ZAMA to secure the network and earn rewards.</li>
</ul>
<p>$ZAMA started trading on 2 February 2026 and lives on Ethereum, BNB Chain and Solana. Want some without buying it directly? <a href="/earn-zama">Hold $ZFROG and earn $ZAMA</a>. ZRIBBIT.</p>
'''+DISC))

# ---------------- /frog-mark-1
pages.append(dict(order=3, slug='frog-mark-1', published='2026-10-18', crumb='FROG Mark 1', eyebrow='Origins',
 title="FROG Mark 1: Zama's FPGA Supercomputer | ZFROG",
 description="FROG Mark 1 is the name of Zama's first FPGA supercomputer for fully homomorphic encryption. What is public, what is not, and how it spawned $ZFROG.",
 h1='FROG Mark 1: <em>Zama\'s FPGA supercomputer.</em>', h1_plain="FROG Mark 1: Zama's FPGA supercomputer",
 lede='Every frog has an origin story. Mine is a rack of hardware.',
 hero_img='/media/machine-poster.jpg', hero_alt='Racks of FPGA hardware: the machine that inspired ZFROG', schema_type='Article',
 about=['FROG Mark 1','Zama','FPGA','HPU','Fully homomorphic encryption','AMD Alveo V80'],
 faq=[
  ('What is FROG Mark 1?','The name given to Zama\'s first FPGA supercomputer for fully homomorphic encryption, shared by Zama CEO Rand Hindi on X on 25 June 2025.'),
  ('What hardware does Zama use for FHE acceleration?','Zama\'s open-source HPU runs on an AMD V80 FPGA board. Zama also uses GPUs, and its roadmap includes dedicated FHE ASICs.'),
  ('How many FPGA cards are in FROG Mark 1?','That number is not public. We have not seen a verified figure.'),
  ('How fast is Zama\'s FPGA accelerator?','Zama reports about 13,000 programmable bootstraps per second per HPU, at about 200W.'),
  ('Is the HPU open source?','Yes. Zama open-sourced the full HPU stack, including the SystemVerilog, in May 2025.'),
  ('Is $ZFROG made by Zama?','No. $ZFROG is an independent community memecoin inspired by the machine\'s name.'),
 ],
 body='''<h2>What is FROG Mark 1?</h2>
<p>FROG Mark 1 is the name of Zama's first FPGA supercomputer for fully homomorphic encryption. Zama CEO Rand Hindi shared it on X on 25 June 2025, the same day Zama announced a $57M Series B that pushed its valuation past $1 billion.</p>
<p><a class="btn btn-ghost chip" href="https://x.com/randhindi/status/1938010202235687040" target="_blank" rel="noopener">See Rand Hindi's original post</a></p>
<p>The purpose is simple. FHE is very heavy to compute, and dedicated hardware makes it fast enough for real onchain use.</p>
<h2>The hardware behind it: Zama's HPU</h2>
<p>On 21 May 2025 Zama announced the <strong>HPU on FPGA</strong>, which it called the first open-source hardware accelerator for FHE. What Zama published:</p>
<ul>
<li><strong>A full processor for encrypted data,</strong> with a register file, control logic and an arithmetic unit that runs instruction streams on encrypted operands.</li>
<li><strong>A programmable bootstrapping module.</strong> Bootstrapping is the expensive step in FHE, and this is where it gets accelerated.</li>
<li><strong>The board:</strong> an AMD V80, a 7nm FPGA with two HBM2e memory stacks, running at 350 MHz.</li>
<li><strong>Throughput:</strong> about 13,000 programmable bootstraps per second at about 200W.</li>
<li><strong>Open source:</strong> the whole stack, driven through the HPU backend in TFHE-rs.</li>
<li><strong>Next step:</strong> Zama said it was working on multi-HPU servers.</li>
</ul>
<p>Source: <a href="https://www.zama.org/post/announcing-hpu-on-fpga-the-first-open-source-hardware-accelerator-for-fhe" rel="noopener">Zama, Announcing HPU on FPGA</a>. The AMD Alveo V80 itself is a data-center accelerator card with about 820 GB/s of memory bandwidth and PCIe Gen5 (<a href="https://www.amd.com/en/products/accelerators/alveo/v80.html" rel="noopener">AMD</a>).</p>
<h3>What is not public</h3>
<p>We do not make up specs in the pond. These details have not been published:</p>
<ul>
<li>How many FPGA cards FROG Mark 1 holds.</li>
<li>Which exact boards are inside, although the V80 is Zama's published HPU platform.</li>
<li>Total throughput, power draw or where the machine sits.</li>
</ul>
<p>If Zama publishes more, this page gets updated.</p>
<h2>Why it matters for Zama</h2>
<p>Zama's litepaper puts current CPU throughput at more than 20 TPS per chain. Zama has shown up to about 1,000 TPS on GPUs, and its longer-term target is far higher throughput on FPGAs and dedicated FHE ASICs.</p>
<p>FPGAs are the bridge. They are reprogrammable silicon, so you can prove an FHE processor design in real hardware before spending big on a custom chip. FROG Mark 1 is that bridge, with a name. Want the basics first? Read <a href="/fhe">FHE explained by a frog</a>.</p>
<h2>From rack to frog</h2>
<p>Most memecoins invent a story. $ZFROG started from a real machine.</p>
<p>A hardware lab named its FHE supercomputer FROG. Crypto noticed. The swamp did the rest.</p>
<p><strong>ZFROG</strong>, Unit 01, is the main character, and in our lore FROG Mark 1 is his creator: the machine made the frog. He is a black and yellow hooded frog with a respirator mask and a glowing Z chip on his chest. He speaks through the respirator. He computes on things he cannot see. He is here to get the world ready for the privacy age. Meet him in the <a href="/memes">meme vault</a> and the <a href="/#brandbook">brand book</a>. His full story, from the watched city to the birth on the lily, is in <a href="/codex">the Pond Codex</a> (<a href="/codex#ch-ii">Chapter II, The machine</a>).</p>
<p>$ZFROG launched on Solana on 3 October 2026, and holders earn $ZAMA automatically. <a href="/earn-zama">Here is how</a>.</p>
'''+DISC))

# ---------------- /agent
AGENT_JSON=RAW+'data/agent.json'
pages.append(dict(order=4, slug='agent', published='2026-10-20', crumb='The agent', eyebrow='ZFROG Mark 1',
 title='ZFROG Mark 1: the Agent That Earns on Zama, in Public | ZFROG',
 description="ZFROG Mark 1 is ZFROG's autonomous agent. It bridges $ZAMA to Ethereum, stakes it with Zama Protocol operators and deposits into Zama confidential vaults. Every move is logged here.",
 h1='The night shift: <em>ZFROG Mark 1.</em>', h1_plain='The night shift: ZFROG Mark 1',
 lede='I built myself a worker. It bridges, it stakes, it shields, and it reports. Every move is on this page.',
 hero_img='/media/council.jpg', hero_alt='ZFROG crouched on a lily pad beside a server, surrounded by hooded frogs in a dark pond', hero_w=1200, hero_h=675,
 schema_type='Article', about=['ZFROG Mark 1','AI agent','Zama Protocol','Staking','Confidential vaults','$ZAMA'],
 faq=[
  ('What is ZFROG Mark 1?','An autonomous agent run by the ZFROG team. It bridges $ZAMA from Solana to Ethereum, stakes about half with the Zama Protocol operator offering the best net APR, and puts the other half to work in Zama confidential vaults. It runs twice a day and reviews its positions every Monday.'),
  ('Whose money is it?','A separate pool funded by the ZFROG team, not the holder reward pot. The 3% transfer fee on $ZFROG is collected, swapped to $ZAMA and distributed to holders by the stonk.fun contract on Solana; the agent never touches it.'),
  ('Can I see the positions on-chain?','Yes. The agent wallets are listed on this page with explorer links. Staking positions are public. Confidential vault balances are encrypted by design; the deposit transactions are public.'),
  ('Does the agent trade $ZFROG or move the price?','No. It only bridges, stakes, shields and deposits $ZAMA and stablecoins on Zama infrastructure. It never buys or sells $ZFROG.'),
  ('Is the yield going to holders?','Not today. Rewards accrue to the agent pool. Any change to that would be announced on X and in the Telegram before it happens, never promised in advance.'),
  ('Is this a Zama product?','No. The agent uses Zama\'s public protocol and app like any user. ZFROG is not affiliated with Zama.'),
 ],
 body=f'''<style>
.live{{display:grid;gap:14px;margin:0 0 28px}}
.live .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
.stat{{background:var(--panel);box-shadow:inset 0 0 0 1px var(--line);padding:18px 20px;display:grid;gap:6px;--notch:10px}}
.stat .k{{font:600 11px/1.3 var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}}
.stat .v{{font:700 clamp(24px,3vw,34px)/1.05 var(--display);color:var(--fg)}}
.stat .v small{{font:500 14px/1 var(--display);color:var(--toxic);margin-left:6px}}
.stat .s{{font:400 13px/1.4 var(--body);color:var(--muted)}}
.pos{{display:grid;gap:12px}}
.pos .card{{background:var(--bog);box-shadow:inset 3px 0 0 var(--toxic);padding:16px 20px;display:grid;gap:4px}}
.pos .card b{{font:700 18px/1.2 var(--display);text-transform:uppercase}}
.pos .card span{{color:var(--muted);font-size:15px}}
.wal{{display:grid;gap:8px;font:400 13px/1.5 var(--mono);color:var(--muted)}}
.wal a{{color:var(--fg);overflow-wrap:anywhere}}
.stamp{{font:500 12px/1.4 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}}
.stamp b{{color:var(--toxic)}}
.ledger td:first-child{{white-space:nowrap;font-family:var(--mono);font-size:13px}}
.ledger .a{{font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--toxic)}}
</style>
<p class="callout"><strong>Two different pots.</strong> The <a href="/#rewards">homepage counter</a> is the holder reward pot: $ZFROG's 3% fee, swapped to $ZAMA and sent to holders by stonk.fun. This page is something else: a separate pool the team put to work on Zama's protocol through an agent. It never touches holder rewards.</p>
<div class="live" id="live">
<p class="stamp" id="stamp">Loading the night shift report…</p>
<div class="grid" id="stats"></div>
<div class="pos" id="positions"></div>
<div class="wal" id="wallets"></div>
</div>
<h2>What the agent does</h2>
<p>ZFROG Mark 1 is a small program that runs on a machine the team controls. Twice a day it wakes up, looks at its wallets, and follows five rules:</p>
<ol>
<li><strong>Bridge.</strong> Any $ZAMA sitting on Solana goes to Ethereum through Zama's official LayerZero bridge, because that is where staking and the confidential vaults live.</li>
<li><strong>Stake half.</strong> About half of each batch is delegated to the Zama Protocol operator with the best net APR after commission. The agent scans every operator each run.</li>
<li><strong>Shield the rest.</strong> The other half is swapped to a stablecoin, shielded into its confidential version, and deposited into the Zama confidential vault with the best yield.</li>
<li><strong>Review on Mondays.</strong> Once a week it compares vault yields and operator rates and moves funds only if the gap is worth the fees.</li>
<li><strong>Report.</strong> Every action, with the transaction hash, is logged. The log feeds this page.</li>
</ol>
<h2>Ledger</h2>
<div class="tablewrap"><table class="ledger" id="ledger"><tr><th>Date</th><th>Action</th><th>Detail</th><th>Tx</th></tr></table></div>
<p id="ledger-note" class="stamp"></p>
<h2>How it is kept safe</h2>
<ul>
<li><strong>Keys never leave the machine.</strong> The wallets were generated locally and are stored encrypted. No AI model and no cloud service has ever seen them.</li>
<li><strong>Allowlist only.</strong> The agent can only talk to Zama Protocol contracts, the official bridge and the swap route it uses. Any other address is refused by the code.</li>
<li><strong>Caps.</strong> Each transaction has a hard USD ceiling. A bad day is a small day.</li>
<li><strong>Dry-run by default.</strong> New logic ships in simulation mode first and only signs after a human reads the dry run.</li>
<li><strong>Separate pool.</strong> The holder reward pot is handled by the stonk.fun contract on Solana and is not reachable by the agent.</li>
</ul>
<h2>Why build it</h2>
<p>Most memecoins have a chart and a Telegram. The Pond wanted a product. ZFROG Mark 1 is proof that one frog, a public protocol and a few hundred lines of code can earn on Zama's stack without trusting anyone to hold the keys. It is also the easiest way to show what shielding, confidential vaults and staking actually look like when they run every day. Want to do it by hand? The <a href="/earn-zama#shielded">five-step guide</a> walks the same path.</p>
<p>Yields quoted on this page are read from the protocols at the time of each run. They change, and nothing here is a promise.</p>
{DISC}
<script>
(function(){{
var SRC='{AGENT_JSON}';
var ETH_RPC='https://ethereum-rpc.publicnode.com', SOL_RPC='https://api.mainnet-beta.solana.com';
var ZAMA_ETH='0xa12cc123ba206d4031d1c7f6223d1c2ec249f4f3', ZAMA_SOL='{ZM}';
function el(id){{return document.getElementById(id)}}
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function num(n,d){{return Number(n).toLocaleString('en-US',{{maximumFractionDigits:d==null?2:d}})}}
function short(a){{return a.slice(0,6)+'…'+a.slice(-4)}}
function rpc(url,method,params){{return fetch(url,{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify({{jsonrpc:'2.0',id:1,method:method,params:params}})}}).then(function(r){{return r.json()}}).then(function(j){{return j.result}})}}
function stat(k,v,unit,s){{return '<div class="stat chip"><span class="k">'+esc(k)+'</span><span class="v">'+esc(v)+(unit?'<small>'+esc(unit)+'</small>':'')+'</span>'+(s?'<span class="s">'+esc(s)+'</span>':'')+'</div>'}}
fetch(SRC,{{cache:'no-store'}}).then(function(r){{return r.json()}}).then(function(d){{
  var t=d.totals||{{}};
  var when=d.updated?new Date(d.updated):null;
  el('stamp').innerHTML='Last report <b>'+(when?esc(when.toUTCString().replace(':00 GMT',' UTC')):'n/a')+'</b> · mode <b>'+esc(d.mode||'?')+'</b> · '+esc(d.cadence||'');
  el('stats').innerHTML=stat('ZAMA staked',num(t.zama_staked),'ZAMA','with Zama Protocol operators')+stat('In confidential vaults',num(t.usdc_in_vaults),'USDC','balance encrypted on-chain')+stat('ZAMA bridged to date',num(t.zama_bridged),'ZAMA','Solana to Ethereum')+stat('Rewards claimed',num(t.rewards_claimed_zama),'ZAMA','staking rewards to date');
  el('positions').innerHTML=(d.positions||[]).map(function(p){{var rate=p.apr!=null?num(p.apr,1)+'% APR':(p.apy!=null?num(p.apy,1)+'% APY':'');return '<div class="card"><b>'+esc(p.venue)+'</b><span>'+num(p.amount)+' '+esc(p.asset)+(rate?' · about '+rate:'')+(p.since?' · since '+esc(p.since):'')+'</span><span>'+esc(p.note||'')+(p.url?' <a href="'+esc(p.url)+'" rel="noopener" target="_blank">'+esc(p.protocol)+'</a>':'')+'</span></div>'}}).join('');
  var w=d.wallets||{{}}; var rows=[];
  if(w.ethereum) rows.push('<div>Ethereum wallet <a href="https://etherscan.io/address/'+esc(w.ethereum)+'" target="_blank" rel="noopener">'+esc(w.ethereum)+'</a> <span id="ethbal"></span></div>');
  if(w.solana) rows.push('<div>Solana wallet <a href="https://solscan.io/account/'+esc(w.solana)+'" target="_blank" rel="noopener">'+esc(w.solana)+'</a> <span id="solbal"></span></div>');
  if(!rows.length) rows.push('<div>Wallet addresses are published here once the next cycle runs.</div>');
  el('wallets').innerHTML=rows.join('');
  var L=(d.ledger||[]).slice().reverse();
  el('ledger').insertAdjacentHTML('beforeend',L.map(function(e){{return '<tr><td>'+esc(e.date)+'</td><td><span class="a">'+esc(e.action)+'</span></td><td>'+esc(e.detail)+'</td><td>'+(e.tx?'<a href="'+esc(e.tx)+'" target="_blank" rel="noopener">view</a>':'—')+'</td></tr>'}}).join(''));
  el('ledger-note').textContent=L.length+' actions logged. Newest first.';
  if(w.ethereum){{
    var pad='000000000000000000000000'+w.ethereum.slice(2).toLowerCase();
    Promise.all([rpc(ETH_RPC,'eth_getBalance',[w.ethereum,'latest']),rpc(ETH_RPC,'eth_call',[{{to:ZAMA_ETH,data:'0x70a08231'+pad}},'latest'])]).then(function(r){{
      var eth=parseInt(r[0],16)/1e18, z=parseInt(r[1],16)/1e18;
      el('ethbal').textContent='· live: '+num(eth,4)+' ETH, '+num(z)+' ZAMA idle';
    }}).catch(function(){{}});
  }}
  if(w.solana){{
    Promise.all([rpc(SOL_RPC,'getBalance',[w.solana]),rpc(SOL_RPC,'getTokenAccountsByOwner',[w.solana,{{mint:ZAMA_SOL}},{{encoding:'jsonParsed'}}])]).then(function(r){{
      var sol=(r[0]&&r[0].value||0)/1e9; var z=0;(r[1]&&r[1].value||[]).forEach(function(a){{z+=Number(a.account.data.parsed.info.tokenAmount.uiAmount||0)}});
      el('solbal').textContent='· live: '+num(sol,4)+' SOL, '+num(z)+' ZAMA waiting to bridge';
    }}).catch(function(){{}});
  }}
}}).catch(function(){{el('stamp').textContent='The report could not be loaded. Try again in a minute.'}});
}})();
</script>'''))

for p in pages:
    body=p.pop('body')
    with open(f'pages/{p["slug"]}.html','w',encoding='utf-8') as f:
        f.write(json.dumps(p,ensure_ascii=False)+'\n'+body)
print('ok')
