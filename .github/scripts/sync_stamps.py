#!/usr/bin/env python3
"""Keep every site title block (основная надпись) in line with the brand book KOR.BB.01.

Source of truth: brandbook.html – revision («Изм.») and date («Дата») from its cover stamp.
Updated in every page (RU and EN): revision, date and organisation name.
Page-specific cells (document code, sheet) are left alone.
Run: python3 .github/scripts/sync_stamps.py [--check]
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP = {"brandbook.html", "logo-preview.html"}
ORG = {"Организация": "КОР – Бюро промышленного ИИ", "Organisation": "KOR – Industrial AI Bureau"}

bb = (ROOT / "brandbook.html").read_text(encoding="utf-8")
rev = re.search(r"<b>Изм\.</b>\s*([\d.]+)\s*<", bb).group(1)
date = re.search(r"<b>Дата</b>\s*(\d{2}\.\d{2}\.\d{4})\s*<", bb).group(1)
want = {"Изменение": f"ББ {rev}", "Revision": f"BB {rev}", "Дата": date, "Date": date, **ORG}

cell = re.compile(r'(<span class="stamp-l">([^<]+)</span><span class="stamp-v"[^>]*>)([^<]*)(</span>)')
changed = []
for path in sorted(ROOT.rglob("*.html")):
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP or rel.startswith(".git"):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    if 'class="stamp"' not in text:
        continue
    new = cell.sub(lambda m: m.group(1) + want.get(m.group(2).strip(), m.group(3)) + m.group(4), text)
    if new != text:
        changed.append(rel)
        if "--check" not in sys.argv:
            path.write_text(new, encoding="utf-8")

print(f"brand book rev {rev}, {date}: {len(changed)} page(s) {'out of date' if '--check' in sys.argv else 'updated'}")
for rel in changed:
    print("  " + rel)
if "--check" in sys.argv and changed:
    sys.exit(1)
