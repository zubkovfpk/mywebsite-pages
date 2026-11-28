"""Check KOR monetary notation in site copy, including markup and metadata."""
from html import unescape
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[2]
bad = re.compile(r"\u20bd|\\u20bd|(?<![^\W\d_])(?:руб|тыс|млн|млрд|трлн)\b(?!\.)", re.I)
errors = []
for file in root.rglob("*"):
    if file.suffix.lower() not in {".html", ".svg", ".js", ".json", ".xml", ".css"}:
        continue
    raw = file.read_bytes()
    encoding = "utf-16" if raw.startswith((b"\xff\xfe", b"\xfe\xff")) else "utf-8-sig"
    for i, line in enumerate(raw.decode(encoding).splitlines(), 1):
        if hit := bad.search(unescape(line)):
            errors.append(f"{file.relative_to(root)}:{i}: {hit.group()!r}")
if errors:
    sys.exit("\n".join(errors))
print("Currency and magnitude notation OK.")
