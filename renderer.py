import json


def build_portfolio_html(owner, about, experience, projects, skills):
    data = {
        "owner":      owner,
        "about":      about,
        "experience": experience,
        "projects":   projects,
        "skills":     skills,
    }

    template = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

  html, body {
    width: 100%; height: 100%;
    background: #0c0c0c;
    color: #c8c8c8;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    overflow: hidden;
    user-select: none;
    cursor: default;
  }

  /* CRT scanlines */
  body::after {
    content: '';
    position: fixed; inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent, transparent 2px,
      rgba(0,0,0,0.18) 2px, rgba(0,0,0,0.18) 4px
    );
    pointer-events: none;
    z-index: 9999;
  }

  /* CRT vignette */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.75) 100%);
    pointer-events: none;
    z-index: 9998;
  }

  #app {
    width: 100%; height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 24px 32px 52px;
    outline: none;
    position: relative;
  }

  /* ── STATUS BAR ── */
  #statusbar {
    position: fixed; bottom: 0; left: 0; right: 0; height: 28px;
    background: #0c0c0c;
    border-top: 1px solid #2a2a2a;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 16px;
    font-size: 11px; letter-spacing: 2px; color: #5a5a5a;
    z-index: 100;
  }
  #statusbar .online { color: #888888; }

  /* ── ANIMATIONS ── */
  @keyframes blink  { 0%,49%{opacity:1} 50%,100%{opacity:0} }
  @keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }

  .blink   { animation: blink 1s step-end infinite; }
  .fade-in { animation: fadeIn 0.22s ease-out both; }

  /* ── WELCOME ── */
  #welcome { text-align: center; max-width: 660px; }

  .w-name {
    font-family: 'VT323', monospace;
    font-size: 92px; letter-spacing: 18px; line-height: 1;
    color: #f0f0f0;
  }
  .w-title {
    font-family: 'VT323', monospace;
    font-size: 27px; letter-spacing: 7px; margin-top: 8px;
    color: #888888;
  }
  .w-divider { color: #2a2a2a; margin: 20px 0; letter-spacing: 2px; font-size: 15px; }
  .w-location { font-size: 13px; letter-spacing: 5px; color: #666666; }
  .w-cta {
    margin-top: 48px;
    font-family: 'VT323', monospace;
    font-size: 31px; letter-spacing: 3px;
    color: #c8c8c8;
  }
  .w-cta em { color: #a09060; font-style: normal; }
  .w-hint { margin-top: 10px; font-size: 11px; color: #505050; letter-spacing: 2px; }

  /* ── MENU ── */
  #menu { max-width: 560px; width: 100%; }

  .m-header {
    font-size: 11px; letter-spacing: 5px; text-transform: uppercase;
    color: #444444;
    margin-bottom: 30px;
  }
  .m-item {
    font-family: 'VT323', monospace;
    font-size: 40px; letter-spacing: 4px; padding: 3px 0;
    color: #444444;
    display: flex; align-items: center; gap: 14px;
    cursor: pointer;
    transition: color 0.07s;
  }
  .m-item.sel { color: #f0f0f0; }
  .m-cursor { color: #a09060; width: 22px; flex-shrink: 0; }
  .m-item:not(.sel) .m-cursor { visibility: hidden; }
  .m-footer { margin-top: 30px; font-size: 11px; color: #505050; letter-spacing: 2px; }

  /* ── SECTION VIEW ── */
  #section { max-width: 700px; width: 100%; }

  .s-header {
    font-family: 'VT323', monospace;
    font-size: 42px; letter-spacing: 5px;
    color: #f0f0f0;
    margin-bottom: 12px;
  }
  .s-divider { border: none; border-top: 1px solid #2a2a2a; margin-bottom: 22px; }
  .s-body {
    max-height: calc(100vh - 210px);
    overflow-y: auto; padding-right: 6px;
    line-height: 1.85;
  }
  .s-body::-webkit-scrollbar { width: 3px; }
  .s-body::-webkit-scrollbar-thumb { background: #333333; }
  .s-footer { margin-top: 18px; font-size: 11px; color: #505050; letter-spacing: 2px; }

  /* About */
  .about-p { color: #c8c8c8; font-size: 13px; line-height: 1.95; }

  /* Experience */
  .exp-block { margin-bottom: 30px; }
  .exp-role    { color: #f0f0f0; font-size: 15px; }
  .exp-company { color: #888888; font-size: 13px; margin-top: 2px; }
  .exp-period  { color: #606060; font-size: 12px; margin: 4px 0 10px; letter-spacing: 1px; }
  .exp-li {
    color: #c8c8c8; font-size: 13px; line-height: 1.85;
    padding-left: 18px; position: relative;
  }
  .exp-li::before { content: '▸'; color: #a09060; position: absolute; left: 0; }

  /* Projects */
  .proj-block {
    border-left: 2px solid #2a2a2a;
    padding-left: 16px; margin-bottom: 26px;
  }
  .proj-name {
    font-family: 'VT323', monospace; font-size: 27px; letter-spacing: 2px;
    color: #f0f0f0;
  }
  .proj-desc   { color: #c8c8c8; font-size: 13px; margin: 4px 0 8px; }
  .proj-detail { color: #808080; font-size: 12px; line-height: 1.72; margin-bottom: 8px; }
  .proj-tags   { display: flex; flex-wrap: wrap; gap: 6px; }
  .proj-tag    {
    color: #888888; font-size: 11px; letter-spacing: 1px;
    border: 1px solid #2a2a2a; padding: 1px 8px;
  }

  /* Skills */
  .sk-cat   { margin-bottom: 20px; }
  .sk-label { color: #888888; font-size: 11px; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 7px; }
  .sk-tags  { display: flex; flex-wrap: wrap; gap: 6px; }
  .sk-tag   {
    background: rgba(255,255,255,0.04);
    border: 1px solid #2a2a2a;
    color: #c8c8c8; padding: 2px 10px; font-size: 12px; letter-spacing: 1px;
  }

  /* Contact */
  .ct-row   { display: flex; gap: 16px; align-items: center; margin-bottom: 14px; }
  .ct-label { color: #888888; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; min-width: 96px; }
  .ct-value { color: #c8c8c8; font-size: 13px; }

</style>
</head>
<body>
<div id="app" tabindex="0"></div>

<div id="statusbar">
  <span id="sb-left">tty://portfolio</span>
  <span class="online">■ online</span>
</div>

<script>
const DATA = __PORTFOLIO_JSON__;
const MENU = ['about', 'experience', 'projects', 'skills', 'contact'];

const app    = document.getElementById('app');
const sbLeft = document.getElementById('sb-left');

let state = { screen: 'welcome', sel: 0 };

function e(s) {
  return String(s)
    .replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function setStatus(t) { sbLeft.textContent = t; }

function transition(next) {
  app.style.opacity = '0.2';
  setTimeout(() => {
    app.style.opacity = '1';
    state.screen = next;
    render();
  }, 75);
}

function render() {
  switch (state.screen) {
    case 'welcome': renderWelcome(); break;
    case 'menu':    renderMenu();    break;
    case 'section': renderSection(); break;
  }
}

function renderWelcome() {
  setStatus('tty://portfolio — boot');
  app.innerHTML = `
    <div id="welcome" class="fade-in">
      <div class="w-name">${e(DATA.owner.name)}</div>
      <div class="w-title">${e(DATA.owner.title)}</div>
      <div class="w-divider">──────────────────────────────────</div>
      <div class="w-location">${e(DATA.owner.location)}</div>
      <div class="w-cta">▸ press <em>[enter]</em> to boot<span class="blink">_</span></div>
      <div class="w-hint">or click anywhere</div>
    </div>`;
  app.onclick = () => transition('menu');
}

function renderMenu() {
  setStatus('tty://portfolio — menu');
  app.onclick = null;
  app.innerHTML = `
    <div id="menu" class="fade-in">
      <div class="m-header">// select module</div>
      ${MENU.map((item, i) => `
        <div class="m-item ${i === state.sel ? 'sel' : ''}" data-i="${i}">
          <span class="m-cursor">▸</span>
          <span>${e(item)}</span>
        </div>`).join('')}
      <div class="m-footer">[↑↓] navigate &nbsp;·&nbsp; [enter] select &nbsp;·&nbsp; [esc] back</div>
    </div>`;
  app.querySelectorAll('.m-item').forEach(el => {
    el.addEventListener('click', () => {
      state.sel = parseInt(el.dataset.i);
      transition('section');
    });
  });
}

function renderSection() {
  const name = MENU[state.sel];
  setStatus(`tty://portfolio — ${name}`);
  app.onclick = null;
  app.innerHTML = `
    <div id="section" class="fade-in">
      <div class="s-header">// ${e(name)}</div>
      <hr class="s-divider">
      <div class="s-body">${getContent(name)}</div>
      <div class="s-footer">[esc] back to menu</div>
    </div>`;
}

function getContent(name) {
  switch (name) {
    case 'about':
      return `<p class="about-p">${e(DATA.about)}</p>`;

    case 'experience':
      return DATA.experience.map(x => `
        <div class="exp-block">
          <div class="exp-role">${e(x.role)}</div>
          <div class="exp-company">${e(x.company)}</div>
          <div class="exp-period">${e(x.period)}</div>
          ${x.highlights.map(h => `<div class="exp-li">${e(h)}</div>`).join('')}
        </div>`).join('');

    case 'projects':
      return DATA.projects.map(p => `
        <div class="proj-block">
          <div class="proj-name">${e(p.name)}</div>
          <div class="proj-desc">${e(p.description)}</div>
          <div class="proj-detail">${e(p.detail)}</div>
          <div class="proj-tags">
            ${p.tech.map(t => `<span class="proj-tag">${e(t)}</span>`).join('')}
          </div>
        </div>`).join('');

    case 'skills':
      return Object.entries(DATA.skills).map(([cat, tags]) => `
        <div class="sk-cat">
          <div class="sk-label">${e(cat)}</div>
          <div class="sk-tags">
            ${tags.map(t => `<span class="sk-tag">${e(t)}</span>`).join('')}
          </div>
        </div>`).join('');

    case 'contact':
      return Object.entries(DATA.owner.contact).map(([k, v]) => `
        <div class="ct-row">
          <span class="ct-label">${e(k)}</span>
          <span class="ct-value">${e(v)}</span>
        </div>`).join('');

    default: return '';
  }
}

document.addEventListener('keydown', ev => {
  if (state.screen === 'welcome') {
    if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); transition('menu'); }

  } else if (state.screen === 'menu') {
    if (ev.key === 'ArrowUp') {
      ev.preventDefault();
      state.sel = (state.sel - 1 + MENU.length) % MENU.length;
      renderMenu();
    } else if (ev.key === 'ArrowDown') {
      ev.preventDefault();
      state.sel = (state.sel + 1) % MENU.length;
      renderMenu();
    } else if (ev.key === 'Enter') {
      ev.preventDefault(); transition('section');
    } else if (ev.key === 'Escape') {
      transition('welcome');
    }

  } else if (state.screen === 'section') {
    if (ev.key === 'Escape') { ev.preventDefault(); transition('menu'); }
  }
});

app.focus();

render();
</script>
</body>
</html>"""

    return template.replace('__PORTFOLIO_JSON__', json.dumps(data))
