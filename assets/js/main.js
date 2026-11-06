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

  var year = document.getElementById('year');
  if (year) { year.textContent = String(new Date().getFullYear()); }
})();

document.querySelectorAll('a[hreflang]').forEach(function (a) {
  a.addEventListener('click', function () {
    try { localStorage.setItem('site-lang', a.getAttribute('hreflang')); } catch (e) {}
  });
});
