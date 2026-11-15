// Build step: adds the Breakpoint popup script to the homepage. Remove this file's call from package.json to switch it off.
const fs = require('fs');
const file = 'index.html';
const tag = '<script src="/assets/bp-popup.js" defer></script>';
let s = fs.readFileSync(file, 'utf8');
if (!s.includes('/assets/bp-popup.js')) {
  const i = Math.max(s.lastIndexOf('</body>'), s.lastIndexOf('</html>'));
  s = i >= 0 ? s.slice(0, i) + tag + '\n' + s.slice(i) : s + '\n' + tag + '\n';
  fs.writeFileSync(file, s);
  console.log('popup script added to ' + file);
}
