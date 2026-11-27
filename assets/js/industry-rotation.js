/* Executed immediately after the section, before the rest of the page loads. */
(() => {
  'use strict';
  const section = document.getElementById('experience');
  const main = section.querySelector('.card-grid');
  const extra = document.getElementById('other-industries');
  const button = section.querySelector('.industry-toggle');
  const more = button.textContent;
  const cards = new Map(Array.from(main.querySelectorAll('a.card'), a =>
    [a.getAttribute('href').split('/').pop(), a]));
  // Offshore operations / built environment / applied detection.
  const pairs = [['shelf', 'vizard'], ['egip', 'developer'], ['agro', 'medtech']]
    .map(pair => pair.map(id => cards.get(id + '.html')));
  if (cards.size !== 6 || !pairs.every(pair => pair.every(Boolean))) return;

  const cookieKey = 'kor-industry-v1';
  const key = 'korIndustry';
  const param = 'dev-industry';
  const readNumber = value => value != null && /^[0-7]$/.test(value) ? Number(value) : null;
  function readCookie() {
    try {
      const match = document.cookie.match(/(?:^|;\s*)kor-industry-v1=(\d+)(?:;|$)/);
      return match ? readNumber(match[1]) : null;
    } catch (_) { return null; }
  }
  function writeCookie(n) {
    try {
      const secure = location.protocol === 'https:' ? '; Secure' : '';
      document.cookie = `${cookieKey}=${n}; Path=/; Max-Age=31536000; SameSite=Lax${secure}`;
      return readCookie() === n;
    } catch (_) { return false; }
  }
  function entry() {
    try { return readNumber(history.state && history.state[key]); } catch (_) { return null; }
  }
  function expand(open) {
    extra.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? button.dataset.less : more;
  }

  let current, persistent;
  function present(restore) {
    const durable = readCookie();
    const previous = durable ?? entry() ?? readNumber(new URL(location.href).searchParams.get(param));
    // Pick any of the eight balanced trios on a genuinely new visit; otherwise
    // swap all three industries whenever cross-page persistence is available.
    current = previous === null ? Math.floor(Math.random() * 8) : previous ^ 7;
    persistent = writeCookie(current);
    if (!persistent && previous !== null) {
      // Each ring contains four trios differing from each other in two slots.
      // Skip the intervening pick on history restores (RU → EN → Back).
      const even = [0, 3, 5, 6];
      const ring = even.includes(previous) ? even : [7, 4, 2, 1];
      current = ring[(ring.indexOf(previous) + (restore ? 2 : 1)) % 4];
    }
    pairs.forEach((pair, i) => {
      const picked = (current >> i) & 1;
      main.append(pair[picked]);
      extra.append(pair[1 - picked]);
    });
    expand(false);
    button.hidden = false;
    let state = { [key]: current };
    try {
      state = { ...history.state, ...state };
      history.replaceState(state, '');
    } catch (_) { /* opaque preview */ }
    if (!persistent) {
      const url = new URL(location.href);
      url.searchParams.set(param, current);
      try { history.replaceState(state, '', url); } catch (_) { /* the outgoing link still carries the cursor */ }
    }
  }
  const navigation = performance.getEntriesByType('navigation')[0];
  present(navigation && navigation.type === 'back_forward');
  window.addEventListener('pageshow', e => { if (e.persisted) present(true); });
  button.addEventListener('click', () => expand(extra.hidden));
  // In a cookie-blocked preview, carry the cursor to either language and the
  // next page. The preview adapter passes it through intermediate pages.
  document.addEventListener('click', e => {
    if (persistent) return;
    const a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.getAttribute('href').startsWith('#')) return;
    const url = new URL(a.href);
    if (url.protocol !== location.protocol || url.host !== location.host) return;
    if (url.hash && url.pathname === location.pathname) return;
    url.searchParams.set(param, current);
    a.href = url.href;
  }, true);
})();
