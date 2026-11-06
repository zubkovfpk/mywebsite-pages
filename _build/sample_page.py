# -*- coding: utf-8 -*-
# Synthetic sample assessment ("Institute N"): all facts and figures are fictional.

def _table(head, rows):
    h = ''.join(f'<th scope="col">{x}</th>' for x in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="matrix-wrap"><table class="matrix"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

def _ul(items):
    return '<ul class="tick-list">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def _sec(n, title, inner):
    return f'<section class="r-sec"><h3><span class="r-num">{n}</span>{title}</h3>{inner}</section>'

T = {
'ru': dict(
 kicker='Отчёт по итогам базовой диагностики · версия 1.0',
 title='«Институт N»: черновики проектной документации на основе исторических аналогов',
 meta='Проектный институт ТЭК · около 900 сотрудников · подготовлено бюро по запросу заказчика',
 synth='Синтетический пример: организация, цифры и выводы вымышлены, совпадения случайны. Структура — как в реальных заключениях бюро.',
 s1='Основные выводы',
 s1_items=['<b>Запрос реалистичен, но ИИ нужен лишь в части задач.</b> Спецификации и чертежи институт уже выпускает из 3D-модели и базы оборудования — это зона классической автоматизации. ИИ нужен для поиска аналогов в неструктурированном архиве и для черновиков текстовых частей.',
  '<b>Три сценария с наибольшим эффектом:</b> гибридный поиск аналогов; черновики текстовых разделов со ссылкой на каждый фрагмент источника; черновики ответов на замечания экспертизы.',
  '<b>Партнёр, а не «коробка».</b> У института сильная собственная ИТ-команда. Предложение должно усиливать её: методика, архитектура закрытого контура, оценка качества, безопасность ИИ.',
  '<b>Главные риски — правовые и режимные, а не технологические:</b> права заказчиков на документацию, сведения о безопасности объектов ТЭК, возможный статус субъекта КИИ.',
  '<b>Неотложная мера:</b> до запуска закрытого контура прекратить загрузку проектной документации в публичные облачные чат-боты.',
  '<b>Следующий шаг:</b> расширенная диагностика 6–8 недель на 3–5 завершённых проектах одного типа, затем пилот 3–4 месяца на 1–2 текстовых разделах. Порядок эффекта — 10–33 эквивалента полной занятости (гипотеза).'],
 s2='Рамки и исходные данные',
 s2_p='Базовая диагностика выполнена по формулировке запроса, открытым источникам и четырём документам заказчика, без доступа к внутренним системам. Все количественные оценки — гипотезы для проверки на расширенной диагностике. Анализ подготовили ведущий агент и семь экспертных ролей Council 7+1; выводы по праву, финансам и отрасли проверили эксперты-люди. Вето по праву, комплаенсу и безопасности обязательны.',
 s3='Достаточность сведений по процессам',
 s3_note='Шкала: Д — достаточно для проектирования; Ч — частично, хватает для концепции; Н — недостаточно.',
 s3_head=['Процесс','Оценка','Чего не хватает'],
 s3_rows=[['Поиск аналогов','Ч','Объём и форматы архива, доля сканов, метаданные'],['Текстовые разделы ПД','Ч','Самые трудоёмкие разделы, замер трудозатрат'],['Спецификации и ведомости','Д','—'],['Ответы на замечания экспертизы','Н','Хранится ли история замечаний в цифровом виде'],['Нормоконтроль оформления','Д','—']],
 s4='Матрица решений по подзадачам',
 s4_head=['Подзадача','Рекомендация','Условия','Почему'],
 s4_rows=[['Оцифровка архива','Гибрид','Контроль качества распознавания на выборке','Стандартное распознавание и разметка структуры; генеративная модель не нужна'],
  ['Поиск аналогов','Гибрид','Фильтр прав до поиска; аналог подтверждает инженер','Метаданные отсекают лишнее, семантический поиск находит похожие решения'],
  ['Черновики текстовых частей','ИИ','Обязательная проверка; числа — только из источников','Вариативный текст с повторяемыми формулировками; ссылка на каждый фрагмент'],
  ['Спецификации и ведомости','Без ИИ','ИИ — только сопоставление позиций с кодами базы оборудования','Источник истины — 3D-модель; модель может «придумать» позицию'],
  ['Чертежи','Отложить','Пересмотреть, когда функции появятся у вендора САПР','Выпуск по 3D-модели уже работает; генеративная графика незрелая'],
  ['Ответы на замечания','ИИ','История замечаний в цифровом виде','Поиск похожих замечаний и черновик ответа со ссылками']],
 s5='Ключевые развилки',
 s5_p=['<b>Спецификации.</b> Точность позиций, кодов и количеств абсолютна, а источник истины уже есть. Генеративная модель здесь снижает качество: ненулевая доля ошибочных позиций, которые инженер может пропустить.',
  '<b>RAG или дообучение.</b> Дообучение «запекает» в модель устаревшие решения и сведения разных заказчиков и не даёт ссылок на источник. RAG сохраняет происхождение, права и актуальность.'],
 s6='Неотложные меры',
 s6_items=['Временная политика использования ИИ: запрет загрузки проектной документации во внешние сервисы.','Перечень разделов, исключаемых из корпуса по режимным основаниям.'],
 s7='Целевой процесс',
 s7_items=['Инженер задаёт тип объекта и раздел → правила отбирают допустимый корпус по правам доступа.','ИИ находит аналоги и готовит черновик со ссылкой на каждый фрагмент.','Автопроверки сверяют числа и нормативные ссылки с источниками.','Инженер проверяет, правит и подписывает; журнал фиксирует источник каждого фрагмента.'],
 s8='Реестр рисков ИБ, права и комплаенса',
 s8_head=['Риск','Основание','Мера'],
 s8_rows=[['ИИ-система в контуре значимого объекта КИИ','187-ФЗ','Определить статус; размещение вне ЗОКИИ'],['Утечка сведений одного заказчика в проект другого','Договоры, коммерческая тайна','Изолированные индексы, фильтр прав до поиска'],['Ошибки черновика пропущены при проверке','Ответственность проектировщика','Ссылки на источники, автопроверки, подсветка изменений'],['Непрямые prompt-инъекции через документы','Угрозы ИИ','Очистка текста, только чтение, без автономных действий'],['Несоответствие лицензии модели','Лицензии разработчиков','Юридическая проверка до пилота']],
 s9='Варианты дорожной карты',
 s9_head=['Вариант','Состав','Когда выбирать'],
 s9_rows=[['A. Минимальный','Поиск аналогов без генерации текста','Права на корпус не ясны, нет GPU'],['B. Базовый (рекомендуем)','A + черновики 1–2 разделов + ответы на замечания','Права подтверждены, есть выборка проектов'],['C. Расширенный','B + тиражирование на разделы и дисциплины','После подтверждения эффекта пилота']],
 s10='Модель эффекта',
 s10_p='ЭПЗ = N × d × k: N — проектировщики, работающие с текстовыми разделами (≈520); d — доля их времени на поиск аналогов, тексты и ответы на замечания (8–14 %); k — сокращение этого времени (25–45 %). Итог: 10–33 ЭПЗ. Все параметры — допущения для замера.',
 s11='Состав расширенной диагностики',
 s11_items=['Данные и корпус: инвентаризация архива, пробное распознавание.','Процессы: интервью с ГИП, замер трудоёмкости.','Право и комплаенс: аудит договоров, статус КИИ.','Архитектура и ИБ: модель угроз, тест 2–3 локальных моделей.','Экономика: модель эффекта, TCO, критерии «продолжать / остановить».'],
 s12='Вопросы к заказчику',
 s12_items=['Какие разделы ПД наиболее трудоёмки и повторяемы?','Каков объём архива и доля сканов?','Есть ли категорированные объекты КИИ?','Как договоры регулируют повторное использование документации?','Есть ли GPU-ресурсы в контуре?','Кто владелец процесса и руководитель пилота?'],
 s13='Особые мнения экспертов',
 s13_items=['<b>Отраслевой эксперт:</b> часть функций может появиться у вендора САПР — пилот стоит фокусировать на знаниях архива.','<b>Финансовый эксперт:</b> если замер покажет d &lt; 8 %, начинать с варианта A.','<b>Безопасность ИИ:</b> без разграничения доступа на уровне фрагмента пилот на реальном корпусе запускать нельзя.'],
 s14='Источники',
 s14_p='В реальном заключении — пронумерованные ссылки на открытые данные, нормативные акты и материалы заказчика.',
 thanks='<b>Спасибо!</b> Полная версия открыта ниже. В рабочей версии сайта PDF придёт на почту, а дальше — не больше трёх писем или звонков.',
 gate_kicker='Полная версия · ещё 10 разделов',
 gate_title='Полный отчёт — в обмен на ваш рабочий email',
 gate_list='Дальше: развилки, неотложные меры, целевой процесс, реестр рисков, варианты A/B/C, модель эффекта, состав расширенной диагностики, вопросы, особые мнения.',
 promise=['Пришлём PDF на почту сразу.','Не больше трёх писем или звонков от Сергея Зубкова — только по делу.','Без рассылок и передачи третьим лицам.'],
 f_name='Имя', f_company='Компания и роль', f_email='Рабочий email', f_phone='Телефон или Telegram — по желанию',
 f_consent='Согласен на обработку персональных данных для отправки отчёта и связи по нему',
 f_btn='Получить полный отчёт',
 f_note='Прототип: данные никуда не отправляются. В рабочей версии полный текст не будет храниться на странице — только в письме.',
),
'en': dict(
 kicker='Baseline diagnostic report · version 1.0',
 title='“Institute N”: drafting design documentation from historical analogues',
 meta='Energy-sector design institute · about 900 employees · prepared by the bureau at the client’s request',
 synth='Synthetic example: the organisation, figures and findings are fictional; any resemblance is coincidental. The structure follows the bureau’s real assessments.',
 s1='Key findings',
 s1_items=['<b>The request is realistic, but AI fits only part of it.</b> The institute already produces specifications and drawings from its 3D model and equipment database — that is conventional automation. AI is needed to find analogues in the unstructured archive and to draft text sections.',
  '<b>Three scenarios with the greatest effect:</b> hybrid analogue search; drafts of text sections with a link to every source fragment; drafts of replies to review comments.',
  '<b>A partner, not a boxed product.</b> The institute has a strong in-house IT team. The proposal should strengthen it: method, closed-environment architecture, quality evaluation, AI security.',
  '<b>The main risks are legal and regulatory, not technological:</b> clients’ rights to documentation, security-sensitive data on energy facilities, possible critical-infrastructure status.',
  '<b>Urgent measure:</b> stop uploading design documentation to public cloud chatbots until the closed environment is running.',
  '<b>Next step:</b> 6–8 weeks of extended diagnostics on 3–5 completed projects of one type, then a 3–4-month pilot on 1–2 text sections. Order of effect: 10–33 full-time equivalents (hypothesis).'],
 s2='Scope and inputs',
 s2_p='The baseline diagnostics used the request, open sources and four client documents, without access to internal systems. All figures are hypotheses to be verified in extended diagnostics. The analysis was prepared by the lead agent and the seven expert roles of Council 7+1; legal, financial and industry findings were reviewed by human experts. Legal, compliance and security vetoes are binding.',
 s3='Information sufficiency by process',
 s3_note='Scale: S — sufficient for design; P — partial, enough for a concept; I — insufficient.',
 s3_head=['Process','Rating','What is missing'],
 s3_rows=[['Analogue search','P','Archive size and formats, share of scans, metadata'],['Text sections of design documentation','P','Most labour-intensive sections, time measurement'],['Specifications and schedules','S','—'],['Replies to review comments','I','Whether comment history is stored digitally'],['Formatting compliance checks','S','—']],
 s4='Decision matrix by subtask',
 s4_head=['Subtask','Recommendation','Conditions','Why'],
 s4_rows=[['Archive digitisation','Hybrid','Recognition quality checked on a sample','Standard recognition and layout parsing; no generative model needed'],
  ['Analogue search','Hybrid','Rights filter before search; an engineer confirms the analogue','Metadata filter out the irrelevant; semantic search finds similar solutions'],
  ['Drafts of text sections','AI','Mandatory review; numbers only from sources','Variable text with recurring wording; a link for every fragment'],
  ['Specifications and schedules','No AI','AI only to match items to equipment-database codes','The 3D model is the source of truth; a model may “invent” an item'],
  ['Drawings','Defer','Revisit when the CAD vendor ships such features','Output from the 3D model already works; generative graphics are immature'],
  ['Replies to review comments','AI','Comment history in digital form','Finding similar comments and drafting a reply with links']],
 s5='Key trade-offs',
 s5_p=['<b>Specifications.</b> Item, code and quantity accuracy must be absolute, and a source of truth already exists. A generative model lowers quality here: a non-zero share of wrong items an engineer may miss.',
  '<b>RAG or fine-tuning.</b> Fine-tuning bakes outdated solutions and different clients’ data into the model and gives no source links. RAG preserves provenance, rights and currency.'],
 s6='Urgent measures',
 s6_items=['An interim AI-use policy: no uploads of design documentation to external services.','A list of sections excluded from the corpus on security grounds.'],
 s7='Target process',
 s7_items=['The engineer sets the facility type and section → rules select the permitted corpus by access rights.','AI finds analogues and drafts text with a link to every fragment.','Automatic checks reconcile numbers and standards references with sources.','The engineer reviews, edits and signs; the log records the source of every fragment.'],
 s8='Security, legal and compliance risk register',
 s8_head=['Risk','Basis','Mitigation'],
 s8_rows=[['AI system inside a significant critical-infrastructure object','Critical-infrastructure law','Determine status; host outside the protected perimeter'],['One client’s data leaking into another’s project','Contracts, trade secrets','Isolated indexes, rights filter before search'],['Draft errors missed in review','Designer’s liability','Source links, automatic checks, change highlighting'],['Indirect prompt injection via documents','AI threats','Text sanitisation, read-only, no autonomous actions'],['Model licence non-compliance','Model developers’ licences','Legal review before the pilot']],
 s9='Roadmap options',
 s9_head=['Option','Scope','When to choose'],
 s9_rows=[['A. Minimal','Analogue search without text generation','Corpus rights unclear, no GPUs'],['B. Core (recommended)','A + drafts of 1–2 sections + replies to comments','Rights confirmed, a sample of projects exists'],['C. Extended','B + rollout to more sections and disciplines','After the pilot effect is confirmed']],
 s10='Effect model',
 s10_p='FTE = N × d × k: N — designers working on text sections (≈520); d — share of their time spent on analogue search, texts and replies to comments (8–14%); k — reduction of that time (25–45%). Result: 10–33 FTE. All parameters are assumptions to be measured.',
 s11='Scope of extended diagnostics',
 s11_items=['Data and corpus: archive inventory, trial recognition.','Processes: interviews with chief project engineers, time measurement.','Legal and compliance: contract audit, critical-infrastructure status.','Architecture and security: threat model, test of 2–3 local models.','Economics: effect model, TCO, continue / stop criteria.'],
 s12='Questions for the client',
 s12_items=['Which design sections are the most labour-intensive and repetitive?','How large is the archive and what share is scanned?','Are there categorised critical-infrastructure objects?','How do contracts govern reuse of documentation?','Are GPU resources available in the environment?','Who owns the process and leads the pilot?'],
 s13='Dissenting views',
 s13_items=['<b>Industry expert:</b> some features may come from the CAD vendor — focus the pilot on archive knowledge.','<b>Financial expert:</b> if measurement shows d &lt; 8%, start with option A.','<b>AI security:</b> no pilot on the real corpus without fragment-level access control.'],
 s14='Sources',
 s14_p='A real assessment contains numbered references to open data, regulations and client materials.',
 thanks='<b>Thank you!</b> The full version is open below. On the live site the PDF will arrive by email, followed by no more than three emails or calls.',
 gate_kicker='Full version · 10 more sections',
 gate_title='The full report in exchange for your work email',
 gate_list='Next: trade-offs, urgent measures, target process, risk register, options A/B/C, effect model, extended diagnostics scope, questions, dissenting views.',
 promise=['We send the PDF by email right away.','No more than three emails or calls from Sergey Zubkov — strictly on topic.','No newsletters, no sharing with third parties.'],
 f_name='Name', f_company='Company and role', f_email='Work email', f_phone='Phone or Telegram — optional',
 f_consent='I agree to the processing of my personal data to receive the report and be contacted about it',
 f_btn='Get the full report',
 f_note='Prototype: data is not sent anywhere. On the live site the full text will not be stored on the page — only in the email.',
)}

def sample_report(lang, chip):
    L = T[lang]
    s4_rows = [[a, chip(b), c, d] for a, b, c, d in L['s4_rows']]
    open_part = (_sec(1, L['s1'], _ul(L['s1_items'])) + _sec(2, L['s2'], f"<p>{L['s2_p']}</p>")
        + _sec(3, L['s3'], f"<p class=\"r-note\">{L['s3_note']}</p>" + _table(L['s3_head'], L['s3_rows']))
        + _sec(4, L['s4'], _table(L['s4_head'], s4_rows)))
    locked = (_sec(5, L['s5'], ''.join(f'<p>{p}</p>' for p in L['s5_p'])) + _sec(6, L['s6'], _ul(L['s6_items']))
        + _sec(7, L['s7'], '<ol class="r-steps">' + ''.join(f'<li>{x}</li>' for x in L['s7_items']) + '</ol>')
        + _sec(8, L['s8'], _table(L['s8_head'], L['s8_rows'])) + _sec(9, L['s9'], _table(L['s9_head'], L['s9_rows']))
        + _sec(10, L['s10'], f"<p>{L['s10_p']}</p>") + _sec(11, L['s11'], _ul(L['s11_items']))
        + _sec(12, L['s12'], _ul(L['s12_items'])) + _sec(13, L['s13'], _ul(L['s13_items']))
        + _sec(14, L['s14'], f"<p>{L['s14_p']}</p>"))
    promise = ''.join(f'<li>{x}</li>' for x in L['promise'])
    return f'''<section class="section"><div class="container report-wrap">
<article class="report reveal" id="report">
 <header class="report-head"><p class="report-kicker">{L['kicker']}</p><h2>{L['title']}</h2><p class="report-meta">{L['meta']}</p><p class="draft-note">{L['synth']}</p></header>
 {open_part}
 <p class="gate-thanks" id="report-thanks">{L['thanks']}</p>
 <div class="report-locked" id="report-locked" aria-hidden="true">{locked}</div>
</article>
<aside class="gate" id="gate">
 <p class="report-kicker">{L['gate_kicker']}</p><h3>{L['gate_title']}</h3><p class="gate-list">{L['gate_list']}</p>
 <ul class="gate-promise">{promise}</ul>
 <form class="form" id="gate-form" novalidate>
  <label>{L['f_name']}<input name="name" required autocomplete="name"></label>
  <label>{L['f_company']}<input name="company" required autocomplete="organization"></label>
  <label>{L['f_email']}<input type="email" name="email" required autocomplete="email"></label>
  <label>{L['f_phone']}<input name="phone" autocomplete="tel"></label>
  <label class="check"><input type="checkbox" name="consent" required><span>{L['f_consent']}</span></label>
  <button class="btn btn-primary" type="submit">{L['f_btn']}</button>
  <p class="contact-note">{L['f_note']}</p>
 </form>
</aside>
</div></section>'''
