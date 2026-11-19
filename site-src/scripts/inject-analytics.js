// Build step: adds Vercel Web Analytics to every HTML page. Needs Web Analytics switched on in the Vercel project settings.
const fs = require('fs');
const path = require('path');
const tag = '<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script>\n<script defer src="/_vercel/insights/script.js"></script>';
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
  if (s.includes('/_vercel/insights/script.js')) continue;
  const i = Math.max(s.lastIndexOf('</body>'), s.lastIndexOf('</html>'));
  s = i >= 0 ? s.slice(0, i) + tag + '\n' + s.slice(i) : s + '\n' + tag + '\n';
  fs.writeFileSync(file, s);
  n++;
}
console.log('analytics added to ' + n + ' pages');
