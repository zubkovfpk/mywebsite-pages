# Project Rules — mywebsite

Static site «Сергей Зубков — Fractional CAIO» (RU + EN). All HTML is generated —
**do not hand-edit `.html` files**; edit the generators in `_build/` and rebuild
with `python _build/build_v3.py`. Full workflow: use the `site-workflow` skill.

- Environment: Windows + PowerShell (no `&&`, no `ls -la`; use `;` / native cmdlets).
- Preview: `python -m http.server 8123`.
- Keep RU and EN versions in sync; follow `CONTENT_PLAN.md` for content and red lines.
- Never commit contents of `foto/` (source photos).
