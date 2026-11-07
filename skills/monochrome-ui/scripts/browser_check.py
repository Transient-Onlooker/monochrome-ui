"""Optional Chromium checks for the bundled demo.

Requires: pip install playwright && python -m playwright install chromium
Run: python scripts/browser_check.py
Override executable with CHROMIUM_PATH if needed.
"""
from pathlib import Path
import os
from playwright.sync_api import sync_playwright

assets = Path(__file__).resolve().parents[1] / "assets"
html = (assets / "demo.html").read_text(encoding="utf-8")
css = (assets / "monochrome.css").read_text(encoding="utf-8")
html = html.replace('<link rel="stylesheet" href="./monochrome.css">', "<style>" + css + "</style>")
with sync_playwright() as p:
    args = {"headless": True}
    if os.getenv("CHROMIUM_PATH"):
        args["executable_path"] = os.environ["CHROMIUM_PATH"]
    browser = p.chromium.launch(**args)
    try:
        for width, height in [(1366, 900), (800, 900), (390, 844), (320, 720)]:
            page = browser.new_page(viewport={"width": width, "height": height})
            try:
                page.set_content(html, wait_until="load")
                overflow = page.evaluate("document.documentElement.scrollWidth")
                assert overflow <= width, f"Horizontal overflow at {width}px: {overflow}px"
                assert page.locator(".mono-card:visible").count() == 3
                page.locator("#query").fill("센서")
                assert page.locator(".mono-card:visible").count() == 1
                page.locator("#reset").click()
                assert page.locator(".mono-card:visible").count() == 3
                page.locator("#category").select_option("dev")
                assert page.locator(".mono-card:visible").count() == 2
                page.locator("#reset").click()
                page.locator("#kindGroup [data-value=project]").click()
                assert page.locator(".mono-card:visible").count() == 1
                page.locator("#reset").click()
                page.locator(".mono-card:visible [data-detail]").first.click()
                assert page.locator("#detail").evaluate("d => d.open")
                page.locator("[data-close=detail]").click()
                assert not page.locator("#detail").evaluate("d => d.open")
                page.locator("#helpOpen").click()
                assert page.locator("#help").evaluate("d => d.open")
                page.keyboard.press("Escape")
                assert not page.locator("#help").evaluate("d => d.open")
                print(f"PASS: {width}x{height}, no overflow; search/filter/reset/dialog")
            finally:
                page.close()
    finally:
        browser.close()
