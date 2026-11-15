// Breakpoint London popup for the homepage. Shows once per visit, stops by itself when entries close.
(function(){
  var END = Date.parse('2026-11-18T00:00:00Z');
  if (Date.now() >= END || location.pathname.replace(/\/+$/, '') !== '') return;
  try { if (sessionStorage.getItem('zfrog-bp-pop')) return; } catch (e) {}
  var IMG = 'https://raw.githubusercontent.com/mrbrown-devai/zfrog-memes/c0e145380b4af82f21047fd61c0423bd07e08eff/brand/breakpoint/london-poster.jpg';
  var css = '.bpp{position:fixed;inset:0;z-index:200;display:grid;place-items:center;padding:20px;background:rgba(5,5,4,.78);opacity:0;transition:opacity .25s}'
    + '.bpp.on{opacity:1}'
    + '.bpp-card{position:relative;width:min(520px,100%);max-height:calc(100dvh - 40px);overflow:auto;background:var(--panel,#111110);box-shadow:inset 0 0 0 1px var(--toxic,#ffcc12);color:var(--fg,#f4f1e6)}'
    + '.bpp-card img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover}'
    + '.bpp-body{display:grid;gap:14px;padding:22px 24px 26px}'
    + '.bpp-eye{font:600 12px/1.3 var(--mono,monospace);letter-spacing:.14em;text-transform:uppercase;color:var(--toxic,#ffcc12)}'
    + '.bpp-card h2{margin:0;font:700 clamp(30px,7vw,44px)/.95 var(--display,sans-serif);text-transform:uppercase}'
    + '.bpp-card h2 em{font-style:normal;color:var(--toxic,#ffcc12)}'
    + '.bpp-card p{margin:0;color:var(--muted,#b9b5a6);font-size:17px;line-height:1.45}'
    + '.bpp-row{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:4px}'
    + '.bpp-go{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;background:var(--toxic,#ffcc12);color:var(--void,#050504);font:700 15px/1 var(--display,sans-serif);letter-spacing:.06em;text-transform:uppercase;text-decoration:none}'
    + '.bpp-go:hover{background:#fff27a}'
    + '.bpp-no{min-height:48px;padding:0 16px;background:none;border:0;color:var(--muted,#b9b5a6);font:600 14px/1 var(--display,sans-serif);letter-spacing:.06em;text-transform:uppercase;cursor:pointer}'
    + '.bpp-no:hover{color:var(--fg,#f4f1e6)}'
    + '.bpp-x{position:absolute;top:10px;right:10px;width:44px;height:44px;display:grid;place-items:center;background:rgba(5,5,4,.72);border:0;color:#f4f1e6;font:400 26px/1 var(--display,sans-serif);cursor:pointer}'
    + '.bpp-x:hover{color:var(--toxic,#ffcc12)}'
    + '.bpp a:focus-visible,.bpp button:focus-visible{outline:2px solid #f4f1e6;outline-offset:2px}'
    + '@media (prefers-reduced-motion:reduce){.bpp{transition:none}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  var el = document.createElement('div');
  el.className = 'bpp'; el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'true'); el.setAttribute('aria-labelledby', 'bppTitle');
  el.innerHTML = '<div class="bpp-card">'
    + '<button class="bpp-x" type="button" aria-label="Close">×</button>'
    + '<img src="' + IMG + '" alt="A black jet marked with a glowing Z flies past Big Ben" width="1280" height="720">'
    + '<div class="bpp-body">'
    + '<span class="bpp-eye">Breakpoint London · 15 to 17 Nov · Olympia</span>'
    + '<h2 id="bppTitle">ZFROG invasion <em>@Breakpoint</em></h2>'
    + '<p>The hooded frog is loose in London. Find a ZFROG sticker, do the quest, and you are in the draw for $ZFROG and a ZFROG Genesis NFT.</p>'
    + '<div class="bpp-row"><a class="bpp-go" href="/breakpoint">Enter the draw</a><button class="bpp-no" type="button">Not now</button></div>'
    + '</div></div>';
  var last = document.activeElement;
  function close(){
    try { sessionStorage.setItem('zfrog-bp-pop', '1'); } catch (e) {}
    document.removeEventListener('keydown', onKey);
    el.remove(); st.remove();
    if (last && last.focus) last.focus();
  }
  function onKey(ev){
    if (ev.key === 'Escape') return close();
    if (ev.key !== 'Tab') return;
    var f = el.querySelectorAll('a,button'), a = f[0], z = f[f.length - 1];
    if (ev.shiftKey && document.activeElement === a) { ev.preventDefault(); z.focus(); }
    else if (!ev.shiftKey && document.activeElement === z) { ev.preventDefault(); a.focus(); }
  }
  el.addEventListener('click', function(ev){ if (ev.target === el) close(); });
  el.querySelector('.bpp-x').addEventListener('click', close);
  el.querySelector('.bpp-no').addEventListener('click', close);
  el.querySelector('.bpp-go').addEventListener('click', function(){ try { sessionStorage.setItem('zfrog-bp-pop', '1'); } catch (e) {} });
  function show(){
    document.body.appendChild(el);
    requestAnimationFrame(function(){ el.classList.add('on'); });
    document.addEventListener('keydown', onKey);
    el.querySelector('.bpp-go').focus({preventScroll: true});
  }
  setTimeout(show, 900);
})();
