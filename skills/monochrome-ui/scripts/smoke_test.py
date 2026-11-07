"""Dependency-free checks for the monochrome-ui Agent Skill.

Run: python scripts/smoke_test.py
This does not replace browser or WCAG testing.
"""
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT = Path(__file__).resolve().parents[1]
files = {
    "skill": ROOT / "SKILL.md",
    "reference": ROOT / "references" / "DESIGN-SYSTEM.md",
    "css": ROOT / "assets" / "monochrome.css",
    "html": ROOT / "assets" / "demo.html",
    "browser": ROOT / "scripts" / "browser_check.py",
}
for name, path in files.items():
    assert path.is_file(), f"Missing {name}: {path}"
skill = files["skill"].read_text(encoding="utf-8")
css = files["css"].read_text(encoding="utf-8")
html = files["html"].read_text(encoding="utf-8")
frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
assert frontmatter, "SKILL.md must start with YAML frontmatter"
assert re.search(r"(?m)^name: monochrome-ui$", frontmatter.group(1))
description = re.search(r"(?m)^description: (.+)$", frontmatter.group(1))
assert description and 1 <= len(description.group(1)) <= 1024
for token in (
    "references/DESIGN-SYSTEM.md", "assets/monochrome.css", "assets/demo.html",
    "--mono-ink:#000", ".mono-workspace", ".mono-card", ".mono-filter-panel",
    "@media(max-width:710px)", "@media(max-width:390px)"
):
    assert token in skill + css, f"Missing selector/reference: {token}"
assert css.count("{") == css.count("}"), "Unbalanced CSS braces"
assert '<link rel="stylesheet" href="./monochrome.css">' in html
assert '<body class="mono-page">' in html
assert "aria-pressed" in html and "aria-live" in html and "<dialog" in html
HTMLParser().feed(html)
print("PASS: skill metadata, package references, CSS selectors, and HTML parsing")
print("NOTE: no browser or automatic accessibility validation performed here")
