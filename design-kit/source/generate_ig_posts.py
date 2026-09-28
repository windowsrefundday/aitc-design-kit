"""Generate 4:5 (1080x1350) Instagram carousel board-announcement posts for AITC.

Layout proportions are traced from the user's reference card:
  - rounded lighter-green panel inset inside the green gradient canvas
  - AITC logo top-left, name + role right-aligned beside it
  - very large name, role at ~0.47x the name size
  - portrait card left-aligned under the header with a deliberate right gap
  - no footer

Rendered with headless Chrome and screenshotted at exactly 1080x1350.
"""

import base64
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "new asset"
HTML_DIR = BASE_DIR / "temp_html_posts"
OUTPUT_DIR = BASE_DIR / "instagram_board_posts"
HTML_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# `year` is optional; set e.g. "junior year" to print a third line under the role.
officers = [
    {
        "filename": "00_cover.png",
        "kind": "cover",
    },
    {
        "filename": "01_joel.png",
        "fact": "i spend my free time clicking links on wikipedia pages until i can't go any further.",
        "name": "Joel Manuel",
        "role": "president/founder of aitc",
        "image_file": BASE_DIR / "joel.jpg",
        "object_position": "50% 30%",
        "year": None,
    },
    {
        "filename": "02_vihaan.png",
        "fact": "i check ken carson's instagram story every 10 minutes on fridays to see if an album is dropping.",
        "name": "Vihaan Patel",
        "role": "vice president of aitc",
        "image_file": BASE_DIR / "vihaan.jpg",
        "object_position": "50% 38%",
        "year": None,
    },
    {
        "filename": "03_yash.png",
        "fact": "one of my favorite hobbies is 3d printing and making things from scratch.",
        "name": "Yash Bafna",
        "role": "competitions director of aitc",
        "image_file": BASE_DIR / "yash.jpg",
        "object_position": "50% 42%",
        "zoom": (1.55, "50% 56%"),
        "year": None,
    },
    {
        "filename": "04_aarit.png",
        "fact": "my favorite video game is kingdom hearts.",
        "name": "Aarit Srivastava",
        "role": "technical director of aitc",
        "image_file": ASSET_DIR / "IMG_0499.png",
        "object_position": "50% 100%",
        "zoom": (1.42, "50% 62%"),
        "year": None,
    },
    {
        "filename": "05_siddarth.png",
        "fact": "i love spending time with my family and friends.",
        "name": "Siddarth Yetukuri",
        "role": "outreach director of aitc",
        "image_file": BASE_DIR / "sid.jpg",
        "object_position": "50% 38%",
        "year": None,
    },
    {
        "filename": "06_nishaanth.png",
        "fact": "i'm double-jointed.",
        "name": "Nishaanth Jay",
        "role": "student engagement director of aitc",
        "image_file": BASE_DIR / "nishanth.jpg",
        "object_position": "50% 6%",
        "zoom": (1.24, "50% 28%"),
        "year": None,
    },
    {
        "filename": "07_outro.png",
        "kind": "outro",
        "outro": "so much more to expect in the coming weeks, stay tuned!!",
    },
]

def img_to_b64(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    mime = "image/jpeg" if path.suffix.lower() in (".jpg", ".jpeg") else "image/png"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


LOGO_B64 = img_to_b64(BASE_DIR / "logo.png")

# Shared forest-green glow behind every cream text element (reference card look).
TEXT_SHADOW = "drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81))"
CREAM_FILL = """
    background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
"""

CSS = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box;
    -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }}

html, body {{ width: 1080px; height: 1350px; }}

:root {{ --logo: url("{LOGO_B64}"); }}

body {{
    position: relative;
    overflow: hidden;
    font-family: "SF Pro Display", -apple-system, BlinkMacSystemFont,
                 "Inter Tight", "Helvetica Neue", sans-serif;
    background: linear-gradient(140deg,
        #6f9d6f 0%,
        #558f61 26%,
        #35744a 58%,
        #1d5730 84%,
        #0f3a20 100%);
}}

/* ---------- the lighter-green rounded panel ---------- */
.panel {{
    position: absolute;
    inset: 22px;
    border-radius: 56px;
    background: rgba(255, 249, 230, 0.135);
    border: 1px solid rgba(255, 249, 230, 0.14);
    padding: 46px 42px 42px;
    display: flex;
    flex-direction: column;
}}

/* ---------- header: logo left, name block right ---------- */
.header {{
    display: flex;
    align-items: flex-start;
    gap: 28px;
    flex: 0 0 auto;
}}

.aitc-logo {{
    width: 158px;
    height: 158px;
    flex: 0 0 auto;
    margin-top: 4px;
    background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
    -webkit-mask: var(--logo) center / contain no-repeat;
    mask: var(--logo) center / contain no-repeat;
    filter: {TEXT_SHADOW};
}}

.name-col {{
    flex: 1 1 auto;
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    text-align: right;
}}

.person-name {{
    font-size: 100px;
    font-weight: 700;
    line-height: 1.0;
    letter-spacing: -0.035em;
    white-space: nowrap;
    {CREAM_FILL}
    filter: {TEXT_SHADOW};
}}

.person-role {{
    margin-top: 12px;
    font-size: 56px;
    font-weight: 700;
    line-height: 1.06;
    white-space: nowrap;
    letter-spacing: -0.035em;
    text-transform: lowercase;
    {CREAM_FILL}
    filter: {TEXT_SHADOW};
}}

.person-year {{
    margin-top: 14px;
    font-size: 36px;
    font-weight: 700;
    letter-spacing: -0.03em;
    text-transform: lowercase;
    {CREAM_FILL}
    filter: {TEXT_SHADOW};
}}

/* ---------- portrait: left-aligned, deliberate right gap ---------- */
.portrait-wrap {{
    flex: 1 1 auto;
    min-height: 0;
    display: flex;
    align-items: stretch;
    margin-top: 34px;
}}

.portrait-frame {{
    flex: 0 0 640px;
    height: 100%;
    min-height: 0;
    border-radius: 40px;
    overflow: hidden;
    border: 2px solid rgba(255, 243, 203, 0.35);
    box-shadow: 0 32px 80px rgba(8, 28, 16, 0.75);
    background: #0c2719;
}}

.portrait-frame img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    filter: contrast(1.04) saturate(1.03);
}}

/* ---------- fun fact: narrow right-aligned column beside the photo ---------- */
.fact-col {{
    flex: 1 1 auto;
    min-width: 0;
    padding-left: 36px;
    padding-top: 78px;
    text-align: right;
}}

.fact-text {{
    font-size: 60px;
    font-weight: 700;
    line-height: 1.08;
    letter-spacing: -0.035em;
    text-transform: lowercase;
    overflow-wrap: break-word;
    {CREAM_FILL}
    filter: {TEXT_SHADOW};
}}

/* ---------- cover: inverted, light ground / dark type ---------- */
body.cover {{
    background:
        radial-gradient(circle at 102% 103%,
            rgba(8, 28, 16, 1) 0%,
            rgba(12, 39, 25, 0.94) 16%,
            rgba(33, 100, 52, 0.62) 34%,
            rgba(255, 243, 203, 0) 72%),
        linear-gradient(135deg,
            #fff3cb 0%,
            #fff3cb 50%,
            #dbe1b3 76%,
            #174b2a 100%);
}}

body.cover .panel {{
    background: rgba(12, 39, 25, 0.045);
    border-color: rgba(12, 39, 25, 0.12);
}}

.cover-top {{
    flex: 0 0 auto;
    font-size: 118px;
    font-weight: 700;
    line-height: 0.92;
    letter-spacing: -0.045em;
    text-transform: lowercase;
    color: #0c2719;
    filter: drop-shadow(7px 13px 28px rgba(12, 39, 25, 0.22));
}}

.cover-logo {{
    flex: 1 1 auto;
    min-height: 0;
    margin: 40px 0 32px;
    background: linear-gradient(160deg, #216434 0%, #174b2a 55%, #0c2719 100%);
    -webkit-mask: var(--logo) center / contain no-repeat;
    mask: var(--logo) center / contain no-repeat;
    filter: drop-shadow(12px 20px 38px rgba(12, 39, 25, 0.34));
}}

/* sits over the deep-forest corner of the gradient, so it flips to cream */
.cover-kicker {{
    flex: 0 0 auto;
    text-align: right;
    font-size: 96px;
    font-weight: 700;
    line-height: 1.0;
    letter-spacing: -0.04em;
    text-transform: lowercase;
    {CREAM_FILL}
    filter: {TEXT_SHADOW};
}}

/* ---------- outro: dark forest / tan type ---------- */
body.outro {{
    background:
        radial-gradient(120% 78% at 14% 6%,
            rgba(45, 110, 66, 0.58) 0%,
            rgba(12, 39, 25, 0) 62%),
        linear-gradient(140deg, #1d5730 0%, #123f22 44%, #0c2719 100%);
}}

body.outro .panel {{
    background: rgba(255, 249, 230, 0.06);
    border-color: rgba(255, 249, 230, 0.12);
}}

.outro-logo {{
    flex: 0 0 auto;
    width: 158px;
    height: 158px;
    background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
    -webkit-mask: var(--logo) center / contain no-repeat;
    mask: var(--logo) center / contain no-repeat;
    filter: {TEXT_SHADOW};
}}

.outro-body {{
    flex: 1 1 auto;
    min-height: 0;
    display: flex;
    align-items: center;
}}

.outro-text {{
    width: 100%;
    text-align: right;
    font-size: 170px;
    font-weight: 700;
    line-height: 0.98;
    letter-spacing: -0.04em;
    text-transform: lowercase;
    overflow-wrap: break-word;
    {CREAM_FILL}
    filter: {TEXT_SHADOW};
}}
"""

# Shrink the name until it fits one line, and the role until it fits two.
AUTOFIT_JS = """
function fitWidth(el, start, min) {
    if (!el) return start;
    for (var s = start; s >= min; s -= 1) {
        el.style.fontSize = s + 'px';
        if (el.scrollWidth <= el.clientWidth + 1) return s;
    }
    return min;
}
var nameSize = fitWidth(document.querySelector('.person-name'), 100, 78);
var role = document.querySelector('.person-role');
if (role) fitWidth(role, Math.round(nameSize * 0.56), 38);

// fun fact: grow as large as the column allows, capped well under the name
var fc = document.querySelector('.fact-col');
var ft = document.querySelector('.fact-text');
if (fc && ft) {
    var avail = fc.clientHeight - parseFloat(getComputedStyle(fc).paddingTop);
    for (var f = 60; f >= 28; f -= 1) {
        ft.style.fontSize = f + 'px';
        if (ft.scrollHeight <= avail && ft.scrollWidth <= ft.clientWidth + 1) break;
    }
}
var ot = document.querySelector('.outro-text');
var ob = document.querySelector('.outro-body');
if (ot && ob) {
    for (var o = 170; o >= 60; o -= 2) {
        ot.style.fontSize = o + 'px';
        if (ot.scrollHeight <= ob.clientHeight) break;
    }
}
"""


def header_html(name: str, role: str, year: str | None) -> str:
    year_html = f'<div class="person-year">{year}</div>' if year else ""
    return f"""
    <header class="header">
        <div class="aitc-logo" role="img" aria-label="AITC"></div>
        <div class="name-col">
            <h1 class="person-name">{name}</h1>
            <p class="person-role">{role}</p>
            {year_html}
        </div>
    </header>"""


def build_html(item: dict) -> str:
    kind = item.get("kind", "officer")

    if kind == "cover":
        title, body_class = "The Board", "cover"
        inner = """
        <div class="cover-top">board<br/>announcement!!</div>
        <div class="cover-logo" role="img" aria-label="AITC"></div>
        <div class="cover-kicker">meet the team</div>"""

    elif kind == "outro":
        title, body_class = "Stay Tuned", "outro"
        inner = f"""
        <div class="outro-logo" role="img" aria-label="AITC"></div>
        <div class="outro-body">
            <p class="outro-text">{item['outro']}</p>
        </div>"""

    else:
        title, body_class = item["name"], ""
        zoom = item.get("zoom")
        zoom_css = (
            f"transform: scale({zoom[0]}); transform-origin: {zoom[1]};" if zoom else ""
        )
        inner = header_html(item["name"], item["role"], item.get("year")) + f"""
        <div class="portrait-wrap">
            <div class="portrait-frame">
                <img src="{img_to_b64(item['image_file'])}" alt="{item['name']}"
                     style="object-position: {item['object_position']}; {zoom_css}" />
            </div>
            <div class="fact-col">
                <p class="fact-text">fun fact: {item['fact']}</p>
            </div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} &middot; AITC 4:5</title>
<style>{CSS}</style>
</head>
<body class="{body_class}">
    <div class="panel">
{inner}
    </div>
<script>{AUTOFIT_JS}</script>
</body>
</html>
"""


for item in officers:
    html_file = HTML_DIR / item["filename"].replace(".png", ".html")
    html_file.write_text(build_html(item), encoding="utf-8")

    out_png = OUTPUT_DIR / item["filename"]
    print(f"rendering {item['filename']} @ 1080x1350 ...")
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--screenshot={out_png}",
            "--window-size=1080,1350",
            "--virtual-time-budget=3000",
            f"file://{html_file}",
        ],
        check=True,
        capture_output=True,
    )

print("done -> instagram_board_posts/")
