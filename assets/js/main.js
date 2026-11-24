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

  var floatCta = document.querySelector('.float-cta');
  if (floatCta && !/contact\.html$/.test(location.pathname)) {
    var heroCta = document.querySelector('.hero .hero-cta');
    var onCta = function () {
      var show = !heroCta || heroCta.getBoundingClientRect().bottom < 0;
      floatCta.classList.toggle('show', show);
    };
    window.addEventListener('scroll', onCta, { passive: true }); onCta();
  }

  document.querySelectorAll('details.faq-item').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      d.parentElement.querySelectorAll('details.faq-item[open]').forEach(function (o) { if (o !== d) o.open = false; });
    });
  });

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
    cards.forEach(function (c, i) { c.style.display = (i === pick) ? 'flex' : 'none'; });
  });
})();
