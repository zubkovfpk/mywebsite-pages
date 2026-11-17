# Conversation History

Newest at top. All timestamps UTC.

## 2026-11-17 ~19:30 UTC — v4 structure + Wordstat research

- **Branch `v4` created** — site restructured to a single-page model (user decision: hide methodology internals, merge industries+cases, shorten to 3–4 blocks).
- v4 index: pain-led hero («Вам продают внедрение ИИ. Мы — ответ, нужен ли он») → Задачи (6 client-voice pains) → Опыт (6 industries merged with case-metric links) → Форматы ladder (all paid; «как работаем» merged in) → Бюро → CTA «Начнём с разговора».
- Removed pages: method, council, industries, formats, insights, bureau (14 pages total now). NAV = Задачи/Опыт/Кейсы/Форматы/Контакт. Numbers strip removed from index (outside users couldn't judge «много или мало»). Numbers remain in cases only.
- Two pains show alternative formulations (`pain-alt` muted line) pending user's pick.
- **`logo-preview.html`** — temp page with 9 logo variants (Quaero/Ratio/Eligo ± «Бюро», 3 radar-based marks), left-aligned wordmark. Awaiting user choice; delete after.
- **Naming brainstorms added:** «-AI» endings (ReshAI/DumAI etc. — parked), «Контекст» (strong candidate), Alice's ARC/GRID/AIM (ARC and GRID kept as directions). Shortlist to compare: **Контекст/Context, ARC, GRID, Ratio, Quaero**.
- **Wordstat research (real data)** via Yandex Search API v2 `topRequests` — key in `D:\WORK\AIprojects\wordstat.txt` (service account `bureau`, folder `b1gegkqs4sj99ic3ohm8`), collectors `wordstat_*.py`, raw JSON + digest. Full report: **`research_wordstat_ru.md`**.
- Key findings: «ИИ не работает» (9,3k) and «ИИ диагностика» (5k) are consumer/medical traps; client-fit clusters = ИИ-агенты на заказ (~2,6k), корпоративный контур (~3k), теневой-ИИ cluster (~1,4k), аудит процессов (~740), директор по ИИ (~1,1k — while «фракционный директор» = 7). Closed-contour niche ≈300, almost no competition. «Внедрение» is dead territory for differentiation.
- No public stats exist for queries inside AI chats (Alice etc.) — planned GEO-monitoring instead (monthly manual check of AI answers to commercial queries).

## 2026-11-13 ~16:00 UTC — All 9 cases finalized

- **medtech finalized** (draft=False) — case review complete for all 9 cases.
- medtech final form: title «ИИ-микроскоп: согласие пациентов растёт на 30%», chip «Новая ниша · экспортная стратегия», facts Функции/Архитектура/Метрика/Эффект («выручка +$30 тыс./год на врача · КП быстрее ×7»), dental.jpg image.
- New mechanism: `card_short` field — shorter lead text for cards while page keeps full `short` (like `card_tags`).
- New field `chip` — tag-row chip styled like award chip («Новая ниша · экспортная стратегия»).
- **Wordmark updated for Quaero variant**: «?» + four verdict bars (green/amber/red/**grey** added — 4th verdict now represented).
- Domain check done: bare quaero/ratio/eligo taken in .ru/.com/.ai; `buroX` free in all three zones (quaero.com held since 1998, ratio.com 1994, eligo.com 1998). Recommendation: `buroX.ru + buroX.ai`.
- Naming shortlist remains: **Quaero / Ratio / Eligo** — awaiting user's final pick.

## 2026-11-13 ~15:00 UTC — Naming shortlist + shelf/medtech cases

- **Naming: user shortlist = Quaero, Ratio, Eligo.** Probatio dropped («доказываем» inverts meaning — we prove groundedness, not AI necessity; law-firm vibe). Delibero, Consilium (conflict w/ Council 7+1), Examen (school connotation) rejected by user. Digit names still out.
  - Quaero: leader contender; RU form «Квэро» fixes pronunciation; pair w/ descriptor «обоснованный ИИ».
  - Ratio: «основание+расчёт+разум» in one root; risk — crowded in fintech, slightly cold.
  - Eligo: «выбор вердикта»; weaker semantic load.
  - Pending: domain + Роспатент availability check; final pick; then BRAND/ROLE cascade in builders.
- **Cases:** esg-nsr replaced by **shelf** (offshore drilling assessment, ГШП заключение) — finalized (draft=False). Direction «Буровое и насосное оборудование · надёжность» — hook for Profitreid/Симфония_Про prospects. edtech replaced by **medtech** (FreeVision 3D AI program) — under review; **image is temporary edtech.jpg, needs real photo/generation**.
- Learned rule: assistant must verify layout balance after content changes (measure column text volume vs sibling cases) instead of pushing that job to the user.

## 2026-11-13 12:30 UTC — Bureau naming analysis + case reviews

- Reviewed/finalized cases: agro marked clean (draft=False). 7 of 9 cases done; remaining drafts: esg-nsr, edtech.
- **Bureau naming — interim conclusions (user will return to this):**
  - Current: `BRAND` = «Бюро Зубкова» / "Zubkov Bureau", `ROLE` = «Бюро обоснованного ИИ» / "Evidence-based AI bureau", `PLAT` = Council 7+1.
  - User candidates analyzed: **Quaero**, **Бюро 4D/4R/4V**, **Бюро 8F**.
  - Digit-based names (4D/4R/4V, 8F) rejected: method factors will grow (safety questions already asked → sub-agents/expanded factors); a number in the name is guaranteed to age; 4D also collides with BIM/construction meaning, 4V reads as volts, 4R as sustainability term.
  - New context: forum webinar «Доказательный ИИ: от пилота к измеримому эффекту» — market converging on «доказательный ИИ» category = validation of the bureau's «обоснованный ИИ» positioning, but the category word will get crowded; name should sit next to the category, not duplicate it.
  - Interim ranking: **Quaero** leads (semantics «ищу/спрашиваю» fits diagnostics-first; survives method changes; risks: occupied by Quaero Capital/old French search project, RU pronunciation unclear) — also candidate as method/platform name. **Probatio** added by Devin («доказательство/испытание»; risk: «пробация» = probation period connotation in RU). Possible pair: Quaero = platform/method, Probatio = signed report.
  - Recommended structure: name-mark + category descriptor («Бюро X — доказательный/обоснованный ИИ»). «Бюро Зубкова» remains fallback.
  - Open: domain/Trademark availability check (Роспатент) before publishing; real domain still unchosen (`SITE=https://example.ru` placeholder).
- Normalized multiplier notation to ×N across case facts (×3, ~×1,7, ×6,3) — commit fc4db89.

## 2026-11-10..12 — earlier sessions

See prior summary history; highlights: cases vizard/shipping/morspas/geodesy/developer/egip finalized; 3×3 cases grid; intl (globe/ribbon) + award (amber medal) card badges with hover tooltips; rules established — 4 facts per case (first = Функции), no duplicate metrics per case page, RU money in «руб.» units, task = client voice.
