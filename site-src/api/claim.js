// Breakpoint London airdrop sign-up. POST registers an entry, GET returns the public count.
// Entries are private blobs: breakpoint/w/<wallet>.json, plus breakpoint/x/<handle> markers for dedupe.
const { put, list, head, BlobNotFoundError } = require('@vercel/blob');
const crypto = require('crypto');

const B58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';
function b58Bytes(s) {
  let n = 0n;
  for (const c of s) { const i = B58.indexOf(c); if (i < 0) return -1; n = n * 58n + BigInt(i); }
  let bytes = 0; while (n > 0n) { n >>= 8n; bytes++; }
  for (const c of s) { if (c === '1') bytes++; else break; }
  return bytes;
}
function send(res, code, obj, cache) {
  res.statusCode = code;
  res.setHeader('content-type', 'application/json; charset=utf-8');
  res.setHeader('cache-control', cache || 'no-store');
  res.end(JSON.stringify(obj));
}
async function exists(pathname) {
  try { await head(pathname); return true; } catch (e) {
    if ((BlobNotFoundError && e instanceof BlobNotFoundError) || /not.?found|does not exist/i.test(String(e && e.message))) return false;
    throw e;
  }
}
async function count() {
  let n = 0, cursor;
  do {
    const r = await list({ prefix: 'breakpoint/w/', cursor, limit: 1000 });
    n += r.blobs.length; cursor = r.hasMore ? r.cursor : undefined;
  } while (cursor);
  return n;
}
// Entries close at the end of Breakpoint London (17 Nov 2026, 23:59 London = UTC in November).
const CLOSE_AT = Date.parse('2026-11-18T00:00:00Z');
const clean = (v, max) => String(v == null ? '' : v).trim().slice(0, max);

module.exports = async (req, res) => {
  try {
    if (req.method === 'GET') return send(res, 200, { count: await count(), open: Date.now() < CLOSE_AT }, 'public, s-maxage=60, stale-while-revalidate=300');
    if (req.method !== 'POST') { res.setHeader('allow', 'GET, POST'); return send(res, 405, { error: 'Method not allowed.' }); }

    if (Date.now() >= CLOSE_AT) return send(res, 410, { error: 'Entries are closed. Thanks for stopping by the pond.' });
    let b = req.body;
    if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
    b = b || {};
    if (b.website) return send(res, 200, { ok: true }); // honeypot: bots get a fake success

    const wallet = clean(b.wallet, 60);
    const x = clean(b.x, 80).replace(/^@/, '').replace(/^(https?:\/\/)?(www\.)?(x|twitter)\.com\//i, '').split(/[/?#]/)[0];
    const tg = clean(b.tg, 80).replace(/^@/, '').replace(/^(https?:\/\/)?t\.me\//i, '').split(/[/?#]/)[0];

    if (!/^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(wallet) || b58Bytes(wallet) !== 32)
      return send(res, 400, { error: 'That does not look like a Solana wallet address. Copy it from Phantom, Solflare or Backpack.', field: 'wallet' });
    if (!/^[A-Za-z0-9_]{1,15}$/.test(x))
      return send(res, 400, { error: 'Enter your X handle, like @FrogMark1.', field: 'x' });
    if (!/^[A-Za-z0-9_]{5,32}$/.test(tg))
      return send(res, 400, { error: 'Enter your Telegram username (5 to 32 letters, numbers or _).', field: 'tg' });
    if (b.agree !== true)
      return send(res, 400, { error: 'Tick the box to confirm you did the three tasks.', field: 'agree' });

    const wPath = `breakpoint/w/${wallet}.json`;
    const xPath = `breakpoint/x/${x.toLowerCase()}.json`;
    if (await exists(wPath)) return send(res, 409, { error: 'This wallet is already in the pond. One entry per wallet.', field: 'wallet' });
    if (await exists(xPath)) return send(res, 409, { error: 'This X account is already in the pond. One entry per person.', field: 'x' });

    const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim();
    const salt = process.env.ADMIN_KEY || 'zfrog';
    const entry = {
      wallet, x, tg,
      at: new Date().toISOString(),
      country: clean(req.headers['x-vercel-ip-country'], 4),
      ref: clean(b.ref, 40).replace(/[^\w-]/g, ''),
      ipHash: ip ? crypto.createHash('sha256').update(salt + ip).digest('hex').slice(0, 16) : '',
      ua: clean(req.headers['user-agent'], 200),
    };
    const opts = { access: 'private', addRandomSuffix: false, allowOverwrite: false, contentType: 'application/json' };
    await put(wPath, JSON.stringify(entry), opts);
    await put(xPath, JSON.stringify({ wallet, at: entry.at }), opts);
    return send(res, 200, { ok: true });
  } catch (e) {
    if (e && /already exists/i.test(String(e.message))) return send(res, 409, { error: 'Already registered. One entry per wallet and per X account.' });
    console.error('claim error', e);
    return send(res, 500, { error: 'The pond is busy. Try again in a minute.' });
  }
};
