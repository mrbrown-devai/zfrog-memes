import json, os
RAW='https://raw.githubusercontent.com/mrbrown-devai/zfrog-memes/main/'
CA='CZ4dvNHa15HybGwBMDaqWhtN4qVpHa9sayBBVrfxoH2T'
ZM='4Zp52aF4hZi9fzH19xpbWKYKQvgLyCN67KFbrQDqeTKh'
DISC='<p class="callout"><strong>Not Zama.</strong> $ZFROG is an independent community memecoin. It is not affiliated with, endorsed by or sponsored by Zama. For official Zama information, go to <a href="https://www.zama.org" rel="noopener">zama.org</a>.</p>'
pages=[]

# ---------------- /earn-zama
pages.append(dict(order=1, slug='earn-zama', crumb='Earn $ZAMA', eyebrow='Rewards guide',
 title='Earn $ZAMA by Holding $ZFROG on Solana | ZFROG',
 description='Hold at least $20 of $ZFROG on Solana and get $ZAMA sent to your wallet automatically. How the rewards work, how to buy on Raydium, and the risks.',
 h1='Earn $ZAMA by <em>holding $ZFROG.</em>', h1_plain='Earn $ZAMA by holding $ZFROG',
 lede='Hold the frog. Get $ZAMA. Nothing to claim, nothing to stake, nothing to lock.',
 hero_img='/media/portrait.jpg', hero_alt='ZFROG, the hooded frog, in a rain-soaked alley', schema_type='Article',
 about=['$ZFROG','$ZAMA','Zama','Solana','Raydium','stonk.fun'],
 faq=[
  ('How do I earn $ZAMA with $ZFROG?','Hold at least $20 worth of $ZFROG in a Solana wallet. $ZAMA from the reward pot is sent to you automatically, in proportion to your holdings.'),
  ('Do I need to claim or stake anything?','No. Distribution is automatic. There is nothing to claim and nothing to lock.'),
  ('Where does the $ZAMA come from?','From the 3% transfer fee on $ZFROG. About 2.5% covers network and operating costs; the rest is swapped to $ZAMA by stonk.fun and sent to holders.'),
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
<li><strong>About 2.5% covers network and operating costs.</strong> The rest goes into the reward pot.</li>
<li><strong>stonk.fun swaps the pot into $ZAMA.</strong></li>
<li><strong>$ZAMA is sent automatically,</strong> pro rata, to every wallet holding at least <strong>$20 of $ZFROG</strong>.</li>
</ol>
<p>No staking. No claim button. No lockup. If your wallet holds the minimum, $ZAMA shows up. More volume in the swamp means a bigger pot. The live total paid to holders is on the <a href="/#rewards">homepage counter</a>.</p>
<div class="tablewrap"><table>
<tr><th>Chain</th><td>Solana</td></tr>
<tr><th>Official $ZFROG contract</th><td><code>{CA}</code></td></tr>
<tr><th>Launched</th><td>3 October 2026</td></tr>
<tr><th>Main pool</th><td>Raydium</td></tr>
<tr><th>Reward token</th><td>$ZAMA (official Solana mint <code>{ZM}</code>)</td></tr>
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
pages.append(dict(order=2, slug='fhe', crumb='FHE explained', eyebrow='Learn',
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
pages.append(dict(order=3, slug='frog-mark-1', crumb='FROG Mark 1', eyebrow='Origins',
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

for p in pages:
    body=p.pop('body')
    with open(f'pages/{p["slug"]}.html','w',encoding='utf-8') as f:
        f.write(json.dumps(p,ensure_ascii=False)+'\n'+body)
print('ok')
