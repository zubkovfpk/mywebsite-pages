(function () {
  'use strict';

  var header = document.querySelector('.site-header');
  function onScroll() {
    if (window.scrollY > 8) { header.classList.add('scrolled'); }
    else { header.classList.remove('scrolled'); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  var toggle = document.getElementById('nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.site-nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }


  var toTop = document.querySelector('.to-top');
  if (toTop) {
    var onTop = function () { toTop.classList.toggle('show', window.scrollY > 600); };
    window.addEventListener('scroll', onTop, { passive: true }); onTop();
    toTop.addEventListener('click', function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }

  document.querySelectorAll('details.faq-item').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      d.parentElement.querySelectorAll('details.faq-item[open]').forEach(function (o) { if (o !== d) o.open = false; });
    });
  });

  var sheetSections = Array.from(document.querySelectorAll('main section[id]')).filter(function (s) { return s.querySelector('.sheet-no'); });
  if (sheetSections.length) {
    var progress = document.createElement('nav');
    progress.className = 'sheet-progress';
    progress.setAttribute('aria-label', document.documentElement.lang === 'ru' ? 'Листы главной' : 'Homepage sheets');
    sheetSections.forEach(function (section, i) {
      var link = document.createElement('a');
      link.href = '#' + section.id;
      link.setAttribute('aria-label', (i + 1) + ' · ' + section.querySelector('h2').textContent);
      link.textContent = String(i + 1);
      progress.appendChild(link);
    });
    var headerInner = document.querySelector('.header-inner');
    var navToggle = document.getElementById('nav-toggle');
    var strip = document.createElement('div');
    strip.className = 'container sheet-strip';
    function toRow() { headerInner.insertBefore(progress, navToggle && navToggle.parentNode === headerInner ? navToggle : null); }
    function rowHeight() { var d = progress.style.display; progress.style.display = 'none'; var h = headerInner.getBoundingClientRect().height; progress.style.display = d; return h; }
    if (headerInner) { toRow(); headerInner.parentNode.appendChild(strip); }
    else document.body.appendChild(progress);
    // Brand book KOR.BB.01 rev 1.7, technique 6: sheets in the header row; a strip under it only if the row has no room
    function placeSheets() {
      if (!headerInner) return;
      toRow();
      document.documentElement.classList.remove('sp-below-on');
      if (getComputedStyle(progress).position === 'fixed') return;
      var box = headerInner.getBoundingClientRect(), cs = getComputedStyle(headerInner);
      var contentRight = box.right - parseFloat(cs.paddingRight);
      var lastRight = Math.max.apply(null, Array.from(headerInner.children).map(function (c) { return c.offsetParent ? c.getBoundingClientRect().right : 0; }));
      if (lastRight > contentRight + 0.5 || headerInner.scrollWidth > headerInner.clientWidth + 1 || box.height > rowHeight() + 1) {
        strip.appendChild(progress);
        document.documentElement.classList.add('sp-below-on');
      }
    }
    window.addEventListener('resize', placeSheets);
    placeSheets();
    function updateSheet() {
      var active = 0;
      sheetSections.forEach(function (section, i) { if (section.getBoundingClientRect().top < window.innerHeight * .5) active = i; });
      progress.querySelectorAll('a').forEach(function (link, i) {
        if (i === active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
      });
      var sheetCell = document.querySelector('.stamp-cell:last-child .stamp-v');
      if (sheetCell) sheetCell.textContent = (active + 1) + ' / ' + sheetSections.length;
    }
    window.addEventListener('scroll', updateSheet, { passive: true });
    updateSheet();
  }

  // Brand book KOR.BB.01 rev 1.8: up to 1250 px the floating buttons give way to one action bar at the bottom,
  // shown only while scrolling up and hidden near the contact band and the footer
  (function () {
    var src = document.querySelector('.float-cta') || document.querySelector('.site-nav .nav-cta');
    if (!src || /contact\.html$/.test(location.pathname)) return;
    var ru = document.documentElement.lang === 'ru';
    var bar = document.createElement('div');
    bar.className = 'action-bar';
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', ru ? 'Быстрые действия' : 'Quick actions');
    var cta = document.createElement('a');
    cta.className = 'action-bar-cta';
    cta.href = src.getAttribute('href');
    cta.textContent = src.textContent.trim();
    var up = document.createElement('a');
    up.className = 'action-bar-top';
    up.href = '#top';
    up.setAttribute('aria-label', ru ? 'Наверх' : 'Back to top');
    up.textContent = '↑';
    up.addEventListener('click', function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); });
    bar.appendChild(cta); bar.appendChild(up);
    document.body.appendChild(bar);
    var stops = Array.from(document.querySelectorAll('.cta-band, .site-footer'));
    var lastY = window.scrollY, nearStop = false;
    if ('IntersectionObserver' in window && stops.length) {
      var seen = new Set();
      var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) seen.add(en.target); else seen.delete(en.target); });
        nearStop = seen.size > 0;
        if (nearStop) bar.classList.remove('show');
      });
      stops.forEach(function (s) { obs.observe(s); });
    }
    window.addEventListener('scroll', function () {
      var y = window.scrollY, d = y - lastY;
      if (Math.abs(d) < 6) return;
      bar.classList.toggle('show', d < 0 && y > 400 && !nearStop);
      lastY = y;
    }, { passive: true });
  })();

  var year = document.getElementById('year');
  if (year) { year.textContent = String(new Date().getFullYear()); }

  // Lockup C2: fit descriptor to the width of the top row (КОР + mark)
  document.querySelectorAll('.lk-c2').forEach(function (lk) {
    var top = lk.querySelector('.lk-c2-top');
    var sub = lk.querySelector('.lk-desc');
    if (!top || !sub) return;
    var w = top.getBoundingClientRect().width;
    var f = parseFloat(getComputedStyle(sub).fontSize);
    var dw = sub.getBoundingClientRect().width - 0.1 * f;
    if (!w || !dw) return;
    var n = sub.textContent.length;
    var ls = 0.1 * f + (w - dw) / Math.max(1, n - 1);
    sub.style.letterSpacing = ls.toFixed(3) + 'px';
    sub.style.marginRight = (-ls).toFixed(3) + 'px';
  });
})();

document.querySelectorAll('a[hreflang]').forEach(function (a) {
  a.addEventListener('click', function () {
    try { localStorage.setItem('site-lang', a.getAttribute('hreflang')); } catch (e) {}
  });
});

// Sample report gate (prototype: unlocks locally, nothing is sent)
(function () {
  var f = document.getElementById('gate-form');
  if (!f) return;
  var root = document.documentElement;
  try { if (localStorage.getItem('report-unlocked')) root.classList.add('report-unlocked'); } catch (e) {}
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    try { localStorage.setItem('report-unlocked', '1'); } catch (e2) {}
    root.classList.add('report-unlocked');
    var t = document.getElementById('report-thanks');
    if (t) t.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
})();

// Random one-per-row case trio on the index page (no-JS shows the first of each group)
(function () {
  document.querySelectorAll('.card-rand').forEach(function (g) {
    var cards = g.querySelectorAll('.card');
    if (cards.length < 2) return;
    var pick = Math.floor(Math.random() * cards.length);
    g.insertBefore(cards[pick], g.firstChild); // CSS shows the first card only
  });
})();
