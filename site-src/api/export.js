// Private CSV export of Breakpoint sign-ups: /api/export?key=ADMIN_KEY  (add &format=json for JSON)
const { list, get } = require('@vercel/blob');
const crypto = require('crypto');

function safeEqual(a, b) {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
}
const csvCell = (v) => { const s = String(v == null ? '' : v); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; };

module.exports = async (req, res) => {
  res.setHeader('cache-control', 'no-store');
  res.setHeader('x-robots-tag', 'noindex');
  const key = (req.query && req.query.key) || '';
  if (!process.env.ADMIN_KEY || !safeEqual(key, process.env.ADMIN_KEY)) { res.statusCode = 401; return res.end('Unauthorized'); }
  try {
    const blobs = []; let cursor;
    do {
      const r = await list({ prefix: 'breakpoint/w/', cursor, limit: 1000 });
      blobs.push(...r.blobs); cursor = r.hasMore ? r.cursor : undefined;
    } while (cursor);
    const rows = [];
    for (let i = 0; i < blobs.length; i += 25) {
      const part = await Promise.all(blobs.slice(i, i + 25).map(async (bl) => {
        const r = await get(bl.pathname, { access: 'private', useCache: false });
        return r ? JSON.parse(await new Response(r.stream).text()) : null;
      }));
      rows.push(...part.filter(Boolean));
    }
    rows.sort((a, b) => String(a.at).localeCompare(String(b.at)));
    const ipCount = {}; rows.forEach((r) => { if (r.ipHash) ipCount[r.ipHash] = (ipCount[r.ipHash] || 0) + 1; });
    rows.forEach((r) => { r.sameIp = r.ipHash ? ipCount[r.ipHash] : 0; });
    if (req.query && req.query.format === 'json') {
      res.setHeader('content-type', 'application/json; charset=utf-8');
      return res.end(JSON.stringify({ count: rows.length, entries: rows }, null, 1));
    }
    const cols = ['at', 'wallet', 'x', 'tg', 'country', 'ref', 'sameIp', 'ipHash', 'ua'];
    const head = ['submitted_at', 'wallet', 'x_handle', 'telegram', 'country', 'ref', 'entries_same_ip', 'ip_hash', 'user_agent'];
    const csv = [head.join(',')].concat(rows.map((r) => cols.map((c) => csvCell(r[c])).join(','))).join('\n') + '\n';
    res.setHeader('content-type', 'text/csv; charset=utf-8');
    res.setHeader('content-disposition', `attachment; filename="zfrog-breakpoint-${new Date().toISOString().slice(0, 10)}.csv"`);
    return res.end(csv);
  } catch (e) {
    console.error('export error', e);
    res.statusCode = 500; return res.end('Export failed');
  }
};
