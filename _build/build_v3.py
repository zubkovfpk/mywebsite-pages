# -*- coding: utf-8 -*-
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lang_detect import lang_script
from radar import radar_svg
from sample_page import sample_report
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = 'Бюро Зубкова'
ROLE = 'Бюро обоснованного ИИ'
PLAT = 'Council 7+1'
SITE = 'https://example.ru'

NAV = [('index.html#pains','Задачи'),('index.html#how','Как работаем'),('index.html#experience','Опыт'),
       ('cases.html','Кейсы'),('index.html#formats','Форматы'),('contact.html','Контакт')]

def nb(s):
    s = re.sub(r'([0-9+]) ', '\\1\u00a0', s)
    return re.sub(r'(млн|млрд|тыс)\.? ', lambda m: m.group(0)[:-1] + '\u00a0', s)

def photo(r, name, alt, cls='', gen=True):
    return f'<figure class="photo{" gen" if gen else ""} {cls}"><img src="{r}assets/img/{name}" alt="{alt}" loading="lazy" decoding="async"></figure>'

def chip(z):
    m={'ИИ':'green','Гибрид':'amber','Без ИИ':'red','Отложить':'grey'}
    return f'<span class="chip chip-{m[z]}">{z}</span>'

def page(path, title, desc, body, active=None):
    depth = path.count('/')
    r = '../'*depth
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{r}{h}"{cur if h==active else ""}>{t}</a>' for h,t in NAV)
    fnav = ''.join(f'<a href="{r}{h}">{t}</a>' for h,t in NAV) + f'<a href="{r}contact.html">Контакт</a><a href="{r}en/{path}" hreflang="en">EN</a>'
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}/{path.replace('index.html','')}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{SITE}/assets/img/team.jpg">
  <link rel="alternate" hreflang="ru" href="{SITE}/{path.replace('index.html','')}">
  <link rel="alternate" hreflang="en" href="{SITE}/en/{path.replace('index.html','')}">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='8' fill='%231C1B18'/%3E%3Crect x='14' y='20' width='10' height='24' fill='%232E7D4F'/%3E%3Crect x='27' y='20' width='10' height='24' fill='%23A9740F'/%3E%3Crect x='40' y='20' width='10' height='24' fill='%23B3402E'/%3E%3C/svg%3E">
  {lang_script('ru', f'{r}en/{path}')}
  <link rel="stylesheet" href="{r}assets/css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"ProfessionalService","name":"{BRAND} — {ROLE.lower()}","url":"{SITE}/",
   "description":"Диагностика процессов и решение, где ИИ оправдан, выгоден и безопасен, а где нужна обычная автоматизация.",
   "founder":{{"@type":"Person","name":"Сергей Зубков","jobTitle":"Основатель, главный конструктор","sameAs":["https://www.linkedin.com/in/sergey-a-zubkov"]}},
   "areaServed":"RU","knowsAbout":["AI strategy","Process diagnostics","MLOps","Maritime logistics","Mining","MedTech"]}}
  </script>
</head>
<body>
<header class="site-header" id="top">
  <div class="container header-inner">
    <a class="wordmark" href="{r}index.html" aria-label="{BRAND} — на главную">
      <span class="wordmark-mark" aria-hidden="true"><b>?</b><i></i><i></i><i></i><i></i></span>
      <span class="wordmark-text"><span class="wordmark-name">{BRAND}</span><span class="wordmark-role">{ROLE}</span></span>
    </a>
    <nav class="site-nav" id="site-nav" aria-label="Основная навигация">
      {nav}
      <a class="nav-lang" href="{r}en/{path}" hreflang="en">EN</a>
      <a class="nav-cta" href="{r}contact.html">Разговор на 45 минут</a>
    </nav>
    <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Меню"><span></span><span></span></button>
  </div>
</header>
<main>
{body.replace('{r}', r)}
</main>
<footer class="site-footer">
  <div class="container footer-inner">
    <p>© <span id="year">2026</span> {BRAND} · {ROLE.lower()} · Сергей Зубков</p>
    <nav class="footer-nav" aria-label="Карта сайта">{fnav}</nav>
    <p class="footer-note">Прототип: названия рабочие, фотографии сгенерированы ИИ и будут заменены. Информация на сайте не является публичной офертой.</p>
  </div>
</footer>
<a class="to-top" href="#top" aria-label="Наверх">↑</a>
<script src="{r}assets/js/main.js"></script>
</body>
</html>
'''
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)

def hero(crumb, eyebrow, title, sub, extra=''):
    c = f'<p class="crumbs"><a href="{{r}}index.html">Главная</a> / {crumb}</p>' if crumb else ''
    return f'''<section class="page-hero"><div class="container">{c}
  <p class="eyebrow reveal">{eyebrow}</p><h1 class="hero-title reveal">{title}</h1>
  <p class="hero-sub reveal">{sub}</p>{extra}</div></section>'''

def sec(id_, eyebrow, title, inner, muted=False, lead=''):
    l = f'<p class="section-lead reveal">{lead}</p>' if lead else ''
    return f'''<section class="section{' section-muted' if muted else ''}" id="{id_}"><div class="container">
  <p class="eyebrow reveal">{eyebrow}</p><h2 class="section-title reveal">{title}</h2>{l}
  {inner}</div></section>'''

CTA = '''<section class="cta-band"><div class="container">
  <h2 class="section-title">Начнём с разговора</h2>
  <p>45 минут: ваш контекст и вопросы. На выходе — понимание, какой объём диагностики вам действительно нужен.</p>
  <div class="hero-cta"><a class="btn btn-primary" href="{r}contact.html">Разговор на 45 минут</a>
  <a class="btn btn-ghost" href="{r}index.html#formats">Форматы и цены</a></div></div></section>'''

# ---------- shared blocks ----------
ZONES = '''<div class="zones">
  <article class="zone zone-green reveal"><p class="zone-tag">ИИ оправдан</p><p class="zone-text">Неструктурированные данные, изменчивость образов, масштаб, прогнозная ценность.</p><p class="zone-example">Детекция плёночных загрязнений по данным БПЛА: точность 91% там, где раньше акваторию патрулировали с судна.</p></article>
  <article class="zone zone-amber reveal"><p class="zone-tag">Гибрид</p><p class="zone-text">ИИ — в части подзадач; правила и человек — на критических решениях.</p><p class="zone-example">Документооборот девелопера: LLM в 3 подзадачах из 8 — только там, где точность выше 95%.</p></article>
  <article class="zone zone-red reveal"><p class="zone-tag">Без ИИ</p><p class="zone-text">Стабильные правила, низкий объём, нетерпимость к ошибке, нехватка данных.</p><p class="zone-example">Предупреждение о подходе судна к ледовой зоне — детерминированная логика: геометрия маршрута и пороги времени.</p></article>
  <article class="zone zone-grey reveal"><p class="zone-tag">Отложить</p><p class="zone-text">Идея разумна, но рано: мало данных, не готовы процессы или нет владельца.</p><p class="zone-example">Сначала навести порядок в данных и регламентах, вернуться к ИИ, когда появится на чём учиться и кому отвечать.</p></article>
</div>'''

MATRIX = '''<div class="matrix-wrap reveal"><table class="matrix">
  <thead><tr><th scope="col">Процесс</th><th scope="col">Решение</th><th scope="col">Допуск</th><th scope="col">Обоснование</th><th scope="col">Эффект / срок</th></tr></thead>
  <tbody>
  <tr><td>Разбор входящих заявок на страхование судов</td><td>%s</td><td><span class="status status-ok">Пилот допустим</span></td><td>Неструктурированные документы, высокий поток, ошибка исправима человеком</td><td>−40–60%% ручного разбора · 3 мес.</td></tr>
  <tr><td>Расчёт тарифа по правилам андеррайтинга</td><td>%s</td><td><span class="status status-ok">Пилот допустим</span></td><td>Правила стабильны и регулируются; нужна полная объяснимость</td><td>Правила в коде · 1 мес.</td></tr>
  <tr><td>Сверка актов выполненных работ с ERP</td><td>%s</td><td><span class="status status-wait">Допустимо после условий</span></td><td>LLM извлекает поля, логика сверяет, спорное — человеку</td><td>−30%% цикла закрытия · 2 мес.</td></tr>
  <tr><td>Прогноз загрузки флота на сезон</td><td>%s</td><td><span class="status status-gap">Недостаточно доказательств</span></td><td>Истории меньше двух лет; сначала собрать данные</td><td>Вернуться через 12 мес.</td></tr>
  </tbody></table></div>
<p class="section-note reveal">Демонстрационный пример, не данные клиента. Цифры условные: в реальном заключении у каждой оценки есть методика и допущения.</p>''' % (chip('ИИ'),chip('Без ИИ'),chip('Гибрид'),chip('Отложить'))

COUNCIL = '''<div class="council">
  <div class="council-lead reveal"><span class="council-num">+1</span><h3>Ведущий агент</h3><p>Уточняет контекст, пока данных не станет достаточно, ставит задачи экспертам, сводит выводы и особые мнения.</p></div>
  <div class="council-grid"><ol class="council-experts">
    <li class="reveal"><span class="council-num">1</span><h3>Процессы</h3><p>Где реальные потери и узкие места</p></li>
    <li class="reveal"><span class="council-num">2</span><h3>Технологии</h3><p>Чем решать: ИИ, правила, интеграция</p></li>
    <li class="reveal"><span class="council-num">3</span><h3>Отрасль</h3><p>Практика и ограничения вашей сферы</p><p class="council-human">+ эксперт-человек</p></li>
    <li class="reveal"><span class="council-num">4</span><h3>Финансы</h3><p>Окупаемость и полная стоимость владения</p><p class="council-human">+ эксперт-человек</p></li>
    <li class="reveal"><span class="council-num">5</span><h3>Право</h3><p>Договоры, данные, ответственность</p><p class="council-human">+ эксперт-человек</p></li>
    <li class="reveal"><span class="council-num">6</span><h3>Комплаенс</h3><p>152-ФЗ, отраслевые требования, закрытые контуры</p></li>
    <li class="reveal"><span class="council-num">7</span><h3>Безопасность ИИ</h3><p>Безопасность моделей (MLSecOps): атаки, утечки, границы автономии</p></li>
  </ol><div class="council-sign reveal"><span class="council-num">= 1 решение</span><h3>Подпись человека</h3><p>Главный конструктор бюро проверяет выводы и подписывает заключение.</p></div></div>
</div>'''

FUNCS = {'caio':'Стратегия и портфель решений ИИ','caito':'Трансформация практик под ИИ',
         'impl':'Архитектура и внедрение','bsm':'Диагностика и бизнес-кейс','ops':'Эксплуатация и контроль границ автономии ИИ-агентов'}
def funcs(*ks): return ' · '.join(FUNCS[k] for k in ks)

CASES = [
 dict(slug='vizard', img='arctic.jpg', tags='Морская безопасность · Арктика и Дальний Восток', card_tags='Морская безопасность · Арктика и ДВ', draft=False,
      title='+13% рейсов по СМП и +14,5% скорости во льдах',
      short='Платформа безопасности плавания для нефтегазовых групп и национального морского перевозчика: ледовая обстановка, маршруты, границы автономии.',
      facts=[('Функции', funcs('caio','ops')),('Контур и стек','Безопасная среда исполнения (safety runtime), 7 модулей в эксплуатации'),('Метрика','<1% выходов агентов за разрешённые границы'),('География и языки','Россия · Китай · Норвегия · Япония — русский, китайский, английский')],
      task='Заказчикам — нефтегазовым группам и морскому перевозчику — требуется повысить безопасность и экономику ледового плавания без потери управляемости: каждое решение агента должно оставаться в разрешённых границах.',
      verdict=[('Ледовая обстановка по спутниковым данным','ИИ','Изменчивые образы, большой поток снимков'),('Предупреждение о подходе к ледовой зоне','Без ИИ','Ошибка недопустима: геометрия маршрута и пороги времени'),('Рекомендации по маршруту','Гибрид','Модель предлагает, капитан решает')],
      result='−65% потерь снастей за 5+ лет. Жёсткие запреты — на уровне среды исполнения, критические решения — с человеком в контуре.'),
 dict(slug='shipping', img='shipping.png', tags='Морское страхование и судовладельцы · международный трек', card_tags='Морское страхование и судовладельцы', draft=False, intl=True,
      title='>2 млрд. руб. экономии для судовладельцев и операторов · 2025–2029',
      short='Метео-бюллетени и контроль страхового покрытия для страховщиков; детекция аномалий флота для судовладельцев. Собственная разработка и внедрение сервиса в семи странах.',
      facts=[('Функции', funcs('bsm','ops')),('География и языки','Россия · Китай · Ближний Восток · Южная Америка · Япония — русский, английский, китайский, испанский'),('Данные','Треки AIS + спутниковые снимки + обезличенные телеком-данные'),('Метрика','≈22% рейсов под защитой услуги · до $9,7–16,6 млн в год предотвращённых потерь (оценка)')],
      task='Страховым компаниям нужен контроль рисков и страхового покрытия флота; промысловым судовладельцам — контроль флота и предотвращение незаконного вылова.',
      verdict=[('Метео- и ситуационные бюллетени','ИИ','Сборка мульти-источниковых данных, персонализация под судно и рейс'),('Контроль страхового покрытия','Без ИИ','Детерминированные правила и пороги — ошибка недопустима'),('Детекция аномалий флота','Гибрид','Модель размечает рассогласования AIS и фактической активности; вывод — после проверки человеком')],
      result='У заказчиков — работающий коммерческий модуль в эксплуатации; для китайского судовладельца выявлен скрытый перегруз вылова отдельными судами в проливе Лаперуза.'),
 dict(slug='morspas', img='oil_spills.png', tags='ФГБУ «Морспасслужба» · мониторинг акваторий', card_tags='Мониторинг акваторий', draft=False,
      title='−38% судо-суток на мониторинг акваторий',
      short='От сплошного визуального патрулирования к точечному мониторингу с БПЛА: ледовая обстановка и нефтяные загрязнения.',
      facts=[('Функции', funcs('impl','ops')),('Метрика','точность 91% · ложных ≤10% · природные «двойники» — 86%'),('Эффект','расходы на мониторинг ниже ~×1,7'),('Данные','Аэрофотосъёмка БПЛА: мультиспектр и ИК, задержка ≤5 с')],
      task='Заказчику требуется сократить дорогое судовое патрулирование акваторий, не теряя полноту обнаружения льда и нефтяных загрязнений.',
      verdict=[('Детекция плёнок по съёмке БПЛА','ИИ','Неструктурированные изображения, масштаб'),('Планирование полётов','Без ИИ','Регламенты и погодные пороги — правила'),('Подтверждение инцидента','Гибрид','Модель отмечает, оператор подтверждает')],
      result='Метрики верифицированы на независимой выборке. В постоянный состав средств МФАСС добавлены БПЛА.'),
 dict(slug='geodesy', img='land_cadastre_remote.jpg', tags='Геодезия и кадастр · закрытый госконтур', card_tags='Геодезия и кадастр · закрытый контур', draft=False, nda=True,
      title='+18% объёма работ филиалов при сокращении штата',
      short='Агент распределяет и приоритизирует работы филиалов в закрытом госконтуре; поверх него — стандарт управления.',
      facts=[('Функции', funcs('caio','impl')),('Контур и стек','На площадке заказчика, без внешних облачных сервисов · суверенные и национальные LLM · система оценки качества'),('Дорожная карта','25 мероприятий · 6 направлений — от методической базы и данных через GeoAI до внедрения в производство'),('Эффект','сокращение штата на 30% при росте эффективности')],
      task='Требуется сохранить объём работ филиалов при сокращении штата — в условиях закрытого госконтура.',
      verdict=[('Планирование загрузки филиалов','ИИ','Много неформализованных факторов'),('Учёт и отчётность','Без ИИ','Достаточно правил и интеграции'),('Распределение срочных заявок','Гибрид','Агент предлагает, руководитель утверждает')],
      result='Агент передан команде проекта; поверх него — матрица границ автономии, ключевые индикаторы риска и система оценки качества.'),
 dict(slug='developer', img='construction.jpg', tags='Девелопмент · топ-3 Москвы', draft=False, nda=True,
      title='LLM в 3 подзадачах из 8 — и это правильно',
      short='Портфель инициатив девелопера топ-3 Москвы: где ИИ оправдан, а где достаточно обычных правил.',
      facts=[('Функции', funcs('caio','bsm')),('Дорожная карта','15 мероприятий по жизненному циклу объекта'),('Метрика','точность LLM >95%'),('Эффект','высвобождено 14+ млн. руб./год ручного труда — экономия на рутинных операциях')],
      task='Требуется разобрать портфель инициатив по жизненному циклу объекта, не тратя бюджет на то, что решается обычной автоматизацией.',
      verdict=[('Извлечение полей из первички','ИИ','Неструктурированные документы'),('Сверка с ERP','Без ИИ','Детерминированные правила'),('Спорные расхождения','Гибрид','Решает человек')],
      result='Гибридный агент Excel → 1С:ERP: LLM только там, где даёт измеримый прирост точности; остальное — детерминированная логика и человек в контуре.'),
 dict(slug='egip', img='city.jpg', tags='ЕГИП г. Москвы · градполитика', draft=False, card_tags='ЕГИП Москвы · градполитика',
      title='37 систем, 60+ ведомств, ~1 млрд. руб. программы',
      short='Единое геоинформационное пространство Москвы: от разрозненных ведомственных данных к управляемой системе.',
      award='Лучшая работа III Международного GIS-Forum',
      facts=[('Функции','Архитектура программы и межведомственная интеграция'),('Данные','1000+ наборов данных · 3D, LiDAR, стереофото, онлайн-телеметрия'),('Процессы','B2G · B2B · B2C: отраслевая аналитика, мобильные инспекции, обратная связь жителей'),('Эффект','поддержка ГИС дешевле ×6,3 · 800+ тыс. жителей в обратной связи')],
      task='Требуется объединить разрозненные данные десятков ведомств в единое геоинформационное пространство города.',
      verdict=[('Интеграция систем','Без ИИ','Требуются стандарты и шины данных, а не модели'),('Качество пространственных данных','Гибрид','Автопроверки и эксперт'),('Аналитика по городу','Отложить','Сначала единые данные')],
      result='Единое пространство как управляемая система: стандарты, межведомственная интеграция, ML-анализ данных лазерного сканирования.'),

 dict(slug='agro', img='agro.jpg', tags='АПК · гео-ML по аэрофотосъёмке', draft=False,
      title='От снимка БПЛА до кейса инспектора — за 2 часа',
      short='ML-детекция сорных и карантинных растений для государственного надзора: от снимка до готового кейса инспектора.',
      facts=[('Функции', funcs('impl','ops')),('Метрика','точность ≥85% при mAP ≥0,70 · на MVP — 65 классов сорняков, 43,6 изобр./мин'),('Данные','БПЛА (RGB + мультиспектр) · тракторные камеры · спутник · планшеты агрономов'),('Эффект','«пустых» выездов меньше на 40% · охват ≥80% площадей за сезон · классов детекции ×3 · точность +9%')],
      task='Надзорному ведомству требуется проверяемая картина состояния полей в промышленном масштабе: заменить выборочные обходы и ручной разбор снимков объективной доказательной базой для предписаний.',
      verdict=[('Детекция сорных растений по снимкам','ИИ','Изменчивые образы, большой объём съёмки'),('Маршрут съёмки и отчётность','Без ИИ','Достаточно правил и шаблонов'),('Решение об обработке поля','Гибрид','Модель размечает, агроном решает')],
      result='Платформа компьютерного зрения выдаёт инспектору готовый кейс с геопривязанной доказательной базой для предписаний.'),
 dict(slug='shelf', img='shelf.jpg', tags='Буровое и насосное оборудование · надёжность', card_tags='Буровое оборудование · надёжность', draft=False,
      title='+17,8 млн руб. за сезон ППБУ · окупаемость от ~13 ч',
      short='Заключение по процессам буровых установок: где ИИ оправдан, а где только детерминированная автоматизация.',
      facts=[('Функции', funcs('caio','ops')),('Процессы','15 сценариев буровых работ — от ТОиР и снабжения до оповещения и отчётности'),('Дорожная карта','бюджет — по сезонам и технологиям, окупаемость с первого года'),('Контур','ИИ вне критической инфраструктуры · модели на борту · на берег — только события')],
      task='Оператору буровых работ на шельфе требуется определить: где ИИ даст измеримый эффект на установках, а где он недопустим по промышленной безопасности и режиму КИИ.',
      verdict=[('Предиктивный ТОиР: насосы, лебёдка, верхний привод','Гибрид','ML ищет ранние признаки деградации; пороги OEM и решение — за механиком'),('Видеоаналитика опасных зон, контроль СИЗ','ИИ','Без компьютерного зрения невозможно; реакция — через сертифицированные системы, не напрямую из модели'),('ПАЗ, ПВО, F&G, оповещение','Без ИИ','Вето комплаенса и ИБ: доказуемое сертифицируемое поведение; ИИ — только параллельный советник')],
      result='Определён порядок запуска: первый пилот ТОиР — на полупогружных установках, где экономика положительная уже в первый сезон; самоподъёмные подключаются при тиражировании. Матрица вердиктов содержит реестр рисков с вето ИБ и комплаенса.'),
 dict(slug='medtech', img='dental.jpg', tags='MedTech · стоматологическая визуализация', card_tags='MedTech · стоматология', chip='Новая ниша · экспортная стратегия', draft=False,
      title='ИИ-микроскоп: согласие пациентов растёт на 30%',
      short='Трёхволновая программа внедрения ИИ в цифровой стоматологический микроскоп: от быстрых функций до первого в мире ИИ-ассистента эндодонтиста.', card_short='Программа внедрения ИИ в стоматологический микроскоп: три волны функций до ИИ-ассистента эндодонтиста.',
      facts=[('Функции', funcs('caio','ops')),('Архитектура','ИИ — отдельным модулем у микроскопа; ПО устройства без изменений'),('Метрика','детекция устьев каналов ~91% · MB2 sens 80–100% · трещины до 97,8%'),('Эффект','выручка +$30 тыс./год на врача · КП быстрее ×7')],
      task='Производителю цифрового стоматологического микроскопа требуется программа внедрения ИИ, повышающая ценность устройства и продажи — без изменения оптической схемы.',
      verdict=[('Улучшение изображения, голосовое управление, автопротоколы','ИИ','Неструктурированный видео- и речевой вход; вне диагностических заявлений — без регистрации медизделия'),('Детекция устьев каналов и трещин в реальном времени','Гибрид','Модель подсвечивает на отдельном модуле у микроскопа, врач подтверждает; ПО самого устройства не меняется'),('Автономная постановка диагноза','Отложить','Цена ошибки недопустима без клинической валидации — решение остаётся за врачом')],
      result='Определена последовательность внедрения: функции вне диагностики за 6–12 месяцев, клинический ассистент после сбора датасета и валидации, затем AR-оверлей и телементоринг. Заказчику выдана стратегия занятия новой ниши с экспортным треком.'),
]

def case_card(c, r='{r}'):
    ph = photo(r, c['img'], c['tags'])
    if c.get('award'):
        ph = ph.replace('</figure>', '<span class="award-star" data-tip="Отмечено наградой"><svg viewBox="0 0 24 24"><path d="M8 13l-2.5 8L12 18l6.5 3L16 13"/><circle cx="12" cy="9" r="6"/><path d="M12 6l1.1 2.2 2.4.3-1.8 1.7.5 2.4L12 11.5 9.8 12.6l.5-2.4-1.8-1.7 2.4-.3z"/></svg></span></figure>')
    if c.get('intl') == 'badge':
        ph = ph.replace('</figure>', '<span class="intl-badge" data-tip="Международный кейс"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.6 3 14.4 0 18M12 3c-3 3.6-3 14.4 0 18"/></svg></span></figure>')
    elif c.get('intl') == 'tag':
        ph = ph.replace('</figure>', '<span class="intl-tag">INTL</span></figure>')
    elif c.get('intl'):
        ph = ph.replace('</figure>', '<span class="ribbon-intl">Международный</span></figure>')
    return f'''<a class="card reveal" href="{r}cases/{c['slug']}.html">{ph}
  <p class="card-tags">{c.get('card_tags', c['tags'])}</p><h3>{c['title']}</h3><p>{c.get('card_short', c['short'])}</p><span class="more">Разбор кейса →</span></a>'''

INDUSTRIES = [
 ('mining.jpg','Добыча полезных ископаемых','Углеводороды и руды. Безопасность и логистика в суровых средах: шельф, лёд, удалённость.','Типично: ИИ — в видеоаналитике и прогнозе отказов; без ИИ — в допусках и регламентах безопасности.'),
 ('city.jpg','Городская инфраструктура','Межведомственная интеграция и городские данные: 60+ ведомств, закрытые контуры, 44-ФЗ / 223-ФЗ.','Типично: сначала единые данные и интеграция; ИИ — в обращениях граждан и анализе ДЗЗ.'),
 ('construction.jpg','Строительство и девелопмент','Весь жизненный цикл объекта: изыскания, проектирование, строительство, эксплуатация, продажи.','Типично: гибрид в документообороте; без ИИ — в сметах и сверках.'),
 ('arctic.jpg','Морская логистика и страхование','Флот и риски: метеообеспечение, контроль страхового покрытия, экономика редких, но крупных событий.','Типично: ИИ — в ледовой обстановке и разборе заявок; без ИИ — в тарифах и предупреждениях.'),
 ('agro.jpg','Сельское хозяйство','Гео-ML мониторинг полей: от аэрофотосъёмки до результата для инспектора за 2 часа вместо 3 дней.','Типично: ИИ — в детекции по снимкам (mAP@0.5 > 80%); отложить — где нет истории урожаев.'),
 ('dental.jpg','Медтехника и здравоохранение','Медицинские изделия и диагностика: ИИ-функции, регистрация ПО как медизделия, ЭПР, клиническая валидация.','Типично: ИИ — в визуализации и документации; автодиагноз — после датасета и валидации.'),
]

FORMATS = [
 ('Шаг 1','Экспресс-скрининг','Короткая анкета и первичная карта: где ИИ стоит рассмотреть, а где точно нет. Онлайн через '+PLAT+'.','бесплатно · скоро'),
 ('Шаг 2','Диагностика','Фикс-скоуп: аудит процессов, матрица решений, бизнес-кейс, дорожная карта. 2–4 недели.','от 500 000 руб. за этап · возможна доля от эффекта (revenue share)'),
 ('Шаг 3','Fractional CAIO','Внешний директор по ИИ на неполную занятость: стратегия, управление ИИ-функцией, контроль внедрений. От 3 месяцев.','от 200 000 руб./мес · день в неделю — от 350 000 руб./мес'),
 ('Шаг 4','Внедрение','Команда бюро делает то, что прошло диагностику. Стандарт промышленной эксплуатации, развёртывание на площадке заказчика при необходимости.','оценка после диагностики'),
 ('Шаг 4 · или','Авторский надзор','Внедряют ваши разработчики или подрядчики, бюро контролирует соответствие заключению и архитектуре, принимает этапы.','по объёму внедрения'),
]
def formats_html():
    return '<div class="formats formats-4 formats-5">' + ''.join(f'<div class="format reveal"><p class="format-step">{a}</p><h3 class="format-name">{b}</h3><p class="format-text">{c}</p><p class="format-price">{d}</p></div>' for a,b,c,d in FORMATS) + '</div>'

FAQ = [
 ('Сколько это стоит?','Диагностика — фикс-цена по скоупу. Внедрение оценивается после того, как понятен действительно необходимый объём. Если ИИ вам не нужен, вы узнаете это на диагностике, а не в конце бюджета.'),
 ('А если вы решите, что ИИ нам не нужен?','Это нормальный и частый результат. Вы получаете матрицу решений и дорожную карту обычной автоматизации и экономите бюджет на ненужном. Для бюро это такой же успешный проект, как внедрение.'),
 ('Работаете с закрытыми контурами?','Да: развёртывание на площадке заказчика (on-prem) и инфраструктура ML (MLOps), суверенные стеки больших языковых моделей (LLM), 152-ФЗ, изолированные контуры без внешних облачных сервисов. Ключевые внедрения — именно там.'),
 ('Кто делает работу?','Анализ готовит '+PLAT+'. Выводы по праву, финансам и отрасли проверяют приглашённые эксперты: юрист, финансист-экономист, отраслевой специалист. Диагностику и архитектуру ведёт и подписывает Сергей Зубков. Внедряют DS/ML-инженеры бюро, без анонимных субподрядчиков.'),
 ('Можно внедрять своими силами или с другим подрядчиком?','Да. Тогда бюро ведёт авторский надзор: проверяет, что решение соответствует заключению и архитектуре, принимает этапы и контролирует метрики.'),
 ('Чем вы отличаетесь от интегратора?','Интегратор зарабатывает на внедрении, поэтому заинтересован внедрять. Бюро зарабатывает на заключении и отвечает за него — поэтому может честно сказать «не нужно».'),
]
def faq_html(items):
    return '<div class="container-narrow" style="margin:0">' + ''.join(f'<details class="faq-item reveal"{" open" if i==0 else ""}><summary>{q}</summary><div class="faq-body"><p>{a}</p></div></details>' for i,(q,a) in enumerate(items)) + '</div>'

# ================= INDEX =================
PAINS = [
 ('ИИ внедрили — эффекта нет','Разберём, что пошло не так: метрика, процесс или выбор задачи.'),
 ('Непонятно, нужен ли ИИ вообще','По каждому процессу — вердикт с обоснованием, включая «ИИ не нужен».'),
 ('Интегратор продаёт внедрение','Мы зарабатываем на заключении, а не на человеко-часах внедрения — у нас есть право сказать «нет».'),
 ('Регуляторика и ИБ блокируют','Закрытые контуры, 152-ФЗ, отраслевые запреты — в заключении есть статус допуска и вето.'),
 ('Нет метрики до проекта','Бизнес-кейс с формулой и допущениями до первого рубля внедрения.'),
 ('Инициатив больше, чем ресурсов','Порядок запуска и бюджет по волнам — что первым, что при тираже.')]
pains = '<div class="card-grid">' + ''.join(f'<article class="card reveal"><h3>{h}</h3><p>{p}</p></article>' for h,p in PAINS) + '</div>'

STEPS3 = '''<ol class="steps steps-3">
 <li class="step reveal"><span class="step-num">01</span><h3 class="step-title">Разговор</h3><p class="step-meta">45 минут</p><p class="step-text">Ваш контекст и вопросы. На выходе — первичная карта: где есть смысл смотреть, а где точно нет.</p></li>
 <li class="step reveal"><span class="step-num">02</span><h3 class="step-title">Диагностика</h3><p class="step-meta">2–4 недели</p><p class="step-text">Вердикт и допуск по каждому процессу, бизнес-кейс, дорожная карта — в подписанном заключении. Заключение — самостоятельный продукт, а не приглашение на внедрение.</p></li>
 <li class="step reveal"><span class="step-num">03</span><h3 class="step-title">Внедрение</h3><p class="step-meta">по дорожной карте</p><p class="step-text">Бюро делает то, что прошло диагностику, — или ведёт авторский надзор за вашими подрядчиками.</p></li>
</ol>'''

IND_SLUGS = [['shelf'],['egip','geodesy'],['developer'],['vizard','shipping','morspas'],['agro'],['medtech']]
BY_SLUG = {c['slug']: c for c in CASES}
def exp_card(ind, slugs):
    i,n,t,v = ind
    links = ''.join(f'<a class="ind-case" href="{{r}}cases/{s}.html">{BY_SLUG[s]["title"]}</a>' for s in slugs)
    return f'<article class="card reveal"><h3>{n}</h3><p>{t}</p><p class="card-tags" style="text-transform:none">{v}</p><div class="ind-cases">{links}</div></article>'
experience = '<div class="card-grid">' + ''.join(exp_card(ind, IND_SLUGS[k]) for k,ind in enumerate(INDUSTRIES)) + '</div>'

index = f'''<section class="hero"><div class="container hero-grid">
  <div class="hero-copy">
    <p class="eyebrow reveal">{ROLE} · Диагностика до внедрения</p>
    <h1 class="hero-title reveal">Вам продают внедрение ИИ.<br><em>Мы — ответ, нужен ли он.</em></h1>
    <p class="hero-sub reveal">По каждому процессу — вердикт: ИИ, гибрид, обычная автоматизация или «пока не нужно». Сначала диагностика и подписанное заключение с экономикой и рисками — потом работа.</p>
    <div class="hero-cta reveal"><a class="btn btn-primary" href="{{r}}contact.html">Разговор на 45 минут</a><a class="btn btn-ghost" href="{{r}}cases.html">Кейсы с цифрами</a></div>
    <p class="hero-meta reveal">Ведёт Сергей Зубков, основатель и главный конструктор · 20+ лет в IT и данных · RU / EN</p>
  </div>
  <figure class="verdict-card reveal" aria-label="Фрагмент заключения: вердикты по процессам">
    <figcaption class="verdict-head"><span>Заключение · фрагмент</span><span>7 / 7 проверок</span></figcaption>
    <ul class="verdict-list">
      <li><span class="v-proc">Детекция загрязнений по съёмке БПЛА</span>{chip('ИИ')}</li>
      <li><span class="v-proc">Сверка первички Excel → ERP</span>{chip('Гибрид')}</li>
      <li><span class="v-proc">Предупреждение о ледовой зоне</span>{chip('Без ИИ')}</li>
      <li><span class="v-proc">Прогноз спроса на услуги филиалов</span>{chip('Отложить')}</li>
    </ul>
    <p class="verdict-foot">Решение подписывает человек · особые мнения экспертов сохраняются</p>
  </figure>
</div></section>
<section class="numbers" aria-label="Результаты клиентов"><div class="container numbers-grid">
  <div class="number-item reveal"><div class="number-value">−38%</div><div class="number-caption">судо-суток на&nbsp;мониторинг акваторий: БПЛА вместо патрулирования</div></div>
  <div class="number-item reveal"><div class="number-value">+18%</div><div class="number-caption">объёма работ филиалов при сокращении штата на&nbsp;30%, закрытый контур</div></div>
  <div class="number-item reveal"><div class="number-value">+13%</div><div class="number-caption">рейсов по&nbsp;Северному морскому пути с&nbsp;ИИ-модулями платформы</div></div>
  <div class="number-item reveal"><div class="number-value accent">3&nbsp;из&nbsp;8</div><div class="number-caption">подзадач документооборота получили LLM. Остальным ИИ не&nbsp;нужен</div></div>
</div></section>
{sec('pains','Задачи','С чем к нам приходят', pains)}
{sec('how','Как работаем','Разговор → заключение → внедрение', STEPS3, muted=True)}
{sec('experience','Опыт','Отрасли и подтверждённые результаты', experience)}
{sec('formats','Форматы','От бесплатного скрининга до внедрения — шаг за шагом', formats_html(), muted=True)}
<section class="section" id="bureau"><div class="container split">
  <div><p class="eyebrow reveal">Бюро</p><h2 class="section-title reveal">Как конструкторское бюро: главный конструктор, расчёты, исполнение</h2>
  <div class="prose reveal"><p>Сергей Зубков лично ведёт диагностику и архитектуру и подписывает каждое заключение. Выводы по праву, финансам и отрасли проверяют приглашённые эксперты. Внедряет инженерная команда бюро или ваши подрядчики под нашим авторским надзором.</p>
  <p>20+ лет в IT и данных, 8+ лет в ИИ-проектах, 3 ИИ-продукта на рынке. Hands-on: сам проектирует и пишет код.</p></div></div>
  {photo('{r}','founder.jpg','Сергей Зубков, основатель бюро','photo-34 reveal', gen=False)}
</div></section>
{CTA}'''
page('index.html', f'{BRAND} — {ROLE.lower()} · Сергей Зубков', 'Диагностика процессов до внедрения ИИ: где ИИ оправдан, где нужен гибрид, где достаточно обычной автоматизации. Добыча, морская логистика, город, АПК, медтехника.', index)

# ================= CASES =================
cases = hero('Кейсы','Кейсы','Где ИИ был нужен — и где мы его не поставили','Каждый кейс разобран по схеме: задача → вердикты по процессам → результат.') + \
 sec('list','Все кейсы','Подтверждённые результаты', '<div class="card-grid">'+''.join(case_card(c) for c in CASES)+'</div>') + CTA
page('cases.html', f'Кейсы — {BRAND}', 'Кейсы бюро: морская безопасность, мониторинг акваторий, закрытый госконтур, девелопмент, ЕГИП Москвы.', cases, 'cases.html')
for i,c in enumerate(CASES):
    nxt = CASES[(i+1)%len(CASES)]
    facts = '<dl class="facts reveal">' + ''.join(f'<div><dt>{a}</dt><dd>{nb(b)}</dd></div>' for a,b in c['facts']) + '</dl>'
    vt = '<div class="matrix-wrap reveal"><table class="matrix"><thead><tr><th>Процесс</th><th>Решение</th><th>Обоснование</th></tr></thead><tbody>' + ''.join(f'<tr><td>{a}</td><td>{chip(b)}</td><td>{d}</td></tr>' for a,b,d in c['verdict']) + '</tbody></table></div>'
    body = f'''<section class="page-hero"><div class="container"><p class="crumbs"><a href="{{r}}index.html">Главная</a> / <a href="{{r}}cases.html">Кейсы</a></p>
  <p class="eyebrow reveal">{c['tags']}{' <span class="nda-tag">детали под NDA</span>' if c.get('nda') else ''}{' <span class="nda-tag award-chip">' + c['award'] + '</span>' if c.get('award') else ''}{' <span class="nda-tag award-chip">' + c['chip'] + '</span>' if c.get('chip') else ''}</p><h1 class="hero-title reveal">{nb(c['title'])}</h1><p class="hero-sub reveal">{nb(c['short'])}</p>
  {photo('{r}',c['img'],c['tags'],'photo-wide reveal',c.get('gen',True)).replace('</figure>', f'<span class="award-tag">{c["award"]}</span></figure>') + f'<p class="award-cap">{c["award"]}</p>' if c.get('award') else photo('{r}',c['img'],c['tags'],'photo-wide reveal',c.get('gen',True))}{facts}</div></section>
<section class="section"><div class="container split split-fill">
  <div class="prose reveal"><div><p class="eyebrow">Задача</p><p>{nb(c['task'])}</p></div>
  <div><p class="eyebrow">Результат</p><p>{nb(c['result'])}</p>
  {'<p class="draft-note">Черновик разбора: детали уточнить с основателем, NDA-ограничения проверить</p>' if c.get('draft', True) else ''}</div></div>
  <div><p class="eyebrow reveal">Вердикты по процессам</p>{vt}</div>
</div></section>
<section class="section section-muted"><div class="container"><p class="eyebrow">Следующий кейс</p><div class="card-grid card-grid-2">{case_card(nxt)}</div></div></section>
{CTA}'''
    page(f"cases/{c['slug']}.html", f"{c['title']} — кейс {BRAND}", c['short'], body, 'cases.html')

# ================= SAMPLE =================
page('sample.html', f'Пример заключения — {BRAND}', 'Пример базовой диагностики на синтетических данных: выводы, достаточность сведений, матрица решений с условиями. Полная версия — в обмен на рабочий email.', hero('Пример заключения','Пример заключения','Так выглядит заключение бюро','Базовая диагностика на синтетических данных: вымышленный проектный институт ТЭК. Первые четыре раздела открыты, полный отчёт — в обмен на рабочий email.') + sample_report('ru', chip) + CTA)

# ================= CONTACT =================
contact = hero('Контакт','Контакт','Начнём с разговора — не с бюджета','45 минут: ваш контекст, ваши вопросы — и понимание, какой объём диагностики вам действительно нужен. Без презентаций «про возможности ИИ».') + \
 f'''<section class="section"><div class="container split">
 <div><div class="contact-links reveal">
  <a class="contact-link" href="mailto:zubkovfpk@gmail.com"><span class="contact-label">Email</span><span class="contact-value">zubkovfpk@gmail.com</span></a>
  <a class="contact-link" href="https://t.me/SergeyAZubkov" target="_blank" rel="noopener"><span class="contact-label">Telegram</span><span class="contact-value">@SergeyAZubkov</span></a>
  <a class="contact-link" href="https://www.linkedin.com/in/sergey-a-zubkov" target="_blank" rel="noopener"><span class="contact-label">LinkedIn</span><span class="contact-value">sergey-a-zubkov</span></a></div>
  <p class="contact-note reveal">Отвечает Сергей лично. Данные из переписки не передаются третьим лицам и не используются для рассылок.</p></div>
 <form class="form reveal" action="mailto:zubkovfpk@gmail.com" method="post" enctype="text/plain">
  <label>Имя<input name="name" required></label>
  <label>Компания и роль<input name="company"></label>
  <label>Отрасль<select name="industry"><option>Добыча</option><option>Морская логистика и страхование</option><option>Город и инфраструктура</option><option>Строительство</option><option>Сельское хозяйство</option><option>Медтехника</option><option>Другое</option></select></label>
  <label>Что хотите обсудить<textarea name="message"></textarea></label>
  <button class="btn btn-primary" type="submit">Отправить</button>
  <p class="contact-note">Прототип: форма открывает почтовый клиент. В продакшене — отправка на сервер.</p>
 </form></div></section>'''
page('contact.html', f'Контакт — {BRAND}', 'Разговор на 45 минут с Сергеем Зубковым: контекст, вопросы и необходимый объём диагностики.', contact, 'contact.html')

# ================= 404 =================
page('404.html', f'Страница не найдена — {BRAND}', 'Страница не найдена.', hero('','404','Такой страницы нет. Вердикт — «отложить».','<a href="{r}index.html">На главную →</a>'))

# ================= sitemap / robots =================
base = ['','cases.html','contact.html','sample.html'] + [f"cases/{c['slug']}.html" for c in CASES]
pages = base + ['en/'+x for x in base]
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}/{x}</loc></url>\n' for x in pages) + '</urlset>\n')
open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
print('built RU', len(base)+1, 'pages')
import runpy; runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)),'build_en.py'))
