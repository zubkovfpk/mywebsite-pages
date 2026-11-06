/* ============================================================
   Сергей Зубков — Fractional CAIO · Концепция B
   Минимальный интерактив: шапка, мобильное меню, reveal, год.
   ============================================================ */

(function () {
  'use strict';

  // Шапка: тень после скролла
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (window.scrollY > 8) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Мобильное меню
  var toggle = document.getElementById('nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // Закрыть меню при переходе по якорю
    document.querySelectorAll('.site-nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Reveal-анимации при попадании в вьюпорт
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }

  // Текущий год в футере
  var year = document.getElementById('year');
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }
})();
