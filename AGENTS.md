# Project Rules — mywebsite

Static site «Сергей Зубков — Fractional CAIO» (RU + EN). All HTML is generated —
**do not hand-edit `.html` files**; edit the generators in `_build/` and rebuild
with `python _build/build_v3.py`. Full workflow: use the `site-workflow` skill.

- Environment: Windows + PowerShell (no `&&`, no `ls -la`; use `;` / native cmdlets).
- Preview: `python -m http.server 8123`.
- Keep RU and EN versions in sync; follow `CONTENT_PLAN.md` for content and red lines.
- Language rule: in the RU version write terms in Russian, or Russian gloss with the English term in parentheses — e.g. «Директор по ИИ (Chief AI Officer)», «безопасная среда исполнения (safety runtime)». In the EN version use English terms directly. Product/brand names (VIZARD, Council 7+1, LLM, on-prem, SaaS) may stay as-is.
- Never commit contents of `foto/` (source photos).
- Case page rules: a metric/number must appear only once per case page — never repeat the same figure across title, facts, task and result. Each case has exactly 4 facts: first is always «Функции»/«Functions» via `funcs()`, then three case-specific items.
