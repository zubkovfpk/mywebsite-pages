# Project Context — mywebsite

Static bilingual (RU/EN) site for Sergey Zubkov — Fractional CAIO / evidence-based AI bureau. Concept B «Экспертный кабинет» → later A «Вердикт» (widget) → C «Прозрачная фабрика». Hosting target: reg.ru. `SITE` placeholder = `https://example.ru` until the real domain is chosen/registered.

## Brand (current, naming under review)

- `BRAND` = «Бюро Зубкова» / "Zubkov Bureau" — wordmark in header.
- `ROLE` = «Бюро обоснованного ИИ» / "Evidence-based AI bureau" — descriptor.
- `PLAT` = Council 7+1 — diagnostics platform name, untranslated.
- Naming candidates under review: **Контекст/Context, ARC, GRID, Ratio, Quaero**. Final structure: name + category descriptor («ИИ-бюро» / «AI Bureau»). Domain not chosen — needs reg.ru + trademark check.

## Architecture

- All HTML generated — never hand-edit `.html`. RU: `_build/build_v3.py` (runs `build_en.py` via runpy → EN pages in `en/`). Rebuild: `python _build/build_v3.py`. Preview: `python -m http.server 8123`.
- Case data lives in `CASES` dicts in both builders; shared helpers: `photo()`, `case_card()`, `chip()`, `nb()`, `funcs()`.
- Shared CSS `assets/css/style.css`; JS `assets/js/main.js`. Design: paper `#FAF7F2`, ink `#1C1B18`, accent `#0F5A46`, zone amber for Hybrid; Georgia/system/mono, no external fonts; respect `prefers-reduced-motion`.
- `foto/` = source photos, gitignored. Published images: `assets/img/`.

## Conventions (user-approved)

- Language: RU uses Russian terms or Russian + English gloss in parentheses; EN plain English. Brands/abbr (LLM, ESG, Council 7+1, on-prem) unchanged.
- Case facts: exactly 4; first always «Функции»/`funcs()` (max 2 functions, cover all 5 keys across cases); no «Отрасль» (industry is in tags). `card_tags` = short one-line label for cards; `nda`, `intl`, `award`, `draft` flags supported.
- A metric appears **once** per case page (title/facts/task/result must not repeat figures). Effects state direction explicitly («меньше на 40%», «ниже ~×1,7»). Multiplier notation: prefix ×N («×3», «~×1,7»).
- `task` = client's voice/request; `result` = client outcomes. Avoid «нужно» in body copy («требуется/необходимо»); «ИИ не нужен» verdict phrasing is allowed.
- RU money: «тыс./млн./млрд. руб.», no ₽; non-breaking number+unit.
- Verdict chips: ИИ/Гибрид/Без ИИ/Отложить — AI/Hybrid/No AI/Defer. Verdict column header «Обоснование»/"Rationale".
- Case review: user says «Чисто» → set `draft=False` in both builders, rebuild, commit .py + regenerated HTML together.
- Card markers: international = globe badge (accent-green) or ribbon — both kept pending audience test; award = amber medal badge; all upper-left, `data-tip` tooltips (no JS).
- Red lines: formal entity names (ИЭПИ, ВИЗАРД) not published; client names only whitelisted (Морспасслужба, Россельхознадзор, ЕГИП/Москва); Роскадастр → «геодезия/кадастр», Capital Group → «девелопер топ-3».

## Environment

- Windows + PowerShell: no `&&`, no bash heredocs; `;` to chain.
- Git: branch `v3`, remote github.com/zubkovfpk/mywebsite. No global identity — commit via `git -c user.name="Sergey A Zubkov" -c user.email="zubkovfpk@gmail.com" commit`.
- `gh` CLI authenticated (zubkovfpk) — prefer over repo-scoped GitHub MCP.

## Canonical docs

Update after each session: `conversation_history.md` (newest top, UTC), `project_context.md`, `project_progress.md`.
