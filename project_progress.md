# Project Progress

## Done

- Static site v3 live structurally: 20 RU + 20 EN generated pages; RU/EN generators, sitemap, robots, auto language choice.
- Cases finalized: ALL 9 — vizard, shipping, morspas, geodesy, developer, egip, agro, shelf, medtech (esg-nsr → shelf, edtech → medtech replacements done).
- Cases page: uniform 3×3 grid, one-line `card_tags`, intl badges (globe on edtech, ribbon on shipping — both kept for audience test), award medal badge on egip, hover tooltips.
- Case content rules enforced: 4 facts (first = Функции), no duplicate metrics per page, client-voice tasks, ×N multiplier notation, «руб.» money units, direction-explicit effects.
- Method page aligned with ARCHITECTURE (8 readiness factors, 0–4 scale + radar, recommendation vs deployment status).
- Site workflow documented: `.devin/skills/site-workflow/SKILL.md`, `AGENTS.md`.
- Multiplier notation ×N normalized; «Почему»→«Обоснование»; AI-label 8px on cards.

## In progress

- **v4 branch**: single-page structure live (pains→experience→formats→bureau→CTA); awaiting user review of pains alt-formulations (`pain-alt` on 2 cards) and logo variants in `logo-preview.html` (9 options, delete after choice).
- **Bureau naming**: candidates to compare — **Контекст/Context, ARC, GRID, Ratio, Quaero** (Alice's AIM/FAB/MAP dropped; «-AI» endings parked). Next: pick → domain + Роспатент → BRAND/ROLE cascade.
- **Search demand research**: RU + international DONE. RU: `research_wordstat_ru.md` (75 phrases, Wordstat API). Intl: `research_keywords_intl.md` (Google Keyword Planner, 7 EN countries + 5 native-language runs; raw CSVs in `D:\WORK\AIprojects\Keywords_ideas\`). Next: merge into semantic map for site copy/naming.
- Domain choice/registration (reg.ru); `SITE` placeholder still `example.ru`.
- GEO-monitoring (AI-chat answers visibility) — to set up after launch.

## Backlog

- Deploy to reg.ru (shared → VPS), real domain, Яндекс Метрика, sitemap/robots already generated.
- Concept A «Вердикт» diagnostic widget (fractionalcaio backend: FastAPI+Postgres+Redis).
- Forms v1.1 (consent checkbox → `/inquiries` endpoint) + privacy policy page.
- Self-hosted woff2 fonts for production.
- Possible rename cascade if new bureau name chosen: BRAND/ROLE constants, wordmark, titles, og-tags, Council 7+1 relationship.
