"""Convert sources/Ruhulla_Sheik_Resume.md to downloads/Ruhulla_Sheik_Resume.pdf."""

from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

# Anchor paths to the repo root (this file lives in scripts/) so the script
# works regardless of the current working directory.
ROOT = Path(__file__).resolve().parent.parent
MD_PATH = ROOT / "sources/Ruhulla_Sheik_Resume.md"
PDF_PATH = ROOT / "downloads/Ruhulla_Sheik_Resume.pdf"

CSS_STYLES = """
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 9.3pt;
    line-height: 1.32;
    color: #1f2937;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 4px;
}

h1 {
    font-size: 20pt;
    font-weight: 700;
    margin: 0 0 2px 0;
    color: #0f172a;
    letter-spacing: -0.2px;
}

/* Role line + contact line directly under the name */
h1 + p {
    font-size: 10pt;
    font-weight: 600;
    color: #1e40af;
    margin: 0 0 3px 0;
}
h1 + p + p {
    font-size: 8.6pt;
    color: #475569;
    margin: 0 0 4px 0;
}

h2 {
    font-size: 10.3pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    color: #1e40af;
    border-bottom: 1.5px solid #bfdbfe;
    padding-bottom: 2px;
    margin: 8px 0 4px 0;
}

h3 {
    font-size: 10.3pt;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 1px 0;
}

h4 {
    font-size: 9.6pt;
    font-weight: 600;
    color: #334155;
    margin: 6px 0 1px 0;
}

p { margin: 2px 0 3px 0; }

ul {
    margin: 1px 0 4px 0;
    padding-left: 16px;
}

li { margin-bottom: 1.5px; }

strong { color: #0f172a; font-weight: 700; }

code {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 8.3pt;
    background: #eff6ff;
    border: 0.5px solid #bfdbfe;
    border-radius: 3px;
    padding: 0.5px 5px;
    color: #1e40af;
    white-space: nowrap;
}

em { color: #475569; font-style: italic; }

a { color: #1e40af; text-decoration: none; }
"""


def build_pdf() -> None:
    md_text = MD_PATH.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Ruhulla Sheik — Resume</title>
  <style>{CSS_STYLES}</style>
</head>
<body>{html_body}</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="domcontentloaded")
        page.pdf(
            path=str(PDF_PATH),
            format="A4",
            margin={"top": "9mm", "bottom": "9mm", "left": "14mm", "right": "14mm"},
            print_background=True,
        )
        browser.close()

    print(f"Generated: {PDF_PATH}")


if __name__ == "__main__":
    build_pdf()
