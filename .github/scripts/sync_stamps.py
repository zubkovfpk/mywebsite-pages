#!/usr/bin/env python3
"""Keep every site title block (основная надпись) consistent – brand book KOR.BB.01, sheet 11, technique 2.

«Изменение» / «Revision» is the revision of the document itself, not of the brand book:
  * page with a revision table (technique 4) – the top row of that table: its number and date;
  * page without one – first issue: «1.0» and the date the page was first published in this repo.
«Организация» / «Organisation» – the brand name with the MS Word dash.
Page-specific cells (document code, sheet, founder) are left alone.
Run: python3 .github/scripts/sync_stamps.py [--check]
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP = {"brandbook.html", "logo-preview.html"}
ORG = {"Организация": "КОР – Бюро промышленного ИИ", "Organisation": "KOR – Industrial AI Bureau"}
REV_LABELS = ("Изменение", "Revision")
DATE_LABELS = ("Дата", "Date")

table = re.compile(r'<table class="(?:rev-table[^"]*|matrix)"><thead><tr><th[^>]*>(?:Изм\.|Rev\.)</th>.*?</thead>\s*<tbody>\s*<tr><td>([^<]+)</td><td>[^<]*</td><td>([^<]+)</td>', re.S)
cell = re.compile(r'(<span class="stamp-l">([^<]+)</span><span class="stamp-v"[^>]*>)([^<]*)(</span>)')


def first_published(rel):
    out = subprocess.run(["git", "log", "--diff-filter=A", "--follow", "--format=%ad", "--date=format:%d.%m.%Y", "--", rel],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    return out[-1] if out else None


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
    m = table.search(text)
    if m:
        rev, date = m.group(1).strip(), m.group(2).strip()
    else:
        rev, date = "1.0", first_published(rel)
    want = dict(ORG)
    for k in REV_LABELS:
        want[k] = rev
    if date:
        for k in DATE_LABELS:
            want[k] = date
    new = cell.sub(lambda c: c.group(1) + want.get(c.group(2).strip(), c.group(3)) + c.group(4), text)
    if new != text:
        changed.append(f"{rel}  ({rev} · {date})")
        if "--check" not in sys.argv:
            path.write_text(new, encoding="utf-8")

print(f"{len(changed)} page(s) {'out of date' if '--check' in sys.argv else 'updated'}")
for line in changed:
    print("  " + line)
if "--check" in sys.argv and changed:
    sys.exit(1)
